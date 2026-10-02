"""Folge 035 · Tötungsdelikte Überblick: §§ 211–229 StGB inkl. Körperverletzung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Übungsfall in der Unibibliothek (Whiteboard, nur abstrakte Symbole), B Sachverhalt,
C Landkarte (zwei Säulen), D Totschlag (Wortlautkarte § 212 I), E Mord (drei Gruppen), F Streit Rspr./Lehre (§ 28),
G milder (§§ 213, 216), H fahrlässige Tötung (§ 222), I Körperverletzung (Wortlautkarte § 223 I), J gefährliche KV
(Wortlautkarte § 224 I), K schwere KV (§ 226), L KV mit Todesfolge (§ 227), M § 229 und Strafantrag § 230,
N Prüfreihenfolge, O Klausurtipp (Lexi), P Klausurschema, Q Merksatz (Lexi).
Rechts oben ab Szene D eine kleine Landkarte, die sich Delikt für Delikt füllt (aktuelles Feld gelb).
Gewalt zurückhaltend: keine Verletzungen, kein Blut, keine Waffen im Bild; der Fall nur mit Personen-Symbolen auf der
Treppe. Keine Geräusche (keine passende sichtbare Handlung; Freesound gesperrt)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_035/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
LEER = (246, 244, 240, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -0.4)                       # Hauptfilmbeginn 0,0 s: Grundbild sofort vollständig

_CMAP = set(TTFont(SP + "humaaans/fonts/Nunito[wght].ttf").getBestCmap())


def glyphen(text):
    """Nunito muss jedes Zeichen haben (sonst Kästchen)."""
    fehl = {c for c in text if ord(c) not in _CMAP and not c.isspace()}
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


# --- Eigene Hilfsfunktion (wie Folge 022/026/029): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------
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


NAMEN = {"BR": ("Britta", LILA), "FL": ("Florian", GRUEN)}
BR, FR, FX = 930, 440, 1570                 # Figur rechts unter der kleinen Landkarte


def name(p, cx, cue, unten=BR, size=28, d=0.2, bis=None, anim="pop"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 26, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def person(cx, unten, breite, cue, farbe, bis=None, anim="pop"):
    """Abstraktes Personen-Symbol (Tabler user) für die Fallbeteiligten; keine Figur, keine Verletzung."""
    return ficon("tabler", "user", cx, unten, breite, cue, fuell=farbe, anim=anim, bis=bis)


# --- Kleine Landkarte rechts oben: füllt sich Delikt für Delikt --------------------------------------------------------
MX0, MY0, MW = 1268, 58, 604
SPALTE = {"L": (MX0 + 182, 200), "K": (MX0 + 392, 200)}         # x links, Breite
ZEILEN = ["hoch", "grund", "runter", "folge", "fahrl"]
ZLABEL = {"hoch": "schärfer", "grund": "Grundtatbestand", "runter": "milder", "folge": "schwere Folge", "fahrl": "fahrlässig"}
ZY = {k: MY0 + 52 + i * 54 for i, k in enumerate(ZEILEN)}
# (Spalte, Zeile, Text, Cue des gesprochenen Paragrafen)
FUELLUNG = [("L", "grund", "§ 212", ("p212", "Paragraf")), ("L", "hoch", "§ 211", ("p211", "Paragraf")),
            ("L", "runter", "§ 213", ("p213", "Paragraf")), ("L", "runter", "§§ 213, 216", ("p216", "Paragraf")),
            ("L", "fahrl", "§ 222", ("p222", "Paragraf")), ("K", "grund", "§ 223", ("p223", "Paragraf")),
            ("K", "hoch", "§ 224", ("p224", "Paragraf")), ("K", "folge", "§ 226", ("p226", "Paragraf")),
            ("K", "folge", "§§ 226, 227", ("k227", "Paragraf")), ("K", "fahrl", "§ 229", ("p229", "Paragraf"))]


def _zelle(sp, zl, text, cue, fill, bis=None, anim="fade"):
    x, w = SPALTE[sp]
    els = [bis_(karte(x, ZY[zl], w, 44, cue, fill=fill, rund=10, schatten=0, rand=3, anim=anim), bis)]
    if text:
        f = F("Bold", 24)
        tw = f.getlength(text)
        assert tw <= w - 12, f"Landkarte: {text} zu breit"
        els.append(z(text, x + (w - tw) / 2, ZY[zl] + 6, cue, "Bold", 24, rechts=x + w, bis=bis, anim=anim))
    return els


def minikarte(start, ende_folie=None):
    """Kleine Landkarte ab Folienbeginn 'start': bereits behandelte Felder weiß, die in dieser Folie gesprochenen Felder
    erscheinen beim Paragrafen und bleiben gelb markiert."""
    t0 = bausteine._t(start)
    els = [hart(karte(MX0, MY0, MW, 330, start, fill=WEISS, rund=18, schatten=6, rand=4, anim="cut")),
           hart(z("Tötung", SPALTE["L"][0] + 100 - F("Bold", 22).getlength("Tötung") / 2, MY0 + 14, start, "Bold", 22, rechts=1862, anim="cut")),
           hart(z("Körperverletzung", SPALTE["K"][0] + 100 - F("Bold", 22).getlength("Körperverletzung") / 2, MY0 + 14, start, "Bold", 22, rechts=1862, anim="cut"))]
    for zl in ZEILEN:
        els.append(hart(z(ZLABEL[zl], MX0 + 14, ZY[zl] + 9, start, "Regular", 21, farbe=TEXT, rechts=MX0 + 180, anim="cut")))
        for sp in "LK":
            els += [hart(e) for e in _zelle(sp, zl, "", start, LEER, anim="cut")]
    # Endstand jeder Zelle vor dieser Folie
    vorher = {}
    for sp, zl, text, c in FUELLUNG:
        if bausteine._t(beim(*c)) < t0 - 0.01:
            vorher[(sp, zl)] = text
    for (sp, zl), text in vorher.items():
        els += [hart(e) for e in _zelle(sp, zl, text, start, WEISS, anim="cut")]
    # in dieser Folie neu
    neu = [(sp, zl, text, beim(*c)) for sp, zl, text, c in FUELLUNG
           if t0 - 0.01 <= bausteine._t(beim(*c)) and (ende_folie is None or bausteine._t(beim(*c)) < bausteine._t(ende_folie))]
    for i, (sp, zl, text, c) in enumerate(neu):
        spaeter = next((c2 for sp2, zl2, _, c2 in neu[i + 1:] if (sp2, zl2) == (sp, zl)), None)
        els += _zelle(sp, zl, text, c, GELB, bis=spaeter)
    return els


# A Fall: Lerngruppe in der Unibibliothek ------------------------------------------------------------------------------
FLX, BRX, FH = 1420, 1735, 450
FLb = ("FL_redet_r", FLX, BR, FH)
BRb = ("BR_redet", BRX, BR, FH)
ST = ficon("tabler", "stairs", 520, 700, 420, NULL, fuell=None)          # Treppe auf dem Whiteboard (Geometrie)
SX0, SY0, SX1, SY1 = ST.x, ST.y, ST.x + ST.sprite.width, ST.y + ST.sprite.height
LAND = SY0 + 6                                                               # oberer Treppenabsatz
folie([(NULL, "Fall · Der Übungsfall"), ("frage", "Fall · Die Frage")], [
    hart(linienzug([(1240, BR + 2), (1880, BR + 2)], NULL, breite=6, farbe=INK)),
    hart(karte(60, 60, 1140, 760, NULL, fill=WEISS, rund=18, schatten=10, rand=5, anim="cut")),     # Whiteboard
    hart(karte(380, 838, 500, 22, NULL, fill=GRAU, rund=8, schatten=0, rand=4, anim="cut")),       # Stiftablage
    hart(ficon("tabler", "books", 1815, 200, 100, NULL, fuell=BLAU, nebenfarbe=GELB, anim="cut")),
    hart(ficon("tabler", "lamp", 1665, 200, 90, NULL, fuell=GELB, anim="cut")),
    pl("Dienstagabend", 1290, 64, NULL, fill=GELB, size=34, anim="cut"),
    pl("Unibibliothek", 1290, 140, beim("fall", "Unibibliothek"), fill=WEISS, size=30),
    # Whiteboard: Übungsfall nur mit Symbolen
    titel("Übungsfall", 110, 100, "fritz", 46),
    pl("Treppenhaus", 110, 190, beim("fritz", "Treppenhaus"), fill=WEISS, size=28),
    bis_(ficon("tabler", "stairs", 520, 700, 420, beim("fritz", "Treppenhaus")), None),
    hart(linienzug([(SX1 - 8, LAND), (1120, LAND)], beim("fritz", "Treppenhaus"), breite=8, farbe=INK)),
    person(860, LAND - 6, 110, beim("fritz", "Fritz"), BLAU),
    pl("Fritz", 860, LAND + 22, beim("fritz", "Fritz"), fill=BLAU, size=28, anker="m"),
    person(1030, LAND - 6, 110, beim("fritz", "Henning"), GRUEN, bis="sturz"),
    pl("Henning", 1030, LAND + 22, beim("fritz", "Henning"), fill=GRUEN, size=28, anker="m", bis="sturz"),
    ficon("ph", "bicycle", 945, LAND - 150, 110, beim("fritz", "Fahrrad"), fuell=GELB, bis="stoss"),
    bis_(pfeil_ink(905, LAND - 70, 975, LAND - 70, "stoss"), beim("sturz", "stürzt")),
    pl("stößt", 940, LAND - 175, "stoss", fill=WEISS, size=28, anker="m", bis="frage"),
    pfeil_ink(SX1 - 40, LAND + 70, SX0 + 70, SY1 - 120, beim("sturz", "stürzt")),
    hart(person(SX0 - 30, SY1 - 4, 110, beim("sturz", "stürzt"), GRUEN)),
    pl("Henning", SX0 - 30, SY1 + 24, beim("sturz", "stürzt"), fill=GRUEN, size=28, anker="m"),
    pl("stürzt", 620, LAND + 40, beim("sturz", "stürzt"), fill=WEISS, size=28, anker="m", bis="frage"),
    # Frage
    pl("Welches Delikt passt?", 1150, 555, "frage", fill=PINK, size=34, anker="r"),
    pl("Welche Folge?", 1150, 640, beim("frage2", "Folge"), fill=WEISS, size=30, anker="r"),
    pl("Was wollte Fritz?", 1150, 715, beim("frage2", "wollte"), fill=WEISS, size=30, anker="r"),
    # Florian und Britta
    *fig("FL", FLX, BR, FH, [("florian", "ruhig")], bis="f1"),
    *redet("FL_redet_r", FLX, BR, FH, "f1", "b1"),
    *fig("FL", FLX, BR, FH, [("b1", "staunt_r"), ("frage", "denkt")], erst="cut"),
    name("FL", FLX, "florian"),
    *fig("BR", BRX, BR, FH, [("britta", "ruhig"), ("f1", "skeptisch")], bis="b1"),
    *redet("BR_redet", BRX, BR, FH, "b1", "frage"),
    *fig("BR", BRX, BR, FH, [("frage", "denkt")], erst="cut"),
    name("BR", BRX, "britta"),
    blase("sprech", 520, 170, "f1", 1560, 300, inhalt=["Klare Sache:", "Körperverletzung."], textsize=36, figur=FLb, bis="b1"),
    blase("sprech", 520, 170, "b1", 1600, 300, inhalt=["Und wenn Henning", "dabei stirbt?"], textsize=36, figur=BRb, bis="frage"),
])

# B Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Im Treppenhaus streiten Fritz und sein Nachbar Henning um ein Fahrrad. Fritz stößt Henning, Henning stürzt die "
    "Treppe hinunter. Grundfall: Fritz will Henning verletzen.",
    "Variante 1: Fritz will Henning töten; Henning stirbt. Variante 2: Fritz rempelt Henning beim Tragen des Fahrrads nur "
    "aus Unachtsamkeit an. Variante 3: Henning erleidet Prellungen. Variante 4: Ein Freund von Fritz versperrt Henning "
    "bewusst den Weg. Variante 5: Henning verliert das Sehvermögen auf einem Auge. Variante 6: Henning stirbt an den "
    "Folgen des Sturzes.",
], "Welche Delikte kommen in Betracht?")

# C Landkarte -----------------------------------------------------------------------------------------------------------
GX0, GW = 110, 1040
GL, GC = 300, 355                           # Breite Zeilenbeschriftung, Spaltenbreite
GY = {k: 300 + i * 105 for i, k in enumerate(ZEILEN)}
folie([("karte", "Überblick · Landkarte §§ 211–229 StGB")], [
    *tafel("karte", "Delikte gegen Leib und Leben"),
    ficon("tabler", "heart", GX0 + GL + GC / 2, 222, 50, "leben", fuell=ROT),
    z("Tötung", GX0 + GL + GC / 2 - F("ExtraBold", 36).getlength("Tötung") / 2 + 0, 228, "leben", "ExtraBold", 36),
    ficon("tabler", "bandage", GX0 + GL + GC + 20 + GC / 2, 222, 50, "koerper", fuell=GELB),
    z("Körperverletzung", GX0 + GL + GC + 20 + GC / 2 - F("ExtraBold", 36).getlength("Körperverletzung") / 2, 228,
      "koerper", "ExtraBold", 36),
    *[e for zl in ZEILEN for e in (
        [z(ZLABEL[zl], GX0, GY[zl] + 24, zl, "Bold" if zl == "grund" else "Regular", 32)] +
        [karte(GX0 + GL + j * (GC + 20), GY[zl], GC, 84, zl, fill=(GELB if zl == "grund" else LEER), rund=14, schatten=0, rand=3)
         for j in range(2)])],
    *fig("FL", FLX, BR, FH, [("karte", "ruhig"), ("folge", "denkt")]),
    name("FL", FLX, "karte", d=0.0),
    *fig("BR", BRX, BR, FH, [("karte", "denkt"), ("hoch", "staunt"), ("fahrl", "froh")]),
    name("BR", BRX, "karte", d=0.0),
    pl("zwei Säulen", 1580, 300, beim("karte", "zwei"), fill=GELB, size=32, anker="m"),
])

# D Totschlag, § 212 ----------------------------------------------------------------------------------------------------
PA = "A. Tötungsdelikte"
P212 = ["„Wer einen Menschen tötet, ohne Mörder zu sein, wird als Totschläger", "mit Freiheitsstrafe nicht unter fünf Jahren bestraft.“"]
wl212, y212 = wortlaut(100, 180, 1060, P212, "§ 212 Abs. 1 StGB", "p212w",
                       marken=[(0, "einen Menschen tötet", beim("p212w", "Menschen")),
                               (1, "nicht unter fünf Jahren", beim("p212w", "nicht"))])
folie([("p212", f"{PA} › Grundtatbestand: Totschlag, § 212 StGB")], [
    *tafel("p212", "Totschlag, § 212 StGB"),
    pl("Grundtatbestand der Tötungsdelikte", 110, 168 - 0, beim("p212", "Grundtatbestand"), fill=GELB, size=30, bis="p212w"),
    *wl212,
    z("Variante 1: Fritz will Henning töten, Henning stirbt", 110, y212 + 40, "v1", size=36),
    fl_block(110, y212 + 120, 1040, 90, GELB, beim("p212s", "Tatbestand"), [("Tatbestand des Totschlags erfüllt", "ExtraBold", 38, INK)]),
    ok(1110, y212 + 165, beim("p212s", "erfüllt"), gr=22),
    *minikarte("p212", "p211"),
    *fig("BR", FX, BR, FR, [("p212", "ruhig"), ("v1", "sorge"), ("p212s", "denkt")]),
    name("BR", FX, "p212", d=0.0),
])

# E Mord, § 211 ---------------------------------------------------------------------------------------------------------
folie([("p211", f"{PA} › Mord, § 211 StGB")], [
    *tafel("p211", "Mord, § 211 StGB"),
    z("zusätzlich: ein Mordmerkmal", 110, 185, beim("p211", "zusätzlich"), "Bold", 38),
    pl("drei Gruppen", 110, 255, "gruppen", fill=GELB, size=32),
    fl_block(110, 335, 1040, 64, PINK, "g1", [("1. Gruppe: Beweggründe", "ExtraBold", 34, INK)]),
    z("Mordlust, Habgier, sonst niedrige Beweggründe", 150, 410, beim("g1", "Mordlust"), size=34),
    fl_block(110, 480, 1040, 64, BLAU, "g2", [("2. Gruppe: Art der Tat", "ExtraBold", 34, INK)]),
    z("heimtückisch, grausam, gemeingefährliche Mittel", 150, 555, beim("g2", "heimtückisch"), size=34),
    fl_block(110, 625, 1040, 64, LILA, "g3", [("3. Gruppe: Zweck", "ExtraBold", 34, INK)]),
    z("andere Straftat ermöglichen oder verdecken", 150, 700, beim("g3", "eine"), size=34),
    z("Strafe: lebenslange Freiheitsstrafe (§ 211 Abs. 1)", 110, 790, "lebensl", "Bold", 34),
    *minikarte("p211", "streit"),
    *fig("FL", FX, BR, FR, [("p211", "ruhig"), ("g2", "denkt"), ("lebensl", "staunt")]),
    name("FL", FX, "p211", d=0.0),
])

# F Streit Rechtsprechung / Lehre ---------------------------------------------------------------------------------------
FLb2 = ("FL_fragt", 1700, BR, 470)
folie([("streit", f"{PA} › Mord und Totschlag: Streit"), ("p28", f"{PA} › Mord und Totschlag › Teilnehmer, § 28 StGB")], [
    *tafel("streit", "Wie hängen Mord und Totschlag zusammen?", size=42),
    fl_block(110, 180, 505, 64, LILA, "lehre", [("Lehre", "ExtraBold", 34, INK)]),
    z("§ 212: Grundtatbestand", 130, 260, beim("lehre", "Totschlag"), size=32, rechts=615),
    z("§ 211: Qualifikation", 130, 305, beim("lehre", "Qualifikation"), size=32, rechts=615),
    fl_block(645, 180, 505, 64, BLAU, "rspr", [("Rechtsprechung (BGH)", "ExtraBold", 34, INK)]),
    z("zwei selbständige", 665, 260, beim("rspr", "selbständige"), size=32),
    z("Tatbestände", 665, 305, beim("rspr", "selbständige"), size=32),
    z("BGH, 5 StR 341/05, Rn. 45 f.", 110, 360, beim("rspr", "selbständige"), "Bold", 27, farbe=TEXT),
    z("Bedeutung: Teilnehmer, § 28 StGB", 110, 435, "p28", "Bold", 36),
    z("Gehilfe kennt niedrige Beweggründe, teilt sie nicht:", 110, 495, "p28a", size=33),
    z("BGH: Beihilfe zum Mord, gemildert (§ 28 Abs. 1)", 150, 548, beim("p28a", "Beihilfe"), size=33),
    z("Lehre: Beihilfe zum Totschlag (§ 28 Abs. 2)", 150, 601, "p28b", size=33),
    fl_block(110, 680, 1040, 64, GELB, "offen", [("5. Strafsenat 2006: Einwände gewichtig, Frage offen", "ExtraBold", 32, INK)]),
    z("BGH, Beschl. v. 10.1.2006 – 5 StR 341/05, Rn. 44–48", 110, 765, beim("offen", "gewichtig"), "Bold", 27, farbe=TEXT),
    *fig("FL", 1700, BR, 470, [("streit", "denkt")], bis="f2"),
    *redet("FL_fragt", 1700, BR, 470, "f2", "p28"),
    *fig("FL", 1700, BR, 470, [("p28", "ruhig"), ("offen", "denkt")], erst="cut"),
    name("FL", 1700, "streit", d=0.0),
    blase("sprech", 560, 170, "f2", 1540, 300, inhalt=["Und wozu brauche", "ich den Streit?"], textsize=36, figur=FLb2, bis="p28"),
    ficon("tabler", "scale", 1450, 470, 150, "streit", fuell=GELB, bis="f2"),
    ficon("tabler", "users", 1440, 470, 140, "p28", fuell=GELB),
])

# G Milder: §§ 213, 216 -------------------------------------------------------------------------------------------------
folie([("milder", f"{PA} › milder: minder schwerer Fall, § 213 StGB"),
       ("p216", f"{PA} › milder: Tötung auf Verlangen, § 216 StGB")], [
    *tafel("milder", "Milder: §§ 213, 216 StGB"),
    z("§ 213: minder schwerer Fall des Totschlags", 110, 190, beim("p213", "Paragraf"), "Bold", 36),
    z("Strafe: ein bis zehn Jahre", 150, 245, beim("p213", "ein"), size=34),
    z("z. B. schwere Beleidigung durch das Opfer,", 150, 300, "zorn", size=34),
    z("ohne eigene Schuld, auf der Stelle zur Tat hingerissen", 150, 350, beim("zorn", "hingerissen"), size=34),
    z("§ 216: Tötung auf Verlangen", 110, 450, "p216", "Bold", 36),
    z("„ausdrückliches und ernstliches Verlangen“", 150, 505, beim("p216", "ausdrückliches"), size=34),
    z("des Getöteten", 150, 555, beim("p216", "Getöteten"), size=34),
    z("Strafe: sechs Monate bis fünf Jahre", 150, 610, "s216", size=34),
    *minikarte("milder", "p222"),
    *fig("BR", FX, BR, FR, [("milder", "ruhig"), ("zorn", "sorge"), ("p216", "denkt")]),
    name("BR", FX, "milder", d=0.0),
])

# H Fahrlässige Tötung, § 222 -------------------------------------------------------------------------------------------
TX, TY = 1450, 840                          # kleine Treppe rechts unten (Fall-Symbole)


def treppe_klein(cue, bis=None):
    st = ficon("tabler", "stairs", TX, TY, 300, cue, bis=bis)
    land = st.y + 5
    return [st, hart(bis_(linienzug([(st.x + st.sprite.width - 6, land), (1860, land)], cue, breite=6, farbe=INK), bis))], st, land


tk, st_h, land_h = treppe_klein("p222")
folie([("p222", f"{PA} › Fahrlässigkeit: fahrlässige Tötung, § 222 StGB")], [
    *tafel("p222", "Fahrlässige Tötung, § 222 StGB"),
    z("ganz unten: die fahrlässige Tötung", 110, 190, beim("p222", "Ganz"), size=36),
    z("Variante 2: Fritz rempelt Henning beim Tragen", 110, 280, "v2", "Bold", 36),
    z("des Fahrrads an, nur aus Unachtsamkeit", 110, 332, beim("v2", "Fahrrads"), "Bold", 36),
    z("Henning stirbt:", 110, 430, "p222s", size=36),
    fl_block(110, 490, 1040, 90, GELB, beim("p222s", "drohen"), [("bis zu fünf Jahre oder Geldstrafe", "ExtraBold", 38, INK)]),
    *minikarte("p222", "p223"),
    *tk,
    person(st_h.x + st_h.sprite.width + 40, land_h - 4, 70, "v2", BLAU),
    ficon("ph", "bicycle", st_h.x + st_h.sprite.width + 125, land_h - 4, 90, beim("v2", "Fahrrads"), fuell=GELB),
    person(st_h.x + st_h.sprite.width + 210, land_h - 4, 70, "v2", GRUEN),
    pl("Unachtsamkeit", 1570, 425, beim("v2", "Unachtsamkeit"), fill=WEISS, size=28, anker="m"),
])

# I Körperverletzung, § 223 ---------------------------------------------------------------------------------------------
PB = "B. Körperverletzungsdelikte"
P223 = ["„Wer eine andere Person körperlich mißhandelt oder an der Gesundheit",
        "schädigt, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe",
        "bestraft.“"]
wl223, y223 = wortlaut(100, 180, 1060, P223, "§ 223 Abs. 1 StGB", "p223w",
                       marken=[(0, "körperlich mißhandelt", beim("p223w", "körperlich")),
                               (0, "an der Gesundheit", beim("p223w", "Gesundheit")), (1, "schädigt", beim("p223w", "schädigt"))])
folie([("p223", f"{PB} › Grundtatbestand: Körperverletzung, § 223 StGB")], [
    *tafel("p223", "Körperverletzung, § 223 StGB"),
    *wl223,
    z("Variante 3: Henning erleidet Prellungen", 110, y223 + 35, "v3", "Bold", 36),
    z("nicht jeder Stoß: Wohlbefinden nicht nur", 110, y223 + 105, "nicht", size=34),
    z("unerheblich beeinträchtigt", 150, y223 + 155, beim("nicht", "unerheblich"), size=34),
    z("BGH, 3 StR 354/16, Rn. 4", 110, y223 + 207, beim("nicht", "unerheblich"), "Bold", 27, farbe=TEXT),
    ok(135, y223 + 283, "prell", gr=22), z("Prellungen: Misshandlung", 175, y223 + 260, "prell", "Bold", 36),
    ok(135, y223 + 338, beim("prell", "Gesundheit"), gr=22),
    z("und Gesundheitsschädigung", 175, y223 + 315, beim("prell", "Gesundheit"), "Bold", 36),
    z("BGH, 4 StR 168/13, Rn. 13", 110, y223 + 370, beim("prell", "Gesundheit"), "Bold", 27, farbe=TEXT),
    *minikarte("p223", "p224"),
    *fig("BR", FX, BR, FR, [("p223", "ruhig"), ("nicht", "skeptisch"), ("prell", "denkt")]),
    name("BR", FX, "p223", d=0.0),
])

# J Gefährliche Körperverletzung, § 224 ---------------------------------------------------------------------------------
P224 = ["„Wer die Körperverletzung",
        "1. durch Beibringung von Gift oder anderen gesundheitsschädlichen Stoffen,",
        "2. mittels einer Waffe oder eines anderen gefährlichen Werkzeugs,",
        "3. mittels eines hinterlistigen Überfalls,",
        "4. mit einem anderen Beteiligten gemeinschaftlich oder",
        "5. mittels einer das Leben gefährdenden Behandlung",
        "begeht, wird mit Freiheitsstrafe von sechs Monaten bis zu zehn Jahren,",
        "in minder schweren Fällen mit Freiheitsstrafe von drei Monaten bis zu",
        "fünf Jahren bestraft.“"]
wl224, y224 = wortlaut(90, 160, 1090, P224, "§ 224 Abs. 1 StGB", beim("p224", "gefährliche"), size=28,
                       marken=[(1, "Gift", "n1"), (2, "Waffe", beim("n2", "Waffe")), (3, "hinterlistigen Überfalls", beim("n3", "hinterlistiger")),
                               (4, "mit einem anderen Beteiligten gemeinschaftlich", beim("n4", "gemeinschaftliche")),
                               (5, "das Leben gefährdenden Behandlung", beim("n5", "Leben"))])
tj, st_j, land_j = treppe_klein("v4")
folie([("p224", f"{PB} › gefährliche Körperverletzung, § 224 StGB"),
       ("nr4", f"{PB} › gefährliche Körperverletzung › § 224 Abs. 1 Nr. 4: gemeinschaftlich")], [
    karte(60, 60, 1140, 840, "p224"), titel("Gefährliche Körperverletzung, § 224 StGB", 110, 92, "p224", 42),
    *wl224,
    z("Variante 4: Freund versperrt bewusst den Weg", 110, y224 + 22, "v4", "Bold", 34),
    ok(135, y224 + 98, "nr4", gr=22), z("Nr. 4: zweiter Beteiligter verstärkt am Tatort", 175, y224 + 75, "nr4", "Bold", 34),
    z("bewusst die Wirkung · BGHSt 47, 383, Rn. 11", 175, y224 + 122, beim("nr4", "bewusst"), size=30, farbe=TEXT),
    z("Nr. 5: gesondert prüfen", 110, y224 + 170, "nr5", "Bold", 34),
    *minikarte("p224", "p226"),
    *tj,
    person(st_j.x + st_j.sprite.width + 40, land_j - 4, 70, "v4", BLAU),
    person(st_j.x + st_j.sprite.width + 125, land_j - 4, 70, "v4", GRUEN),
    person(st_j.x + st_j.sprite.width + 210, land_j - 4, 70, beim("v4", "Freund"), GRAU),
    pl("Freund", st_j.x + st_j.sprite.width + 210, land_j + 22, beim("v4", "Freund"), fill=GRAU, size=24, anker="m"),
    pl("fünf Begehungsweisen", 1570, 425, "nall", fill=GELB, size=30, anker="m", bis="v4"),
    pl("versperrt den Weg", 1570, 425, beim("v4", "versperrt"), fill=WEISS, size=28, anker="m"),
    pl("Nr. 4", 1400, 500, "nr4", fill=GELB, size=30, anker="m"),
])

# K Schwere Körperverletzung, § 226 -------------------------------------------------------------------------------------
folie([("p226", f"{PB} › schwere Körperverletzung, § 226 StGB")], [
    *tafel("p226", "Schwere Körperverletzung, § 226 StGB", size=44),
    z("knüpft an schwere Dauerfolgen an", 110, 190, beim("p226", "knüpft"), "Bold", 36),
    z("z. B. Verlust eines wichtigen Glieds", 150, 250, "folgen", size=34),
    z("Variante 5: Sehvermögen auf einem Auge verloren", 110, 340, "v5", "Bold", 36),
    z("§ 18: für die Folge genügt wenigstens Fahrlässigkeit", 110, 440, "p18", size=34),
    fl_block(110, 520, 1040, 90, GELB, "abs2", [("Abs. 2: absichtlich oder wissentlich", "ExtraBold", 36, INK)]),
    z("mindestens drei Jahre", 150, 630, beim("abs2", "mindestens"), "Bold", 34),
    *minikarte("p226", "p227"),
    ficon("tabler", "eye-off", 1400, 640, 120, "v5", fuell=WEISS),
    pl("Dauerfolge", 1400, 670, "v5", fill=WEISS, size=26, anker="m"),
    *fig("FL", 1700, BR, FR, [("p226", "ruhig"), ("v5", "muede"), ("abs2", "denkt")]),
    name("FL", 1700, "p226", d=0.0),
])

# L Körperverletzung mit Todesfolge, § 227 ------------------------------------------------------------------------------
tl, st_l, land_l = treppe_klein("p227")
folie([("p227", f"{PB} › Körperverletzung mit Todesfolge, § 227 StGB")], [
    *tafel("p227", "Körperverletzung mit Todesfolge, § 227 StGB", size=40),
    z("Fritz wollte nur verletzen, Henning stirbt", 110, 185, "p227", "Bold", 36),
    pl("Variante 6", 110, 245, "v6", fill=GELB, size=30),
    fl_block(110, 320, 1040, 80, WEISS, "k227", [("§ 227: Körperverletzung mit Todesfolge", "ExtraBold", 36, INK)]),
    nein(135, 450, "gefahr", gr=22), z("bloßer Kausalzusammenhang genügt nicht", 175, 427, "gefahr", size=34),
    ok(135, 505, beim("gefahr", "Im"), gr=22), z("im Tod: spezifische Gefahr der Körperverletzung", 175, 482, beim("gefahr", "Im"), "Bold", 34),
    z("BGH, 5 StR 435/07, Rn. 8", 175, 535, beim("gefahr", "niederschlagen"), "Bold", 27, farbe=TEXT),
    z("Stoß auf der Treppe: liegt nahe", 110, 610, "treppe", size=34),
    z("Tod: Fahrlässigkeit genügt (§ 18)", 110, 690, "t227", "Bold", 34),
    z("Strafe: mindestens drei Jahre", 110, 745, beim("t227", "Strafe"), "Bold", 34),
    *minikarte("p227", "p229"),
    *tl,
    person(st_l.x + st_l.sprite.width + 60, land_l - 4, 70, "p227", BLAU),
    person(st_l.x - 10, TY - 4, 70, "p227", GRUEN),
    pfeil_ink(st_l.x + st_l.sprite.width - 30, land_l + 40, st_l.x + 40, TY - 90, "p227"),
    pl("Tod", st_l.x - 10, TY + 22, beim("p227", "stirbt"), fill=GRAU, size=24, anker="m"),
])

# M Fahrlässige Körperverletzung, § 229; Strafantrag, § 230 -------------------------------------------------------------
folie([("p229", f"{PB} › fahrlässige Körperverletzung, § 229 StGB"), ("p230", f"{PB} › Strafantrag, § 230 StGB")], [
    *tafel("p229", "Fahrlässige Körperverletzung, § 229 StGB", size=42),
    z("daneben: die fahrlässige Körperverletzung", 110, 190, "p229", size=36),
    z("Variante 2: Henning überlebt verletzt", 110, 250, "v2b", "Bold", 36),
    fl_block(110, 360, 1040, 80, GELB, "p230", [("§ 230: nur auf Antrag", "ExtraBold", 38, INK)]),
    z("bei einfacher (§ 223) und fahrlässiger (§ 229)", 150, 465, beim("p230", "Einfache"), size=34),
    z("Körperverletzung", 150, 515, beim("p230", "Einfache"), size=34),
    z("außer: besonderes öffentliches Interesse,", 110, 600, "oeff", "Bold", 34),
    z("bejaht von der Strafverfolgungsbehörde", 150, 650, beim("oeff", "bejaht"), size=34),
    *minikarte("p229", "reihe"),
    ficon("tabler", "signature", 1400, 640, 120, beim("p230", "Antrag"), fuell=GELB),
    pl("Antrag", 1400, 670, beim("p230", "Antrag"), fill=GELB, size=26, anker="m"),
    *fig("BR", 1700, BR, FR, [("p229", "ruhig"), ("p230", "staunt"), ("oeff", "denkt")]),
    name("BR", 1700, "p229", d=0.0),
])

# N Prüfreihenfolge -----------------------------------------------------------------------------------------------------
folie([("reihe", "Prüfreihenfolge · Klausurkonvention")], [
    *tafel("reihe", "Womit fängst du an?"),
    z("Faustregel: das schwerste Delikt zuerst", 110, 195, beim("r1", "Faustregel"), "Bold", 38),
    z("Todesfall: zuerst die vorsätzliche Tötung", 110, 265, beim("r1", "Todesfall"), size=36),
    z("1. Totschlag und Mord", 150, 345, "r2", "Bold", 36),
    z("2. ohne Tötungsvorsatz: Körperverletzungsdelikte", 150, 415, "r3", "Bold", 36),
    z("bis zur Todesfolge, § 227", 190, 467, beim("r3", "Todesfolge"), size=34),
    z("3. Fahrlässigkeit zuletzt", 150, 545, "r4", "Bold", 36),
    pl("Klausurkonvention, kein Gesetz", 110, 640, "konv", fill=GELB, size=34),
    *fig("FL", FLX, BR, FH, [("reihe", "denkt"), ("r2", "froh")]),
    name("FL", FLX, "reihe", d=0.0),
    *fig("BR", BRX, BR, FH, [("reihe", "skeptisch"), ("r1", "denkt"), ("konv", "froh")]),
    name("BR", BRX, "reihe", d=0.0),
    ficon("tabler", "list-numbers", 1580, 330, 130, beim("r1", "Faustregel"), fuell=GELB),
])

# O Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Mordmerkmale im Aufbau")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Mordmerkmale im Aufbau richtig einordnen", 200, 200, beim("tipp", "Ordne"), "Bold", 36),
    fl_block(110, 300, 1040, 64, BLAU, "tipp2", [("2. Gruppe: tatbezogen", "ExtraBold", 34, INK)]),
    z("objektiver Tatbestand", 150, 380, beim("tipp2", "objektiven"), "Bold", 34),
    z("der Vorsatz muss sie umfassen", 150, 432, beim("tipp2", "Vorsatz"), size=34),
    fl_block(110, 520, 1040, 64, PINK, "tipp3", [("1. und 3. Gruppe: täterbezogen", "ExtraBold", 34, INK)]),
    z("subjektiver Tatbestand", 150, 600, beim("tipp3", "subjektiven"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.0),
])

# P Klausurschema -------------------------------------------------------------------------------------------------------
K1, K2 = 130, 190
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Delikte gegen Leib und Leben", 110, 90, "sch", 50),
    z("I. Vorsätzliche Tötung: Totschlag, § 212, und Mord, § 211", K1, 200, "k1", "ExtraBold", 40, rechts=1820),
    z("dazu § 213 und § 216", K2, 265, "k1b", size=36, farbe=TEXT, rechts=1820),
    z("II. Körperverletzung, § 223", K1, 350, "k2", "ExtraBold", 40, rechts=1820),
    z("1. gefährliche Körperverletzung, § 224", K2, 415, "k2b", "Bold", 36, rechts=1820),
    z("2. schwere Körperverletzung, § 226, und mit Todesfolge, § 227", K2, 470, "k2c", "Bold", 36, rechts=1820),
    z("III. Fahrlässigkeitsdelikte: § 222, § 229", K1, 560, "k3", "ExtraBold", 40, rechts=1820),
    z("Am Ende: Strafantrag, § 230", K1, 640, "k4", "ExtraBold", 40, rechts=1820),
])

# Q Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 170, "merke", 84, anker="m"),
    *markertext([[("Grundtatbestände", "a"), (": Totschlag", 0)], [("und Körperverletzung.", 0)]], 750, 300, 44, "merke",
                {"a": beim("merke", "Grundtatbestände")}),
    *markertext([[("Mordmerkmale", "b"), (" und § 224 Nr. 1–5:", 0)], [("schärfere Strafe.", 0)]], 750, 470, 44, "m2",
                {"b": beim("m2", "Mordmerkmale")}),
    *markertext([[("Schwere Folgen: wenigstens", 0)], [("Fahrlässigkeit", "c"), (" genügt, § 18.", 0)]], 750, 640, 44, "m3",
                {"c": beim("m3", "Fahrlässigkeit")}),
    *redet("LX_erklaert", 1680, 990, 700, "merke", lexi_bis_ende("merke")),
    pl("Lexi", 1680, 1000, "merke", fill=GELB, size=28, anker="m", d=0.0),
])

# Zeichenprüfung für alle übrigen Texte (Pfade, Blöcke, Titel, Blasen, Sachverhalt)
for f_ in FOLIEN:
    for _, t_ in f_["pfade"]:
        glyphen(t_)
    for e_ in f_["els"]:
        n_ = e_.name or ""
        if n_.startswith(("block:", "titel:", "pille:", "blase:")):
            glyphen(n_.split(":", 1)[1].replace("(", "").replace(")", "").replace("'", ""))
        elif not n_.startswith(("bild:", "ficon:", "icon:", "karte", "linie", "pfeil", "ring", "marker", "haken", "kreuz")):
            glyphen(n_)
