"""Gutgläubiger Zweiterwerb der forderungsentkleideten Hypothek – Open-Peeps-Stil, schlanke Posen, Pinselblasen (E)."""
import bausteine
from bausteine import *

bausteine.FIGORDNER = "op_hy/"
FOLIEN = bausteine.FOLIEN
BODEN = 870
FH = 470                      # Figurenhöhe in den Fallszenen
TITEL = "Die Hypothek ohne Darlehen"


def brief(cx, unten, cue, breite=120, **k):
    """Hypothekenbrief: Phosphor certificate (MIT), mit Palettenfarbe gefüllt."""
    return ficon("ph", "certificate", cx, unten, breite, cue, fuell=GELB, **k)


# 1 Fall I: Emma und Bruno ---------------------------------------------------------------------------------------
EX, HX, BX = 360, 760, 1520
folie([("fall", "Fall")], [
    titel(TITEL, 80, 55, "fall", 70),
    linienzug([(60, BODEN), (1860, BODEN)], "fall", breite=7, farbe=INK),
    *figuren([("EM_ruhig", "fall"), ("EM_froh", "bruno"), ("EM_besorgt", "nie")], EX, BODEN, FH),
    pille("Emma", EX, BODEN + 18, "fall", fill=TUERKIS, size=30, anker="m", d=0.2),
    ficon("ph", "house-line", HX, BODEN - 4, 250, "fall", fuell=GELB, d=0.4),
    pille("Grundstück", HX, BODEN + 18, "fall", fill=WEISS, size=30, anker="m", d=0.5),
    *figuren([("BR_ruhig", "bruno"), ("BR_verschlagen", "nie")], BX, BODEN, FH),
    pille("Bruno", BX, BODEN + 18, "bruno", fill=BLAU, size=30, anker="m", d=0.2),
    blase("sprech", 440, 180, "bruno", 1230, 250, inhalt=["100.000 € Darlehen", "für dich!"], textsize=36,
          figur=("BR_ruhig", BX, BODEN, FH), d=0.4, bis="hyp"),
    # Briefhypothek: erst bei Emma, dann zu Bruno
    brief(1080, 700, "hyp", d=0.2, bis="brief"),
    pille("Briefhypothek", 1080, 720, "hyp", fill=GELB, size=30, anker="m", d=0.4, bis="brief"),
    bewegt(brief(1330, 700, "brief"), "brief", ("brief", 0.8), -250),
    pille("Grundbuch: Hypothek für Bruno", 1060, 300, "brief", fill=WEISS, size=32, anker="m", d=0.6),
    # Darlehen kommt nie
    icon("fluent-emoji-high-contrast", "money-bag", 1060, 440, 110, "nie", farbe="#151515"),
    nein(1140, 400, "nie", gr=30),
    pille("Darlehen nie ausgezahlt", 1060, 520, "nie", fill=ROT, size=32, anker="m", d=0.3),
    blase("denk", 400, 190, "nie", 300, 250, inhalt=["Wo bleibt", "das Geld?"], textsize=36, figur=("EM_besorgt", EX, BODEN, FH), d=0.6),
])

# 2 Fall II: Bruno → Clara → David -----------------------------------------------------------------------------------
B2, C2, D2 = 300, 960, 1620
folie([("clara", "Fall")], [
    titel(TITEL, 80, 55, "clara", 70),
    linienzug([(60, BODEN), (1860, BODEN)], "clara", breite=7, farbe=INK),
    peep_voll("BR_verschlagen_r", B2, BODEN, FH, "clara"),
    pille("Bruno", B2, BODEN + 18, "clara", fill=BLAU, size=30, anker="m", d=0.2),
    *figuren([("CL_ruhig_l", "clara"), ("CL_froh", "ahnungslos")], C2, BODEN, FH, d=0.3),
    pille("Clara", C2, BODEN + 18, "clara", fill=LILA, size=30, anker="m", d=0.5),
    pfeil_ink(460, 560, 800, 560, "clara", d=0.7),
    brief(630, 530, "clara", breite=100, d=1.0),
    pille("Abtretung + Brief", 630, 580, "clara", fill=WEISS, size=28, anker="m", d=1.2),
    blase("denk", 420, 190, "ahnungslos", 850, 240, inhalt=["Eine sichere", "Hypothek!"], textsize=36,
          figur=("CL_froh", C2, BODEN, FH)),
    *figuren([("DV_ruhig", "david"), ("DV_wissend", "weiss")], D2, BODEN, FH),
    pille("David", D2, BODEN + 18, "david", fill=ORANGE, size=30, anker="m", d=0.2),
    pfeil_ink(1120, 560, 1460, 560, "david", d=0.4),
    brief(1290, 530, "david", breite=100, d=0.7),
    pille("Abtretung + Brief", 1290, 580, "david", fill=WEISS, size=28, anker="m", d=0.9),
    blase("denk", 440, 190, "weiss", 1570, 240, inhalt=["Bruno hat nie", "ausgezahlt …"], textsize=36,
          figur=("DV_wissend", D2, BODEN, FH)),
    pille("Hat David die Hypothek erworben?", 960, 960, "frage", fill=PINK, size=38, anker="m"),
])

