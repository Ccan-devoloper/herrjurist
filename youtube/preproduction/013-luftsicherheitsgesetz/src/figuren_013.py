"""Figuren für Folge 013 (Luftsicherheitsgesetz) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Verteidigungsminister Lorenz: standing/blazer-3, Pilotin: Brustbild body/Sporty Tee (im Funkbild), Vielflieger Herr Seiler:
standing/resting-2 (Szenenplan). Die Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Alle Grundmimiken mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als „Augen|Serious/Smile“.
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_013")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "LO": ("standing/blazer-3", "Gray Short", None, "Glasses 4", {"Skin": "#E6B48F", "Jacket": "#8DB3F2", "Pants": "#3D3D58"}, 1),
    "PI": ("body/Sporty Tee", "Bun", None, None, {"Skin": "#8D5A3B", "Top": "#8FD694"}, 1),
    "SE": ("standing/resting-2", "Short 4", None, "Glasses 2", {"Skin": "#C58E64", "Pants": "#B8A9F5"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("LO_ruhig", "LO", "Calm", 0), ("LO_redet", "LO", "Serious", 1), ("LO_denkt", "LO", "Solemn", 0),
    ("LO_sorge", "LO", "Concerned|Serious", 0),
    ("PI_ruhig", "PI", "Calm", 0), ("PI_redet", "PI", "Serious", 1),
    ("SE_ruhig", "SE", "Calm", 0), ("SE_redet", "SE", "Driven", 1), ("SE_sorge", "SE", "Concerned|Serious", 0),
    ("SE_froh", "SE", "Smile", 0), ("SE_denkt", "SE", "Suspicious", 0),
]

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
