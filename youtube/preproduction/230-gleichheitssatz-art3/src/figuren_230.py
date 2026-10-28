"""Figuren für Folge 230 (Gleichheitssatz, Einheimischentarif im Freizeitbad) aus der LexVerse-Figma-Bibliothek (Open Peeps,
CC0). Alle Figuren fiktiv; der reale Beschwerdeführer wird NICHT dargestellt.
Herr Kühnel (KU, um 45, Kassierer des Bads; Stimme stephan): standing/pointing_finger-2 (zeigt auf die Preistafel; schwarzes
Shirt der Pose, Hose Türkis #7FD6D0 als Badkleidung), Kopf Short 5 (dunkles Haar der Vorlage), Haut #E3B08C, kein Bart.
Frau Dittmer (DI, um 70, Einwohnerin der Gemeinde; Stimme hilde): standing/shirt-3 (Hemdbluse Lila #B8A9F5, schwarze Hose
der Pose), Kopf Gray Medium (Haar #C9C9CF), Brille Glasses, Haut #F0C8A8; blazer-1 wegen Beinprothese verworfen, blazer-3
wegen der parallelen Folge 229.
Martha (MA, um 28, wohnt im Nachbarort; Stimme lucy): standing/shirt-4 (schwarzes Hemd der Pose, Hose Grün #8FD694), Kopf
Medium 2 (dunkles Haar der Vorlage), Haut #E0AC85; shirt-1 (Prothese) und walking-1/Medium Bangs 2 (parallele Folge 229)
verworfen.
Posen nicht aus 225–228 (shirt-2, crossed_arms-1/-2, walking-2/-3, resting-1, blazer-2/-4, pointing_finger-1, easing-1,
robot_dance-2, polka_dots, sitting/crossed_legs, sitting/closed_legs-1) und nicht aus der parallelen 229 (robot_dance-3,
blazer-3, easing-2, walking-1); keine Polka Dots, keine Bärte, keine Prothesen-Posen.
Präfix KU_/DI_/MA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (KU_redet, DI_redet, MA_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_230")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "KU": ("standing/pointing_finger-2", "Short 5", None, None, {"Skin": "#E3B08C", "Pants": "#7FD6D0"}),
    "DI": ("standing/shirt-3", "Gray Medium", None, "Glasses", {"Skin": "#F0C8A8", "Top": "#B8A9F5", "Hair": "#C9C9CF"}),
    "MA": ("standing/shirt-4", "Medium 2", None, None, {"Skin": "#E0AC85", "Pants": "#8FD694"}),
}

LISTE = [
    ("KU_ruhig", "KU", "Calm", 0), ("KU_redet", "KU", "Smile", 1), ("KU_froh", "KU", "Smile", 0),
    ("KU_denkt", "KU", "Suspicious", 0), ("KU_ernst", "KU", "Serious", 0),
    ("DI_ruhig", "DI", "Calm", 0), ("DI_redet", "DI", "Smile", 1), ("DI_froh", "DI", "Cute", 0),
    ("DI_denkt", "DI", "Suspicious", 0),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Concerned|Serious", 1), ("MA_sorge", "MA", "Concerned|Serious", 0),
    ("MA_denkt", "MA", "Suspicious", 0), ("MA_ernst", "MA", "Serious", 0), ("MA_froh", "MA", "Smile Big|Smile", 0),
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
