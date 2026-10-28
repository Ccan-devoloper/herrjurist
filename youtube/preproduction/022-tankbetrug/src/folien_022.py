"""Folge 022 · Tankbetrug: Tanken ohne zu zahlen – Diebstahl oder Betrug? – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall, Personen erfunden. Szenen laut ../SZENENPLAN.md: A Säule drei (Tankstelle am Abend), B Sachverhalt,
C Diebstahl (Wortlaut § 242 I StGB), D1 Betrug: Wortlaut § 263 I StGB und Merkmale, D2 Subsumtion, E1 Abwandlung (Wortlaut § 22),
E2 BGH 2012 und Subsidiarität (Wortlaut § 246 I), F1 Gegenfall an der Tankstelle, F2 Renate: § 263/§ 242 (-), § 246,
F3 Streit um den Eigentumsübergang, G Klausurtipp (Lexi), H Klausurschema, I Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Zapfhahn beim Tanken, anfahrendes Auto beim Wegfahren – Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_022/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
WAND = (226, 231, 246, 255)
GLAS = (214, 230, 250, 255)
THEKE = (249, 196, 140, 255)
ASPHALT = (214, 216, 224, 255)
HC = "fluent-emoji-high-contrast"
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())
_ERSATZ_OK = {"→"}


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen); nur „→“ kommt aus der Ersatzschrift."""
    fehl = {c for c in text if ord(c) not in _CMAP and c not in _ERSATZ_OK and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    return pille(glyphen(text), *a, **k)


def tafel(cue, titel_, h=840, fill=WEISS, size=46):
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def hart(e):
    e.anim = "cut"
    return e


def bis_(e, cue):
    e.bis = cue
    return e


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def wortlaut(x, y, w, zeilen, quelle, cue, marken=(), size=31, bis=None):
    """Wortlautkarte: Normtext wörtlich (gesetze-im-internet.de), als Zitat mit Normangabe; marken = [(zeile, wort, cue)]
    legt synchron zum gesprochenen Merkmal einen Textmarker hinter das Wort."""
    lh = int(size * 1.42)
    hgt = 40 + lh * len(zeilen) + 46
    els = [bis_(karte(x, y, w, hgt, cue, fill=HELL, rund=18, schatten=6, rand=4), bis)]
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


# --- Eigene Hilfsfunktion (wie Folge 018/019): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ---------------
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
    """Wie bausteine.redet(), aber Wortende = hörbares Ende; Viseme aus der Schreibung geschätzt (kein Phonem-Alignment)."""
    cj = bausteine._cj(); ta, tb = bausteine._t(cue), bausteine._t(bis)
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


BODEN, FH = 880, 430
FX, BR, FR = 1560, 930, 470                 # Figur rechts neben der Tafel
NAMEN = {"JE": ("Jens", TUERKIS), "BI": ("Birgit", LILA), "RE": ("Renate", ORANGE)}


def name(p, cx, cue, unten=BODEN, size=28, d=0.2, bis=None, anim="pop"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


# --- Tankstelle (Fallszenen A und F) -------------------------------------------------------------------------------------
SHX0, SHX1, SHY = 60, 720, 380              # Shop-Gebäude links
BIX = 300                                   # Birgit hinter der Theke
PUX, CAR, JEX = 1000, 1560, 1215            # Zapfsäule, Auto an der Säule, Jens zwischen Säule und Auto


def tankstelle(cue, mit_birgit_ab=None):
    """Shop mit Fenster, Theke, Kasse und Bildschirm; Zapfsäule 3; Bodenlinie. Elemente stehen ab cue (harter Schnitt)."""
    return [
        hart(karte(SHX0, SHY, SHX1 - SHX0, BODEN - SHY, cue, fill=WAND, rund=10, schatten=0, rand=5, anim="cut")),
        hart(pl("Shop · Kasse", SHX1 - 140, SHY - 32, cue, fill=GELB, size=30, anker="m", anim="cut")),
        hart(karte(SHX0 + 50, SHY + 60, SHX1 - SHX0 - 100, 300, cue, fill=GLAS, rund=8, schatten=0, rand=4, anim="cut")),
        hart(karte(30, BODEN, 1860, 60, cue, fill=ASPHALT, rund=0, schatten=0, rand=0, anim="cut")),
        hart(linienzug([(30, BODEN), (1890, BODEN)], cue, breite=6, farbe=INK)),
        hart(ficon("tabler", "gas-station", PUX, BODEN, 230, cue, fuell=ROT, anim="cut")),
        hart(pl("3", PUX - 18, BODEN - 300, cue, fill=WEISS, size=34, anker="m", anim="cut")),
    ]


def theke(cue):
    """Theke vor Birgit (verdeckt ihre Beine), darauf Kasse und Bildschirm."""
    return [hart(karte(SHX0 + 30, 690, SHX1 - SHX0 - 60, 190, cue, fill=THEKE, rund=8, schatten=0, rand=5, anim="cut")),
            hart(ficon("tabler", "cash-register", 470, 692, 120, cue, fuell=WEISS, anim="cut"))]


# A Fall: Säule drei -----------------------------------------------------------------------------------------------------
JEb = ("JE_redet", JEX, BODEN, FH)
BIb = ("BI_redet_r", BIX, BODEN - 10, 400)
folie([(NULL, "Fall · Säule drei"), ("frage", "Fall · Die Frage")], [
    *tankstelle(NULL),
    hart(pl("Dienstagabend", 70, 40, NULL, fill=GELB, size=40, anim="cut")),
    hart(ficon("tabler", "moon-stars", 1790, 200, 110, NULL, fuell=GELB, anim="cut")),
    pl("Selbstbedienung", PUX, 380, beim("fall", "Selbstbedienungstankstelle"), fill=WEISS, size=30, anker="m", bis="tanken"),
    pl("am Stadtrand", 1460, 300, beim("fall", "Stadtrand"), fill=WEISS, size=30, anker="m", bis="jens"),
    # Birgit hinter der Theke (ab [birgit]), Theke steht von Anfang an
    *fig("BI", BIX, BODEN - 10, 400, [("birgit", "ruhig_r"), (beim("birgit", "Bildschirm"), "schaut_r")], bis="b1"),
    *redet("BI_redet_r", BIX, BODEN - 10, 400, "b1", "frage"),
    peep_voll("BI_ernst_r", BIX, BODEN - 10, 400, "frage", anim="cut"),
    *theke(NULL),
    ficon("tabler", "device-desktop", 620, 692, 120, beim("birgit", "Bildschirm"), fuell=GLAS),
    pl("Säule 3 läuft", 620, 470, beim("birgit", "Säule"), fill=WEISS, size=28, anker="m", bis="weg"),
    pl("lässt ihn tanken", 390, 240, beim("birgit", "lässt"), fill=GRUEN, size=30, anker="m", bis="weg"),
    name("BI", BIX, "birgit", unten=BODEN + 2),
    # Jens kommt, tankt, fährt weg
    pl("Säule drei", PUX, 470, beim("jens", "Säule"), fill=WEISS, size=30, anker="m", bis="tanken"),
    *fig("JE", JEX, BODEN, FH, [(beim("jens", "Säule", ende=True), "ruhig"), (beim("jens", "leer"), "denkt"), ("plan", "cool")], bis="j1"),
    *redet("JE_redet", JEX, BODEN, FH, "j1", "tanken"),
    *fig("JE", JEX, BODEN, FH, [("tanken", "ruhig"), (beim("tanken", "hundertzehn"), "cool")], bis=beim("weg", "steigt"), erst="cut"),
    name("JE", JEX, beim("jens", "Säule", ende=True), bis=beim("weg", "steigt")),
    ficon("tabler", "wallet-off", JEX + 170, 430, 80, beim("jens", "leer"), fuell=WEISS, bis="j1"),
    pl("Konto leer", JEX + 170, 445, beim("jens", "leer"), fill=WEISS, size=28, anker="m", bis="j1"),
    pl("beschlossen: heute nicht zahlen", 1360, 120, beim("plan", "beschlossen"), fill=ROT, size=32, anker="m", bis="j1"),
    blase("sprech", 640, 190, "j1", 1290, 210, inhalt=["Einmal volltanken, und", "dann nichts wie weg."], textsize=34,
          figur=JEb, bis="tanken"),
    szene(ficon("tabler", "droplet", PUX + 120, 690, 60, beim("tanken", "tankt"), fuell=GELB, bis=beim("weg", "Zapfhahn")), "022zapf*", 0.8, versatz=-0.9),
    pl("60 Liter Super", 1440, 220, beim("tanken", "sechzig"), fill=GELB, size=32, anker="m", bis="weg"),
    pl("110 €", 1440, 310, beim("tanken", "hundertzehn"), fill=GELB, size=34, anker="m", bis="weg"),
    pl("fährt davon", 1500, 470, beim("weg", "fährt"), fill=ROT, size=32, anker="m", bis="frage"),
    blase("sprech", 520, 190, "b1", 330, 210, inhalt=["Halt! Säule drei", "ist nicht bezahlt!"], textsize=38, figur=BIb, bis="frage"),
    pl("Diebstahl oder Betrug?", 960, 40, "frage", fill=PINK, size=40, anker="m"),
    pl("Und wenn Birgit nicht hinsieht?", 1360, 470, "frage2", fill=PINK, size=32, anker="m"),
])
# Auto fährt an die Säule (von rechts, Front nach links) und fährt nach dem Einsteigen nach rechts davon.
# Bewusst außerhalb des Bildes beginnend/endend, deshalb nach folie() angehängt (wie die Autos in Folge 001/019).
_AUTO_W = 380
FOLIEN[-1]["els"] += [
    bewegt(ficon("tabler", "car", CAR, BODEN + 30, _AUTO_W, NULL, fuell=BLAU, spiegeln=True, anim="cut", bis=beim("weg", "fährt")),
           NULL, beim("jens", "Säule", ende=True), 760),
    bis_(szene(bewegt(ficon("tabler", "car", CAR + 900, BODEN + 30, _AUTO_W, beim("weg", "fährt"), fuell=BLAU, anim="cut"),
                      beim("weg", "fährt"), ("weg", 3.6), -900), "022auto*", 1.0, versatz=-0.8), "frage"),
]

# B Sachverhalt -------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Dienstagabend an einer Selbstbedienungstankstelle: Jens hat kein Geld auf dem Konto und schon zu Hause beschlossen, "
    "nicht zu zahlen. Er tankt an Säule 3 sechzig Liter Super für 110 Euro. Kassiererin Birgit sieht auf ihrem Bildschirm, "
    "dass an Säule 3 ein Kunde tankt, und lässt ihn tanken. Dann fährt Jens davon, ohne zu bezahlen.",
    "Abwandlung: Birgit telefoniert und bemerkt den Tankvorgang gar nicht.",
    "Gegenfall: Renate tankt und will bezahlen. Erst als sie die lange Schlange an der Kasse sieht, beschließt sie, "
    "ohne zu zahlen wegzufahren, und fährt davon.",
    "(Fiktiver Fall, alle Personen erfunden.)",
], "Wie haben sich Jens und Renate strafbar gemacht?")

