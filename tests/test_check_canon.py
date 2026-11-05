#!/usr/bin/env python3
"""Tests for check-canon.py. Standard library only: `python3 tests/test_check_canon.py`.

Regression and edge cases for the checker. Several pin wrong answers it gave
during development, including:

  * `forbid: [car]` fired on the word "carries"
  * `forbid: [lens flare]` fired on a prompt correctly reading "no lens flare"
  * a canon value of "(interior)" or ".*" matched nothing, so a checked
    episode reported as unchecked

Exit codes under test: 0 clean, 1 drifted, 2 the canon or episode is unusable.
"""

import pathlib
import subprocess
import sys
import tempfile

CHK = str(pathlib.Path(__file__).resolve().parent.parent / "check-canon.py")

def run(canon, prompts, manifest="| shot | voice |\n| 1 | v_1 |\n", long_episode=False):
    d = tempfile.mkdtemp()
    ep = pathlib.Path(d, "ep")
    ep.mkdir()
    canon_path = pathlib.Path(d, "canon.md")
    if canon is None:
        canon_path.mkdir()
    else:
        canon_path.write_text(canon, encoding="utf-8")
    if isinstance(prompts, bytes):
        (ep / "prompts.md").write_bytes(prompts)
    else:
        (ep / "prompts.md").write_text(prompts, encoding="utf-8")
    (ep / "manifest.md").write_text(manifest, encoding="utf-8")
    target = str(ep / ("x" * 300)) if long_episode else str(ep)
    p = subprocess.run([sys.executable, CHK, target, "--canon", str(canon_path)],
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr

def block(body): return "# canon\n\n```canon\n" + body + "\n```\n"

CASES = []
def case(name, expect_code, canon, prompts, manifest=None, expect_in=None, long_episode=False):
    CASES.append((name, expect_code, canon, prompts, manifest, expect_in, long_episode))

# --- error paths (exit 2) ---
case("empty canon file", 2, "", "x")
case("no canon blocks", 2, "# just prose\n", "x", expect_in="no ```canon blocks")
case("field before entry", 2, block("  value: x"), "x", expect_in="field before any")
case("forbid not a list", 2, block("- attr: a\n  value: x\n  forbid: y, z"), "x", expect_in="one-line list")
case("bad scope", 2, block("- attr: a\n  value: x\n  scope: frames"), "x", expect_in="scope must be")
case("entry with no value", 2, block("- attr: a\n  required: true"), "x", expect_in="no value")

# --- word boundary ---
case("forbid 'car' must NOT match 'carries'", 0,
     block("- attr: a\n  value: one room\n  forbid: [car]"),
     "one room, and this carries over")
case("forbid 'car' DOES match standalone 'car'", 1,
     block("- attr: a\n  value: one room\n  forbid: [car]"),
     "one room with a car in it")

# --- masking: forbid term inside its own value ---
case("'no lens flare' not flagged for 'lens flare'", 0,
     block("- attr: a\n  value: flat, no lens flare\n  forbid: [lens flare]"),
     "> flat, no lens flare")
case("bare 'lens flare' IS flagged", 1,
     block("- attr: a\n  value: flat, no lens flare\n  forbid: [lens flare]"),
     "> flat, no lens flare\n> plus a lens flare here")

# --- markdown wrapping ---
case("value wrapped across blockquote lines", 0,
     block("- attr: a\n  value: flat, no lens flare\n  forbid: [lens flare]\n  required: true"),
     "> something flat, no\n> lens flare and more")
case("value wrapped across list-item lines", 0,
     block("- attr: a\n  value: red flight jacket\n  required: true"),
     "- wearing a red\n  flight jacket\n")

# --- required / missing ---
case("required value absent -> MISSING", 1,
     block("- attr: a\n  value: Mira\n  required: true"), "nobody here", expect_in="MISSING")
case("optional value absent -> ok", 0,
     block("- attr: a\n  value: Mira"), "nobody here")

# --- scope: manifest ---
case("manifest scope checks manifest not prompts", 1,
     block("- attr: v\n  value: v_8821\n  scope: manifest\n  required: true"),
     "prompt mentions v_8821 but manifest does not", "| 1 | v_1042 |\n", expect_in="MISSING")
case("manifest scope passes when manifest has it", 0,
     block("- attr: v\n  value: v_8821\n  scope: manifest\n  required: true"),
     "no voice here", "| 1 | v_8821 |\n")

# --- case insensitivity ---
case("case-insensitive match", 0,
     block("- attr: a\n  value: Shaved Head\n  required: true"), "> a SHAVED head")

# --- regex-special characters ---
case("regex chars in value: 9:16", 0,
     block("- attr: a\n  value: 9:16\n  required: true"), "> aspect 9:16")
case("regex chars in value: a+b", 0,
     block("- attr: a\n  value: a+b\n  required: true"), "> uses a+b here")
case("regex chars in value: parens", 0,
     block("- attr: a\n  value: (interior)\n  required: true"), "> shot (interior) wide")
case("regex chars in value: dot-star", 0,
     block("- attr: a\n  value: .*\n  required: true"), "> literally .* here")
case("regex chars in forbid: brackets", 1,
     block("- attr: a\n  value: ok\n  forbid: [[bad]]"), "> ok and [bad] here")

# --- line endings / unicode ---
case("CRLF line endings", 0,
     block("- attr: a\n  value: one room\n  required: true"), "> one room\r\n> more\r\n")
case("non-Latin value", 0,
     block("- attr: a\n  value: 一つの部屋\n  required: true"), "> 一つの部屋 here")
case("emoji in prompt, value still found", 0,
     block("- attr: a\n  value: one room\n  required: true"), "> one room \U0001F3A5 shot")

# --- multiple blocks ---
case("two canon blocks both enforced", 1,
     block("- attr: a\n  value: x\n  required: true") + block("- attr: b\n  value: y\n  required: true"),
     "> x only")

# --- a rule that cannot be read must stop the run, not silently go unenforced ---
A = "- attr: a\n  value: x\n"
case("misspelled field", 2, block(A + "  requierd: true"), "> x", expect_in="requierd")
case("capitalised field", 2, block(A + "  Required: true"), "> x", expect_in="Required")
case("attr with a space", 2, block("- attr: two words\n  value: x"), "> x", expect_in="two words")
case("required neither true nor false", 2, block(A + "  required: maybe"), "> x", expect_in="maybe")

# --- unusable input is exit 2, because exit 1 means drift ---
case("prompts not UTF-8", 2, block(A), b"\xff\xfe bad", expect_in="UTF-8")
case("canon is a folder", 2, None, "> x", expect_in="canon document")
case("empty prompts, optional canon", 2, block(A), "  \n", expect_in="empty")

# --- found in review: rules that silently did nothing, or matched too far ---
Q = '- attr: a\n  value: x\n  forbid: ["long hair"]'
case("quoted forbid still enforced", 1, block(Q), "> x long hair")
case("quoted value still enforced", 0, block('- attr: a\n  value: "x y"\n  required: true'), "> x y")
GOOD = block("- attr: a\n  value: x")
case("unclosed canon block", 2, GOOD + "```canon\n- attr: b\n  value: y\n  required: true\n", "> x",
     expect_in="canon block")
case("canon fence with extra words", 2, GOOD + "```canon notes\n- attr: b\n  value: y\n```\n", "> x",
     expect_in="canon block")
case("tilde canon fence", 2, GOOD + "~~~canon\n- attr: b\n  value: y\n~~~\n", "> x",
     expect_in="canon block")
R = block("- attr: a\n  value: red jacket\n  required: true")
case("value does not cross a blank line", 1, R, "> a red\n>\n> jacket")
case("value still found across one wrap", 0, R, "> a red\n> jacket")
case("value starting with a list marker", 0, block("- attr: a\n  value: -5 dB\n  required: true"), "-5 dB here")
case("episode path too long", 2, GOOD, "> x", expect_in="error:", manifest="m", long_episode=True)

fails = 0
for name, expect_code, canon, prompts, manifest, expect_in, long_episode in CASES:
    code, out = run(canon, prompts, manifest, long_episode) if manifest else run(canon, prompts)
    ok = (code == expect_code) and (expect_in is None or expect_in in out)
    if not ok:
        fails += 1
        print(f"FAIL  {name}\n      expected exit {expect_code}" +
              (f" containing {expect_in!r}" if expect_in else "") +
              f", got exit {code}\n{out.rstrip()}\n")
    else:
        print(f"pass  {name}")

# --- the examples the README quotes keep giving the results it quotes ---
ROOT = pathlib.Path(CHK).parent
EXAMPLES = [
    ("planted mistakes", "examples/ep-07", "examples/series-canon.md", 1, "drifted=2  pass=6"),
    ("live run", "examples/live-run", "examples/live-run/canon.md", 0, "drifted=0  pass=8"),
    ("Mattermost run", "examples/mattermost-run", "examples/mattermost-run/canon.md", 0, "drifted=0  pass=8"),
]
for name, episode, canon, expect_code, expect_in in EXAMPLES:
    p = subprocess.run([sys.executable, CHK, episode, "--canon", canon],
                       capture_output=True, text=True, cwd=ROOT)
    if p.returncode == expect_code and expect_in in p.stdout:
        print(f"pass  example: {name}")
    else:
        fails += 1
        print(f"FAIL  example: {name}\n{p.stdout}{p.stderr}")

# --- output a terminal cannot encode must not read as drift ---
p = subprocess.run([sys.executable, CHK, "examples/live-run", "--canon", "examples/live-run/canon.md"],
                   capture_output=True, text=True, cwd=ROOT, env={"PYTHONIOENCODING": "ascii"})
if p.returncode == 0:
    print("pass  ASCII-only terminal")
else:
    fails += 1
    print(f"FAIL  ASCII-only terminal: exit {p.returncode}")

total = len(CASES) + len(EXAMPLES) + 1
print(f"\n{total-fails}/{total} passed, {fails} failed")
sys.exit(1 if fails else 0)
