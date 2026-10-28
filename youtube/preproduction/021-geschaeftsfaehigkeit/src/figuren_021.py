"""Figuren für Folge 021 (Geschäftsfähigkeit §§ 104 ff. BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Frieda (Schülerin, 15): standing/easing-1 (offenes grünes Hemd über weißem Shirt), Herr Ritter (Inhaber des Handyladens,
um 60): standing/shirt-3 (blaues Hemd), Friedas Mutter (um 45): standing/blazer-3 (roter Blazer).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben
der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Serious/Smile“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe). Keine Bärte, keine Prothesen-Posen."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_021")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "FR": ("standing/easing-1", "Long Bangs", None, None, {"Skin": "#D9A47A", "Jacket": "#8FD694", "Top": "#FFFFFF"}, 1),
    "RI": ("standing/shirt-3", "Gray Short", None, "Glasses 3", {"Skin": "#F0C8A8", "Top": "#8DB3F2"}, 1),
    "MU": ("standing/blazer-3", "Medium 2", None, None, {"Skin": "#D9A47A", "Jacket": "#F07A6A", "Pants": "#3D3D58"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("FR_ruhig", "FR", "Calm", 0), ("FR_redet", "FR", "Smile", 1), ("FR_froh", "FR", "Smile Big|Smile", 0),
    ("FR_sorge", "FR", "Concerned|Serious", 0), ("FR_denkt", "FR", "Serious", 0), ("FR_ueberlegt", "FR", "Suspicious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Smile", 1), ("RI_froh", "RI", "Smile", 0),
    ("RI_denkt", "RI", "Suspicious", 0), ("RI_sorge", "RI", "Concerned|Serious", 0), ("RI_ernst", "RI", "Serious", 0),
    ("MU_ruhig", "MU", "Calm", 0), ("MU_redet", "MU", "Serious", 1), ("MU_denkt", "MU", "Suspicious", 0),
    ("MU_ernst", "MU", "Serious", 0), ("MU_froh", "MU", "Smile", 0),
]

if __name__ == "__main__":
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben, sp = P[p]
        for suffix, gespiegelt in (("", sp), ("_r", 1 - sp)):
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
