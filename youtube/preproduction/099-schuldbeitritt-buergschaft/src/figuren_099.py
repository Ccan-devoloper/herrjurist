"""Figuren für Folge 099 (Schuldbeitritt, Schuldübernahme oder Bürgschaft?) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Jochen (um 35, Kreditnehmer, Hauptschuldner): standing/shirt-4 (schwarzes Hemd, blaue Hose), Kopf Short 5, kein Bart.
Katja (um 32, Freundin von Jochen, Erklärende): standing/walking-3 (schwarzes T-Shirt, schwarze Hose, Schrittpose), Kopf Long
(schwarzes Haar).
Frau Zöllner (um 60, Mitarbeiterin der Bank, Gläubigerseite): standing/blazer-1 (blauer Blazer, dunkle Hose, Beinprothese),
Kopf Gray Bun, Brille Glasses 4.
Keine Bärte, keine Karikatur, keine Klischees; die Prothesen-Pose trägt die sachliche Bankmitarbeiterin, keine Täterrolle.
Posen nicht aus den Folgen 096–098 (resting-1, easing-1, blazer-4, crossed_arms-1, pointing_finger-2, walking-1); keine Polka Dots.
Präfix JO_/KA_/ZO_ (nie ER_). Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md); sprechende Ansichten JO_redet, KA_redet, ZO_redet und Lexi
zusätzlich mit a/o/e (Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_099")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

JO_F = {"Skin": "#E8B998", "Pants": "#8DB3F2"}
KA_F = {"Skin": "#D9A27C"}
ZO_F = {"Skin": "#F2C9A5", "Jacket": "#5B7DB8", "Pants": "#3D4A7A"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "JO": ("standing/shirt-4", "Short 5", None, None, JO_F),
    "KA": ("standing/walking-3", "Long", None, None, KA_F),
    "ZO": ("standing/blazer-1", "Gray Bun", None, "Glasses 4", ZO_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JO_ruhig", "JO", "Calm", 0), ("JO_redet", "JO", "Serious", 1), ("JO_froh", "JO", "Smile Big|Smile", 0),
    ("JO_sorge", "JO", "Concerned|Serious", 0), ("JO_denkt", "JO", "Suspicious", 0),
    ("KA_ruhig", "KA", "Calm", 0), ("KA_redet", "KA", "Serious", 1), ("KA_froh", "KA", "Smile Big|Smile", 0),
    ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_denkt", "KA", "Suspicious", 0), ("KA_staunt", "KA", "Awe", 0),
    ("ZO_ruhig", "ZO", "Calm", 0), ("ZO_redet", "ZO", "Serious", 1), ("ZO_froh", "ZO", "Smile Big|Smile", 0),
    ("ZO_denkt", "ZO", "Suspicious", 0), ("ZO_sorge", "ZO", "Concerned|Serious", 0),
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
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
