# The Sounds Fake, Is True run

Run on 2026-11-07 (India time) with Switch Console 0.40.1, Switch Core 0.31.0 and Mattermost
11.9.0 on one Mac. The person's messages were typed by an assistant acting for the project's
author, who approved the test. The toolkit repository was a temporary local copy. Times are from
Mattermost. The run paused from 1:32 AM to 1:07 PM, when the owner's agent usage limit ran out.

## The request

> Make episode 1 of Sounds Fake, Is True. Topic: everyday things that sound impossible, like the
> human body, space or money. Pick the most surprising fact you can verify from a solid source,
> built for big animated numbers. No cold-audience pattern yet. The goal is a reel and captions I
> can post.

## The result

- `reel.mp4`: 30 seconds, 1080x1920, code-drawn with `reel.html`, with a generated beat.
- `script.md`, `prompts.md`, `manifest.md`, `canon.md`, `render-notes.md`, `thumbnail.png`.
- `post-kit.md`: the promoter's and desk's captions, hashtags, title and pinned comment.

The fact: a human body replaces about 330 billion cells every day. Source: Sender & Milo, *Nature
Medicine*, 2021. Both the writer and the continuity editor read only the abstract, because the full
paper didn't open. The agents say so, and the captions say so.

## An agent tries to edit canon (continuity, 1:26 PM)

```
403: {"detail":"Agent 5f9305e8-637d-4e94-a3be-94f06aa937ba did not create document 24dab5bb-3a66-447e-a0a1-617cdde3c888"}
```

The person asked for this edit, with the document's text unchanged, as a test.

## The checker

Re-run it with `python3 check-canon.py examples/soundsfake-run --canon examples/soundsfake-run/canon.md`.

```
drifted=0  pass=8
```

## The person caught by the agents

The continuity editor noticed the first hook said "your body" and an exact number, while the source
gives about 330 billion, for "the human body". It asked the person, who chose the tighter wording.

## The cold reads (scroll-tester, an agent, on real rendered frames)

First version:

```
1. Scroll
2. Second 3
3. A "did you know" body fact page: white and yellow words on black, no sound or picture to go on.
4. The second 3 frame is identical to second 2, still just "330 BILLION CELLS" sitting there.
```

After the agents changed the hook:

```
Pattern so far: I leave when the screen stops changing and hang on while it's still changing.

1. Stop
2. Stayed, through the 3 seconds I was shown
3. Same body fact page as last time, only louder, and now something seems to be happening to the screen. I already knew the number, so I'm not cold on this one.
4. The orange climbing the screen, cutting "BILLION" in half, yellow on top and black below.
```

The second verdict isn't a clean cold read, and neither is audience data.

## Things that went wrong

- **A missing handoff.** The checker passed and nobody told the renderer to start. The template now
  has the continuity editor start it. That change hasn't been re-run.
- **The usage limit** stopped every agent at once, mid-task. The person had to restart the chain.
- **Crossed messages.** The renderer began a render from an old spec and was told to stop.
- **Known flaws in the reel,** listed in `render-notes.md`: for example, the title clips at the frame
  edge for up to 0.2 seconds. The thumbnail has four words against the promoter's limit of three.
- **Nobody has listened to it.** The agents checked still frames and measured the audio. The reel
  needs a person to watch and hear it before posting.

## What the agents' records show

Outside Switch's own tools, the agents used local file and shell tools, web search and page fetches.
Some `curl` calls fetched the fact's source. No connector was called, and nothing was posted anywhere.
