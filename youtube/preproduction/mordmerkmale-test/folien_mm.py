"""Gekreuzte Mordmerkmale – Open-Peeps-Stil, aktuelles Regelwerk (inkl. Sachverhalt-Karte, alles im Bild)."""
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_mm/"
FOLIEN = bausteine.FOLIEN
BODEN = 870

# 1 Fall ------------------------------------------------------------------------------------------------
BX, TX, AX0, AX1 = 420, 960, 1560, 1080
folie([("fall", "Fall")], [
    titel("Das Erbe der Tante", 80, 55, "fall", 70),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    # Tante Tilde (verschwindet mit dem Gespräch zwischen Ben und Alex)
    peep_voll("T_ruhig", TX, BODEN, 480, "fall", d=0.2, bis="entdeckt"),
    peep_voll("T_skeptisch", TX, BODEN, 480, "entdeckt", anim="cut", bis="ueberredet"),
    pille("Tante Tilde", TX, BODEN + 18, "fall", fill=LILA, size=30, anker="m", d=0.3, bis="ueberredet"),
    icon("fluent-emoji-high-contrast", "money-bag", TX + 190, 420, 110, "fall", farbe="#151515", d=0.6, bis="ueberredet"),
    # Ben
    peep_voll("B_ruhig", BX, BODEN, 480, "b", bis="gier"),
    peep_voll("B_gierig", BX, BODEN, 480, "gier", anim="cut", bis="tat"),
    peep_voll("B_nachdenklich", BX, BODEN, 480, "tat", anim="cut"),
    pille("Ben", BX, BODEN + 18, "b", fill=GRUEN, size=30, anker="m", d=0.2),
    blase("denk", 300, 170, "gier", 250, 245, inhalt=["Das Erbe!"], textsize=40, ziel=(400, 375), bis="a"),
    # Alex
    peep_voll("AX_ruhig", AX0, BODEN, 480, "a", bis="betrug"),
    peep_voll("AX_nervoes", AX0, BODEN, 480, "betrug", anim="cut", bis="ueberredet"),
    pille("Alex", AX0, BODEN + 18, "a", fill=ORANGE, size=30, anker="m", d=0.2, bis="ueberredet"),
    icon("ph", "file-x-duotone", AX0 - 250, 400, 120, "betrug", farbe="#151515", bis="ueberredet"),
    pille("Betrug an Tilde", AX0 - 250, 470, "betrug", fill=ROT, size=28, anker="m", d=0.2, bis="ueberredet"),
    bewegt(peep_voll("AX_redet", AX1, BODEN, 480, "ueberredet", anim="cut", bis="tat"), "ueberredet", ("ueberredet", 0.7), AX0 - AX1),
    peep_voll("AX_verschlagen", AX1, BODEN, 480, "tat", anim="cut"),
    pille("Alex", AX1, BODEN + 18, "ueberredet", fill=ORANGE, size=30, anker="m", d=0.7),
    blase("sprech", 300, 170, "ueberredet", 1400, 280, inhalt=["Tu es!"], textsize=44, spiegeln=True, bis="ben"),
    blase("denk", 340, 190, "ben", 270, 250, inhalt=["Das Erbe", "gehört mir!"], textsize=34, ziel=(400, 375)),
    blase("denk", 440, 210, "alex", 1480, 250, inhalt=["Mein Betrug darf", "nie rauskommen!"], textsize=32, ziel=(1110, 375)),
    pille("Ben tötet Tilde.", 760, 560, "tat", fill=ROT, size=40, anker="m"),
    pille("Wie haben sich Ben und Alex strafbar gemacht?", 960, 960, "frage", fill=PINK, size=36, anker="m"),
])

# 2 Sachverhalt zum Nachlesen --------------------------------------------------------------------------------
sachverhalt("sv", [
    "Tante Tilde ist wohlhabend. Ihr Neffe Ben möchte möglichst schnell an ihr Erbe kommen.",
    "Bens Freund Alex hat Tilde um eine größere Geldsumme betrogen. Tilde hat den Betrug inzwischen entdeckt.",
    "Alex überredet Ben, Tilde zu töten. Ben geht es dabei um das Erbe. Alex geht es darum, dass sein Betrug "
    "nicht aufgedeckt wird. Ben tötet Tilde vorsätzlich.",
], "Wie haben sich Ben und Alex strafbar gemacht?")

