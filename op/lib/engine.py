"""Gemeinsame Engine der Open-Peeps-Videos (aus 081-etbi-test/openpeeps-v3 übernommen, 01.10.2026; Assets unter preproduction/blasen, humaaans/fonts, peeps).

Kleine Folien-Engine: Papierhintergrund, Text, Emoji (Fluent Emoji Flat), Denkwolken, Pfeile, Blöcke.

Jedes Element wird einmal als RGBA-Sprite gerendert und erscheint zu seiner Wortmarke mit einer
kurzen Animation (rise = Einblenden von unten, pop = federndes Skalieren, fade = Überblenden).
"""
import json, io, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import cairosvg

W, H = 1920, 1080
FD = "../fonts/"
INK = (30, 30, 30, 255)
GRAU = (95, 95, 95, 255)
PFADGRAU = (140, 140, 136, 255)
GELB = (247, 192, 69, 255)
WEISS = (250, 250, 248, 255)
ROT = (200, 57, 42, 255)
GRUEN = (46, 140, 80, 255)

_fc = {}
FONTMAP = None  # {stil: (pfad, gewicht)} für variable Schriften, z. B. DM Sans im Humaaans-Stil

def F(stil, size):
    key = (stil, size, id(FONTMAP))
    if key not in _fc:
        if FONTMAP:
            pfad, gew = FONTMAP[stil]
            f = ImageFont.truetype(pfad, size)
            werte = []
            for a in f.get_variation_axes():
                werte.append(min(max(size, a["minimum"]), a["maximum"]) if a["name"] == b"Optical size" else gew)
            f.set_variation_by_axes(werte)
            _fc[key] = f
        else:
            _fc[key] = ImageFont.truetype(FD + f"AlegreyaSans-{stil}.ttf", size)
    return _fc[key]

