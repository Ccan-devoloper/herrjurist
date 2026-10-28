"""Folge 081 Open Peeps v3 – überarbeitet nach Sichtprüfung (Nacht, Choreografie, Karten, Erzähler nur punktuell)."""
from ostil import *

FOLIEN = []
PP = SP + "peeps/op/"
BG_FARBE = {"creme": (255, 248, 236, 255), "nacht": None}
PFAD_FARBE = {"creme": (21, 21, 21, 140), "nacht": (220, 225, 255, 170)}


def folie(bg, pfade, els):
    FOLIEN.append(dict(bg=bg, pfade=pfade, els=els))


def _breite(text, stil, size):
    # tatsächliche Breite inkl. Ersatzschrift für "→" + ein Leerzeichen
    return OT(text, 0, 0, "_", stil, size).sprite.width - 8 + F(stil, size).getlength(" ")


def st(text, x, y, cue, plus, size=44, d=0.0, stil="Regular"):
    zeichen = "(+)" if plus else "(-)"
    return [OT(text, x, y, cue, stil, size, d=d),
            OT(zeichen, x + _breite(text, stil, size), y, cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT), d=d)]


def st2(text, x, y, cue, st_cue, plus, size=44, stil="Regular", d=0.0):
    zeichen = "(+)" if plus else "(-)"
    return [OT(text, x, y, cue, stil, size, d=d),
            OT(zeichen, x + _breite(text, stil, size), y, st_cue, "ExtraBold", size, farbe=(DGRUEN if plus else DROT))]


def P(name, cx, unten, hoehe, cue, **k):
    return peep(name, cx, unten, hoehe, cue, **k)


# ======================================================================================================
# 1 Fall (Nacht) – Choreografie: B rennt heran, A erschrickt, A stürmt vor und schlägt, B geht zu Boden
# ======================================================================================================
BODEN, FH = 880, 560
K = FH / 902                      # Maßstab der stehenden Figuren (B-Originalhöhe 902 px)
AX0, AX1, BX = 480, 1030, 1200     # A wartet bei der Bank, A nach dem Vorstürmen, B's Endposition

folie("nacht", [("fall", "Fall · nachts am Bahnhof")], [
    linienzug([(0, BODEN), (W, BODEN)], "fall", breite=7, farbe=(15, 18, 40, 255)),
    titel_voll("Nachts am Bahnhof", 70, 60, "fall", 70),
    icon("pepicons-pencil", "moon", 1790, 120, 150, "fall", farbe="#F9D56E", d=0.3),
    icon("pepicons-pencil", "train", 1560, 150, 170, "fall", farbe="#DCE1FF", d=0.45),
    lichtschein(BX + 40, 620, 420, "fall", d=0.6),
    # A wartet (ruhig), wird skeptisch/angespannt, bekommt Angst; geht dann auf B los (Pose "RoboDance")
    P("A_ruhig", AX0, BODEN, FH, "a", bis="b"),
    P("A_skeptisch", AX0, BODEN, FH, "b", anim="cut", bis="tasche"),
    P("A_angespannt", AX0, BODEN, FH, "tasche", anim="cut", bis="messer"),
    P("A_angst", AX0, BODEN, FH, "messer", anim="cut", bis="faust"),
    bewegt(P("A_stoss", AX1, BODEN, FH, "faust", anim="cut", bis="nase"), "faust", ("faust", 0.28), AX0 - AX1),
    P("A_schreck", AX1, BODEN, FH, "nase", anim="cut", bis="licht"),
    P("A_betroffen", AX1, BODEN, FH, "licht", anim="cut"),
    pille("A", AX0, BODEN + 22, "a", fill=GELB, size=32, anker="m", d=0.2, bis="faust"),
    pille("A", AX1, BODEN + 22, "faust", fill=GELB, size=32, anker="m", anim="cut"),
    # B rennt heran (Pose "Walking" in Bewegung), wird getroffen und weicht zurück, sitzt dann am Boden
    bewegt(P("B_ruft", BX, BODEN, FH, "b", anim="cut", bis=("faust", 0.28)), "b", "tasche", 820),
    bewegt(P("B_getroffen", BX + 70, BODEN, FH, ("faust", 0.28), anim="cut", bis="nase"), ("faust", 0.28), ("faust", 0.6), -70),
    P("B_boden", BX + 90, BODEN, int(578 * K), "nase", anim="cut", bis="handy"),
    P("B_boden_traurig", BX + 90, BODEN, int(578 * K), "handy", anim="cut"),
    pille("B", BX, BODEN + 22, "tasche", fill=BLAU, size=32, anker="m", bis="nase"),
    pille("B", BX + 90, BODEN + 22, "nase", fill=BLAU, size=32, anker="m", anim="cut"),
    blase("denk", 360, 290, "messer", 800, 300, inhalt="Messer!", bild_=PP + "B_killer.png", bildhoehe=165,
          textsize=40, ziel=(500, 330), bis="faust"),
    pille("Nase gebrochen", BX + 110, 470, "nase", fill=ROT, size=30, anker="m", bis="handy"),
    blase("sprech", 480, 250, "handy", 1270, 290, inhalt=["Ich wollte Ihnen nur", "Ihr Handy geben!"], textsize=31,
          spiegeln=True, bis="licht"),
    rueckblende2(1655, 430, "licht", bis="frage"),
    pille("Wie hat sich A strafbar gemacht?", 70, 175, "frage", fill=PINK, size=38),
])

