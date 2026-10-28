"""Figuren für Folge 082 (§ 80 V VwGO, Imbiss) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Herr Hinrichs (um 50, betreibt seit 20 Jahren eine Imbissbude): standing/shirt-3 (weißes Hemd, schwarze Hose),
Kopf Short 4 (dunkelbraunes Haar).
Frau Steinke (um 40, Lebensmittelüberwachung der Stadt): standing/doctor-nurse-02 (weißer Kittel, Überschuhe), Kopf Medium 2.
Die Richterin (um 55, Verwaltungsgericht): standing/shirt-4 (schwarzes Hemd, dunkle Hose), Kopf Medium Bangs, Brille Glasses 3.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Driven, Calm, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_082")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HI": ("standing/shirt-3", "Short 4", None, None, {"Skin": "#EDB98A", "Hair": "#4A3428", "Top": "#FFFFFF"}),
    "ST": ("standing/doctor-nurse-02", "Medium 2", None, None, {"Skin": "#F2C7A8", "Hair": "#8A4B2A"}),
    "RI": ("standing/shirt-4", "Medium Bangs", None, "Glasses 3", {"Skin": "#D9A07A", "Pants": "#34343C", "Hair": "#3A2A22"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HI_ruhig", "HI", "Smile", 0), ("HI_redet", "HI", "Driven", 1), ("HI_sorge", "HI", "Concerned|Serious", 0),
    ("HI_denkt", "HI", "Suspicious", 0), ("HI_aerger", "HI", "Rage|Serious", 0), ("HI_muede", "HI", "Tired", 0),
    ("HI_froh", "HI", "Smile Big|Smile", 0),
    ("ST_ruhig", "ST", "Serious", 0), ("ST_redet", "ST", "Serious", 1), ("ST_denkt", "ST", "Solemn", 0),
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
