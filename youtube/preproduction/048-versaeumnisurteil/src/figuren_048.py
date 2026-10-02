"""Figuren für Folge 048 (Versäumnisurteil, mündlicher Grundstückskauf) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Herr Baumann (Verkäufer, Kläger, um 55): standing/pointing_finger-2 (erhobener Zeigefinger: „Dann beantrage ich ein
Versäumnisurteil!“), Kopf Gray Short, ohne Bart und Brille, blaue Hose.
Frau Ehlers (Käuferin, Beklagte, um 35): standing/easing-2 (rosa Jacke, dunkle Hose), Kopf Medium Bangs 2.
Richterin am Amtsgericht (um 55, ohne Namen): standing/blazer-4 (dunkler Blazer wie eine Robe, weißes Oberteil), Kopf Gray
Medium, Brille Glasses 4.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2 verworfen), keine Bärte. Alle Posen blicken im Original nach rechts; die
Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Fear, Contempt, Suspicious
bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_048")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BA": ("standing/pointing_finger-2", "Gray Short", None, None, {"Skin": "#E8B98F", "Pants": "#8DB3F2"}),
    "EH": ("standing/easing-2", "Medium Bangs 2", None, None, {"Skin": "#D9A07A", "Jacket": "#F6A5C0", "Pants": "#3A3A48"}),
    "RI": ("standing/blazer-4", "Gray Medium", None, "Glasses 4", {"Skin": "#F0C8A8", "Jacket": "#3A3A48", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BA_ruhig", "BA", "Calm", 0), ("BA_froh", "BA", "Smile", 0), ("BA_redet", "BA", "Driven", 1),
    ("BA_klagt", "BA", "Concerned|Serious", 1), ("BA_sorge", "BA", "Concerned|Serious", 0), ("BA_denkt", "BA", "Serious", 0),
    ("BA_schreck", "BA", "Fear", 0), ("BA_aerger", "BA", "Contempt", 0),
    ("EH_ruhig", "EH", "Calm", 0), ("EH_redet", "EH", "Smile", 1), ("EH_trotz", "EH", "Suspicious", 1),
    ("EH_denkt", "EH", "Serious", 0), ("EH_sorge", "EH", "Concerned|Serious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_denkt", "RI", "Suspicious", 0),
    ("RI_froh", "RI", "Smile", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
