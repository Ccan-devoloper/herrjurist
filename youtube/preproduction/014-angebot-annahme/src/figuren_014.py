"""Figuren für Folge 014 (Angebot und Annahme) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Gerd (Verkäufer, um 70): standing/robot_dance-3 (offene Hand), Lotte (Käuferin, um 25): standing/polka_dots,
Malte (Kaufinteressent, um 30): Brustbild body/Hoodie (nur im Telefonbild). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als „Augen|Serious/Smile“.
Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund', Schnitt bei 60 % der
Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_014")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "GE": ("standing/robot_dance-3", "No Hair 3", None, "Glasses 3", {"Skin": "#EBC4A0", "Top": "#8DB3F2", "Pants": "#3D3D58"}, 1),
    "LO": ("standing/polka_dots", "Medium Straight", None, None, {"Skin": "#C99470", "Pants": "#B8A9F5"}, 1),
    "MA": ("body/Hoodie", "Short 2", None, None, {"Skin": "#F0C8A8", "Jacket": "#F9A66C"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("GE_ruhig", "GE", "Calm", 0), ("GE_redet", "GE", "Smile", 1), ("GE_protest", "GE", "Serious", 1),
    ("GE_denkt", "GE", "Suspicious", 0), ("GE_aerger", "GE", "Contempt", 0), ("GE_froh", "GE", "Smile", 0),
    ("GE_sorge", "GE", "Concerned|Serious", 0),
    ("LO_ruhig", "LO", "Calm", 0), ("LO_redet", "LO", "Smile", 1), ("LO_froh", "LO", "Smile Big|Smile", 0),
    ("LO_denkt", "LO", "Serious", 0), ("LO_ueberlegt", "LO", "Suspicious", 0), ("LO_sorge", "LO", "Concerned|Serious", 0),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Driven", 1),
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
