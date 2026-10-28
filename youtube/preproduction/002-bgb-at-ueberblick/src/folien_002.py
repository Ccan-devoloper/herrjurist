"""Folge 002 · BGB AT Überblick: Vom Vertragsschluss bis zur Anfechtung – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Wohnzimmer, B Garage, C Anruf am Abend, D Sachverhalt, E Aufbau, F Einigung, G Stellvertretung,
H Minderjährige Vertreterin und Gegenfall, I Wirksamkeitshindernisse, J1/J2 Anfechtung, K Durchsetzbarkeit und Ergebnis,
L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Fahrradklingel, Handy)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_002/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
DAUER = bausteine._cj()["dauer"]
P0 = "§ 433 I 1 BGB"                      # Anspruchsgrundlage im Prüfpfad


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, 50)]


def bis_(e, cue):
    """Endzeit für Elemente ohne bis-Parameter (Haken/Kreuz)."""
    e.bis = cue
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def ebike(cx, unten, breite, cue, bis=None, d=0.0, anim="pop"):
    """E-Bike: Tabler 'bike' (blaue Räder) mit gelbem Tabler-'bolt' am Rahmen."""
    return [ficon("tabler", "bike", cx, unten, breite, cue, fuell=BLAU, d=d, bis=bis, anim=anim),
            ficon("tabler", "bolt", cx, unten - breite * 0.30, int(breite * 0.22), cue, fuell=GELB, d=d, bis=bis, anim=anim)]


BODEN, FH = 880, 460

# A Fall: Karls Wohnzimmer --------------------------------------------------------------------------------------------
KX, EX = 400, 1520                         # Karl links (blickt nach rechts), Emma rechts (blickt nach links)
KA = ("KA_redet_r", KX, BODEN, FH)
folie([(("fall", -0.4), "Fall · Opas Auftrag")], [               # Prüfpfad ab dem ersten Bild nach dem Intro (0,0 s)
    pille("Der E-Bike-Fall", 70, 40, "fall", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    ficon("tabler", "armchair", 1800, BODEN - 2, 190, "fall", fuell=GRUEN, d=0.3),
    ficon("tabler", "lamp", 140, BODEN - 2, 130, "fall", fuell=GELB, d=0.4),
    peep_voll("KA_ruhig_r", KX, BODEN, FH, "fall", bis="k1"),
    *redet("KA_redet_r", KX, BODEN, FH, "k1", "garage"),
    pille("Opa Karl, 72", KX, BODEN + 22, "fall", fill=GRUEN, size=30, anker="m", d=0.3),
    # die Anzeige auf dem Laptop
    ficon("tabler", "device-laptop", 900, 640, 300, "anzeige", fuell=WEISS, bis="k1"),
    karte(700, 150, 520, 300, "anzeige", fill=WEISS, schatten=8),
    z("Anzeige", 740, 175, "anzeige", "ExtraBold", 36, rechts=1210),
    *ebike(1120, 435, 150, "anzeige"),
    z("Gebrauchtes E-Bike", 740, 235, beim("anzeige", "gebrauchtes"), "Bold", 32, rechts=1210),
    z("gut erhalten", 740, 285, beim("anzeige", "gut"), size=32, rechts=1210),
    pille("Preis auf Anfrage", 740, 350, beim("anzeige", "Preis"), fill=ORANGE, size=32),
    # Emma kommt
    peep_voll("EM_ruhig", EX, BODEN, FH, "auftrag", bis=beim("k1", "Bis")),
    peep_voll("EM_froh", EX, BODEN, FH, beim("k1", "Bis"), anim="cut"),
    pille("Emma, 17", EX, BODEN + 22, beim("auftrag", "siebzehnjährige"), fill=ORANGE, size=30, anker="m"),
    blase("sprech", 600, 300, "k1", 830, 620, inhalt=["Schau es dir an, Emma.", "Wenn es gut ist, kauf es", "in meinem Namen.",
                                                        "Bis 800 Euro."], textsize=34, figur=KA),
    pille("Vollmacht: bis 800 €", EX, 330, beim("k1", "achthundert"), fill=GELB, size=34, anker="m"),
])

# B Fall: in der Garage des Verkäufers ------------------------------------------------------------------------------------
EG, RX, JX = 380, 560, 1330                # Emma stehend, Emma auf dem Rad, Jens
RH = 490                                   # Radpose: gleiche Kopfgröße wie stehend (FH 460)
JE = ("JG_redet", JX, BODEN, FH)
folie([("garage", "Fall · In der Garage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "garage", breite=7, farbe=INK),
    ficon("ph", "garage", 1680, BODEN - 2, 330, "garage", fuell=GELB, d=0.2),
    ficon("ph", "toolbox", 1680, BODEN - 2, 120, "garage", fuell=ROT, d=0.4),
    peep_voll("JE_ruhig", JX, BODEN, FH, "garage", d=0.3, bis="j1"),
    pille("Verkäufer Jens", JX, BODEN + 22, "garage", fill=BLAU, size=30, anker="m", d=0.5),
    peep_voll("EM_ruhig_r", EG, BODEN, FH, "garage", bis="probe"),
    pille("Emma", EG, BODEN + 22, "garage", fill=ORANGE, size=30, anker="m", d=0.2, bis="probe"),
    pille("kauft im Namen ihres Großvaters", 560, 300, beim("garage", "Namen"), fill=GELB, size=34, anker="m", bis="probe"),
    # Probefahrt: Emma kommt auf dem E-Bike zurück und bleibt darauf sitzen
    szene(bewegt(peep_voll("EM_rad_r", RX, BODEN, RH, "probe", anim="cut", bis="e1"), ("probe", 0.0), ("preis", 0.0), -250),
          "ebike_klingel*", 0.8, versatz=0.15),
    ficon("tabler", "bolt", RX + 120, BODEN - 175, 60, ("preis", 0.0), fuell=GELB, bis="e1"),
    pille("Probefahrt", 1000, 420, beim("probe", "Probefahrt"), fill=GRUEN, size=36, anker="m", bis="preis"),
    *redet("EM_rad_r", RX, BODEN, RH, "e1", "abend"),
    bis_(ficon("tabler", "bolt", RX + 120, BODEN - 175, 60, "e1", fuell=GELB, anim="cut"), "abend"),
    pille("Emma", RX, BODEN + 22, "preis", fill=ORANGE, size=30, anker="m"),
    # Jens nennt den Preis – und verspricht sich
    *redet("JG_redet", JX, BODEN, FH, "j1", "dreher"),
    peep_voll("JE_froh", JX, BODEN, FH, "dreher", anim="cut"),
    blase("sprech", 560, 220, "j1", 1080, 200, inhalt=["Für 570 Euro gehört", "es Ihrem Opa."], textsize=38, figur=JE, bis="dreher"),
    blase("denk", 330, 230, "dreher", 1150, 240, inhalt=["750 €"], textsize=56, figur=("JE_froh", JX, BODEN, FH), bis="e1"),
    pille("gesagt: 570 €", 860, 330, beim("dreher", "versprochen"), fill=ROT, size=36, anker="m", bis="e1"),
    pille("ohne es zu merken", 860, 420, beim("dreher", "ohne"), fill=WEISS, size=32, anker="m", bis="e1"),
    blase("sprech", 640, 220, "e1", 760, 210, inhalt=["Abgemacht! Ich kaufe es", "im Namen von Opa Karl."], textsize=36,
          figur=("EM_rad_r", RX, BODEN, RH)),
    icon("fluent-emoji-high-contrast", "handshake", 1040, 470, 110, beim("e1", "Abgemacht", ende=True)),
])

# C Fall: der Anruf am Abend ---------------------------------------------------------------------------------------------
JA, KA2 = 420, 1500
folie([("abend", "Fall · Der Anruf"), ("frage", "Fall · Die Frage")], [
    ficon("tabler", "moon-stars", 960, 200, 120, "abend", fuell=GELB, d=0.2),
    linienzug([(60, BODEN), (1860, BODEN)], "abend", breite=7, farbe=INK),
    linienzug([(960, 330), (960, BODEN)], "abend", breite=5, farbe=GRAU),
    peep_voll("JE_schreck_r", JA, BODEN, FH, "abend", bis="j2"),
    pille("Jens", JA, BODEN + 22, "abend", fill=BLAU, size=30, anker="m", d=0.2),
    blase("denk", 330, 220, beim("abend", "Zahlendreher"), 660, 260, inhalt=["570 statt 750!"], textsize=40,
          figur=("JE_schreck_r", JA, BODEN, FH), bis="j2"),
    peep_voll("KA_ruhig", KA2, BODEN, FH, "abend", d=0.3, bis="k2"),
    pille("Karl", KA2, BODEN + 22, "abend", fill=GRUEN, size=30, anker="m", d=0.4),
    szene(ficon("tabler", "phone-call", 1230, 520, 110, beim("abend", "ruft"), fuell=GRUEN), "handy_klingel*", 0.7),
    ficon("tabler", "phone", 690, 520, 100, beim("abend", "ruft"), fuell=BLAU),
    *redet("JG_ernst_r", JA, BODEN, FH, "j2", "k2"),
    peep_voll("JG_ernst_r", JA, BODEN, FH, "k2", anim="cut"),
    blase("sprech", 620, 260, "j2", 560, 240, inhalt=["Ich habe mich versprochen.", "Gemeint waren 750 Euro.",
                                                      "Ich fechte den Kauf an."], textsize=32,
          figur=("JG_ernst_r", JA, BODEN, FH), bis="frage"),
    *redet("KA_streng", KA2, BODEN, FH, "k2", "frage"),
    peep_voll("KA_streng", KA2, BODEN, FH, "frage", anim="cut"),
    blase("sprech", 560, 220, "k2", 1390, 240, inhalt=["Gekauft ist gekauft! Ich will", "das Rad für 570 Euro."], textsize=32,
          figur=("KA_streng", KA2, BODEN, FH)),
    pille("Kann Karl das Rad für 570 € verlangen?", 960, 960, "frage", fill=PINK, size=36, anker="m"),
])

# D Sachverhalt ---------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Der 72-jährige Karl bittet seine 17-jährige Enkelin Emma, ein gebrauchtes E-Bike aus einer Internetanzeige "
    "(„Preis auf Anfrage“) für ihn zu kaufen: in seinem Namen und bis 800 Euro. Emma sagt dem Verkäufer Jens, dass sie im "
    "Namen ihres Großvaters kauft. Nach einer Probefahrt sagt Jens: „Für 570 Euro gehört es Ihrem Opa.“ Gemeint hatte er "
    "750 Euro. Emma erwidert sofort: „Abgemacht! Ich kaufe es im Namen von Opa Karl.“ Abholung und Zahlung sollen am "
    "nächsten Tag erfolgen.",
    "Am Abend bemerkt Jens den Zahlendreher und ruft sofort bei Karl an: „Ich habe mich versprochen. Gemeint waren "
    "750 Euro. Ich fechte den Kauf an.“ Karl besteht auf dem Kauf.",
], "Kann Karl von Jens das E-Bike für 570 Euro verlangen?")

# E Anspruchsgrundlage und Aufbau ---------------------------------------------------------------------------------------
FX, BR, FR = 1560, 930, 500
folie([("agl", f"Karl gegen Jens, {P0}"), ("drei", f"Karl gegen Jens, {P0} › Aufbau in drei Schritten")], [
    *tafel("agl", "Karl gegen Jens"),
    z("Anspruch auf Übergabe und Übereignung", 110, 200, "agl", "Bold", 38),
    z("des E-Bikes, § 433 I 1 BGB", 110, 255, beim("agl", "Anspruchsgrundlage"), "Bold", 38),
    fl_block(110, 360, 760, 110, GELB, "drei", [("I. Anspruch entstanden?", "ExtraBold", 40, INK)]),
    fl_block(180, 500, 760, 110, BLAU, "drei2", [("II. Anspruch untergegangen?", "ExtraBold", 40, INK)]),
    fl_block(250, 640, 760, 110, LILA, "drei3", [("III. Anspruch durchsetzbar?", "ExtraBold", 40, INK)]),
    peep_voll("KA_streng", FX, BR, FR, "agl", bis="drei"),
    peep_voll("KA_denkt", FX, BR, FR, "drei", anim="cut"),
    *ebike(FX, 360, 250, beim("agl", "Übergabe")),
])

# F I. 1. Einigung: Angebot und Annahme --------------------------------------------------------------------------------------
E1, J1 = 1400, 1730
PE = f"{P0} › I. Entstanden › 1. Einigung"
folie([("vs", PE), ("inv", f"{PE} › Anzeige: Angebot?"), ("ang", f"{PE} › Angebot"), ("ausl", f"{PE} › Auslegung"),
       ("ann", f"{PE} › Annahme")], [
    *tafel("vs", "I. 1. Einigung"),
    z("Kaufvertrag: Angebot und Annahme, §§ 145 ff. BGB", 110, 195, beim("vs", "Angebot"), "Bold", 34),
    nein(135, 290, beim("inv", "Anzeige"), gr=22), z("Anzeige: noch kein Angebot", 175, 270, beim("inv", "Anzeige"), "Bold", 34),
    z("kein Rechtsbindungswille, nur Einladung", 215, 322, beim("inv", "Rechtsbindungswille"), size=32, farbe=TEXT),
    z("zu Angeboten (invitatio ad offerendum)", 215, 366, beim("inv", "lädt"), size=32, farbe=TEXT),
    ok(135, 450, "ang", gr=22), z("Angebot: Jens, 570 € an Karl", 175, 430, "ang", "Bold", 34),
    z("entgegengenommen von Emma", 215, 482, beim("ang", "entgegengenommen"), size=32, farbe=TEXT),
    z("Auslegung, §§ 133, 157 BGB:", 175, 545, "ausl", "Bold", 34),
    z("wie durfte Emma die Erklärung verstehen?", 215, 597, beim("ausl", "wie"), size=32, farbe=TEXT),
    z("innerer Wille von Jens (750 €) zählt nicht", 215, 641, beim("ausl", "Was"), size=32, farbe=TEXT),
    ok(135, 715, "ann", gr=22), z("Annahme: Emma, sofort (§ 147 I BGB)", 175, 695, "ann", "Bold", 34),
    fl_block(110, 775, 1040, 95, GRUEN, beim("ann", "Einigung"), [("Einigung über 570 €", "ExtraBold", 40, INK)]),
    peep_voll("EM_ruhig_r", E1, BR, FR - 30, "vs", bis="ann"),
    peep_voll("EM_froh_r", E1, BR, FR - 30, "ann", anim="cut"),
    peep_voll("JE_ruhig", J1, BR, FR - 30, "vs", d=0.2, bis="ausl"),
    peep_voll("JE_denkt", J1, BR, FR - 30, "ausl", anim="cut"),
    # Anzeige durchgestrichen
    ficon("tabler", "device-laptop", 1560, 330, 230, beim("inv", "Anzeige"), fuell=WEISS, bis="ang"),
    bis_(kreuz_i(1560, 260, beim("inv", "kein"), gr=46), "ang"),
    pille("570 € an Karl", 1560, 280, "ang", fill=GELB, size=36, anker="m", bis="ausl"),
    blase("denk", 300, 220, beim("ausl", "Was"), 1640, 250, inhalt=["750 €"], textsize=50,
          figur=("JE_denkt", J1, BR, FR - 30), bis="ann"),
    bis_(kreuz_i(1640, 250, beim("ausl", "zählt"), gr=40), "ann"),
    pille("Emma versteht: 570 €", 1420, 380, "ausl", fill=ORANGE, size=30, anker="m", bis="ann"),
    icon("fluent-emoji-high-contrast", "handshake", 1565, 300, 140, "ann"),
])

# G I. 2. Stellvertretung, § 164 I BGB ----------------------------------------------------------------------------------------
PS_ = f"{P0} › I. Entstanden › 2. Stellvertretung"
folie([("st", f"{PS_}, § 164 I BGB"), ("st1", f"{PS_} › eigene Willenserklärung"), ("st2", f"{PS_} › im fremden Namen"),
       ("st3", f"{PS_} › Vertretungsmacht")], [
    *tafel("st", "I. 2. Stellvertretung"),
    z("Emmas Erklärung wirkt für Karl, § 164 I BGB, bei:", 110, 200, beim("st", "Für"), "Bold", 34),
    ok(135, 305, "st1", gr=24), z("1. eigener Willenserklärung", 175, 285, "st1", "Bold", 38),
    z("entscheidet selbst – keine Botin", 215, 345, beim("st1", "Sie"), size=34, farbe=TEXT),
    ok(135, 445, "st2", gr=24), z("2. Handeln im fremden Namen", 175, 425, "st2", "Bold", 38),
    z("offen: „im Namen von Opa Karl“", 215, 485, beim("st2", "offen"), size=34, farbe=TEXT),
    ok(135, 585, "st3", gr=24), z("3. Vertretungsmacht", 175, 565, "st3", "Bold", 38),
    z("Vollmacht, § 167 BGB: bis 800 €", 215, 625, beim("st3", "Vollmacht"), size=34, farbe=TEXT),
    fl_block(110, 720, 1040, 100, GRUEN, beim("st3", "achthundert", ende=True), [("570 € ≤ 800 € – Emma vertritt Karl", "ExtraBold", 38, INK)]),
    peep_voll("EM_ruhig_r", E1, BR, FR - 30, "st", bis="st1"),
    peep_voll("EM_denkt_r", E1, BR, FR - 30, "st1", anim="cut", bis="st2"),
    peep_voll("EM_froh_r", E1, BR, FR - 30, "st2", anim="cut"),
    peep_voll("KA_ruhig", J1, BR, FR - 30, "st", d=0.2, bis="st3"),
    peep_voll("KA_froh", J1, BR, FR - 30, "st3", anim="cut"),
    pfeil_ink(1470, 300, 1660, 300, beim("st", "wirkt")),
    pille("wirkt für Karl", 1565, 200, beim("st", "wirkt"), fill=GELB, size=30, anker="m", bis="st1"),
    pille("Wahl: kaufen oder nicht", 1500, 200, "st1", fill=WEISS, size=30, anker="m", bis="st2"),
    pille("„im Namen von Opa Karl“", 1530, 200, "st2", fill=ORANGE, size=30, anker="m", bis="st3"),
    pille("Vollmacht bis 800 €", 1565, 200, "st3", fill=GELB, size=30, anker="m"),
])

# H Minderjährige Vertreterin, § 165 BGB, und Gegenfall ohne Vertretungsmacht ------------------------------------------------
folie([("gf", f"{PS_} › minderjährige Vertreterin, § 165 BGB"), ("gegen", f"{PS_} › Gegenfall: ohne Vertretungsmacht")], [
    *tafel("gf", "Emma ist erst 17"),
    z("beschränkt geschäftsfähig, §§ 2, 106 BGB", 110, 195, beim("gf", "beschränkt"), "Bold", 36),
    ok(135, 285, "gf2", gr=24), z("§ 165 BGB: schadet beim Vertreter nicht", 175, 265, "gf2", "Bold", 36),
    z("die Folgen treffen Karl, nicht Emma", 215, 322, beim("gf2", "Die"), size=34, farbe=TEXT),
    z("Gegenfall: Kauf für 900 €", 110, 420, "gegen", "ExtraBold", 38),
    nein(135, 505, beim("gegen", "Vertretungsmacht"), gr=22), z("keine Vertretungsmacht", 175, 485, beim("gegen", "Vertretungsmacht"), "Bold", 34),
    z("Vertrag hängt von Karls Genehmigung ab,", 215, 540, beim("gegen", "Genehmigung"), size=32, farbe=TEXT),
    z("§ 177 I BGB", 215, 584, beim("gegen", "Genehmigung"), size=32, farbe=TEXT),
    z("Emma haftet nicht, § 179 III 2 BGB", 175, 660, "gegen2", "Bold", 34),
    z("außer mit Zustimmung der Eltern", 215, 715, beim("gegen2", "außer"), size=32, farbe=TEXT),
    peep_voll("EM_ruhig", FX, BR, FR, "gf", bis="gegen"),
    peep_voll("EM_staunt", FX, BR, FR, "gegen", anim="cut", bis="gegen2"),
    peep_voll("EM_froh", FX, BR, FR, "gegen2", anim="cut"),
    pille("17 Jahre", FX, 330, beim("gf", "siebzehn"), fill=ORANGE, size=36, anker="m", bis="gegen"),
    pille("Folgen: Karl", FX, 230, beim("gf2", "Folgen"), fill=GRUEN, size=32, anker="m", bis="gegen"),
    pille("900 € > 800 €", FX, 330, "gegen", fill=ROT, size=36, anker="m"),
    pille("Karl genehmigt?", FX, 230, beim("gegen", "Genehmigung"), fill=GELB, size=32, anker="m", bis="gegen2"),
    pille("Emma haftet nicht", FX, 230, "gegen2", fill=GRUEN, size=32, anker="m"),
])

# I I. 3. Wirksamkeitshindernisse -----------------------------------------------------------------------------------------
folie([("wh", f"{P0} › I. Entstanden › 3. Wirksamkeitshindernisse"), ("wh_erg", f"{P0} › I. Anspruch entstanden (+)")], [
    *tafel("wh", "I. 3. Wirksamkeitshindernisse"),
    ok(135, 225, beim("wh", "Karl"), gr=24), z("Geschäftsfähigkeit: Karl und Jens voll", 175, 200, beim("wh", "Karl"), "Bold", 36),
    ok(135, 305, "form", gr=24), z("Form: keine vorgeschrieben (§ 125 BGB)", 175, 280, "form", "Bold", 36),
    fl_block(110, 400, 1040, 160, GRUEN, "wh_erg", [("I. Anspruch entstanden (+)", "ExtraBold", 42, INK),
                                                    ("Kaufvertrag Karl – Jens über 570 €", "Regular", 34, INK)]),
    peep_voll("KA_froh", E1, BR, FR - 30, "wh"),
    peep_voll("JE_ruhig", J1, BR, FR - 30, "wh", d=0.2),
    pille("72", E1, 330, beim("wh", "Karl"), fill=GRUEN, size=32, anker="m"),
    pille("volljährig", J1, 330, beim("wh", "voll"), fill=BLAU, size=32, anker="m"),
    icon("fluent-emoji-high-contrast", "handshake", 1565, 210, 110, "form"),
])

# J1 II. Untergegangen: Anfechtung – Erklärung und Grund ----------------------------------------------------------------------
PA = f"{P0} › II. Untergegangen › Anfechtung"
folie([("unter", f"{PA}, § 142 I BGB"), ("ae", f"{PA} › Erklärung, § 143 BGB"), ("grund", f"{PA} › Grund, § 119 I BGB")], [
    *tafel("unter", "II. Anspruch untergegangen?"),
    z("Anfechtung: von Anfang an nichtig, § 142 I BGB", 110, 200, beim("unter", "Dann"), "Bold", 34),
    ok(135, 305, "ae", gr=24), z("1. Erklärung gegenüber Karl, § 143 BGB", 175, 285, "ae", "Bold", 36),
    z("Anfechtungsgegner: der Vertragspartner", 215, 342, beim("ae", "seinem"), size=32, farbe=TEXT),
    ok(135, 435, "grund", gr=24), z("2. Grund: Erklärungsirrtum,", 175, 415, "grund", "Bold", 36),
    z("§ 119 I Alt. 2 BGB", 215, 470, beim("grund", "Paragraf"), "Bold", 34),
    z("gesagt 570 €, gewollt 750 € (versprochen)", 215, 525, beim("grund", "Jens"), size=32, farbe=TEXT),
    ok(175, 600, "kaus", gr=20), z("sonst nicht so erklärt (Kausalität)", 215, 580, "kaus", size=32, farbe=TEXT),
    peep_voll("JE_ruhig", FX, BR, FR, "unter", bis="ae"),
    peep_voll("JG_ernst", FX, BR, FR, "ae", anim="cut"),
    ficon("tabler", "phone", 1330, 520, 100, "ae", fuell=BLAU),
    pille("an Karl", 1330, 360, beim("ae", "Karl"), fill=GRUEN, size=30, anker="m", bis="grund"),
    pille("gewollt: 750 €", FX - 60, 170, beim("grund", "siebenhundertfünfzig"), fill=GRUEN, size=34, anker="m"),
    pille("gesagt: 570 €", FX - 60, 260, beim("grund", "versprochen"), fill=ROT, size=34, anker="m"),
])

# J2 Anfechtungsfrist, Folge -------------------------------------------------------------------------------------------------
folie([("frist", f"{PA} › Frist, § 121 BGB"), ("ue_erg", f"{P0} › II. Anspruch untergegangen (+)")], [
    *tafel("frist", "II. Anfechtung: Frist und Folge"),
    ok(135, 225, "frist", gr=24), z("3. Frist: unverzüglich, § 121 I BGB", 175, 200, "frist", "Bold", 36),
    z("Anruf noch am selben Abend", 215, 258, beim("frist", "Er"), size=34, farbe=TEXT),
    fl_block(110, 350, 1040, 160, ROT, "ue_erg", [("Vertrag nichtig, § 142 I BGB", "ExtraBold", 42, INK),
                                                ("II. Anspruch untergegangen (+)", "Regular", 34, INK)]),
    pille("Karl: allenfalls Vertrauensschaden, § 122 BGB", 110, 570, "vt", fill=GELB, size=34),
    ficon("tabler", "moon-stars", 1390, 260, 120, "frist", fuell=GELB),
    ficon("tabler", "clock", 1690, 260, 130, beim("frist", "unverzüglich"), fuell=WEISS),
    peep_voll("KA_denkt", FX, BR, FR, "frist", bis="ue_erg"),
    peep_voll("KA_muede", FX, BR, FR, "ue_erg", anim="cut"),
])

# K III. Durchsetzbar, Ergebnis ------------------------------------------------------------------------------------------------
folie([("durch", f"{P0} › III. Durchsetzbar"), ("erg", "Ergebnis")], [
    *tafel("durch", "III. Anspruch durchsetzbar?"),
    z("Einreden, z. B. Verjährung, § 214 I BGB", 110, 200, beim("durch", "Einreden"), "Bold", 36),
    z("hier nicht mehr zu prüfen", 150, 262, beim("durch", "Darauf"), size=34, farbe=TEXT),
    fl_block(110, 380, 1040, 160, ROT, "erg", [("Ergebnis: kein Anspruch", "ExtraBold", 42, INK),
                                             ("auf das E-Bike für 570 €", "Regular", 36, INK)]),
    ficon("tabler", "hourglass", 1560, 330, 110, beim("durch", "Verjährung"), fuell=GELB, bis="erg"),
    *ebike(1560, 360, 250, "erg"),
    kreuz_i(1560, 270, beim("erg", "nicht"), gr=50),
    peep_voll("KA_muede", FX, BR, FR, "durch"),
])

# L Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Anfechtung beim Untergang"), ("tipp2", "Klausurtipp · Irrtum des Vertreters, § 166 I BGB")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Anfechtung erst beim Untergang", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("des Anspruchs prüfen", 200, 250, beim("tipp", "Prüfe"), "Bold", 36),
    z("bis zur Anfechtung ist der Vertrag wirksam", 215, 320, beim("tipp", "Bis"), size=34, farbe=TEXT),
    ok(175, 445, "tipp2", gr=22), z("Irrtum: Wer hat die Erklärung abgegeben?", 215, 425, "tipp2", "Bold", 34),
    z("Vertreter verspricht sich → sein Irrtum zählt,", 215, 485, beim("tipp2", "Hätte"), size=34),
    z("§ 166 I BGB", 215, 535, beim("tipp2", "Paragraf"), "Bold", 34),
    *redet("LX_warnt", LXX, BR, FR + 60, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# M Klausurschema ------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 200, 260
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Anspruch prüfen", 110, 90, "sch", 54),
    z("Anspruchsgrundlage, z. B. § 433 I 1 BGB", K1, 195, "sch", "Bold", 36, rechts=1820),
    z("I. Anspruch entstanden", K2, 260, "s1a", "Bold", 38, rechts=1820),
    z("1. Einigung: Angebot und Annahme, §§ 145 ff. BGB", K3, 318, beim("s1a", "Erstens"), size=34, farbe=TEXT, rechts=1820),
    z("2. ggf. Stellvertretung, § 164 I BGB: eigene Erklärung, im fremden Namen, Vertretungsmacht",
      K3, 370, "s1b", size=34, farbe=TEXT, rechts=1820),
    z("3. keine Wirksamkeitshindernisse, z. B. Geschäftsfähigkeit, Form", K3, 422, "s1c", size=34, farbe=TEXT, rechts=1820),
    z("II. Anspruch untergegangen", K2, 500, "s2", "Bold", 38, rechts=1820),
    z("z. B. Anfechtung: Erklärung (§ 143), Grund (§§ 119 ff.), Frist (§ 121) → § 142 I BGB", K3, 558,
      beim("s2", "Anfechtung"), size=34, farbe=TEXT, rechts=1820),
    z("III. Anspruch durchsetzbar", K2, 636, "s3", "Bold", 38, rechts=1820),
    z("keine Einreden, z. B. Verjährung (§ 214 I BGB)", K3, 694, beim("s3", "keine"), size=34, farbe=TEXT, rechts=1820),
])

# N Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Auch ein wirksam geschlossener", 0)], [("Vertrag kann durch ", 0), ("Anfechtung", "a")],
                 [("rückwirkend entfallen.", "b")]], 750, 310, 52, "merke",
                {"a": beim("merke", "Anfechtung"), "b": beim("merke", "rückwirkend")}),
    *markertext([[("Darum immer in drei Schritten:", 0)], [("entstanden", "c"), (" · ", 0), ("untergegangen", "d"), (" · ", 0),
                                                         ("durchsetzbar", "e")]],
                750, 620, 44, "m2", {"c": beim("m2", "entstanden"), "d": beim("m2", "untergegangen"), "e": beim("m2", "durchsetzbar")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
