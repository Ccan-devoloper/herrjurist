"""Figuren für Folge 066 (Revision Strafrecht: Sachrüge vs. Verfahrensrüge) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Herr Brockmann (Mandant, verurteilter Angeklagter, um 35): standing/easing-2 (blaues offenes Hemd, dunkle Hose), Kopf Short 1,
ohne Bart, heller Hautton (keine Prothese, kein Herkunfts- oder Hautfarben-Klischee bei der verurteilten Person).
Rechtsanwältin Lenz (Verteidigerin, um 45): standing/blazer-1 (lila Blazer, Beinprothese der Originalpose), Kopf Medium Straight.
Vorsitzender Richter (um 60, ohne Namen): standing/blazer-2 (dunkles Sakko wie eine Robe, weißes Hemd), Kopf Gray Short (Haar grau eingefärbt),
Brille Glasses 3, ohne Bart. Herr Stoll (Alibizeuge, um 35, spricht nicht): standing/resting-2 (grüne Hose), Kopf Pomp.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious,
Suspicious, Fear, Solemn, Tired, Very Angry bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_066")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BR": ("standing/easing-2", "Short 1", None, None, {"Skin": "#E8B98F", "Jacket": "#8DB3F2", "Pants": "#5A5A6A"}),
    "LZ": ("standing/blazer-1", "Medium Straight", None, None, {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Pants": "#5A5A6A"}),
    "RI": ("standing/blazer-2", "Gray Short", None, "Glasses 3", {"Skin": "#F2CDB0", "Jacket": "#3A3A48", "Top": "#FFFFFF", "Hair": "#C4C4CC"}),
    "ST": ("standing/resting-2", "Pomp", None, None, {"Skin": "#D9A47E", "Pants": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Concerned|Serious", 1), ("BR_sorge", "BR", "Concerned|Serious", 0),
    ("BR_aerger", "BR", "Very Angry", 0), ("BR_denkt", "BR", "Suspicious", 0), ("BR_froh", "BR", "Smile", 0),
    ("BR_schreck", "BR", "Fear", 0),
    ("LZ_ruhig", "LZ", "Calm", 0), ("LZ_redet", "LZ", "Serious", 1), ("LZ_denkt", "LZ", "Suspicious", 0),
    ("LZ_froh", "LZ", "Smile", 0), ("LZ_sorge", "LZ", "Concerned|Serious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_streng", "RI", "Solemn", 0),
    ("RI_denkt", "RI", "Suspicious", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_wartet", "ST", "Tired", 0), ("ST_sorge", "ST", "Concerned|Serious", 0),
    ("ST_froh", "ST", "Smile", 0),
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
