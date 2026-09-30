"""Grundschema Bilanzierung nach Handels- und Steuerrecht – Open-Peeps-Stil, Pinselblasen (E)."""
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_bi/"
FOLIEN = bausteine.FOLIEN
BODEN = 870
FH = 470
TITEL = "Die neue Maschine"


def maschine(cx, unten, breite, cue, fuell=GELB, **k):
    """Maschine: MDI robot-industrial-outline (Apache 2.0), mit Palettenfarbe gefüllt."""
    return ficon("mdi", "robot-industrial-outline", cx, unten, breite, cue, fuell=fuell, **k)


# 1 Fall ----------------------------------------------------------------------------------------------------------------
LX, MA, VX = 360, 820, 1540
folie([("fall", "Fall")], [
    titel(TITEL, 80, 55, "fall", 70),
    pille("e. K., Fertigungsbetrieb, Millionenumsatz", 80, 150, "fall", fill=WEISS, size=30, d=0.5, bis="wert"),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    *figuren([("LE_ruhig", "fall"), ("LE_froh", "kauf"), ("LE_zeigt", "nd"), ("LE_besorgt", "wert")], LX, BODEN, FH),
    pille("Lena", LX, BODEN + 18, "fall", fill=PINK, size=30, anker="m", d=0.2),
    maschine(MA, BODEN - 4, 270, "kauf"),
    pille("Maschine", MA, BODEN + 18, "kauf", fill=WEISS, size=30, anker="m", d=0.3),
    # Verkäufer, Preis, Nebenkosten (bis zur Nutzungsdauer)
    peep_voll("MX_redet", VX, BODEN, FH, "kauf", d=0.2, bis="nd"),
    pille("Verkäufer", VX, BODEN + 18, "kauf", fill=GRUEN, size=30, anker="m", d=0.4, bis="nd"),
    blase("sprech", 380, 170, "kauf", 1560, 250, inhalt=["Macht 50.000 €!"], textsize=38,
          figur=("MX_redet", VX, BODEN, FH), d=0.6, bis="nd"),
    ficon("ph", "truck", 1150, 700, 170, "neben", fuell=BLAU, bis="nd"),
    pille("Transport + Montage: 2.000 €", 1150, 720, "neben", fill=WEISS, size=30, anker="m", d=0.3, bis="nd"),
    # Nutzungsdauer, neues Modell, Wertverlust
    ficon("tabler", "calendar", 1180, 290, 120, "nd", fuell=GELB),
    pille("Nutzungsdauer: 10 Jahre", 1180, 305, "nd", fill=WEISS, size=30, anker="m", d=0.3),
    maschine(1560, BODEN - 4, 230, "modell", fuell=GRUEN),
    icon("fluent-emoji-high-contrast", "new-button", 1660, 560, 90, "modell", farbe="#151515", d=0.3),
    pille("neues Modell", 1560, BODEN + 18, "modell", fill=GRUEN, size=30, anker="m", d=0.3),
    ficon("ph", "chart-line-down", 1180, 505, 110, "wert", fuell=None),
    pille("31.12.: nur noch 30.000 € (dauerhaft)", 1180, 522, "wert", fill=ROT, size=30, anker="m", d=0.3),
    blase("denk", 440, 200, "wert", 330, 250, inhalt=["Was steht jetzt", "in der Bilanz?"], textsize=34,
          figur=("LE_besorgt", LX, BODEN, FH), d=0.6),
    pille("Welcher Wert in Handels- und Steuerbilanz?", 960, 960, "frage", fill=PINK, size=36, anker="m"),
])

# 2 Sachverhalt ----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Lena betreibt als eingetragene Kauffrau einen Fertigungsbetrieb mit mehreren Millionen Euro Umsatz.",
    "Am 2. Januar kauft sie eine neue Maschine für 50.000 € (netto). Für Transport und Montage zahlt sie weitere 2.000 €. "
    "Die Maschine soll zehn Jahre genutzt werden.",
    "Im Herbst kommt ein deutlich besseres Modell auf den Markt. Am 31. Dezember ist Lenas Maschine voraussichtlich "
    "dauerhaft nur noch 30.000 € wert.",
], "Mit welchem Wert steht die Maschine in Handels- und Steuerbilanz?")

