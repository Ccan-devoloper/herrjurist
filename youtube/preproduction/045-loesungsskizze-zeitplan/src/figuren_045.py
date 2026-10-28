"""Figuren für Folge 045 (Lösungsskizze und Zeitplan, Klausursaal) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Johanna (Examenskandidatin, Mitte 20, spricht nicht): standing/shirt-3 (türkises Hemd, schwarze Hose), Kopf Long Bangs.
Jakob (Examenskandidat, Mitte 20): standing/resting-2 (schwarzes Shirt, blaue Hose), Kopf Short 4, ohne Bart.
Aufsicht (um 60, ohne Namen): standing/robot_dance-2 (schwarzer Pullover, dunkle Hose), Kopf Gray Medium (graues Haar),
Brille Glasses 2. Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Driven, Suspicious, Fear, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile). Sprechende Ansichten zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_045")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
GRAU_HAAR = "#D6D6D6"

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "JO": ("standing/shirt-3", "Long Bangs", None, None, {"Skin": "#E8B98F"}),
    "JA": ("standing/resting-2", "Short 4", None, None, {"Skin": "#D9A47E", "Pants": "#5A6E9A"}),
    "AU": ("standing/robot_dance-2", "Gray Medium", None, "Glasses 2", {"Skin": "#F0C8A8", "Hair": GRAU_HAAR, "Pants": "#3D3D58"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JO_ruhig", "JO", "Calm", 0), ("JO_liest", "JO", "Serious", 0), ("JO_schreibt", "JO", "Driven", 0),
    ("JO_froh", "JO", "Smile", 0), ("JO_denkt", "JO", "Suspicious", 0),
    ("JA_ruhig", "JA", "Calm", 0), ("JA_cool", "JA", "Cheeky|Smile", 0), ("JA_hektisch", "JA", "Driven", 0),
    ("JA_schreck", "JA", "Fear", 0), ("JA_redet", "JA", "Concerned|Serious", 1), ("JA_plan", "JA", "Serious", 1),
    ("JA_muede", "JA", "Tired", 0),
    ("AU_ruhig", "AU", "Calm", 0), ("AU_redet", "AU", "Serious", 1),
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
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
