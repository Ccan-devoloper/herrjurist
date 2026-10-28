"""Figuren für Folge 083 (gutgläubiger Erwerb, §§ 932 ff. BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Erika (um 60, Eigentümerin, verleiht ihr Fahrrad): standing/easing-1 (lila Hemdjacke über lila Oberteil, schwarze Hose),
Kopf Gray Bun, keine Brille.
Benno (um 40, Freund von Erika, Entleiher, verkauft das Rad als seines): standing/resting-1 (grüner Pullover, schwarze Hose),
Kopf Short 4. Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Selma (um 25, Käuferin): standing/blazer-4 (roter Blazer, weißes Oberteil, schwarze Hose), Kopf Long Curly;
sitting/bike (gleiche Kleidung: roter Blazer, weißes Oberteil, schwarze Hose; Rahmen Blau) für die Sonntagsszene.
Präfix EK_ statt ER_ (bausteine.peep_voll leitet ER_* in den Ordner op_we um). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious bzw. „Augen|
geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (EK_redet, EK_empoert, BE_redet, SE_redet,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_083")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

ER_F = {"Skin": "#F3D3B8", "Top": "#B8A9F5", "Jacket": "#B8A9F5"}
BE_F = {"Skin": "#EDC09A", "Top": "#8FD694"}
SE_F = {"Skin": "#A8714A", "Top": "#FFFFFF", "Jacket": "#F07A6A", "Bicycle Frame": "#8DB3F2"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "EK": ("standing/easing-1", "Gray Bun", None, None, ER_F),
    "BE": ("standing/resting-1", "Short 4", None, None, BE_F),
    "SE": ("standing/blazer-4", "Long Curly", None, None, SE_F),
    "SE_B": ("sitting/bike", "Long Curly", None, None, SE_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EK_ruhig", "EK", "Calm", 0), ("EK_redet", "EK", "Smile", 1), ("EK_froh", "EK", "Smile Big|Smile", 0),
    ("EK_empoert", "EK", "Serious", 1), ("EK_sorge", "EK", "Concerned|Serious", 0), ("EK_denkt", "EK", "Suspicious", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Smile", 1), ("BE_froh", "BE", "Smile Big|Smile", 0),
    ("BE_denkt", "BE", "Suspicious", 0), ("BE_sorge", "BE", "Concerned|Serious", 0),
    ("SE_ruhig", "SE", "Calm", 0), ("SE_redet", "SE", "Serious", 1), ("SE_froh", "SE", "Smile Big|Smile", 0),
    ("SE_denkt", "SE", "Suspicious", 0), ("SE_sorge", "SE", "Concerned|Serious", 0),
    ("SE_rad", "SE_B", "Smile Big|Smile", 0),
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
