"""Figuren für Folge 024 (Zwangsvollstreckung Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Frau Köhler (Malermeisterin, Gläubigerin, um 45): standing/crossed_arms-1 (weißes Malerhemd), Herr Vogel (Schuldner, um 28):
standing/walking-3 (schwarzes Shirt und Hose, Pose ohne einfärbbare Kleidung), Gerichtsvollzieher (um 50): standing/blazer-4
(dunkles Sakko, weißes Hemd), Urkundsbeamtin der Geschäftsstelle (um 60): standing/polka_dots (gepunktete Bluse, lila Hose).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben
der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Serious/Smile“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe). Keine Bärte (Mund bleibt frei), keine Prothesen-Posen."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_024")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "KO": ("standing/crossed_arms-1", "Medium 3", None, None, {"Skin": "#E8B98F", "Top": "#FFFFFF"}, 1),
    "VO": ("standing/walking-3", "Short 2", None, None, {"Skin": "#C99470"}, 1),
    "GV": ("standing/blazer-4", "No Hair 2", None, "Glasses 3", {"Skin": "#D9A07A", "Jacket": "#3A3A48", "Top": "#FFFFFF"}, 1),
    "UB": ("standing/polka_dots", "Gray Medium", None, "Glasses 2", {"Skin": "#F0C8A8", "Pants": "#B8A9F5"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("KO_ruhig", "KO", "Calm", 0), ("KO_redet", "KO", "Driven", 1), ("KO_froh", "KO", "Smile", 0),
    ("KO_aerger", "KO", "Contempt", 0), ("KO_denkt", "KO", "Serious", 0), ("KO_sorge", "KO", "Concerned|Serious", 0),
    ("VO_ruhig", "VO", "Calm", 0), ("VO_redet", "VO", "Suspicious", 1), ("VO_trotz", "VO", "Contempt", 0),
    ("VO_schreck", "VO", "Fear", 0), ("VO_muede", "VO", "Tired", 0),
    ("GV_ruhig", "GV", "Calm", 0), ("GV_redet", "GV", "Serious", 1), ("GV_denkt", "GV", "Suspicious", 0),
    ("UB_ruhig", "UB", "Calm", 0), ("UB_redet", "UB", "Smile", 1),
]

if __name__ == "__main__":
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben, sp = P[p]
        for suffix, gespiegelt in (("", sp), ("_r", 1 - sp)):
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
