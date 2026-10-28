"""Folge 005 · Abstraktionsprinzip & Trennungsprinzip: Ein Kauf, drei Verträge – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Bäckerei, B drei Verträge, C Trennung/Abstraktion, D Walters Haustür, E Sachverhalt,
F 1. Kaufvertrag, G 2. Übereignung Plattenspieler, H 3. Übereignung Geld, I Fehleridentität, J/K Rückabwicklung,
L Klausurtipp (Lexi), M Klausurschema, N Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Münzen auf der Theke,
Geldscheine an der Haustür)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_005/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = bausteine.BG_FARBE
PFAD_FARBE = bausteine.PFAD_FARBE
HELL = (255, 251, 230, 255)
DAUER = bausteine._cj()["dauer"]


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, 50)]


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


def drei(cue, aktiv):
    """Übersichtsleiste der drei Verträge; der gerade geprüfte ist gelb."""
    namen = ["1 Kaufvertrag", "2 Übereignung Plattenspieler", "3 Übereignung Geld"]
    els, x = [], 110
    for i, n in enumerate(namen):
        p = pille(n, x, 172, cue, fill=(GELB if i + 1 == aktiv else WEISS), size=26, anim="fade")
        els.append(p); x += p.sprite.width + 14
    assert x <= 1180
    return els


def namensschild(text, cx, unten, cue, fill, **k):
    return pille(text, cx, unten + 22, cue, fill=fill, size=30, anker="m", **k)


BODEN, FH = 880, 500
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
X1, X2 = 1420, 1720                     # zwei Figuren neben der Tafel
P985, P812 = "§ 985 BGB", "§ 812 I 1 Alt. 1 BGB"

# A Fall: Bäckerei ---------------------------------------------------------------------------------------------------------
HX, SX = 590, 1440                      # Hanne hinter der Theke, Sandra davor
folie([("baeck", "Fall · Beim Bäcker")], [
    pille("Bäckerei Hanne", 70, 40, "baeck", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "baeck", breite=7, farbe=INK),
    # Hanne (hinter der Theke)
    peep_voll("HA_ruhig_r", HX, BODEN, FH, "baeck", bis="h1"),
    *redet("HA_redet_r", HX, BODEN, FH, "h1", "muenzen"),
    peep_voll("HA_freundlich_r", HX, BODEN, FH, "muenzen", anim="cut"),
    # Theke mit Auslage
    fl_block(470, 640, 780, 240, ORANGE, "baeck", [], anim="fade"),
    ficon("ph", "cash-register", 1120, 640, 120, "baeck", fuell=BLAU, d=0.2),
    ficon("fluent-emoji-high-contrast", "croissant", 760, 640, 120, "baeck", fuell=GELB, d=0.3),
    ficon("fluent-emoji-high-contrast", "pretzel", 890, 640, 110, "baeck", fuell=GELB, d=0.4),
    ficon("fluent-emoji-high-contrast", "bread", 1010, 640, 110, "baeck", fuell=GELB, d=0.5, bis=beim("muenzen", "Tüte")),
    pille("Roggenbrötchen", 1010, 470, beim("s1", "Roggenbrötchen"), fill=WEISS, size=30, anker="m", bis="h1"),
    pille("0,60 €", 1010, 470, beim("h1", "Sechzig"), fill=GELB, size=34, anker="m", bis=beim("muenzen", "Tüte")),
    # Sandra
    peep_voll("SA_zeigt", SX, BODEN, 520, "sandra", anim="fade", bis="s1"),
    *redet("SA_redet", SX, BODEN, 520, "s1", "h1"),
    peep_voll("SA_zeigt", SX, BODEN, 520, "h1", anim="cut", bis="muenzen"),
    peep_voll("SA_redet", SX, BODEN, 520, "muenzen", anim="cut"),
    namensschild("Sandra", SX, BODEN, "sandra", BLAU, d=0.2),
    namensschild("Hanne", HX, BODEN, "baeck", WEISS, d=0.2),
    blase("sprech", 520, 180, "s1", 1300, 220, inhalt=["Ein Roggenbrötchen,", "bitte."], textsize=34,
          figur=("SA_redet", SX, BODEN, 520), bis="h1"),
    blase("sprech", 440, 160, "h1", 520, 210, inhalt=["Sechzig Cent."], textsize=38, figur=("HA_redet_r", HX, BODEN, FH),
          bis="muenzen"),
    # Münzen hinlegen, Tüte nehmen
    szene(ficon("tabler", "coins", 1212, 640, 64, beim("muenzen", "Münzen"), fuell=GELB), "005muenzen_1", 0.8),
    ficon("tabler", "paper-bag", SX + 95, BODEN - 175, 90, beim("muenzen", "Tüte"), fuell=WEISS),
    pille("1 Kauf = 3 Verträge", 960, 170, "drei", fill=PINK, size=50, anker="m"),
])

# B Drei Verträge ------------------------------------------------------------------------------------------------------------
f40 = F("Bold", 40)
folie([("kv", "Ein Kauf, drei Verträge › 1. Kaufvertrag, § 433 BGB"),
       ("ue1", "Ein Kauf, drei Verträge › 2. Übereignung Brötchen, § 929 S. 1 BGB"),
       ("ue2", "Ein Kauf, drei Verträge › 3. Übereignung Münzen, § 929 S. 1 BGB")], [
    *tafel("kv", "Ein Kauf, drei Verträge"),
    z("1. Kaufvertrag, § 433 BGB", 110, 200, "kv", "Bold", 40),
    z("Hanne: Brötchen übergeben, Eigentum verschaffen", 150, 262, beim("kv2", "Hanne"), size=32, farbe=TEXT),
    z("Sandra: Preis zahlen", 150, 308, beim("kv2", "Sandra"), size=32, farbe=TEXT),
    pille("Verpflichtungsgeschäft", 140 + f40.getlength("1. Kaufvertrag, § 433 BGB") + 20, 194, "verpfl", fill=GELB, size=28),
    z("2. Übereignung Brötchen, § 929 S. 1 BGB", 110, 390, "ue1", "Bold", 38),
    z("Einigung + Übergabe", 150, 450, beim("ue1", "Einigung"), size=32, farbe=TEXT),
    z("3. Übereignung Münzen, § 929 S. 1 BGB", 110, 530, "ue2", "Bold", 38),
    z("Münzen an Hanne: Einigung + Übergabe", 150, 590, beim("ue2", "Hanne"), size=32, farbe=TEXT),
    fl_block(110, 680, 1040, 150, BLAU, "verf", [("2. + 3. = Verfügungsgeschäfte", "Bold", 36, INK),
                                               ("Erst sie lassen das Eigentum übergehen.", "Regular", 34, INK)]),
    ficon("tabler", "file-text", (X1 + X2) // 2, 420, 110, "kv", fuell=WEISS, bis="ue1"),
    pille("Kaufvertrag", (X1 + X2) // 2, 150, "kv", fill=GELB, size=30, anker="m", bis="ue1"),
    ficon("fluent-emoji-high-contrast", "bread", (X1 + X2) // 2, 250, 100, "ue1", fuell=GELB),
    pfeil(X1 + 40, 280, X2 - 40, 280, beim("ue1", "Übergabe"), breite=8, kopf=26),
    ficon("tabler", "coins", (X1 + X2) // 2, 400, 90, "ue2", fuell=GELB),
    pfeil(X2 - 40, 420, X1 + 40, 420, beim("ue2", "Hanne"), breite=8, kopf=26),
    peep_voll("HA_ruhig", X1, BR, FR, "kv"),
    peep_voll("SA_wartet", X2, BR, FR, "kv", d=0.2, bis="verf"),
    peep_voll("SA_zufrieden", X2, BR, FR, "verf", anim="cut"),
    namensschild("Hanne", X1, BR, "kv", WEISS, d=0.2),
    namensschild("Sandra", X2, BR, "kv", BLAU, d=0.3),
])

# C Trennung und Abstraktion -------------------------------------------------------------------------------------------------
folie([("trenn", "Trennungsprinzip"), ("abstr", "Abstraktionsprinzip")], [
    *tafel("trenn", "Trennung und Abstraktion"),
    z("Trennungsprinzip", 110, 200, "trenn", "Bold", 42),
    z("Verpflichtung und Verfügung sind", 150, 265, beim("trenn", "Verpflichtung"), size=36),
    z("getrennte Rechtsgeschäfte.", 150, 315, beim("trenn", "getrennte"), size=36),
    z("Abstraktionsprinzip", 110, 410, "abstr", "Bold", 42),
    z("Die Wirksamkeit der Übereignung hängt", 150, 475, beim("abstr", "Wirksamkeit"), size=36),
    z("grundsätzlich nicht vom Kaufvertrag ab.", 150, 525, beim("abstr", "grundsätzlich"), size=36),
    pille("Und wenn der Kaufvertrag scheitert?", 110, 650, beim("spannend", "Spannend"), fill=PINK, size=36),
    ficon("tabler", "file-text", X1, 420, 130, "trenn", fuell=WEISS),
    pille("Kaufvertrag", X1, 450, "trenn", fill=GELB, size=30, anker="m"),
    ficon("fluent-emoji-high-contrast", "bread", X2 - 50, 400, 90, "trenn", fuell=GELB, d=0.2),
    ficon("tabler", "coins", X2 + 60, 400, 80, "trenn", fuell=GELB, d=0.3),
    pille("Übereignungen", X2, 450, "trenn", fill=BLAU, size=30, anker="m", d=0.3),
    linienzug([(1570, 230), (1570, 540)], beim("trenn", "getrennte"), breite=7, farbe=INK),
    ficon("tabler", "link-off", 1570, 690, 120, beim("abstr", "hängt"), fuell=WEISS),
    pille("unabhängig wirksam", 1570, 720, beim("abstr", "hängt"), fill=WEISS, size=30, anker="m"),
    nein(X1, 330, beim("spannend", "scheitert"), gr=40),
    pille("?", X2, 230, beim("spannend", "scheitert"), fill=PINK, size=44, anker="m"),
])

# D Fall: Walters Haustür --------------------------------------------------------------------------------------------------------
WX, BX, SX2 = 470, 1130, 1560           # Walter (vor seiner Tür), Ben, Sandra
PL_Y, GS_Y = 640, 560                   # Höhe (Unterkante) Plattenspieler / Geldscheine in der Hand
folie([("ben", "Fall · Der Plattenspieler"), ("mutter", "Fall · Die Eltern sagen Nein")], [
    pille("Am Nachmittag", 70, 40, "ben", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "ben", breite=7, farbe=INK),
    ficon("tabler", "door", 190, BODEN - 2, 230, "ben", fuell=ROT),
    # Walter
    peep_voll("WA_ruhig_r", WX, BODEN, FH, "ben", bis="w0"),
    *redet("WA_redet_r", WX, BODEN, FH, "w0", "fuehrer"),
    peep_voll("WA_ruhig_r", WX, BODEN, FH, "fuehrer", anim="cut", bis="s2"),
    peep_voll("WA_aerger_r", WX, BODEN, FH, "s2", anim="cut", bis="w1"),
    *redet("WA_fordert_r", WX, BODEN, FH, "w1", "frage"),
    peep_voll("WA_denkt_r", WX, BODEN, FH, "frage", anim="cut"),
    namensschild("Walter", WX, BODEN, "ben", WEISS, d=0.2),
    # Ben
    peep_voll("BE_ruhig", BX, BODEN, FH, beim("ben", "Ben"), anim="fade", bis="b1"),
    *redet("BE_redet", BX, BODEN, FH, "b1", "w0"),
    peep_voll("BE_froh", BX, BODEN, FH, "w0", anim="cut", bis="s2"),
    peep_voll("BE_ertappt", BX, BODEN, FH, "s2", anim="cut"),
    namensschild("Ben, 17", BX, BODEN, beim("ben", "siebzehn"), GRUEN),
    # Plattenspieler und Geld wechseln die Hände
    ficon("tabler", "vinyl", 800, PL_Y, 170, "kauf", fuell=BLAU, bis="w0"),
    pille("Plattenspieler", 800, 410, beim("kauf", "Plattenspieler"), fill=WEISS, size=30, anker="m", bis="b1"),
    pille("120 €", 990, 290, beim("kauf", "hundertzwanzig"), fill=GELB, size=36, anker="m", bis="w0"),
    szene(ficon("tabler", "cash-banknote", 1000, GS_Y, 130, "b1", fuell=GRUEN, bis="w0"), "005geldscheine_1", 0.7, versatz=0.1),
    bewegt(ficon("tabler", "cash-banknote", 640, GS_Y, 130, "w0", fuell=GRUEN, anim="cut", bis="frage"),
           "w0", beim("w0", "schön", ende=True), 360),
    bewegt(ficon("tabler", "vinyl", 990, PL_Y, 170, "w0", fuell=BLAU, anim="cut"),
           "w0", beim("w0", "Plattenspieler", ende=True), -190),
    blase("sprech", 520, 200, "b1", 1290, 210, inhalt=["Hier sind hundertzwanzig", "Euro, bar."], textsize=32,
          figur=("BE_redet", BX, BODEN, FH), bis="w0"),
    blase("sprech", 600, 200, "w0", 560, 230, inhalt=["Bitte schön, der Plattenspieler.", "Viel Spaß damit!"], textsize=30,
          figur=("WA_redet_r", WX, BODEN, FH), bis="fuehrer"),
    # Geld der Eltern für den Führerschein
    ficon("tabler", "steering-wheel", 1660, 330, 130, "fuehrer", fuell=WEISS, bis="mutter"),
    pille("Geld der Eltern: für den Führerschein", 1240, 250, beim("fuehrer", "Führerschein"), fill=LILA, size=30, anker="m",
          bis="mutter"),
    # Sandra kommt dazu
    peep_voll("SA_aerger", SX2, BODEN, 520, "mutter", anim="fade", bis="s2"),
    *redet("SA_streng", SX2, BODEN, 520, "s2", "w1"),
    peep_voll("SA_aerger", SX2, BODEN, 520, "w1", anim="cut"),
    namensschild("Sandra", SX2, BODEN, "mutter", BLAU, d=0.2),
    blase("sprech", 640, 210, "s2", 1290, 190, inhalt=["Den Kauf genehmigen wir nicht!", "Wir wollen das Geld zurück."], textsize=30,
          figur=("SA_streng", SX2, BODEN, 520), bis="w1"),
    blase("sprech", 640, 200, "w1", 660, 200, inhalt=["Dann will ich aber meinen", "Plattenspieler wiederhaben."], textsize=30,
          figur=("WA_fordert_r", WX, BODEN, FH), bis="frage"),
    pille("Wem gehören Plattenspieler und Geld?", 960, 150, "frage", fill=PINK, size=42, anker="m"),
    pille("Wie kommt beides zurück?", 960, 245, beim("frage", "wie"), fill=PINK, size=36, anker="m"),
])

# E Sachverhalt ---------------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Der 17-jährige Ben kauft seinem Nachbarn Walter dessen alten Plattenspieler für 120 Euro ab. Er zahlt bar mit Geld, "
    "das ihm seine Eltern für den Führerschein gegeben haben. Walter übergibt den Plattenspieler und legt die Scheine "
    "in eine Schublade.",
    "Als Ben zu Hause davon erzählt, geht seine Mutter Sandra zu Walter und erklärt für beide Eltern: „Den Kauf "
    "genehmigen wir nicht! Wir wollen das Geld zurück.“ Walter verlangt daraufhin den Plattenspieler zurück.",
    "(Frei erfundener Übungsfall.)",
], "Wem gehören Plattenspieler und Geld – und wie kommt beides zurück?")

# F 1. Kaufvertrag ------------------------------------------------------------------------------------------------------------------
K = "1. Kaufvertrag Ben–Walter"
folie([("v1", f"{K}, § 433 BGB › beschränkte Geschäftsfähigkeit"), ("nachteil", f"{K} › rechtlich nachteilig, § 107 BGB"),
       ("p110", f"{K} › § 110 BGB?"), ("schwebend", f"{K} › § 108 I BGB: unwirksam")], [
    *tafel("v1", "1. Kaufvertrag (§ 433 BGB)"),
    *drei(beim("v1", "drei"), 1),
    z("Ben, 17: beschränkt geschäftsfähig, §§ 2, 106 BGB", 110, 265, "mj", "Bold", 34),
    z("verpflichtet zur Zahlung: rechtlich nachteilig", 110, 325, "nachteil", size=34),
    z("§ 107 BGB: Einwilligung der Eltern nötig", 110, 385, "p107", "Bold", 34),
    nein(135, 485, beim("p110", "hilft"), gr=24),
    z("§ 110 BGB (Taschengeld)?", 175, 465, "p110", "Bold", 34),
    z("Geld war für den Führerschein bestimmt", 215, 520, beim("p110", "Das"), size=32, farbe=TEXT),
    z("schwebend unwirksam, § 108 I BGB", 110, 600, "schwebend", "Bold", 34),
    fl_block(110, 680, 1040, 150, ROT, "verweigert", [("Genehmigung verweigert:", "Bold", 36, INK),
                                                    ("Kaufvertrag endgültig unwirksam", "ExtraBold", 38, INK)]),
    ficon("tabler", "steering-wheel", (X1 + X2) // 2, 400, 120, beim("p110", "Führerschein"), fuell=WEISS, bis="schwebend"),
    peep_voll("BE_denkt", X1, BR, FR, "v1", bis="verweigert"),
    peep_voll("BE_ertappt", X1, BR, FR, "verweigert", anim="cut"),
    peep_voll("SA_wartet", X2, BR, FR, "v1", d=0.2, bis="verweigert"),
    peep_voll("SA_aerger", X2, BR, FR, "verweigert", anim="cut"),
    namensschild("Ben", X1, BR, "v1", GRUEN, d=0.2),
    namensschild("Sandra", X2, BR, "v1", BLAU, d=0.3),
])

# G 2. Übereignung des Plattenspielers ------------------------------------------------------------------------------------------------
U2 = "2. Übereignung Plattenspieler"
Q1 = "„… dass Verfügungen als abstrakte Rechtsgeschäfte unabhängig"
Q2 = "von den ihnen zugrunde liegenden Kausalgeschäften"
Q3 = "zu beurteilen sind.“  BGH, Beschl. v. 25.11.2004 – V ZB 13/04"
folie([("v2", f"{U2}, § 929 S. 1 BGB › Einigung, Übergabe"), ("vorteil", f"{U2} › lediglich rechtlicher Vorteil, § 107 BGB"),
       ("abstr2", f"{U2} › Abstraktionsprinzip")], [
    *tafel("v2", "2. Übereignung (§ 929 S. 1 BGB)"),
    *drei("v2", 2),
    ok(135, 290, "eu", gr=24), z("Einigung Walter – Ben", 175, 265, "eu", "Bold", 34),
    ok(135, 345, beim("eu", "übergeben"), gr=24), z("Übergabe durch Walter", 175, 320, beim("eu", "übergeben"), "Bold", 34),
    ok(135, 400, beim("vorteil", "Vorteil"), gr=24),
    z("Ben erlangt nur Eigentum:", 175, 375, "vorteil", "Bold", 34),
    z("lediglich rechtlicher Vorteil, § 107 BGB", 215, 425, beim("vorteil", "lediglich"), size=32, farbe=TEXT),
    z("Kaufvertrag unwirksam? Spielt keine Rolle:", 110, 500, "abstr2", "Bold", 34),
    pille("Abstraktionsprinzip", 110, 550, beim("abstr2", "Abstraktionsprinzip"), fill=GELB, size=32),
    karte(110, 630, 1040, 140, "bgh", fill=HELL, rund=18, schatten=6, rand=4),
    z(Q1, 135, 645, "bgh", size=27, rechts=1140),
    z(Q2, 135, 683, "bgh", size=27, rechts=1140),
    z(Q3, 135, 721, "bgh", size=27, rechts=1140),
    fl_block(110, 795, 1040, 80, GRUEN, "eig", [("Ben ist Eigentümer des Plattenspielers.", "ExtraBold", 34, INK)]),
    ficon("tabler", "vinyl", X2, 400, 150, "v2", fuell=BLAU),
    peep_voll("WA_ruhig", X1, BR, FR, "v2", bis="abstr2"),
    peep_voll("WA_aerger", X1, BR, FR, "abstr2", anim="cut"),
    peep_voll("BE_ruhig", X2, BR, FR, "v2", d=0.2, bis="eig"),
    peep_voll("BE_froh", X2, BR, FR, "eig", anim="cut"),
    namensschild("Walter", X1, BR, "v2", WEISS, d=0.2),
    namensschild("Ben", X2, BR, "v2", GRUEN, d=0.3),
])

# H 3. Übereignung des Geldes -------------------------------------------------------------------------------------------------------
U3 = "3. Übereignung Geld"
folie([("v3", f"{U3}, § 929 S. 1 BGB › rechtlich nachteilig")], [
    *tafel("v3", "3. Übereignung (§ 929 S. 1 BGB)"),
    *drei("v3", 3),
    z("Ben verliert sein Eigentum an den Scheinen", 110, 265, "geld", "Bold", 34),
    z("rechtlich nachteilig, § 107 BGB", 150, 325, beim("geld", "rechtlich"), size=34),
    nein(175, 405, beim("geld", "Eltern"), gr=24), z("keine Zustimmung der Eltern", 215, 385, beim("geld", "Eltern"), size=34),
    fl_block(110, 480, 1040, 150, ROT, "geld_unw", [("Übereignung des Geldes", "Bold", 36, INK),
                                                  ("unwirksam, §§ 107, 108 I BGB", "ExtraBold", 38, INK)]),
    ficon("tabler", "cash-banknote", X1, 400, 130, "v3", fuell=GRUEN),
    nein(X1 + 60, 320, "geld_unw", gr=34),
    peep_voll("WA_ruhig", X1, BR, FR, "v3"),
    peep_voll("BE_denkt", X2, BR, FR, "v3", d=0.2, bis="geld_unw"),
    peep_voll("BE_ertappt", X2, BR, FR, "geld_unw", anim="cut"),
    namensschild("Walter", X1, BR, "v3", WEISS, d=0.2),
    namensschild("Ben", X2, BR, "v3", GRUEN, d=0.3),
])

# I Fehleridentität ------------------------------------------------------------------------------------------------------------------
folie([("fi", f"{U3} › Fehleridentität")], [
    *tafel("fi", "Fehleridentität"),
    nein(135, 225, beim("fi", "nicht"), gr=24), z("nicht: weil der Kaufvertrag scheitert", 175, 200, beim("fi", "nicht"), size=34),
    ok(135, 285, beim("fi", "sondern"), gr=24), z("sondern: derselbe Fehler trifft auch", 175, 260, beim("fi", "sondern"), "Bold", 34),
    z("die Übereignung selbst", 175, 310, beim("fi", "Übereignung"), "Bold", 34),
    pille("Fehleridentität", 110, 390, beim("fi2", "Fehleridentität"), fill=GELB, size=40),
    z("durchbricht das Abstraktionsprinzip nicht:", 110, 480, beim("fi2", "Sie"), size=34),
    z("jedes Geschäft für sich, hier derselbe Mangel", 150, 530, beim("fi2", "Jedes"), size=34, farbe=TEXT),
    fl_block(110, 620, 1040, 160, BLAU, "fi3", [("Typisch: Geschäftsunfähigkeit, § 105 I BGB", "Bold", 36, INK),
                                              ("Kauf und beide Übereignungen nichtig", "Regular", 36, INK)]),
    # Übersicht der drei Geschäfte
    ficon("tabler", "file-text", 1400, 300, 100, "fi", fuell=WEISS),
    pille("Kaufvertrag", 1500, 230, "fi", fill=WEISS, size=28),
    nein(1830, 255, "fi", gr=26),
    ficon("tabler", "vinyl", 1400, 500, 110, "fi", fuell=BLAU, d=0.15),
    pille("Plattenspieler", 1500, 430, "fi", fill=WEISS, size=28, d=0.15),
    ok(1830, 455, "fi", gr=26, d=0.15),
    ficon("tabler", "cash-banknote", 1400, 690, 110, "fi", fuell=GRUEN, d=0.3),
    pille("Geld", 1500, 620, "fi", fill=WEISS, size=28, d=0.3),
    nein(1830, 645, "fi", gr=26),
    ring(1600, 645, 260, 72, beim("fi", "derselbe"), farbe=ORANGE, breite=6),
])

# J Rückabwicklung: Geld -------------------------------------------------------------------------------------------------------------
folie([("rueck", "Rückabwicklung › Geld: § 985 BGB")], [
    *tafel("rueck", "Rückabwicklung: das Geld"),
    ok(135, 225, "geld_zur", gr=24), z("Ben ist Eigentümer der Scheine geblieben", 175, 200, "geld_zur", "Bold", 34),
    z("solange Walter sie noch hat:", 175, 270, beim("geld_zur", "Solange"), size=34),
    fl_block(110, 360, 1040, 120, GRUEN, beim("geld_zur", "Paragraf"),
             [("Ben gegen Walter: § 985 BGB", "ExtraBold", 38, INK)]),
    ficon("tabler", "cash-banknote", X1, 400, 130, "rueck", fuell=GRUEN, bis=beim("geld_zur", "herausverlangen")),
    bewegt(ficon("tabler", "cash-banknote", X2, 400, 130, beim("geld_zur", "herausverlangen"), fuell=GRUEN, anim="cut"),
           beim("geld_zur", "herausverlangen"), beim("geld_zur", "herausverlangen", ende=True), -300),
    peep_voll("WA_denkt", X1, BR, FR, "rueck"),
    peep_voll("BE_ruhig", X2, BR, FR, "rueck", d=0.2),
    namensschild("Walter", X1, BR, "rueck", WEISS, d=0.2),
    namensschild("Ben", X2, BR, "rueck", GRUEN, d=0.3),
])

# K Rückabwicklung: Plattenspieler -------------------------------------------------------------------------------------------------
folie([("w985", "Rückabwicklung › Plattenspieler: § 985 BGB?"), ("w812", f"Rückabwicklung › Plattenspieler: {P812}")], [
    *tafel("w985", "Rückabwicklung: der Plattenspieler"),
    nein(135, 225, beim("w985", "scheidet"), gr=24), z("§ 985 BGB: Walter nicht mehr Eigentümer", 175, 200, "w985", "Bold", 34),
    z("§ 812 Abs. 1 S. 1 Alt. 1 BGB", 110, 300, "w812", "Bold", 40),
    ok(135, 385, "erlangt", gr=24), z("etwas erlangt: Eigentum und Besitz", 175, 360, "erlangt", size=34),
    ok(135, 445, "leistung", gr=24), z("durch Leistung Walters", 175, 420, "leistung", size=34),
    ok(135, 505, "ohne", gr=24), z("ohne rechtlichen Grund: Kaufvertrag unwirksam", 175, 480, "ohne", size=34),
    fl_block(110, 580, 1040, 120, GRUEN, "rf", [("Ben muss zurückübereignen und herausgeben", "ExtraBold", 34, INK)]),
    ficon("tabler", "vinyl", X2, 400, 150, "w985", fuell=BLAU, bis="rf"),
    bewegt(ficon("tabler", "vinyl", X1, 400, 150, "rf", fuell=BLAU, anim="cut"), "rf", beim("rf", "zurückübereignen", ende=True), 300),
    peep_voll("WA_aerger", X1, BR, FR, "w985", bis="w812"),
    peep_voll("WA_denkt", X1, BR, FR, "w812", anim="cut", bis="rf"),
    peep_voll("WA_ruhig", X1, BR, FR, "rf", anim="cut"),
    peep_voll("BE_ruhig", X2, BR, FR, "w985", d=0.2, bis="rf"),
    peep_voll("BE_muede", X2, BR, FR, "rf", anim="cut"),
    namensschild("Walter", X1, BR, "w985", WEISS, d=0.2),
    namensschild("Ben", X2, BR, "w985", GRUEN, d=0.3),
])

# L Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------------
LXX = 1560
T3 = "„Kaufvertrag unwirksam, also kein Eigentum“"
folie([("tipp", "Klausurtipp · erst § 985, jede Übereignung einzeln")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Herausgabe verlangt? Zuerst § 985 BGB", 200, 200, beim("tipp", "Verlangt"), "Bold", 36),
    ok(175, 335, "tipp2", gr=22), z("Eigentum: jede Übereignung für sich prüfen", 215, 315, "tipp2", size=34),
    nein(175, 435, "tipp3", gr=22), z("Nie:", 215, 415, "tipp3", "Bold", 34),
    z(T3, 215, 470, beim("tipp3", "Der"), size=34),
    *redet("LX_warnt", LXX, BR, 560, "tipp", "sch"),
    namensschild("Lexi", LXX, BR, "tipp", GELB, d=0.2),
])

# M Klausurschema ------------------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Walter gegen Ben auf Herausgabe", 110, 90, "sch", 50),
    z("A. § 985 BGB", K1, 190, "k1", "Bold", 38, rechts=1820),
    z("I. Ben ist Besitzer (+)", K2, 245, beim("k1", "Römisch"), size=34, rechts=1820),
    z("II. Walter noch Eigentümer?", K2, 297, "k2", size=34, rechts=1820),
    z("1. Verlust durch Übereignung, § 929 S. 1 BGB: Einigung, Übergabe", K3, 349, "k3", size=32, farbe=TEXT, rechts=1820),
    z("2. Einigung wirksam: lediglich rechtlich vorteilhaft, § 107 BGB (Abstraktionsprinzip)", K3, 399, "k4", size=32,
      farbe=TEXT, rechts=1820),
    z("III. Ergebnis: kein Anspruch (–)", K2, 451, "k5", "Bold", 34, rechts=1820),
    z("B. § 812 Abs. 1 S. 1 Alt. 1 BGB", K1, 535, "k6", "Bold", 38, rechts=1820),
    z("I. etwas erlangt: Eigentum und Besitz (+)", K2, 590, "k7", size=34, rechts=1820),
    z("II. durch Leistung (+)", K2, 642, "k8", size=34, rechts=1820),
    z("III. ohne rechtlichen Grund: Kaufvertrag unwirksam, §§ 107, 108 I BGB (+)", K2, 694, "k9", size=34, rechts=1820),
    z("IV. Rechtsfolge: Rückübereignung und Herausgabe", K2, 746, "k10", "Bold", 34, rechts=1820),
])

# N Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der Kaufvertrag ", 0), ("verpflichtet,", "a")], [("die Übereignung ", 0), ("verfügt.", "b")]],
                750, 330, 54, "merke", {"a": beim("merke", "verpflichtet"), "b": beim("merke", "verfügt")}),
    *markertext([[("Fällt nur der Kaufvertrag weg,", 0)], [("bleibt die Übereignung wirksam.", "c")],
                 [("Zurück geht es über § 812 BGB.", 0)]],
                750, 560, 44, "m2", {"c": beim("m2", "bleibt")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
