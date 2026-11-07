# Story series: Two Dots

Set **Series format** to `story`, then paste these into the two canon fields under the advanced options.

**Canon, the show**

```yaml
- attr: show.title
  value: Two Dots
  required: true
- attr: show.proof
  value: Fiction:
  required: true
- attr: show.people
  value: no people on screen
  forbid: [talking head, presenter, actor, realistic person, stock footage]
  required: true
```

**Canon, the look**

```yaml
- attr: look.type
  value: small lowercase captions
  forbid: [giant uppercase, handwritten, script font]
  required: true
- attr: look.palette
  value: night ink, street grey, orange dot, blue dot
  forbid: [pastel, gradient mesh, neon purple]
  required: true
- attr: look.motion
  value: dots glide along city streets and draw glowing trails
  forbid: [flash cut, screen shake, ken burns]
  required: true
- attr: look.audio
  value: narrator voice only, no music
  forbid: [drum, soundtrack]
  required: true
```
