"""Figuren für Folge 170 (Unmöglichkeit § 275 BGB, Oldtimer) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Waldemar (um 55, privater Verkäufer, Schuldner): standing/robot_dance-3 (Oberteil Blau #8DB3F2, Hose Dunkelgrau #4A4A58;
die offene Hand passt zum Erklären am Wagen), Kopf Short 2 (kurzes dunkles Haar), Brille Glasses, kein Bart.
Adelheid (um 65, private Käuferin, Gläubigerin): standing/blazer-2 (Blazer Grün #8FD694, Oberteil Weiß; Pose mit
Beinprothese, die Käuferin ist keine Täterrolle), Kopf Gray Medium (graues Haar), Brille Glasses 2.
Keine Bärte, keine Karikatur, keine Polka Dots.
Posen, Farben und Muster nicht aus den Folgen 167–169 (resting-1, blazer-1, crossed_arms-1, blazer-4, pointing_finger-1,
doctor-nurse-02, shirt-4) und nicht aus 166 (resting-2, pointing_finger-2, blazer-3, walking-1).
Präfix WA_/AD_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Fear, Tired bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (WA_redet, WA_sorge_redet, AD_redet,
AD_bestimmt, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_170")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

WA_F = {"Skin": "#E8B48E", "Top": "#8DB3F2", "Pants": "#4A4A58"}
AD_F = {"Skin": "#F0CDB0", "Jacket": "#8FD694", "Top": "#FFFFFF", "Hair": "#BDBDBD"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WA": ("standing/robot_dance-3", "Short 2", None, "Glasses", WA_F),
    "AD": ("standing/blazer-2", "Gray Medium", None, "Glasses 2", AD_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WA_ruhig", "WA", "Calm", 0), ("WA_redet", "WA", "Smile", 1), ("WA_sorge", "WA", "Concerned|Serious", 0),
    ("WA_sorge_redet", "WA", "Concerned|Serious", 1), ("WA_schreck", "WA", "Fear", 0), ("WA_muede", "WA", "Tired", 0),
    ("WA_denkt", "WA", "Suspicious", 0), ("WA_froh", "WA", "Smile Big|Smile", 0), ("WA_ernst", "WA", "Serious", 0),
    ("AD_ruhig", "AD", "Calm", 0), ("AD_redet", "AD", "Smile", 1), ("AD_bestimmt", "AD", "Serious", 1),
    ("AD_sorge", "AD", "Concerned|Serious", 0), ("AD_staunt", "AD", "Awe", 0), ("AD_denkt", "AD", "Suspicious", 0),
    ("AD_froh", "AD", "Smile Big|Smile", 0),
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
