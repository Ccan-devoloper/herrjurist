"""Figuren für Folge 074 (Ermessensfehler, § 114 VwGO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Kampmann (um 35, betreibt ein kleines Café): standing/easing-1 (korallrote Jacke über weißem Shirt), Kopf Medium Bangs 2
(kastanienbraunes Haar).
Herr Hornung (um 60, Sachbearbeiter der Stadt): standing/blazer-4 (graues Jackett, hellblaues Hemd), Kopf No Hair 2, Brille Glasses 3.
Die Richterin (um 45, Verwaltungsgericht): standing/resting-2 (schwarzes Oberteil, dunkelblaue Hose), Kopf Medium Straight,
Brille Glasses 4.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Driven, Calm, Solemn, Cute bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_074")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KA": ("standing/easing-1", "Medium Bangs 2", None, None, {"Skin": "#F2C7A8", "Hair": "#8A4B2A", "Jacket": "#F07A6A", "Top": "#FFFFFF"}),
    "HO": ("standing/blazer-4", "No Hair 2", None, "Glasses 3", {"Skin": "#E8B998", "Jacket": "#7A7A86", "Top": "#8DB3F2"}),
    "RI": ("standing/resting-2", "Medium Straight", None, "Glasses 4", {"Skin": "#C99272", "Hair": "#2E2420", "Pants": "#3D4A7A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KA_ruhig", "KA", "Smile", 0), ("KA_redet", "KA", "Driven", 1), ("KA_hofft", "KA", "Cute", 0),
    ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_aerger", "KA", "Rage|Serious", 0), ("KA_denkt", "KA", "Suspicious", 0),
    ("KA_froh", "KA", "Smile Big|Smile", 0),
    ("HO_ruhig", "HO", "Serious", 0), ("HO_redet", "HO", "Serious", 1), ("HO_denkt", "HO", "Solemn", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1),
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
