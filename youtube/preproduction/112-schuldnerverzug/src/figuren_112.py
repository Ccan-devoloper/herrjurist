"""Figuren für Folge 112 (Schuldnerverzug, Fahrradwerkstatt) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Klara (um 35, Inhaberin einer Fahrradwerkstatt mit Laden, Unternehmerin, Gläubigerin): standing/pointing_finger-2
(schwarzes Oberteil, Arbeitshose Blau #8DB3F2, feste Schuhe; der erhobene Zeigefinger passt zur Zahlungsaufforderung),
Kopf Medium Bangs 3, keine Brille.
Gustav (um 65, privater Kunde, Verbraucher, Schuldner): standing/walking-1 (T-Shirt Türkis #7FD6D0, schwarze Hose,
Turnschuhe), Kopf Gray Short, Brille Glasses 2, kein Bart (nichts über dem Mund).
Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Posen, Farben und Muster nicht aus den Folgen 107–109 (shirt-3, resting-2, blazer-3, robot_dance-3, pointing_finger-1,
crossed_arms-1, easing-2, walking-3); keine Polka Dots.
Präfix KL_/GU_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Tired bzw. „Augen|
geschlossener Mund“ (Smile Big|Smile, Concerned|Serious, Cheeky|Smile). Sprechende Ansichten (KL_redet, GU_redet, GU_frech,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_112")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

KL_F = {"Skin": "#B97E58", "Pants": "#8DB3F2"}
GU_F = {"Skin": "#F2D0B1", "Top": "#7FD6D0", "Hair": "#C8C8C8"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KL": ("standing/pointing_finger-2", "Medium Bangs 3", None, None, KL_F),
    "GU": ("standing/walking-1", "Gray Short", None, "Glasses 2", GU_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KL_ruhig", "KL", "Calm", 0), ("KL_redet", "KL", "Serious", 1), ("KL_froh", "KL", "Smile Big|Smile", 0),
    ("KL_sorge", "KL", "Concerned|Serious", 0), ("KL_denkt", "KL", "Suspicious", 0),
    ("GU_ruhig", "GU", "Calm", 0), ("GU_redet", "GU", "Smile", 1), ("GU_frech", "GU", "Cheeky|Smile", 1),
    ("GU_froh", "GU", "Smile Big|Smile", 0), ("GU_sorge", "GU", "Concerned|Serious", 0), ("GU_denkt", "GU", "Suspicious", 0),
    ("GU_staunt", "GU", "Awe", 0), ("GU_muede", "GU", "Tired", 0),
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
