"""Figuren für Folge 165 (Analogieverbot, Art. 103 Abs. 2 GG) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, ruhige Darstellung, keine Karikatur, keine Bärte, keine Prothesen-Posen, keine Polka Dots.
Wieland (WI, um 30, nimmt das Tretboot; Stimme niklas): standing/walking-1 (T-Shirt Türkis #7FD6D0, schwarze Hose, weiße
Schuhe), Kopf Short 3 (Haar #6B4A2E), Haut #EDC3A1; im Boot dieselbe Kleidung über sitting/mid-2 (Reihe -2: farbiges
Oberteil, schwarze Hose wie walking-1), Beine vom Bootsrumpf verdeckt.
Hartwin (HA, um 65, Eigentümer des Tretboots; Stimme helmut): standing/crossed_arms-2 (Pullover Schwarz, Hose Braun
#6B5640), Kopf No Hair 2, Brille Glasses 2, Haut #E6B796.
Posen nicht aus den letzten drei Folgen (162: easing-1, blazer-4, sitting/closed_legs-1; 163: easing-2, easing-1, walking-3,
robot_dance-2; 164: shirt-3, blazer-4); robot_dance-1 bleibt Lexi.
Präfix WI_/HA_ (nie ER_). Blickrichtung im Kontaktbild geprüft (besetzung_165.png): Grundansicht gespiegelt (blickt nach
links), Suffix _r ungespiegelt (blickt nach rechts).
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (WI_redet, HA_redet, HA_fragt, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_165")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
WI_F = {"Skin": "#EDC3A1", "Top": "#7FD6D0", "Hair": "#6B4A2E"}

P = {
    "WI": ("standing/walking-1", "Short 3", None, None, WI_F),
    "WB": ("sitting/mid-2", "Short 3", None, None, WI_F),          # Wieland im Tretboot
    "HA": ("standing/crossed_arms-2", "No Hair 2", None, "Glasses 2", {"Skin": "#E6B796", "Pants": "#6B5640"}),
}

LISTE = [
    ("WI_ruhig", "WI", "Calm", 0), ("WI_redet", "WI", "Smile", 1), ("WI_froh", "WI", "Smile Big|Smile", 0),
    ("WI_frech", "WI", "Cheeky|Smile", 0), ("WI_denkt", "WI", "Suspicious", 0), ("WI_sorge", "WI", "Concerned|Serious", 0),
    ("WB_froh", "WB", "Smile Big|Smile", 0), ("WB_ruhig", "WB", "Calm", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Serious", 1), ("HA_fragt", "HA", "Concerned|Serious", 1),
    ("HA_denkt", "HA", "Suspicious", 0), ("HA_ernst", "HA", "Solemn", 0), ("HA_sorge", "HA", "Concerned|Serious", 0),
    ("HA_muede", "HA", "Tired", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
