"""Figuren für Folge 169 (Apotheken-Urteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; der
reale Beschwerdeführer (ein angestellter Apotheker), Behörden und Richter werden nicht dargestellt.
Grete (GR, um 30, Apothekerin, will eine eigene Apotheke eröffnen; Stimme ela_froh): standing/doctor-nurse-02 (weißer
Kittel in den Originalfarben der Pose: Oberteil Hellblau #9FD8E5, Hose Blau #8FA7DF; die drei Kleidungsflächen heißen in Figma
gleich „Clothes“ und lassen sich nicht einzeln umfärben), Kopf Medium Bangs 2 (Haar #8A5A33), Haut #F1C9A5, ohne Brille.
Herr Dannemann (DA, um 60, Sachbearbeiter der Erlaubnisbehörde; Stimme helmut): standing/shirt-4 (schwarzes Hemd der Pose,
Hose Grau #6B6B78), Kopf Gray Short (Haar #A8A8A8), Brille Glasses 4, Haut #E0AC88, ohne Bart. Sachlich, kein Bösewicht:
Calm/Serious/Suspicious.
Posen nicht aus 165–167 (walking-1, crossed_arms-2, resting-2, pointing_finger-2, blazer-3, resting-1, blazer-1) und nicht aus
164 (shirt-3, blazer-4); keine Prothesen-Posen, keine Polka Dots, keine Bärte.
Präfix GR_/DA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (GR_redet, DA_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_169")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "GR": ("standing/doctor-nurse-02", "Medium Bangs 2", None, None, {"Skin": "#F1C9A5", "Hair": "#8A5A33"}),
    "DA": ("standing/shirt-4", "Gray Short", None, "Glasses 4", {"Skin": "#E0AC88", "Pants": "#6B6B78", "Hair": "#A8A8A8"}),
}

LISTE = [
    ("GR_ruhig", "GR", "Calm", 0), ("GR_redet", "GR", "Serious", 1), ("GR_denkt", "GR", "Suspicious", 0),
    ("GR_froh", "GR", "Smile", 0), ("GR_sorge", "GR", "Concerned|Serious", 0),
    ("DA_ruhig", "DA", "Calm", 0), ("DA_redet", "DA", "Serious", 1), ("DA_denkt", "DA", "Suspicious", 0),
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
