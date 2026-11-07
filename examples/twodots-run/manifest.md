# Two Dots, episode 1: manifest, city cut

Status: this is the specified setup for the city cut. It has not been rendered, and the earlier
cut's measured figures no longer apply. If the renderer has to use anything different, it reports
it and this file changes to what was actually used.

## Format, all shots

- Aspect: 9:16
- Size: 1080x1920
- Frame rate: 30 fps
- Length: 30s
- Video: H.264, CRF 19, then converted to limited-range yuv420p, because `render-frames.mjs`
  writes yuvj420p
- Audio: AAC at the 192k setting
- Method: one HTML page drawn with code and rendered by `tools/render-frames.mjs`. No generated
  images or video.

## Shots

| Shot | Time | Length | Voice at | Voice until | Camera |
|---|---|---|---|---|---|
| 1 | 0:00-0:03 | 3s | 0.1 | 3.0 | fixed, full city |
| 2 | 0:03-0:07 | 4s | 3.1 | 7.0 | fixed, full city |
| 3 | 0:07-0:12 | 5s | 7.1 | 12.0 | fixed, full city |
| 4 | 0:12-0:15 | 3s | 12.1 | 15.0 | fixed, full city |
| 5 | 0:15-0:19 | 4s | 15.1 | 19.0 | fixed, full city |
| 6 | 0:19-0:23 | 4s | 19.1 | 21.0 | fixed, full city |
| 7 | 0:23-0:26 | 3s | 23.1 | 26.0 | fixed, full city |
| 8 | 0:26-0:30 | 4s | 26.1 | 29.0 | fixed, full city |

Voice lines are the exact `Voice` lines in `prompts.md`. Silence from 21.0 to 23.0 and from 29.0
to 30.0 is intended.

## Voice settings

The words and timing have not changed, so reuse the existing `episodes/ep-01/render/voice-30s.wav`
as it is: Kokoro voice `af_heart`, padded to 30.00s. No `--beat`, and `tools/make-beat.py` is not
used. The padding matters because `render-frames.mjs` encodes with `-shortest`.

## Colour values

Canon names these five colours and gives no values, so these hex values are this episode's choice
and are not canon.

| Colour | Hex | Used for |
|---|---|---|
| night ink | `#0b0e1a` | river, caption backing, base of the ground and buildings |
| street grey | `#9aa0ae` | tram line at 100%, streets at 32%, mixed into the ground and buildings |
| orange dot | `#ff8a2b` | orange dot and line |
| blue dot | `#3fa7ff` | blue dot and line |
| warm gold | `#ffc765` | captions, windows, streets and bloom in the gold light |

## Captions

- Avenir Next, weight 600, 88px, lowercase, warm gold at 100%, line height 1.12
- Centred on x=540, at most two lines, centred on y=1500, inside x 140-940 and y 1400-1600, so
  they clear the phone's interface
- A soft night-ink backing behind them at 72%, across the full width, full from y=1420 to y=1580
  and feathering out over 140px either side, with no visible edge, so the words stay easy to read over the city. The city stays visible through it.
- Fade in over 0.25s from 0.1s into the shot, and out over 0.15s at the end of the shot
- Two exceptions: shot 1's caption is at full opacity from frame 0, and shot 8's caption holds at
  full opacity through 30.00

## Output paths

The earlier cut is left in `episodes/ep-01/render/`. Do not build on its page or timeline.

- `episodes/ep-01/render/city/reel.html`
- `episodes/ep-01/render/city/reel.mp4`, `first-3s.mp4`, `cold-frames.png`
- `episodes/ep-01/render/city/thumbnail.png`: thumbnail idea 1 from `prompts.md`, drawn as its own
  frame, 1080x1920

## Render check

Before encoding, on the eased paths with the warp applied, check every frame: orange and blue line
centres at least 20px apart up to 0:23, and dot centres at least 100px apart up to 0:19. Also confirm
the caption fits its box in all eight shots, and read a still of each at phone size.
