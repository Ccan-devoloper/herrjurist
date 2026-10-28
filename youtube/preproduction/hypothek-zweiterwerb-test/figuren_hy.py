"""Mehrfarbige Open-Peeps-Figuren: Kopf in Hautfarbe (SVG), Körperflächen per Konturlinien-Segmentierung eingefärbt."""
import json, subprocess, io, sys
import numpy as np, cairosvg
from PIL import Image, ImageOps
from scipy import ndimage

H_STAND, H_BUST = 1400, 1400
# Farbflächen je Pose (Komponenten-IDs aus den Kartenbildern maps_*.png, Renderhöhe 1400 px)
KLASSEN = {
    "RestingWB":   {"haut": [1, 3, 5], "oben": [2, 4], "socke": [18, 19], "schuh": [20, 21]},
    "RoboDanceWB": {"haut": [1, 5, 10], "oben": [2, 6], "socke": [14, 15], "schuh": [16, 17], "sohle": [31, 32]},
    "WalkingBW":   {"haut": [1, 3, 4], "unten": [5], "schuh": [6, 10, 13], "socke": [12], "sohle": [19]},
    "RoboDanceBW": {"haut": [1, 4, 7], "unten": [10, 11], "socke": [12, 13], "schuh": [14, 15], "sohle": [23, 24]},
    "Killer":      {"haut": [1, 5], "griff": [3], "klinge": [4]},
    "Device":      {"haut": [1, 17], "oben": [9, 16], "objekt": [14, 12]},
    "ArmsCrossed": {"haut": [1, 11, 12, 13]},
    "PointingUp":  {"haut": [1, 2, 3, 6], "_rest": "muster"},
    "Coffee":      {"haut": [1, 5, 7], "objekt": [6], "oben": [2]},
    "Whatever":    {"haut": [1, 18, 19], "_rest": "oben"},
    "Shirt":       {"haut": [1, 5], "oben": [3]},
    "HandsBackBW": {"haut": [1, 2, 3], "unten": [4], "schuh": [5]},
    "PointingFingerWB": {"haut": [1, 5, 7], "oben": [2], "schuh": [10, 11]},
    "WalkingWB": {"haut": [1, 4, 5, 6], "oben": [2], "socke": [13], "schuh": [7, 14], "sohle": [11, 20]},
    "BlazerPantsWB": {"haut": [1, 9, 10], "oben": [2, 4, 7, 3], "innen": [5], "socke": [11], "schuh": [13, 14]},
    "CrossedArmsWB": {"haut": [1, 9], "oben": [2, 11], "socke": [14, 15], "schuh": [17, 18], "sohle": [19, 20]},
    "ShirtPantsWB": {"haut": [1, 7, 8], "oben": [2, 3, 4, 5, 6], "socke": [9, 10], "schuh": [11, 12], "sohle": [13, 15]},
    "EasingWB": {"haut": [1, 16, 17], "oben": [4, 6, 11, 14, 18], "innen": [13], "socke": [19, 20], "schuh": [21, 22, 23, 24], "sohle": [25, 26]},
}
HAUT = {"hell": "#F6D2B4", "mittel": "#E0A57E", "braun": "#B07552", "dunkel": "#7B4B34"}
P = dict(pink="#F6A5C0", gruen="#8FD694", gelb="#F9D56E", blau="#8DB3F2", lila="#B8A9F5", tuerkis="#7FD6D0",
         orange="#F9A66C", rot="#F07A6A", weiss="#FFFFFF", schwarz="#1B1B1B", grau="#D9D9D9", dunkelgrau="#3C3C44", silber="#DADDE3", braun="#8A5A3C")

