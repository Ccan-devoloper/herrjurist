"""Figuren für Folge 138 (EU-Rechtsakte Art. 288 AEUV) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Fiktive Personen.
Herr Stegemann (um 58, führt ein kleines Reisebüro, stellt Pauschalreisen zusammen): standing/resting-1 (Pullover Grün
  #8FD694, schwarze Hose aus der Pose), Kopf No Hair 2 (Halbglatze), Brille Glasses, Haut #E8B894, ohne Bart.
Frau Kettner (um 40, Datenschutzbeauftragte): standing/blazer-1 (Blazer in der Originalfarbe Pink, schwarzes Oberteil aus
  der Pose, Hose Schwarz #151515, Prothese aus der Originalpose – keine Täterrolle), Kopf Bun, Haut #C68E6A, ohne Brille.
Parallel produzierte Folge 139 nutzt robot_dance-3 und pointing_finger-2 (grauer Kurzhaarschnitt, Brille) – deshalb
  hier bewusst andere Posen, Köpfe und Farben.
Posen der letzten drei Folgen (135: blazer-4, crossed_arms-2; 136: blazer-3, robot_dance-2, pointing_finger-1; 137: easing-2,
shirt-3, resting-2) nicht verwendet; keine Polka Dots; Blazerfarben der Vorfolgen (Lila 135, Blau 136) vermieden.
Alle Posen blicken im Original nach rechts; Suffix _r = Original (blickt nach rechts), ohne Suffix gespiegelt (nach links).
Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_138")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "ST": ("standing/resting-1", "No Hair 2", None, "Glasses", {"Skin": "#E8B894", "Top": "#8FD694"}),
    "KE": ("standing/blazer-1", "Bun", None, None, {"Skin": "#C68E6A", "Pants": "#151515"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("ST_ruhig", "ST", "Calm", 0), ("ST_froh", "ST", "Smile", 0), ("ST_redet", "ST", "Suspicious", 1),
    ("ST_redetfroh", "ST", "Smile", 1), ("ST_denkt", "ST", "Suspicious", 0), ("ST_staunt", "ST", "Awe", 0),
    ("ST_still", "ST", "Solemn", 0),
    ("KE_ruhig", "KE", "Calm", 0), ("KE_redet", "KE", "Serious", 1), ("KE_ernst", "KE", "Serious", 0),
    ("KE_froh", "KE", "Smile", 0), ("KE_denkt", "KE", "Suspicious", 0), ("KE_staunt", "KE", "Awe", 0),
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
