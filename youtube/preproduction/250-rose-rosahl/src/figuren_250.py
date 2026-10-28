"""Figuren für Folge 250 (Rose-Rosahl-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Edeltraud (ED, Bauunternehmerin, Anstifterin; Stimme hilde): standing/shirt-4 (schwarze Bluse der Pose, Hose Bordeaux #8E3B53;
  robot_dance-3 verworfen, weil die Geste Lexis robot_dance-1 gleicht), Kopf Gray Medium (Haar #B9B9B9), Haut #EBC29E, keine Brille, kein Bart – neutral, keine Karikatur.
Vinzenz (VI, Bekannter, Täter; Stimme stephan): standing/crossed_arms-2 (schwarzes Oberteil der Pose, Hose Jeansblau #4F6D8F),
  Kopf Short 2 (Haar #3B2A20), Haut #D8A07A, keine Brille, kein Bart – neutral, keine fiese Mimik.
Spaziergänger (SP): wird nicht als Person gezeigt, nur als dunkle Silhouetten-Andeutung einer Open-Peeps-Figur
  (standing/walking-1, Kopf Short 4, alle Flächen einheitlich Nachtgrau, kein Gesicht erkennbar).
Posen nicht aus 247–249 (easing-1/-2, walking-1, blazer-2/-3/-4, crossed_arms-1, pointing_finger-2, resting-1, shirt-3);
keine Prothesen-Posen (shirt-1, shirt-2, blazer-1), keine Polka Dots, keine Bärte. Präfix ED_/VI_/SP_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (ED_redet, VI_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
import numpy as np
from PIL import Image
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_250")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "ED": ("standing/shirt-4", "Gray Medium", None, None, {"Skin": "#EBC29E", "Pants": "#8E3B53", "Hair": "#B9B9B9"}),
    "VI": ("standing/crossed_arms-2", "Short 2", None, None, {"Skin": "#D8A07A", "Pants": "#4F6D8F", "Hair": "#3B2A20"}),
}

LISTE = [
    ("ED_ruhig", "ED", "Calm", 0), ("ED_ernst", "ED", "Serious", 0), ("ED_denkt", "ED", "Suspicious", 0),
    ("ED_sorge", "ED", "Concerned|Serious", 0), ("ED_angst", "ED", "Fear", 0), ("ED_muede", "ED", "Tired", 0),
    ("ED_feierlich", "ED", "Solemn", 0), ("ED_staunt", "ED", "Awe", 0),
    ("ED_redet", "ED", "Serious", 1),
    ("VI_ruhig", "VI", "Calm", 0), ("VI_ernst", "VI", "Serious", 0), ("VI_denkt", "VI", "Suspicious", 0),
    ("VI_sorge", "VI", "Concerned|Serious", 0), ("VI_angst", "VI", "Fear", 0), ("VI_muede", "VI", "Tired", 0),
    ("VI_feierlich", "VI", "Solemn", 0), ("VI_staunt", "VI", "Awe", 0),
    ("VI_redet", "VI", "Serious", 1),
]

NACHTGRAU = (44, 50, 72)


def silhouette(spiegeln):
    """Open-Peeps-Figur als einheitlich dunkle Fläche (nur Umriss, kein Gesicht): Andeutung des Spaziergängers."""
    im = figur("standing/walking-1", "Short 4", "Calm", None, None, {}, hoehe=1200, spiegeln=spiegeln)
    a = np.asarray(im)[:, :, 3]
    out = np.zeros((*a.shape, 4), np.uint8)
    out[..., :3] = NACHTGRAU
    out[..., 3] = a
    return Image.fromarray(out, "RGBA")


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
    silhouette(True).save(f"{ZIEL}/SP_schatten.png"); silhouette(False).save(f"{ZIEL}/SP_schatten_r.png"); n += 2
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
