"""Figuren für Folge 259 (Taschengeldparagraph, Ratenkauf) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle
Figuren fiktiv.
Fridolin (FR, 16, Schüler, Käufer; spricht nicht): standing/blazer-4 als offene Jacke (Grün #8FD694, Shirt Weiß, schwarze
Hose der Pose), Kopf Short 5, Haut #F0C8A8; auf dem Rad sitting/bike (gleiche Jacke, Shirt, Hose; Rahmen Lila #B8A9F5).
Sympathisch: Mimiken Calm/Smile/Smile Big|Smile/Suspicious/Concerned|Serious/Awe – keine Bloßstellung.
Herr Heinemann (HN, um 60, Inhaber eines Radladens; Stimme william): standing/resting-1 (Pullover Blau #8DB3F2, schwarze
Hose der Pose), Kopf Gray Short, Haut #E3B48C, keine Brille, kein Bart.
Mutter (MU, um 45, gesetzliche Vertreterin, zugleich für den Vater; Stimme laura_ruhig): standing/crossed_arms-1
(Oberteil Lila #B8A9F5, schwarze Hose der Pose), Kopf Long, Haut #F0C8A8 (wie Fridolin). Kein Dutt (Lexi).
Posen nicht aus den letzten drei Folgen 256–258 (easing-1/-2, walking-2/-3, resting-2, shirt-4, robot_dance-2,
pointing_finger-2, crossed_arms-2, blazer-3); keine Polka Dots, keine Prothesen-Posen, keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix FR_/HN_/MU_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (HN_redet, MU_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_259")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
FR_F = {"Skin": "#F0C8A8", "Jacket": "#8FD694", "Top": "#FFFFFF", "Bicycle Frame": "#B8A9F5"}

P = {
    "FR": ("standing/blazer-4", "Short 5", None, None, FR_F),
    "FB": ("sitting/bike", "Short 5", None, None, FR_F),
    "HN": ("standing/resting-1", "Gray Short", None, None, {"Skin": "#E3B48C", "Top": "#8DB3F2"}),
    "MU": ("standing/crossed_arms-1", "Long", None, None, {"Skin": "#F0C8A8", "Top": "#B8A9F5"}),
}

LISTE = [
    ("FR_ruhig", "FR", "Calm", 0), ("FR_froh", "FR", "Smile", 0), ("FR_strahlt", "FR", "Smile Big|Smile", 0),
    ("FR_denkt", "FR", "Suspicious", 0), ("FR_sorge", "FR", "Concerned|Serious", 0), ("FR_ernst", "FR", "Serious", 0),
    ("FR_staunt", "FR", "Awe", 0), ("FR_muede", "FR", "Tired", 0),
    ("FR_rad", "FB", "Smile Big|Smile", 0),
    ("HN_ruhig", "HN", "Calm", 0), ("HN_redet", "HN", "Smile", 1), ("HN_froh", "HN", "Smile", 0),
    ("HN_denkt", "HN", "Suspicious", 0), ("HN_ernst", "HN", "Serious", 0), ("HN_sorge", "HN", "Concerned|Serious", 0),
    ("MU_ruhig", "MU", "Calm", 0), ("MU_redet", "MU", "Serious", 1), ("MU_ernst", "MU", "Serious", 0),
    ("MU_denkt", "MU", "Suspicious", 0), ("MU_sorge", "MU", "Concerned|Serious", 0), ("MU_froh", "MU", "Smile", 0),
    ("MU_staunt", "MU", "Awe", 0),
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
