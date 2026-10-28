"""Figuren für Folge 072 (Verfahrensrüge § 344 II 2 StPO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Richter am Bundesgerichtshof (um 60, ohne Namen): standing/blazer-3 (dunkles Sakko, graue Hose), Kopf No Hair 2 (Resthaar grau),
Brille Glasses 2, ohne Bart. Rechtsanwältin Hellwig (Verteidigerin, um 45): standing/pointing_finger-2 (schwarzes Oberteil,
lila Hose), Kopf Medium 2. Herr Bachmann (Mandant, verurteilter Angeklagter, um 40): standing/crossed_arms-2 (schwarzes
Oberteil, grüne Hose), Kopf Short 5, ohne Bart, heller Hautton (keine Prothese, kein Herkunfts- oder Hautfarben-Klischee).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious,
Suspicious, Fear, Solemn, Tired bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_072")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RI": ("standing/blazer-3", "No Hair 2", None, "Glasses 2", {"Skin": "#F2CDB0", "Jacket": "#3A3A48", "Pants": "#5A5A6A", "Hair": "#C4C4CC"}),
    "HW": ("standing/pointing_finger-2", "Medium 2", None, None, {"Skin": "#F0C8A8", "Pants": "#B8A9F5"}),
    "BA": ("standing/crossed_arms-2", "Short 5", None, None, {"Skin": "#E8B98F", "Pants": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_denkt", "RI", "Suspicious", 0),
    ("RI_streng", "RI", "Solemn", 0), ("RI_froh", "RI", "Smile", 0),
    ("HW_ruhig", "HW", "Calm", 0), ("HW_redet", "HW", "Serious", 1), ("HW_denkt", "HW", "Suspicious", 0),
    ("HW_froh", "HW", "Smile", 0), ("HW_sorge", "HW", "Concerned|Serious", 0), ("HW_schreck", "HW", "Fear", 0),
    ("BA_ruhig", "BA", "Calm", 0), ("BA_redet", "BA", "Concerned|Serious", 1), ("BA_sorge", "BA", "Concerned|Serious", 0),
    ("BA_denkt", "BA", "Suspicious", 0), ("BA_froh", "BA", "Smile", 0), ("BA_schreck", "BA", "Fear", 0),
    ("BA_muede", "BA", "Tired", 0),
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
