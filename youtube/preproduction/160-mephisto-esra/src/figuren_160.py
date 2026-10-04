"""Figuren für Folge 160 (Mephisto-Beschluss) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv;
reale Personen (Klaus Mann, Gustaf Gründgens, Hendrik Höfgen als Romanfigur, Autor und Klägerinnen im Esra-Fall) werden
NICHT dargestellt.
Liesel (LI, um 33, Autorin; Stimme lucy): standing/crossed_arms-1 (Oberteil Rot #F07A6A, schwarze Hose), Kopf
Medium Straight, Haut #EDC3A3, keine Brille.
Winfried (WI, um 36, ihr früherer Partner, sitzt im Publikum; Stimme stephan): sitting/closed_legs-2 (Jackett Blau
#8DB3F2, Hose Grau #6B6B78), Kopf Short 1, Haut #E2B48E, kein Bart. Er sitzt in jeder Szene auf demselben Stuhl.
Frau Hollerbach (HO, um 65, Buchhändlerin; Stimme hilde): standing/resting-1 (Oberteil Grün #8FD694), Kopf Gray Short,
Brille Glasses 2, Haut #F0C8A8.
Posen nicht aus 155–158 (blazer-4, walking-3, hands_back-1, easing-2, shirt-3, walking-2, robot_dance-2,
pointing_finger-2, resting-2, walking-1, shirt-4, easing-1) und nicht 154 (crossed_arms-2, blazer-3); keine Polka Dots,
keine Bärte, keine Prothesen-Posen.
Präfix LI_/WI_/HO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (LI_redet, WI_redet, HO_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_160")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "LI": ("standing/crossed_arms-1", "Medium Straight", None, None, {"Skin": "#EDC3A3", "Top": "#F07A6A"}),
    "WI": ("sitting/closed_legs-2", "Short 1", None, None, {"Skin": "#E2B48E", "Jacket": "#8DB3F2", "Pants": "#6B6B78"}),
    "HO": ("standing/resting-1", "Gray Short", None, "Glasses 2", {"Skin": "#F0C8A8", "Top": "#8FD694"}),
}

LISTE = [
    ("LI_ruhig", "LI", "Smile", 0), ("LI_redet", "LI", "Serious", 1), ("LI_denkt", "LI", "Suspicious", 0),
    ("LI_froh", "LI", "Cute", 0), ("LI_sorge", "LI", "Concerned|Serious", 0),
    ("WI_ruhig", "WI", "Smile", 0), ("WI_redet", "WI", "Concerned|Serious", 1), ("WI_denkt", "WI", "Suspicious", 0),
    ("WI_aerger", "WI", "Rage|Serious", 0), ("WI_froh", "WI", "Cute", 0), ("WI_ernst", "WI", "Serious", 0),
    ("HO_ruhig", "HO", "Smile", 0), ("HO_redet", "HO", "Smile", 1), ("HO_froh", "HO", "Cute", 0),
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
