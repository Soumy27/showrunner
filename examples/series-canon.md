# Series canon

**Series:** tinyhorror
**Premise:** A 30-second horror series. One apartment, one woman, one rule:
the camera never leaves the room she is in.
**Episode length:** 30s

This is an export of the "Series canon" room document, as the checker reads
it. In a live workflow this document lives in the `#tinyhorror-bible` room,
owned by the person who deployed the template — which is why no agent can
edit it.

## The world

```canon
- attr: world.room
  value: one apartment
  forbid: [outdoors, street, car, office, forest, rooftop]
  required: true
- attr: world.camera
  value: never leaves the room she is in
  forbid: [aerial, drone shot, exterior shot, establishing shot of the building]
```

## Characters

```canon
- attr: protagonist.name
  value: Mira
  required: true
- attr: protagonist.hair
  value: shaved head
  forbid: [short dark hair, long hair, ponytail, bangs, wavy hair]
  required: true
- attr: protagonist.wardrobe
  value: red flight jacket
  forbid: [blue jacket, hoodie, coat, leather jacket]
  required: true
```

## Look and sound

```canon
- attr: world.lighting
  value: flat, no lens flare
  forbid: [lens flare, golden hour, bloom, cinematic glow, god rays]
- attr: voice.id
  value: v_8821
  scope: manifest
  required: true
- attr: render.aspect
  value: 9:16
  scope: manifest
  required: true
```

## Established by episode

- **ep-03** — the hallway light has a two-second delay before it comes on.
- **ep-05** — Mira never speaks to the thing directly. She talks past it.