# C Diebstahl, § 242 ------------------------------------------------------------------------------------------------------
P242 = ["„Wer eine fremde bewegliche Sache einem anderen in der Absicht", "wegnimmt, die Sache sich oder einem Dritten rechtswidrig",
        "zuzueignen, …“"]
wl242, y242 = wortlaut(100, 170, 1060, P242, "§ 242 Abs. 1 StGB", beim("p242", "Diebstahl"), marken=[(1, "wegnimmt", "wegn")])
folie([("a", "A. Jens"), ("p242", "A. Jens › I. Diebstahl, § 242 StGB"), ("wegn", "A. Jens › I. § 242 StGB › Wegnahme"),
       ("kein242", "A. Jens › I. Diebstahl (-)")], [
    *tafel("a", "A. Jens · I. Diebstahl?"),
    *wl242,
    z("Wegnahme = fremden Gewahrsam brechen", 110, y242 + 30, "wegn", "Bold", 36),
    z("Tankstelle lässt ihn tanken:", 110, y242 + 100, "erlaubt", size=36),
    z("Birgit ist mit dem Einfüllen einverstanden", 150, y242 + 150, beim("erlaubt", "Birgit"), size=34),
    z("BGH: durch Täuschung bewirktes Geben,", 110, y242 + 225, "geben", "Bold", 36),
    z("kein Nehmen", 150, y242 + 278, beim("geben", "kein"), "Bold", 36),
    nein(135, y242 + 375, "kein242", gr=24), z("Diebstahl scheidet aus", 175, y242 + 352, "kein242", "Bold", 38),
    *fig("JE", FX, BR, FR, [("a", "ruhig"), ("erlaubt", "cool"), ("kein242", "ruhig")]),
    name("JE", FX, "a", unten=BR),
    ficon("tabler", "gas-station", 1400, 380, 140, "erlaubt", fuell=ROT),
    ok(1490, 250, beim("erlaubt", "einverstanden"), gr=30),
    pl("Geben", 1400, 400, beim("geben", "Geben"), fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "hand-grab", 1760, 380, 120, beim("geben", "Nehmen"), fuell=WEISS),
    kreuz_i(1760, 320, beim("geben", "Nehmen"), gr=44),
    pl("Nehmen", 1760, 400, beim("geben", "Nehmen"), fill=WEISS, size=30, anker="m"),
])

