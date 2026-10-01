"""Folge 006 · Anspruchsaufbau Zivilrecht: Wer will was von wem woraus? (Methodik) – Serienstandard Open Peeps (Katzenkönig).
Szenen laut ../SZENENPLAN.md: A Wohnungstür, B Klausurfrage, C Sachverhalt, D Fallfrage zerlegen, E Reihenfolge, F Warum?,
G1/G2 I. § 546 Abs. 1 BGB (entstanden, nicht erloschen, durchsetzbar), H1 II./III. § 985, H2 Gegenfall Februar,
H3 IV./V. und Ergebnis, I typische Fehler, J Klausurtipp (Lexi), K Klausurschema, L Merksatz (Lexi).
Geräusche nur bei sichtbarer Handlung (Türklingel, Tür fällt zu)."""
import sys
sys.path.insert(0, "../../etb2/src")
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_006/"
FOLIEN = bausteine.FOLIEN
BG_FARBE = bausteine.BG_FARBE
PFAD_FARBE = bausteine.PFAD_FARBE
HELL = (255, 251, 230, 255)
DAUER = bausteine._cj()["dauer"]
A = "A. Albers gegen Jana"


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


def nein_bis(x, y, cue, gr, bis):
    """Bleistift-Kreuz, das mit seinem Requisit wieder verschwindet."""
    e = nein(x, y, cue, gr=gr)
    e.bis = bis
    return e


def lexi_bis_ende(cue):
    return (cue, round(DAUER - bausteine._t(cue) - 0.05, 3))


BODEN, FH = 880, 480
BR, FR = 930, 480                       # Figuren rechts neben der Tafel
AX, JX = 1420, 1720                     # Albers, Jana neben der Tafel
NX = 1560                               # Noah bzw. Lexi allein neben der Tafel

# A Fall: an der Wohnungstür -----------------------------------------------------------------------------------------------
JA0, TUER, AL0 = 300, 610, 1530          # Jana, Wohnungstür, Albers
ALF = ("AL_fordert", AL0, BODEN, FH)
JAT = ("JA_trotzig_r", JA0, BODEN, FH)
folie([("haus", "Fall · An der Wohnungstür")], [
    pille("Der Mietwohnungs-Fall", 70, 40, "haus", fill=GELB, size=48),
    linienzug([(60, BODEN), (1860, BODEN)], "haus", breite=7, farbe=INK),
    # die Wohnungstür: offen (weiß), nach [tuer] zu und verriegelt (blau + Schloss)
    ficon("tabler", "door", TUER, BODEN - 2, 360, "haus", fuell=WEISS, bis="tuer"),
    szene(ficon("tabler", "door", TUER, BODEN - 2, 360, "tuer", fuell=BLAU, anim="cut"), "006tuer*", 0.9, versatz=-0.22),
    ficon("tabler", "lock", TUER + 60, 700, 70, beim("tuer", "Tür"), fuell=GELB),
    # Eigentum und Kündigung (oben, bis Albers spricht)
    ficon("tabler", "home", 880, 250, 130, beim("haus", "Wohnung"), fuell=GELB, bis="a1"),
    pille("gehört Albers", 880, 270, beim("haus", "Albers"), fill=WEISS, size=30, anker="m", bis="a1"),
    ficon("tabler", "file-text", 1300, 250, 110, "kuend", fuell=WEISS, bis="a1"),
    pille("Kündigung zum 31. März", 1300, 270, beim("kuend", "einunddreißigsten"), fill=ROT, size=30, anker="m", bis="a1"),
    # Jana
    peep_voll("JA_ruhig_r", JA0, BODEN, FH, "haus", bis="j1"),
    *redet("JA_trotzig_r", JA0, BODEN, FH, "j1", "tuer"),
    pille("Jana", JA0, BODEN + 22, "haus", fill=GRUEN, size=30, anker="m", d=0.2, bis="tuer"),
    pille("wohnt noch dort", JA0, 330, "noch", fill=GELB, size=30, anker="m", bis="j1"),
    # Albers kommt und klingelt
    szene(peep_voll("AL_ruhig", AL0, BODEN, FH, "april", bis="a1"), "006klingel*", 0.7, versatz=0.1),
    ficon("tabler", "bell", TUER + 215, 560, 56, "april", fuell=GELB, d=0.1),
    *redet("AL_fordert", AL0, BODEN, FH, "a1", "j1"),
    peep_voll("AL_denkt", AL0, BODEN, FH, "j1", anim="cut", bis="tuer"),
    peep_voll("AL_aerger", AL0, BODEN, FH, "tuer", anim="cut"),
    pille("Albers", AL0, BODEN + 22, "april", fill=BLAU, size=30, anker="m", d=0.2),
    ficon("tabler", "calendar", 1060, BODEN - 2, 130, "april", fuell=WEISS),
    pille("1. April", 1060, 690, beim("april", "April"), fill=WEISS, size=32, anker="m"),
    # Sprechblasen
    blase("sprech", 640, 210, "a1", 1180, 200, inhalt=["Der Mietvertrag ist vorbei.", "Ich will meine Wohnung zurück!"],
          textsize=32, figur=ALF, bis="j1"),
    blase("sprech", 700, 220, "j1", 720, 255, inhalt=["Erst will ich meine Kaution zurück.", "Vorher bekommen Sie", "die Schlüssel nicht."],
          textsize=30, figur=JAT, bis="tuer"),
    ficon("tabler", "coin-euro", 880, BODEN - 2, 100, beim("j1", "Kaution"), fuell=GELB, bis="tuer"),
    ficon("tabler", "key", 1250, BODEN - 2, 100, beim("j1", "Schlüssel"), fuell=GELB, bis="tuer"),
])