# ======================================================================================================
# 2 Schema I – Karte wächst Zeile für Zeile mit
# ======================================================================================================
KX, KW = 260, 1400
X0, X1, X2 = 330, 390, 450
folie("creme", [("schema", "A. § 223 I StGB › I. Tatbestand"), ("rw", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    *wachsende_karte(KX, 60, KW, [("schema", 180), ("a223", 270), ("tb", 360), ("tbok", 430), ("vors", 500),
                                   ("rw", 595), ("nw", 690)]),
    titel("Strafbarkeit des A", X0, 110, "schema", 72),
    OT("A. Strafbarkeit gem. § 223 I StGB", X0, 240, "a223", "ExtraBold", 50),
    OT("I. Tatbestand", X1, 330, "tb", "Bold", 48),
    *st("1. Objektiver Tatbestand", X2, 400, "tbok", True),
    *st("2. Subjektiver Tatbestand", X2, 470, "vors", True),
    OT("II. Rechtswidrigkeit", X1, 565, "rw", "Bold", 48),
    OT("1. Notwehr, § 32", X2, 640, "nw", size=44),
])

# 3 § 32 --------------------------------------------------------------------------------------------------
folie("creme", [("norm", "II. Rechtswidrigkeit › Notwehr, § 32 StGB")], [
    *wachsende_karte(210, 90, 1500, [("norm", 390), ("abs2", 760)], fill=(255, 251, 230, 255)),
    titel("§ 32 StGB · Notwehr", 960, 150, "norm", 72, anker="m"),
    *markertext([[("Abs. 1: Wer eine Tat begeht, die durch Notwehr", 0)],
                 [("geboten ist, handelt nicht ", 0), ("rechtswidrig", "a"), (".", 0)]],
                960, 300, 48, "norm", {"a": "hl1"}, d=0.35),
    *markertext([[("Abs. 2: Notwehr ist die Verteidigung, die erforderlich ist,", 0)],
                 [("um einen ", 0), ("gegenwärtigen rechtswidrigen Angriff", "b")],
                 [("von sich oder einem anderen abzuwenden.", 0)]],
                960, 510, 48, "abs2", {"b": "hl2"}),
])

# 4 Notwehrlage -------------------------------------------------------------------------------------------
folie("creme", [("nwl", "II. Rechtswidrigkeit › Notwehrlage")], [
    titel("Notwehrlage?", 960, 50, "nwl", 76, anker="m"),
    OT("Angriff = drohende Verletzung rechtlich geschützter Interessen durch einen Menschen", 960, 140, "nwl",
       size=36, farbe=TEXT, anker="m", d=0.3),
    P("B_handy_schwarz", 1400, 830, 420, "wirkl", d=0.1),
    blase("sprech", 400, 230, "wirkl", 1690, 380, inhalt=["Ich bringe", "Ihr Handy!"], textsize=38),
    OT("Wirklichkeit", 1400, 845, "wirkl", "ExtraBold", 50, anker="m", d=0.2),
    ton(kreuz_i(1280, 950, "wirkl", gr=30, d=0.35), "minimal_uncheck", 0.8),
    OT("kein Angriff", 1325, 925, "wirkl", "Bold", 42, d=0.35),
    P("A_bueste_angst", 520, 830, 420, "vorst", d=0.1),
    blase("denk", 380, 290, "vorst", 250, 330, inhalt="Messerangriff!", bild_=PP + "B_killer.png", bildhoehe=160,
          textsize=34, ziel=(430, 420)),
    OT("Vorstellung von A", 520, 845, "vorst", "ExtraBold", 50, anker="m", d=0.2),
    ton(haken_i(450, 950, "vorst", gr=32, d=0.35), "minimal_check", 0.8),
    OT("Angriff", 495, 925, "vorst", "Bold", 42, d=0.35),
    ton(pille("Putativnotwehr", 960, 560, "putativ", fill=ORANGE, size=42, anker="m"), "soft_select"),
])

# 5 Schema II (Rückkehr: gleiche Karte wie Folie 2, sofort vollständig) -------------------------------------
folie("creme", [("zurueck", "A. § 223 I StGB › II. Rechtswidrigkeit")], [
    karte(KX, 60, KW, 820, "zurueck"),
    titel("Strafbarkeit des A", X0, 110, "zurueck", 72),
    OT("A. Strafbarkeit gem. § 223 I StGB", X0, 240, "zurueck", "ExtraBold", 50, anim="fade"),
    *st("I. Tatbestand", X1, 330, "zurueck", True, size=48, stil="Bold"),
    *st("1. Objektiver Tatbestand", X2, 400, "zurueck", True),
    *st("2. Subjektiver Tatbestand", X2, 470, "zurueck", True),
    *st2("II. Rechtswidrigkeit", X1, 565, "zurueck", "nwneg", True, size=48, stil="Bold"),
    *st2("1. Notwehr, § 32", X2, 640, "zurueck", "nwneg", False),
    pille("Was folgt aus dem Irrtum von A?", X1, 745, "frage2", fill=PINK, size=40),
])

# 6 Zwei Irrtümer ------------------------------------------------------------------------------------------
folie("creme", [("irrtum", "Exkurs › Irrtümer im StGB")], [
    P("T_verwirrt", 480, 690, 340, "irrtum"),
    P("T_skeptisch", 1440, 690, 340, "irrtum", d=0.2),
    ton(blase("denk", 360, 200, "tbi", 230, 170, inhalt=["Irrtum über", "Sachverhalt"], textsize=38, ziel=(450, 350)), "soft_expand", 0.7),
    OT("Tatbestandsirrtum", 480, 720, "tbi", "ExtraBold", 60, anker="m", d=0.2),
    OT("(§ 16 Abs. 1 StGB)", 480, 800, "tbi", size=42, farbe=TEXT, anker="m", d=0.3),
    pille("Vorsatz entfällt", 480, 875, "tbifolge", fill=GRUEN, size=38, anker="m"),
    ton(blase("denk", 400, 240, "vi", 1690, 180, inhalt=["Irrtum über die", "rechtliche", "Bewertung"], textsize=34,
              ziel=(1480, 350)), "soft_expand", 0.7),
    OT("Verbotsirrtum", 1440, 720, "vi", "ExtraBold", 60, anker="m", d=0.2),
    OT("(§ 17 StGB)", 1440, 800, "vi", size=42, farbe=TEXT, anker="m", d=0.3),
    pille("ohne Schuld nur, wenn unvermeidbar", 1440, 875, "vifolge", fill=ORANGE, size=36, anker="m"),
])

# 7 Matrix (zentriert) ----------------------------------------------------------------------------------------
MX1, MX2, CW = 560, 1150, 560
Y1, Y2, RH = 280, 515, 205
folie("creme", [("matrix", "Exkurs › Worüber irrt der Täter?")], [
    titel("Worüber irrt der Täter?", 960, 60, "matrix", 72, anker="m"),
    OT("Tatsachen", MX1 + CW / 2, 205, "matrix", "ExtraBold", 44, anker="m", d=0.3),
    OT("Rechtliche Bewertung", MX2 + CW / 2, 205, "matrix", "ExtraBold", 44, anker="m", d=0.5),
    OT("Tatbestand", 520, Y1 + RH / 2 - 24, "matrix", "ExtraBold", 44, anker="r", d=0.7),
    OT("Rechtfertigung", 520, Y2 + RH / 2 - 24, "matrix", "ExtraBold", 44, anker="r", d=0.9),
    fl_block(MX1, Y1, CW, RH, GRUEN, "m1", [("Tatbestandsirrtum", "ExtraBold", 44, INK), ("§ 16 I 1 StGB", "Regular", 38, INK)]),
    fl_block(MX2, Y1, CW, RH, BLAU, "m2", [("Verbotsirrtum", "ExtraBold", 44, INK), ("§ 17 StGB", "Regular", 38, INK)]),
    fl_block(MX2, Y2, CW, RH, LILA, "m3", [("Erlaubnisirrtum", "ExtraBold", 44, INK), ("= Verbotsirrtum, § 17 StGB", "Regular", 36, INK)]),
    fl_block(MX1, Y2, CW, RH, WEISS, "m4", [("?", "ExtraBold", 100, INK)], bis="etbi"),
    ton(fl_block(MX1, Y2, CW, RH, GELB, "etbi", [], anim="cut"), "studio_success", 0.8),
    block(MX1, Y2, CW, RH, (0, 0, 0, 0), None, "etbi", anim="fade",
          zeilen=[("Erlaubnistatbestands-", "ExtraBold", 44, INK), ("irrtum (ETBI)", "ExtraBold", 44, INK)]),
    ton(warnung_i(600, 840, "luecke", gr=34), "soft_warning", 0.8),
    pille("Keine gesetzliche Regelung", 650, 805, "luecke", fill=ROT, size=40),
])

# 8 Liegt ein ETBI vor? (Karte wächst; Erzähler erscheint nur beim Klausurfehler) ---------------------------
LX = 170
folie("creme", [("pruef", "Erlaubnistatbestandsirrtum › Vorliegen")], [
    *wachsende_karte(100, 60, 1340, [("pruef", 170), ("wenn", 260), ("c1", 340), ("c2", 420), ("c3", 500),
                                    ("c4", 580), ("c5", 690), ("tipp", 900)]),
    titel("Liegt ein ETBI vor?", LX, 100, "pruef", 70),
    OT("Wäre A gerechtfertigt, wenn seine Vorstellung stimmen würde?", LX, 225, "wenn", "Bold", 40),
    ton(haken_i(210, 335, "c1", gr=30), "minimal_check", 0.7), OT("Gegenwärtiger, rechtswidriger Angriff (Messer)", 260, 310, "c1", size=42),
    ton(haken_i(210, 415, "c2", gr=30), "minimal_check", 0.7), OT("Erforderlich: kein milderes, gleich sicheres Mittel", 260, 390, "c2", size=42),
    ton(haken_i(210, 495, "c3", gr=30), "minimal_check", 0.7), OT("Geboten", 260, 470, "c3", size=42),
    ton(haken_i(210, 575, "c4", gr=30), "minimal_check", 0.7), OT("Verteidigungswille", 260, 550, "c4", size=42),
    ton(pille("ETBI (+)", 180, 630, "c5", fill=GRUEN, size=46), "soft_complete", 0.8),
    ton(warnung_i(215, 810, "tipp", gr=30), "soft_warning", 0.8),
    OT("Klausurfehler: hypothetische Prüfung vergessen", 265, 783, "tipp", "ExtraBold", 40, farbe=DROT),
    OT("Auch bei echtem Angriff überzogen → ETBI hilft nicht", 265, 845, "tipp", size=38, farbe=TEXT, d=0.6),
    P("E_warnt", 1690, 1080, 560, "tipp", d=0.15),
])

# 9 Streitstand ----------------------------------------------------------------------------------------------
def nummer(n, y, cue, d, farbe):
    return pille(str(n), X0, y - 8, cue, fill=farbe, size=34, d=d, pad=(20, 8))


folie("creme", [("streit", "Erlaubnistatbestandsirrtum › Streitstand")], [
    *wachsende_karte(KX, 60, KW, [("streit", 180), ("vier", 690)]),
    titel("Wie wird der ETBI behandelt?", X0, 110, "streit", 70),
    nummer(1, 300, "vier", 0.0, GRUEN), OT("Lehre von den negativen Tatbestandsmerkmalen", 420, 300, "vier", size=44),
    nummer(2, 400, "vier", 0.35, BLAU), OT("Strenge Schuldtheorie", 420, 400, "vier", size=44, d=0.35),
    nummer(3, 500, "vier", 0.7, LILA), OT("Eingeschränkte Schuldtheorie", 420, 500, "vier", size=44, d=0.7),
    nummer(4, 600, "vier", 1.05, ORANGE), OT("Rechtsfolgenverweisende eingeschränkte Schuldtheorie", 420, 600, "vier", size=44, d=1.05),
])

# 10 Negative Tatbestandsmerkmale (zentriert) -------------------------------------------------------------------
BLX, TXX = 360, 960
folie("creme", [("lnt", "Streitstand › 1. Negative Tatbestandsmerkmale")], [
    titel("Lehre von den negativen Tatbestandsmerkmalen", 960, 60, "lnt", 64, anker="m"),
    fl_block(BLX, 250, 470, 150, GRUEN, "bloecke", [("Tatbestand", "ExtraBold", 48, INK)], bis="merge"),
    fl_block(BLX, 410, 470, 150, BLAU, "bloecke", [("RWK", "ExtraBold", 48, INK)], d=0.2, bis="merge"),
    fl_block(BLX, 570, 470, 150, PINK, "bloecke", [("Schuld", "ExtraBold", 48, INK)], d=0.4),
    ton(fl_block(BLX, 250, 470, 310, LILA, "merge", [], anim="cut"), "organic_snap", 0.8),
    block(BLX, 250, 470, 310, (0, 0, 0, 0), None, "merge", anim="fade",
          zeilen=[("Gesamt-", "ExtraBold", 44, INK), ("Unrechtstatbestand", "ExtraBold", 44, INK)]),
    pille("§ 16 I 1 StGB direkt", TXX, 270, "lntfolge", fill=GELB, size=42),
    OT("Vorsatz entfällt", TXX + 10, 370, "lntfolge", "Bold", 46, d=0.3),
    OT("Kritik", TXX + 10, 480, "lntkritik", "ExtraBold", 50, farbe=DROT),
    icon("fluent-emoji-high-contrast", "mosquito", TXX + 45, 600, 70, "lntkritik", d=0.3),
    OT("Mücke töten = Notwehr üben?", TXX + 100, 575, "lntkritik", size=44, d=0.3),
    OT("Tatbestandslos ≠ gerechtfertigt", TXX + 10, 660, "lntkritik", size=44, d=0.8),
])

# 11 Strenge Schuldtheorie -----------------------------------------------------------------------------------
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

# 12 Eingeschränkte Schuldtheorie ---------------------------------------------------------------------------
folie("creme", [("est", "Streitstand › 3. Eingeschränkte Schuldtheorie")], [
    titel("Eingeschränkte Schuldtheorie", 960, 50, "est", 72, anker="m"),
    pille("§ 16 I 1 StGB analog", 960, 165, "est16", fill=LILA, size=42, anker="m"),
    OT("Lage gleicht einem Tatbestandsirrtum", 960, 262, "est16", size=38, farbe=TEXT, anker="m", d=0.4),
    OT("→ Vorsatzunrecht entfällt", 960, 320, "estfolge", "ExtraBold", 48, anker="m"),
    OT("Kritik: keine vorsätzliche, rechtswidrige Haupttat", 960, 405, "estkritik", "ExtraBold", 42, farbe=DROT, anker="m"),
    P("H_schlau", 520, 900, 380, "teiln"),
    OT("Hintermann kennt die Wahrheit", 520, 915, "teiln", "Bold", 34, anker="m", d=0.2),
    pfeil_ink(760, 700, 1150, 700, "teiln", d=0.5),
    OT("Anstiftung / Beihilfe", 955, 610, "teiln", "ExtraBold", 36, anker="m", d=0.6),
    OT("§§ 26, 27 StGB", 955, 655, "teiln", size=32, farbe=TEXT, anker="m", d=0.6),
    P("A_bueste_ruhig", 1390, 900, 380, "teiln", d=0.8),
    OT("A: Haupttat?", 1390, 915, "teiln", "Bold", 34, anker="m", d=0.9),
    ton(pille("Strafbarkeitslücke", 955, 770, "lueck2", fill=ROT, size=36, anker="m"), "soft_warning", 0.7),
    kreuz_i(1545, 940, "lueck2", gr=32),
])

# 13 Rechtsfolgenverweisende eingeschränkte Schuldtheorie (voller Titel) ------------------------------------
RBX, RTX = 380, 980
folie("creme", [("rest", "Streitstand › 4. Herrschende Meinung")], [
    titel("Rechtsfolgenverweisende eingeschränkte Schuldtheorie", 960, 50, "rest", 56, anker="m"),
    pille("herrschende Meinung", 960, 160, "rest", fill=GRUEN, size=36, anker="m", d=0.5),
    fl_block(RBX, 290, 520, 140, GRUEN, "rest", [("Tatbestand", "ExtraBold", 46, INK)], d=1.0),
    fl_block(RBX, 440, 520, 140, BLAU, "rest", [("RWK", "ExtraBold", 46, INK)], d=1.2),
    fl_block(RBX, 590, 520, 140, PINK, "rest", [("Schuld", "ExtraBold", 46, INK)], d=1.4),
    ton(haken_i(RTX, 360, "restvors", gr=32), "minimal_check", 0.7), OT("Vorsatz bleibt", RTX + 50, 335, "restvors", "Bold", 46),
    ton(haken_i(RTX, 510, "restrw", gr=32), "minimal_check", 0.7), OT("Tat rechtswidrig", RTX + 50, 485, "restrw", "Bold", 46),
    ton(kreuz_i(RTX, 660, "restschuld", gr=30), "minimal_uncheck", 0.8), OT("Vorsatzschuld entfällt", RTX + 50, 635, "restschuld", "ExtraBold", 46),
    OT("§ 16 I 1 StGB analog, nur Rechtsfolge", RTX + 50, 700, "restschuld", size=36, farbe=TEXT, d=0.6),
    haken_i(RBX + 25, 830, "restvorteil", gr=30), OT("Teilnahmefähige Haupttat bleibt", RBX + 75, 805, "restvorteil", "ExtraBold", 44),
    pille("Rspr.: § 16 StGB entsprechend", RBX, 880, "bgh", fill=GELB, size=38),
])

# 14 Ergebnis der Ansichten --------------------------------------------------------------------------------
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
    ton(block(TX0 - 6, RY[3] - 6, TX2 - TX0 + 12, 94, (0, 0, 0, 0), None, "folge", rund=16, rand=DGRUEN, randbreite=7, anim="fade"), "minimal_check", 0.8),
    haken_i(TX2 + 60, RY[3] + 41, "folge", gr=34),
    OT("Strenge Schuldtheorie wird dem rechtstreuen Täter nicht gerecht", 160, 870, "f1", size=34, farbe=TEXT),
    OT("Nur die h. M. schließt die Lücke bei der Teilnahme", 160, 920, "f2", size=34, farbe=TEXT),
])

