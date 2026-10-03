"""Figuren für Folge 094 (Sirius-Fall, mittelbare Täterschaft bei Täuschung über den Tod) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Fiktiver Fall; keine realen Personen nachgebildet (die Beteiligten aus BGHSt 32, 38 erscheinen nicht),
keine Karikaturen, keine bösen Mimiken (kein Contempt, kein Angry), keine Verspottung der Getäuschten, keine Bärte.
Hartwig (um 55, nennt sich spiritueller Lehrer): standing/robot_dance-2 (schwarzer Pullover, Hose Lila #B8A9F5),
  Kopf Gray Short (Haar grau #B5B5B5), Brille Glasses 2, Haut #E2B08C.
Wilma (Mitte 30): standing/polka_dots (Oberteil mit Punkten, Hose Grün #8FD694), Kopf Long Curly, Haut #F0C8A8.
Benedikt (um 30, ihr Bruder): standing/blazer-3 (Jacke Blau #8DB3F2, Hose #3B3B4F), Kopf Short 3, Haut #B07552.
Posen der letzten drei Folgen (090–092: easing-1/-2, shirt-3, walking-2, robot_dance-3, shirt-4, walking-1, resting-1/-2,
crossed_arms-1) nicht verwendet; Polka Dots zuletzt in 087. Alle Posen blicken im Original nach rechts; Suffix _r = Original
(blickt nach rechts), ohne Suffix gespiegelt (blickt nach links, zur Tafel).
Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_094")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HW": ("standing/robot_dance-2", "Gray Short", None, "Glasses 2", {"Skin": "#E2B08C", "Pants": "#B8A9F5", "Hair": "#B5B5B5"}),
    "WI": ("standing/polka_dots", "Long Curly", None, None, {"Skin": "#F0C8A8", "Pants": "#8FD694"}),
    "BE": ("standing/blazer-3", "Short 3", None, None, {"Skin": "#B07552", "Jacket": "#8DB3F2", "Pants": "#3B3B4F"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HW_ruhig", "HW", "Calm", 0), ("HW_redet", "HW", "Smile", 1), ("HW_ernst", "HW", "Serious", 0),
    ("HW_still", "HW", "Solemn", 0),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_vertraut", "WI", "Smile", 0), ("WI_redet", "WI", "Calm", 1),
    ("WI_ernst", "WI", "Serious", 0), ("WI_still", "WI", "Solemn", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Concerned|Serious", 1), ("BE_sorge", "BE", "Concerned|Serious", 0),
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
