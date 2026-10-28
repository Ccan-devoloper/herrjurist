"""Figuren für Folge 092 (§ 985 BGB, Herausgabeanspruch) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Theresa (um 30, Eigentümerin des Plattenspielers): Reihe „-2“ (schwarzes Oberteil, rote Hose `#F07A6A`):
standing/resting-2 (alle Ansichten); Kopf Bun 2.
Clemens (um 30, Ex-Partner, Besitzer): Reihe „-1“ (lila Pullover `#B8A9F5`, schwarze Hose): standing/resting-1 (ruhig, redet,
meint, froh, Sorge), standing/crossed_arms-1 (denkt); Kopf Short 5. Keine Prothesen-Posen, keine Bärte, keine Karikatur.
Posen, Kleidung und Muster nicht aus den Folgen 089–091 (shirt-3, easing-2, walking-2, easing-1, crossed_arms-2, blazer-4,
robot_dance-3, shirt-4, walking-1). Präfixe TH_/CL_ (nie ER_, bausteine.peep_voll leitet ER_* nach op_we um).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious bzw. „Augen|geschlossener Mund“
(Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (TH_redet, TH_bittet, CL_redet, CL_meint, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_092")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

TH_F = {"Skin": "#F2CDB0", "Pants": "#F07A6A"}
CL_F = {"Skin": "#C68E68", "Top": "#B8A9F5"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "TH": ("standing/resting-2", "Bun 2", None, None, TH_F),
    "CL": ("standing/resting-1", "Short 5", None, None, CL_F),
    "CL_A": ("standing/crossed_arms-1", "Short 5", None, None, CL_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TH_ruhig", "TH", "Calm", 0), ("TH_redet", "TH", "Smile", 1), ("TH_bittet", "TH", "Serious", 1),
    ("TH_froh", "TH", "Smile Big|Smile", 0), ("TH_sorge", "TH", "Concerned|Serious", 0), ("TH_denkt", "TH", "Suspicious", 0),
    ("CL_ruhig", "CL", "Calm", 0), ("CL_redet", "CL", "Smile", 1), ("CL_meint", "CL", "Calm", 1),
    ("CL_froh", "CL", "Smile Big|Smile", 0), ("CL_sorge", "CL", "Concerned|Serious", 0), ("CL_denkt", "CL_A", "Suspicious", 0),
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
