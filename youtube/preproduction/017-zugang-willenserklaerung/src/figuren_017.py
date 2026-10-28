"""Figuren für Folge 017 (Zugang § 130 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Helga (Café-Inhaberin, um 50): standing/blazer-4 (lila Blazer, weißes Oberteil), Werner (Inhaber der Wartungsfirma,
um 55): standing/shirt-4 (schwarzes Hemd, blaue Hose), Paula (Büroangestellte bei Werner, um 25): standing/resting-1
(grünes Oberteil), der Bote (nur im Bild, spricht nicht): standing/walking-1 (orange T-Shirt).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben
der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Serious/Smile“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe). Keine Bärte, keine Prothesen-Posen."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_017")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "HE": ("standing/blazer-4", "Gray Medium", None, "Glasses 2", {"Skin": "#E8B894", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}, 1),
    "WE": ("standing/shirt-4", "No Hair 1", None, "Glasses 4", {"Skin": "#F0C8A8", "Pants": "#8DB3F2"}, 1),
    "PA": ("standing/resting-1", "Long", None, None, {"Skin": "#D9A47A", "Top": "#8FD694"}, 1),
    "BO": ("standing/walking-1", "Short 4", None, None, {"Skin": "#C99470", "Top": "#F9A66C"}, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Smile", 1), ("HE_froh", "HE", "Smile Big|Smile", 0),
    ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_denkt", "HE", "Serious", 0), ("HE_ueberlegt", "HE", "Suspicious", 0),
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Smile", 1), ("WE_abwehr", "WE", "Very Angry", 1),
    ("WE_denkt", "WE", "Suspicious", 0), ("WE_liest", "WE", "Serious", 0), ("WE_froh", "WE", "Cheeky|Smile", 0),
    ("WE_muede", "WE", "Tired", 0),
    ("PA_ruhig", "PA", "Calm", 0), ("PA_redet", "PA", "Smile", 1), ("PA_froh", "PA", "Cute", 0),
    ("BO_ruhig", "BO", "Calm", 0), ("BO_ratlos", "BO", "Concerned|Serious", 0),
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
