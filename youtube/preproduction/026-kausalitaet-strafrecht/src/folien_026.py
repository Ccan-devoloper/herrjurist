"""Folge 026 · Kausalität im Strafrecht: Conditio-sine-qua-non einfach erklärt – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall, Personen erfunden. Szenen laut ../SZENENPLAN.md: A Am Dorfkiosk, B Die Scheune brennt (Nacht), C Sachverhalt,
D Erfolgsdelikte (Wortlaut §§ 212 I, 222, 306 I Nr. 1 StGB), E Bedingungstheorie, F Formel am Fall (Wegdenken), G Ersatzursache,
H Unterbrechung?, I Nur die erste Hürde, J Abwandlung 1 (überholende Kausalität), K Abwandlung 2 (alternative Kausalität),
L Abwandlung 3 (kumulative Kausalität), M Ausblick Unterlassen, N Klausurtipp (Lexi), O Klausurschema, P Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: Feuerzeug zündet, Feuer knistert, Blitz/Donner – Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_026/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
WAND = (238, 232, 246, 255)
GLAS = (214, 230, 250, 255)
THEKE = (249, 196, 140, 255)
STROH = (246, 222, 140, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())
_ERSATZ_OK = {"→"}


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen); nur „→“ kommt aus der Ersatzschrift (nur über zeile())."""
    fehl = {c for c in text if ord(c) not in _CMAP and c not in _ERSATZ_OK and not c.isspace()}
    assert not fehl, f"Zeichen fehlt in Nunito: {fehl} in {text!r}"
    return text


