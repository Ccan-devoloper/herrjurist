"""Figuren für Folge 009 (Strafrechtsklausur Aufbau, Akku-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Bruno (Anstifter): shirt-4, Kim: robot_dance-3, Tara: blazer-3, Ladeninhaber Ohm: walking-1 (stehend/laufend) und
sitting/hands_back-2 (nach dem Sturz am Boden, gleiche Reihe -1/-2 nicht verfügbar: gleiches Shirt-Farbfeld, schwarze Hose).
Grundansicht blickt nach links (gespiegelt), Suffix _r blickt nach rechts. Keine Prothesen-Posen.
Grundmimik immer mit geschlossenem Mund ("Augen|Mund" bei Mimiken mit offenem Mund, FOLGE-ABLAUF.md).
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_009")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

OH_F = {"Skin": "#EBC4A0", "Top": "#8FD694"}
# Person: (Pose, Kopf, Bart, Brille, Farben); Grundansicht gespiegelt (blickt nach links)
P = {
    "BR": ("standing/shirt-4", "Gray Short", "Chin", None, {"Skin": "#F0C8A8", "Pants": "#5A5A6A"}),
    "KI": ("standing/robot_dance-3", "Medium Bangs 3", None, None, {"Skin": "#E8B98F", "Top": "#F07A6A", "Pants": "#3D3D58"}),
    "TA": ("standing/blazer-3", "Twists 2", None, None, {"Skin": "#8D5A3B", "Jacket": "#B8A9F5", "Pants": "#2E2E3A"}),
    "OH": ("standing/walking-1", "No Hair 3", "Moustache 4", "Glasses 2", OH_F),
    "OHS": ("sitting/hands_back-2", "No Hair 3", "Moustache 4", "Glasses 2", OH_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Suspicious", 1), ("BR_zufrieden", "BR", "Smile", 0),
    ("BR_denkt", "BR", "Serious", 0), ("BR_ertappt", "BR", "Concerned|Serious", 0),
    ("KI_ruhig", "KI", "Calm", 0), ("KI_redet", "KI", "Smile", 1), ("KI_cool", "KI", "Cheeky|Smile", 0),
    ("KI_schreck", "KI", "Fear", 0), ("KI_wuetend", "KI", "Very Angry", 0), ("KI_ertappt", "KI", "Concerned|Serious", 0),
    ("KI_denkt", "KI", "Serious", 0),
    ("TA_ruhig", "TA", "Calm", 0), ("TA_freundlich", "TA", "Smile", 0), ("TA_cool", "TA", "Cheeky|Smile", 0),
    ("TA_wuetend", "TA", "Very Angry", 0), ("TA_ertappt", "TA", "Concerned|Serious", 0), ("TA_denkt", "TA", "Serious", 0),
    ("OH_ruhig", "OH", "Calm", 0), ("OH_freundlich", "OH", "Smile", 0), ("OH_schreck", "OH", "Concerned|Serious", 0),
    ("OH_ruft", "OH", "Rage|Serious", 1),
    ("OH_sitzt", "OHS", "Concerned|Serious", 0), ("OH_sitzt_schreck", "OHS", "Fear", 0),
]

n = 0
for name, p, mimik, mund in LISTE:
    pose, kopf, bart, brille, farben = P[p]
    for suffix, gespiegelt in (("", 1), ("_r", 0)):
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
