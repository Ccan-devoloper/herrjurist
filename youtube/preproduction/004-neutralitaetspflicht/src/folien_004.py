"""Folge 004 · Neutralitätspflicht: Darf eine Ministerin gegen eine Partei posten? – Serienstandard Open Peeps (Katzenkönig).
Frei nach BVerfGE 148, 11 (2 BvE 1/16); Gegenfall nach BVerfGE 154, 320 (2 BvE 1/19); Linie BVerfGE 162, 207 (2 BvE 4/20).
Personen und Partei erfunden. Szenen laut ../SZENENPLAN.md: A Ministerbüro, B Der Beitrag, C Mia, D Partei X, E Sachverhalt,
F Zulässigkeit, G Maßstab, H Schritt 1 amtlich, I Schritt 2 Eingriff, J Schritt 3 Rechtfertigung/Ergebnis, K Gegenfall Parteitag,
L Linie 2022, M Klausurtipp (Lexi), N Klausurschema, O Merksatz (Lexi). Geräusche nur bei sichtbarer Handlung (Tippen, Applaus)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_004/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
DAUER = bausteine._cj()["dauer"]
HC = "fluent-emoji-high-contrast"


def z(text, x, y, cue, stil="Regular", size=38, farbe=INK, d=0.0, rechts=1170, **k):
    """Tafelzeile, die rechts nicht über die Karte hinausragen darf."""
    e = zeile(text, x, y, cue, stil, size, farbe=farbe, d=d, **k)
    assert e.x + e.sprite.width <= rechts, f"Zeile zu breit: {text} ({e.x + e.sprite.width:.0f} > {rechts})"
    return e


def tafel(cue, titel_, h=840, fill=WEISS, size=50):
    """Rechtstafel links, rechts bleibt Platz für die Figuren."""
    return [karte(60, 60, 1140, h, cue, fill=fill), titel(titel_, 110, 100, cue, size)]


def bis_(el, bis):
    """Element blendet bei Marke bis wieder aus (für Bausteine ohne bis-Parameter)."""
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


BODEN, FH = 880, 470
BX, KX = 420, 1500                     # Brandt, Krüger im Büro

# A Fall: im Ministerium ---------------------------------------------------------------------------------------------------
BR1 = ("BR_redet_r", BX, BODEN, FH)
folie([("buero", "Fall · Im Ministerium")], [
    pille("Rote Karte vom Dienstkanal", 70, 40, "buero", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "buero", breite=7, farbe=INK),
    ficon("tabler", "building-bank", 1735, 200, 110, "buero", fuell=GELB, d=0.2),
    pille("Bundesministerium", 1735, 212, "buero", fill=WEISS, size=28, anker="m", d=0.3),
    ficon("tabler", "desk", 960, BODEN - 2, 360, "buero", fuell=GELB, d=0.4),
    ficon("tabler", "device-laptop", 960, 610, 150, "buero", fuell=BLAU, d=0.5),
    # Kundgebung von Partei X angekündigt
    ficon("tabler", "speakerphone", 650, 450, 110, beim("kundg", "Kundgebung"), fuell=ORANGE),
    pille("Partei X: Kundgebung am Samstag", 1030, 380, beim("kundg", "Kundgebung"), fill=ORANGE, size=34, anker="m"),
    # Brandt
    peep_voll("BR_ruhig_r", BX, BODEN, FH, "buero", bis="brandt"),
    peep_voll("BR_denkt_r", BX, BODEN, FH, "brandt", anim="cut", bis="b1"),
    *redet("BR_redet_r", BX, BODEN, FH, "b1", "k1"),
    peep_voll("BR_redet_r", BX, BODEN, FH, "k1", anim="cut", bis="b2"),
    *redet("BR_cool_r", BX, BODEN, FH, "b2", "post"),
    pille("Ministerin Brandt", BX, BODEN + 22, "buero", fill=LILA, size=30, anker="m", d=0.2),
    szene(ficon("tabler", "device-mobile", 640, 640, 90, beim("b1", "poste"), fuell=WEISS), "tippen*", 0.8),
    ficon("tabler", "rectangle-vertical", 640, 612, 34, beim("b1", "Rote"), fuell=ROT),
    # Krüger
    peep_voll("KR_ruhig", KX, BODEN, FH, "buero", d=0.3, bis="k1"),
    *redet("KR_zweifel", KX, BODEN, FH, "k1", "b2"),
    peep_voll("KR_schock", KX, BODEN, FH, "b2", anim="cut"),
    pille("Pressesprecher Krüger", KX, BODEN + 22, "buero", fill=TUERKIS, size=30, anker="m", d=0.5),
    # Sprechblasen
    blase("sprech", 640, 230, "b1", 780, 210, inhalt=["Das poste ich sofort:", "Rote Karte für Partei X!"], textsize=34,
          figur=BR1, bis="k1"),
    blase("sprech", 620, 210, "k1", 1160, 210, inhalt=["Über den offiziellen Kanal", "des Ministeriums?"], textsize=34,
          figur=("KR_zweifel", KX, BODEN, FH), bis="b2"),
    blase("sprech", 600, 210, "b2", 780, 210, inhalt=["Natürlich.", "Dort lesen es die meisten."], textsize=34,
          figur=("BR_cool_r", BX, BODEN, FH)),
])

# B Fall: der Beitrag ---------------------------------------------------------------------------------------------------
PX0, PY0, PW, PH = 700, 90, 520, 800    # Handy-Ansicht des Beitrags
folie([("post", "Fall · Der Beitrag")], [
    karte(PX0, PY0, PW, PH, "post", fill=WEISS, rund=44),
    ficon(HC, "eagle", 785, 225, 96, beim("post", "Wappen"), fuell=GELB),
    z("Bundesministerium", 850, 130, "post", "Bold", 32, rechts=1210),
    z("offizieller Kanal", 850, 178, "post", size=28, farbe=TEXT, rechts=1210),
    linienzug([(PX0 + 20, 255), (PX0 + PW - 20, 255)], "post", breite=4, farbe=INK),
    ficon("tabler", "rectangle-vertical", 960, 545, 150, "post2", fuell=ROT),
    z("Rote Karte für Partei X!", 735, 570, "post2", "ExtraBold", 34, rechts=1210),
    z("Ihre Redner treiben die", 735, 630, beim("post2", "Ihre"), size=32, rechts=1210),
    z("Radikalisierung voran.", 735, 675, beim("post2", "Ihre"), size=32, rechts=1210),
    z("Wer am Samstag mitläuft,", 735, 745, "post3", "Bold", 32, rechts=1210),
    z("stärkt sie.", 735, 790, "post3", "Bold", 32, rechts=1210),
    peep_voll("BR_cool_r", 330, BODEN, FH, "post", bis="post3"),
    peep_voll("BR_zufrieden_r", 330, BODEN, FH, "post3", anim="cut"),
    pille("Ministerin Brandt", 330, BODEN + 22, "post", fill=LILA, size=30, anker="m"),
    peep_voll("KR_schock", 1600, BODEN, FH, "post"),
    pille("Pressesprecher Krüger", 1600, BODEN + 22, "post", fill=TUERKIS, size=30, anker="m"),
])

# C Fall: Mia liest den Beitrag -----------------------------------------------------------------------------------------
MX = 1500
folie([("mia", "Fall · Die Leserin")], [
    linienzug([(60, BODEN), (1860, BODEN)], "mia", breite=7, farbe=INK),
    ficon(HC, "placard", 560, BODEN - 2, 300, beim("mia", "Kundgebung"), fuell=ORANGE),
    pille("Kundgebung Partei X · Samstag", 560, 400, beim("mia", "Kundgebung"), fill=ORANGE, size=32, anker="m"),
    peep_voll("MI_neugierig", MX, BODEN, FH, "mia", bis="m1"),
    *redet("MI_unsicher", MX, BODEN, FH, "m1", "hahn"),
    pille("Studentin Mia", MX, BODEN + 22, "mia", fill=GRUEN, size=30, anker="m", d=0.2),
    ficon("tabler", "device-mobile", 1330, 640, 100, beim("mia", "eigentlich"), fuell=WEISS),
    ficon("tabler", "rectangle-vertical", 1330, 610, 38, beim("mia", "eigentlich"), fuell=ROT, d=0.1),
    blase("sprech", 700, 210, "m1", 1000, 210, inhalt=["Wenn sogar die Ministerin das sagt,", "bleibe ich lieber weg."],
          textsize=32, figur=("MI_unsicher", MX, BODEN, FH)),
])

# D Fall: Partei X will nach Karlsruhe, die Frage ----------------------------------------------------------------------
HX = 1460
folie([("hahn", "Fall · Partei X"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "hahn", breite=7, farbe=INK),
    pille("Partei X", 1460, 60, "hahn", fill=ORANGE, size=48, anker="m"),
    ficon("tabler", "flag", 1790, BODEN - 2, 150, "hahn", fuell=ORANGE, d=0.2),
    peep_voll("HA_ernst", HX, BODEN, FH, "hahn", bis="h1"),
    *redet("HA_wuetend", HX, BODEN, FH, "h1", "frage"),
    peep_voll("HA_ernst", HX, BODEN, FH, "frage", anim="cut"),
    pille("Vorsitzender Hahn", HX, BODEN + 22, "hahn", fill=ORANGE, size=30, anker="m", d=0.2),
    blase("sprech", 620, 210, "h1", 860, 220, inhalt=["Das ist Missbrauch des Amtes!", "Wir gehen nach Karlsruhe."],
          textsize=34, figur=("HA_wuetend", HX, BODEN, FH), bis="frage"),
    ficon(HC, "classical-building", 300, 640, 220, beim("h1", "Karlsruhe"), fuell=WEISS),
    pille("Karlsruhe", 300, 660, beim("h1", "Karlsruhe"), fill=WEISS, size=30, anker="m"),
    pille("Durfte die Ministerin so posten?", 840, 250, "frage", fill=PINK, size=40, anker="m"),
    ficon("tabler", "podium", 540, 600, 110, beim("frage", "Parteitag"), fuell=LILA),
    pille("Und auf dem Parteitag?", 880, 530, beim("frage", "Parteitag"), fill=PINK, size=40, anker="m"),
])

# E Sachverhalt -----------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Partei X kündigt für Samstag eine Kundgebung gegen die Politik der Bundesregierung an. Bundesministerin Brandt "
    "veröffentlicht daraufhin über den offiziellen Social-Media-Kanal ihres Ministeriums, mit dem Wappen des Ministeriums "
    "im Profil: „Rote Karte für Partei X! Ihre Redner treiben die Radikalisierung voran. Wer am Samstag mitläuft, stärkt sie.“",
    "Die Studentin Mia beschließt, der Kundgebung fernzubleiben. Partei X will vor das Bundesverfassungsgericht ziehen.",
    "(Frei nach BVerfGE 148, 11 – 2 BvE 1/16, „Rote Karte“; Personen und Partei erfunden.)",
], "Hat Ministerin Brandt Partei X in ihren Rechten verletzt?")

# F Zulässigkeit: Organstreit ----------------------------------------------------------------------------------------------
FX, BR, FR = 1560, 930, 500
HA2, BR2 = 1415, 1730
folie([("zul", "A. Zulässigkeit › Organstreit, Art. 94 I Nr. 1 GG"), ("bet", "A. Zulässigkeit › Beteiligtenfähigkeit"),
       ("gegenst", "A. Zulässigkeit › Maßnahme"), ("befugt", "A. Zulässigkeit › Antragsbefugnis"),
       ("rsb", "A. Zulässigkeit › Rechtsschutzbedürfnis"), ("frist", "A. Zulässigkeit › Frist, § 64 III BVerfGG")], rechts_frei([
    *tafel("zul", "A. Zulässigkeit: Organstreit"),
    z("Organstreit, Art. 94 I Nr. 1 GG", 110, 190, beim("zul", "Organstreitverfahren"), "Bold", 38),
    z("§§ 13 Nr. 5, 63 ff. BVerfGG · bis 27.12.2024: Art. 93 I Nr. 1 GG", 110, 245, beim("zul", "Grundgesetz"),
      size=28, farbe=TEXT),
    ok(135, 345, beim("bet", "Beteiligtenfähig"), gr=22), z("Beteiligte: Partei X (Status aus Art. 21 GG)", 175, 325,
                                                          beim("bet", "Beteiligtenfähig"), size=34),
    ok(135, 415, "bet2", gr=22), z("Ministerin (Art. 65 S. 2 GG: eigene Rechte)", 175, 395, "bet2", size=34),
    ok(135, 485, "gegenst", gr=22), z("Maßnahme: der Beitrag", 175, 465, "gegenst", size=34),
    ok(135, 555, "befugt", gr=22), z("Antragsbefugnis: Verletzung möglich", 175, 535, "befugt", size=34),
    ok(135, 625, beim("rsb", "Rechtsschutzbedürfnis"), gr=22),
    z("Rechtsschutzbedürfnis: Wiederholungsgefahr", 175, 605, beim("rsb", "Rechtsschutzbedürfnis"), size=34),
    ok(135, 695, "frist", gr=22), z("Frist: sechs Monate, § 64 III BVerfGG", 175, 675, "frist", size=34),
    ficon(HC, "classical-building", 1560, 300, 200, "zul", fuell=WEISS, bis="rsb"),
    pille("Bundesverfassungsgericht", 1560, 315, "zul", fill=WEISS, size=28, anker="m", bis="rsb"),
    peep_voll("HA_ernst", HA2, BR, FR, "zul"),
    pille("Antragsteller", HA2, BR + 22, "bet", fill=ORANGE, size=28, anker="m"),
    peep_voll("BR_denkt", BR2, BR, FR, "bet2"),
    pille("Antragsgegnerin", BR2, BR + 22, "bet2", fill=LILA, size=28, anker="m"),
    ficon("tabler", "trash", 1480, 300, 110, beim("rsb", "gelöscht"), fuell=GRAU, bis="frist"),
    ficon("tabler", "repeat", 1660, 300, 110, beim("rsb", "wiederholen"), fuell=GELB, bis="frist"),
    ficon("tabler", "calendar", 1560, 280, 120, "frist", fuell=WEISS),
    pille("6 Monate", 1560, 300, beim("frist", "sechs"), fill=GELB, size=30, anker="m"),
]))

# G Begründetheit: Maßstab -----------------------------------------------------------------------------------------------
folie([("mass", "B. Begründetheit › Maßstab, Art. 20 II GG"), ("art21", "B. Begründetheit › Chancengleichheit, Art. 21 I GG"),
       ("info", "B. Begründetheit › Öffentlichkeitsarbeit")], rechts_frei([
    *tafel("mass", "B. Begründetheit: Maßstab"),
    z("Art. 20 II GG: Alle Staatsgewalt geht vom Volke aus", 110, 190, "art20", "Bold", 34),
    z("Willensbildung: vom Volk zu den Staatsorganen", 150, 250, beim("art20", "Willensbildung"), size=32),
    nein(175, 325, beim("art20", "umgekehrt"), gr=20), z("nicht umgekehrt", 210, 305, beim("art20", "umgekehrt"), size=32),
    z("Art. 21 I GG: Chancengleichheit der Parteien", 110, 400, "art21", "Bold", 36),
    z("→ Staatsorgane müssen neutral bleiben", 150, 460, beim("art21", "neutral"), size=34),
    z("auch außerhalb des Wahlkampfs", 150, 515, "immer", size=34),
    z("Öffentlichkeitsarbeit: Politik erklären,", 110, 620, "info", "Bold", 34),
    z("Kritik zurückweisen", 150, 675, beim("info", "Kritik"), "Bold", 34),
    pille("aber nur sachlich", 110, 750, beim("info", "sachlich"), fill=GELB, size=34),
    # Volk -> Staatsorgane
    ficon("tabler", "building-bank", 1560, 360, 200, "art20", fuell=GELB, bis="art21"),
    ficon("tabler", "users", 1560, 880, 220, "art20", fuell=BLAU, d=0.2, bis="art21"),
    pfeil(1480, 650, 1480, 400, beim("art20", "Willensbildung"), breite=10, kopf=30, bis="art21"),
    pfeil(1650, 400, 1650, 650, beim("art20", "umgekehrt"), breite=10, kopf=30, bis="art21"),
    bis_(kreuz_i(1650, 525, beim("art20", "umgekehrt"), gr=34), "art21"),
    # gleiche Chancen für alle Parteien
    ficon("tabler", "scale", 1560, 520, 260, "art21", fuell=GELB, bis="info"),
    pille("Partei A", 1365, 600, beim("art21", "Parteien"), fill=BLAU, size=28, anker="m", bis="info"),
    pille("Partei B", 1560, 600, beim("art21", "Parteien"), fill=GRUEN, size=28, anker="m", d=0.1, bis="info"),
    pille("Partei X", 1755, 600, beim("art21", "Parteien"), fill=ORANGE, size=28, anker="m", d=0.2, bis="info"),
    ficon("tabler", "calendar", 1560, 860, 150, "immer", fuell=WEISS, bis="info"),
    # Regierung informiert
    ficon("tabler", "presentation", 1420, 400, 200, "info", fuell=WEISS),
    peep_voll("BR_ruhig", 1700, BR, FR, "info"),
]))

# H Schritt 1: amtliches Handeln? -------------------------------------------------------------------------------------------
folie([("amt", "B. Begründetheit › I. Amtliches Handeln?"), ("mittel", "B. Begründetheit › I. Autorität oder Ressourcen des Amtes"),
       ("sub_amt", "B. Begründetheit › I. Amtliches Handeln (+)")], rechts_frei([
    *tafel("amt", "I. Amtliches Handeln?"),
    z("Ministerin oder Parteipolitikerin?", 110, 190, beim("amt", "Hat"), "Bold", 38),
    z("Parteipolitik erlaubt, aber ohne Mittel des Amtes", 150, 250, "pp", size=32),
    z("Amtlich: Autorität oder Ressourcen des Amtes", 110, 345, "mittel", "Bold", 36),
    z("• Pressemitteilungen", 150, 405, beim("mittel", "Pressemitteilungen"), size=34),
    z("• Internetseite des Ministeriums", 150, 455, beim("mittel", "Internetseite"), size=34),
    z("• Staatssymbole", 150, 505, beim("mittel", "Staatssymbole"), size=34),
    z("• offizielle Konten in sozialen Medien („dürfte“)", 150, 555, "konto", size=34),
    fl_block(110, 650, 1040, 150, GRUEN, "sub_amt", [("Dienstkanal mit Wappen: amtlich (+)", "ExtraBold", 40, INK),
                                                     ("Brandt handelt als Ministerin", "Regular", 32, INK)]),
    ficon("tabler", "building-bank", 1400, 290, 140, beim("amt", "Ministerin"), fuell=GELB, bis="mittel"),
    pille("Ministerin", 1400, 305, beim("amt", "Ministerin"), fill=GELB, size=28, anker="m", bis="mittel"),
    ficon("tabler", "podium", 1720, 290, 140, beim("amt", "Parteipolitikerin"), fuell=LILA, bis="mittel"),
    pille("Parteipolitikerin", 1720, 305, beim("amt", "Parteipolitikerin"), fill=LILA, size=28, anker="m", bis="mittel"),
    ficon("tabler", "file-text", 1380, 300, 110, beim("mittel", "Pressemitteilungen"), fuell=WEISS, bis="konto"),
    ficon("tabler", "world", 1560, 300, 110, beim("mittel", "Internetseite"), fuell=BLAU, bis="konto"),
    ficon(HC, "eagle", 1740, 300, 110, beim("mittel", "Staatssymbole"), fuell=GELB, bis="konto"),
    ficon("tabler", "device-mobile", 1560, 330, 120, "konto", fuell=WEISS),
    ficon(HC, "eagle", 1560, 268, 40, beim("sub_amt", "Wappen"), fuell=GELB),
    ficon("tabler", "rectangle-vertical", 1560, 312, 30, beim("sub_amt", "Wappen"), fuell=ROT),
    peep_voll("BR_denkt", FX, BR, FR, "amt", bis="sub_amt"),
    peep_voll("BR_ertappt", FX, BR, FR, "sub_amt", anim="cut"),
]))

# I Schritt 2: Eingriff ----------------------------------------------------------------------------------------------------
folie([("eingriff", "B. Begründetheit › II. Eingriff in Art. 21 I GG")], rechts_frei([
    *tafel("eingriff", "II. Eingriff in Art. 21 I GG"),
    ok(135, 220, "rk", gr=22), z("Rote Karte: einseitig negative Bewertung", 175, 200, "rk", size=36),
    ok(135, 300, "abschreck", gr=22), z("soll Menschen von der Kundgebung fernhalten", 175, 280, "abschreck", size=36),
    z("Schon abschreckende Wirkung genügt", 175, 380, "mia2", "Bold", 36),
    fl_block(110, 480, 1040, 110, GRUEN, beim("mia2", "greift"), [("Eingriff (+)", "ExtraBold", 42, INK)]),
    ficon("tabler", "rectangle-vertical", 1420, 420, 170, "rk", fuell=ROT),
    ficon(HC, "placard", 1720, 420, 210, "abschreck", fuell=ORANGE),
    kreuz_i(1720, 300, beim("abschreck", "fernhalten"), gr=40),
    peep_voll("MI_liest", 1560, BR, FR, "eingriff", bis="mia2"),
    peep_voll("MI_unsicher", 1560, BR, FR, "mia2", anim="cut"),
    pille("Mia", 1560, BR + 22, "eingriff", fill=GRUEN, size=28, anker="m"),
]))

# J Schritt 3: Rechtfertigung, Ergebnis ---------------------------------------------------------------------------------------
folie([("recht", "B. Begründetheit › III. Rechtfertigung?"), ("erg", "B. Begründetheit › Ergebnis")], rechts_frei([
    *tafel("recht", "III. Rechtfertigung?"),
    z("Befugnis: Kritik an der Regierung zurückweisen", 110, 190, beim("recht", "beruft"), "Bold", 34),
    nein(135, 290, beim("sach", "erklärt"), gr=22), z("erklärt keine Politik", 175, 270, beim("sach", "erklärt"), size=36),
    nein(135, 360, beim("sach", "widerlegt"), gr=22), z("widerlegt keinen Vorwurf", 175, 340, beim("sach", "widerlegt"), size=36),
    nein(135, 430, beim("sach", "wertet"), gr=22), z("wertet nur ab", 175, 410, beim("sach", "wertet"), size=36),
    z("Kein „Recht auf Gegenschlag“", 110, 500, "gegenschlag", "Bold", 38),
    fl_block(110, 590, 1040, 140, GRUEN, "erg", [("Verletzung von Art. 21 I GG", "ExtraBold", 42, INK),
                                                ("Recht auf Chancengleichheit", "Regular", 32, INK)]),
    z("BVerfGE 148, 11 (2018): Rote Karte auf Ministeriumsseite", 110, 775, "wanka", size=30, farbe=TEXT),
    ficon("tabler", "arrow-back-up", 1560, 330, 150, "gegenschlag", fuell=ROT, bis="erg"),
    bis_(kreuz_i(1560, 260, beim("gegenschlag", "gibt"), gr=44), "erg"),
    ficon(HC, "classical-building", 1560, 330, 200, "erg", fuell=WEISS),
    peep_voll("BR_cool", 1720, BR, FR, "recht", bis="gegenschlag"),
    peep_voll("BR_ertappt", 1720, BR, FR, "gegenschlag", anim="cut"),
    peep_voll("HA_zufrieden", 1400, BR, FR, "erg"),
]))

# K Gegenfall: Parteitag --------------------------------------------------------------------------------------------------
PTX = 1530
folie([("parteitag", "Gegenfall · Rede auf dem Parteitag"), ("titel", "Gegenfall · Ministertitel"),
       ("repost", "Gegenfall · Ministerium teilt das Video"), ("urt20", "Gegenfall · BVerfGE 154, 320 (2020)")], rechts_frei([
    *tafel("parteitag", "Gegenfall: Rede auf dem Parteitag", size=46),
    ok(135, 220, beim("parteitag", "Parteipolitikerin"), gr=22),
    z("als Parteipolitikerin, ohne Mittel des Amtes", 175, 200, beim("parteitag", "Parteipolitikerin"), size=34),
    ok(135, 290, "pt2", gr=22), z("scharfe Kritik an Partei X erlaubt", 175, 270, "pt2", size=34),
    ok(135, 360, beim("pt2", "Neutralitätsgebot"), gr=22),
    z("Neutralitätsgebot greift dort nicht", 175, 340, beim("pt2", "Neutralitätsgebot"), size=34),
    ok(135, 430, "titel", gr=22), z("Ministertitel allein macht nicht amtlich", 175, 410, "titel", size=34),
    nein(135, 510, beim("repost", "Teilt"), gr=22),
    z("Ministerium teilt das Video: Mittel des Amtes", 175, 490, beim("repost", "Teilt"), "Bold", 34),
    z("BVerfGE 154, 320 (2020):", 110, 590, "urt20", "Bold", 34),
    *plusminus("Interview zulässig", 150, 650, beim("urt20", "Interview"), True, size=34),
    *plusminus("Veröffentlichung auf der Ministeriumsseite", 150, 710, beim("urt20", "Veröffentlichung"), False, size=34),
    pille("Parteitag", 1560, 70, "parteitag", fill=LILA, size=44, anker="m"),
    peep_voll("BR_kaempft", PTX, BR, 520, "parteitag", bis="repost"),
    peep_voll("BR_ertappt", PTX, BR, 520, "repost", anim="cut"),
    ficon("tabler", "podium", PTX, BR, 240, "parteitag", fuell=LILA, d=0.1),
    pille("Ministerin Brandt", PTX, 830, "titel", fill=WEISS, size=24, anker="m"),
    szene(ficon("tabler", "users", 1320, BR, 110, beim("parteitag", "Parteitag"), fuell=BLAU), "applaus*", 0.7),
    ficon("tabler", "users", 1810, BR, 110, beim("parteitag", "Parteitag"), fuell=GRUEN, d=0.1),
    ficon("tabler", "device-mobile", 1780, 400, 120, beim("repost", "Teilt"), fuell=WEISS),
    ficon(HC, "eagle", 1780, 345, 44, beim("repost", "Teilt"), fuell=GELB, d=0.1),
    ficon("tabler", "share", 1780, 230, 80, beim("repost", "Kanal"), fuell=GELB),
]))

# L Linie 2022 (ohne Figur: reale Person) -------------------------------------------------------------------------------------
folie([("kanzler", "Linie · BVerfGE 162, 207 (2022)")], rechts_frei([
    *tafel("kanzler", "BVerfGE 162, 207 (2022)"),
    z("Gleicher Maßstab für die Kanzlerin", 110, 190, beim("kanzler", "galt"), "Bold", 38),
    ok(135, 290, beim("kanzler", "Pressekonferenz"), gr=22),
    z("Pressekonferenz im Ausland: amtlich", 175, 270, beim("kanzler", "Pressekonferenz"), size=36),
    ok(135, 360, beim("kanzler", "verletzte"), gr=22),
    z("verletzte die Chancengleichheit", 175, 340, beim("kanzler", "verletzte"), size=36),
    z("Rechtfertigung möglich:", 110, 450, "kanzler3", "Bold", 36),
    z("• Stabilität der Regierung", 150, 510, beim("kanzler3", "Stabilität"), size=34),
    z("• Ansehen im Ausland", 150, 565, beim("kanzler3", "Ansehen"), size=34),
    pille("nur wenn wirklich gefährdet", 110, 650, beim("kanzler3", "wirklich"), fill=ROT, size=36),
    ficon("tabler", "plane", 1560, 330, 200, beim("kanzler", "Ausland"), fuell=BLAU),
    ficon("tabler", "microphone", 1560, 600, 130, beim("kanzler", "Pressekonferenz"), fuell=GRAU),
    ficon("tabler", "scale", 1560, 880, 230, "kanzler3", fuell=GELB),
]))

# M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Erst amtlich, dann neutral"), ("tipp2", "Klausurtipp · Art. 94 I Nr. 1 GG")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Zuerst prüfen: amtlich gehandelt?", 200, 200, beim("tipp", "Prüfe"), "Bold", 36),
    z("Erst dann: Neutralität und Sachlichkeit", 200, 280, "tipp1", size=36),
    z("Organstreit heute: Art. 94 I Nr. 1 GG", 200, 390, "tipp2", "Bold", 36),
    z("ältere Urteile: Art. 93 I Nr. 1 GG a. F.", 200, 450, beim("tipp2", "Ältere"), size=32, farbe=TEXT),
    z("(Neufassung in Kraft seit 28.12.2024)", 200, 500, beim("tipp2", "Ältere"), size=32, farbe=TEXT),
    *redet("LX_warnt", LXX, BR, FR + 40, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# N Klausurschema ---------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Äußerung einer Ministerin", 110, 90, "sch", 54),
    z("A. Zulässigkeit: Organstreit, Art. 94 I Nr. 1 GG", K1, 190, "s1", "Bold", 40, rechts=1820),
    z("I. Beteiligte (Partei: Art. 21 GG; Ministerin: Art. 65 S. 2 GG)", K2, 252, "s1b", size=34, farbe=TEXT, rechts=1820),
    z("II. Maßnahme", K2, 304, beim("s1b", "Maßnahme"), size=34, farbe=TEXT, rechts=1820),
    z("III. Antragsbefugnis", K2, 356, beim("s1b", "Antragsbefugnis"), size=34, farbe=TEXT, rechts=1820),
    z("IV. Rechtsschutzbedürfnis", K2, 408, beim("s1b", "Rechtsschutzbedürfnis"), size=34, farbe=TEXT, rechts=1820),
    z("V. Frist: sechs Monate, § 64 III BVerfGG", K2, 460, beim("s1b", "Frist"), size=34, farbe=TEXT, rechts=1820),
    z("B. Begründetheit", K1, 550, "s2", "Bold", 40, rechts=1820),
    z("I. Recht auf Chancengleichheit, Art. 21 I GG", K2, 615, "s2a", size=38, rechts=1820),
    z("II. Amtliches Handeln: Autorität oder Ressourcen des Amtes", K2, 677, "s2b", size=38, rechts=1820),
    z("III. Eingriff durch einseitige Parteinahme", K2, 739, "s2c", size=38, rechts=1820),
    z("IV. Rechtfertigung, vor allem Sachlichkeit", K2, 801, "s2d", size=38, rechts=1820),
])

# O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Als Parteipolitikerin darf", 0)], [("die Ministerin ", 0), ("austeilen.", "a")]], 750, 320, 54, "merke",
                {"a": beim("merke", "austeilen")}),
    *markertext([[("Wer Amt und Kanäle nutzt,", 0)], [("muss ", 0), ("neutral", "b"), (" und ", 0), ("sachlich", "c")],
                 [("bleiben.", 0)]], 750, 560, 50, "m2", {"b": beim("m2", "neutral"), "c": beim("m2", "sachlich")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
