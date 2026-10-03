"""Folge 100 · Rücktritt vom Versuch § 24 StGB: Das Schema Schritt für Schritt – Serienstandard Open Peeps (Katzenkönig).
Fall (Plan-Hook): Heiner setzt an einem Dienstagnachmittag einen Hebel am Küchenfenster der Erdgeschosswohnung von
Annegret an (Fenster direkt am Gehweg), der Rahmen bekommt eine Delle; aus Gewissensbissen steckt er den Hebel ein und geht
nach Hause. Keine Gewalt gegen Personen; der Hebel ist nur stilisiert (programmatischer Baustein: Tuschelinie mit
gebogener Klaue, Palettenfarbe), kein Bruch, kein Eindringen.
Szenen laut ../SZENENPLAN.md: A Fall (Seitenstraße), B Sachverhalt, C Wortlaut § 24 Abs. 1, D Versuch I.–III. (kurz,
Verweis auf Folge 097), E IV. 1. kein Fehlschlag, F IV. 2. unbeendet/beendet, G IV. 3. Rücktrittshandlung,
H IV. 4. Freiwilligkeit, I § 24 Abs. 2 und Ergebnis, J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Geräusche: nur Handlungsgeräusche – Holz knarzt unter dem Hebel (szene_100hebel_1) und Schlüsselbund, als Annegret
heimkommt (szene_100schluessel_1) (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 097 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_100/"

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
DAUER = bausteine._cj()["dauer"]
T_ = bausteine._t

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=34, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf (Mindestgröße 26 px, mobile Lesbarkeit)."""
    assert size >= 26, f"Schrift zu klein: {text}"
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert k.get("size", 40) >= 26
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def blk(x, y, w, h, fill, cue, zeilen, **k):
    for t, s, g, f in zeilen:
        assert F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
    from engine import block as _block
    return _block(x, y, w, h, fill, None, cue, textsize=max(g for _, _, g, _ in zeilen), rund=k.pop("rund", 18), rand=INK,
                  randbreite=k.pop("rand", 5), anim=k.pop("anim", "rise"), zeilen=zeilen, **k)


def bis_(el, bis):
    el.bis = bis
    return el


def hart(e):
    """Harter Schnitt statt Einblendung."""
    e.anim = "cut"
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - T_(cue) + 0.5, 3))       # Lexi bleibt bis zum letzten Frame


