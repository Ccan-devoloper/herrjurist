"""Folge 155 · Schwere Körperverletzung § 226 & Todesfolge § 227 StGB – Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Freitagabend vor einer Bar. Roswitha und Ludger wollen in dasselbe Taxi; Roswitha schlägt Ludger mit der Faust
ins Gesicht, Ludger stürzt rückwärts auf das Pflaster. Variante A: dauerhafter Verlust des Sehvermögens auf dem linken Auge.
Variante B: Ludger stirbt, weil sein Kopf beim Sturz auf das Pflaster schlägt.
Szenen laut ../SZENENPLAN.md: A1 Vor der Bar, A2 Die Varianten, B Sachverhalt, C1 Grunddelikt/Erfolgsqualifikation, C2
Wortlautkarte § 18, D Wortlautkarte § 226 Abs. 1, E Variante A, F Wortlautkarte § 227 Abs. 1, G1 Gefahrzusammenhang/Streit,
G2 Gubener Hetzjagd/älteres Urteil, H Lösung Variante B, I Abgrenzung §§ 212, 222, J Klausurtipp (Lexi), K Prüfungsschema,
L Merksatz (Lexi).
DARSTELLUNG: kein Schlag im Bild, kein Blut, keine Verletzungen, keine Leiche, kein Krankenhausbett; der Faustschlag erscheint
nur als Text-Pille, Ludger sitzt nach dem Sturz benommen auf dem Pflaster (Open-Peeps-Sitzpose, keine Verletzungsdetails).
Die Folgen stehen nur als Text (Pille „Sehvermögen auf einem Auge verloren“; der Tod nur als Text, kein Kreuz, kein Grab).
Gubener Hetzjagd nur als Text mit Fundstelle, keine Darstellung der Beteiligten. Ein Handlungsgeräusch (Taxi fährt vor;
../geraeusche_herkunft.json). Namensschild jeder Figur, solange sie im Bild ist. Hilfsfunktionen glyphen/z/pl/tafel/blk/
wortlaut/redet/fig/ns/okz/neinz als eigene Kopie aus Folge 124 (gemeinsame Dateien unverändert); neu: bar(), pflaster(),
taxischild(), paar(). Zahlen auf Tafeln, Pillen und Blasen als Ziffern."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from engine import pfeil
from ostil import mond, laterne, lichtkegel, bewegt
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_155/"

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
        if n.startswith(("bild:", "ficon:", "bank")) or "/op_155/" in n:
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


# --- Konstanten der Tafelszenen ---------------------------------------------------------------------------------------------
X1, X2 = 1430, 1730                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"RO": "Roswitha", "LU": "Ludger", "LS": "Ludger"}
NFARBE = {"RO": LILA, "LU": GRUEN, "LS": GRUEN}


def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit über den Figuren: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
    els = []
    for i, (c, ic, txt, pf) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        if ic:
            s_, n_, br, fu = ic
            els.append(ficon(s_, n_, px, pu, br, c, fuell=fu, bis=b))
        if txt:
            els.append(pl(txt, px, py, c, fill=pf, size=28, anker="m", bis=b))
    return rechts_frei(els)


def stehend(k, x, folge, bis=None):
    return rechts_frei([*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)])


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) -------------------------------------------------
PFL = 880                                   # Oberkante des Pflasters = Standlinie der Figuren in der Fallszene
WAND = (236, 214, 186, 255)
GRAU = (206, 206, 202, 255)
GLAS = (228, 238, 253, 255)


def _h(c):
    return (lambda e: hart(e)) if c == NULL else (lambda e: e)


def pflaster(cue):
    """Gehweg mit Pflastersteinen (Seitenansicht): graues Band mit Fugen, Tuschekante oben."""
    s = 2
    w, h = 1860, 1000 - PFL
    im = Image.new("RGBA", (w * s, h * s))
    dr = ImageDraw.Draw(im)
    dr.rectangle((0, 0, w * s, h * s), fill=GRAU)
    dr.line((0, 0, w * s, 0), fill=INK, width=6 * s)
    for r, y in enumerate(range(38, h, 38)):
        dr.line((0, y * s, w * s, y * s), fill=(170, 170, 166, 255), width=2 * s)
    for r in range(0, h // 38 + 1):
        for x in range(30 + (r % 2) * 45, w, 90):
            dr.line((x * s, (r * 38 + 4) * s, x * s, (r * 38 + 34) * s), fill=(170, 170, 166, 255), width=2 * s)
    im = im.resize((w, h), Image.LANCZOS)
    return _h(cue)(El(im, 30, PFL, cue, "cut", 0.0, None, name="pflaster"))


def bar(cue):
    """Fassade einer Bar aus Grundformen: Wand, Schaufenster, Tür, Schild „Bar“ (fiktiv, ohne Logo)."""
    s = 2
    x0, y0, w, h = 70, 370, 620, PFL - 370
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    dr = ImageDraw.Draw(im)
    o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=WAND, outline=INK, width=5 * s)
    dr.rectangle((o, o, o + w * s, o + 30 * s), fill=ROT, outline=INK, width=5 * s)            # Dachkante
    dr.rounded_rectangle((o + 60 * s, o + 190 * s, o + 330 * s, o + 420 * s), 10 * s, fill=GLAS, outline=INK, width=5 * s)
    dr.line((o + 195 * s, o + 190 * s, o + 195 * s, o + 420 * s), fill=INK, width=4 * s)
    dr.rounded_rectangle((o + 420 * s, o + 250 * s, o + 560 * s, o + h * s), 8 * s, fill=HOLZ, outline=INK, width=5 * s)
    dr.ellipse((o + 528 * s, o + 380 * s, o + 544 * s, o + 396 * s), fill=INK)
    dr.rounded_rectangle((o + 150 * s, o + 60 * s, o + 470 * s, o + 160 * s), 14 * s, fill=INK)
    f = F("ExtraBold", 64 * s)
    b = f.getbbox("Bar")
    dr.text((o + 310 * s - (b[2] - b[0]) / 2 - b[0], o + 110 * s - (b[3] - b[1]) / 2 - b[1]), "Bar", font=f, fill=GELB)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return _h(cue)(El(im, x0 - 6, y0 - 6, cue, "cut", 0.0, None, name="bar"))


def taxischild(cx, unten, cue, bis=None):
    """Taxischild auf dem Autodach (Grundform: gelbes Schild mit Schriftzug)."""
    s = 2
    w, h = 130, 46
    im = Image.new("RGBA", ((w + 8) * s, (h + 8) * s))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle((4 * s, 4 * s, (w + 4) * s, (h + 4) * s), 10 * s, fill=GELB, outline=INK, width=4 * s)
    f = F("ExtraBold", 30 * s)
    b = f.getbbox("TAXI")
    dr.text(((w / 2 + 4) * s - (b[2] - b[0]) / 2 - b[0], (h / 2 + 4) * s - (b[3] - b[1]) / 2 - b[1]), "TAXI", font=f, fill=INK)
    im = im.resize((im.width // s, im.height // s), Image.LANCZOS)
    return El(im, cx - im.width / 2, unten - im.height, cue, "cut", 0.0, bis, name="taxischild")


def kulisse(c):
    """Fallszene: Bar, Laterne, Mond, Pflaster (für jede Folie neu erzeugt)."""
    h = _h(c)
    return [pflaster(c), bar(c), h(mond(1800, 110, 46, c)),
            h(ficon("tabler", "glass-cocktail", 620, 530, 70, c, fuell=PINK, anim="cut"))]


# ===========================================================================================================================
# A1 Fall: vor der Bar
# ===========================================================================================================================
FH = 440                                    # stehende Figur in der Fallszene
ROX, LUX = 880, 1190                        # Roswitha (blickt nach rechts), Ludger (blickt nach links)
TX, TW = 1580, 380                          # Taxi: Mitte, Breite
TAXI_DA = ("taxi", 1.8)
LSX, LSH = 1230, 300                        # Ludger sitzt nach dem Sturz auf dem Pflaster
folie([(NULL, "Fall · Vor der Bar"), ("taxi", "Fall · Das Taxi"), ("schlag", "Fall · Der Faustschlag"),
       ("sturz", "Fall · Der Sturz")], [
    *kulisse(NULL),
    hart(pl("Freitagabend vor einer Bar", 70, 30, NULL, fill=GELB, size=40)),
    # das Taxi fährt vor (von rechts) und hält
    szene(bewegt(ficon("tabler", "car", TX, PFL, TW, "taxi", fuell=GELB, anim="cut"), "taxi", TAXI_DA, 120, 0),
          "155taxi*", 0.6, 0.0),
    bewegt(taxischild(TX + 10, PFL - 168, "taxi"), "taxi", TAXI_DA, 120, 0),
    pl("beide wollen in dasselbe Taxi", 70, 120, beim("taxi", "dasselbe"), fill=WEISS, size=34, bis="schlag"),
    # Roswitha und Ludger stehen sich gegenüber
    *fig("RO", ROX, PFL, FH, [("taxi", "ruhig_r"), ("l1", "denkt_r")], bis="r1"),
    *redet("RO_redet_r", ROX, PFL, FH, "r1", "schlag"),
    *fig("RO", ROX, PFL, FH, [("schlag", "ernst_r"), ("sturz", "schreck_r")], erst="cut"),
    ns("Roswitha", ROX, PFL, "taxi", LILA, d=0.1),
    peep_voll("LU_ruhig", LUX, PFL, FH, "taxi", anim="pop", bis="l1"),
    *redet("LU_redet", LUX, PFL, FH, "l1", "r1"),
    *fig("LU", LUX, PFL, FH, [("r1", "still"), ("schlag", "sorge")], bis="sturz", erst="cut"),
    bis_(ns("Ludger", LUX, PFL, "taxi", GRUEN, d=0.1), "sturz"),
    blase("sprech", 560, 190, "l1", 1330, 230, inhalt=["Das Taxi habe", "ich bestellt!"], textsize=38,
          figur=("LU_redet", LUX, PFL, FH), bis="r1"),
    blase("sprech", 560, 190, "r1", 1010, 230, inhalt=["Ich war aber", "zuerst hier."], textsize=38,
          figur=("RO_redet_r", ROX, PFL, FH), bis="schlag"),
    # der Faustschlag nur als Text; Ludger sitzt danach benommen auf dem Pflaster
    pl("Faustschlag ins Gesicht", 70, 120, "schlag", fill=HELLROT, size=36),
    pl("will verletzen, mehr nicht", 70, 205, beim("schlag", "Sie"), fill=WEISS, size=34),
    peep_voll("LS_benommen", LSX, PFL + 40, LSH, "sturz", anim="cut"),
    ns("Ludger", LSX, PFL + 40, "sturz", GRUEN, anim="cut"),
    pl("stürzt rückwärts auf das Pflaster", 70, 290, "sturz", fill=WEISS, size=34),
    ficon("tabler", "alert-triangle", LSX - 20, PFL + 40 - LSH - 10, 80, beim("sturz", "stürzt"), fuell=GELB),
])

# ===========================================================================================================================
# A2 Fall: die Varianten und die Frage
# ===========================================================================================================================
folie([("va", "Fall · Variante A"), ("vb", "Fall · Variante B"), ("frage", "Fall · Die Frage")], rechts_frei([
    *tafel("va", "Zwei Varianten"),
    karte(110, 180, 1040, 180, "va", fill=HELL, rund=18, schatten=6, rand=4),
    z("Variante A: durch den Schlag, dauerhaft", 140, 200, "va", "ExtraBold", 34),
    pl("Sehvermögen auf einem Auge verloren", 140, 270, beim("va", "Sehvermögen"), fill=GELB, size=34),
    karte(110, 390, 1040, 180, "vb", fill=LILAHELL, rund=18, schatten=6, rand=4),
    z("Variante B: Kopf schlägt beim Sturz aufs Pflaster", 140, 410, "vb", "ExtraBold", 34),
    pl("Ludger stirbt an dieser Kopfverletzung.", 140, 480, beim("vb", "Ludger"), fill=LILA, size=34),
    z("Mit beidem hat Roswitha nicht gerechnet.", 110, 610, "nicht", "Bold", 34),
    pl("Faustschlag, Sturz, verlorenes Auge – oder Tod?", 110, 690, "frage", fill=WEISS, size=34),
    pl("Was ändert die schwere Folge?", 110, 780, "frage2", fill=PINK, size=38),
    *requisit([("va", ("tabler", "eye", 110, WEISS), "Variante A", GELB),
               ("vb", None, "Variante B", LILA),
               ("nicht", ("tabler", "help-circle", 100, WEISS), "nicht gerechnet", WEISS),
               ("frage", ("tabler", "scale", 110, GELB), "schwere Folge?", PINK)]),
    *stehend("RO", FX, [("va", "still"), ("nicht", "schreck"), ("frage", "sorge")]),
]))


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_155(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.30)
        els += e; y += 18
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=32))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_155("sv", [
    "Ein Freitagabend vor einer Bar in der Altstadt. Roswitha und Ludger wollen beide in dasselbe Taxi steigen. Ludger: "
    "„Das Taxi habe ich bestellt!“ Roswitha: „Ich war aber zuerst hier.“",
    "Roswitha schlägt Ludger mit der Faust ins Gesicht. Sie will ihn verletzen, mehr nicht. Ludger stürzt rückwärts auf "
    "das Pflaster.",
    "Variante A: Durch den Schlag verliert Ludger dauerhaft das Sehvermögen auf dem linken Auge; äußerlich ist er nicht "
    "entstellt. Variante B: Beim Sturz schlägt sein Kopf auf das Pflaster, und Ludger stirbt an dieser Kopfverletzung. "
    "Mit beidem hat Roswitha nicht gerechnet.",
], "Wie hat sich Roswitha strafbar gemacht?")

# ===========================================================================================================================
# C1 Grunddelikt und Erfolgsqualifikation
# ===========================================================================================================================
folie([("grund", "Grunddelikt · § 223 StGB"), ("eq", "Erfolgsqualifizierte Delikte · §§ 226, 227 StGB")], rechts_frei([
    *tafel("grund", "Grunddelikt und schwere Folge"),
    *okz("Faustschlag: vorsätzlich körperlich misshandelt", 190, beim("grund", "vorsätzlich"), "Bold", 34, x=160),
    z("Grunddelikt: § 223 StGB", 160, 245, beim("grund", "Paragraf"), size=32),
    z("Einzelheiten: Video „Körperverletzung“", 160, 300, beim("grund", "mehr"), "Bold", 30, farbe=TEXT),
    linienzug([(130, 380), (1130, 380)], "eq", breite=3),
    z("§§ 226, 227 StGB bauen darauf auf:", 110, 410, "eq", "Bold", 34),
    z("erfolgsqualifizierte Delikte", 110, 465, beim("eq", "erfolgsqualifizierte"), "ExtraBold", 36),
    blk(110, 560, 1040, 110, GELB, "formel", [("Grunddelikt  +  schwere Folge", "ExtraBold", 44, INK)]),
    *requisit([("grund", ("tabler", "alert-triangle", 100, GELB), "§ 223 StGB", WEISS),
               ("eq", ("tabler", "plus", 100, WEISS), "Erfolgsqualifikation", GELB)]),
    *stehend("RO", FX, [("grund", "ruhig"), ("eq", "denkt")]),
]))

# ===========================================================================================================================
# C2 Wortlautkarte § 18
# ===========================================================================================================================
W18 = ["„Knüpft das Gesetz an eine besondere Folge der Tat eine",
       "schwerere Strafe, so trifft sie den Täter oder den Teilnehmer",
       "nur, wenn ihm hinsichtlich dieser Folge wenigstens",
       "Fahrlässigkeit zur Last fällt.“"]
w18, w18_y = wortlaut(80, 170, 1100, W18, "§ 18 StGB", "p18", marken=[
    (0, "besondere Folge", beim("p18", "besondere")), (1, "schwerere Strafe", beim("p18", "schwerere")),
    (2, "wenigstens", beim("p18", "wenigstens")), (3, "Fahrlässigkeit", beim("p18", "Fahrlässigkeit"))], size=34)
folie([("p18", "Erfolgsqualifikation › § 18 StGB: wenigstens Fahrlässigkeit")], rechts_frei([
    *tafel("p18", "Die Folge: § 18 StGB"),
    *w18,
    blk(110, w18_y + 40, 1040, 80, BLAU, beim("vf", "Vorsatz"), [("Vorsatz: Grunddelikt", "ExtraBold", 36, INK)]),
    blk(110, w18_y + 140, 1040, 80, GRUEN, beim("vf", "wenigstens"),
        [("wenigstens Fahrlässigkeit: schwere Folge", "ExtraBold", 36, INK)]),
    *requisit([("p18", ("tabler", "book", 100, WEISS), "§ 18 StGB", GELB),
               ("vf", ("tabler", "scale", 100, GELB), "Vorsatz + Fahrlässigkeit", WEISS)]),
    *stehend("RO", FX, [("p18", "ruhig"), ("vf", "denkt")]),
]))

# ===========================================================================================================================
# D Wortlautkarte § 226 Abs. 1
# ===========================================================================================================================
W226 = ["„(1) Hat die Körperverletzung zur Folge, daß die verletzte Person",
        "1. das Sehvermögen auf einem Auge oder beiden Augen, das Gehör,",
        "    das Sprechvermögen oder die Fortpflanzungsfähigkeit verliert,",
        "2. ein wichtiges Glied des Körpers verliert oder dauernd nicht mehr",
        "    gebrauchen kann oder",
        "3. in erheblicher Weise dauernd entstellt wird oder in Siechtum,",
        "    Lähmung oder geistige Krankheit oder Behinderung verfällt,",
        "so ist die Strafe Freiheitsstrafe von einem Jahr bis zu zehn Jahren.“"]
w226, w226_y = wortlaut(80, 160, 1100, W226, "§ 226 Abs. 1 StGB", "p226", marken=[
    (1, "Sehvermögen auf einem Auge", beim("nr1", "Sehvermögens")), (3, "wichtiges Glied", beim("nr2", "wichtiges")),
    (3, "dauernd nicht mehr", beim("nr2", "dauernd")),
    (5, "in erheblicher Weise dauernd entstellt", beim("nr3", "erhebliche")), (5, "Siechtum", beim("nr3", "Siechtum")),
    (7, "von einem Jahr bis zu zehn Jahren", beim("rahmen1", "ein"))], size=30)
PA = "Variante A › § 226 Abs. 1 StGB"
folie([("p226", PA), ("nr1", f"{PA} › Nr. 1"), ("nr2", f"{PA} › Nr. 2"), ("nr3", f"{PA} › Nr. 3"),
       ("rahmen1", f"{PA} › Strafrahmen")], rechts_frei([
    *tafel("p226", "Schwere Körperverletzung"),
    *w226,
    pl("3 Gruppen schwerer Folgen", 110, w226_y + 30, beim("p226", "drei"), fill=GELB, size=32),
    pl("1 bis 10 Jahre", 640, w226_y + 30, "rahmen1", fill=HELLROT, size=32),
    *requisit([("p226", ("tabler", "book", 100, WEISS), "§ 226 Abs. 1 StGB", GELB),
               ("nr1", ("tabler", "eye", 110, WEISS), "Nr. 1: Sinne, Fortpflanzung", WEISS),
               ("nr2", ("tabler", "hand-stop", 100, WEISS), "Nr. 2: wichtiges Glied", WEISS),
               ("nr3", ("tabler", "alert-triangle", 100, GELB), "Nr. 3: Entstellung u. a.", WEISS),
               ("rahmen1", ("tabler", "scale", 100, GELB), "1 bis 10 Jahre", HELLROT)]),
    *stehend("RO", FX, [("p226", "ruhig"), ("nr3", "denkt"), ("rahmen1", "sorge")]),
]))

# ===========================================================================================================================
# E Variante A: § 226 Abs. 1 Nr. 1, Fahrlässigkeit, Abs. 2
# ===========================================================================================================================
PA1 = "Variante A"
folie([("sub_a", f"{PA1} › Nr. 1: Sehvermögen auf einem Auge"), ("nr23", f"{PA1} › Nr. 2 und 3 (−)"),
       ("fahrl_a", f"{PA1} › Fahrlässigkeit, § 18 StGB"), ("erg_a", f"{PA1} › Ergebnis: § 226 Abs. 1 Nr. 1 StGB"),
       ("abs2", "Abgrenzung · § 226 Abs. 2 StGB: absichtlich oder wissentlich")], rechts_frei([
    *tafel("sub_a", "Variante A: das Auge"),
    z("Ludger: Sehvermögen links dauerhaft verloren", 110, 175, "sub_a", "Bold", 34),
    z("Verlust: Sehkraft faktisch weg, Minderung reicht nicht", 160, 232, "verlust", size=32),
    zit("BGH, Beschl. v. 14.12.2000 – 4 StR 327/00, Rn. 16", 160, 280, beim("verlust", "eine")),
    *okz("Nr. 1 liegt vor", 330, beim("verlust", "Nummer"), "Bold", 34, x=160),
    *neinz("Nr. 2: kein Glied · Nr. 3: nicht entstellt", 395, "nr23", "Bold", 34, x=160),
    *okz("Fahrlässigkeit: Folge vorhersehbar", 460, beim("fahrl_a", "Dass"), "Bold", 34, x=160),
    z("nicht außerhalb aller Lebenserfahrung", 160, 515, beim("fahrl_a", "außerhalb"), size=32),
    zit("Maßstab: BGH, Urt. v. 9.10.2002 – 5 StR 42/02, Rn. 42", 160, 562, beim("fahrl_a", "außerhalb")),
    blk(110, 615, 1040, 80, GRUEN, "erg_a", [("Roswitha: § 226 Abs. 1 Nr. 1 StGB", "ExtraBold", 36, INK)]),
    z("Abs. 2: absichtlich oder wissentlich verursacht:", 110, 725, "abs2", "Bold", 32),
    z("Freiheitsstrafe nicht unter 3 Jahren", 110, 772, beim("abs2", "Freiheitsstrafe"), "Bold", 32),
    *requisit([("sub_a", ("tabler", "eye", 110, WEISS), "Sehvermögen verloren", GELB),
               ("nr23", ("tabler", "x", 90, None), "Nr. 2 und 3 (−)", WEISS),
               ("fahrl_a", ("tabler", "bulb", 100, GELB), "vorhersehbar", WEISS),
               ("erg_a", ("tabler", "gavel", 100, HOLZ), "§ 226 Abs. 1 Nr. 1", GRUEN),
               ("abs2", None, "Abs. 2: mind. 3 Jahre", HELLROT)]),
    *paar("RO", [("sub_a", "still"), ("erg_a", "sorge")], "LU", [("sub_a", "still")]),
]))

# ===========================================================================================================================
# F Variante B: Wortlautkarte § 227 Abs. 1, Kausalität
# ===========================================================================================================================
W227 = ["„(1) Verursacht der Täter durch die Körperverletzung (§§ 223",
        "bis 226a) den Tod der verletzten Person, so ist die Strafe",
        "Freiheitsstrafe nicht unter drei Jahren.“"]
w227, w227_y = wortlaut(80, 170, 1100, W227, "§ 227 Abs. 1 StGB", "p227", marken=[
    (0, "durch die Körperverletzung", beim("p227", "Körperverletzung")), (1, "den Tod", beim("p227", "Tod")),
    (2, "nicht unter drei Jahren", beim("p227", "nicht"))], size=34)
PB = "Variante B"
folie([("p227", f"{PB} › § 227 Abs. 1 StGB"), ("kaus", f"{PB} › Kausalität"),
       ("nurk", f"{PB} › Kausalität genügt nicht")], rechts_frei([
    *tafel("p227", "Variante B: Körperverletzung mit Todesfolge", size=40),
    *w227,
    *okz("Faustschlag, Sturz, Tod: ursächlich", w227_y + 50, "kaus", "Bold", 34, x=160),
    *neinz("bloße Kausalität reicht nicht", w227_y + 120, "nurk", "Bold", 34, x=160),
    *requisit([("p227", ("tabler", "book", 100, WEISS), "§ 227 Abs. 1 StGB", GELB),
               ("kaus", ("tabler", "link", 100, WEISS), "Kausalität (+)", WEISS),
               ("nurk", ("tabler", "help-circle", 100, WEISS), "reicht nicht", HELLROT)]),
    *stehend("RO", FX, [("p227", "still"), ("nurk", "denkt")]),
]))

# ===========================================================================================================================
# G1 Spezifischer Gefahrzusammenhang: Erfolg oder Handlung?
# ===========================================================================================================================
LX0, RX0, SW = 110, 640, 510
PG = f"{PB} › spezifischer Gefahrzusammenhang"
folie([("spez", PG), ("woran", f"{PG} › Streit: Erfolg oder Handlung?"), ("leta", f"{PG} › Letalitätstheorie"),
       ("bgh", f"{PG} › BGH: auch die Handlung")], rechts_frei([
    *tafel("spez", "Spezifischer Gefahrzusammenhang", size=44),
    blk(110, 170, 1040, 120, LILA, "spez", [("Der Körperverletzung haftet die Gefahr an,", "ExtraBold", 32, INK),
                                            ("zum Tod des Opfers zu führen,", "ExtraBold", 32, INK)]),
    z("und gerade diese Gefahr schlägt sich im Tod nieder.", 110, 305, "nieder", "Bold", 32),
    zit("BGH, Urt. v. 9.10.2002 – 5 StR 42/02 (BGHSt 48, 34), Rn. 37; BGHSt 31, 96, 98", 110, 352, beim("nieder", "Gefahr")),
    z("Woran knüpft die Gefahr an?", 110, 405, "woran", "ExtraBold", 34),
    karte(LX0, 460, SW, 300, "leta", fill=HELLROT, rund=18, schatten=6, rand=4),
    z("Letalitätstheorie (Lehre)", LX0 + 25, 475, "leta", "ExtraBold", 30, rechts=LX0 + SW - 10),
    z("Verletzungserfolg selbst", LX0 + 25, 535, beim("leta", "Verletzungserfolg"), size=30, rechts=LX0 + SW - 10),
    z("muss tödlich sein", LX0 + 25, 577, beim("leta", "Verletzungserfolg"), size=30, rechts=LX0 + SW - 10),
    z("Ludger: tödlich war", LX0 + 25, 640, "leta_b", "Bold", 30, rechts=LX0 + SW - 10),
    z("erst der Aufprall", LX0 + 25, 682, beim("leta_b", "Aufprall"), "Bold", 30, rechts=LX0 + SW - 10),
    karte(RX0, 460, SW, 300, "bgh", fill=HELLGRUEN, rund=18, schatten=6, rand=4),
    z("BGH", RX0 + 25, 475, "bgh", "ExtraBold", 30, rechts=RX0 + SW - 10),
    z("auch die Gefahr der", RX0 + 25, 535, beim("bgh", "Gefahr"), size=30, rechts=RX0 + SW - 10),
    z("Körperverletzungshandlung", RX0 + 25, 577, beim("bgh", "Körperverletzungshandlung"), size=30, rechts=RX0 + SW - 10),
    z("Verweis auf §§ 223 bis 226a:", RX0 + 25, 640, "arg", "Bold", 30, rechts=RX0 + SW - 10),
    z("erfasst auch den Versuch", RX0 + 25, 682, beim("arg", "Versuch"), "Bold", 30, rechts=RX0 + SW - 10),
    zit("Rn. 37 f.; 5 StR 435/07, Rn. 8", RX0 + 25, 724, beim("arg", "Versuch"), rechts=RX0 + SW - 10),
    *requisit([("spez", ("tabler", "alert-triangle", 100, GELB), "spezifische Gefahr", LILA),
               ("woran", ("tabler", "arrows-split", 100, WEISS), "Erfolg oder Handlung?", WEISS),
               ("leta", None, "Erfolg tödlich?", HELLROT),
               ("bgh", ("tabler", "scale", 100, GELB), "auch die Handlung", GRUEN)]),
    *stehend("RO", FX, [("spez", "ruhig"), ("woran", "denkt"), ("bgh", "still")]),
]))

# ===========================================================================================================================
# G2 Versuchte Körperverletzung mit Todesfolge: Gubener Hetzjagd; älteres Urteil
# ===========================================================================================================================
folie([("guben", f"{PG} › versuchte Körperverletzung mit Todesfolge"), ("typisch", f"{PG} › Flucht des Opfers"),
       ("aelter", f"{PG} › älteres Urteil: zu restriktiv")], rechts_frei([
    *tafel("guben", "Flucht des Opfers"),
    blk(110, 170, 1040, 80, GELB, "guben", [("versuchte Körperverletzung mit Todesfolge möglich", "ExtraBold", 32, INK)]),
    z("„Gubener Hetzjagd“, 2002:", 110, 280, beim("guben", "So"), "Bold", 34),
    zit("BGH, Urt. v. 9.10.2002 – 5 StR 42/02 (BGHSt 48, 34), Rn. 39 f.", 110, 328, beim("guben", "So")),
    z("Flucht in Todesangst vor einer Gruppe von Angreifern,", 160, 380, "floh", size=32),
    z("dabei tödliche Verletzungen zugezogen", 160, 425, beim("floh", "zog"), size=32),
    *okz("naheliegende, geradezu deliktstypische Reaktion", 490, "typisch", "Bold", 32, x=160),
    *okz("Zusammenhang nicht unterbrochen", 550, beim("typisch", "sie"), "Bold", 32, x=160),
    linienzug([(130, 625), (1130, 625)], "aelter", breite=3),
    z("älteres Urteil: Zurechnung bei Selbstgefährdung verneint", 110, 650, "aelter", size=32),
    zit("BGH, Urt. v. 30.9.1970 – 3 StR 119/70 (NJW 1971, 152)", 110, 698, "aelter"),
    z("2008 „zu restriktiv“", 110, 745, beim("aelter", "zweitausendacht"), "Bold", 32),
    zit("BGH, Urt. v. 10.1.2008 – 5 StR 435/07, Rn. 10", 110, 793, beim("aelter", "zweitausendacht")),
    *requisit([("guben", ("tabler", "book", 100, WEISS), "BGHSt 48, 34", GELB),
               ("typisch", ("tabler", "link", 100, WEISS), "Zusammenhang (+)", GRUEN),
               ("aelter", ("tabler", "calendar-event", 100, WEISS), "1970 / 2008", WEISS)]),
    *stehend("RO", FX, [("guben", "denkt"), ("aelter", "ruhig")]),
]))

# ===========================================================================================================================
# H Lösung Variante B
# ===========================================================================================================================
folie([("sub_b", f"{PB} › Gefahrzusammenhang im Fall"), ("vorh", f"{PB} › Fahrlässigkeit, § 18 StGB"),
       ("erg_b", f"{PB} › Ergebnis: § 227 Abs. 1 StGB"), ("msf", f"{PB} › minder schwerer Fall, § 227 Abs. 2 StGB")],
      rechts_frei([
    *tafel("sub_b", "Variante B: Lösung"),
    z("wuchtiger Faustschlag ins Gesicht: typische Gefahr,", 110, 180, beim("sub_b", "Ein"), "Bold", 32),
    z("dass das Opfer stürzt und mit dem Kopf aufschlägt", 110, 225, beim("sub_b", "dass"), "Bold", 32),
    *okz("Gefahr hat sich im Tod verwirklicht", 295, "gef_ok", "Bold", 34, x=160),
    *okz("Gefahrzusammenhang (+)", 355, beim("gef_ok", "der"), "Bold", 34, x=160),
    *okz("Tod vorhersehbar: nicht außerhalb aller Lebenserfahrung", 425, "vorh", "Bold", 32, x=160),
    z("Einzelheiten des Ablaufs muss sie nicht vorhersehen", 160, 480, beim("vorh", "die"), size=32),
    zit("BGH, Urt. v. 9.10.2002 – 5 StR 42/02, Rn. 42", 160, 527, beim("vorh", "die")),
    blk(110, 590, 1040, 80, GRUEN, "erg_b", [("Roswitha: § 227 Abs. 1 StGB", "ExtraBold", 36, INK)]),
    z("minder schwerer Fall, Abs. 2: 1 bis 10 Jahre", 110, 705, "msf", "Bold", 32),
    *requisit([("sub_b", ("tabler", "alert-triangle", 100, GELB), "typische Gefahr", LILA),
               ("vorh", ("tabler", "bulb", 100, GELB), "vorhersehbar", WEISS),
               ("erg_b", ("tabler", "gavel", 100, HOLZ), "§ 227 Abs. 1 StGB", GRUEN),
               ("msf", ("tabler", "scale", 100, WEISS), "Abs. 2: 1 bis 10 Jahre", WEISS)]),
    *stehend("RO", FX, [("sub_b", "still"), ("erg_b", "sorge")]),
]))

# ===========================================================================================================================
# I Abgrenzung §§ 212, 222
# ===========================================================================================================================
folie([("abgr", "Abgrenzung · § 212 StGB"), ("p222", "Abgrenzung · § 222 StGB")], rechts_frei([
    *tafel("abgr", "Abgrenzung"),
    blk(110, 190, 1040, 120, HELLROT, "abgr", [("Vorsatz bezüglich des Todes:", "Bold", 34, INK),
                                               ("Totschlag, § 212 StGB", "ExtraBold", 36, INK)]),
    blk(110, 350, 1040, 120, LILAHELL, "p222", [("kein Körperverletzungsvorsatz:", "Bold", 34, INK),
                                                ("fahrlässige Tötung, § 222 StGB", "ExtraBold", 36, INK)]),
    z("Überblick: Video „Tötungsdelikte“", 110, 520, "v035", "Bold", 30, farbe=TEXT),
    *requisit([("abgr", ("tabler", "arrows-split", 100, WEISS), "§ 212 StGB", HELLROT),
               ("p222", None, "§ 222 StGB", LILA)]),
    *stehend("RO", FX, [("abgr", "ruhig")]),
]))

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · § 227 nicht mit der Kausalität abhaken"),
       ("tipp2", "Klausurtipp · Schwerpunkt Gefahrzusammenhang"), ("tipp3", "Klausurtipp · § 18 StGB gesondert")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("§ 227 StGB nicht mit der", 200, 200, beim("tipp", "Hake"), "Bold", 36),
    z("Kausalität abhaken", 200, 250, beim("tipp", "Kausalität"), "Bold", 36),
    linienzug([(130, 330), (1130, 330)], "tipp2", breite=3),
    z("Schwerpunkt: Gefahrzusammenhang", 200, 360, "tipp2", "Bold", 36),
    z("Kommt es auf den Streit an (wie bei Ludger):", 200, 420, beim("tipp2", "Kommt"), size=34),
    z("entscheiden.", 200, 470, beim("tipp2", "entscheide"), "Bold", 34),
    linienzug([(130, 545), (1130, 545)], "tipp3", breite=3),
    z("Fahrlässigkeit für die Folge gesondert prüfen,", 200, 575, "tipp3", "Bold", 34),
    z("§ 18 StGB", 200, 625, beim("tipp3", "Paragraf"), "Bold", 34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "I. Tatbestand", True),
          ("s1a", 1, "1. Grunddelikt: vorsätzliche Körperverletzung (§§ 223 bis 226a)", False),
          ("s1b", 1, "2. schwere Folge: Tod", False),
          ("s1c", 1, "3. Kausalität und objektive Zurechnung", False),
          ("s1d", 1, "4. spezifischer Gefahrzusammenhang", True),
          ("s1e", 1, "5. wenigstens Fahrlässigkeit bezüglich der Folge, § 18 StGB", False),
          ("s2", 0, "II. Rechtswidrigkeit", True),
          ("s3", 0, "III. Schuld", True)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Körperverletzung mit Todesfolge"), 110, 90, "sch", 46),
           z("§ 227 Abs. 1 StGB", 110, 160, "sch", "Bold", 32, farbe=TEXT, rechts=1800)]
y = 235
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    if c == "s1d":
        els_sch.append(karte(180, y - 14, 1640, 70, c, fill=HELLGRUEN, rund=16, schatten=5, rand=4))
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 38 if ebene == 0 else 35, rechts=1800))
    y += {0: 80, 1: 72}[ebene]
els_sch.append(blk(130, y + 10, 1660, 80, GELB, "s226", [("§ 226 StGB: an 2. Stelle eine der schweren Dauerfolgen",
                                                          "ExtraBold", 34, INK)]))
assert y + 90 <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › I. Tatbestand"), ("s1a", "Prüfungsschema › I. 1. Grunddelikt"),
       ("s1b", "Prüfungsschema › I. 2. schwere Folge"), ("s1c", "Prüfungsschema › I. 3. Kausalität, Zurechnung"),
       ("s1d", "Prüfungsschema › I. 4. spezifischer Gefahrzusammenhang"),
       ("s1e", "Prüfungsschema › I. 5. Fahrlässigkeit, § 18 StGB"), ("s2", "Prüfungsschema › II. Rechtswidrigkeit"),
       ("s3", "Prüfungsschema › III. Schuld"), ("s226", "Prüfungsschema › § 226 StGB: schwere Dauerfolge")], els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Grunddelikt plus schwere Folge,", 0)], [("für die Folge ", 0), ("wenigstens", "a")],
                 [("Fahrlässigkeit", "a"), (".", 0)]], 750, 290, 44, "merke", {"a": beim("merke", "wenigstens")}),
    *markertext([[("Beim Tod muss sich die", 0)], [("spezifische Gefahr", "b"), (" verwirklichen,", 0)],
                 [("sie kann schon von der Handlung ausgehen.", 0)]], 750, 580, 44, "m2", {"b": beim("m2", "spezifische")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
