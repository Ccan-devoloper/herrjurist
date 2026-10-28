"""Folge 081 im Humaaans-Stil: gleiche Tonspur und Wortmarken wie v2 (skript2.py)."""
from hstil import *

FOLIEN = []


def folie(bg, pfade, els):
    FOLIEN.append(dict(bg=bg, pfade=pfade, els=els))


KX, KY, KW, KH = 60, 50, 1800, 960  # Standardkarte


def k(cue, **kw):
    return karte(KX, KY, KW, KH, cue, **kw)


# 1 Fall ---------------------------------------------------------------------------------
folie("cyan", [("fall", "Fall")], [
    k("fall", keil=(930, 830, TIEF)),
    HT("DER FALL", 140, 120, "fall", "Bold", 30, farbe=BLAU),
    HT("Nachts am Bahnhof", 140, 165, "fall", "ExtraBold", 72),
    kreis(1340, 190, 75, GELBKREIS, "fall", d=0.3),
    raute(1010, 930, 26, PFIRSICH, "fall", d=0.5),
    HT("A wartet auf den letzten Zug.", 140, 300, "a", size=40, farbe=TEXT),
    fig("A_steht", 1150, 900, 500, "a", bis="faust"),
    fig("A_schlaegt", 1150, 900, 520, "faust", anim="cut"),
    HT("B rennt auf A zu", 140, 360, "b", size=40, farbe=TEXT),
    fig("B_rennt", 1620, 900, 520, "b", bis="handy"),
    HT("und greift in die Jackentasche.", 140, 412, "tasche", size=40, farbe=TEXT),
    E("coat", 1790, 640, 80, "tasche"),
    hwolke(280, 170, "Messer!", "messer", 985, 195, ziel=(1095, 360), emoji="kitchen-knife", emoji_size=80),
    HT("A denkt: Messer! Und schlägt zu.", 140, 480, "messer", size=40, farbe=TEXT),
    E("oncoming-fist", 1390, 590, 110, "faust"),
    E("collision", 1480, 500, 90, "faust", d=0.25),
    E("face-with-head-bandage", 1735, 395, 70, "nase"),
    HT("B: Nase gebrochen.", 140, 532, "nase", size=40, farbe=TEXT),
    fig("B_gibt", 1620, 900, 500, "handy", anim="cut"),
    hwolke(290, 170, "Ihr Handy!", "handy", 1690, 190, ziel=(1650, 360), emoji="mobile-phone", emoji_size=80),
    HT("Dabei wollte B nur das Handy zurückgeben.", 140, 600, "handy", "Bold", 40),
    E("eyes", 165, 690, 50, "licht"),
    HT("Bei genauem Hinsehen erkennbar.", 205, 668, "licht", size=40, farbe=TEXT),
    pille("Wie hat sich A strafbar gemacht?", 140, 790, "frage", size=40),
])

