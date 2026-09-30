"""Willenserklärung (Trierer Weinversteigerung) – Open-Peeps-Stil.

Regeln aus der Abnahme: Figuren vollständig im Bild (Prüfung in peep_voll), Karten von Anfang an vollständig,
Geräusche nur bei Haken/Kreuz, Requisiten nur aus Bibliotheken (Open Peeps, Phosphor, Pepicons, Fluent HC).
"""
import sys
sys.path.insert(0, "../../etb2/src")
from ostil import *
import engine

FOLIEN = []
FIG = SP + "peeps/op_we/"
BG_FARBE = {"creme": (255, 248, 236, 255)}
PFAD_FARBE = {"creme": (21, 21, 21, 140)}
RAND = 24


def folie(pfade, els):
    FOLIEN.append(dict(bg="creme", pfade=pfade, els=els))


def peep_voll(name, cx, unten, hoehe, cue, **k):
    """Stehende Figur – bricht ab, wenn sie nicht vollständig mit Rand im Bild steht."""
    e = bild(FIG + name + ".png", cx, unten, hoehe, cue, **k)
    assert e.x >= RAND and e.y >= RAND and e.x + e.sprite.width <= engine.W - RAND and e.y + e.sprite.height <= engine.H - RAND, \
        f"Figur {name} ragt aus dem Bild: {e.x},{e.y},{e.sprite.width}x{e.sprite.height}"
    return e


def figuren(liste, cx, unten, hoehe, erst="pop", d=0.0):
    """Wechselnde Posen/Gesichter einer Figur am selben Platz: [(name, cue), ...]."""
    els = []
    for i, (n, c) in enumerate(liste):
        bis = liste[i + 1][1] if i + 1 < len(liste) else None
        els.append(peep_voll(n, cx, unten, hoehe, c, anim=(erst if i == 0 else "cut"), d=(d if i == 0 else 0.0), bis=bis))
    return els


def ok(x, y, cue, gr=30):
    return ton(haken_i(x, y, cue, gr=gr), "minimal_check", 0.55)


def nein(x, y, cue, gr=28):
    return ton(kreuz_i(x, y, cue, gr=gr), "minimal_uncheck", 0.6)


def zeile(text, x, y, cue, stil="Regular", size=42, farbe=INK, d=0.0, **k):
    return OT(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)


def plusminus(text, x, y, cue, plus, size=40, stil="Regular", d=0.0):
    z = "(+)" if plus else "(-)"
    breite = OT(text, 0, 0, "_", stil, size).sprite.width - 8 + F(stil, size).getlength(" ")
    return [OT(text, x, y, cue, stil, size, d=d),
            OT(z, x + breite, y, cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT), d=d)]


BODEN = 870

# 1 Fall ------------------------------------------------------------------------------------------------
folie([("fall", "Fall · Weinversteigerung")], [
    titel("Weinversteigerung in Trier", 80, 60, "fall", 74),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    *figuren([("VK_ruhig", "fall"), ("VK_ruft", "zuschlag"), ("VK_zufrieden", "frage")], 330, BODEN, 560, d=0.3),
    pille("Auktionator", 330, BODEN + 18, "fall", fill=LILA, size=30, anker="m", d=0.4),
    icon("ph", "wine-duotone", 610, 640, 130, "wein"),
    pille("Riesling", 610, 720, "wein", fill=PINK, size=30, anker="m", d=0.1),
    *figuren([("AN_ruhig", "a"), ("AN_winkt", "winkt"), ("AN_schreck", "schreck")], 1000, BODEN, 560),
    pille("Anton", 1000, BODEN + 18, "a", fill=TUERKIS, size=30, anker="m", d=0.2),
    *figuren([("FR_ruhig", "freund"), ("FR_winkt", "winkt")], 1620, BODEN, 540),
    pille("Freund", 1620, BODEN + 18, "freund", fill=ORANGE, size=30, anker="m", d=0.2),
    icon("pepicons-pencil", "raise-hand", 1165, 205, 90, "regel"),
    pille("Hand heben = Gebot: + 100 €", 1220, 175, "regel", fill=GELB, size=36),
    blase("sprech", 380, 220, "zuschlag", 560, 330, inhalt=["Zum Dritten –", "zugeschlagen!"], textsize=36),
    icon("ph", "gavel-duotone", 770, 470, 110, "zuschlag", d=0.2),
    pille("Muss Anton den Wein bezahlen?", 960, 975, "frage", fill=PINK, size=38, anker="m"),
])

