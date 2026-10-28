"""Jauchegrubenfall – Open-Peeps-Stil, Pinselblasen, Figurenrede mit eigenen Stimmen und Mundbewegung."""
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_ja/"
FOLIEN = bausteine.FOLIEN
BODEN = 870
FH = 470
TITEL = "Streit am Gartenzaun"
FX, GX, JX = 470, 1180, 1640
LIEGT = Image.open(FIG + "op_ja/GI_liegt.png")
LH = int(FH * LIEGT.height / LIEGT.width)


def liegend(cx, cue, bis=None, **k):
    return bild(FIG + "op_ja/GI_liegt.png", cx, BODEN - 4, LH, cue, anim="cut", bis=bis, **k)


# 1 Fall ------------------------------------------------------------------------------------------------------------------
folie([("fall", "Fall")], [
    titel(TITEL, 80, 55, "fall", 70),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    ficon("tabler", "fence", 830, BODEN - 2, 190, "fall", fuell=None, d=0.3),
    # Frank
    peep_voll("FR_ruhig", FX, BODEN, FH, "fall", bis="f1"),
    *spricht("FR_droht_auf", "FR_droht_zu", FX, BODEN, FH, "f1", "wuergen"),
    peep_voll("FR_wut", FX, BODEN, FH, "wuergen", anim="cut", bis="f2"),
    *spricht("FR_erschrocken_auf", "FR_erschrocken_zu", FX, BODEN, FH, "f2", "grube"),
    peep_voll("FR_erschrocken_zu", FX, BODEN, FH, "grube", anim="cut"),
    pille("Frank", FX, BODEN + 18, "fall", fill=ROT, size=30, anker="m", d=0.2),
    # Gisela
    peep_voll("GI_ruhig", GX, BODEN, FH, "fall", d=0.2, bis="streit"),
    peep_voll("GI_sauer_zu", GX, BODEN, FH, "streit", anim="cut", bis="g1"),
    *spricht("GI_sauer_auf", "GI_sauer_zu", GX, BODEN, FH, "g1", "f1"),
    peep_voll("GI_angst", GX, BODEN, FH, "f1", anim="cut", bis="tot"),
    liegend(GX, "tot", bis="grube"),
    bewegt(liegend(JX, "grube", bis="ertrinkt"), ("grube", 2.2), ("grube", 3.6), GX - JX),
    pille("Gisela", GX, BODEN + 18, "fall", fill=TUERKIS, size=30, anker="m", d=0.4, bis="grube"),
    # Sprechblasen
    blase("sprech", 520, 190, "g1", 1400, 250, inhalt=["Dein Zaun steht auf", "meinem Grundstück!"], textsize=34,
          figur=("GI_sauer_auf", GX, BODEN, FH), bis="f1"),
    blase("sprech", 440, 170, "f1", 330, 250, inhalt=["Das wagst du nicht!"], textsize=38,
          figur=("FR_droht_auf", FX, BODEN, FH), bis="wuergen"),
    blase("sprech", 470, 190, "f2", 330, 250, inhalt=["Sie atmet nicht mehr …", "Sie muss verschwinden."], textsize=32,
          figur=("FR_erschrocken_auf", FX, BODEN, FH), bis="grube"),
    # Akte und Jauchegrube
    pille("1. Akt: Würgen – mit Tötungsvorsatz", 830, 200, "wuergen", fill=ORANGE, size=32, anker="m", d=0.3, bis="f2"),
    pille("nur bewusstlos!", GX, 600, "lebt", fill=GELB, size=32, anker="m", bis="grube"),
    icon("fluent-emoji-high-contrast", "hole", JX, BODEN - 48, 200, "grube", farbe="#151515"),
    pille("Jauchegrube", JX, BODEN + 18, "grube", fill=WEISS, size=30, anker="m", d=0.2),
    pille("2. Akt: Versenken – hält sie für tot", 1100, 200, "grube", fill=BLAU, size=32, anker="m", d=0.4),
    pille("Gisela ertrinkt", JX, 690, "ertrinkt", fill=ROT, size=32, anker="m"),
    pille("Vollendeter Totschlag?", 960, 960, "frage", fill=PINK, size=38, anker="m"),
])

