"""Figuren für Folge 043 (Stellvertretung Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Gruber (um 55, Inhaber einer Werbeagentur): standing/blazer-4 (Sakko, Hand in der Hüfte), Kopf Gray Short, Glasses 3.
Wiebke (um 30, Angestellte): standing/easing-1 (offene Jacke), Kopf Long Bangs.
Frau Engel (um 45, Möbelhändlerin): standing/resting-1, Kopf Long Curly, Glasses 2.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Contempt bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile, Loving Grin 1|Smile). Sprechende Ansichten (GR_redet,
WI_redet, EN_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic,
Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_043")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "GR": ("standing/blazer-4", "Gray Short", None, "Glasses 3",
           {"Skin": "#E8B98F", "Jacket": "#4A4A66", "Top": "#FFFFFF"}),
    "WI": ("standing/easing-1", "Long Bangs", None, None,
           {"Skin": "#F1C6A5", "Jacket": "#8FD694", "Top": "#FFFFFF"}),
    "EN": ("standing/resting-1", "Long Curly", None, "Glasses 2",
           {"Skin": "#C68E6A", "Top": "#F07A6A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GR_ruhig", "GR", "Calm", 0), ("GR_froh", "GR", "Smile", 0), ("GR_redet", "GR", "Serious", 1),
    ("GR_aerger", "GR", "Contempt", 0), ("GR_denkt", "GR", "Suspicious", 0), ("GR_schreck", "GR", "Fear", 0),
    ("GR_ernst", "GR", "Serious", 0),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_froh", "WI", "Smile", 0), ("WI_redet", "WI", "Smile", 1),
    ("WI_denkt", "WI", "Suspicious", 0), ("WI_sorge", "WI", "Concerned|Serious", 0),
    ("WI_strahlt", "WI", "Smile Big|Smile", 0), ("WI_verliebt", "WI", "Loving Grin 1|Smile", 0),
    ("WI_schreck", "WI", "Fear", 0),
    ("EN_ruhig", "EN", "Calm", 0), ("EN_froh", "EN", "Smile", 0), ("EN_redet", "EN", "Smile", 1),
    ("EN_denkt", "EN", "Suspicious", 0),
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
