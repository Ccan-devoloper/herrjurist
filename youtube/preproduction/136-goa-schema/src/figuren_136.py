"""Figuren für Folge 136 (GoA, brennende Mülltonne) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Harald (um 45, Nachbar, Geschäftsführer): mit Jacke standing/blazer-3 (Jacke Blau #5B8FD9, schwarzes Oberteil, Hose
Anthrazit #3A3F47), nach dem Löschen ohne Jacke standing/robot_dance-2 (dasselbe schwarze Oberteil, dieselbe Hose) – der
Wechsel ist die Handlung (die Jacke ist verbrannt). Kopf Short 1, Haut #E6B08A, kein Bart, keine Brille. Stimme marc.
Frau Huber (um 55, Nachbarin, Geschäftsherrin): standing/pointing_finger-1 (schwarze Kleidung der Pose), Kopf Medium 3,
Brille Glasses 3, Haut #F2D2B6. Stimme laura_ruhig.
Abwechslung: Posen nicht aus 133–135 (resting-1, easing-1, blazer-2, shirt-4, blazer-4, crossed_arms-2); keine Polka Dots,
keine Bärte, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Karikatur.
Präfix HJ_/HA_/HU_ (nie ER_). Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts. Grundmimik immer
mit geschlossenem Mund (Calm, Serious, Smile, Suspicious, Awe, Driven bzw. „Augen|geschlossener Mund“). Sprechende Ansichten
(HJ_redet, HA_redet, HU_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic,
Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_136")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HJ": ("standing/blazer-3", "Short 1", None, None, {"Skin": "#E6B08A", "Jacket": "#5B8FD9", "Top": "#151515",
                                                       "Pants": "#3A3F47"}),
    "HA": ("standing/robot_dance-2", "Short 1", None, None, {"Skin": "#E6B08A", "Pants": "#3A3F47"}),
    "HU": ("standing/pointing_finger-1", "Medium 3", None, "Glasses 3", {"Skin": "#F2D2B6"}),
}

LISTE = [
    ("HJ_ruhig", "HJ", "Calm", 0), ("HJ_sorge", "HJ", "Concerned|Serious", 0), ("HJ_redet", "HJ", "Concerned|Serious", 1),
    ("HJ_entschlossen", "HJ", "Driven", 0),
    ("HA_entschlossen", "HA", "Driven", 0), ("HA_froh", "HA", "Smile Big|Smile", 0), ("HA_sorge", "HA", "Concerned|Serious", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Smile", 1), ("HA_denkt", "HA", "Suspicious", 0),
    ("HA_staunt", "HA", "Awe", 0), ("HA_zufrieden", "HA", "Smile", 0), ("HA_ernst", "HA", "Serious", 0),
    ("HU_ruhig", "HU", "Calm", 0), ("HU_froh", "HU", "Smile Big|Smile", 0), ("HU_redet", "HU", "Serious", 1),
    ("HU_denkt", "HU", "Suspicious", 0), ("HU_ernst", "HU", "Serious", 0), ("HU_staunt", "HU", "Awe", 0),
    ("HU_zufrieden", "HU", "Smile", 0),
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
