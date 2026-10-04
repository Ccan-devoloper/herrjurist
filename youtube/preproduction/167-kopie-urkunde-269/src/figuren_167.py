"""Figuren für Folge 167 (Kopie als Urkunde, Scan/PDF, § 269 StGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Janosch (JA, 20, Bewerber): standing/resting-1 (Pullover Rot #F07A6A, schwarze Hose, Sneaker), Kopf Short 1,
  Haar #5A3A22, Haut #E8B990; gewöhnlicher junger Erwachsener, keine Karikatur, keine „fiese“ Täterfigur.
Frau Hagemann (HA, um 45, Personalabteilung): standing/blazer-1 (Blazer Lila #B8A9F5, Hose Dunkelgrau #3A3A44),
  Kopf Long, Haar #3B2A20, Brille Glasses 2, Haut #D9A47E.
Posen der letzten drei Folgen (162: easing-1, blazer-4, closed_legs-1; 163: easing-2, easing-1, walking-3, robot_dance-2;
164: shirt-3, blazer-4) nicht verwendet; keine Polka Dots, keine Prothesen-Posen, keine Bärte. Präfixe JA_/HA_.
Blickrichtung im Original laut Kontaktbild: ohne Suffix gespiegelt (blickt nach links, zur Tafel), Suffix _r = Original
(blickt nach rechts). Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_167")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "JA": ("standing/resting-1", "Short 1", None, None, {"Skin": "#E8B990", "Top": "#F07A6A", "Hair": "#5A3A22"}),
    "HA": ("standing/blazer-1", "Long", None, "Glasses 2", {"Skin": "#D9A47E", "Jacket": "#B8A9F5", "Pants": "#3A3A44",
                                                            "Hair": "#3B2A20"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JA_ruhig", "JA", "Calm", 0), ("JA_redet", "JA", "Smile", 1), ("JA_froh", "JA", "Smile", 0),
    ("JA_denkt", "JA", "Suspicious", 0), ("JA_ernst", "JA", "Serious", 0), ("JA_sorge", "JA", "Concerned|Serious", 0),
    ("JA_eifrig", "JA", "Driven", 0), ("JA_still", "JA", "Solemn", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Smile", 1), ("HA_froh", "HA", "Smile", 0),
    ("HA_ernst", "HA", "Serious", 0), ("HA_denkt", "HA", "Suspicious", 0),
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
