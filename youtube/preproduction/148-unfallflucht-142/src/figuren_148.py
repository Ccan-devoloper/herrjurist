"""Figuren für Folge 148 (Unfallflucht § 142, Schramme beim Ausparken) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Gerlinde (um 60, parkt nachts aus, schrammt das Auto, lässt einen Zettel da; Stimme hilde): standing/robot_dance-3
(Oberteil Rot #F07A6A, Hose Anthrazit #3A3A48, weiße Schuhe; offene Handgeste), Kopf Gray Bun, Brille Glasses 3,
Haut #F0CDB4.
Bernhard (um 45, Halter des geschrammten Autos; Stimme christian): standing/walking-3 (schwarzes Shirt, schwarze Hose,
weiße Schuhe; geht), Kopf Pomp (dunkelbraun), Haut #E2B08C, kein Bart, keine Brille.
Sachlich, keine Karikatur, keine bösen Mimiken; keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 bewusst nicht), keine
Bärte, keine Polka Dots. Posen nicht aus den letzten drei Folgen 145–147 (resting-1, easing-1, crossed_arms-1, blazer-3,
pointing_finger-2, easing-2) und nicht aus 140 (crossed_arms-1, walking-1); Lexi bleibt robot_dance-1.
Präfix GL_/BE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (GL_redet, BE_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_148")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "GL": ("standing/robot_dance-3", "Gray Bun", None, "Glasses 3", {"Skin": "#F0CDB4", "Top": "#F07A6A", "Pants": "#3A3A48"}),
    "BE": ("standing/walking-3", "Pomp", None, None, {"Skin": "#E2B08C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GL_ruhig", "GL", "Calm", 0), ("GL_redet", "GL", "Calm", 1), ("GL_schreck", "GL", "Fear", 0),
    ("GL_denkt", "GL", "Suspicious", 0), ("GL_sorge", "GL", "Concerned|Serious", 0), ("GL_still", "GL", "Solemn", 0),
    ("GL_muede", "GL", "Tired", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Serious", 1), ("BE_denkt", "BE", "Suspicious", 0),
    ("BE_sorge", "BE", "Concerned|Serious", 0), ("BE_still", "BE", "Solemn", 0), ("BE_ernst", "BE", "Serious", 0),
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