# D1 Betrug: Wortlaut § 263 I, Merkmale ------------------------------------------------------------------------------------
P263 = ["„Wer in der Absicht, sich oder einem Dritten einen rechtswidrigen", "Vermögensvorteil zu verschaffen, das Vermögen eines anderen",
        "dadurch beschädigt, daß er durch Vorspiegelung falscher oder", "durch Entstellung oder Unterdrückung wahrer Tatsachen einen",
        "Irrtum erregt oder unterhält, …“"]
wl263, y263 = wortlaut(100, 170, 1060, P263, "§ 263 Abs. 1 StGB", beim("p263", "Betrug"),
                       marken=[(2, "Vorspiegelung falscher", beim("merkm", "Täuschung")), (4, "Irrtum", beim("merkm", "Irrtum")),
                               (2, "beschädigt", beim("merkm", "Schaden")), (0, "Absicht", beim("merkm", "Absicht"))])
MK = [("Täuschung", "Täuschung", 110, 0), ("Irrtum", "Irrtum", 350, 0), ("Vermögensverfügung", "Vermögensverfügung", 545, 0),
      ("Schaden", "Schaden", 110, 1), ("Vorsatz", "Vorsatz", 330, 1), ("Bereicherungsabsicht", "Absicht", 535, 1)]
