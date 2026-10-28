"""Figuren für Folge 146 (Lüth-Urteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; die
realen Beteiligten (Erich Lüth, Veit Harlan, Filmgesellschaften, Richter) werden nicht dargestellt.
Wenke (um 30, Filmbloggerin; Stimme lucy): standing/resting-1 (Pullover Grün #8FD694), Kopf Medium Bangs 3, keine Brille.
Herr Gerstner (um 55, Filmproduzent; Stimme stephan): standing/crossed_arms-1 (Pullover Lila #B8A9F5), Kopf Gray Short
(Haar #B5B5B5), Brille Glasses 4, kein Bart. Sachlich, kein Bösewicht: Smile/Serious/Suspicious/Concerned|Serious/Cute.
Posen nicht aus 142–144 (easing-2, resting-2, shirt-4, walking-2, shirt-3); keine Prothesen-Posen (blazer-1/-2,
shirt-1/-2), keine Polka Dots, keine Bärte.
Präfix WE_/GE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (WE_redet, GE_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_146")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "WE": ("standing/resting-1", "Medium Bangs 3", None, None, {"Skin": "#F1C6A5", "Top": "#8FD694"}),
    "GE": ("standing/crossed_arms-1", "Gray Short", None, "Glasses 4", {"Skin": "#E0AC84", "Top": "#B8A9F5", "Hair": "#B5B5B5"}),
}

LISTE = [
    ("WE_ruhig", "WE", "Smile", 0), ("WE_redet", "WE", "Serious", 1), ("WE_denkt", "WE", "Suspicious", 0),
    ("WE_froh", "WE", "Cute", 0), ("WE_sorge", "WE", "Concerned|Serious", 0),
    ("GE_ruhig", "GE", "Smile", 0), ("GE_redet", "GE", "Serious", 1), ("GE_denkt", "GE", "Suspicious", 0),
    ("GE_froh", "GE", "Cute", 0), ("GE_sorge", "GE", "Concerned|Serious", 0),
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
