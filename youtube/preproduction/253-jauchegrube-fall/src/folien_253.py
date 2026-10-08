"""Folge 253 · Jauchegrube-Fall: dolus generalis oder Versuch plus Fahrlässigkeit? – Serienstandard Open Peeps (Katzenkönig).
Übungsfall (Personen fiktiv), dem echten Fall nachgebildet: Brunhilde greift im Streit am Gartenzaun ihre Nachbarin an und nimmt
deren Tod in Kauf; sie hält die Regungslose für tot, beschließt erst dann, die vermeintliche Leiche verschwinden zu lassen, und
versenkt sie im Teich; erst dort stirbt die bewusstlose Nachbarin. Der echte Fall (BGHSt 14, 193) nur abstrakt als Tafel.
DARSTELLUNG: keine Gewaltszene, kein Würgen, keine Leiche, kein Ertrinken im Bild; die Nachbarin ist keine Figur (auch keine
Silhouette); nur Symbole: leerer Garten hinter dem Zaun, Wasseroberfläche (Ringe), Uhr, Pillen.
Danach zweiaktiges Geschehen, objektiver Tatbestand, § 16 Abs. 1 S. 1 (Wortlautkarte), 1. dolus generalis, 2. BGH (BGHSt 14, 193;
Formel BGH 4 StR 223/15 Rn. 12), 3. Versuchslösung (Lehre), 4. Tatplan (vermittelnd), Ergebnis, Klausurtipp, Schema, Merksatz mit
Lexi. Szenen laut ../SZENENPLAN.md.
Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld/requisit/tisch/fenster als eigene Kopie aus Folge 250
(gemeinsame Dateien unverändert); neu: zaun(), teich().
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut StGB nach gesetze-im-internet.de, Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_253/"

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
HELLGRAU = (226, 226, 222, 255)
TUERKIS_ = (127, 214, 208, 255)
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
        assert g >= 26 and F(s, g).getlength(glyphen(t)) <= w - 30, f"Blockzeile zu breit: {t}"
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
        if n.startswith(("bild:", "ficon:")) or "/op_253/" in n:
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def umbruch(text, size, breite, stil="Regular"):
    f = F(stil, size); zeilen, akt = [], ""
    for w in text.split(" "):
        t = (akt + " " + w).strip()
        if f.getlength(t) <= breite:
            akt = t
        else:
            zeilen.append(akt); akt = w
    return zeilen + [akt]


def wortlaut(x, y, w, text, quelle, cue, marken=(), size=32, bis=None):
    """Wortlautkarte: Normtext wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026), als Zitat mit Normangabe; der
    Zeilenumbruch wird berechnet. marken = [(wort, cue)] legt synchron zum gesprochenen Wort einen Textmarker hinter die
    erste noch nicht markierte Fundstelle von 'wort' (muss in einer Zeile stehen)."""
    zeilen = umbruch(glyphen(text), size, w - 60)
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=ZITAT, rund=18, schatten=6, rand=4), bis)]
    f = F("Regular", size)
    tx, ty = x + 28, y + 26
    belegt = []
    for wort, mc in marken:
        treffer = None
        for zi, t in enumerate(zeilen):
            a = t.find(wort)
            while a >= 0 and (zi, a) in belegt:
                a = t.find(wort, a + 1)
            if a >= 0:
                treffer = (zi, a); break
        assert treffer, f"Marker {wort!r} nicht in einer Zeile: {zeilen}"
        belegt.append(treffer)
        zi, a = treffer; t = zeilen[zi]
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203) -------------------------------------
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
    return pl(text, cx, unten + 22, cue, fill=fill, size=26 if len(text) > 14 else 30, anker="m", **k)


def okz(text, y, cue, stil="Regular", size=34, x=185, gr=20, **k):
    """Tafelzeile mit Bleistift-Haken davor (zur gesprochenen Bejahung)."""
    return [bis_(ok(x - 45, y + 20, cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


def neinz(text, y, cue, stil="Regular", size=34, x=185, gr=20, kreuz=None, **k):
    """Tafelzeile mit Bleistift-Kreuz davor; kreuz = Cue der gesprochenen Verneinung (sonst mit der Zeile)."""
    return [bis_(nein(x - 45, y + 20, kreuz or cue, gr=gr), k.get("bis")), z(text, x, y, cue, stil, size, **k)]


# --- eigene Szenenbausteine (programmatisch, Palettenflächen, Tuschekontur) ---------------------------------------------------
BODEN = 860
FH = 440                                    # stehende Figur in der Fallszene
X1, X2 = 1400, 1720                         # zwei Figuren neben der Tafel
FB, FR = 930, 480                           # Figuren neben der Tafel: Unterkante, Höhe
FX = 1560                                   # eine Figur neben der Tafel
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
PX, PY, PU = 1575, 160, 380                 # Requisit über den Figuren: Mitte, Pillenhöhe, Unterkante
NAME = {"BR": "Brunhilde"}
NFARBE = {"BR": ORANGE}
WAND = (246, 236, 220, 255)


def _flaeche(w, h):
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s))
    return im, ImageDraw.Draw(im), s


def boden(cue):
    return hart(linienzug([(40, BODEN), (1880, BODEN)], cue, breite=7, farbe=INK))

def _feld(w, h, fill=WEISS, rand=4, rund=14):
    im, dr, s = _flaeche(w, h)
    o = 6 * s
    dr.rounded_rectangle((o, o, o + w * s, o + h * s), rund * s, fill=fill, outline=INK, width=rand * s)
    return im.resize((w + 12, h + 12), Image.LANCZOS)


def feld(x, y, w, h, cue, fill=WEISS, rand=4, rund=14, bis=None, anim="cut", name="feld"):
    return El(_feld(w, h, fill, rand, rund), x, y, cue, anim, 0.0, bis, name=name)


def requisit(folge, px=PX, bis=None, pu=PU, py=PY):
    """Wechselndes Requisit rechts der Tafel: folge = [(cue, (set, icon, breite, fuell), pillentext, pillenfarbe)]."""
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
    els = [*fig(k, x, FB, FR, folge, bis=bis), bis_(ns(NAME[k], x, FB, folge[0][0], NFARBE[k], d=0.1), bis)]
    return rechts_frei(els, 1200)


def paar(a, af, b, bf):
    """Tafelszene: zwei Figuren rechts der Tafel (beide blicken nach links zur Tafel)."""
    return [*stehend(a, X1, af), *stehend(b, X2, bf)]




# --- Folge 253: Raumbausteine ---------------------------------------------------------------------------------------------
HOLZ = (214, 160, 110, 255)
WASSER = (120, 170, 222, 255)
SCHILF = (110, 160, 100, 255)
BAUM = (96, 150, 104, 255)
BRX = 1480                                  # Brunhilde in den Fallszenen (blickt nach links zum Zaun bzw. Teich)


def zaun(x0, x1, cue):
    """Gartenzaun: Pfosten und zwei Latten (Tuschekontur, Holzfarbe)."""
    els = [hart(feld(x0 - 10, BODEN - 150, x1 - x0 + 20, 18, cue, fill=HOLZ, rand=4, rund=6, name="latte")),
           hart(feld(x0 - 10, BODEN - 76, x1 - x0 + 20, 18, cue, fill=HOLZ, rand=4, rund=6, name="latte"))]
    for x in range(x0, x1 + 1, 112):
        els.append(hart(feld(x, BODEN - 190, 24, 190, cue, fill=HOLZ, rand=4, rund=6, name="pfosten")))
    return els


def teich(cue):
    """Teich: Wasserfläche im Boden, Schilf am Rand (Tuschekontur, Palettenflächen)."""
    return [hart(feld(110, BODEN - 6, 1060, 130, cue, fill=WASSER, rand=5, rund=40, name="teich")),
            *[hart(ficon("ph", "plant", x, BODEN + 4, 110, cue, fuell=SCHILF, anim="cut")) for x in (150, 1150)]]


def ringe(cue, bis):
    """Wasseroberfläche bewegt: Ringe auf dem Teich (Symbol statt Handlung)."""
    return [bis_(hart(ficon("tabler", "ripple", x, BODEN + 96, w, cue, fuell=None)), bis) for x, w in ((520, 150), (700, 110))]


PF = "Fall"

# ===========================================================================================================================
# A1 Fall: Streit am Gartenzaun – hinter dem Zaun bleibt die Szene leer (die Nachbarin ist keine Figur)
# ===========================================================================================================================
NULL = ("fall", -round(T_("fall"), 3))      # = 0,0 s: erstes Bild nach dem Intro vollständig
folie([(NULL, f"{PF} · Brunhilde und ihre Nachbarin"), ("streit", f"{PF} · Streit am Gartenzaun"),
       ("angriff", f"{PF} · Der Angriff"), ("still", f"{PF} · Regungslos"), ("br1", f"{PF} · „Sie ist tot.“")], [
    boden(NULL),
    hart(ficon("ph", "tree", 150, BODEN - 2, 220, NULL, fuell=BAUM, anim="cut")),
    hart(ficon("ph", "house", 720, BODEN - 2, 250, NULL, fuell=HELLGRAU, anim="cut")),   # Haus der Nachbarin, Szene bleibt leer
    *zaun(330, 1110, NULL),
    *[hart(ficon("ph", "flower-tulip", x, BODEN - 2, 70, NULL, fuell=ROT, anim="cut")) for x in (1230, 1720)],
    bis_(hart(pl("Brunhilde und ihre Nachbarin streiten seit Jahren über den Weg zum Teich.", 70, 30, NULL, fill=GELB, size=31)), "streit"),
    bis_(ficon("tabler", "route", 720, 540, 110, beim("fall", "Weg"), fuell=None), "streit"),
    *fig("BR", BRX, BODEN, FH, [(NULL, "ruhig"), ("streit", "wut"), ("angriff", "ernst"), ("still", "angst")], bis="br1", erst="cut"),
    *redet("BR_redet", BRX, BODEN, FH, "br1", "verst"),
    hart(ns(NAME["BR"], BRX, BODEN, NULL, NFARBE["BR"])),
    bis_(pl("Eines Nachmittags eskaliert der Streit am Gartenzaun.", 70, 30, "streit", fill=ORANGE, size=31), "angriff"),
    bis_(ficon("ph", "sun", 1760, 250, 120, beim("streit", "Nachmittags"), fuell=GELB), None),
    bis_(ficon("tabler", "messages", 720, 540, 120, beim("streit", "eskaliert"), fuell=HELLROT), "angriff"),
    bis_(pl("Brunhilde greift die Nachbarin an.", 70, 30, "angriff", fill=ROT, size=31), "still"),
    bis_(pl("Dass sie dabei sterben kann, nimmt Brunhilde in Kauf.", 70, 94, beim("angriff", "Dass"), fill=WEISS, size=30), "still"),
    bis_(ficon("tabler", "alert-triangle", 720, 540, 110, "angriff", fuell=HELLROT), "still"),
    bis_(pl("Die Nachbarin bleibt regungslos liegen.", 70, 30, "still", fill=BLAUHELL, size=31), "verst"),
    bis_(ficon("tabler", "clock", 720, 540, 110, "still", fuell=WEISS), "br1"),
    blase("sprech", 600, 230, "br1", 1020, 300, inhalt=["Sie atmet nicht mehr.", "Sie ist tot."], textsize=34,
          figur=("BR_redet", BRX, BODEN, FH), bis="verst"),
])

# ===========================================================================================================================
# A2 Fall: am Teich – nur Wasseroberfläche, Uhr, Pillen; kein Körper, kein Ertrinken im Bild
# ===========================================================================================================================
folie([("verst", f"{PF} · Die vermeintliche Leiche"), ("teich", f"{PF} · Im Teich"), ("lebte", f"{PF} · Nur bewusstlos"),
       ("stirbt", f"{PF} · Erst im Wasser stirbt sie")], [
    boden("verst"),
    *teich("verst"),
    hart(ficon("ph", "tree", 1760, BODEN - 2, 200, "verst", fuell=BAUM, anim="cut")),
    *fig("BR", BRX, BODEN, FH, [("verst", "ernst"), ("teich", "muede"), ("lebte", "muede"), ("stirbt", "ruhig")], erst="cut"),
    hart(ns(NAME["BR"], BRX, BODEN, "verst", NFARBE["BR"])),
    bis_(pl("Erst jetzt beschließt Brunhilde, die vermeintliche Leiche verschwinden zu lassen.", 70, 30, "verst", fill=GELB, size=30), "teich"),
    bis_(ficon("tabler", "bulb", BRX, 360, 100, beim("verst", "beschließt"), fuell=GELB), "teich"),
    bis_(pl("Sie versenkt die Nachbarin im Teich.", 70, 30, "teich", fill=BLAUHELL, size=31), "lebte"),
    *ringe(beim("teich", "versenkt"), "stirbt"),
    bis_(pl("Doch die Nachbarin war nur bewusstlos.", 70, 30, "lebte", fill=WEISS, size=31), "stirbt"),
    bis_(ficon("ph", "heartbeat", 620, 560, 120, beim("lebte", "bewusstlos"), fuell=HELLROT), "stirbt"),
    pl("Erst im Wasser stirbt sie.", 70, 30, "stirbt", fill=ROT, size=31),
    ficon("tabler", "clock", 620, 560, 110, "stirbt", fuell=WEISS),
])

# ===========================================================================================================================
# A3 Die Frage
# ===========================================================================================================================
folie([("frage", "Die Frage · Tötungsvorsatz, aber beim Versenken?"), ("frage2", "Die Frage · Vollendung oder Versuch?")], [
    *tafel("frage", "Die Frage"),
    z("Brunhilde wollte die Nachbarin töten.", 110, 200, "frage", "Bold", 38),
    z("Beim Versenken hielt sie sie schon für tot.", 110, 260, beim("frage", "Doch"), "Bold", 38),
    blk(110, 360, 1040, 90, GELB, "frage2", [("Vollendeter Totschlag?", "ExtraBold", 36, INK)]),
    blk(110, 490, 1040, 90, LILAHELL, beim("frage2", "Oder"), [("Oder: Versuch und fahrlässige Tötung?", "ExtraBold", 36, INK)]),
    *requisit([("frage", ("tabler", "ripple", 120, None), "Teich", BLAUHELL),
               ("frage2", ("tabler", "scale", 120, GELB), "vollendet?", GELB)]),
    *stehend("BR", FX, [("frage", "sorge"), ("frage2", "denkt")]),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_253(cue, absaetze, frage):
    els = [karte(140, 40, 1640, 950, cue, fill=HELL), titel("Sachverhalt", 210, 70, cue, 56)]
    y = 160
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=34, zeilenabstand=1.28)
        els += e; y += 18
    assert y + 70 <= 985, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 4, cue, fill=PINK, size=34))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_253("sv", [
    "Brunhilde und ihre Nachbarin streiten seit Jahren über den Weg zum Teich. Eines Nachmittags eskaliert der Streit am "
    "Gartenzaun. Brunhilde greift die Nachbarin an; dass sie dabei sterben kann, nimmt Brunhilde in Kauf. Die Nachbarin "
    "bleibt regungslos liegen. Brunhilde: „Sie atmet nicht mehr. Sie ist tot.“",
    "Erst jetzt beschließt Brunhilde, die vermeintliche Leiche verschwinden zu lassen; beim Angriff hatte sie daran nicht "
    "gedacht. Sie versenkt die Nachbarin im Teich. Die Nachbarin war nur bewusstlos. Erst im Wasser stirbt sie.",
], "Ist Brunhilde wegen vollendeten Totschlags strafbar?")

# ===========================================================================================================================
# C Der echte Fall (nur abstrakt): BGHSt 14, 193
# ===========================================================================================================================
PJ = "Der Jauchegrube-Fall, BGHSt 14, 193"
folie([("echt", f"{PJ} · Ein Klassiker"), ("echt2", f"{PJ} · Der Sachverhalt"), ("echt3", f"{PJ} · Erst dort stirbt die Frau")], [
    *tafel("echt", "Der Jauchegrube-Fall (BGH 1960)"),
    zit("BGH, Urt. v. 26.4.1960 – 5 StR 77/60, BGHSt 14, 193", 110, 172, "echt"),
    z("Die Angeklagte greift eine Frau an,", 110, 250, "echt2", size=36),
    z("mit bedingtem Tötungsvorsatz.", 110, 304, beim("echt2", "bedingtem"), "Bold", 36),
    z("Sie hält die Bewusstlose für tot", 110, 384, beim("echt2", "Sie"), size=36),
    z("und wirft sie in eine Jauchegrube.", 110, 438, beim("echt2", "warf"), "Bold", 36),
    blk(110, 530, 1040, 90, HELLROT, "echt3", [("Erst dort stirbt die Frau.", "ExtraBold", 36, INK)]),
    *requisit([("echt", ("tabler", "scale", 120, WEISS), "BGH 1960", WEISS),
               ("echt2", ("tabler", "alert-triangle", 110, HELLROT), "bedingter Vorsatz", HELLROT),
               (beim("echt2", "Sie"), ("tabler", "ripple", 120, None), "Jauchegrube", WEISS),
               ("echt3", ("tabler", "clock", 110, WEISS), "erst dort", WEISS)]),
    *stehend("BR", FX, [("echt", "ruhig"), ("echt2", "ernst"), ("echt3", "sorge")]),
])

# ===========================================================================================================================
# D1 Das Problem: zweiaktiges Geschehen
# ===========================================================================================================================
PZ = "Das Problem · zweiaktiges Geschehen"
folie([("zwei", PZ), ("akt1", f"{PZ} › 1. Akt: der Angriff"), ("akt2", f"{PZ} › 2. Akt: das Versenken")], [
    *tafel("zwei", "Das Problem: zwei Akte"),
    z("Ein zweiaktiges Geschehen", 110, 172, "zwei", "Bold", 36),
    blk(110, 240, 500, 300, BLAUHELL, "akt1", [("1. Akt:", "ExtraBold", 34, INK), ("Angriff", "ExtraBold", 34, INK),
                                            ("Tötungsvorsatz", "Regular", 32, INK)]),
    blk(650, 240, 500, 300, LILAHELL, "akt2", [("2. Akt:", "ExtraBold", 34, INK), ("Versenken", "ExtraBold", 34, INK),
                                            ("hier tritt der Tod ein", "Regular", 32, INK)]),
    z("tötet nicht unmittelbar", 130, 470, beim("akt1", "Doch"), "Bold", 32, rechts=600),
    z("hält sie schon für tot", 670, 470, beim("akt2", "Da"), "Bold", 32, rechts=1140),
    ficon("tabler", "arrow-right", 630, 400, 60, "akt2", fuell=None),
    z("Glaubt: Der Erfolg ist längst eingetreten.", 110, 600, beim("akt2", "Da"), "Bold", 34),
    *requisit([("zwei", ("tabler", "timeline", 120, None), "zwei Akte", WEISS),
               ("akt1", ("tabler", "alert-triangle", 110, BLAUHELL), "1. Akt", BLAUHELL),
               ("akt2", ("tabler", "ripple", 120, None), "2. Akt", LILAHELL),
               (beim("akt2", "Da"), ("tabler", "clock", 110, WEISS), "schon tot?", WEISS)]),
    *stehend("BR", FX, [("zwei", "ruhig"), ("akt1", "ernst"), ("akt2", "denkt")]),
])

# ===========================================================================================================================
# D2 Objektiver Tatbestand: Kausalität, objektive Zurechnung
# ===========================================================================================================================
PA = "Brunhilde, § 212 StGB (Angriff)"
folie([("obj", f"{PA} › Objektiver Tatbestand"), ("kaus", f"{PA} › Objektiv › Kausalität (+)"),
       ("kaus2", f"{PA} › Objektiv › eigenes späteres Handeln"), ("zurech", f"{PA} › Objektiv › objektive Zurechnung")], [
    *tafel("obj", "Objektiver Tatbestand"),
    *okz("Kausalität: Angriff ursächlich für den Tod", 180, "kaus", "Bold", 34),
    z("Ohne ihn: nicht für tot gehalten, nicht versenkt", 185, 234, beim("kaus", "Ohne"), size=33),
    *okz("Eigenes späteres Handeln wirkt mit: unschädlich", 320, "kaus2", "Bold", 34),
    zit("BGHSt 14, 193, 194; BGH, Urt. v. 3.12.2015 – 4 StR 223/15, Rn. 10", 185, 374, beim("kaus2", "ändert")),
    z("Lehre: zusätzlich objektive Zurechnung", 110, 470, "zurech", "Bold", 34),
    *okz("bejahbar: Ein solcher Verlauf liegt nicht fern.", 534, beim("zurech", "Sie"), size=34),
    *requisit([("obj", ("tabler", "list-check", 110, WEISS), "objektiv", WEISS),
               ("kaus", ("tabler", "link", 110, HELLGRUEN), "ursächlich", HELLGRUEN),
               ("kaus2", ("tabler", "arrows-join", 110, WEISS), "2. Akt wirkt mit", WEISS),
               ("zurech", ("tabler", "scale", 120, BLAUHELL), "Zurechnung", BLAUHELL)]),
    *stehend("BR", FX, [("obj", "ruhig"), ("kaus", "ernst"), ("kaus2", "denkt"), ("zurech", "ruhig")]),
])

# ===========================================================================================================================
# D3 Subjektiver Tatbestand: § 16 Abs. 1 Satz 1 (Wortlautkarte), Zeitpunkt, Kausalverlauf
# ===========================================================================================================================
w16, w16_y = wortlaut(80, 240, 1100, "„Wer bei Begehung der Tat einen Umstand nicht kennt, der zum gesetzlichen Tatbestand "
                      "gehört, handelt nicht vorsätzlich.“", "§ 16 Abs. 1 Satz 1 StGB", beim("p16", "Paragraf"),
                      marken=[("bei Begehung der Tat", beim("p16", "Begehung")), ("Umstand", beim("p16", "Umstand"))], size=34)
folie([("p16", f"{PA} › Vorsatz? § 16 Abs. 1 Satz 1"), ("zeit", f"{PA} › Vorsatz › bei der Tathandlung"),
       ("kv", f"{PA} › Vorsatz › Kausalverlauf"), ("f68", f"{PA} › Irrtum über den Kausalverlauf: Folge 068")], [
    *tafel("p16", "Subjektiver Tatbestand: Vorsatz"),
    z("Schwierig ist der Vorsatz.", 110, 172, "p16", "Bold", 36),
    *w16,
    z("Vorsatz muss bei der Tathandlung vorliegen.", 110, w16_y + 30, "zeit", "Bold", 34),
    z("Auch der Kausalverlauf: nur in den wesentlichen Zügen", 110, w16_y + 100, "kv", "Bold", 33),
    zit("BGH, Urt. v. 3.12.2015 – 4 StR 223/15, Rn. 12", 110, w16_y + 152, beim("kv", "wesentlichen")),
    zit("Irrtum über den Kausalverlauf: Folge 068", 110, w16_y + 222, "f68"),
    *requisit([("p16", ("tabler", "book", 110, BLAUHELL), "§ 16 StGB", BLAUHELL),
               ("zeit", ("tabler", "clock", 110, WEISS), "Zeitpunkt", WEISS),
               ("kv", ("tabler", "route", 110, GELB), "Kausalverlauf", GELB),
               ("f68", ("tabler", "book", 110, WEISS), "Folge 068", WEISS)]),
    *stehend("BR", FX, [("p16", "denkt"), ("zeit", "ernst"), ("kv", "denkt"), ("f68", "ruhig")]),
])
assert w16_y + 270 <= 900, w16_y

# ===========================================================================================================================
# E1 Lösung 1: dolus generalis (historisch), vom BGH abgelehnt
# ===========================================================================================================================
PV = f"{PA} › Vorsatz bzgl. Kausalverlauf"
folie([("dg", f"{PV} › 1. dolus generalis"), ("dg2", f"{PV} › 1. Gesamtvorsatz"), ("dg3", f"{PV} › 1. vom BGH abgelehnt"),
       ("dg4", f"{PV} › 1. heute nicht mehr vertreten")], [
    *tafel("dg", "1. dolus generalis (historisch)"),
    z("Ältere Lehre vom dolus generalis", 110, 172, "dg", "Bold", 35),
    blk(110, 236, 1040, 130, BLAUHELL, "dg2", [("Beide Akte = ein Geschehen,", "ExtraBold", 34, INK),
                                            ("getragen von einem Gesamtvorsatz", "Regular", 34, INK)]),
    z("Folge: vollendeter Totschlag", 110, 390, beim("dg2", "Danach"), "Bold", 34),
    *neinz("BGH 1960: abgelehnt", 470, "dg3", "ExtraBold", 34, kreuz=beim("dg3", "abgelehnt")),
    z("„unklar und rechtsgeschichtlich überholt“", 185, 524, beim("dg3", "Generalvorsatz"), size=34),
    z("Vorsatz nicht auf spätere Handlungen ausdehnen", 185, 578, beim("dg3", "Mit"), size=34),
    zit("BGH, Urt. v. 26.4.1960 – 5 StR 77/60, BGHSt 14, 193", 185, 632, beim("dg3", "Mit")),
    blk(110, 700, 1040, 90, HELLGRAU, "dg4", [("Heute nicht mehr vertreten", "ExtraBold", 34, INK)]),
    *requisit([("dg", ("tabler", "history", 110, WEISS), "historisch", WEISS),
               ("dg2", ("tabler", "link", 110, BLAUHELL), "Gesamtvorsatz", BLAUHELL),
               ("dg3", ("tabler", "scale", 120, HELLROT), "abgelehnt", HELLROT),
               ("dg4", ("tabler", "archive", 110, HELLGRAU), "überholt", HELLGRAU)]),
    *stehend("BR", FX, [("dg", "ruhig"), ("dg2", "staunt"), ("dg3", "ernst"), ("dg4", "ruhig")]),
])

# ===========================================================================================================================
# E2 Lösung 2: der BGH – unwesentliche Abweichung vom vorgestellten Kausalverlauf
# ===========================================================================================================================
folie([("bgh", f"{PV} › 2. BGH: vollendet"), ("bgh2", f"{PV} › 2. BGH: Anknüpfung an den 1. Akt"),
       ("bgh3", f"{PV} › 2. BGH: Abweichung unwesentlich"), ("bedingt", f"{PV} › 2. BGH: bedingter Vorsatz genügt")], [
    *tafel("bgh", "2. BGH: unwesentliche Abweichung"),
    *okz("Vollendeter Totschlag bestätigt", 180, "bgh", "ExtraBold", 35),
    zit("BGH, Urt. v. 26.4.1960 – 5 StR 77/60, BGHSt 14, 193", 185, 234, "bgh"),
    z("Anknüpfung: der erste Akt", 110, 310, "bgh2", "Bold", 35),
    z("Er verursachte den Tod, mit bedingtem Vorsatz.", 110, 364, beim("bgh2", "Mit"), size=34),
    z("Tod anders eingetreten als vorgestellt", 110, 440, "bgh3", "Bold", 34),
    blk(110, 500, 1040, 90, HELLGRUEN, beim("bgh3", "Diese"), [("Abweichung gering, rechtlich ohne Bedeutung", "ExtraBold", 34, INK)]),
    *okz("Bedingter statt direkter Vorsatz: ändert nichts", 640, "bedingt", "Bold", 34),
    *requisit([("bgh", ("tabler", "scale", 120, HELLGRUEN), "vollendet", HELLGRUEN),
               ("bgh2", ("tabler", "alert-triangle", 110, BLAUHELL), "1. Akt", BLAUHELL),
               ("bgh3", ("tabler", "route", 110, GELB), "Abweichung", GELB),
               ("bedingt", ("tabler", "target", 110, HELLGRUEN), "bedingt genügt", HELLGRUEN)]),
    *stehend("BR", FX, [("bgh", "sorge"), ("bgh2", "ernst"), ("bgh3", "denkt"), ("bedingt", "muede")]),
])

# ===========================================================================================================================
# E3 Der BGH heute: die Formel (4 StR 223/15 Rn. 12)
# ===========================================================================================================================
folie([("formel", f"{PV} › 2. BGH heute: die Formel"), ("verdeck", f"{PV} › 2. BGH: Verdeckungshandlung")], [
    *tafel("formel", "Der BGH heute: die Formel"),
    blk(110, 180, 1040, 230, BLAUHELL, "formel", [("Eine Abweichung ist unwesentlich, wenn", "ExtraBold", 34, INK),
                                               ("sie sich innerhalb der Grenzen des nach", "Regular", 34, INK),
                                               ("allgemeiner Lebenserfahrung", "Regular", 34, INK),
                                               ("Vorhersehbaren hält", "Regular", 34, INK)]),
    *okz("und keine andere Bewertung der Tat rechtfertigt", 440, beim("formel", "keine"), "Bold", 34),
    zit("BGH, Urt. v. 3.12.2015 – 4 StR 223/15, Rn. 12 (st. Rspr.)", 185, 494, beim("formel", "keine")),
    z("Tod erst durch Verdeckungshandlung", 110, 580, "verdeck", "Bold", 34),
    z("ohne Tötungsvorsatz:", 110, 632, beim("verdeck", "nicht"), size=34),
    blk(110, 690, 1040, 90, HELLGRUEN, beim("verdeck", "verneint"), [("keine wesentliche Abweichung", "ExtraBold", 34, INK)]),
    zit("Rn. 12, u. a. mit BGHSt 14, 193 (5 StR 77/60)", 110, 794, beim("verdeck", "verneint")),
    *requisit([("formel", ("tabler", "eye", 110, BLAUHELL), "vorhersehbar?", BLAUHELL),
               (beim("formel", "keine"), ("tabler", "scale", 120, WEISS), "Bewertung", WEISS),
               ("verdeck", ("tabler", "ripple", 120, None), "Verdeckung", WEISS),
               (beim("verdeck", "verneint"), ("tabler", "scale", 120, HELLGRUEN), "unwesentlich", HELLGRUEN)]),
    *stehend("BR", FX, [("formel", "denkt"), (beim("formel", "keine"), "ernst"), ("verdeck", "sorge")]),
])

# ===========================================================================================================================
# E4 Lösung 3: Versuchslösung (Teil der Lehre)
# ===========================================================================================================================
folie([("vers", f"{PV} › 3. Versuchslösung (Lehre)"), ("vers2", f"{PV} › 3. Versuch + § 222"),
       ("vers3", f"{PV} › 3. kein Vorsatz beim tödlichen Akt"), ("vers4", f"{PV} › 3. Kritik")], [
    *tafel("vers", "3. Versuchslösung (Teil der Lehre)"),
    z("Trennt die beiden Akte", 110, 172, "vers", "Bold", 35),
    blk(110, 236, 1040, 90, BLAUHELL, "vers2", [("1. Akt: versuchter Totschlag", "ExtraBold", 34, INK)]),
    blk(110, 350, 1040, 90, LILAHELL, beim("vers2", "zweite"), [("2. Akt: fahrlässige Tötung, § 222", "ExtraBold", 34, INK)]),
    z("Beim tödlichen Akt fehlte der Vorsatz.", 110, 476, "vers3", "Bold", 34),
    zit("z. B. Kühl AT § 13 Rn. 48 (nach Uni Freiburg, Vorlesung StrafR AT)", 110, 530, "vers3"),
    blk(110, 610, 1040, 130, HELLROT, "vers4", [("Kritik:", "ExtraBold", 34, INK),
                                             ("reißt Zusammengehöriges auseinander", "Regular", 34, INK)]),
    *requisit([("vers", ("tabler", "unlink", 110, LILAHELL), "getrennt", LILAHELL),
               ("vers2", ("tabler", "book", 110, WEISS), "Versuch + § 222", WEISS),
               ("vers3", ("tabler", "clock", 110, WEISS), "kein Vorsatz", WEISS),
               ("vers4", ("tabler", "alert-triangle", 110, HELLROT), "Kritik", HELLROT)]),
    *stehend("BR", FX, [("vers", "ruhig"), ("vers2", "staunt"), ("vers3", "denkt"), ("vers4", "ernst")]),
])

# ===========================================================================================================================
# E5 Lösung 4: vermittelnd – der Tatplan
# ===========================================================================================================================
folie([("plan", f"{PV} › 4. vermittelnd: Tatplan"), ("plan2", f"{PV} › 4. Beseitigen eingeplant?")], [
    *tafel("plan", "4. Vermittelnd: der Tatplan"),
    z("Vermittelnde Stimmen fragen nach dem Tatplan.", 110, 180, "plan", "Bold", 35),
    blk(110, 260, 1040, 130, GELB, "plan2", [("Vollendung nur, wenn das Beseitigen", "ExtraBold", 34, INK),
                                          ("schon beim 1. Akt eingeplant war", "ExtraBold", 34, INK)]),
    zit("Nachweise: Uni Freiburg, Intensivkurs StrafR (Fall 1); juraexamen.info", 110, 410, beim("plan2", "eingeplant")),
    *requisit([("plan", ("tabler", "map-2", 110, GELB), "Tatplan", GELB),
               (beim("plan2", "eingeplant"), ("tabler", "zoom-question", 110, WEISS), "eingeplant?", WEISS)]),
    *stehend("BR", FX, [("plan", "ruhig"), ("plan2", "denkt")]),
])

# ===========================================================================================================================
# F Ergebnis im Fall (nach dem BGH) und nach den Gegenansichten
# ===========================================================================================================================
folie([("erg", f"{PA} › Subsumtion"), ("e1", f"{PA} › Vorsatz und Kausalität (+)"),
       ("e2", f"{PA} › im Rahmen der Lebenserfahrung"), ("e3", f"{PA} › keine andere Bewertung"),
       ("e4", "Ergebnis: § 212 StGB (+) nach BGH"), ("e5", "Ergebnis › Versuchslösung: §§ 212, 22 + § 222"),
       ("e6", "Ergebnis › Tatplan: ebenso")], [
    *tafel("erg", "Zurück zu Brunhilde"),
    *okz("Angriff mit Tötungsvorsatz, ursächlich", 170, "e1", "Bold", 33),
    *okz("Beseitigen der vermeintlichen Leiche:", 236, "e2", "Bold", 33),
    z("nicht außerhalb der Lebenserfahrung", 185, 284, beim("e2", "liegt"), size=33),
    *okz("Keine andere Bewertung: Sie wollte töten.", 350, "e3", "Bold", 33),
    blk(110, 420, 1040, 90, HELLGRUEN, "e4", [("BGH: vollendeter Totschlag, § 212 (+)", "ExtraBold", 34, INK)]),
    z("Mordmerkmale: hier offen", 110, 526, beim("e4", "Mordmerkmale"), size=33),
    blk(110, 590, 1040, 90, HELLROT, "e5", [("Versuchslösung: Versuch + fahrlässige Tötung", "ExtraBold", 33, INK)]),
    z("Tatplan: ebenso, Versenken nicht eingeplant", 110, 700, "e6", "Bold", 33),
    *requisit([("erg", ("tabler", "ripple", 120, None), "der Fall", WEISS),
               ("e1", ("tabler", "link", 110, HELLGRUEN), "ursächlich", HELLGRUEN),
               ("e2", ("tabler", "eye", 110, BLAUHELL), "vorhersehbar", BLAUHELL),
               ("e3", ("tabler", "scale", 120, WEISS), "Bewertung", WEISS),
               ("e4", ("tabler", "scale", 120, HELLGRUEN), "§ 212 (+)", HELLGRUEN),
               ("e5", ("tabler", "unlink", 110, HELLROT), "nur Versuch", HELLROT),
               ("e6", ("tabler", "map-2", 110, GELB), "nicht geplant", GELB)]),
    *stehend("BR", FX, [("erg", "ruhig"), ("e1", "ernst"), ("e2", "sorge"), ("e3", "muede"), ("e4", "feierlich"),
                        ("e5", "staunt"), ("e6", "denkt")]),
])

# ===========================================================================================================================
# G Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · Vorsatz bzgl. Kausalverlauf"), ("k1", "Klausurtipp › erst Versenken, dann Angriff"),
       ("k2", "Klausurtipp › Streit entscheiden")], [
    *tafel("tipp", "Klausurtipp: Wo steht der Streit?", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Subjektiver Tatbestand:", 200, 200, beim("tipp", "subjektiven"), "ExtraBold", 34),
    z("Vorsatz bzgl. des Kausalverlaufs", 240, 252, beim("tipp", "Vorsatz"), size=34),
    linienzug([(130, 316), (1130, 316)], "k1", breite=3),
    z("Kurz: Beim Versenken kein Tötungsvorsatz", 200, 340, "k1", "ExtraBold", 34),
    z("Dann den Angriff prüfen", 240, 392, beim("k1", "Prüfe"), size=34),
    linienzug([(130, 456), (1130, 456)], "k2", breite=3),
    z("dolus generalis höchstens kurz", 200, 480, "k2", "ExtraBold", 34),
    z("Streit entscheiden: verschiedene Ergebnisse", 240, 532, beim("k2", "Den", 2), size=34),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# H Klausurschema (Lexi), Punkt für Punkt
# ===========================================================================================================================
folie([("sch", "Klausurschema · § 212 durch den Angriff"), ("s1", "Klausurschema › I. 1. objektiver Tatbestand"),
       ("s2", "Klausurschema › I. 2. a) Vorsatz bzgl. Tod"), ("s3", "Klausurschema › I. 2. b) Kausalverlauf: Streit"),
       ("s4", "Klausurschema › II. Rechtswidrigkeit, III. Schuld")], [
    *tafel("sch", "Klausurschema"),
    z("Totschlag, § 212 StGB – durch den Angriff", 110, 166, "sch", "ExtraBold", 34),
    z("I. Tatbestand", 150, 226, "s1", "Bold", 33),
    *plusminus("1. Objektiv: Tod, Kausalität, obj. Zurechnung", 190, 276, beim("s1", "Objektiver"), True, size=32),
    z("trotz des zweiten Akts", 236, 326, beim("s1", "trotz"), size=32),
    z("2. Subjektiv", 190, 392, "s2", "Bold", 32),
    *plusminus("a) Vorsatz bzgl. des Todes", 236, 442, beim("s2", "Vorsatz"), True, size=32),
    z("b) Vorsatz bzgl. des Kausalverlaufs: Streit", 236, 500, "s3", "Bold", 32),
    *plusminus("BGH: Abweichung unwesentlich", 282, 550, beim("s3", "Nach"), True, size=32),
    z("II. Rechtswidrigkeit, III. Schuld", 150, 626, "s4", "Bold", 33),
    *redet("LX_erklaert", FX, FB, FR + 40, "sch", "merke"),
    ns("Lexi", FX, FB, "sch", GELB, d=0.2),
])

# ===========================================================================================================================
# I Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Den ", 0), ("Generalvorsatz", "a"), (" lehnt der BGH ab.", 0)]], 750, 290, 40, "merke",
                {"a": beim("merke", "Generalvorsatz")}),
    *markertext([[("Stirbt das Opfer erst durch den zweiten Akt,", 0)],
                 [("ist das nach dem BGH in der Regel nur eine", 0)],
                 [("unwesentliche Abweichung", "b"), (" vom vorgestellten", 0)],
                 [("Kausalverlauf.", 0)]], 750, 410, 38, "m2", {"b": beim("m2", "unwesentliche")}),
    *markertext([[("Der Täter ist dann wegen ", 0), ("vollendeter Tat", "c"), (" strafbar.", 0)]],
                750, 700, 38, "m3", {"c": beim("m3", "vollendeter")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