PERSONEN = {
    # feste Statur je Person: nur schlanke Posen (BlazerPants, ShirtPants, Easing, Walking)
    "EM": dict(hair="MediumBangsFilled", haut="hell", oben="tuerkis", innen="weiss", socke="pink", schuh="braun", sohle="braun"),
    "BR": dict(hair="ShortMessy", facialHair="Goatee", haut="mittel", oben="blau", socke="gelb", schuh="schwarz", sohle="schwarz"),
    "CL": dict(hair="Bun", haut="braun", oben="lila", innen="weiss", socke="gelb", schuh="weiss", sohle="grau"),
    "DV": dict(hair="FlatTop", haut="dunkel", oben="orange", socke="pink", schuh="weiss", sohle="grau"),
}
FIGUREN = [
    ("EM_ruhig", "EM", "BlazerPantsWB", "Calm", 0, 0), ("EM_froh", "EM", "BlazerPantsWB", "Smile", 0, 0),
    ("EM_besorgt", "EM", "BlazerPantsWB", "ConcernedFear", 0, 0), ("EM_sauer", "EM", "BlazerPantsWB", "Angry", 0, 0),
    ("BR_ruhig", "BR", "ShirtPantsWB", "Smile", 0, 1), ("BR_verschlagen", "BR", "ShirtPantsWB", "Cheeky", 0, 1),
    ("BR_verschlagen_r", "BR", "ShirtPantsWB", "Cheeky", 0, 0),
    ("CL_froh", "CL", "EasingWB", "Smile", 0, 0), ("CL_ruhig", "CL", "EasingWB", "Calm", 0, 0),
    ("CL_ruhig_l", "CL", "EasingWB", "Calm", 0, 1),
    ("DV_ruhig", "DV", "WalkingWB", "Calm", 0, 1), ("DV_wissend", "DV", "WalkingWB", "Suspicious", 0, 1),
    ("DV_wissend_r", "DV", "WalkingWB", "Suspicious", 0, 0),
]

def hexrgb(h):
    h = h.lstrip("#"); return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)

specs = []
FIGUREN = [f if len(f) == 7 else (*f, {}) for f in FIGUREN]
for name, per, pose, face, bust, _, ueb in FIGUREN:
    p = {**PERSONEN[per], **ueb}
    specs.append(dict(name=name, body=pose, face=face, hair=p["hair"], facialHair=p.get("facialHair", "None"),
                      accessory=p.get("accessory", "None"), bust=bool(bust), haut=HAUT[p["haut"]]))
json.dump(specs, open("op_hy/specs.json", "w"))
subprocess.run(["node", "teile.js", "op_hy/specs.json", "op_hy/raw"], check=True)

for name, per, pose, face, bust, spiegel, ueb in FIGUREN:
    p = {**PERSONEN[per], **ueb}
    h = H_BUST if bust else H_STAND
    kr = np.asarray(Image.open(io.BytesIO(cairosvg.svg2png(url=f"op_hy/raw/{name}_koerper.svg", output_height=h))).convert("RGBA")).astype(float)
    kopf = Image.open(io.BytesIO(cairosvg.svg2png(url=f"op_hy/raw/{name}_kopf.svg", output_height=h))).convert("RGBA")
    r, g, b, a = [kr[..., i] for i in range(4)]
    mag = (a > 200) & (r > 200) & (g < 60) & (b > 200)
    lab, nl = ndimage.label(mag)
    kl = KLASSEN[pose]
    farbe_von = {}
    for klasse, ids in kl.items():
        if klasse.startswith("_"): continue
        for i in ids: farbe_von[i] = klasse
    rest = kl.get("_rest")
    # Klasse je Label; nicht zugeordnete Flächen: _rest oder Klasse der nächstgelegenen zugeordneten Fläche
    klasse_arr = np.full(nl + 1, "", dtype=object)
    for i, k in farbe_von.items():
        if i <= nl: klasse_arr[i] = k
    zug = np.isin(lab, list(farbe_von.keys()))
    _, (iy, ix) = ndimage.distance_transform_edt(~zug, return_indices=True)
    for i in range(1, nl + 1):
        if klasse_arr[i]: continue
        if rest: klasse_arr[i] = rest; continue
        ys, xs = np.nonzero(lab == i)
        klasse_arr[i] = klasse_arr[lab[iy[ys[0], xs[0]], ix[ys[0], xs[0]]]] or "oben"
    # Kantenpixel (Magenta mit Tusche gemischt) dem nächsten Label zuordnen
    fl = (a > 0) & (r > g + 40)
    _, (jy, jx) = ndimage.distance_transform_edt(lab == 0, return_indices=True)
    nearest = lab[jy, jx]
    out = kr.copy()
    ink = np.array([17, 17, 17], float)
    anteil = np.clip((g * -1 + r - 17) / (255 - 17), 0, 1)  # Magenta-Anteil: R hoch, G niedrig
    for i in range(1, nl + 1):
        k = klasse_arr[i]
        farbname = p.get(k)
        if k == "haut": farbe = hexrgb(HAUT[p["haut"]])
        elif farbname: farbe = hexrgb(P[farbname])
        else: farbe = hexrgb(P["weiss"])
        m = fl & (nearest == i)
        t = anteil[m][:, None]
        out[m, :3] = t * farbe + (1 - t) * ink
    koerper = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")
    koerper.alpha_composite(kopf)
    koerper = koerper.crop(koerper.getbbox())
    if spiegel: koerper = ImageOps.mirror(koerper)
    koerper.save(f"op_hy/{name}.png")
print("fertig", len(FIGUREN))