# 3 Ben -------------------------------------------------------------------------------------------------------
X0, X1, X2 = 170, 230, 290
folie([("schema", "A. Strafbarkeit des Ben")], [
    karte(100, 70, 1300, 860, "schema"),
    titel("A. Strafbarkeit des Ben", X0, 120, "schema", 60),
    *plusminus("I. Totschlag, § 212 StGB", X1, 250, "ben212", True, size=44, stil="Bold"),
    zeile("vorsätzliche Tötung der Tilde", X2, 320, "ben212", size=38, farbe=TEXT, d=0.5),
    zeile("II. Mord, § 211 StGB", X1, 420, "habgier", "Bold", 44),
    ok(X2 + 20, 510, "habgier", gr=26), zeile("Habgier: tötet, um an das Erbe zu kommen", X2 + 60, 490, "habgier", size=38, d=0.4),
    pille("Ben: Mord aus Habgier", X1, 620, "benerg", fill=GRUEN, size=40),
    peep_voll("B_gierig", 1660, BODEN, 560, "schema", d=0.3),
])

# 4 Alex: Anstiftung ------------------------------------------------------------------------------------------
folie([("alexsch", "B. Strafbarkeit des Alex › Anstiftung")], [
    karte(100, 70, 1300, 860, "alexsch"),
    titel("B. Strafbarkeit des Alex", X0, 120, "alexsch", 60),
    zeile("Anstiftung zum Mord, §§ 212, 211, 26 StGB", X1, 240, "anst", "Bold", 44),
    ok(X2 + 20, 340, "haupt", gr=26), zeile("Haupttat: Bens Mord aus Habgier", X2 + 60, 320, "haupt", size=40),
    ok(X2 + 20, 420, "kennt", gr=26), zeile("Vorsatz: Alex kennt Bens Habgier", X2 + 60, 400, "kennt", size=40),
    nein(X2 + 20, 520, "problem", gr=24), zeile("Alex selbst: keine Habgier", X2 + 60, 500, "problem", "Bold", 40),
    ok(X2 + 20, 600, "verd", gr=26), zeile("aber: Verdeckungsabsicht", X2 + 60, 580, "verd", "Bold", 40),
    pille("Problem: unterschiedliche Mordmerkmale", X1, 700, "verd", fill=GELB, size=36, d=0.8),
    peep_voll("AX_verschlagen", 1660, BODEN, 560, "alexsch", d=0.3),
])

# 5 Begriff: gekreuzte Mordmerkmale --------------------------------------------------------------------------------
folie([("begriff", "B. Alex › Gekreuzte Mordmerkmale")], [
    titel("Gekreuzte Mordmerkmale", 960, 55, "begriff", 70, anker="m"),
    peep_voll("B_gierig", 400, 700, 460, "kreuz"),
    peep_voll("AX_verschlagen", 1520, 700, 460, "kreuz", d=0.2),
    fl_block(200, 740, 400, 110, GRUEN, "kreuz", [("Habgier", "ExtraBold", 46, INK)]),
    fl_block(1250, 740, 470, 110, ORANGE, "kreuz", [("Verdeckungsabsicht", "ExtraBold", 40, INK)], d=0.2),
    pfeil_ink(430, 730, 760, 470, "gruppen", d=0.2),
    pfeil_ink(1480, 730, 1160, 470, "gruppen", d=0.4),
    pille("Täter", 400, 900, "kreuz", fill=WEISS, size=30, anker="m"),
    pille("Anstifter", 1520, 900, "kreuz", fill=WEISS, size=30, anker="m", d=0.2),
    fl_block(610, 170, 700, 190, GELB, "gruppen", [("täterbezogen:", "ExtraBold", 40, INK), ("1. und 3. Gruppe des § 211", "Regular", 36, INK)]),
    pille("besondere persönliche Merkmale, § 28 StGB", 960, 385, "28", fill=LILA, size=34, anker="m"),
])