folie([("p263", "A. Jens › II. Betrug, § 263 StGB")], [
    *tafel("p263", "A. Jens · II. Betrug?"),
    *wl263,
    *[pl(t, x, y263 + 30 + r * 78, beim("merkm", w), fill=(GELB if r == 0 else LILA), size=32) for t, w, x, r in MK],
    *fig("JE", FX, BR, FR, [("p263", "denkt")]),
    name("JE", FX, "p263", unten=BR),
])

# D2 Betrug: Subsumtion ------------------------------------------------------------------------------------------------
BX2 = 1720
folie([("taeu", "A. Jens › II. § 263 StGB › 1. Täuschung"), ("irr", "A. Jens › II. § 263 StGB › 2. Irrtum"),
       ("verf", "A. Jens › II. § 263 StGB › 3. Vermögensverfügung"), ("schad", "A. Jens › II. § 263 StGB › 4. Schaden"),
       ("subj", "A. Jens › II. § 263 StGB › 5. Vorsatz, Bereicherungsabsicht"), ("erg1", "A. Jens › Ergebnis")], [
    *tafel("taeu", "II. Betrug, § 263 StGB"),
    z("1. Täuschung: tritt auf wie jeder Kunde", 110, 190, "taeu", "Bold", 34),
    z("schlüssig: „Ich bezahle nach dem Tanken.“", 150, 240, "konkl", size=33),
    ok(135, 312, "falsch", gr=22), z("falsch: von Anfang an nicht zahlungswillig", 175, 290, "falsch", size=33),
    ok(135, 382, "irr", gr=22), z("2. Irrtum: Birgit sieht ihn, hält ihn für zahlungsbereit", 175, 360, "irr", "Bold", 31),
    ok(135, 452, "verf", gr=22), z("3. Verfügung: gestattet das Tanken", 175, 430, "verf", "Bold", 34),
    ok(135, 522, "schad", gr=22), z("4. Schaden: Benzin weg, ohne Gegenwert", 175, 500, "schad", "Bold", 34),
    ok(135, 592, "subj", gr=22), z("5. Vorsatz, Absicht rechtswidriger Bereicherung", 175, 570, "subj", "Bold", 33),
    fl_block(110, 660, 1040, 110, GRUEN, "erg1", [("Jens: Betrug, § 263 Abs. 1 StGB", "ExtraBold", 40, INK)]),
    *fig("JE", 1380, BR, FR, [("taeu", "ruhig"), ("konkl", "cool"), ("falsch", "denkt"), ("schad", "cool"), ("erg1", "ertappt")]),
    name("JE", 1380, "taeu", unten=BR),
    *fig("BI", BX2, BR - 6, FR - 20, [("irr", "schaut"), ("schad", "ernst")]),
    name("BI", BX2, "irr", unten=BR - 6),
    pl("hält ihn für zahlungsbereit", 1540, 120, beim("irr", "hält"), fill=WEISS, size=28, anker="m", bis="verf"),
    pl("gestattet das Tanken", 1540, 120, "verf", fill=GRUEN, size=30, anker="m", bis="schad"),
    ficon("tabler", "droplet", 1460, 250, 70, "schad", fuell=GELB),
    ficon("tabler", "coin-euro", 1640, 250, 80, "schad", fuell=WEISS),
    kreuz_i(1640, 210, "schad", gr=28),
    pl("ohne Gegenwert", 1550, 270, beim("schad", "Gegenwert"), fill=ROT, size=28, anker="m"),
])

