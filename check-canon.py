#!/usr/bin/env python3
"""Check an episode's generation prompts and manifest against the series canon.

The canon document is owned by a person and no agent can write to it — Switch
enforces that, not this script. What this script does is the other half: it
tells you whether the episode the agents produced actually honours what the
canon says, before you publish it rather than after someone comments.

Two checks, both mechanical:

  prompts   a canon entry's `value` must appear in the episode's shot prompts
            (when `required`), and none of its `forbid` wordings may appear
  manifest  an entry with `scope: manifest` is checked against the generation
            parameters the designer recorded, not the prompt text

Standard library only, by design: a checker with dependencies is a checker that
stops running. Exits non-zero when anything drifted, so it works as a CI step
over a directory of episodes.

    python3 check-canon.py examples/ep-07 --canon examples/series-canon.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CANON_FENCE = re.compile(r"```canon\s*\n(.*?)```", re.DOTALL)
CANON_OPENER = re.compile(r"^\s*(?:`{3,}|~{3,})\s*canon\b", re.MULTILINE)
# Any whitespace except a blank line: a phrase may wrap, not span paragraphs.
GAP = r"(?:[^\S\n]*\n[^\S\n]*|[^\S\n]+)"
ENTRY_START = re.compile(r"^\s*-\s+attr:\s*(?P<attr>\S+)\s*$")
FIELD = re.compile(r"^\s+(?P<key>[a-z_]+):\s*(?P<value>.*?)\s*$")


class CanonError(Exception):
    """The canon or the episode is not usable. Say so and stop."""


def unquote(raw: str) -> str:
    """Drop one pair of matching quotes, so `"long hair"` means long hair."""
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1].strip()
    return raw


def parse_canon(text: str) -> list[dict]:
    """Pull every ```canon block out of the document, in order."""
    entries: list[dict] = []
    blocks = CANON_FENCE.findall(text)
    if len(CANON_OPENER.findall(text)) != len(blocks):
        raise CanonError(
            "a canon block could not be read. Each one must open with exactly "
            "```canon on its own line and close with ```."
        )
    for block in blocks:
        current: dict | None = None
        for line in block.splitlines():
            if not line.strip() or line.strip().startswith("#"):
                continue
            start = ENTRY_START.match(line)
            if start:
                current = {"attr": start.group("attr"), "forbid": [], "required": False,
                           "scope": "prompts"}
                entries.append(current)
                continue
            field = FIELD.match(line)
            if not field:
                raise CanonError(f"cannot read this canon line: {line.strip()!r}")
            if current is None:
                raise CanonError(f"field before any '- attr:' entry: {line.strip()!r}")
            key, raw = field.group("key"), field.group("value")
            if key not in {"value", "scope", "forbid", "required"}:
                raise CanonError(f"{current['attr']}: unknown field {key!r}")
            if key == "forbid":
                inner = raw.strip()
                if not (inner.startswith("[") and inner.endswith("]")):
                    raise CanonError(
                        f"{current['attr']}: forbid must be a one-line list "
                        f"like [a, b, c], got {raw!r}"
                    )
                current["forbid"] = [unquote(w) for w in inner[1:-1].split(",") if unquote(w)]
            elif key == "required":
                answer = raw.strip().lower()
                if answer not in {"true", "yes", "false", "no"}:
                    raise CanonError(
                        f"{current['attr']}: required must be true or false, got {raw!r}"
                    )
                current["required"] = answer in {"true", "yes"}
            else:
                current[key] = unquote(raw)
    for entry in entries:
        if not entry.get("value"):
            raise CanonError(f"{entry['attr']}: no value")
        if entry["scope"] not in {"prompts", "manifest"}:
            raise CanonError(
                f"{entry['attr']}: scope must be 'prompts' or 'manifest', "
                f"got {entry['scope']!r}"
            )
    return entries


def _pattern(needle: str) -> re.Pattern[str]:
    """Whole-word, case-insensitive, and indifferent to how the text wraps.

    Two things this has to survive. Without word boundaries, a canon entry
    forbidding "car" fires on the word "carries". And prose wraps: a prompt
    saying "flat, no lens flare" may carry a newline and two spaces of indent
    between "no" and "lens", so every run of whitespace in the needle has to
    match whitespace in the text, short of a blank line.

    And a word boundary only exists next to a word character, so ``\\b`` goes
    on each end only when that end is one. A canon value of "(interior)" or
    ".*" anchored with ``\\b`` on both sides matches nothing at all, which
    reads as a missing value — the worst kind of wrong answer, because it is a
    failure report on an episode that was never actually checked."""
    tokens = [re.escape(t) for t in needle.split()]
    if not tokens:
        raise CanonError("a canon value cannot be empty")
    body = GAP.join(tokens)
    lead = r"\b" if _wordish(needle[0]) else ""
    tail = r"\b" if _wordish(needle[-1]) else ""
    return re.compile(lead + body + tail, re.IGNORECASE)


def _wordish(char: str) -> bool:
    return char.isalnum() or char == "_"


def unwrap(text: str) -> str:
    """Blank out leading blockquote and list markers, line by line.

    Shot prompts are written as markdown blockquotes, so a canon phrase that
    wraps reads "flat, no\\n> lens flare" — and a ">" is not whitespace, so a
    whitespace-tolerant pattern still misses it. The markers are replaced with
    spaces rather than removed, which keeps every offset and line number
    exactly where it was."""
    return re.sub(
        r"^([ \t]*)([>|*+-]+[ \t]*)",
        lambda m: m.group(1) + " " * len(m.group(2)),
        text,
        flags=re.MULTILINE,
    )


def locate(needle: str, text: str) -> list[int]:
    """1-indexed line numbers where needle appears as a whole word.

    Matched against the whole text rather than line by line, so a phrase that
    wraps is still found; the line reported is where the match starts."""
    pattern = _pattern(needle)
    return [text.count("\n", 0, m.start()) + 1 for m in pattern.finditer(text)]


def mask(value: str, text: str) -> str:
    """Blank out every occurrence of the canon value, keeping line structure.

    A forbidden wording is often a substring of the canon value it protects:
    canon says "flat, no lens flare" and forbids "lens flare". Scanning the
    raw text flags the compliant prompt. The canon value is permitted text by
    definition, so it is removed before the forbidden wordings are looked for,
    and replaced with spaces so reported line numbers still point somewhere
    real."""
    def blank(match: re.Match[str]) -> str:
        return "".join("\n" if c == "\n" else " " for c in match.group(0))

    return _pattern(value).sub(blank, text)


def check(entries: list[dict], prompts: str, manifest: str) -> list[tuple[str, str, str]]:
    """Return one (status, attr, detail) row per canon entry."""
    rows: list[tuple[str, str, str]] = []
    for entry in entries:
        attr, value = entry["attr"], entry["value"]
        target, label = (manifest, "manifest") if entry["scope"] == "manifest" else (prompts, "prompts")
        raw, target = target, unwrap(target)

        residue = mask(value, target)
        hits = [w for w in entry["forbid"] if locate(w, residue)]
        if hits:
            word = hits[0]
            lines = ", ".join(f"line {n}" for n in locate(word, residue))
            rows.append((
                "DRIFT", attr,
                f'canon says "{value}", {label} says "{word}" ({lines})',
            ))
            continue

        # The raw text too, since unwrap blanks a value that starts like a marker.
        found = locate(value, target) or locate(value, raw)
        if found:
            where = f"{len(found)} place{'s' if len(found) > 1 else ''} in {label}"
            rows.append(("ok", attr, f'"{value}" — {where}'))
        elif entry["required"]:
            rows.append((
                "MISSING", attr,
                f'canon requires "{value}" and it appears nowhere in the {label}',
            ))
        else:
            rows.append(("ok", attr, f"nothing forbidden in the {label}"))
    return rows


def read(path: Path, what: str) -> str:
    try:
        if not path.exists():
            raise CanonError(
                f"no {what} at {path}. The designer writes this file; an episode "
                f"without it has not been checked, which is not the same as passing."
            )
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise CanonError(f"{what} at {path} is not UTF-8 text") from exc
    except OSError as exc:
        raise CanonError(f"cannot read {what} at {path}: {exc.strerror}") from exc
    if not text.strip():
        raise CanonError(
            f"{what} at {path} is empty. An empty file has not been checked, "
            f"which is not the same as passing."
        )
    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check an episode's prompts and manifest against series canon.",
    )
    parser.add_argument("episode", type=Path, help="episode directory (holds prompts.md, manifest.md)")
    parser.add_argument("--canon", type=Path, required=True, help="the series canon document")
    args = parser.parse_args()
    # A terminal that cannot show a character must not turn into a crash.
    sys.stdout.reconfigure(errors="replace")

    try:
        entries = parse_canon(read(args.canon, "canon document"))
        if not entries:
            raise CanonError(
                f"{args.canon} has no ```canon blocks. A rule that is not a block "
                f"is a rule nobody enforces."
            )
        prompts = read(args.episode / "prompts.md", "prompts.md")
        manifest = read(args.episode / "manifest.md", "manifest.md")
        rows = check(entries, prompts, manifest)
    except CanonError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    width = max(len(attr) for _, attr, _ in rows)
    print(f"\n  {args.episode} against {args.canon}\n")
    for status, attr, detail in rows:
        print(f"  [{status:<7}] {attr:<{width}}  {detail}")

    drifted = sum(1 for status, _, _ in rows if status != "ok")
    print(f"\n  drifted={drifted}  pass={len(rows) - drifted}\n")
    if drifted:
        print(
            "  Drift does not mean the episode is wrong. It means the episode and\n"
            "  the canon disagree, and a person has to say which one moves. Fix the\n"
            "  prompt, or ask the person who keeps canon to change it.\n"
        )
    return 1 if drifted else 0


if __name__ == "__main__":
    sys.exit(main())
