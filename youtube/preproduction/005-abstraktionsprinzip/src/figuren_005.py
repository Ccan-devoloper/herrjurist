"""Figuren für Folge 005 (Abstraktionsprinzip) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Sandra: pointing_finger-2 / crossed_arms-2 (gleiche Reihe -2: schwarzes Oberteil, blaue Hose), Bäckerin Hanne:
doctor-nurse-02 (weißer Kittel als Bäckerkittel, ohne Haube), Ben: shirt-3, Walter: robot_dance-2 (übergibt mit offener
Hand). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts
neben der Tafel), Suffix _r blickt nach rechts.
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der
Gesichtshöhe). Grundmimiken mit offenem Mund (Concerned, Fear, Smile Big, Rage) werden als 'Augen|Mund' mit
geschlossenem Mund zusammengesetzt (Befund Folge 004), damit der Mund in Pausen und bei anderen Sprechern zu ist."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_005")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

SA_F = {"Skin": "#E8B98F", "Pants": "#8DB3F2"}
HA_F = {"Skin": "#D9A07A", "Hair": "#C9C9C9"}
BE_F = {"Skin": "#C99470", "Top": "#8FD694"}
WA_F = {"Skin": "#F0C8A8", "Pants": "#9C7A5B"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "SA": ("standing/pointing_finger-2", "Long Bangs", None, None, SA_F, 1),
    "SA_ARME": ("standing/crossed_arms-2", "Long Bangs", None, None, SA_F, 1),
    "HA": ("standing/doctor-nurse-02", "Gray Medium", None, "Glasses 3", HA_F, 1),
    "BE": ("standing/shirt-3", "Short 5", None, None, BE_F, 1),
    "WA": ("standing/robot_dance-2", "No Hair 2", None, "Glasses 4", WA_F, 1),
}

# (Name, Pose, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r
LISTE = [
    ("SA_zeigt", "SA", "Calm", 0), ("SA_redet", "SA", "Smile", 1), ("SA_streng", "SA", "Serious", 1),
    ("SA_wartet", "SA_ARME", "Calm", 0), ("SA_aerger", "SA_ARME", "Contempt", 0), ("SA_zufrieden", "SA_ARME", "Smile", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Serious", 1), ("HA_freundlich", "HA", "Smile", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Smile", 1), ("BE_froh", "BE", "Smile Big|Smile", 0),
    ("BE_ertappt", "BE", "Concerned|Serious", 0), ("BE_denkt", "BE", "Serious", 0), ("BE_muede", "BE", "Tired", 0),
    ("WA_ruhig", "WA", "Old", 0), ("WA_redet", "WA", "Smile", 1), ("WA_fordert", "WA", "Serious", 1),
    ("WA_aerger", "WA", "Contempt", 0), ("WA_denkt", "WA", "Suspicious", 0),
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