# E1 Abwandlung: niemand bemerkt den Tankvorgang -----------------------------------------------------------------------------
P22 = ["„Eine Straftat versucht, wer nach seiner Vorstellung von der Tat", "zur Verwirklichung des Tatbestandes unmittelbar ansetzt.“"]
wl22, y22 = wortlaut(100, 440, 1060, P22, "§ 22 StGB", "vers", marken=[(0, "nach seiner Vorstellung", "vers"),
                                                                     (1, "unmittelbar ansetzt", beim("vers", "unmittelbar"))])
folie([("abw", "A. Abwandlung › Birgit bemerkt nichts"), ("kirr", "A. Abwandlung › II. § 263 StGB › 2. Irrtum (-)"),
       ("vers", "A. Abwandlung › III. versuchter Betrug, §§ 263, 22, 23 StGB")], [
    *tafel("abw", "Abwandlung: Birgit bemerkt nichts"),
    z("Birgit telefoniert, sieht Jens gar nicht", 110, 190, "abw", "Bold", 36),
    nein(135, 280, "kirr", gr=22), z("kein Irrtum", 175, 258, "kirr", "Bold", 36),
    z("→ Betrug nicht vollendet", 175, 315, beim("kirr", "ohne"), size=36),
    *wl22,
    fl_block(110, y22 + 30, 1040, 150, GRUEN, "vers2", [("Jens: versuchter Betrug", "ExtraBold", 40, INK),
                                                        ("§§ 263, 22, 23 StGB", "Regular", 34, INK)]),
    *fig("BI", 1440, BR, FR, [("abw", "froh")]),
    ficon("tabler", "phone-call", 1555, 520, 90, beim("abw", "telefoniert"), fuell=GELB),
    name("BI", 1440, "abw", unten=BR),
    *fig("JE", 1760, BR, FR, [("abw", "cool"), ("vers2", "ertappt")]),
    name("JE", 1760, "abw", unten=BR),
    pl("nicht bemerkt", 1440, 120, beim("abw", "bemerkt"), fill=PINK, size=30, anker="m"),
])

