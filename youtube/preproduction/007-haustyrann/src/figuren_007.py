"""Figuren für Folge 007 (Haustyrannen-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Nadine: resting-1 (gehend: walking-1, gleiche Reihe -1 = gleiches Outfit), Ralf: pointing_finger-1 (Drohgeste, Stiefel),
Beraterin: robot_dance-3 (einladende offene Hand). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt
und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund ("Augen|Mund" bei Mimiken mit offenem Mund). Je sprechender Ansicht vier
Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_007")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

NA_F = {"Skin": "#E3B38E", "Top": "#B8A9F5", "Pants": "#3D3D58"}
# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "NA": ("standing/resting-1", "Medium Straight", None, None, NA_F, 1),
    "NG": ("standing/walking-1", "Medium Straight", None, None, NA_F, 1),        # Nadine gehend (hypothetisch: Auszug)
    "RA": ("standing/pointing_finger-1", "No Hair 3", "Full 3", None, {"Skin": "#F0C8A8", "Top": "#4A4A58", "Pants": "#2E2E3A"}, 1),
    "BE": ("standing/robot_dance-3", "Medium Bangs 3", None, "Glasses 3", {"Skin": "#8D5A3B", "Top": "#8FD694", "Pants": "#3D3D58"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("NA_ruhig", "NA", "Calm", 0), ("NA_angst", "NA", "Fear", 0), ("NA_muede", "NA", "Tired", 0),
    ("NA_ernst", "NA", "Serious", 0), ("NA_traurig", "NA", "Concerned|Serious", 0), ("NA_redet", "NA", "Solemn", 1),
    ("NA_zu", "NA", "Eyes Closed", 0), ("NA_hoffnung", "NA", "Smile", 0),
    ("NG_geht", "NG", "Calm", 0), ("NG_hoffnung", "NG", "Smile", 0),
    ("RA_kalt", "RA", "Contempt", 0), ("RA_wuetend", "RA", "Very Angry", 0), ("RA_redet", "RA", "Angry with Fang", 1),
    ("BE_freundlich", "BE", "Smile", 0), ("BE_redet", "BE", "Calm", 1),
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
for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious"),
                            "LX_freut": ("standing/crossed_arms-1", "Cute")}.items():
    a = LX.AUSSEHEN
    for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
        figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
print(n, "Figurenbilder ->", ZIEL)
