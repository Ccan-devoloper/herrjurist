"""Figuren für Folge 051 (Diebstahl § 242 Schema, Lesesaal der Unibibliothek) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Antje (Studentin, Anfang 20): standing/easing-2 (offenes Hemd Grün über schwarzem Top, Hose Blau), Kopf „Long Curly“.
Matthias (Student, Anfang 20): standing/walking-2 (schwarzes T-Shirt der Pose, Hose Lila; geht mit der Hand in der
    Tasche), Kopf „Short 2“. Keine Prothese, kein Bart, keine Waffe.
Je Person eine Pose (Outfit konstant). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (zur Tafel), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Suspicious, Driven, Fear, Awe
bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile). Sprechende Ansichten zusätzlich mit
a/o/e (Augen der Grundmimik + Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_051")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

AN_F = {"Skin": "#F0C8A8", "Jacket": "#8FD694", "Pants": "#8DB3F2"}
MA_F = {"Skin": "#D9A27A", "Pants": "#B8A9F5"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "AN": ("standing/easing-2", "Long Curly", None, None, AN_F),
    "MA": ("standing/walking-2", "Short 2", None, None, MA_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("AN_ruhig", "AN", "Calm", 0), ("AN_redet", "AN", "Concerned|Serious", 1), ("AN_froh", "AN", "Smile", 0),
    ("AN_erschrickt", "AN", "Fear", 0), ("AN_denkt", "AN", "Serious", 0), ("AN_skeptisch", "AN", "Suspicious", 0),
    ("AN_staunt", "AN", "Awe", 0),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Cheeky|Smile", 1), ("MA_ehrlich", "MA", "Smile", 1),
    ("MA_listig", "MA", "Suspicious", 0), ("MA_froh", "MA", "Smile", 0), ("MA_entschlossen", "MA", "Driven", 0),
    ("MA_denkt", "MA", "Serious", 0), ("MA_ertappt", "MA", "Fear", 0), ("MA_sorge", "MA", "Concerned|Serious", 0),
    ("MA_staunt", "MA", "Awe", 0),
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