# 15 Endschema § 223 (Karte wächst) ----------------------------------------------------------------------------
folie("creme", [("end", "Ergebnis › § 223 I StGB")], [
    *wachsende_karte(KX, 60, KW, [("end", 280), ("e1", 350), ("e2", 500), ("e3", 650), ("e4", 720), ("e5", 790),
                                   ("e6", 900)]),
    titel("Strafbarkeit des A", X0, 110, "end", 72),
    OT("A. Strafbarkeit gem. § 223 I StGB", X0, 230, "end", "ExtraBold", 48, d=0.4),
    *st("I. Tatbestand", X1, 320, "e1", True, size=46, stil="Bold"),
    *st("II. Rechtswidrigkeit", X1, 395, "e2", True, size=46, stil="Bold"),
    *st("1. Notwehr, § 32", X2, 465, "e2", False, size=42, d=0.5),
    OT("III. Schuld", X1, 545, "e3", "Bold", 46),
    *st("1. Erlaubnistatbestandsirrtum", X2, 615, "e3", True, size=42, d=0.5),
    OT("2. Streitentscheid: h. M.", X2, 685, "e4", size=42),
    *st("→ Vorsatzschuld", X2, 755, "e5", False, size=42, stil="Bold"),
    ton(pille("IV. Ergebnis: § 223 I StGB (-)", X1 - 20, 830, "e6", fill=ROT, size=42), "soft_complete", 0.8),
])

