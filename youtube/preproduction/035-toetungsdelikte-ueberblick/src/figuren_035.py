"""Figuren für Folge 035 (Tötungsdelikte Überblick, Lerngruppe in der Unibibliothek) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0).
Britta (Studentin, Anfang 20): standing/crossed_arms-2, Kopf Long Bangs, Hose Lila (Oberteil der Pose ist Tusche/schwarz).
Florian (Student, Mitte 20): standing/shirt-1, Kopf Short 3, Hemd Grün, Beinprothese der Originalpose (kein Täter).
Je Person eine Pose (Outfit konstant). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (zur Tafel), Suffix _r nach rechts. Keine Bärte.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Suspicious, Awe, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e (Augen der Grundmimik +
Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_035")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

BR_F = {"Skin": "#F0C8A8", "Pants": "#B8A9F5"}
FL_F = {"Skin": "#D9A27A", "Top": "#8FD694"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BR": ("standing/crossed_arms-2", "Long Bangs", None, None, BR_F),
    "FL": ("standing/shirt-1", "Short 3", None, None, FL_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Concerned|Serious", 1), ("BR_denkt", "BR", "Serious", 0),
    ("BR_skeptisch", "BR", "Suspicious", 0), ("BR_froh", "BR", "Smile", 0), ("BR_staunt", "BR", "Awe", 0),
    ("BR_sorge", "BR", "Concerned|Serious", 0),
    ("FL_ruhig", "FL", "Calm", 0), ("FL_redet", "FL", "Smile", 1), ("FL_fragt", "FL", "Suspicious", 1),
    ("FL_denkt", "FL", "Serious", 0), ("FL_froh", "FL", "Smile", 0), ("FL_staunt", "FL", "Awe", 0),
    ("FL_muede", "FL", "Tired", 0),
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
