"""Folien der Folge 081 v2. Jedes Element nennt die Wortmarke, zu der es erscheint."""
from engine import *

C1, C2, C3 = (232, 149, 138, 255), (222, 106, 88, 255), (200, 57, 42, 255)
ZELLE = (255, 255, 255, 150)
ORANGE = (240, 128, 60, 255)


def ok(x, y, cue, size=58, d=0.0):
    return E("check-mark-button", x, y, size, cue, d=d)


def nein(x, y, cue, size=58, d=0.0):
    return E("cross-mark", x, y, size, cue, d=d)


def zeile_mit_status(text, x, y, cue, status, status_cue, size=56, stil="Regular", d=0.0):
    """Schemazeile, deren (+)/(-) erst zur eigenen Marke hinter dem Text erscheint."""
    els = [T(text, x, y, cue, stil, size, d=d)]
    w = F(stil, size).getlength(text + " ")
    els.append(T(status, x + w, y, status_cue, "Bold", size))
    return els


FOLIEN = []


def folie(bg, pfade, els):
    FOLIEN.append(dict(bg=bg, pfade=pfade, els=els))


# 1 Fall -------------------------------------------------------------------------------
folie("hell", [("fall", "Fall")], [
    T("Nachts am Bahnhof", 960, 60, "fall", "ExtraBold", 96, anker="m"),
    E("crescent-moon", 455, 112, 105, "fall", d=0.15),
    E("station", 1465, 112, 105, "fall", d=0.3),
    E("person-standing", 560, 590, 290, "a"),
    T("A", 560, 755, "a", "ExtraBold", 84, anker="m", d=0.15),
    E("person-running", 1360, 590, 290, "b"),
    T("B", 1360, 755, "b", "ExtraBold", 84, anker="m", d=0.15),
    E("coat", 1560, 520, 110, "tasche"),
    T("greift in die Jackentasche", 1360, 850, "tasche", "Regular", 44, anker="m", d=0.1),
    wolke(360, 210, "Messer!", "messer", 600, 270, schwanz=(-40, 1), emoji="kitchen-knife", emoji_size=100, textsize=52),
    E("oncoming-fist", 960, 560, 170, "faust"),
    E("collision", 1150, 470, 120, "faust", d=0.25),
    E("face-with-head-bandage", 1135, 928, 62, "nase"),
    T("Nase gebrochen", 1180, 905, "nase", "Regular", 44),
    wolke(380, 210, "Ihr Handy!", "handy", 1400, 270, schwanz=(-20, 1), emoji="mobile-phone", emoji_size=100, textsize=52),
    E("eyes", 310, 873, 62, "licht"),
    T("hätte das Handy sehen können", 350, 850, "licht", "Regular", 44),
    T("Wie hat sich A strafbar gemacht?", 960, 975, "frage", "ExtraBold", 62, anker="m"),
])

