"""Figuren für Folge 056 (Werkvertrag oder Dienstvertrag?) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Mareike (Studentin/Bestellerin, um 22): standing/resting-1 (lila Pullover, schwarze Hose), Kopf „Long“.
Henrik (Nachhilfelehrer, um 25): standing/robot_dance-3 (offene, erklärende Hand; grünes Oberteil, gelbe Hose), Kopf „Pomp“.
Frau Ostertag (Malerin, um 30): standing/shirt-3 (weißes Arbeitshemd, schwarze Hose), Kopf „Bangs“ (blond).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Serious/Smile“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe). Keine Bärte, keine Prothesen-Posen."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_056")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

MA_F = {"Skin": "#F2C9A5", "Top": "#B8A9F5"}
HE_F = {"Skin": "#B9825C", "Top": "#8FD694"}
OS_F = {"Skin": "#E9B48A", "Top": "#FFFFFF"}
# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "MA": ("standing/resting-1", "Long", None, None, MA_F, 1),
    "HE": ("standing/robot_dance-3", "Pomp", None, None, HE_F, 1),
    "OS": ("standing/shirt-3", "Bangs", None, None, OS_F, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_froh", "MA", "Smile Big|Smile", 0), ("MA_denkt", "MA", "Serious", 0),
    ("MA_ueberlegt", "MA", "Suspicious", 0), ("MA_sorge", "MA", "Concerned|Serious", 0), ("MA_muede", "MA", "Tired", 0),
    ("MA_redet", "MA", "Serious", 1),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_froh", "HE", "Smile", 0), ("HE_denkt", "HE", "Suspicious", 0),
    ("HE_ernst", "HE", "Serious", 0), ("HE_redet", "HE", "Smile", 1),
    ("OS_ruhig", "OS", "Calm", 0), ("OS_froh", "OS", "Smile", 0), ("OS_denkt", "OS", "Serious", 0),
    ("OS_ertappt", "OS", "Concerned|Serious", 0), ("OS_redet", "OS", "Smile", 1),
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
