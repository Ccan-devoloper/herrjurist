"""Folge 081 im mehrfarbigen Open-Peeps-Stil (gleiche Tonspur/Wortmarken wie v2)."""
from ostil import *

FOLIEN = []
PP = SP + "peeps/op/"


def folie(bg, pfade, els):
    FOLIEN.append(dict(bg=bg, pfade=pfade, els=els))


def st(text, x, y, cue, plus, size=44, d=0.0, stil="Regular"):
    """Schemazeile mit farbigem (+)/(-) dahinter."""
    zeichen = "(+)" if plus else "(-)"
    return [OT(text, x, y, cue, stil, size, d=d),
            OT(zeichen, x + F(stil, size).getlength(text + " "), y, cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT), d=d)]


def st2(text, x, y, cue, st_cue, plus, size=44, stil="Regular", d=0.0):
    zeichen = "(+)" if plus else "(-)"
    return [OT(text, x, y, cue, stil, size, d=d),
            OT(zeichen, x + F(stil, size).getlength(text + " "), y, st_cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT))]


BODEN = 905
AX, BX, FH = 600, 1330, 600
lat, kopf = laterne(1640, BODEN, 640, "fall", d=0.6)

# 1 Fall ----------------------------------------------------------------------------------------------
folie("creme", [("fall", "Fall")], [
    titel("Nachts am Bahnhof", 90, 60, "fall", 80),
    mond(1800, 110, 50, "fall", d=0.3),
    schild("Gleis 3", 900, 150, "fall", d=0.45),
    boden(BODEN, "fall"),
    lat,
    lichtkegel(kopf[0], kopf[1], 230, BODEN, "licht"),
    *mimik([("A_ruhig", "a"), ("A_skeptisch", "b"), ("A_angst", "messer"), ("A_stoss", "faust"),
            ("A_schreck", "handy"), ("A_betroffen", "licht")], AX, BODEN, FH),
    pille("A", AX - 20, BODEN + 18, "a", fill=GELB, size=34, anker="m", d=0.2),
    *mimik([("B_ruft", "b"), ("B_getroffen", "nase"), ("B_gibt", "handy")], BX, BODEN, FH),
    pille("B", BX, BODEN + 18, "b", fill=BLAU, size=34, anker="m", d=0.2),
    blase("denk", 360, 290, "messer", 240, 350, inhalt="Messer!", bild_=PP + "B_killer.png", bildhoehe=170, textsize=40, ziel=(555, 360), bis="handy"),
    E("collision", 1300, 390, 130, "faust", bis="handy"),
    blase("sprech", 420, 250, "handy", 1700, 330, inhalt=["Ihr Handy!"], textsize=46),
    E("mobile-phone", 1228, 512, 72, "handy", d=0.1),
    ring(1364, 610, 50, 44, "tasche", bis="messer"),
    pille("Wie hat sich A strafbar gemacht?", 1100, 975, "frage", fill=PINK, size=38, anker="m"),
])

