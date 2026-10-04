"""Figuren für Folge 140 (Gefährdung des Straßenverkehrs, Überholen vor einer Kuppe) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Reinhold (um 45, überholt vor der Kuppe; Stimme stephan): standing/crossed_arms-1 (Oberteil Grün #8FD694, schwarze Hose,
weiße Schuhe; verschränkte Arme), Kopf Short 2 (Haar dunkelbraun #4A3222), Haut #EAC1A0, kein Bart, keine Brille.
Gertrud (um 60, kommt entgegen, Vollbremsung; Stimme hilde): standing/walking-1 (Oberteil Lila #B8A9F5, schwarze Hose),
Kopf Gray Medium (Haar grau #C9C4BE), Brille Glasses, Haut #F2D3BD.
Sachlich, keine Karikatur, keine bösen Mimiken bei Reinhold; keine Prothesen-Posen (shirt-1/-2 bewusst nicht), keine Bärte,
keine Polka Dots. Posen nicht aus 137–139 (easing-2, resting-2, shirt-3, blazer-1, resting-1, pointing_finger-2,
robot_dance-3) und nicht aus 130 (robot_dance-2, blazer-3, blazer-4) oder 124 (walking-2, shirt-4, sitting/bike);
Lexi bleibt robot_dance-1.
Präfix RE_/GE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (RE_redet, GE_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_140")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "RE": ("standing/crossed_arms-1", "Short 2", None, None, {"Skin": "#EAC1A0", "Top": "#8FD694", "Hair": "#4A3222"}),
    "GE": ("standing/walking-1", "Gray Medium", None, "Glasses", {"Skin": "#F2D3BD", "Top": "#B8A9F5", "Hair": "#C9C4BE"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RE_ruhig", "RE", "Calm", 0), ("RE_redet", "RE", "Serious", 1), ("RE_denkt", "RE", "Suspicious", 0),
    ("RE_ernst", "RE", "Serious", 0), ("RE_sorge", "RE", "Concerned|Serious", 0), ("RE_still", "RE", "Solemn", 0),
    ("RE_muede", "RE", "Tired", 0),
    ("GE_ruhig", "GE", "Calm", 0), ("GE_redet", "GE", "Concerned|Serious", 1), ("GE_angst", "GE", "Fear", 0),
    ("GE_sorge", "GE", "Concerned|Serious", 0), ("GE_still", "GE", "Solemn", 0), ("GE_froh", "GE", "Smile", 0),
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