# 2 Anspruch und Vertragsschluss (Karte sofort vollständig) --------------------------------------------------
folie([("schema", "A. § 433 II BGB › Kaufvertrag")], [
    karte(80, 70, 1060, 860, "schema"),
    titel("Anspruch auf den Kaufpreis?", 140, 125, "schema", 60),
    zeile("Versteigerer gegen Anton", 140, 235, "schema", "Bold", 44, d=0.3),
    zeile("§ 433 II BGB: Zahlung des Kaufpreises", 140, 310, "a433", size=42),
    zeile("Voraussetzung: wirksamer Kaufvertrag", 140, 400, "vertrag", "Bold", 42),
    zeile("= zwei übereinstimmende Willenserklärungen", 170, 460, "vertrag", size=38, farbe=TEXT, d=0.5),
    zeile("Gebot = Angebot", 170, 545, "gebot", size=42),
    zeile("Zuschlag = Annahme", 170, 610, "zsl", size=42),
    pille("§ 156 S. 1 BGB", 170, 680, "156", fill=LILA, size=36),
    pille("Ist das Handheben eine Willenserklärung?", 140, 815, "kern", fill=PINK, size=36),
    peep_voll("VK_ruhig", 1270, 860, 420, "schema", d=0.4),
    peep_voll("AN_gruesst", 1750, 860, 420, "schema", d=0.6),
    pfeil_ink(1620, 420, 1370, 420, "gebot"),
    OT("Gebot", 1495, 355, "gebot", "ExtraBold", 34, anker="m"),
    pfeil_ink(1370, 540, 1620, 540, "zsl"),
    OT("Zuschlag", 1495, 575, "zsl", "ExtraBold", 34, anker="m"),
])

# 3 Definition --------------------------------------------------------------------------------------------------
folie([("def", "Willenserklärung › Definition")], [
    karte(80, 70, 1340, 860, "def", fill=(255, 251, 230, 255)),
    titel("Willenserklärung", 750, 125, "def", 72, anker="m"),
    *markertext([[("Äußerung eines ", 0), ("Willens", "a"), (", der unmittelbar", 0)],
                 [("auf eine ", 0), ("Rechtsfolge", "b"), (" gerichtet ist.", 0)]],
                750, 270, 50, "def", {"a": ("def", 1.6), "b": ("def", 3.4)}, d=0.3),
    fl_block(160, 560, 580, 250, BLAU, "zwei", [("objektiver", "ExtraBold", 50, INK), ("Tatbestand", "ExtraBold", 50, INK)]),
    fl_block(770, 560, 580, 250, GRUEN, "zwei", [("subjektiver", "ExtraBold", 50, INK), ("Tatbestand", "ExtraBold", 50, INK)], d=0.4),
    peep_voll("ER_erklaert", 1680, 1000, 720, "def", d=0.5),
])

# 4 Objektiver Tatbestand ----------------------------------------------------------------------------------------
folie([("obj", "Willenserklärung › objektiver Tatbestand")], [
    titel("Objektiver Tatbestand", 960, 55, "obj", 70, anker="m"),
    zeile("Wie durfte ein vernünftiger Empfänger das Verhalten verstehen?", 960, 165, "obj", "Bold", 40, anker="m"),
    pille("Empfängerhorizont, §§ 133, 157 BGB", 960, 235, "133", fill=BLAU, size=36, anker="m"),
    peep_voll("VK_skeptisch", 560, BODEN, 520, "objfall"),
    blase("denk", 340, 220, "objfall", 250, 470, inhalt=["Er bietet", "100 € mehr!"], textsize=34, ziel=(520, 380)),
    peep_voll("AN_gruesst", 1300, BODEN, 520, "obj", d=0.4),
    linienzug([(60, BODEN), (1860, BODEN)], "obj", breite=7, farbe=INK),
    ok(1580, 520, "objok", gr=40),
    OT("objektiver", 1640, 470, "objok", "ExtraBold", 44),
    OT("Tatbestand", 1640, 525, "objok", "ExtraBold", 44),
])