# 6 Streit ------------------------------------------------------------------------------------------------------------
folie([("streit", "B. Alex › § 28 I oder II?")], [
    titel("§ 28 Abs. 1 oder Abs. 2?", 960, 50, "streit", 66, anker="m"),
    zeile("Entscheidend: Verhältnis von Mord und Totschlag", 960, 150, "streit", "Bold", 38, farbe=TEXT, anker="m"),
    karte(90, 220, 820, 700, "rspr"),
    karte(1010, 220, 820, 700, "lit"),
    zeile("Rechtsprechung", 140, 265, "rspr", "ExtraBold", 50),
    zeile("§ 211 = eigenständiger Tatbestand", 140, 345, "rspr", "Bold", 36),
    zeile("Merkmale strafbegründend", 140, 405, "rspr28", size=38),
    pille("§ 28 Abs. 1 StGB", 140, 460, "rspr28", fill=BLAU, size=34),
    ok(165, 590, "rspr1", gr=26), zeile("Anstiftung zum Mord", 210, 568, "rspr1", "Bold", 38),
    zeile("Alex kennt Bens Habgier", 210, 620, "rspr1", size=34, farbe=TEXT, d=0.4),
    nein(165, 710, "rspr2", gr=24), zeile("keine Milderung:", 210, 688, "rspr2", "Bold", 38),
    zeile("eigenes gleichartiges Mordmerkmal", 210, 740, "rspr2", size=34, farbe=TEXT, d=0.4),
    zeile("Literatur", 1060, 265, "lit", "ExtraBold", 50),
    zeile("§ 211 = Qualifikation des § 212", 1060, 345, "lit", "Bold", 36),
    zeile("Merkmale strafschärfend", 1060, 405, "lit28", size=38),
    pille("§ 28 Abs. 2 StGB", 1060, 460, "lit28", fill=ORANGE, size=34),
    zeile("jeder nach eigenen Merkmalen", 1060, 568, "lit1", "Bold", 38),
    ok(1085, 660, "lit2", gr=26), zeile("Verdeckungsabsicht", 1130, 638, "lit2", "Bold", 38),
    zeile("Anstiftung zum Mord", 1130, 690, "lit2", size=34, farbe=TEXT, d=0.5),
])

# 7 Ergebnis + Klausurtipp -----------------------------------------------------------------------------------------------
folie([("erg", "B. Alex › Ergebnis")], [
    titel("Ergebnis", 960, 55, "erg", 74, anker="m"),
    fl_block(360, 190, 1200, 150, GRUEN, "erg", [("Beide Ansichten: Anstiftung zum Mord", "ExtraBold", 44, INK), ("ohne Strafmilderung", "Regular", 38, INK)]),
    pille("Streit kann offenbleiben", 960, 380, "offen", fill=GELB, size=40, anker="m"),
    warnung_i(250, 520, "tipp", gr=30),
    zeile("Klausurtipp: Teilnehmer ohne eigenes Mordmerkmal", 300, 495, "tipp", "ExtraBold", 40, farbe=DROT),
    zeile("Rechtsprechung: Anstiftung zum Mord, gemildert (§ 28 I, § 49 I)", 300, 575, "tipp2", size=38),
    zeile("Literatur: nur Anstiftung zum Totschlag (§ 28 II)", 300, 640, "tipp3", size=38),
    pille("Nur dann ist der Streit zu entscheiden", 300, 720, "tipp3", fill=PINK, size=34, d=0.8),
    peep_voll("ER_warnt" if False else "ER_arme", 1690, BODEN, 440, "tipp"),
])

# 8 Klausurschema ---------------------------------------------------------------------------------------------------------
K0, K1, K2 = 250, 310, 380
folie([("sch", "Klausurschema")], [
    karte(180, 50, 1560, 920, "sch"),
    titel("Klausurschema: Gekreuzte Mordmerkmale", K0, 95, "sch", 58),
    *plusminus("A. Strafbarkeit des Täters: §§ 212, 211 (Habgier)", K1, 210, "s1", True, stil="Bold", size=40),
    zeile("B. Strafbarkeit des Anstifters: §§ 212, 211, 26", K1, 295, "s2", "Bold", 40),
    *plusminus("I. Vorsätzliche rechtswidrige Haupttat", K2, 365, "s2", True, size=38, d=0.8),
    *plusminus("II. Bestimmen + doppelter Anstiftervorsatz", K2, 425, "s2", True, size=38, d=1.6),
    zeile("III. § 28: Abs. 1 (Rspr.) oder Abs. 2 (Lit.)?", K2, 495, "s3", size=38),
    zeile("gekreuzte Mordmerkmale: eigenes Merkmal", K2 + 60, 560, "s4", size=36, farbe=TEXT),
    zeile("→ Rspr.: keine Milderung · Lit.: Mord über § 28 II", K2 + 60, 615, "s4", size=36, farbe=TEXT, d=0.6),
    pille("Ergebnis: Anstiftung zum Mord, Streit offen", K1, 720, "s4", fill=GRUEN, size=38, d=1.4),
])

# 9 Merksatz -------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=(255, 251, 230, 255)),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Gekreuzte Mordmerkmale:", "a")], [("nach beiden Ansichten", 0)], [("Anstiftung zum ", 0), ("Mord", "b"), (",", 0)]],
                750, 320, 50, "merke", {"a": ("merke", 0.6), "b": ("merke", 4.5)}),
    *markertext([[("ohne ", 0), ("Milderung", "c"), (".", 0)], [("Den Streit kannst du offenlassen.", 0)]],
                750, 600, 50, "m2", {"c": ("m2", 0.1)}),
    peep_voll("ER_freut", 1680, 1000, 720, "merke", d=0.4),
])
