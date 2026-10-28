"""Figuren für Folge 135 (Vertragsverletzungsverfahren) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Fiktive Personen.
Antonia (AN, um 24, Jurastudentin in der Lerngruppe): standing/blazer-4 (Blazer Lila #B8A9F5, Oberteil Weiß, schwarze Hose),
  Kopf Long, Brille Glasses 2, Haut #F0CDB4.
Konstantin (KO, um 25, Jurastudent): standing/crossed_arms-2 (schwarzes Oberteil, Hose Blau #8DB3F2), Kopf Short 3,
  Haut #B07552, ohne Bart und Brille.
Posen der letzten drei Folgen (131: blazer-3, crossed_arms-1, shirt-3; 132: robot_dance-3, easing-2, walking-3, shirt-2,
shirt-1; 133: resting-1, easing-1, blazer-2) nicht verwendet; keine Polka Dots, keine Prothesen-Posen. Keine Landwirte.
Alle Posen blicken im Original nach rechts; Suffix _r = Original (blickt nach rechts), ohne Suffix gespiegelt (blickt nach
links, zur Tafel). Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_135")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "AN": ("standing/blazer-4", "Long", None, "Glasses 2", {"Skin": "#F0CDB4", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}),
    "KO": ("standing/crossed_arms-2", "Short 3", None, None, {"Skin": "#B07552", "Pants": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("AN_ruhig", "AN", "Calm", 0), ("AN_redet", "AN", "Calm", 1), ("AN_denkt", "AN", "Suspicious", 0),
    ("AN_froh", "AN", "Smile", 0), ("AN_ernst", "AN", "Serious", 0), ("AN_staunt", "AN", "Awe", 0),
    ("KO_ruhig", "KO", "Calm", 0), ("KO_redet", "KO", "Driven", 1), ("KO_denkt", "KO", "Suspicious", 0),
    ("KO_froh", "KO", "Smile", 0), ("KO_staunt", "KO", "Awe", 0), ("KO_ernst", "KO", "Serious", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
