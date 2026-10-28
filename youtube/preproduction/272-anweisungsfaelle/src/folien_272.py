"""Folge 272 · Anweisungsfälle im Bereicherungsrecht: Wer muss zurückzahlen? · Serienstandard Open Peeps (Katzenkönig).
Beispielfall: Der Fliesenleger Herr Stemmler sagt Tomke, sein Betrieb sei voll versichert, und stellt die Anzahlung von
3.500 € in Rechnung; Tomke lässt ihre (namenlose) Bank überweisen. Der Betrieb ist nicht versichert, Tomke ficht den
Werkvertrag wegen arglistiger Täuschung an (§ 123 Abs. 1, § 142 Abs. 1 BGB). In der Bank verlangt sie, das Geld direkt bei
Herrn Stemmler zurückzuholen; Bankberater Herr Feldhaus lehnt ab. Danach: Anweisungsdreieck (Deckungs-/Valutaverhältnis),
Leistungsbegriff aus Empfängersicht (zwei Leistungen), Fehlersuche, Anspruch Tomke gegen Herrn Stemmler (Wortlautkarte
§ 812 Abs. 1 Satz 1 BGB), keine Durchgriffskondiktion (Subsidiarität; Risikoverteilung: Einwendungen, Insolvenzrisiko),
Ausnahmen (fehlende Anweisung, Widerruf, Kenntnis; Wortlautkarte § 675u BGB), Ergebnis, Klausurtipp, Schema, Merksatz.
Szenen laut ../SZENENPLAN.md. Hilfsfunktionen glyphen/z/pl/tafel/blk/wortlaut/redet/fig/ns/okz/neinz/feld als eigene Kopie
aus Folge 245 (gemeinsame Dateien unverändert); neu: fliesen(), handy() (Überweisung), bankraum(), schalter(), ecken()
(Anweisungsdreieck). Keine echte Bankmarke: die Bank ist nur das Tabler-Symbol building-bank, ohne Namen oder Logo.
Handlungsgeräusch: Tippen auf dem Smartphone beim Überweisen (A2); ../geraeusche_herkunft.json.
Zahlen auf Tafeln, Pillen und Blasen als Ziffern; Wortlaut nach gesetze-im-internet.de (BGB), Abruf 08.10.2026."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_272/"

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
BLAUHELL = (228, 238, 253, 255)
LILAHELL = (240, 236, 255, 255)
HELLGRAU = (226, 226, 222, 255)
HOLZ = (214, 160, 110, 255)
DUNKELHOLZ = (150, 98, 66, 255)
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
        if n.startswith(("bild:", "ficon:")) or "/op_272/" in n:
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


# --- Mundbewegung nur, solange im Wort tatsächlich Stimme klingt (wie Folgen 160/203/205/229/245) ---------------------------------
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
NAME = {"TO": "Tomke", "ST": "Herr Stemmler", "FE": "Herr Feldhaus"}
NFARBE = {"TO": LILA, "ST": BLAU, "FE": TUERKIS}


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



def fenster(x, y, w, h, cue):
    """Fenster mit Sprossen (Tageslicht)."""
    return [hart(feld(x, y, w, h, cue, fill=BLAUHELL, rand=5, rund=8, name="fenster")),
            hart(feld(x + w // 2 - 4, y + 6, 8, h - 12, cue, fill=INK, rand=1, rund=2, name="sprosse1")),
            hart(feld(x + 6, y + h // 2 - 4, w - 12, 8, cue, fill=INK, rand=1, rund=2, name="sprosse2"))]


def fliesen(x, y, w, h, cue, k=70):
    """Alte Fliesenwand aus Grundformen (hellblaue Quadrate, Tuschefugen)."""
    s = 2
    im = Image.new("RGBA", ((w + 12) * s, (h + 12) * s)); dr = ImageDraw.Draw(im); o = 6 * s
    dr.rectangle((o, o, o + w * s, o + h * s), fill=(214, 232, 236, 255), outline=INK, width=4 * s)
    for xx in range(x, x + w, k):
        dr.line((o + (xx - x) * s, o, o + (xx - x) * s, o + h * s), fill=INK, width=2 * s)
    for yy in range(y, y + h, k):
        dr.line((o, o + (yy - y) * s, o + w * s, o + (yy - y) * s), fill=INK, width=2 * s)
    im = im.resize((w + 12, h + 12), Image.LANCZOS)
    return hart(El(im, x - 6, y - 6, cue, "cut", 0.0, None, name="fliesen"))


# ===========================================================================================================================
# A1 Fall: das alte Bad – der Fliesenleger und die Anzahlung
# ===========================================================================================================================
TOX, STX = 1000, 1500
folie([(NULL, "Fall · Das alte Bad von Tomke"), ("stemmler", "Fall · Der Fliesenleger Herr Stemmler"),
       ("rechnung", "Fall · Rechnung: Anzahlung 3.500 €"), ("st1", "Fall · „Mein Betrieb ist voll versichert“")], [
    boden(NULL), fliesen(80, 300, 560, 554, NULL),
    ficon("tabler", "bath", 370, BODEN, 430, NULL, fuell=WEISS, anim="cut"),
    *fenster(650, 150, 130, 140, NULL),
    hart(pl("Das alte Bad", 70, 30, NULL, fill=GELB, size=32)),
    *fig("TO", TOX, BODEN, FH, [(NULL, "ruhig_r"), ("rechnung", "denkt_r"), ("st1", "froh_r")], erst="cut"),
    hart(ns(NAME["TO"], TOX, BODEN, NULL, NFARBE["TO"])),
    *fig("ST", STX, BODEN, FH, [("stemmler", "ruhig")], bis="st1", erst="pop"),
    *redet("ST_redet", STX, BODEN, FH, "st1", "ueberw"),
    ns(NAME["ST"], STX, BODEN, "stemmler", NFARBE["ST"], d=0.1),
    pl("Fliesenleger", 1700, 330, beim("stemmler", "Fliesenleger"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "file-invoice", 1250, 560, 110, "rechnung", fuell=WEISS),
    pl("Anzahlung: 3.500 €", 1250, 392, beim("rechnung", "Rechnung"), fill=GELB, size=30, anker="m"),
    ficon("tabler", "shield-check", 1765, 520, 110, beim("st1", "versichert"), fuell=GRUEN),
    blase("sprech", 820, 230, "st1", 1215, 190, inhalt=["Keine Sorge, mein Betrieb ist voll", "versichert. Sobald die Anzahlung",
                                                      "da ist, fange ich an."], textsize=31,
          figur=("ST_redet", STX, BODEN, FH)),
])


# ===========================================================================================================================
# A2 Bei Tomke zu Hause: Überweisung, Gutschrift – eine Woche später: nicht versichert, Anfechtung
# ===========================================================================================================================
TOX2 = 1400


def handy(x, y, cue, bis=None):
    """Smartphone mit dem Überweisungsauftrag (Rahmen aus Grundformen, ohne Bank- oder App-Kennzeichen)."""
    w, h = 430, 500
    els = [bis_(feld(x, y, w, h, cue, fill=INK, rand=4, rund=40, anim="pop", name="handy"), bis),
           bis_(feld(x + 18, y + 40, w - 36, h - 80, cue, fill=WEISS, rand=2, rund=16, anim="pop", name="display"), bis),
           bis_(z("Überweisung", x + 50, y + 70, cue, "ExtraBold", 34, rechts=x + w - 20), bis),
           bis_(feld(x + 40, y + 140, w - 80, 230, cue, fill=BLAUHELL, rand=3, rund=18, anim="pop", name="auftrag"), bis),
           bis_(z("an: Herr Stemmler", x + 64, y + 166, cue, "Bold", 30, rechts=x + w - 40), bis),
           bis_(z("3.500 €", x + 64, y + 230, cue, "ExtraBold", 50, rechts=x + w - 40), bis),
           bis_(z("Anzahlung Bad", x + 64, y + 306, cue, "Bold", 28, rechts=x + w - 40), bis)]
    return els


folie([("ueberw", "Fall · Tomke überweist die Anzahlung"), ("gutschr", "Fall · Gutschrift bei Herrn Stemmler"),
       ("woche", "Fall · Eine Woche später: nicht versichert"), ("anf", "Fall · Anfechtung wegen arglistiger Täuschung"),
       ("bank", "Fall · Tomke geht zu ihrer Bank")], [
    boden("ueberw"),
    ficon("tabler", "sofa", 1650, BODEN, 420, "ueberw", fuell=LILA, anim="cut"),
    ficon("tabler", "plant-2", 1130, BODEN, 110, "ueberw", fuell=GRUEN, anim="cut"),
    hart(pl("Bei Tomke zu Hause", 70, 30, "ueberw", fill=GELB, size=32, bis="woche")),
    *fig("TO", TOX2, BODEN, FH, [("ueberw", "ruhig"), ("gutschr", "froh"), ("woche", "staunt"), ("anf", "ernst"),
                                 ("bank", "ernst_r")], erst="pop"),
    ns(NAME["TO"], TOX2, BODEN, "ueberw", NFARBE["TO"], d=0.1),
    *[szene(e, "272tippen*", 0.8, 0.3) if i == 0 else e for i, e in enumerate(handy(200, 150, "ueberw", bis="woche"))],
    ficon("tabler", "device-mobile", 1316, 645, 54, "ueberw", fuell=WEISS, bis="woche"),     # Handy in der Hand
    ficon("tabler", "building-bank", 760, 330, 130, "gutschr", fuell=BLAUHELL, bis="woche"),
    pfeil(840, 268, 1040, 268, beim("gutschr", "Betrag"), breite=8, kopf=26, bis="woche"),
    pl("Gutschrift bei Herrn Stemmler: 3.500 €", 1060, 242, beim("gutschr", "Betrag"), fill=GRUEN, size=30, bis="woche"),
    hart(pl("Eine Woche später", 70, 30, "woche", fill=GELB, size=32)),
    ficon("tabler", "shield-x", 330, 520, 200, beim("woche", "Versichert"), fuell=HELLROT),
    pl("Betrieb gar nicht versichert", 330, 540, beim("woche", "Versichert"), fill=ROT, size=30, anker="m"),
    ficon("tabler", "mail", 880, 520, 180, "anf", fuell=WEISS),
    pl("Anfechtung: arglistige Täuschung", 880, 540, beim("anf", "arglistiger"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "building-bank", 1700, 380, 130, "bank", fuell=BLAUHELL),
    pl("zur Bank", 1700, 400, "bank", fill=BLAUHELL, size=30, anker="m"),
])


# ===========================================================================================================================
# A3 In der Bank: Tomke will, dass die Bank das Geld bei Herrn Stemmler zurückholt – die Frage
# ===========================================================================================================================
FEX = 1560


def bankraum(cue):
    """Schalterraum einer namenlosen Bank: Bank-Symbol an der Wand, Schalter, Bildschirm."""
    return [boden(cue), ficon("tabler", "building-bank", 1790, 330, 130, cue, fuell=BLAUHELL, anim="cut"),
            ficon("tabler", "plant-2", 150, BODEN, 120, cue, fuell=GRUEN, anim="cut")]


def schalter(cue, bis=None):
    return [bis_(hart(feld(1380, 640, 470, 214, cue, fill=HOLZ, rand=5, rund=10, name="schalter")), bis),
            bis_(ficon("tabler", "device-desktop", 1765, 640, 140, cue, fuell=BLAUHELL, anim="cut"), bis)]


folie([("t1", "Fall · In der Bank: „Holen Sie mein Geld zurück!“"), ("f1", "Fall · Der Bankberater lehnt ab"),
       ("frage", "Die Frage · Wer muss an wen zurückzahlen?"), ("frage2", "Die Frage · Warum kein Durchgriff der Bank?")], [
    *bankraum("t1"),
    hart(pl("In der Bank", 70, 30, "t1", fill=GELB, size=32, bis="frage")),
    *redet("TO_redet_r", TOX, BODEN, FH, "t1", "f1"),
    *fig("TO", TOX, BODEN, FH, [("f1", "sorge_r"), ("frage", "denkt_r")], erst="cut"),
    hart(ns(NAME["TO"], TOX, BODEN, "t1", NFARBE["TO"])),
    *fig("FE", FEX, BODEN, FH, [("t1", "ruhig")], bis="f1", erst="cut"),
    *redet("FE_redet", FEX, BODEN, FH, "f1", "frage"),
    *fig("FE", FEX, BODEN, FH, [("frage", "ruhig")], erst="cut"),
    *schalter("t1"),
    hart(ns(NAME["FE"], FEX, BODEN, "t1", NFARBE["FE"])),
    blase("sprech", 760, 230, "t1", 720, 230, inhalt=["Holen Sie meine 3.500 € bitte", "direkt bei Herrn Stemmler zurück!"],
          textsize=33, figur=("TO_redet_r", TOX, BODEN, FH), bis="f1"),
    blase("sprech", 960, 260, "f1", 1150, 210, inhalt=["Das geht nicht. Wir haben Ihren", "Auftrag richtig ausgeführt. An Herrn",
                                                     "Stemmler müssen Sie sich selbst halten."], textsize=31,
          figur=("FE_redet", FEX, BODEN, FH), bis="frage"),
    pl("Hat der Bankberater recht?", 70, 30, "frage", fill=WEISS, size=32),
    pl("Wer muss hier an wen zurückzahlen?", 70, 104, beim("frage", "Wer"), fill=PINK, size=34),
    pl("Warum kann die Bank nicht direkt bei Herrn Stemmler kondizieren?", 70, 184, "frage2", fill=PINK, size=32),
])


# ===========================================================================================================================
# B Sachverhalt
# ===========================================================================================================================
def sachverhalt_272(cue, absaetze, frage):
    els = [karte(140, 60, 1640, 900, cue, fill=HELL), titel("Sachverhalt", 210, 100, cue, 60)]
    y = 210
    for a in absaetze:
        e, y = absatz(glyphen(a), 210, y, 1500, cue, size=36, zeilenabstand=1.3)
        els += e; y += 16
    assert y + 70 <= 950, f"Sachverhalt zu lang ({y})"
    els.append(pille(glyphen(frage), 210, y + 6, cue, fill=PINK, size=30))
    folie([(cue, "Sachverhalt")], els)


sachverhalt_272("sv", [
    "Tomke lässt ihr altes Bad von dem Fliesenleger Herrn Stemmler erneuern. Er sagt ihr, sein Betrieb sei voll versichert, "
    "und stellt die vereinbarte Anzahlung von 3.500 € in Rechnung. Tomke beauftragt ihre Bank, den Betrag zu überweisen; "
    "er wird Herrn Stemmler gutgeschrieben.",
    "Eine Woche später erfährt Tomke, dass der Betrieb nicht versichert ist und Herr Stemmler das wusste. Sie ficht den "
    "Werkvertrag wegen arglistiger Täuschung an. Gearbeitet hat Herr Stemmler noch nicht.",
    "Tomke verlangt von ihrer Bank, das Geld direkt bei Herrn Stemmler zurückzuholen. Der Bankberater lehnt ab.",
], "Wer kann von wem die 3.500 € zurückverlangen?")


# ===========================================================================================================================
# C Das Anweisungsdreieck (XI ZR 243/13 Rn. 17; XI ZR 343/22 Rn. 14)
# ===========================================================================================================================
TC = (960, 400, 250)                    # Tomke oben: Mitte, Unterkante, Höhe
SC = (1590, 820, 250)                   # Herr Stemmler rechts unten
BC = (330, 820, 190)                    # Bank links unten: Mitte, Unterkante, Breite
DECK = [(845, 430), (420, 630)]
VAL = [(1075, 430), (1510, 590)]
R = 1820                                # Textgrenze der breiten Dreieckskarte


def ecken(cue, mt="ruhig", ms="ruhig", rollen=True, folge_t=None, folge_s=None):
    """Grundbild des Dreiecks: Karte, Tomke (Anweisende), Bank (Angewiesene), Herr Stemmler (Empfänger), beide
    Verhältnisse mit Beschriftung – alles hart zum Folienstart (Szenen D und E bauen darauf auf)."""
    els = [karte(60, 50, 1800, 900, cue, anim="cut"),
           *fig("TO", TC[0], TC[1], TC[2], folge_t or [(cue, mt)], erst="cut"),
           hart(ns(NAME["TO"], TC[0], TC[1], cue, NFARBE["TO"])),
           ficon("tabler", "building-bank", BC[0], BC[1], BC[2], cue, fuell=BLAUHELL, anim="cut"),
           hart(ns("Bank", BC[0], BC[1], cue, WEISS)),
           *fig("ST", SC[0], SC[1], SC[2], folge_s or [(cue, ms)], erst="cut"),
           hart(ns(NAME["ST"], SC[0], SC[1], cue, NFARBE["ST"])),
           hart(linienzug(DECK, cue, breite=6)), hart(linienzug(VAL, cue, breite=6)),
           hart(pl("Deckungsverhältnis", 380, 376, cue, fill=GELB, size=30, anker="m")),
           hart(z("Zahlungsdiensterahmenvertrag", 190, 446, cue, "Bold", 28, rechts=R)),
           hart(pl("Valutaverhältnis", 1430, 376, cue, fill=LILAHELL, size=30, anker="m")),
           hart(z("Werkvertrag", 1258, 446, cue, "Bold", 28, rechts=R))]
    if rollen:
        els += [hart(pl("Anweisende", TC[0], TC[1] + 78, cue, fill=WEISS, size=26, anker="m")),
                hart(pl("Angewiesene", BC[0], BC[1] + 76, cue, fill=WEISS, size=26, anker="m")),
                hart(pl("Empfänger", SC[0], SC[1] + 76, cue, fill=WEISS, size=26, anker="m"))]
    return els


PD = "Anweisungsdreieck"
folie([("dreieck", f"{PD} · drei Beteiligte"), ("anw", f"{PD} › Tomke: Anweisende"), ("angew", f"{PD} › Bank: Angewiesene"),
       ("empf", f"{PD} › Herr Stemmler: Empfänger"), ("deck", f"{PD} › Deckungsverhältnis: Tomke – Bank"),
       ("valuta", f"{PD} › Valutaverhältnis: Tomke – Herr Stemmler"), ("zuw", f"{PD} › Die Zahlung: Bank an Herrn Stemmler")], [
    karte(60, 50, 1800, 900, "dreieck"),
    titel("Das Anweisungsdreieck", 110, 90, "dreieck", 44),
    pl("3 Beteiligte", 975, 600, beim("dreieck", "drei"), fill=GELB, size=30, anker="m", bis="zuw"),
    *fig("TO", TC[0], TC[1], TC[2], [("anw", "ruhig")], erst="pop"),
    ns(NAME["TO"], TC[0], TC[1], "anw", NFARBE["TO"], d=0.1),
    pl("Anweisende", TC[0], TC[1] + 78, beim("anw", "Anweisende"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "building-bank", BC[0], BC[1], BC[2], "angew", fuell=BLAUHELL),
    ns("Bank", BC[0], BC[1], "angew", WEISS, d=0.1),
    pl("Angewiesene", BC[0], BC[1] + 76, beim("angew", "Angewiesene"), fill=WEISS, size=26, anker="m"),
    *fig("ST", SC[0], SC[1], SC[2], [("empf", "ruhig"), ("zuw", "froh")], erst="pop"),
    ns(NAME["ST"], SC[0], SC[1], "empf", NFARBE["ST"], d=0.1),
    pl("Empfänger", SC[0], SC[1] + 76, beim("empf", "Empfänger"), fill=WEISS, size=26, anker="m"),
    linienzug(DECK, beim("deck", "Deckungsverhältnis"), breite=6),
    pl("Deckungsverhältnis", 380, 376, beim("deck", "Deckungsverhältnis"), fill=GELB, size=30, anker="m"),
    z("Zahlungsdiensterahmenvertrag", 190, 446, beim("deck", "Zahlungsdiensterahmenvertrag"), "Bold", 28, rechts=R),
    linienzug(VAL, beim("valuta", "Valutaverhältnis"), breite=6),
    pl("Valutaverhältnis", 1430, 376, beim("valuta", "Valutaverhältnis"), fill=LILAHELL, size=30, anker="m"),
    z("Werkvertrag", 1258, 446, beim("valuta", "Werkvertrag"), "Bold", 28, rechts=R),
    pfeil(450, 770, 1500, 770, "zuw", breite=8, kopf=28),
    ficon("tabler", "cash-banknote-move", 975, 690, 120, "zuw", fuell=GRUEN),
    pl("Zahlung: 3.500 €", 975, 700, beim("zuw", "Bank"), fill=GRUEN, size=28, anker="m"),
    zit("BGH, Urt. v. 16.6.2015 – XI ZR 243/13, Rn. 17", 1170, 170, beim("deck", "Deckungsverhältnis"), rechts=R),
    zit("BGH, Urt. v. 19.9.2023 – XI ZR 343/22, Rn. 14", 1170, 206, beim("deck", "Zahlungsdiensterahmenvertrag"), rechts=R),
])


# ===========================================================================================================================
# D Leistungsbegriff aus Empfängersicht: zwei Leistungen, keine Leistungsbeziehung Bank – Empfänger, Rückabwicklung über Eck
# ===========================================================================================================================
PL = "Leistungsbegriff"
folie([("leist", f"{PL} · Wer hat an wen geleistet?"), ("sicht", f"{PL} › Sicht des Empfängers"),
       ("zwei", f"{PL} › eine Zahlung, zwei Leistungen"), ("lbank", f"{PL} › Leistung 1: Bank an Tomke"),
       ("ltomke", f"{PL} › Leistung 2: Tomke an Herrn Stemmler"), ("keine", f"{PL} › Bank – Herr Stemmler: keine Leistung"),
       ("eck", "Rückabwicklung · über Eck, im fehlerhaften Verhältnis")], [
    *ecken("leist", folge_t=[("leist", "ruhig"), ("ltomke", "ernst")], folge_s=[("leist", "ruhig"), ("keine", "denkt")]),
    hart(titel("Wer hat an wen geleistet?", 110, 90, "leist", 44)),
    hart(pfeil(450, 770, 1500, 770, "leist", breite=8, kopf=28)),
    hart(pl("Zahlung: 3.500 €", 975, 700, "leist", fill=GRUEN, size=28, anker="m")),
    blk(110, 160, 640, 160, GELB, beim("leist", "Leistung"), [("Leistung = bewusste und", "ExtraBold", 30, INK),
                                                          ("zweckgerichtete Mehrung", "ExtraBold", 30, INK),
                                                          ("fremden Vermögens", "ExtraBold", 30, INK)], bis="eck"),
    bis_(zit("BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 17", 110, 330, beim("leist", "Leistung"), rechts=R), "eck"),
    blk(1170, 160, 640, 110, BLAUHELL, "sicht", [("Vorstellungen auseinander:", "ExtraBold", 30, INK),
                                               ("Sicht des Empfängers", "ExtraBold", 30, INK)]),
    pl("eine Zahlung, zwei Leistungen", 975, 596, beim("zwei", "Zahlung"), fill=WEISS, size=28, anker="m"),
    zit("BGH, Urt. v. 16.6.2015 – XI ZR 243/13, Rn. 17", 1170, 284, beim("zwei", "Bundesgerichtshof"), rechts=R),
    pfeil(470, 655, 835, 490, "lbank", breite=8, kopf=26, farbe=DGRUEN),
    pl("Leistung 1", 600, 690, "lbank", fill=GRUEN, size=28, anker="m"),
    zit("BGH, Urt. v. 21.11.2013 – IX ZR 52/13, Rn. 16", 1170, 318, "lbank", rechts=R),
    pfeil(1085, 490, 1490, 640, "ltomke", breite=8, kopf=26, farbe=DGRUEN),
    pl("Leistung 2", 1340, 690, "ltomke", fill=GRUEN, size=28, anker="m"),
    nein(975, 770, beim("keine", "keine"), gr=26),
    pl("keine Leistungsbeziehung", 975, 794, beim("keine", "keine"), fill=HELLROT, size=26, anker="m"),
    blk(110, 160, 640, 110, GELB, "eck", [("Rückabwicklung über Eck:", "ExtraBold", 30, INK),
                                        ("im fehlerhaften Verhältnis", "ExtraBold", 30, INK)]),
    zit("BGH, Urt. v. 21.1.2010 – IX ZR 226/08, Rn. 15", 110, 284, beim("eck", "jeweils"), rechts=R),
])


# ===========================================================================================================================
# E Welches Verhältnis ist fehlerhaft? Deckung in Ordnung (§§ 675j, 675c, 670; XI ZR 343/22), Valuta nichtig (§ 142 Abs. 1)
# ===========================================================================================================================
PF = "Fehlersuche"
folie([("fehler", f"{PF} · Welches Verhältnis ist fehlerhaft?"), ("dok", f"{PF} › Deckung: autorisiert, in Ordnung"),
       ("aufw", f"{PF} › Deckung: Aufwendungsersatz für die Bank"), ("vfehl", f"{PF} › Valuta: Werkvertrag nichtig")], [
    *ecken("fehler", folge_t=[("fehler", "denkt"), ("dok", "ruhig")], folge_s=[("fehler", "ruhig"), ("vfehl", "sorge")]),
    hart(titel("Welches Verhältnis ist fehlerhaft?", 110, 90, "fehler", 42)),
    hart(linienzug(DECK, beim("dok", "Ordnung"), breite=8, farbe=DGRUEN)),
    ok(160, 400, beim("dok", "Ordnung"), gr=22),
    blk(110, 160, 700, 110, HELLGRUEN, beim("dok", "Überweisung"), [("Deckung in Ordnung:", "ExtraBold", 30, INK),
                                                                ("Überweisung autorisiert", "ExtraBold", 30, INK)]),
    zit("§ 675j Abs. 1 Satz 1 BGB", 110, 284, beim("dok", "autorisiert"), rechts=R),
    z("Also darf die Bank das Konto belasten", 530, 600, "aufw", "Bold", 30, rechts=1490),
    z("und Aufwendungsersatz verlangen", 530, 644, beim("aufw", "Aufwendungen"), "Bold", 30, rechts=1490),
    zit("§ 675c Abs. 1, § 670 BGB; BGH, Urt. v. 19.9.2023 – XI ZR 343/22, Rn. 15 f.", 530, 690,
        beim("aufw", "Aufwendungen"), rechts=1490),
    hart(linienzug(VAL, beim("vfehl", "Valutaverhältnis"), breite=8, farbe=DROT)),
    nein(1632, 400, beim("vfehl", "Valutaverhältnis"), gr=22),
    blk(1170, 160, 640, 110, HELLROT, beim("vfehl", "Werkvertrag"), [("Valuta fehlerhaft:", "ExtraBold", 30, INK),
                                                                  ("Werkvertrag nichtig", "ExtraBold", 30, INK)]),
    zit("§ 142 Abs. 1 BGB, nach Anfechtung", 1170, 284, beim("vfehl", "Paragraf"), rechts=R),
    zit("wegen arglistiger Täuschung, § 123 Abs. 1 BGB", 1170, 318, beim("vfehl", "Paragraf"), rechts=R),
])


# ===========================================================================================================================
# Tafel-Helfer
# ===========================================================================================================================
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


# ===========================================================================================================================
# F Anspruch Tomke gegen Herrn Stemmler: § 812 Abs. 1 Satz 1 Alt. 1 BGB (Wortlautkarte; IX ZR 164/14 Rn. 8)
# ===========================================================================================================================
PA = "Anspruch Tomke gegen Herrn Stemmler"
w812, w812_y = wortlaut(80, 236, 1100, "„(1) Wer durch die Leistung eines anderen oder in sonstiger Weise auf dessen Kosten "
                                       "etwas ohne rechtlichen Grund erlangt, ist ihm zur Herausgabe verpflichtet. …“",
                        "§ 812 Abs. 1 Satz 1 BGB", "w812",
                        marken=[("durch die Leistung eines anderen", beim("w812", "Leistung")), ("etwas", beim("w812", "etwas")),
                                ("ohne rechtlichen Grund", beim("w812", "rechtlichen")), ("erlangt", beim("w812", "erlangt"))])
folie([("w812", f"{PA} · § 812 Abs. 1 Satz 1 Alt. 1 BGB"), ("erl", f"{PA} › etwas erlangt: die Gutschrift"),
       ("durch", f"{PA} › durch Leistung von Tomke"), ("org", f"{PA} › ohne rechtlichen Grund"),
       ("erg1", f"{PA} › 3.500 € zurück")], [
    *tafel("w812", "Tomke gegen Herrn Stemmler"),
    z("§ 812 Abs. 1 Satz 1 Alt. 1 BGB", 110, 176, beim("w812", "Paragraf"), "ExtraBold", 34),
    *w812,
    *okz("etwas erlangt: die Gutschrift,", w812_y + 24, "erl", "Bold", 34),
    z("also ein Anspruch gegen seine Bank", 185, w812_y + 70, beim("erl", "Anspruch"), "Bold", 34),
    zit("BGH, Urt. v. 5.3.2015 – IX ZR 164/14, Rn. 8", 185, w812_y + 116, beim("erl", "Anspruch")),
    *okz("durch Leistung von Tomke", w812_y + 160, "durch", "Bold", 34),
    *okz("ohne rechtlichen Grund: Werkvertrag nichtig", w812_y + 216, "org", "Bold", 34),
    blk(110, w812_y + 280, 1040, 80, HELLGRUEN, "erg1", [("Tomke kann 3.500 € zurückverlangen", "ExtraBold", 34, INK)]),
    *requisit([("w812", ("tabler", "scale", 120, WEISS), "§ 812 BGB", GELB),
               ("erl", ("tabler", "receipt-euro", 120, GRUEN), "Gutschrift", GRUEN),
               ("erg1", ("tabler", "coin-euro", 120, GELB), "3.500 € zurück", GELB)], px=1560, pu=330, py=90),
    *paar("TO", [("w812", "ruhig"), ("erg1", "froh")], "ST", [("w812", "ruhig"), ("org", "sorge")]),
])
assert w812_y + 280 + 80 <= 900, w812_y

# ===========================================================================================================================
# G Keine Durchgriffskondiktion der Bank (IX ZR 52/13 Rn. 16; IX ZR 212/19 Rn. 21)
# ===========================================================================================================================
PG = "Streitfrage: Durchgriff der Bank?"
folie([("durchg", f"{PG} · Das Geld kam von der Bank"), ("nein", f"{PG} › Durchgriffskondiktion: grundsätzlich nicht"),
       ("nleist", f"{PG} › Die Bank leistete nicht an Herrn Stemmler"), ("vorrang", f"{PG} › Subsidiarität der Nichtleistungskondiktion")], [
    *tafel("durchg", "Durchgriff der Bank?"),
    z("Auf den ersten Blick: Das Geld kam von der Bank.", 110, 180, beim("durchg", "Auf"), "Bold", 34),
    *neinz("Durchgriffskondiktion: grundsätzlich nicht", 250, beim("nein", "grundsätzlich"), "Bold", 34, kreuz=beim("nein", "nicht")),
    *neinz("Die Bank leistete nicht an Herrn Stemmler,", 320, "nleist", "Bold", 34),
    *okz("sondern an Tomke", 372, beim("nleist", "sondern"), "Bold", 34),
    zit("BGH, Urt. v. 21.11.2013 – IX ZR 52/13, Rn. 16", 185, 418, beim("nleist", "sondern")),
    blk(110, 470, 1040, 120, HELLROT, "vorrang", [("Nichtleistungskondiktion: subsidiär,", "ExtraBold", 32, INK),
                                                ("Vorrang der Leistungskondiktion", "ExtraBold", 32, INK)]),
    zit("BGH, Urt. v. 29.10.2020 – IX ZR 212/19, Rn. 21", 110, 606, beim("vorrang", "Vorrang")),
    ficon("tabler", "building-bank", 270, 850, 150, "nein", fuell=BLAUHELL),
    pfeil(380, 770, 820, 770, "nein", breite=8, kopf=26),
    nein(600, 770, beim("nein", "nicht"), gr=26),
    pl("Herr Stemmler", 850, 746, "nein", fill=BLAU, size=28),
    *requisit([("durchg", ("tabler", "help-circle", 110, WEISS), "Durchgriff?", WEISS),
               ("nein", ("tabler", "ban", 110, HELLROT), "kein Durchgriff", HELLROT)], px=1560, pu=330, py=90),
    *paar("FE", [("durchg", "denkt"), ("nein", "ernst")], "ST", [("durchg", "ruhig"), ("nein", "denkt")]),
])

# ===========================================================================================================================
# G2 Gründe: Risikoverteilung – Einwendungen, Insolvenzrisiko (vgl. V ZR 269/13 Rn. 22 f.; XI ZR 343/22 Rn. 20)
# ===========================================================================================================================
folie([("gruende", f"{PG} › Grund: Risikoverteilung"), ("einw", f"{PG} › Einwendungen bleiben im Verhältnis"),
       ("insolv", f"{PG} › Insolvenzrisiko des eigenen Partners"), ("pleite", f"{PG} › Herr Stemmler pleite? Risiko bei Tomke")], [
    *tafel("gruende", "Warum kein Durchgriff?"),
    blk(110, 180, 1040, 80, GELB, "gruende", [("Dahinter steht eine Risikoverteilung", "ExtraBold", 34, INK)]),
    zit("vgl. BGH, Urt. v. 19.9.2014 – V ZR 269/13, Rn. 22 f.", 110, 274, "gruende"),
    *okz("1. Jeder behält seine Einwendungen", 330, "einw", "Bold", 34),
    z("gegenüber dem eigenen Vertragspartner", 185, 376, beim("einw", "eigenen"), "Bold", 34),
    zit("vgl. BGH, Urt. v. 19.9.2023 – XI ZR 343/22, Rn. 20", 185, 422, beim("einw", "eigenen")),
    *okz("2. Jeder trägt nur das Insolvenzrisiko", 480, "insolv", "Bold", 34),
    z("des Partners, den er selbst ausgesucht hat", 185, 526, beim("insolv", "Partners"), "Bold", 34),
    blk(110, 600, 1040, 120, HELLROT, "pleite", [("Herr Stemmler pleite?", "ExtraBold", 33, INK),
                                               ("Das trifft Tomke, nicht die Bank", "ExtraBold", 33, INK)]),
    *requisit([("gruende", ("tabler", "scale", 120, GELB), "Risikoverteilung", GELB),
               ("pleite", ("tabler", "wallet-off", 120, HELLROT), "pleite?", HELLROT)], px=1560, pu=330, py=90),
    *paar("TO", [("gruende", "ruhig"), ("pleite", "sorge")], "FE", [("gruende", "ruhig"), ("insolv", "ernst")]),
])

# ===========================================================================================================================
# H Ausnahmen: fehlende Anweisung, Widerruf (XI ZR 243/13 Rn. 18–20; XI ZR 158/24 Rn. 11; VIII ZR 39/17 Rn. 34)
# ===========================================================================================================================
PH = "Ausnahme: fehlerhafte Anweisung"
folie([("ausn", f"{PH} · Fehler schon in der Anweisung"), ("fehlt", f"{PH} › keine wirksame Anweisung: Direktkondiktion"),
       ("widerr", f"{PH} › Widerruf: früher hielt sich die Bank an den Kunden"), ("kennt", f"{PH} › außer: Empfänger kannte den Widerruf")], [
    *tafel("ausn", "Ausnahme: fehlerhafte Anweisung"),
    z("Fehler schon in der Anweisung?", 110, 176, "ausn", "Bold", 36),
    z("1. Keine wirksame Anweisung, etwa ein", 110, 246, "fehlt", "Bold", 34),
    z("gefälschter Überweisungsauftrag", 150, 292, beim("fehlt", "gefälschten"), "Bold", 34),
    blk(110, 350, 1040, 120, HELLGRUEN, beim("fehlt", "kondiziert"), [("Direktkondiktion der Bank beim Empfänger,", "ExtraBold", 31, INK),
                                                                  ("§ 812 Abs. 1 Satz 1 Alt. 2 BGB", "ExtraBold", 31, INK)]),
    z("auch wenn der Empfänger nichts wusste", 150, 484, beim("fehlt", "auch"), "Bold", 33),
    zit("BGH, Urt. v. 16.6.2015 – XI ZR 243/13, Rn. 18;", 150, 528, beim("fehlt", "auch")),
    zit("BGH, Urt. v. 21.7.2026 – XI ZR 158/24, Rn. 11", 150, 562, beim("fehlt", "auch")),
    z("2. Widerruf, die Bank zahlt trotzdem:", 110, 620, "widerr", "Bold", 34),
    z("früher hielt sich die Bank an ihren Kunden", 150, 666, beim("widerr", "musste"), "Bold", 34),
    *okz("außer: Der Empfänger kannte den Widerruf.", 726, "kennt", "Bold", 33),
    zit("BGH, Urt. v. 16.6.2015 – XI ZR 243/13, Rn. 19 f.;", 185, 772, "kennt"),
    zit("BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 33 f.", 185, 806, "kennt"),
    *requisit([("ausn", ("tabler", "file-alert", 120, GELB), "Anweisung?", WEISS),
               ("fehlt", ("tabler", "file-x", 120, HELLROT), "gefälscht", HELLROT),
               ("widerr", ("tabler", "arrow-back-up", 120, WEISS), "Widerruf", WEISS),
               ("kennt", ("tabler", "eye", 120, BLAUHELL), "Kenntnis?", BLAUHELL)]),
    *stehend("FE", FX, [("ausn", "ruhig"), ("fehlt", "ernst"), ("kennt", "denkt")]),
])

# ===========================================================================================================================
# H2 Zahlungsdienste: § 675u BGB (Wortlautkarte), BGH XI ZR 243/13 Rn. 22–24
# ===========================================================================================================================
w675, w675_y = wortlaut(80, 176, 1100, "„Im Fall eines nicht autorisierten Zahlungsvorgangs hat der Zahlungsdienstleister des "
                                       "Zahlers gegen diesen keinen Anspruch auf Erstattung seiner Aufwendungen. Er ist "
                                       "verpflichtet, dem Zahler den Zahlungsbetrag unverzüglich zu erstatten …“",
                        "§ 675u Satz 1, 2 BGB", "w675u",
                        marken=[("nicht autorisierten", beim("w675u", "Autorisierung")),
                                ("keinen Anspruch", beim("w675u", "keinen")), ("Aufwendungen", beim("w675u", "Aufwendungen"))])
folie([("w675u", f"{PH} › Zahlungsdienste: § 675u BGB"),
       (beim("w675u", "Widerruf"), f"{PH} › Widerruf: nicht mehr autorisiert"),
       (beim("w675u", "deshalb"), f"{PH} › Direktkondiktion, auch ohne Kenntnis")], [
    *tafel("w675u", "Zahlungsdienste: § 675u BGB"),
    *w675,
    z("nach Widerruf: Zahlung nicht autorisiert", 110, w675_y + 26, beim("w675u", "Widerruf"), "Bold", 34),
    zit("§ 675j Abs. 2 BGB", 110, w675_y + 72, beim("w675u", "Widerruf")),
    blk(110, w675_y + 124, 1040, 120, HELLGRUEN, beim("w675u", "deshalb"),
        [("Direktkondiktion beim Empfänger,", "ExtraBold", 33, INK), ("auch wenn er nichts wusste", "ExtraBold", 33, INK)]),
    zit("BGH, Urt. v. 16.6.2015 – XI ZR 243/13, BGHZ 205, 377, Rn. 22–24", 110, w675_y + 258, beim("w675u", "deshalb")),
    *requisit([("w675u", ("tabler", "building-bank", 130, BLAUHELL), "§ 675u BGB", GELB),
               (beim("w675u", "deshalb"), ("tabler", "arrow-back-up", 120, GRUEN), "direkt zurück", GRUEN)]),
    *stehend("FE", FX, [("w675u", "ruhig"), (beim("w675u", "deshalb"), "ernst")]),
])
assert w675_y + 258 + 34 <= 895, w675_y

# ===========================================================================================================================
# I Ergebnis: zurück in der Bank
# ===========================================================================================================================
folie([("erg", "Ergebnis · Die Bank bleibt außen vor"), ("erg2", "Ergebnis › Tomke gegen Herrn Stemmler: 3.500 €")], [
    *bankraum("erg"),
    *fig("TO", TOX, BODEN, FH, [("erg", "ernst_r"), ("erg2", "froh_r")], erst="cut"),
    hart(ns(NAME["TO"], TOX, BODEN, "erg", NFARBE["TO"])),
    *fig("FE", FEX, BODEN, FH, [("erg", "ruhig"), (beim("erg", "Bankberater"), "froh")], erst="cut"),
    *schalter("erg"),
    hart(ns(NAME["FE"], FEX, BODEN, "erg", NFARBE["FE"])),
    *okz("Der Bankberater hat recht.", 40, beim("erg", "Bankberater"), "Bold", 32, x=130, rechts=1700),
    z("Anweisung wirksam, die Bank bleibt außen vor", 130, 86, beim("erg", "Anweisung"), "Bold", 32, rechts=1700),
    *okz("Tomke gegen Herrn Stemmler: 3.500 €,", 150, "erg2", "Bold", 32, x=130, rechts=1700),
    z("§ 812 Abs. 1 Satz 1 Alt. 1 BGB", 130, 196, beim("erg2", "zurückverlangen"), "Bold", 32, rechts=1700),
    ficon("tabler", "coin-euro", 1250, 520, 110, beim("erg2", "zurückverlangen"), fuell=GELB),
])

# ===========================================================================================================================
# J Klausurtipp (Lexi)
# ===========================================================================================================================
folie([("tipp", "Klausurtipp · zuerst das Dreieck zeichnen"), ("tipp2", "Klausurtipp · Ist die Anweisung wirksam?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("1. Bei drei Beteiligten zuerst das", 200, 200, "tipp", "Bold", 35),
    z("Dreieck zeichnen und Deckungs- und", 200, 250, beim("tipp", "Dreieck"), "Bold", 35),
    z("Valutaverhältnis eintragen", 200, 300, beim("tipp", "trage"), "Bold", 35),
    linienzug([(130, 380), (1130, 380)], "tipp2", breite=3),
    z("2. Gibt es eine wirksame Anweisung?", 200, 410, "tipp2", "Bold", 35),
    *okz("ja: im fehlerhaften Verhältnis rückabwickeln", 480, beim("tipp2", "Wenn"), "Bold", 33, x=245),
    *neinz("nein: Direktkondiktion gegen den Empfänger", 550, beim("tipp2", "Wenn", nr=2), "Bold", 33, x=245),
    *redet("LX_warnt", FX, FB, FR + 40, "tipp", "sch"),
    ns("Lexi", FX, FB, "tipp", GELB, d=0.2),
])

# ===========================================================================================================================
# K Prüfungsschema
# ===========================================================================================================================
REIHEN = [("s1", 0, "1. Beteiligte und Verhältnisse bestimmen", True),
          (beim("s1", "Deckung"), 1, "Deckungs- und Valutaverhältnis", False),
          ("s2", 0, "2. Leistungen aus der Sicht des Empfängers zuordnen", True),
          ("s3", 0, "3. Wirksame, autorisierte Anweisung?", True),
          ("s4", 0, "4. Wenn ja: Leistungskondiktion im fehlerhaften Verhältnis", True),
          (beim("s4", "kein"), 1, "kein Durchgriff", False),
          ("s5", 0, "5. Wenn nein: Nichtleistungskondiktion der Bank", True),
          (beim("s5", "gegen"), 1, "gegen den Empfänger, § 812 Abs. 1 Satz 1 Alt. 2 BGB", False)]
els_sch = [karte(60, 50, 1800, 940, "sch"),
           titel(glyphen("Prüfungsschema: Anweisungsfälle, § 812 BGB"), 110, 90, "sch", 44)]
y = 200
for c, ebene, text, fett in REIHEN:
    x = (130, 200)[ebene]
    els_sch.append(z(text, x, y, c, "ExtraBold" if fett else "Regular", 40 if ebene == 0 else 36, rechts=1800))
    y += {0: 86, 1: 80}[ebene]
assert y <= 975, y
folie([("sch", "Prüfungsschema"), ("s1", "Prüfungsschema › 1. Beteiligte und Verhältnisse"),
       ("s2", "Prüfungsschema › 2. Leistungen zuordnen"), ("s3", "Prüfungsschema › 3. Wirksame Anweisung?"),
       ("s4", "Prüfungsschema › 4. Ja: Leistungskondiktion über Eck"), ("s5", "Prüfungsschema › 5. Nein: Direktkondiktion")],
      els_sch)

# ===========================================================================================================================
# L Merksatz (Lexi)
# ===========================================================================================================================
folie([("merke", "Merksatz")], [
    karte(80, 100, 1340, 840, "merke", fill=HELL),
    titel("Merke", 750, 150, "merke", 84, anker="m"),
    *markertext([[("Bei wirksamer Anweisung wird", 0)], [("über Eck", "a"), (" rückabgewickelt, jeder mit", 0)],
                 [("seinem ", 0), ("eigenen Vertragspartner", "b"), (".", 0)]],
                750, 270, 44, "merke", {"a": beim("merke", "Eck"), "b": beim("merke", "eigenen")}),
    *markertext([[("Fehlt eine wirksame Anweisung, holt", 0)], [("sich die Bank das Geld in aller Regel", 0)],
                 [("direkt beim Empfänger", "c"), (".", 0)]],
                750, 560, 44, "merk2", {"c": beim("merk2", "direkt")}),
    *redet("LX_erklaert", 1680, 950, 680, "merke", lexi_bis_ende("merke")),
    ns("Lexi", 1680, 950, "merke", GELB, d=0.2),
])