# 2 Schema I ------------------------------------------------------------------------------------------
folie("creme", [("schema", "A. § 223 I StGB › I. Tatbestand"), ("rw", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    karte(80, 60, 1250, 930, "schema"),
    peep("N_kaffee", 1610, 1080, 640, "schema", d=0.3),
    titel("Strafbarkeit des A", 150, 120, "schema", 72),
    OT("A. Strafbarkeit gem. § 223 I StGB", 150, 250, "a223", "ExtraBold", 50),
    OT("I. Tatbestand", 210, 350, "tb", "Bold", 48),
    *st("1. Objektiver Tatbestand", 270, 425, "tbok", True),
    *st("2. Subjektiver Tatbestand", 270, 495, "vors", True),
    OT("II. Rechtswidrigkeit", 210, 590, "rw", "Bold", 48),
    OT("1. Notwehr, § 32", 270, 665, "nw", size=44),
])

# 3 § 32 ------------------------------------------------------------------------------------------------
folie("creme", [("norm", "II. Rechtswidrigkeit › Notwehr, § 32 StGB")], [
    karte(80, 90, 1400, 860, "norm", fill=(255, 251, 230, 255)),
    peep("N_tipp", 1680, 1080, 640, "norm", d=0.3),
    titel("§ 32 StGB · Notwehr", 780, 150, "norm", 72, anker="m"),
    *markertext([[("Abs. 1: Wer eine Tat begeht, die durch Notwehr", 0)],
                 [("geboten ist, handelt nicht ", 0), ("rechtswidrig", "a"), (".", 0)]],
                780, 320, 48, "norm", {"a": "hl1"}, d=0.35),
    *markertext([[("Abs. 2: Notwehr ist die Verteidigung, die erforderlich ist,", 0)],
                 [("um einen ", 0), ("gegenwärtigen rechtswidrigen Angriff", "b")],
                 [("von sich oder einem anderen abzuwenden.", 0)]],
                780, 540, 48, "abs2", {"b": "hl2"}),
])

# 4 Notwehrlage ----------------------------------------------------------------------------------------
folie("creme", [("nwl", "II. Rechtswidrigkeit › Notwehrlage")], [
    titel("Notwehrlage?", 960, 50, "nwl", 76, anker="m"),
    OT("Angriff = drohende Verletzung rechtlich geschützter Interessen durch einen Menschen", 960, 140, "nwl",
       size=36, farbe=TEXT, anker="m", d=0.3),
    peep("B_handy", 1400, 830, 420, "wirkl", d=0.1),
    blase("sprech", 400, 230, "wirkl", 1690, 380, inhalt=["Ich bringe", "Ihr Handy!"], textsize=38),
    OT("Wirklichkeit", 1400, 845, "wirkl", "ExtraBold", 50, anker="m", d=0.2),
    kreuz(1280, 950, "wirkl", gr=30, d=0.35),
    OT("kein Angriff", 1325, 925, "wirkl", "Bold", 42, d=0.35),
    peep("A_bueste_angst", 520, 830, 420, "vorst", d=0.1),
    blase("denk", 380, 290, "vorst", 250, 330, inhalt="Messerangriff!", bild_=PP + "B_killer.png", bildhoehe=160, textsize=34, ziel=(430, 420)),
    OT("Vorstellung von A", 520, 845, "vorst", "ExtraBold", 50, anker="m", d=0.2),
    haken(450, 950, "vorst", gr=32, d=0.35),
    OT("Angriff", 495, 925, "vorst", "Bold", 42, d=0.35),
    pille("Putativnotwehr", 960, 560, "putativ", fill=ORANGE, size=42, anker="m"),
])

# 5 Schema II ------------------------------------------------------------------------------------------
folie("creme", [("zurueck", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    karte(80, 60, 1250, 930, "zurueck"),
    peep("N_nachdenklich", 1610, 1080, 640, "zurueck", anim="fade"),
    titel("Strafbarkeit des A", 150, 120, "zurueck", 72),
    OT("A. Strafbarkeit gem. § 223 I StGB", 150, 250, "zurueck", "ExtraBold", 50, anim="fade"),
    *st("I. Tatbestand", 210, 350, "zurueck", True, size=48, stil="Bold"),
    *st("1. Objektiver Tatbestand", 270, 425, "zurueck", True),
    *st("2. Subjektiver Tatbestand", 270, 495, "zurueck", True),
    *st2("II. Rechtswidrigkeit", 210, 590, "zurueck", "nwneg", True, size=48, stil="Bold"),
    *st2("1. Notwehr, § 32", 270, 665, "zurueck", "nwneg", False),
    pille("Was folgt aus dem Irrtum von A?", 180, 800, "frage2", fill=PINK, size=40),
])

# 6 Zwei Irrtümer --------------------------------------------------------------------------------------
folie("creme", [("irrtum", "Exkurs › Irrtümer im StGB")], [
    peep("T_verwirrt", 480, 690, 340, "irrtum"),
    peep("T_skeptisch", 1440, 690, 340, "irrtum", d=0.2),
    blase("denk", 360, 200, "tbi", 220, 150, inhalt=["Irrtum über", "Sachverhalt"], textsize=38, ziel=(450, 350)),
    OT("Tatbestandsirrtum", 480, 720, "tbi", "ExtraBold", 60, anker="m", d=0.2),
    OT("(§ 16 Abs. 1 StGB)", 480, 800, "tbi", size=42, farbe=TEXT, anker="m", d=0.3),
    pille("Vorsatz entfällt", 480, 875, "tbifolge", fill=GRUEN, size=38, anker="m"),
    blase("denk", 400, 240, "vi", 1700, 150, inhalt=["Irrtum über die", "rechtliche", "Bewertung"], textsize=34, ziel=(1480, 350)),
    OT("Verbotsirrtum", 1440, 720, "vi", "ExtraBold", 60, anker="m", d=0.2),
    OT("(§ 17 StGB)", 1440, 800, "vi", size=42, farbe=TEXT, anker="m", d=0.3),
    pille("ohne Schuld nur, wenn unvermeidbar", 1440, 875, "vifolge", fill=ORANGE, size=36, anker="m"),
])

# 7 Matrix ---------------------------------------------------------------------------------------------
X1, X2, CW = 640, 1230, 560
Y1, Y2, RH = 280, 515, 205
folie("creme", [("matrix", "Exkurs › Worüber irrt der Täter?")], [
    titel("Worüber irrt der Täter?", 960, 60, "matrix", 72, anker="m"),
    OT("Tatsachen", X1 + CW / 2, 205, "matrix", "ExtraBold", 44, anker="m", d=0.3),
    OT("Rechtliche Bewertung", X2 + CW / 2, 205, "matrix", "ExtraBold", 44, anker="m", d=0.5),
    OT("Tatbestand", 600, Y1 + RH / 2 - 24, "matrix", "ExtraBold", 44, anker="r", d=0.7),
    OT("Rechtfertigung", 600, Y2 + RH / 2 - 24, "matrix", "ExtraBold", 44, anker="r", d=0.9),
    fl_block(X1, Y1, CW, RH, GRUEN, "m1", [("Tatbestandsirrtum", "ExtraBold", 44, INK), ("§ 16 I 1 StGB", "Regular", 38, INK)]),
    fl_block(X2, Y1, CW, RH, BLAU, "m2", [("Verbotsirrtum", "ExtraBold", 44, INK), ("§ 17 StGB", "Regular", 38, INK)]),
    fl_block(X2, Y2, CW, RH, LILA, "m3", [("Erlaubnisirrtum", "ExtraBold", 44, INK), ("= Verbotsirrtum, § 17 StGB", "Regular", 36, INK)]),
    fl_block(X1, Y2, CW, RH, WEISS, "m4", [("?", "ExtraBold", 100, INK)], bis="etbi"),
    fl_block(X1, Y2, CW, RH, GELB, "etbi", [], anim="cut"),
    block(X1, Y2, CW, RH, (0, 0, 0, 0), None, "etbi", anim="fade",
          zeilen=[("Erlaubnistatbestands-", "ExtraBold", 44, INK), ("irrtum (ETBI)", "ExtraBold", 44, INK)]),
    warnung(680, 840, "luecke", gr=34),
    pille("Keine gesetzliche Regelung", 730, 805, "luecke", fill=ROT, size=40),
])

# 8 Liegt ein ETBI vor? --------------------------------------------------------------------------------
folie("creme", [("pruef", "Erlaubnistatbestandsirrtum › Vorliegen")], [
    karte(80, 60, 1380, 930, "pruef"),
    peep("N_tipp", 1690, 1080, 620, "tipp", anim="cut"),
    peep("N_nachdenklich", 1690, 1080, 620, "pruef", d=0.3, bis="tipp"),
    titel("Liegt ein ETBI vor?", 150, 110, "pruef", 72),
    OT("Wäre A gerechtfertigt, wenn seine Vorstellung stimmen würde?", 150, 235, "wenn", "Bold", 40),
    haken(190, 355, "c1", gr=30), OT("Gegenwärtiger, rechtswidriger Angriff (Messer)", 240, 330, "c1", size=42),
    haken(190, 435, "c2", gr=30), OT("Erforderlich: kein milderes, gleich sicheres Mittel", 240, 410, "c2", size=42),
    haken(190, 515, "c3", gr=30), OT("Geboten", 240, 490, "c3", size=42),
    haken(190, 595, "c4", gr=30), OT("Verteidigungswille", 240, 570, "c4", size=42),
    pille("ETBI (+)", 160, 660, "c5", fill=GRUEN, size=46),
    warnung(195, 835, "tipp", gr=30),
    OT("Klausurfehler: hypothetische Prüfung vergessen", 245, 808, "tipp", "ExtraBold", 40, farbe=DROT),
    OT("Auch bei echtem Angriff überzogen » ETBI hilft nicht", 245, 870, "tipp", size=38, farbe=TEXT, d=0.6),
])

# 9 Streitstand ----------------------------------------------------------------------------------------
def nummer(n, y, cue, d, farbe):
    return [pille(str(n), 150, y - 8, cue, fill=farbe, size=34, d=d, pad=(20, 8))]


folie("creme", [("streit", "Erlaubnistatbestandsirrtum › Streitstand")], [
    karte(80, 60, 1400, 930, "streit"),
    peep("N_nachdenklich", 1690, 1080, 620, "streit", d=0.3),
    titel("Wie wird der ETBI behandelt?", 150, 110, "streit", 70),
    *nummer(1, 330, "vier", 0.0, GRUEN), OT("Lehre von den negativen Tatbestandsmerkmalen", 240, 330, "vier", size=44),
    *nummer(2, 430, "vier", 0.35, BLAU), OT("Strenge Schuldtheorie", 240, 430, "vier", size=44, d=0.35),
    *nummer(3, 530, "vier", 0.7, LILA), OT("Eingeschränkte Schuldtheorie", 240, 530, "vier", size=44, d=0.7),
    *nummer(4, 630, "vier", 1.05, ORANGE), OT("Rechtsfolgenverweisende eingeschränkte Schuldtheorie", 240, 630, "vier", size=44, d=1.05),
])

# 10 Negative Tatbestandsmerkmale ---------------------------------------------------------------------
folie("creme", [("lnt", "Streitstand › 1. Negative Tatbestandsmerkmale")], [
    titel("Lehre von den negativen Tatbestandsmerkmalen", 960, 60, "lnt", 64, anker="m"),
    fl_block(200, 250, 470, 150, GRUEN, "bloecke", [("Tatbestand", "ExtraBold", 48, INK)], bis="merge"),
    fl_block(200, 410, 470, 150, BLAU, "bloecke", [("RWK", "ExtraBold", 48, INK)], d=0.2, bis="merge"),
    fl_block(200, 570, 470, 150, PINK, "bloecke", [("Schuld", "ExtraBold", 48, INK)], d=0.4),
    fl_block(200, 250, 470, 310, LILA, "merge", [], anim="cut"),
    block(200, 250, 470, 310, (0, 0, 0, 0), None, "merge", anim="fade",
          zeilen=[("Gesamt-", "ExtraBold", 44, INK), ("Unrechtstatbestand", "ExtraBold", 44, INK)]),
    pille("§ 16 I 1 StGB direkt", 800, 270, "lntfolge", fill=GELB, size=42),
    OT("Vorsatz entfällt", 810, 370, "lntfolge", "Bold", 46, d=0.3),
    OT("Kritik", 810, 480, "lntkritik", "ExtraBold", 50, farbe=DROT),
    E("mosquito", 845, 600, 70, "lntkritik", d=0.3),
    OT("Mücke töten = Notwehr üben?", 900, 575, "lntkritik", size=44, d=0.3),
    OT("Tatbestandslos ≠ gerechtfertigt", 810, 660, "lntkritik", size=44, d=0.8),
])

# 11 Strenge Schuldtheorie ---------------------------------------------------------------------------
folie("creme", [("sst", "Streitstand › 2. Strenge Schuldtheorie")], [
    titel("Strenge Schuldtheorie", 960, 60, "sst", 76, anker="m"),
    OT("Anwendung von § 17 StGB", 960, 200, "sst17", "Bold", 50, anker="m"),
    linienzug([(620, 350), (960, 285), (1300, 350)], "sst17", breite=8, farbe=INK, d=0.3),
    OT("Vermeidbarkeit (+)", 560, 385, "sstv1", "ExtraBold", 46, anker="m"),
    pfeil_ink(560, 460, 560, 540, "sstv1", d=0.3),
    pille("Strafmilderung möglich", 560, 560, "sstv1", fill=ORANGE, size=42, anker="m", d=0.5),
    OT("§ 17 S. 2, § 49 I StGB", 560, 665, "sstv1", size=36, farbe=TEXT, anker="m", d=0.7),
    OT("Vermeidbarkeit (-)", 1360, 385, "sstv2", "ExtraBold", 46, anker="m"),
    pfeil_ink(1360, 460, 1360, 540, "sstv2", d=0.3),
    pille("Straflosigkeit", 1360, 560, "sstv2", fill=GRUEN, size=42, anker="m", d=0.5),
    OT("Schuld entfällt", 1360, 665, "sstv2", size=36, farbe=TEXT, anker="m", d=0.7),
    OT("Kritik: A wollte sich rechtstreu verhalten", 960, 790, "sstkritik", "ExtraBold", 46, farbe=DROT, anker="m"),
    OT("Er irrt über Tatsachen, nicht über das Recht.", 960, 860, "sstkritik", size=42, anker="m", d=0.6),
])

# 12 Eingeschränkte Schuldtheorie --------------------------------------------------------------------
folie("creme", [("est", "Streitstand › 3. Eingeschränkte Schuldtheorie")], [
    titel("Eingeschränkte Schuldtheorie", 960, 50, "est", 72, anker="m"),
    pille("§ 16 I 1 StGB analog", 960, 165, "est16", fill=LILA, size=42, anker="m"),
    OT("Lage gleicht einem Tatbestandsirrtum", 960, 262, "est16", size=38, farbe=TEXT, anker="m", d=0.4),
    OT("» Vorsatzunrecht entfällt", 960, 320, "estfolge", "ExtraBold", 48, anker="m"),
    OT("Kritik: keine vorsätzliche, rechtswidrige Haupttat", 960, 405, "estkritik", "ExtraBold", 42, farbe=DROT, anker="m"),
    peep("H_schlau", 520, 900, 380, "teiln"),
    OT("Hintermann kennt die Wahrheit", 520, 915, "teiln", "Bold", 34, anker="m", d=0.2),
    pfeil_ink(760, 720, 1150, 720, "teiln", d=0.5),
    OT("Anstiftung / Beihilfe", 955, 630, "teiln", "ExtraBold", 36, anker="m", d=0.6),
    OT("§§ 26, 27 StGB", 955, 675, "teiln", size=32, farbe=TEXT, anker="m", d=0.6),
    peep("A_bueste_ruhig", 1390, 900, 380, "teiln", d=0.8),
    OT("A: Haupttat?", 1390, 915, "teiln", "Bold", 34, anker="m", d=0.9),
    kreuz(1620, 600, "lueck2", gr=40),
    pille("Strafbarkeitslücke", 1580, 480, "lueck2", fill=ROT, size=36, anker="m"),
])

# 13 Rechtsfolgenverweisende eingeschränkte Schuldtheorie -------------------------------------------
folie("creme", [("rest", "Streitstand › 4. Herrschende Meinung")], [
    titel("Rechtsfolgenverweisende eingeschr. Schuldtheorie", 960, 50, "rest", 58, anker="m"),
    pille("herrschende Meinung", 960, 160, "rest", fill=GRUEN, size=36, anker="m", d=0.5),
    fl_block(200, 290, 520, 140, GRUEN, "rest", [("Tatbestand", "ExtraBold", 46, INK)], d=1.0),
    fl_block(200, 440, 520, 140, BLAU, "rest", [("RWK", "ExtraBold", 46, INK)], d=1.2),
    fl_block(200, 590, 520, 140, PINK, "rest", [("Schuld", "ExtraBold", 46, INK)], d=1.4),
    haken(800, 360, "restvors", gr=32), OT("Vorsatz bleibt", 850, 335, "restvors", "Bold", 46),
    haken(800, 510, "restrw", gr=32), OT("Tat rechtswidrig", 850, 485, "restrw", "Bold", 46),
    kreuz(800, 660, "restschuld", gr=30), OT("Vorsatzschuld entfällt", 850, 635, "restschuld", "ExtraBold", 46),
    OT("§ 16 I 1 StGB analog, nur Rechtsfolge", 850, 700, "restschuld", size=36, farbe=TEXT, d=0.6),
    haken(225, 830, "restvorteil", gr=30), OT("Teilnahmefähige Haupttat bleibt", 275, 805, "restvorteil", "ExtraBold", 44),
    pille("Rspr.: § 16 StGB entsprechend", 200, 880, "bgh", fill=GELB, size=38),
])

# 14 Ergebnis der Ansichten --------------------------------------------------------------------------
TX0, TX1, TX2 = 160, 1040, 1740
RY = [290, 385, 480, 575]
FARBEN = [GRUEN, BLAU, LILA, ORANGE]
folie("creme", [("tab", "Streitstand › Entscheidung")], [
    titel("Ergebnis der Ansichten für A", 960, 50, "tab", 72, anker="m"),
    OT("Ansicht", TX0 + 30, 205, "tab", "ExtraBold", 38, farbe=TEXT),
    OT("Strafbarkeit aus § 223 StGB", TX1 + 30, 205, "tab", "ExtraBold", 38, farbe=TEXT),
    *[fl_block(TX0, y, TX2 - TX0, 82, (*FARBEN[i][:3], 110), "tab", [], rund=14, rand=3, d=0.2 + 0.2 * i) for i, y in enumerate(RY)],
    OT("Negative Tatbestandsmerkmale", TX0 + 30, RY[0] + 18, "tab", size=40, d=0.3),
    OT("Strenge Schuldtheorie", TX0 + 30, RY[1] + 18, "tab", size=40, d=0.5),
    OT("Eingeschränkte Schuldtheorie", TX0 + 30, RY[2] + 18, "tab", size=40, d=0.7),
    OT("Rechtsfolgenverweisende (h. M.)", TX0 + 30, RY[3] + 18, "tab", size=40, d=0.9),
    OT("(-)  Vorsatz entfällt", TX1 + 30, RY[0] + 18, "t1", size=40),
    OT("(-)  Vorsatzunrecht entfällt", TX1 + 30, RY[2] + 18, "t1", size=40, d=0.25),
    OT("(-)  Vorsatzschuld entfällt", TX1 + 30, RY[3] + 18, "t1", size=40, d=0.5),
    block(TX0 - 6, RY[1] - 6, TX2 - TX0 + 12, 94, (0, 0, 0, 0), None, "t2", rund=16, rand=DROT, randbreite=6, anim="fade"),
    OT("(+)  nur Strafmilderung", TX1 + 30, RY[1] + 18, "t2", "ExtraBold", 40, farbe=DROT),
    pille("Streitentscheid erforderlich", 960, 695, "entsch", fill=GELB, size=42, anker="m"),
    OT("Tipp: Irrtum unvermeidbar? Dann sind alle einig, Streit offenlassen.", 160, 810, "tipp2", "Bold", 38),
    block(TX0 - 6, RY[3] - 6, TX2 - TX0 + 12, 94, (0, 0, 0, 0), None, "folge", rund=16, rand=DGRUEN, randbreite=7, anim="fade"),
    haken(TX2 + 60, RY[3] + 41, "folge", gr=34),
    OT("Strenge Schuldtheorie wird dem rechtstreuen Täter nicht gerecht", 160, 870, "f1", size=34, farbe=TEXT),
    OT("Nur die h. M. schließt die Lücke bei der Teilnahme", 160, 920, "f2", size=34, farbe=TEXT),
])

# 15 Endschema § 223 ---------------------------------------------------------------------------------
folie("creme", [("end", "Ergebnis › § 223 I StGB")], [
    karte(80, 60, 1250, 930, "end"),
    peep("N_freut", 1610, 1080, 640, "end", d=0.3),
    titel("Strafbarkeit des A", 150, 110, "end", 72),
    OT("A. Strafbarkeit gem. § 223 I StGB", 150, 230, "end", "ExtraBold", 48, d=0.4),
    *st("I. Tatbestand", 210, 320, "e1", True, size=46, stil="Bold"),
    *st("II. Rechtswidrigkeit", 210, 395, "e2", True, size=46, stil="Bold"),
    *st("1. Notwehr, § 32", 270, 465, "e2", False, size=42, d=0.5),
    OT("III. Schuld", 210, 545, "e3", "Bold", 46),
    *st("1. Erlaubnistatbestandsirrtum", 270, 615, "e3", True, size=42, d=0.5),
    OT("2. Streitentscheid: h. M.", 270, 685, "e4", size=42),
    *st("» Vorsatzschuld", 270, 755, "e5", False, size=42, stil="Bold"),
    pille("IV. Ergebnis: § 223 I StGB (-)", 190, 840, "e6", fill=ROT, size=42),
])

# 16 § 229 --------------------------------------------------------------------------------------------
folie("creme", [("b229", "Ergebnis › § 229 StGB")], [
    karte(80, 60, 1300, 930, "b229"),
    peep("A_bueste_betroffen", 1650, 1080, 600, "b229", d=0.3),
    titel("B. Strafbarkeit gem. § 229 StGB", 150, 110, "b229", 66),
    OT("§ 16 I 2 StGB analog: Fahrlässigkeit bleibt unberührt", 150, 225, "b229", size=38, farbe=TEXT, d=0.6),
    OT("I. Tatbestand", 210, 315, "b1", "Bold", 48),
    *st("Objektive Sorgfaltspflichtverletzung", 270, 390, "b2", True, size=42),
    OT("genauer Blick unter der Laterne: Handy erkennbar", 270, 455, "b2", size=36, farbe=TEXT, d=0.3),
    *st("II. Rechtswidrigkeit", 210, 540, "b3", True, size=46, stil="Bold"),
    *st("III. Schuld", 210, 615, "b3", True, size=46, stil="Bold", d=0.3),
    pille("IV. Ergebnis: § 229 StGB (+)", 190, 700, "b3", fill=GRUEN, size=42, d=0.6),
    OT("Denk an den Strafantrag, § 230 StGB", 210, 850, "b4", "Bold", 42),
])

# 17 Merksatz -------------------------------------------------------------------------------------------
folie("creme", [("merke", "Merksatz")], [
    karte(80, 120, 1400, 800, "merke", fill=(255, 251, 230, 255)),
    peep("N_freut", 1680, 1080, 640, "merke", d=0.3),
    titel("Merke", 780, 180, "merke", 84, anker="m"),
    *markertext([[("Irrt der Täter über ", 0), ("Tatsachen", "a"), (", die ihn", 0)],
                 [("rechtfertigen würden, entfällt nach h. M.", 0)],
                 [("die ", 0), ("Vorsatzschuld", "b"), (".", 0)]],
                780, 330, 50, "merke", {"a": "hl3", "b": "hl4"}, d=0.3),
    *markertext([[("Irrt er über die ", 0), ("rechtliche Bewertung", "c"), (",", 0)],
                 [("hilft ihm nur § 17 StGB.", 0)]],
                780, 620, 50, "merke2", {"c": "hl5"}),
])
