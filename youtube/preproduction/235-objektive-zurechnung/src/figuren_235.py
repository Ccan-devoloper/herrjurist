"""Figuren für Folge 235 (Objektive Zurechnung, Gewitterfall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Hildegard (HI, wohlhabende Witwe Mitte 70; Stimme laura_ruhig): standing/walking-3 (dunkles Shirt und Hose der Pose, weiße
  Schuhe), Kopf Gray Bun, Brille Glasses 2, Haut #F1C9A5, kein Bart – freundlich, sympathisch.
Rupert (RU, Neffe um 40; Stimme marc): standing/blazer-4 (Sakko Petrol #3E7C74, Shirt Weiß #FFFFFF), Kopf Short 2, Haut
  #E0AC85, keine Brille, kein Bart – ruhig und unauffällig, keine Karikatur (keine fiesen Mimiken).
Posen nicht aus 229–232 (blazer-3, easing-2, walking-1, robot_dance-3, pointing_finger-2, shirt-3, shirt-4, walking-2,
crossed_arms-1, easing-1, resting-1); keine Prothesen-Posen (shirt-1, shirt-2, blazer-1, blazer-2), keine Polka Dots, keine
Bärte. Präfix HI_/RU_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt
und blickt nach links, Suffix _r blickt nach rechts (im Kontaktbild out/richtung2.png geprüft).
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (RU_redet, HI_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_235")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HI": ("standing/walking-3", "Gray Bun", None, "Glasses 2", {"Skin": "#F1C9A5"}),
    "RU": ("standing/blazer-4", "Short 2", None, None, {"Skin": "#E0AC85", "Jacket": "#3E7C74", "Top": "#FFFFFF"}),
}

LISTE = [
    ("HI_froh", "HI", "Smile", 0), ("HI_ruhig", "HI", "Calm", 0), ("HI_geniesst", "HI", "Eyes Closed", 0),
    ("HI_sorge", "HI", "Concerned|Serious", 0), ("HI_schreck", "HI", "Awe", 0),
    ("HI_redet", "HI", "Smile", 1),
    ("RU_ruhig", "RU", "Calm", 0), ("RU_froh", "RU", "Smile", 0), ("RU_ernst", "RU", "Serious", 0),
    ("RU_denkt", "RU", "Suspicious", 0), ("RU_muede", "RU", "Tired", 0), ("RU_sorge", "RU", "Concerned|Serious", 0),
    ("RU_feierlich", "RU", "Solemn", 0), ("RU_staunt", "RU", "Awe", 0),
    ("RU_redet", "RU", "Smile", 1),
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