# 2 Sachverhalt ------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Frank und Gisela sind Nachbarn. Bei einem Streit am Gartenzaun gerät Frank in Wut. Er will Gisela töten und würgt sie, "
    "bis sie reglos zusammensackt.",
    "Frank hält Gisela für tot. Tatsächlich ist sie nur bewusstlos. Um die vermeintliche Leiche zu beseitigen, wirft er sie "
    "in eine Jauchegrube. Dort ertrinkt Gisela.",
    "(Nach BGHSt 14, 193 – Jauchegrubenfall.)",
], "Hat sich Frank wegen vollendeten Totschlags strafbar gemacht?")

# 3 Objektiver Tatbestand -----------------------------------------------------------------------------------------------------
X0, X1, X2 = 170, 230, 290
folie([("schema", "§ 212 StGB › Objektiver Tatbestand")], [
    karte(100, 70, 1300, 860, "schema"),
    titel("§ 212 StGB: Objektiver Tatbestand", X0, 120, "schema", 56),
    ok(X1 + 20, 262, "erfolg", gr=26), zeile("Erfolg: Tod der Gisela", X1 + 60, 240, "erfolg", "Bold", 40),
    ok(X1 + 20, 362, "kaus", gr=26), zeile("Kausalität des Würgens", X1 + 60, 340, "kaus", "Bold", 40),
    zeile("ohne Würgen kein Versenken (conditio sine qua non)", X1 + 60, 397, "kaus", size=36, farbe=TEXT, d=1.2),
    ok(X1 + 20, 492, "zurech", gr=26), zeile("objektive Zurechnung", X1 + 60, 470, "zurech", "Bold", 40),
    zeile("Beseitigen der „Leiche“ ist nicht lebensfremd", X1 + 60, 527, "zurech", size=36, farbe=TEXT, d=1.2),
    pille("Objektiver Tatbestand erfüllt", X1, 640, "zurech", fill=GRUEN, size=40, d=3.0),
    peep_voll("FR_ruhig", 1650, BODEN, 560, "schema", d=0.3),
])

# 4 Subjektiver Tatbestand: zwei Akte ------------------------------------------------------------------------------------------
folie([("vorsatz", "§ 212 StGB › Vorsatz")], [
    titel("Das Problem: zwei Akte", 960, 55, "vorsatz", 70, anker="m"),
    fl_block(140, 200, 740, 150, ORANGE, "akt1", [("1. Akt: Würgen", "ExtraBold", 48, INK)]),
    ok(200, 440, "akt1", gr=26, d=0.8), zeile("mit Tötungsvorsatz", 245, 418, "akt1", "Bold", 40, d=0.8),
    nein(200, 520, "akt1", gr=24), zeile("nicht todesursächlich", 245, 498, "akt1", "Bold", 40, d=2.6),
    pfeil_ink(900, 275, 1020, 275, "akt2"),
    fl_block(1040, 200, 740, 150, BLAU, "akt2", [("2. Akt: Versenken", "ExtraBold", 48, INK)], d=0.2),
    ok(1100, 440, "akt2", gr=26, d=0.8), zeile("todesursächlich", 1145, 418, "akt2", "Bold", 40, d=0.8),
    nein(1100, 520, "akt2", gr=24), zeile("ohne Vorsatz: „schon tot“", 1145, 498, "akt2", "Bold", 40, d=2.8),
    pille("Wie ist das zweiaktige Geschehen zu bewerten?", 960, 680, "frage2", fill=PINK, size=40, anker="m"),
])

# 5 Die Ansichten --------------------------------------------------------------------------------------------------------------
def karte4(x, y, cue, titel_, zeilen, fazit, plus, fcue):
    els = [karte(x, y, 860, 380, cue), zeile(titel_, x + 45, y + 40, cue, "ExtraBold", 44)]
    yy = y + 120
    for z, c, d in zeilen:
        els.append(zeile(z, x + 45, yy, c, size=34, farbe=TEXT, d=d)); yy += 50
    els += [(ok if plus else nein)(x + 70, y + 322, fcue, gr=24), zeile(fazit, x + 110, y + 300, fcue, "Bold", 36)]
    return els