# 3 Grundschema + Maßgeblichkeit -----------------------------------------------------------------------------------------
folie([("schema", "Grundschema")], [
    titel("Das Grundschema", 960, 50, "schema", 70, anker="m"),
    fl_block(100, 180, 520, 170, BLAU, "g1", [("1. Pflicht", "ExtraBold", 48, INK), ("Wer bilanziert?", "Regular", 38, INK)]),
    pfeil_ink(630, 265, 690, 265, "g2"),
    fl_block(700, 180, 520, 170, GELB, "g2", [("2. Ansatz", "ExtraBold", 48, INK), ("Ob in die Bilanz?", "Regular", 38, INK)], d=0.2),
    pfeil_ink(1230, 265, 1290, 265, "g3"),
    fl_block(1300, 180, 520, 170, GRUEN, "g3", [("3. Bewertung", "ExtraBold", 48, INK), ("Mit welchem Wert?", "Regular", 38, INK)], d=0.2),
    fl_block(300, 470, 460, 140, WEISS, "mg", [("Handelsbilanz", "ExtraBold", 46, INK), ("HGB", "Regular", 36, TEXT)]),
    pfeil_ink(780, 540, 1140, 540, "mg", d=0.4),
    fl_block(1160, 470, 460, 140, WEISS, "mg", [("Steuerbilanz", "ExtraBold", 46, INK), ("EStG", "Regular", 36, TEXT)], d=0.6),
    pille("Maßgeblichkeit, § 5 I 1 EStG", 960, 650, "mg", fill=GELB, size=36, anker="m", d=1.0),
    warnung_i(560, 800, "vorb", gr=30),
    zeile("Vorbehalt: Steuergesetz oder steuerliches Wahlrecht", 610, 776, "vorb", "Bold", 38, farbe=DROT),
])

# 4 I. Bilanzierungspflicht ------------------------------------------------------------------------------------------------
X0, X1, X2 = 170, 230, 290
folie([("wer", "I. Bilanzierungspflicht")], [
    karte(100, 70, 1300, 860, "wer"),
    titel("I. Wer muss bilanzieren?", X0, 120, "wer", 58),
    ok(X1 + 20, 262, "wer", gr=26), zeile("Kauffrau, keine Befreiung nach § 241a HGB", X1 + 60, 240, "wer", "Bold", 40, d=0.3),
    ok(X1 + 20, 362, "wer1", gr=26), zeile("Buchführungspflicht, § 238 I HGB", X1 + 60, 340, "wer1", "Bold", 40),
    zeile("Jahresabschluss mit Bilanz, § 242 HGB", X1 + 60, 397, "wer1", size=36, farbe=TEXT, d=0.8),
    ok(X1 + 20, 492, "wer2", gr=26), zeile("steuerlich: § 140 AO", X1 + 60, 470, "wer2", "Bold", 40),
    zeile("Gewinn durch Betriebsvermögensvergleich, § 5 I EStG", X1 + 60, 527, "wer2", size=36, farbe=TEXT, d=0.8),
    pille("Lena muss bilanzieren", X1, 640, "wer2", fill=GRUEN, size=40, d=2.2),
    peep_voll("LE_nachdenklich", 1650, BODEN, 560, "wer", d=0.3),
])

