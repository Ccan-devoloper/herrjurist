"""Figuren für Folge 150 (Elfes-Urteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; der
reale Beschwerdeführer (Wilhelm Elfes), Behörden und Richter werden nicht dargestellt.
Torben (TB, um 30, beantragt einen Reisepass; Stimme niklas): standing/shirt-3 (Hemd Grün #8FD694, schwarze Hose),
Kopf Short 4 (Haar #4A3222), keine Brille.
Herr Haupt (HP, um 60, Sachbearbeiter der Passbehörde; Stimme helmut): standing/blazer-3 (Sakko Blau #8DB3F2, schwarzes
Oberteil, Hose Grau #6B6B78), Kopf No Hair 2, Brille Glasses 3. Sachlich, kein Bösewicht: Calm/Serious/Suspicious/
Concerned|Serious/Smile.
Posen nicht aus 147–149 (pointing_finger-2, easing-2, robot_dance-3, walking-3, blazer-4, crossed_arms-2) und nicht aus 146
(resting-1, crossed_arms-1); keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Polka Dots, keine Bärte.
Präfix TB_/HP_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (TB_redet, HP_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_150")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "TB": ("standing/shirt-3", "Short 4", None, None, {"Skin": "#EBC0A0", "Top": "#8FD694", "Hair": "#4A3222"}),
    "HP": ("standing/blazer-3", "No Hair 2", None, "Glasses 3", {"Skin": "#E2B08C", "Jacket": "#8DB3F2", 
                                                                "Pants": "#6B6B78", "Hair": "#9C9C9C"}),
}

LISTE = [
    ("TB_ruhig", "TB", "Calm", 0), ("TB_redet", "TB", "Serious", 1), ("TB_denkt", "TB", "Suspicious", 0),
    ("TB_froh", "TB", "Smile", 0), ("TB_sorge", "TB", "Concerned|Serious", 0),
    ("HP_ruhig", "HP", "Calm", 0), ("HP_redet", "HP", "Serious", 1), ("HP_denkt", "HP", "Suspicious", 0),
    ("HP_froh", "HP", "Smile", 0), ("HP_sorge", "HP", "Concerned|Serious", 0),
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
