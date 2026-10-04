"""Folge 140 · Gefährdung des Straßenverkehrs § 315c: Die 7 Todsünden & Schema – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Reinhold überholt auf einer Landstraße bergauf einen langsamen Lastwagen vor einer Kuppe, ohne Sicht auf den
Gegenverkehr; Gertrud kommt entgegen und verhindert mit einer Vollbremsung den Zusammenstoß. Niemand wird verletzt.
Szenen laut ../SZENENPLAN.md: A1 Überholen vor der Kuppe, A2 am Straßenrand, B Sachverhalt, C Wortlautkarte § 315c Abs. 1
(Auszug) und I. 1., D I. 2. Tathandlung (Nr. 1, Tabelle Nr. 2 a–g), E Wortlautkarten Nr. 2 b und § 5 Abs. 2 S. 1 StVO,
F I. 3. grob verkehrswidrig und rücksichtslos, G I. 4. konkrete Gefahr, H fremde Sachen (750 €), I I. 5. Kombinationen
(Tabelle, Wortlautkarte Abs. 3), J subjektiver Tatbestand im Fall, K Ergebnis, L Klausurtipp (Lexi), M Prüfschema,
N Merksatz (Lexi). Kuppe in Seitenansicht (kuppe_strasse()): Fahrzeuge folgen der Steigung (Icons nur gedreht, nicht
umgezeichnet), Bewegung als Folge kurzer Positionen (fahrt()). Kein Aufprall im Bild: nur Bremsspur-Strich und Warnsymbol.
Zwei Handlungsgeräusche (Überholen, Vollbremsung; ../geraeusche_herkunft.json).
Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz
als eigene Kopie aus Folge 130 (gemeinsame Dateien unverändert); neu: kuppe_strasse(), fz(), fahrt(), strasse_flach().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import mond, laterne, lichtkegel
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_140/"

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
HELLROT = (253, 232, 228, 255)
HELLGRUEN = (232, 247, 233, 255)
LILAHELL = (246, 243, 255, 255)
BLAUHELL = (228, 238, 253, 255)
HOLZ = (214, 160, 110, 255)
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
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
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
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_140/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), als Zitat mit Normangabe;
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 103/109/112) --------------------------------
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


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [ok(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Kreuz davor (zur gesprochenen Verneinung)."""
    return [nein(x - 45, y + 20, cue, gr=gr), z(text, x, y, cue, stil, size, **k)]




# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
import math
ASPH = (200, 200, 198, 255)
GRAS = (205, 234, 196, 255)
XC, HW, HH, T0 = 900, 600, 120, 700          # Kuppe: Scheitel bei x = 900, halbe Breite, Höhe, Fahrbahnoberkante im Flachen
RB = 120                                     # Fahrbahnbreite in der Seitenansicht
SPUR = {"fern": 46, "nah": 114}              # Unterkante der Fahrzeuge: Gegenfahrbahn (hinten) / eigene Spur (vorn)


def tk(x):
    """Fahrbahnoberkante an der Stelle x (Kosinus-Kuppe)."""
    u = (x - XC) / HW
    return T0 - (HH * (1 + math.cos(math.pi * u)) / 2 if abs(u) < 1 else 0.0)


def steig(x):
    return (tk(x + 1) - tk(x - 1)) / 2


def kuppe_strasse(cue):
    """Landstraße über eine Kuppe in Seitenansicht: Asphalt mit gestrichelter Mittellinie, Gras darunter."""
    s = 2
    xs = list(range(30, 1891, 6))
    im = Image.new("RGBA", (1920 * s, 1080 * s))
    dr = ImageDraw.Draw(im)
    dr.polygon([(x * s, (tk(x) + RB + 2) * s) for x in xs] + [(1890 * s, 1000 * s), (30 * s, 1000 * s)], fill=GRAS)
    dr.polygon([(x * s, tk(x) * s) for x in xs] + [(x * s, (tk(x) + RB) * s) for x in reversed(xs)], fill=ASPH)
    dr.line([(x * s, tk(x) * s) for x in xs], fill=INK, width=6 * s, joint="curve")
    dr.line([(x * s, (tk(x) + RB) * s) for x in xs], fill=INK, width=6 * s, joint="curve")
    for x0 in range(40, 1880, 120):
        dr.line([(x * s, (tk(x) + 60) * s) for x in range(x0, x0 + 60, 4)], fill=WEISS, width=8 * s)
    im = im.resize((1920, 1080), Image.LANCZOS)
    im = im.crop((0, 400, 1920, 1003))
    return El(im, 0, 400, cue, "cut", 0.0, None, name="strasse")


def fz(setname, icon, breite, fuell, x, spur, cue, bis=None, spiegeln=False, anim="cut"):
    """Fahrzeug-Icon an der Stelle x auf der Spur (Offset zur Fahrbahnoberkante), um die Steigung gedreht."""
    base = ficon(setname, icon, 0, 0, breite, cue, fuell=fuell, spiegeln=spiegeln)
    sp = base.sprite
    off = SPUR[spur] if isinstance(spur, str) else spur
    a = math.atan(-steig(x))
    rot = sp.rotate(math.degrees(a), expand=True, resample=Image.BICUBIC)
    yb = tk(x) + off
    cx, cy = x - math.sin(a) * sp.height / 2, yb - math.cos(a) * sp.height / 2
    return El(rot, cx - rot.width / 2, cy - rot.height / 2, cue, anim, 0.0, bis, name=f"ficon:{icon}")