# 5 Subjektiver Tatbestand ----------------------------------------------------------------------------------------
BX, TX = 180, 740
folie([("subj", "Willenserklärung › subjektiver Tatbestand")], [
    titel("Subjektiver Tatbestand", 960, 55, "subj", 70, anker="m"),
    fl_block(BX, 200, 500, 170, GELB, "hw", [("Handlungswille", "ExtraBold", 44, INK)]),
    zeile("bewusstes Handeln", TX, 220, "hw", size=42),
    zeile("fehlt z. B. bei einem Reflex", TX, 275, "hwbsp", size=38, farbe=TEXT),
    nein(TX + 25, 345, "hwfolge"), zeile("fehlt er: keine Willenserklärung", TX + 70, 322, "hwfolge", "Bold", 38, farbe=DROT),
    fl_block(BX, 410, 500, 170, ORANGE, "eb", [("Erklärungs-", "ExtraBold", 44, INK), ("bewusstsein", "ExtraBold", 44, INK)]),
    zeile("Bewusstsein, irgendetwas rechtlich", TX, 440, "eb", size=42),
    zeile("Erhebliches zu erklären", TX, 495, "eb", size=42),
    fl_block(BX, 620, 500, 170, GRUEN, "gw", [("Geschäftswille", "ExtraBold", 44, INK)]),
    zeile("Wille zu einer bestimmten Rechtsfolge", TX, 640, "gw", size=42),
    ok(TX + 25, 723, "gwfolge"), zeile("fehlt er: wirksam, aber anfechtbar, § 119 BGB", TX + 70, 700, "gwfolge", "Bold", 38, farbe=DGRUEN),
])

# 6 Anwendung auf Anton -----------------------------------------------------------------------------------------------
folie([("anton", "Willenserklärung › subjektiver Tatbestand bei Anton")], [
    titel("Und bei Anton?", 960, 55, "anton", 70, anker="m"),
    peep_voll("AN_gruesst", 560, BODEN, 560, "anton"),
    linienzug([(60, BODEN), (1860, BODEN)], "anton", breite=7, farbe=INK),
    blase("denk", 380, 220, "antoneb", 330, 330, inhalt=["Ich grüße nur", "meinen Freund!"], textsize=34, ziel=(540, 330)),
    ok(1060, 360, "antonhw", gr=36), zeile("Handlungswille", 1120, 330, "antonhw", "ExtraBold", 48),
    zeile("Hand bewusst gehoben", 1120, 395, "antonhw", size=38, farbe=TEXT, d=0.4),
    nein(1060, 520, "antoneb", gr=34), zeile("Erklärungsbewusstsein", 1120, 490, "antoneb", "ExtraBold", 48),
    zeile("will nur grüßen", 1120, 555, "antoneb", size=38, farbe=TEXT, d=0.4),
])

# 7 Streitstand ------------------------------------------------------------------------------------------------------
folie([("streit", "Fehlendes Erklärungsbewusstsein › Streitstand")], [
    titel("Fehlendes Erklärungsbewusstsein", 960, 50, "streit", 64, anker="m"),
    karte(90, 170, 820, 660, "streit"),
    karte(1010, 170, 820, 660, "streit"),
    zeile("Willenstheorie", 140, 220, "wt", "ExtraBold", 50),
    nein(165, 330, "wt"), zeile("keine Willenserklärung", 210, 305, "wt", "Bold", 42),
    zeile("kein echter Wille", 210, 365, "wt", size=38, farbe=TEXT, d=0.4),
    zeile("aber: Vertrauensschaden", 140, 470, "wtfolge", "Bold", 42),
    zeile("§ 122 BGB analog", 140, 530, "wtfolge", size=40, farbe=TEXT, d=0.3),
    zeile("h. M. / BGH: Zurechnung", 1060, 220, "hm", "ExtraBold", 50),
    ok(1085, 330, "hm1"), zeile("WE, wenn erkennbar und", 1130, 305, "hm1", "Bold", 40),
    zeile("vermeidbar bei verkehrs-", 1130, 360, "hm1", size=38, d=0.3),
    zeile("erforderlicher Sorgfalt", 1130, 410, "hm1", size=38, d=0.3),
    ok(1085, 500, "hm2"), zeile("Empfänger hat sie als", 1130, 475, "hm2", "Bold", 40),
    zeile("Willenserklärung verstanden", 1130, 530, "hm2", size=38, d=0.3),
    zeile("Grund: Schutz des Rechtsverkehrs", 1060, 640, "hmgrund", "Bold", 38),
    pille("Anfechtung analog § 119 I BGB", 1060, 730, "hmanf", fill=GELB, size=36),
])

