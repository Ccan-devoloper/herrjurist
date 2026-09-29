"""Folien des Reels 081 (1080 × 1920) im Stil von v2."""
import engine
engine.W, engine.H = 1080, 1920
from engine import *
ZELLE = (255, 255, 255, 150)
ORANGE = (240, 128, 60, 255)

def ok(x, y, cue, size=58, d=0.0):
    return E("check-mark-button", x, y, size, cue, d=d)

def nein(x, y, cue, size=58, d=0.0):
    return E("cross-mark", x, y, size, cue, d=d)

FOLIEN = []
def folie(bg, pfade, els):
    FOLIEN.append(dict(bg=bg, pfade=pfade, els=els))

# 1 Hook
folie("hell", [("hook", "Erlaubnistatbestandsirrtum")], [
    T("Notwehr gegen", 540, 500, "hook", "ExtraBold", 116, anker="m"),
    T("einen Angriff,", 540, 635, "hook", "ExtraBold", 116, anker="m", d=0.25),
    T("den es nie gab?", 540, 770, "hook", "ExtraBold", 116, anker="m", d=0.5),
    E("thinking-face", 540, 1130, 300, "hook", d=0.8),
])

# 2 Fall
folie("hell", [("fall", "Fall")], [
    T("Nachts am Bahnhof", 540, 150, "fall", "ExtraBold", 92, anker="m"),
    E("crescent-moon", 400, 330, 110, "fall", d=0.2),
    E("station", 680, 330, 110, "fall", d=0.35),
    E("person-standing", 290, 1060, 360, "fall", d=0.5),
    T("A", 290, 1255, "fall", "ExtraBold", 96, anker="m", d=0.6),
    E("person-running", 790, 1060, 360, "b"),
    T("B", 790, 1255, "b", "ExtraBold", 96, anker="m", d=0.15),
    E("coat", 975, 900, 100, "tasche"),
    T("greift in die Tasche", 790, 1375, "tasche", "Regular", 50, anker="m", d=0.1),
    wolke(330, 200, "Messer!", "messer", 300, 650, schwanz=(-20, 1), emoji="kitchen-knife", emoji_size=90, textsize=52),
    E("oncoming-fist", 545, 1010, 150, "faust"),
    E("collision", 650, 890, 110, "faust", d=0.25),
    wolke(340, 200, "Ihr Handy!", "handy", 790, 650, schwanz=(-20, 1), emoji="mobile-phone", emoji_size=90, textsize=52),
])

# 3 Notwehr?
folie("hell", [("nw", "II. Rechtswidrigkeit › Notwehr")], [
    T("Notwehr?", 540, 190, "nw", "ExtraBold", 124, anker="m"),
    E("mobile-phone", 170, 480, 110, "kein"),
    T("Wirklichkeit:", 250, 425, "kein", "Bold", 60),
    T("kein Angriff", 250, 497, "kein", "Regular", 60),
    nein(910, 480, "kein", size=86, d=0.3),
    E("kitchen-knife", 170, 700, 110, "vorst"),
    T("Vorstellung:", 250, 645, "vorst", "Bold", 60),
    T("Angriff", 250, 717, "vorst", "Regular", 60),
    ok(910, 700, "vorst", size=86, d=0.3),
    block(90, 880, 900, 330, (255, 244, 225, 235), None, "etbi", rund=22, rand=ORANGE, randbreite=7, anim="pop",
          zeilen=[("Erlaubnistatbestands-", "ExtraBold", 72, INK), ("irrtum", "ExtraBold", 72, INK),
                  ("Irrtum über rechtfertigende Tatsachen", "Regular", 44, GRAU)]),
])

# 4 Streit
folie("hell", [("streit", "III. Schuld › Streitstand")], [
    E("warning", 540, 250, 140, "streit"),
    T("Keine gesetzliche", 540, 350, "streit", "ExtraBold", 90, anker="m", d=0.15),
    T("Regelung", 540, 450, "streit", "ExtraBold", 90, anker="m", d=0.3),
    block(90, 600, 900, 260, ZELLE, None, "sst", rund=20, rand=INK, randbreite=3,
          zeilen=[("Strenge Schuldtheorie", "Bold", 60, INK), ("§ 17 StGB → nur Strafmilderung", "Regular", 48, GRAU),
                  ("(bei vermeidbarem Irrtum)", "Regular", 40, GRAU)]),
    block(90, 910, 900, 240, ZELLE, None, "hm", rund=20, rand=GRUEN, randbreite=6,
          zeilen=[("Herrschende Meinung", "Bold", 60, INK), ("§ 16 I 1 StGB analog", "Regular", 52, GRAU)]),
    ok(200, 1262, "vs", size=84),
    T("Vorsatzschuld entfällt", 265, 1228, "vs", "ExtraBold", 68),
])

# 5 Ergebnis
folie("hell", [("erg", "Ergebnis")], [
    T("Strafbarkeit des A", 540, 190, "erg", "ExtraBold", 96, anker="m"),
    nein(150, 442, "erg", size=84, d=0.3),
    T("§ 223 StGB", 220, 400, "erg", "ExtraBold", 80, d=0.3),
    T("Vorsatzschuld (-)", 220, 502, "erg", "Regular", 58, farbe=GRAU, d=0.5),
    E("eyes", 150, 742, 84, "fahr"),
    T("§ 229 StGB", 220, 700, "fahr", "ExtraBold", 80),
    T("wenn Irrtum vermeidbar", 220, 802, "fahr", "Regular", 58, farbe=GRAU, d=0.3),
    T("→ fahrlässige", 220, 895, "fahr", "Bold", 62, d=0.7),
    T("Körperverletzung", 265, 970, "fahr", "Bold", 62, d=0.7),
])

# 6 Merksatz
folie("dunkel", [("merke", "Merksatz")], [
    kreis_emoji("light-bulb", 540, 420, 130, "merke"),
    T("Merke", 540, 600, "merke", "Bold", 104, farbe=WEISS, anker="m", d=0.2),
    *richtext([[("Irrtum über ", 0), ("Tatsachen", "a")], [("→ § 16 I 1 analog", 0)]], 540, 780, 66, "merke", {"a": "hl1"}, d=0.3),
    *richtext([[("Irrtum über ", 0), ("Recht", "b")], [("→ § 17 StGB", 0)]], 540, 1050, 66, "m2", {"b": "hl2"}),
])
