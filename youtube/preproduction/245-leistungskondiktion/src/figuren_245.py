"""Figuren für Folge 245 (Leistungskondiktion, nichtiger Klavierkauf) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Mila (MI, um 25; Stimme lucy): standing/shirt-4 (schwarzes Hemd der Pose, Hose Türkis #7FD6D0), Kopf Medium 2 (Haar der
Bibliothek), Haut #E8B48C, kein Bart, keine Brille.
Frau Heidkamp (HK, um 70; Stimme hilde): standing/shirt-3 (Bluse Lila #B8A9F5, Hose Dunkelgrau #4A4A55), Kopf Gray Bun,
Brille Glasses 2, Haut #EFC6A4 – Verkäuferin, sachlich und freundlich, keine Karikatur.
Posen nicht aus den letzten drei Folgen 242–244 (walking-2, blazer-3, pointing_finger-1/2, blazer-2, walking-3,
robot_dance-2/3, shirt-1, crossed_arms-1, resting-1, polka_dots); keine Polka Dots, keine Prothesen-Posen (shirt-2 mit
Beinprothese verworfen), keine Bärte. Lexi nach lexi.py (robot_dance-1).
Präfix MI_/HK_ (nie ER_). Beide Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (MI_redet, MI_sorgt, HK_redet, HK_fest,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_245")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "MI": ("standing/shirt-4", "Medium 2", None, None, {"Skin": "#E8B48C", "Pants": "#7FD6D0"}),
    "HK": ("standing/shirt-3", "Gray Bun", None, "Glasses 2", {"Skin": "#EFC6A4", "Top": "#B8A9F5", "Pants": "#4A4A55"}),
}

LISTE = [
    ("MI_ruhig", "MI", "Calm", 0), ("MI_redet", "MI", "Serious", 1), ("MI_sorgt", "MI", "Concerned|Serious", 1),
    ("MI_froh", "MI", "Smile", 0), ("MI_staunt", "MI", "Awe", 0), ("MI_denkt", "MI", "Suspicious", 0),
    ("MI_ernst", "MI", "Serious", 0), ("MI_sorge", "MI", "Concerned|Serious", 0), ("MI_strahlt", "MI", "Smile Big|Smile", 0),
    ("HK_ruhig", "HK", "Calm", 0), ("HK_redet", "HK", "Concerned|Serious", 1), ("HK_fest", "HK", "Serious", 1),
    ("HK_froh", "HK", "Smile", 0), ("HK_denkt", "HK", "Suspicious", 0), ("HK_ernst", "HK", "Serious", 0),
    ("HK_sorge", "HK", "Concerned|Serious", 0), ("HK_tippt", "HK", "Driven", 0),
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
