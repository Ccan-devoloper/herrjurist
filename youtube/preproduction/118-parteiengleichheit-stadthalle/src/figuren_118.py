"""Figuren für Folge 118 (Parteiengleichheit, Stadthalle) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren
fiktiv; keine realen Personen, keine Karikaturen, keine Parteifarben realer Parteien.
Hartmut (um 55, Landesgeschäftsführer der fiktiven Weitblick-Partei; Stimme christian): standing/robot_dance-3 (Hemd
Weiß, Hose Grau #8C9399), Kopf Short 2 (grau), Brille Glasses 2, kein Bart. Sachlich, nicht als Bösewicht: nur Calm/Smile/
Serious/Suspicious/Concerned|Serious.
Bürgermeisterin (um 60, Funktionsrolle; Stimme hilde): standing/resting-1 (Pullover Lila #B8A9F5, schwarze Hose),
Kopf Bun (grau).
Richterin (um 40, Funktionsrolle; Stimme lucy): standing/crossed_arms-2 (schwarzes Oberteil, dunkle Hose wie eine Robe),
Kopf Medium Bangs 3.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2 zeigen Prothesen und wurden deshalb verworfen), keine Polka Dots, keine Bärte. Posen nicht aus 114–117 (crossed_arms-1, walking-2, blazer-4,
shirt-3, crossed_legs, resting-2, blazer-3, easing-1, robot_dance-2, shirt-4, pointing_finger-2).
Präfix HA_/BM_/RI_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (HA_redet, BM_redet, RI_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_118")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HA": ("standing/robot_dance-3", "Short 2", None, "Glasses 2", {"Skin": "#EAC3A0", "Top": "#FFFFFF", "Pants": "#8C9399",
                                                                     "Hair": "#8A8A8A"}),
    "BM": ("standing/resting-1", "Bun", None, None, {"Skin": "#F2D0B1", "Top": "#B8A9F5", "Hair": "#B9B4AE"}),
    "RI": ("standing/crossed_arms-2", "Medium Bangs 3", None, None, {"Skin": "#B07552", "Pants": "#2B2B2B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Serious", 1), ("HA_froh", "HA", "Smile", 0),
    ("HA_denkt", "HA", "Suspicious", 0), ("HA_sorge", "HA", "Concerned|Serious", 0),
    ("BM_ruhig", "BM", "Calm", 0), ("BM_redet", "BM", "Serious", 1), ("BM_denkt", "BM", "Suspicious", 0),
    ("BM_sorge", "BM", "Concerned|Serious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_froh", "RI", "Smile", 0),
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