def fahrt(setname, icon, breite, fuell, von, nach, start, dauer, n=12, spiegeln=False, bis=None):
    """Bewegung als Folge kurzer Positionen (jeweils um die Steigung gedreht); von/nach = (x, spur-offset)."""
    c, t0 = start
    els = []
    for i in range(n + 1):
        p = i / n
        q = 3 * p * p - 2 * p ** 3
        x = von[0] + (nach[0] - von[0]) * q
        off = von[1] + (nach[1] - von[1]) * q
        a_ = (c, round(t0 + dauer * i / n, 3))
        b_ = (c, round(t0 + dauer * (i + 1) / n, 3)) if i < n else bis
        els.append(fz(setname, icon, breite, fuell, x, off, a_, bis=b_, spiegeln=spiegeln))
    return els


def strichlinie(p0, p1, cue, n=9, breite=6, farbe=INK):
    """Gestrichelte Sichtlinie aus kurzen Linienstücken."""
    els = []
    for i in range(n):
        a, b = i / n, (i + 0.55) / n
        els.append(linienzug([(p0[0] + (p1[0] - p0[0]) * a, p0[1] + (p1[1] - p0[1]) * a),
                              (p0[0] + (p1[0] - p0[0]) * b, p0[1] + (p1[1] - p0[1]) * b)], cue, breite=breite, farbe=farbe))
    return els


STR_O, STR_U = 700, 850                      # flache Straße (Szene A2)
FAHR = 836
FH = 440


def strasse_flach(cue):
    """Flache Landstraße in Seitenansicht mit gestrichelter Mittellinie und Gras (Szene A2)."""
    s = 2
    im = Image.new("RGBA", (1860 * s, (1000 - STR_O) * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, 1860 * s, (STR_U - STR_O) * s), fill=ASPH)
    dr.line((0, 0, 1860 * s, 0), fill=INK, width=6 * s)
    dr.line((0, (STR_U - STR_O) * s, 1860 * s, (STR_U - STR_O) * s), fill=INK, width=6 * s)
    for x in range(10, 1860, 120):
        dr.rounded_rectangle((x * s, 70 * s, (x + 60) * s, 78 * s), 4 * s, fill=WEISS)
    dr.rectangle((0, (STR_U - STR_O + 3) * s, 1860 * s, (1000 - STR_O) * s), fill=GRAS)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, 30, STR_O, cue, "cut", 0.0, None, name="strasse")


BODEN = 860
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"RE": "Reinhold", "GE": "Gertrud"}
NFARBE = {"RE": GRUEN, "GE": LILA}
CW, LW = 210, 270                           # Breite Auto, Lastwagen


def requisit(folge, px=PX):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else None
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, PU, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, PY, c, fill=pf, size=28, anker="m", bis=b))
    return els


def stehend(k, x, folge, unten=FB, hoehe=FR):
    return [*fig(k, x, unten, hoehe, folge), ns(NAME[k], x, unten, folge[0][0], NFARBE[k], d=0.1)]


P = "§ 315c StGB"

