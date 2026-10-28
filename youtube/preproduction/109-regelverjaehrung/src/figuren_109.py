"""Figuren für Folge 109 (Regelverjährung, Darlehen unter Freunden) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Pia (um 28, Darlehensnehmerin, Schuldnerin): standing/easing-2 (offenes Hemd Koralle #F07A6A über schwarzem Shirt,
Hose Gelb #F9D56E, Turnschuhe), Kopf Long Bangs, keine Brille.
Finn (um 28, guter Freund, Darlehensgeber, Gläubiger): standing/walking-3 (schwarzes T-Shirt, schwarze Hose, weiße
Turnschuhe; die Pose hat keine einfärbbaren Kleidungsflächen), Kopf Short 3, keine Brille.
Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Posen, Farben und Muster nicht aus den Folgen 105–107 (resting-1/-2, walking-2, blazer-2/-3/-4, crossed_arms-2, shirt-3);
keine Polka Dots (102).
Präfix PI_/FI_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious, Cheeky|Smile). Sprechende Ansichten (PI_redet, PI_frech, FI_redet, FI_fordert,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_109")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

PI_F = {"Skin": "#F1C9A5", "Jacket": "#F07A6A", "Pants": "#F9D56E"}
FI_F = {"Skin": "#D8A47F"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "PI": ("standing/easing-2", "Long Bangs", None, None, PI_F),
    "FI": ("standing/walking-3", "Short 3", None, None, FI_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("PI_ruhig", "PI", "Calm", 0), ("PI_redet", "PI", "Smile", 1), ("PI_frech", "PI", "Cheeky|Smile", 1),
    ("PI_froh", "PI", "Smile Big|Smile", 0), ("PI_sorge", "PI", "Concerned|Serious", 0), ("PI_denkt", "PI", "Suspicious", 0),
    ("PI_staunt", "PI", "Awe", 0),
    ("FI_ruhig", "FI", "Calm", 0), ("FI_redet", "FI", "Smile", 1), ("FI_fordert", "FI", "Serious", 1),
    ("FI_froh", "FI", "Smile Big|Smile", 0), ("FI_sorge", "FI", "Concerned|Serious", 0), ("FI_denkt", "FI", "Suspicious", 0),
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