# 16 § 229 (Karte wächst; A betroffen daneben) ----------------------------------------------------------------
folie("creme", [("b229", "Ergebnis › § 229 StGB")], [
    *wachsende_karte(100, 60, 1300, [("b229", 270), ("b1", 350), ("b2", 480), ("b3", 740), ("b4", 880)]),
    P("A_bueste_betroffen", 1650, 1080, 600, "b229", d=0.3),
    titel("B. Strafbarkeit gem. § 229 StGB", 170, 110, "b229", 66),
    OT("§ 16 I 2 StGB analog: Fahrlässigkeit bleibt unberührt", 170, 225, "b229", size=38, farbe=TEXT, d=0.6),
    OT("I. Tatbestand", 230, 315, "b1", "Bold", 48),
    *st("Objektive Sorgfaltspflichtverletzung", 290, 390, "b2", True, size=42),
    OT("genauer Blick unter der Laterne: Handy erkennbar", 290, 455, "b2", size=36, farbe=TEXT, d=0.3),
    *st("II. Rechtswidrigkeit", 230, 540, "b3", True, size=46, stil="Bold"),
    *st("III. Schuld", 230, 615, "b3", True, size=46, stil="Bold", d=0.3),
    ton(pille("IV. Ergebnis: § 229 StGB (+)", 210, 700, "b3", fill=GRUEN, size=42, d=0.6), "soft_complete", 0.8, 0.6),
    OT("Denk an den Strafantrag, § 230 StGB", 230, 830, "b4", "Bold", 42),
])

