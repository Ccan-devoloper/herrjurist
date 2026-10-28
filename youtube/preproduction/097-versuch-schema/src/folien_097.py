"""Folge 097 · Versuch Schema: Vorprüfung, Tatentschluss, unmittelbares Ansetzen – Serienstandard Open Peeps (Katzenkönig).
Fall (Plan-Hook): Herbert schießt nach einem Streit um das Auto vor seiner Garage auf seinen Nachbarn Gregor und verfehlt
ihn um Zentimeter; niemand wird verletzt. Gewalt zurückhaltend: Pistole nur als stilisiertes Linien-Icon (Fluent Emoji
High Contrast, weiß gefüllt), kein Mündungsfeuer, kein Blut, die Flugbahn nur als gestrichelte Linie mit Einschlag in der
Hauswand.
Szenen laut ../SZENENPLAN.md: A Fall (Wohnstraße), B Sachverhalt, C Wortlaut §§ 22, 23 Abs. 1 und Aufbau, D 0. Vorprüfung,
E I.1 Tatentschluss, F I.2 unmittelbares Ansetzen, G II. Rechtswidrigkeit, III. Schuld, H IV. Rücktritt, I Ergebnis,
J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Geräusche: nur Handlungsgeräusche – Haustür fällt zu (szene_097tuer_1) und Schlüssel im Schloss (szene_097schloss_1), als
Gregor in sein Haus rennt und abschließt (../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 095 (gemeinsame Dateien unverändert). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_097/"

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
        if n.startswith(("bild:", "ficon:")) or "/op_097/" in n:
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


def pistole(cx, unten, breite, cue, spiegeln=False, bis=None, anim="pop"):
    """Stilisierte Pistole: Linien-Icon (Fluent Emoji High Contrast „water-pistol“), weiß gefüllt, ohne Mündungsfeuer."""
    return ficon("fluent-emoji-high-contrast", "water-pistol", cx, unten, breite, cue, fuell=WEISS, spiegeln=spiegeln,
                 bis=bis, anim=anim)


def haus(x0, y0, w, h, cue, dach=ROT, wand=WEISS, tuer=None, fenster=(), bis=None, name="haus"):
    """Hausfront im Aufriss (programmatisch wie Tür/Fliesenwand in 095): Wand mit Tuschekontur, Satteldach, Tür, Fenster.
    tuer = (x, Breite, Höhe) relativ zur Wand; fenster = [(x, y, b, h)] relativ zur Wand. Dachhöhe 0,3 · Breite."""
    s = 2
    dh = int(w * 0.30)
    im = Image.new("RGBA", ((w + 40) * s, (h + dh + 12) * s))
    dr = ImageDraw.Draw(im)
    ox, oy = 20 * s, (dh + 6) * s
    dr.rectangle((ox, oy, ox + w * s, oy + h * s), fill=wand, outline=INK, width=5 * s)
    dr.polygon([(ox - 16 * s, oy), (ox + w * s / 2, 6 * s), (ox + (w + 16) * s, oy)], fill=dach, outline=INK)
    dr.line([(ox - 16 * s, oy), (ox + w * s / 2, 6 * s), (ox + (w + 16) * s, oy), (ox - 16 * s, oy)], fill=INK, width=5 * s,
            joint="curve")
    if tuer:
        tx, tb, th = tuer
        dr.rounded_rectangle((ox + tx * s, oy + (h - th) * s, ox + (tx + tb) * s, oy + h * s), 6 * s, fill=GELB, outline=INK,
                             width=5 * s)
        dr.ellipse((ox + (tx + tb - 26) * s, oy + (h - th / 2) * s, ox + (tx + tb - 14) * s, oy + (h - th / 2 + 12) * s), fill=INK)
    for fx, fy, fb, fh in fenster:
        dr.rectangle((ox + fx * s, oy + fy * s, ox + (fx + fb) * s, oy + (fy + fh) * s), fill=BLAU, outline=INK, width=5 * s)
        dr.line([(ox + (fx + fb / 2) * s, oy + fy * s), (ox + (fx + fb / 2) * s, oy + (fy + fh) * s)], fill=INK, width=4 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0 - 20, y0 - dh - 6, cue, "cut", 0.0, bis, name=name)


def garage(x0, y0, w, h, cue):
    """Garage mit Sektionaltor (programmatisch: Rahmen, waagerechte Torfugen)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((6 * s, 6 * s, (w + 6) * s, (h + 6) * s), fill=WEISS, outline=INK, width=5 * s)
    dr.rectangle((30 * s, 40 * s, (w - 18) * s, (h + 6) * s), fill=(236, 236, 240, 255), outline=INK, width=4 * s)
    for k in range(1, 5):
        y = 40 + k * (h - 34) / 5
        dr.line([(30 * s, y * s), ((w - 18) * s, y * s)], fill=INK, width=3 * s)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, x0 - 6, y0 - 6, cue, "cut", 0.0, None, name="garage")


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
NAME = {"HE": "Herbert", "GR": "Gregor"}
NFARBE = {"HE": BLAU, "GR": GRUEN}
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
    """Tafelszene: Herbert (links) und Gregor (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("HE", X1, FB, FR, lf), ns("Herbert", X1, FB, c0, NFARBE["HE"], d=0.1),
            *fig("GR", X2, FB, FR, rf, d=0.2), ns("Gregor", X2, FB, c0, NFARBE["GR"], d=0.3)]


# A Fall: die Wohnstraße -------------------------------------------------------------------------------------------------
BA, SH = 900, 500                           # Boden, Figurenhöhe im Fall
HX, GX, GTX = 860, 1530, 1745               # Herbert, Gregor vor seiner Hauswand, Gregor an der Haustür
HW = (60, 420, 330, 480)                    # Haus von Herbert: x, y (Wandoberkante), Breite, Höhe
GW = (1420, 300, 440, 600)                  # Haus von Gregor
GT = (285, 120, 210)                        # Tür von Gregor relativ zur Wand
G_HAND = hand_oben("HE_entschlossen_r", HX, BA, SH, +1)
MUENDUNG = (G_HAND[0] + 70, G_HAND[1] - 16)
EIN = (1632, 338)                            # Einschlag in der Hauswand, knapp über Gregors Kopf
STREIT = beim("gregor", "streiten")
DRUECKT = beim("schuss", "drückt")
SCHLIESST = beim("flieht", "schließt")
GR_TUER = beim("flieht", "rennt")
folie([(NULL, "Fall · Die Wohnstraße"), ("holt", "Fall · Die Pistole"), ("schuss", "Fall · Der Schuss"),
       ("frage", "Fall · Die Frage")], [
    hart(linienzug([(40, BA + 2), (1880, BA + 2)], NULL, breite=7, farbe=INK)),
    hart(pl("Samstagabend · ruhige Wohnstraße", 60, 30, NULL, fill=GELB, size=36)),
    hart(haus(HW[0], HW[1], HW[2], HW[3], NULL, dach=LILA, tuer=(190, 105, 200), fenster=[(40, 70, 100, 90), (190, 70, 100, 90)])),
    hart(garage(410, 660, 290, 240, NULL)),
    hart(haus(GW[0], GW[1], GW[2], GW[3], NULL, dach=ROT, tuer=GT, fenster=[(50, 80, 120, 110), (250, 80, 120, 110),
                                                                            (50, 280, 120, 110)])),
    hart(ficon("ph", "car-profile", 560, BA + 4, 300, NULL, fuell=BLAU)),
    pl("Garage von Herbert", 555, 600, beim("auto", "Garage"), fill=WEISS, size=28, anker="m", bis="holt"),
    ring(560, 845, 175, 70, beim("auto", "parkt"), farbe=ROT, bis="holt"),
    pl("streiten seit Monaten", 60, 110, STREIT, fill=WEISS, size=30, bis="holt"),
    pl("Auto von Gregor parkt vor der Garage", 60, 185, beim("auto", "parkt"), fill=PINK, size=30, bis="h1"),
    # Herbert (blickt nach rechts zu Gregor)
    *fig("HE", HX, BA, SH, [(NULL, "ruhig_r"), (beim("auto", "Immer"), "wuetend_r")], bis="h1", erst="cut"),
    *redet("HE_redet_r", HX, BA, SH, "h1", "holt"),
    hart(ns("Herbert", HX, BA, NULL, NFARBE["HE"], bis="holt")),
    pl("Anfang 60", HX, 300, beim("herbert", "Anfang"), fill=WEISS, size=28, anker="m", bis="h1"),
    blase("sprech", 640, 200, "h1", 600, 250, inhalt=["Fahr endlich", "dein Auto weg!"], textsize=36,
          figur=("HE_redet_r", HX, BA, SH), bis="holt"),
    # Herbert geht ins Haus und holt die Pistole
    pl("geht ins Haus, holt eine alte Pistole", 60, 110, beim("holt", "geht"), fill=WEISS, size=30, bis="zurueck"),
    ring(HW[0] + 242, BA - 100, 80, 125, beim("holt", "Haus"), farbe=ROT, bis="zurueck"),
    pistole(560, 330, 120, beim("holt", "Pistole"), spiegeln=True, bis="zurueck"),
    pl("1 einzige Patrone", 560, 380, "patrone", fill=GELB, size=30, anker="m", bis="schuss"),
    # Herbert kommt zurück und zielt
    *fig("HE", HX, BA, SH, [("zurueck", "entschlossen_r")], bis="h2", erst="cut"),
    hart(ns("Herbert", HX, BA, "zurueck", NFARBE["HE"])),
    hart(pistole(G_HAND[0] + 22, G_HAND[1] + 26, 84, "zurueck", spiegeln=True)),
    linienzug([(HX + 110, BA - 40), (GX - 110, BA - 40)], beim("zurueck", "fünf"), breite=5, farbe=INK),
    pl("5 m", (HX + GX) / 2, BA - 100, beim("zurueck", "fünf"), fill=WEISS, size=30, anker="m"),
    pl("zielt auf Gregor", HX + 40, 240, beim("zurueck", "zielt"), fill=WEISS, size=30, anker="m", bis="g1"),
    # Gregor vor seiner Hauswand (blickt nach links zu Herbert)
    *fig("GR", GX, BA, SH, [(NULL, "ruhig"), (beim("auto", "parkt"), "genervt"), ("h1", "genervt"),
                           ("zurueck", "angst")], bis="g1", erst="cut"),
    *redet("GR_redet", GX, BA, SH, "g1", "schuss"),
    *fig("GR", GX, BA, SH, [("schuss", "angst")], bis=GR_TUER, erst="cut"),
    hart(ns("Gregor", GX, BA, NULL, NFARBE["GR"], bis=GR_TUER)),
    blase("sprech", 700, 200, "g1", 1110, 210, inhalt=["Herbert, leg die", "Pistole weg!"], textsize=36,
          figur=("GR_redet", GX, BA, SH), bis="schuss"),
    # Der Schuss: Flugbahn knapp über den Kopf, Einschlag in der Hauswand
    pl("will Gregor töten", HX + 40, 240, beim("schuss", "töten"), fill=PINK, size=30, anker="m", bis="h2"),
    strich(MUENDUNG, EIN, DRUECKT),
    punkt(EIN[0], EIN[1], 9, DRUECKT),
    ring(EIN[0], EIN[1], 34, 34, "verfehlt", farbe=ROT),
    pl("um wenige Zentimeter verfehlt", 1500, 140, beim("verfehlt", "verfehlt"), fill=GELB, size=30, anker="m", bis="frage"),
    # Gregor rennt in sein Haus und schließt ab (Tür, Schlüssel)
    *fig("GR", GTX, BA, SH, [(GR_TUER, "angst_r")], bis=SCHLIESST, erst="cut"),
    hart(ns("Gregor", GTX, BA, GR_TUER, NFARBE["GR"], bis=SCHLIESST)),
    szene(ficon("ph", "lock", GW[0] + GT[0] + 60, BA - 60, 60, SCHLIESST, fuell=GELB), "097tuer*", 0.8, 0.0),
    szene(pl("schließt ab", GW[0] + GT[0] + 60, BA - 260, SCHLIESST, fill=WEISS, size=28, anker="m", bis="frage"),
          "097schloss*", 0.7, 0.45),
    # Herbert: nur die eine Patrone
    *redet("HE_bestuerzt_r", HX, BA, SH, "h2", "frage2"),
    *fig("HE", HX, BA, SH, [("frage2", "muede_r")], erst="cut"),
    blase("sprech", 660, 200, "h2", 620, 250, inhalt=["Das war meine", "einzige Patrone."], textsize=36,
          figur=("HE_bestuerzt_r", HX, BA, SH), bis="frage"),
    # Frage
    pl("Gregor bleibt unverletzt", 1500, 140, "frage", fill=GRUEN, size=32, anker="m"),
    pl("Ist Herbert trotzdem strafbar?", 640, 220, beim("frage", "Ist"), fill=PINK, size=40, anker="m"),
    pl("versuchter Totschlag, Schritt für Schritt", 640, 310, "frage2", fill=WEISS, size=32, anker="m"),
])


# B Sachverhalt -------------------------------------------------------------------------------------------------------
def sachverhalt_097(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.32)
        els += e; y += 22
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_097("sv", [
    "Herbert (Anfang 60) und sein Nachbar Gregor streiten seit Monaten, weil Gregor sein Auto immer wieder vor Herberts "
    "Garage parkt. An einem Samstagabend kommt es erneut zum Streit.",
    "Herbert holt aus seinem Haus eine alte Pistole, in der eine einzige Patrone steckt; weitere Munition hat er nicht. "
    "Er zielt aus 5 Metern auf Gregor, der ihm zuruft, er solle die Pistole weglegen. Herbert will Gregor töten und "
    "drückt ab. Die Kugel verfehlt Gregor um wenige Zentimeter und schlägt in die Hauswand ein.",
    "Gregor rennt in sein Haus und schließt ab. Herbert weiß, dass er keine Patrone mehr hat. Gregor bleibt unverletzt.",
], "Hat sich Herbert wegen versuchten Totschlags strafbar gemacht?")

# C Wortlaut §§ 22, 23 Abs. 1 und Aufbau ---------------------------------------------------------------------------------
W22 = ["„Eine Straftat versucht, wer nach seiner Vorstellung von der Tat",
       "zur Verwirklichung des Tatbestandes unmittelbar ansetzt.“"]
W23 = ["„(1) Der Versuch eines Verbrechens ist stets strafbar, der Versuch",
       "eines Vergehens nur dann, wenn das Gesetz es ausdrücklich",
       "bestimmt.“"]
w22, w22_y = wortlaut(80, 170, 1100, W22, "§ 22 StGB", "p22", marken=[
    (0, "nach seiner Vorstellung von der Tat", beim("p22w", "nach")), (1, "unmittelbar ansetzt", beim("p22w", "unmittelbar"))])
w23, w23_y = wortlaut(80, w22_y + 22, 1100, W23, "§ 23 Abs. 1 StGB", "p23", marken=[
    (0, "Verbrechens ist stets strafbar", beim("p23w", "Verbrechens"))])
AB_Y = w23_y + 28
folie([("p22", "Versuch › Wortlaut §§ 22, 23 Abs. 1 StGB"), ("aufbau", "Versuch › Aufbau"),
       ("mord", "Versuchter Totschlag, §§ 212, 22, 23 Abs. 1 StGB")], rechts_frei([
    *tafel("p22", "Der Versuch, §§ 22, 23 StGB"),
    *w22, *w23,
    blk(110, AB_Y, 330, 76, GELB, beim("aufbau", "Vorprüfung"), [("0. Vorprüfung", "ExtraBold", 32, INK)]),
    blk(460, AB_Y, 330, 76, BLAU, beim("aufbau", "Tatentschluss"), [("1. Tatentschluss", "ExtraBold", 32, INK)]),
    blk(810, AB_Y, 340, 76, LILA, beim("aufbau", "unmittelbares"), [("2. Ansetzen", "ExtraBold", 32, INK)]),
    z("Mordmerkmale: im Fall nicht nahegelegt", 110, AB_Y + 112, "mord", size=34),
    z("geprüft: Totschlag, § 212 Abs. 1 StGB", 110, AB_Y + 162, beim("mord", "Wir"), "Bold", 34),
    *requisit([("p22", ("tabler", "target", 100, WEISS), "§ 22", WEISS),
               ("aufbau", ("tabler", "list-numbers", 100, WEISS), "Aufbau", WEISS),
               ("mord", ("tabler", "scale", 110, WEISS), "§ 212", WEISS)]),
    *paar("p22", [("p22", "ernst"), ("aufbau", "denkt")], [("p22", "ruhig"), ("mord", "ernst")]),
]))

# D 0. Vorprüfung --------------------------------------------------------------------------------------------------------
VT = "Versuchter Totschlag"
folie([("vp", f"{VT} › 0. Vorprüfung"), ("vp1", f"{VT} › 0. Vorprüfung › 1. Nichtvollendung"),
       ("vp2", f"{VT} › 0. Vorprüfung › 2. Strafbarkeit des Versuchs")], rechts_frei([
    *tafel("vp", "0. Vorprüfung"),
    *okz("1. Tat nicht vollendet: Gregor lebt", 200, "vp1", "Bold", 36, x=160),
    z("2. Ist der Versuch strafbar?", 115, 300, "vp2", "Bold", 36),
    z("§ 212 Abs. 1: Freiheitsstrafe nicht unter 5 Jahren", 160, 365, "vp3", size=34),
    z("also ein Verbrechen,", 160, 425, beim("vp3", "Verbrechen"), size=34),
    z("§ 12 Abs. 1 StGB", 160, 475, beim("vp3", "Paragraf"), "Bold", 34),
    blk(110, 560, 1040, 96, GRUEN, "vp4", [("§ 23 Abs. 1: Versuch stets strafbar", "ExtraBold", 38, INK)]),
    *requisit([("vp", ("tabler", "checklist", 100, WEISS), "Vorprüfung", WEISS),
               ("vp1", ("tabler", "heart", 100, ROT), "Gregor lebt", GRUEN),
               ("vp3", ("tabler", "scale", 110, WEISS), "Verbrechen", GELB)]),
    *paar("vp", [("vp", "ernst"), ("vp4", "muede")], [("vp", "ruhig"), ("vp1", "erleichtert"), ("vp3", "ernst")]),
]))

# E I.1 Tatentschluss ----------------------------------------------------------------------------------------------------
HEd = ("HE_denkt", X1, FB, FR)
folie([("te", f"{VT} › I. Tatbestand › 1. Tatentschluss")], rechts_frei([
    *tafel("te", "I. 1. Tatentschluss"),
    z("vorsatzgleiche Vorstellung, die sich auf alle", 110, 190, "te1", "Bold", 34),
    z("Umstände des äußeren Tatbestands bezieht", 110, 240, beim("te1", "Umstände"), "Bold", 34),
    zit("BGH, Beschl. v. 9.1.2020 – 4 StR 324/19, Rn. 17", 110, 292, beim("te1", "bezieht")),
    z("dazu besondere subjektive Merkmale, z. B. Absicht", 110, 370, "te2", size=34),
    zit("Klausurstandard", 110, 420, beim("te2", "Absicht")),
    *neinz("§ 212 verlangt keine", 470, beim("te2", "Paragraf"), size=34, x=160),
    *okz("Herbert will Gregor töten: einen anderen Menschen", 570, "te3", "Bold", 34, x=160),
    blk(110, 660, 1040, 90, GRUEN, beim("te3", "Der"), [("Tatentschluss (+)", "ExtraBold", 38, INK)]),
    blase("denk", 330, 210, "te3", 1520, 190, figur=HEd, bis=None),
    ficon("tabler", "target", 1520, 235, 90, "te3", fuell=ROT),
    *fig("HE", X1, FB, FR, [("te", "ernst"), ("te3", "denkt")]), ns("Herbert", X1, FB, "te", NFARBE["HE"], d=0.1),
    *fig("GR", X2, FB, FR, [("te", "ruhig"), ("te3", "angst")], d=0.2), ns("Gregor", X2, FB, "te", NFARBE["GR"], d=0.3),
    pl("Vorstellung", PX, PY, "te1", fill=WEISS, size=28, anker="m", bis="te3"),
    ficon("tabler", "bulb", PX, PU - 40, 90, "te1", fuell=GELB, bis="te3"),
]))

# F I.2 unmittelbares Ansetzen -------------------------------------------------------------------------------------------
UA = f"{VT} › I. Tatbestand › 2. unmittelbares Ansetzen"
folie([("ua", UA), ("vorb", f"{UA} › Abgrenzung: Vorbereitung")], rechts_frei([
    *tafel("ua", "I. 2. Unmittelbares Ansetzen"),
    z("subjektiv: Schwelle zum „jetzt geht’s los“", 110, 190, "ua1", "Bold", 34),
    z("Handlung soll nach dem Tatplan ohne Zwischen-", 110, 250, "ua2", size=34),
    z("schritte in die Tatbestandsverwirklichung einmünden", 110, 298, beim("ua2", "Zwischenschritte"), size=34),
    zit("BGH, Beschl. v. 28.4.2020 – 5 StR 15/20 (BGHSt 65, 15), Rn. 4", 110, 350, beim("ua2", "einmünden")),
    z("wesentlich: Maß konkreter Gefährdung des Rechtsguts", 110, 410, "ua3", size=34),
    zit("ebd. Rn. 5 (aus Sicht des Täters)", 110, 460, beim("ua3", "Sicht")),
    *okz("Herbert hat abgedrückt: alles getan", 530, "ua4", "Bold", 34, x=160),
    blk(175, 595, 975, 80, GRUEN, beim("ua4", "Das"), [("unmittelbares Ansetzen (+)", "ExtraBold", 36, INK)]),
    *neinz("nur Pistole holen: Zwischenschritte fehlen,", 715, "vorb", "Bold", 34, x=160),
    z("bloße Vorbereitung", 160, 765, beim("vorb", "Das"), "Bold", 34),
    # rechts: vom Holen zum Abdrücken
    pl("„jetzt geht’s los“", PX, 150, "ua1", fill=GELB, size=30, anker="m", bis="ua4"),
    ficon("tabler", "target", PX, 380, 110, "ua1", fuell=ROT, bis="ua4"),
    ficon("ph", "house", 1415, 290, 110, "ua4", fuell=WEISS),
    pistole(1740, 270, 110, "ua4", spiegeln=True),
    pfeil_ink(1490, 235, 1665, 235, beim("vorb", "Zwischenschritte")),
    pl("abgedrückt", 1740, 315, "ua4", fill=GRUEN, size=28, anker="m"),
    pl("holen: Vorbereitung", 1415, 315, "vorb", fill=PINK, size=28, anker="m"),
    pl("Zwischenschritte", 1578, 140, beim("vorb", "Zwischenschritte"), fill=WEISS, size=28, anker="m"),
    *paar("ua", [("ua", "ernst"), ("ua4", "entschlossen")], [("ua", "ruhig"), ("ua4", "angst"), ("vorb", "ernst")]),
]))

# G II. Rechtswidrigkeit, III. Schuld ------------------------------------------------------------------------------------
folie([("rw", f"{VT} › II. Rechtswidrigkeit"), ("schuld", f"{VT} › III. Schuld")], rechts_frei([
    *tafel("rw", "II. Rechtswidrigkeit, III. Schuld"),
    z("II. Rechtswidrigkeit", 110, 190, "rw", "ExtraBold", 38),
    z("Gregor hat nur mit Worten gestritten", 160, 255, beim("rw", "Gregor"), size=34),
    *neinz("kein Angriff, keine Notwehr", 320, "rw2", "Bold", 34, x=200),
    blk(110, 395, 1040, 80, GRUEN, beim("rw2", "Notwehr"), [("rechtswidrig (+)", "ExtraBold", 36, INK)]),
    z("III. Schuld", 110, 530, "schuld", "ExtraBold", 38),
    z("keine Anhaltspunkte für Schuldunfähigkeit", 160, 595, beim("schuld", "Für"), size=34),
    z("oder eine Entschuldigung", 160, 645, beim("schuld", "Entschuldigung"), size=34),
    blk(110, 715, 1040, 80, GRUEN, beim("schuld", "spricht"), [("schuldhaft (+)", "ExtraBold", 36, INK)]),
    *requisit([("rw", ("tabler", "message-circle", 100, WEISS), "nur Worte", WEISS),
               ("rw2", ("tabler", "shield-off", 100, WEISS), "keine Notwehr", PINK),
               ("schuld", ("tabler", "user-check", 100, WEISS), "Schuld", WEISS)]),
    *paar("rw", [("rw", "ernst"), ("schuld", "muede")], [("rw", "genervt"), ("rw2", "ernst")]),
]))

# H IV. Rücktritt --------------------------------------------------------------------------------------------------------
folie([("rt", f"{VT} › IV. Rücktritt, § 24 StGB"), ("rt1", f"{VT} › IV. Rücktritt › fehlgeschlagener Versuch")], rechts_frei([
    *tafel("rt", "IV. Rücktritt, § 24 StGB"),
    z("eigener Prüfungspunkt nach der Schuld", 110, 185, beim("rt", "eigener"), "Bold", 34),
    z("ausgeschlossen beim fehlgeschlagenen Versuch:", 110, 260, "rt1", "Bold", 34),
    z("Tat mit eingesetzten oder anderen naheliegenden", 160, 320, "rt2", size=34),
    z("Mitteln nicht mehr vollendbar, Täter erkennt das", 160, 368, beim("rt2", "nicht"), size=34),
    z("maßgeblich: seine Sicht nach dem Schuss", 160, 430, "rt3", size=34),
    zit("Rücktrittshorizont · BGH, Urt. v. 26.3.2025 – 2 StR 598/24, Rn. 11", 160, 480, beim("rt3", "Schuss")),
    *okz("nur 1 Patrone, und Herbert weiß das", 550, "rt4", "Bold", 34, x=160),
    blk(110, 625, 1040, 90, PINK, "rt5", [("fehlgeschlagen: kein Rücktritt", "ExtraBold", 38, INK)]),
    *requisit([("rt", ("tabler", "arrow-back-up", 100, WEISS), "Rücktritt?", WEISS),
               ("rt1", ("tabler", "circle-x", 100, ROT), "fehlgeschlagen?", WEISS),
               ("rt4", None, "0 Patronen übrig", GELB)]),
    pistole(PX, PU - 20, 110, "rt4", spiegeln=False),
    *paar("rt", [("rt", "ernst"), ("rt4", "muede")], [("rt", "ruhig"), ("rt5", "erleichtert")]),
]))

# I Ergebnis, Milderung, Konkurrenz --------------------------------------------------------------------------------------
folie([("erg", "Ergebnis"), ("mild", "Ergebnis › Strafmilderung, § 23 Abs. 2 StGB"), ("konk", "Ergebnis › Konkurrenzen")],
      rechts_frei([
    *tafel("erg", "Ergebnis"),
    blk(110, 180, 1040, 130, GRUEN, "erg", [("Herbert: versuchter Totschlag,", "ExtraBold", 38, INK),
                                            ("§§ 212 Abs. 1, 22, 23 Abs. 1 StGB", "ExtraBold", 38, INK)]),
    z("Strafe kann gemildert werden:", 110, 370, "mild", "Bold", 36),
    z("§ 23 Abs. 2 i. V. m. § 49 Abs. 1 StGB", 160, 425, beim("mild", "gemildert"), size=36),
    z("versuchte gefährliche Körperverletzung", 110, 520, "konk", "Bold", 34),
    z("tritt dahinter zurück", 160, 570, beim("konk", "tritt"), size=34),
    zit("BGH, Beschl. v. 13.8.2013 – 2 StR 180/13, Rn. 12", 160, 620, beim("konk", "Bundesgerichtshof")),
    *requisit([("erg", ("tabler", "gavel", 100, WEISS), "strafbar", PINK),
               ("mild", ("tabler", "arrow-down", 90, WEISS), "kann gemildert werden", WEISS),
               ("konk", ("tabler", "stack-2", 100, WEISS), "tritt zurück", WEISS)]),
    *paar("erg", [("erg", "muede"), ("mild", "denkt")], [("erg", "ernst"), ("mild", "ruhig")]),
]))

# J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Tatentschluss vor Ansetzen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, beim("tipp", "Gliedere"), gr=26),
    z("Tatbestand beim Versuch nicht in", 200, 200, beim("tipp", "Gliedere"), "Bold", 36),
    z("objektiv und subjektiv gliedern", 200, 252, beim("tipp", "objektiv"), "Bold", 36),
    z("objektiver Tatbestand ist gerade nicht erfüllt", 110, 340, "tipp2", size=36),
    blk(110, 420, 1040, 90, BLAU, beim("tipp2", "Prüfe"), [("zuerst: Tatentschluss", "ExtraBold", 38, INK)]),
    z("Ansetzen richtet sich nach seiner", 110, 560, "tipp3", size=36),
    z("Vorstellung von der Tat", 110, 612, beim("tipp3", "Vorstellung"), "Bold", 36),
    zit("Klausurkonvention", 110, 670, beim("tipp3", "Tat")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# K Klausurschema -------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: versuchter Totschlag, §§ 212, 22, 23 Abs. 1 StGB"), 110, 90, "sch", 44),
    z("0. Vorprüfung", K1, 190, "s0", "Bold", 40, rechts=1820),
    z("1. Nichtvollendung", K2, 250, beim("s0", "Nichtvollendung"), size=38, rechts=1820),
    z("2. Strafbarkeit des Versuchs", K2, 305, "s0b", size=38, rechts=1820),
    z("I. Tatbestand", K1, 385, "s1", "Bold", 40, rechts=1820),
    z("1. Tatentschluss", K2, 445, beim("s1", "Tatentschluss"), size=38, rechts=1820),
    z("2. unmittelbares Ansetzen", K2, 500, "s1b", size=38, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 580, "s2", "Bold", 40, rechts=1820),
    z("III. Schuld", K1, 650, "s3", "Bold", 40, rechts=1820),
    z("IV. Rücktritt, § 24 StGB", K1, 720, "s4", "Bold", 40, rechts=1820),
    z("ausgeschlossen beim fehlgeschlagenen Versuch", K2, 780, "s4b", size=38, rechts=1820),
])

# L Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Versucht hat, wer nach seiner ", 0), ("Vorstellung", "a")], [("unmittelbar ansetzt.", 0)]],
                750, 290, 44, "merke", {"a": beim("merke", "Vorstellung")}),
    *markertext([[("Der ", 0), ("Tatentschluss", "b"), (" kommt", 0)], [("vor dem Ansetzen.", 0)]],
                750, 480, 44, "m2", {"b": beim("m2", "Tatentschluss")}),
    *markertext([[("Wer erkennt, dass er die Tat nicht", 0)], [("mehr vollenden kann, kann nicht", 0)],
                 [("mehr ", 0), ("zurücktreten.", "c")]], 750, 640, 42, "m3", {"c": beim("m3", "zurücktreten")}),
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