# 8 Anwendung der h. M. -------------------------------------------------------------------------------------------------
folie([("hmfall", "Fehlendes Erklärungsbewusstsein › Anwendung")], [
    titel("Anwendung auf Anton", 960, 55, "hmfall", 70, anker="m"),
    peep_voll("AN_nachdenklich", 300, BODEN, 520, "hmfall"),
    peep_voll("VK_zufrieden", 1620, BODEN, 520, "hmfall2"),
    linienzug([(60, BODEN), (1860, BODEN)], "hmfall", breite=7, farbe=INK),
    ok(560, 300, "hmfall", gr=32), zeile("Anton hätte erkennen können:", 610, 275, "hmfall", "Bold", 42),
    zeile("Hand heben bei Versteigerung = Gebot", 610, 335, "hmfall", size=40, farbe=TEXT, d=0.4),
    ok(560, 440, "hmfall2", gr=32), zeile("Auktionator hat es als Gebot", 610, 415, "hmfall2", "Bold", 42),
    zeile("verstanden", 610, 475, "hmfall2", size=40, farbe=TEXT, d=0.3),
    pille("Willenserklärung (+)", 610, 580, "hmerg", fill=GRUEN, size=42),
    zeile("Kaufvertrag mit Zuschlag zustande gekommen", 610, 680, "hmerg", "Bold", 38, d=0.8),
])

# 9 Anfechtung --------------------------------------------------------------------------------------------------------
folie([("anf", "Anfechtung")], [
    titel("Anfechtung", 960, 55, "anf", 74, anker="m"),
    fl_block(120, 230, 500, 190, GELB, "anf", [("Anfechtung", "ExtraBold", 46, INK), ("§ 119 I BGB analog", "Regular", 38, INK)]),
    pfeil_ink(640, 325, 740, 325, "121"),
    fl_block(760, 230, 440, 190, ORANGE, "121", [("unverzüglich", "ExtraBold", 46, INK), ("§ 121 I BGB", "Regular", 38, INK)]),
    icon("pepicons-pencil", "hourglass", 980, 480, 90, "121", d=0.3),
    pfeil_ink(1220, 325, 1320, 325, "142"),
    fl_block(1340, 230, 460, 190, LILA, "142", [("nichtig ex tunc", "ExtraBold", 46, INK), ("§ 142 I BGB", "Regular", 38, INK)]),
    icon("ph", "file-x-duotone", 1570, 480, 90, "142", d=0.3),
    fl_block(380, 600, 1160, 190, PINK, "122", [("aber: Ersatz des Vertrauensschadens", "ExtraBold", 44, INK), ("§ 122 BGB", "Regular", 38, INK)]),
    zeile("z. B. Kosten einer erneuten Versteigerung", 960, 830, "122bsp", size=40, farbe=TEXT, anker="m"),
])

# 10 Klausurschema (Karte sofort vollständig) ----------------------------------------------------------------------------
X0, X1, X2, X3 = 250, 310, 380, 450
folie([("sch", "Klausurschema")], [
    karte(180, 50, 1560, 920, "sch"),
    titel("Klausurschema", X0, 95, "sch", 64),
    zeile("A. Anspruch V gegen A aus § 433 II BGB", X0, 200, "sch", "ExtraBold", 44, d=0.4),
    zeile("I. Anspruch entstanden: Kaufvertrag, § 156 BGB", X1, 280, "s1", "Bold", 42),
    zeile("1. Angebot: Gebot des A", X2, 350, "s1", size=40, d=0.8),
    *plusminus("a) objektiver Tatbestand", X3, 410, "s2", True),
    *plusminus("b) subjektiver Tatbestand: Erklärungsbewusstsein", X3, 470, "s2", False, d=0.6),
    *plusminus("c) Zurechnung nach h. M.", X3, 530, "s3", True),
    *plusminus("2. Annahme: Zuschlag", X2, 600, "s3", True, d=0.8),
    *plusminus("II. Anspruch untergegangen: Anfechtung, §§ 119 I analog, 121, 142 I", X1, 680, "s4", True, stil="Bold", size=40),
    pille("III. Ergebnis: kein Kaufpreis, aber § 122 BGB", X1, 770, "s5", fill=GRUEN, size=40),
])

# 11 Merksatz -------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=(255, 251, 230, 255)),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ohne ", 0), ("Handlungswillen", "a")], [("keine Willenserklärung.", 0)]], 750, 310, 50, "merke", {"a": ("merke", 0.8)}),
    *markertext([[("Ohne ", 0), ("Erklärungsbewusstsein", "b"), (" nach h. M. schon,", 0)],
                 [("wenn sie zurechenbar ist.", 0)]], 750, 490, 50, "m2", {"b": ("m2", 0.9)}),
    *markertext([[("Dann hilft nur die ", 0), ("Anfechtung", "c"), (".", 0)]], 750, 700, 50, "m3", {"c": ("m3", 0.9)}),
    peep_voll("ER_freut", 1680, 1000, 720, "merke", d=0.4),
])
