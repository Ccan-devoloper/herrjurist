"""Figuren für Folge 137 (Urkunde § 267 StGB, gefälschte Entschuldigung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Femke (FE, 16, Schülerin): standing/easing-2 (offenes grünes Hemd #8FD694 über schwarzem Shirt, Hose Blau #8DB3F2,
  Sneaker), Kopf Buns (zwei Dutts, jugendlich), Haar #3B2A20, Haut #F0C29E; im Bild etwa 90 % der Erwachsenenhöhe
  (Jugendliche, FOLGE-ABLAUF Abschnitt 3); respektvoll, keine Karikatur.
Frau Melzer (ME, um 58, Klassenlehrerin): standing/shirt-3 (lila Bluse #B8A9F5, schwarze Hose), Kopf Gray Medium,
  Haar #B9B9C2, Brille Glasses 4, Haut #EDC3A3.
Mutter (MU, um 45, spricht nicht): standing/resting-2 (schwarzes Oberteil, Hose Rot #F07A6A), Kopf Medium 2, Haar #3B2A20,
  Haut #F0C29E.
Posen der letzten drei Folgen (134: shirt-4, blazer-4, crossed_arms-2; 135: blazer-4, crossed_arms-2; 136: blazer-3,
robot_dance-2, pointing_finger-1) nicht verwendet; keine Polka Dots, keine Prothesen-Posen, keine Bärte. Präfixe FE_/ME_/MU_.
Alle drei Posen blicken im Original nach rechts (Kontaktbild geprüft): ohne Suffix gespiegelt (blickt nach links, zur
Tafel), Suffix _r = Original (blickt nach rechts). Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich
a/o/e (Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_137")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "FE": ("standing/easing-2", "Buns", None, None, {"Skin": "#F0C29E", "Jacket": "#8FD694", "Pants": "#8DB3F2", "Hair": "#3B2A20"}),
    "ME": ("standing/shirt-3", "Gray Medium", None, "Glasses 4", {"Skin": "#EDC3A3", "Top": "#B8A9F5", "Hair": "#B9B9C2"}),
    "MU": ("standing/resting-2", "Medium 2", None, None, {"Skin": "#F0C29E", "Pants": "#F07A6A", "Hair": "#3B2A20"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FE_ruhig", "FE", "Calm", 0), ("FE_redet", "FE", "Calm", 1), ("FE_froh", "FE", "Smile", 0),
    ("FE_denkt", "FE", "Suspicious", 0), ("FE_ernst", "FE", "Serious", 0), ("FE_sorge", "FE", "Concerned|Serious", 0),
    ("FE_eifrig", "FE", "Driven", 0), ("FE_still", "FE", "Solemn", 0),
    ("ME_ruhig", "ME", "Calm", 0), ("ME_redet", "ME", "Smile", 1), ("ME_froh", "ME", "Smile", 0),
    ("ME_ernst", "ME", "Serious", 0), ("ME_denkt", "ME", "Suspicious", 0),
    ("MU_ruhig", "MU", "Calm", 0), ("MU_froh", "MU", "Smile", 0), ("MU_denkt", "MU", "Suspicious", 0),
    ("MU_ernst", "MU", "Serious", 0),
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
