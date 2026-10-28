"""Figuren für Folge 036 (Verfahrensarten BVerfG) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Pfeiffer (um 50, Inhaberin eines Feuerwerksladens): standing/polka_dots, Kopf Medium Bangs 3.
Fraktionschef Pohl (um 35, Bundestag): standing/blazer-3 (Sakko), Kopf Short 1.
Ministerpräsidentin Hagedorn (um 55, Land Süd): standing/easing-2 (Jacke), Kopf Gray Bun.
Richter Glaser (um 60, Amtsgericht): standing/shirt-3 (dunkles Hemd), Kopf Gray Short, Brille Glasses 2.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Solemn, Driven bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_036")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "PF": ("standing/polka_dots", "Medium Bangs 3", None, None, {"Skin": "#F1C6A5", "Top": "#F6A5C0", "Pants": "#8DB3F2"}),
    "PO": ("standing/blazer-3", "Short 1", None, None, {"Skin": "#B07552", "Jacket": "#8DB3F2", "Pants": "#3D3D58"}),
    "HA": ("standing/easing-2", "Gray Bun", None, None, {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Pants": "#3D3D58"}),
    "GL": ("standing/shirt-3", "Gray Short", None, "Glasses 2", {"Skin": "#E6B48F", "Top": "#4A4A66"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("PF_ruhig", "PF", "Smile", 0), ("PF_redet", "PF", "Serious", 1), ("PF_sorge", "PF", "Concerned|Serious", 0),
    ("PF_denkt", "PF", "Suspicious", 0), ("PF_entschl", "PF", "Driven", 0),
    ("PO_ruhig", "PO", "Smile", 0), ("PO_redet", "PO", "Serious", 1), ("PO_denkt", "PO", "Suspicious", 0),
    ("PO_entschl", "PO", "Driven", 0),
    ("HA_ruhig", "HA", "Smile", 0), ("HA_redet", "HA", "Serious", 1), ("HA_denkt", "HA", "Solemn", 0),
    ("HA_entschl", "HA", "Driven", 0), ("HA_sorge", "HA", "Concerned|Serious", 0),
    ("GL_ruhig", "GL", "Serious", 0), ("GL_redet", "GL", "Serious", 1), ("GL_denkt", "GL", "Suspicious", 0),
    ("GL_ernst", "GL", "Solemn", 0),
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
