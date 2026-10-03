"""Figuren für Folge 105 (Klagebefugnis) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Nolte (um 40, Adressatin des Gebührenbescheids): standing/resting-1 (koralles Pullover-Oberteil, schwarze Hose),
Kopf Medium Straight (dunkelbraun eingefärbt).
Herr Wilke (um 45, ihr Freund, klagt aus Solidarität mit): standing/walking-2 (schwarzes T-Shirt, blaue Hose), Kopf Short 1,
Brille Glasses 4.
Die Richterin (um 55, Verwaltungsgericht): standing/blazer-2 (dunkelgrauer Blazer über hellgrünem Oberteil; die Pose hat
eine Beinprothese – bewusst bei einer Richterin, nicht bei einer Täterrolle), Kopf Medium Bangs 3, Brille Glasses 2.
Posen bewusst anders als in 101–103 (crossed_arms-1, pointing_finger-1/2, robot_dance-2, polka_dots, shirt-3, easing-1/2).
Keine Bärte. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts
neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Driven, Solemn, Smile, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_105")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "NO": ("standing/resting-1", "Medium Straight", None, None, {"Skin": "#EBC2A0", "Top": "#F07A6A", "Hair": "#5A3A28"}),
    "WI": ("standing/walking-2", "Short 1", None, "Glasses 4", {"Skin": "#C68E62", "Pants": "#8DB3F2"}),
    "RI": ("standing/blazer-2", "Medium Bangs 3", None, "Glasses 2", {"Skin": "#D9A07A", "Jacket": "#4A4A55", "Top": "#8FD694",
                                                                      "Prosthesis": "#B8B8C4"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("NO_ruhig", "NO", "Calm", 0), ("NO_redet", "NO", "Driven", 1), ("NO_sorge", "NO", "Concerned|Serious", 0),
    ("NO_aerger", "NO", "Rage|Serious", 0), ("NO_denkt", "NO", "Suspicious", 0), ("NO_froh", "NO", "Smile", 0),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_redet", "WI", "Driven", 1), ("WI_denkt", "WI", "Suspicious", 0),
    ("WI_sorge", "WI", "Concerned|Serious", 0), ("WI_muede", "WI", "Tired", 0),
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
