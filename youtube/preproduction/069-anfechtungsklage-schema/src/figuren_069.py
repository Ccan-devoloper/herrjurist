"""Figuren für Folge 069 (Anfechtungsklage Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Ebeling (um 38, betreibt einen Foodtruck): standing/easing-2 (hellblaues Hemd über schwarzem Shirt, gelbe Hose),
Kopf Long Bangs (dunkelbraunes Haar).
Herr Gerlach (um 58, Gewerbeamt der Stadt): standing/blazer-3, Kopf Gray Short, dunkelblaues Jackett, graue Hose.
Die Richterin (um 50, Verwaltungsgericht): standing/resting-1, Kopf Medium Bangs 3, Brille Glasses 2, dunkles Oberteil.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Driven, Calm, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_069")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "EB": ("standing/easing-2", "Long Bangs", None, None, {"Skin": "#F1C6A5", "Hair": "#4A3428", "Jacket": "#8DB3F2"}),
    "GE": ("standing/blazer-3", "Gray Short", None, None, {"Skin": "#E6B48F", "Jacket": "#3D4A7A", "Pants": "#7A7A86"}),
    "RI": ("standing/resting-1", "Medium Bangs 3", None, "Glasses 2", {"Skin": "#D9A07A", "Top": "#34343C", "Hair": "#5A3A2A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EB_ruhig", "EB", "Smile", 0), ("EB_redet", "EB", "Driven", 1), ("EB_sorge", "EB", "Concerned|Serious", 0),
    ("EB_denkt", "EB", "Suspicious", 0), ("EB_aerger", "EB", "Rage|Serious", 0), ("EB_muede", "EB", "Tired", 0),
    ("GE_ruhig", "GE", "Serious", 0), ("GE_redet", "GE", "Serious", 1), ("GE_denkt", "GE", "Solemn", 0),
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
