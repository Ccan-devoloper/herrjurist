"""Figuren für Folge 265 („Gekauft wie gesehen“: Hält der Gewährleistungsausschluss?) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Christel (CH, um 40, Käuferin, privat; Stimme laura_ruhig): standing/resting-2 (schwarzes Oberteil der Pose, Hose Lila
#B8A9F5), Kopf Medium 2, Haut #F1C9A5. Kein Dutt (Lexi).
Herr Burmeister (BU, um 65, privater Verkäufer; Stimme william): standing/shirt-1 (Hemd Grün #8FD694, schwarze kurze Hose
der Pose, Beinprothese der Pose – ehrlicher Verkäufer, keine Täterrolle), Kopf Gray Short (Haar #C9C9C9), Brille Glasses 4,
Haut #E8B48F, kein Bart.
Mechanikerin (ME, um 35, Kfz-Werkstatt; Stimme sabrina; Funktionsrolle ohne Namen): standing/walking-2 (schwarzes Shirt
der Pose, Arbeitshose Blau #5B7DB1), Kopf Cornrows 2 (langer Zopf), Haut #B07552.
Posen nicht aus den letzten drei Folgen 262–264 (easing-1, blazer-3, pointing_finger-2, shirt-4, resting-1, blazer-4,
robot_dance-2, crossed_arms-2) und nicht aus den parallel laufenden 266/267 (crossed_arms-1, blazer-2, shirt-3,
robot_dance-3, walking-3, polka_dots, easing-2); keine Polka Dots, keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix CH_/BU_/ME_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (CH_redet, BU_redet, BU_redet2, ME_redet,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_265")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "CH": ("standing/resting-2", "Medium 2", None, None, {"Skin": "#F1C9A5", "Pants": "#B8A9F5"}),
    "BU": ("standing/shirt-1", "Gray Short", None, "Glasses 4", {"Skin": "#E8B48F", "Top": "#8FD694", "Hair": "#C9C9C9"}),
    "ME": ("standing/walking-2", "Cornrows 2", None, None, {"Skin": "#B07552", "Pants": "#5B7DB1"}),
}

LISTE = [
    ("CH_ruhig", "CH", "Calm", 0), ("CH_froh", "CH", "Smile", 0), ("CH_strahlt", "CH", "Smile Big|Smile", 0),
    ("CH_denkt", "CH", "Suspicious", 0), ("CH_sorge", "CH", "Concerned|Serious", 0), ("CH_ernst", "CH", "Serious", 0),
    ("CH_staunt", "CH", "Awe", 0), ("CH_aerger", "CH", "Very Angry", 0), ("CH_redet", "CH", "Concerned|Serious", 1),
    ("BU_ruhig", "BU", "Calm", 0), ("BU_froh", "BU", "Smile", 0), ("BU_redet", "BU", "Smile", 1),
    ("BU_redet2", "BU", "Serious", 1), ("BU_denkt", "BU", "Suspicious", 0), ("BU_ernst", "BU", "Serious", 0),
    ("BU_sorge", "BU", "Concerned|Serious", 0), ("BU_staunt", "BU", "Awe", 0),
    ("ME_ruhig", "ME", "Calm", 0), ("ME_redet", "ME", "Serious", 1), ("ME_ernst", "ME", "Serious", 0),
    ("ME_denkt", "ME", "Suspicious", 0),
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
