"""Figuren für Folge 025 (Auschwitzlüge) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Möller (um 58, Versammlungsbehörde, Behördenfigur): standing/blazer-4 (blaues Jackett), Kopf Gray Short (graues Haar),
Glasses 2. Svenja (um 26, Referendarin in der Verwaltungsstation): standing/easing-1 (orange Jacke), Kopf Medium Bangs.
Keine Bärte, keine Prothesen-Posen, keine realen Personen. Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious bzw. „Augen|geschlossener
Mund“ (Concerned|Serious). Sprechende Ansichten (MO_redet, SV_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_025")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MO": ("standing/blazer-4", "Gray Short", None, "Glasses 2", {"Skin": "#E6B48F", "Hair": "#C9C9CF", "Jacket": "#8DB3F2"}),
    "SV": ("standing/easing-1", "Medium Bangs", None, None, {"Skin": "#F1C6A5", "Jacket": "#F9A66C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MO_ruhig", "MO", "Calm", 0), ("MO_redet", "MO", "Serious", 1), ("MO_ernst", "MO", "Serious", 0),
    ("MO_denkt", "MO", "Suspicious", 0),
    ("SV_ruhig", "SV", "Calm", 0), ("SV_redet", "SV", "Concerned|Serious", 1), ("SV_denkt", "SV", "Suspicious", 0),
    ("SV_froh", "SV", "Smile", 0), ("SV_ernst", "SV", "Serious", 0), ("SV_sorge", "SV", "Concerned|Serious", 0),
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