folie([("dg", "§ 212 StGB › Vorsatz › Ansichten")], [
    *karte4(70, 70, "dg", "dolus generalis", [("Gesamtvorsatz für beide Akte", "dg", 0.8)],
            "heute abgelehnt: Vorsatz bei Tathandlung", False, "dg2"),
    *karte4(990, 70, "tr", "Trennungstheorie", [("Akt 1: versuchter Totschlag", "tr2", 0.0), ("Akt 2: fahrlässige Tötung, § 222", "tr2", 1.8)],
            "keine Vollendung", False, ("tr2", 3.0)),
    *karte4(70, 520, "rspr", "BGH und h. L.", [("Irrtum über den Kausalverlauf", "rspr", 1.0), ("unwesentlich, wenn voraussehbar", "rspr2", 0.0),
                                              ("und keine andere Bewertung", "rspr2", 3.0)],
            "vollendeter Totschlag", True, "rspr3"),
    *karte4(990, 520, "roxin", "Roxin: Planverwirklichung", [("1. Akt mit Tötungsabsicht?", "roxin2", 0.0), ("Frank wollte töten", "roxin2", 3.0)],
            "vollendeter Totschlag", True, ("roxin2", 4.5)),
])

# 6 Ergebnis + Klausurtipp -----------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis")], [
    titel("Ergebnis", 960, 55, "erg", 74, anker="m"),
    fl_block(360, 180, 1200, 150, GRUEN, "erg", [("Frank: vollendeter Totschlag, § 212 StGB", "ExtraBold", 44, INK),
                                                 ("unwesentliche Abweichung vom Kausalverlauf", "Regular", 36, INK)]),
    zeile("Mordmerkmale nicht ersichtlich", 960, 380, "mord", size=38, farbe=TEXT, anker="m"),
    warnung_i(250, 540, "tipp", gr=30),
    zeile("Klausurtipp: Problem im subjektiven Tatbestand", 300, 515, "tipp", "ExtraBold", 40, farbe=DROT),
    zeile("Vorsatz bezüglich des Kausalverlaufs", 300, 590, "tipp", size=38, d=2.5),
    zeile("die Kausalität selbst ist unproblematisch", 300, 660, "tipp2", size=38),
    peep_voll("ER_erklaert", 1690, BODEN, 440, "tipp"),
])

# 7 Klausurschema --------------------------------------------------------------------------------------------------------------
K0, K1, K2 = 250, 310, 380
folie([("sch", "Klausurschema")], [
    karte(180, 50, 1560, 920, "sch"),
    titel("Klausurschema: § 212 StGB (zweiaktig)", K0, 95, "sch", 56),
    zeile("I. Objektiver Tatbestand", K1, 210, "k1", "Bold", 40),
    zeile("Erfolg, Kausalität, objektive Zurechnung", K2, 270, "k1", size=36, farbe=TEXT, d=0.8),
    zeile("II. Subjektiver Tatbestand", K1, 360, "k2", "Bold", 40),
    zeile("Vorsatz, auch bezüglich des Kausalverlaufs", K2, 420, "k2", size=36, farbe=TEXT, d=0.8),
    zeile("Streit: dolus generalis · Trennung · BGH/h. L. · Roxin", K2, 475, "k3", size=36, farbe=TEXT),
    zeile("III. Rechtswidrigkeit   IV. Schuld", K1, 565, "k4", "Bold", 40),
    pille("Ergebnis: vollendeter Totschlag", K1, 660, "k4", fill=GRUEN, size=38, d=1.5),
])

# 8 Merksatz --------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=(255, 251, 230, 255)),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Jauchegrubenfall:", "a")], [("Abweichung vom Kausalverlauf", 0)], [("ist ", 0), ("unwesentlich", "b"), (".", 0)]],
                750, 320, 50, "merke", {"a": ("merke", 0.5), "b": ("merke", 4.0)}),
    *markertext([[("Der Täter ist wegen", 0)], [("vollendeter", "c"), (" Tat strafbar.", 0)]],
                750, 590, 50, "m2", {"c": ("m2", 1.0)}),
    peep_voll("ER_freut", 1680, 1000, 720, "merke", d=0.4),
])
