"""Figuren für Folge 143 (Fraport-Urteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; die
realen Beteiligten (Beschwerdeführerin, Aktivisten, Mitarbeiter der Betreiberin, Richter) werden nicht dargestellt.
Herr Sievers (um 45, Mitarbeiter der Flughafengesellschaft; Stimme marc): standing/shirt-4 (schwarzes Hemd, Hose Marine
#4A5A85), Kopf Short 5, kein Bart, keine Brille. Sachlich, kein Bösewicht: Calm/Serious/Smile/Suspicious/Concerned|Serious.
Dorothea (um 40, Reisende; Stimme sabrina): standing/easing-2 (Jacke Koralle #F07A6A über schwarzem Oberteil, Hose
#3D3D58), Kopf Medium Bangs 2.
Posen nicht aus 139–141 (robot_dance-3, pointing_finger-2, crossed_arms-1, walking-1, blazer-4, crossed_arms-2, easing-1,
robot_dance-2, blazer-3); keine Prothesen-Posen, keine Polka Dots, keine Bärte.
Präfix SI_/DO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (SI_redet, DO_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_143")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "SI": ("standing/shirt-4", "Short 5", None, None, {"Skin": "#E2B08C", "Pants": "#4A5A85", "Hair": "#4A3222"}),
    "DO": ("standing/easing-2", "Medium Bangs 2", None, None, {"Skin": "#F1C6A5", "Jacket": "#F07A6A", "Pants": "#3D3D58",
                                                              "Hair": "#8A5A3C"}),
}

LISTE = [
    ("SI_ruhig", "SI", "Smile", 0), ("SI_redet", "SI", "Serious", 1), ("SI_froh", "SI", "Cute", 0),
    ("SI_denkt", "SI", "Suspicious", 0), ("SI_sorge", "SI", "Concerned|Serious", 0),
    ("DO_ruhig", "DO", "Smile", 0), ("DO_redet", "DO", "Serious", 1), ("DO_denkt", "DO", "Suspicious", 0),
    ("DO_froh", "DO", "Cute", 0), ("DO_sorge", "DO", "Concerned|Serious", 0),
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
