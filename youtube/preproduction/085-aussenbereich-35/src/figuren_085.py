"""Figuren für Folge 085 (§ 35 BauGB, Wochenendhaus im Wald) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Wiesner (um 45, hat ein Waldgrundstück gekauft, Bauherrin): standing/robot_dance-3 (grünes Oberteil, dunkelblaue Hose),
Kopf Medium 3 (braunes Haar).
Herr Dreher (um 60, Bauaufsichtsbehörde): standing/blazer-3 (braunes Jackett, schwarzes Shirt, graue Hose), Kopf Gray Short,
Brille Glasses.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet, …_protest,
…_seufzt, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der
Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_085")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WI": ("standing/robot_dance-3", "Medium 3", None, None,
           {"Skin": "#F1C6A5", "Hair": "#7A4E2D", "Top": "#8FD694", "Pants": "#3D4A7A"}),
    "DR": ("standing/blazer-3", "Gray Short", None, "Glasses",
           {"Skin": "#E8B48E", "Jacket": "#8A6E50", "Pants": "#7A7A86"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WI_ruhig", "WI", "Smile", 0), ("WI_redet", "WI", "Smile", 1), ("WI_froh", "WI", "Smile Big|Smile", 0),
    ("WI_denkt", "WI", "Suspicious", 0), ("WI_sorge", "WI", "Concerned|Serious", 0),
    ("WI_protest", "WI", "Rage|Serious", 1), ("WI_seufzt", "WI", "Tired", 1),
    ("DR_ruhig", "DR", "Serious", 0), ("DR_redet", "DR", "Serious", 1), ("DR_denkt", "DR", "Solemn", 0),
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
