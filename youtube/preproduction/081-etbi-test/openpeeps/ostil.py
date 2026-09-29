"""Open-Peeps-Stil (mehrfarbig): Tusche-Konturen, Pastellflächen, Nunito, Blasen aus MingCute/Phosphor."""
import json, io, math
import engine
from engine import *
import cairosvg

SP = "../../"
NUN = SP + "humaaans/fonts/Nunito[wght].ttf"
engine.FONTMAP = {"Light": (NUN, 300), "Regular": (NUN, 500), "Medium": (NUN, 600), "Bold": (NUN, 800), "ExtraBold": (NUN, 900)}

INK = (21, 21, 21, 255)
TEXT = (55, 55, 60, 255)
CREME = (255, 248, 236, 255)
WEISS = (255, 255, 255, 255)
GELB = (249, 213, 110, 255)
PINK = (246, 165, 192, 255)
GRUEN = (143, 214, 148, 255)
BLAU = (141, 179, 242, 255)
LILA = (184, 169, 245, 255)
TUERKIS = (127, 214, 208, 255)
ORANGE = (249, 166, 108, 255)
ROT = (240, 122, 106, 255)
DGRUEN = (40, 150, 85, 255)
DROT = (215, 60, 45, 255)
MARKER = (249, 213, 110, 255)


def OT(text, x, y, cue, stil="Regular", size=46, farbe=INK, **k):
    return T(text, x, y, cue, stil, size, farbe=farbe, **k)


def _ink_rahmen(maske, breite):
    """Tuschekontur um eine Maske (L, 2x-Auflösung)."""
    return maske.filter(ImageFilter.MaxFilter(breite * 2 + 1))


def titel(text, x, y, cue, size=76, anker="l", d=0.0, marker=MARKER):
    """Überschrift mit Textmarker hinter der unteren Hälfte (wie der gelbe Schein im Open-Peeps-Logo)."""
    f = F("ExtraBold", size)
    b = f.getbbox(text)
    w, h = b[2] - b[0] + 40, b[3] - b[1] + 30
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((6, int(h * 0.48), w - 6, h - 6), 10, fill=marker)
    dr.text((20 - b[0], 12 - b[1]), text, font=f, fill=INK)
    if anker == "m": x -= w / 2
    assert x >= 10 and x + w <= engine.W - 10, f"Titel zu breit: {text}"
    return El(im, x, y - 12, cue, "rise", d, name="titel:" + text)


def karte(x, y, w, h, cue, fill=WEISS, rund=26, schatten=10, rand=5, anim="fade", d=0.0, schattenfarbe=INK):
    s = 2
    im = Image.new("RGBA", ((w + schatten + 20) * s, (h + schatten + 20) * s))
    dr = ImageDraw.Draw(im)
    o = 10 * s
    dr.rounded_rectangle((o + schatten * s, o + schatten * s, o + (w + schatten) * s, o + (h + schatten) * s), rund * s, fill=schattenfarbe)
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=INK)
    dr.rounded_rectangle((o + rand * s, o + rand * s, o + (w - rand) * s, o + (h - rand) * s), max(1, rund - rand) * s, fill=fill)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x - 10, y - 10, cue, anim, d, name="karte")


