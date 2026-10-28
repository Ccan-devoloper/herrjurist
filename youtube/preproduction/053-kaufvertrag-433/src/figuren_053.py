"""Figuren für Folge 053 (§ 433 BGB, Pflichten aus dem Kaufvertrag) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Inga (Käuferin, um 22): standing/easing-1 (grüne Jacke, weißes Oberteil, schwarze Hose) und – nur beim Davonfahren –
sitting/bike mit derselben grünen Jacke und demselben weißen Oberteil (gleiches Outfit; das rosa Rad der Pose ist das
gekaufte Rad). Herr Lüders (Verkäufer, um 35): nur standing/robot_dance-2 (offene Hand; schwarzes Oberteil, Hose Blau, dunkle
Schuhe). pointing_finger-2 wurde nach der Kopfprobe verworfen (andere Statur).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Smile/Serious“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe). Keine Bärte, keine Prothesen-Posen."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_053")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

IN_F = {"Skin": "#E8B98F", "Jacket": "#8FD694", "Top": "#FFFFFF", "Shoes": "#FFFFFF"}
LU_F = {"Skin": "#D9A07A", "Pants": "#8DB3F2", "Shoes": "#3D3D58"}
# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "IN": ("standing/easing-1", "Medium Bangs", None, None, IN_F, 1),
    "INR": ("sitting/bike", "Medium Bangs", None, None, IN_F, 1),
    "LU": ("standing/robot_dance-2", "Short 2", None, None, LU_F, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("IN_ruhig", "IN", "Calm", 0), ("IN_froh", "IN", "Smile Big|Smile", 0), ("IN_redet", "IN", "Smile", 1),
    ("IN_denkt", "IN", "Serious", 0), ("IN_ueberlegt", "IN", "Suspicious", 0), ("IN_sorge", "IN", "Concerned|Serious", 0),
    ("IN_rad", "INR", "Smile", 0),
    ("LU_ruhig", "LU", "Calm", 0), ("LU_froh", "LU", "Smile", 0), ("LU_redet", "LU", "Smile", 1),
    ("LU_denkt", "LU", "Suspicious", 0), ("LU_ernst", "LU", "Serious", 0), ("LU_sorge", "LU", "Concerned|Serious", 0),
    ("LU_streng", "LU", "Serious", 1),
]

if __name__ == "__main__":
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
