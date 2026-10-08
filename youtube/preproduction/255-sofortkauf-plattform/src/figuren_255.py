"""Figuren für Folge 255 („Sofort kaufen“ geklickt) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Eichler (EI, um 50, privater Verkäufer; Stimme stephan): standing/robot_dance-3 (Pullover Blau #8DB3F2, Hose Grau
#5A5F6E), Kopf Short 3, Brille Glasses 3, Haut #E3B48C, kein Bart – sachlich, keine Karikatur.
Frau Hegemann (HE, um 30, Käuferin; Stimme lucy): standing/blazer-4 (Blazer Lila #B8A9F5, Shirt Weiß, schwarze Hose der Pose),
Kopf Medium Straight, Haut #D9A27E, keine Brille. Bewusst kein Dutt (Verwechslung mit Lexi).
Posen nicht aus den letzten Folgen 251–254 (easing-1, resting-1/2, pointing_finger-2, blazer-3, walking-1/2, robot_dance-2,
crossed_arms-1, shirt-3); keine Polka Dots, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2), keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix EI_/HE_ (nie ER_). Beide Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (EI_redet, HE_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_255")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "EI": ("standing/robot_dance-3", "Short 3", None, "Glasses 3", {"Skin": "#E3B48C", "Top": "#8DB3F2", "Pants": "#5A5F6E"}),
    "HE": ("standing/blazer-4", "Medium Straight", None, None, {"Skin": "#D9A27E", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}),
}

LISTE = [
    ("EI_ruhig", "EI", "Calm", 0), ("EI_redet", "EI", "Concerned|Serious", 1), ("EI_froh", "EI", "Smile", 0),
    ("EI_denkt", "EI", "Suspicious", 0), ("EI_ernst", "EI", "Serious", 0), ("EI_sorge", "EI", "Concerned|Serious", 0),
    ("EI_schreck", "EI", "Fear", 0), ("EI_staunt", "EI", "Awe", 0), ("EI_still", "EI", "Solemn", 0),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Driven", 1), ("HE_froh", "HE", "Smile", 0),
    ("HE_strahlt", "HE", "Smile Big|Smile", 0), ("HE_denkt", "HE", "Suspicious", 0), ("HE_ernst", "HE", "Serious", 0),
    ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_staunt", "HE", "Awe", 0),
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
