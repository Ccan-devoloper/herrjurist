"""Testfolien: Open-Peeps-Figuren (CC0, via react-peeps) statt Personen-Emojis."""
from engine import *
from folien import ok, nein

PP = "../../peeps/svg/"
FOLIEN = []
def folie(bg, pfade, els):
    FOLIEN.append(dict(bg=bg, pfade=pfade, els=els))

AX, BX, UNTEN, HF = 540, 1330, 760, 460
# Fall: Gesichter/Posen wechseln wortgenau; Wechsel als harter Schnitt, die Figur bleibt stehen
folie("hell", [("fall", "Fall")], [
    T("Nachts am Bahnhof", 960, 40, "fall", "ExtraBold", 96, anker="m"),
    E("crescent-moon", 455, 92, 105, "fall", d=0.15),
    E("station", 1465, 92, 105, "fall", d=0.3),
    bild(PP + "A_ruhig.png", AX, UNTEN, HF, "a", bis="messer"),
    bild(PP + "A_angst.png", AX, UNTEN, HF, "messer", anim="cut", bis="faust"),
    bild(PP + "A_wut.png", AX, UNTEN, HF, "faust", anim="cut", bis="handy"),
    bild(PP + "A_schreck.png", AX, UNTEN, HF, "handy", anim="cut"),
    T("A", AX, 772, "a", "ExtraBold", 72, anker="m", d=0.15),
    bild(PP + "B_laeuft.png", BX, UNTEN, HF, "b", bis="nase"),
    bild(PP + "B_verletzt.png", BX, UNTEN, HF, "nase", anim="cut", bis="handy"),
    bild(PP + "B_zeigt.png", BX + 40, UNTEN, int(HF * 872 / 953), "handy", anim="cut"),
    T("B", BX, 772, "b", "ExtraBold", 72, anker="m", d=0.15),
    E("coat", 1575, 560, 100, "tasche"),
    T("greift in die Jackentasche", BX, 860, "tasche", "Regular", 44, anker="m", d=0.1),
    wolke(330, 190, "Messer!", "messer", 230, 200, ziel=(500, 330), emoji="kitchen-knife", emoji_size=95, textsize=50),
    E("oncoming-fist", 930, 520, 150, "faust"),
    E("collision", 1110, 420, 110, "faust", d=0.25),
    E("face-with-head-bandage", 1135, 941, 60, "nase"),
    T("Nase gebrochen", 1178, 915, "nase", "Regular", 44),
    wolke(340, 190, "Ihr Handy!", "handy", 1690, 240, ziel=(1400, 335), emoji="mobile-phone", emoji_size=95, textsize=50),
    E("eyes", 330, 886, 60, "licht"),
    T("hätte das Handy sehen können", 370, 860, "licht", "Regular", 44),
    T("Wie hat sich A strafbar gemacht?", 960, 985, "frage", "ExtraBold", 60, anker="m"),
])

# Zwei Irrtümer: Figur statt Ninja-Emoji
folie("hell", [("irrtum", "Exkurs › Irrtümer im StGB")], [
    bild(PP + "T_verwirrt.png", 470, 680, 300, "irrtum", oben=0.42),
    bild(PP + "T_denkt.png", 1450, 680, 300, "irrtum", d=0.2, oben=0.42),
    wolke(440, 200, ["Irrtum über", "Sachverhalt"], "tbi", 430, 150, ziel=(492, 400), textsize=52),
    T("Tatbestandsirrtum", 470, 705, "tbi", "ExtraBold", 78, anker="m", d=0.2),
    T("(§ 16 Abs. 1 StGB)", 470, 800, "tbi", "Regular", 58, anker="m", d=0.3),
    T("→ Vorsatz entfällt", 470, 905, "tbifolge", "Bold", 54, anker="m"),
    wolke(540, 200, ["Irrtum über rechtliche", "Bewertung"], "vi", 1390, 150, ziel=(1472, 400), textsize=52),
    T("Verbotsirrtum", 1450, 705, "vi", "ExtraBold", 78, anker="m", d=0.2),
    T("(§ 17 StGB)", 1450, 800, "vi", "Regular", 58, anker="m", d=0.3),
    T("→ ohne Schuld nur, wenn unvermeidbar", 1450, 905, "vifolge", "Bold", 50, anker="m"),
])
