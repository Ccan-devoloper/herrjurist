"""Folge 003 · Gutachtenstil in 6 Minuten (Methodik) – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Flohmarkt, B Klausurfrage, C Sachverhalt, D Obersatz, E Voraussetzung, F Definition,
G/H Subsumtion, I Ergebnis, J Gutachten- gegen Urteilsstil, K typische Fehler, L Klausurtipp (Lexi), M Klausurschema,
N Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Schritte, Fahrradklingel)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_003/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = bausteine.BG_FARBE
PFAD_FARBE = bausteine.PFAD_FARBE
HELL = (255, 251, 230, 255)
DAUER = bausteine._cj()["dauer"]
A = "A. Greta gegen Paul"


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, 50)]


def wortring(text, wort, x, y, size, stil, cue, farbe=ORANGE, bis=None):
    """Handgezeichneter Ring um 'wort' in einer mit z() gesetzten Zeile (text an x, y)."""
    f = F(stil, size)
    i = text.index(wort)
    x0 = x + f.getlength(text[:i]); w = f.getlength(wort)
    return ring(int(x0 + w / 2), int(y + size * 0.42), int(w / 2 + 16), int(size * 0.62), cue, farbe=farbe, breite=6, bis=bis)


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
GX, PX = 1420, 1720                     # Greta, Paul neben der Tafel

# A Fall: Flohmarkt -------------------------------------------------------------------------------------------------------
GA, RAD, PA = 450, 820, 1350            # Greta, Fahrrad, Paul (nach dem Hereingehen)
GREDET = ("GR_redet_r", GA, BODEN, FH)
folie([("markt", "Fall · Der Flohmarkt"), ("morgen", "Fall · Am nächsten Tag")], [
    pille("Der Flohmarkt-Fall", 70, 40, "markt", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "markt", breite=7, farbe=INK),
    ficon("tabler", "lamp", 100, BODEN - 2, 110, "markt", fuell=BLAU, d=0.2),
    ficon("tabler", "armchair", 245, BODEN - 2, 170, "markt", fuell=GELB, d=0.3),
    # Greta
    peep_voll("GR_ruhig_r", GA, BODEN, FH, "markt", bis="g1"),
    *redet("GR_redet_r", GA, BODEN, FH, "g1", "p1"),
    peep_voll("GR_ruhig_r", GA, BODEN, FH, "p1", anim="cut", bis="g2"),
    *redet("GR_redet_r", GA, BODEN, FH, "g2", "faehrt"),
    peep_voll("GR_zufrieden_r", GA, BODEN, FH, "faehrt", anim="cut", bis="achtzig"),
    peep_voll("GR_aerger_r", GA, BODEN, FH, "achtzig", anim="cut"),
    pille("Greta", GA, BODEN + 22, "markt", fill=LILA, size=30, anker="m", d=0.2),
    # das Fahrrad
    ficon("fluent-emoji-high-contrast", "bicycle", RAD, BODEN - 2, 330, "rad", fuell=WEISS, bis="faehrt"),
    pille("altes Fahrrad", RAD, 560, beim("rad", "Fahrrad"), fill=WEISS, size=32, anker="m", bis="g1"),
    # Paul kommt
    szene(bewegt(peep_voll("PA_geht", PA, BODEN, FH, "paul", anim="fade", bis=beim("paul", "fragt")),
                 ("paul", 0.0), beim("paul", "stehen", ende=True), 420), "schritte_flohmarkt_1", 0.8),
    peep_voll("PA_ruhig", PA, BODEN, FH, beim("paul", "fragt"), anim="cut", bis="p1"),
    *redet("PA_redet", PA, BODEN, FH, "p1", "g2"),
    peep_voll("PA_ruhig", PA, BODEN, FH, "g2", anim="cut", bis="faehrt"),
    pille("Paul", PA, BODEN + 22, beim("paul", "fragt"), fill=GRUEN, size=30, anker="m", bis="faehrt"),
    # Preise und Sprechblasen
    pille("80 €", RAD, 560, beim("g1", "Achtzig"), fill=GELB, size=40, anker="m", bis="p1"),
    pille("70 €", RAD, 560, beim("p1", "siebzig"), fill=ORANGE, size=40, anker="m", bis="faehrt"),
    blase("sprech", 560, 190, "g1", 700, 230, inhalt=["Achtzig Euro, und", "es gehört Ihnen."], textsize=34,
          figur=GREDET, bis="p1"),
    blase("sprech", 660, 200, "p1", 1110, 230, inhalt=["Ich nehme es für siebzig.", "Das Geld bringe ich morgen."], textsize=32,
          figur=("PA_redet", PA, BODEN, FH), bis="g2"),
    blase("sprech", 440, 160, "g2", 720, 250, inhalt=["Na gut, siebzig."], textsize=38, figur=GREDET, bis="faehrt"),
    icon("fluent-emoji-high-contrast", "handshake", RAD, 430, 110, beim("g2", "siebzig"), bis="faehrt"),
    # Paul fährt davon
    szene(bewegt(peep_voll("PA_rad_r", 1520, BODEN, 430, "faehrt", anim="cut", bis="morgen"),
                 ("faehrt", 0.0), beim("faehrt", "davon", ende=True), -620), "fahrradklingel_1", 0.7, versatz=0.25),
    # am nächsten Tag
    ficon("tabler", "calendar", 1400, BODEN - 2, 170, "morgen", fuell=BLAU),
    pille("am nächsten Tag", 1400, 600, "morgen", fill=WEISS, size=32, anker="m", d=0.2),
    ficon("tabler", "coin-euro", 1720, BODEN - 2, 150, beim("morgen", "kein"), fuell=GELB),
    nein(1720, 790, beim("morgen", "Geld"), gr=40),
    pille("kein Geld", 1720, 600, beim("morgen", "Geld"), fill=ROT, size=32, anker="m"),
    pille("verlangt jetzt 80 €", GA, 300, beim("achtzig", "verlangt"), fill=ROT, size=34, anker="m"),
])

# B Klausurfrage ------------------------------------------------------------------------------------------------------------
MX, MB, MF = 1560, 930, 520
folie([("klausur", "Fall · Die Klausurfrage"), ("vier", "Gutachtenstil · Die vier Schritte")], [
    *tafel("klausur", "Klausur · Zivilrecht"),
    ficon("tabler", "clock", 1100, 170, 80, "klausur", fuell=GELB, d=0.3),
    z("Fallfrage:", 110, 200, beim("klausur", "Hat"), "Bold", 38),
    z("Hat Greta gegen Paul einen Anspruch", 110, 260, beim("klausur", "Hat"), size=38),
    z("auf Zahlung von 80 €?", 110, 315, beim("klausur", "achtzig"), size=38),
    z("Gutachtenstil in vier Schritten:", 110, 395, beim("vier", "Gutachtenstil"), "Bold", 38),
    fl_block(110, 700, 260, 160, GELB, beim("vier", "Obersatz"), [("1. Obersatz", "ExtraBold", 30, INK)]),
    fl_block(380, 620, 260, 240, BLAU, beim("vier", "Definition"), [("2. Definition", "ExtraBold", 30, INK)]),
    fl_block(650, 540, 260, 320, LILA, beim("vier", "Subsumtion"), [("3. Subsumtion", "ExtraBold", 30, INK)]),
    fl_block(920, 460, 260, 400, GRUEN, beim("vier", "Ergebnis"), [("4. Ergebnis", "ExtraBold", 30, INK)]),
    peep_voll("MI_denkt", MX, MB, MF, "klausur", bis="mia"),
    *redet("MI_fragt", MX, MB, MF, "mia", "vier"),
    peep_voll("MI_froh", MX, MB, MF, "vier", anim="cut"),
    pille("Mia", MX, MB + 22, "klausur", fill=ROT, size=30, anker="m", d=0.2),
    blase("sprech", 480, 190, "mia", 1450, 210, inhalt=["Und wie schreibe ich", "das jetzt auf?"], textsize=32,
          figur=("MI_fragt", MX, MB, MF), bis="vier"),
])

# C Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Auf einem Flohmarkt bietet Greta ihr altes Fahrrad an. Zu Paul sagt sie: „80 Euro, und es gehört Ihnen.“ "
    "Paul antwortet: „Ich nehme es für 70. Das Geld bringe ich morgen.“ Greta erwidert: „Na gut, 70.“",
    "Paul fährt mit dem Rad davon. Am nächsten Tag zahlt er nicht. Verärgert verlangt Greta nun 80 Euro.",
    "(Frei erfundener Übungsfall.)",
], "Hat Greta gegen Paul einen Anspruch auf Zahlung von 80 €?")

# D Schritt 1: Obersatz ---------------------------------------------------------------------------------------------------------
OB1 = "Greta könnte gegen Paul einen Anspruch auf"
OB2 = "Zahlung von 80 € aus § 433 II BGB haben."
folie([("ob", f"{A}, § 433 II BGB › 1. Obersatz")], [
    *tafel("ob", "1. Obersatz"),
    z("Wer will was von wem woraus?", 110, 200, "wer", "Bold", 40),
    z("Wer?", 150, 280, beim("wer", "Wer"), "Bold", 36, farbe=TEXT),
    z("Was?", 150, 335, beim("wer", "was"), "Bold", 36, farbe=TEXT),
    z("Von wem?", 150, 390, beim("wer", "wem"), "Bold", 36, farbe=TEXT),
    z("Woraus?", 150, 445, beim("wer", "woraus"), "Bold", 36, farbe=TEXT),
    z("Greta", 380, 280, beim("ob_satz", "Greta"), size=36),
    z("Paul", 380, 390, beim("ob_satz", "Paul"), size=36),
    z("Zahlung von 80 €", 380, 335, beim("ob_satz", "achtzig"), size=36),
    z("§ 433 Abs. 2 BGB", 380, 445, beim("ob_satz", "Paragraf"), size=36),
    karte(110, 545, 1040, 150, beim("ob_satz", "haben"), fill=HELL, rund=18, schatten=6, rand=4),
    z(OB1, 150, 575, beim("ob_satz", "haben"), "Bold", 36),
    z(OB2, 150, 630, beim("ob_satz", "haben"), "Bold", 36),
    wortring(OB1, "könnte", 150, 575, 36, "Bold", "konj"),
    pille("Konjunktiv: Ergebnis noch offen", 110, 750, beim("konj", "Ergebnis"), fill=PINK, size=34),
    peep_voll("GR_fordert", GX, BR, FR, "ob"),
    peep_voll("PA_ruhig", PX, BR, FR, "ob", d=0.2),
    pille("Greta", GX, BR + 22, "ob", fill=LILA, size=30, anker="m", d=0.2),
    pille("Paul", PX, BR + 22, "ob", fill=GRUEN, size=30, anker="m", d=0.4),
])

# E Voraussetzung ---------------------------------------------------------------------------------------------------------------
folie([("vor", f"{A} › § 433 II BGB › Voraussetzung: Kaufvertrag")], [
    *tafel("vor", "§ 433 Abs. 2 BGB"),
    z("„Der Käufer ist verpflichtet, dem Verkäufer", 110, 200, "vor", size=36, farbe=TEXT),
    z("den vereinbarten Kaufpreis zu zahlen …“", 110, 255, "vor", size=36, farbe=TEXT),
    pille("vereinbarter Kaufpreis", 110, 340, beim("vor", "vereinbarten"), fill=GELB, size=34),
    z("Voraussetzung:", 110, 470, "vor2", "Bold", 40),
    z("wirksamer Kaufvertrag zwischen Greta und Paul", 110, 535, beim("vor2", "Kaufvertrag"), "Bold", 36),
    pille("„müssten“: wieder Konjunktiv", 110, 640, beim("vor2", "müssten"), fill=PINK, size=34),
    ficon("tabler", "coin-euro", GX, 400, 130, beim("vor", "Kaufpreis"), fuell=GELB),
    ficon("tabler", "file-certificate", PX, 400, 130, beim("vor2", "Kaufvertrag"), fuell=BLAU),
    peep_voll("GR_fordert", GX, BR, FR, "vor"),
    peep_voll("PA_ruhig", PX, BR, FR, "vor", bis="vor2"),
    peep_voll("PA_denkt", PX, BR, FR, "vor2", anim="cut"),
])

# F Schritt 2: Definition -----------------------------------------------------------------------------------------------------------
f38 = F("Regular", 38)
folie([("def", f"{A} › 2. Definition: Vertrag"), ("quelle", f"{A} › 2. Definition › Woher?")], [
    *tafel("def", "2. Definition"),
    z("sagt abstrakt, wann ein Merkmal erfüllt ist", 110, 200, beim("def", "Sie"), size=36, farbe=TEXT),
    z("Vertrag:", 110, 300, "def2", "Bold", 40),
    z("zwei übereinstimmende Willenserklärungen", 150, 365, beim("def2", "zwei"), "Bold", 38),
    z("Angebot", 190, 440, beim("def2", "Angebot"), size=38),
    z("+ Annahme", 190 + f38.getlength("Angebot ") + 6, 440, beim("def2", "Annahme"), size=38),
    z("§§ 145 ff. BGB", 150, 515, beim("def2", "Paragrafen"), size=36, farbe=TEXT),
    pille("BGH, Urt. v. 17.12.2025 – VIII ZR 56/25, Rn. 34", 110, 690, "bgh", fill=GRUEN, size=30),
    ficon("tabler", "message", 1420, 420, 190, beim("def2", "Angebot"), fuell=GELB, bis="quelle"),
    pille("Angebot", 1420, 450, beim("def2", "Angebot"), fill=WEISS, size=32, anker="m", bis="quelle"),
    ficon("tabler", "message", 1720, 420, 190, beim("def2", "Annahme"), fuell=BLAU, spiegeln=True, bis="quelle"),
    pille("Annahme", 1720, 450, beim("def2", "Annahme"), fill=WEISS, size=32, anker="m", bis="quelle"),
    ficon("tabler", "book", 1350, 400, 150, beim("quelle", "Gesetz"), fuell=ROT),
    pille("Gesetz", 1350, 430, beim("quelle", "Gesetz"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "gavel", 1580, 400, 150, beim("quelle", "Rechtsprechung"), fuell=GELB),
    pille("Rechtsprechung", 1580, 430, beim("quelle", "Rechtsprechung"), fill=WEISS, size=30, anker="m"),
    ficon("tabler", "school", 1800, 400, 140, beim("quelle", "Lehre"), fuell=LILA),
    pille("Lehre", 1800, 430, beim("quelle", "Lehre"), fill=WEISS, size=30, anker="m"),
    ring(1580, 330, 120, 115, "bgh", farbe=ORANGE, breite=7),
])

# G Schritt 3: Subsumtion, Angebot und abändernde Annahme -----------------------------------------------------------------------------
folie([("sub", f"{A} › 3. Subsumtion"), ("ang", f"{A} › 3. Subsumtion › Angebot Greta"),
       ("ann", f"{A} › 3. Subsumtion › Annahme Paul? § 150 II BGB")], [
    *tafel("sub", "3. Subsumtion"),
    z("Sachverhalt neben die Definition legen", 110, 200, beim("sub", "Jetzt"), size=36, farbe=TEXT),
    ok(135, 305, beim("ang", "Das"), gr=24), z("Angebot Greta: Rad für 80 €", 175, 285, "ang", "Bold", 38),
    z("Annahme durch Paul?", 175, 375, "ann", "Bold", 38),
    z("will das Rad, aber nur für 70 €", 215, 440, "ann2", size=36),
    nein(135, 395, beim("p150", "Ablehnung"), gr=24),
    fl_block(110, 540, 1040, 170, GELB, "p150", [("§ 150 II BGB: Annahme mit Änderungen", "Bold", 36, INK),
                                                ("= Ablehnung + neuer Antrag", "Regular", 36, INK)]),
    peep_voll("GR_ruhig", GX, BR, FR, "sub"),
    peep_voll("PA_ruhig", PX, BR, FR, "sub", d=0.2, bis="ann"),
    peep_voll("PA_denkt", PX, BR, FR, "ann", anim="cut"),
    pille("80 €", GX, 360, "ang", fill=GELB, size=36, anker="m"),
    pille("nur 70 €", PX, 360, beim("ann2", "nur"), fill=ORANGE, size=36, anker="m"),
])

# H Subsumtion: neues Angebot, Annahme, Problemstelle -------------------------------------------------------------------------------
folie([("neu", f"{A} › 3. Subsumtion › neues Angebot Paul"), ("gr_ann", f"{A} › 3. Subsumtion › Annahme Greta, § 147 I BGB"),
       ("problem", f"{A} › 3. Subsumtion: das Problem")], [
    *tafel("neu", "3. Subsumtion"),
    nein(135, 225, "neu", gr=24), z("Angebot über 80 €: erloschen, § 146 BGB", 175, 200, "neu", "Bold", 36),
    ok(135, 305, beim("neu", "Paul"), gr=24), z("neues Angebot Paul: 70 €", 175, 280, beim("neu", "Paul"), "Bold", 36),
    ok(135, 385, "gr_ann", gr=24), z("Annahme Greta: „Na gut, siebzig.“", 175, 360, "gr_ann", "Bold", 36),
    z("sofort, unter Anwesenden: § 147 I BGB", 215, 425, "p147", size=34, farbe=TEXT),
    pille("Problem des Falls: hier ausführlich", 110, 560, "problem", fill=PINK, size=36),
    peep_voll("GR_ruhig", GX, BR, FR, "neu", bis="gr_ann"),
    peep_voll("GR_zufrieden", GX, BR, FR, "gr_ann", anim="cut"),
    peep_voll("PA_ruhig", PX, BR, FR, "neu", d=0.2),
    pille("80 €", GX, 360, "neu", fill=GELB, size=36, anker="m"),
    nein(GX, 395, "neu", gr=34),
    pille("70 €", PX, 360, beim("neu", "Paul"), fill=ORANGE, size=36, anker="m"),
    icon("fluent-emoji-high-contrast", "handshake", (GX + PX) // 2, 230, 120, "gr_ann"),
])

# I Schritt 4: Ergebnis -----------------------------------------------------------------------------------------------------------------
folie([("erg", f"{A} › 4. Ergebnis"), ("gezahlt", f"{A} › Anspruch nicht erloschen"), ("erg3", f"{A} › Ergebnis")], [
    *tafel("erg", "4. Ergebnis"),
    z("beantwortet den Obersatz, ohne Konjunktiv", 110, 200, beim("erg", "Es"), size=36, farbe=TEXT),
    ok(135, 305, "erg2", gr=24), z("Also: Kaufvertrag über 70 € (+)", 175, 280, "erg2", "Bold", 38),
    ok(135, 385, "gezahlt", gr=24), z("nicht erloschen: Paul hat nicht gezahlt", 175, 360, "gezahlt", "Bold", 36),
    z("(keine Erfüllung, § 362 I BGB)", 215, 420, beim("gezahlt", "erloschen"), size=32, farbe=TEXT),
    fl_block(110, 520, 1040, 160, GRUEN, "erg3", [("Greta kann 70 € verlangen", "ExtraBold", 42, INK),
                                                ("§ 433 Abs. 2 BGB", "Regular", 34, INK)]),
    pille("nicht 80 €", 110, 720, beim("erg3", "nicht"), fill=ROT, size=36),
    peep_voll("GR_fordert", GX, BR, FR, "erg", bis="erg3"),
    peep_voll("GR_zufrieden", GX, BR, FR, "erg3", anim="cut"),
    peep_voll("PA_ruhig", PX, BR, FR, "erg", d=0.2, bis="gezahlt"),
    peep_voll("PA_ertappt", PX, BR, FR, "gezahlt", anim="cut"),
    ficon("tabler", "coin-euro", (GX + PX) // 2, 330, 120, "erg3", fuell=GELB),
    pille("70 €", (GX + PX) // 2, 350, "erg3", fill=GELB, size=34, anker="m", d=0.15),
])

# J Gutachtenstil gegen Urteilsstil -------------------------------------------------------------------------------------------------------
L, R_ = 110, 1010
folie([("urteil", "Gutachtenstil oder Urteilsstil"), ("examen", "Urteilsstil · 2. Examen")], [
    karte(60, 50, 1800, 900, "urteil"),
    titel("Gutachtenstil oder Urteilsstil?", 110, 90, "urteil", 54),
    linienzug([(960, 200), (960, 700)], "urteil", breite=5, farbe=INK),
    z("Gutachtenstil", L, 205, "urteil", "ExtraBold", 40, rechts=930),
    z("1. Obersatz: Greta könnte …", L, 275, "urteil", size=34, farbe=TEXT, rechts=930),
    z("2. Definition: Ein Vertrag kommt …", L, 330, "urteil", size=34, farbe=TEXT, rechts=930),
    z("3. Subsumtion: Hier …", L, 385, "urteil", size=34, farbe=TEXT, rechts=930),
    z("4. Ergebnis: Also …", L, 440, "urteil", size=34, farbe=TEXT, rechts=930),
    z("Urteilsstil", R_, 205, beim("urteil", "Er"), "ExtraBold", 40, rechts=1820),
    z("1. Ergebnis", R_, 275, beim("urteil", "erst"), "Bold", 34, rechts=1820),
    z("2. Begründung", R_, 330, beim("urteil", "Begründung"), "Bold", 34, rechts=1820),
    z("Greta hat gegen Paul einen Anspruch", R_, 410, "urteil2", size=34, rechts=1820),
    z("auf 70 € aus § 433 II BGB,", R_, 460, "urteil2", size=34, rechts=1820),
    z("denn die beiden haben einen", R_, 510, beim("urteil2", "denn"), size=34, rechts=1820),
    z("Kaufvertrag geschlossen.", R_, 560, beim("urteil2", "denn"), size=34, rechts=1820),
    ficon("tabler", "gavel", 1720, 330, 120, "gericht", fuell=GELB),
    pille("so begründen Gerichte", 1580, 630, "gericht", fill=BLAU, size=30, anker="m"),
    pille("denn", R_, 630, beim("signal", "denn"), fill=BLAU, size=34),
    pille("weil", R_ + 150, 630, beim("signal", "weil"), fill=BLAU, size=34),
    pille("könnte", L, 520, beim("signal2", "könnte"), fill=GELB, size=34),
    pille("müsste", L + 190, 520, beim("signal2", "müsste"), fill=GELB, size=34),
    pille("also", L + 380, 520, beim("signal2", "also"), fill=GELB, size=34),
    pille("2. Examen: Entscheidungsgründe im Urteilsstil", 960, 790, beim("examen", "Entscheidungsgründe"), fill=GRUEN, size=38, anker="m"),
])

# K Typische Fehler (Mia) ---------------------------------------------------------------------------------------------------------------
MQ1, MQ2 = "„Greta hat einen Anspruch,", "weil Paul das Rad gekauft hat.“"
folie([("fehler", "Typische Fehler")], [
    *tafel("fehler", "Typische Fehler"),
    z(MQ1, 110, 200, "mia2", "Bold", 38),
    z(MQ2, 130, 255, "mia2", "Bold", 38),
    wortring(MQ1, "Greta hat einen Anspruch", 110, 200, 38, "Bold", "f1", bis="f2"),
    nein(135, 395, "f1", gr=24), z("1. Ergebnis vorweg: gehört ans Ende", 175, 370, "f1", "Bold", 36),
    nein(135, 475, "f2", gr=24), z("2. Anspruchsgrundlage fehlt: woraus?", 175, 450, "f2", "Bold", 36),
    pille("§ 433 II BGB?", 750, 255, "f2", fill=GELB, size=30, bis="f3"),
    nein(135, 555, "f3", gr=24), z("3. „gekauft“ ist nur behauptet", 175, 530, "f3", "Bold", 36),
    z("→ erst Definition und Subsumtion", 215, 595, beim("f3", "Ob"), size=34, farbe=TEXT),
    wortring(MQ2, "gekauft", 130, 255, 38, "Bold", "f3"),
    peep_voll("MI_ruhig", MX, MB, MF, "fehler", bis="mia2"),
    *redet("MI_redet", MX, MB, MF, "mia2", "f1"),
    peep_voll("MI_ertappt", MX, MB, MF, "f1", anim="cut", bis="f3"),
    peep_voll("MI_denkt", MX, MB, MF, "f3", anim="cut"),
    pille("Mia", MX, MB + 22, "fehler", fill=ROT, size=30, anker="m", d=0.2),
    blase("sprech", 500, 230, "mia2", 1460, 210, inhalt=["Greta hat einen Anspruch,", "weil Paul das Rad", "gekauft hat."],
          textsize=31, figur=("MI_redet", MX, MB, MF), bis="f1"),
])

# L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Gutachten nur am Problem")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Gutachtenstil nur, wo es ein Problem gibt", 200, 200, beim("tipp", "Ausführlich"), "Bold", 36),
    ok(175, 345, "tipp2", gr=22), z("Klares: ein Satz im Urteilsstil", 215, 325, "tipp2", size=36),
    z("Gretas Angebot: ein Satz", 215, 430, beim("tipp3", "Gretas"), size=36),
    z("Pauls Antwort: alle vier Schritte", 215, 490, beim("tipp3", "Pauls"), "Bold", 36),
    *redet("LX_warnt", LXX, BR, 520 + 40, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# M Klausurschema ----------------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Flohmarkt-Fall", 110, 90, "sch", 54),
    z("A. Greta gegen Paul: Kaufpreis, § 433 II BGB", K1, 200, "k1", "Bold", 40, rechts=1820),
    z("I. Anspruch entstanden: wirksamer Kaufvertrag", K2, 265, "k2", "Bold", 36, rechts=1820),
    z("1. Angebot Greta: 80 €", K3, 322, "k3", size=34, farbe=TEXT, rechts=1820),
    z("2. Annahme Paul? (–) § 150 II BGB: neues Angebot über 70 €", K3, 374, "k4", size=34, farbe=TEXT, rechts=1820),
    z("3. Annahme Greta (+), sofort, § 147 I BGB", K3, 426, "k5", size=34, farbe=TEXT, rechts=1820),
    z("II. Anspruch nicht erloschen: keine Zahlung, § 362 I BGB", K2, 500, "k6", "Bold", 36, rechts=1820),
    z("III. Ergebnis: Anspruch auf 70 €", K2, 560, "k7", "Bold", 36, rechts=1820),
    z("An jedem Prüfungspunkt:", K1, 690, "k8", "Bold", 38, rechts=1820),
    pille("Obersatz", 640, 675, beim("k8", "Obersatz"), fill=GELB, size=34),
    pille("Definition", 880, 675, beim("k8", "Definition"), fill=BLAU, size=34),
    pille("Subsumtion", 1135, 675, beim("k8", "Subsumtion"), fill=LILA, size=34),
    pille("Ergebnis", 1415, 675, beim("k8", "Ergebnis"), fill=GRUEN, size=34),
])

# N Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Im Gutachten steht", 0)], [("das ", 0), ("Ergebnis am Ende,", "a")], [("nicht am Anfang.", 0)]],
                750, 320, 54, "merke", {"a": beim("merke", "Ergebnis")}),
    *markertext([[("Erst fragen, dann definieren,", 0)], [("dann subsumieren, ", 0), ("dann entscheiden.", "b")]],
                750, 620, 44, "m2", {"b": beim("m2", "entscheiden")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
