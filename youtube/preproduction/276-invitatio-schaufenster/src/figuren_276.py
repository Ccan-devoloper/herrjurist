"""Figuren für Folge 276 (Invitatio ad offerendum: Preis im Schaufenster) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Edelgard (ED, um 65, Kundin; Stimme hilde): standing/easing-2 (offene Jacke Rot #F07A6A, Shirt schwarz der Pose, Hose Grau
#5A5F6E), Kopf Gray Medium, Brille Glasses 4, Haut #F0C8A8 – kein Dutt (Abgrenzung zu Lexi).
Herr Böckmann (BO, um 45, Inhaber des Modegeschäfts; Stimme christian): standing/pointing_finger-2 (Pullover schwarz der Pose, Hose
Blau #8DB3F2), Kopf Short 2, Haut #C9946B, keine Brille, kein Bart – sachlich, keine Karikatur.
Posen nicht aus den letzten Folgen 270–273 und 251/255 (resting-1/2, robot_dance-1/2/3, blazer-3/4, easing-1, crossed_arms-1/2,
shirt-4); keine Polka Dots, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2), keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix ED_/BO_ (nie ER_). Beide Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (ED_redet, ED_beharrt, BO_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_276")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "ED": ("standing/easing-2", "Gray Medium", None, "Glasses 4", {"Skin": "#F0C8A8", "Hair": "#D2D2D2", "Jacket": "#F07A6A", "Pants": "#5A5F6E"}),
    "BO": ("standing/pointing_finger-2", "Short 2", None, None, {"Skin": "#C9946B", "Pants": "#8DB3F2"}),
}

LISTE = [
    ("ED_ruhig", "ED", "Calm", 0), ("ED_redet", "ED", "Smile", 1), ("ED_beharrt", "ED", "Driven", 1),
    ("ED_froh", "ED", "Smile", 0), ("ED_strahlt", "ED", "Smile Big|Smile", 0), ("ED_staunt", "ED", "Awe", 0),
    ("ED_denkt", "ED", "Suspicious", 0), ("ED_ernst", "ED", "Serious", 0), ("ED_sorge", "ED", "Concerned|Serious", 0),
    ("ED_still", "ED", "Solemn", 0),
    ("BO_ruhig", "BO", "Calm", 0), ("BO_redet", "BO", "Concerned|Serious", 1), ("BO_froh", "BO", "Smile", 0),
    ("BO_denkt", "BO", "Suspicious", 0), ("BO_ernst", "BO", "Serious", 0), ("BO_sorge", "BO", "Concerned|Serious", 0),
    ("BO_schreck", "BO", "Fear", 0), ("BO_still", "BO", "Solemn", 0),
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
