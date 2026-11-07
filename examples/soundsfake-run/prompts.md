# Sounds Fake, Is True: Episode 1, render spec

These are instructions for the renderer. The first cold verdict came before this version of shot 1. The current render in `render/` was made from this version, and every other shot is as it was in the first render.

**Fact:** A human body replaces about 330 billion cells every day.
**Length:** 30s, 900 frames.
**Beat:** 120 bpm, so one beat is 0.5s. Every time below sits on that grid.

**Source line, as it appears on screen in shot 9:** `Source: Nature Medicine, 2021` / `Sender & Milo`

**Full source:** Sender R. & Milo R., "The distribution of cellular turnover in the human body", Nature Medicine (Springer Nature), 2021. https://www.nature.com/articles/s41591-020-01182-9 (DOI 10.1038/s41591-020-01182-9)

**Sentences relied on, from the abstract:** "We found a total cellular mass turnover of 80 ± 20 grams per day, dominated by blood cells and gut epithelial cells. In terms of cell numbers, close to 90% of the (0.33 ± 0.02) × 10^12 cells per day turnover was blood cells."

**Numbers on screen:** only those in the script. No per-second rate, no 86%, no other figure. No twelve-digit figure at any point, and `330` always appears with `ABOUT` beside it in shots 1 and 3.

## Rules for every shot

- All text renders through `text-transform: uppercase`. Keep the source strings in the casing written here.
- Text stays inside the 64px side margins, so the text width is 952px.
- Each shot holds at scale 1 for its whole length. Delete the starter's per-shot scale creep, white cut flash and progress bar, and use none of its red, violet, glow or grey panel colours.
- A slam or stamp is the starter's `p` pop: on at the stated time, settled in 0.2s. It starts at 1.35x, except in shot 1, where it starts at 1.12x so the stack stays inside the frame.
- Colour is flat. Only the five canon colours, with no tints or opacity.

## Shots

### Shot 1. Hook (3s, 0:00-0:03)

- **On screen:** `TODAY A HUMAN BODY REPLACES ABOUT 330 BILLION CELLS`
- **Canon:** no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** ink background, paper type, `ABOUT 330 BILLION` in yellow. Coral block with ink type wherever the block covers the screen.
- **Layout:** six lines: `TODAY A HUMAN BODY` / `REPLACES` / `ABOUT` / `330` / `BILLION` / `CELLS`. Set `ABOUT`, `330` and `BILLION` at the same sizes as the shot 3 stack, so `330 BILLION` is by far the biggest thing on screen. Fit `TODAY A HUMAN BODY` to the 952px width, and set `REPLACES` and `CELLS` at 200px. The block fills at least 70% of the frame height.
- **Motion:** slam `TODAY A HUMAN BODY` at 0.0s, `REPLACES` at 0.5s, `CELLS` at 1.0s, leaving the `ABOUT`, `330` and `BILLION` slots empty. Slam those three into their slots together last, at 1.5s, so the number never shows without `ABOUT`. The type then holds still.
- **The big move:** at 1.5s, on the same frame as that slam, a full-width solid coral block starts rising from the bottom edge of the frame at a constant 1280px per second. It is still moving on the last frame of the shot, and reaches the top at the 3.0s cut. The block's top edge is a hard horizontal line. All type below that line is ink and all type above it keeps its colour, split exactly at the line, so a letter can be two colours at once. No fades. The number never changes.

### Shot 2. Title (2s, 0:03-0:05)

- **On screen:** `Sounds Fake, Is True`
- **Canon:** Sounds Fake, Is True. no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** yellow background, ink type.
- **Layout:** two lines, `Sounds Fake,` / `Is True`, each fitted to the 952px width, rotated -1.6deg as one block.
- **Motion:** hard cut at 3.0s. One stamp at 3.0s, then hold.

### Shot 3. The count (5s, 0:05-0:10)

- **On screen:** `ABOUT 330 BILLION` / `CELLS REPLACED. EVERY DAY.`
- **Canon:** no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** ink background, yellow `ABOUT`, counter and `BILLION`, so they read as one phrase. Paper label.
- **Layout:** a stack of `ABOUT` / counter / `BILLION`, with `BILLION` fitted to the full 952px and the counter's digits at least that size. Use tabular digits and fit the three-digit width, so the digits don't shift as the number grows. No twelve-digit figure and no commas. The label sits below.
- **Motion:** `ABOUT`, `BILLION` and the label are on and fixed from 5.0s. Between them the counter climbs from 0 at 5.0s and reaches 330 at 9.5s, the final beat. Use the starter's cubic ease-out over 4.5s. Hold to the cut.

### Shot 4. Turn (3s, 0:10-0:13)

