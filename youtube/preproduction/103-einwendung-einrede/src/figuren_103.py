"""Figuren für Folge 103 (Einwendung und Einrede, Werklohn eines Tischlers) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Tilda (31, Kundin/Bestellerin): standing/easing-1 (offenes lila Hemd über blauem Shirt, schwarze Hose, Turnschuhe),
Kopf Medium 2, keine Brille.
Herr Grünwald (um 55, Tischler, Unternehmer): standing/pointing_finger-2 (schwarzer Pullover, blaue Arbeitshose, Stiefel,
Zeigefinger erhoben), Kopf No Hair 1, Brille Glasses.
Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Posen, Farben und Köpfe nicht aus den Folgen 100–102 (robot_dance-2/-3, crossed_arms-1, pointing_finger-1, polka_dots,
shirt-3, easing-2); keine Polka Dots.
Präfix TI_/GR_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious, Cheeky|Smile). Sprechende Ansichten (TI_redet, GR_redet, GR_fordert, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_103")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

TI_F = {"Skin": "#F3CDB0", "Jacket": "#B8A9F5"}
GR_F = {"Skin": "#E3AE88", "Pants": "#3F5E8C"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "TI": ("standing/easing-1", "Medium 2", None, None, TI_F),
    "GR": ("standing/pointing_finger-2", "No Hair 1", None, "Glasses", GR_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TI_ruhig", "TI", "Calm", 0), ("TI_redet", "TI", "Serious", 1), ("TI_froh", "TI", "Smile Big|Smile", 0),
    ("TI_sorge", "TI", "Concerned|Serious", 0), ("TI_denkt", "TI", "Suspicious", 0), ("TI_staunt", "TI", "Awe", 0),
    ("TI_frech", "TI", "Cheeky|Smile", 0),
    ("GR_ruhig", "GR", "Calm", 0), ("GR_redet", "GR", "Smile", 1), ("GR_fordert", "GR", "Serious", 1),
    ("GR_froh", "GR", "Smile Big|Smile", 0), ("GR_sorge", "GR", "Concerned|Serious", 0), ("GR_denkt", "GR", "Suspicious", 0),
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
