"""Figuren für Folge 004 (Neutralitätspflicht) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Ministerin Brandt: easing-2, Pressesprecher Krüger: resting-1, Studentin Mia: walking-2, Vorsitzender Hahn (Partei X):
robot_dance-3 (Szenenplan). Alle vier Posen blicken im Original nach rechts; die Grundansicht ist daher gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_004")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "BR": ("standing/easing-2", "Medium Bangs 2", None, None, {"Skin": "#E6B48F", "Jacket": "#B8A9F5", "Pants": "#3D3D58"}, 1),
    "KR": ("standing/resting-1", "Short 1", None, "Glasses 2", {"Skin": "#B07552", "Top": "#7FD6D0", "Pants": "#3D3D58"}, 1),
    "MI": ("standing/walking-2", "Buns", None, None, {"Skin": "#8D5A3B", "Pants": "#8DB3F2"}, 1),
    "HA": ("standing/robot_dance-3", "Gray Short", "Moustache 4", None, {"Skin": "#F0C8A8", "Top": "#B0B2BE", "Pants": "#3D3D58"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
# Grundmimik "Augen|Mund": Mimiken mit offenem Mund (Concerned, Fear, Rage, Smile Big) bekommen einen geschlossenen Mund,
# damit der Mund in Pausen, zwischen Wörtern und bei anderen Sprechern zu ist (Sichtprüfung 01.10.2026).
LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Driven", 1), ("BR_cool", "BR", "Cheeky", 1),
    ("BR_zufrieden", "BR", "Smile Big|Smile", 0), ("BR_denkt", "BR", "Serious", 0), ("BR_ertappt", "BR", "Concerned|Serious", 0),
    ("BR_kaempft", "BR", "Smile", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_zweifel", "KR", "Concerned|Serious", 1), ("KR_schock", "KR", "Fear|Serious", 0),
    ("MI_neugierig", "MI", "Smile", 0), ("MI_liest", "MI", "Serious", 0), ("MI_unsicher", "MI", "Concerned|Serious", 1),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_wuetend", "HA", "Rage|Serious", 1), ("HA_ernst", "HA", "Serious", 0),
    ("HA_zufrieden", "HA", "Smile", 0),
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
