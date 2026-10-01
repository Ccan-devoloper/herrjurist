"""Figuren für Folge 001 (Raser-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Jonas: blazer-4, Max: shirt-4 (Szenenplan). Grundansicht blickt nach links (Figur rechts neben der Tafel),
Suffix _r blickt nach rechts. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e
(lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_rf")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "JO": ("standing/blazer-4", "Short 4", None, None, {"Skin": "#E8B98F", "Jacket": "#F07A6A", "Top": "#2E2E3A", "Pants": "#2E2E3A"}, 1),
    "MX": ("standing/shirt-4", "Flat Top", "Goatee 1", None, {"Skin": "#C99470", "Top": "#2E2E3A", "Pants": "#8DB3F2"}, 0),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JO_cool", "JO", "Cheeky", 0), ("JO_redet", "JO", "Suspicious", 1), ("JO_schock", "JO", "Fear", 0),
    ("JO_klagt", "JO", "Concerned", 1), ("JO_denkt", "JO", "Serious", 0), ("JO_muede", "JO", "Tired", 0),
    ("JO_stolz", "JO", "Smile Big", 0),
    ("MX_cool", "MX", "Calm", 0), ("MX_redet", "MX", "Smile", 1), ("MX_ernst", "MX", "Serious", 0),
    ("MX_denkt", "MX", "Concerned", 0),
]

n = 0
for name, p, mimik, mund in LISTE:
    pose, kopf, bart, brille, farben, sp = P[p]
    for suffix, gespiegelt in (("", sp), ("_r", 1 - sp)):
        figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
        if mund:
            for k, m in MUND.items():
                figur(pose, kopf, f"{mimik}|{m}", bart, brille, farben, hoehe=1200,
                      spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
# Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious"),
                            "LX_freut": ("standing/crossed_arms-1", "Cute")}.items():
    a = LX.AUSSEHEN
    for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
        figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
print(n, "Figurenbilder ->", ZIEL)
