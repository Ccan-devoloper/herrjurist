"""Figuren für Folge 131 (Klagearten EuGH) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Fiktive Personen.
Richterin Eichhorn (EI, um 58, Verwaltungsgericht): standing/blazer-3 (Jacke und Hose Dunkelgrau #3D3D48 wie eine Robe),
  Kopf Gray Medium (Haar Grau #A7A7B2), Brille Glasses 4, Haut #F0CDB4.
Frau Pfister (PF, um 35, Unternehmerin, Baustofffirma): standing/crossed_arms-1 (Oberteil Rot #F07A6A, schwarze Hose),
  Kopf Medium Straight, Haut #E8B894.
Herr Teichmann (TE, um 45, Beamter der Europäischen Kommission): standing/shirt-3 (Hemd Blau #8DB3F2, schwarze Hose),
  Kopf Short 4, Haut #D9A07A, ohne Bart und Brille.
Posen der letzten Folgen (127: blazer-2, crossed_arms-2; 128: easing-1, resting-2; 129: pointing_finger-2, shirt-4) nicht
verwendet; keine Polka Dots, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; Suffix _r = Original
(blickt nach rechts), ohne Suffix gespiegelt (blickt nach links, zur Tafel).
Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_131")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "EI": ("standing/blazer-3", "Gray Medium", None, "Glasses 4", {"Skin": "#F0CDB4", "Jacket": "#3D3D48", "Pants": "#3D3D48", "Hair": "#A7A7B2"}),
    "PF": ("standing/crossed_arms-1", "Medium Straight", None, None, {"Skin": "#E8B894", "Top": "#F07A6A"}),
    "TE": ("standing/shirt-3", "Short 4", None, None, {"Skin": "#D9A07A", "Top": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EI_ruhig", "EI", "Calm", 0), ("EI_redet", "EI", "Serious", 1), ("EI_denkt", "EI", "Suspicious", 0),
    ("EI_froh", "EI", "Smile", 0), ("EI_staunt", "EI", "Awe", 0), ("EI_ernst", "EI", "Serious", 0),
    ("PF_ruhig", "PF", "Calm", 0), ("PF_redet", "PF", "Driven", 1), ("PF_entschlossen", "PF", "Driven", 0),
    ("PF_sorge", "PF", "Concerned|Serious", 0), ("PF_froh", "PF", "Smile", 0), ("PF_denkt", "PF", "Suspicious", 0),
    ("TE_ruhig", "TE", "Calm", 0), ("TE_redet", "TE", "Serious", 1), ("TE_ernst", "TE", "Serious", 0),
    ("TE_denkt", "TE", "Suspicious", 0), ("TE_freundlich", "TE", "Smile", 0), ("TE_still", "TE", "Solemn", 0),
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
