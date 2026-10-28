"""Figuren für Folge 006 (Anspruchsaufbau, Mietwohnungs-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Vermieter Albers: pointing_finger-1, Mieterin Jana: polka_dots, Jurastudent Noah: crossed_arms-2 (Szenenplan).
Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund ("Augen|Mund" bei Mimiken mit offenem Mund, FOLGE-ABLAUF.md).
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_006")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "AL": ("standing/pointing_finger-1", "No Hair 1", None, "Glasses 3", {"Skin": "#F0C8A8"}, int(os.environ.get("SP_AL", 1))),
    "JA": ("standing/polka_dots", "Long Curly", None, None, {"Skin": "#8D5A3B", "Pants": "#8FD694"}, int(os.environ.get("SP_JA", 1))),
    "NO": ("standing/crossed_arms-2", "Short 3", None, None, {"Skin": "#E8B98F", "Pants": "#F9D56E"}, int(os.environ.get("SP_NO", 1))),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("AL_ruhig", "AL", "Calm", 0), ("AL_fordert", "AL", "Serious", 1), ("AL_aerger", "AL", "Very Angry", 0),
    ("AL_zufrieden", "AL", "Smile", 0), ("AL_denkt", "AL", "Suspicious", 0),
    ("JA_ruhig", "JA", "Calm", 0), ("JA_trotzig", "JA", "Driven", 1), ("JA_ertappt", "JA", "Concerned|Serious", 0),
    ("JA_zufrieden", "JA", "Smile", 0), ("JA_denkt", "JA", "Serious", 0),
    ("NO_denkt", "NO", "Serious", 0), ("NO_fragt", "NO", "Concerned|Serious", 1), ("NO_redet", "NO", "Smile", 1),
    ("NO_ertappt", "NO", "Fear", 0), ("NO_froh", "NO", "Smile Big|Smile", 0),
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
