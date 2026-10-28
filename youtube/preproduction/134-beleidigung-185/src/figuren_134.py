"""Figuren für Folge 134 (Beleidigung, üble Nachrede, Verleumdung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Fiktive Nachbarn aus der Chatgruppe „Nachbarn Ahornweg“:
Henner (HE, um 45, der Betroffene): standing/shirt-4 (schwarzes Hemd, Hose Blau #8DB3F2), Kopf Short 3, Haut #E3B48C,
  ohne Bart und Brille.
Hannelore (HA, um 65, schreibt „Idiot“): standing/blazer-4 (Blazer Grün #8FD694, Oberteil Weiß), Kopf Gray Bun,
  Brille Glasses 2, Haut #F0C8A8.
Dörte (DO, um 35, behauptet die Tatsache): standing/crossed_arms-2 (schwarzes Oberteil, Hose Lila #B8A9F5), Kopf
  Medium Bangs, Haut #D9A07A.
Posen der letzten drei Folgen (131: blazer-3, crossed_arms-1, shirt-3; 132/133: blazer-1, blazer-2, easing-1, easing-2,
resting-1, robot_dance-3, shirt-1, shirt-2, walking-3) nicht verwendet; keine Polka Dots, keine Prothesen-Posen, keine
Karikatur (sachliche Mimik, keine „fiese“ Figur). Präfixe HE_/HA_/DO_ (nie ER_).
Alle Posen blicken im Original nach rechts; Suffix _r = Original (blickt nach rechts), ohne Suffix gespiegelt (blickt nach
links, zur Tafel). Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_134")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HE": ("standing/shirt-4", "Short 3", None, None, {"Skin": "#E3B48C", "Pants": "#8DB3F2", "Hair": "#3B2A20"}),
    "HA": ("standing/blazer-4", "Gray Bun", None, "Glasses 2", {"Skin": "#F0C8A8", "Jacket": "#8FD694", "Top": "#FFFFFF",
                                                               "Hair": "#B9B9C2"}),
    "DO": ("standing/crossed_arms-2", "Medium Bangs", None, None, {"Skin": "#D9A07A", "Pants": "#B8A9F5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Serious", 1), ("HE_ernst", "HE", "Serious", 0),
    ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_still", "HE", "Solemn", 0), ("HE_staunt", "HE", "Awe", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Driven", 1), ("HA_entschlossen", "HA", "Driven", 0),
    ("HA_denkt", "HA", "Suspicious", 0), ("HA_ernst", "HA", "Serious", 0), ("HA_still", "HA", "Solemn", 0),
    ("DO_ruhig", "DO", "Calm", 0), ("DO_redet", "DO", "Concerned|Serious", 1), ("DO_sorge", "DO", "Concerned|Serious", 0),
    ("DO_denkt", "DO", "Suspicious", 0), ("DO_ernst", "DO", "Serious", 0), ("DO_still", "DO", "Solemn", 0),
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