# B Klausurfrage ------------------------------------------------------------------------------------------------------------
MB, MF = 930, 520
folie([("klausur", "Fall · Die Klausurfrage"), ("vier", "Fallfrage · Wer will was von wem woraus?")], [
    *tafel("klausur", "Klausur · Zivilrecht"),
    ficon("tabler", "clock", 1100, 170, 80, "klausur", fuell=GELB, d=0.3),
    z("Fallfrage:", 110, 200, beim("klausur", "Kann"), "Bold", 38),
    z("Kann Albers von Jana die Rückgabe", 110, 260, beim("klausur", "Kann"), size=38),
    z("der Wohnung verlangen?", 110, 315, beim("klausur", "Wohnung"), size=38),
    ficon("tabler", "file-certificate", 240, 560, 120, beim("n1", "Mietvertrag"), fuell=BLAU),
    pille("Mietvertrag", 240, 580, beim("n1", "Mietvertrag"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "home", 540, 560, 120, beim("n1", "Eigentum"), fuell=GELB),
    pille("Eigentum", 540, 580, beim("n1", "Eigentum"), fill=WEISS, size=28, anker="m"),
    ficon("tabler", "coin-euro", 840, 560, 120, beim("n1", "Kaution"), fuell=GELB),
    pille("Kaution", 840, 580, beim("n1", "Kaution"), fill=WEISS, size=28, anker="m"),
    pille("Wer?", 110, 730, beim("vier", "Wer"), fill=GELB, size=36),
    pille("Was?", 330, 730, beim("vier", "was"), fill=BLAU, size=36),
    pille("Von wem?", 550, 730, beim("vier", "wem"), fill=LILA, size=36),
    pille("Woraus?", 850, 730, beim("vier", "woraus"), fill=GRUEN, size=36),
    peep_voll("NO_denkt", NX, MB, MF, "klausur", bis="n1"),
    *redet("NO_fragt", NX, MB, MF, "n1", "vier"),
    peep_voll("NO_froh", NX, MB, MF, "vier", anim="cut"),
    pille("Noah", NX, MB + 22, "klausur", fill=GELB, size=30, anker="m", d=0.2),
    blase("sprech", 560, 230, "n1", 1480, 210, inhalt=["Mietvertrag, Eigentum,", "Kaution … wo fange", "ich bloß an?"], textsize=31,
          figur=("NO_fragt", NX, MB, MF), bis="vier"),
])

# C Sachverhalt -------------------------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Jana wohnt zur Miete in einer Wohnung, die Herrn Albers gehört. Bei Einzug hat sie eine Kaution gezahlt. "
    "Am 2. Januar kündigt Jana schriftlich zum 31. März.",
    "Am 1. April klingelt Albers. Jana wohnt immer noch dort. Albers: „Der Mietvertrag ist vorbei. Ich will meine Wohnung "
    "zurück!“ Jana: „Erst will ich meine Kaution zurück. Vorher bekommen Sie die Schlüssel nicht.“ Albers hat die Kaution "
    "noch nicht abgerechnet.",
    "(Frei erfundener Übungsfall.)",
], "Kann Albers von Jana die Rückgabe der Wohnung verlangen?")

