"""Figuren für Folge 095 (Abnahme Werkvertrag, § 640 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Susanne (um 40, Verbraucherin, lässt ihr Bad sanieren): standing/easing-2 (korallrote offene Jacke über schwarzem Shirt,
dunkelblaue Hose, weiße Turnschuhe), Kopf Medium Bangs 2 (braun), keine Brille.
Herr Fiedler (um 50, Fliesenleger, Unternehmer): standing/shirt-3 (blaues Arbeitshemd, schwarze Hose), Kopf Gray Short.
Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Posen, Farben und Köpfe nicht aus den Folgen 091–093 (robot_dance-2/-3, shirt-4, walking-1, resting-1/-2,
crossed_arms-1, blazer-3, pointing_finger-1); keine Polka Dots.
Präfix SU_/FI_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (SU_redet, FI_redet, Lexi) zusätzlich mit a/o/e: Augen
der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_095")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

SU_F = {"Skin": "#F2C9A5", "Jacket": "#F07A6A", "Pants": "#3D4A7A", "Hair": "#7A4B2E"}
FI_F = {"Skin": "#E0A57E", "Top": "#5B7DB8", "Hair": "#BDBDBD"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "SU": ("standing/easing-2", "Medium Bangs 2", None, None, SU_F),
    "FI": ("standing/shirt-3", "Gray Short", None, None, FI_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SU_ruhig", "SU", "Calm", 0), ("SU_redet", "SU", "Serious", 1), ("SU_froh", "SU", "Smile Big|Smile", 0),
    ("SU_sorge", "SU", "Concerned|Serious", 0), ("SU_denkt", "SU", "Suspicious", 0), ("SU_staunt", "SU", "Awe", 0),
    ("FI_ruhig", "FI", "Calm", 0), ("FI_redet", "FI", "Smile", 1), ("FI_froh", "FI", "Smile Big|Smile", 0),
    ("FI_sorge", "FI", "Concerned|Serious", 0), ("FI_denkt", "FI", "Suspicious", 0), ("FI_ernst", "FI", "Serious", 0),
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
