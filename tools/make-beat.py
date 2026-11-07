#!/usr/bin/env python3
"""Write a simple 120 bpm beat as a WAV, with an impact at each time you list.

    python3 make-beat.py beat.wav --seconds 30 --hits 8.5,15.5 --cuts 0,3,6,9

Needs numpy. Everything is generated here, so there is no licensed audio in it."""
import argparse
import wave

import numpy as np

SR = 44100
p = argparse.ArgumentParser()
p.add_argument("out")
p.add_argument("--seconds", type=float, default=30)
p.add_argument("--hits", default="")
p.add_argument("--cuts", default="")
a = p.parse_args()
n = int(a.seconds * SR)
beat = np.zeros(n, np.float32)
rng = np.random.default_rng(5)


def add(at, sig, gain=1.0):
    s = int(at * SR)
    e = min(n, s + len(sig))
    if 0 <= s < n:
        beat[s:e] += (sig[: e - s] * gain).astype(np.float32)


def times(d):
    return np.arange(int(d * SR)) / SR


kt = times(0.28)
kick = np.sin(2 * np.pi * (48 * kt + 45 * (1 - np.exp(-kt * 28)) / 28)) * np.exp(-kt * 13)
ht = times(0.05)
hat = rng.normal(0, 1, len(ht)) * np.exp(-ht * 90) * np.sin(2 * np.pi * 7000 * ht)


def bass(f, d=0.42):
    t = times(d)
    return (np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t)) * np.minimum(t / 0.01, 1) * np.minimum((d - t) / 0.06, 1)


roots = [55, 55, 65.41, 49]
hits = [float(x) for x in a.hits.split(",") if x]
for i in range(int(a.seconds * 2)):
    at = i * 0.5
    if any(h - 0.5 <= at < h for h in hits):
        continue  # a held breath before each impact
    add(at, kick, 0.5 if i % 2 == 0 else 0.34)
    add(at + 0.25, hat, 0.1)
    add(at + 0.25, bass(roots[(i // 8) % 4]), 0.17)
it = times(1.1)
for h in hits:
    add(h, np.sin(2 * np.pi * 46 * it) * np.exp(-it * 3.2), 0.75)
for c in [float(x) for x in a.cuts.split(",") if x]:
    add(c, bass(110, 0.12), 0.1)
fade = int(0.4 * SR)
beat[:fade] *= np.linspace(0, 1, fade)
beat[-fade:] *= np.linspace(1, 0, fade)
beat = np.clip(beat / max(1, np.abs(beat).max() / 0.92), -1, 1)
w = wave.open(a.out, "wb")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(SR)
w.writeframes((beat * 32767).astype(np.int16).tobytes())
w.close()
print(f"wrote {a.out}")