# E2 BGH 2012, Subsidiarität § 246 -----------------------------------------------------------------------------------------
P246 = ["„Wer eine fremde bewegliche Sache sich oder einem Dritten", "rechtswidrig zueignet, wird mit Freiheitsstrafe bis zu drei Jahren",
        "oder mit Geldstrafe bestraft, wenn die Tat nicht in anderen", "Vorschriften mit schwererer Strafe bedroht ist.“"]
wl246s, y246s = wortlaut(100, 470, 1060, P246, "§ 246 Abs. 1 StGB", "subs",
                         marken=[(2, "wenn die Tat nicht in anderen", beim("subs", "greift")),
                                 (3, "mit schwererer Strafe bedroht ist", beim("subs", "schwererer"))])
folie([("bgh12", "A. Abwandlung › BGH, 10.1.2012 – 4 StR 632/11"), ("subs", "A. Abwandlung › § 246 StGB tritt zurück")], [
    *tafel("bgh12", "BGH, Beschl. v. 10.1.2012 – 4 StR 632/11"),
    z("NJW 2012, 1092", 110, 165, "bgh12", size=30, farbe=TEXT),
    z("nicht geklärt: Hat die Kassiererin etwas bemerkt?", 110, 230, beim("bgh12", "Das"), "Bold", 34),
    ok(135, 322, "zugunsten", gr=22), z("zugunsten des Täters: nur Versuch", 175, 300, "zugunsten", "Bold", 36),
    z("Unterschlagung tritt dahinter zurück", 110, 385, "subs", "Bold", 36),
    *wl246s,
    ficon("tabler", "gavel", 1500, 360, 150, "bgh12", fuell=GELB),
    pl("bemerkt?", 1500, 120, beim("bgh12", "bemerkt"), fill=PINK, size=30, anker="m"),
    *fig("JE", 1720, BR, FR, [("bgh12", "muede")]),
    name("JE", 1720, "bgh12", unten=BR),
    pl("§ 246: subsidiär", 1460, 470, beim("subs", "greift"), fill=WEISS, size=30, anker="m"),
])

# F1 Gegenfall an der Tankstelle ----------------------------------------------------------------------------------------
REX = JEX
REb = ("RE_redet", REX, BODEN, FH)
folie([("gegen", "B. Gegenfall: Renate")], [
    *tankstelle("gegen"),
    *fig("BI", BIX, BODEN - 10, 400, [("gegen", "ruhig_r")]),
    *theke("gegen"),
    hart(ficon("tabler", "device-desktop", 620, 692, 120, "gegen", fuell=GLAS, anim="cut")),
    hart(name("BI", BIX, "gegen", unten=BODEN + 2, anim="cut", d=0.0)),
    hart(ficon("tabler", "car", CAR, BODEN + 30, _AUTO_W, "gegen", fuell=GRUEN, spiegeln=True, anim="cut", bis="rweg")),
    *fig("RE", REX, BODEN, FH, [(("gegen", 0.3), "froh"), ("schlange", "denkt")], bis="r1"),
    *redet("RE_redet", REX, BODEN, FH, "r1", "rweg"),
    name("RE", REX, ("gegen", 0.3), bis="rweg"),
    pl("will bezahlen", REX, 300, beim("gegen", "bezahlen"), fill=GRUEN, size=30, anker="m", bis="schlange"),
    ficon("tabler", "users-group", 540, 872, 120, beim("schlange", "Schlange"), fuell=GRAU),
    ficon("tabler", "users", 650, 872, 100, beim("schlange", "Schlange"), fuell=GRAU, d=0.15),
    pl("lange Schlange", (SHX0 + SHX1) / 2, 250, beim("schlange", "Schlange"), fill=WEISS, size=30, anker="m"),
    blase("sprech", 600, 190, "r1", 1300, 210, inhalt=["Die Schlange ist mir zu lang.", "Dann eben nicht."], textsize=34,
          figur=REb, bis="rweg"),
    pl("fährt davon", 1500, 470, beim("rweg", "fährt"), fill=ROT, size=32, anker="m"),
])
FOLIEN[-1]["els"] += [
    szene(bewegt(ficon("tabler", "car", CAR + 900, BODEN + 30, _AUTO_W, "rweg", fuell=GRUEN, anim="cut"),
                 "rweg", ("rweg", 1.4), -900), "022auto*", 1.0, versatz=-0.8),
]

