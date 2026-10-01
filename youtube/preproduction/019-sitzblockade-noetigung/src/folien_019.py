"""Folge 019 · Sitzblockade Nötigung: Klimakleber & die Zweite-Reihe-Rechtsprechung – Serienstandard Open Peeps (Katzenkönig).
Fiktiver Fall, Personen erfunden, keine reale Gruppe. Szenen laut ../SZENENPLAN.md: A Die Blockade / die erste Reihe (Ringstraße),
B Die zweite Reihe (Stau), C Sachverhalt, D Gewalt: erste Reihe (Wortlaut § 240 I StGB), E Zweite-Reihe-Rechtsprechung,
F Festkleben, G Mittäterschaft/Erfolg/Vorsatz, H Rechtswidrigkeit (Wortlaut § 240 II StGB, Abwägungskriterien),
I Abwägung im Fall/Ergebnis, J Gegenfall, K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung: das erste Auto bremst, Sabine steigt aus (Autotür) – Freesound CC0."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np
import wave as _wave

bausteine.FIGORDNER = "op_019/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
ASPHALT = (214, 216, 224, 255)
HAUS = (226, 231, 246, 255)
WIESE = (196, 230, 190, 255)
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


def hand(name, cx, unten, hoehe, seite, von=0.55, bis=1.0):
    """Äußerster Figurenpunkt (Hand am Boden) im Höhenband von–bis; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * von):int(h * bis)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return e.x + xs[i], e.y + int(h * von) + ys[i]


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
    return els


# --- Eigene Hilfsfunktion (wie Folge 018): Mundbewegung nur, solange im Wort tatsächlich Stimme klingt ----------------
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


def redet_019(basis, cx, unten, hoehe, cue, bis, **k):
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


redet = redet_019

BODEN, FH = 860, 440
SITZ = 290                                  # Sitzende: Kopf etwa so groß wie bei Stehenden
FX, BR, FR = 1560, 930, 470                 # Figur rechts neben der Tafel
NAMEN = {"HA": ("Hanna", LILA), "LU": ("Lukas", GRUEN), "DI": ("Dieter", ROT), "SA": ("Sabine", BLAU)}


def name(p, cx, cue, unten=BODEN, size=28, d=0.2, bis=None, anim="pop"):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 30, cue, fill=f, size=size, anker="m", d=d, bis=bis, anim=anim)


def strasse(cue, x0=60, x1=1860, haeuser=False):
    """Ringstraße von der Seite: Asphaltband, Bodenlinie, Häuserzeile im Hintergrund."""
    els = []
    if haeuser:
        els += [hart(ficon("tabler", n, x, BODEN - 4, b, cue, fuell=HAUS, anim="cut"))
                for n, x, b in (("buildings", 300, 300), ("building-skyscraper", 760, 190), ("buildings", 1180, 280),
                                ("building", 1640, 230))]
    els += [hart(karte(x0, BODEN, x1 - x0, 70, cue, fill=ASPHALT, rund=0, schatten=0, rand=0, anim="cut")),
            hart(linienzug([(x0, BODEN), (x1, BODEN)], cue, breite=6, farbe=INK)),
            hart(linienzug([(x0, BODEN + 70), (x1, BODEN + 70)], cue, breite=4, farbe=INK))]
    return els


def auto(cx, cue, fill, breite=330, bis=None, anim="pop", d=0.0, links=True):
    """Pkw (tabler car) auf der Fahrbahn, Front nach links (fährt Richtung Blockade)."""
    return ficon("tabler", "car", cx, BODEN + 40, breite, cue, fuell=fill, spiegeln=links, bis=bis, anim=anim, d=d)


# A Fall: die Blockade und die erste Reihe -----------------------------------------------------------------------------
E2X, LUX, HAX, E1X = 200, 400, 640, 860        # Sitzende, blicken nach rechts zum Verkehr
CAR1, DIX = 1210, 1640
HAr = ("HA_redet_r", HAX, BODEN + 30, SITZ)
DIb = ("DI_redet", DIX, BODEN + 20, FH)
khx, khy = hand("HA_ernst_r", HAX, BODEN + 30, SITZ, +1)
erstes = szene(bewegt(auto(CAR1, "dieter", ROT, anim="fade"), "dieter", beim("dieter", "bremst", ende=True), 520),
               "019bremse*", 1.0, versatz=-0.3)
