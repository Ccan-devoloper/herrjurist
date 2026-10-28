"""Figuren für Folge 060 (hinreichender Tatverdacht, Fahrraddiebstahl mit einer einzigen Zeugin) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Frau Wessel (Eigentümerin des Fahrrads, Verletzte, um 30): standing/walking-2 (kommt nach Hause; schwarzes Oberteil,
blaue Hose), Kopf Bun. Frau Hesse (Nachbarin, Zeugin, um 70): standing/blazer-3 (grüner Blazer), Kopf Gray Medium (Haar grau eingefärbt),
Brille Glasses 2. Herr Mertens (Nachbar, Beschuldigter, um 45): standing/walking-1 (rotes Oberteil, schwarze Hose),
Kopf Short 2, ohne Bart, heller Hautton (kein Herkunfts- oder Hautfarben-Klischee bei der Täterrolle).
Staatsanwalt (um 50, ohne Namen): standing/crossed_arms-1 (lila Oberteil), Kopf No Hair 3, Brille Glasses 4, ohne Bart.
Keine Prothesen-Posen, keine Bärte (Mund bleibt frei).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben
der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile,
Serious, Suspicious, Fear, Driven, Solemn, Tired bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende
Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der
Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_060")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WE": ("standing/walking-2", "Bun", None, None, {"Skin": "#F0C8A8", "Pants": "#8DB3F2"}),
    "HE": ("standing/blazer-3", "Gray Medium", None, "Glasses 2", {"Skin": "#F2CDB0", "Jacket": "#8FD694", "Pants": "#5A5A6A", "Hair": "#C4C4CC"}),
    "ME": ("standing/walking-1", "Short 2", None, None, {"Skin": "#E8B98F", "Top": "#F07A6A"}),
    "SA": ("standing/crossed_arms-1", "No Hair 3", None, "Glasses 4", {"Skin": "#D9A47E", "Top": "#B8A9F5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Concerned|Serious", 1), ("WE_sorge", "WE", "Concerned|Serious", 0),
    ("WE_froh", "WE", "Smile", 0), ("WE_denkt", "WE", "Serious", 0),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Serious", 1), ("HE_froh", "HE", "Smile", 0),
    ("HE_denkt", "HE", "Suspicious", 0), ("HE_sorge", "HE", "Concerned|Serious", 0),
    ("ME_ruhig", "ME", "Calm", 0), ("ME_redet", "ME", "Driven", 1), ("ME_denkt", "ME", "Suspicious", 0),
    ("ME_sorge", "ME", "Concerned|Serious", 0), ("ME_schreck", "ME", "Fear", 0), ("ME_froh", "ME", "Smile", 0),
    ("SA_ruhig", "SA", "Calm", 0), ("SA_redet", "SA", "Serious", 1), ("SA_denkt", "SA", "Solemn", 0),
    ("SA_froh", "SA", "Smile", 0), ("SA_skeptisch", "SA", "Suspicious", 0),
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
