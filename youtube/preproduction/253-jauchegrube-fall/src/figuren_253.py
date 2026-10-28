"""Figuren für Folge 253 (Jauchegrube-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Brunhilde (BR, um 50, Täterin im Übungsfall; Stimme sabrina): standing/crossed_arms-1 (Oberteil Rostrot #C0603A, schwarze Hose der
  Pose), Kopf Medium 3, Haut #EDB98A, keine Brille, kein Bart – neutral, keine Karikatur, keine fiese Mimik.
Die Nachbarin (Opfer) ist keine Figur (Darstellungsvorgabe): sie erscheint nie im Bild, auch nicht als Silhouette.
Posen nicht aus 250–252 (shirt-4, crossed_arms-2, walking-1, easing-1, resting-2, pointing_finger-2, blazer-3, walking-2,
robot_dance-2); keine Prothesen-Posen (shirt-1, shirt-2, blazer-1), keine Polka Dots, kein Bart. Präfix BR_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansicht (BR_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
from PIL import Image
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_253")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "BR": ("standing/crossed_arms-1", "Medium 3", None, None, {"Skin": "#EDB98A", "Top": "#C0603A"}),
}

LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_ernst", "BR", "Serious", 0), ("BR_denkt", "BR", "Suspicious", 0),
    ("BR_sorge", "BR", "Concerned|Serious", 0), ("BR_angst", "BR", "Fear", 0), ("BR_muede", "BR", "Tired", 0),
    ("BR_feierlich", "BR", "Solemn", 0), ("BR_staunt", "BR", "Awe", 0), ("BR_wut", "BR", "Very Angry", 0),
    ("BR_redet", "BR", "Concerned|Serious", 1),
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
