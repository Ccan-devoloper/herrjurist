#!/usr/bin/env python3
"""Locked-camera 30 fps reel: timed holds and discrete character cels, no zoom."""
import argparse
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent
W, H, FPS = 941, 1672, 30


def source(name):
    paths = [ROOT / 'masters' / (name + '.jpg'),
             ROOT.parent / 'reel-2026-09-30-v4' / 'masters' / (name + '.jpg')]
    for path in paths:
        if path.exists():
            im = Image.open(path).convert('RGB')
            if im.size != (W, H):
                raise ValueError(str(path) + ': master has unexpected dimensions')
            return im
    raise FileNotFoundError(name)


def soft_mask(box, blur):
    mask = Image.new('L', (W, H))
    ImageDraw.Draw(mask).rectangle(box, fill=255)
    return mask.filter(ImageFilter.GaussianBlur(blur))


def render_frame(t, timing, images, masks):
    e = timing['events']
    if t < e['intro_end']:
        base = images['01-consent']
        if t < e['scanner_at']:
            return base
        # Localized scanner response. This is already painted in the master.
        return Image.composite(images['01-reject'], base, masks['scanner'])
    if t < e['fatigue_at']:
        return images['02-interrogation']
    if t < e['slam_at']:
        return images['02-later-tired']
    if t < e['after_at']:
        return images['03-slam']
    if t < e['zylla_at']:
        return images['03-aftershock']
    if t < e['consent_at']:
        return images['04-statement']
    if t < e['law1_at']:
        return images['01-consent']
    if t < e['law2_at']:
        return images['05-law1']
    if t < e['shield_at']:
        return images['06-law2']
    if t < e['cross_at']:
        return images['07-shield']
    # The rejection is a masked paper change; the figures/table stay registered.
    return Image.composite(images['08-cross'], images['07-shield'], masks['paper'])


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--timing', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    timing = json.loads(Path(args.timing).read_text())
    names = ['01-consent', '01-reject', '02-interrogation',
             '02-later-tired', '03-slam', '03-aftershock',
             '04-statement', '05-law1', '06-law2', '07-shield', '08-cross']
    images = {name: source(name) for name in names}
    masks = {'scanner': soft_mask((695, 615, 940, 958), 8),
             'paper': soft_mask((285, 873, 830, 1295), 7)}
    dest = Path(args.out)
    dest.parent.mkdir(parents=True, exist_ok=True)
    frames = math.ceil(timing['final_duration'] * FPS)
    command = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo',
               '-pixel_format', 'rgb24', '-video_size', f'{W}x{H}',
               '-framerate', str(FPS), '-i', 'pipe:0', '-vf',
               'scale=1080:1920:flags=lanczos,format=yuv420p',
               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19',
               '-pix_fmt', 'yuv420p', str(dest)]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    try:
        for frame in range(frames):
            proc.stdin.write(render_frame(frame / FPS, timing, images, masks).tobytes())
        proc.stdin.close()
        if proc.wait():
            raise RuntimeError('FFmpeg video encoder failed')
    except BaseException:
        proc.kill()
        raise
    print(f'{dest}: {frames} frames, {frames / FPS:.2f}s, no zoom')


if __name__ == '__main__':
    main()