def zit(text, x, y, cue, size=26, **k):
    """Fundstellenzeile (grau, 26 px)."""
    return z(text, x, y, cue, size=size, farbe=TEXT, **k)


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_100/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de, als Zitat mit Normangabe;
    marken = [(zeile, wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    for zi, wort, mc in marken:
        t = zeilen[zi]
        a = t.index(wort)
        x0 = tx + f.getlength(t[:a]) - 4
        x1 = tx + f.getlength(t[:a + len(wort)]) + 4
        y0 = ty + zi * lh + size * 0.30
        im = Image.new("RGBA", (int(x1 - x0) + 2, int(size * 0.85)))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 7, fill=MARKER)
        els.append(El(im, x0, y0, mc, "fade", 0.0, bis, name="marker:" + wort))
    for i, t in enumerate(zeilen):
        els.append(z(t, tx, ty + i * lh, cue, size=size, rechts=x + w - 16, bis=bis))
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", size - 4, farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 051/095) --------------------------------------
_W = _wave.open("../stimme.wav"); _SR = _W.getframerate()
_X = np.frombuffer(_W.readframes(_W.getnframes()), np.int16).astype(np.float32) / 32768
_W.close()


def _hoerbares_ende(a, b, schwelle=-38.0):
    h = int(0.01 * _SR); seg = _X[int(a * _SR):int(b * _SR)]; n = len(seg) // h
    if n == 0:
        return b
    db = 20 * np.log10(np.sqrt((seg[: n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
    laut = np.nonzero(db > schwelle)[0]
    return min(b, a + (laut[-1] + 1) * 0.01) if len(laut) else min(b, a + 0.1)


def redet(basis, cx, unten, hoehe, cue, bis, **k):
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt."""
    cj = bausteine._cj(); ta, tb = T_(cue), T_(bis)
    els = [peep_voll(basis, cx, unten, hoehe, cue, anim="cut", bis=bis, **k)]
    for s_ in cj["segmente"]:
        for w, (a, b) in zip(s_["text"].split(), s_["woerter"]):
            if a < ta - 0.01 or b > tb + 0.01:
                continue
            b = _hoerbares_ende(a, b)
            folge = bausteine.mundfolge(w)
            dauer = (b - a) * 0.88
            n = max(1, min(len(folge), int(dauer / 0.1)))
            folge = folge[:: max(1, len(folge) // n)][:n]
            for j, v in enumerate(folge):
                s0, s1 = a + dauer * j / n, a + dauer * (j + 1) / n
                els.append(peep_voll(f"{basis}_{v}", cx, unten, hoehe, (cue, round(s0 - ta, 3)), anim="cut",
                                     bis=(cue, round(s1 - ta, 3)), **k))
    return els


def fig(name, cx, unten, hoehe, folge, bis=None, erst="pop", d=0.0):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def ns(text, cx, unten, cue, fill, **k):
    """Namensschild unter der Figur (ab ihrem ersten Auftritt, solange sie im Bild ist)."""
    return pl(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


def hand_oben(name, cx, unten, hoehe, seite):
    """Äußerster Punkt des erhobenen Arms (Band 15–45 % der Höhe); seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.15):int(h * 0.45)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.15) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def strich(p0, p1, cue, farbe=INK, breite=5, luecke=16, bis=None):
    """Gestrichelte Flugbahn (programmatisch, ohne Mündungsfeuer)."""
    x0, y0 = min(p0[0], p1[0]) - 10, min(p0[1], p1[1]) - 10
    w, h = abs(p1[0] - p0[0]) + 20, abs(p1[1] - p0[1]) + 20
    s = 2
    im = Image.new("RGBA", (int(w * s), int(h * s)))
    dr = ImageDraw.Draw(im)
    L = math.hypot(p1[0] - p0[0], p1[1] - p0[1]); n = int(L // (luecke * 2))
    for k in range(n + 1):
        a = k * 2 * luecke / L; b = min(1.0, (k * 2 + 1) * luecke / L)
        xa, ya = p0[0] + (p1[0] - p0[0]) * a - x0, p0[1] + (p1[1] - p0[1]) * a - y0
        xb, yb = p0[0] + (p1[0] - p0[0]) * b - x0, p0[1] + (p1[1] - p0[1]) * b - y0
        dr.line([(xa * s, ya * s), (xb * s, yb * s)], fill=farbe, width=breite * s)
    im = im.resize((int(w), int(h)), Image.LANCZOS)
    return El(im, x0, y0, cue, "fade", 0.0, bis, name="flugbahn")


def punkt(cx, cy, r, cue, farbe=INK, bis=None):
    im = Image.new("RGBA", (2 * r + 2, 2 * r + 2))
    ImageDraw.Draw(im).ellipse((1, 1, 2 * r, 2 * r), fill=farbe)
    return El(im, cx - r, cy - r, cue, "cut", 0.0, bis, name="einschlag")



import math


def hand_vorn(name, cx, unten, hoehe, seite, band=(0.30, 0.55)):
    """Äußerster Punkt der ausgestreckten Hand (Band 30–55 % der Höhe); seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    b = a[int(h * band[0]):int(h * band[1])]
    ys, xs = np.nonzero(b)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * band[0]) + ys[i])


def hebel(p0, p1, cue, bis=None, breite=12, name="hebel"):
    """Stilisierter Hebel (Kuhfuß) als Baustein: gerader Stab mit kurzer gebogener Klaue am Ende p1, Tuschekontur,
    Füllung Palettenblau. Keine Gewaltdarstellung, kein Bruch."""
    s = 2
    x0, y0 = min(p0[0], p1[0]) - 40, min(p0[1], p1[1]) - 40
    w, h = abs(p1[0] - p0[0]) + 80, abs(p1[1] - p0[1]) + 80
    im = Image.new("RGBA", (int(w * s), int(h * s)))
    dr = ImageDraw.Draw(im)
    P = lambda p: ((p[0] - x0) * s, (p[1] - y0) * s)
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    klaue = [p1, (p1[0] + ux * 14 - uy * 10, p1[1] + uy * 14 + ux * 10), (p1[0] + ux * 6 - uy * 26, p1[1] + uy * 6 + ux * 26)]
    for farbe, br in ((INK, breite + 8), (BLAU, breite)):
        dr.line([P(p0), P(p1)], fill=farbe, width=br * s)
        dr.line([P(q) for q in klaue], fill=farbe, width=br * s, joint="curve")
        for q in (p0, klaue[-1]):
            r = br * s / 2
            dr.ellipse((P(q)[0] - r, P(q)[1] - r, P(q)[0] + r, P(q)[1] + r), fill=farbe)
    im = im.resize((int(w), int(h)), Image.LANCZOS)
    return El(im, x0, y0, cue, "cut", 0.0, bis, name=name)


def haus_flach(x0, y0, w, h, cue, fenster=(), tuer=None, bis=None):
    """Mehrfamilienhaus im Aufriss mit Flachdach (programmatisch): Wand mit Tuschekontur, Dachkante, Fenster mit
    Rahmen und Sprosse, Haustür. fenster/tuer relativ zur Wand."""
    s = 2
    im = Image.new("RGBA", ((w + 40) * s, (h + 40) * s))
    dr = ImageDraw.Draw(im)
    ox, oy = 20 * s, 30 * s
    dr.rectangle((ox, oy, ox + w * s, oy + h * s), fill=(250, 238, 222, 255), outline=INK, width=5 * s)
    dr.rectangle((ox - 14 * s, oy - 24 * s, ox + (w + 14) * s, oy), fill=ROT, outline=INK, width=5 * s)
    for fx, fy, fb, fh in fenster:
        dr.rectangle((ox + fx * s, oy + fy * s, ox + (fx + fb) * s, oy + (fy + fh) * s), fill=WEISS, outline=INK, width=6 * s)
        dr.rectangle((ox + (fx + 14) * s, oy + (fy + 14) * s, ox + (fx + fb - 14) * s, oy + (fy + fh - 14) * s), fill=BLAU,
                     outline=INK, width=4 * s)
        dr.line([(ox + (fx + fb / 2) * s, oy + (fy + 14) * s), (ox + (fx + fb / 2) * s, oy + (fy + fh - 14) * s)], fill=INK, width=4 * s)
        dr.rectangle((ox + (fx - 10) * s, oy + (fy + fh) * s, ox + (fx + fb + 10) * s, oy + (fy + fh + 12) * s), fill=WEISS,
                     outline=INK, width=4 * s)
    if tuer:
        tx, tb, th = tuer
        dr.rounded_rectangle((ox + tx * s, oy + (h - th) * s, ox + (tx + tb) * s, oy + h * s), 6 * s, fill=GELB, outline=INK, width=5 * s)
        dr.ellipse((ox + (tx + 18) * s, oy + (h - th / 2) * s, ox + (tx + 30) * s, oy + (h - th / 2 + 12) * s), fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0 - 20, y0 - 30, cue, "cut", 0.0, bis, name="haus")


def fenster_icon(cx, unten, b, h, cue, offen=False, bis=None):
    """Kleines Fenster als Requisit (programmatisch wie haus_flach): geschlossen oder einen Spalt geöffnet."""
    s = 2
    im = Image.new("RGBA", ((b + 20) * s, (h + 20) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((10 * s, 10 * s, (b + 10) * s, (h + 10) * s), fill=WEISS, outline=INK, width=5 * s)
    dr.rectangle((22 * s, 22 * s, (b - 2) * s, (h - 2) * s), fill=BLAU, outline=INK, width=4 * s)
    dr.line([((b / 2 + 10) * s, 22 * s), ((b / 2 + 10) * s, (h - 2) * s)], fill=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - im.width / 2, unten - im.height, cue, "pop", 0.0, bis, name="fenster")


NAME = {"HN": "Heiner", "AN": "Annegret"}
NFARBE = {"HN": GRUEN, "AN": BLAU}
X1, X2 = 1420, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
PX, PY, PU = 1570, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig


def requisit(folge, px=PX, py=PY, pu=PU):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell) | None, pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return els


def paar(c0, lf, rf):
    """Tafelszene: Heiner (links) und Annegret (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("HN", X1, FB, FR, lf), ns("Heiner", X1, FB, c0, NFARBE["HN"], d=0.1),
            *fig("AN", X2, FB, FR, rf, d=0.2), ns("Annegret", X2, FB, c0, NFARBE["AN"], d=0.3)]


# A Fall: die Seitenstraße ------------------------------------------------------------------------------------------------
BA, SH = 900, 500                           # Boden, Figurenhöhe im Fall
HW = (1040, 330, 820, 570)                  # Mehrfamilienhaus: x, y (Wandoberkante), Breite, Höhe
KF = (60, 250, 220, 180)                    # Küchenfenster (Erdgeschoss) relativ zur Wand
FENSTER = [(60, 50, 220, 150), (560, 50, 220, 150), KF]
TUER = (620, 140, 270)
KX0, KY0 = HW[0] + KF[0], HW[1] + KF[1]     # linke obere Ecke des Küchenfensters
H_X = 860                                   # Heiner am Fenster (blickt nach rechts)
_hx, _hy = hand_vorn("HN_angespannt_r", H_X, BA, SH, +1)
H_X += (KX0 + 4) - _hx                      # Hand genau an den linken Fensterrahmen
HAND = hand_vorn("HN_angespannt_r", H_X, BA, SH, +1)
HEBEL = ((HAND[0] - 70, HAND[1] + 40), (KX0 + 6, HAND[1] - 6))
DELLE = (KX0 + 2, HAND[1] - 6)
HEIM_X = 560                                # Heiner auf dem Heimweg (blickt nach links)
AN_X = 1480                                 # Annegret vor dem Haus (blickt nach links zum Küchenfenster)
folie([(NULL, "Fall · Die Seitenstraße"), ("hebel", "Fall · Der Hebel"), ("reue", "Fall · Die Gewissensbisse"),
       ("abends", "Fall · Am Abend"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(40, BA + 2), (1880, BA + 2)], NULL, breite=7, farbe=INK)),
    hart(bis_(pl("Dienstagnachmittag · ruhige Seitenstraße", 60, 30, NULL, fill=GELB, size=36), "abends")),
    hart(haus_flach(HW[0], HW[1], HW[2], HW[3], NULL, fenster=FENSTER, tuer=TUER)),
    # Heiner (blickt nach rechts zum Fenster)
    *fig("HN", H_X, BA, SH, [(NULL, "ruhig_r"), (beim("heiner", "braucht"), "denkt_r"), ("hebel", "angespannt_r")],
         bis="h1", erst="cut"),
    hart(ns("Heiner", H_X, BA, NULL, NFARBE["HN"], bis=beim("heim", "geht"))),
    pl("Mitte 40", H_X - 40, 300, beim("heiner", "Mitte"), fill=WEISS, size=28, anker="m", bis="wohnung"),
    pl("braucht dringend Geld", 60, 110, beim("heiner", "braucht"), fill=WEISS, size=30, bis="hebel"),
    ficon("tabler", "cash-banknote", 500, 158, 80, beim("heiner", "Geld"), fuell=GRUEN, bis="hebel"),
    # Die Wohnung von Annegret
    ring(HW[0] + 300, KY0 + 120, 330, 175, beim("wohnung", "Erdgeschosswohnung"), farbe=ROT, bis="gehweg"),
    pl("Erdgeschosswohnung von Annegret", KX0 + 380, HW[1] - 70, "annegret", fill=BLAU, size=30, anker="m", bis="abends"),
    pl("Spätschicht: niemand zu Hause", KX0 + 380, HW[1] - 140, beim("annegret", "Spätschicht"), fill=WEISS, size=30,
       anker="m", bis="hebel"),
    ficon("tabler", "clock", 1780, HW[1] - 96, 60, beim("annegret", "Spätschicht"), fuell=GELB, bis="hebel"),
    ring(KX0 + KF[2] / 2, KY0 + KF[3] / 2 + 6, 150, 120, beim("gehweg", "Küchenfenster"), farbe=ROT, bis="hebel"),
    pl("Küchenfenster direkt am Gehweg", 60, 185, beim("gehweg", "Küchenfenster"), fill=WEISS, size=30, bis="hebel"),
    # Der Hebel
    pl("will einbrechen und stehlen", 60, 110, "hebel", fill=PINK, size=30, bis="reue"),
    hebel(HEBEL[0], HEBEL[1], beim("hebel", "setzt"), bis=beim("heim", "ein")),
    pl("Hebel am Fensterrahmen", 60, 185, beim("hebel", "Hebel"), fill=WEISS, size=30, bis="delle"),
    szene(ring(DELLE[0], DELLE[1], 34, 34, "delle", farbe=ROT, bis="abends"), "100hebel*", 0.7, 0.0),
    pl("tiefe Delle im Rahmen", 60, 185, beim("delle", "tiefe"), fill=GELB, size=30, bis="heim"),
    # Heiner: Gewissensbisse
    *redet("HN_redet_r", H_X, BA, SH, "h1", "reue"),
    blase("sprech", 640, 210, "h1", 560, 330, inhalt=["Was mache ich hier", "eigentlich? Das ist", "nicht richtig."],
          textsize=36, figur=("HN_redet_r", H_X, BA, SH), bis="reue"),
    *fig("HN", H_X, BA, SH, [("reue", "reue_r")], bis=beim("heim", "geht"), erst="cut"),
    pl("Gewissensbisse", 60, 110, "reue", fill=LILA, size=30, bis="heim"),
    ficon("tabler", "heart", H_X - 40, 370, 80, "reue", fuell=ROT, bis="heim"),
    pl("niemand hat ihn bemerkt", 60, 185, "niemand", fill=WEISS, size=30, bis="heim"),
    pl("Fenster gleich offen", 60, 260, beim("niemand", "Fenster"), fill=WEISS, size=30, bis="heim"),
    # Heiner geht nach Hause
    *fig("HN", HEIM_X, BA, SH, [(beim("heim", "geht"), "ruhig")], bis="abends", erst="cut"),
    hart(ns("Heiner", HEIM_X, BA, beim("heim", "geht"), NFARBE["HN"], bis="abends")),
    pl("steckt den Hebel ein", 60, 110, "heim", fill=WEISS, size=30, bis="abends"),
    pl("geht nach Hause", 60, 185, beim("heim", "geht"), fill=GRUEN, size=30, bis="abends"),
    ficon("ph", "house", 170, 380, 110, beim("heim", "Hause"), fuell=GRUEN, bis="abends"),
    bis_(pfeil_ink(HEIM_X - 150, 330, 250, 330, beim("heim", "Hause")), "abends"),
    # Am Abend: Annegret kommt heim
    pl("Am Abend", 60, 30, "abends", fill=GELB, size=36),
    *fig("AN", AN_X, BA, SH, [("abends", "ruhig")], bis="a1", erst="pop"),
    ns("Annegret", AN_X, BA, "abends", NFARBE["AN"]),
    szene(ficon("ph", "key", AN_X - 120, 640, 60, "abends", fuell=GELB, bis="a1"), "100schluessel*", 0.6, 0.1),
    *redet("AN_redet", AN_X, BA, SH, "a1", "frage"),
    blase("sprech", 640, 210, "a1", 1240, 160, inhalt=["Was ist denn mit meinem", "Fensterrahmen passiert?"],
          textsize=34, figur=("AN_redet", AN_X, BA, SH), bis="frage"),
    *fig("AN", AN_X, BA, SH, [("frage", "genervt")], erst="cut"),
    ring(DELLE[0], DELLE[1], 34, 34, beim("a1", "Fensterrahmen"), farbe=ROT),
    # Frage
    pl("Ist Heiner strafbar?", 520, 300, "frage", fill=PINK, size=44, anker="m"),
    pl("Rücktritt vom Versuch, Schritt für Schritt", 520, 400, "frage2", fill=WEISS, size=32, anker="m"),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------
def sachverhalt_100(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_100("sv", [
    "Heiner (Mitte 40) braucht dringend Geld. An einem Dienstagnachmittag will er in die Erdgeschosswohnung von "
    "Annegret einbrechen und dort stehlen. Er weiß, dass Annegret dort wohnt und gerade in der Spätschicht arbeitet. "
    "Das Küchenfenster liegt direkt am Gehweg.",
    "Heiner setzt einen Hebel am Fensterrahmen an und drückt. Das Holz gibt nach, im Rahmen bleibt eine tiefe Delle. "
    "Das Fenster hätte er gleich aufgehebelt.",
    "Da bekommt Heiner Gewissensbisse. Niemand hat ihn bemerkt. Trotzdem steckt er den Hebel ein und geht nach Hause. "
    "Am Abend entdeckt Annegret die Delle.",
], "Ist Heiner strafbar?")

# C Wortlaut § 24 Abs. 1 -------------------------------------------------------------------------------------------------
W24 = ["„(1) Wegen Versuchs wird nicht bestraft, wer freiwillig die weitere",
       "Ausführung der Tat aufgibt oder deren Vollendung verhindert.",
       "Wird die Tat ohne Zutun des Zurücktretenden nicht vollendet,",
       "so wird er straflos, wenn er sich freiwillig und ernsthaft",
       "bemüht, die Vollendung zu verhindern.“"]
w24, w24_y = wortlaut(80, 180, 1100, W24, "§ 24 Abs. 1 StGB (Satz 1 und 2)", "p24", marken=[
    (0, "freiwillig", beim("p24w", "freiwillig")), (1, "Ausführung der Tat aufgibt", beim("p24w", "Ausführung")),
    (1, "Vollendung verhindert", beim("p24w", "Vollendung")), (3, "freiwillig und ernsthaft", beim("p24s2", "freiwillig"))])
folie([("p24", "Rücktritt › Wortlaut § 24 Abs. 1 StGB")], rechts_frei([
    *tafel("p24", "Der Rücktritt, § 24 StGB"),
    *w24,
    pl("Satz 1", 80, w24_y + 30, "p24w", fill=GELB, size=30),
    pl("Satz 2", 260, w24_y + 30, "p24s2", fill=GELB, size=30),
    *requisit([("p24", ("tabler", "arrow-back-up", 100, WEISS), "§ 24", WEISS),
               ("p24s2", ("tabler", "hand-stop", 100, WEISS), "ernsthaft bemühen", WEISS)]),
    *paar("p24", [("p24", "ernst"), ("p24s2", "denkt")], [("p24", "ruhig"), ("p24s2", "ernst")]),
]))

# D Versuch I.–III. (zwei Sätze) -----------------------------------------------------------------------------------------
VW = "Versuchter Wohnungseinbruchdiebstahl"
folie([("vers", f"{VW} › I.–III. Versuch (wie Folge 097)")], rechts_frei([
    *tafel("vers", "Zuerst der Versuch (Folge 097)"),
    *okz("Tatentschluss: einbrechen und stehlen", 195, beim("vers1", "einbrechen"), "Bold", 34, x=160),
    *okz("unmittelbares Ansetzen: Einbruchswerkzeug", 265, beim("vers1", "setzt"), "Bold", 34, x=160),
    z("schon angesetzt", 160, 315, beim("vers1", "angesetzt"), "Bold", 34),
    zit("BGH, Beschl. v. 28.4.2020 – 5 StR 15/20 (BGHSt 65, 15), Rn. 8", 160, 367, beim("vers1", "angesetzt")),
    *okz("rechtswidrig und schuldhaft", 435, "vers2", "Bold", 34, x=160),
    blk(110, 520, 1040, 130, GRUEN, beim("vers2", "versuchter"), [("versuchter Wohnungseinbruchdiebstahl", "ExtraBold", 36, INK),
                                                                   ("dauerhaft genutzte Privatwohnung", "ExtraBold", 36, INK)]),
    zit("§§ 242, 244 Abs. 1 Nr. 3, Abs. 4, 22, 23 Abs. 1 StGB", 110, 675, beim("vers2", "Paragraf")),
    *requisit([("vers", ("ph", "house", 110, WEISS), "bewohnte Wohnung", WEISS),
               (beim("vers1", "setzt"), ("tabler", "target", 100, ROT), "angesetzt", GELB),
               (beim("vers2", "versuchter"), ("tabler", "scale", 110, WEISS), "§ 244 Abs. 4", WEISS)]),
    *paar("vers", [("vers", "ernst"), (beim("vers1", "setzt"), "angespannt")], [("vers", "genervt"), ("vers2", "ernst")]),
]))

# E IV. 1. Kein fehlgeschlagener Versuch -----------------------------------------------------------------------------------
RT = f"{VW} › IV. Rücktritt"
folie([("rt", RT), ("rt1", f"{RT} › 1. kein fehlgeschlagener Versuch")], rechts_frei([
    *tafel("rt", "IV. Rücktritt, § 24 Abs. 1 StGB"),
    z("1. kein fehlgeschlagener Versuch", 110, 180, "rt1", "ExtraBold", 38),
    z("fehlgeschlagen, wenn die Tat mit eingesetzten oder", 110, 250, "rt1b", "Bold", 34),
    z("anderen naheliegenden Mitteln nicht mehr vollendbar", 110, 300, beim("rt1b", "anderen"), "Bold", 34),
    z("ist und der Täter das erkennt,", 110, 350, beim("rt1b", "erkennt"), "Bold", 34),
    z("oder er hält die Vollendung nicht mehr für möglich", 110, 405, beim("rt1b", "oder"), size=34),
    zit("BGH, Beschl. v. 27.4.2022 – 4 StR 408/21, Rn. 5", 110, 457, beim("rt1b", "möglich")),
    z("Folge 097: einzige Patrone verschossen", 110, 530, "rt1c", size=34),
    *okz("hier: Heiner hätte das Fenster gleich aufgehebelt", 605, beim("rt1c", "Heiner"), "Bold", 34, x=160),
    blk(110, 690, 1040, 90, GRUEN, beim("rt1c", "aufgehebelt"), [("nicht fehlgeschlagen", "ExtraBold", 38, INK)]),
    *requisit([("rt", ("tabler", "arrow-back-up", 100, WEISS), "Rücktritt?", WEISS),
               ("rt1c", ("tabler", "circle-x", 100, ROT), "Folge 097: Fehlschlag", WEISS),
               (beim("rt1c", "Heiner"), None, "gleich aufgehebelt", GELB)]),
    fenster_icon(PX, PU - 10, 130, 150, beim("rt1c", "Heiner")),
    *paar("rt", [("rt", "ernst"), (beim("rt1c", "Heiner"), "denkt")], [("rt", "ruhig"), ("rt1c", "ernst")]),
]))

# F IV. 2. Unbeendet oder beendet --------------------------------------------------------------------------------------------
HNd = ("HN_denkt", X1, FB, FR)
folie([("rt2", f"{RT} › 2. unbeendet oder beendet"), ("korr", f"{RT} › 2. Korrektur des Rücktrittshorizonts"),
       ("unb2", f"{RT} › 2. unbeendeter Versuch")], rechts_frei([
    *tafel("rt2", "IV. 2. Unbeendet oder beendet?"),
    z("maßgeblich: Vorstellung nach der letzten", 110, 180, "hor", "Bold", 34),
    z("Ausführungshandlung (Rücktrittshorizont)", 110, 228, beim("hor", "Ausführungshandlung"), "Bold", 34),
    blk(110, 290, 1040, 120, BLAU, "unb", [("unbeendet: noch nicht alles getan, was", "Bold", 32, INK),
                                          ("nach seiner Vorstellung nötig ist", "Bold", 32, INK)]),
    blk(110, 430, 1040, 120, LILA, "bee", [("beendet: hält den Erfolg für möglich oder", "Bold", 32, INK),
                                          ("macht sich darüber keine Gedanken", "Bold", 32, INK)]),
    zit("BGH, Beschl. v. 27.4.2022 – 4 StR 408/21, Rn. 5 f.", 110, 565, beim("bee", "Gedanken")),
    z("Korrektur: in engen zeitlichen Grenzen möglich", 110, 620, "korr", size=34),
    *okz("Fenster noch zu, nichts gestohlen", 690, "unb2", "Bold", 34, x=160),
    blk(110, 765, 1040, 90, GRUEN, beim("unb2", "Der"), [("unbeendeter Versuch", "ExtraBold", 38, INK)]),
    blase("denk", 330, 230, "unb2", 1500, 190, figur=HNd, bis=None),
    fenster_icon(1500, 255, 90, 100, beim("unb2", "Heiner")),
    *fig("HN", X1, FB, FR, [("rt2", "ernst"), ("hor", "denkt")]), ns("Heiner", X1, FB, "rt2", NFARBE["HN"], d=0.1),
    *fig("AN", X2, FB, FR, [("rt2", "ruhig"), ("unb2", "ernst")], d=0.2), ns("Annegret", X2, FB, "rt2", NFARBE["AN"], d=0.3),
    pl("Rücktrittshorizont", PX, PY, "hor", fill=WEISS, size=28, anker="m", bis="unb2"),
    ficon("tabler", "eye", PX, PU - 40, 90, "hor", fuell=WEISS, bis="unb2"),
]))

# G IV. 3. Rücktrittshandlung --------------------------------------------------------------------------------------------
folie([("rh", f"{RT} › 3. Rücktrittshandlung")], rechts_frei([
    *tafel("rh", "IV. 3. Rücktrittshandlung"),
    blk(110, 180, 1040, 80, BLAU, "rh1", [("unbeendet: weitere Ausführung aufgeben", "Bold", 34, INK)]),
    zit("§ 24 Abs. 1 S. 1 Alt. 1 StGB", 130, 272, beim("rh1", "Satz")),
    blk(110, 330, 1040, 80, LILA, "rh2", [("beendet: Vollendung verhindern", "Bold", 34, INK)]),
    zit("§ 24 Abs. 1 S. 1 Alt. 2 StGB", 130, 422, beim("rh2", "zweite")),
    z("ohne sein Zutun nicht vollendet: freiwilliges", 110, 480, "rh3", size=34),
    z("und ernsthaftes Bemühen genügt", 110, 528, beim("rh3", "freiwilliges"), size=34),
    zit("§ 24 Abs. 1 S. 2 StGB", 130, 580, beim("rh3", "Bemühen")),
    *okz("Heiner steckt den Hebel ein und geht nach Hause", 650, "rh4", "Bold", 34, x=160),
    blk(110, 725, 1040, 90, GRUEN, beim("rh4", "Er"), [("Tat aufgegeben", "ExtraBold", 38, INK)]),
    *requisit([("rh", ("tabler", "hand-stop", 100, WEISS), "Rücktrittshandlung", WEISS),
               ("rh4", ("ph", "house", 110, GRUEN), "nach Hause", GRUEN)]),
    *paar("rh", [("rh", "ernst"), ("rh4", "erleichtert")], [("rh", "ruhig"), ("rh2", "ernst")]),
]))

# H IV. 4. Freiwilligkeit ------------------------------------------------------------------------------------------------
folie([("fw", f"{RT} › 4. Freiwilligkeit")], rechts_frei([
    *tafel("fw", "IV. 4. Freiwilligkeit"),
    z("Herr seiner Entschlüsse, hält die Tat", 110, 180, "fw1", "Bold", 34),
    z("noch für ausführbar", 110, 228, beim("fw1", "ausführbar"), "Bold", 34),
    zit("BGH, Beschl. v. 14.1.2020 – 2 StR 284/19, Rn. 8", 110, 280, beim("fw1", "ausführbar")),
    blk(110, 335, 510, 120, GRUEN, "fw2", [("autonom: aus dem", "Bold", 32, INK), ("Täter selbst", "Bold", 32, INK)]),
    blk(640, 335, 510, 120, PINK, "fw3", [("heteronom: zwingendes", "Bold", 32, INK), ("Hindernis von außen", "Bold", 32, INK)]),
    zit("Begriffe: Klausurstandard; Hindernis: BGH ebd.", 110, 470, beim("fw3", "zwingend")),
    z("sittlich billigenswertes Motiv nicht nötig", 110, 530, "fw4", size=34),
    zit("BGH ebd. Rn. 9", 110, 580, beim("fw4", "Bundesgerichtshof")),
    *okz("Gewissensbisse, niemand stört ihn", 650, "fw5", "Bold", 34, x=160),
    blk(110, 725, 1040, 90, GRUEN, beim("fw5", "Er"), [("freiwillig zurückgetreten", "ExtraBold", 38, INK)]),
    *requisit([("fw", ("tabler", "brain", 100, WEISS), "Freiwilligkeit", WEISS),
               ("fw2", ("tabler", "heart", 100, ROT), "autonom", GRUEN),
               ("fw3", ("tabler", "barrier-block", 100, WEISS), "heteronom", PINK),
               ("fw5", ("tabler", "heart", 100, ROT), "Gewissensbisse", LILA)]),
    *paar("fw", [("fw", "ernst"), ("fw5", "reue")], [("fw", "ruhig"), ("fw4", "ernst")]),
]))

# I § 24 Abs. 2 und Ergebnis -------------------------------------------------------------------------------------------
folie([("zwei", "§ 24 Abs. 2 StGB · mehrere Beteiligte"), ("erg", "Ergebnis")], rechts_frei([
    *tafel("zwei", "Mehrere Beteiligte · Ergebnis"),
    z("mehrere Beteiligte: Vollendung verhindern", 110, 190, "zwei", "Bold", 34),
    zit("§ 24 Abs. 2 S. 1 StGB", 110, 242, beim("zwei", "Absatz")),
    blk(110, 330, 1040, 130, GRUEN, "erg", [("versuchter Wohnungseinbruchdiebstahl:", "ExtraBold", 36, INK),
                                           ("straflos (Rücktritt)", "ExtraBold", 36, INK)]),
    blk(110, 500, 1040, 130, PINK, "erg2", [("strafbar bleibt er wegen der Delle", "ExtraBold", 36, INK),
                                            ("im Fensterrahmen", "ExtraBold", 36, INK)]),
    *requisit([("zwei", ("tabler", "users", 100, WEISS), "mehrere Beteiligte", WEISS),
               ("erg", ("tabler", "gavel", 100, WEISS), "straflos", GRUEN),
               ("erg2", None, "Delle im Rahmen", GELB)]),
    fenster_icon(PX, PU - 10, 130, 150, "erg2"),
    ring(PX - 52, PU - 95, 30, 30, "erg2", farbe=ROT),
    *paar("zwei", [("zwei", "ernst"), ("erg", "erleichtert"), ("erg2", "muede")], [("zwei", "ruhig"), ("erg2", "genervt")]),
]))

# J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Rücktritt erfasst nur den Versuch")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, beim("tipp", "Rücktritt"), gr=26),
    z("Rücktritt: persönlicher Strafaufhebungsgrund", 200, 200, beim("tipp", "Rücktritt"), "Bold", 36),
    zit("BGH, Urt. v. 17.3.2022 – 4 StR 223/21, Rn. 21", 200, 255, beim("tipp", "Strafaufhebungsgrund")),
    z("erfasst nur den Versuch", 200, 310, beim("tipp", "erfasst"), "Bold", 36),
    z("vollendete Delikte bleiben strafbar", 110, 400, "tipp2", size=36),
    zit("BGH, Urt. v. 14.2.1996 – 3 StR 445/95 (BGHSt 42, 43), Rn. 7", 110, 455, beim("tipp2", "strafbar")),
    blk(110, 520, 1040, 130, BLAU, "tipp3", [("Delle: vollendete Sachbeschädigung,", "ExtraBold", 36, INK),
                                            ("§ 303 Abs. 1 StGB", "ExtraBold", 36, INK)]),
    z("gesondert prüfen", 110, 690, beim("tipp3", "Prüfe"), "Bold", 36),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema -------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Rücktritt vom Versuch, § 24 Abs. 1 StGB"), 110, 90, "sch", 44),
    z("0.–III. Vorprüfung, Tatbestand, Rechtswidrigkeit, Schuld: wie beim Versuch", K1, 195, "s0", size=38, rechts=1820),
    z("IV. Rücktritt, § 24 Abs. 1 StGB", K1, 290, "s4", "Bold", 40, rechts=1820),
    z("1. kein fehlgeschlagener Versuch", K2, 360, "s41", size=38, rechts=1820),
    z("2. unbeendet oder beendet (Rücktrittshorizont)", K2, 425, "s42", size=38, rechts=1820),
    z("3. Rücktrittshandlung", K2, 490, "s43", size=38, rechts=1820),
    z("unbeendet: Aufgeben", K2 + 70, 550, "s43a", size=36, rechts=1820),
    z("beendet: Verhindern oder ernsthaftes Bemühen", K2 + 70, 605, "s43b", size=36, rechts=1820),
    z("4. Freiwilligkeit", K2, 675, "s44", size=38, rechts=1820),
])

# L Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Zurücktreten kann nur, wessen Versuch", 0)], [("nicht ", 0), ("fehlgeschlagen", "a"), (" ist.", 0)]],
                750, 290, 44, "merke", {"a": beim("merke", "fehlgeschlagen")}),
    *markertext([[("Unbeendet: ", 0), ("aufgeben", "b"), (".", 0)], [("Beendet: Vollendung verhindern.", 0)]],
                750, 480, 44, "m2", {"b": beim("m2", "Aufgeben")}),
    *markertext([[("Was schon vollendet ist,", 0)], [("bleibt ", 0), ("strafbar", "c"), (".", 0)]],
                750, 670, 44, "m3", {"c": beim("m3", "strafbar")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