folie([(NULL, "Fall · Die Blockade"), ("dieter", "Fall · Die erste Reihe")], [
    hart(pl("Die Sitzblockade", 70, 40, NULL, fill=GELB, size=46, anim="cut")),
    hart(ficon("tabler", "sun", 1760, 200, 120, NULL, fuell=GELB, anim="cut")),
    *strasse(NULL),
    hart(pl("Montag, 8 Uhr", 520, 46, NULL, fill=WEISS, size=34, anim="cut")),
    pl("Berufsverkehr", 960, 300, beim("fall", "Berufsverkehr"), fill=WEISS, size=34, anker="m", bis="sitzen"),
    pl("Ringstraße", 960, 220, beim("fall", "Ringstraße"), fill=WEISS, size=34, anker="m", bis="sitzen"),
    # die vier Sitzenden
    *fig("E2", E2X, BODEN + 30, SITZ, [("sitzen", "ruhig_r")]),
    *fig("LU", LUX, BODEN + 30, SITZ, [(("sitzen", 0.15), "ruhig_r"), ("lukas", "denkt_r")]),
    *fig("HA", HAX, BODEN + 30, SITZ, [(("sitzen", 0.3), "ruhig_r"), ("kleben", "ernst_r")], bis="h1"),
    *redet("HA_redet_r", HAX, BODEN + 30, SITZ, "h1", "dieter"),
    peep_voll("HA_ernst_r", HAX, BODEN + 30, SITZ, "dieter", anim="cut"),
    *fig("E1", E1X, BODEN + 30, SITZ, [(("sitzen", 0.45), "ruhig_r")]),
    pl("nach gemeinsamem Plan", 520, 300, beim("sitzen", "Plan"), fill=WEISS, size=32, anker="m", bis="kleben"),
    pl("quer über alle Spuren", 520, 380, beim("sitzen", "Spuren"), fill=WEISS, size=32, anker="m", bis="kleben"),
    ficon("tabler", "droplet", khx + 6, khy + 6, 54, beim("kleben", "Sekundenkleber"), fuell=GELB),
    pl("Sekundenkleber", HAX, 420, beim("kleben", "Sekundenkleber"), fill=GELB, size=32, anker="m", bis="h1"),
    pl("sitzt nur", LUX, 480, beim("lukas", "sitzt"), fill=GRUEN, size=30, anker="m", bis="h1"),
    name("HA", HAX, "kleben"), name("LU", LUX, "lukas"),
    blase("sprech", 600, 200, "h1", 1260, 300, inhalt=["Wir bleiben hier sitzen.", "Für mehr Klimaschutz!"], textsize=36,
          figur=HAr, bis="dieter"),
    # Dieter kommt als Erster und bremst
    erstes,
    pl("als Erster", CAR1, 600, beim("dieter", "Erster"), fill=ROT, size=30, anker="m"),
    *fig("DI", DIX, BODEN + 20, FH, [(beim("dieter", "bremst", ende=True), "schreck")], bis="d1"),
    *redet("DI_redet", DIX, BODEN + 20, FH, "d1", "sabine"),
    name("DI", DIX, beim("dieter", "bremst", ende=True), unten=BODEN + 20),
    blase("sprech", 640, 200, "d1", 1260, 250, inhalt=["Ich kann doch nicht", "über Menschen fahren!"], textsize=38,
          figur=DIb),
])

# Berufsverkehr vor der Blockade: zwei Autos fahren von rechts nach links durchs Bild und verlassen es vor [sitzen]
# (bewusst außerhalb des Bildes beginnend/endend, deshalb nach folie() angehängt – wie die einfahrenden Autos in Folge 001)
FOLIEN[-1]["els"] += [bewegt(auto(-260, NULL, GRAU, breite=300, anim="cut", bis="sitzen"), NULL, ("fall", 3.0), 1720),
                      bewegt(auto(-260, NULL, GELB, breite=300, anim="cut", bis="sitzen"), ("fall", 0.4), ("fall", 4.0), 2420)]