def pille(text, x, y, cue, fill=GELB, size=40, stil="Bold", anker="l", d=0.0, farbe=INK, anim="pop", pad=(30, 14)):
    f = F(stil, size)
    b = f.getbbox(text)
    tw, th = b[2] - b[0], b[3] - b[1]
    w, h = tw + 2 * pad[0], int(size * 1.05) + 2 * pad[1]
    s = 2
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((5 * s, 5 * s, (w + 5) * s, (h + 5) * s), h * s // 2, fill=INK)
    dr.rounded_rectangle((0, 0, w * s, h * s), h * s // 2, fill=INK)
    dr.rounded_rectangle((4 * s, 4 * s, (w - 4) * s, (h - 4) * s), (h // 2 - 4) * s, fill=fill)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    ImageDraw.Draw(im).text((pad[0] - b[0], (h - th) / 2 - b[1]), text, font=f, fill=farbe)
    if anker == "m": x -= w / 2
    elif anker == "r": x -= w
    assert x >= 10 and x + w + 8 <= engine.W - 10, f"Pille ragt aus dem Bild: {text}"
    return El(im, x, y, cue, anim, d, name="pille:" + text)


def fl_block(x, y, w, h, fill, cue, zeilen, rund=18, anim="rise", d=0.0, bis=None, rand=5):
    """Pastellblock mit Tuschekontur; zeilen = [(text, stil, size, farbe)]."""
    return block(x, y, w, h, fill, None, cue, rund=rund, rand=INK, randbreite=rand, anim=anim, d=d, bis=bis, zeilen=zeilen)


def haken(cx, cy, cue, gr=46, farbe=DGRUEN, d=0.0):
    s = 3
    im = Image.new("RGBA", (gr * 2 * s, gr * 2 * s))
    dr = ImageDraw.Draw(im)
    pts = [(0.18, 0.55), (0.42, 0.78), (0.85, 0.2)]
    dr.line([(px * gr * 2 * s, py * gr * 2 * s) for px, py in pts], fill=farbe, width=int(gr * 0.32 * s), joint="curve")
    for px, py in (pts[0], pts[-1]):
        r = gr * 0.16 * s
        dr.ellipse((px * gr * 2 * s - r, py * gr * 2 * s - r, px * gr * 2 * s + r, py * gr * 2 * s + r), fill=farbe)
    im = im.resize((gr * 2, gr * 2), Image.LANCZOS)
    return El(im, cx - gr, cy - gr, cue, "pop", d, name="haken")


def kreuz(cx, cy, cue, gr=40, farbe=DROT, d=0.0):
    s = 3
    im = Image.new("RGBA", (gr * 2 * s, gr * 2 * s))
    dr = ImageDraw.Draw(im)
    a, b = 0.2 * gr * 2 * s, 0.8 * gr * 2 * s
    for p in (((a, a), (b, b)), ((b, a), (a, b))):
        dr.line(p, fill=farbe, width=int(gr * 0.3 * s))
        for q in p:
            r = gr * 0.15 * s
            dr.ellipse((q[0] - r, q[1] - r, q[0] + r, q[1] + r), fill=farbe)
    im = im.resize((gr * 2, gr * 2), Image.LANCZOS)
    return El(im, cx - gr, cy - gr, cue, "pop", d, name="kreuz")


def warnung(cx, cy, cue, gr=40, d=0.0):
    s = 3
    W_ = int(gr * 2.2)
    im = Image.new("RGBA", (W_ * s, W_ * s))
    dr = ImageDraw.Draw(im)
    tri = [(W_ / 2 * s, 4 * s), ((W_ - 4) * s, (W_ - 6) * s), (4 * s, (W_ - 6) * s)]
    dr.polygon(tri, fill=INK)
    inn = [(W_ / 2 * s, 16 * s), ((W_ - 15) * s, (W_ - 12) * s), (15 * s, (W_ - 12) * s)]
    dr.polygon(inn, fill=GELB)
    f = F("ExtraBold", int(gr * 1.1 * s))
    bb = f.getbbox("!")
    dr.text((W_ / 2 * s - (bb[2] - bb[0]) / 2 - bb[0], W_ * 0.62 * s - (bb[3] - bb[1]) / 2 - bb[1]), "!", font=f, fill=INK)
    im = im.resize((W_, W_), Image.LANCZOS)
    return El(im, cx - W_ / 2, cy - W_ / 2, cue, "pop", d, name="warnung")


# --- Blasen: Formen aus MingCute (thought-fill, Apache 2.0) und Phosphor (chat-circle-fill, MIT) -------------
_ic = {}
def _form(set_, name, w, h):
    if set_ not in _ic:
        _ic[set_] = json.load(open(SP + f"blasen/{set_}/package/icons.json"))
    d = _ic[set_]
    ic = d["icons"][name]
    vw = ic.get("width", d.get("width", 24)); vh = ic.get("height", d.get("height", 24))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}" preserveAspectRatio="none" width="{w}" height="{h}">'
           + ic["body"].replace("currentColor", "#000") + "</svg>")
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=w, output_height=h)
    return Image.open(io.BytesIO(png)).getchannel("A")


def blase(art, w, h, cue, cx, cy, inhalt=None, bild_=None, bildhoehe=None, spiegeln=False, textsize=44, d=0.0, bis=None,
          stil="Bold", ziel=None):
    """art = 'denk' | 'sprech'. Weiße Fläche + Tuschekontur.
    denk: Wolkenform aus MingCute (nur Hauptwolke) + eigene Gedankenpunkte Richtung ziel (Kopf, absolute Koordinaten).
    sprech: Phosphor chat-circle mit Schwanz unten links (spiegeln = unten rechts)."""
    from scipy import ndimage
    s = 2
    rand = 7
    pad = 150 if ziel else rand + 6
    maske = _form("mingcute", "thought-fill", w * s, h * s) if art == "denk" else _form("ph", "chat-circle-fill", w * s, h * s)
    if spiegeln:
        maske = maske.transpose(Image.FLIP_LEFT_RIGHT)
    arr = np.asarray(maske) > 128
    if art == "denk":
        lab, n = ndimage.label(arr)
        arr = lab == (1 + int(np.argmax(ndimage.sum(arr, lab, range(1, n + 1)))))
        ys, xs = np.nonzero(arr)
        arr = arr[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    haupt = Image.fromarray((arr * 255).astype(np.uint8)).resize((w * s, h * s), Image.LANCZOS)
    big = Image.new("L", (haupt.width + 2 * pad * s, haupt.height + 2 * pad * s))
    big.paste(haupt, (pad * s, pad * s))
    ox_abs, oy_abs = cx - big.width / (2 * s), cy - big.height / (2 * s)   # Canvas-Ursprung im Bild
    ys, xs = np.nonzero(np.asarray(big) > 128)
    ccx, ccy = xs.mean() / s, ys.mean() / s                                   # Wolkenschwerpunkt (lokal, 1x)
    if ziel:
        zx, zy = ziel[0] - ox_abs, ziel[1] - oy_abs
        dx, dy = zx - ccx, zy - ccy
        ln = math.hypot(dx, dy); ux, uy = dx / ln, dy / ln
        barr = np.asarray(big) > 128
        t = 0.0
        while True:  # Austrittspunkt am Wolkenrand
            px, py = int((ccx + ux * t) * s), int((ccy + uy * t) * s)
            if not (0 <= px < barr.shape[1] and 0 <= py < barr.shape[0]) or not barr[py, px]:
                break
            t += 2
        rest = max(40.0, ln - t - 28)
        md = ImageDraw.Draw(big)
        for frac, rr in ((0.28, 17), (0.62, 12), (0.92, 7)):
            q = t + rest * frac
            px, py = (ccx + ux * q) * s, (ccy + uy * q) * s
            md.ellipse((px - rr * s, py - rr * s, px + rr * s, py + rr * s), fill=255)
    kontur = big.filter(ImageFilter.MaxFilter(rand * 2 * s + 1))
    im = Image.new("RGBA", big.size)
    im.paste(Image.new("RGBA", big.size, INK), (0, 0), kontur)
    im.paste(Image.new("RGBA", big.size, WEISS), (0, 0), big)
    im = im.resize((big.width // s, big.height // s), Image.LANCZOS)
    hy0, hy1 = pad, pad + haupt.height / s
    hx0, hx1 = pad, pad + haupt.width / s
    if art == "sprech":
        hy1 = hy0 + (hy1 - hy0) * 0.88
    icx, icy = ccx, (ccy if art == "denk" else (hy0 + hy1) / 2)
    iw, ih = (hx1 - hx0) * 0.70, (hy1 - hy0) * 0.66
    dr = ImageDraw.Draw(im)
    zeilen = inhalt if isinstance(inhalt, list) else ([inhalt] if inhalt else [])
    f = F(stil, textsize); lh = int(textsize * 1.15)
    bh = 0
    fig = None
    if bild_:
        fig = Image.open(bild_).convert("RGBA")
        bhh = bildhoehe or int(ih * (0.62 if zeilen else 0.95))
        fig = fig.resize((int(fig.width * bhh / fig.height), bhh), Image.LANCZOS)
        bh = bhh + (6 if zeilen else 0)
    block_h = bh + len(zeilen) * lh
    assert block_h <= ih * 1.25, f"Blaseninhalt zu hoch: {block_h:.0f} > {ih:.0f}"
    y0 = icy - block_h / 2
    if fig is not None:
        im.alpha_composite(fig, (int(icx - fig.width / 2), int(y0)))
        y0 += bh
    for z in zeilen:
        bb = f.getbbox(z)
        assert bb[2] - bb[0] <= iw * 1.1, f"Blasentext zu breit: {z} ({bb[2]-bb[0]} > {iw:.0f})"
        dr.text((icx - (bb[2] - bb[0]) / 2 - bb[0], y0 + (lh - (bb[3] - bb[1])) / 2 - bb[1]), z, font=f, fill=INK)
        y0 += lh
    return El(im, ox_abs, oy_abs, cue, "pop", d, bis, name=f"blase:{art}:" + "/".join(zeilen))


def peep(name, cx, unten, hoehe, cue, anim="pop", d=0.0, bis=None):
    return bild(SP + f"peeps/op/{name}.png", cx, unten, hoehe, cue, anim=anim, d=d, bis=bis)


def mimik(namen_cues, cx, unten, hoehe, erst_anim="pop", d=0.0):
    """Wechselnde Gesichter/Posen einer Figur am selben Platz: [(bild, cue), ...]; Wechsel als harter Schnitt."""
    els = []
    for i, (n, c) in enumerate(namen_cues):
        bis = namen_cues[i + 1][1] if i + 1 < len(namen_cues) else None
        els.append(peep(n, cx, unten, hoehe, c, anim=(erst_anim if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=bis))
    return els


def markertext(zeilen_tokens, cx, y, size, cue, hl_cues, marker=PINK, lh=1.3, d=0.0):
    """Zentrierter Mehrzeilentext (Tusche). Hervorgehobene Wörter bekommen zur Marke einen Textmarker;
    das Overlay zeichnet Marker + dieselben Wörter an identischer Stelle (kein Geistertext)."""
    fr, fb = F("Regular", size), F("ExtraBold", size)
    lines = []
    maxw = 0
    for toks in zeilen_tokens:
        wid = sum((fb if h else fr).getlength(t) for t, h in toks)
        maxw = max(maxw, wid); lines.append((toks, wid))
    assert maxw <= engine.W - 200, f"Markertext zu breit: {maxw}"
    hgt = int(len(lines) * size * lh + size * 0.5)
    im = Image.new("RGBA", (int(maxw) + 40, hgt))
    ov = {}
    dr = ImageDraw.Draw(im)
    yy = 0
    for toks, wid in lines:
        xx = 20 + (maxw - wid) / 2
        for t, h in toks:
            f = fb if h else fr
            tw = f.getlength(t)
            if h:
                if h not in ov: ov[h] = Image.new("RGBA", im.size)
                od = ImageDraw.Draw(ov[h])
                od.rounded_rectangle((xx - 6, yy + size * 0.45, xx + tw + 6, yy + size * 1.12), 8, fill=marker)
                od.text((xx, yy), t, font=f, fill=INK)
            dr.text((xx, yy), t, font=f, fill=INK)
            xx += tw
        yy += size * lh
    x0 = cx - im.width / 2
    els = [El(im, x0, y, cue, "rise", d, name="markertext")]
    for key, oim in ov.items():
        els.append(El(oim, x0, y, hl_cues[key], "fade", 0.0, name="marker:" + key))
    return els


# --- gezeichnete Requisiten -----------------------------------------------------------------------------
def mond(cx, cy, r, cue, d=0.0):
    s = 3
    R = (r + 8) * s
    im = Image.new("RGBA", (2 * R, 2 * R))
    m = Image.new("L", im.size, 0); md = ImageDraw.Draw(m)
    md.ellipse((R - r * s, R - r * s, R + r * s, R + r * s), fill=255)
    md.ellipse((R - r * s + r * 0.55 * s, R - r * s - r * 0.25 * s, R + r * s + r * 0.55 * s, R + r * s - r * 0.25 * s), fill=0)
    k = m.filter(ImageFilter.MaxFilter(2 * 5 * s + 1))
    im.paste(Image.new("RGBA", im.size, INK), (0, 0), k)
    im.paste(Image.new("RGBA", im.size, GELB), (0, 0), m)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - im.width / 2, cy - im.height / 2, cue, "pop", d, name="mond")


def laterne(x, boden, hoehe, cue, d=0.0):
    """Straßenlaterne: Mast bei x, Kopf ragt nach links. Gibt (Element, Kopfposition) zurück."""
    s = 2
    W_, H_ = 260, hoehe + 20
    im = Image.new("RGBA", (W_ * s, H_ * s))
    dr = ImageDraw.Draw(im)
    mx = (W_ - 40) * s
    dr.rounded_rectangle((mx - 9 * s, 60 * s, mx + 9 * s, H_ * s), 6 * s, fill=INK)
    dr.rounded_rectangle((mx - 30 * s, (H_ - 22) * s, mx + 30 * s, H_ * s), 6 * s, fill=INK)
    dr.arc((40 * s, 40 * s, mx + 9 * s, 180 * s), 180, 270, fill=INK, width=14 * s)
    dr.line((110 * s, 40 * s, mx, 40 * s), fill=INK, width=14 * s)
    dr.arc((mx - 60 * s, 40 * s, mx + 9 * s, 110 * s), 270, 360, fill=INK, width=14 * s)
    dr.polygon([(12 * s, 150 * s), (108 * s, 150 * s), (86 * s, 104 * s), (34 * s, 104 * s)], fill=INK)
    dr.polygon([(22 * s, 144 * s), (98 * s, 144 * s), (80 * s, 110 * s), (40 * s, 110 * s)], fill=GELB)
    im = im.resize((W_, H_), Image.LANCZOS)
    ox, oy = x - (W_ - 40), boden - H_
    return El(im, ox, oy, cue, "fade", d, name="laterne"), (ox + 60, oy + 150)


def lichtkegel(kx, ky, breite, boden, cue, d=0.0):
    im = Image.new("RGBA", (int(breite * 2), int(boden - ky)))
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).polygon([(breite - 45, 0), (breite + 45, 0), (breite * 2, im.height), (0, im.height)], fill=90)
    m = m.filter(ImageFilter.GaussianBlur(10))
    lay = Image.new("RGBA", im.size, GELB); lay.putalpha(m)
    return El(lay, kx - breite, ky, cue, "fade", d, name="licht")


def schild(text, x, y, cue, d=0.0):
    f = F("ExtraBold", 38)
    b = f.getbbox(text)
    w, h = b[2] - b[0] + 50, 70
    s = 2
    im = Image.new("RGBA", (w * s, (h + 60) * s))
    dr = ImageDraw.Draw(im)
    for xx in (w * 0.25, w * 0.75):
        dr.line((xx * s, 0, xx * s, 60 * s), fill=INK, width=6 * s)
    dr.rounded_rectangle((0, 60 * s, w * s, (60 + h) * s), 12 * s, fill=INK)
    dr.rounded_rectangle((5 * s, 65 * s, (w - 5) * s, (55 + h) * s), 9 * s, fill=(70, 110, 200, 255))
    im = im.resize((w, h + 60), Image.LANCZOS)
    ImageDraw.Draw(im).text((25 - b[0], 60 + (h - (b[3] - b[1])) / 2 - b[1]), text, font=f, fill=WEISS)
    return El(im, x - w / 2, y, cue, "pop", d, name="schild")


def boden(y, cue, x0=60, x1=1860):
    return linienzug([(x0, y), (x1, y)], cue, breite=7, farbe=INK)


def pfeil_ink(x1, y1, x2, y2, cue, d=0.0):
    return pfeil(x1, y1, x2, y2, cue, breite=10, kopf=32, farbe=INK, d=d)


def ring(cx, cy, rx, ry, cue, farbe=ORANGE, breite=8, d=0.0, bis=None):
    """Handgezeichnete Hervorhebung (Ellipse)."""
    s = 3
    im = Image.new("RGBA", ((2 * rx + 20) * s, (2 * ry + 20) * s))
    ImageDraw.Draw(im).ellipse((10 * s, 10 * s, (2 * rx + 10) * s, (2 * ry + 10) * s), outline=farbe, width=breite * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - rx - 10, cy - ry - 10, cue, "pop", d, bis, name="ring")
