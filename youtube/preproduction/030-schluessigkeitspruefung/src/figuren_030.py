"""Figuren für Folge 030 (Schlüssigkeitsprüfung, Darlehensfall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Frau Schubert (Klägerin, Darlehensgeberin, um 45): standing/resting-2 (schwarzes Oberteil, blaue Hose), Kopf Medium Straight.
Herr Franke (Nachbar, Beklagter, um 60): standing/pointing_finger-1 (erhobener Zeigefinger: „Von Juni war nie die Rede!“),
Kopf No Hair 1, Brille Glasses, grünes Oberteil. Kein Bart (Mund bleibt frei).
Richterin am Amtsgericht (um 50): standing/robot_dance-2 (offene Hand: Hinweis), Kopf Long Bangs, Brille Glasses 2, dunkle Hose.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2 verworfen). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Fear, Contempt, Suspicious, Tired
bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_030")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "SC": ("standing/resting-2", "Medium Straight", None, None, {"Skin": "#E8B98F", "Pants": "#8DB3F2"}),
    "FR": ("standing/pointing_finger-1", "No Hair 1", None, "Glasses", {"Skin": "#F0C8A8", "Top": "#8FD694"}),
    "RI": ("standing/robot_dance-2", "Long Bangs", None, "Glasses 2", {"Skin": "#B07552", "Pants": "#3A3A48"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SC_ruhig", "SC", "Calm", 0), ("SC_redet", "SC", "Driven", 1), ("SC_froh", "SC", "Smile", 0),
    ("SC_sorge", "SC", "Concerned|Serious", 0), ("SC_denkt", "SC", "Serious", 0), ("SC_aerger", "SC", "Contempt", 0),
    ("SC_schreck", "SC", "Fear", 0),
    ("FR_ruhig", "FR", "Calm", 0), ("FR_redet", "FR", "Smile", 1), ("FR_trotz", "FR", "Suspicious", 1),
    ("FR_denkt", "FR", "Serious", 0), ("FR_muede", "FR", "Tired", 0),
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