# B Fall: die zweite Reihe -------------------------------------------------------------------------------------------
C1, C2, SAX, C3, C4 = 440, 800, 1110, 1420, 1740
SAb = ("SA_redet", SAX, BODEN + 20, FH)
zweites = bewegt(auto(C2, "sabine", BLAU, anim="fade"), "sabine", beim("sabine", "hält", ende=True), 420)
folie([("sabine", "Fall · Die zweite Reihe"), ("frage", "Fall · Die Frage")], [
    *strasse("sabine"),
    auto(C1, "sabine", ROT, anim="cut"),
    pl("Dieter", C1, 600, "sabine", fill=ROT, size=28, anker="m"),
    zweites,
    szene(peep_voll("SA_ruhig", SAX, BODEN + 20, FH, beim("sabine", "Sabine", ende=True), anim="pop", bis="s1"), "019tuer*", 0.9),
    *redet("SA_redet", SAX, BODEN + 20, FH, "s1", "polizei"),
    *fig("SA", SAX, BODEN + 20, FH, [("polizei", "genervt"), (beim("polizei", "fünfzig"), "muede")], erst="cut"),
    name("SA", SAX, beim("sabine", "Sabine", ende=True), unten=BODEN + 20),
    auto(C3, beim("sabine", "staut"), GRAU, breite=300),
    auto(C4, beim("sabine", "staut"), GRAU, breite=300, d=0.25),
    pl("über 1 km Stau", 1540, 560, beim("sabine", "Kilometer"), fill=WEISS, size=32, anker="m"),
    ficon("tabler", "trees", 165, BODEN - 2, 170, beim("eng", "Mittelinsel"), fuell=GRUEN),
    pl("Mittelinsel", 165, 600, beim("eng", "Mittelinsel"), fill=GRUEN, size=28, anker="m"),
    pl("Gehweg", 1600, BODEN + 12, beim("eng", "Gehweg"), fill=WEISS, size=28, anker="m"),
    blase("sprech", 720, 200, "s1", 1030, 220, inhalt=["Vor mir ein Auto, hinter mir ein Auto.", "Ich komme hier nicht weg."],
          textsize=34, figur=SAb, bis="polizei"),
    ficon("tabler", "calendar-off", 160, 330, 100, "polizei", fuell=WEISS),
    pl("nicht angekündigt", 230, 250, "polizei", fill=WEISS, size=32),
    ficon("tabler", "clock", 160, 470, 100, beim("polizei", "fünfzig"), fuell=GELB),
    pl("nach 50 Minuten", 230, 390, beim("polizei", "fünfzig"), fill=GELB, size=32),
    ficon(HC, "police-car", 1560, 330, 130, beim("polizei", "Polizei"), fuell=None),
    pl("Polizei löst die Hand, räumt", 1560, 360, beim("polizei", "Polizei"), fill=WEISS, size=30, anker="m"),
    pl("Nötigung, § 240 StGB?", 960, 40, beim("frage", "Nötigung"), fill=PINK, size=40, anker="m"),
])

# C Sachverhalt ----------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Montag, 8 Uhr, Berufsverkehr auf der Ringstraße: Hanna, Lukas und zwei weitere Personen setzen sich nach gemeinsamem "
    "Plan quer über alle Fahrspuren auf die Fahrbahn, um den Verkehr anzuhalten. Hanna klebt ihre Hand mit Sekundenkleber "
    "auf dem Asphalt fest, Lukas sitzt nur daneben. Angekündigt ist die Aktion nicht.",
    "Dieter hält als Erster, um niemanden zu überfahren. Hinter ihm hält Sabine, dahinter staut es sich über einen "
    "Kilometer. Links liegt eine Mittelinsel, rechts der Gehweg; ausweichen kann niemand. Nach 50 Minuten hat die Polizei "
    "Hannas Hand gelöst und die Straße geräumt.",
    "(Fiktiver Fall, alle Personen erfunden.)",
], "Haben sich die vier wegen Nötigung (§ 240 StGB) strafbar gemacht?")