# D Fallfrage zerlegen ---------------------------------------------------------------------------------------------------------
FZ = "Fallfrage zerlegen"
folie([("wer", f"{FZ} › Wer?"), ("was", f"{FZ} › Was?"), ("vonwem", f"{FZ} › Von wem?"), ("woraus", f"{FZ} › Woraus?")], [
    *tafel("wer", "Wer will was von wem woraus?"),
    z("Wer?", 110, 200, "wer", "Bold", 38, farbe=TEXT),
    z("Albers, der Anspruchsteller", 380, 200, beim("wer", "Albers"), "Bold", 36),
    z("Was?", 110, 290, "was", "Bold", 38, farbe=TEXT),
    z("Rückgabe der Wohnung", 380, 290, beim("was", "Rückgabe"), "Bold", 36),
    nein(400, 368, beim("was", "Geld"), gr=20), z("kein Geld", 430, 350, beim("was", "Geld"), size=32, farbe=TEXT),
    nein(640, 368, beim("was", "Schadensersatz"), gr=20), z("kein Schadensersatz", 670, 350, beim("was", "Schadensersatz"), size=32, farbe=TEXT),
    z("Von wem?", 110, 450, "vonwem", "Bold", 38, farbe=TEXT),
    z("Jana, die Anspruchsgegnerin", 380, 450, beim("vonwem", "Jana"), "Bold", 36),
    z("Woraus?", 110, 540, "woraus", "Bold", 38, farbe=TEXT),
    z("Anspruchsgrundlage", 380, 540, beim("woraus", "Anspruchsgrundlage"), "Bold", 36),
    fl_block(110, 630, 1040, 130, GELB, beim("woraus", "Norm"), [("eine Norm, deren Rechtsfolge", "Bold", 34, INK),
                                                                 ("genau dieses Ziel gewährt", "Bold", 34, INK)]),
    peep_voll("AL_ruhig", AX, BR, FR, "wer", bis=beim("wer", "Albers")),
    peep_voll("AL_zufrieden", AX, BR, FR, beim("wer", "Albers"), anim="cut"),
    peep_voll("JA_ruhig", JX, BR, FR, "wer", d=0.2, bis=beim("vonwem", "Jana")),
    peep_voll("JA_ertappt", JX, BR, FR, beim("vonwem", "Jana"), anim="cut"),
    pille("Albers", AX, BR + 22, "wer", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Jana", JX, BR + 22, "wer", fill=GRUEN, size=30, anker="m", d=0.4),
    pille("Anspruchsteller", AX, 330, beim("wer", "Anspruchsteller"), fill=GELB, size=28, anker="m"),
    ficon("tabler", "key", (AX + JX) // 2, 300, 110, beim("was", "Rückgabe"), fuell=GELB),
    pille("Anspruchsgegnerin", JX, 370, beim("vonwem", "Anspruchsgegnerin"), fill=LILA, size=28, anker="m"),
    pille("§ ?", (AX + JX) // 2, 90, beim("woraus", "Anspruchsgrundlage"), fill=GRUEN, size=40, anker="m"),
])

# E Reihenfolge -------------------------------------------------------------------------------------------------------------------
RF = [("1. Vertrag", BLAU, "r1", "Erstens"), ("2. Vertragsähnlich: c.i.c., GoA", LILA, "r2", "Zweitens"),
      ("3. Dingliche Ansprüche", GRUEN, "r3", "Drittens"), ("4. Delikt", ORANGE, "r4", "viertens"),
      ("5. Bereicherung", GELB, "r5", "fünftens")]
folie([("reihe", "Reihenfolge der Anspruchsgrundlagen"), ("lehre", "Reihenfolge · Lehre, kein Gesetz")], [
    *tafel("reihe", "Prüfungsreihenfolge"),
    *[fl_block(110 + 40 * i, 185 + 100 * i, 1000 - 40 * i, 82, f, c, [(t, "Bold", 34, INK)]) for i, (t, f, c, _) in enumerate(RF)],
    pille("steht in keinem Gesetz: Lehre", 110, 715, beim("lehre", "keinem"), fill=PINK, size=32),
    z("Früheres kann Späteres ausschließen", 110, 815, beim("lehre", "Was"), "Bold", 36),
    peep_voll("NO_denkt", NX, MB, MF, "reihe", bis="lehre"),
    peep_voll("NO_froh", NX, MB, MF, "lehre", anim="cut"),
    pille("Noah", NX, MB + 22, "reihe", fill=GELB, size=30, anker="m", d=0.2),
])

# F Warum diese Reihenfolge? -------------------------------------------------------------------------------------------------------
LY = {1: 235, 2: 350, 3: 465, 4: 580, 5: 695}          # Leiter rechts: y-Mitte je Stufe
LT = {1: ("Vertrag", BLAU), 2: ("vertragsähnlich", LILA), 3: ("dinglich", GRUEN), 4: ("Delikt", ORANGE), 5: ("Bereicherung", GELB)}
LXM = 1520


def leiter_ring(stufe, cue, bis):
    t = LT[stufe][0]
    w = F("Bold", 32).getlength(t) + 60
    return ring(LXM, LY[stufe] + 4, int(w / 2 + 22), 46, cue, farbe=DROT, breite=6, bis=bis)


folie([("w1", "Reihenfolge · Warum? Vertrag vor dinglich"), ("w2", "Reihenfolge · Warum? Vertrag vor Bereicherung"),
       ("w3", "Reihenfolge · Warum? Vertrag vor GoA"), ("w4", "Reihenfolge · Warum? dinglich vor Delikt"),
       ("w5", "Reihenfolge · Warum? Bereicherung zuletzt")], [
    *tafel("w1", "Warum diese Reihenfolge?"),
    z("Vertrag → Recht zum Besitz:", 110, 195, "w1", "Bold", 34),
    z("§ 985 scheitert an § 986 I", 150, 243, beim("w1", "Dann"), size=32, farbe=TEXT),
    z("Vertrag → rechtlicher Grund:", 110, 315, "w2", "Bold", 34),
    z("§ 812 I scheitert", 150, 363, beim("w2", "Dann"), size=32, farbe=TEXT),
    z("GoA, § 677: nur ohne Auftrag", 110, 435, "w3", "Bold", 34),
    z("→ erst den Vertrag klären", 150, 483, beim("w3", "also"), size=32, farbe=TEXT),
    z("§ 993 I: redlicher Besitzer schuldet", 110, 555, "w4", "Bold", 34),
    z("im Übrigen keinen Schadensersatz", 150, 603, beim("w4", "keinen"), size=32, farbe=TEXT),
    pille("dinglich vor Delikt", 730, 595, "w4b", fill=GRUEN, size=28),
    z("Bereicherung zuletzt: „ohne rechtlichen", 110, 675, "w5", "Bold", 34),
    z("Grund“ hängt von allem davor ab", 150, 723, beim("w5", "hängt"), size=32, farbe=TEXT),
    # Leiter rechts mit den fünf Stufen; Ringe zeigen, welche Stufe welche verdrängt
    *[pille(LT[s][0], LXM, LY[s] - 28, "w1", fill=LT[s][1], size=32, anker="m", d=0.05 * s) for s in LT],
    leiter_ring(1, "w1", "w2"), leiter_ring(3, beim("w1", "Dann"), "w2"),
    pille("§ 986", 1790, (LY[1] + LY[3]) // 2 - 26, beim("w1", "Dann"), fill=WEISS, size=30, anker="m", bis="w2"),
    leiter_ring(1, "w2", "w3"), leiter_ring(5, beim("w2", "Dann"), "w3"),
    pille("§ 812", 1790, (LY[1] + LY[5]) // 2 - 26, beim("w2", "Dann"), fill=WEISS, size=30, anker="m", bis="w3"),
    leiter_ring(1, "w3", "w4"), leiter_ring(2, "w3", "w4"),
    pille("§ 677", 1790, (LY[1] + LY[2]) // 2 - 26, "w3", fill=WEISS, size=30, anker="m", bis="w4"),
    leiter_ring(3, "w4", "w5"), leiter_ring(4, beim("w4", "keinen"), "w5"),
    pille("§ 993", 1790, (LY[3] + LY[4]) // 2 - 26, beim("w4", "keinen"), fill=WEISS, size=30, anker="m", bis="w5"),
    leiter_ring(5, "w5", None),
    pille("zuletzt", 1790, LY[5] - 26, "w5", fill=WEISS, size=30, anker="m"),
    z("früher kann später ausschließen", 1290, 800, "w1", size=30, farbe=TEXT, rechts=1850, d=0.3),
])

# G1 I. § 546 Abs. 1: entstanden, nicht erloschen ------------------------------------------------------------------------------------
folie([("i", f"{A} › I. § 546 I BGB"), ("entst", f"{A} › I. 1. entstanden"), ("erl", f"{A} › I. 2. nicht erloschen")], [
    *tafel("i", "I. § 546 Abs. 1 BGB"),
    z("„Der Mieter ist verpflichtet, die Mietsache nach", 110, 195, "i", size=33, farbe=TEXT),
    z("Beendigung des Mietverhältnisses zurückzugeben.“", 110, 243, "i", size=33, farbe=TEXT),
    pille("1. entstanden", 110, 310, beim("drei", "entstanden"), fill=GELB, size=30),
    pille("2. nicht erloschen", 400, 310, beim("drei", "nicht"), fill=BLAU, size=30),
    pille("3. durchsetzbar", 760, 310, beim("drei", "durchsetzbar"), fill=GRUEN, size=30),
    ok(135, 445, beim("entst", "Mietvertrag"), gr=22), z("1. entstanden: Mietvertrag", 175, 425, "entst", "Bold", 36),
    ok(215, 515, "entst2", gr=20), z("Kündigung zum 31. März: beendet", 250, 497, "entst2", size=34),
    z("(schriftlich, fristgerecht: §§ 568 I, 573c I BGB)", 250, 547, beim("entst2", "fristgerechte"), size=28, farbe=TEXT),
    z("2. nicht erloschen: Erfüllung = Rückgabe", 175, 630, "erl", "Bold", 36),
    z("(§ 362 I BGB)", 215, 680, beim("erl", "Erfüllt"), size=28, farbe=TEXT),
    ok(135, 650, "erl2", gr=22), z("Schlüssel noch bei Jana", 250, 730, "erl2", size=34),
    peep_voll("AL_ruhig", AX, BR, FR, "i"),
    peep_voll("JA_ruhig", JX, BR, FR, "i", d=0.2, bis="erl2"),
    peep_voll("JA_trotzig", JX, BR, FR, "erl2", anim="cut"),
    pille("Albers", AX, BR + 22, "i", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Jana", JX, BR + 22, "i", fill=GRUEN, size=30, anker="m", d=0.4),
    ficon("tabler", "file-certificate", (AX + JX) // 2, 230, 110, beim("entst", "Mietvertrag"), fuell=BLAU, bis="entst2"),
    ficon("tabler", "calendar", (AX + JX) // 2, 230, 110, "entst2", fuell=WEISS, bis="erl"),
    ficon("tabler", "file-certificate", (AX + JX) // 2 - 110, 230, 90, "entst2", fuell=BLAU, bis="erl"),
    nein_bis((AX + JX) // 2 - 110, 190, beim("entst2", "beendet"), 26, "erl"),
    pille("31. März", (AX + JX) // 2, 250, beim("entst2", "einunddreißigsten"), fill=WEISS, size=28, anker="m", bis="erl"),
    ficon("tabler", "key", JX, 360, 100, "erl2", fuell=GELB),
])

# G2 I. 3. durchsetzbar --------------------------------------------------------------------------------------------------------------
folie([("durch", f"{A} › I. 3. durchsetzbar?"), ("p570", f"{A} › I. 3. durchsetzbar: § 570 BGB"),
       ("faellig", f"{A} › I. 3. Kaution erst nach Prüfungsfrist")], [
    *tafel("durch", "I. 3. durchsetzbar?"),
    z("Jana: erst die Kaution zurück", 110, 200, beim("durch", "Jana"), "Bold", 36),
    z("Zurückbehaltungsrecht?", 175, 265, beim("durch", "Kaution"), size=36),
    nein(135, 285, beim("p570", "kein"), gr=22),
    fl_block(110, 350, 1040, 150, GELB, "p570", [("§ 570 BGB: kein Zurückbehaltungsrecht", "Bold", 34, INK),
                                                ("des Mieters gegen den Rückgabeanspruch", "Regular", 32, INK)]),
    *plusminus("3. durchsetzbar", 110, 545, beim("p570", "Zurückbehaltungsrecht"), True, size=36, stil="Bold"),
    z("Kaution zurück erst nach", 110, 640, "faellig", "Bold", 34),
    z("angemessener Prüfungsfrist", 110, 690, beim("faellig", "angemessenen"), "Bold", 34),
    pille("BGH, Urt. v. 10.7.2024 – VIII ZR 184/23, Rn. 18", 110, 770, beim("faellig", "Prüfungsfrist"), fill=GRUEN, size=28),
    peep_voll("AL_ruhig", AX, BR, FR, "durch", bis="p570"),
    peep_voll("AL_zufrieden", AX, BR, FR, "p570", anim="cut"),
    peep_voll("JA_trotzig", JX, BR, FR, "durch", bis="p570"),
    peep_voll("JA_ertappt", JX, BR, FR, "p570", anim="cut"),
    pille("Albers", AX, BR + 22, "durch", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Jana", JX, BR + 22, "durch", fill=GRUEN, size=30, anker="m", d=0.4),
    ficon("tabler", "key", JX - 70, 360, 90, "durch", fuell=GELB),
    ficon("tabler", "coin-euro", JX + 70, 360, 90, beim("durch", "Kaution"), fuell=GELB),
    pille("erst Kaution?", JX, 380, beim("durch", "Kaution"), fill=WEISS, size=28, anker="m", bis="p570"),
    pille("kein Zurückbehaltungsrecht", (AX + JX) // 2, 380, beim("p570", "kein"), fill=ROT, size=28, anker="m"),
    ficon("tabler", "calendar-clock", AX, 250, 100, "faellig", fuell=WEISS),
    pille("Prüfungsfrist", AX, 120, beim("faellig", "Prüfungsfrist"), fill=WEISS, size=28, anker="m"),
])

# H1 II. vertragsähnlich, III. § 985 ---------------------------------------------------------------------------------------------------
folie([("ii", f"{A} › II. Vertragsähnliche Ansprüche"), ("iii", f"{A} › III. § 985 BGB"),
       ("rzb", f"{A} › III. § 985 › Recht zum Besitz, § 986 I")], [
    *tafel("ii", "II. und III."),
    z("II. vertragsähnlich: nicht ersichtlich", 110, 195, "ii", "Bold", 36),
    z("III. § 985 BGB", 110, 300, "iii", "Bold", 38),
    ok(175, 385, beim("iii", "Eigentümer"), gr=22), z("Eigentümer: Albers", 215, 365, beim("iii", "Eigentümer"), size=36),
    ok(175, 455, beim("iii", "Besitzerin"), gr=22), z("Besitzerin: Jana", 215, 435, beim("iii", "Besitzerin"), size=36),
    z("Recht zum Besitz, § 986 I?", 215, 505, "rzb", size=36),
    z("nur aus dem Mietvertrag – beendet", 255, 560, beim("rzb", "und"), size=32, farbe=TEXT),
    ok(175, 545, beim("rzb", "beendet"), gr=22),
    *plusminus("§ 985 BGB", 110, 660, beim("rzb", "Auch"), True, size=38, stil="Bold"),
    peep_voll("AL_ruhig", AX, BR, FR, "ii", bis=beim("iii", "Eigentümer")),
    peep_voll("AL_zufrieden", AX, BR, FR, beim("iii", "Eigentümer"), anim="cut"),
    peep_voll("JA_ruhig", JX, BR, FR, "ii", d=0.2, bis=beim("rzb", "beendet")),
    peep_voll("JA_ertappt", JX, BR, FR, beim("rzb", "beendet"), anim="cut"),
    pille("Albers", AX, BR + 22, "ii", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Jana", JX, BR + 22, "ii", fill=GRUEN, size=30, anker="m", d=0.4),
    ficon("tabler", "home", AX, 360, 100, beim("iii", "Eigentümer"), fuell=GELB),
    pille("Eigentum", AX, 380, beim("iii", "Eigentümer"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "key", JX, 360, 100, beim("iii", "Besitzerin"), fuell=GELB),
    pille("Besitz", JX, 380, beim("iii", "Besitzerin"), fill=WEISS, size=26, anker="m"),
    ficon("tabler", "file-certificate", (AX + JX) // 2, 200, 90, "rzb", fuell=BLAU),
    nein((AX + JX) // 2, 160, beim("rzb", "beendet"), gr=26),
])

# H2 Gegenfall: Februar --------------------------------------------------------------------------------------------------------------
folie([("feb", "Gegenfall · Februar: Vertrag läuft"), ("sperre", "Gegenfall · Der Vertrag entscheidet")], [
    *tafel("feb", "Gegenfall: Februar"),
    ok(135, 225, beim("feb", "Da"), gr=22), z("Mietvertrag läuft noch", 175, 200, beim("feb", "Da"), "Bold", 36),
    ok(135, 305, "feb2", gr=22), z("Jana: Recht zum Besitz, § 986 I", 175, 280, beim("feb2", "Jana"), "Bold", 36),
    nein(135, 385, beim("feb2", "verweigern"), gr=22), z("§ 985: Herausgabe verweigert", 175, 360, beim("feb2", "verweigern"), size=36),
    fl_block(110, 480, 1040, 150, GRUEN, "sperre", [("Der Vertrag entscheidet", "ExtraBold", 40, INK),
                                                   ("über den dinglichen Anspruch", "Bold", 34, INK)]),
    pille("darum: Vertrag zuerst", 110, 690, beim("sperre", "dinglichen"), fill=BLAU, size=32),
    peep_voll("AL_ruhig", AX, BR, FR, "feb", bis="feb2"),
    peep_voll("AL_denkt", AX, BR, FR, "feb2", anim="cut"),
    peep_voll("JA_ruhig", JX, BR, FR, "feb", d=0.2, bis="feb2"),
    peep_voll("JA_zufrieden", JX, BR, FR, "feb2", anim="cut"),
    pille("Albers", AX, BR + 22, "feb", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Jana", JX, BR + 22, "feb", fill=GRUEN, size=30, anker="m", d=0.4),
    ficon("tabler", "calendar", (AX + JX) // 2, 230, 110, "feb", fuell=WEISS),
    pille("Februar", (AX + JX) // 2, 250, beim("feb", "Februar"), fill=LILA, size=30, anker="m"),
    ficon("tabler", "shield-check", JX, 380, 100, "feb2", fuell=GRUEN),
])

# H3 IV./V. und Ergebnis --------------------------------------------------------------------------------------------------------------
folie([("ivv", f"{A} › IV./V. Delikt, Bereicherung"), ("erg", f"{A} › Ergebnis")], [
    *tafel("ivv", "IV./V. und Ergebnis"),
    z("IV./V. Delikt, Bereicherung: kurz", 110, 195, "ivv", "Bold", 36),
    z("§ 823 I BGB führt zu Schadensersatz", 150, 260, beim("ivv", "Deliktsrecht"), size=34, farbe=TEXT),
    z("Albers will aber seine Wohnung", 150, 315, beim("ivv", "Albers"), size=34, farbe=TEXT),
    fl_block(110, 420, 1040, 160, GRUEN, "erg", [("Albers kann die Rückgabe verlangen", "ExtraBold", 40, INK),
                                                ("aus § 546 Abs. 1 und § 985 BGB", "Bold", 34, INK)]),
    pille("beide Ansprüche nebeneinander", 110, 640, "konk", fill=GELB, size=34),
    peep_voll("AL_ruhig", AX, BR, FR, "ivv", bis="erg"),
    peep_voll("AL_zufrieden", AX, BR, FR, "erg", anim="cut"),
    peep_voll("JA_denkt", JX, BR, FR, "ivv", d=0.2, bis="erg"),
    peep_voll("JA_ertappt", JX, BR, FR, "erg", anim="cut"),
    pille("Albers", AX, BR + 22, "ivv", fill=BLAU, size=30, anker="m", d=0.2),
    pille("Jana", JX, BR + 22, "ivv", fill=GRUEN, size=30, anker="m", d=0.4),
    ficon("tabler", "coin-euro", (AX + JX) // 2, 260, 100, beim("ivv", "Schadensersatz"), fuell=GELB, bis="erg"),
    nein_bis((AX + JX) // 2, 210, beim("ivv", "Wohnung"), 28, "erg"),
    ficon("tabler", "key", AX, 380, 100, "erg", fuell=GELB),
    pille("§ 546 I", (AX + JX) // 2 - 80, 120, "konk", fill=BLAU, size=28, anker="m"),
    pille("§ 985", (AX + JX) // 2 + 90, 120, "konk", fill=GRUEN, size=28, anker="m"),
])

# I Typische Fehler (Noah) ------------------------------------------------------------------------------------------------------------
NQ1, NQ2, NQ3 = "„Albers könnte einen Anspruch", "aus § 985 haben. Jana hat aber", "einen Anspruch auf die Kaution.“"
folie([("fehler", "Typische Fehler"), ("f2", "Typische Fehler · Kaution ist eigener Anspruch")], [
    *tafel("fehler", "Typische Fehler"),
    z(NQ1, 110, 195, "n2", "Bold", 36), z(NQ2, 130, 245, "n2", "Bold", 36),
    z(NQ3, 130, 295, beim("n2", "Jana"), "Bold", 36),
    wortring(NQ2, "§ 985", 130, 245, 36, "Bold", "f1", bis="f2"),
    nein(135, 415, "f1", gr=24), z("1. Start beim Eigentum", 175, 390, "f1", "Bold", 36),
    z("→ ob Jana besitzen darf, sagt erst der Vertrag", 215, 445, beim("f1", "Ob"), size=32, farbe=TEXT),
    wortring(NQ3, "Anspruch auf die Kaution", 130, 295, 36, "Bold", "f2"),
    nein(135, 545, "f2", gr=24), z("2. Kaution: eigener Anspruch Jana gegen Albers", 175, 520, "f2", "Bold", 34),
    z("→ hier nur Gegenrecht: bei „durchsetzbar“", 215, 580, "f3", size=32, farbe=TEXT),
    peep_voll("NO_denkt", NX, MB, MF, "fehler", bis="n2"),
    *redet("NO_redet", NX, MB, MF, "n2", "f1"),
    peep_voll("NO_ertappt", NX, MB, MF, "f1", anim="cut", bis="f3"),
    peep_voll("NO_denkt", NX, MB, MF, "f3", anim="cut"),
    pille("Noah", NX, MB + 22, "fehler", fill=GELB, size=30, anker="m", d=0.2),
    blase("sprech", 600, 250, "n2", 1500, 220, inhalt=["Albers könnte einen Anspruch", "aus § 985 haben. Jana hat aber",
                                                       "einen Anspruch auf die Kaution."], textsize=29,
          figur=("NO_redet", NX, MB, MF), bis="f1"),
])

# J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------------------
folie([("tipp", "Klausurtipp · Gegenrechte richtig einordnen")], [
    *tafel("tipp", "Klausurtipp", fill=HELL),
    warnung_i(150, 225, "tipp", gr=26),
    z("Jedes Gegenrecht an seinen Platz:", 200, 200, beim("tipp", "Jedes"), "Bold", 36),
    z("entstanden:", 150, 300, "t1", "Bold", 34), z("was ihn hindert, etwa Nichtigkeit", 420, 300, "t1", size=34),
    z("erloschen:", 150, 380, "t2", "Bold", 34), z("Erfüllung, Aufrechnung", 420, 380, "t2", size=34),
    z("(§§ 362, 389 BGB)", 420, 425, "t2", size=28, farbe=TEXT),
    z("durchsetzbar:", 150, 495, "t3", "Bold", 34), z("Einreden: Verjährung,", 420, 495, beim("t3", "Einreden"), size=34),
    z("Zurückbehaltungsrecht (§§ 214, 273 BGB)", 420, 540, beim("t3", "Einreden"), size=28, farbe=TEXT),
    pille("Verjährung beim Erlöschen? Punkte verschenkt", 110, 640, "t4", fill=ROT, size=32),
    *redet("LX_warnt", NX, BR, 520 + 40, "tipp", "sch"),
    pille("Lexi", NX, BR + 22, "tipp", fill=GELB, size=30, anker="m", d=0.2),
])

# K Klausurschema ----------------------------------------------------------------------------------------------------------------------
K1, K2, K3 = 150, 210, 270
folie([("sch", "Klausurschema")], [
    karte(60, 50, 1800, 900, "sch"),
    titel("Klausurschema: Mietwohnungs-Fall", 110, 90, "sch", 54),
    z("A. Albers gegen Jana: Rückgabe der Wohnung", K1, 195, "k1", "Bold", 40, rechts=1820),
    z("I. § 546 Abs. 1 BGB", K2, 260, "k2", "Bold", 36, rechts=1820),
    z("1. entstanden: Mietvertrag, beendet (Kündigung zum 31. März)", K3, 315, "k3", size=34, farbe=TEXT, rechts=1820),
    z("2. nicht erloschen: keine Rückgabe, § 362 I BGB", K3, 367, "k4", size=34, farbe=TEXT, rechts=1820),
    z("3. durchsetzbar: kein Zurückbehaltungsrecht, § 570 BGB", K3, 419, "k5", size=34, farbe=TEXT, rechts=1820),
    z("II. Vertragsähnliche Ansprüche: nicht ersichtlich", K2, 490, "k6", "Bold", 36, rechts=1820),
    z("III. § 985 BGB: Eigentum, Besitz, kein Recht zum Besitz (§ 986 I)", K2, 550, "k7", "Bold", 36, rechts=1820),
    z("IV. Delikt · V. Bereicherung: kurz", K2, 610, "k8", "Bold", 36, rechts=1820),
    z("VI. Ergebnis: Rückgabe aus § 546 I und § 985 BGB", K2, 670, "k9", "Bold", 36, rechts=1820),
])

# L Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=HELL),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Erst fragst du: ", 0), ("Wer will was", "a")], [("von wem?", "a")]],
                750, 310, 54, "merke", {"a": beim("merke", "wer")}),
    *markertext([[("Das Woraus in fester Reihenfolge:", 0)], [("Vertrag · vertragsähnlich · dinglich", "b")],
                 [("Delikt · Bereicherung", "b")]], 750, 540, 44, "m2", {"b": beim("m2", "Vertrag")}),
    *redet("LX_erklaert", 1680, 1000, 720, "merke", lexi_bis_ende("merke")),
])
