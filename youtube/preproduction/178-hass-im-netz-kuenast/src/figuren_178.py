"""Figuren für Folge 178 (Hass im Netz, Fall Künast) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Fiktiver Rahmen: Sprechstunde am Lehrstuhl. Die reale Politikerin, die Kommentierenden, der Blogger sowie Gerichts- und
Plattformpersonen werden NICHT dargestellt, auch die fiktive Stadträtin des Hooks nicht (nur Text).
Mattes (MA, um 23, Jurastudent; Stimme niklas): standing/resting-1 (Pullover Grün #8FD694, schwarze Hose aus der Pose),
  Kopf Short 4, Haut #E8B98F, ohne Brille.
Professor Ruhland (RU, um 60, Lehrstuhlinhaber; Stimme helmut): standing/shirt-3 (weißes Hemd, schwarze Hose aus der Pose),
  Kopf No Hair 2 (Haarkranz), Brille Glasses 3, Haut #E3B08C, kein Bart.
Posen nicht aus 174–176 (crossed_arms-1/-2, resting-2, shirt-4, easing-1, pointing_finger-1/-2, blazer-1); keine
Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Polka Dots, keine Bärte.
Ruhige Mimiken (ernstes Thema): Calm, Serious, Suspicious, Solemn; kein Lachen.
Präfix MA_/RU_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (MA_redet, RU_redet, Lexi) zusätzlich
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_178")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "MA": ("standing/resting-1", "Short 4", None, None, {"Skin": "#E8B98F", "Top": "#8FD694"}),
    "RU": ("standing/shirt-3", "No Hair 2", None, "Glasses 3", {"Skin": "#E3B08C", "Top": "#FFFFFF"}),
}

LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Serious", 1), ("MA_denkt", "MA", "Suspicious", 0),
    ("MA_ernst", "MA", "Solemn", 0),
    ("RU_ruhig", "RU", "Calm", 0), ("RU_redet", "RU", "Serious", 1), ("RU_denkt", "RU", "Suspicious", 0),
    ("RU_ernst", "RU", "Solemn", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