# 5 II. Ansatz ------------------------------------------------------------------------------------------------------------------
folie([("ansatz", "II. Ansatz")], [
    karte(100, 60, 1300, 900, "ansatz"),
    titel("II. Ansatz: Kommt sie in die Bilanz?", X0, 105, "ansatz", 54),
    ok(X1 + 20, 232, "vg", gr=26), zeile("Vermögensgegenstand / Wirtschaftsgut", X1 + 60, 210, "vg", "Bold", 40),
    zeile("selbständig bewertbar, Nutzen über den Stichtag", X1 + 60, 265, "vg", size=36, farbe=TEXT, d=0.6),
    ok(X1 + 20, 352, "zur", gr=26), zeile("persönlich zurechenbar: Eigentum der Lena", X1 + 60, 330, "zur", "Bold", 40),
    ok(X1 + 20, 432, "zur", gr=26, d=1.6), zeile("sachlich: notwendiges Betriebsvermögen", X1 + 60, 410, "zur", "Bold", 40, d=1.6),
    ok(X1 + 20, 512, "verbot", gr=26), zeile("kein Ansatzverbot", X1 + 60, 490, "verbot", "Bold", 40),
    pille("Aktivierungspflicht: § 246 I HGB, § 5 I EStG", X1, 600, "pflicht", fill=GRUEN, size=38),
    pille("Anlagevermögen, § 247 II HGB", X1, 700, "av", fill=BLAU, size=38),
    zeile("dient dem Betrieb dauernd", X1 + 30, 790, "av", size=36, farbe=TEXT, d=0.8),
    maschine(1650, 760, 300, "ansatz", d=0.3),
    pille("Maschine", 1650, 780, "ansatz", fill=WEISS, size=32, anker="m", d=0.5),
])

# 6 III. Bewertung: Zugang und planmäßige AfA ---------------------------------------------------------------------------------
R = 1200   # rechte Kante der Beträge
folie([("bew", "III. Bewertung")], [
    karte(100, 60, 1300, 900, "bew"),
    titel("III. Bewertung", X0, 105, "bew", 58),
    zeile("Zugang: Anschaffungskosten", X1, 215, "zugang", "Bold", 42),
    zeile("§ 255 I HGB · § 6 I Nr. 1 EStG", X1, 275, "zugang", size=36, farbe=TEXT, d=0.5),
    zeile("Kaufpreis", X1, 370, "ak", size=40), zeile("50.000 €", R, 370, "ak", size=40, anker="r"),
    zeile("+ Transport und Montage", X1, 430, "ak", size=40, d=1.2), zeile("2.000 €", R, 430, "ak", size=40, anker="r", d=1.2),
    linienzug([(X1, 495), (R, 495)], "ak", breite=4, farbe=INK, d=2.2),
    zeile("= Anschaffungskosten", X1, 515, "ak", "Bold", 40, d=2.4), zeile("52.000 €", R, 515, "ak", "Bold", 40, anker="r", d=2.4),
    zeile("− planmäßige AfA, 10 Jahre", X1, 600, "afa", size=40), zeile("5.200 €", R, 600, "afa", size=40, anker="r"),
    zeile("§ 253 III 1 HGB · § 7 I EStG", X1 + 30, 655, "afa", size=34, farbe=TEXT, d=0.6),
    linienzug([(X1, 720), (R, 720)], "fak", breite=4, farbe=INK),
    zeile("= fortgeführte AK am 31.12.", X1, 740, "fak", "Bold", 40, d=0.2),
    pille("46.800 €", R, 725, "fak", fill=GELB, size=40, anker="r", d=0.4),
    peep_voll("LE_zeigt", 1640, BODEN, 560, "bew", d=0.3),
])

# 7 Außerplanmäßig: Handels- vs. Steuerbilanz ------------------------------------------------------------------------------------
folie([("apl", "III. Bewertung › Wertminderung")], [
    titel("Wertminderung auf 30.000 €", 960, 50, "apl", 64, anker="m"),
    zeile("voraussichtlich dauernd", 960, 150, "apl", "Bold", 38, farbe=TEXT, anker="m", d=0.5),
    karte(90, 220, 820, 700, "hgb"),
    karte(1010, 220, 820, 700, "estg"),
    zeile("Handelsbilanz", 140, 265, "hgb", "ExtraBold", 50),
    zeile("§ 253 III 5 HGB", 140, 350, "hgb", "Bold", 38),
    zeile("Pflicht zur außerplanmäßigen", 140, 410, "hgb", size=38),
    zeile("Abschreibung (Anlagevermögen)", 140, 460, "hgb", size=38),
    pille("30.000 €", 140, 560, "hb", fill=GRUEN, size=48),
    zeile("Steuerbilanz", 1060, 265, "estg", "ExtraBold", 50),
    zeile("§ 6 I Nr. 1 S. 2 EStG", 1060, 350, "estg", "Bold", 38),
    zeile("niedrigerer Teilwert „kann“", 1060, 410, "estg", size=38),
    zeile("angesetzt werden", 1060, 460, "estg", size=38),
    pille("eigenes steuerliches Wahlrecht", 1060, 530, "wahl", fill=BLAU, size=34),
    pille("30.000 € oder 46.800 €", 1060, 630, "sb", fill=GELB, size=46),
    zeile("bei Abweichung: Verzeichnis, § 5 I 2 EStG", 1060, 760, "verz", size=34, farbe=TEXT),
])

