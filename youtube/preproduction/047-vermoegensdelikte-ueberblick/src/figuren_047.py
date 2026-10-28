"""Figuren für Folge 047 (Vermögensdelikte Überblick, Dagmars Kameraladen) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Dagmar (Ladeninhaberin, um 50): standing/blazer-1 (Blazer Lila, Hose Blau; Beinprothese der Originalpose – Dagmar ist
    keine Täterin), Kopf „Medium Bangs 3“.
Klaus (Kunde, um 40): standing/shirt-3 (Hemd Grün, schwarze Hose der Pose), Kopf „Short 4“. Keine Prothese, kein Bart.
Je Person eine Pose (Outfit konstant). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (zur Tafel), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF): Calm, Smile, Serious, Suspicious, Driven, Contempt, Fear, Awe
bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile, Rage|Serious). Sprechende Ansichten zusätzlich mit
a/o/e (Augen der Grundmimik + Mund Explaining/Concerned Fear/Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_047")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

DA_F = {"Skin": "#C99470", "Jacket": "#B8A9F5", "Pants": "#8DB3F2"}
KL_F = {"Skin": "#EDB98A", "Top": "#8FD694"}

# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "DA": ("standing/blazer-1", "Medium Bangs 3", None, None, DA_F),
    "KL": ("standing/shirt-3", "Short 4", None, None, KL_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen)
LISTE = [
    ("DA_ruhig", "DA", "Calm", 0), ("DA_redet", "DA", "Smile", 1), ("DA_froh", "DA", "Smile", 0),
    ("DA_erschrickt", "DA", "Fear", 0), ("DA_sorge", "DA", "Concerned|Serious", 0), ("DA_denkt", "DA", "Serious", 0),
    ("DA_skeptisch", "DA", "Suspicious", 0), ("DA_staunt", "DA", "Awe", 0),
    ("KL_ruhig", "KL", "Calm", 0), ("KL_redet", "KL", "Cheeky|Smile", 1), ("KL_droht", "KL", "Rage|Serious", 1),
    ("KL_bittet", "KL", "Smile", 1), ("KL_listig", "KL", "Suspicious", 0), ("KL_froh", "KL", "Smile", 0),
    ("KL_entschlossen", "KL", "Driven", 0), ("KL_denkt", "KL", "Serious", 0), ("KL_ertappt", "KL", "Fear", 0),
    ("KL_veraechtlich", "KL", "Contempt", 0),
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
