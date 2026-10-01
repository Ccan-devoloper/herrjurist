"""Folge 017 · Zugang Willenserklärung § 130 BGB: Wann ist der Brief angekommen? – Serienstandard Open Peeps
(Katzenkönig). Szenen laut ../SZENENPLAN.md: A Café und Vertrag, B Silvesternacht am Büro (Nacht, weil der Fall um
23 Uhr spielt), C Der zweite Januar, D Sachverhalt, E Wirksamwerden § 130 I, F I. Abgabe, G II. Zugang (Machtbereich,
Kenntnisnahme), H II. Zugang (BGH Silvester), I III. Widerruf und Ergebnis, J Gegenfall E-Mail, K Empfangsbotin,
L Erklärungsbote und Annahmeverweigerung, M Beweis Einwurf-Einschreiben, N Klausurtipp (Lexi), O Klausurschema,
P Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Brief fällt in den Briefkasten, Werner öffnet die Klappe,
der Bote klingelt)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *
from fontTools.ttLib import TTFont

bausteine.FIGORDNER = "op_017/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE, nacht=None)                  # Nacht = Verlauf, erzeugt im Renderer
PFAD_FARBE = dict(bausteine.PFAD_FARBE, nacht=(255, 255, 255, 170))
HELL = (255, 251, 230, 255)
GRAU = (205, 205, 210, 255)
NACHTWAND = (78, 92, 150, 255)
LINIE = (225, 228, 240, 255)
DAUER = bausteine._cj()["dauer"]
NULL = ("fall", -round(bausteine._t("fall") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar

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


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(glyphen(titel_), 110, 100, cue, size)]


def block(x, y, w, h, fill, cue, text, size=38, **k):
    return fl_block(x, y, w, h, fill, cue, [(glyphen(text), "ExtraBold", size, INK)], **k)


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


def nachtfolie(pfade, els):
    pruefe_im_bild(els)
    FOLIEN.append(dict(bg="nacht", pfade=pfade, els=els))


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel

# A Fall: Café und Wartungsvertrag (Tag) --------------------------------------------------------------------------------
HX, WX = 640, 1560
folie([(NULL, "Fall · Der Wartungsvertrag"), ("silv", "Fall · Die Kündigung")], [
    linienzug([(60, BODEN), (1860, BODEN)], NULL, breite=7, farbe=INK),
    ficon("tabler", "building-store", 300, BODEN - 4, 380, NULL, fuell=GELB),
    pl("Helgas Café", 300, 440, NULL, fill=WEISS, size=32, anker="m"),
    ficon("tabler", "coffee", 300, 780, 110, beim("fall", "Café"), fuell=WEISS),
    peep_voll("HE_ruhig_r", HX, BODEN, FH, NULL, bis="silv"),
    peep_voll("HE_denkt_r", HX, BODEN, FH, "silv", anim="cut"),
    namensschild("Helga", HX, BODEN, NULL, LILA),
    # Werners Firma wartet die Kaffeemaschine
    peep_voll("WE_ruhig", WX, BODEN, FH, beim("vertrag", "Werner"), anim="fade", bis="silv"),
    namensschild("Werner", WX, BODEN, beim("vertrag", "Werner"), BLAU, bis="silv"),
    ficon("tabler", "tools", WX - 170, 700, 90, beim("vertrag", "wartet"), fuell=GRAU, bis="silv"),
    pl("Wartung der Kaffeemaschine", WX, 230, beim("vertrag", "wartet"), fill=BLAU, size=30, anker="m", bis="silv"),
    # der Vertrag in der Mitte
    ficon("tabler", "file-text", 1060, 640, 150, beim("vertrag", "Vertrag"), fuell=WEISS),
    pl("verlängert sich um 1 Jahr", 1060, 420, beim("vertrag", "verlängert"), fill=WEISS, size=30, anker="m"),
    pl("Kündigung bis 31. Dezember bei Werner", 1060, 340, beim("vertrag", "einunddreißigsten"), fill=ROT, size=30,
       anker="m"),
    # Silvester: Helga schreibt die Kündigung
    pl("Silvester", 70, 40, "silv", fill=GELB, size=44),
    ficon("tabler", "writing", HX + 150, 660, 90, beim("silv", "schreibt"), fuell=WEISS),
    ficon("tabler", "mail", HX + 160, 560, 90, beim("silv", "Silvester"), fuell=GELB),
])

# B Fall: Silvesternacht am Büro (Nacht) --------------------------------------------------------------------------------
BX, MX, HX = 760, 1180, 1560            # Werners Büro, Briefkasten, Helga
SCHLITZ = (MX, 610)
nachtfolie([("einwurf", "Fall · Silvester, 23 Uhr")], [
    mond(1760, 170, 60, "einwurf"),
    linienzug([(60, BODEN), (1860, BODEN)], "einwurf", breite=7, farbe=LINIE),
    ficon("tabler", "building", BX, BODEN - 4, 420, "einwurf", fuell=NACHTWAND),
    pl("Werners Büro", BX, 400, "einwurf", fill=BLAU, size=32, anker="m"),
    linienzug([(MX, 700), (MX, BODEN)], "einwurf", breite=10, farbe=LINIE),
    ficon("tabler", "mailbox", MX, 705, 170, "einwurf", fuell=WEISS, bis=beim("einwurf", "Briefkasten", ende=True)),
    szene(ficon("tabler", "mailbox", MX, 705, 170, beim("einwurf", "Briefkasten", ende=True), fuell=GELB, anim="cut"),
          "017einwurf*", 0.9, -0.30),
    pl("31. Dezember", 70, 40, "einwurf", fill=GELB, size=44),
    ficon("tabler", "clock-hour-11", 380, 300, 90, beim("einwurf", "dreiundzwanzig"), fuell=WEISS),
    pl("23 Uhr", 380, 340, beim("einwurf", "dreiundzwanzig"), fill=GELB, size=34, anker="m"),
    peep_voll("HE_ruhig", HX, BODEN, FH, "einwurf", bis="h1"),
    *redet("HE_redet", HX, BODEN, FH, "h1", "jan"),
    namensschild("Helga", HX, BODEN, "einwurf", LILA),
    # der Brief wandert von Helgas Hand in den Briefkasten
    bewegt(ficon("tabler", "mail", SCHLITZ[0], SCHLITZ[1], 80, beim("einwurf", "wirft"), fuell=GELB,
                 bis=beim("einwurf", "Briefkasten", ende=True)),
           beim("einwurf", "wirft"), beim("einwurf", "Briefkasten", ende=True), HX - 140 - SCHLITZ[0], 40),
    blase("sprech", 700, 190, "h1", 1150, 170, inhalt=["Geschafft, noch vor Mitternacht!"], textsize=36,
          figur=("HE_redet", HX, BODEN, FH)),
])

# C Fall: der zweite Januar (Tag) ---------------------------------------------------------------------------------------
WX = 1500
folie([("jan", "Fall · Der zweite Januar"), ("frage", "Fall · Die Frage")], [
    ficon("tabler", "sun", 1760, 220, 110, "jan", fuell=GELB, d=0.2),
    linienzug([(60, BODEN), (1860, BODEN)], "jan", breite=7, farbe=INK),
    ficon("tabler", "building", BX, BODEN - 4, 420, "jan", fuell=BLAU),
    pl("Werners Büro", BX, 400, "jan", fill=WEISS, size=32, anker="m"),
    pl("über Neujahr geschlossen", BX, 320, beim("jan", "geschlossen"), fill=GRAU, size=30, anker="m",
       bis=beim("jan", "Am")),
    ficon("tabler", "lock", BX, 780, 80, beim("jan", "geschlossen"), fuell=GELB, bis=beim("jan", "Am")),
    linienzug([(MX, 700), (MX, BODEN)], "jan", breite=10, farbe=INK),
    ficon("tabler", "mailbox", MX, 705, 170, "jan", fuell=GELB, bis=beim("jan", "leert")),
    szene(ficon("tabler", "mailbox", MX, 705, 170, beim("jan", "leert"), fuell=WEISS, anim="cut"), "017klappe*", 0.8, -0.25),
    pl("2. Januar", 70, 40, beim("jan", "zweiten"), fill=GELB, size=44),
    peep_voll("WE_ruhig", WX, BODEN, FH, beim("jan", "Am"), anim="fade", bis=beim("jan", "leert")),
    peep_voll("WE_liest", WX, BODEN, FH, beim("jan", "leert"), anim="cut", bis="w1"),
    *redet("WE_redet", WX, BODEN, FH, "w1", "frage"),
    peep_voll("WE_froh", WX, BODEN, FH, "frage", anim="cut"),
    namensschild("Werner", WX, BODEN, beim("jan", "Am"), BLAU),
    # Werner holt den Brief heraus und liest
    bewegt(ficon("tabler", "mail-opened", WX - 150, 600, 90, beim("jan", "leert"), fuell=GELB),
           beim("jan", "leert"), beim("jan", "Briefkasten", ende=True), SCHLITZ[0] - (WX - 150), SCHLITZ[1] - 600),
    blase("sprech", 720, 200, "w1", 1100, 180, inhalt=["Zu spät! Der Vertrag", "läuft noch ein Jahr."], textsize=36,
          figur=("WE_redet", WX, BODEN, FH), bis="frage"),
    pl("Ist Helgas Kündigung rechtzeitig wirksam geworden?", 960, 200, "frage", fill=PINK, size=40, anker="m"),
])

# D Sachverhalt -------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Helga betreibt ein kleines Café. Die Firma von Werner wartet ihre Kaffeemaschine. Laut Vertrag verlängert sich "
    "der Wartungsvertrag um ein Jahr, wenn Helgas Kündigung Werner nicht bis zum 31. Dezember zugeht. Eine Form ist "
    "nicht vereinbart.",
    "Helga schreibt die Kündigung erst an Silvester und wirft den Brief um 23 Uhr in den Briefkasten von Werners Büro. "
    "Das Büro ist, wie in der Branche üblich, an Silvester nachmittags und an Neujahr geschlossen. Werner leert den "
    "Briefkasten am Morgen des 2. Januar, einem Werktag, und meint, die Kündigung sei zu spät gekommen.",
    "(Frei erfundener Übungsfall.)",
], "Ist Helgas Kündigung rechtzeitig wirksam geworden?")

# E Wirksamwerden nach § 130 I ------------------------------------------------------------------------------------------
folie([("norm", "Wirksamwerden · § 130 Abs. 1 S. 1 BGB"), ("glied", "Wirksamwerden · Abgabe, Zugang, kein Widerruf")],
      rechts_frei([
    *tafel("norm", "Wann wird die Kündigung wirksam?"),
    z("Kündigung: empfangsbedürftige Willenserklärung", 110, 190, "norm", "Bold", 36),
    z("abgegeben in Werners Abwesenheit", 150, 250, beim("norm", "abgegeben"), size=34),
    z("§ 130 Abs. 1 S. 1 BGB:", 110, 340, beim("p130", "Paragraf"), "Bold", 38),
    z("wirksam erst, wenn sie Werner zugeht", 150, 400, beim("p130", "wirksam"), size=34),
    block(110, 510, 320, 120, GELB, beim("glied", "Abgabe"), "I. Abgabe", size=36),
    block(470, 510, 320, 120, BLAU, beim("glied", "Zugang"), "II. Zugang", size=36),
    block(830, 510, 320, 120, GRUEN, beim("glied", "Widerruf"), "III. Widerruf?", size=36),
    ficon("tabler", "mail", (X1 + X2) // 2, 380, 120, "norm", fuell=GELB),
    peep_voll("HE_ruhig", X1, BR, FR, "norm"),
    peep_voll("WE_ruhig", X2, BR, FR, "norm", d=0.2, bis="p130"),
    peep_voll("WE_denkt", X2, BR, FR, "p130", anim="cut"),
    namensschild("Helga", X1, BR, "norm", LILA, d=0.2),
    namensschild("Werner", X2, BR, "norm", BLAU, d=0.3),
]))

# F I. Abgabe ---------------------------------------------------------------------------------------------------------
MB = (X1 + X2) // 2
folie([("abg", "I. Abgabe")], rechts_frei([
    *tafel("abg", "I. Abgabe (Helga)"),
    z("Helga bringt die Erklärung willentlich", 110, 200, beim("abg", "Helga"), "Bold", 36),
    z("so auf den Weg, dass sie Werner erreichen kann", 110, 255, beim("abg", "erreichen"), "Bold", 36),
    ok(135, 380, beim("abg_ok", "geschehen"), gr=22), z("Einwurf am 31. Dezember, 23 Uhr", 175, 360, "abg_ok", size=34),
    block(110, 470, 1040, 100, GRUEN, beim("abg_ok", "geschehen"), "Mit dem Einwurf geschehen.", size=38),
    ficon("tabler", "mailbox", MB, 420, 150, "abg", fuell=WEISS, bis=beim("abg_ok", "Einwurf", ende=True)),
    ficon("tabler", "mailbox", MB, 420, 150, beim("abg_ok", "Einwurf", ende=True), fuell=GELB, anim="cut"),
    bewegt(ficon("tabler", "mail", MB, 300, 80, beim("abg", "Weg"), fuell=GELB, bis=beim("abg_ok", "Einwurf", ende=True)),
           beim("abg", "Weg"), beim("abg_ok", "Einwurf", ende=True), X1 - MB, 0),
    peep_voll("HE_ruhig", X1, BR, FR, "abg", bis="abg_ok"),
    peep_voll("HE_froh", X1, BR, FR, "abg_ok", anim="cut"),
    peep_voll("WE_ruhig", X2, BR, FR, "abg", d=0.2),
    namensschild("Helga", X1, BR, "abg", LILA, d=0.2),
    namensschild("Werner", X2, BR, "abg", BLAU, d=0.3),
]))

# G II. Zugang: Machtbereich und Kenntnisnahme --------------------------------------------------------------------------
folie([("zug", "II. Zugang › Machtbereich"), ("kennt", "II. Zugang › Kenntnisnahme zu erwarten")], rechts_frei([
    *tafel("zug", "II. Zugang (bei Werner)"),
    z("1. Machtbereich des Empfängers", 110, 190, "macht", "Bold", 36),
    ok(135, 265, beim("macht", "gehört"), gr=22), z("Werners Briefkasten gehört dazu", 175, 245, beim("macht", "Sein"), size=34),
    z("2. Möglichkeit der Kenntnisnahme", 110, 330, "kennt", "Bold", 36),
    z("unter gewöhnlichen Umständen", 150, 385, beim("kennt", "gewöhnlichen"), size=34),
    z("Briefkasten: wann ist nach der Verkehrsanschauung", 110, 470, "leer", "Bold", 32),
    z("mit der nächsten Leerung zu rechnen?", 150, 515, beim("leer", "nächsten"), "Bold", 32),
    nein(175, 590, beim("leer", "nicht"), gr=22),
    z("nicht: wann Werner tatsächlich nachsieht", 215, 570, beim("leer", "nicht"), size=32, farbe=TEXT),
    block(110, 660, 1040, 100, GELB, "feste", "Eine feste Uhrzeit gibt es nicht.", size=38),
    ficon("tabler", "mailbox", MB, 420, 150, beim("macht", "Briefkasten"), fuell=GELB),
    ficon("tabler", "eye", X2 - 120, 230, 80, "kennt", fuell=WEISS, bis="feste"),
    ficon("tabler", "clock-question", MB, 230, 100, "feste", fuell=WEISS),
    peep_voll("HE_ruhig", X1, BR, FR, "zug"),
    peep_voll("WE_ruhig", X2, BR, FR, "zug", d=0.2, bis="kennt"),
    peep_voll("WE_liest", X2, BR, FR, "kennt", anim="cut", bis="feste"),
    peep_voll("WE_denkt", X2, BR, FR, "feste", anim="cut"),
    namensschild("Helga", X1, BR, "zug", LILA, d=0.2),
    namensschild("Werner", X2, BR, "zug", BLAU, d=0.3),
]))

# H II. Zugang: Silvester nach Geschäftsschluss (BGH) -------------------------------------------------------------------
TX = 260
folie([("bgh", "II. Zugang › nach Geschäftsschluss, BGH")], rechts_frei([
    *tafel("bgh", "II. Zugang: Silvester, 23 Uhr"),
    z("BGH: Einwurf nach Geschäftsschluss in den", 110, 190, beim("bgh", "Wer"), "Bold", 34),
    z("Briefkasten eines Büros: kein Zugang mehr am", 110, 240, beim("bgh", "Büros"), "Bold", 34),
    z("selben Tag", 110, 290, beim("bgh", "keinen"), "Bold", 34),
    z("auch Silvester nachmittags, wenn dort", 150, 360, "silv2", size=34),
    z("üblicherweise niemand mehr arbeitet", 150, 410, beim("silv2", "üblicherweise"), size=34),
    z("BGH, Urt. v. 5.12.2007 – XII ZR 148/05, Rn. 9", 150, 465, beim("silv2", "arbeitet"), size=28, farbe=TEXT),
    pl("31.12.", TX, 560, "zug_erg", fill=WEISS, size=30, anker="m"),
    pl("1.1. Neujahr", TX + 320, 560, "zug_erg", fill=GRAU, size=30, anker="m"),
    pl("2.1.", TX + 640, 560, beim("zug_erg", "zweiten"), fill=GRUEN, size=30, anker="m"),
    nein(TX, 640, "zug_erg", gr=24),
    nein(TX + 320, 640, "zug_erg", gr=24),
    ok(TX + 640, 640, beim("zug_erg", "zweiten"), gr=24),
    block(110, 710, 1040, 100, ROT, beim("zug_erg", "zweiten"), "Zugang erst am 2. Januar", size=40),
    ficon("tabler", "building", MB, 400, 190, "bgh", fuell=BLAU),
    ficon("tabler", "lock", MB, 400, 60, beim("bgh", "Geschäftsschluss"), fuell=GELB),
    ficon("tabler", "moon", MB + 120, 190, 70, beim("silv2", "Silvester"), fuell=GELB, bis="zug_erg"),
    ficon("tabler", "calendar-event", MB + 120, 210, 80, "zug_erg", fuell=WEISS),
    peep_voll("HE_ruhig", X1, BR, FR, "bgh", bis="zug_erg"),
    peep_voll("HE_sorge", X1, BR, FR, "zug_erg", anim="cut"),
    peep_voll("WE_ruhig", X2, BR, FR, "bgh", d=0.2, bis="zug_erg"),
    peep_voll("WE_froh", X2, BR, FR, "zug_erg", anim="cut"),
    namensschild("Helga", X1, BR, "bgh", LILA, d=0.2),
    namensschild("Werner", X2, BR, "bgh", BLAU, d=0.3),
]))

# I III. kein Widerruf und Ergebnis ------------------------------------------------------------------------------------
folie([("wid", "III. kein Widerruf, § 130 Abs. 1 S. 2 BGB"), ("erg", "Ergebnis · Zugang erst am 2. Januar, zu spät")],
      rechts_frei([
    *tafel("wid", "III. Widerruf?"),
    z("§ 130 Abs. 1 S. 2 BGB: Ein Widerruf muss", 110, 190, beim("wid", "Paragraf"), "Bold", 34),
    z("vorher oder gleichzeitig zugehen", 150, 245, beim("wid", "vorher"), size=34),
    nein(135, 345, beim("wid2", "spät"), gr=22),
    z("Anruf am 2. Januar mittags: zu spät", 175, 325, beim("wid2", "Anruf"), size=34),
    z("auch wenn Werner den Brief noch nicht gelesen hat", 175, 380, beim("wid2", "auch"), size=32, farbe=TEXT),
    block(110, 490, 1040, 100, ROT, "erg", "Zugang erst am 2. Januar: zu spät", size=38),
    block(110, 620, 1040, 100, GELB, "erg2", "Der Vertrag verlängert sich um ein Jahr.", size=38),
    ficon("tabler", "phone-call", X1 - 130, 560, 70, beim("wid2", "Anruf"), fuell=WEISS, bis="erg"),
    ficon("tabler", "mail-opened", X2 - 140, 600, 80, beim("wid2", "Brief"), fuell=GELB, bis="erg"),
    ficon("tabler", "calendar-event", MB, 380, 110, "erg2", fuell=WEISS),
    pl("+ 1 Jahr", MB, 180, "erg2", fill=GELB, size=30, anker="m"),
    peep_voll("HE_ruhig", X1, BR, FR, "wid", bis="wid2"),
    peep_voll("HE_ueberlegt", X1, BR, FR, "wid2", anim="cut", bis="erg"),
    peep_voll("HE_sorge", X1, BR, FR, "erg", anim="cut"),
    peep_voll("WE_ruhig", X2, BR, FR, "wid", d=0.2, bis="erg"),
    peep_voll("WE_froh", X2, BR, FR, "erg", anim="cut"),
    namensschild("Helga", X1, BR, "wid", LILA, d=0.2),
    namensschild("Werner", X2, BR, "wid", BLAU, d=0.3),
]))

# J Gegenfall E-Mail ---------------------------------------------------------------------------------------------------
folie([("mail", "Gegenfall · E-Mail im Geschäftsverkehr")], rechts_frei([
    *tafel("mail", "Gegenfall: E-Mail"),
    pl("30. Dezember, 10 Uhr: E-Mail statt Brief", 110, 180, "mail", fill=PINK, size=32),
    z("BGH: Im Geschäftsverkehr geht die E-Mail zu,", 110, 280, "mail2", "Bold", 34),
    z("sobald sie während der üblichen Geschäftszeiten", 150, 335, beim("mail2", "während"), size=34),
    z("abrufbereit auf dem Mailserver liegt", 150, 390, beim("mail2", "abrufbereit"), size=34),
    z("BGH, Urt. v. 6.10.2022 – VII ZR 895/21, Rn. 19", 150, 445, beim("mail2", "liegt"), size=28, farbe=TEXT),
    ok(135, 545, "mail3", gr=22), z("Ob Werner sie liest: egal", 175, 525, "mail3", size=34),
    z("außerhalb der Geschäftszeiten: offengelassen", 110, 620, "mail4", "Bold", 34, farbe=TEXT),
    ficon("tabler", "device-laptop", X1, 560, 130, "mail", fuell=WEISS),
    ficon("tabler", "server", X2, 600, 90, beim("mail2", "Mailserver"), fuell=BLAU),
    bewegt(ficon("tabler", "mail", X2, 330, 90, beim("mail", "E-Mail"), fuell=GELB),
           beim("mail", "E-Mail"), beim("mail", "E-Mail", ende=True), X1 - X2, 0),
    ficon("tabler", "clock", MB, 250, 80, "mail", fuell=WEISS),
    ficon("tabler", "clock-question", MB, 250, 80, "mail4", fuell=WEISS, anim="cut"),
    peep_voll("HE_ruhig", X1, BR, FR, "mail"),
    peep_voll("WE_ruhig", X2, BR, FR, "mail", d=0.2, bis="mail4"),
    peep_voll("WE_denkt", X2, BR, FR, "mail4", anim="cut"),
    namensschild("Helga", X1, BR, "mail", LILA, d=0.2),
    namensschild("Werner", X2, BR, "mail", BLAU, d=0.3),
]))

# K Empfangsbotin Paula -------------------------------------------------------------------------------------------------
folie([("bote", "Sonderfall · Empfangsbotin")], rechts_frei([
    *tafel("bote", "Sonderfall: Boten"),
    z("Silvestermorgen: Brief an Paula", 110, 190, "paula", "Bold", 36),
    z("Paula: Werners Büroangestellte", 150, 250, beim("paula", "Büroangestellter"), size=34),
    z("Paula ist Empfangsbotin", 150, 305, beim("paula", "Empfangsbotin"), "Bold", 34),
    z("Zugang, sobald unter normalen Umständen", 110, 410, "weiter", "Bold", 34),
    z("mit der Weitergabe an Werner zu rechnen ist", 150, 465, beim("weiter", "Weitergabe"), size=34),
    z("BAG, Urt. v. 9.6.2011 – 6 AZR 687/09, Rn. 18", 150, 520, beim("weiter", "rechnen"), size=28, farbe=TEXT),
    pl("Silvestermorgen", MB, 160, "paula", fill=GELB, size=30, anker="m"),
    bewegt(ficon("tabler", "mail", X2 - 150, 600, 80, beim("paula", "Brief"), fuell=GELB),
           beim("paula", "Brief"), beim("paula", "Silvestermorgen", ende=True), X1 + 150 - (X2 - 150), 0),
    peep_voll("HE_ruhig_r", X1, BR, FR, "bote"),
    peep_voll("PA_ruhig", X2, BR, FR, beim("paula", "Paula"), anim="fade", bis="p1"),
    *redet("PA_redet", X2, BR, FR, "p1", "weiter"),
    peep_voll("PA_froh", X2, BR, FR, "weiter", anim="cut"),
    namensschild("Helga", X1, BR, "bote", LILA, d=0.2),
    namensschild("Paula", X2, BR, beim("paula", "Paula"), GRUEN),
    blase("sprech", 760, 190, "p1", 1530, 175, inhalt=["Ich lege ihn Werner gleich", "auf den Schreibtisch."],
          textsize=32, figur=("PA_redet", X2, BR, FR), bis="weiter"),
]))

# L Erklärungsbote und Annahmeverweigerung -------------------------------------------------------------------------------
folie([("erkl", "Sonderfall · Erklärungsbote"), ("verw", "Sonderfall · Annahme verweigert, § 242 BGB")], rechts_frei([
    *tafel("erkl", "Sonderfall: eigener Bote"),
    z("Helgas eigener Bote: Erklärungsbote", 110, 190, beim("erkl", "eigenen"), "Bold", 36),
    z("Risiko bei Helga, bis er bei Werner abliefert", 150, 245, beim("erkl", "Bis"), size=34),
    pl("Werner nimmt den Brief nicht ab?", 110, 320, "verw", fill=PINK, size=32),
    z("grundlos verweigert, obwohl mit", 110, 420, "treu", "Bold", 34),
    z("rechtserheblichen Erklärungen zu rechnen ist", 110, 470, beim("treu", "rechtserheblichen"), "Bold", 34),
    z("Treu und Glauben: zugegangen beim Übergabeversuch", 150, 530, beim("treu", "Treu"), size=32),
    z("§ 242 BGB", 150, 580, beim("treu", "Paragraf"), "Bold", 32),
    z("Voraussetzung: Helga hat alles Zumutbare getan", 110, 670, "zumut", size=34),
    z("BAG, Urt. v. 26.3.2015 – 2 AZR 483/14, Rn. 21", 150, 725, beim("zumut", "getan"), size=28, farbe=TEXT),
    bis_(ficon("tabler", "mail", X1 + 140, 600, 80, beim("erkl", "eigenen"), fuell=GELB), beim("treu", "Treu")),
    ficon("tabler", "mail-check", X1 + 140, 600, 80, beim("treu", "Treu"), fuell=GRUEN, anim="cut"),
    peep_voll("BO_ruhig_r", X1, BR, FR, beim("erkl", "eigenen"), bis="treu"),
    peep_voll("BO_ratlos_r", X1, BR, FR, "treu", anim="cut"),
    namensschild("Bote", X1, BR, beim("erkl", "eigenen"), ORANGE, d=0.2),
    szene(ficon("tabler", "bell-ringing", X2, 330, 90, ("verw", -0.25), fuell=GELB, bis="w2"), "017klingel*", 0.7, -0.05),
    peep_voll("WE_ruhig", X2, BR, FR, beim("verw", "Werner"), anim="fade", bis="w2"),
    *redet("WE_abwehr", X2, BR, FR, "w2", "treu"),
    peep_voll("WE_denkt", X2, BR, FR, "treu", anim="cut"),
    namensschild("Werner", X2, BR, beim("verw", "Werner"), BLAU),
    ficon("tabler", "hand-stop", X2 - 150, 505, 80, "w2", fuell=ROT, bis="treu"),
    blase("sprech", 600, 170, "w2", 1560, 180, inhalt=["Den nehme ich nicht an!"], textsize=36,
          figur=("WE_abwehr", X2, BR, FR), bis="treu"),
]))

# M Beweis: Einwurf-Einschreiben ----------------------------------------------------------------------------------------
folie([("bew", "Beweis · Einwurf-Einschreiben")], rechts_frei([
    *tafel("bew", "Beweis: Einwurf-Einschreiben"),
    z("Den Zugang muss Helga beweisen.", 110, 190, beim("bew", "Den"), "Bold", 36),
    z("Einlieferungsbeleg + Sendungsstatus:", 110, 290, beim("einw", "Einlieferungsbeleg"), "Bold", 34),
    nein(175, 365, beim("einw", "keinen"), gr=22), z("kein Anscheinsbeweis (BAG)", 215, 345, beim("einw", "keinen"), size=34),
    z("Kopie des Auslieferungsbelegs:", 110, 440, beim("ausl", "Kopie"), "Bold", 34),
    ok(175, 515, beim("ausl", "eingehalten"), gr=22),
    z("Anscheinsbeweis, wenn Verfahren eingehalten (BGH)", 215, 495, beim("ausl", "Zusteller"), size=32),
    nein(175, 600, beim("scan", "abgelehnt"), gr=22),
    z("Scan-Verfahren: auch dann nicht (BAG)", 215, 580, beim("scan", "Scan"), size=34),
    z("BAG 2 AZR 68/24 · BGH V ZR 203/22 · BAG 2 AZR 184/25", 110, 680, beim("scan", "abgelehnt"), size=26, farbe=TEXT),
    ficon("tabler", "receipt", MB, 300, 90, beim("einw", "Einlieferungsbeleg"), fuell=WEISS, bis="ausl"),
    ficon("tabler", "file-certificate", MB, 300, 90, beim("ausl", "Kopie"), fuell=WEISS, bis="scan"),
    ficon("tabler", "scan", MB, 300, 90, beim("scan", "Scan"), fuell=WEISS),
    peep_voll("HE_denkt", X1, BR, FR, "bew", bis=beim("ausl", "eingehalten")),
    peep_voll("HE_froh", X1, BR, FR, beim("ausl", "eingehalten"), anim="cut", bis="scan"),
    peep_voll("HE_sorge", X1, BR, FR, "scan", anim="cut"),
    peep_voll("WE_ruhig", X2, BR, FR, "bew", d=0.2),
    namensschild("Helga", X1, BR, "bew", LILA, d=0.2),
    namensschild("Werner", X2, BR, "bew", BLAU, d=0.3),
]))

# N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · zwei Fragen beim Zugang")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Trenne beim Zugang zwei Fragen.", 200, 200, beim("tipp", "Trenne"), "Bold", 38),
    z("1. Ist die Erklärung im Machtbereich?", 150, 310, "tipp2", size=36),
    z("2. Wann war mit der Kenntnisnahme zu rechnen?", 150, 380, beim("tipp2", "Zweitens"), size=36),
    nein(175, 500, beim("tipp3", "prüfst"), gr=24),
    z("nicht prüfen: wirklich gelesen?", 215, 480, "tipp3", size=36, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, 560, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# O Klausurschema -----------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel(glyphen("Klausurschema: Wirksamwerden, § 130 Abs. 1 S. 1 BGB"), 110, 90, "sch", 46),
    z("I. Abgabe", K1, 200, "k1", "Bold", 38, rechts=1820),
    z("II. Zugang", K1, 275, "k2", "Bold", 38, rechts=1820),
    z("1. Machtbereich des Empfängers", K2, 330, "k2a", size=34, rechts=1820),
    z("2. Kenntnisnahme unter gewöhnlichen Umständen zu erwarten", K2, 382, "k2b", size=34, rechts=1820),
    z("3. Sonderfälle: Boten, E-Mail, Vereitelung", K2, 434, "k2c", size=34, rechts=1820),
    z("III. kein vorheriger oder gleichzeitiger Widerruf, § 130 Abs. 1 S. 2 BGB", K1, 510, "k3", "Bold", 38, rechts=1820),
    z("IV. Ergebnis mit genauem Zeitpunkt", K1, 585, "k4", "Bold", 38, rechts=1820),
])

# P Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Zugegangen ist, was im ", 0), ("Machtbereich", "a")], [("des Empfängers liegt", 0)]], 750, 320, 48,
                "merke", {"a": beim("merke", "Machtbereich")}),
    *markertext([[("und was er unter ", 0), ("gewöhnlichen Umständen", "b")], [("zur Kenntnis nehmen kann.", 0)]],
                750, 490, 46, "m2", {"b": beim("m2", "gewöhnlichen")}),
    *markertext([[("Ob er es wirklich liest, zählt nicht.", 0)]], 750, 660, 42, beim("m2", "Ob"), {}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
