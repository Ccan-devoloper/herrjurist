"""Figuren für Folge 142 (§ 1004 BGB, Äste auf dem Garagendach) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Franziska (um 35, Garageneigentümerin): standing/easing-2 (hellblaues offenes Hemd über schwarzem Oberteil, gelbe Hose,
weiße Turnschuhe), Kopf Medium Bangs, Haut #E8B48C.
Rosemarie (um 70, Nachbarin mit dem Ahorn): standing/resting-2 (schwarzes Oberteil, grüne Hose #8FD694, schwarze Schuhe),
Kopf Gray Bun, Haut #F2CDB0, Augenpartie „Old“ (geschlossener Mund).
Je Person eine Pose (Outfit konstant). Keine Prothesen-Posen, keine Bärte, keine Karikatur. Posen, Kleidung und Muster nicht
aus den Folgen 139–141 (blazer-3, blazer-4, crossed_arms-1, crossed_arms-2, easing-1, pointing_finger-2, robot_dance-2,
robot_dance-3, walking-1); keine Polka Dots. Präfixe FR_/RO_ (nie ER_, bausteine.peep_voll leitet ER_* nach op_we um).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Old, Serious, Smile, Suspicious bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (FR_redet, FR_bittet, RO_redet, RO_meint, Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_142")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

FR_F = {"Skin": "#E8B48C"}
RO_F = {"Skin": "#F2CDB0", "Pants": "#8FD694"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "FR": ("standing/easing-2", "Medium Bangs", None, None, FR_F),
    "RO": ("standing/resting-2", "Gray Bun", None, None, RO_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FR_ruhig", "FR", "Calm", 0), ("FR_redet", "FR", "Smile", 1), ("FR_bittet", "FR", "Serious", 1),
    ("FR_froh", "FR", "Smile Big|Smile", 0), ("FR_sorge", "FR", "Concerned|Serious", 0), ("FR_denkt", "FR", "Suspicious", 0),
    ("RO_ruhig", "RO", "Old", 0), ("RO_redet", "RO", "Smile", 1), ("RO_meint", "RO", "Calm", 1),
    ("RO_froh", "RO", "Smile Big|Smile", 0), ("RO_sorge", "RO", "Concerned|Serious", 0), ("RO_denkt", "RO", "Suspicious", 0),
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
