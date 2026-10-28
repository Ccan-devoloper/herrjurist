"""Figuren für Folge 262 (Unfallwagen verschwiegen: arglistige Täuschung oder Mängelrechte?) aus der LexVerse-Figma-
Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Angelika (AN, um 40, selbständige Hebamme, Käuferin; Stimme sabrina): standing/easing-1 als offene rote Hemdjacke
(#F07A6A) über weißem Shirt, schwarze Hose der Pose, Kopf Medium Straight, Haut #EBC2A0. Kein Dutt (Lexi).
Herr Hecker (HK, um 50, Gebrauchtwagenhändler, Verkäufer; Stimme marc): standing/blazer-3 (Sakko Blau #8DB3F2, Hose
Schiefer #3D4A5C), Kopf Short 3, Haut #E3B48C, keine Brille, kein Bart. Bewusst unauffällig und freundlich gezeichnet (keine
„fiese“ Händlerfigur, kein Klischee), Mimiken Calm/Smile/Suspicious/Serious/Concerned|Serious/Fear.
Prüfer (PR, um 60, Prüfingenieur bei der Hauptuntersuchung; Stimme william; Funktionsrolle ohne Namen):
standing/pointing_finger-2 (schwarzer Pullover der Pose, Hose Grün #8FD694; pointing_finger-1 lässt sich nicht umfärben), Kopf No Hair 2, Brille Glasses 2, Haut
#D9A57E.
Posen nicht aus den letzten drei Folgen 259–261 (blazer-4, sitting/bike, resting-1, crossed_arms-1, robot_dance-3,
sitting/one_leg_up-2, resting-2, shirt-3, easing-2); keine Polka Dots, keine Prothesen-Posen, keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix AN_/HK_/PR_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (AN_redet, HK_redet, PR_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_262")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "AN": ("standing/easing-1", "Medium Straight", None, None, {"Skin": "#EBC2A0", "Jacket": "#F07A6A", "Top": "#FFFFFF"}),
    "HK": ("standing/blazer-3", "Short 3", None, None, {"Skin": "#E3B48C", "Jacket": "#8DB3F2", "Pants": "#3D4A5C"}),
    "PR": ("standing/pointing_finger-2", "No Hair 2", None, "Glasses 2", {"Skin": "#D9A57E", "Pants": "#8FD694"}),
}

LISTE = [
    ("AN_ruhig", "AN", "Calm", 0), ("AN_froh", "AN", "Smile", 0), ("AN_strahlt", "AN", "Smile Big|Smile", 0),
    ("AN_denkt", "AN", "Suspicious", 0), ("AN_sorge", "AN", "Concerned|Serious", 0), ("AN_ernst", "AN", "Serious", 0),
    ("AN_staunt", "AN", "Awe", 0), ("AN_empoert", "AN", "Very Angry", 0), ("AN_redet", "AN", "Rage|Serious", 1),
    ("HK_ruhig", "HK", "Calm", 0), ("HK_froh", "HK", "Smile", 0), ("HK_redet", "HK", "Smile", 1),
    ("HK_denkt", "HK", "Suspicious", 0), ("HK_ernst", "HK", "Serious", 0), ("HK_sorge", "HK", "Concerned|Serious", 0),
    ("HK_ertappt", "HK", "Fear", 0),
    ("PR_ruhig", "PR", "Calm", 0), ("PR_redet", "PR", "Serious", 1), ("PR_ernst", "PR", "Serious", 0),
    ("PR_denkt", "PR", "Suspicious", 0),
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