# F2 Renate: § 263, § 242 (-), § 246 ----------------------------------------------------------------------------------------
wl246, y246 = wortlaut(100, 380, 1060, P246, "§ 246 Abs. 1 StGB", "p246", marken=[(0, "fremde", "fremd")])
folie([("r263", "B. Renate › Betrug, Diebstahl (-)"), ("p246", "B. Renate › Unterschlagung, § 246 StGB"),
       ("fremd", "B. Renate › § 246 StGB › fremde Sache?")], [
    *tafel("r263", "B. Gegenfall: Renate"),
    nein(135, 213, "r263", gr=22), z("Betrug: beim Tanken zahlungswillig,", 175, 190, "r263", size=34),
    z("also keine Täuschung", 215, 240, beim("r263", "also"), size=34),
    nein(135, 318, "r242", gr=22), z("Diebstahl: das Tanken war erlaubt", 175, 295, "r242", size=34),
    *wl246,
    pl("beim Wegfahren noch fremd?", 110, y246 + 30, "fremd", fill=PINK, size=34),
    pl("umstritten", 640, y246 + 30, beim("fremd", "umstritten"), fill=GELB, size=34),
    *fig("RE", FX, BR, FR, [("r263", "ruhig"), ("fremd", "denkt")]),
    name("RE", FX, "r263", unten=BR),
    ficon("tabler", "droplet", 1560, 330, 90, beim("fremd", "Benzin"), fuell=GELB),
    pl("Benzin noch fremd?", 1560, 360, beim("fremd", "Benzin"), fill=WEISS, size=28, anker="m"),
])

# F3 Streit um den Eigentumsübergang ----------------------------------------------------------------------------------------
folie([("ans1", "B. Renate › § 246 StGB › Streit: Eigentumsübergang"), ("offen", "B. Renate › § 246 StGB › BGH: offen")], [
    *tafel("ans1", "Wann geht das Eigentum über?"),
    karte(100, 165, 1060, 175, "ans1", rund=18, schatten=6, rand=5),
    z("1. Schon beim Einfüllen Eigentümerin", 130, 185, "ans1", "ExtraBold", 34, rechts=1150),
    z("Renate straflos, schuldet nur den Kaufpreis", 170, 255, beim("ans1", "straflos"), size=32, rechts=1150),
    z("OLG Düsseldorf, NStZ 1982, 249", 130, 350, beim("olg", "Düsseldorf"), "Bold", 27, farbe=TEXT),
    karte(100, 405, 1060, 175, "ans2", rund=18, schatten=6, rand=5),
    z("2. Ware gegen Geld: Eigentum erst mit dem Bezahlen", 130, 425, "ans2", "ExtraBold", 34, rechts=1150),
    z("Benzin bleibt fremd: Unterschlagung (+)", 170, 495, "unt", size=32, rechts=1150),
    z("OLG Hamm, NStZ 1983, 266 · OLG Koblenz, 10.8.1998 – 2 Ss 206/98", 130, 590, "olg", "Bold", 27, farbe=TEXT),
    z("Vermischung im Tank: Miteigentum hindert § 246 nicht (OLG Koblenz)", 110, 665, "misch", size=30),
    fl_block(100, 750, 1060, 110, GELB, "offen", [("BGH: Frage offengelassen (NJW 1983, 2827)", "ExtraBold", 34, INK)]),
    *fig("RE", FX, BR, FR, [("ans1", "froh"), ("ans2", "denkt"), ("unt", "ruhig")]),
    name("RE", FX, "ans1", unten=BR),
    ficon("tabler", "receipt-euro", 1440, 320, 90, beim("ans1", "Kaufpreis"), fuell=WEISS),
    pl("Kaufpreis", 1440, 340, beim("ans1", "Kaufpreis"), fill=WEISS, size=28, anker="m", bis="ans2"),
    ficon("tabler", "coin-euro", 1680, 320, 90, beim("ans2", "Ware"), fuell=GELB),
    pl("Ware gegen Geld", 1680, 340, beim("ans2", "Ware"), fill=GELB, size=28, anker="m"),
])

