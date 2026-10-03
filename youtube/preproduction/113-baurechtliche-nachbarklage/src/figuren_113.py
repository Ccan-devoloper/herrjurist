"""Figuren für Folge 113 (Baurechtliche Nachbarklage) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Mahnke (um 55, Nachbarin, Klägerin): standing/resting-1 (Pullover Koralle #F07A6A, schwarze Hose der Pose),
Kopf Medium 1 (dunkler Bob; die Frisur ist nicht umfärbbar), Brille Glasses 3.
Herr Pütz (um 45, Bauherr des Anbaus): standing/shirt-1 (Hemd Hellgrün #8FD694 statt der Grundfarbe, schwarze Shorts der Pose;
die Pose hat eine Beinprothese – bewusst bei einer gewöhnlichen, nicht negativen Rolle), Kopf Short 2 (schwarzes Haar), ohne Bart.
Posen bewusst anders als in 110–112 (shirt-4, easing-1, blazer-1, pointing_finger-2, walking-1) und als der Bauherr in 090
(crossed_arms-2); keine Polka-Dots, keine Bärte, kein Dutt (Lexi).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Tired bzw. „Augen|geschlossener
Mund“ (Concerned|Serious, Rage|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet, …_protest, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_113")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MA": ("standing/resting-1", "Medium 1", None, "Glasses 3",
           {"Skin": "#F0C8A8", "Top": "#F07A6A"}),
    "PU": ("standing/shirt-1", "Short 2", None, None, {"Skin": "#D9A07A", "Top": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_sorge", "MA", "Concerned|Serious", 0), ("MA_denkt", "MA", "Suspicious", 0),
    ("MA_protest", "MA", "Rage|Serious", 1), ("MA_froh", "MA", "Smile Big|Smile", 0), ("MA_ernst", "MA", "Serious", 0),
    ("PU_ruhig", "PU", "Smile", 0), ("PU_redet", "PU", "Smile", 1), ("PU_denkt", "PU", "Suspicious", 0),
    ("PU_ernst", "PU", "Serious", 0), ("PU_muede", "PU", "Tired", 0), ("PU_neu", "PU", "Calm", 1),
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
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
