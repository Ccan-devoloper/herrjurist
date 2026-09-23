#!/usr/bin/env python3
import argparse
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

def rgb(hexwert):
    h = hexwert.strip().lstrip("#")
    return np.array([int(h[i:i+2], 16) for i in (0, 2, 4)], dtype=np.float32)

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True)
ap.add_argument("--output", required=True)
ap.add_argument("--crop-y", type=int, default=900)
args = ap.parse_args()

img = np.array(Image.open(args.input).convert("RGB"))
h, w = img.shape[:2]
y0 = max(0, min(h - 1, args.crop_y))
crop = img[y0:h].copy()

# Farben direkt aus dem bestehenden Cover ableiten:
# oben links liegt das dunkle Fachband, im freien Mittelbereich die Grundfarbe.
bg_probe = img[min(h - 1, 900):min(h, 1100), 0:min(w, 120)]
bg = np.median(bg_probe.reshape(-1, 3), axis=0).astype(np.float32)
dark_probe = img[8:min(h, 50), 8:min(w, 150)]
dark = np.median(dark_probe.reshape(-1, 3), axis=0).astype(np.float32)

# Alte Fusszeile lokal entfernen. Es werden nur kleine, texttypische dunkle
# Komponenten im bekannten Fussbereich maskiert; grosse Figuren-/Portalformen
# bleiben unangetastet.
yy1, yy2 = max(0, 1735 - y0), min(crop.shape[0], 1850 - y0)
xx1, xx2 = 700, min(w, 1075)
roi = crop[yy1:yy2, xx1:xx2]
if roi.size:
    dist_dark = np.linalg.norm(roi.astype(np.float32) - dark, axis=2)
    kandidat = (dist_dark < 42).astype(np.uint8)
    n, labels, stats, _ = cv2.connectedComponentsWithStats(kandidat, 8)
    maske_roi = np.zeros_like(kandidat)
    for i in range(1, n):
        x, y, cw, ch, area = stats[i]
        gx, gy = x + xx1, y + yy1 + y0
        # Schrift der Fusszeile: kompakte Komponenten nahe der Baseline.
        if gy >= 1748 and 4 <= ch <= 58 and 2 <= cw <= 300 and 8 <= area <= 2200:
            maske_roi[labels == i] = 255
    maske_roi = cv2.dilate(maske_roi, np.ones((3,3), np.uint8), iterations=1)
    maske = np.zeros(crop.shape[:2], dtype=np.uint8)
    maske[yy1:yy2, xx1:xx2] = maske_roi
    if np.any(maske):
        crop = cv2.inpaint(crop, maske, 3, cv2.INPAINT_TELEA)

# Einfarbigen Marken-Hintergrund lokal freistellen. Keine generative KI,
# kein externer Dienst: nur Farbdistanz und weiche Alpha-Kante.
dist_bg = np.linalg.norm(crop.astype(np.float32) - bg, axis=2)
alpha = np.clip((dist_bg - 10.0) / 34.0 * 255.0, 0, 255).astype(np.uint8)

# Reines JPEG-Rauschen in fast transparenten Flaechen entfernen.
alpha[alpha < 18] = 0
rgba = np.dstack([crop, alpha])
Path(args.output).parent.mkdir(parents=True, exist_ok=True)
Image.fromarray(rgba, "RGBA").save(args.output)
