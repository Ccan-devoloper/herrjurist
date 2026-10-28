"""Figuren für Folge 033 (Notwehr-Schema, Tasche vor der Stadtbibliothek) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Ulrike (Mitte 40, Angegriffene): standing/easing-1, Kopf Medium Bangs, Jacke Lila, Oberteil Grün.
Torsten (Mitte 20, Angreifer): standing/robot_dance-3 (greifender Arm), Kopf Short 4, Oberteil Orange.
Herr Kluge (um 70, Passant): standing/shirt-4, Kopf No Hair 1, Brille Glasses 2, Hose Blau.
Je Person eine Pose (Outfit konstant). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r nach rechts. Keine Bärte, keine Prothesen-Posen.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Driven, Fear, Tired, Suspicious bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten zusätzlich mit a/o/e (Augen der Grundmimik +
Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_033")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

UL_F = {"Skin": "#E8B894", "Jacket": "#B8A9F5", "Top": "#8FD694"}
TO_F = {"Skin": "#F0C8A8", "Top": "#F9A66C", "Pants": "#4A4A5E"}
KL_F = {"Skin": "#E0B48E", "Pants": "#8DB3F2"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "UL": ("standing/easing-1", "Medium Bangs", None, None, UL_F),
    "TO": ("standing/robot_dance-3", "Short 4", None, None, TO_F),
    "KL": ("standing/shirt-4", "No Hair 1", None, "Glasses 2", KL_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("UL_ruhig", "UL", "Calm", 0), ("UL_schreck", "UL", "Fear", 0), ("UL_fest", "UL", "Driven", 0),
    ("UL_redet", "UL", "Driven", 1), ("UL_denkt", "UL", "Serious", 0), ("UL_froh", "UL", "Smile", 0),
    ("UL_sorge", "UL", "Concerned|Serious", 0),
    ("TO_ruhig", "TO", "Calm", 0), ("TO_gier", "TO", "Driven", 0), ("TO_redet", "TO", "Rage|Serious", 1),
    ("TO_wut", "TO", "Rage|Serious", 0), ("TO_schmerz", "TO", "Concerned|Serious", 0), ("TO_muede", "TO", "Tired", 0),
    ("TO_denkt", "TO", "Suspicious", 0),
    ("KL_ruhig", "KL", "Calm", 0), ("KL_redet", "KL", "Concerned|Serious", 1), ("KL_ernst", "KL", "Serious", 0),
    ("KL_schreck", "KL", "Fear", 0),
]

if __name__ == "__main__":
    n = 0
    for name, v, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[v]
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
