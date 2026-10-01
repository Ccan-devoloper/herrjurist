"""Folge 013 · Luftsicherheitsgesetz: Darf der Staat ein Flugzeug abschießen? – Serienstandard Open Peeps (Katzenkönig).
Frei nach BVerfGE 115, 118 (1 BvR 357/05); Plenum BVerfGE 132, 1 (2 PBvU 1/11); LuftSiG i. d. F. vom 11.3.2026 (§ 15a).
Personen erfunden. Szenen laut ../SZENENPLAN.md: A Entführung, B Alarmrotte, C Lagezentrum, D Vielflieger/Frage,
E Sachverhalt, F Zulässigkeit, G Schutzbereich/Eingriff/Schranke, H formell (Wehrverfassung), I materiell (Menschenwürde),
J Einwände, K Schutzpflicht/Ergebnis, L Gegenfall nur Täter, M heute (§ 15a) und Strafrecht, N Klausurtipp (Lexi),
O Klausurschema, P Merksatz (Lexi). Sensibles Thema: Flugzeug nur als Icon, Abschuss nur als Frage/Pfeil, kein Treffer.
Geräusche nur bei sichtbarer Handlung (Kampfjets steigen auf, Funkspruch der Pilotin)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_013/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = dict(bausteine.BG_FARBE)
PFAD_FARBE = dict(bausteine.PFAD_FARBE)
HELL = (255, 251, 230, 255)
GRAU = (176, 178, 190, 255)
HIMMEL = (226, 236, 252, 255)
DAUER = bausteine._cj()["dauer"]
HC = "fluent-emoji-high-contrast"
NULL = ("lage", -round(bausteine._t("lage") + 0.4, 3))   # 0,4 s vor Hauptfilmbeginn: ab 0,0 s voll sichtbar (Pop/Fade fertig)


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


def frage_pfeil(x1, y1, x2, y2, cue, bis=None):
    """Abschuss nur als Frage: gestrichelter Pfeil mit Fragezeichen, kein Treffer."""
    import math
    els, n = [], 7
    for i in range(n):
        a, b = i / n, (i + 0.55) / n
        p, q = (x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)
        if i < n - 1:
            els.append(bis_(linienzug([p, q], cue, breite=7, farbe=DROT), bis))
        else:
            els.append(pfeil(p[0], p[1], x2, y2, cue, breite=7, kopf=24, farbe=DROT, bis=bis))
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    els.append(pille("?", mx - 30, my - 95, cue, fill=WEISS, size=44, farbe=DROT, bis=bis))
    return els


BODEN, FH = 880, 470
BR, FR = 930, 500

# A Fall: die Entführung -------------------------------------------------------------------------------------------------
folie([(NULL, "Fall · Die Entführung")], [
    ficon("tabler", "cloud", 260, 300, 200, NULL, fuell=WEISS),
    ficon("tabler", "cloud", 1700, 230, 170, NULL, fuell=WEISS),
    ficon("tabler", "cloud", 1080, 160, 130, NULL, fuell=WEISS),
    bewegt(ficon("tabler", "plane", 640, 640, 300, NULL, fuell=WEISS), NULL, beim("lage", "Berlin", ende=True), -260, 120),
    pille("auf dem Weg nach Berlin", 640, 690, beim("lage", "Berlin"), fill=BLAU, size=34, anker="m"),
    pille("140 Menschen an Bord", 640, 780, beim("lage", "hundertvierzig"), fill=WEISS, size=34, anker="m"),
    ficon("tabler", "alert-triangle", 640, 360, 90, "entf", fuell=ROT),
    pille("in der Gewalt von Entführern", 640, 220, "entf", fill=ROT, size=34, anker="m"),
    linienzug([(1200, BODEN), (1860, BODEN)], "drohung", breite=7, farbe=INK),
    ficon("tabler", "building-stadium", 1560, BODEN - 2, 360, "drohung", fuell=GRUEN),
    pille("volles Fußballstadion", 1560, BODEN + 24, beim("drohung", "Fußballstadion"), fill=GRUEN, size=32, anker="m"),
    *frage_pfeil(860, 520, 1380, 690, beim("drohung", "steuern")),
])

# B Fall: die Alarmrotte -------------------------------------------------------------------------------------------------
PIX, PIU, PIH = 1600, 860, 400
folie([("jets", "Fall · Die Alarmrotte")], [
    ficon("tabler", "cloud", 820, 170, 150, "jets", fuell=WEISS),
    ficon("tabler", "plane", 560, 600, 300, "jets", fuell=WEISS),
    pille("entführte Maschine", 560, 640, "jets", fill=WEISS, size=30, anker="m"),
    szene(bewegt(ficon("tabler", "plane", 300, 400, 150, beim("jets", "Kampfflugzeuge"), fuell=GRAU),
                 beim("jets", "Kampfflugzeuge"), beim("jets", "steigen"), -180, 380), "013jet*", 1.0),
    bewegt(ficon("tabler", "plane", 840, 860, 150, beim("jets", "Kampfflugzeuge"), fuell=GRAU, d=0.2),
           beim("jets", "Kampfflugzeuge"), beim("jets", "steigen"), 120, 180),
    pille("Luftwaffe", 300, 180, beim("jets", "Luftwaffe"), fill=GRAU, size=30, anker="m"),
    pille("warnen", 300, 760, beim("warn", "warnen"), fill=GELB, size=32, anker="m"),
    pille("abdrängen", 300, 850, beim("warn", "abzudrängen"), fill=GELB, size=32, anker="m"),
    # Funkbild der Pilotin
    karte(1360, 420, 480, 440, "meldet", fill=HIMMEL),
    peep_voll("PI_ruhig", PIX, PIU, PIH, "meldet", bis="p1"),
    *redet("PI_redet", PIX, PIU, PIH, "p1", "minister"),
    szene(ficon("tabler", "headset", 1430, 520, 90, "meldet", fuell=GELB), "013funk*", 0.8),
    pille("Pilotin", PIX, 900, "meldet", fill=GRUEN, size=30, anker="m"),
    blase("sprech", 720, 200, "p1", 1420, 230, inhalt=["Keine Reaktion. Die Maschine", "hält Kurs auf das Stadion."],
          textsize=34, figur=("PI_redet", PIX, PIU, PIH)),
])

# C Fall: die Entscheidung im Lagezentrum ---------------------------------------------------------------------------------
LX_, = (1480,)
folie([("minister", "Fall · Die Entscheidung")], [
    linienzug([(60, BODEN), (1860, BODEN)], "minister", breite=7, farbe=INK),
    pille("Lagezentrum", 70, 40, beim("minister", "Lagezentrum"), fill=GELB, size=44),
    ficon("tabler", "desk", 820, BODEN - 2, 420, "minister", fuell=GELB, d=0.1),
    ficon("tabler", "device-desktop", 820, 700, 230, "minister", fuell=WEISS, d=0.2),
    ficon("tabler", "radar-2", 820, 610, 90, "minister", fuell=GRUEN, d=0.3),
    peep_voll("LO_ruhig", LX_, BODEN, FH, "minister", bis="l1"),
    *redet("LO_redet", LX_, BODEN, FH, "l1", "gesetz"),
    peep_voll("LO_denkt", LX_, BODEN, FH, "gesetz", anim="cut"),
    pille("Verteidigungsminister Lorenz", LX_, BODEN + 22, beim("minister", "Verteidigungsminister"), fill=BLAU, size=28,
          anker="m"),
    blase("sprech", 820, 220, "l1", 980, 230, inhalt=["140 an Bord, 50.000 im Stadion.", "Darf ich den Abschuss befehlen?"],
          textsize=34, figur=("LO_redet", LX_, BODEN, FH), bis="gesetz"),
    ficon("tabler", "plane", 450, 560, 200, beim("l1", "Abschuss"), fuell=WEISS, bis="gesetz"),
    ficon("tabler", "plane", 170, 330, 130, beim("l1", "Abschuss"), fuell=GRAU, bis="gesetz"),
    *frage_pfeil(240, 290, 350, 420, beim("l1", "Abschuss"), bis="gesetz"),
    # Das Gesetz von 2005
    karte(110, 120, 1060, 330, "gesetz", fill=WEISS),
    ficon("tabler", "book", 200, 250, 100, "gesetz", fuell=GELB),
    z("Luftsicherheitsgesetz (2005)", 280, 165, "gesetz", "Bold", 40),
    z("§ 14 III: mit Waffengewalt auf ein Flugzeug einwirken,", 160, 290, "p143", size=32),
    z("das gegen das Leben von Menschen eingesetzt werden soll", 160, 340, beim("p143", "gegen"), size=32),
    pille("als einziges Mittel", 160, 385, "einzig", fill=ROT, size=30),
])

# D Fall: der Vielflieger, die Frage ---------------------------------------------------------------------------------------
SX = 1520
folie([("seiler", "Fall · Der Vielflieger"), ("frage", "Fall · Die Frage")], [
    linienzug([(60, BODEN), (1860, BODEN)], "seiler", breite=7, farbe=INK),
    ficon("tabler", "building-airport", 420, BODEN - 2, 330, "seiler", fuell=BLAU),
    ficon("tabler", "plane-departure", 420, 470, 150, "seiler", fuell=WEISS, d=0.2),
    ficon("tabler", "luggage", 1300, BODEN - 2, 120, "seiler", fuell=LILA, d=0.2),
    pille("fast jede Woche", 830, 560, beim("seiler", "fast"), fill=GELB, size=34, anker="m"),
    ficon("tabler", "calendar-repeat", 830, 540, 110, beim("seiler", "fast"), fuell=WEISS),
    peep_voll("SE_ruhig", SX, BODEN, FH, "seiler", bis="s1"),
    *redet("SE_redet", SX, BODEN, FH, "s1", "frage"),
    peep_voll("SE_sorge", SX, BODEN, FH, "frage", anim="cut"),
    pille("Herr Seiler", SX, BODEN + 22, "seiler", fill=LILA, size=30, anker="m", d=0.2),
    blase("sprech", 900, 260, "s1", 900, 210, inhalt=["Dann dürfte der Staat auch", "mein Flugzeug abschießen.",
                                                      "Dagegen wehre ich mich in Karlsruhe."],
          textsize=34, figur=("SE_redet", SX, BODEN, FH), bis="frage"),
    ficon(HC, "classical-building", 830, 830, 160, beim("s1", "Karlsruhe"), fuell=WEISS, bis="frage"),
    pille("Karlsruhe", 830, 845, beim("s1", "Karlsruhe"), fill=WEISS, size=26, anker="m", bis="frage"),
    pille("Darf der Staat ein entführtes Flugzeug abschießen,", 760, 100, "frage", fill=PINK, size=36, anker="m"),
    pille("um andere zu retten,", 760, 180, beim("frage", "um"), fill=PINK, size=36, anker="m"),
    pille("auch wenn Unbeteiligte an Bord sind?", 760, 260, beim("frage", "auch"), fill=PINK, size=36, anker="m"),
])

# E Sachverhalt ---------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Entführer bringen ein Passagierflugzeug mit 140 Menschen an Bord in ihre Gewalt und kündigen an, es in ein volles "
    "Fußballstadion zu steuern. Zwei Kampfflugzeuge der Luftwaffe warnen die Maschine und versuchen, sie abzudrängen; ohne "
    "Erfolg. Verteidigungsminister Lorenz fragt sich, ob er den Abschuss befehlen darf. § 14 Abs. 3 LuftSiG (Fassung 2005) "
    "erlaubt, als einziges Mittel mit Waffengewalt auf ein Flugzeug einzuwirken, das gegen das Leben von Menschen "
    "eingesetzt werden soll.",
    "Herr Seiler fliegt fast jede Woche. Er erhebt Verfassungsbeschwerde unmittelbar gegen § 14 Abs. 3 LuftSiG.",
    "(Frei nach BVerfGE 115, 118 – 1 BvR 357/05; Personen erfunden.)",
], "Ist die Verfassungsbeschwerde zulässig und begründet?")

# F Zulässigkeit -----------------------------------------------------------------------------------------------------------
folie([("zul", "A. Zulässigkeit › Verfassungsbeschwerde, Art. 94 I Nr. 4a GG"),
       ("gegen", "A. Zulässigkeit › Beschwerdegegenstand: Gesetz"), ("befugt", "A. Zulässigkeit › Beschwerdebefugnis")],
      rechts_frei([
    *tafel("zul", "A. Zulässigkeit"),
    z("Verfassungsbeschwerde, Art. 94 I Nr. 4a GG", 110, 190, beim("zul", "Verfassungsbeschwerde"), "Bold", 38),
    z("§§ 13 Nr. 8a, 90 BVerfGG · bis 27.12.2024: Art. 93 I Nr. 4a GG", 110, 245, beim("zul", "Grundgesetz"),
      size=28, farbe=TEXT),
    z("Gegenstand: das Gesetz selbst (§ 14 III LuftSiG)", 110, 330, "gegen", "Bold", 36),
    z("Beschwerdebefugnis: Seiler muss betroffen sein", 110, 420, "befugt", "Bold", 36),
    ok(175, 510, beim("oft", "hinreichend"), gr=22), z("selbst", 215, 490, beim("befugt", "selbst"), size=34),
    ok(175, 570, beim("oft", "hinreichend"), gr=22), z("gegenwärtig", 215, 550, beim("befugt", "gegenwärtig"), size=34),
    ok(175, 630, beim("oft", "hinreichend"), gr=22), z("unmittelbar", 215, 610, beim("befugt", "unmittelbar"), size=34),
    pille("Vielflieger: Betroffenheit hinreichend wahrscheinlich", 110, 700, beim("oft", "hinreichend"), fill=GELB, size=32),
    ficon(HC, "classical-building", 1560, 330, 220, "zul", fuell=WEISS, bis="gegen"),
    ficon("tabler", "file-text", 1560, 330, 170, "gegen", fuell=WEISS, bis="oft"),
    pille("§ 14 III LuftSiG", 1560, 345, "gegen", fill=WEISS, size=30, anker="m", bis="oft"),
    ficon("tabler", "plane-departure", 1450, 330, 150, "oft", fuell=WEISS),
    ficon("tabler", "calendar-repeat", 1690, 330, 130, "oft", fuell=GELB, d=0.1),
    peep_voll("SE_ruhig", 1560, BR, FR, "zul", bis="befugt"),
    peep_voll("SE_denkt", 1560, BR, FR, "befugt", anim="cut", bis="oft"),
    peep_voll("SE_froh", 1560, BR, FR, "oft", anim="cut"),
    pille("Herr Seiler", 1560, BR + 22, "zul", fill=LILA, size=28, anker="m"),
]))

# G Begründetheit: Schutzbereich, Eingriff, Schranke ---------------------------------------------------------------------------
folie([("sb", "B. Begründetheit › I. Schutzbereich: Leben, Art. 2 II 1 GG"), ("ein", "B. Begründetheit › II. Eingriff"),
       ("schranke", "B. Begründetheit › III. Rechtfertigung: Gesetzesvorbehalt")], rechts_frei([
    *tafel("sb", "B. Begründetheit"),
    z("I. Recht auf Leben, Art. 2 II 1 GG", 110, 190, beim("sb", "Geschützt"), "Bold", 38),
    z("II. Eingriff: Abschuss führt mit an Sicherheit grenzender", 110, 290, "ein", "Bold", 34),
    z("Wahrscheinlichkeit zum Tod aller an Bord", 150, 340, beim("ein", "Wahrscheinlichkeit"), size=34),
    z("III. Rechtfertigung: Gesetzesvorbehalt, Art. 2 II 3 GG", 110, 440, "schranke", "Bold", 34),
    z("Eingriff auf Grund eines Gesetzes erlaubt", 150, 495, beim("schranke", "Gesetzes"), size=34),
    pille("aber nur, wenn es in jeder Hinsicht verfassungsgemäß ist", 110, 580, "jeder", fill=GELB, size=30),
    ficon("tabler", "activity-heartbeat", 1560, 330, 200, "sb", fuell=ROT, bis="ein"),
    ficon("tabler", "plane", 1560, 330, 200, "ein", fuell=WEISS, bis="schranke"),
    ficon("tabler", "book", 1560, 330, 170, "schranke", fuell=GELB),
    pille("Gesetz", 1560, 345, "schranke", fill=GELB, size=30, anker="m"),
    peep_voll("SE_ruhig", 1560, BR, FR, "sb", bis="ein"),
    peep_voll("SE_sorge", 1560, BR, FR, "ein", anim="cut", bis="schranke"),
    peep_voll("SE_denkt", 1560, BR, FR, "schranke", anim="cut"),
]))

# H Rechtfertigung formell: Wehrverfassung -------------------------------------------------------------------------------------
folie([("formell", "B. › III. 1. formell: Wehrverfassung"), ("art87", "B. › III. 1. formell: Art. 87a II GG"),
       ("art35", "B. › III. 1. formell: Art. 35 II 2, III GG"), ("plenum", "B. › III. 1. formell: Plenum 2012")],
      rechts_frei([
    *tafel("formell", "III. 1. Formell: Wehrverfassung", size=46),
    z("Art. 87a II GG: außer zur Verteidigung nur,", 110, 190, "art87", "Bold", 34),
    z("wo das Grundgesetz es ausdrücklich erlaubt", 150, 240, beim("art87", "wo"), size=34),
    z("Art. 35 II 2, III GG: Hilfe bei einem", 110, 320, "art35", "Bold", 34),
    z("besonders schweren Unglücksfall", 150, 370, beim("art35", "besonders"), size=34),
    nein(135, 470, "waffen", gr=22),
    z("spezifisch militärische Waffen (Bordwaffen)", 175, 450, "waffen", size=34),
    z("BVerfGE 115, 118 (2006), Erster Senat", 175, 500, beim("waffen", "Ersten"), size=28, farbe=TEXT),
    fl_block(110, 570, 1040, 250, BLAU, "plenum", []),
    z("Plenum 2012 (BVerfGE 132, 1): gelockert", 145, 605, "plenum", "ExtraBold", 36),
    z("militärische Mittel nicht grundsätzlich ausgeschlossen,", 145, 675, beim("plenum", "Militärische"), size=32),
    z("nur unter engen Voraussetzungen, als letztes Mittel", 145, 735, beim("plenum", "engen"), size=32),
    ficon("tabler", "shield", 1560, 320, 180, beim("art87", "Bundeswehr"), fuell=GRAU),
    pille("Bundeswehr", 1560, 335, beim("art87", "Bundeswehr"), fill=GRAU, size=28, anker="m"),
    ficon("tabler", "alert-triangle", 1430, 560, 130, "art35", fuell=GELB, bis="plenum"),
    pille("Unglücksfall", 1430, 575, "art35", fill=GELB, size=26, anker="m", bis="plenum"),
    ficon("tabler", "plane", 1700, 560, 140, "waffen", fuell=GRAU, bis="plenum"),
    bis_(kreuz_i(1700, 490, beim("waffen", "erlaubt"), gr=40), "plenum"),
    ficon(HC, "classical-building", 1430, 560, 190, "plenum", fuell=WEISS),
    pille("Plenum 2012", 1430, 575, "plenum", fill=BLAU, size=28, anker="m"),
    peep_voll("LO_denkt", 1760, BR, 330, "formell"),
]))

# I Rechtfertigung materiell: Menschenwürde --------------------------------------------------------------------------------------
folie([("mw", "B. › III. 2. materiell: Menschenwürde, Art. 1 I GG")], rechts_frei([
    *tafel("mw", "III. 2. Materiell: Menschenwürde", size=46),
    z("Art. 1 I GG: Die Würde des Menschen ist unantastbar.", 110, 190, beim("mw", "Menschenwürde"), "Bold", 34),
    z("Kein Mensch darf bloßes Objekt des Staates sein", 110, 260, "objekt", size=34),
    ok(135, 360, "ausweg", gr=22), z("Passagiere und Besatzung: ausweglose Lage", 175, 340, "ausweg", size=34),
    ok(135, 430, "rettung", gr=22), z("Tötung als Mittel, um andere zu retten", 175, 410, "rettung", size=34),
    fl_block(110, 510, 1040, 150, ROT, "objekt2", [("bloße Objekte der Rettungsaktion", "ExtraBold", 40, INK),
                                                  ("Würde der Unbeteiligten verletzt", "Regular", 32, INK)]),
    z("BVerfGE 115, 118 Rn. 121–124", 110, 700, beim("objekt2", "Rettungsaktion"), size=28, farbe=TEXT),
    ficon("tabler", "user-shield", 1560, 330, 190, "mw", fuell=GELB, bis="ausweg"),
    ficon("tabler", "plane", 1560, 330, 200, "ausweg", fuell=WEISS),
    ficon("tabler", "building-stadium", 1760, 520, 140, "rettung", fuell=GRUEN),
    ficon("tabler", "box", 1380, 520, 110, "objekt2", fuell=GRAU),
    pille("Objekt?", 1380, 535, "objekt2", fill=ROT, size=26, anker="m"),
    peep_voll("SE_ruhig", 1560, BR, 340, "mw", bis="objekt2"),
    peep_voll("SE_sorge", 1560, BR, 340, "objekt2", anim="cut"),
]))

# J Einwände ----------------------------------------------------------------------------------------------------------------------
folie([("ohnehin", "B. › III. 2. materiell: Einwände")], rechts_frei([
    *tafel("ohnehin", "Einwände – und warum sie nicht tragen", size=44),
    z("„Sie sterben doch ohnehin.“", 110, 200, "ohnehin", "Bold", 36),
    nein(135, 280, beim("ohnehin", "Das"), gr=22),
    z("Leben geschützt, egal wie lange es noch dauert", 175, 260, beim("ohnehin", "Das"), size=32),
    z("„Die Passagiere sind Teil der Waffe.“", 110, 380, "waffe", "Bold", 36),
    nein(135, 460, beim("waffe", "macht"), gr=22),
    z("macht sie zur Sache", 175, 440, beim("waffe", "macht"), size=32),
    z("„Wer einsteigt, willigt ein.“", 110, 560, "einw", "Bold", 36),
    nein(135, 640, beim("einw", "lebensfremde"), gr=22),
    z("lebensfremde Fiktion", 175, 620, beim("einw", "lebensfremde"), size=32),
    z("BVerfGE 115, 118 Rn. 131–134", 110, 720, beim("einw", "Fiktion"), size=28, farbe=TEXT),
    ficon("tabler", "hourglass", 1560, 330, 140, "ohnehin", fuell=GELB, bis="waffe"),
    ficon("tabler", "box", 1560, 330, 140, "waffe", fuell=GRAU, bis="einw"),
    ficon("tabler", "ticket", 1560, 330, 160, "einw", fuell=GELB),
    peep_voll("SE_denkt", 1560, BR, FR, "ohnehin", bis="einw"),
    peep_voll("SE_sorge", 1560, BR, FR, "einw", anim="cut"),
]))

# K Schutzpflicht, Ergebnis ---------------------------------------------------------------------------------------------------------
folie([("schutz", "B. › III. 2. materiell: Schutzpflicht"), ("erg", "B. Begründetheit › Ergebnis")], rechts_frei([
    *tafel("schutz", "Schutzpflicht – und Ergebnis", size=46),
    z("Schutzpflicht für die Menschen im Stadion", 110, 190, "schutz", "Bold", 36),
    z("aber nur mit verfassungsgemäßen Mitteln", 150, 250, "mittel", size=34),
    fl_block(110, 360, 1040, 170, GRUEN, "erg", [("§ 14 III LuftSiG verletzt Art. 2 II 1", "ExtraBold", 38, INK),
                                               ("i. V. m. Art. 1 I GG (Unbeteiligte an Bord)", "Regular", 32, INK)]),
    z("BVerfGE 115, 118 (15.2.2006): nichtig", 110, 580, "nichtig", "Bold", 36),
    ficon("tabler", "building-stadium", 1560, 330, 260, "schutz", fuell=GRUEN, bis="erg"),
    ficon("tabler", "shield", 1560, 300, 110, "schutz", fuell=WEISS, d=0.2, bis="erg"),
    ficon(HC, "classical-building", 1560, 330, 220, "erg", fuell=WEISS),
    ficon("tabler", "gavel", 1760, 330, 130, "nichtig", fuell=GELB),
    peep_voll("SE_denkt", 1560, BR, FR, "schutz", bis="erg"),
    peep_voll("SE_froh", 1560, BR, FR, "erg", anim="cut"),
]))

# L Gegenfall: nur Täter an Bord ---------------------------------------------------------------------------------------------------
folie([("taeter", "Gegenfall · Nur Entführer an Bord")], rechts_frei([
    *tafel("taeter", "Gegenfall: nur Entführer an Bord", size=46),
    ok(135, 220, "verantw", gr=22), z("Täter wird nicht zum Objekt", 175, 200, "verantw", size=36),
    ok(135, 290, beim("verantw", "Ihm"), gr=22), z("ihm wird sein Handeln zugerechnet", 175, 270, beim("verantw", "Ihm"), size=36),
    ok(135, 360, "vhm", gr=22), z("Abschuss insoweit verhältnismäßig", 175, 340, "vhm", size=36),
    z("BVerfGE 115, 118 Rn. 140–154", 175, 400, beim("vhm", "verhältnismäßig"), size=28, farbe=TEXT),
    fl_block(110, 480, 1040, 150, ROT, "trotzdem", [("Trotzdem ganz nichtig", "ExtraBold", 40, INK),
                                                   ("wegen der Wehrverfassung (Rn. 155)", "Regular", 32, INK)]),
    ficon("tabler", "plane", 1560, 380, 230, "taeter", fuell=WEISS),
    pille("nur Entführer", 1560, 395, "taeter", fill=ROT, size=28, anker="m"),
    ficon("tabler", "scale", 1560, 740, 220, "vhm", fuell=GELB),
    peep_voll("LO_denkt", 1760, BR, 340, "taeter", bis="trotzdem"),
    peep_voll("LO_sorge", 1760, BR, 340, "trotzdem", anim="cut"),
]))

# M Rechtslage heute, Strafrecht -------------------------------------------------------------------------------------------------------
folie([("heute", "Rechtslage heute · LuftSiG (Stand 2026)"), ("drohne", "Rechtslage heute · § 15a LuftSiG"),
       ("straf", "Strafrecht · offen gelassen")], rechts_frei([
    *tafel("heute", "Heute und Strafrecht"),
    nein(135, 210, "heute", gr=22),
    z("keine Befugnis: Waffengewalt gegen", 175, 190, "heute", "Bold", 34),
    z("ein Flugzeug mit Menschen an Bord", 175, 240, beim("heute", "Flugzeug"), size=34),
    ok(135, 380, "drohne", gr=22),
    z("§ 15a II (seit 17.3.2026): Waffengewalt gegen Drohnen", 175, 360, "drohne", "Bold", 32),
    z("zur Verhinderung eines besonders schweren Unglücksfalls", 175, 410, beim("drohne", "besonders"), size=30),
    z("Strafbarkeit eines Abschusses: offengelassen (Rn. 130)", 110, 520, "straf", "Bold", 32),
    pille("übergesetzlicher Notstand? – umstritten", 110, 590, "streit", fill=GELB, size=32),
    ficon("tabler", "plane", 1560, 330, 200, beim("heute", "Flugzeug"), fuell=WEISS, bis="drohne"),
    pille("Menschen an Bord", 1560, 345, beim("heute", "Menschen"), fill=WEISS, size=28, anker="m", bis="drohne"),
    ficon("tabler", "drone", 1560, 330, 200, beim("drohne", "Drohnen"), fuell=GRAU, bis="straf"),
    pille("unbemannt", 1560, 345, beim("drohne", "Drohnen"), fill=GRAU, size=28, anker="m", bis="straf"),
    ficon("tabler", "scale", 1560, 330, 200, "straf", fuell=GELB),
    peep_voll("LO_ruhig", 1560, BR, FR, "heute", bis="straf"),
    peep_voll("LO_sorge", 1560, BR, FR, "straf", anim="cut"),
]))

# N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
LXX = 1560
folie([("tipp", "Klausurtipp · Würde vor Abwägung")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Unbeteiligte: keine Abwägung", 200, 200, beim("tipp", "Unbeteiligten"), "Bold", 36),
    z("die Verletzung der Würde entscheidet", 200, 280, "tipp1", size=36),
    z("Verhältnismäßigkeit nur für die Täter", 200, 360, "tipp2", size=36),
    *redet("LX_warnt", LXX, BR, FR + 40, "tipp", "sch"),
    pille("Lexi", LXX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# O Klausurschema ---------------------------------------------------------------------------------------------------------
K1, K2 = 150, 210
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Verfassungsbeschwerde gegen § 14 III LuftSiG", 110, 90, "sch", 50),
    z("A. Zulässigkeit: Verfassungsbeschwerde, Art. 94 I Nr. 4a GG", K1, 190, "k1", "Bold", 40, rechts=1820),
    z("Beschwerdebefugnis: selbst, gegenwärtig, unmittelbar betroffen", K2, 252, "k1b", size=34, farbe=TEXT, rechts=1820),
    z("B. Begründetheit: Recht auf Leben, Art. 2 II 1 GG", K1, 340, "k2", "Bold", 40, rechts=1820),
    z("I. Schutzbereich: Leben", K2, 402, beim("k2", "Schutzbereich"), size=38, rechts=1820),
    z("II. Eingriff durch den Abschuss", K2, 464, "k3", size=38, rechts=1820),
    z("III. Rechtfertigung: Gesetzesvorbehalt, Art. 2 II 3 GG", K2, 526, "k4", size=38, rechts=1820),
    z("1. formell: Wehrverfassung, Art. 87a II, 35 II 2, III GG", K2 + 60, 588, "k5", size=36, rechts=1820),
    z("2. materiell: Menschenwürde, Art. 1 I GG", K2 + 60, 645, "k6", size=36, rechts=1820),
    *plusminus("Unbeteiligte an Bord: Würde verletzt", K2 + 110, 710, beim("k7", "Unbeteiligten"), False, size=34),
    *plusminus("nur Täter an Bord: verhältnismäßig", K2 + 110, 765, beim("k7", "reinen"), True, size=34),
])

# P Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Der Staat darf Unbeteiligte", 0)], [("nicht ", 0), ("töten", "a"), (", um andere zu retten.", 0)]],
                750, 320, 52, "merke", {"a": beim("merke", "töten")}),
    *markertext([[("Ihre ", 0), ("Würde", "b"), (" lässt sich nicht gegen", 0)], [("die Zahl der Geretteten", 0)],
                 [("aufrechnen.", "c")]], 750, 560, 50, "m2", {"b": beim("m2", "Würde"), "c": beim("m2", "aufrechnen")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
