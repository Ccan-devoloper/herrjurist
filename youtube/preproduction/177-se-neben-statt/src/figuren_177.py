"""Figuren für Folge 177 (Schadensersatz neben oder statt der Leistung, Druckerei/Chip) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Elfriede (um 60, Inhaberin einer Druckerei, Käuferin): standing/blazer-3 (Blazer Lila #B8A9F5, schwarzes Oberteil der Pose,
Hose Dunkelblau #2E3550), Kopf Gray Bun (graues Haar, Dutt), Brille Glasses 2.
Dietrich (um 50, stellt Steuerchips her und verkauft sie, Verkäufer): standing/robot_dance-2 (schwarzes Oberteil der Pose,
Hose Khaki #C9A27A; die ausgestreckte Hand passt zum Angebot „neuer Chip“), Kopf Short 4, keine Brille.
Keine Bärte, keine Karikatur, keine Polka Dots.
Posen und Muster nicht aus den Folgen 174–176 (crossed_arms-1, crossed_arms-2, resting-2, shirt-4, easing-1,
pointing_finger-1, blazer-1, pointing_finger-2) und nicht wie 170 (robot_dance-3, blazer-2).
Präfix EL_/DI_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Tired bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (EL_bestimmt, DI_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_177")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

EL_F = {"Skin": "#F0CDB0", "Jacket": "#B8A9F5", "Pants": "#2E3550"}
DI_F = {"Skin": "#D9A07A", "Pants": "#C9A27A"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "EL": ("standing/blazer-3", "Gray Bun", None, "Glasses 2", EL_F),
    "DI": ("standing/robot_dance-2", "Short 4", None, None, DI_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EL_ruhig", "EL", "Calm", 0), ("EL_bestimmt", "EL", "Serious", 1), ("EL_sorge", "EL", "Concerned|Serious", 0),
    ("EL_staunt", "EL", "Awe", 0), ("EL_denkt", "EL", "Suspicious", 0), ("EL_froh", "EL", "Smile Big|Smile", 0),
    ("EL_laechelt", "EL", "Smile", 0),
    ("DI_ruhig", "DI", "Calm", 0), ("DI_redet", "DI", "Smile", 1), ("DI_sorge", "DI", "Concerned|Serious", 0),
    ("DI_denkt", "DI", "Suspicious", 0), ("DI_ernst", "DI", "Serious", 0), ("DI_muede", "DI", "Tired", 0),
    ("DI_froh", "DI", "Smile Big|Smile", 0),
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