def z(text, x, y, cue, stil="Regular", size=36, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(glyphen(text), x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def pl(text, *a, **k):
    assert "→" not in text, "→ nur über zeile() (Ersatzschrift)"
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


def grau(e):
    """Requisit „weggedacht“: Linien und Flächen ausgegraut (gleiches Icon, nur blasser)."""
    a = np.asarray(e.sprite).copy()
    a[..., :3] = (a[..., :3].astype(float) * 0.35 + 255 * 0.65).astype(np.uint8)
    e.sprite = Image.fromarray(a)
    e.name = (e.name or "") + ":grau"
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


# --- Eigene Hilfsfunktion (wie Folge 018/019/022): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ------------
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
NAMEN = {"EG": ("Egon", GRUEN), "BO": ("Bodo", ROT), "MA": ("Maren", BLAU), "SI": ("Silke", LILA)}


def name(p, cx, cue, unten=BODEN, size=28, d=0.2, bis=None, anim="pop", text=None):
    t, f = NAMEN[p]
    return pl(text or t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def flammen(cx, unten, breite, cue, bis=None, n=3, d=0.0):
    """Feuer am Gebäude: mehrere Tabler-Flammen (Orange/Gelb), nebeneinander."""
    els = []
    for i in range(n):
        dx = (i - (n - 1) / 2) * breite * 0.62
        els.append(ficon("tabler", "flame", cx + dx, unten - (18 if i % 2 else 0), int(breite * (1.0 if i % 2 else 0.8)), cue,
                         fuell=(GELB if i % 2 else ORANGE), d=d + 0.08 * i, bis=bis))
    return els


def scheune(cx, unten, breite, cue, anim="pop", bis=None):
    return ficon("ph", "barn", cx, unten, breite, cue, fuell=ROT, nebenfarbe=WEISS, anim=anim, bis=bis)


# A Fall: am Dorfkiosk -----------------------------------------------------------------------------------------------------
KX0, KX1 = 240, 1000                        # Kiosk-Häuschen
EGX, BOX = 620, 1250                        # Egon hinter der Theke, Bodo vor dem Kiosk
EGb = ("EG_redet_r", EGX, BODEN - 10, 400)
BOb = ("BO_redet", BOX, BODEN, FH)
folie([(NULL, "Fall · Am Dorfkiosk")], [
    hart(karte(KX0, 230, KX1 - KX0, BODEN - 230, NULL, fill=WAND, rund=10, schatten=0, rand=5, anim="cut")),
    hart(karte(KX0 - 30, 150, KX1 - KX0 + 60, 90, NULL, fill=ROT, rund=12, schatten=0, rand=5, anim="cut")),
    hart(pl("Kiosk", (KX0 + KX1) / 2, 163, NULL, fill=GELB, size=36, anker="m", anim="cut")),
    hart(karte(KX0 + 50, 270, KX1 - KX0 - 100, 420, NULL, fill=GLAS, rund=8, schatten=0, rand=4, anim="cut")),
    hart(linienzug([(40, BODEN), (1880, BODEN)], NULL, breite=6, farbe=INK)),
    hart(pl("Freitagabend", 70, 40, NULL, fill=GELB, size=40, anim="cut")),
    hart(ficon("tabler", "sunset-2", 1760, 220, 130, NULL, fuell=GELB, anim="cut")),
    hart(ficon("tabler", "news", 360, 520, 80, NULL, fuell=WEISS, anim="cut")),
    hart(ficon("tabler", "bottle", 880, 520, 60, NULL, fuell=BLAU, anim="cut")),
    # Egon hinter der Theke (ab [egon]); die Theke liegt darüber und verdeckt die Beine
    *fig("EG", EGX, BODEN - 10, 400, [("egon", "ruhig_r")], bis="e1"),
    *redet("EG_redet_r", EGX, BODEN - 10, 400, "e1", "ahnt"),
    peep_voll("EG_froh_r", EGX, BODEN - 10, 400, "ahnt", anim="cut"),
    hart(karte(KX0 + 30, 690, KX1 - KX0 - 60, 190, NULL, fill=THEKE, rund=8, schatten=0, rand=5, anim="cut")),
    name("EG", EGX, "egon", unten=BODEN + 2, text="Egon, Kiosk"),
    pl("Mitte 60", EGX, 420, beim("egon", "Mitte"), fill=WEISS, size=28, anker="m", bis="e1"),
    # Bodo kommt herein und wartet vor der Theke
    bewegt(peep_voll("BO_ruhig", BOX, BODEN, FH, "bodo", anim="cut", bis="b1"), "bodo", beim("bodo", "herein", ende=True), 420),
    *redet("BO_redet", BOX, BODEN, FH, "b1", "e1"),
    *fig("BO", BOX, BODEN, FH, [("e1", "ruhig"), (beim("ahnt", "Egon"), "schleicht")], erst="cut"),
    bewegt(name("BO", BOX, "bodo", d=0.0, anim="cut"), "bodo", beim("bodo", "herein", ende=True), 420),
    blase("sprech", 520, 190, "b1", 1450, 210, inhalt=["Ein Feuerzeug, bitte."], textsize=38, figur=BOb, bis="e1"),
    blase("sprech", 440, 170, "e1", 620, 345, inhalt=["Macht zwei Euro."], textsize=38, figur=EGb, bis="ahnt"),
    ficon("tabler", "lighter", 820, 692, 70, beim("e1", "Macht"), fuell=ROT),
    ficon("tabler", "coin-euro", 920, 692, 60, beim("e1", "Euro"), fuell=GELB),
    pl("ahnt nichts", EGX, 420, beim("ahnt", "ahnt"), fill=GRUEN, size=30, anker="m"),
])

# B Fall: die Scheune brennt (Nacht) -----------------------------------------------------------------------------------
SCX = 720                                    # Scheune
BOn, MAX = 1240, 1560
MAb = ("MA_redet", MAX, BODEN, FH)
folie([("nacht", "Fall · Die Scheune brennt"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(40, BODEN), (1880, BODEN)], "nacht", breite=6, farbe=INK)),
    hart(pl("In der Nacht", 70, 40, "nacht", fill=LILA, size=40, anim="cut")),
    hart(ficon("tabler", "moon-stars", 1780, 220, 110, "nacht", fuell=GELB, anim="cut")),
    hart(scheune(SCX, BODEN, 560, "nacht", anim="cut")),
    hart(karte(SCX - 100, BODEN - 70, 200, 70, "nacht", fill=STROH, rund=10, schatten=0, rand=4, anim="cut")),
    hart(pl("Stroh", SCX, BODEN - 52, "nacht", fill=WEISS, size=24, anker="m", anim="cut")),
    pl("Scheune der Landwirtin Maren", SCX, 160, beim("nacht", "Scheune"), fill=WEISS, size=32, anker="m", bis="frage"),
    bewegt(peep_voll("BO_schleicht", BOn, BODEN, FH, "nacht", anim="cut", bis="zuend"), "nacht", beim("nacht", "Maren"), 520),
    peep_voll("BO_zuendet", BOn, BODEN, FH, "zuend", anim="cut", bis="brand"),
    bewegt(name("BO", BOn, "nacht", d=0.0, bis="brand", anim="cut"), "nacht", beim("nacht", "Maren"), 520),
    szene(ficon("tabler", "lighter", BOn - 120, 640, 64, beim("zuend", "Feuerzeug"), fuell=ROT, bis="brand"), "026feuerzeug*", 1.0, -0.05),
    ficon("tabler", "flame", SCX - 60, BODEN - 64, 70, beim("zuend", "Stroh"), fuell=ORANGE, bis="brand"),
    pl("zündet das Stroh an", BOn, 300, beim("zuend", "zündet"), fill=ORANGE, size=30, anker="m", bis="brand"),
    *flammen(SCX, 430, 170, "brand", bis=None),
    szene(ficon("tabler", "flame", SCX - 60, BODEN - 64, 90, "brand", fuell=GELB), "026feuer*", 1.0, 0.0),
    pl("verletzt wird niemand", 1180, 300, beim("brand", "verletzt"), fill=GRUEN, size=30, anker="m", bis="frage"),
    *fig("MA", MAX, BODEN, FH, [(beim("brand", "verletzt"), "traurig")], bis="m1"),
    *redet("MA_redet", MAX, BODEN, FH, "m1", "frage"),
    peep_voll("MA_traurig", MAX, BODEN, FH, "frage", anim="cut"),
    name("MA", MAX, beim("brand", "verletzt"), text="Maren, Landwirtin"),
    blase("sprech", 440, 190, "m1", 1560, 300, inhalt=["Meine Scheune!"], textsize=40, figur=MAb, bis="frage"),
    pl("Verkauf des Feuerzeugs kausal für den Brand?", 960, 130, "frage", fill=PINK, size=36, anker="m"),
    ficon("tabler", "building-store", 1300, 560, 120, "frage", fuell=WEISS),
    ficon("tabler", "lighter", 1300, 640, 60, "frage", fuell=ROT),
    pl("Egon strafbar?", 1300, 220, "frage2", fill=PINK, size=34, anker="m"),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Freitagabend kauft Bodo bei Kioskbesitzer Egon (Mitte 60) ein Feuerzeug für 2 Euro. Egon ahnt nichts von Bodos Plan. "
    "In der Nacht zündet Bodo mit dem Feuerzeug das Stroh in der Scheune der Landwirtin Maren an. Die Scheune brennt "
    "nieder, verletzt wird niemand.",
    "Abwandlung 1: Bodos Kerze im Stroh soll erst in einer Stunde zünden; vorher brennt die Scheune durch einen Blitz ab.",
    "Abwandlung 2: Silke legt unabhängig am anderen Ende Feuer; jedes Feuer hätte allein gereicht. "
    "Abwandlung 3: Jedes Feuer wäre allein erloschen. (Fiktiver Fall, Personen erfunden.)",
], "Ist der Verkauf kausal für den Brand?")

# D Erfolgsdelikte: Wortlaut §§ 212 I, 222, 306 I Nr. 1 -----------------------------------------------------------------
P212 = ["„Wer einen Menschen tötet, ohne Mörder zu sein, wird als", "Totschläger mit Freiheitsstrafe nicht unter fünf Jahren bestraft.“"]
wl212, y212 = wortlaut(100, 240, 1060, P212, "§ 212 Abs. 1 StGB", beim("erfolg", "Tod"),
                       marken=[(0, "tötet", beim("erfolg", "Totschlag"))])
P222 = ["„Wer durch Fahrlässigkeit den Tod eines Menschen verursacht, wird", "mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.“"]
wl222, y222 = wortlaut(100, y212 + 18, 1060, P222, "§ 222 StGB", "p222", marken=[(0, "verursacht", beim("p222", "verursacht"))])
P306 = ["„Wer fremde 1. Gebäude oder Hütten, … in Brand setzt …, wird", "mit Freiheitsstrafe von einem Jahr bis zu zehn Jahren bestraft.“"]
wl306, y306 = wortlaut(100, y222 + 18, 1060, P306, "§ 306 Abs. 1 Nr. 1 StGB", beim("p306", "Brand"),
                       marken=[(0, "in Brand setzt", beim("p306", "Brandstiftung"))])
folie([("erfolg", "Erfolgsdelikte › Erfolg im Tatbestand"), ("p222", "Erfolgsdelikte › § 222 StGB: „verursacht“"),
       ("p306", "Erfolgsdelikte › Brandstiftung, § 306 Abs. 1 Nr. 1 StGB")], [
    *tafel("erfolg", "Kausalität bei Erfolgsdelikten"),
    z("Ein Erfolg gehört zum Tatbestand", 110, 175, beim("erfolg", "Dort"), "Bold", 36),
    *wl212, *wl222, *wl306,
    *fig("MA", FX, BR, FR, [("erfolg", "traurig")]),
    name("MA", FX, "erfolg", unten=BR),
    scheune(FX, 400, 240, beim("p306", "Brand")),
    *flammen(FX, 250, 80, beim("p306", "Brand"), d=0.1),
    pl("Erfolg: Brand", FX, 120, beim("p306", "Brand"), fill=ORANGE, size=30, anker="m"),
])

# E Bedingungstheorie ----------------------------------------------------------------------------------------------------
folie([("csqn", "A. Kausalität › Bedingungstheorie (BGH)"), ("formel", "A. Kausalität › Conditio-sine-qua-non-Formel"),
       ("aequi", "A. Kausalität › Äquivalenztheorie (Lehre)")], [
    *tafel("csqn", "Wann ist eine Handlung ursächlich?"),
    z("BGH: Bedingungstheorie", 110, 190, beim("csqn", "Bundesgerichtshof"), "ExtraBold", 38),
    z("Ursächlich ist jede Bedingung, die nicht", 150, 265, "formel", size=36),
    z("hinweggedacht werden kann, ohne dass der Erfolg", 150, 315, beim("formel", "hinweggedacht"), size=36),
    z("in seiner konkreten Gestalt entfiele", 150, 365, beim("formel", "in"), "Bold", 36),
    z("BGH, 4 StR 138/22, Rn. 11; BGHSt 39, 195, 197", 150, 425, beim("formel", "in"), "Bold", 27, farbe=TEXT),
    pl("Conditio-sine-qua-non-Formel", 150, 490, beim("formel", "Conditio"), fill=GELB, size=34),
    z("Lehre: Äquivalenztheorie", 110, 610, "aequi", "ExtraBold", 38),
    z("alle Bedingungen sind gleichwertig", 150, 665, beim("aequi", "alle"), size=36),
    *fig("EG", FX, BR, FR, [("csqn", "denkt")]),
    name("EG", FX, "csqn", unten=BR),
    ficon("tabler", "help-circle", FX, 330, 110, "csqn", fuell=GELB, bis="aequi"),
    # drei Bedingungen, gleichwertig
    ficon("tabler", "building-store", 1360, 330, 100, "aequi", fuell=WEISS),
    pl("=", 1460, 260, beim("aequi", "alle"), fill=WEISS, size=34, anker="m"),
    ficon("tabler", "lighter", 1560, 330, 60, "aequi", fuell=ROT, d=0.1),
    pl("=", 1660, 260, beim("aequi", "alle"), fill=WEISS, size=34, anker="m"),
    ficon("tabler", "flame", 1760, 330, 80, "aequi", fuell=ORANGE, d=0.2),
    pl("gleichwertig", FX, 380, beim("aequi", "gleichwertig"), fill=GELB, size=30, anker="m"),
])

# F Formel am Fall: Wegdenken ---------------------------------------------------------------------------------------------
CX, LBX = 1370, 1640                        # Kette rechts: Icons und Beschriftungen
YF, YK, YL, YB = 215, 430, 620, 880         # Unterkanten: Hersteller, Kiosk, Feuerzeug, Scheune
PF = "A. Kausalität › Formel am Fall"
folie([("bodo_k", f"{PF} › Bodo: Anzünden"), ("egon_k", f"{PF} › Egon: Verkauf"), ("weit", f"{PF} › reicht sehr weit")], [
    *tafel("bodo_k", "Wegdenken: Wer ist kausal?"),
    z("1. Bodo: das Anzünden weggedacht", 110, 185, "bodo_k", "Bold", 36),
    z("→ die Scheune brennt nicht", 150, 237, beim("bodo_k", "dann"), size=34),
    ok(165, 315, beim("bodo_k", "Kausal"), gr=22), z("Anzünden: kausal", 205, 292, beim("bodo_k", "Kausal"), "Bold", 34),
    z("2. Egon: den Verkauf weggedacht", 110, 375, "egon_k", "Bold", 36),
    z("→ Bodo hat in dieser Nacht kein Feuerzeug", 150, 427, beim("egon_k", "dann"), size=34),
    z("→ die Scheune brennt nicht so, wie sie gebrannt hat", 150, 477, beim("egon_k", "und"), size=33),
    ok(165, 557, beim("egon_k", "Auch"), gr=22), z("auch der Verkauf: kausal", 205, 534, beim("egon_k", "Auch"), "Bold", 34),
    z("3. sogar der Hersteller des Feuerzeugs: kausal", 110, 620, beim("weit", "sogar"), "Bold", 34),
    fl_block(110, 700, 1040, 120, GELB, beim("weit", "Die"), [("Die Formel allein reicht sehr weit", "ExtraBold", 40, INK)]),
    # Kette rechts: Kiosk (Egon) → Feuerzeug (Bodo) → Scheune (Brand)
    ficon("tabler", "building-store", CX, YK, 130, "bodo_k", fuell=WEISS, bis=beim("egon_k", "Denk")),
    grau(ficon("tabler", "building-store", CX, YK, 130, beim("egon_k", "Denk"), fuell=WEISS, anim="cut", bis="weit")),
    hart(ficon("tabler", "building-store", CX, YK, 130, "weit", fuell=WEISS)),
    pl("Egon: Verkauf", LBX, YK - 95, "bodo_k", fill=GRUEN, size=28, anker="m"),
    pfeil_ink(CX, YK + 20, CX, YL - 110, "bodo_k"),
    ficon("tabler", "lighter", CX, YL, 70, "bodo_k", fuell=ROT, bis=beim("bodo_k", "Denk")),
    grau(ficon("tabler", "lighter", CX, YL, 70, beim("bodo_k", "Denk"), fuell=ROT, anim="cut", bis="egon_k")),
    hart(ficon("tabler", "lighter", CX, YL, 70, "egon_k", fuell=ROT, bis=beim("egon_k", "kein"))),
    grau(ficon("tabler", "lighter", CX, YL, 70, beim("egon_k", "kein"), fuell=ROT, anim="cut", bis="weit")),
    hart(ficon("tabler", "lighter", CX, YL, 70, "weit", fuell=ROT)),
    pl("Bodo: Anzünden", LBX, YL - 75, "bodo_k", fill=ROT, size=28, anker="m"),
    pfeil_ink(CX, YL + 20, CX, YB - 190, "bodo_k"),
    scheune(CX, YB, 200, "bodo_k"),
    *flammen(CX, YB - 150, 64, "bodo_k", bis=beim("bodo_k", "brennt")),
    *[hart(e) for e in flammen(CX, YB - 150, 64, beim("bodo_k", "Kausal"), bis=beim("egon_k", "brennt"))],
    *[hart(e) for e in flammen(CX, YB - 150, 64, beim("egon_k", "Auch"))],
    pl("Brand", LBX, YB - 110, "bodo_k", fill=ORANGE, size=28, anker="m"),
    pl("weggedacht", LBX, YL - 20, beim("bodo_k", "Denk"), fill=WEISS, size=26, anker="m", bis="egon_k"),
    pl("kein Brand", LBX, YB - 55, beim("bodo_k", "brennt"), fill=WEISS, size=26, anker="m", bis=beim("bodo_k", "Kausal")),
    pl("weggedacht", LBX, YK - 40, beim("egon_k", "Denk"), fill=WEISS, size=26, anker="m", bis="weit"),
    pl("kein Feuerzeug", LBX, YL - 20, beim("egon_k", "kein"), fill=WEISS, size=26, anker="m", bis="weit"),
    pl("nicht so", LBX, YB - 55, beim("egon_k", "brennt"), fill=WEISS, size=26, anker="m", bis=beim("egon_k", "Auch")),
    # sogar der Hersteller
    ficon("tabler", "building-factory-2", CX, YF, 120, beim("weit", "Hersteller"), fuell=BLAU),
    pfeil_ink(CX, YF + 20, CX, YK - 140, beim("weit", "Hersteller")),
    pl("Hersteller", LBX, YF - 75, beim("weit", "Hersteller"), fill=BLAU, size=28, anker="m"),
])

# G Ersatzursache -------------------------------------------------------------------------------------------------------
BOg = ("BO_frech", FX, BR, FR)
folie([("reserve", "A. Kausalität › Ersatzursache?")], [
    *tafel("reserve", "Bodos Einwand"),
    z("Ohne Egon: sonst Streichhölzer?", 110, 190, beim("b2", "Streichhölzer"), "Bold", 36),
    z("Kausal bleibt eine Bedingung auch dann, wenn", 110, 280, "res2", size=34),
    z("sonst ein anderer gehandelt und denselben", 110, 328, beim("res2", "sonst"), size=34),
    z("Erfolg herbeigeführt hätte", 110, 376, beim("res2", "Erfolg"), size=34),
    z("BGH, 5 StR 327/03, Rn. 14 (BGHSt 49, 1)", 110, 432, beim("res2", "Erfolg"), "Bold", 27, farbe=TEXT),
    nein(135, 535, "res3", gr=22), z("Ersatzursachen bleiben außer Betracht", 175, 512, "res3", "Bold", 36),
    ok(135, 605, beim("res3", "Es"), gr=22), z("Es zählt der tatsächliche Ablauf", 175, 582, beim("res3", "Es"), "Bold", 36),
    *fig("BO", FX, BR, FR, [("reserve", "denkt")], bis="b2"),
    *redet("BO_frech", FX, BR, FR, "b2", "res2"),
    peep_voll("BO_ertappt", FX, BR, FR, "res2", anim="cut"),
    name("BO", FX, "reserve", unten=BR),
    blase("sprech", 600, 210, "b2", 1540, 190, inhalt=["Ohne Egon hätte ich", "eben Streichhölzer geholt."], textsize=34,
          figur=BOg, bis="res2"),
    ficon("tabler", "matchstick", 1330, 520, 90, beim("b2", "Streichhölzer"), fuell=GELB),
    kreuz_i(1330, 470, "res3", gr=40),
    pl("außer Betracht", 1360, 560, "res3", fill=WEISS, size=26, anker="m"),
])

# H Unterbrechung? -------------------------------------------------------------------------------------------------------
folie([("dritt", "A. Kausalität › Unterbrechung durch Bodos Tat?")], [
    *tafel("dritt", "Unterbricht Bodos Tat den Zusammenhang?", size=42),
    nein(135, 213, beim("neu", "Nein"), gr=22), z("Nein.", 175, 190, beim("neu", "Nein"), "ExtraBold", 38),
    z("Unterbrochen nur, wenn ein späteres Ereignis", 110, 260, beim("neu", "Unterbrochen"), size=34),
    z("die Fortwirkung der ersten Bedingung beseitigt", 110, 308, beim("neu", "Fortwirkung"), size=34),
    z("und allein eine neue Ursachenreihe eröffnet", 110, 356, beim("neu", "allein"), size=34),
    z("BGH, 3 StR 394/20, Rn. 5; BGHSt 39, 195, 197", 110, 412, beim("neu", "allein"), "Bold", 27, farbe=TEXT),
    ok(135, 505, "knuepft", gr=22), z("Bodo knüpft an das Feuerzeug an", 175, 482, "knuepft", "Bold", 36),
    z("Vorsätzliche Mitwirkung eines Dritten", 110, 565, beim("knuepft", "Dass"), size=34),
    z("ändert an der Kausalität nichts", 110, 613, beim("knuepft", "ändert"), size=34),
    z("BGH, 4 StR 223/15, Rn. 10; BGHSt 39, 195, 197", 110, 669, beim("knuepft", "ändert"), "Bold", 27, farbe=TEXT),
    # rechts: Kiosk → Feuerzeug → Bodo
    ficon("tabler", "building-store", 1340, 300, 110, "dritt", fuell=WEISS),
    pl("Egon", 1340, 330, "dritt", fill=GRUEN, size=26, anker="m"),
    ficon("tabler", "lighter", 1560, 290, 60, "dritt", fuell=ROT),
    ficon("ph", "link", 1450, 280, 70, "knuepft", fuell=None),
    pl("knüpft an", 1450, 120, "knuepft", fill=GELB, size=28, anker="m"),
    ficon("tabler", "flame", 1770, 300, 80, "dritt", fuell=ORANGE),
    *fig("BO", 1640, BR, FR - 30, [("dritt", "denkt"), ("knuepft", "ertappt")]),
    name("BO", 1640, "dritt", unten=BR),
])

# I Nur die erste Hürde ------------------------------------------------------------------------------------------------
PH = "A. Kausalität › nur die erste Hürde"
folie([("huerde", PH), ("zurech", "B. Nächster Schritt › objektive Zurechnung (Lehre)"), ("vors", "B. Nächster Schritt › Vorsatz Egon (-)")], [
    *tafel("huerde", "Ist Egon damit schon strafbar?"),
    ok(135, 213, beim("huerde", "Kausalität"), gr=22), z("Kausalität: nur die erste Hürde", 175, 190, beim("huerde", "Kausalität"), "Bold", 36),
    z("Zurechnung des Brandes:", 110, 290, "zurech", "Bold", 36),
    z("nach der Lehre der nächste Schritt,", 150, 342, beim("zurech", "Lehre"), size=34),
    z("die objektive Zurechnung", 150, 390, beim("zurech", "objektiven"), "Bold", 34),
    pl("eigene Folge", 150, 450, beim("zurech", "eigene"), fill=GELB, size=30),
    nein(135, 583, "vors", gr=22), z("Vorsatz: Egon wusste nichts", 175, 560, "vors", "Bold", 36),
    z("von Bodos Plan", 215, 612, beim("vors", "wusste"), size=34),
    *fig("EG", FX, BR, FR, [("huerde", "sorge"), ("vors", "froh")]),
    name("EG", FX, "huerde", unten=BR),
    ficon("tabler", "stairs-up", FX, 330, 120, beim("huerde", "Hürde"), fuell=GELB),
    pl("erste Hürde", FX, 360, beim("huerde", "Hürde"), fill=WEISS, size=28, anker="m"),
])

# J Abwandlung 1: überholende Kausalität -------------------------------------------------------------------------------
S1X, S1U = 1500, 560
B1 = "B. Abwandlung 1"
folie([("var1", f"{B1} · Kerze im Stroh"), ("ueberh", f"{B1} › überholende Kausalität (Lehre)"),
       ("versuch", f"{B1} › versuchte Brandstiftung, §§ 306, 22, 23 StGB")], [
    *tafel("var1", "Abwandlung 1: Kerze im Stroh"),
    z("Bodo stellt eine brennende Kerze ins Stroh,", 110, 185, "var1", size=34),
    z("sie soll in einer Stunde das Stroh entzünden", 110, 233, beim("var1", "Sie"), size=34),
    z("vorher: Blitz, die Scheune brennt ab", 110, 305, "blitz", "Bold", 36),
    z("Der Blitz eröffnet eine neue Ursachenreihe", 110, 380, "ueberh", size=34),
    z("und überholt die Kerze", 110, 428, beim("ueberh", "überholt"), size=34),
    z("Lehre: überholende Kausalität", 110, 486, beim("ueberh", "Lehre"), "Bold", 34),
    nein(135, 583, "versuch", gr=22), z("Bodos Kerze: für den Brand nicht kausal", 175, 560, "versuch", "Bold", 36),
    fl_block(110, 650, 1040, 150, LILA, beim("versuch", "Ihm"), [("Bodo: nur versuchte Brandstiftung", "ExtraBold", 38, INK),
                                                                ("§§ 306, 22, 23 StGB", "Regular", 34, INK)]),
    scheune(S1X, S1U, 330, "var1"),
    karte(S1X - 175, S1U - 46, 120, 46, "var1", fill=STROH, rund=8, schatten=0, rand=3),
    ficon("tabler", "candle", S1X - 115, S1U - 40, 130, beim("var1", "Kerze"), fuell=GELB),
    pl("Kerze", S1X - 115, S1U + 18, beim("var1", "Kerze"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "clock", 1330, 160, 64, beim("var1", "Stunde"), fuell=WEISS),
    pl("in 1 Stunde", 1330, 178, beim("var1", "Stunde"), fill=WEISS, size=24, anker="m"),
    szene(ficon("ph", "cloud-lightning", S1X + 120, 200, 150, beim("blitz", "Blitz"), fuell=GRAU), "026donner*", 1.0, 0.0),
    *flammen(S1X, S1U - 210, 110, beim("blitz", "brennt")),
    pl("neue Ursachenreihe", 1480, 690, beim("ueberh", "neue"), fill=GELB, size=28, anker="m"),
    *fig("BO", 1790, BR, 400, [("var1", "zuendet"), (beim("blitz", "Blitz"), "schreck"), ("versuch", "ertappt")]),
    name("BO", 1790, "var1", unten=BR),
])

# K Abwandlung 2: alternative Kausalität ------------------------------------------------------------------------------
S2X, S2U, BOX2, SIX2 = 1560, 600, 1340, 1785
C2 = "C. Abwandlung 2"


def scheune2(cue):
    return [scheune(S2X, S2U, 300, cue), karte(S2X - 150, S2U - 40, 300, 40, cue, fill=STROH, rund=8, schatten=0, rand=3)]


folie([("var2", f"{C2} · zwei Feuer"), ("streng", f"{C2} › Formel streng angewandt"), ("alt", f"{C2} › alternative Kausalität")], [
    *tafel("var2", "Abwandlung 2: zwei Feuer"),
    z("Auch Silke legt Feuer, unabhängig von Bodo", 110, 185, beim("var2", "Silke"), size=34),
    z("jedes hätte die Scheune allein zerstört", 110, 233, beim("jedes", "jedes"), size=34),
    z("Streng nach der Formel:", 110, 300, "streng", "Bold", 36),
    nein(170, 372, beim("streng", "Bodos"), gr=20), z("Bodos Feuer weg: brennt trotzdem", 205, 350, beim("streng", "Bodos"), size=34),
    nein(170, 422, beim("streng", "Silke"), gr=20), z("Silkes Feuer weg: genauso", 205, 400, beim("streng", "Silke"), size=34),
    z("dann wäre keiner kausal?", 205, 450, beim("streng", "Dann"), "Bold", 34),
    z("BGH: zwei Schüsse, jeder allein tödlich:", 110, 525, beim("alt", "Bundesgerichtshof"), "Bold", 34),
    ok(170, 597, beim("alt", "beide"), gr=20), z("beide ursächlich", 205, 575, beim("alt", "beide"), "Bold", 34),
    z("BGH, 5 StR 720/92 (BGHSt 39, 195)", 520, 580, beim("alt", "beide"), "Bold", 27, farbe=TEXT),
    fl_block(110, 650, 1040, 80, GELB, "altlehre", [("Lehre: alternative Kausalität", "ExtraBold", 36, INK)]),
    z("Von mehreren Bedingungen, die zwar alternativ,", 110, 750, beim("altlehre", "Von"), size=32),
    z("aber nicht kumulativ hinweggedacht werden", 110, 793, beim("altlehre", "aber"), size=32),
    z("können, ist jede ursächlich", 110, 836, beim("altlehre", "können"), "Bold", 32),
    *scheune2("var2"),
    ficon("tabler", "flame", S2X - 110, S2U - 40, 90, "var2", fuell=GELB),
    ficon("tabler", "flame", S2X + 110, S2U - 40, 90, beim("var2", "anderen"), fuell=GELB),
    *flammen(S2X, S2U - 190, 100, "jedes"),
    *fig("BO", BOX2, BR, 380, [("var2", "zuendet_r"), ("streng", "ruhig_r"), ("alt", "ertappt_r")]),
    name("BO", BOX2, "var2", unten=BR),
    *fig("SI", SIX2, BR, 380, [(beim("var2", "Silke"), "schleicht"), ("alt", "ertappt")]),
    name("SI", SIX2, beim("var2", "Silke"), unten=BR),
    pl("unabhängig", S2X, 260, beim("var2", "unabhängig"), fill=WEISS, size=28, anker="m", bis="jedes"),
])

# L Abwandlung 3: kumulative Kausalität ------------------------------------------------------------------------------
D3 = "D. Abwandlung 3"
folie([("var3", f"{D3} · feuchtes Stroh"), ("kum", f"{D3} › kumulative Kausalität (Lehre)")], [
    *tafel("var3", "Abwandlung 3: feuchtes Stroh"),
    z("Bodo und Silke legen wieder Feuer,", 110, 185, "var3", size=34),
    z("jedes wäre allein im feuchten Stroh erloschen", 110, 233, beim("var3", "jedes"), size=34),
    z("erst zusammen: Brand der Scheune", 110, 300, beim("var3", "Erst"), "Bold", 36),
    z("Lehre: kumulative Kausalität", 110, 390, "kum", "ExtraBold", 38),
    z("einen Beitrag weggedacht: Erfolg entfällt", 110, 455, beim("kum", "Denkt"), size=34),
    ok(135, 535, beim("kum", "Also"), gr=22), z("beide kausal", 175, 512, beim("kum", "Also"), "Bold", 36),
    z("Zurechnung: erst der nächste Prüfungsschritt", 110, 610, "kum2", size=34, farbe=TEXT),
    *scheune2("var3"),
    ficon("tabler", "droplet", S2X - 40, 690, 44, beim("var3", "feuchten"), fuell=BLAU),
    ficon("tabler", "droplet", S2X + 40, 690, 44, beim("var3", "feuchten"), fuell=BLAU, d=0.1),
    ficon("tabler", "flame", S2X - 110, S2U - 40, 60, "var3", fuell=GELB, bis=beim("var3", "Erst")),
    ficon("tabler", "flame", S2X + 110, S2U - 40, 60, "var3", fuell=GELB, bis=beim("var3", "Erst")),
    pl("allein: erloschen", S2X, 260, beim("var3", "erloschen"), fill=WEISS, size=28, anker="m", bis=beim("var3", "Erst")),
    *flammen(S2X, S2U - 190, 100, beim("var3", "zusammen")),
    hart(ficon("tabler", "flame", S2X - 110, S2U - 40, 90, beim("var3", "Erst"), fuell=GELB)),
    hart(ficon("tabler", "flame", S2X + 110, S2U - 40, 90, beim("var3", "Erst"), fuell=GELB)),
    pl("zusammen", S2X, 210, beim("var3", "zusammen"), fill=ORANGE, size=28, anker="m"),
    *fig("BO", BOX2, BR, 380, [("var3", "schleicht_r"), ("kum", "ertappt_r")]),
    name("BO", BOX2, "var3", unten=BR),
    *fig("SI", SIX2, BR, 380, [("var3", "schleicht"), ("kum", "ertappt")]),
    name("SI", SIX2, "var3", unten=BR),
])

# M Ausblick Unterlassen ------------------------------------------------------------------------------------------------
folie([("unterl", "Ausblick › Unterlassen: Quasi-Kausalität")], [
    *tafel("unterl", "Ausblick: Unterlassen"),
    z("keine Handlung, die man wegdenken kann", 110, 190, beim("unterl", "Dort"), "Bold", 36),
    z("deshalb: die gebotene Handlung hinzudenken", 110, 270, "quasi", "Bold", 36),
    z("Quasi-kausal, wenn der Erfolg dann", 110, 360, beim("quasi", "Quasi"), size=36),
    z("mit an Sicherheit grenzender Wahrscheinlichkeit", 110, 410, beim("quasi", "Sicherheit"), "Bold", 36),
    z("ausgeblieben wäre", 110, 460, beim("quasi", "ausgeblieben"), size=36),
    z("BGH, 4 StR 200/21, Rn. 16 f.", 110, 520, beim("quasi", "ausgeblieben"), "Bold", 27, farbe=TEXT),
    ficon("tabler", "hand-off", FX, 440, 140, beim("unterl", "fehlt"), fuell=WEISS, bis="quasi"),
    pl("keine Handlung", FX, 470, beim("unterl", "fehlt"), fill=WEISS, size=30, anker="m", bis="quasi"),
    ficon("tabler", "fire-extinguisher", FX, 560, 170, "quasi", fuell=ROT),
    pl("+ gebotene Handlung", FX, 590, beim("quasi", "gebotene"), fill=GRUEN, size=30, anker="m"),
    pl("Erfolg ausgeblieben?", FX, 680, beim("quasi", "ausgeblieben"), fill=GELB, size=30, anker="m"),
])

# N Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Kausalität knapp oder ausführlich?")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Kausalität offensichtlich? Ein Satz genügt.", 200, 200, beim("tipp", "Ist"), "Bold", 36),
    z("Ausführlich nur in Sonderfällen:", 200, 300, "tipp2", "Bold", 36),
    z("Ersatzursachen,", 240, 355, beim("tipp2", "Ersatzursachen"), size=34),
    z("alternative, kumulative oder überholende Kausalität", 240, 405, beim("tipp2", "alternativer"), size=33),
    z("Nicht schon bei der Kausalität einschränken", 200, 505, "tipp3", "Bold", 36),
    z("Wertungen: erst in den nächsten Prüfungsschritten", 240, 560, beim("tipp3", "Wertungen"), size=33),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema ------------------------------------------------------------------------------------------------------
K1, K2 = 150, 230
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: objektiver Tatbestand des Erfolgsdelikts", 110, 90, "sch", 50),
    z("1. Handlung", K1, 200, "k1", "ExtraBold", 40, rechts=1820),
    z("2. Erfolg", K1, 270, "k2", "ExtraBold", 40, rechts=1820),
    z("3. Kausalität nach der Formel", K1, 340, "k3", "ExtraBold", 40, rechts=1820),
    z("Ersatzursachen bleiben außer Betracht", K2, 405, "k3a", size=36, farbe=TEXT, rechts=1820),
    z("alternative Kausalität: angepasste Formel", K2, 460, "k3b", size=36, farbe=TEXT, rechts=1820),
    z("kumulative Kausalität: alle Beiträge kausal", K2, 515, "k3c", size=36, farbe=TEXT, rechts=1820),
    z("überholte Bedingung: nicht kausal", K2, 570, "k3d", size=36, farbe=TEXT, rechts=1820),
    z("4. objektive Zurechnung (Lehre)", K1, 650, "k4", "ExtraBold", 40, rechts=1820),
])

# P Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Kausal", "a"), (" ist jede Bedingung, die man", 0)], [("nicht wegdenken kann, ohne dass", 0)],
                 [("der konkrete Erfolg entfiele.", 0)]], 750, 300, 44, "merke", {"a": beim("merke", "Kausal")}),
    *markertext([[("Ersatzursachen", "b"), (", die nicht gewirkt", 0)], [("haben, zählen nicht.", 0)]], 750, 540, 44, "m2",
                {"b": beim("m2", "Ersatzursachen")}),
    *markertext([[("Kausal heißt noch nicht ", 0), ("strafbar.", "c")]], 750, 720, 46, "m3", {"c": beim("m3", "strafbar")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m", d=0.2),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        assert "→" not in t_
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
