"""Figuren für Folge 029 (Vorsatzformen, Gartenmauer und Nachbarzaun) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Volker (Hausbesitzer, Anfang 60): standing/shirt-3, Kopf Gray Short, Brille Glasses 3, Hemd Blau, Hose dunkel.
Heike (Nachbarin, um 45): standing/resting-1, Kopf Medium Straight, Oberteil Lila.
Je Person eine Pose (Outfit konstant). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r nach rechts. Keine Bärte.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Driven, Contempt, Fear, Tired, Suspicious bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e (Augen der Grundmimik +
Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_029")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

VO_F = {"Skin": "#F0C8A8", "Top": "#8DB3F2", "Pants": "#4A4A5E"}
HE_F = {"Skin": "#D9A27A", "Top": "#B8A9F5"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "VO": ("standing/shirt-3", "Gray Short", None, "Glasses 3", VO_F),
    "HE": ("standing/resting-1", "Medium Straight", None, None, HE_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("VO_ruhig", "VO", "Calm", 0), ("VO_redet", "VO", "Calm", 1), ("VO_arbeit", "VO", "Driven", 0),
    ("VO_grimmig", "VO", "Driven", 1), ("VO_bedauert", "VO", "Concerned|Serious", 1), ("VO_egal", "VO", "Contempt", 1),
    ("VO_zuversicht", "VO", "Smile", 1), ("VO_schreck", "VO", "Fear", 0), ("VO_denkt", "VO", "Serious", 0),
    ("VO_froh", "VO", "Smile", 0), ("VO_ertappt", "VO", "Concerned|Serious", 0),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Concerned|Serious", 1), ("HE_ruft", "HE", "Fear", 1),
    ("HE_traurig", "HE", "Tired", 0), ("HE_skeptisch", "HE", "Suspicious", 0),
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
