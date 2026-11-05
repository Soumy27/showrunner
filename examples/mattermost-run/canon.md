# Series canon

**Series:** twoseconds
**Premise:** A 30-second horror series. One apartment, one woman, one rule: the camera never leaves the room she is in.
**Episode length:** 30s

One block per thing that must stay true. The checker reads these and
nothing else. Replace the examples with your own and keep the shape.

## The world

```canon
- attr: world.room
  value: one apartment
  forbid: [outdoors, street, car, office, forest, rooftop]
  required: true
- attr: world.camera
  value: never leaves the room she is in
  forbid: [aerial, drone shot, exterior shot]
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
  forbid: [lens flare, golden hour, bloom, cinematic glow]
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

Added by a person as episodes establish things.