# 2 Schema I ---------------------------------------------------------------------------
folie("hell", [("schema", "A. § 223 I StGB › I. Tatbestand"), ("rw", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    T("Strafbarkeit des A", 960, 60, "schema", "ExtraBold", 100, anker="m"),
    T("A. Strafbarkeit gem. § 223 I StGB", 330, 220, "a223", "ExtraBold", 74),
    T("I. Tatbestand", 470, 330, "tb", "Regular", 64),
    *zeile_mit_status("1. Objektiver Tatbestand", 560, 415, "tbok", "(+)", "tbok", 58),
    *zeile_mit_status("2. Subjektiver Tatbestand", 560, 495, "vors", "(+)", "vors", 58),
    T("II. Rechtswidrigkeit", 470, 590, "rw", "Regular", 64),
    T("1. Notwehr, § 32", 560, 675, "nw", "Regular", 58),
])

# 3 § 32 (dunkel) ----------------------------------------------------------------------
folie("dunkel", [("norm", "II. Rechtswidrigkeit › Notwehr, § 32 StGB")], [
    kreis_emoji("open-book", 960, 205, 112, "norm"),
    T("§ 32 StGB", 960, 355, "norm", "Bold", 86, farbe=WEISS, anker="m", d=0.2),
    *richtext([[("Abs. 1: Wer eine Tat begeht, die durch Notwehr", 0)],
               [("geboten ist, handelt nicht ", 0), ("rechtswidrig", "a"), (".", 0)]],
              960, 470, 56, "norm", {"a": "hl1"}, d=0.35),
    *richtext([[("Abs. 2: Notwehr ist die Verteidigung, die erforderlich ist,", 0)],
               [("um einen ", 0), ("gegenwärtigen rechtswidrigen Angriff", "b")],
               [("von sich oder einem anderen abzuwenden.", 0)]],
              960, 650, 56, "abs2", {"b": "hl2"}),
])

# 4 Notwehrlage: Vorstellung vs. Wirklichkeit ------------------------------------------
folie("hell", [("nwl", "II. Rechtswidrigkeit › Notwehrlage")], [
    T("Notwehrlage?", 960, 45, "nwl", "ExtraBold", 96, anker="m"),
    T("Angriff = drohende Verletzung rechtlich geschützter Interessen durch einen Menschen",
      960, 170, "nwl", "Regular", 44, farbe=GRAU, anker="m", d=0.3),
    wolke(460, 200, "Ich bringe das Handy", "wirkl", 1360, 380, schwanz=(-10, 1), emoji="mobile-phone", emoji_size=90, textsize=44),
    E("person-running", 1360, 660, 210, "wirkl", d=0.1),
    T("Wirklichkeit", 1360, 790, "wirkl", "ExtraBold", 64, anker="m", d=0.2),
    nein(1215, 912, "wirkl", d=0.35),
    T("kein Angriff", 1255, 885, "wirkl", "Regular", 54, d=0.35),
    wolke(460, 200, "Messerangriff!", "vorst", 560, 380, schwanz=(10, 1), emoji="kitchen-knife", emoji_size=90, textsize=44),
    E("person-standing", 560, 660, 210, "vorst", d=0.1),
    T("Vorstellung von A", 560, 790, "vorst", "ExtraBold", 64, anker="m", d=0.2),
    ok(435, 912, "vorst", d=0.35),
    T("Angriff", 475, 885, "vorst", "Regular", 54, d=0.35),
    T("Putativ-", 960, 560, "putativ", "ExtraBold", 60, anker="m"),
    T("notwehr", 960, 630, "putativ", "ExtraBold", 60, anker="m"),
])

# 5 Schema II --------------------------------------------------------------------------
folie("hell", [("zurueck", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    T("Strafbarkeit des A", 960, 60, "zurueck", "ExtraBold", 100, anker="m", anim="fade"),
    T("A. Strafbarkeit gem. § 223 I StGB", 330, 220, "zurueck", "ExtraBold", 74, anim="fade"),
    T("I. Tatbestand (+)", 470, 330, "zurueck", "Regular", 64, anim="fade"),
    T("1. Objektiver Tatbestand (+)", 560, 415, "zurueck", "Regular", 58, anim="fade"),
    T("2. Subjektiver Tatbestand (+)", 560, 495, "zurueck", "Regular", 58, anim="fade"),
    *zeile_mit_status("II. Rechtswidrigkeit", 470, 590, "zurueck", "(+)", "nwneg", 64),
    *zeile_mit_status("1. Notwehr, § 32", 560, 675, "zurueck", "(-)", "nwneg", 58),
    E("thinking-face", 540, 830, 110, "frage2"),
    T("Was folgt aus dem Irrtum von A?", 620, 800, "frage2", "ExtraBold", 62),
])

# 6 Zwei Irrtümer ----------------------------------------------------------------------
folie("hell", [("irrtum", "Exkurs › Irrtümer im StGB")], [
    E("ninja", 470, 555, 230, "irrtum"),
    E("ninja", 1450, 555, 230, "irrtum", d=0.2),
    wolke(440, 220, ["Irrtum über", "Sachverhalt"], "tbi", 510, 230, schwanz=(-30, 1), textsize=54),
    T("Tatbestandsirrtum", 470, 705, "tbi", "ExtraBold", 78, anker="m", d=0.2),
    T("(§ 16 Abs. 1 StGB)", 470, 800, "tbi", "Regular", 58, anker="m", d=0.3),
    T("→ Vorsatz entfällt", 470, 905, "tbifolge", "Bold", 54, anker="m"),
    wolke(560, 220, ["Irrtum über rechtliche", "Bewertung"], "vi", 1490, 230, schwanz=(-30, 1), textsize=54),
    T("Verbotsirrtum", 1450, 705, "vi", "ExtraBold", 78, anker="m", d=0.2),
    T("(§ 17 StGB)", 1450, 800, "vi", "Regular", 58, anker="m", d=0.3),
    T("→ ohne Schuld nur, wenn unvermeidbar", 1450, 905, "vifolge", "Bold", 50, anker="m"),
])

# 7 Matrix -----------------------------------------------------------------------------
X0, X1, X2, CW = 250, 620, 1210, 560
Y1, Y2, RH = 270, 510, 210
folie("hell", [("matrix", "Exkurs › Worüber irrt der Täter?")], [
    T("Worüber irrt der Täter?", 960, 40, "matrix", "ExtraBold", 90, anker="m"),
    E("magnifying-glass-tilted-left", X1 + CW / 2 + 35 - F("ExtraBold", 54).getlength("Tatsachen") / 2 - 45, 222, 60, "matrix", d=0.3),
    T("Tatsachen", X1 + CW / 2 + 35, 195, "matrix", "ExtraBold", 54, anker="m", d=0.3),
    E("balance-scale", X2 + CW / 2 + 35 - F("ExtraBold", 54).getlength("Rechtliche Bewertung") / 2 - 45, 222, 60, "matrix", d=0.5),
    T("Rechtliche Bewertung", X2 + CW / 2 + 35, 195, "matrix", "ExtraBold", 54, anker="m", d=0.5),
    T("Tatbestand", 590, Y1 + RH / 2 - 26, "matrix", "ExtraBold", 54, anker="r", d=0.7),
    T("Rechtfertigung", 590, Y2 + RH / 2 - 26, "matrix", "ExtraBold", 54, anker="r", d=0.9),
    block(X1, Y1, CW, RH, ZELLE, None, "m1", rund=18, rand=INK, randbreite=3,
          zeilen=[("Tatbestandsirrtum", "Bold", 52, INK), ("§ 16 I 1 StGB", "Regular", 46, GRAU)]),
    block(X2, Y1, CW, RH, ZELLE, None, "m2", rund=18, rand=INK, randbreite=3,
          zeilen=[("Verbotsirrtum", "Bold", 52, INK), ("§ 17 StGB", "Regular", 46, GRAU)]),
    block(X2, Y2, CW, RH, ZELLE, None, "m3", rund=18, rand=INK, randbreite=3,
          zeilen=[("Erlaubnisirrtum", "Bold", 52, INK), ("= Verbotsirrtum, § 17 StGB", "Regular", 46, GRAU)]),
    block(X1, Y2, CW, RH, ZELLE, None, "m4", rund=18, rand=INK, randbreite=3, bis="etbi",
          zeilen=[("?", "ExtraBold", 110, INK)]),
    # Fläche wechselt sofort, nur der neue Text blendet ein (keine durchscheinende alte Schrift)
    block(X1, Y2, CW, RH, (255, 244, 225, 235), None, "etbi", rund=18, rand=ORANGE, randbreite=7, anim="cut", zeilen=[]),
    block(X1, Y2, CW, RH, (0, 0, 0, 0), None, "etbi", anim="fade",
          zeilen=[("Erlaubnistatbestands-", "Bold", 52, INK), ("irrtum (ETBI)", "Bold", 52, INK)]),
    E("warning", 560, 820, 76, "luecke"),
    T("Keine gesetzliche Regelung", 615, 792, "luecke", "ExtraBold", 62, farbe=ROT),
])

# 8 Liegt ein ETBI vor? -----------------------------------------------------------------
folie("hell", [("pruef", "Erlaubnistatbestandsirrtum › Vorliegen")], [
    T("Liegt ein ETBI vor?", 960, 40, "pruef", "ExtraBold", 96, anker="m"),
    E("thinking-face", 330, 222, 90, "wenn"),
    T("Wäre A gerechtfertigt, wenn seine Vorstellung stimmen würde?", 395, 195, "wenn", "Regular", 54),
    ok(420, 348, "c1"), T("Gegenwärtiger, rechtswidriger Angriff (Messer)", 480, 322, "c1", "Regular", 54),
    ok(420, 433, "c2"), T("Erforderlich: kein milderes, gleich sicheres Mittel", 480, 407, "c2", "Regular", 54),
    ok(420, 518, "c3"), T("Geboten", 480, 492, "c3", "Regular", 54),
    ok(420, 603, "c4"), T("Verteidigungswille", 480, 577, "c4", "Regular", 54),
    T("→ ETBI (+)", 400, 675, "c5", "ExtraBold", 74),
    E("warning", 420, 858, 76, "tipp"),
    T("Klausurfehler: hypothetische Prüfung vergessen", 480, 825, "tipp", "Bold", 54, farbe=ROT),
    T("Auch bei echtem Angriff überzogen → ETBI hilft nicht", 480, 898, "tipp", "Regular", 48, farbe=GRAU, d=0.6),
])

# 9 Streitstand Überblick ---------------------------------------------------------------
folie("hell", [("streit", "Erlaubnistatbestandsirrtum › Streitstand")], [
    T("Wie wird der ETBI behandelt?", 960, 45, "streit", "ExtraBold", 90, anker="m"),
    E("balance-scale", 960, 250, 140, "streit", d=0.3),
    T("1. Lehre von den negativen Tatbestandsmerkmalen", 360, 380, "vier", "Regular", 58),
    T("2. Strenge Schuldtheorie", 360, 475, "vier", "Regular", 58, d=0.35),
    T("3. Eingeschränkte Schuldtheorie", 360, 570, "vier", "Regular", 58, d=0.7),
    T("4. Rechtsfolgenverweisende eingeschränkte Schuldtheorie", 360, 665, "vier", "Regular", 58, d=1.05),
])

# 10 Negative Tatbestandsmerkmale ------------------------------------------------------
folie("hell", [("lnt", "Streitstand › 1. Negative Tatbestandsmerkmale")], [
    T("Lehre von den negativen", 960, 35, "lnt", "ExtraBold", 90, anker="m"),
    T("Tatbestandsmerkmalen", 960, 130, "lnt", "ExtraBold", 90, anker="m"),
    block(300, 270, 470, 150, C1, "Tatbestand", "bloecke", 62, bis="merge"),
    block(300, 420, 470, 150, C2, "RWK", "bloecke", 62, d=0.2, bis="merge"),
    block(300, 570, 470, 150, C3, "Schuld", "bloecke", 62, d=0.4),
    block(300, 270, 470, 300, (215, 118, 102, 255), None, "merge", anim="cut", zeilen=[]),
    block(300, 270, 470, 300, (0, 0, 0, 0), None, "merge", anim="fade",
          zeilen=[("Gesamt-", "Regular", 50, WEISS), ("Unrechtstatbestand", "Regular", 50, WEISS)]),
    T("→ § 16 I 1 StGB direkt", 880, 300, "lntfolge", "Bold", 62),
    T("Vorsatz entfällt", 930, 385, "lntfolge", "Regular", 56, d=0.3),
    T("Kritik:", 880, 505, "lntkritik", "ExtraBold", 58, farbe=ROT),
    E("mosquito", 935, 612, 80, "lntkritik", d=0.3),
    T("Mücke töten = Notwehr üben?", 990, 585, "lntkritik", "Regular", 54, d=0.3),
    T("Tatbestandslos ≠ gerechtfertigt", 880, 670, "lntkritik", "Regular", 54, d=0.8),
])

# 11 Strenge Schuldtheorie -------------------------------------------------------------
folie("hell", [("sst", "Streitstand › 2. Strenge Schuldtheorie")], [
    T("Strenge Schuldtheorie", 960, 45, "sst", "ExtraBold", 100, anker="m"),
    T("Anwendung von § 17 StGB", 960, 180, "sst17", "Regular", 62, anker="m"),
    linienzug([(640, 330), (960, 262), (1280, 330)], "sst17", breite=9, d=0.3),
    T("Vermeidbarkeit (+)", 560, 365, "sstv1", "Regular", 60, anker="m"),
    pfeil(560, 455, 560, 545, "sstv1", breite=18, kopf=44, d=0.3),
    T("Strafmilderung möglich", 560, 570, "sstv1", "Regular", 60, anker="m", d=0.5),
    T("§ 17 S. 2, § 49 I StGB", 560, 648, "sstv1", "Regular", 44, farbe=GRAU, anker="m", d=0.7),
    T("Vermeidbarkeit (-)", 1360, 365, "sstv2", "Regular", 60, anker="m"),
    pfeil(1360, 455, 1360, 545, "sstv2", breite=18, kopf=44, d=0.3),
    T("Straflosigkeit", 1360, 570, "sstv2", "Regular", 60, anker="m", d=0.5),
    T("Schuld entfällt", 1360, 648, "sstv2", "Regular", 44, farbe=GRAU, anker="m", d=0.7),
    T("Kritik: A wollte sich rechtstreu verhalten", 960, 790, "sstkritik", "ExtraBold", 56, farbe=ROT, anker="m"),
    T("Er irrt über Tatsachen, nicht über das Recht.", 960, 870, "sstkritik", "Regular", 52, anker="m", d=0.6),
])

# 12 Eingeschränkte Schuldtheorie ------------------------------------------------------
folie("hell", [("est", "Streitstand › 3. Eingeschränkte Schuldtheorie")], [
    T("Eingeschränkte Schuldtheorie", 960, 40, "est", "ExtraBold", 96, anker="m"),
    T("§ 16 I 1 StGB analog", 960, 170, "est16", "Bold", 66, anker="m"),
    T("Lage gleicht einem Tatbestandsirrtum", 960, 250, "est16", "Regular", 48, farbe=GRAU, anker="m", d=0.4),
    T("→ Vorsatzunrecht entfällt", 960, 325, "estfolge", "ExtraBold", 62, anker="m"),
    T("Kritik: keine vorsätzliche, rechtswidrige Haupttat", 960, 440, "estkritik", "Bold", 56, farbe=ROT, anker="m"),
    E("ninja", 560, 700, 180, "teiln"),
    T("Hintermann kennt", 560, 810, "teiln", "Regular", 44, anker="m", d=0.2),
    T("die Wahrheit", 560, 860, "teiln", "Regular", 44, anker="m", d=0.2),
    pfeil(700, 700, 1180, 700, "teiln", breite=14, kopf=40, d=0.5),
    T("Anstiftung / Beihilfe", 940, 580, "teiln", "Regular", 44, anker="m", d=0.6),
    T("§§ 26, 27 StGB", 940, 632, "teiln", "Regular", 40, farbe=GRAU, anker="m", d=0.6),
    E("person-standing", 1340, 700, 180, "teiln", d=0.8),
    T("A: Haupttat?", 1340, 810, "teiln", "Regular", 44, anker="m", d=0.9),
    nein(1450, 610, "lueck2", size=76),
    T("→ Strafbarkeitslücke", 960, 950, "lueck2", "ExtraBold", 62, farbe=ROT, anker="m"),
])

# 13 Rechtsfolgenverweisende eingeschränkte Schuldtheorie ------------------------------
folie("hell", [("rest", "Streitstand › 4. Herrschende Meinung")], [
    T("Rechtsfolgenverweisende", 960, 30, "rest", "ExtraBold", 88, anker="m"),
    T("eingeschränkte Schuldtheorie", 960, 120, "rest", "ExtraBold", 88, anker="m"),
    T("herrschende Meinung", 960, 222, "rest", "Bold", 46, farbe=GRAU, anker="m", d=0.5),
    block(300, 300, 520, 140, C1, "Tatbestand", "rest", 60, d=1.0),
    block(300, 440, 520, 140, C2, "RWK", "rest", 60, d=1.2),
    block(300, 580, 520, 140, C3, "Schuld", "rest", 60, d=1.4),
    ok(880, 370, "restvors"), T("Vorsatz bleibt", 930, 343, "restvors", "Regular", 56),
    ok(880, 510, "restrw"), T("Tat rechtswidrig", 930, 483, "restrw", "Regular", 56),
    nein(880, 640, "restschuld"), T("Vorsatzschuld entfällt", 930, 613, "restschuld", "Bold", 56),
    T("§ 16 I 1 StGB analog, nur Rechtsfolge", 930, 682, "restschuld", "Regular", 44, farbe=GRAU, d=0.6),
    ok(330, 825, "restvorteil"), T("Teilnahmefähige Haupttat bleibt", 385, 798, "restvorteil", "Bold", 54),
    E("balance-scale", 330, 915, 58, "bgh"), T("Rspr.: § 16 StGB entsprechend", 385, 888, "bgh", "Regular", 54),
])

# 14 Ergebnis der Ansichten ------------------------------------------------------------
TX0, TX1, TX2 = 200, 1060, 1720
RY = [285, 385, 485, 585]
folie("hell", [("tab", "Streitstand › Entscheidung")], [
    T("Ergebnis der Ansichten für A", 960, 35, "tab", "ExtraBold", 90, anker="m"),
    T("Ansicht", TX0 + 20, 190, "tab", "Bold", 48, farbe=GRAU),
    T("Strafbarkeit aus § 223 StGB", TX1 + 30, 190, "tab", "Bold", 48, farbe=GRAU),
    linienzug([(TX0, 265), (TX2, 265)], "tab", breite=4),
    T("Negative Tatbestandsmerkmale", TX0 + 20, RY[0] + 25, "tab", "Regular", 48, d=0.3),
    T("Strenge Schuldtheorie", TX0 + 20, RY[1] + 25, "tab", "Regular", 48, d=0.5),
    T("Eingeschränkte Schuldtheorie", TX0 + 20, RY[2] + 25, "tab", "Regular", 48, d=0.7),
    T("Rechtsfolgenverweisende (h. M.)", TX0 + 20, RY[3] + 25, "tab", "Regular", 48, d=0.9),
    *[linienzug([(TX0, y + 100), (TX2, y + 100)], "tab", breite=2, farbe=(120, 120, 120, 255), d=0.3) for y in RY],
    T("(-)  Vorsatz entfällt", TX1 + 30, RY[0] + 25, "t1", "Regular", 48),
    T("(-)  Vorsatzunrecht entfällt", TX1 + 30, RY[2] + 25, "t1", "Regular", 48, d=0.25),
    T("(-)  Vorsatzschuld entfällt", TX1 + 30, RY[3] + 25, "t1", "Regular", 48, d=0.5),
    T("(+)  nur Strafmilderung", TX1 + 30, RY[1] + 25, "t2", "Bold", 48, farbe=ROT),
    block(TX0 - 10, RY[1] + 4, TX2 - TX0 + 20, 92, (0, 0, 0, 0), None, "t2", rund=14, rand=ORANGE, randbreite=5, anim="fade", d=0.3),
    T("→ Streitentscheid erforderlich", 960, 710, "entsch", "ExtraBold", 62, anker="m"),
    E("light-bulb", 330, 832, 66, "tipp2"),
    T("Irrtum unvermeidbar? Dann sind alle einig: Streit offenlassen.", 390, 805, "tipp2", "Regular", 50),
    block(TX0 - 10, RY[3] + 4, TX2 - TX0 + 20, 92, (0, 0, 0, 0), None, "folge", rund=14, rand=GRUEN, randbreite=6, anim="fade"),
    ok(TX2 + 55, RY[3] + 50, "folge", size=64),
    T("Strenge Schuldtheorie wird dem rechtstreuen Täter nicht gerecht", 390, 885, "f1", "Regular", 44, farbe=GRAU),
    T("Nur die h. M. schließt die Lücke bei der Teilnahme", 390, 945, "f2", "Regular", 44, farbe=GRAU),
])

# 15 Endschema § 223 -------------------------------------------------------------------
folie("hell", [("end", "Ergebnis › § 223 I StGB")], [
    T("Strafbarkeit des A", 960, 30, "end", "ExtraBold", 96, anker="m"),
    T("A. Strafbarkeit gem. § 223 I StGB", 300, 165, "end", "ExtraBold", 68, d=0.4),
    T("I. Tatbestand (+)", 420, 265, "e1", "Regular", 58),
    T("II. Rechtswidrigkeit (+)", 420, 345, "e2", "Regular", 58),
    T("1. Notwehr, § 32 (-)", 510, 420, "e2", "Regular", 52, d=0.5),
    T("III. Schuld", 420, 500, "e3", "Regular", 58),
    T("1. Erlaubnistatbestandsirrtum (+)", 510, 575, "e3", "Regular", 52, d=0.5),
    T("2. Streitentscheid: h. M.", 510, 650, "e4", "Regular", 52),
    T("→ Vorsatzschuld (-)", 510, 725, "e5", "Bold", 52),
    T("IV. Ergebnis: § 223 I StGB (-)", 420, 815, "e6", "ExtraBold", 60),
])

# 16 § 229 -----------------------------------------------------------------------------
folie("hell", [("b229", "Ergebnis › § 229 StGB")], [
    T("B. Strafbarkeit gem. § 229 StGB", 960, 45, "b229", "ExtraBold", 86, anker="m"),
    T("§ 16 I 2 StGB analog: Fahrlässigkeit bleibt unberührt", 960, 165, "b229", "Regular", 52, farbe=GRAU, anker="m", d=0.6),
    T("I. Tatbestand", 420, 280, "b1", "Regular", 60),
    T("Objektive Sorgfaltspflichtverletzung (+)", 510, 360, "b2", "Regular", 54),
    E("eyes", 555, 458, 60, "b2", d=0.3),
    T("genauer Blick: Handy erkennbar", 600, 432, "b2", "Regular", 48, farbe=GRAU, d=0.3),
    T("II. Rechtswidrigkeit (+)", 420, 530, "b3", "Regular", 60),
    T("III. Schuld (+)", 420, 610, "b3", "Regular", 60, d=0.3),
    T("IV. Ergebnis: § 229 StGB (+)", 420, 700, "b3", "ExtraBold", 62, d=0.6),
    E("memo", 450, 850, 66, "b4"),
    T("Strafantrag, § 230 StGB", 510, 822, "b4", "Regular", 54),
])

# 17 Merksatz (dunkel) -----------------------------------------------------------------
folie("dunkel", [("merke", "Merksatz")], [
    kreis_emoji("light-bulb", 960, 205, 112, "merke"),
    T("Merke", 960, 355, "merke", "Bold", 86, farbe=WEISS, anker="m", d=0.2),
    *richtext([[("Irrt der Täter über ", 0), ("Tatsachen", "a"), (", die ihn rechtfertigen", 0)],
               [("würden, entfällt nach h. M. die ", 0), ("Vorsatzschuld", "b"), (".", 0)]],
              960, 470, 58, "merke", {"a": "hl3", "b": "hl4"}, d=0.3),
    *richtext([[("Irrt er über die ", 0), ("rechtliche Bewertung", "c"), (",", 0)],
               [("hilft ihm nur § 17 StGB.", 0)]],
              960, 680, 58, "merke2", {"c": "hl5"}),
])
