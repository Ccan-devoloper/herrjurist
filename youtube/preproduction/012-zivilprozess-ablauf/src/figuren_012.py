"""Figuren für Folge 012 (Zivilprozess Ablauf, Klavierkauf) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Frau Seidel (Klägerin, um 65): pointing_finger-1, Herr Krüger (Beklagter, um 28): shirt-4, Richterin (um 45): blazer-3
(dunkles Kostüm, robenähnlich), Gerichtsvollzieher (um 50): walking-2. Alle Posen blicken im Original nach rechts; die
Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Driven, Fear, Contempt, Suspicious, Tired.
Sprechende Ansichten zusätzlich mit a/o/e (Augen der Grundmimik + Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 %)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_012")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "SE": ("standing/pointing_finger-1", "Gray Bun", None, "Glasses 2", {"Skin": "#F0C8A8"}, 1),
    "KR": ("standing/shirt-4", "Short 4", None, None, {"Skin": "#D9A07A", "Pants": "#8DB3F2"}, 1),
    "RI": ("standing/blazer-3", "Medium Bangs", None, None, {"Skin": "#B07552", "Jacket": "#3A3A48", "Pants": "#3A3A48"}, 1),
    "GV": ("standing/walking-2", "Short 5", "Moustache 6", None, {"Skin": "#E0AC84", "Pants": "#7FD6D0"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen)
LISTE = [
    ("SE_ruhig", "SE", "Calm", 0), ("SE_redet", "SE", "Driven", 1), ("SE_aerger", "SE", "Contempt", 0),
    ("SE_froh", "SE", "Smile", 0), ("SE_sorge", "SE", "Concerned|Serious", 0), ("SE_denkt", "SE", "Serious", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_redet", "KR", "Suspicious", 1), ("KR_trotz", "KR", "Contempt", 0),
    ("KR_schreck", "KR", "Fear", 0), ("KR_denkt", "KR", "Serious", 0), ("KR_muede", "KR", "Tired", 0),
    ("KR_froh", "KR", "Smile", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1),
    ("GV_ruhig", "GV", "Calm", 0), ("GV_redet", "GV", "Serious", 1),
]

if __name__ == "__main__":
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben, sp = P[p]
        for suffix, gespiegelt in (("", sp), ("_r", 1 - sp)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
