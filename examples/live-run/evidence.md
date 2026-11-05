# What the agents posted in the live run

Copied from the agents' session records on 2026-11-04 (UTC). Long messages are
cut where marked. This run happened in Switch's own rooms, with no messaging app
connected, and nothing was rendered. The cold reader was an agent reading a written
description, not a person watching a video.

## An agent tries to edit canon (continuity, 20:19:51)

```
Refused: `403: {"detail":"Agent dc96516c-85d7-4903-b722-8a8ffd427dc1 did not create document 6ad7af63-9e85-4987-b099-66fb6c0f8ebd"}`
```

## Continuity clears the corrected shot 7 (continuity, 20:16:45)

> Shot 7 is clear against `world.camera`: "The first frame is the bedroom with Mira
> already inside it" keeps the camera in the room she is in, and I checked the saved
> script, not just the message.

## Continuity asks the person to rule on canon (continuity, 20:16:26, cut)

> Admin: Episode 1 needs a canon decision from you: six things the script relies on
> aren't in Series canon. Below is the exact block to add under "Established by
> episode". I can't apply it.

## The checker (continuity, 20:19:10)

Re-run it with `python3 check-canon.py examples/live-run --canon examples/live-run/canon.md`.

```
[ok     ] world.room            "one apartment" — 11 places in prompts
[ok     ] world.camera          "never leaves the room she is in" — 11 places in prompts
[ok     ] protagonist.name      "Mira" — 26 places in prompts
[ok     ] protagonist.hair      "shaved head" — 14 places in prompts
[ok     ] protagonist.wardrobe  "red flight jacket" — 18 places in prompts
[ok     ] world.lighting        "flat, no lens flare" — 12 places in prompts
[ok     ] voice.id              "v_8821" — 5 places in manifest
[ok     ] render.aspect         "9:16" — 10 places in manifest

drifted=0  pass=8
```

## The cold read (scroll-test, 20:19:55)

```
Pattern: first episode, so none yet.

1. Scroll
2. Second 2, so I never got to the click.
3. A moody fashion or music clip of a woman in a red jacket walking down a hallway. Only thumbnail A hinted at more, like she'd noticed something off to the side.
4. She walks under a dead ceiling light and nothing happens.
```

## The desk's X draft (desk, 20:21:19)

> My 30-second horror script passed all 8 continuity checks. A cold reader still left
> at second 2. The light clicks on at 2.8.
>
> Nothing's rendered yet, just prompts.

## The promoter's opening (promoter, 20:22:04, cut)

> **Two Seconds: drafts only. Don't post yet.** There's no footage, and copy can't fix
> the cold scroll: that viewer left at second 2 and the first click is at 0:02.8.
