# Character series

Set **Series format** to `character`, then paste these into the two canon fields under the advanced options. Change the title and the look to suit the show.

**Canon, the show**

```yaml
- attr: show.title
  value: Your Series Title
  required: true
- attr: show.proof
  value: Fiction:
  required: true
- attr: show.people
  value: one simple flat cartoon character
  forbid: [realistic person, talking head, stock footage]
  required: true
```

**Canon, the look**

```yaml
- attr: look.type
  value: short rounded captions
  forbid: [script font]
  required: true
- attr: look.palette
  value: night blue, warm orange, cream
  forbid: [gradient mesh, neon purple]
  required: true
- attr: look.motion
  value: gentle character walks and small gestures
  forbid: [ken burns, screen shake]
  required: true
- attr: look.audio
  value: narrator voice only, no music
  forbid: [drum, soundtrack]
  required: true
```