# G Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Zeitpunkt des Entschlusses")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Wann beschließt der Täter, nicht zu zahlen?", 200, 200, beim("tipp", "Entscheidend"), "Bold", 36),
    z("Schon vor dem Tanken: Betrug prüfen", 200, 300, "tipp1", "Bold", 36),
    z("Hat das Personal den Vorgang bemerkt?", 240, 355, beim("tipp1", "frage"), size=34),
    z("Bleibt das offen: zugunsten des Täters nur Versuch", 240, 430, "tipp2", size=34),
    z("Erst danach: Unterschlagung prüfen", 200, 530, "tipp3", "Bold", 36),
    z("Streit ums Eigentum entscheiden", 240, 585, beim("tipp3", "entscheide"), size=34),
    ficon("tabler", "clock", 1800, 300, 100, beim("tipp", "wann"), fuell=GELB),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# H Klausurschema -------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Tanken ohne zu zahlen", 110, 90, "sch", 54),
    z("A. Entschluss schon vor dem Tanken", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("I. Diebstahl, § 242 StGB: scheitert an der Wegnahme (Geben statt Nehmen)", K2, 265, "k1a", size=34, rechts=1820),
    z("II. Betrug, § 263 StGB: Täuschung, Irrtum, Verfügung, Schaden, Vorsatz, Bereicherungsabsicht", K2, 320, "k1b",
      size=32, rechts=1820),
    z("III. Fehlt der Irrtum: nur Betrugsversuch, §§ 263, 22, 23 StGB", K2, 375, "k1c", size=34, rechts=1820),
    z("Unterschlagung, § 246 StGB, tritt zurück", K3, 430, "k1d", size=32, farbe=TEXT, rechts=1820),
    z("B. Entschluss erst nach dem Tanken", K1, 530, "k2", "Bold", 40, rechts=1820),
    z("Betrug und Diebstahl scheiden aus", K2, 595, "k2a", size=34, rechts=1820),
    z("Unterschlagung nur, wenn das Benzin noch der Tankstelle gehört (Streit)", K2, 650, "k2b", size=34, rechts=1820),
])

# I Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Wer schon zahlungsunwillig tankt,", 0)], [("begeht ", 0), ("Betrug.", "a")]], 750, 300, 48, "merke",
                {"a": beim("merke", "Betrug")}),
    *markertext([[("Bemerkt ihn niemand: ", 0), ("Versuch.", "b")]], 750, 460, 44, "m2", {"b": beim("m2", "Versuch")}),
    *markertext([[("Entschluss erst danach: höchstens", 0)], [("Unterschlagung", "c"), (", wenn das Benzin", 0)],
                 [("noch ", 0), ("fremd", "d"), (" ist.", 0)]], 750, 560, 44, "m3",
                {"c": beim("m3", "Unterschlagung"), "d": beim("m3", "fremd")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
