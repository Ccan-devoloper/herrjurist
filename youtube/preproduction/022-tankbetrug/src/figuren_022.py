"""Figuren für Folge 022 (Tankbetrug) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Personen erfunden.
Jens (tankt ohne Zahlungswillen): standing/easing-1 · Birgit (Kassiererin): standing/pointing_finger-2 ·
Renate (Gegenfall, älter): standing/resting-1. Grundansicht blickt nach links (Figur rechts neben der Tafel),
Suffix _r blickt nach rechts (am Kontaktbild geprüft). Farbflächen laut SVG: easing-1 Jacket+Top, pointing_finger-2 Pants,
resting-1 Top. Alle Grundmimiken mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als „Augen|Serious/Smile“.
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_022")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "JE": ("standing/easing-1", "Short 5", None, None, {"Skin": "#E8B98F", "Jacket": "#7FD6D0", "Top": "#2E2E3A"}, 1),
    "BI": ("standing/pointing_finger-2", "Long Bangs", None, "Glasses 4", {"Skin": "#C99470", "Pants": "#B8A9F5"}, 1),
    "RE": ("standing/resting-1", "Gray Medium", None, "Glasses", {"Skin": "#F1C7A5", "Top": "#F9A66C", "Hair": "#E2E2E2"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JE_ruhig", "JE", "Calm", 0), ("JE_redet", "JE", "Suspicious", 1), ("JE_cool", "JE", "Cheeky|Smile", 0),
    ("JE_ertappt", "JE", "Fear", 0), ("JE_denkt", "JE", "Serious", 0), ("JE_muede", "JE", "Tired", 0),
    ("BI_ruhig", "BI", "Calm", 0), ("BI_redet", "BI", "Rage|Serious", 1), ("BI_froh", "BI", "Smile", 0),
    ("BI_schaut", "BI", "Suspicious", 0), ("BI_ernst", "BI", "Serious", 0),
    ("RE_ruhig", "RE", "Calm", 0), ("RE_redet", "RE", "Contempt", 1), ("RE_denkt", "RE", "Serious", 0),
    ("RE_froh", "RE", "Smile", 0),
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
