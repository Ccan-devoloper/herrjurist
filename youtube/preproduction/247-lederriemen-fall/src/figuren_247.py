"""Figuren für Folge 247 (Lederriemen-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Namen fiktiv (echter Fall,
vereinfacht und mit anderen Namen erzählt). Das Opfer erscheint nicht als Figur (FOLGE-ABLAUF Abschnitt 1).
Willi (WI, schlägt den Riemen vor; Stimme william): standing/easing-1 (Jacke Camel #C98B4E, Shirt Creme #F2E3C6, schwarze Hose
  der Pose), Kopf Short 3, Haut #E6B794, keine Brille, kein Bart – neutral, keine Karikatur.
Hans (HA, rät zum Sandsack; Stimme marc): standing/walking-1 (Pullover Oliv #7A8B4A, schwarze Hose der Pose), Kopf Short 1,
  Haut #D9A47E, keine Brille, kein Bart – neutral, keine Karikatur.
Posen nicht aus 244–246 (robot_dance-2/-3, crossed_arms-1/-2, resting-1/-2, polka_dots, walking-3, shirt-3/-4, blazer-4); keine
Prothesen-Posen (shirt-1, shirt-2, blazer-1, blazer-2), keine Polka Dots, keine Bärte, keine fiesen Mimiken. Präfix WI_/HA_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (WI_redet, HA_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_247")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "WI": ("standing/easing-1", "Short 3", None, None, {"Skin": "#E6B794", "Jacket": "#C98B4E", "Top": "#F2E3C6"}),
    "HA": ("standing/walking-1", "Short 1", None, None, {"Skin": "#D9A47E", "Top": "#7A8B4A"}),
}

LISTE = [
    ("WI_ruhig", "WI", "Calm", 0), ("WI_ernst", "WI", "Serious", 0), ("WI_denkt", "WI", "Suspicious", 0),
    ("WI_sorge", "WI", "Concerned|Serious", 0), ("WI_angst", "WI", "Fear", 0), ("WI_muede", "WI", "Tired", 0),
    ("WI_feierlich", "WI", "Solemn", 0), ("WI_staunt", "WI", "Awe", 0),
    ("WI_redet", "WI", "Serious", 1),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_ernst", "HA", "Serious", 0), ("HA_denkt", "HA", "Suspicious", 0),
    ("HA_sorge", "HA", "Concerned|Serious", 0), ("HA_angst", "HA", "Fear", 0), ("HA_muede", "HA", "Tired", 0),
    ("HA_feierlich", "HA", "Solemn", 0), ("HA_staunt", "HA", "Awe", 0),
    ("HA_redet", "HA", "Concerned|Serious", 1),
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
