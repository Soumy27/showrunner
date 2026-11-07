# Sounds Fake, Is True: Episode 1, manifest

**Status:** the current render in `render/` was made from this spec, after the cold verdict changed shot 1 only. The renderer reports that its settings match. The new hook has not yet had a cold verdict. The renderer corrects this file if anything it actually uses differs.

**Format for every shot:** aspect 9:16, size 1080x1920, 30 fps, 30s and 900 frames in total.

| Shot | Name | Start | Length | Frames | Aspect | Size | FPS | Background | Build |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Hook | 0.0s | 3s | 90 | 9:16 | 1080x1920 | 30 | ink, coral block rising from 1.5s | code: type, block |
| 2 | Title | 3.0s | 2s | 60 | 9:16 | 1080x1920 | 30 | yellow | code: type |
| 3 | The count | 5.0s | 5s | 150 | 9:16 | 1080x1920 | 30 | ink | code: type, counter |
| 4 | Turn | 10.0s | 3s | 90 | 9:16 | 1080x1920 | 30 | paper | code: type |
| 5 | The weight | 13.0s | 5s | 150 | 9:16 | 1080x1920 | 30 | paper | code: type, counter, bar, bracket |
| 6 | Turn | 18.0s | 2s | 60 | 9:16 | 1080x1920 | 30 | coral | code: type |
| 7 | The split | 20.0s | 5s | 150 | 9:16 | 1080x1920 | 30 | ink | code: type, grid |
| 8 | Reset | 25.0s | 2s | 60 | 9:16 | 1080x1920 | 30 | ink | code: type, counter |
| 9 | Source | 27.0s | 3s | 90 | 9:16 | 1080x1920 | 30 | paper | code: type |

## Settings

- **Render:** `tools/render-frames.mjs`, from a copy of `tools/reel-starter.html`, with `--seconds 30 --size 1080x1920`. Its frame rate is fixed at 30.
- **Colours:** the starter's values for the canon names. ink `#0b0b0f`, paper `#f7f3ea`, coral `#ff6a3d`, yellow `#ffe14d`, mint `#2fe39a`.
- **Type:** the starter's `Avenir Next Condensed`, weight 800. Do not let it fall back to the non-condensed `Avenir Next`.
- **Margins:** 64px left and right.
- **Audio:** `tools/make-beat.py` at its fixed 120 bpm, so no licensed audio and no voice. `--seconds 30 --cuts 0,3,5,10,13,18,20,25,27 --hits 1.5,9.5,16.5`
- **Generated images or footage:** none.
