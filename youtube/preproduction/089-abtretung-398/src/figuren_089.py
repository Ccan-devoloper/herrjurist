"""Figuren für Folge 089 (Abtretung, § 398 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Ewald (um 58, Malermeister, Altgläubiger): standing/shirt-3 (weißes Hemd mit Brusttasche wie Malerkleidung, schwarze Hose),
Kopf Gray Short, kein Bart.
Tanja (um 32, Kundin und Schuldnerin): standing/easing-2 (grünes offenes Hemd, blaue Hose, Turnschuhe), Kopf Medium Bangs.
Sven (um 30, Sachbearbeiter im Inkassobüro, Neugläubiger-Seite): standing/walking-2 (schwarzes T-Shirt, lila Hose, Schrittpose), Kopf Short 4.
Keine Prothesen-Pose, keine Bärte, keine Karikatur, keine Täter-Klischees.
Posen und Farben nicht aus den Folgen 084–086 (blazer-3, resting-2, robot_dance-3, walking-1, crossed_arms-1); keine Polka Dots.
Präfix EW_/TA_/SV_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Awe bzw. „Augen|geschlossener Mund“
(Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (EW_redet, SV_redet, TA_redet, Lexi) zusätzlich mit a/o/e: Augen
der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_089")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

EW_F = {"Skin": "#E8B48F", "Top": "#F7F7F2"}
TA_F = {"Skin": "#B07552", "Jacket": "#8FD694", "Pants": "#8DB3F2"}
SV_F = {"Skin": "#F5D0B5", "Pants": "#B8A9F5"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "EW": ("standing/shirt-3", "Gray Short", None, None, EW_F),
    "TA": ("standing/easing-2", "Medium Bangs", None, None, TA_F),
    "SV": ("standing/walking-2", "Short 4", None, None, SV_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EW_ruhig", "EW", "Calm", 0), ("EW_redet", "EW", "Serious", 1), ("EW_froh", "EW", "Smile Big|Smile", 0),
    ("EW_sorge", "EW", "Concerned|Serious", 0), ("EW_denkt", "EW", "Suspicious", 0),
    ("TA_ruhig", "TA", "Calm", 0), ("TA_redet", "TA", "Serious", 1), ("TA_froh", "TA", "Smile Big|Smile", 0),
    ("TA_sorge", "TA", "Concerned|Serious", 0), ("TA_denkt", "TA", "Suspicious", 0), ("TA_staunt", "TA", "Awe", 0),
    ("SV_ruhig", "SV", "Calm", 0), ("SV_redet", "SV", "Serious", 1), ("SV_froh", "SV", "Smile Big|Smile", 0),
    ("SV_sorge", "SV", "Concerned|Serious", 0), ("SV_denkt", "SV", "Suspicious", 0),
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
