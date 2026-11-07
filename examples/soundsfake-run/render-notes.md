# Sounds Fake, Is True: Episode 1, render notes

This render is from the 1:32 spec, the hook-only fix after the cold verdict. It replaces all earlier renders.

This is code-drawn motion graphics: HTML type and shapes drawn frame by frame in headless Chrome. There is no generated footage, no people, no voice and no licensed audio. The beat comes from `tools/make-beat.py`.

## Measured with ffprobe

| File | Length | Frames | Size | Rate | Audio |
|---|---|---|---|---|---|
| `reel.mp4` | 30.000s | 900 | 1080x1920 | 30 fps | AAC, 30.000s |
| `first-3s.mp4` | 3.000s | 90 | 1080x1920 | 30 fps | AAC, 3.000s |

- **Audio level:** max -0.7 dB, mean -16.1 dB.
- **Cuts:** scene detection finds cuts at 3, 5, 10, 13, 18, 20, 25 and 27s, and shot 1 starts at 0. It also flags 1.5s, 11.5s and 16.5s, which are the slams and the bracket snap, plus the settling frames after some cuts.
- **Locks, read from exact frames:** the counter shows 329 on frame 284 and 330 on frame 285 (9.5s). The weight shows 79 with no bracket on frame 494, and `80 ± 20` with the bracket on frame 495 (16.5s). The bottom grid row is still unflipped on frame 749, the last of shot 7.

## Shot 1, measured from the encoded video

- **Size:** the six-line block runs from y=243 to y=1656, which is 73.6% of the frame height. The spec asks for at least 70%.
- **Type sizes:** `REPLACES` and `CELLS` fit at the spec's 200px, so they did not need reducing.
- **Slam:** at 1.12x, starting from the centre of each full-width line, the type stays in frame on every frame before the block appears (x=7 to x=1076).
- **Block:** it first shows on frame 46 and its top edge moves about 43px per frame, reading y=1280 on frame 60 and y=44 on frame 89. It is still moving on the last frame and has not reached the top, as specified. The edge is rounded to whole pixels.
- **Split:** on frame 60, a row just above the edge has yellow in `BILLION` and no coral; a row just below has coral and ink and no yellow. On frame 89 all type is ink on coral.

## Not checked

- I checked still frames and measurements only. Nobody has watched the reel in motion or listened to the audio, so how the block's rise and the slams feel is untested.
- Whether the nine-word hook can be read in 3s is unproven, and the block crosses the type while it is being read. It needs a person to watch it.
- I did not query which font file Chrome used. The type looks like `Avenir Next Condensed` in every still, and the font is installed.

## Where the picture falls short

**Shot 1, hook.**
- **"Fills the frame":** the spec applies the 70% to the six-line block. The `ABOUT` / `330` / `BILLION` stack alone is about 45% of the frame height (861px, measured in shot 3 at the same sizes). If the person meant the stack by itself, this falls short.
- **Second 1 has no number:** at 1.0s the screen reads `TODAY A HUMAN BODY REPLACES`, a large empty gap, then `CELLS`. It stays that way until 1.5s. This follows the spec, so the number never appears without `ABOUT`, but anyone who leaves before 1.5s never sees the number.
- **Script:** `script.md` shot 1 still said "Graphic: type only" when this was rendered, because the block came in through the spec. Continuity has asked the writer to update it.

**Slams outside shot 1.** The hook-only decision puts these back to the first render's 1.35x, so full-width lines run past the margins and clip at the frame edge for up to 0.2s. It is most visible at 3.0s and 25.0s, and they settle inside the margins.

**Shot 2, title.** Back to the first render: the -1.6deg rotation pushes the corners of the fitted lines a few pixels past the 64px margin. Both lines still fit in frame.

**Shots 3 and 8, counter.**
- To land on the beat, the counter rounds down rather than using the starter's rounding, which would have shown 330 about half a second early. It sits on 329 from about 8.85s until the lock at 9.5s.
- The climb passes through figures the source does not give. A paused frame can read `ABOUT 0 BILLION` or `ABOUT 174 BILLION`, and shot 8 is on about 271 at its last frame. The person's call on this is still open, and a decision against count-ups would need another render.

**Shot 5, weight.**
- The spec gives no curve for this count. I used shot 3's cubic ease-out over 3.5s, so it sits on 79 from about 15.7s until the lock. A paused frame can read `73 GRAMS OF CELLS`.
- The bar moves in whole grams because its width is tied to the displayed count.

**Shot 8, reset.** Back to the first render, as the spec now asks. The script says the counter climbs "behind the type", but the ink panels sit above and below the stack and overlap only its line boxes, not the letters. It reads as a stack between two lines. The stack keeps shot 3's position without its label, so about 30% of the frame below it is empty.

**Thumbnail.** `thumbnail.png` is thumbnail idea 1, as the designer asked: `ABOUT`, `330`, `BILLION`, `CELLS`. It is drawn separately, so it is not a frame from the reel. Its four lines stay readable at 120px wide, but I judged that by eye rather than measuring each line against the 135px minimum.

**Cold frames.** `cold-frames.png` uses frames 30, 60 and 89 (1.0s, 2.0s and 2.967s). Exactly 3.0s is the first frame of the title shot, so I used the last frame of the third second. All three now differ.

## Layout choices the spec left open

- **Shot 1:** 44px gaps either side of the `ABOUT` / `330` / `BILLION` stack.
- **Shot 3:** the label is on two fitted lines.
- **Shot 4:** `IT`, `HAS` and `A` at 240px, so `WEIGHT.` is the largest.
- **Shot 5:** `DAILY.` at 190px.
- **Shot 9:** `Source:` is also fitted to the width, `2021` at 180px, `Sender & Milo` at 145px.
- **Thumbnail:** `ABOUT` at 240px, `CELLS` at 300px.

## Settings against the manifest

Everything used matches the manifest: size, frame rate, length, colours, typeface, margins and beat arguments. The script, spec, manifest and canon were not changed. The manifest's status line still says the render is out of date.
