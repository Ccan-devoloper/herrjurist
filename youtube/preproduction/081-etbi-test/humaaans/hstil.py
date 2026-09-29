"""Humaaans-Stil: Farben, Schrift (DM Sans), Karten, Kreise, Rauten, Pillen, Figuren."""
import engine
from engine import *

HF = "../../humaaans/"
engine.FONTMAP = {
    "Light": (HF + "fonts/DMSans[opsz,wght].ttf", 300),
    "Regular": (HF + "fonts/DMSans[opsz,wght].ttf", 400),
    "Medium": (HF + "fonts/DMSans[opsz,wght].ttf", 500),
    "Bold": (HF + "fonts/DMSans[opsz,wght].ttf", 700),
    "ExtraBold": (HF + "fonts/DMSans[opsz,wght].ttf", 800),
}

NAVY = (31, 29, 91, 255)
TEXT = (61, 65, 102, 255)
BLAU = (47, 60, 244, 255)
TIEF = (35, 39, 168, 255)
ORANGE = (255, 154, 31, 255)
ROT = (240, 72, 52, 255)
GRUEN = (38, 166, 120, 255)
CYAN = (213, 241, 244, 255)
TEAL = (140, 200, 207, 255)
GELBKREIS = (238, 231, 182, 255)
LAVENDEL = (202, 205, 248, 255)
PFIRSICH = (255, 227, 200, 255)
MINT = (189, 231, 221, 255)
ROSA = (246, 214, 230, 255)
ZELLE = (238, 241, 255, 255)
GELB = (255, 210, 90, 255)
WEISS = (255, 255, 255, 255)


def HT(text, x, y, cue, stil="Regular", size=48, farbe=NAVY, **k):
    return T(text, x, y, cue, stil, size, farbe=farbe, **k)


def karte(x, y, w, h, cue, fill=WEISS, rund=34, keil=None, anim="fade", d=0.0):
    """Weiße Web-Karte mit weichem Schatten; keil = (x_oben, x_unten, farbe) färbt die rechte Seite schräg ein."""
    s = 2
    pad = 40
    im = Image.new("RGBA", ((w + 2 * pad) * s, (h + 2 * pad) * s))
    maske = Image.new("L", im.size, 0)
    ImageDraw.Draw(maske).rounded_rectangle((pad * s, pad * s, (pad + w) * s, (pad + h) * s), rund * s, fill=255)
    sh = maske.filter(ImageFilter.GaussianBlur(22 * s)).point(lambda v: int(v * 0.16))
    schatten = Image.new("RGBA", im.size, (31, 29, 91, 0)); schatten.putalpha(sh)
    im.alpha_composite(schatten, (0, 12 * s))
    flaeche = Image.new("RGBA", im.size, fill)
    if keil:
        xo, xu, farbe = keil
        ImageDraw.Draw(flaeche).polygon([((pad + xo) * s, 0), (im.width, 0), (im.width, im.height), ((pad + xu) * s, im.height)], fill=farbe)
    im.paste(flaeche, (0, 0), maske)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x - pad, y - pad, cue, anim, d, name="karte")


def kreis(cx, cy, r, farbe, cue, anim="pop", d=0.0, bis=None):
    s = 3
    im = Image.new("RGBA", (2 * r * s, 2 * r * s))
    ImageDraw.Draw(im).ellipse((0, 0, 2 * r * s - 1, 2 * r * s - 1), fill=farbe)
    im = im.resize((2 * r, 2 * r), Image.LANCZOS)
    return El(im, cx - r, cy - r, cue, anim, d, bis, name="kreis")


def raute(cx, cy, a, farbe, cue, d=0.0):
    s = 3
    im = Image.new("RGBA", (2 * a * s, 2 * a * s))
    ImageDraw.Draw(im).polygon([(a * s, 0), (2 * a * s, a * s), (a * s, 2 * a * s), (0, a * s)], fill=farbe)
    im = im.resize((2 * a, 2 * a), Image.LANCZOS)
    return El(im, cx - a, cy - a, cue, "pop", d, name="raute")


def pille(text, x, y, cue, fill=BLAU, farbe=WEISS, size=40, stil="Bold", anker="l", d=0.0, pad=(34, 16), anim="pop",
          rahmen=None):
    """Button wie auf humaaans.com; y = Oberkante."""
    f = F(stil, size)
    b = f.getbbox(text)
    tw, th = b[2] - b[0], b[3] - b[1]
    w, h = tw + 2 * pad[0], int(size * 1.0) + 2 * pad[1]
    s = 2
    im = Image.new("RGBA", (w * s, h * s))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, w * s - 1, h * s - 1), 10 * s, fill=fill,
                                         outline=rahmen, width=(3 * s if rahmen else 0))
    im = im.resize((w, h), Image.LANCZOS)
    ImageDraw.Draw(im).text((pad[0] - b[0], (h - th) / 2 - b[1]), text, font=f, fill=farbe)
    if anker == "m": x -= w / 2
    elif anker == "r": x -= w
    assert x >= 20 and x + w <= engine.W - 20, f"Pille ragt aus dem Bild: {text}"
    return El(im, x, y, cue, anim, d, name="pille:" + text)


def fig(name, cx, unten, hoehe, cue, anim="pop", d=0.0, bis=None, oben=1.0):
    return bild(HF + "fig/" + name + ".png", cx, unten, hoehe, cue, anim=anim, d=d, bis=bis, oben=oben)


def hwolke(w, h, inhalt, cue, cx, cy, **k):
    k.setdefault("textsize", 44)
    return wolke(w, h, inhalt, cue, cx, cy, kontur=None, textfarbe=NAVY, schatten=True, **k)


def status(text, x, y, cue, plus, size=48, d=0.0):
    """(+)/(-) als farbiges Wort hinter einer Schemazeile."""
    return HT(text, x, y, cue, "ExtraBold", size, farbe=(BLAU if plus else ROT), d=d)


def zeile(text, x, y, cue, st=None, st_cue=None, plus=True, size=48, stil="Regular", d=0.0, farbe=NAVY):
    els = [HT(text, x, y, cue, stil, size, farbe=farbe, d=d)]
    if st:
        els.append(status(st, x + F(stil, size).getlength(text + " "), y, st_cue or cue, plus, size))
    return els


def ok(x, y, cue, size=58, d=0.0):
    return E("check-mark-button", x, y, size, cue, d=d)


def nein(x, y, cue, size=58, d=0.0):
    return E("cross-mark", x, y, size, cue, d=d)
