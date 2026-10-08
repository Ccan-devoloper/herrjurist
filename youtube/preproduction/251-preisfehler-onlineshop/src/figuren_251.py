"""Figuren für Folge 251 (Preisfehler im Onlineshop) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Kübler (KU, um 35, Käufer; Stimme marc): standing/easing-1 (offenes Hemd Grün #8FD694, Shirt Weiß, schwarze Hose der
Pose), Kopf Short 1, Haut #C99470, kein Bart, keine Brille.
Frau Wetzel (WE, um 45, Händlerin mit kleinem Onlineshop; Stimme sabrina): standing/resting-2 (schwarzes Oberteil der Pose,
Hose Rot #F07A6A), Kopf Medium Bangs 2, Brille Glasses 4, Haut #F2C9A6 – sachlich, keine Karikatur. Bewusst kein Dutt
(Verwechslung mit Lexi).
Posen nicht aus den letzten drei Folgen 248–250 (blazer-2/3/4, pointing_finger-2, crossed_arms-1/2, easing-2, shirt-3/4,
resting-1); keine Polka Dots, keine Prothesen-Posen (blazer-1 und shirt-1 mit Beinprothese verworfen), keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix KU_/WE_ (nie ER_). Beide Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (KU_redet, WE_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_251")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "KU": ("standing/easing-1", "Short 1", None, None, {"Skin": "#C99470", "Jacket": "#8FD694", "Top": "#FFFFFF"}),
    "WE": ("standing/resting-2", "Medium Bangs 2", None, "Glasses 4", {"Skin": "#F2C9A6", "Pants": "#F07A6A"}),
}

LISTE = [
    ("KU_ruhig", "KU", "Calm", 0), ("KU_redet", "KU", "Driven", 1), ("KU_froh", "KU", "Smile", 0),
    ("KU_strahlt", "KU", "Smile Big|Smile", 0), ("KU_staunt", "KU", "Awe", 0), ("KU_denkt", "KU", "Suspicious", 0),
    ("KU_ernst", "KU", "Serious", 0), ("KU_sorge", "KU", "Concerned|Serious", 0),
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Serious", 1), ("WE_froh", "WE", "Smile", 0),
    ("WE_denkt", "WE", "Suspicious", 0), ("WE_ernst", "WE", "Serious", 0), ("WE_sorge", "WE", "Concerned|Serious", 0),
    ("WE_schreck", "WE", "Fear", 0), ("WE_tippt", "WE", "Driven", 0),
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
