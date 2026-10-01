"""Figuren für Folge 023 (Anfechtung Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Ilse (um 55, Buchhändlerin): standing/resting-2 (Hand in der Hüfte), Kopf Bun, Glasses 4.
Herr Winkler (um 50, Großhändler): standing/robot_dance-2 (offene Hand), Kopf Short 3.
Jörg (um 40, Verkäufer des Lieferwagens): standing/walking-2, Kopf Short 5.
Die „-2“-Posen haben ein schwarzes Oberteil (nicht umfärbbar); unterschieden wird über Hose, Frisur und Hautton.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Tired, Contempt bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile, Cheeky|Smile). Sprechende Ansichten (IL_redet, WI_redet,
JO_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_023")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "IL": ("standing/resting-2", "Bun", None, "Glasses 4",
           {"Skin": "#EBC4A0", "Hair": "#8A6A55", "Pants": "#B8A9F5"}),
    "WI": ("standing/robot_dance-2", "Short 3", None, None,
           {"Skin": "#D9A07A", "Pants": "#8DB3F2"}),
    "JO": ("standing/walking-2", "Short 5", None, None,
           {"Skin": "#F0C8A8", "Pants": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("IL_ruhig", "IL", "Calm", 0), ("IL_froh", "IL", "Smile", 0), ("IL_redet", "IL", "Concerned|Serious", 1),
    ("IL_denkt", "IL", "Suspicious", 0), ("IL_schreck", "IL", "Fear", 0), ("IL_sorge", "IL", "Concerned|Serious", 0),
    ("IL_ernst", "IL", "Serious", 0), ("IL_strahlt", "IL", "Smile Big|Smile", 0), ("IL_muede", "IL", "Tired", 0),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_froh", "WI", "Smile", 0), ("WI_redet", "WI", "Serious", 1),
    ("WI_aerger", "WI", "Contempt", 0), ("WI_denkt", "WI", "Suspicious", 0),
    ("JO_ruhig", "JO", "Calm", 0), ("JO_redet", "JO", "Cheeky|Smile", 1), ("JO_ertappt", "JO", "Fear", 0),
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