# ---------------------------------------------------------------- Hintergründe
def papier(dunkel=False, seed=7):
    rng = np.random.default_rng(seed)
    def rausch(sigma, amp):
        n = rng.standard_normal((H // 2, W // 2)).astype(np.float32)
        im = Image.fromarray(((n - n.min()) / (n.max() - n.min()) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(sigma))
        a = np.asarray(im.resize((W, H), Image.BICUBIC), np.float32) / 255 - 0.5
        return a * amp
    hoehe = rausch(1.2, 1.0) + rausch(3, 1.6) + rausch(9, 1.2)
    # Putzrelief: Licht von links oben
    gx = np.gradient(hoehe, axis=1); gy = np.gradient(hoehe, axis=0)
    relief = (-(gx + gy)) * 90
    feinkorn = rausch(0.6, 10)
    basis = 42 if dunkel else 234
    img = basis + relief + feinkorn + rausch(40, 10)
    y = np.linspace(-1, 1, H)[:, None]; x = np.linspace(-1, 1, W)[None, :]
    img -= (x ** 2 + y ** 2) * (4 if dunkel else 7)  # leichte Vignette
    img = np.clip(img, 0, 255)
    rgb = np.stack([img, img * 1.0, img * (0.985 if not dunkel else 1.0)], -1)
    return Image.fromarray(rgb.astype(np.uint8)).convert("RGBA")

# ---------------------------------------------------------------- Emoji
# Pfad relativ zu dieser Datei (preproduction/blasen/…), unabhängig vom Arbeitsordner des Videos
import os as _os
_ej = None
def emoji_img(name, size):
    global _ej
    if _ej is None:
        _ej = json.load(open(_os.path.join(_os.environ["OP_RES"], "blasen/fluent-emoji-flat/package/icons.json")))
    ic = _ej["icons"].get(name)
    if ic is None:
        al = _ej.get("aliases", {}).get(name)
        assert al, f"Emoji fehlt: {name}"
        ic = _ej["icons"][al["parent"]]
    w = ic.get("width", _ej.get("width", 32)); h = ic.get("height", _ej.get("height", 32))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{ic["body"]}</svg>'
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")

# ---------------------------------------------------------------- Element
class El:
    def __init__(self, sprite, x, y, cue, anim="rise", d=0.0, bis=None, name=None):
        self.sprite, self.x, self.y = sprite, int(round(x)), int(round(y))
        self.cue, self.anim, self.d, self.bis = cue, anim, d, bis
        self.name = name

def _leer(w, h):
    return Image.new("RGBA", (max(1, int(w)), max(1, int(h))))

ERSATZ = None  # (pfad, {stil: gewicht}) Ersatzschrift für Zeichen, die der Hauptschrift fehlen (z. B. "→" in Nunito)
_fe = {}
def _ersatz(stil, size):
    key = (stil, size)
    if key not in _fe:
        pfad, gew = ERSATZ
        f = ImageFont.truetype(pfad, size)
        f.set_variation_by_axes([min(max(size, a["minimum"]), a["maximum"]) if a["name"] == b"Optical size" else gew[stil]
                                 for a in f.get_variation_axes()])
        _fe[key] = f
    return _fe[key]

def text_sprite(text, stil="Regular", size=60, farbe=INK, schatten=False):
    f = F(stil, size)
    if ERSATZ and "→" in text:
        import re as _re
        teile = [t for t in _re.split("(→)", text) if t]
        b = f.getbbox(text.replace("→", "M"))
        breite = sum((_ersatz(stil, size) if t == "→" else f).getlength(t) for t in teile)
        im = _leer(breite + 8, b[3] - b[1] + 12)
        dr = ImageDraw.Draw(im)
        x = 4 - b[0]
        for t in teile:
            ff = _ersatz(stil, size) if t == "→" else f
            dr.text((x, 4 - b[1]), t, font=ff, fill=farbe)
            x += ff.getlength(t)
        return im, (b[0], b[1], b[0] + breite, b[3])
    b = f.getbbox(text)
    im = _leer(b[2] - b[0] + 8, b[3] - b[1] + 12)
    ImageDraw.Draw(im).text((4 - b[0], 4 - b[1]), text, font=f, fill=farbe)
    return im, b

def T(text, x, y, cue, stil="Regular", size=60, farbe=INK, anker="l", anim="rise", d=0.0, bis=None, maxw=None):
    """Textzeile; y = Oberkante der Versalhöhe; anker l/m/r bezogen auf x."""
    im, b = text_sprite(text, stil, size, farbe)
    if maxw is not None:
        assert im.width <= maxw, f"Text zu breit ({im.width}>{maxw}): {text}"
    assert im.width <= W - 40, f"Text zu breit für Bild: {text}"
    if anker == "m": x = x - im.width / 2
    elif anker == "r": x = x - im.width
    return El(im, x - 4, y - 4, cue, anim, d, bis, name=text)

def E(name, cx, cy, size, cue, anim="pop", d=0.0, bis=None):
    im = emoji_img(name, size)
    return El(im, cx - size / 2, cy - size / 2, cue, anim, d, bis, name=name)

def kreis_emoji(name, cx, cy, r, cue, d=0.0):
    s = 3
    im = _leer(2 * r * s, 2 * r * s)
    ImageDraw.Draw(im).ellipse((0, 0, 2 * r * s - 1, 2 * r * s - 1), fill=WEISS)
    im = im.resize((2 * r, 2 * r), Image.LANCZOS)
    e = emoji_img(name, int(r * 1.25))
    im.alpha_composite(e, (r - e.width // 2, r - e.height // 2))
    return El(im, cx - r, cy - r, cue, "pop", d, name="kreis:" + name)

def wolke(w, h, inhalt, cue, cx, cy, schwanz=None, d=0.0, textsize=46, emoji=None, emoji_size=90, ziel=None, bis=None,
          kontur=INK, textfarbe=INK, fuellung=WEISS, schatten=False):
    """Denkwolke mit dunkler Kontur (wie Referenz). schwanz = (dx, dy) Richtung zur denkenden Figur;
    ziel = (x, y) absoluter Bildpunkt (Kopf), zu dem die Gedankenblasen führen."""
    s = 2
    pad = 190 if ziel else 60
    CW, CH = (w + 2 * pad) * s, (h + 2 * pad + (0 if ziel else 160)) * s
    mask = Image.new("L", (CW, CH), 0)
    md = ImageDraw.Draw(mask)
    ox, oy = pad * s, pad * s
    md.ellipse((ox + w * 0.08 * s, oy + h * 0.12 * s, ox + w * 0.92 * s, oy + h * 0.88 * s), fill=255)
    n = 11
    for k in range(n):
        a = 2 * math.pi * k / n + 0.2
        px = ox + (w / 2 + math.cos(a) * w * 0.40) * s
        py = oy + (h / 2 + math.sin(a) * h * 0.36) * s
        r = (min(w, h) * (0.22 + 0.05 * math.sin(3 * k))) * s
        md.ellipse((px - r, py - r, px + r, py + r), fill=255)
    kreise = []
    if schwanz:
        dx, dy = schwanz
        bx, by = ox + w / 2 * s + dx * s * 0.10, oy + h * 1.0 * s
        for j, rr in enumerate((22, 15, 9)):
            cxk = bx + dx * s * (0.10 + 0.13 * j); cyk = by + (30 + 38 * j) * s
            kreise.append((cxk, cyk, rr * s))
            md.ellipse((cxk - rr * s, cyk - rr * s, cxk + rr * s, cyk + rr * s), fill=255)
    if ziel:
        ux, uy = ziel[0] - cx, ziel[1] - cy
        ln = math.hypot(ux, uy); ux, uy = ux / ln, uy / ln
        # Austrittspunkt am Wolkenrand, dann drei kleiner werdende Blasen Richtung Kopf
        ex, ey = w / 2 + ux * w * 0.47, h / 2 + uy * h * 0.47
        for dist, rr in ((34, 22), (78, 15), (112, 9)):
            px, py = ox + (ex + ux * dist) * s, oy + (ey + uy * dist) * s
            md.ellipse((px - rr * s, py - rr * s, px + rr * s, py + rr * s), fill=255)
    rand = mask.filter(ImageFilter.MaxFilter(11))
    im = Image.new("RGBA", (CW, CH))
    if schatten:
        sh = mask.filter(ImageFilter.GaussianBlur(18 * s)).point(lambda v: int(v * 0.22))
        schicht = Image.new("RGBA", (CW, CH), (31, 29, 91, 0)); schicht.putalpha(sh)
        im.alpha_composite(schicht, (0, 10 * s))
    if kontur:
        im.paste(Image.new("RGBA", (CW, CH), kontur), (0, 0), rand)
    im.paste(Image.new("RGBA", (CW, CH), fuellung), (0, 0), mask)
    im = im.resize((CW // s, CH // s), Image.LANCZOS)
    dr = ImageDraw.Draw(im)
    zeilen = inhalt if isinstance(inhalt, list) else [inhalt]
    f = F("Regular", textsize)
    lh = int(textsize * 1.18)
    block = len(zeilen) * lh + (emoji_size + 10 if emoji else 0)
    y0 = pad + h / 2 - block / 2
    if emoji:
        e = emoji_img(emoji, emoji_size)
        im.alpha_composite(e, (int(pad + w / 2 - emoji_size / 2), int(y0)))
        y0 += emoji_size + 10
    for z in zeilen:
        bb = f.getbbox(z)
        assert bb[2] - bb[0] <= w * 0.86, f"Wolkentext zu breit: {z}"
        dr.text((pad + w / 2 - (bb[2] - bb[0]) / 2 - bb[0], y0 - bb[1] + (lh - (bb[3] - bb[1])) / 2), z, font=f, fill=textfarbe)
        y0 += lh
    return El(im, cx - pad - w / 2, cy - pad - h / 2, cue, "pop", d, bis, name="wolke:" + "/".join(zeilen))

def pfeil(x1, y1, x2, y2, cue, breite=12, kopf=34, farbe=INK, d=0.0, anim="fade", bis=None):
    s = 3
    minx, miny = min(x1, x2) - kopf - 4, min(y1, y2) - kopf - 4
    maxx, maxy = max(x1, x2) + kopf + 4, max(y1, y2) + kopf + 4
    im = _leer((maxx - minx) * s, (maxy - miny) * s)
    dr = ImageDraw.Draw(im)
    a = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - math.cos(a) * kopf * 0.9, y2 - math.sin(a) * kopf * 0.9
    P = lambda x, y: ((x - minx) * s, (y - miny) * s)
    if kopf:
        dr.line([P(x1, y1), P(ex, ey)], fill=farbe, width=breite * s)
        l, r = a + 2.6, a - 2.6
        dr.polygon([P(x2, y2), P(x2 + math.cos(l) * kopf, y2 + math.sin(l) * kopf), P(x2 + math.cos(r) * kopf, y2 + math.sin(r) * kopf)], fill=farbe)
    else:
        dr.line([P(x1, y1), P(x2, y2)], fill=farbe, width=breite * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, minx, miny, cue, anim, d, bis, name="pfeil")

def linienzug(punkte, cue, breite=10, farbe=INK, d=0.0):
    s = 3
    xs = [p[0] for p in punkte]; ys = [p[1] for p in punkte]
    minx, miny = min(xs) - breite, min(ys) - breite
    im = _leer((max(xs) - minx + breite) * s, (max(ys) - miny + breite) * s)
    dr = ImageDraw.Draw(im)
    dr.line([((x - minx) * s, (y - miny) * s) for x, y in punkte], fill=farbe, width=breite * s, joint="curve")
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, minx, miny, cue, "fade", d, name="linie")

def block(x, y, w, h, fill, text, cue, textsize=64, textfarbe=WEISS, stil="Regular", anim="rise", d=0.0, bis=None,
          rund=0, rand=None, randbreite=0, zeilen=None):
    s = 2
    im = _leer(w * s, h * s)
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((0, 0, w * s - 1, h * s - 1), rund * s, fill=fill, outline=rand, width=randbreite * s)
    im = im.resize((w, h), Image.LANCZOS)
    dr = ImageDraw.Draw(im)
    ls = zeilen if zeilen is not None else ([text] if text else [])
    f = F(stil, textsize)
    lh = int(textsize * 1.15)
    y0 = h / 2 - len(ls) * lh / 2
    for z in ls:
        if isinstance(z, tuple):
            z, zst, zsz, zf = z
            ff = F(zst, zsz)
        else:
            ff, zf = f, textfarbe
        bb = ff.getbbox(z)
        assert bb[2] - bb[0] <= w - 24, f"Blocktext zu breit: {z}"
        dr.text((w / 2 - (bb[2] - bb[0]) / 2 - bb[0], y0 + (lh - (bb[3] - bb[1])) / 2 - bb[1]), z, font=ff, fill=zf)
        y0 += lh
    return El(im, x, y, cue, anim, d, bis, name="block:" + (text or "/".join(str(z) for z in ls)))

def richtext(zeilen_tokens, cx, y, size, cue, hl_cues, farbe=WEISS, hl=GELB, lh=1.22, d=0.0):
    """Zentrierter Mehrzeilentext; Tokens (text, hervorheben?). Hervorgehobene Wörter sind fett
    und bekommen zu ihrer Marke eine gelbe Einfärbung an exakt derselben Stelle (kein Geistertext)."""
    fr, fb = F("Regular", size), F("Bold", size)
    basis, overlays = [], {}
    maxw = 0
    lines = []
    for toks in zeilen_tokens:
        wid = sum(fb.getlength(t) if h else fr.getlength(t) for t, h in toks)
        maxw = max(maxw, wid); lines.append((toks, wid))
    assert maxw <= W - 160, f"Richtext zu breit: {maxw}"
    hgt = int(len(lines) * size * lh + size * 0.4)
    im = _leer(maxw + 20, hgt)
    ov = {}
    dr = ImageDraw.Draw(im)
    yy = 0
    for toks, wid in lines:
        xx = 10 + (maxw - wid) / 2
        for t, h in toks:
            f = fb if h else fr
            dr.text((xx, yy), t, font=f, fill=farbe)
            if h:
                if h not in ov: ov[h] = _leer(im.width, im.height)
                ImageDraw.Draw(ov[h]).text((xx, yy), t, font=f, fill=hl)
            xx += f.getlength(t)
        yy += size * lh
    x0 = cx - im.width / 2
    els = [El(im, x0, y, cue, "rise", d, name="richtext")]
    for key, oim in ov.items():
        els.append(El(oim, x0, y, hl_cues[key], "fade", 0.0, name="hl:" + key))
    return els


_bc = {}
def bild(pfad, cx, unten, hoehe, cue, anim="pop", d=0.0, bis=None, oben=1.0):
    """Freigestellte PNG-Figur, unten mittig auf (cx, unten) gestellt. oben < 1 = nur oberer Anteil (Brustbild)."""
    if (pfad, oben) not in _bc:
        im = Image.open(pfad).convert("RGBA")
        if oben < 1:
            im = im.crop((0, 0, im.width, int(im.height * oben)))
            im = im.crop(im.getbbox())
        _bc[(pfad, oben)] = im
    im = _bc[(pfad, oben)]
    im = im.resize((int(im.width * hoehe / im.height), hoehe), Image.LANCZOS)
    return El(im, cx - im.width / 2, unten - hoehe, cue, anim, d, bis, name="bild:" + pfad.split("/")[-1])
