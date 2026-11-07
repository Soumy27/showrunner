# The Two Dots run (story format, not finished)

Run on 2026-11-07 (India time) with the same template, from one request in Mattermost. The person's
messages were typed by an assistant acting for the project's author, who approved the test. The
agents cloned the toolkit from the public GitHub repository.

## What worked

- The writer invented the story and marked it `Fiction:`. The designer wrote the spec.
- The renderer drew `reel-first-cut.mp4` with code and voiced it with `tools/make-voice.py`, with no music.
- The continuity editor ran the checker on the spec: `drifted=0 pass=9`.
- The continuity editor stopped and asked the person for a ruling on shot 3, because lines lighting up
  with no dot on them could break canon's `look.motion` rule. The person let them stay for this episode.
- A person changed canon through the API. The old spec then failed with `drifted=4 pass=7`, and the
  designer's new spec passed with `drifted=0 pass=11`.

## What didn't finish

- **The bolder cut.** The owner's agent usage limit stopped every agent at about 6:41 PM, while the
  renderer was building it. Only the first cut exists.
- **The cold read and the captions.** Neither ran, so this episode has no scroll-test verdict or post kit.
- **Nobody has listened to it.** The renderer measured the voice timing and can't hear it.

## Other things that went wrong

- **Safety check.** Claude Code's auto mode refused to run `check-canon.py` from the cloned repository
  ("Code from External"). It ran after the person said in chat that the repository was theirs and approved it.
- **Console's false error.** Console said "Nothing was created" after a timeout, but all seven agents and
  three rooms existed.
- **The first cut's look.** The person's review was that it reads like a circuit diagram with a flat ending,
  which is why they asked for the bolder version.