- **On screen:** `IT HAS A WEIGHT.`
- **Canon:** no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** paper background, ink type. This is the opposite of shot 3.
- **Layout:** one word per line, with `WEIGHT.` fitted to the 952px width and the largest.
- **Motion:** hard cut at 10.0s. Slam `IT` at 10.0s, `HAS` at 10.5s, `A` at 11.0s, `WEIGHT.` at 11.5s. Hold to the cut.

### Shot 5. The weight (5s, 0:13-0:18)

- **On screen:** `80 ± 20 GRAMS OF CELLS. DAILY.`, plus the bracket label `± 20`
- **Canon:** no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** paper background, ink type, coral bar, ink bracket and bracket label.
- **Layout:** `80 ± 20` on the first line, largest. `GRAMS OF CELLS.` / `DAILY.` below it. The single horizontal bar sits under the type.
- **Scale:** 9.52px per gram, from a zero baseline at x=64. The bar ends at x=825.6 (80). The bracket runs from x=635.2 (60) to x=1016 (100). So the range is drawn to the same scale as the bar. Do not print 60, 100, 0 or any other axis number.
- **Motion:** at 13.0s the type slams on with `80` showing as 0 and the `± 20` in the line hidden. `80` counts up from 0 while the bar grows, with bar width tied directly to the count. Both lock at 16.5s. On that same frame the bracket and its `± 20` label snap on and `± 20` appears in the line. Hold to the cut.

### Shot 6. Turn (2s, 0:18-0:20)

- **On screen:** `WHICH CELLS?`
- **Canon:** no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** coral background, ink type.
- **Layout:** two lines, `WHICH` / `CELLS?`, each fitted to the 952px width.
- **Motion:** hard cut at 18.0s. One hit at 18.0s, then hold.

### Shot 7. The split (5s, 0:20-0:25)

- **On screen:** `CLOSE TO 90% ARE BLOOD CELLS`
- **Canon:** no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** ink background, paper type, grid squares paper until flipped, then mint.
- **Layout:** the line above, ten-by-ten square grid below, 952px wide with even gaps. No labels on the grid; the only figure is the 90% in the line. The grid counts cells, not grams, so nothing from the shot 5 bar carries over.
- **Motion:** hard cut at 20.0s, with the line slamming on at that moment. Flip the nine rows to mint from the top, one per beat, at 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5 and 24.0s. Each row changes colour on a single frame. The bottom row never flips. Hold to the cut, so the unflipped row can be read.

### Shot 8. Reset (2s, 0:25-0:27)

- **On screen:** `TOMORROW? ALL OVER AGAIN.`, with the shot 3 counter behind it
- **Canon:** no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** ink background, coral counter, paper type on solid ink panels.
- **Layout:** the `ABOUT` / counter / `BILLION` stack at the same size and position as shot 3, in coral, with no shot 3 label. `TOMORROW?` and `ALL OVER AGAIN.` sit over the top and bottom edges of the stack, each on a solid ink panel so the type stays readable. The panels must leave the digits, `ABOUT` and `BILLION` readable too.
- **Motion:** hard cut at 25.0s. The counter reads 0 on the cut and climbs on shot 3's curve. It is still climbing at the next cut and never stops on a number. Type slams on at 25.0s.

### Shot 9. Source (3s, 0:27-0:30)

- **On screen:** `Source: Nature Medicine, 2021` / `Sender & Milo`
- **Canon:** Source: no people on screen. giant condensed uppercase type. ink, paper, coral, yellow, mint. hard cuts on the beat.
- **Colour here:** paper background, ink type.
- **Layout:** `Source:` / `Nature Medicine,` / `2021` / `Sender & Milo`, with `Nature Medicine,` fitted to the 952px width. Use the show's type, not the starter's monospace source style.
- **Motion:** hard cut at 27.0s. Everything hits at once at 27.0s and holds to the end at 30.0s.

**Total: 3 + 2 + 5 + 3 + 5 + 2 + 5 + 2 + 3 = 30 seconds.**

## Thumbnail ideas

At 120px wide everything is one-ninth of its full size, so nothing goes below 135px tall at full size (15px in the thumbnail). All use giant condensed uppercase type, in ink, paper, coral, yellow, mint. Words come from the script only.

1. **The number:** ink background, `ABOUT` in yellow, `330` in yellow filling the width, `BILLION` fitted to the width under it, `CELLS` in paper below. Four lines and nothing else.
2. **The grid:** ink background, the shot 7 grid at full width with its nine mint rows and one paper row, `CLOSE TO 90%` in paper above it on one or two lines. The unflipped row is the thing to spot.
3. **The weight:** paper background, `80 ± 20` in ink filling the width, `GRAMS` under it, and a thick coral bar with the ink bracket below.
