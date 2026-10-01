"""Figuren für Folge 003 (Gutachtenstil, Flohmarkt-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Greta: easing-1, Paul: resting-1 / walking-1 / sitting-bike (gleiche -1-Reihe, grünes Oberteil, schwarze Hose),
Mia: blazer-3 (Szenenplan). Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_003")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

GR_F = {"Skin": "#F2C9A6", "Top": "#B8A9F5"}
PA_F = {"Skin": "#B07552", "Top": "#8FD694", "Jacket": "#8FD694", "Bicycle Frame": "#3A3A44"}
MI_F = {"Skin": "#E8B98F", "Jacket": "#F07A6A"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "GR": ("standing/easing-1", "Gray Bun", None, "Glasses 2", GR_F, 1),
    "PA": ("standing/resting-1", "Short 2", "Full", None, PA_F, 1),
    "PA_GEHT": ("standing/walking-1", "Short 2", "Full", None, PA_F, 1),
    "PA_RAD": ("sitting/bike", "Short 2", "Full", None, PA_F, 1),
    "MI": ("standing/blazer-3", "Medium Bangs", None, None, MI_F, 1),
}
SPIEGEL = {k: int(os.environ.get("SP_" + k, v[5])) for k, v in P.items()}

# (Name, Pose, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r
LISTE = [
    ("GR_ruhig", "GR", "Calm", 0), ("GR_redet", "GR", "Smile", 1), ("GR_zufrieden", "GR", "Smile Big", 0),
    ("GR_aerger", "GR", "Contempt", 0), ("GR_fordert", "GR", "Serious", 0),
    ("PA_ruhig", "PA", "Calm", 0), ("PA_redet", "PA", "Cheeky", 1), ("PA_ertappt", "PA", "Suspicious", 0),
    ("PA_denkt", "PA", "Serious", 0), ("PA_geht", "PA_GEHT", "Calm", 0), ("PA_rad", "PA_RAD", "Smile Big", 0),
    ("MI_ruhig", "MI", "Calm", 0), ("MI_fragt", "MI", "Concerned", 1), ("MI_redet", "MI", "Smile", 1),
    ("MI_ertappt", "MI", "Fear", 0), ("MI_denkt", "MI", "Serious", 0), ("MI_froh", "MI", "Smile Big", 0),
]

n = 0
for name, p, mimik, mund in LISTE:
    pose, kopf, bart, brille, farben, _ = P[p]
    sp = SPIEGEL[p]
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
