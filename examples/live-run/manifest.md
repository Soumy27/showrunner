# Episode 1: manifest

**Nothing was rendered.** Render mode is prompts-only. Every value below is what would be passed, not what was used. No model was called and no seed, job or output exists.

Model ids and limits were read from the Higgsfield model listing on 2026-11-05. No generation was run.

## Shots

Model for every shot: `seedance_2_0`, mode `std`, `genre: auto`, `generate_audio: false`, `character sheet image as image_references`.

| Shot | Episode time | Final length | Render length | Aspect ratio | Voice id | Seed |
|---|---|---|---|---|---|---|
| 1 | 0:00-0:03 | 3s | 4s, trim to first 3s | 9:16 | none | none available |
| 2 | 0:03-0:07 | 4s | 4s | 9:16 | none | none available |
| 3 | 0:07-0:10 | 3s | 4s, trim to first 3s | 9:16 | none | none available |
| 4 | 0:10-0:15 | 5s | 5s | 9:16 | v_8821 | none available |
| 5 | 0:15-0:18 | 3s | 4s, trim to first 3s | 9:16 | none | none available |
| 6 | 0:18-0:22 | 4s | 4s | 9:16 | v_8821 | none available |
| 7 | 0:22-0:26 | 4s | 4s | 9:16 | none | none available |
| 8 | 0:26-0:30 | 4s | 4s | 9:16 | v_8821 | none available |

## Dialogue

Model: `seed_audio`, with `voice_type: preset`, `voice_id: v_8821`. Lines placed in the edit at these episode times:

- Shot 4: "One." at 0:12, "Two." at 0:13
- Shot 6: "It's not coming on for me."
- Shot 8: "One." at 0:26.5

## Stills

| Asset | Model | Aspect ratio | Seed |
|---|---|---|---|
| Character sheet: Mira | `soul_2` | 9:16 | none available |
| Thumbnails A, B, C | `soul_2` | 9:16 | none available |

## What a render would have to deal with

- **Seed:** the listing shows no seed parameter on `seedance_2_0` or `soul_2`, so none is recorded and no shot can be reproduced exactly. Mira's consistency rests on the character sheet reference and the verbatim prompt text.
- **3s shots:** `seedance_2_0` starts at 4s and takes whole seconds, so shots 1, 3 and 5 would render long and be trimmed.
- **Timing:** the model is not guaranteed to hit the clip times in the prompts. The two-second gaps would have to be checked by eye and fixed in the edit.
- **Voice:** `v_8821` comes from canon. It has not been checked against the voices available on this service, so the `voice_type` above is an assumption.
- **Sound:** native audio is off so the model cannot invent a voice. The clicks, the switch and the door at the times in `prompts.md` would be added in the edit, and no source for them is chosen.
