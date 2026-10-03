"""Figuren für Folge 096 (Drittwiderspruchsklage § 771 ZPO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Wendland (um 78, Großmutter, Eigentümerin des Gemäldes): standing/resting-1 (blauer Pullover, schwarze Hose),
Kopf Gray Medium (graues Haar), Brille Glasses.
Herr Vollmer (um 23, Student, ihr Enkel, Schuldner): standing/easing-1 (offenes grünes Hemd über weißem Shirt, dunkle Hose),
Kopf Pomp.
Die Gerichtsvollzieherin (um 35, ohne Namen, sachlich): standing/blazer-4 (dunkelblauer Blazer, weißes Oberteil),
Kopf Medium Bangs 3.
Herr Gebhardt (um 50, Fahrradhändler, Gläubiger, spricht nicht): standing/crossed_arms-1 (türkisfarbener Pullover,
schwarze Hose), Kopf Short 1, Brille Glasses 3; neutrale Mimik, keine „fiese“ Darstellung.
Posen bewusst anders als in 093–095 (robot_dance-2, blazer-3, pointing_finger-1, polka_dots, easing-2, shirt-3).
Keine Bärte, keine Prothesen-Posen, keine Muster. Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Driven, Fear, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet…, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_096")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WE": ("standing/resting-1", "Gray Medium", None, "Glasses", {"Skin": "#F0C8A8", "Top": "#8DB3F2", "Hair": "#C4C4CC"}),
    "VO": ("standing/easing-1", "Pomp", None, None, {"Skin": "#E2B08C", "Jacket": "#8FD694", "Top": "#FFFFFF", "Pants": "#3A3A48"}),
    "GV": ("standing/blazer-4", "Medium Bangs 3", None, None, {"Skin": "#B07552", "Jacket": "#3D4A7A", "Top": "#FFFFFF"}),
    "GE": ("standing/crossed_arms-1", "Short 1", None, "Glasses 3", {"Skin": "#F2CDB0", "Top": "#9ED9DC"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WE_ruhig", "WE", "Calm", 0), ("WE_froh", "WE", "Smile", 0), ("WE_redet", "WE", "Smile", 1),
    ("WE_redetstreng", "WE", "Driven", 1), ("WE_sorge", "WE", "Concerned|Serious", 0), ("WE_entschlossen", "WE", "Driven", 0),
    ("WE_denkt", "WE", "Suspicious", 0), ("WE_strahlt", "WE", "Smile Big|Smile", 0),
    ("VO_ruhig", "VO", "Calm", 0), ("VO_froh", "VO", "Smile", 0), ("VO_schreck", "VO", "Fear", 0),
    ("VO_redet", "VO", "Concerned|Serious", 1), ("VO_sorge", "VO", "Concerned|Serious", 0), ("VO_denkt", "VO", "Suspicious", 0),
    ("GV_ruhig", "GV", "Calm", 0), ("GV_redet", "GV", "Serious", 1), ("GV_denkt", "GV", "Solemn", 0),
    ("GE_ruhig", "GE", "Calm", 0), ("GE_denkt", "GE", "Suspicious", 0), ("GE_ernst", "GE", "Serious", 0),
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
