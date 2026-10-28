"""Figuren für Folge 127 (Costa/ENEL, Anwendungsvorrang) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Übungsfall mit fiktiven Personen; Herr Costa (echter Verfahrensbeteiligter) erscheint nicht als Figur, nur namentlich.
Hedwig (um 40, Inhaberin einer kleinen Limonadenmanufaktur): standing/blazer-2 (Blazer Grün #8FD694, Oberteil Weiß,
  Prothese aus der Originalpose), Kopf Long Curly, Haut #EBC3A0.
Herr Lammert (um 55, Lebensmittelüberwachung): standing/crossed_arms-2 (schwarzes Oberteil, Hose Marine #3B4A6B), Kopf
  No Hair 1, Brille Glasses 2, Haut #E2B48E, ohne Bart.
Posen der letzten Folgen (124: walking-2, shirt-4, bike; 125: easing-2, crossed_arms-1; 126: blazer-1, shirt-3, walking-1,
blazer-4, resting-1) nicht verwendet; keine Polka Dots. Alle Posen blicken im Original nach rechts; Suffix _r = Original
(blickt nach rechts), ohne Suffix gespiegelt (blickt nach links, zur Tafel).
Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_127")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HE": ("standing/blazer-2", "Long Curly", None, None, {"Skin": "#EBC3A0", "Jacket": "#8FD694", "Top": "#FFFFFF"}),
    "LA": ("standing/crossed_arms-2", "No Hair 1", None, "Glasses 2", {"Skin": "#E2B48E", "Pants": "#3B4A6B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_froh", "HE", "Smile", 0), ("HE_redet", "HE", "Concerned|Serious", 1),
    ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_denkt", "HE", "Suspicious", 0), ("HE_staunt", "HE", "Awe", 0),
    ("LA_ruhig", "LA", "Calm", 0), ("LA_redet", "LA", "Serious", 1), ("LA_ernst", "LA", "Serious", 0),
    ("LA_denkt", "LA", "Suspicious", 0), ("LA_still", "LA", "Solemn", 0), ("LA_staunt", "LA", "Awe", 0),
    ("LA_freundlich", "LA", "Smile", 0),
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
