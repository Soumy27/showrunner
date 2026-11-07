#!/usr/bin/env -S uv run --quiet --python 3.12 --script
# /// script
# dependencies = ["kokoro-onnx==0.4.9", "soundfile"]
# ///
"""Speak timed lines with a local voice and write them as a WAV, with an optional beat underneath.

    uv run tools/make-voice.py voice.json voice.wav --beat beat.wav

voice.json lists each line and the seconds it must fit between:

    [{"at": 0.1, "until": 3, "text": "Today, a human body replaces about 330 billion cells."}]

A line that runs long is sped up by at most 15%. If it still doesn't fit, nothing is written and the
exit code is 1, so shorten the line. The exit code is 2 for unusable input or missing voice files.

The voice runs on this computer with no account or media service. It needs ffmpeg, plus the two Kokoro
model files in ~/.cache/showrunner-voice (or $SHOWRUNNER_VOICE_DIR); the README has the download."""
import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf

SR = 44100
MAX_SPEED = 1.15


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def load_lines(path):
    try:
        lines = json.loads(Path(path).read_text(encoding="utf-8"))
        for line in lines:
            if not (line["text"].strip() and 0 <= line["at"] < line["until"]):
                fail(f"Bad line: {line}")
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        fail(f"Can't read {path}: {error}")
    if not lines:
        fail(f"{path} has no lines")
    lines = sorted(lines, key=lambda line: line["at"])
    for line, following in zip(lines, lines[1:]):
        if line["until"] > following["at"]:
            fail(f"These lines overlap: {line['text']} / {following['text']}")
    return lines


def resample(samples, rate):
    with tempfile.TemporaryDirectory() as folder:
        src, dst = Path(folder, "in.wav"), Path(folder, "out.wav")
        sf.write(src, samples, rate)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ar", str(SR), "-ac", "1", dst], check=True)
        return sf.read(dst, dtype="float32")[0]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("lines")
    p.add_argument("out")
    p.add_argument("--beat", help="WAV to play quietly under the voice")
    p.add_argument("--beat-level", type=float, default=0.14)
    p.add_argument("--voice", default="af_heart")
    a = p.parse_args()

    lines = load_lines(a.lines)
    models = Path(os.environ.get("SHOWRUNNER_VOICE_DIR", Path.home() / ".cache/showrunner-voice"))
    model, voices = models / "kokoro-v1.0.onnx", models / "voices-v1.0.bin"
    if not (model.exists() and voices.exists()):
        fail(f"Voice files not found in {models}. The person needs to download them; see the README.")

    from kokoro_onnx import Kokoro

    engine = Kokoro(str(model), str(voices))
    spoken, too_long = [], []
    for line in lines:
        room = line["until"] - line["at"]
        samples, rate = engine.create(line["text"], voice=a.voice, speed=1.0, lang="en-us")
        length = len(samples) / rate
        speed = 1.0
        if length > room:
            speed = min(MAX_SPEED, length / room * 1.02)
            samples, rate = engine.create(line["text"], voice=a.voice, speed=speed, lang="en-us")
            length = len(samples) / rate
        print(f"{line['at']:>6.2f}s  {length:.2f}s of {room:.2f}s  speed {speed:.2f}  {line['text']}")
        if length > room:
            too_long.append(line["text"])
        spoken.append((line["at"], resample(samples, rate)))
    if too_long:
        print("Too long to fit, even sped up:", *too_long, sep="\n  ", file=sys.stderr)
        sys.exit(1)

    end = max(at + len(samples) / SR for at, samples in spoken)
    music = None
    if a.beat:
        try:
            music, rate = sf.read(a.beat, dtype="float32", always_2d=True)
        except (OSError, RuntimeError) as error:
            fail(f"Can't read {a.beat}: {error}")
        if rate != SR:
            music = resample(music, rate)[:, None]
        music = music.mean(axis=1)
        end = max(end, len(music) / SR)

    mix = np.zeros(int(end * SR) + 1, np.float32)
    for at, samples in spoken:
        start = int(at * SR)
        mix[start : start + len(samples)] += samples
    peak = float(np.abs(mix).max())
    if peak == 0:
        fail("The voice came out silent.")
    mix *= 0.85 / peak
    if music is not None:
        mix[: len(music)] += music * a.beat_level
    mix = np.clip(mix, -1, 1)
    sf.write(a.out, mix, SR, subtype="PCM_16")
    print(f"Wrote {a.out}: {len(mix) / SR:.2f}s, peak {np.abs(mix).max():.2f}")


if __name__ == "__main__":
    main()