# 3 Sachverhalt zum Nachlesen --------------------------------------------------------------------------------------------
sachverhalt("sv", [
    "Emma besitzt ein Grundstück. Bruno verspricht ihr ein Darlehen über 100.000 €. Zur Sicherheit bestellt Emma ihm "
    "eine Briefhypothek; Bruno wird im Grundbuch eingetragen und erhält den Brief.",
    "Bruno zahlt das Darlehen nie aus. Trotzdem tritt er die angebliche Forderung samt Hypothek schriftlich an Clara ab "
    "und übergibt ihr den Brief. Clara ahnt nichts.",
    "Später tritt Clara Forderung und Hypothek ebenso an David ab. David weiß, dass Bruno das Darlehen nie ausgezahlt hat.",
], "Hat David die Hypothek erworben?")

# 4 I. Ausgangslage ----------------------------------------------------------------------------------------------------------
X0, X1, X2 = 170, 230, 290
folie([("schema", "I. Ausgangslage")], [
    karte(100, 70, 1300, 860, "schema"),
    titel("I. Wem steht die Hypothek zu?", X0, 120, "schema", 58),
    zeile("Hypothek ist akzessorisch, § 1113 BGB", X1, 250, "akz", "Bold", 42),
    zeile("setzt eine gesicherte Forderung voraus", X1, 310, "akz", size=38, farbe=TEXT, d=0.5),
    nein(X1 + 20, 430, "keine", gr=26), zeile("Darlehen nie ausgezahlt:", X1 + 60, 408, "keine", "Bold", 40),
    zeile("kein Rückzahlungsanspruch, § 488 I 2", X1 + 60, 465, "keine", size=38, farbe=TEXT, d=0.5),
    fl_block(X1, 580, 1000, 160, GRUEN, "egs", [("Eigentümergrundschuld der Emma", "ExtraBold", 44, INK),
                                                 ("§§ 1163 I 1, 1177 I BGB", "Regular", 38, INK)]),
    peep_voll("EM_besorgt", 1650, BODEN, 560, "schema", d=0.3),
])

# 5 II. Ersterwerb durch Clara ------------------------------------------------------------------------------------------------
folie([("s_clara", "II. Ersterwerb durch Clara")], [
    karte(100, 60, 1300, 900, "s_clara"),
    titel("II. Ersterwerb durch Clara", X0, 105, "s_clara", 58),
    ok(X1 + 20, 235, "abtr", gr=26), zeile("Abtretung schriftlich + Briefübergabe", X1 + 60, 213, "abtr", "Bold", 40),
    zeile("§§ 1153, 1154 I BGB", X1 + 60, 268, "abtr", size=36, farbe=TEXT, d=0.5),
    nein(X1 + 20, 352, "nb", gr=24), zeile("Bruno: Nichtberechtigter", X1 + 60, 330, "nb", "Bold", 40),
    zeile("Forderung nicht gutgläubig erwerbbar", X1 + 60, 385, "nb", size=36, farbe=TEXT, d=0.8),
    pille("§ 1138: §§ 891 ff. gelten auch für die Forderung", X1, 460, "1138", fill=BLAU, size=36),
    ok(X1 + 20, 580, "gg", gr=26), zeile("Bruno eingetragen, Clara gutgläubig, § 892", X1 + 60, 558, "gg", "Bold", 40),
    pille("forderungsentkleidete Hypothek", X1, 640, "entkl", fill=GELB, size=40),
    ok(X1 + 20, 780, "folge", gr=26), zeile("Vollstreckung ins Grundstück, § 1147", X1 + 60, 758, "folge", size=38),
    nein(X1 + 20, 850, "folge2", gr=24), zeile("keine Zahlung von Emma persönlich", X1 + 60, 828, "folge2", size=38),
    peep_voll("CL_froh", 1660, BODEN, 560, "s_clara", d=0.3),
])

