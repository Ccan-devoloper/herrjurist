"""Figuren für Folge 010 (Culpa in contrahendo, Teppichrollen im Einrichtungshaus) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Kundin Hartmann: resting-2 (nach dem Sturz kniend am Boden: sitting/hands_back-1, dort schwarzes Oberteil und einfärbbare Hose wie resting-2 = gleiches Outfit), Verkäufer Jannik: easing-2 (grüne Jacke als Arbeitskleidung),
Inhaber Kessler: crossed_arms-2 (verschränkte Arme = Abwehr). Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2) für die
verletzte Kundin. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links
(Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund ("Augen|Mund" bei Mimiken mit offenem Mund, FOLGE-ABLAUF.md). Je sprechender
Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_010")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "HA": ("standing/resting-2", "Long Bangs", None, None, {"Skin": "#D9A47A", "Pants": "#B8A9F5"}, 1),
    "HS": ("sitting/hands_back-1", "Long Bangs", None, None, {"Skin": "#D9A47A", "Pants": "#B8A9F5"}, 1),   # Hartmann am Boden
    "JA": ("standing/easing-2", "Short 5", None, None, {"Skin": "#8D5A3B", "Jacket": "#8FD694", "Pants": "#3D3D58"}, 1),
    "KE": ("standing/crossed_arms-2", "No Hair 2", "Moustache 6", "Glasses 2", {"Skin": "#F0C8A8", "Pants": "#8DB3F2"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HA_ruhig", "HA", "Calm", 0), ("HA_freut", "HA", "Smile", 0), ("HA_redet", "HA", "Smile", 1),
    ("HA_angst", "HA", "Fear", 0), ("HA_schmerz", "HA", "Concerned|Serious", 0), ("HA_fordert", "HA", "Driven", 0),
    ("HA_ernst", "HA", "Serious", 0), ("HA_zufrieden", "HA", "Cute", 0),
    ("HS_angst", "HS", "Fear", 0), ("HS_schmerz", "HS", "Concerned|Serious", 0),
    ("JA_freundlich", "JA", "Smile", 0), ("JA_redet", "JA", "Concerned|Serious", 1), ("JA_schreck", "JA", "Fear", 0),
    ("JA_ernst", "JA", "Serious", 0), ("JA_muede", "JA", "Tired", 0),
    ("KE_ruhig", "KE", "Calm", 0), ("KE_redet", "KE", "Serious", 1), ("KE_abwehr", "KE", "Contempt", 0),
    ("KE_ertappt", "KE", "Concerned|Serious", 0), ("KE_denkt", "KE", "Suspicious", 0),
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