# 2 Schema I -----------------------------------------------------------------------------
folie("cyan", [("schema", "A. § 223 I StGB › I. Tatbestand"), ("rw", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    k("schema"),
    kreis(1540, 560, 270, LAVENDEL, "schema", d=0.2),
    fig("Erklaerer", 1540, 860, 560, "schema", d=0.4),
    raute(1230, 220, 24, PFIRSICH, "schema", d=0.5),
    HT("Strafbarkeit des A", 140, 110, "schema", "ExtraBold", 76),
    HT("A. Strafbarkeit gem. § 223 I StGB", 140, 235, "a223", "Bold", 52),
    HT("I. Tatbestand", 200, 335, "tb", size=48),
    *zeile("1. Objektiver Tatbestand", 260, 410, "tbok", "(+)", size=44, farbe=TEXT),
    *zeile("2. Subjektiver Tatbestand", 260, 480, "vors", "(+)", size=44, farbe=TEXT),
    HT("II. Rechtswidrigkeit", 200, 575, "rw", size=48),
    HT("1. Notwehr, § 32", 260, 650, "nw", size=44, farbe=TEXT),
])

# 3 § 32 (blau) --------------------------------------------------------------------------
folie("blau", [("norm", "II. Rechtswidrigkeit › Notwehr, § 32 StGB")], [
    kreis(130, 820, 120, (60, 68, 255, 255), "norm", d=0.4),
    raute(1760, 170, 30, PFIRSICH, "norm", d=0.5),
    kreis(1790, 900, 60, LAVENDEL, "norm", d=0.6),
    kreis_emoji("open-book", 960, 205, 112, "norm"),
    HT("§ 32 StGB", 960, 355, "norm", "ExtraBold", 80, farbe=WEISS, anker="m", d=0.2),
    *richtext([[("Abs. 1: Wer eine Tat begeht, die durch Notwehr", 0)],
               [("geboten ist, handelt nicht ", 0), ("rechtswidrig", "a"), (".", 0)]],
              960, 470, 50, "norm", {"a": "hl1"}, hl=GELB, d=0.35),
    *richtext([[("Abs. 2: Notwehr ist die Verteidigung, die erforderlich ist,", 0)],
               [("um einen ", 0), ("gegenwärtigen rechtswidrigen Angriff", "b")],
               [("von sich oder einem anderen abzuwenden.", 0)]],
              960, 650, 50, "abs2", {"b": "hl2"}, hl=GELB),
])

# 4 Notwehrlage --------------------------------------------------------------------------
folie("cyan", [("nwl", "II. Rechtswidrigkeit › Notwehrlage")], [
    k("nwl"),
    HT("Notwehrlage?", 960, 95, "nwl", "ExtraBold", 76, anker="m"),
    HT("Angriff = drohende Verletzung rechtlich geschützter Interessen durch einen Menschen",
       960, 195, "nwl", size=34, farbe=TEXT, anker="m", d=0.3),
    kreis(1360, 590, 210, MINT, "wirkl"),
    fig("B_gibt", 1360, 790, 400, "wirkl", d=0.15),
    hwolke(400, 160, "Ich bringe das Handy", "wirkl", 1560, 330, ziel=(1380, 420), emoji="mobile-phone", emoji_size=70, textsize=38),
    HT("Wirklichkeit", 1360, 820, "wirkl", "ExtraBold", 52, anker="m", d=0.25),
    pille("kein Angriff", 1360, 895, "wirkl", fill=ROT, anker="m", size=36, d=0.4),
    kreis(560, 590, 210, PFIRSICH, "vorst"),
    fig("A_steht", 560, 790, 400, "vorst", d=0.15),
    hwolke(360, 160, "Messerangriff!", "vorst", 350, 330, ziel=(545, 420), emoji="kitchen-knife", emoji_size=70, textsize=38),
    HT("Vorstellung von A", 560, 820, "vorst", "ExtraBold", 52, anker="m", d=0.25),
    pille("Angriff", 560, 895, "vorst", fill=BLAU, anker="m", size=36, d=0.4),
    HT("Putativ-", 960, 540, "putativ", "ExtraBold", 50, farbe=BLAU, anker="m"),
    HT("notwehr", 960, 600, "putativ", "ExtraBold", 50, farbe=BLAU, anker="m"),
])

# 5 Schema II ----------------------------------------------------------------------------
folie("cyan", [("zurueck", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    k("zurueck"),
    kreis(1540, 580, 270, LAVENDEL, "zurueck", anim="fade"),
    fig("Denker", 1540, 800, 470, "zurueck", anim="fade"),
    HT("Strafbarkeit des A", 140, 110, "zurueck", "ExtraBold", 76, anim="fade"),
    HT("A. Strafbarkeit gem. § 223 I StGB", 140, 235, "zurueck", "Bold", 52, anim="fade"),
    *zeile("I. Tatbestand", 200, 335, "zurueck", "(+)", size=48),
    *zeile("1. Objektiver Tatbestand", 260, 410, "zurueck", "(+)", size=44, farbe=TEXT),
    *zeile("2. Subjektiver Tatbestand", 260, 480, "zurueck", "(+)", size=44, farbe=TEXT),
    *zeile("II. Rechtswidrigkeit", 200, 575, "zurueck", "(+)", "nwneg", size=48),
    *zeile("1. Notwehr, § 32", 260, 650, "zurueck", "(-)", "nwneg", plus=False, size=44, farbe=TEXT),
    E("thinking-face", 180, 810, 80, "frage2"),
    pille("Was folgt aus dem Irrtum von A?", 240, 772, "frage2", size=40),
])

# 6 Zwei Irrtümer (Hanlon-Layout: weiß / blau) ------------------------------------------
folie("cyan", [("irrtum", "Exkurs › Irrtümer im StGB")], [
    k("irrtum", keil=(1000, 920, TIEF)),
    fig("T_links", 480, 690, 330, "irrtum"),
    fig("T_rechts", 1440, 690, 330, "irrtum", d=0.2),
    hwolke(400, 170, ["Irrtum über", "Sachverhalt"], "tbi", 300, 165, ziel=(455, 330), textsize=42),
    HT("Tatbestandsirrtum", 480, 720, "tbi", "ExtraBold", 60, anker="m", d=0.2),
    HT("(§ 16 Abs. 1 StGB)", 480, 800, "tbi", size=42, farbe=TEXT, anker="m", d=0.3),
    pille("Vorsatz entfällt", 480, 875, "tbifolge", anker="m", size=38),
    hwolke(500, 170, ["Irrtum über rechtliche", "Bewertung"], "vi", 1620, 165, ziel=(1470, 330), textsize=42),
    HT("Verbotsirrtum", 1440, 720, "vi", "ExtraBold", 60, farbe=WEISS, anker="m", d=0.2),
    HT("(§ 17 StGB)", 1440, 800, "vi", size=42, farbe=(210, 214, 255, 255), anker="m", d=0.3),
    pille("ohne Schuld nur, wenn unvermeidbar", 1440, 875, "vifolge", fill=ORANGE, anker="m", size=36),
])

# 7 Matrix -------------------------------------------------------------------------------
X1, X2, CW = 640, 1230, 560
Y1, Y2, RH = 280, 515, 205
folie("cyan", [("matrix", "Exkurs › Worüber irrt der Täter?")], [
    k("matrix"),
    HT("Worüber irrt der Täter?", 960, 95, "matrix", "ExtraBold", 72, anker="m"),
    E("magnifying-glass-tilted-left", X1 + CW / 2 - F("Bold", 42).getlength("Tatsachen") / 2 - 20, 234, 50, "matrix", d=0.3),
    HT("Tatsachen", X1 + CW / 2 + 20, 210, "matrix", "Bold", 42, anker="m", d=0.3),
    E("balance-scale", X2 + CW / 2 - F("Bold", 42).getlength("Rechtliche Bewertung") / 2 - 20, 234, 50, "matrix", d=0.5),
    HT("Rechtliche Bewertung", X2 + CW / 2 + 20, 210, "matrix", "Bold", 42, anker="m", d=0.5),
    HT("Tatbestand", 605, Y1 + RH / 2 - 22, "matrix", "Bold", 42, anker="r", d=0.7),
    HT("Rechtfertigung", 605, Y2 + RH / 2 - 22, "matrix", "Bold", 42, anker="r", d=0.9),
    block(X1, Y1, CW, RH, ZELLE, None, "m1", rund=22,
          zeilen=[("Tatbestandsirrtum", "Bold", 44, NAVY), ("§ 16 I 1 StGB", "Regular", 38, TEXT)]),
    block(X2, Y1, CW, RH, ZELLE, None, "m2", rund=22,
          zeilen=[("Verbotsirrtum", "Bold", 44, NAVY), ("§ 17 StGB", "Regular", 38, TEXT)]),
    block(X2, Y2, CW, RH, ZELLE, None, "m3", rund=22,
          zeilen=[("Erlaubnisirrtum", "Bold", 44, NAVY), ("= Verbotsirrtum, § 17 StGB", "Regular", 38, TEXT)]),
    block(X1, Y2, CW, RH, PFIRSICH, None, "m4", rund=22, bis="etbi", zeilen=[("?", "ExtraBold", 100, NAVY)]),
    block(X1, Y2, CW, RH, ORANGE, None, "etbi", rund=22, anim="cut", zeilen=[]),
    block(X1, Y2, CW, RH, (0, 0, 0, 0), None, "etbi", anim="fade",
          zeilen=[("Erlaubnistatbestands-", "Bold", 44, WEISS), ("irrtum (ETBI)", "Bold", 44, WEISS)]),
    E("warning", 645, 832, 60, "luecke"),
    pille("Keine gesetzliche Regelung", 690, 800, "luecke", fill=ROT, size=40),
])

# 8 Liegt ein ETBI vor? ------------------------------------------------------------------
folie("cyan", [("pruef", "Erlaubnistatbestandsirrtum › Vorliegen")], [
    k("pruef"),
    raute(1740, 150, 28, PFIRSICH, "pruef", d=0.3),
    kreis(1720, 880, 70, LAVENDEL, "pruef", d=0.4),
    HT("Liegt ein ETBI vor?", 140, 105, "pruef", "ExtraBold", 76),
    E("thinking-face", 170, 248, 64, "wenn"),
    HT("Wäre A gerechtfertigt, wenn seine Vorstellung stimmen würde?", 220, 225, "wenn", size=42),
    ok(185, 353, "c1", size=54), HT("Gegenwärtiger, rechtswidriger Angriff (Messer)", 240, 330, "c1", size=42, farbe=TEXT),
    ok(185, 433, "c2", size=54), HT("Erforderlich: kein milderes, gleich sicheres Mittel", 240, 410, "c2", size=42, farbe=TEXT),
    ok(185, 513, "c3", size=54), HT("Geboten", 240, 490, "c3", size=42, farbe=TEXT),
    ok(185, 593, "c4", size=54), HT("Verteidigungswille", 240, 570, "c4", size=42, farbe=TEXT),
    pille("ETBI (+)", 160, 660, "c5", size=46),
    E("warning", 180, 836, 60, "tipp"),
    HT("Klausurfehler: hypothetische Prüfung vergessen", 230, 810, "tipp", "Bold", 42, farbe=ROT),
    HT("Auch bei echtem Angriff überzogen → ETBI hilft nicht", 230, 870, "tipp", size=38, farbe=TEXT, d=0.6),
])

# 9 Streitstand ---------------------------------------------------------------------------
NUM = lambda n, y, cue, d: [kreis(185, y + 26, 30, BLAU, cue, d=d),
                            HT(str(n), 185, y + 4, cue, "Bold", 36, farbe=WEISS, anker="m", d=d)]
folie("cyan", [("streit", "Erlaubnistatbestandsirrtum › Streitstand")], [
    k("streit"),
    kreis(1620, 330, 190, LAVENDEL, "streit", d=0.2),
    fig("Grueblerin", 1620, 480, 330, "streit", d=0.4),
    HT("Wie wird der ETBI behandelt?", 140, 110, "streit", "ExtraBold", 72),
    *NUM(1, 330, "vier", 0.0), HT("Lehre von den negativen Tatbestandsmerkmalen", 240, 330, "vier", size=44),
    *NUM(2, 430, "vier", 0.35), HT("Strenge Schuldtheorie", 240, 430, "vier", size=44, d=0.35),
    *NUM(3, 530, "vier", 0.7), HT("Eingeschränkte Schuldtheorie", 240, 530, "vier", size=44, d=0.7),
    *NUM(4, 630, "vier", 1.05), HT("Rechtsfolgenverweisende eingeschränkte Schuldtheorie", 240, 630, "vier", size=44, d=1.05),
])

# 10 Negative Tatbestandsmerkmale -------------------------------------------------------
folie("cyan", [("lnt", "Streitstand › 1. Negative Tatbestandsmerkmale")], [
    k("lnt"),
    HT("Lehre von den negativen", 960, 90, "lnt", "ExtraBold", 68, anker="m"),
    HT("Tatbestandsmerkmalen", 960, 170, "lnt", "ExtraBold", 68, anker="m"),
    block(200, 300, 470, 150, TEAL, "Tatbestand", "bloecke", 50, stil="Bold", textfarbe=NAVY, rund=18, bis="merge"),
    block(200, 460, 470, 150, BLAU, "RWK", "bloecke", 50, stil="Bold", rund=18, d=0.2, bis="merge"),
    block(200, 620, 470, 150, NAVY, "Schuld", "bloecke", 50, stil="Bold", rund=18, d=0.4),
    block(200, 300, 470, 310, (91, 110, 245, 255), None, "merge", rund=18, anim="cut", zeilen=[]),
    block(200, 300, 470, 310, (0, 0, 0, 0), None, "merge", anim="fade",
          zeilen=[("Gesamt-", "Bold", 44, WEISS), ("Unrechtstatbestand", "Bold", 44, WEISS)]),
    pille("§ 16 I 1 StGB direkt", 800, 320, "lntfolge", size=44),
    HT("Vorsatz entfällt", 800, 415, "lntfolge", size=46, d=0.3),
    HT("Kritik", 800, 530, "lntkritik", "ExtraBold", 50, farbe=ROT),
    E("mosquito", 830, 640, 70, "lntkritik", d=0.3),
    HT("Mücke töten = Notwehr üben?", 885, 615, "lntkritik", size=44, farbe=TEXT, d=0.3),
    HT("Tatbestandslos ≠ gerechtfertigt", 800, 700, "lntkritik", size=44, farbe=TEXT, d=0.8),
])

# 11 Strenge Schuldtheorie --------------------------------------------------------------
folie("cyan", [("sst", "Streitstand › 2. Strenge Schuldtheorie")], [
    k("sst"),
    HT("Strenge Schuldtheorie", 960, 95, "sst", "ExtraBold", 76, anker="m"),
    HT("Anwendung von § 17 StGB", 960, 215, "sst17", size=50, anker="m"),
    linienzug([(620, 360), (960, 295), (1300, 360)], "sst17", breite=8, farbe=NAVY, d=0.3),
    HT("Vermeidbarkeit (+)", 560, 395, "sstv1", "Bold", 46, anker="m"),
    pfeil(560, 470, 560, 545, "sstv1", breite=14, kopf=36, farbe=NAVY, d=0.3),
    pille("Strafmilderung möglich", 560, 565, "sstv1", fill=ORANGE, anker="m", size=42, d=0.5),
    HT("§ 17 S. 2, § 49 I StGB", 560, 665, "sstv1", size=36, farbe=TEXT, anker="m", d=0.7),
    HT("Vermeidbarkeit (-)", 1360, 395, "sstv2", "Bold", 46, anker="m"),
    pfeil(1360, 470, 1360, 545, "sstv2", breite=14, kopf=36, farbe=NAVY, d=0.3),
    pille("Straflosigkeit", 1360, 565, "sstv2", anker="m", size=42, d=0.5),
    HT("Schuld entfällt", 1360, 665, "sstv2", size=36, farbe=TEXT, anker="m", d=0.7),
    HT("Kritik: A wollte sich rechtstreu verhalten", 960, 790, "sstkritik", "ExtraBold", 46, farbe=ROT, anker="m"),
    HT("Er irrt über Tatsachen, nicht über das Recht.", 960, 860, "sstkritik", size=42, farbe=TEXT, anker="m", d=0.6),
])

# 12 Eingeschränkte Schuldtheorie -------------------------------------------------------
folie("cyan", [("est", "Streitstand › 3. Eingeschränkte Schuldtheorie")], [
    k("est"),
    HT("Eingeschränkte Schuldtheorie", 960, 90, "est", "ExtraBold", 72, anker="m"),
    pille("§ 16 I 1 StGB analog", 960, 195, "est16", anker="m", size=44),
    HT("Lage gleicht einem Tatbestandsirrtum", 960, 290, "est16", size=38, farbe=TEXT, anker="m", d=0.4),
    HT("→ Vorsatzunrecht entfällt", 960, 350, "estfolge", "ExtraBold", 48, anker="m"),
    HT("Kritik: keine vorsätzliche, rechtswidrige Haupttat", 960, 440, "estkritik", "Bold", 44, farbe=ROT, anker="m"),
    kreis(560, 760, 150, ROSA, "teiln"),
    fig("Hintermann", 560, 880, 330, "teiln", d=0.1),
    HT("Hintermann kennt die Wahrheit", 560, 900, "teiln", size=34, farbe=TEXT, anker="m", d=0.2),
    pfeil(740, 740, 1170, 740, "teiln", breite=12, kopf=34, farbe=NAVY, d=0.5),
    HT("Anstiftung / Beihilfe", 955, 650, "teiln", "Bold", 36, anker="m", d=0.6),
    HT("§§ 26, 27 StGB", 955, 695, "teiln", size=32, farbe=TEXT, anker="m", d=0.6),
    kreis(1360, 760, 150, PFIRSICH, "teiln", d=0.8),
    fig("A_steht", 1360, 880, 330, "teiln", d=0.9),
    HT("A: Haupttat?", 1360, 900, "teiln", size=34, farbe=TEXT, anker="m", d=1.0),
    pille("Strafbarkeitslücke", 1360, 530, "lueck2", fill=ROT, anker="m", size=36),
    nein(1600, 564, "lueck2", size=60),
])

# 13 Rechtsfolgenverweisende eingeschränkte Schuldtheorie -------------------------------
folie("cyan", [("rest", "Streitstand › 4. Herrschende Meinung")], [
    k("rest"),
    HT("Rechtsfolgenverweisende", 960, 80, "rest", "ExtraBold", 68, anker="m"),
    HT("eingeschränkte Schuldtheorie", 960, 158, "rest", "ExtraBold", 68, anker="m"),
    pille("herrschende Meinung", 960, 250, "rest", fill=GRUEN, anker="m", size=34, d=0.5),
    block(200, 350, 520, 130, TEAL, "Tatbestand", "rest", 48, stil="Bold", textfarbe=NAVY, rund=18, d=1.0),
    block(200, 490, 520, 130, BLAU, "RWK", "rest", 48, stil="Bold", rund=18, d=1.2),
    block(200, 630, 520, 130, NAVY, "Schuld", "rest", 48, stil="Bold", rund=18, d=1.4),
    ok(790, 415, "restvors", size=54), HT("Vorsatz bleibt", 840, 392, "restvors", size=46),
    ok(790, 555, "restrw", size=54), HT("Tat rechtswidrig", 840, 532, "restrw", size=46),
    nein(790, 690, "restschuld", size=54), HT("Vorsatzschuld entfällt", 840, 667, "restschuld", "Bold", 46),
    HT("§ 16 I 1 StGB analog, nur Rechtsfolge", 840, 727, "restschuld", size=36, farbe=TEXT, d=0.6),
    ok(225, 845, "restvorteil", size=54), HT("Teilnahmefähige Haupttat bleibt", 275, 822, "restvorteil", "Bold", 44),
    E("balance-scale", 225, 925, 54, "bgh"), HT("Rspr.: § 16 StGB entsprechend", 275, 902, "bgh", size=44, farbe=TEXT),
])

# 14 Ergebnis der Ansichten -------------------------------------------------------------
TX0, TX1, TX2 = 160, 1040, 1760
RY = [300, 395, 490, 585]
folie("cyan", [("tab", "Streitstand › Entscheidung")], [
    k("tab"),
    HT("Ergebnis der Ansichten für A", 960, 90, "tab", "ExtraBold", 72, anker="m"),
    HT("Ansicht", TX0 + 30, 215, "tab", "Bold", 38, farbe=TEXT),
    HT("Strafbarkeit aus § 223 StGB", TX1 + 30, 215, "tab", "Bold", 38, farbe=TEXT),
    *[block(TX0, y, TX2 - TX0, 82, ZELLE, None, "tab", rund=14, d=0.2 + 0.2 * i, zeilen=[]) for i, y in enumerate(RY)],
    HT("Negative Tatbestandsmerkmale", TX0 + 30, RY[0] + 20, "tab", size=40, d=0.3),
    HT("Strenge Schuldtheorie", TX0 + 30, RY[1] + 20, "tab", size=40, d=0.5),
    HT("Eingeschränkte Schuldtheorie", TX0 + 30, RY[2] + 20, "tab", size=40, d=0.7),
    HT("Rechtsfolgenverweisende (h. M.)", TX0 + 30, RY[3] + 20, "tab", size=40, d=0.9),
    HT("(-)  Vorsatz entfällt", TX1 + 30, RY[0] + 20, "t1", size=40),
    HT("(-)  Vorsatzunrecht entfällt", TX1 + 30, RY[2] + 20, "t1", size=40, d=0.25),
    HT("(-)  Vorsatzschuld entfällt", TX1 + 30, RY[3] + 20, "t1", size=40, d=0.5),
    block(TX0, RY[1], TX2 - TX0, 82, (0, 0, 0, 0), None, "t2", rund=14, rand=ORANGE, randbreite=5, anim="fade"),
    HT("(+)  nur Strafmilderung", TX1 + 30, RY[1] + 20, "t2", "Bold", 40, farbe=ROT),
    pille("Streitentscheid erforderlich", 960, 700, "entsch", anker="m", size=42),
    E("light-bulb", 190, 842, 54, "tipp2"),
    HT("Irrtum unvermeidbar? Dann sind alle einig: Streit offenlassen.", 235, 818, "tipp2", size=38),
    block(TX0, RY[3], TX2 - TX0, 82, (0, 0, 0, 0), None, "folge", rund=14, rand=GRUEN, randbreite=6, anim="fade"),
    ok(TX2 + 42, RY[3] + 41, "folge", size=54),
    HT("Strenge Schuldtheorie wird dem rechtstreuen Täter nicht gerecht", 235, 880, "f1", size=34, farbe=TEXT),
    HT("Nur die h. M. schließt die Lücke bei der Teilnahme", 235, 930, "f2", size=34, farbe=TEXT),
])

# 15 Endschema § 223 --------------------------------------------------------------------
folie("cyan", [("end", "Ergebnis › § 223 I StGB")], [
    k("end"),
    kreis(1540, 580, 270, MINT, "end", d=0.2),
    fig("Erklaerer", 1540, 880, 580, "end", d=0.4),
    HT("Strafbarkeit des A", 140, 100, "end", "ExtraBold", 76),
    HT("A. Strafbarkeit gem. § 223 I StGB", 140, 215, "end", "Bold", 50, d=0.4),
    *zeile("I. Tatbestand", 200, 305, "e1", "(+)", size=46),
    *zeile("II. Rechtswidrigkeit", 200, 380, "e2", "(+)", size=46),
    *zeile("1. Notwehr, § 32", 260, 450, "e2", "(-)", plus=False, size=42, farbe=TEXT, d=0.5),
    HT("III. Schuld", 200, 530, "e3", size=46),
    *zeile("1. Erlaubnistatbestandsirrtum", 260, 600, "e3", "(+)", size=42, farbe=TEXT, d=0.5),
    HT("2. Streitentscheid: h. M.", 260, 670, "e4", size=42, farbe=TEXT),
    *zeile("→ Vorsatzschuld", 260, 740, "e5", "(-)", plus=False, size=42, stil="Bold"),
    pille("IV. Ergebnis: § 223 I StGB (-)", 190, 830, "e6", fill=ROT, size=44),
])

# 16 § 229 ------------------------------------------------------------------------------
folie("cyan", [("b229", "Ergebnis › § 229 StGB")], [
    k("b229"),
    kreis(1560, 600, 250, PFIRSICH, "b229", d=0.2),
    fig("A_steht", 1560, 880, 520, "b229", d=0.4),
    HT("B. Strafbarkeit gem. § 229 StGB", 140, 100, "b229", "ExtraBold", 68),
    HT("§ 16 I 2 StGB analog: Fahrlässigkeit bleibt unberührt", 140, 200, "b229", size=40, farbe=TEXT, d=0.6),
    HT("I. Tatbestand", 200, 300, "b1", size=48),
    *zeile("Objektive Sorgfaltspflichtverletzung", 260, 375, "b2", "(+)", size=42, farbe=TEXT),
    E("eyes", 285, 470, 50, "b2", d=0.3),
    HT("genauer Blick: Handy erkennbar", 325, 448, "b2", size=38, farbe=TEXT, d=0.3),
    *zeile("II. Rechtswidrigkeit", 200, 535, "b3", "(+)", size=48),
    *zeile("III. Schuld", 200, 610, "b3", "(+)", size=48, d=0.3),
    pille("IV. Ergebnis: § 229 StGB (+)", 190, 700, "b3", fill=GRUEN, size=44, d=0.6),
    E("memo", 215, 868, 56, "b4"),
    HT("Strafantrag, § 230 StGB", 265, 845, "b4", size=44),
])

# 17 Merksatz (blau) --------------------------------------------------------------------
folie("blau", [("merke", "Merksatz")], [
    kreis(1750, 930, 170, (60, 68, 255, 255), "merke", d=0.4),
    raute(170, 160, 30, PFIRSICH, "merke", d=0.5),
    kreis(150, 930, 60, LAVENDEL, "merke", d=0.6),
    kreis_emoji("light-bulb", 960, 205, 112, "merke"),
    HT("Merke", 960, 355, "merke", "ExtraBold", 80, farbe=WEISS, anker="m", d=0.2),
    *richtext([[("Irrt der Täter über ", 0), ("Tatsachen", "a"), (", die ihn rechtfertigen", 0)],
               [("würden, entfällt nach h. M. die ", 0), ("Vorsatzschuld", "b"), (".", 0)]],
              960, 470, 52, "merke", {"a": "hl3", "b": "hl4"}, hl=GELB, d=0.3),
    *richtext([[("Irrt er über die ", 0), ("rechtliche Bewertung", "c"), (",", 0)],
               [("hilft ihm nur § 17 StGB.", 0)]],
              960, 680, 52, "merke2", {"c": "hl5"}, hl=GELB),
])
