"""Folge 014 · Angebot und Annahme §§ 145 ff. BGB: Wann ist der Vertrag geschlossen? – Serienstandard Open Peeps
(Katzenkönig). Szenen laut ../SZENENPLAN.md: A Probefahrt, B E-Mails der Woche, C Sachverhalt, D Anspruch/Vertrag,
E I. Angebot, F II. Bindung/Widerruf, G III. Annahme/Ergebnis, H Gegenfall Samstag, I Gegenfall ohne Frist,
J Gegenfall Telefon, K Klausurtipp (Lexi), L Klausurschema, M Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Schlüsselübergabe, Telefon klingelt)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_014/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def bis_(el, bis):
    el.bis = bis
    return el


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def rechts_frei(els, x0=1250):
    """Figuren und Requisiten der Tafelfolien stehen rechts der Tafel (x ≥ 1250)."""
    for e in els:
        n = e.name or ""
        if n.startswith(("bild:", "ficon:")):
            assert e.x >= x0, f"{n} ragt in die Tafel ({e.x} < {x0})"
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


TAGE = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"]


def woche(x0, y, cue, schritt=96, size=28, tage=TAGE, hervor=(), bis=None):
    """Wochenleiste: ein Feld je Tag; hervor = [(Tag, Farbe, von, bis)] legt farbige Felder darüber."""
    els = []
    for i, t in enumerate(tage):
        els.append(pille(t, x0 + i * schritt, y, cue, fill=WEISS, size=size, anker="m", anim="fade", bis=bis))
    for t, farbe, von, b in hervor:
        i = tage.index(t)
        els.append(pille(t, x0 + i * schritt, y, von, fill=farbe, size=size, anker="m", anim="cut", bis=b))
    return els


def tag_x(x0, t, schritt=96):
    return x0 + TAGE.index(t) * schritt


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel: Gerd links, Lotte rechts

# A Fall: die Probefahrt ----------------------------------------------------------------------------------------------
GX, LX_A = 330, 1500
folie([(NULL, "Fall · Die Probefahrt")], [
    pille("Samstag", 70, 40, NULL, fill=GELB, size=44),
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    ficon("tabler", "car", 880, BODEN - 4, 480, NULL, fuell=BLAU),
    peep_voll("GE_ruhig_r", GX, BODEN, FH, NULL, bis="probe"),
    peep_voll("GE_froh_r", GX, BODEN, FH, "probe", anim="cut"),
    namensschild("Gerd", GX, BODEN, NULL, BLAU),
    pille("alter Kombi", 880, 450, beim("fall", "Kombi"), fill=WEISS, size=34, anker="m"),
    pille("zu verkaufen", 880, 360, beim("fall", "verkaufen"), fill=GELB, size=30, anker="m", bis="probe"),
    peep_voll("LO_ruhig", LX_A, BODEN, FH, beim("probe", "Lotte"), anim="fade", bis=beim("probe", "Probefahrt")),
    peep_voll("LO_froh", LX_A, BODEN, FH, beim("probe", "Probefahrt"), anim="cut"),
    namensschild("Lotte", LX_A, BODEN, beim("probe", "Lotte"), LILA),
    # Gerd gibt Lotte den Schlüssel für die Probefahrt
    szene(bewegt(ficon("tabler", "key", LX_A - 150, 640, 80, beim("probe", "Lotte", ende=True), fuell=GELB),
                 beim("probe", "Lotte", ende=True), beim("probe", "Probefahrt"), -(LX_A - 150 - GX - 150), 0),
          "014schluessel*", 0.8),
    pille("Probefahrt", 880, 360, beim("probe", "Probefahrt"), fill=GRUEN, size=34, anker="m"),
])

# B Fall: die E-Mails der Woche ---------------------------------------------------------------------------------------
GX, LX = 300, 1600
W0 = 670                                # Mitte des Feldes „So“ in der Wochenleiste
LAP = (620, 650)                        # Laptop auf Gerds Tisch (Mitte, Unterkante)
HANDY = (1500, 650)                     # Lottes Handy
MAILY = 600
folie([("mail", "Fall · Die E-Mail am Sonntag"), ("anruf", "Fall · Mittwoch: Malte ruft an"),
       ("donn", "Fall · Donnerstag: Lottes Antwort"), ("frage", "Fall · Die Frage")], [
    *woche(W0, 40, "mail", hervor=[("So", GELB, "mail", "anruf"), ("Mi", GELB, "anruf", "donn"),
                                    ("Do", GELB, "donn", None)]),
    linienzug([(W0 - 40, 112), (tag_x(W0, "Fr") + 40, 112)], beim("g1", "Freitag"), breite=6, farbe=DROT),
    pille("Frist bis Freitag", (W0 + tag_x(W0, "Fr")) / 2, 122, beim("g1", "Freitag"), fill=ROT, size=26, anker="m"),
    linienzug([(60, BODEN), (1860, BODEN)], "mail", breite=7, farbe=INK),
    # Gerd zu Hause am Tisch mit Laptop
    ficon("tabler", "desk", 640, BODEN - 4, 300, "mail", fuell=GELB),
    ficon("tabler", "device-laptop", LAP[0], LAP[1], 150, "mail", fuell=WEISS, d=0.1),
    peep_voll("GE_ruhig_r", GX, BODEN, FH, "mail", bis="g1"),
    *redet("GE_redet_r", GX, BODEN, FH, "g1", "liest"),
    peep_voll("GE_ruhig_r", GX, BODEN, FH, "liest", anim="cut", bis="anruf"),
    peep_voll("GE_denkt_r", GX, BODEN, FH, "anruf", anim="cut", bis="zurueck"),
    peep_voll("GE_ruhig_r", GX, BODEN, FH, "zurueck", anim="cut", bis="l1"),
    peep_voll("GE_sorge_r", GX, BODEN, FH, "l1", anim="cut", bis="g2"),
    *redet("GE_protest_r", GX, BODEN, FH, "g2", "frage"),
    peep_voll("GE_aerger_r", GX, BODEN, FH, "frage", anim="cut"),
    namensschild("Gerd", GX, BODEN, "mail", BLAU),
    # Lotte mit Handy
    ficon("tabler", "device-mobile", HANDY[0], HANDY[1], 70, "mail", fuell=WEISS, d=0.1),
    peep_voll("LO_ruhig", LX, BODEN, FH, "mail", bis="liest"),
    peep_voll("LO_froh", LX, BODEN, FH, "liest", anim="cut", bis="zurueck"),
    peep_voll("LO_sorge", LX, BODEN, FH, "zurueck", anim="cut", bis="donn"),
    peep_voll("LO_ruhig", LX, BODEN, FH, "donn", anim="cut", bis="l1"),
    *redet("LO_redet", LX, BODEN, FH, "l1", "g2"),
    peep_voll("LO_ueberlegt", LX, BODEN, FH, "g2", anim="cut"),
    namensschild("Lotte", LX, BODEN, "mail", LILA),
    # Sonntag: Gerds Angebot per E-Mail
    bewegt(ficon("tabler", "mail", HANDY[0], MAILY, 90, beim("mail", "E-Mail"), fuell=GELB, bis="liest"),
           beim("mail", "E-Mail"), beim("mail", "E-Mail", ende=True), LAP[0] - HANDY[0], 0),
    blase("sprech", 860, 260, "g1", 960, 330, inhalt=["Liebe Lotte, du kannst den Kombi", "für viertausend Euro haben.",
                                                     "Mein Angebot gilt bis Freitag."], textsize=34,
          figur=("GE_redet_r", GX, BODEN, FH), bis="liest"),
    ficon("tabler", "mail-opened", HANDY[0], MAILY, 90, "liest", fuell=GELB, bis="zurueck"),
    pille("gelesen: Sonntag", HANDY[0], 420, beim("liest", "Sonntag"), fill=GRUEN, size=28, anker="m", bis="zurueck"),
    # Mittwoch: Malte ruft an
    szene(ficon("tabler", "phone-call", 470, 430, 80, beim("anruf", "ruft"), fuell=GRUEN, bis="zurueck"),
          "014telefon*", 0.55),
    bis_(karte(820, 380, 400, 380, beim("anruf", "Malte"), fill=(226, 236, 252, 255)), "zurueck"),
    peep_voll("MA_ruhig", 1020, 755, 320, beim("anruf", "Malte"), bis="m1"),
    *redet("MA_redet", 1020, 755, 320, "m1", "zurueck"),
    pille("Malte am Telefon", 1020, 785, beim("anruf", "Malte"), fill=ORANGE, size=28, anker="m", bis="zurueck"),
    blase("sprech", 820, 190, "m1", 1020, 285, inhalt=["Ich zahle Ihnen viertausendfünfhundert", "Euro für den Wagen."],
          textsize=32, figur=("MA_redet", 1020, 755, 320), bis="zurueck"),
    # Gerds zweite Mail: Widerruf
    bewegt(ficon("tabler", "mail-x", HANDY[0], MAILY, 90, beim("zurueck", "schreibt"), fuell=ROT, bis="donn"),
           beim("zurueck", "schreibt"), beim("zurueck", "sofort", ende=True), LAP[0] - HANDY[0], 0),
    pille("„Ich ziehe mein Angebot zurück.“", 1010, 400, beim("zurueck", "Ich"), fill=ROT, size=32, anker="m", bis="donn"),
    # Donnerstag: Lottes Annahme
    bewegt(ficon("tabler", "mail-check", LAP[0], LAP[1] - 160, 90, beim("donn", "antwortet"), fuell=GRUEN),
           beim("donn", "antwortet"), beim("donn", "trotzdem", ende=True), HANDY[0] - LAP[0], MAILY - LAP[1] + 160),
    pille("gelesen: Donnerstagmittag", LAP[0], 300, beim("donn", "Gerd"), fill=GRUEN, size=28, anker="m", bis="l1"),
    blase("sprech", 620, 180, "l1", 1150, 330, inhalt=["Ich nehme den Kombi", "für viertausend Euro!"], textsize=34,
          figur=("LO_redet", LX, BODEN, FH), bis="g2"),
    blase("sprech", 700, 180, "g2", 760, 330, inhalt=["Aber ich habe mein Angebot", "doch zurückgezogen!"], textsize=34,
          figur=("GE_protest_r", GX, BODEN, FH), bis="frage"),
    pille("Ist der Kombi jetzt an Lotte verkauft?", 1000, 230, "frage", fill=PINK, size=40, anker="m"),
    pille("Wann genau kam der Vertrag zustande?", 1000, 320, beim("frage", "wann"), fill=PINK, size=36, anker="m"),
])

# C Sachverhalt -------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Gerd möchte seinen alten Kombi verkaufen. Am Samstag macht Lotte eine Probefahrt. Am Sonntagabend schreibt Gerd "
    "ihr per E-Mail: „Liebe Lotte, du kannst den Kombi für 4.000 Euro haben. Mein Angebot gilt bis Freitag.“ Lotte liest "
    "die Mail noch am Sonntag.",
    "Am Mittwoch bietet Malte Gerd am Telefon 4.500 Euro. Gerd schreibt Lotte sofort: „Ich ziehe mein Angebot zurück.“ "
    "Am Donnerstagmittag antwortet Lotte per E-Mail: „Ich nehme den Kombi für 4.000 Euro!“ Gerd liest die Mail gleich "
    "und meint, er habe sein Angebot doch zurückgezogen.",
    "(Frei erfundener Übungsfall.)",
], "Kann Lotte von Gerd den Kombi verlangen – und wann kam der Vertrag zustande?")

# D Anspruch und Vertrag ----------------------------------------------------------------------------------------------
folie([("ansp", "Lotte gegen Gerd · § 433 I 1 BGB"), ("vertrag", "Kaufvertrag · Angebot und Annahme, §§ 145 ff. BGB")],
      rechts_frei([
    *tafel("ansp", "Lotte gegen Gerd: der Kombi"),
    z("Anspruch: § 433 Abs. 1 S. 1 BGB", 110, 200, beim("ansp", "Paragraf"), "Bold", 40),
    z("Voraussetzung: ein Kaufvertrag", 110, 290, "vertrag", "Bold", 38),
    z("zwei passende Willenserklärungen", 150, 350, beim("vertrag", "zwei"), size=36),
    fl_block(110, 460, 500, 150, GELB, beim("vertrag", "Angebot"), [("Angebot", "ExtraBold", 44, INK),
                                                                    ("Gerd", "Regular", 34, INK)]),
    fl_block(650, 460, 500, 150, GRUEN, beim("vertrag", "Annahme"), [("Annahme", "ExtraBold", 44, INK),
                                                                     ("Lotte", "Regular", 34, INK)]),
    z("§§ 145 ff. BGB", 110, 660, beim("vertrag", "Paragrafen"), "Bold", 38),
    ficon("tabler", "car", (X1 + X2) // 2, 380, 260, "ansp", fuell=BLAU),
    peep_voll("GE_ruhig", X1, BR, FR, "ansp"),
    peep_voll("LO_ruhig", X2, BR, FR, "ansp", d=0.2, bis="vertrag"),
    peep_voll("LO_denkt", X2, BR, FR, "vertrag", anim="cut"),
    namensschild("Gerd", X1, BR, "ansp", BLAU, d=0.2),
    namensschild("Lotte", X2, BR, "ansp", LILA, d=0.3),
]))

# E I. Angebot ----------------------------------------------------------------------------------------------------------
folie([("ang", "I. Angebot › wesentliche Punkte"), ("rbw", "I. Angebot › Rechtsbindungswille"),
       ("zug", "I. Angebot › Zugang, § 130 I 1 BGB")], rechts_frei([
    *tafel("ang", "I. Angebot (Gerd, Sonntag)"),
    z("wesentliche Punkte:", 110, 190, "ess", "Bold", 36),
    pille("Ware: Kombi", 110, 245, beim("ess", "Ware"), fill=BLAU, size=28),
    pille("Preis: 4.000 €", 390, 245, beim("ess", "Preis"), fill=GELB, size=28),
    pille("Vertragspartner: Gerd, Lotte", 690, 245, beim("ess", "Vertragspartner"), fill=LILA, size=28),
    ok(135, 350, "ja", gr=22), z("Lotte muss nur noch „Ja“ sagen können", 175, 330, "ja", size=34),
    z("Bindungswille: Gerd will sich erkennbar binden", 110, 410, "rbw", "Bold", 36),
    ok(175, 490, beim("rbw", "deutlicher"), gr=22), z("„Mein Angebot gilt bis Freitag.“", 215, 470, beim("rbw", "Mein"), size=34),
    nein(175, 550, "inv", gr=22),
    z("Werbeschreiben: nur Einladung zum Angebot", 215, 530, "inv", size=34, farbe=TEXT),
    z("E-Mail: Erklärung unter Abwesenden", 110, 610, "zug", "Bold", 36),
    z("wirksam mit Zugang, § 130 Abs. 1 S. 1 BGB", 150, 665, beim("zug", "Zugang"), size=34),
    ok(175, 740, beim("zug", "gelesen"), gr=22), z("Lotte hat sie am Sonntag gelesen", 215, 720, beim("zug", "Lotte"), size=34),
    fl_block(110, 790, 1040, 90, GRUEN, "ang_ok", [("Das Angebot ist wirksam.", "ExtraBold", 38, INK)]),
    # rechts: die drei Punkte als Requisiten, dann die Mail
    ficon("tabler", "car", 1420, 360, 170, beim("ess", "Ware"), fuell=BLAU, bis="rbw"),
    ficon("tabler", "currency-euro", 1590, 360, 110, beim("ess", "Preis"), fuell=GELB, bis="rbw"),
    ficon("tabler", "users", 1760, 360, 120, beim("ess", "Vertragspartner"), fuell=LILA, bis="rbw"),
    ficon("tabler", "mail", 1560, 360, 140, "rbw", fuell=GELB, bis="inv"),
    pille("gilt bis Freitag", 1560, 160, beim("rbw", "Mein"), fill=ROT, size=28, anker="m", bis="inv"),
    ficon("tabler", "speakerphone", 1560, 360, 140, "inv", fuell=WEISS, bis="zug"),
    pille("Werbeschreiben", 1560, 160, "inv", fill=WEISS, size=28, anker="m", bis="zug"),
    ficon("tabler", "mail-opened", 1720, 380, 120, beim("zug", "Lotte"), fuell=GELB),
    peep_voll("GE_ruhig", X1, BR, FR, "ang", bis="rbw"),
    peep_voll("GE_froh", X1, BR, FR, "rbw", anim="cut"),
    peep_voll("LO_ruhig", X2, BR, FR, "ang", d=0.2, bis="ja"),
    peep_voll("LO_froh", X2, BR, FR, "ja", anim="cut"),
    namensschild("Gerd", X1, BR, "ang", BLAU, d=0.2),
    namensschild("Lotte", X2, BR, "ang", LILA, d=0.3),
]))

# F II. Bindung und Widerruf ------------------------------------------------------------------------------------------
TX0 = 260                                # Zeitleiste in der Tafel
folie([("bind", "II. Bindung › § 145 BGB"), ("p130", "II. Bindung › Widerruf, § 130 I 2 BGB")], rechts_frei([
    *tafel("bind", "II. Bindung und Widerruf"),
    pille("Durfte Gerd am Mittwoch zurückziehen?", 110, 180, "bind", fill=PINK, size=32),
    z("§ 145 BGB: Gerd ist an sein Angebot gebunden", 110, 280, "p145", "Bold", 36),
    z("außer: Bindung ausgeschlossen", 150, 335, beim("p145", "außer"), size=34, farbe=TEXT),
    z("§ 130 Abs. 1 S. 2 BGB: Widerruf wirkt nur,", 110, 415, "p130", "Bold", 36),
    z("wenn er vorher oder gleichzeitig zugeht", 150, 470, beim("p130", "vorher"), size=34),
    *woche(TX0, 560, "spaet", schritt=120, tage=TAGE[:4],
           hervor=[("So", GELB, "spaet", None), ("Mi", ROT, beim("spaet", "kam"), None)]),
    pille("Angebot zugegangen", TX0, 630, "spaet", fill=WEISS, size=26, anker="m"),
    pille("Widerruf", tag_x(TX0, "Mi", 120), 630, beim("spaet", "kam"), fill=ROT, size=26, anker="m"),
    nein(tag_x(TX0, "Mi", 120) + 120, 650, beim("spaet", "spät"), gr=26),
    pille("drei Tage zu spät", 820, 560, beim("spaet", "drei"), fill=ROT, size=30),
    fl_block(110, 760, 1040, 100, GRUEN, beim("spaet", "Das"), [("Das Angebot steht.", "ExtraBold", 40, INK)]),
    ficon("tabler", "mail-x", X1, 380, 120, "p130", fuell=ROT),
    ficon("tabler", "mail", X2, 380, 120, "bind", fuell=GELB),
    peep_voll("GE_denkt", X1, BR, FR, "bind", bis="spaet"),
    peep_voll("GE_aerger", X1, BR, FR, "spaet", anim="cut"),
    peep_voll("LO_ruhig", X2, BR, FR, "bind", d=0.2, bis=beim("spaet", "Das")),
    peep_voll("LO_froh", X2, BR, FR, beim("spaet", "Das"), anim="cut"),
    namensschild("Gerd", X1, BR, "bind", BLAU, d=0.2),
    namensschild("Lotte", X2, BR, "bind", LILA, d=0.3),
]))

# G III. Annahme und Ergebnis -----------------------------------------------------------------------------------------
TX1 = 200
folie([("ann", "III. Annahme › deckungsgleich"), ("aend", "III. Annahme › Änderungen, § 150 II BGB"),
       ("frist", "III. Annahme › rechtzeitig, § 148 BGB"), ("erg", "Ergebnis · Vertrag am Donnerstag geschlossen")],
      rechts_frei([
    *tafel("ann", "III. Annahme (Lotte, Donnerstag)"),
    ok(135, 210, beim("deck", "genau"), gr=22), z("deckungsgleich: genau dieser Kombi, dieser Preis", 175, 190, "deck", "Bold", 34),
    z("„3.500 €“ wäre Ablehnung + neues Angebot,", 175, 250, "aend", size=32, farbe=TEXT),
    z("§ 150 Abs. 2 BGB", 175, 295, beim("aend", "Paragraf"), size=32, farbe=TEXT),
    z("rechtzeitig: Frist bis Freitag, § 148 BGB", 110, 370, "frist", "Bold", 34),
    *woche(TX1, 440, beim("frist", "Frist"), schritt=110,
           hervor=[("Fr", ROT, beim("frist", "Freitag"), None), ("Do", GRUEN, "do", None)]),
    linienzug([(TX1 - 40, 510), (tag_x(TX1, "Fr", 110) + 40, 510)], beim("frist", "Freitag"), breite=6, farbe=DROT),
    ok(tag_x(TX1, "Do", 110), 560, "do", gr=24),
    pille("Lottes Antwort", tag_x(TX1, "Do", 110) - 230, 530, "do", fill=GRUEN, size=26),
    fl_block(110, 620, 1040, 130, GRUEN, "erg", [("Kaufvertrag geschlossen:", "Bold", 36, INK),
                                                ("Donnerstagmittag, als die Antwort ankam", "ExtraBold", 36, INK)]),
    z("Gerd muss übergeben und übereignen, § 433 I 1 BGB", 110, 790, "pflicht", "Bold", 34),
    ficon("tabler", "mail-check", X2, 380, 120, "deck", fuell=GRUEN, bis="pflicht"),
    pille("3.500 €?", X2, 160, "aend", fill=WEISS, size=28, anker="m", bis="frist"),
    ficon("tabler", "calendar-event", X1, 380, 110, "frist", fuell=WEISS, bis="pflicht"),
    bewegt(ficon("tabler", "car", X2, 380, 200, "pflicht", fuell=BLAU), "pflicht", beim("pflicht", "übergeben", ende=True),
           X1 - X2, 0),
    peep_voll("GE_ruhig", X1, BR, FR, "ann", bis="erg"),
    peep_voll("GE_sorge", X1, BR, FR, "erg", anim="cut"),
    peep_voll("LO_ruhig", X2, BR, FR, "ann", d=0.2, bis="erg"),
    peep_voll("LO_froh", X2, BR, FR, "erg", anim="cut"),
    namensschild("Gerd", X1, BR, "ann", BLAU, d=0.2),
    namensschild("Lotte", X2, BR, "ann", LILA, d=0.3),
]))

# H Gegenfall: Antwort erst am Samstag --------------------------------------------------------------------------------
TX2 = 200
folie([("sams", "Gegenfall · Antwort erst am Samstag"), ("p150", "Gegenfall · neues Angebot, § 150 I BGB")], rechts_frei([
    *tafel("sams", "Gegenfall: Antwort am Samstag"),
    *woche(TX2, 190, "sams", schritt=110, hervor=[("Fr", ROT, "sams", None), ("Sa", ORANGE, beim("sams", "Samstag"), None)]),
    linienzug([(TX2 - 40, 260), (tag_x(TX2, "Fr", 110) + 40, 260)], "sams", breite=6, farbe=DROT),
    nein(135, 345, "p146", gr=22), z("Gerds Angebot ist erloschen, § 146 BGB", 175, 325, "p146", "Bold", 34),
    z("Lottes verspätete Annahme = neues Angebot,", 110, 420, "p150", "Bold", 34),
    z("§ 150 Abs. 1 BGB", 150, 470, beim("p150", "Paragraf"), size=34),
    z("Jetzt muss Gerd annehmen.", 110, 555, "jetzt", size=34),
    fl_block(110, 650, 1040, 120, ROT, "schweig", [("Schweigen ist grundsätzlich", "Bold", 36, INK),
                                                  ("keine Annahme.", "ExtraBold", 38, INK)]),
    bewegt(ficon("tabler", "mail", X1, 380, 110, beim("sams", "antwortet"), fuell=ORANGE, bis="schweig"),
           beim("sams", "antwortet"), beim("sams", "Samstag", ende=True), X2 - X1, 0),
    pille("neues Angebot", X1, 160, "p150", fill=ORANGE, size=28, anker="m"),
    ficon("tabler", "message-off", X1, 380, 110, "schweig", fuell=WEISS),
    peep_voll("GE_ruhig", X1, BR, FR, "sams", bis="jetzt"),
    peep_voll("GE_denkt", X1, BR, FR, "jetzt", anim="cut"),
    peep_voll("LO_ruhig", X2, BR, FR, "sams", d=0.2, bis="p146"),
    peep_voll("LO_sorge", X2, BR, FR, "p146", anim="cut"),
    namensschild("Gerd", X1, BR, "sams", BLAU, d=0.2),
    namensschild("Lotte", X2, BR, "sams", LILA, d=0.3),
]))

# I Gegenfall: ohne Frist ---------------------------------------------------------------------------------------------
folie([("ohne", "Gegenfall · ohne Frist, § 147 II BGB")], rechts_frei([
    *tafel("ohne", "Gegenfall: ohne Frist"),
    z("§ 147 Abs. 2 BGB", 110, 190, beim("ohne", "Paragraf"), "Bold", 40),
    z("Annahme möglich, solange Gerd unter", 110, 270, "regel", size=36),
    z("regelmäßigen Umständen mit der Antwort", 110, 320, beim("regel", "regelmäßigen"), size=36),
    z("rechnen darf", 110, 370, beim("regel", "rechnen"), size=36),
    z("Bundesgerichtshof: Die Frist setzt sich zusammen aus", 110, 460, "drei", "Bold", 32),
    fl_block(110, 530, 300, 120, BLAU, beim("drei", "Hinweg"), [("Hinweg", "ExtraBold", 36, INK)]),
    fl_block(430, 530, 400, 120, GELB, beim("drei", "Überlegungszeit"), [("Überlegungszeit", "ExtraBold", 36, INK)]),
    fl_block(850, 530, 300, 120, BLAU, beim("drei", "Rückweg"), [("Rückweg", "ExtraBold", 36, INK)]),
    z("BGH, Urt. v. 11.6.2010 – V ZR 85/09, Rn. 11", 110, 700, beim("drei", "Bundesgerichtshof"), size=28, farbe=TEXT),
    bewegt(ficon("tabler", "mail", X2, 300, 100, beim("drei", "Hinweg"), fuell=GELB, bis=beim("drei", "Überlegungszeit")),
           beim("drei", "Hinweg"), beim("drei", "Hinweg", ende=True), X1 - X2, 0),
    ficon("tabler", "hourglass", X2, 300, 100, beim("drei", "Überlegungszeit"), fuell=GELB, bis=beim("drei", "Rückweg")),
    bewegt(ficon("tabler", "mail-check", X1, 300, 100, beim("drei", "Rückweg"), fuell=GRUEN),
           beim("drei", "Rückweg"), beim("drei", "Rückweg", ende=True), X2 - X1, 0),
    ficon("tabler", "clock", (X1 + X2) // 2, 300, 110, "ohne", fuell=WEISS, bis=beim("drei", "Hinweg")),
    peep_voll("GE_ruhig", X1, BR, FR, "ohne"),
    peep_voll("LO_ruhig", X2, BR, FR, "ohne", d=0.2, bis=beim("drei", "Überlegungszeit")),
    peep_voll("LO_ueberlegt", X2, BR, FR, beim("drei", "Überlegungszeit"), anim="cut"),
    namensschild("Gerd", X1, BR, "ohne", BLAU, d=0.2),
    namensschild("Lotte", X2, BR, "ohne", LILA, d=0.3),
]))

# J Gegenfall: am Telefon ---------------------------------------------------------------------------------------------
folie([("tel", "Gegenfall · am Telefon, § 147 I BGB")], rechts_frei([
    *tafel("tel", "Gegenfall: am Telefon"),
    z("Anruf: Gespräch von Person zu Person", 110, 200, "anw", "Bold", 36),
    z("wie unter Anwesenden", 150, 255, beim("anw", "wie"), size=34),
    z("§ 147 Abs. 1 BGB: nur sofort annehmen", 110, 345, beim("anw", "Paragraf"), "Bold", 36),
    ok(135, 455, "sofort", gr=22), z("„Deal!“ sofort: Vertrag geschlossen", 175, 435, "sofort", size=34),
    nein(135, 535, "spaeter", gr=22), z("später zugesagt: nur neues Angebot", 175, 515, "spaeter", size=34),
    ficon("tabler", "device-mobile", X1 - 70, 560, 50, "tel", fuell=WEISS),
    ficon("tabler", "device-mobile", X2 - 70, 560, 50, "tel", fuell=WEISS),
    peep_voll("GE_ruhig", X1, BR, FR, "tel", bis="sofort"),
    peep_voll("GE_froh", X1, BR, FR, "sofort", anim="cut"),
    peep_voll("LO_ruhig", X2, BR, FR, "tel", d=0.2, bis="deal"),
    *redet("LO_redet", X2, BR, FR, "deal", "sofort"),
    peep_voll("LO_froh", X2, BR, FR, "sofort", anim="cut"),
    namensschild("Gerd", X1, BR, "tel", BLAU, d=0.2),
    namensschild("Lotte", X2, BR, "tel", LILA, d=0.3),
    blase("sprech", 420, 160, "deal", 1640, 230, inhalt=["Deal! Abgemacht."], textsize=36,
          figur=("LO_redet", X2, BR, FR), bis="spaeter"),
    pille("Kombi für 4.000 €?", X1, 250, beim("anw", "Bietet"), fill=GELB, size=28, anker="m", bis="deal"),
]))

# K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
LXX, TX3 = 1560, 200
folie([("tipp", "Klausurtipp · Zeitleiste")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Mal dir eine Zeitleiste.", 200, 200, beim("tipp", "Mal"), "Bold", 38),
    z("Jede Erklärung mit dem Tag ihres Zugangs", 200, 270, "tipp2", size=34),
    *woche(TX3, 380, "tipp2", schritt=150, tage=TAGE[:6]),
    pille("Angebot", tag_x(TX3, "So", 150), 450, beim("tipp2", "Erklärung"), fill=GELB, size=26, anker="m"),
    pille("Widerruf", tag_x(TX3, "Mi", 150), 450, beim("tipp3", "Widerruf"), fill=ROT, size=26, anker="m"),
    pille("Annahme", tag_x(TX3, "Do", 150), 520, beim("tipp3", "Annahme"), fill=GRUEN, size=26, anker="m"),
    pille("Fristende", tag_x(TX3, "Fr", 150) + 30, 450, beim("tipp3", "Frist"), fill=WEISS, size=26, anker="m"),
    nein(tag_x(TX3, "Mi", 150), 620, beim("tipp3", "spät"), gr=24),
    z("Widerruf zu spät?", 110, 680, beim("tipp3", "Widerruf"), size=34),
    ok(tag_x(TX3, "Do", 150), 620, beim("tipp3", "Frist"), gr=24),
    z("Annahme in der Frist?", 600, 680, beim("tipp3", "Annahme"), size=34),
    *redet("LX_warnt", LXX, BR, 560, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# L Klausurschema -----------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Lotte gegen Gerd, § 433 Abs. 1 S. 1 BGB", 110, 90, "sch", 46),
    z("I. Angebot (Gerd)", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("1. wesentliche Punkte und Rechtsbindungswille", K2, 255, "k1a", size=34, rechts=1820),
    z("2. wirksam mit Zugang, § 130 Abs. 1 S. 1 BGB", K2, 307, "k1b", size=34, rechts=1820),
    z("II. Bindung, § 145 BGB: kein wirksamer Widerruf, § 130 Abs. 1 S. 2 BGB", K1, 380, "k2", "Bold", 38, rechts=1820),
    z("III. Annahme (Lotte)", K1, 455, "k3", "Bold", 38, rechts=1820),
    z("1. deckungsgleich", K2, 510, "k3a", size=34, rechts=1820),
    z("2. rechtzeitig, §§ 147, 148 BGB", K2, 562, "k3b", size=34, rechts=1820),
    *plusminus("IV. Ergebnis: Vertrag geschlossen, Anspruch entstanden", K1, 640, "k4", True, size=38, stil="Bold"),
])

# M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Ein zugegangenes Angebot ", 0), ("bindet.", "a")]], 750, 340, 50, "merke",
                {"a": beim("merke", "bindet")}),
    *markertext([[("Der Vertrag steht in der Regel,", 0)], [("sobald die passende Annahme", 0)],
                 [("rechtzeitig zugeht.", "b")]], 750, 500, 46, "m2", {"b": beim("m2", "rechtzeitig")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
