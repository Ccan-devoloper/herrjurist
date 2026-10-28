"""Figuren für Folge 016 (Volkszählungsurteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Frau Hartmann (um 65, soll den Fragebogen ausfüllen): standing/polka_dots, Kopf Gray Medium (graues Haar), Glasses 3.
Herr Lehmann (um 25, ehrenamtlicher Zähler, Behördenfigur): standing/shirt-4 (schwarzes Hemd, blaue Hose), Kopf Short 2.
Herr Sommer (um 70, Nachbar, Bürgerinitiative): standing/pointing_finger-1 (grünes Oberteil, schwarze Hose), Kopf No Hair 3, Glasses 4.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Driven, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (HA_redet, LE_redet, SO_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_016")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
GRAU_HAAR = "#C9C9CF"

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HA": ("standing/polka_dots", "Gray Medium", None, "Glasses 3", {"Skin": "#EBC4A0", "Hair": GRAU_HAAR, "Pants": "#B8A9F5"}),
    "LE": ("standing/shirt-4", "Short 2", None, None, {"Skin": "#C58E64", "Pants": "#8DB3F2"}),
    "SO": ("standing/pointing_finger-1", "No Hair 3", None, "Glasses 4", {"Skin": "#F0C8A8", "Top": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HA_ruhig", "HA", "Calm", 0), ("HA_liest", "HA", "Serious", 0), ("HA_redet", "HA", "Concerned|Serious", 1),
    ("HA_sorge", "HA", "Concerned|Serious", 0), ("HA_denkt", "HA", "Suspicious", 0), ("HA_froh", "HA", "Smile", 0),
    ("HA_schreck", "HA", "Fear", 0),
    ("LE_ruhig", "LE", "Calm", 0), ("LE_redet", "LE", "Serious", 1), ("LE_froh", "LE", "Smile", 0),
    ("SO_ruhig", "SO", "Calm", 0), ("SO_redet", "SO", "Concerned|Serious", 1), ("SO_sorge", "SO", "Fear", 0),
    ("SO_denkt", "SO", "Serious", 0), ("SO_froh", "SO", "Smile", 0),
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
