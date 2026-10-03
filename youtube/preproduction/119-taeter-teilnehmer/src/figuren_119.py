"""Figuren für Folge 119 (Abgrenzung Täter/Teilnehmer) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Zwei Referendare lesen die alten Akten in der Bibliothek; die Beteiligten der echten Fälle erscheinen NICHT als Figuren.
Luise (LU, um 28, Referendarin): standing/easing-2 (offenes Hemd/Jacke Grün #8FD694, Hose Gelb #F9D56E), Kopf Long Bangs,
        Haut #E3A982. Stimme sabrina.
Oskar (OS, um 32, Referendar): standing/blazer-3 (Blazer Blau #8DB3F2 über schwarzem Shirt, Hose Grau #5B5F66),
        Kopf Short 1, Haut #F2D3B8. Stimme marc.
Lexi nach lexi.py (robot_dance-1).
Posen der letzten Folgen (pointing_finger-1 verworfen: Oberteil nicht einfärbbar; 116–118: easing-1, robot_dance-2/-3, shirt-4, pointing_finger-2, resting-1, crossed_arms-2;
104: blazer-4, crossed_arms-2, walking-1, resting-1, shirt-4) nicht verwendet; keine Polka Dots, keine Bärte, keine
Prothesen-Posen. Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel),
Suffix _r nach rechts. Grundmimik immer mit geschlossenem Mund; sprechende Ansichten (LU_redet, OS_redet) zusätzlich
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_119")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
P = {
    "LU": ("standing/easing-2", "Long Bangs", None, None, {"Skin": "#E3A982", "Jacket": "#8FD694", "Pants": "#F9D56E"}),
    "OS": ("standing/blazer-3", "Short 1", None, None, {"Skin": "#F2D3B8", "Jacket": "#8DB3F2", "Pants": "#5B5F66"}),
}
LISTE = [
    ("LU_ruhig", "LU", "Calm", 0), ("LU_froh", "LU", "Smile", 0), ("LU_ernst", "LU", "Serious", 0),
    ("LU_redet", "LU", "Serious", 1), ("LU_zweifel", "LU", "Suspicious", 0), ("LU_still", "LU", "Solemn", 0),
    ("LU_staunt", "LU", "Awe", 0),
    ("OS_ruhig", "OS", "Calm", 0), ("OS_froh", "OS", "Smile", 0), ("OS_ernst", "OS", "Serious", 0),
    ("OS_redet", "OS", "Serious", 1), ("OS_zweifel", "OS", "Suspicious", 0), ("OS_still", "OS", "Solemn", 0),
    ("OS_staunt", "OS", "Awe", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