# D Gewalt: Wortlaut § 240 I, BVerfGE 92, 1, erste Reihe -------------------------------------------------------------
P240_1 = ["„Wer einen Menschen rechtswidrig mit Gewalt oder durch", "Drohung mit einem empfindlichen Übel zu einer Handlung,",
          "Duldung oder Unterlassung nötigt, …“"]
folie([("pruef", "Nötigung, § 240 StGB › I. Tatbestand"), ("gewalt", "§ 240 StGB › I. 1. Gewalt"),
       ("bv95", "§ 240 StGB › I. 1. Gewalt › BVerfGE 92, 1 (Art. 103 II GG)"), ("dieter2", "§ 240 StGB › I. 1. Gewalt › erste Reihe: Dieter")], [
    *tafel("pruef", "Nötigung, § 240 StGB"),
    *wortlaut(100, 165, 1060, P240_1, "§ 240 Abs. 1 StGB", beim("pruef", "Nötigung"), marken=[(0, "mit Gewalt", "gewalt")]),
    z("Gewalt = körperlich wirkender Zwang", 110, 425, "def", "Bold", 36),
    z("früher: bloße Anwesenheit genügte, wenn sie", 110, 485, "alt", size=34),
    z("psychisch hemmte („vergeistigter“ Gewaltbegriff)", 150, 532, beim("alt", "psychisch"), size=34, farbe=TEXT),
    z("BVerfGE 92, 1 (10.1.1995): verworfen", 110, 598, "bv95", "Bold", 36),
    z("nur Anwesenheit + nur psychischer Zwang:", 150, 652, "anwesend", size=34),
    z("keine Gewalt", 150, 700, beim("anwesend", "keine"), "Bold", 34),
    z("sonst Verstoß gegen Art. 103 II GG", 150, 752, "art103", size=34),
    nein(135, 845, beim("dieter2", "Das"), gr=24),
    z("Dieter: bloßes Sitzen ist keine Gewalt", 175, 822, beim("dieter2", "Das"), "Bold", 36),
    *fig("DI", FX, BR, FR, [("pruef", "ruhig"), ("dieter2", "denkt")]),
    ficon("tabler", "car", 1560, 330, 220, "dieter2", fuell=ROT, spiegeln=True),
    pl("psychischer Zwang", 1560, 96, "anwesend", fill=PINK, size=30, anker="m"),
])

# E Zweite-Reihe-Rechtsprechung ---------------------------------------------------------------------------------------
folie([("zweite", "§ 240 StGB › I. 1. Gewalt › zweite Reihe: Sabine (BGHSt 41, 182)"),
       ("bv11", "§ 240 StGB › I. 1. Gewalt › BVerfG 2011: mittelbare Täterschaft")], [
    *tafel("zweite", "Die Zweite-Reihe-Rechtsprechung"),
    z("BGH, 20.7.1995 – 1 StR 126/95 (BGHSt 41, 182)", 110, 200, beim("zweite", "Bundesgerichtshof"), "Bold", 34),
    ok(135, 290, "hindernis", gr=24),
    z("Sabine: Auto von Dieter = körperliches Hindernis", 175, 270, "hindernis", size=34),
    ok(135, 360, "werkzeug", gr=24),
    z("Blockierer benutzen das erste Auto als Werkzeug", 175, 340, "werkzeug", size=34),
    fl_block(110, 440, 1040, 170, GRUEN, "bv11", [("BVerfG (Kammer), 7.3.2011 – 1 BvR 388/05:", "Bold", 32, INK),
                                                  ("gebilligt", "ExtraBold", 40, INK)]),
    z("Gewalt in mittelbarer Täterschaft, § 25 I Alt. 2 StGB", 110, 650, beim("bv11", "mittelbarer"), size=34),
    # Mini-Kette rechts oben: Blockade → erstes Auto → zweites Auto
    peep_voll("E1_ruhig_r", 1320, 330, 120, "zweite"),
    ficon("tabler", "car", 1510, 330, 170, "zweite", fuell=ROT, spiegeln=True),
    ficon("tabler", "car", 1730, 330, 170, "hindernis", fuell=BLAU, spiegeln=True),
    pl("Hindernis", 1510, 140, "hindernis", fill=ROT, size=28, anker="m"),
    pl("Werkzeug", 1510, 360, "werkzeug", fill=WEISS, size=28, anker="m"),
    *fig("SA", FX + 40, BR, FR, [("zweite", "ruhig"), ("hindernis", "genervt"), ("bv11", "ernst")]),
])

