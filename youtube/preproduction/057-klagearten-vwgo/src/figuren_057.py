"""Figuren für Folge 057 (Klagearten VwGO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Behrens (um 45, Bootsverleih am See): standing/walking-3 (schwarzes Outfit), Kopf Long (braunes Haar).
Frau Thiele (um 40, Bauamt): standing/resting-2, Kopf Medium Bangs, Brille Glasses, blaue Hose.
Bürgermeister Harms (um 62): standing/blazer-4, Kopf No Hair 2 mit grauem Haarkranz, dunkelblaues Jackett.
Herr Lindemann (um 45, Ordnungsamt): standing/easing-1, Kopf Short 2.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Solemn, Driven, Cute, Calm bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_057")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BE": ("standing/walking-3", "Long", None, None, {"Skin": "#F1C6A5", "Hair": "#6B4A3A"}),
    "TH": ("standing/resting-2", "Medium Bangs", None, "Glasses", {"Skin": "#F0C8A8", "Pants": "#8DB3F2"}),
    "HA": ("standing/blazer-4", "No Hair 2", None, None, {"Skin": "#E6B48F", "Jacket": "#3D4A7A", "Hair": "#9A9AA6"}),
    "LI": ("standing/easing-1", "Short 2", None, None, {"Skin": "#D9A07A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BE_ruhig", "BE", "Smile", 0), ("BE_redet", "BE", "Driven", 1), ("BE_sorge", "BE", "Concerned|Serious", 0),
    ("BE_denkt", "BE", "Suspicious", 0), ("BE_froh", "BE", "Cute", 0),
    ("TH_ruhig", "TH", "Serious", 0), ("TH_redet", "TH", "Serious", 1),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Serious", 1),
    ("LI_ruhig", "LI", "Serious", 0), ("LI_redet", "LI", "Serious", 1), ("LI_denkt", "LI", "Solemn", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
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
