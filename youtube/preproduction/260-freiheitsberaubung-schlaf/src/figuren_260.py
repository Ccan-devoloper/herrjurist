"""Figuren für Folge 260 (Freiheitsberaubung im Schlaf: Vermieter schließt den schlafenden Untermieter nachts ein) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, keine Karikatur, keine Klischees, kein Gewaltbild.
Herr Gerber (um 60, Vermieter, wohnt in derselben Wohnung; Stimme helmut): standing/robot_dance-3 (Pullover Ocker #C9A66B,
Hose Schiefergrau #3D4A5C), Kopf No Hair 1, Brille Glasses 4, Haut #E3B38E, kein Bart.
Joscha (um 25, Untermieter; Stimme niklas): sitting/one_leg_up-2 (sitzt im Bett, T-Shirt Lila #B8A9F5, schwarze Hose der
Pose; die Beine liegen im Bild unter der Bettdecke), Kopf Short 5, Haut #F0C8A8. Er schläft ruhig (Eyes Closed).
Posen nicht aus den letzten drei Folgen 257–259 (shirt-4, easing-1, robot_dance-2, blazer-3, crossed_arms-1/-2,
pointing_finger-2, blazer-4, resting-1, sitting/bike); keine Polka Dots, keine Bärte, keine Prothesen-Posen (shirt-1/-2 und
blazer-1/-2 verworfen). Präfix GE_/JO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt
und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (GE_redet, JO_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_260")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "GE": ("standing/robot_dance-3", "No Hair 1", None, "Glasses 4", {"Skin": "#E3B38E", "Top": "#C9A66B", "Pants": "#3D4A5C"}),
    "JO": ("sitting/one_leg_up-2", "Short 5", None, None, {"Skin": "#F0C8A8", "Top": "#B8A9F5", "Pants": "#2E3440"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GE_ruhig", "GE", "Calm", 0), ("GE_redet", "GE", "Smile", 1), ("GE_froh", "GE", "Smile", 0),
    ("GE_denkt", "GE", "Suspicious", 0), ("GE_ernst", "GE", "Serious", 0), ("GE_sorge", "GE", "Concerned|Serious", 0),
    ("GE_still", "GE", "Solemn", 0),
    ("JO_schlaeft", "JO", "Eyes Closed", 0), ("JO_ruhig", "JO", "Calm", 0), ("JO_redet", "JO", "Smile", 1),
    ("JO_froh", "JO", "Smile", 0), ("JO_denkt", "JO", "Suspicious", 0),
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
