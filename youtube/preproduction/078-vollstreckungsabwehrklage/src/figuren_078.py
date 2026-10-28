"""Figuren für Folge 078 (Vollstreckungsabwehrklage § 767 ZPO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Herr Rademacher (Tischlermeister, Gläubiger, um 60): standing/easing-2 (offenes, holzbraunes Arbeitshemd, blaugraue Hose),
Kopf Gray Short (graues Haar), Brille Glasses 3, ohne Bart; spricht nicht. Herr Neubauer (Schuldner, um 40):
standing/robot_dance-3 (grünes Oberteil, dunkle Hose, offene Hand – zeigt den Überweisungsbeleg), Kopf Short 3, ohne Bart.
Rechtsanwältin Kellermann (um 45): standing/blazer-4 (dunkles Sakko, weißes Oberteil), Kopf Long.
Gerichtsvollzieherin (um 50, ohne Namen, sachlich): standing/blazer-3 (blaugraues Sakko, dunkle Hose), Kopf Bun, Brille Glasses 2.
Keine Prothesen-Posen, keine Bärte (Mund frei), keine realen Personen, keine Klischees.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious,
Suspicious, Fear, Solemn bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_078")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RA": ("standing/easing-2", "Gray Short", None, "Glasses 3", {"Skin": "#F0C8A8", "Jacket": "#D6A06E", "Pants": "#5A6A8A", "Hair": "#C4C4CC"}),
    "NB": ("standing/robot_dance-3", "Short 3", None, None, {"Skin": "#E8B98F", "Top": "#8FD694", "Pants": "#3A3A48"}),
    "KM": ("standing/blazer-4", "Long", None, None, {"Skin": "#C99470", "Jacket": "#3A3A48", "Top": "#FFFFFF"}),
    "GV": ("standing/blazer-3", "Bun", None, "Glasses 2", {"Skin": "#F2CDB0", "Jacket": "#5A6A8A", "Pants": "#3A3A48"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RA_ruhig", "RA", "Calm", 0), ("RA_streng", "RA", "Suspicious", 0), ("RA_froh", "RA", "Smile", 0),
    ("RA_sorge", "RA", "Concerned|Serious", 0), ("RA_denkt", "RA", "Serious", 0),
    ("NB_ruhig", "NB", "Calm", 0), ("NB_redet", "NB", "Concerned|Serious", 1), ("NB_sorge", "NB", "Concerned|Serious", 0),
    ("NB_denkt", "NB", "Suspicious", 0), ("NB_froh", "NB", "Smile", 0), ("NB_schreck", "NB", "Fear", 0),
    ("KM_ruhig", "KM", "Calm", 0), ("KM_redet", "KM", "Serious", 1), ("KM_froh", "KM", "Smile", 0),
    ("KM_denkt", "KM", "Suspicious", 0),
    ("GV_ruhig", "GV", "Calm", 0), ("GV_redet", "GV", "Serious", 1), ("GV_denkt", "GV", "Suspicious", 0),
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