# 6 III. Zweiterwerb durch David: Streit -------------------------------------------------------------------------------------
folie([("s_david", "III. Zweiterwerb durch David")], [
    titel("III. Zweiterwerb durch David", 960, 50, "s_david", 64, anker="m"),
    zeile("David bösgläubig, Forderung fehlt weiterhin", 960, 150, "boes", "Bold", 38, farbe=TEXT, anker="m"),
    karte(90, 220, 820, 700, "aa"),
    karte(1010, 220, 820, 700, "hm"),
    zeile("Mindermeinung", 140, 265, "aa", "ExtraBold", 50),
    zeile("§ 1138 schützt nur Gutgläubige", 140, 360, "aa", "Bold", 38),
    nein(165, 480, "aa2", gr=24), zeile("David erwirbt nichts", 210, 458, "aa2", "Bold", 38),
    zeile("herrschende Meinung", 1060, 265, "hm", "ExtraBold", 50),
    ok(1085, 382, "hm1", gr=26), zeile("Clara ist Berechtigte", 1130, 360, "hm1", "Bold", 38),
    zeile("Erwerb vom Berechtigten:", 1130, 415, "hm1", size=36, farbe=TEXT, d=1.2),
    zeile("guter Glaube unerheblich", 1130, 465, "hm1", size=36, farbe=TEXT, d=2.0),
    ok(1085, 572, "hm2", gr=26), zeile("Übertragung wie gewohnt", 1130, 550, "hm2", "Bold", 38),
    zeile("§§ 1153, 1154 I BGB", 1130, 605, "hm2", size=36, farbe=TEXT, d=0.6),
    pille("sonst wäre Claras Recht unverkäuflich", 1060, 720, "arg", fill=GELB, size=34),
    ok(1100, 840, "arg", gr=26, d=1.0), zeile("überzeugt", 1145, 818, "arg", "Bold", 38, d=1.0),
])

# 7 Ergebnis + Klausurtipp --------------------------------------------------------------------------------------------------
folie([("erg", "Ergebnis")], [
    titel("Ergebnis", 960, 55, "erg", 74, anker="m"),
    fl_block(360, 180, 1200, 150, GRUEN, "erg", [("David hat die Hypothek erworben", "ExtraBold", 44, INK),
                                                 ("ohne Forderung", "Regular", 38, INK)]),
    zeile("Emma muss die Vollstreckung dulden, § 1147", 960, 370, "emma", "Bold", 38, anker="m"),
    zeile("Ausgleich: Emma gegen Bruno, z. B. § 816 I 1", 960, 425, "ausgl", size=38, farbe=TEXT, anker="m"),
    warnung_i(250, 560, "tipp", gr=30),
    zeile("Klausurtipp: guter Glaube nur beim Ersterwerb", 300, 535, "tipp", "ExtraBold", 40, farbe=DROT),
    zeile("danach: Erwerb vom Berechtigten", 300, 615, "tipp2", size=38),
    pille("umstritten: Rückerwerb durch Bruno selbst", 300, 690, "tipp3", fill=PINK, size=34),
    peep_voll("ER_arme", 1690, BODEN, 440, "tipp"),
])

# 8 Klausurschema -----------------------------------------------------------------------------------------------------------
K0, K1, K2 = 250, 310, 380
folie([("sch", "Klausurschema")], [
    karte(180, 50, 1560, 920, "sch"),
    titel("Klausurschema: Zweiterwerb der Hypothek", K0, 95, "sch", 56),
    zeile("I. Entstehung: Forderung?", K1, 210, "k1", "Bold", 40),
    zeile("fehlt → Eigentümergrundschuld, §§ 1163 I 1, 1177 I", K2, 270, "k1", size=36, farbe=TEXT, d=0.8),
    zeile("II. Ersterwerb: §§ 1153, 1154 I", K1, 360, "k2", "Bold", 40),
    zeile("vom Nichtberechtigten: § 1138 i. V. m. § 892", K2, 420, "k2", size=36, farbe=TEXT, d=0.8),
    zeile("→ forderungsentkleidete Hypothek", K2, 475, "k2", size=36, farbe=TEXT, d=1.6),
    zeile("III. Zweiterwerb: §§ 1153, 1154 I", K1, 565, "k3", "Bold", 40),
    zeile("Erwerb vom Berechtigten? Streit darstellen", K2, 625, "k3", size=36, farbe=TEXT, d=0.8),
    pille("h. M.: auch der Bösgläubige erwirbt", K1, 720, "k3", fill=GRUEN, size=38, d=1.8),
])

# 9 Merksatz ----------------------------------------------------------------------------------------------------------------
folie([("merke", "Merksatz")], [
    karte(80, 120, 1340, 800, "merke", fill=(255, 251, 230, 255)),
    titel("Merke", 750, 180, "merke", 84, anker="m"),
    *markertext([[("Forderungsentkleidete Hypothek:", "a")], [("einmal gutgläubig erworben,", 0)], [("frei ", 0), ("übertragbar", "b"), (".", 0)]],
                750, 320, 50, "merke", {"a": ("merke", 0.6), "b": ("merke", 4.5)}),
    *markertext([[("Der Zweiterwerber erwirbt", 0)], [("vom ", 0), ("Berechtigten", "c"), (",", 0)], [("auch wenn er bösgläubig ist.", 0)]],
                750, 560, 50, "m2", {"c": ("m2", 0.8)}),
    peep_voll("ER_freut", 1680, 1000, 720, "merke", d=0.4),
])