# ===========================================================================================================================
# A1 Fall: Überholen vor der Kuppe
# ===========================================================================================================================
RX0, LX_, RX1, RX2 = 330, 600, 860, 950     # Reinhold: Start hinter dem Lastwagen, Lastwagen, auf der Gegenfahrbahn, zurück
GX0, GX1, GX2 = 1780, 1340, 1250            # Gertrud: kommt hinter der Kuppe hervor, beginnt zu bremsen, steht
UEB = beim("ueber", "überholt")
KNAPP = ("knapp", 0.0)
folie([(NULL, "Fall · Auf der Landstraße"), ("kuppe", "Fall · Vor der Kuppe"), ("ueber", "Fall · Reinhold überholt"),
       ("gert", "Fall · Gegenverkehr"), ("brems", "Fall · Vollbremsung"), ("heil", "Fall · Niemand verletzt")], [
    hart(kuppe_strasse(NULL)),
    hart(ficon("tabler", "trees", 150, T0 + 4, 170, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "trees", 1560, T0 + 4, 170, NULL, fuell=GRUEN, anim="cut")),
    hart(ficon("tabler", "tree", 1760, T0 + 4, 130, NULL, fuell=GRUEN, anim="cut")),
    hart(pl("Eine Landstraße am Vormittag", 70, 30, NULL, fill=GELB, size=40)),
    # Reinhold: steht ab 0,0 s hinter dem Lastwagen, schert bei „überholt“ aus, zieht bei „knapp“ zurück nach rechts
    hart(fz("tabler", "car", CW, GRUEN, RX0, "nah", NULL, bis=UEB)),
    *fahrt("tabler", "car", CW, GRUEN, (RX0, SPUR["nah"]), (RX1, SPUR["fern"]), UEB, 1.6, n=16, bis=KNAPP),
    *fahrt("tabler", "car", CW, GRUEN, (RX1, SPUR["fern"]), (RX2, SPUR["nah"]), KNAPP, 0.8, n=8),
    pl("Reinhold hinter einem langsamen Lastwagen", 70, 115, "lkw", fill=GRUEN, size=32),
    ficon("tabler", "clock", RX0, tk(RX0) - 10, 80, "spaet", fuell=WEISS, bis=UEB),
    pl("spät dran für einen Termin", 70, 190, "spaet", fill=WEISS, size=32),
    # Kuppe: keine Sicht auf das, was dahinter kommt
    *[bis_(e, UEB) for e in strichlinie((RX0 + 70, tk(RX0) + 18), (XC - 20, tk(XC) - 14), "kuppe")],
    ficon("tabler", "eye-off", XC, tk(XC) - 18, 80, beim("kuppe", "nicht"), fuell=WEISS, bis=("gert", 0.3)),
    pl("vor der Kuppe: keine Sicht", 70, 265, "kuppe", fill=WEISS, size=32),
    szene(pl("überholt trotzdem", 70, 340, UEB, fill=HELLROT, size=32), "140ueberholen*", 0.9, 0.0),
    # Gertrud kommt hinter der Kuppe entgegen und bremst voll; kein Zusammenstoß (nur Bremsspur und Warnsymbol)
    *fahrt("tabler", "car", CW, LILA, (GX0, SPUR["fern"]), (GX1, SPUR["fern"]), ("gert", 0.3), 1.8, n=14, spiegeln=True,
           bis=("brems", 0.0)),
    *fahrt("tabler", "car", CW, LILA, (GX1, SPUR["fern"]), (GX2, SPUR["fern"]), ("brems", 0.0), 0.7, n=6, spiegeln=True),
    pl("Gertrud kommt entgegen", 1180, 40, beim("gert", "Gertrud"), fill=LILA, size=32),
    szene(pl("Vollbremsung", 1180, 115, beim("brems", "Vollbremsung"), fill=HELLROT, size=32), "140bremsung*", 0.9, -0.3),
    linienzug([(x, tk(x) + SPUR["fern"] - 6) for x in range(GX2 + CW // 2, 1600, 20)], beim("brems", "Vollbremsung"),
              breite=7, farbe=INK),
    ficon("fluent-emoji-flat", "warning", 1060, tk(1060) - 40, 90, beim("brems", "Vollbremsung")),
    pl("knapp zurück nach rechts", 70, 415, KNAPP, fill=WEISS, size=32),
    pl("kein Zusammenstoß, niemand verletzt", 1180, 190, "heil", fill=GRUEN, size=32),
    # Lastwagen zuletzt (vorn, eigene Spur)
    hart(fz("tabler", "truck", LW, WEISS, LX_, "nah", NULL)),
])

# ===========================================================================================================================
# A2 Fall: am Straßenrand
# ===========================================================================================================================
REX, GEX = 860, 1250                        # Reinhold (blickt nach rechts), Gertrud (blickt nach links)
folie([("rand", "Fall · Am Straßenrand"), ("frage", "Fall · Die Frage")], [
    strasse_flach("rand"),
    ficon("tabler", "trees", 160, STR_O + 4, 170, "rand", fuell=GRUEN, anim="cut"),
    ficon("tabler", "car", 470, FAHR, 300, "rand", fuell=GRUEN, anim="cut"),
    ficon("tabler", "car", 1640, FAHR, 300, "rand", fuell=LILA, spiegeln=True, anim="cut"),
    pl("Kurz darauf am Straßenrand", 70, 30, "rand", fill=GELB, size=40),
    *fig("GE", GEX, FAHR, FH, [("rand", "angst")], bis="g1", erst="pop"),
    *redet("GE_redet", GEX, FAHR, FH, "g1", "r1"),
    *fig("GE", GEX, FAHR, FH, [("r1", "sorge"), ("frage", "still")], erst="cut"),
    ns("Gertrud", GEX, FAHR, "rand", LILA, d=0.2),
    blase("sprech", 640, 210, "g1", 1450, 250, inhalt=["Das war knapp! Ich konnte", "gerade noch bremsen."], textsize=34,
          figur=("GE_redet", GEX, FAHR, FH), bis="r1"),
    *fig("RE", REX, FAHR, FH, [("rand", "still_r")], bis="r1", erst="pop"),
    *redet("RE_redet_r", REX, FAHR, FH, "r1", "frage"),
    *fig("RE", REX, FAHR, FH, [("frage", "sorge_r")], erst="cut"),
    ns("Reinhold", REX, FAHR, "rand", GRUEN, d=0.1),
    blase("sprech", 720, 210, "r1", 640, 250, inhalt=["Ich dachte, da kommt schon keiner.", "Ich musste pünktlich sein."],
          textsize=34, figur=("RE_redet_r", REX, FAHR, FH), bis="frage"),
    pl("§ 315c StGB?", 70, 130, "frage", fill=PINK, size=36),
    pl("Vorsatz oder Fahrlässigkeit?", 70, 215, "frage2", fill=PINK, size=36),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_140(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 20
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_140("sv", [
    "Reinhold fährt an einem Vormittag auf einer Landstraße bergauf hinter einem langsamen Lastwagen. Er ist spät dran für "
    "einen Termin. Vor ihm liegt eine Kuppe; was dahinter kommt, kann er nicht sehen. Er denkt: „Da kommt schon keiner.“ "
    "Um pünktlich zu sein, schert er aus und überholt.",
    "Hinter der Kuppe kommt ihm Gertrud mit ihrem Auto entgegen. Nur weil sie sofort voll bremst, kommt es nicht zum "
    "Zusammenstoß: Wenige Meter vor ihrem Auto zieht Reinhold knapp vor dem Lastwagen zurück nach rechts.",
    "Verletzt wird niemand. Reinhold ist nüchtern.",
], "Hat sich Reinhold nach § 315c StGB strafbar gemacht – vorsätzlich oder fahrlässig?")

# ===========================================================================================================================
# C Überblick: Wortlautkarte § 315c Abs. 1 (Auszug), I. 1. Führen eines Fahrzeugs im Straßenverkehr
# ===========================================================================================================================
W1 = ["„(1) Wer im Straßenverkehr",
      "1. ein Fahrzeug führt, obwohl er a) infolge des Genusses",
      "alkoholischer Getränke … oder b) infolge geistiger oder",
      "körperlicher Mängel nicht in der Lage ist, das Fahrzeug",
      "sicher zu führen, oder",
      "2. grob verkehrswidrig und rücksichtslos a) … g) …,",
      "und dadurch Leib oder Leben eines anderen Menschen oder",
      "fremde Sachen von bedeutendem Wert gefährdet, wird …",
      "bestraft.“"]
w1, w1_y = wortlaut(80, 160, 1100, W1, "§ 315c Abs. 1 StGB (Auszug)", "p315c", marken=[
    (1, "1. ein Fahrzeug führt", "nr1"), (3, "nicht in der Lage ist", beim("nr1", "fahruntüchtigen")),
    (5, "2. grob verkehrswidrig und rücksichtslos a) … g)", "nr2"),
    (6, "und dadurch Leib oder Leben eines anderen Menschen", "gef"),
    (7, "fremde Sachen von bedeutendem Wert", beim("gef", "fremde")),
    (0, "im Straßenverkehr", "fuehr")], size=30)
folie([("p315c", f"{P} › Überblick Abs. 1"), ("nr1", f"{P} › Nr. 1: Fahruntüchtigkeit"),
       ("nr2", f"{P} › Nr. 2: sieben Verkehrsverstöße"), ("gef", f"{P} › konkrete Gefahr"),
       ("fuehr", f"{P} › I. 1. Führen eines Fahrzeugs im Straßenverkehr")], rechts_frei([
    *tafel("p315c", "§ 315c Abs. 1 StGB: zwei Wege", h=w1_y + 110 - 60),
    *w1,
    *okz("1. Führen eines Fahrzeugs im Straßenverkehr: (+)", w1_y + 30, beim("fuehr", "Auto"), "Bold", 32, x=160),
    *requisit([("p315c", ("tabler", "book", 100, WEISS), "§ 315c Abs. 1 StGB", GELB),
               ("nr1", ("tabler", "steering-wheel", 100, WEISS), "Nr. 1: fahruntüchtig", WEISS),
               ("nr2", ("tabler", "list-numbers", 100, WEISS), "Nr. 2: 7 Verstöße", WEISS),
               ("gef", ("tabler", "alert-triangle", 100, GELB), "konkrete Gefahr", HELLROT),
               ("fuehr", ("tabler", "car", 150, GRUEN), "Führen (+)", GRUEN)]),
    *stehend("RE", X1, [("p315c", "ruhig"), ("gef", "ernst")]),
    *stehend("GE", X2, [("p315c", "ruhig"), ("gef", "sorge")]),
]))

# ===========================================================================================================================
# D I. 2. Tathandlung: Nr. 1 (−), Nr. 2 a–g als Tabelle
# ===========================================================================================================================
PT = "I. 2. Tathandlung"
TAB = [("ta", "a)", ["Vorfahrt nicht beachtet"]),
       ("tb", "b)", ["falsch überholt"]),
       ("tc", "c)", ["an Fußgängerüberwegen falsch gefahren"]),
       ("td", "d)", ["zu schnell an unübersichtlichen Stellen, Kreuzungen,", "Einmündungen und Bahnübergängen"]),
       ("te", "e)", ["an unübersichtlichen Stellen nicht rechts gefahren"]),
       ("tf", "f)", ["Autobahn, Kraftfahrstraße: gewendet, rückwärts oder", "entgegen der Fahrtrichtung gefahren"]),
       ("tg", "g)", ["haltende oder liegengebliebene Fahrzeuge nicht kenntlich gemacht"])]
els_t = [*tafel("th", "2. Tathandlung"),
         *neinz("Nr. 1: Reinhold nüchtern und fahrtüchtig (−)", 165, "nr1b", "Bold", 32, x=160),
         zit("zur Fahruntüchtigkeit: Folge 130, § 316 StGB", 160, 213, beim("nr1b", "Fahruntüchtigkeit")),
         z("Nr. 2: die „sieben Todsünden“ (Lehrbuchbegriff)", 110, 270, "tods", "Bold", 32)]
y = 330
for c, bu, zeilen in TAB:
    els_t.append(z(bu, 130, y, c, "ExtraBold", 30))
    for i, t in enumerate(zeilen):
        els_t.append(z(t, 185, y + i * 44, c, size=30))
    y += 44 * len(zeilen) + 14
els_t.append(z("andere Verstöße: nicht von Nr. 2 erfasst", 110, y + 8, "liste", "Bold", 32))
assert y + 60 <= 900, y
folie([("th", f"{P} › {PT}"), ("nr1b", f"{P} › {PT} › Nr. 1 (−)"), ("tods", f"{P} › {PT} › Nr. 2: „sieben Todsünden“"),
       ("liste", f"{P} › {PT} › Nr. 2 abschließend")], rechts_frei([
    *els_t,
    *requisit([("th", ("tabler", "car", 150, GRUEN), "Tathandlung?", WEISS),
               ("nr1b", ("tabler", "steering-wheel", 100, WEISS), "Nr. 1 (−)", HELLROT),
               ("tods", ("tabler", "list-numbers", 100, WEISS), "7 Todsünden", GELB),
               ("liste", ("tabler", "ban", 100, ROT), "sonst: nein", WEISS)]),
    *stehend("RE", FX, [("th", "ruhig"), ("tods", "denkt"), ("tb", "ernst")]),
]))

# ===========================================================================================================================
# E Wortlautkarten Nr. 2 b und § 5 Abs. 2 S. 1 StVO
# ===========================================================================================================================
PB = f"{PT} › Nr. 2 b"
W2 = ["„Wer im Straßenverkehr … 2. grob verkehrswidrig und",
      "rücksichtslos … b) falsch überholt oder sonst bei",
      "Überholvorgängen falsch fährt, …“"]
w2, w2_y = wortlaut(80, 160, 1100, W2, "§ 315c Abs. 1 Nr. 2 b StGB", "p2b", marken=[
    (1, "b) falsch überholt", beim("p2b", "falsch")), (1, "oder sonst bei", beim("p2b", "sonst")),
    (2, "Überholvorgängen falsch fährt", beim("p2b", "Überholvorgängen"))], size=32)
W5 = ["„Überholen darf nur, wer übersehen kann, dass während",
      "des ganzen Überholvorgangs jede Behinderung des",
      "Gegenverkehrs ausgeschlossen ist.“"]
w5, w5_y = wortlaut(80, w2_y + 24, 1100, W5, "§ 5 Abs. 2 S. 1 StVO", "stvo", marken=[
    (0, "übersehen kann", beim("stvo", "übersehen")), (1, "jede Behinderung des", beim("stvo", "Gegenverkehr")),
    (2, "Gegenverkehrs", beim("stvo", "Gegenverkehr"))], size=32)
folie([("p2b", f"{P} › {PB}: falsch überholt"), ("stvo", f"{P} › {PB} › § 5 Abs. 2 S. 1 StVO"),
       ("sicht", f"{P} › {PB} › vor der Kuppe: keine Sicht"), ("falsch", f"{P} › {PB} (+)")], rechts_frei([
    *tafel("p2b", "Nr. 2 b: falsch überholt"),
    *w2, *w5,
    *neinz("vor der Kuppe: keine Sicht auf den Gegenverkehr", w5_y + 26, "sicht", "Bold", 32, x=160),
    blk(110, w5_y + 96, 1040, 80, GELB, "falsch", [("Reinhold hat falsch überholt: Nr. 2 b (+)", "ExtraBold", 34, INK)]),
    *requisit([("p2b", ("tabler", "car", 150, GRUEN), "Überholen", WEISS),
               ("stvo", ("tabler", "book", 100, WEISS), "§ 5 StVO", GELB),
               ("sicht", ("tabler", "eye-off", 100, WEISS), "keine Sicht", HELLROT),
               ("falsch", ("tabler", "car", 150, GRUEN), "Nr. 2 b (+)", GRUEN)]),
    *stehend("RE", FX, [("p2b", "ruhig"), ("sicht", "denkt"), ("falsch", "still")]),
]))

# ===========================================================================================================================
# F I. 3. grob verkehrswidrig und rücksichtslos
# ===========================================================================================================================
PG = "I. 3. grob verkehrswidrig und rücksichtslos"
folie([("grob", f"{P} › {PG}"), ("grob2", f"{P} › I. 3. grob verkehrswidrig: objektiv"),
       ("rueck", f"{P} › I. 3. rücksichtslos: subjektiv"), ("rein", f"{P} › I. 3. Reinhold (+)")], rechts_frei([
    *tafel("grob", "3. grob verkehrswidrig, rücksichtslos"),
    z("grob verkehrswidrig: objektiv", 110, 175, "grob2", "Bold", 34),
    z("besonders gefährlicher Verstoß", 110, 222, beim("grob2", "besonders"), size=32),
    zit("OLG Koblenz, Beschl. v. 20.7.2023 – 4 ORs 4 Ss 16/23; BGH 4 StR 225/20, Rn. 14", 110, 266,
        beim("grob2", "Verstoß")),
    *okz("Überholen ohne jede Sicht auf den Gegenverkehr", 318, "grob3", size=32, x=160),
    linienzug([(130, 390), (1130, 390)], "rueck", breite=3),
    z("rücksichtslos: subjektiv", 110, 410, "rueck", "Bold", 34),
    z("aus eigensüchtigen Gründen bewusst über Pflichten hinweg", 110, 460, beim("rueck", "eigensüchtigen"), size=32),
    z("oder aus Gleichgültigkeit Bedenken nicht aufkommen lassen", 110, 506, "gleich", size=32),
    zit("BGH, Urt. v. 14.3.2024 – 4 StR 354/23, Rn. 29 (nach BGHSt 5, 392, 395)", 110, 552, beim("gleich", "Gleichgültigkeit")),
    z("Vertrauen auf einen guten Ausgang: hilft nicht", 110, 602, "vertr", "Bold", 32),
    blk(110, 660, 1040, 120, GRUEN, "rein", [("Reinhold kannte die fehlende Sicht und", "ExtraBold", 32, INK),
                                            ("überholte, um pünktlich zu sein: (+)", "ExtraBold", 32, INK)]),
    *requisit([("grob", ("tabler", "car", 150, GRUEN), "grob? rücksichtslos?", WEISS),
               ("grob2", ("tabler", "alert-triangle", 100, ROT), "objektiv", WEISS),
               ("rueck", ("tabler", "clock", 100, WEISS), "subjektiv: Motive", WEISS),
               ("rein", ("tabler", "clock", 100, WEISS), "pünktlich sein", GRUEN)]),
    *stehend("RE", FX, [("grob", "ruhig"), ("rueck", "denkt"), ("rein", "still")]),
]))

# ===========================================================================================================================
# G I. 4. konkrete Gefahr
# ===========================================================================================================================
PK = "I. 4. Konkrete Gefahr"
folie([("gefahr", f"{P} › {PK}"), ("beinahe", f"{P} › {PK} › Beinahe-Unfall"),
       ("gert2", f"{P} › {PK} › Gertrud: Leib und Leben (+)"), ("dadurch", f"{P} › {PK} › gerade durch das Überholen")],
      rechts_frei([
    *tafel("gefahr", "4. Konkrete Gefahr"),
    z("Beinahe-Unfall: Schaden hängt nur noch vom Zufall ab", 110, 180, "beinahe", "Bold", 32),
    z("Beobachter: „Das ist noch einmal gut gegangen.“", 110, 228, beim("beinahe", "Beobachter"), size=32),
    zit("BGH, Beschl. v. 19.6.2024 – 4 StR 73/24, Rn. 6; 4 StR 391/24, Rn. 4", 110, 276, beim("beinahe", "Beobachter")),
    blk(110, 330, 1040, 120, LILA, "gert2", [("Gertrud bremst sofort voll: kein Zusammenstoß,", "ExtraBold", 32, INK),
                                             ("die Autos verfehlen sich um wenige Meter", "ExtraBold", 32, INK)]),
    *okz("Leib und Leben von Gertrud konkret gefährdet", 490, beim("gert2", "Ihr"), "Bold", 32, x=160),
    *okz("Gefahr folgt gerade aus dem falschen Überholen", 560, "dadurch", size=32, x=160),
    zit("„und dadurch“: BGH, Beschl. v. 19.6.2024 – 4 StR 73/24, Rn. 9", 160, 608, beim("dadurch", "falschen")),
    *requisit([("gefahr", ("tabler", "alert-triangle", 100, GELB), "konkrete Gefahr?", WEISS),
               ("beinahe", ("fluent-emoji-flat", "warning", 100, None), "Beinahe-Unfall", HELLROT),
               ("dadurch", ("tabler", "car", 150, GRUEN), "durch das Überholen", WEISS)]),
    *stehend("GE", FX, [("gefahr", "ruhig"), ("gert2", "angst"), ("dadurch", "still")]),
]))

# ===========================================================================================================================
# H fremde Sachen von bedeutendem Wert, Tatfahrzeug, Mitfahrer
# ===========================================================================================================================
folie([("sache", f"{P} › {PK} › fremde Sachen von bedeutendem Wert"), ("wert", f"{P} › {PK} › Wertgrenze 750 €"),
       ("eigen", f"{P} › {PK} › Tatfahrzeug zählt nicht"), ("mitf", f"{P} › {PK} › Mitfahrer")], rechts_frei([
    *tafel("sache", "4. Konkrete Gefahr: fremde Sachen"),
    z("1. Sache von bedeutendem Wert", 110, 180, "sache", "Bold", 34),
    z("2. drohender bedeutender Schaden", 110, 232, beim("sache", "drohenden"), "Bold", 34),
    blk(110, 300, 1040, 80, GELB, "wert", [("Grenze jeweils: 750 €", "ExtraBold", 36, INK)]),
    zit("BGH, Beschl. v. 10.4.2019 – 4 StR 86/19, Rn. 7; 4 StR 391/24, Rn. 4", 110, 402, "wert"),
    *neinz("vom Täter geführtes Fahrzeug: zählt nicht, auch wenn fremd", 465, "eigen", size=32, x=160),
    zit("BGH 4 StR 86/19, Rn. 8; BGH 4 StR 435/12, Rn. 5", 160, 513, beim("eigen", "Fahrzeug")),
    z("Mitfahrer: geschützt, wenn nicht an der Tat beteiligt", 160, 575, "mitf", size=32),
    zit("BGH 4 StR 73/24, Rn. 7; BGH 4 StR 435/12, Rn. 6", 160, 623, beim("mitf", "beteiligt")),
    *requisit([("sache", ("tabler", "coin", 100, GELB), "fremde Sache", WEISS),
               ("wert", ("tabler", "currency-euro", 100, GELB), "750 €", GELB),
               ("eigen", ("tabler", "car-off", 130, WEISS), "Tatfahrzeug", HELLROT),
               ("mitf", ("tabler", "users", 110, WEISS), "Mitfahrer", WEISS)]),
    *stehend("GE", FX, [("sache", "ruhig")]),
]))

# ===========================================================================================================================
# I I. 5. Vorsatz-Fahrlässigkeits-Kombinationen (Tabelle, Wortlautkarte Abs. 3)
# ===========================================================================================================================
PS_ = "I. 5. Subjektiver Tatbestand"
SP_ = (130, 420, 730, 980)
els_k = [*tafel("kombi", "5. Vorsatz und Fahrlässigkeit"),
         *[z(t, x, 170, "kombi", "ExtraBold", 30) for t, x in zip(("Handlung", "Gefahr", "Norm", "Strafe bis"), SP_)],
         linienzug([(120, 214), (1140, 214)], "kombi", breite=3)]
for i, (c, h, g, n_, st) in enumerate([("kvv", "Vorsatz", "Vorsatz", "Abs. 1", "5 Jahre"),
                                       ("kvf", "Vorsatz", "Fahrlässigkeit", "Abs. 3 Nr. 1", "2 Jahre"),
                                       ("kff", "Fahrlässigkeit", "Fahrlässigkeit", "Abs. 3 Nr. 2", "2 Jahre")]):
    yy = 232 + i * 52
    for t, x in zip((h, g, n_), SP_):
        els_k.append(z(t, x, yy, c, "Bold" if c == "kvf" else "Regular", 30))
    els_k.append(z(st, SP_[3], yy, "rahmen", "Bold", 30))
W3 = ["„(3) Wer in den Fällen des Absatzes 1",
      "1. die Gefahr fahrlässig verursacht oder",
      "2. fahrlässig handelt und die Gefahr fahrlässig verursacht,",
      "wird mit Freiheitsstrafe bis zu zwei Jahren oder mit",
      "Geldstrafe bestraft.“"]
w3, w3_y = wortlaut(80, 420, 1100, W3, "§ 315c Abs. 3 StGB", "kvf", marken=[
    (1, "die Gefahr fahrlässig verursacht", beim("kvf", "Gefahr")), (2, "fahrlässig handelt", "kff"),
    (3, "bis zu zwei Jahren", "rahmen")], size=32)
folie([("kombi", f"{P} › {PS_}"), ("kvv", f"{P} › {PS_} › Abs. 1: Vorsatz/Vorsatz"),
       ("kvf", f"{P} › {PS_} › Abs. 3 Nr. 1: Vorsatz/Fahrlässigkeit"),
       ("kff", f"{P} › {PS_} › Abs. 3 Nr. 2: Fahrlässigkeit/Fahrlässigkeit")], rechts_frei([
    *els_k, *w3,
    *requisit([("kombi", ("tabler", "scale", 110, WEISS), "3 Kombinationen", WEISS),
               ("kvf", ("tabler", "book", 100, WEISS), "§ 315c Abs. 3", GELB),
               ("rahmen", ("tabler", "gavel", 100, HOLZ), "5 oder 2 Jahre", WEISS)]),
    *stehend("RE", FX, [("kombi", "ruhig"), ("kvf", "denkt")]),
]))

# ===========================================================================================================================
# J subjektiver Tatbestand im Fall: Abs. 3 Nr. 1
# ===========================================================================================================================
folie([("gvors", f"{P} › {PS_} › Gefährdungsvorsatz?"), ("rein2", f"{P} › {PS_} › Reinhold: Handlung vorsätzlich"),
       ("fahrl", f"{P} › {PS_} › Gefahr fahrlässig: Abs. 3 Nr. 1")], rechts_frei([
    *tafel("gvors", "5. Subjektiver Tatbestand im Fall"),
    z("Gefährdungsvorsatz: Beinahe-Unfall für möglich halten", 110, 180, "gvors", "Bold", 32),
    z("und billigend in Kauf nehmen", 110, 228, beim("gvors", "billigend"), "Bold", 32),
    zit("BGH, Beschl. v. 27.3.2024 – 4 StR 493/23, Rn. 14", 110, 276, beim("gvors", "billigend")),
    *okz("bewusst ohne Sicht überholt: Handlung vorsätzlich", 340, "rein2", size=32, x=160),
    *neinz("vertraute, dass niemand kommt: kein Gefährdungsvorsatz", 405, beim("rein2", "vertraute"), size=32, x=160),
    *okz("Gegenverkehr vorhersehbar: Gefahr fahrlässig", 470, "fahrl", size=32, x=160),
    blk(110, 545, 1040, 80, LILA, beim("fahrl", "Absatz"), [("§ 315c Abs. 1 Nr. 2 b, Abs. 3 Nr. 1 StGB", "ExtraBold", 34, INK)]),
    *requisit([("gvors", ("tabler", "help-circle", 100, WEISS), "Vorsatz zur Gefahr?", WEISS),
               ("rein2", ("tabler", "eye-off", 100, WEISS), "„kommt schon keiner“", WEISS),
               ("fahrl", ("tabler", "alert-triangle", 100, GELB), "fahrlässig", LILA)]),
    *stehend("RE", FX, [("gvors", "ruhig"), ("rein2", "denkt"), ("fahrl", "sorge")]),
]))

# ===========================================================================================================================
# K II., III., Konkurrenzen, Ergebnis
# ===========================================================================================================================
folie([("rws", "II. Rechtswidrigkeit · III. Schuld"), ("konk", "Konkurrenzen · § 316 tritt zurück"),
       ("erg", "Ergebnis · § 315c Abs. 1 Nr. 2 b, Abs. 3 Nr. 1 StGB"), ("fe", "Ergebnis · § 69 Abs. 2 Nr. 1 StGB")],
      rechts_frei([
    *tafel("rws", "Ergebnis"),
    *okz("II. Rechtswidrigkeit, III. Schuld: unproblematisch", 175, "rws", "Bold", 32, x=160),
    z("Konkurrenzen: § 316 tritt hinter § 315c zurück", 110, 250, "konk", "Bold", 32),
    zit("§ 316 Abs. 1 StGB a. E.", 110, 298, beim("konk", "zurück")),
    z("Reinhold ist strafbar nach", 110, 365, "erg", "Bold", 36),
    blk(110, 425, 1040, 80, GELB, beim("erg", "Paragraf"), [("§ 315c Abs. 1 Nr. 2 b, Abs. 3 Nr. 1 StGB", "ExtraBold", 36, INK)]),
    z("Fahrerlaubnis in der Regel entzogen: § 69 Abs. 2 Nr. 1 StGB", 110, 545, "fe", "Bold", 32),
    *requisit([("erg", ("tabler", "gavel", 100, HOLZ), "Ergebnis", GRUEN), ("fe", ("tabler", "id", 100, WEISS), "Fahrerlaubnis", WEISS)]),
    *stehend("RE", X1, [("rws", "ruhig"), ("erg", "muede")]),
    *stehend("GE", X2, [("rws", "ruhig"), ("erg", "still")]),
]))

# ===========================================================================================================================
# L Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zwei getrennte Merkmale"), ("tipp2", "Klausurtipp · Motive des Fahrers"),
       ("tipp3", "Klausurtipp · Beinahe-Unfall mit Tatsachen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("grob verkehrswidrig und rücksichtslos:", 200, 200, beim("tipp", "Grob"), "Bold", 34),
    z("zwei getrennte Merkmale", 200, 248, beim("tipp", "getrennte"), size=34),
    z("Rücksichtslosigkeit: mit den Motiven begründen", 200, 310, "tipp2", "Bold", 34),
    zit("BGH 4 StR 354/23, Rn. 30; OLG Koblenz 4 ORs 4 Ss 16/23", 200, 360, beim("tipp2", "Motiven")),
    linienzug([(130, 420), (1130, 420)], "tipp3", breite=3),
    z("Beinahe-Unfall mit Tatsachen belegen:", 200, 445, "tipp3", "Bold", 34),
    z("Abstände, Geschwindigkeiten", 200, 495, beim("tipp3", "Abständen"), size=34),
    z("„stark gebremst“ allein genügt nicht", 200, 545, beim("tipp3", "stark"), size=34),
    zit("BGH, Beschl. v. 2.2.2023 – 4 StR 293/22, Rn. 6", 200, 595, beim("tipp3", "stark")),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# M Prüfschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Tatbestand", True),
          (beim("s1", "Führen"), 1, "1. Führen eines Fahrzeugs im Straßenverkehr", False),
          ("s1b", 1, "2. Tathandlung: Nr. 1 oder Nr. 2 a–g", False),
          ("s1c", 2, "bei Nr. 2: grob verkehrswidrig und rücksichtslos", False),
          ("s1d", 1, "3. konkrete Gefahr, verursacht durch die Tathandlung", False),
          ("s1e", 1, "4. Vorsatz oder Kombination nach Abs. 3", False),
          ("s2", 0, "II. Rechtswidrigkeit  ·  III. Schuld", True),
          ("s3", 0, "Konkurrenzen", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfschema: Gefährdung des Straßenverkehrs"), 110, 90, "sch", 46),
           z("§ 315c StGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 240
for c, ebene, text, fett in REIHEN:
    x = (130, 200, 270)[ebene]
    if c == "s1b":
        els_sch.append(karte(180, y - 16, 1640, 160, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 96, 1: 80, 2: 80}[ebene]
assert y <= 970, y
folie([("sch", "Prüfschema"), ("s1", "Prüfschema › I. Tatbestand"), ("s1b", "Prüfschema › I. 2. Tathandlung"),
       ("s1d", "Prüfschema › I. 3. konkrete Gefahr"), ("s1e", "Prüfschema › I. 4. Vorsatz/Fahrlässigkeit"),
       ("s2", "Prüfschema › II. und III."), ("s3", "Prüfschema › Konkurrenzen")], els_sch)

# ===========================================================================================================================
# N Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("§ 315c Abs. 1 Nr. 2", 0)], [("verlangt dreierlei:", 0)]], 750, 290, 44, "merke", {}),
    *markertext([[("eine der sieben Todsünden", "a"), (",", 0)], [("grob verkehrswidrig und rücksichtslos", "b"),
                 (" begangen,", 0)]], 750, 450, 44, "m2", {"a": beim("m2", "Todsünden"), "b": beim("m2", "grob")}),
    *markertext([[("und dadurch einen ", 0), ("Beinahe-Unfall", "c"), (".", 0)]], 750, 600, 44, "m3",
                {"c": beim("m3", "Beinahe")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