# 8 Klausurtipp ------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp")], [
    titel("Klausurtipp", 960, 55, "tipp", 74, anker="m"),
    fl_block(200, 230, 560, 160, WEISS, "tipp", [("1. Handelsbilanz", "ExtraBold", 46, INK), ("GoB, HGB", "Regular", 36, TEXT)]),
    pfeil_ink(780, 310, 900, 310, "tipp2"),
    fl_block(920, 230, 560, 160, GELB, "tipp2", [("2. Abweichungen?", "ExtraBold", 46, INK), ("EStG-Sonderregeln, Wahlrechte", "Regular", 34, INK)], d=0.2),
    warnung_i(250, 520, "tipp2", gr=30, d=1.0),
    zeile("Nicht mit dem Steuerrecht anfangen!", 300, 495, "tipp2", "ExtraBold", 40, farbe=DROT, d=1.0),
    peep_voll("ER_erklaert", 1690, BODEN, 440, "tipp"),
])

# 9 Klausurschema --------------------------------------------------------------------------------------------------------------------
K0, K1, K2 = 250, 310, 380
folie([("sch", "Klausurschema")], [
    karte(180, 50, 1560, 920, "sch"),
    titel("Grundschema der Bilanzierung", K0, 95, "sch", 58),
    zeile("I. Bilanzierungspflicht: §§ 238, 242 HGB · § 140 AO, § 5 I EStG", K1, 210, "k1", "Bold", 38),
    zeile("II. Ansatz (dem Grunde nach)", K1, 300, "k2", "Bold", 40),
    zeile("Vermögensgegenstand / Wirtschaftsgut", K2, 360, "k2", size=36, farbe=TEXT, d=0.8),
    zeile("Zurechnung: persönlich, sachlich (Betriebsvermögen)", K2, 410, "k2", size=36, farbe=TEXT, d=1.6),
    zeile("kein Ansatzverbot", K2, 460, "k2", size=36, farbe=TEXT, d=2.4),
    zeile("III. Bewertung (der Höhe nach)", K1, 545, "k3", "Bold", 40),
    zeile("Zugang: Anschaffungs-/Herstellungskosten", K2, 605, "k3", size=36, farbe=TEXT, d=0.8),
    zeile("planmäßige AfA", K2, 655, "k3", size=36, farbe=TEXT, d=1.6),
    zeile("außerplanmäßig (HGB) / Teilwert (EStG)", K2, 705, "k3", size=36, farbe=TEXT, d=2.4),
    pille("überall: Maßgeblichkeit mit steuerlichem Vorbehalt", K1, 790, "k4", fill=GELB, size=36),
])

# 10 Merksatz ----------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=(255, 251, 230, 255)),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst der ", 0), ("Ansatz", "a"), (",", 0)], [("dann die ", 0), ("Bewertung", "b"), (".", 0)]],
                750, 320, 54, "merke", {"a": ("merke", 0.5), "b": ("merke", 1.3)}),
    *markertext([[("Die Handelsbilanz ist ", 0), ("maßgeblich", "c"), (",", 0)], [("soweit das Steuerrecht", 0)], [("nichts anderes bestimmt.", 0)]],
                750, 530, 50, "m2", {"c": ("m2", 0.8)}),
    peep_voll("ER_freut", 1680, 1000, 720, "merke", d=0.4),
])