# 17 Merksatz (Erzähler freut sich, neben der Karte) ---------------------------------------------------------
folie("creme", [("merke", "Merksatz")], [
    *wachsende_karte(100, 120, 1340, [("merke", 470), ("merke2", 800)], fill=(255, 251, 230, 255)),
    ton(P("E_freut", 1690, 1080, 560, "merke", d=0.3), "dreamy_notification", 0.7),
    titel("Merke", 770, 180, "merke", 84, anker="m"),
    *markertext([[("Irrt der Täter über ", 0), ("Tatsachen", "a"), (", die ihn", 0)],
                 [("rechtfertigen würden, entfällt nach h. M.", 0)],
                 [("die ", 0), ("Vorsatzschuld", "b"), (".", 0)]],
                770, 320, 50, "merke", {"a": "hl3", "b": "hl4"}, d=0.3),
    *markertext([[("Irrt er über die ", 0), ("rechtliche Bewertung", "c"), (",", 0)],
                 [("hilft ihm nur § 17 StGB.", 0)]],
                770, 610, 50, "merke2", {"c": "hl5"}),
])

# Geräusche der Fallszene --------------------------------------------------------------------------------------
_fall = FOLIEN[0]["els"]
for e in _fall:
    if e.name.startswith("blase:denk") and e.cue == "messer":
        ton(e, "soft_expand", 0.8)
    if e.name == "bild:B_getroffen.png":
        ton(e, "cinematic_drop", 1.3)
    if e.name == "bild:B_boden.png":
        ton(e, "organic_drop", 1.0)
    if e.name.startswith("blase:sprech"):
        ton(e, "soft_select", 0.8)
    if e.name == "rueckblende":
        ton(e, "dreamy_expand", 0.8)
