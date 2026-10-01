"""Figuren für Folge 019 (Sitzblockade) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Personen erfunden.
Hanna (klebt sich fest): sitting/hands_back-1 · Lukas (sitzt nur): sitting/one_leg_up-2 · zwei weitere Sitzende ohne Rolle:
sitting/mid-1, sitting/closed_legs-1 · Dieter (erste Reihe): standing/shirt-3 · Sabine (zweite Reihe): standing/crossed_arms-2.
Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts (geprüft am Kontaktbild).
Farbflächen je Pose laut SVG: hands_back-1/mid-1/crossed_arms-2 nur Pants, one_leg_up-2/shirt-3 nur Top, closed_legs-1 Top+Jacket.
Alle Grundmimiken mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als „Augen|Serious/Smile“.
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_019")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)  – Spiegelung so, dass die Grundansicht nach links blickt
P = {
    "HA": ("sitting/hands_back-1", "Long", None, None, {"Skin": "#E8B98F", "Pants": "#B8A9F5"}, 1),
    "LU": ("sitting/one_leg_up-2", "Short 2", None, None, {"Skin": "#C99470", "Top": "#8FD694"}, 1),
    "E1": ("sitting/mid-1", "Afro", None, None, {"Skin": "#8D5A3B", "Pants": "#F9A66C"}, 1),
    "E2": ("sitting/closed_legs-1", "Bangs", None, "Glasses 2", {"Skin": "#F1C7A5", "Top": "#FFFFFF", "Jacket": "#7FD6D0"}, 1),
    "DI": ("standing/shirt-3", "Short 3", None, "Glasses 3", {"Skin": "#E6B48F", "Top": "#F07A6A"}, 1),
    "SA": ("standing/crossed_arms-2", "Medium Bangs", None, None, {"Skin": "#8D5A3B", "Pants": "#8DB3F2"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Driven", 1), ("HA_ernst", "HA", "Serious", 0),
    ("HA_froh", "HA", "Smile", 0),
    ("LU_ruhig", "LU", "Calm", 0), ("LU_ernst", "LU", "Serious", 0), ("LU_denkt", "LU", "Suspicious", 0),
    ("E1_ruhig", "E1", "Calm", 0), ("E2_ruhig", "E2", "Calm", 0),
    ("DI_ruhig", "DI", "Calm", 0), ("DI_schreck", "DI", "Fear", 0), ("DI_redet", "DI", "Concerned|Serious", 1),
    ("DI_denkt", "DI", "Serious", 0), ("DI_muede", "DI", "Tired", 0),
    ("SA_ruhig", "SA", "Calm", 0), ("SA_redet", "SA", "Suspicious", 1), ("SA_genervt", "SA", "Very Angry", 0),
    ("SA_muede", "SA", "Tired", 0), ("SA_ernst", "SA", "Serious", 0),
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
