"""Figuren für Folge 093 (Verpflichtungsklage Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Herr Feldmann (um 40, führt ein Café): standing/robot_dance-2 (schwarzes Shirt, Jeans-blaue Hose), Kopf Short 3.
Frau Siebert (um 60, Sachbearbeiterin der Stadt): standing/blazer-3 (graublauer Blazer über schwarzem Shirt, dunkelblaue
Hose), Kopf Gray Bun, Brille Glasses 2.
Die Richterin (um 40, Verwaltungsgericht): standing/pointing_finger-1 (schwarzes Oberteil, schwarze Hose), Kopf Long Curly,
Brille Glasses 4.
Posen bewusst anders als in 089–092 (shirt-3, easing-1/2, walking-1/2, crossed_arms-1/2, blazer-4, robot_dance-3, shirt-4,
resting-1/2). Keine Bärte, keine Prothesen-Posen, keine Muster. Alle Posen blicken im Original nach rechts; die Grundansicht
ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Driven, Calm, Solemn, Cute bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet…, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_093")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "FE": ("standing/robot_dance-2", "Short 3", None, None, {"Skin": "#E8B998", "Pants": "#5B7DB8"}),
    "SI": ("standing/blazer-3", "Gray Bun", None, "Glasses 2", {"Skin": "#F2C7A8", "Jacket": "#8F9DB8", "Pants": "#3D4A7A"}),
    "RI": ("standing/pointing_finger-1", "Long Curly", None, "Glasses 4", {"Skin": "#A86B4A", "Top": "#2B2B2B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FE_ruhig", "FE", "Smile", 0), ("FE_redet", "FE", "Driven", 1), ("FE_redetfroh", "FE", "Smile", 1),
    ("FE_hofft", "FE", "Cute", 0), ("FE_sorge", "FE", "Concerned|Serious", 0), ("FE_denkt", "FE", "Suspicious", 0),
    ("FE_froh", "FE", "Smile Big|Smile", 0),
    ("SI_ruhig", "SI", "Calm", 0), ("SI_redet", "SI", "Serious", 1), ("SI_denkt", "SI", "Solemn", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1),
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
