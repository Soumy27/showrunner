# Episode 1: manifest

**Nothing was rendered.** Render mode is prompts-only. Every value below is what would be passed, not what was used. No model was called and no seed, job or output exists.

Model ids and limits are copied from `examples/live-run/manifest.md`, which read them from a service listing. They were not re-checked for this episode, because connected services are off limits to this role. Treat them as unverified.

## Shots

Model for every shot: `seedance_2_0`, mode `std`, `genre: auto`, `generate_audio: false`, `character sheet image as image_references`.

| Shot | Episode time | Final length | Render length | Aspect ratio | Voice id | Seed |
|---|---|---|---|---|---|---|
| 1 | 0:00-0:03 | 3s | 4s, trim to first 3s | 9:16 | none | none available |
| 2 | 0:03-0:07 | 4s | 4s | 9:16 | none | none available |
| 3 | 0:07-0:12 | 5s | 5s | 9:16 | v_8821 | none available |
| 4 | 0:12-0:15 | 3s | 4s, trim to first 3s | 9:16 | none | none available |
| 5 | 0:15-0:20 | 5s | 5s | 9:16 | none | none available |
| 6 | 0:20-0:24 | 4s | 4s | 9:16 | none | none available |
| 7 | 0:24-0:27 | 3s | 4s, trim to first 3s | 9:16 | v_8821 | none available |
| 8 | 0:27-0:30 | 3s | 4s, trim to first 3s | 9:16 | v_8821 | none available |

Final lengths total 30s.

## Dialogue

Model: `seed_audio`, with `voice_type: preset`, `voice_id: v_8821`. Lines placed in the edit at these episode times:

- Shot 3: "One." at 0:10.5, "Two." at 0:11.5
- Shot 7: "One." at 0:26.5, off screen, very quietly
- Shot 8: "Two." at 0:27.5

## Sound placed in the edit

No source for these is chosen.

- Click, light on: 0:02.5
- Click, light off: 0:08
- Click, light on: 0:11.5, on "Two."
- Click, light off: 0:13.5
- Click, light on: 0:27.5, on "Two."
- Room tone only through shot 5

## Stills

| Asset | Model | Aspect ratio | Seed |
|---|---|---|---|
| Character sheet: Mira | `soul_2` | 9:16 | none available |
| Thumbnails A, B, C | `soul_2` | 9:16 | none available |

## What a render would have to deal with

- **Seed:** the listing recorded in `examples/live-run/manifest.md` shows no seed parameter on `seedance_2_0` or `soul_2`, so none is recorded and no shot could be reproduced exactly. Mira's consistency rests on the character sheet reference and the verbatim prompt text.
- **3s shots:** that listing has `seedance_2_0` starting at 4s, in whole seconds, so shots 1, 4, 7 and 8 would render long and be trimmed.
- **Timing:** the model is not guaranteed to hit the clip times in the prompts, and these gaps have to be exact. Each one would have to be checked by eye and fixed in the edit. The last gap crosses the cut from shot 7 to shot 8.
- **The first frame:** the prop has to be legible on frame one of shot 1. A video model may not hold a small object in a walking hand, so this is the shot most likely to need several attempts.
- **Shot 3 framing:** the full width of a room in a 9:16 frame makes Mira small, and the camera cannot back out of the room to help.
- **Voice:** `v_8821` comes from canon, and canon does not say it is Mira's (script list, item 6). It has not been checked against the voices on any service, so `voice_type` above is an assumption.
- **Sound:** native audio is off so the model cannot invent a voice.
