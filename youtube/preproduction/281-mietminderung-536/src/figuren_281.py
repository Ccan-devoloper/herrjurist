"""Figuren für Folge 281 (Mietminderung § 536 BGB: Schimmel, Baulärm, kalte Heizung) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Friedemann (FR, um 35, Mieter; Stimme christian): standing/shirt-4 (Hemd schwarz der Pose, Hose Blau #8DB3F2), Kopf Short 3,
Haut #E8B894, keine Brille, kein Bart.
Frau Teuber (TB, um 60, Vermieterin; Stimme hilde): standing/resting-1 (Pullover Orange #F9A66C, Hose schwarz der Pose),
Kopf Gray Short (Haar #D2D2D2), Haut #F0C8A8, Brille Glasses 3 – ruhig, sachlich, keine Karikatur (Hände locker, kein Zeigefinger,
keine verschränkten Arme).
Posen nicht aus den letzten drei Folgen 278–280 (walking-1, blazer-3, robot_dance-3, mid-2, blazer-4; 280 laut Ordner
noch nicht im Repository) und nicht aus 276/277 (easing-1/-2, pointing_finger-2, blazer-2); keine Polka Dots, keine
Prothesen-Posen (shirt-1/-2, blazer-1/-2), keine Bärte. Lexi nach lexi.py (robot_dance-1).
Präfix FR_/TB_ (nie ER_). Beide Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (FR_redet, TB_redet, Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_281")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "FR": ("standing/shirt-4", "Short 3", None, None, {"Skin": "#E8B894", "Pants": "#8DB3F2"}),
    "TB": ("standing/resting-1", "Gray Short", None, "Glasses 3", {"Skin": "#F0C8A8", "Top": "#F9A66C", "Hair": "#D2D2D2"}),
}

LISTE = [
    ("FR_ruhig", "FR", "Calm", 0), ("FR_redet", "FR", "Serious", 1), ("FR_froh", "FR", "Smile", 0),
    ("FR_schreck", "FR", "Fear", 0), ("FR_staunt", "FR", "Awe", 0), ("FR_denkt", "FR", "Suspicious", 0),
    ("FR_ernst", "FR", "Serious", 0), ("FR_sorge", "FR", "Concerned|Serious", 0), ("FR_muede", "FR", "Tired", 0),
    ("FR_erleichtert", "FR", "Smile Big|Smile", 0), ("FR_still", "FR", "Solemn", 0),
    ("TB_ruhig", "TB", "Calm", 0), ("TB_redet", "TB", "Serious", 1), ("TB_froh", "TB", "Smile", 0),
    ("TB_denkt", "TB", "Suspicious", 0), ("TB_ernst", "TB", "Serious", 0), ("TB_sorge", "TB", "Concerned|Serious", 0),
    ("TB_staunt", "TB", "Awe", 0),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
