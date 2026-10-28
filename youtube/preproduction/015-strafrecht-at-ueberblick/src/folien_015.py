"""Folge 015 · Strafrecht AT Überblick: Welches Prüfungsschema wann? – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Gartenfest (Blumentopf), B Am Zaun (Rasenmäher), C Am Grill, D Gerdas Hund, E Fallfrage,
F Sachverhalt, G Grundfall und vier Weichen, H A. Konrad (Grundschema), I B. Ina (Beteiligung), J1/J2 C. Rudolf (Versuch),
K1/K2 D. Bernd (Fahrlässigkeit), L1/L2 E. Gerda (Unterlassen), M Klausurtipp (Lexi), N Klausurschema (Entscheidungsbaum),
O Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Topf zerbricht, Stichflamme, Hund knurrt)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont
import numpy as np

bausteine.FIGORDNER = "op_015/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
WIESE = (214, 236, 200, 255)
DAUER = bausteine._cj()["dauer"]

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
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def fig(name, cx, unten, hoehe, folge, d=0.0, bis=None, erst="pop"):
    """Mimikfolge einer Figur am selben Platz: folge = [(cue, suffix)] → harte Schnitte; erstes Bild poppt (erst="cut",
    wenn die Figur am selben Platz schon zu sehen war)."""
    els = []
    for i, (c, s) in enumerate(folge):
        b = folge[i + 1][0] if i + 1 < len(folge) else bis
        els.append(peep_voll(f"{name}_{s}", cx, unten, hoehe, c, anim=erst if i == 0 else "cut", d=d if i == 0 else 0.0, bis=b))
    return els


def gedreht(el, winkel, cx, unten):
    """Requisit gekippt (umgestürzter Topf): Sprite gedreht, unten mittig auf (cx, unten)."""
    el.sprite = el.sprite.rotate(winkel, expand=True, resample=Image.BICUBIC)
    el.sprite = el.sprite.crop(el.sprite.getbbox())
    el.x, el.y = int(cx - el.sprite.width / 2), int(unten - el.sprite.height)
    return el


def hand(name, cx, unten, hoehe, seite):
    """Äußerster Punkt der Figur (ausgestreckte Hand) im Band 28–60 % der Höhe; seite = -1 links, +1 rechts."""
    e = peep_voll(name, cx, unten, hoehe, "_")
    a = np.asarray(e.sprite)[:, :, 3] > 40
    h = a.shape[0]
    band = a[int(h * 0.28):int(h * 0.60)]
    ys, xs = np.nonzero(band)
    i = xs.argmin() if seite < 0 else xs.argmax()
    return e.x + xs[i], e.y + int(h * 0.28) + ys[i]


def garten(cue, zaun=(), x0=60, x1=1860):
    """Kleingarten: Wiese als Bodenstreifen, Bodenlinie, Zaunfelder im Hintergrund."""
    els = [karte(x0, BODEN, x1 - x0, 60, cue, fill=WIESE, rund=0, schatten=0, rand=0),
           linienzug([(x0, BODEN), (x1, BODEN)], cue, breite=7, farbe=INK)]
    els += [ficon("tabler", "fence", x, BODEN - 2, 150, cue, fuell=WEISS, nebenfarbe=WEISS) for x in zaun]
    return els


BODEN, FH = 880, 480
FB, FR = 930, 420                          # Figuren neben der Tafel
SITZ = 310                                 # Gerda sitzend (closed_legs-1): Kopf gleich groß wie stehend
NAMEN = {"OT": ("Otto", LILA), "KO": ("Konrad", BLAU), "IN": ("Ina", ROT), "RU": ("Rudolf", GELB), "BE": ("Bernd", ORANGE),
         "GE": ("Gerda", GRUEN)}


def name(p, cx, cue, unten=BODEN, size=30, d=0.2, bis=None):
    t, f = NAMEN[p]
    return pl(t, cx, unten + 22, cue, fill=f, size=size, anker="m", d=d, bis=bis)


# A Fall: Gartenfest, Blumentopf ------------------------------------------------------------------------------------------
OTX, TOPF, KOX, INX, KOS = 380, 640, 1250, 1600, 860
KOR = ("KO_redet_r", KOX, BODEN, FH)
hx, hy = hand("IN_ruhig", INX, BODEN, FH, -1)                 # Ina hält den Hammer in der Hand
kx, ky = hand("KO_ruhig_r", KOX, BODEN, FH, +1)               # Konrads ausgestreckte Hand (blickt nach rechts zu Ina)
sx, sy = hand("KO_wuetend", KOS, BODEN, FH, -1)              # Konrad am Topf, Hand nach links
folie([("fall", "Fall · Sommerfest im Kleingarten")], [
    *garten("fall", zaun=(1050, 1430)),
    pl("Der Gartenfest-Fall", 70, 40, "fall", fill=GELB, size=46),
    *[ficon("ph", "tree", x, BODEN - 2, 150, "fall", fuell=GRUEN) for x in (150, 1790)],
    ficon("tabler", "sun", 1700, 230, 110, "fall", fuell=GELB, nebenfarbe=GELB),
    ficon("ph", "potted-plant", TOPF, BODEN - 2, 130, "fall", fuell=ORANGE, nebenfarbe=GRUEN, bis="schlag"),
    gedreht(ficon("ph", "potted-plant", TOPF, BODEN - 2, 130, "schlag", fuell=ORANGE, nebenfarbe=GRUEN, anim="cut"), 100, TOPF - 20, BODEN - 2),
    szene(pl("Topf zerschlagen", TOPF - 40, 700, "schlag", fill=ROT, size=30, anker="m"), "015topf*", 0.9, versatz=-0.08),
    # Otto
    *fig("OT", OTX, BODEN, FH, [("fall", "ruhig_r"), ("otto", "streng_r"), ("schlag", "schreck_r")]),
    name("OT", OTX, "otto"),
    pl("Streit um die Hecke", 600, 250, beim("otto", "Hecke"), fill=WEISS, size=32, anker="m", bis="schlag"),
    pl("Ottos Blumentopf", TOPF, 640, beim("k1", "Blumentopf"), fill=WEISS, size=28, anker="m", bis="schlag"),
    # Konrad: spricht Ina an (blickt nach rechts), läuft dann zum Topf
    peep_voll("KO_wuetend", KOX, BODEN, FH, beim("otto", "Konrad"), bis="k1"),      # erst Blick zu Otto (Streit)
    *redet("KO_redet_r", KOX, BODEN, FH, "k1", "reicht"),
    peep_voll("KO_ruhig_r", KOX, BODEN, FH, "reicht", anim="cut", bis="schlag"),
    bewegt(peep_voll("KO_wuetend", KOS, BODEN, FH, "schlag", anim="cut"), "schlag", ("schlag", 0.6), KOX - KOS, 0),
    name("KO", KOX, beim("otto", "Konrad"), bis="schlag"),
    name("KO", KOS, ("schlag", 0.6), d=0.0),
    blase("sprech", 700, 190, "k1", 980, 200, inhalt=["Ina, gib mir mal deinen Hammer.", "Ottos Blumentopf ist fällig."],
          textsize=31, figur=KOR, bis="reicht"),
    # Ina mit dem Hammer
    *fig("IN", INX, BODEN, FH, [("k1", "ruhig"), ("reicht", "cool")]),
    name("IN", INX, "k1"),
    ficon("tabler", "hammer", hx - 10, hy + 40, 90, beim("k1", "Hammer"), fuell=GRAU, nebenfarbe=ORANGE, bis="reicht"),
    bewegt(ficon("tabler", "hammer", kx + 20, ky + 40, 90, "reicht", fuell=GRAU, nebenfarbe=ORANGE, anim="cut", bis="schlag"),
           "reicht", ("reicht", 0.7), (hx - 10) - (kx + 20), (hy - ky)),
    bewegt(ficon("tabler", "hammer", sx - 20, sy + 40, 90, "schlag", fuell=GRAU, nebenfarbe=ORANGE, anim="cut", spiegeln=True),
           "schlag", ("schlag", 0.6), KOX - KOS, 0),
    pl("reicht den Hammer", INX - 180, 300, "reicht", fill=GELB, size=30, anker="m", bis="schlag"),
])

# B Fall: Am Zaun, Rasenmäher ---------------------------------------------------------------------------------------------
RU1, RU2, MAEH, PFOST = 560, 1060, 1300, 1560
folie([("rudolf", "Fall · Am Zaun: Ottos Rasenmäher")], [
    *garten("rudolf", zaun=(180, 1760)),
    linienzug([(PFOST, BODEN), (PFOST, 560)], "rudolf", breite=16, farbe=INK),
    ficon("tabler", "lawn-mower", MAEH, BODEN - 2, 260, "rudolf", fuell=ROT, nebenfarbe=WEISS),
    pl("Ottos Rasenmäher", MAEH, 560, "rudolf", fill=WEISS, size=30, anker="m", d=0.3),
    *fig("RU", RU1, BODEN, FH, [("rudolf", "ruhig_r"), (beim("rudolf", "behalten"), "gierig_r")], bis="zieht"),
    name("RU", RU1, "rudolf", bis="zieht"),
    pl("will ihn mitnehmen und behalten", 760, 300, beim("rudolf", "behalten"), fill=GELB, size=30, anker="m", bis="zieht"),
    *fig("RU", RU2, BODEN, FH, [("zieht", "zieht_r"), ("kette", "schreck_r"), (beim("kette", "Werkzeug"), "ertappt_r")]),
    name("RU", RU2, "zieht"),
    pfeil(RU2 - 120, 560, RU2 - 340, 560, beim("zieht", "zieht"), breite=9, kopf=30, farbe=DROT, bis="kette"),   # Zugrichtung hinter Rudolf
    pl("zieht los", RU2 - 240, 480, beim("zieht", "zieht"), fill=WEISS, size=30, anker="m", bis="kette"),
    gedreht(ficon("fluent-emoji-high-contrast", "chains", 0, 0, 100, "kette", fuell=GRAU, nebenfarbe=GRAU), 90,
            (MAEH + 120 + PFOST) // 2, BODEN - 60),
    ring((MAEH + 120 + PFOST) // 2, BODEN - 85, 120, 60, "kette", farbe=DROT, breite=7),
    pl("angekettet", PFOST + 170, 620, "kette", fill=ROT, size=32, anker="m"),
    pl("kein Werkzeug", RU2, 300, beim("kette", "Werkzeug"), fill=WEISS, size=30, anker="m"),
])

# C Fall: Am Grill ------------------------------------------------------------------------------------------------------------
BEX, GRX, OTG = 560, 930, 1330
bx, by = hand("BE_ruhig_r", BEX, BODEN, FH, +1)
folie([("grill", "Fall · Am Grill")], [
    *garten("grill", zaun=(180, 1130, 1760)),
    ficon("tabler", "grill", GRX, BODEN - 2, 230, "grill", fuell=GRAU, nebenfarbe=WEISS),
    *fig("BE", BEX, BODEN, FH, [("grill", "froh_r"), ("flamme", "schreck_r"), ("blase", "ertappt_r")]),
    name("BE", BEX, "grill"),
    ficon("tabler", "bottle", bx + 30, by + 60, 70, beim("grill", "Brennspiritus"), fuell=BLAU, nebenfarbe=WEISS),
    pl("Brennspiritus", bx + 160, by - 60, beim("grill", "Brennspiritus"), fill=BLAU, size=28, anker="m", bis="flamme"),
    pfeil(bx + 70, by + 10, GRX - 40, BODEN - 210, beim("grill", "Glut"), breite=8, kopf=26, farbe=INK, bis="flamme"),
    pl("damit es schneller geht", 760, 250, beim("grill", "schneller"), fill=WEISS, size=30, anker="m", bis="flamme"),
    szene(ficon("tabler", "flame", GRX, BODEN - 230, 200, "flamme", fuell=ORANGE), "015flamme*", 0.9, versatz=-0.1),
    pl("Stichflamme", GRX, 250, "flamme", fill=ORANGE, size=32, anker="m"),
    *fig("OT", OTG, BODEN, FH, [("grill", "ruhig"), ("flamme", "schreck")]),
    name("OT", OTG, "grill"),
    ring(OTG - 10, BODEN - FH * 0.62, 80, 55, "blase", farbe=DROT, breite=7),
    pl("Brandblase an der Hand", OTG, 260, beim("blase", "Brandblase"), fill=ROT, size=30, anker="m"),
])

# D Fall: Gerdas Hund -------------------------------------------------------------------------------------------------------
GEX, HU1, HU2, OTH = 400, 760, 1120, 1420
GER = ("GE_redet_r", GEX, BODEN - 20, SITZ)
OTR = ("OT_redet", OTH, BODEN, FH)
folie([("hund", "Fall · Gerdas Hund")], [
    *garten("hund", zaun=(1720,)),
    karte(GEX - 230, BODEN - 34, 460, 34, "hund", fill=PINK, rund=10, schatten=0, rand=4),        # Picknickdecke
    *fig("GE", GEX, BODEN - 20, SITZ, [("hund", "ruhig_r"), ("o1", "schaut_r")], bis="g1"),
    *redet("GE_redet_r", GEX, BODEN - 20, SITZ, "g1", "biss"),
    peep_voll("GE_boese_r", GEX, BODEN - 20, SITZ, "biss", anim="cut"),
    name("GE", GEX, "hund"),
    szene(ficon("fluent-emoji-high-contrast", "dog", HU1, BODEN - 2, 190, "hund", fuell=ORANGE, nebenfarbe=ORANGE,
                spiegeln=True, bis="biss"), "015hund*", 0.8, versatz=0.0),
    pl("knurrt", HU1 + 20, 620, beim("hund", "knurrt"), fill=WEISS, size=30, anker="m", bis="biss"),
    bewegt(ficon("fluent-emoji-high-contrast", "dog", HU2, BODEN - 2, 190, "biss", fuell=ORANGE, nebenfarbe=ORANGE,
                 spiegeln=True, anim="cut"), beim("biss", "Hund"), (beim("biss", "Hund")[0], beim("biss", "Hund")[1] + 0.5), HU1 - HU2, 0),
    *fig("OT", OTH, BODEN, FH, [("hund", "schreck")], bis="o1"),
    *redet("OT_redet", OTH, BODEN, FH, "o1", "g1"),
    *fig("OT", OTH, BODEN, FH, [("g1", "wuetend"), (beim("biss", "beißt"), "schreck")], erst="cut"),
    name("OT", OTH, "hund"),
    blase("sprech", 640, 170, "o1", 1060, 200, inhalt=["Gerda, ruf deinen", "Hund zurück!"], textsize=36, figur=OTR, bis="g1"),
    blase("sprech", 520, 150, "g1", 640, 330, inhalt=["Geschieht dir recht."], textsize=36, figur=GER, bis="biss"),
    pl("Gerda bleibt sitzen", GEX, 420, beim("biss", "sitzen"), fill=WEISS, size=30, anker="m"),
    ring(OTH - 20, BODEN - 70, 85, 60, beim("biss", "beißt"), farbe=DROT, breite=7),
    pl("Biss in die Wade", OTH - 30, 280, beim("biss", "Wade"), fill=ROT, size=30, anker="m"),
])

# E Fallfrage -------------------------------------------------------------------------------------------------------------------
FRAGEPOS = [("KO", 1330, 520, "ruhig"), ("IN", 1560, 520, "ruhig"), ("RU", 1790, 520, "ruhig"),
            ("BE", 1430, 960, "ruhig"), ("GE", 1700, 940, "ruhig")]
folie([("frage", "Fallfrage · Welches Schema für wen?")], [
    *tafel("frage", "Klausur · Strafrecht AT"),
    z("Bearbeitervermerk:", 110, 200, "frage", "Bold", 38),
    z("Wer hat sich wie strafbar gemacht?", 110, 260, beim("frage", "Wer"), size=38),
    pl("5 Personen", 110, 400, beim("fuenf", "Fünf"), fill=GELB, size=36),
    pl("jede braucht ein anderes Prüfungsschema", 110, 500, beim("fuenf", "jede"), fill=PINK, size=34),
    *[e for p, cx, unten, m in FRAGEPOS for e in
      fig(p, cx, unten, (SITZ * 300 // FH) if p == "GE" else 300, [("frage", m), (beim("fuenf", "jede"), "denkt")], d=0.1)],
    *[pl(NAMEN[p][0], cx, unten + 14, "frage", fill=NAMEN[p][1], size=24, anker="m", d=0.3) for p, cx, unten, m in FRAGEPOS],
])

# F Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Sommerfest in der Kleingartenanlage. Konrad liegt mit Otto im Streit um die Hecke. Er bittet Ina um ihren Hammer, um "
    "Ottos Blumentopf zu zerschlagen; Ina weiß das, hat selbst kein Interesse daran und reicht ihm den Hammer. Konrad "
    "zerschlägt den Topf. Rudolf will Ottos Rasenmäher mitnehmen und behalten, packt den Griff und zieht. Der Mäher ist "
    "angekettet, was Rudolf übersehen hat; Werkzeug hat er nicht. Er lässt den Mäher stehen.",
    "Bernd gießt Brennspiritus in die Grillglut, damit es schneller geht, und vertraut darauf, dass nichts passiert. Eine "
    "Stichflamme verursacht bei Otto eine Brandblase an der Hand. Gerdas Hund knurrt Otto an; Gerda sieht, dass er gleich "
    "zubeißt. Ein Ruf würde genügen, der Hund gehorcht ihr zuverlässig. Gerda bleibt sitzen, weil sie den Biss will. Der Hund "
    "beißt Otto in die Wade. Otto stellt gegen alle Strafantrag. (Frei erfundener Übungsfall.)",
], "Wer hat sich wie strafbar gemacht?")

# G Grundfall und vier Weichen ---------------------------------------------------------------------------------------------
GX, GY = 1330, [330, 470, 610, 750]
WEICHEN = [("w1", "1. allein oder mit anderen?", "mit anderen"), ("w2", "2. vollendet oder versucht?", "versucht"),
           ("w3", "3. Vorsatz oder Fahrlässigkeit?", "fahrlässig"), ("w4", "4. Tun oder Unterlassen?", "unterlassen")]
folie([("weichen", "Überblick › Grundfall"), ("vier", "Überblick › vier Weichen"),
       ("konv", "Überblick › Klausurkonvention, kein Gesetz")], [
    *tafel("weichen", "Grundfall und vier Weichen"),
    z("Grundfall:", 110, 190, "weichen", "Bold", 36),
    z("allein · vorsätzlich · aktives Tun · vollendet", 110, 245, beim("weichen", "allein"), size=36),
    z("Jede Abweichung stellt eine Weiche:", 110, 335, "vier", "Bold", 36),
    *[z(t, 150, 395 + 60 * i, c, size=36) for i, (c, t, _) in enumerate(WEICHEN)],
    pl("Klausurkonvention, kein Gesetz", 110, 670, beim("konv", "Schemata"), fill=PINK, size=32),
    z("Schemata ordnen, was die Paragrafen verlangen", 110, 760, beim("konv", "ordnen"), size=32, farbe=TEXT),
    # Gleisbild rechts: Grundfall oben, vier Abzweige
    pl("Grundfall", GX, 150, "weichen", fill=GELB, size=32, anker="m"),
    linienzug([(GX, 200), (GX, 880)], "weichen", breite=10, farbe=INK),
    *[pfeil(GX, GY[i], GX + 190, GY[i] + 60, c, breite=8, kopf=24, farbe=DROT) for i, (c, _, _) in enumerate(WEICHEN)],
    *[pl(lbl, GX + 200, GY[i] + 40, c, fill=WEISS, size=28) for i, (c, _, lbl) in enumerate(WEICHEN)],
])

# H A. Konrad: Grundschema --------------------------------------------------------------------------------------------------
PK = "A. Konrad, § 303 I StGB"
khx, khy = hand("KO_ruhig", 1560, FB, FR, -1)
folie([("konrad", "A. Konrad › Grundfall"), ("p303", PK), ("tb", f"{PK} › I. Tatbestand"),
       ("rw", f"{PK} › II. Rechtswidrigkeit"), ("schuld", f"{PK} › III. Schuld")], [
    *tafel("konrad", "A. Konrad · Grundschema"),
    z("Konrad ist der Grundfall", 110, 190, "konrad", "Bold", 36),
    z("Sachbeschädigung, § 303 I StGB", 110, 265, "p303", "Bold", 38),
    z("„Wer rechtswidrig eine fremde Sache beschädigt", 150, 325, "p303", size=30, farbe=TEXT),
    z("oder zerstört, …“", 170, 365, "p303", size=30, farbe=TEXT),
    z("I. Tatbestand", 110, 440, "tb", "Bold", 38),
    ok(175, 515, beim("tb", "objektiv"), gr=22), z("objektiv: fremde Sache zerstört", 215, 495, beim("tb", "objektiv"), size=34),
    ok(175, 575, beim("tb", "subjektiv"), gr=22), z("subjektiv: Wissen und Wollen", 215, 555, beim("tb", "subjektiv"), size=34),
    z("II. Rechtswidrigkeit", 110, 650, "rw", "Bold", 38), ok(560, 670, beim("schuld", "Beides"), gr=22),
    z("III. Schuld", 110, 720, "schuld", "Bold", 38), ok(380, 740, beim("schuld", "Beides"), gr=22),
    *fig("KO", 1560, FB, FR, [("konrad", "ruhig"), ("tb", "denkt"), (beim("schuld", "Beides"), "ertappt")]),
    name("KO", 1560, "konrad", unten=FB, size=28),
    gedreht(ficon("ph", "potted-plant", 1330, FB - 2, 110, "konrad", fuell=ORANGE, nebenfarbe=GRUEN, d=0.2), 100, 1330, FB - 2),
    ficon("tabler", "hammer", khx - 15, khy + 35, 80, "konrad", fuell=GRAU, nebenfarbe=ORANGE, spiegeln=True, d=0.3),
    pl("fremde Sache", 1330, 720, beim("tb", "fremde"), fill=WEISS, size=26, anker="m"),
])

# I B. Ina: Beteiligung ----------------------------------------------------------------------------------------------------
PI = "B. Ina"
P27 = ["§ 27 I: „Als Gehilfe wird bestraft, wer vorsätzlich", "einem anderen zu dessen vorsätzlich begangener",
       "rechtswidriger Tat Hilfe geleistet hat.“"]
folie([("ina", f"{PI} › 1. Weiche: allein oder mit anderen?"), ("tvt", f"{PI} › Täter vor Teilnehmer"),
       ("p27", f"{PI} › Beihilfe, § 27 I StGB"), ("mitt", f"{PI} › keine Mittäterin")], [
    *tafel("ina", "B. Ina · Beteiligung"),
    pl("1. Weiche: allein oder mit anderen?", 110, 175, "ina", fill=PINK, size=30),
    z("Ina hat nicht selbst zugeschlagen", 110, 250, beim("ina", "Ina"), "Bold", 34),
    fl_block(110, 305, 1040, 72, GELB, "tvt", [("erst der Täter, dann der Teilnehmer", "Bold", 34, INK)]),
    *[z(t, 110 + (20 if i else 0), 405 + 42 * i, "p27", size=30, farbe=TEXT) for i, t in enumerate(P27)],
    ok(135, 560, "haupt", gr=20), z("vorsätzliche rechtswidrige Haupttat: Konrad", 170, 543, "haupt", size=32),
    ok(135, 615, "hammer", gr=20), z("Hilfe geleistet: der Hammer", 170, 598, "hammer", size=32),
    ok(135, 670, "vorsatz", gr=20), z("Vorsatz: Konrads Tat und ihre Hilfe", 170, 653, "vorsatz", size=32),
    nein(135, 725, "mitt", gr=20), z("Mittäterin? Tat war allein Konrads Sache", 170, 708, "mitt", size=32),
    *plusminus("Beihilfe zur Sachbeschädigung, §§ 303 I, 27 I", 110, 785, beim("mitt", "Beihilfe"), True, size=32, stil="Bold"),
    *fig("KO", 1380, FB, FR, [("ina", "ruhig")]),
    name("KO", 1380, "ina", unten=FB, size=28),
    *fig("IN", 1720, FB, FR, [("ina", "ruhig"), ("vorsatz", "denkt"), ("mitt", "cool")]),
    name("IN", 1720, "ina", unten=FB, size=28),
    pl("1", 1380, 410, beim("tvt", "Täter"), fill=GELB, size=40, anker="m"),
    pl("2", 1720, 410, beim("tvt", "Teilnehmer"), fill=GELB, size=40, anker="m"),
    ficon("tabler", "hammer", 1550, 700, 80, "hammer", fuell=GRAU, nebenfarbe=ORANGE),
    pfeil(1610, 640, 1470, 640, "hammer", breite=7, kopf=24, farbe=INK),
])

# J1 C. Rudolf: Vorprüfung --------------------------------------------------------------------------------------------------
PR = "C. Rudolf"
RX, MX = 1400, 1640
def rudolf_rechts(cue, folge):
    return [*fig("RU", RX, FB, FR, folge), name("RU", RX, cue, unten=FB, size=28),
            ficon("tabler", "lawn-mower", MX, FB - 2, 190, cue, fuell=ROT, nebenfarbe=WEISS, d=0.2),
            gedreht(ficon("fluent-emoji-high-contrast", "chains", 0, 0, 50, cue, fuell=GRAU, nebenfarbe=GRAU, d=0.3), 90, MX + 130, FB - 40)]


folie([("rudolf2", f"{PR} › 2. Weiche: vollendet oder versucht?"), ("vorpr", f"{PR} › 0. Vorprüfung"),
       ("p242", f"{PR} › Vorprüfung › Strafbarkeit, § 242 II StGB")], [
    *tafel("rudolf2", "C. Rudolf · Versuch"),
    pl("2. Weiche: vollendet oder versucht?", 110, 175, "rudolf2", fill=PINK, size=30),
    z("Der Mäher steht noch da", 110, 255, beim("rudolf2", "Bei"), "Bold", 36),
    z("0. Vorprüfung", 110, 360, "vorpr", "Bold", 38),
    ok(175, 440, beim("vorpr", "nicht"), gr=22), z("Tat nicht vollendet", 215, 420, beim("vorpr", "nicht"), size=36),
    ok(175, 505, "p242", gr=22), z("Versuch strafbar: § 242 II StGB", 215, 485, "p242", size=36),
    z("„Der Versuch ist strafbar.“", 255, 545, beim("p242", "Paragraf"), size=30, farbe=TEXT),
    *rudolf_rechts("rudolf2", [("rudolf2", "ertappt"), ("p242", "denkt")]),
    pl("noch da", MX, 680, beim("rudolf2", "Mäher"), fill=WEISS, size=28, anker="m"),
])

# J2 C. Rudolf: Tatbestand und Rücktritt ----------------------------------------------------------------------------------------
P22 = ["§ 22: „… wer nach seiner Vorstellung von der Tat", "zur Verwirklichung des Tatbestandes unmittelbar ansetzt.“"]
folie([("entschl", f"{PR} › I. 1. Tatentschluss"), ("ansetz", f"{PR} › I. 2. unmittelbares Ansetzen, § 22 StGB"),
       ("ruecktr", f"{PR} › IV. Rücktritt, § 24 StGB")], [
    *tafel("entschl", "C. Rudolf · §§ 242 I, II, 22, 23 I StGB", size=42),
    z("I. Tatbestand", 110, 185, "entschl", "Bold", 38),
    ok(175, 265, beim("entschl", "Rudolf"), gr=22), z("1. Tatentschluss: wegnehmen und behalten", 215, 245, "entschl", size=34),
    z("2. unmittelbares Ansetzen, § 22 StGB", 215, 320, "ansetz", size=34),
    *[z(t, 255 + (20 if i else 0), 375 + 40 * i, "ansetz", size=28, farbe=TEXT) for i, t in enumerate(P22)],
    ok(175, 490, beim("ansetz", "gezogen"), gr=22), z("hat schon gezogen", 215, 470, beim("ansetz", "gezogen"), size=34),
    z("II. Rechtswidrigkeit, III. Schuld", 110, 570, beim("ruecktr", "Rechtswidrigkeit"), "Bold", 36),
    z("IV. Rücktritt, § 24 StGB", 110, 640, beim("ruecktr", "Rücktritt"), "Bold", 36),
    nein(175, 720, beim("ruecktr", "fehlgeschlagen"), gr=22),
    z("Versuch fehlgeschlagen: kein Rücktritt", 215, 700, beim("ruecktr", "fehlgeschlagen"), size=34),
    *plusminus("versuchter Diebstahl", 110, 790, beim("ruecktr", "fehlgeschlagen", ende=True), True, size=34, stil="Bold"),
    *rudolf_rechts("entschl", [("entschl", "gierig"), ("ansetz", "zieht"), ("ruecktr", "ertappt")]),
    ring(MX + 130, FB - 60, 65, 55, beim("ruecktr", "fehlgeschlagen"), farbe=DROT, breite=6),
])

# K1 D. Bernd: Vorsatz oder Fahrlässigkeit ------------------------------------------------------------------------------------
PB = "D. Bernd"
BX2, GX2 = 1430, 1730
def bernd_rechts(cue, folge):
    return [*fig("BE", BX2, FB, FR, folge), name("BE", BX2, cue, unten=FB, size=28),
            ficon("tabler", "grill", GX2, FB - 2, 170, cue, fuell=GRAU, nebenfarbe=WEISS, d=0.2),
            ficon("tabler", "flame", GX2, FB - 170, 110, cue, fuell=ORANGE, d=0.3)]


P15 = ["§ 15: „Strafbar ist nur vorsätzliches Handeln, wenn", "nicht das Gesetz fahrlässiges Handeln", "ausdrücklich mit Strafe bedroht.“"]
folie([("bernd", f"{PB} › 3. Weiche: Vorsatz oder Fahrlässigkeit?"), ("p15", f"{PB} › § 15 StGB"),
       ("p229", f"{PB} › fahrlässige Körperverletzung, § 229 StGB")], [
    *tafel("bernd", "D. Bernd · Fahrlässigkeit"),
    pl("3. Weiche: Vorsatz oder Fahrlässigkeit?", 110, 175, "bernd", fill=PINK, size=30),
    nein(135, 275, beim("bernd", "niemanden"), gr=22), z("Vorsatz? Bernd wollte niemanden verletzen", 175, 255, beim("bernd", "niemanden"), size=34),
    *[z(t, 110 + (20 if i else 0), 350 + 44 * i, "p15", size=32, farbe=TEXT) for i, t in enumerate(P15)],
    ok(135, 535, "p229", gr=22), z("ausdrücklich bestimmt in § 229 StGB:", 175, 515, "p229", size=34),
    z("„Wer durch Fahrlässigkeit die Körperverletzung", 215, 575, beim("p229", "fahrlässige"), size=30, farbe=TEXT),
    z("einer anderen Person verursacht, …“", 235, 615, beim("p229", "fahrlässige"), size=30, farbe=TEXT),
    *bernd_rechts("bernd", [("bernd", "ertappt"), ("p229", "denkt")]),
    pl("kein Vorsatz", BX2, 380, beim("bernd", "niemanden"), fill=WEISS, size=28, anker="m"),
])

# K2 D. Bernd: Tatbestand des Fahrlässigkeitsdelikts --------------------------------------------------------------------------
P229 = "D. Bernd, § 229 StGB"
folie([("erfolg", f"{P229} › I. Tatbestand"), ("sorg", f"{P229} › objektive Sorgfaltspflichtverletzung"),
       ("zurech", f"{P229} › Gefahr verwirklicht"), ("subj", f"{P229} › kein subjektiver Tatbestand")], [
    *tafel("erfolg", "D. Bernd · § 229 StGB"),
    z("I. Tatbestand", 110, 185, "erfolg", "Bold", 38),
    ok(175, 265, beim("erfolg", "Kausalität"), gr=22), z("Erfolg, Handlung, Kausalität", 215, 245, beim("erfolg", "Erfolg"), size=34),
    fl_block(110, 305, 1040, 125, GELB, "sorg", []),
    z("objektive Sorgfaltspflichtverletzung", 150, 322, "sorg", "Bold", 34),
    z("bei objektiver Vorhersehbarkeit", 150, 376, "sorg", "Bold", 34),
    ok(175, 470, "spiritus", gr=22), z("Spiritus in Glut: bekannt gefährlich", 215, 450, "spiritus", size=34),
    ok(175, 535, "zurech", gr=22), z("genau diese Gefahr hat sich verwirklicht", 215, 515, "zurech", size=34),
    nein(175, 610, beim("subj", "keinen"), gr=22), z("kein subjektiver Tatbestand (üblicher Aufbau)", 215, 590, beim("subj", "keinen"), size=32),
    z("III. Schuld: Konnte Bernd die Gefahr", 110, 680, beim("subj", "Schuld"), "Bold", 34),
    z("persönlich erkennen?", 150, 730, beim("subj", "Schuld"), "Bold", 34),
    *bernd_rechts("erfolg", [("erfolg", "denkt"), ("sorg", "ertappt"), ("subj", "denkt")]),
    ring(GX2, FB - 225, 80, 75, "zurech", farbe=DROT, breite=6),
    pl("Brandblase", GX2, 560, beim("zurech", "Brandblase"), fill=ROT, size=28, anker="m"),
])

# L1 E. Gerda: Tun oder Unterlassen ------------------------------------------------------------------------------------------
PG = "E. Gerda"
GEX2, HUX = 1430, 1720
def gerda_rechts(cue, folge):
    return [*fig("GE", GEX2, FB, SITZ * FR // FH, folge), name("GE", GEX2, cue, unten=FB, size=28),
            ficon("fluent-emoji-high-contrast", "dog", HUX, FB - 2, 170, cue, fuell=ORANGE, nebenfarbe=ORANGE, d=0.2)]


P13 = ["§ 13 I: „Wer es unterläßt, einen Erfolg abzuwenden, …,", "ist … nur dann strafbar, wenn er rechtlich dafür",
       "einzustehen hat, daß der Erfolg nicht eintritt, …“"]
folie([("gerda", f"{PG} › 4. Weiche: Tun oder Unterlassen?"), ("p13", f"{PG} › § 13 I StGB")], [
    *tafel("gerda", "E. Gerda · Unterlassen"),
    pl("4. Weiche: Tun oder Unterlassen?", 110, 175, "gerda", fill=PINK, size=30),
    z("Gerda hat nichts getan:", 110, 255, beim("gerda", "Gerda"), "Bold", 36),
    z("Hund nicht zurückgerufen", 150, 310, beim("gerda", "sie"), size=36),
    *[z(t, 110 + (20 if i else 0), 410 + 46 * i, "p13", size=32, farbe=TEXT) for i, t in enumerate(P13)],
    pl("rechtlich einstehen?", 110, 600, beim("p13", "rechtlich"), fill=GELB, size=32),
    *gerda_rechts("gerda", [("gerda", "ruhig"), ("p13", "denkt")]),
    pl("nicht gerufen", 1580, 420, beim("gerda", "sie"), fill=WEISS, size=28, anker="m"),
])

# L2 E. Gerda: Tatbestand des Unterlassungsdelikts --------------------------------------------------------------------------
PG2 = "E. Gerda, §§ 223 I, 13 I StGB"
folie([("biss2", f"{PG2} › I. Tatbestand › Erfolg"), ("rufen", f"{PG2} › Handlung möglich"),
       ("quasi", f"{PG2} › Hund hätte gehorcht"), ("garant", f"{PG2} › Garantenstellung"),
       ("entspr", f"{PG2} › Entsprechung"), ("gvors", f"{PG2} › Vorsatz")], [
    *tafel("biss2", "E. Gerda · §§ 223 I, 13 I StGB"),
    z("I. Tatbestand", 110, 185, "biss2", "Bold", 38),
    ok(175, 265, beim("biss2", "Biss"), gr=22), z("Erfolg: Biss ist eine Körperverletzung", 215, 245, beim("biss2", "Biss"), size=34),
    ok(175, 330, "rufen", gr=22), z("Gerda hätte rufen können", 215, 310, "rufen", size=34),
    ok(175, 395, "quasi", gr=22), z("der Hund hätte gehorcht", 215, 375, "quasi", size=34),
    ok(175, 460, beim("garant", "Garantenstellung"), gr=22), z("Garantenstellung: Halterin überwacht", 215, 440, "garant", size=34),
    z("ihren Hund", 255, 490, "garant", size=34),
    ok(175, 570, beim("entspr", "Tun"), gr=22), z("Entsprechung: bei Körperverletzung", 215, 550, "entspr", size=34),
    z("ohne Weiteres", 255, 600, "entspr", size=34),
    ok(175, 680, "gvors", gr=22), z("Vorsatz: Gerda wollte den Biss", 215, 660, "gvors", size=34),
    *plusminus("Körperverletzung durch Unterlassen", 110, 760, beim("gvors", "Körperverletzung"), True, size=36, stil="Bold"),
    *gerda_rechts("biss2", [("biss2", "denkt"), ("gvors", "ertappt")]),
    ring(HUX, FB - 80, 115, 80, "garant", farbe=ORANGE, breite=6),
    pl("Halterin", HUX, 640, "garant", fill=GELB, size=28, anker="m"),
])

# M Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Weichen kombinieren")], [
    *tafel("tipp", "Klausurtipp", fill=HELL, size=50),
    warnung_i(150, 225, "tipp", gr=26),
    z("Die Weichen lassen sich kombinieren", 200, 200, beim("tipp", "Die"), "Bold", 36),
    z("Gerda übersieht den Hund,", 150, 320, "tipp2", size=36),
    z("obwohl sie aufpassen musste:", 150, 375, beim("tipp2", "obwohl"), size=36),
    z("3. Weiche: fahrlässig", 190, 470, beim("tipp2", "fahrlässige"), "Bold", 34),
    z("4. Weiche: Unterlassen", 190, 530, beim("tipp2", "Unterlassen"), "Bold", 34),
    fl_block(150, 610, 1000, 130, GELB, beim("tipp2", "Unterlassen", ende=True), []),
    z("fahrlässige Körperverletzung durch Unterlassen", 190, 630, beim("tipp2", "Unterlassen", ende=True), "Bold", 34),
    z("§§ 229, 13 I StGB", 190, 685, beim("tipp2", "Unterlassen", ende=True), "Bold", 32),
    *redet("LX_warnt", LXX, FB, 560, "tipp", "sch"),
    pl("Lexi", LXX, FB + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema: Entscheidungsbaum ------------------------------------------------------------------------------------------
QX, QW, AX, AW = 110, 500, 760, 1050
RY = [175, 325, 475, 625, 775]
BAUM = [("e1", "1. Mehrere beteiligt?", "Täter vor Teilnehmer, §§ 25 bis 27 StGB", None),
        ("e2", "2. Nur versucht?", "0. Vorprüfung · I. 1. Tatentschluss,", "2. unmittelbares Ansetzen, §§ 22, 23 I"),
        ("e3", "3. Fahrlässig?", "nur bei ausdrücklicher Strafdrohung, § 15;", "objektive Sorgfaltspflichtverletzung"),
        ("e4", "4. Unterlassen?", "§ 13 I mit Garantenstellung", None),
        ("e5", "Keine Weiche?", "Grundschema: I. Tatbestand ·", "II. Rechtswidrigkeit · III. Schuld")]
baum = []
for i, (c, q, a1, a2) in enumerate(BAUM):
    baum.append(fl_block(QX, RY[i], QW, 100, PINK if c != "e5" else GELB, c, [(glyphen(q), "Bold", 34, INK)]))
    an = beim(c, "Dann")
    baum.append(pfeil(QX + QW + 10, RY[i] + 50, AX - 10, RY[i] + 50, an, breite=7, kopf=22, farbe=INK))
    if c != "e5":
        baum.append(T("ja", QX + QW + 70, RY[i] + 5, an, "Bold", 26, farbe=DGRUEN, anim="fade"))
    oy = 0 if a2 is None else 12
    baum.append(fl_block(AX, RY[i] - oy, AW, 100 if a2 is None else 125, WEISS, an, []))
    if a2 is None:
        baum.append(z(a1, AX + 40, RY[i] + 34, an, "Bold", 32, rechts=1820))
    else:
        baum.append(z(a1, AX + 40, RY[i] + 6, an, size=32, rechts=1820))
        baum.append(z(a2, AX + 40, RY[i] + 56, an, size=32, rechts=1820))
    if i + 1 < len(BAUM):
        nxt = BAUM[i + 1][0]
        baum.append(pfeil(QX + 60, RY[i] + 104, QX + 60, RY[i + 1] - 6, nxt, breite=6, kopf=18, farbe=INK))
        baum.append(T("nein", QX + 80, RY[i] + 104, nxt, "Bold", 24, farbe=DROT, anim="fade"))
folie([("sch", "Klausurschema · Entscheidungsbaum")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Entscheidungsbaum", 110, 90, "sch", 52),
    *baum,
])

# O Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Das Gerüst bleibt immer gleich:", 0)],
                 [("Tatbestand", "a"), (", ", 0), ("Rechtswidrigkeit", "b"), (", ", 0), ("Schuld", "c")]],
                750, 320, 50, "merke", {"a": beim("merke", "Tatbestand"), "b": beim("merke", "Rechtswidrigkeit"),
                                        "c": beim("merke", "Schuld")}),
    *markertext([[("Die Weichen verändern", 0)], [("vor allem den ", 0), ("Tatbestand", "d"), (".", 0)]],
                750, 560, 50, "m2", {"d": beim("m2", "Tatbestand")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