# F Festkleben ---------------------------------------------------------------------------------------------------------
fhx, fhy = hand("HA_ernst", FX, BR, SITZ + 30, -1)
folie([("kleber", "§ 240 StGB › I. 1. Gewalt › Festkleben"), ("offen", "§ 240 StGB › I. 1. Gewalt › Festkleben: offen")], [
    *tafel("kleber", "Und das Festkleben?"),
    z("BVerfGE 104, 92 (24.10.2001):", 110, 200, "kette", "Bold", 36),
    ok(135, 285, beim("kette", "Anketten"), gr=24),
    z("Anketten als Gewalt zulässig: echte Barriere", 175, 265, beim("kette", "Anketten"), size=34),
    z("OLG Karlsruhe, 4.2.2025 – 2 ORs 350 SRs 613/24:", 110, 365, "olg", "Bold", 34),
    ok(135, 450, beim("olg", "Festkleben"), gr=24),
    z("Festkleben = Gewalt", 175, 430, beim("olg", "Festkleben"), "Bold", 36),
    z("Folge: auf die zweite Reihe käme es nicht mehr an", 110, 510, "erste", size=32, farbe=TEXT),
    z("BayObLG, 11.3.2025 – 203 StRR 1/25:", 110, 600, "offen", "Bold", 34),
    z("Frage offengelassen", 175, 660, beim("offen", "offengelassen"), size=34),
    pl("höchstrichterlich ungeklärt", 110, 740, beim("offen", "Höchstrichterlich"), fill=PINK, size=34),
    *fig("HA", FX, BR, SITZ + 30, [("kleber", "ernst")]),
    ficon("tabler", "droplet", fhx - 4, fhy + 6, 60, "kleber", fuell=GELB),
    ficon("tabler", "link", 1440, 330, 120, beim("kette", "Anketten"), fuell=GRAU),
    pl("Anketten", 1440, 360, beim("kette", "Anketten"), fill=WEISS, size=28, anker="m"),
    pl("Festkleben", 1700, 360, beim("olg", "Festkleben"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "droplet", 1700, 330, 90, beim("olg", "Festkleben"), fuell=GELB),
    name("HA", FX, "kleber", unten=BR - 10),
])

# G Mittäterschaft, Nötigungserfolg, Vorsatz -----------------------------------------------------------------------------
folie([("lukas2", "§ 240 StGB › I. Tatbestand › Mittäterschaft, § 25 II StGB"), ("erfolg", "§ 240 StGB › I. 2. Nötigungserfolg"),
       ("vorsatz", "§ 240 StGB › I. 3. Vorsatz")], [
    *tafel("lukas2", "Lukas, Erfolg, Vorsatz"),
    z("Lukas klebt nicht", 110, 200, "lukas2", "Bold", 36),
    ok(135, 285, beim("lukas2", "gemeinsamen"), gr=24),
    z("gemeinsamer Plan: Mittäter, § 25 II StGB", 175, 265, beim("lukas2", "gemeinsamen"), size=34),
    ok(135, 400, "erfolg", gr=24),
    z("2. Nötigungserfolg: Sabine muss warten", 175, 380, "erfolg", "Bold", 36),
    ok(135, 495, "vorsatz", gr=24),
    z("3. Vorsatz: alle vier", 175, 475, "vorsatz", "Bold", 36),
    *fig("LU", 1400, BR, SITZ + 30, [("lukas2", "denkt")]),
    name("LU", 1400, "lukas2", unten=BR - 10),
    *fig("SA", 1720, BR, FR, [("erfolg", "muede")]),
    ficon("tabler", "clock", 1720, 400, 110, beim("erfolg", "warten"), fuell=GELB),
])

# H Rechtswidrigkeit: § 34, Art. 8 GG, Wortlaut § 240 II, Abwägungskriterien ------------------------------------------------
P240_2 = ["„Rechtswidrig ist die Tat, wenn die Anwendung der Gewalt", "oder die Androhung des Übels zu dem angestrebten",
          "Zweck als verwerflich anzusehen ist.“"]
folie([("rw", "§ 240 StGB › II. Rechtswidrigkeit"), ("art8", "§ 240 StGB › II. Rechtswidrigkeit › Art. 8 GG"),
       ("kein", "§ 240 StGB › II. Rechtswidrigkeit › Verwerflichkeit, § 240 II StGB"),
       ("abw", "§ 240 StGB › II. Verwerflichkeit › Abwägung (BVerfGE 104, 92)")], [
    *tafel("rw", "II. Rechtswidrigkeit"),
    bis_(nein(135, 225, "not", gr=22), "abw"),
    z("Notstand, § 34 StGB: von den OLG abgelehnt", 175, 200, "not", size=34, bis="abw"),
    z("Art. 8 GG: Sitzblockade = Versammlung", 110, 275, "art8", "Bold", 36, bis="abw"),
    z("bleibt friedlich, auch wenn sie andere behindert", 150, 335, "friedlich", size=34, bis="abw"),
    bis_(nein(175, 415, beim("kein", "rechtfertigt"), gr=22), "abw"),
    z("rechtfertigt nicht → wirkt in § 240 II StGB", 215, 395, beim("kein", "rechtfertigt"), size=34, bis="abw"),
    # Kriterien (ersetzen die Zeilen oben)
    z("Abwägung nach BVerfGE 104, 92:", 110, 190, "abw", "Bold", 34),
    z("· Dauer und Intensität", 150, 245, beim("abw", "Dauer"), size=34),
    z("· vorherige Bekanntgabe", 150, 295, beim("abw", "vorherige"), size=34),
    z("· Ausweichmöglichkeiten", 150, 345, beim("abw", "Ausweichmöglichkeiten"), size=34),
    z("· Dringlichkeit der Fahrten", 150, 395, beim("abw", "Dringlichkeit"), size=34),
    z("· Sachbezug zum Protestthema", 150, 445, beim("abw", "Sachbezug"), size=34),
    pl("politisches Anliegen: nicht bewerten", 110, 498, "inhalt", fill=PINK, size=30),
    *wortlaut(100, 600, 1060, P240_2, "§ 240 Abs. 2 StGB", beim("kein", "Verwerflichkeit"),
              marken=[(2, "verwerflich", beim("kein", "Verwerflichkeit"))]),
    *fig("HA", 1400, BR, SITZ + 30, [("rw", "ruhig")]),
    *fig("LU", 1740, BR, SITZ + 30, [("rw", "ruhig")]),
    pl("Versammlung", 1570, 480, beim("art8", "Versammlung"), fill=WEISS, size=30, anker="m"),
])

# I Abwägung im Fall, Schuld, Ergebnis ---------------------------------------------------------------------------------
folie([("subs", "§ 240 StGB › II. Verwerflichkeit › Abwägung im Fall"), ("schuld", "§ 240 StGB › III. Schuld · Ergebnis")], [
    *tafel("subs", "Abwägung im Fall"),
    ficon("tabler", "clock", 150, 240, 56, beim("subs", "fünfzig"), fuell=GELB),
    z("50 Minuten im Berufsverkehr", 200, 195, beim("subs", "fünfzig"), size=36),
    ficon("tabler", "calendar-off", 150, 305, 56, beim("subs", "unangekündigt"), fuell=WEISS),
    z("unangekündigt", 200, 260, beim("subs", "unangekündigt"), size=36),
    ficon("tabler", "ban", 150, 370, 56, beim("subs", "kein"), fuell=ROT),
    z("kein Ausweichen", 200, 325, beim("subs", "kein"), size=36),
    ficon("tabler", "car", 150, 432, 60, "sach", fuell=GRAU),
    z("Sachbezug zum Autoverkehr: nur teilweise", 200, 390, "sach", size=36),
    fl_block(110, 470, 1040, 100, GRUEN, "verw", [("Verwerflichkeit (+), mit den OLG", "ExtraBold", 38, INK)]),
    ok(135, 625, "schuld", gr=24), z("III. Schuld (+)", 175, 605, "schuld", "Bold", 36),
    fl_block(110, 680, 1040, 170, GRUEN, "erg", [("Alle vier: Nötigung, §§ 240, 25 II StGB", "ExtraBold", 38, INK),
                                                ("jedenfalls gegenüber Sabine und den Fahrern hinter ihr", "Regular", 30, INK)]),
    *fig("SA", FX, BR, FR, [("subs", "muede"), ("erg", "ernst")]),
])

# J Gegenfall: kurze, angekündigte Blockade mit Umleitung -------------------------------------------------------------
folie([("gegen", "Gegenfall · kurze, angekündigte Blockade")], [
    *strasse("gegen"),
    *fig("E2", 380, BODEN + 30, SITZ, [("gegen", "ruhig_r")]),
    *fig("E1", 600, BODEN + 30, SITZ, [(("gegen", 0.15), "ruhig_r")]),
    auto(1000, "gegen", GRAU, breite=300),
    pl("kurz", 490, 520, beim("gegen", "kurze"), fill=WEISS, size=34, anker="m"),
    ficon("tabler", "calendar", 980, 330, 110, beim("gegen", "bekannt"), fuell=GRUEN),
    pl("vorher bekannt gegeben", 980, 360, beim("gegen", "bekannt"), fill=GRUEN, size=30, anker="m"),
    ficon("tabler", "route", 1690, 640, 120, beim("gegen", "Umleitung"), fuell=WEISS),
    pl("Umleitung", 1690, 670, beim("gegen", "Umleitung"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "scale", 1400, 330, 120, beim("gegen", "leichter"), fuell=GELB),
    pl("wiegt viel leichter", 1400, 360, beim("gegen", "leichter"), fill=GELB, size=32, anker="m"),
    pl("Verwerflichkeit kann fehlen", 960, 970, "gegen2", fill=PINK, size=38, anker="m"),
])

# K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Gewalt je Reihe prüfen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Gewalt getrennt für jede Reihe prüfen", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("1. Reihe: nur psychischer Zwang", 200, 300, "tipp1", size=36),
    z("außer: Festkleben schon Gewalt?", 240, 355, beim("tipp1", "es"), size=34, farbe=TEXT),
    z("ab 2. Reihe: Zweite-Reihe-Rechtsprechung", 200, 450, "tipp2", size=36),
    z("Art. 8 GG → in die Verwerflichkeit", 200, 550, "tipp3", "Bold", 36),
    z("kein eigener Rechtfertigungsgrund", 240, 605, beim("tipp3", "nicht"), size=34, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pl("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# L Klausurschema ---------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Nötigung, § 240 StGB", 110, 90, "sch", 54),
    z("I. Tatbestand, § 240 I StGB", K1, 210, "k1", "Bold", 40, rechts=1820),
    z("1. Gewalt, getrennt nach erster und zweiter Reihe (ggf. Festkleben, Zweite-Reihe-Rspr.)", K3, 280, "k1a",
      size=32, farbe=TEXT, rechts=1820),
    z("2. Nötigungserfolg", K3, 340, "k1b", size=32, farbe=TEXT, rechts=1820),
    z("3. Vorsatz", K3, 400, "k1c", size=32, farbe=TEXT, rechts=1820),
    z("II. Rechtswidrigkeit", K1, 490, "k2", "Bold", 40, rechts=1820),
    z("1. keine Rechtfertigung", K3, 560, "k2a", size=32, farbe=TEXT, rechts=1820),
    z("2. Verwerflichkeit, § 240 II StGB: Abwägung mit Art. 8 GG", K3, 620, "k2b", size=32, farbe=TEXT, rechts=1820),
    z("III. Schuld", K1, 720, "k3", "Bold", 40, rechts=1820),
])

# M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Sitzen allein ist ", 0), ("keine Gewalt.", "a")]], 750, 320, 52, "merke", {"a": beim("merke", "keine")}),
    *markertext([[("Wer das erste Auto zur Barriere macht,", 0)], [("nötigt", "b"), (" die Fahrer dahinter.", 0)]],
                750, 450, 46, "m2", {"b": beim("m2", "nötigt")}),
    *markertext([[("Ob das rechtswidrig ist, entscheidet", 0)], [("die Verwerflichkeit.", "c")]],
                750, 640, 46, "m3", {"c": beim("m3", "Verwerflichkeit")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
