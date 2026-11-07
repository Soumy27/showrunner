# Series canon

**Series:** soundsfake
**Premise:** Sounds Fake, Is True. A 30-second faceless series: one surprising fact per episode, true and sourced, told with bold animated type and charts.
**Episode length:** 30s

One block per thing that must stay true. The checker reads these and
nothing else. Replace the examples with your own and keep the shape.

## The show

```canon
- attr: show.title
  value: Sounds Fake, Is True
  required: true
- attr: show.proof
  value: Source:
  required: true
- attr: show.people
  value: no people on screen
  forbid: [talking head, presenter, actor, realistic person, stock footage]
  required: true
```

## The look

```canon
- attr: look.type
  value: giant condensed uppercase type
  forbid: [serif, handwritten, script font]
  required: true
- attr: look.palette
  value: ink, paper, coral, yellow, mint
  forbid: [pastel, gradient mesh, neon purple]
  required: true
- attr: look.motion
  value: hard cuts on the beat
  forbid: [slow fade, ken burns]
  required: true
```

## The format

```canon
- attr: format.aspect
  value: 9:16
  scope: manifest
  required: true
- attr: format.size
  value: 1080x1920
  scope: manifest
  required: true
```

## Established by episode

Added by a person as episodes establish things.
