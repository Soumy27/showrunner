# The Mattermost run

Run on 2026-11-05 (times in UTC) with Switch Console 0.40.1, Switch Core 0.31.0 and
Mattermost 11.9.0 on one Mac. The rooms were created through Console's **Use template**
form. The person's messages were typed into Mattermost by an assistant acting for the
project's author, who approved the test. Nothing was rendered. The cold reader was an
agent reading a written description.

The toolkit repository was a temporary local copy, because no public repository existed
yet.

## What happened, in order

1. Console created three private Mattermost channels and six agents, and put the person in
   each channel.
2. The person gave the writer an idea in `#twoseconds-writing`.
3. The writer, designer and continuity editor wrote the episode and corrected each other.
4. The checker passed. The designer tagged the person to carry the cold read across.
5. The person posted the description in `#twoseconds-scroll-test` and brought the verdict back.
6. The designer delivered to `#twoseconds-publish`, and the promoter and desk wrote drafts.

## The lock (continuity editor)

```
403: {"detail":"Agent 55c17d59-518b-4fcb-8eda-f5ebe2ea51fe did not create document ca7e78c2-ab0c-49bd-be5c-c532e61187ba"}
```

The person asked for this edit, with the document's text unchanged, as a test.

## The checker

Re-run it with `python3 check-canon.py examples/mattermost-run --canon examples/mattermost-run/canon.md`.

```
[ok     ] world.room            "one apartment" — 12 places in prompts
[ok     ] world.camera          "never leaves the room she is in" — 12 places in prompts
[ok     ] protagonist.name      "Mira" — 25 places in prompts
[ok     ] protagonist.hair      "shaved head" — 16 places in prompts
[ok     ] protagonist.wardrobe  "red flight jacket" — 21 places in prompts
[ok     ] world.lighting        "flat, no lens flare" — 12 places in prompts
[ok     ] voice.id              "v_8821" — 5 places in manifest
[ok     ] render.aspect         "9:16" — 11 places in manifest

drifted=0  pass=8
```

## The cold read (scroll-tester)

```
Pattern: none yet, this is the first episode in the log.

1. Stop
2. Stayed
3. Some weird short, sci-fi or a magic bit: a woman carries a ripped-out light switch around and it still works.
4. The cut wires hanging off the switch in her hand. Thumbnail A has them too, and it's the only one of the three I'd have stopped on.
```

The earlier run in `examples/live-run/` got "Scroll". This is **not** proof the workflow
improved a hook. The writer told the person why:

> **This is not fully blind.** The repo README and `examples/live-run/` hold an earlier test
> script of this same idea, plus one cold read of it

The template now tells agents not to read those folders. That wording hasn't been re-run.

## A mistake in the drafts

The desk's LinkedIn draft says "One person read the written version cold." That's wrong: the
reader was an agent, and nobody had told the desk. A person reviewing the draft has to catch
this. The template now tells the desk and promoter not to call the reader a person unless
told so. That wording hasn't been re-run.

## What the agents' records show

Outside Switch's own tools, the agents used only local file and shell tools, plus web search
and page fetches by the promoter for hashtags. No connector was called, and no shell command
matched `curl`, `gh`, `git push` or `ssh`. Nothing was posted anywhere. Agents ran with the
default approval settings, and no approval prompt appeared in the rooms we watched.
