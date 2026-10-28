"""Figuren für Folge 055 (Ladendiebstahl, Gewahrsamsenklave, Supermarkt) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Monika (Kundin, um 40): standing/blazer-3 (Blazer mit Taschen, Lila #B8A9F5, schwarzes Top, Hose Blau), Kopf „Medium Straight“.
Rainer (Ladendetektiv, um 45): standing/crossed_arms-1 (Pullover Grün #8FD694, schwarze Hose, verschränkte Arme =
    beobachtet ruhig), Kopf „Short 3“. Keine Prothese, kein Bart, keine Waffe, keine Uniform.
Je Person eine Pose (Outfit konstant). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (zur Tafel), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Suspicious, Fear, Awe, Tired
bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile). Sprechende Ansichten zusätzlich mit
a/o/e (Augen der Grundmimik + Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_055")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

MO_F = {"Skin": "#F1C6A5", "Jacket": "#B8A9F5", "Pants": "#8DB3F2"}
RA_F = {"Skin": "#D9A07A", "Top": "#8FD694"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MO": ("standing/blazer-3", "Medium Straight", None, None, MO_F),
    "RA": ("standing/crossed_arms-1", "Short 3", None, None, RA_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("MO_ruhig", "MO", "Calm", 0), ("MO_redet", "MO", "Cheeky|Smile", 1), ("MO_listig", "MO", "Suspicious", 0),
    ("MO_froh", "MO", "Smile", 0), ("MO_erschrickt", "MO", "Fear", 0), ("MO_denkt", "MO", "Serious", 0),
    ("MO_reuig", "MO", "Concerned|Serious", 0), ("MO_staunt", "MO", "Awe", 0), ("MO_muede", "MO", "Tired", 0),
    ("RA_ruhig", "RA", "Calm", 0), ("RA_beobachtet", "RA", "Serious", 0), ("RA_redet", "RA", "Calm", 1),
    ("RA_wach", "RA", "Suspicious", 0), ("RA_froh", "RA", "Smile", 0),
]

if __name__ == "__main__":
    n = 0
    for name, v, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[v]
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
