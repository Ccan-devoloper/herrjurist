#!/usr/bin/env python3
"""Fixed-camera cartoon cels for the 01.10. review Reel; no digital zoom."""
import argparse
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent
W, H, FPS = 941, 1672, 30


def load(name):
    im = Image.open(ROOT / 'masters' / (name + '.png')).convert('RGB')
    if im.size not in [(W, H), (W, H - 1)]:
        raise ValueError(f'{name}: unexpected dimensions {im.size}')
    if im.height == H - 1:
        im = im.resize((W, H), Image.Resampling.LANCZOS)
    return im


def frame(t, ev, images, gate_mask):
    if t < ev['intro_end']:
        closed = images['01-gate-closed']
        if t < ev['door_close_at']:
            return Image.composite(images['00-gate-ajar'], closed, gate_mask)
        return closed
    if t < ev['silence_at']:
        return images['02-fachgericht']
    if t < ev['return_at']:
        return images['03-silence']
    if t < ev['evidence_at']:
        return images['04-mara-protests']
    if t < ev['law_at']:
        return images['05-empty-rights']
    if t < ev['reaction_at']:
        return images['06-law']
    if t < ev['two_hurdles_at']:
        return images['05-empty-rights']
    if t < ev['pointe_at']:
        return images['07-two-hurdles']
    return images['08-pointe']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timing', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    timing = json.loads(Path(args.timing).read_text())
    ev = timing['events']
    order = ['door_close_at', 'intro_end', 'silence_at', 'return_at',
             'evidence_at', 'law_at', 'reaction_at', 'two_hurdles_at',
             'pointe_at']
    if any(ev[a] >= ev[b] for a, b in zip(order, order[1:])):
        raise ValueError('Scene order is not strictly increasing: ' + str(ev))
    names = ['00-gate-ajar', '01-gate-closed', '02-fachgericht',
             '03-silence', '04-mara-protests', '05-empty-rights',
             '06-law', '07-two-hurdles', '08-pointe']
    images = {n: load(n) for n in names}
    mask = Image.new('L', (W, H))
    ImageDraw.Draw(mask).rectangle((636, 435, W, 1540), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(7))
    nframes = math.ceil(timing['final_duration'] * FPS)
    dest = Path(args.out)
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo',
           '-pixel_format', 'rgb24', '-video_size', f'{W}x{H}',
           '-framerate', str(FPS), '-i', 'pipe:0', '-vf',
           'scale=1080:1920:flags=lanczos,format=yuv420p',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19',
           '-pix_fmt', 'yuv420p', str(dest)]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for i in range(nframes):
            process.stdin.write(frame(i / FPS, ev, images, mask).tobytes())
        process.stdin.close()
        if process.wait():
            raise RuntimeError('FFmpeg silent export failed')
    except BaseException:
        process.kill()
        raise
    print(f'{dest}: {nframes} frames, {nframes / FPS:.2f} s, no zoom')


if __name__ == '__main__':
    main()
