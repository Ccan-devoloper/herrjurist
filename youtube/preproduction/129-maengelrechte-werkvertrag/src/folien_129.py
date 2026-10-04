"""Folge 129 · Mängelrechte Werkvertrag § 634 BGB: Schema und Unterschiede zum Kauf – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Beate lässt das Dach ihres Hauses von Herrn Wenzel für 18.000 € neu eindecken und nimmt es ab; zwei Monate
später Wasserflecken, der Anschluss am Schornstein ist undicht (Reparatur 2.400 €); Herr Wenzel geht nicht ans Telefon.
Szenen laut ../SZENENPLAN.md: A1 Das neue Dach, A2 Regen/Befund, A3 Keine Antwort, B Sachverhalt, C 1. Werkvertrag und
Abnahme, D 2. Mangel (Wortlaut § 633 Abs. 2, Auszug), E1 3. Rechte (Wortlaut § 634), E2 Nacherfüllung/Wahlrecht,
F Selbstvornahme (Wortlaut § 637 Abs. 1), G Vorschuss (Wortlaut § 637 Abs. 3), H Rücktritt/Minderung/Schadensersatz,
I 4. Verjährung (Wortlaut § 634a, Auszug), J 5. Unterschiede zum Kauf (Tabelle), K Ergebnis, L Klausurtipp (Lexi),
M Schema, N Merksatz (Lexi). Zwei Handlungsgeräusche (Regen, Telefon; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/hand/okz/
neinz als eigene Kopie aus Folge 125 (gemeinsame Dateien unverändert); neu: Haus im Aufriss (dach, schornstein, haus,
flecken, ring) und tabelle() für den Vergleich Kauf/Werkvertrag.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern (Wortlautkarten wörtlich)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_129/"

# Sprechblasen müssen im Stil C entstehen (kein stiller Rückfall auf Stil e)
_run0 = bausteine._sp.run


def _run_c(args, **k):
    r = _run0(args, **k)
    if len(args) > 1 and str(args[1]).endswith("blase_c.js"):
        assert r.returncode == 0, f"Blase Stil C fehlgeschlagen: {args[2]}"
    return r


bausteine._sp.run = _run_c

FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
ZITAT = (246, 246, 250, 255)
HELLROT = (250, 205, 198, 255)
HELLGRUEN = (214, 240, 214, 255)
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


def tafel(cue, titel_, h=840, fill=WEISS, size=46, frei=1170):
    """Rechtstafel links, rechts bleibt Platz für die Figuren; frei = rechte Grenze des Titels (Rechenleiste)."""
    assert 110 + F("ExtraBold", size).getlength(glyphen(titel_)) <= frei, f"Titel zu breit: {titel_}"
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (Diagramm-Icons des Zeitstrahls ausgenommen)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")) or "/op_129/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def dicon(*a, **k):
    """Icon als Teil eines Diagramms innerhalb der Tafel (Zeitstrahl), nicht als Requisit."""
    e = ficon(*a, **k)
    e.name = "diagramm:" + (e.name or "")
    return e


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
    els.append(z(quelle, tx, ty + len(zeilen) * lh + 4, cue, "Bold", max(26, size - 4), farbe=TEXT, rechts=x + w - 16, bis=bis))
    return els, y + hgt


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 027/073/083/103) --------------------------------
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


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (Hand) im Band 40–62 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.40):int(h * 0.62)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return int(e.x + xs[i]), int(e.y + int(h * 0.40) + ys[i])


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


BODEN, FH = 860, 480
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
BE_N, WE_N = LILA, GELB                     # Farben der Namensschilder
PX, PY, PU = 1560, 120, 340                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
GRAU = (190, 190, 196, 255)
ZIEGEL = (214, 92, 70, 255)
KAUF, WERK = (214, 228, 250, 255), (253, 236, 186, 255)   # Spaltenfarben Kauf (hellblau) / Werkvertrag (hellgelb)
WASSER = (110, 150, 220, 200)


def boden(cue, hart_=False):
    e = linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK)
    return hart(e) if hart_ else e


def requisit(folge, bis_ende=None):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis_ende
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, PX, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, PX, PY, c, fill=pf, size=30, anker="m", bis=b))
    return els


def paar(c0, be, we, bis=None):
    """Tafelszene: Beate (links) und Herr Wenzel (rechts) neben der Tafel, beide blicken zur Tafel (nach links)."""
    return [*fig("BE", X1, FB, FR, be, bis=bis), ns("Beate", X1, FB, c0, BE_N, d=0.1),
            *fig("WE", X2, FB, FR, we, bis=bis, d=0.2), ns("Herr Wenzel", X2, FB, c0, WE_N, d=0.3)]


# --- Das Haus im Aufriss (programmatisch aus Palettenflächen, kein Fremdbild) -------------------------------------------
HX0, HX1, HY = 300, 1000, 560               # Hauswand links/rechts, Traufe
DX0, DX1, DFIRST = 240, 1060, (650, 250)    # Dachfuß links/rechts, First
SCH = (820, 870, 300)                       # Schornstein x0, x1, oben


def _dach_y(x):
    """Höhe der rechten Dachfläche an der Stelle x."""
    return DFIRST[1] + (x - DFIRST[0]) / (DX1 - DFIRST[0]) * (HY - DFIRST[1])


def dach(cue, neu, bis=None, anim="cut"):
    s = 2
    x0, y0 = DX0 - 10, DFIRST[1] - 10
    w, h = DX1 - DX0 + 20, HY - DFIRST[1] + 20
    im = Image.new("RGBA", (w * s, h * s)); dr = ImageDraw.Draw(im)
    P = lambda x, y: ((x - x0) * s, (y - y0) * s)
    poly = [P(DX0, HY), P(*DFIRST), P(DX1, HY)]
    dr.polygon(poly, fill=ZIEGEL if neu else GRAU)
    # Ziegelreihen
    for k in range(1, 7):
        y = DFIRST[1] + k * (HY - DFIRST[1]) / 7
        xl = DFIRST[0] - (y - DFIRST[1]) / (HY - DFIRST[1]) * (DFIRST[0] - DX0)
        xr = DFIRST[0] + (y - DFIRST[1]) / (HY - DFIRST[1]) * (DX1 - DFIRST[0])
        if neu:
            dr.line([P(xl + 4, y), P(xr - 4, y)], fill=INK, width=3 * s)
            n = int((xr - xl) / 46)
            for j in range(1, n):
                xx = xl + j * (xr - xl) / n + (12 if k % 2 else -12)
                dr.line([P(xx, y), P(xx, y + (HY - DFIRST[1]) / 7 - 2)], fill=INK, width=2 * s)
        elif k % 2:
            dr.line([P(xl + 30, y), P(xr - 60, y)], fill=TEXT, width=3 * s)
    dr.line(poly + [poly[0]], fill=INK, width=6 * s, joint="curve")
    im = im.resize((w, h), Image.LANCZOS)
    return El(im, x0, y0, cue, anim, 0.0, bis, name="dach:" + ("neu" if neu else "alt"))


def schornstein(cue, anim="cut"):
    x0, x1, yo = SCH
    yu = int(_dach_y(x1)) + 6
    e = karte(x0, yo, x1 - x0, yu - yo, cue, fill=ROT, rund=4, schatten=0, rand=5, anim=anim)
    return e


def haus(c0, hart_=True, neu=True, alt_bis=None):
    an = "cut" if hart_ else "fade"
    els = [boden(c0, hart_), schornstein(c0, an),
           karte(HX0, HY, HX1 - HX0, BODEN - HY, c0, fill=WEISS, rund=6, schatten=6, rand=5, anim=an),
           karte(380, 640, 150, 120, c0, fill=BLAU, rund=8, schatten=0, rand=5, anim=an),
           karte(600, 650, 120, BODEN - 650, c0, fill=GELB, rund=6, schatten=0, rand=5, anim=an)]
    if neu is True:
        els.append(dach(c0, True, anim=an))
    else:
        els += [dach(c0, False, bis=neu, anim=an), dach(neu, True, anim="fade")]
    return els


def flecken(cue, n=3):
    els = []
    for i, (cx, cy, rx, ry) in enumerate([(850, 600, 46, 22), (780, 615, 28, 14), (905, 630, 22, 12)][:n]):
        im = Image.new("RGBA", (rx * 4 + 4, ry * 4 + 4)); dr = ImageDraw.Draw(im)
        dr.ellipse((2, 2, rx * 4, ry * 4), fill=WASSER, outline=(70, 100, 170, 255), width=4)
        im = im.resize((rx * 2 + 2, ry * 2 + 2), Image.LANCZOS)
        els.append(El(im, cx - rx, cy - ry, cue, "pop", 0.1 * i, name="fleck"))
    return els


def ring(cx, cy, r, cue, farbe=DROT, bis=None):
    im = Image.new("RGBA", (r * 4 + 16, r * 4 + 16)); dr = ImageDraw.Draw(im)
    dr.ellipse((8, 8, r * 4 + 8, r * 4 + 8), outline=farbe, width=16)
    im = im.resize((r * 2 + 8, r * 2 + 8), Image.LANCZOS)
    return El(im, cx - r - 4, cy - r - 4, cue, "pop", 0.0, bis, name="ring")


WX, BX = 1330, 1680                         # Herr Wenzel (links, blickt nach rechts), Beate (rechts, blickt nach links)

# ===========================================================================================================================
# A1 Fall: Das neue Dach
# ===========================================================================================================================
NEU = beim("fall", "neu")
folie([(NULL, "Fall · Das neue Dach"), ("abn", "Fall · Die Abnahme")], [
    *haus(NULL, neu=NEU),
    hart(pl("Beates Haus", 70, 30, NULL, fill=GELB, size=40)),
    pl("neu eindecken", 70, 112, NEU, fill=WEISS, size=32),
    pl("18.000 €", 360, 112, beim("fall", "achtzehntausend"), fill=GELB, size=32),
    pl("nach 3 Wochen: fertig", 560, 112, beim("fertig", "drei"), fill=WEISS, size=32),
    blase("sprech", 600, 190, "we1", 1000, 262, inhalt=["Fertig! Das Dach hält", "jetzt viele Jahre."], textsize=36,
          figur=("WE_redet_r", WX, BODEN, FH), bis="abn"),
    ficon("tabler", "zoom-check", 1150, 360, 100, beim("abn", "genau"), fuell=WEISS, bis=beim("abn", "nimmt")),
    ok(1100, 330, beim("abn", "nimmt"), gr=22),
    pl("abgenommen", 1135, 298, beim("abn", "nimmt"), fill=GRUEN, size=32),
    ficon("tabler", "receipt-euro", 1150, 470, 90, "bez", fuell=WEISS),
    pl("Rechnung bezahlt", 1135, 220, beim("bez", "zahlt"), fill=GRUEN, size=30),
    *fig("WE", WX, BODEN, FH, [(NULL, "ruhig_r"), ("fertig", "froh_r")], erst="cut", bis="we1"),
    *redet("WE_redet_r", WX, BODEN, FH, "we1", "abn"),
    *fig("WE", WX, BODEN, FH, [("abn", "froh_r")], erst="cut"),
    hart(ns("Herr Wenzel", WX, BODEN, NULL, WE_N)),
    *fig("BE", BX, BODEN, FH, [(NULL, "ruhig"), ("fertig", "froh"), (beim("abn", "genau"), "denkt"),
                               (beim("abn", "nimmt"), "zufrieden")], erst="cut"),
    hart(ns("Beate", BX, BODEN, NULL, BE_N)),
])

# ===========================================================================================================================
# A2 Fall: Zwei Monate später – Regen, Wasserflecken, Befund
# ===========================================================================================================================
REG = beim("regen", "regnet")
SX = (SCH[0] + SCH[1]) // 2
folie([("regen", "Fall · Zwei Monate später"), ("gut", "Fall · Der undichte Anschluss")], [
    *haus("regen", hart_=False),
    pl("2 Monate später", 70, 30, "regen", fill=GELB, size=40),
    szene(ficon("tabler", "cloud-rain", 640, 225, 170, REG, fuell=BLAU), "129regen*", 0.8),
    ficon("tabler", "cloud-rain", 920, 205, 150, REG, fuell=BLAU, d=0.15),
    pl("Wasserflecken an der Decke", 40, 150, beim("fleck", "Wasserflecken"), fill=BLAU, size=30),
    *flecken(beim("fleck", "Wasserflecken")),
    ring(SX, int(_dach_y(SCH[1])) - 10, 62, beim("gut", "Anschluss")),
    pl("Anschluss am Schornstein undicht", 1000, 330, beim("gut", "Schornstein"), fill=ROT, size=30),
    ficon("tabler", "file-invoice", 1150, 560, 90, "kost", fuell=WEISS),
    pl("Reparatur laut Angebot: 2.400 €", 1000, 410, beim("kost", "zweitausendvierhundert"), fill=GELB, size=30),
    *fig("BE", BX, BODEN, FH, [("regen", "ruhig"), (beim("fleck", "Wasserflecken"), "sorge"), ("gut", "denkt"),
                               (beim("kost", "zweitausendvierhundert"), "staunt")], erst="pop"),
    ns("Beate", BX, BODEN, "regen", BE_N, d=0.1),
])

# ===========================================================================================================================
# A3 Fall: Niemand geht ran
# ===========================================================================================================================
TELX = 1450
folie([("anruf", "Fall · Keine Antwort"), ("frage", "Fall · Die Frage")], [
    *haus("anruf", hart_=False),
    *flecken("anruf"),
    szene(ficon("tabler", "phone-calling", TELX, 470, 110, "anruf", fuell=WEISS, bis=beim("anruf", "Niemand")),
          "129telefon*", 0.6),
    ficon("tabler", "phone-x", TELX, 470, 110, beim("anruf", "Niemand"), fuell=ROT, anim="cut"),
    pl("Herr Wenzel geht nicht ran", 1010, 250, beim("anruf", "Niemand"), fill=ROT, size=30, bis="be1"),
    blase("sprech", 700, 230, "be1", 1150, 280, inhalt=["Herr Wenzel, mein Dach", "ist undicht! Bitte rufen",
                                                        "Sie mich zurück."], textsize=34,
          figur=("BE_redet", BX, BODEN, FH), bis="nie"),
    pl("3 weitere Anrufe: keine Antwort", 1010, 250, "nie", fill=ROT, size=30),
    pl("Was kann Beate verlangen?", 40, 120, "frage", fill=PINK, size=36),
    pl("Was ist anders als beim Kauf?", 40, 205, "frage2", fill=PINK, size=36),
    *fig("BE", BX, BODEN, FH, [("anruf", "denkt"), (beim("anruf", "Niemand"), "sorge")], erst="pop", bis="be1"),
    ns("Beate", BX, BODEN, "anruf", BE_N, d=0.1),
    *redet("BE_redet", BX, BODEN, FH, "be1", "nie"),
    *fig("BE", BX, BODEN, FH, [("nie", "aerger"), ("frage", "denkt")], erst="cut"),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_129(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 56)]
    y = 205
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=38, zeilenabstand=1.30)
        els += e; y += 14
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=36))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_129("sv", [
    "Beate lässt das Dach ihres Hauses vom Dachdecker Herrn Wenzel für 18.000 Euro neu eindecken. Nach drei Wochen "
    "ist er fertig. Beate sieht sich alles genau an, nimmt das Dach ab und zahlt die Rechnung.",
    "Zwei Monate später regnet es stark. Im Dachgeschoss zeigen sich Wasserflecken an der Decke. Ein anderer "
    "Dachdecker stellt fest: Herr Wenzel hat den Anschluss am Schornstein undicht ausgeführt. Die Reparatur kostet "
    "laut seinem Angebot 2.400 Euro.",
    "Beate ruft Herrn Wenzel an und bittet um Rückruf. Auch auf drei weitere Anrufe kommt keine Antwort.",
], "Was kann Beate verlangen? Was ist anders als beim Kauf?")

# ===========================================================================================================================
# C 1. Werkvertrag und Abnahme
# ===========================================================================================================================
folie([("p1", "1. Werkvertrag und Abnahme"), ("p1b", "1. › Abnahme als Zäsur"),
       ("bau", "1. › Bauvertrag, § 650a BGB")], rechts_frei([
    *tafel("p1", "1. Werkvertrag und Abnahme"),
    z("Geschuldet: ein Erfolg, ein dichtes neues Dach", 110, 190, beim("p1a", "Erfolg"), "Bold", 34),
    *okz("Werkvertrag, § 631 Abs. 1 BGB", 250, beim("p1a", "Werkvertrag"), "Bold", 34, x=160),
    pl("Abgrenzung zum Dienstvertrag: eigenes Video", 110, 315, "p056", fill=GELB, size=28),
    z("Mängelrechte grundsätzlich erst nach der Abnahme", 110, 410, "p1b", "Bold", 34),
    zit("BGH, Urt. v. 19.1.2017 – VII ZR 301/13, Leitsatz 1 (Rn. 31)", 110, 458, beim("p1b", "Abnahme")),
    *okz("Beate hat abgenommen", 520, "p1c", "Bold", 34, x=160),
    pl("Mehr dazu: Video zur Abnahme", 600, 515, beim("p1c", "mehr"), fill=GELB, size=28),
    *okz("Neueindeckung stellt einen Teil des Hauses wieder her:", 620, "bau", "Bold", 32, x=160),
    z("zugleich Bauvertrag, § 650a Abs. 1 BGB", 160, 670, beim("bau", "Bauvertrag"), "Bold", 32),
    blk(110, 740, 1040, 90, WERK, beim("bau", "Dessen"), [("Bauvertragsregeln gelten nur ergänzend", "Bold", 34, INK)]),
    *requisit([("p1", ("tabler", "home", 110, ZIEGEL), "Beates Haus", WEISS),
               ("p1b", ("tabler", "checklist", 100, WEISS), "Abnahme", GRUEN),
               ("bau", ("tabler", "building", 100, WEISS), "Bauvertrag", WERK)]),
    *paar("p1", [("p1", "ruhig"), ("p1c", "zufrieden"), ("bau", "denkt")], [("p1", "ruhig"), ("p1b", "ernst")]),
]))

# ===========================================================================================================================
# D 2. Mangel, § 633 Abs. 2 BGB (Wortlautkarte, Auszug)
# ===========================================================================================================================
W633 = ["„Das Werk ist frei von Sachmängeln, wenn es die vereinbarte",
        "Beschaffenheit hat. Soweit die Beschaffenheit nicht vereinbart ist,",
        "ist das Werk frei von Sachmängeln, 1. wenn es sich für die nach dem",
        "Vertrag vorausgesetzte, sonst 2. für die gewöhnliche Verwendung eignet",
        "und eine Beschaffenheit aufweist, die bei Werken der gleichen Art",
        "üblich ist und die der Besteller nach der Art des Werkes erwarten kann.“"]
w633, w633_y = wortlaut(110, 165, 1040, W633, "§ 633 Abs. 2 Satz 1 und 2 BGB (Auszug)", "m1", marken=[
    (0, "vereinbarte", beim("m2", "vereinbarte")),
    (1, "Beschaffenheit hat", beim("m2", "Beschaffenheit")),
    (3, "Vertrag vorausgesetzte", beim("m3", "vorausgesetzte")),
    (3, "gewöhnliche Verwendung", beim("m3", "gewöhnliche"))], size=28)
folie([("m1", "2. Mangel, § 633 Abs. 2 BGB"), ("m4", "2. Mangel › das undichte Dach"),
       ("m5", "2. Mangel › Zeitpunkt der Abnahme")], rechts_frei([
    *tafel("m1", "2. Mangel"),
    *w633,
    *okz("Ein Dach muss dicht sein. Wasser dringt ein: Sachmangel", w633_y + 26, "m4", "Bold", 32, x=160),
    *okz("Maßgeblich: grundsätzlich der Zeitpunkt der Abnahme", w633_y + 96, "m5", "Bold", 32, x=160),
    zit("BGH, Urt. v. 19.1.2017 – VII ZR 301/13, Rn. 32", 160, w633_y + 144, beim("m5", "Zeitpunkt")),
    blk(110, w633_y + 200, 1040, 120, GELB, "m6", [("Anschluss war bei der Abnahme schon undicht,", "Bold", 32, INK),
                                                  ("das Wasser zeigte sich erst später", "Bold", 32, INK)]),
    *requisit([("m1", ("tabler", "home", 110, ZIEGEL), "Sachmangel?", WEISS),
               ("m4", ("tabler", "droplet", 90, BLAU), "Wasser dringt ein", ROT),
               ("m5", ("tabler", "checklist", 100, WEISS), "Zeitpunkt: Abnahme", GRUEN)]),
    *paar("m1", [("m1", "ruhig"), ("m4", "sorge"), ("m6", "denkt")], [("m1", "ruhig"), ("m4", "ernst")]),
]))

# ===========================================================================================================================
# E1 3. Rechte aus § 634 BGB (Wortlautkarte)
# ===========================================================================================================================
W634 = ["„Ist das Werk mangelhaft, kann der Besteller, wenn die Voraussetzungen der",
        "folgenden Vorschriften vorliegen und soweit nicht ein anderes bestimmt ist,",
        "1. nach § 635 Nacherfüllung verlangen,",
        "2. nach § 637 den Mangel selbst beseitigen und Ersatz der erforderlichen",
        "Aufwendungen verlangen,",
        "3. nach den §§ 636, 323 und 326 Abs. 5 von dem Vertrag zurücktreten oder",
        "nach § 638 die Vergütung mindern und",
        "4. nach den §§ 636, 280, 281, 283 und 311a Schadensersatz oder nach § 284",
        "Ersatz vergeblicher Aufwendungen verlangen.“"]
w634, w634_y = wortlaut(110, 165, 1040, W634, "§ 634 BGB", "r1", marken=[
    (2, "Nacherfüllung verlangen", beim("r2", "Nacherfüllung")),
    (3, "den Mangel selbst beseitigen", beim("r3", "selbst")),
    (5, "zurücktreten", beim("r4", "zurücktreten")),
    (6, "die Vergütung mindern", beim("r4", "mindern")),
    (7, "Schadensersatz", beim("r5", "Schadensersatz"))], size=28)
folie([("r1", "3. Rechte aus § 634 BGB")], rechts_frei([
    *tafel("r1", "3. Rechte des Bestellers"),
    *w634,
    *requisit([("r1", ("tabler", "list-numbers", 100, WEISS), "4 Rechte", WEISS),
               ("r3", ("tabler", "tools", 100, WEISS), "selbst beseitigen", GELB)]),
    *paar("r1", [("r1", "ruhig"), ("r3", "froh")], [("r1", "ruhig"), ("r3", "denkt")]),
]))

# ===========================================================================================================================
# E2 3.1 Nacherfüllung, § 635 BGB – Wahlrecht
# ===========================================================================================================================
folie([("nach", "3. › Nacherfüllung, § 635 BGB"), ("kauf1", "3. › Nacherfüllung › anders beim Kauf, § 439 Abs. 1 BGB")],
      rechts_frei([
    *tafel("nach", "3.1 Nacherfüllung zuerst"),
    *okz("Vorrang der Nacherfüllung, § 635 BGB", 190, beim("nach", "Nacherfüllung"), "Bold", 34, x=160),
    z("Wer wählt, wie nacherfüllt wird?", 110, 270, "wahl", "Bold", 34),
    karte(110, 340, 505, 300, "kauf1", fill=KAUF, rund=18, schatten=6, rand=4),
    z("Kauf", 140, 360, "kauf1", "ExtraBold", 40),
    z("der Käufer", 140, 430, beim("kauf1", "Käufer"), "Bold", 34, rechts=600),
    z("Beseitigung oder", 140, 490, beim("kauf1", "Käufer"), "Regular", 30, rechts=600),
    z("Lieferung, § 439 Abs. 1", 140, 535, beim("kauf1", "Paragraf"), "Regular", 30, rechts=600),
    karte(645, 340, 505, 300, beim("wahl", "Unternehmer"), fill=WERK, rund=18, schatten=6, rand=4),
    z("Werkvertrag", 675, 360, beim("wahl", "Unternehmer"), "ExtraBold", 40),
    z("der Unternehmer", 675, 430, beim("wahl", "Unternehmer"), "Bold", 34, rechts=1135),
    z("Mangel beseitigen oder", 675, 490, beim("wahl", "beseitigt"), "Regular", 30, rechts=1135),
    z("neu herstellen, § 635 Abs. 1", 675, 535, beim("wahl", "neu"), "Regular", 30, rechts=1135),
    zit("BGH, Beschl. v. 8.10.2020 – VII ARZ 1/20, Rn. 27", 110, 680, beim("kauf1", "Käufer")),
    *requisit([("nach", ("tabler", "tools", 100, WEISS), "Nacherfüllung", GELB),
               ("kauf1", ("tabler", "shopping-cart", 100, KAUF), "beim Kauf: Käufer wählt", KAUF)]),
    *paar("nach", [("nach", "ruhig"), ("kauf1", "denkt")], [("nach", "ruhig"), ("wahl", "froh")]),
]))

# ===========================================================================================================================
# F 3.2 Selbstvornahme, § 637 Abs. 1 BGB (Wortlautkarte), Frist
# ===========================================================================================================================
W637 = ["„Der Besteller kann wegen eines Mangels des Werkes nach erfolglosem",
        "Ablauf einer von ihm zur Nacherfüllung bestimmten angemessenen Frist",
        "den Mangel selbst beseitigen und Ersatz der erforderlichen",
        "Aufwendungen verlangen, wenn nicht der Unternehmer die",
        "Nacherfüllung zu Recht verweigert.“"]
w637, w637_y = wortlaut(110, 165, 1040, W637, "§ 637 Abs. 1 BGB", "s1", marken=[
    (0, "nach erfolglosem", beim("s2", "erfolglosem")),
    (1, "angemessenen Frist", beim("s2", "angemessenen")),
    (2, "den Mangel selbst beseitigen", beim("s2", "selbst")),
    (2, "Ersatz der erforderlichen", beim("s2", "Ersatz")),
    (4, "zu Recht verweigert", beim("s3", "Recht"))], size=30)
folie([("s1", "3. › Selbstvornahme, § 637 Abs. 1 BGB"), ("s4", "3. › Selbstvornahme › Frist entbehrlich?"),
       ("s6", "3. › Selbstvornahme › Beate setzt eine Frist")], rechts_frei([
    *tafel("s1", "3.2 Selbstvornahme"),
    *w637,
    z("Frist entbehrlich, etwa bei ernsthafter und endgültiger", 110, w637_y + 26, "s4", "Bold", 32),
    z("Verweigerung, § 637 Abs. 2 mit § 323 Abs. 2 Nr. 1 BGB", 110, w637_y + 72, beim("s4", "ernsthaft"), "Bold", 32),
    zit("strenge Anforderungen: BGH, Urt. v. 13.7.2011 – VIII ZR 215/10, Rn. 24", 110, w637_y + 124, beim("s5", "strenge")),
    *neinz("nicht ans Telefon gehen: keine endgültige Verweigerung", w637_y + 176, beim("s5", "Wer"), "Bold", 32, x=160),
    blk(110, w637_y + 250, 1040, 90, GELB, "s6", [("Beate muss eine Frist setzen, am besten schriftlich", "Bold", 34, INK)]),
    *requisit([("s1", ("tabler", "tools", 100, WEISS), "Selbstvornahme", GELB),
               ("s2", ("tabler", "hourglass", 90, GELB), "Frist", GELB),
               ("s5", ("tabler", "phone-x", 100, ROT), "geht nicht ran", ROT),
               ("s6", ("tabler", "writing-sign", 100, WEISS), "Frist setzen", GRUEN)]),
    *paar("s1", [("s1", "ruhig"), ("s4", "denkt"), ("s6", "zufrieden")], [("s1", "ruhig"), ("s5", "ernst")]),
]))

# ===========================================================================================================================
# G 3.2 Vorschuss, § 637 Abs. 3 BGB (Wortlautkarte)
# ===========================================================================================================================
W637_3 = ["„Der Besteller kann von dem Unternehmer für die zur Beseitigung",
          "des Mangels erforderlichen Aufwendungen Vorschuss verlangen.“"]
w637c, w637c_y = wortlaut(110, 165, 1040, W637_3, "§ 637 Abs. 3 BGB", "v1", marken=[
    (1, "Vorschuss verlangen", beim("v1", "Vorschuss"))], size=30)
folie([("v1", "3. › Selbstvornahme › Vorschuss, § 637 Abs. 3 BGB"), ("kauf2", "3. › Vorschuss › anders beim Kauf")],
      rechts_frei([
    *tafel("v1", "3.2 Vorschuss"),
    *w637c,
    *okz("keine Vorfinanzierung nötig", w637c_y + 26, beim("v1", "Vorschuss"), "Bold", 34, x=160),
    zit("BGH, Beschl. v. 8.10.2020 – VII ARZ 1/20, Rn. 67", 160, w637c_y + 76, beim("v1", "Vorschuss")),
    *okz("für die Reparatur verwenden", w637c_y + 140, beim("v2", "Reparatur"), "Bold", 34, x=160),
    *okz("danach abrechnen", w637c_y + 210, beim("v2", "abrechnen"), "Bold", 34, x=160),
    zit("BGH, Urt. v. 9.11.2023 – VII ZR 92/20, Rn. 28", 160, w637c_y + 260, beim("v2", "abrechnen")),
    karte(110, w637c_y + 330, 1040, 120, "kauf2", fill=KAUF, rund=18, schatten=6, rand=4),
    *neinz("Kauf: weder Selbstvornahme noch Vorschuss", w637c_y + 352, "kauf2", "ExtraBold", 34, x=190),
    zit("vgl. §§ 437, 439 BGB; BGH VII ARZ 1/20, Rn. 67", 190, w637c_y + 400, beim("kauf2", "Selbstvornahme")),
    *requisit([("v1", ("tabler", "cash-banknote", 110, GRUEN), "Vorschuss", GRUEN),
               ("v2", ("tabler", "file-invoice", 90, WEISS), "abrechnen", WEISS),
               ("kauf2", ("tabler", "shopping-cart", 100, KAUF), "nicht beim Kauf", KAUF)]),
    *paar("v1", [("v1", "froh"), ("v2", "ruhig")], [("v1", "ernst"), ("kauf2", "denkt")]),
]))

# ===========================================================================================================================
# H 3.3 Rücktritt, Minderung, Schadensersatz
# ===========================================================================================================================
folie([("rm1", "3. › Rücktritt und Minderung, §§ 636, 323, 638 BGB"),
       ("se1", "3. › Schadensersatz, §§ 636, 280, 281 BGB")], rechts_frei([
    *tafel("rm1", "3.3 Rücktritt, Minderung, Schadensersatz"),
    *okz("Rücktritt und Minderung: erfolglose Frist", 190, "rm1", "Bold", 34, x=160),
    zit("§§ 634 Nr. 3, 636, 323 Abs. 1 BGB", 160, 240, beim("rm1", "Paragrafen")),
    *neinz("unerheblicher Mangel: kein Rücktritt", 310, beim("rm2", "unerheblichen"), "Bold", 34, x=160),
    zit("§ 323 Abs. 5 Satz 2 BGB", 160, 360, beim("rm2", "Rücktritt")),
    *okz("mindern geht trotzdem", 420, beim("rm2", "mindern"), "Bold", 34, x=160),
    zit("§ 638 Abs. 1 Satz 2 BGB", 160, 470, beim("rm2", "Paragraf")),
    *okz("Schadensersatz statt der Leistung: zusätzlich", 540, "se1", "Bold", 34, x=160),
    z("Vertretenmüssen – wird vermutet", 160, 595, beim("se1", "vermutet"), "Bold", 34),
    zit("§§ 634 Nr. 4, 636, 280 Abs. 1 Satz 2, 281 BGB", 160, 645, beim("se1", "Paragrafen")),
    *requisit([("rm1", ("tabler", "arrow-back-up", 100, WEISS), "zurücktreten oder mindern", WEISS),
               ("se1", ("tabler", "coins", 100, GELB), "Schadensersatz", GELB)]),
    *paar("rm1", [("rm1", "ruhig"), ("se1", "denkt")], [("rm1", "ruhig"), ("se1", "ernst")]),
]))

# ===========================================================================================================================
# I 4. Verjährung, § 634a BGB (Wortlautkarte, Auszug)
# ===========================================================================================================================
W634A = ["„(1) Die in § 634 Nr. 1, 2 und 4 bezeichneten Ansprüche verjähren",
         "1. vorbehaltlich der Nummer 2 in zwei Jahren bei einem Werk, dessen",
         "Erfolg in der Herstellung, Wartung oder Veränderung einer Sache … besteht,",
         "2. in fünf Jahren bei einem Bauwerk …",
         "(2) Die Verjährung beginnt in den Fällen des Absatzes 1 Nr. 1 und 2",
         "mit der Abnahme.“"]
w634a, w634a_y = wortlaut(110, 165, 1040, W634A, "§ 634a Abs. 1 Nr. 1 und 2, Abs. 2 BGB (Auszug)", "vj1", marken=[
    (3, "in fünf Jahren bei einem Bauwerk", beim("vj2", "Bauwerk")),
    (1, "in zwei Jahren", beim("vj2", "zwei")),
    (5, "mit der Abnahme", beim("vj5", "Abnahme"))], size=28)
folie([("vj1", "4. Verjährung, § 634a BGB"), ("vj3", "4. Verjährung › Bauwerk"),
       ("vj5", "4. Verjährung › Beginn mit der Abnahme")], rechts_frei([
    *tafel("vj1", "4. Verjährung"),
    *w634a,
    z("Bauwerk auch: Arbeiten am bestehenden Gebäude,", 110, w634a_y + 24, "vj3", "Bold", 32),
    z("wesentlich für den Bestand, Teile fest verbunden", 110, w634a_y + 70, beim("vj3", "wesentlich"), "Bold", 32),
    zit("BGH, Urt. v. 2.6.2016 – VII ZR 348/13, Rn. 19", 110, w634a_y + 118, beim("vj3", "wesentlich")),
    *okz("neu eingedecktes Dach: 5 Jahre", w634a_y + 176, "vj4", "Bold", 34, x=160),
    *okz("Beginn mit der Abnahme: Beate hat Zeit", w634a_y + 246, beim("vj5", "Beate"), "Bold", 34, x=160),
    *requisit([("vj1", ("tabler", "hourglass", 90, GELB), "Verjährung", WEISS),
               ("vj3", ("tabler", "building", 100, WEISS), "Bauwerk: 5 Jahre", GELB),
               ("vj5", ("tabler", "calendar-time", 100, WEISS), "ab der Abnahme", GRUEN)]),
    *paar("vj1", [("vj1", "ruhig"), ("vj4", "froh")], [("vj1", "ruhig"), ("vj3", "denkt")]),
]))

# ===========================================================================================================================
# J 5. Unterschiede zum Kauf (Tabelle, progressiv)
# ===========================================================================================================================
TX0, TC1, TC2, TX1 = 110, 430, 790, 1150    # Tabellenspalten: Merkmal | Kauf | Werkvertrag
TY0 = 200


def tabelle():
    els = [karte(TX0, TY0, TX1 - TX0, 70, "u1", fill=WEISS, rund=12, schatten=4, rand=4),
           karte(TC1, TY0, TC2 - TC1, 70, "u1", fill=KAUF, rund=0, schatten=0, rand=4),
           karte(TC2, TY0, TX1 - TC2, 70, "u1", fill=WERK, rund=0, schatten=0, rand=4),
           z("Kauf, § 437 BGB", TC1 + 18, TY0 + 14, "u1", "ExtraBold", 30, rechts=TC2 - 8),
           z("Werkvertrag, § 634", TC2 + 18, TY0 + 14, "u1", "ExtraBold", 30, rechts=TX1 - 8)]
    reihen = [("u2", ["Wahlrecht bei der", "Nacherfüllung"], ["Käufer,", "§ 439 Abs. 1"], ["Unternehmer,", "§ 635 Abs. 1"],
               beim("u2", "Käufer"), beim("u2", "Unternehmer")),
              ("u3", ["Selbstvornahme", "und Vorschuss"], ["gibt es nicht"], ["§ 637 Abs. 1, 3"], "u3", beim("u3", "Werkvertrag")),
              ("u4", ["maßgeblich", "für den Mangel"], ["Gefahrübergang,", "i. d. R. Übergabe"], ["Abnahme"],
               beim("u4", "Gefahrübergang"), beim("u4", "Abnahme")),
              ("u5", ["Beginn der", "Verjährung"], ["Ablieferung,", "§ 438 Abs. 2"], ["Abnahme,", "§ 634a Abs. 2"],
               beim("u5", "Ablieferung"), beim("u5", "Abnahme"))]
    y = TY0 + 66
    for c, merk, kauf, werk, ck, cw in reihen:
        h = 116
        els += [karte(TX0, y, TC1 - TX0, h, c, fill=WEISS, rund=0, schatten=0, rand=4),
                karte(TC1, y, TC2 - TC1, h, ck, fill=KAUF, rund=0, schatten=0, rand=4),
                karte(TC2, y, TX1 - TC2, h, cw, fill=WERK, rund=0, schatten=0, rand=4)]
        for spalte_, (x0, x1, cc, stil) in ((merk, (TX0, TC1, c, "Bold")), (kauf, (TC1, TC2, ck, "Regular")),
                                           (werk, (TC2, TX1, cw, "Bold"))):
            y0 = y + h / 2 - len(spalte_) * 40 / 2 + 2
            for i, t in enumerate(spalte_):
                els.append(z(t, x0 + 18, y0 + i * 40, cc, stil, 30, rechts=x1 - 8))
        y += h - 4
    assert y <= 860, y
    return els


folie([("u1", "5. Unterschiede zum Kauf")], rechts_frei([
    *tafel("u1", "5. Unterschiede zum Kauf"),
    *tabelle(),
    zit("Zeitpunkt: §§ 434 Abs. 1, 446 BGB; BGH VII ZR 301/13, Rn. 32", 110, 755, beim("u4", "Abnahme")),
    *requisit([("u1", ("tabler", "arrows-exchange", 100, WEISS), "Kauf und Werkvertrag", WEISS),
               ("u3", ("tabler", "tools", 100, WERK), "nur im Werkvertrag", WERK),
               ("u5", ("tabler", "calendar-time", 100, WEISS), "Beginn der Verjährung", WEISS)]),
    *paar("u1", [("u1", "ruhig"), ("u3", "froh"), ("u5", "denkt")], [("u1", "ruhig"), ("u2", "froh")]),
]))

# ===========================================================================================================================
# K Ergebnis
# ===========================================================================================================================
folie([("erg", "Ergebnis")], rechts_frei([
    *tafel("erg", "Ergebnis"),
    *okz("Frist zur Nacherfüllung setzen: schriftlich,", 190, "erg", "Bold", 34, x=160),
    z("angemessen, etwa 2 Wochen", 160, 240, beim("erg", "etwa"), "Bold", 34),
    *okz("ergebnislos abgelaufen: anderen Dachdecker", 320, "erg2", "Bold", 34, x=160),
    z("beauftragen, § 637 Abs. 1 BGB", 160, 370, beim("erg2", "beauftragen"), "Bold", 34),
    blk(110, 450, 1040, 130, GRUEN, "erg3", [("Vorschuss von Herrn Wenzel:", "ExtraBold", 38, INK),
                                            ("2.400 €, § 637 Abs. 3 BGB", "Bold", 36, INK)]),
    *okz("verjährt ist nichts: 5 Jahre ab Abnahme", 630, "erg4", "Bold", 34, x=160),
    *requisit([("erg", ("tabler", "writing-sign", 100, WEISS), "Frist setzen", GELB),
               ("erg2", ("tabler", "tools", 100, WEISS), "anderer Dachdecker", WEISS),
               ("erg3", ("tabler", "cash-banknote", 110, GRUEN), "2.400 € Vorschuss", GRUEN)]),
    *paar("erg", [("erg", "ruhig"), ("erg3", "froh")], [("erg", "ernst"), ("erg3", "denkt")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Erst die Frist prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Mangel beseitigen lassen ohne vorherige Frist?", 200, 200, beim("tipp", "Hat"), "Bold", 36),
    *neinz("Kosten nach § 637 BGB nicht ersetzt", 290, beim("tipp", "bekommt"), "Bold", 36, x=250),
    z("Deshalb immer zuerst prüfen:", 200, 400, "tipp2", "Bold", 36),
    *okz("Frist zur Nacherfüllung gesetzt?", 480, beim("tipp2", "Frist"), "Bold", 34, x=250),
    *okz("oder entbehrlich, § 637 Abs. 2 BGB?", 550, beim("tipp2", "entbehrlich"), "Bold", 34, x=250),
    dicon("tabler", "hourglass", 980, 820, 130, "tipp2", fuell=GELB),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Klausurschema (progressiv)
# ===========================================================================================================================
REIHEN = [("k1", "I.", "wirksamer Werkvertrag, § 631 BGB", BLAU),
          ("k2", "II.", "Abnahme (grundsätzlich), § 640 BGB", GRUEN),
          ("k3", "III.", "Mangel bei Abnahme, § 633 BGB", GELB),
          ("k4", "IV.", "erfolglose angemessene Frist zur Nacherfüllung oder Entbehrlichkeit", LILA),
          ("k5", "V.", "keine berechtigte Verweigerung durch den Unternehmer", ROT),
          ("k6", "VI.", "Ersatz der erforderlichen Aufwendungen oder Vorschuss, § 637 Abs. 1, 3", WERK),
          ("k7", "VII.", "keine Verjährung, § 634a BGB", KAUF)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Schema: Aufwendungsersatz und Vorschuss, §§ 634 Nr. 2, 637 BGB"), 110, 90, "sch", 46)]
y = 200
for c, r, txt, farbe in REIHEN:
    els_sch += [karte(110, y, 120, 70, c, fill=farbe, rund=14, schatten=5, rand=4),
                z(r, 170 - F("ExtraBold", 36).getlength(r) / 2, y + 11, c, "ExtraBold", 36, rechts=1820),
                z(txt, 265, y + 11, c, "Bold", 36, rechts=1820)]
    y += 104
assert y <= 975, y
folie([("sch", "Schema: §§ 634 Nr. 2, 637 BGB"), ("k1", "Schema › I. Werkvertrag"), ("k2", "Schema › II. Abnahme"),
       ("k3", "Schema › III. Mangel"), ("k4", "Schema › IV. Frist"), ("k5", "Schema › V. keine berechtigte Verweigerung"),
       ("k6", "Schema › VI. Rechtsfolge"), ("k7", "Schema › VII. keine Verjährung")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Im Werkvertrag ", 0), ("wählt der Unternehmer,", "a")], [("wie er nacherfüllt.", 0)]], 750, 290, 44,
                "merke", {"a": beim("merke", "wählt")}),
    *markertext([[("Lässt er die ", 0), ("Frist", "b"), (" verstreichen, darf", 0)],
                 [("der Besteller den Mangel selbst beseitigen lassen", 0)]], 750, 480, 38, "mk2",
                {"b": beim("mk2", "Frist")}),
    *markertext([[("und dafür ", 0), ("Vorschuss", "c"), (" verlangen.", 0)], [("Das gibt es beim Kauf nicht.", 0)]],
                750, 680, 40, "mk3", {"c": beim("mk3", "Vorschuss")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
