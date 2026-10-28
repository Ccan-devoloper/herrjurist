"""Figuren für Folge 062 (rechtfertigende Einwilligung, Tattoo mit 17) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Marie (17, Kundin): standing/easing-1 (offene hellblaue Jacke im Original, grünes Shirt, schwarze Hose, Sneaker), Kopf
Long Bangs, Haut #F2CDB0; sachlich-respektvoll, Alltagskleidung, kein Klischee.
Herr Riedel (um 40, Tätowierer): standing/shirt-3 (lila Hemd, schwarze Hose; Pose ohne Prothese), Kopf Short 1, ohne Bart,
Haut #E2B088; ohne Tattoo- oder Rocker-Klischee.
Keine Prothesen-Posen (shirt-1/2, blazer-1/2 verworfen), keine Bärte (Mund bleibt frei). robot_dance-3 verworfen: Silhouette
wie Lexi (robot_dance-1).
shirt-3 blickt im Original nach rechts, easing-1 nach links (geprüft im Fallbild); die Grundansicht blickt immer nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious,
Suspicious, Fear bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_062")
ORIGINAL_LINKS = {"standing/easing-1"}
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MA": ("standing/easing-1", "Long Bangs", None, None, {"Skin": "#F2CDB0", "Top": "#8FD694"}),
    "RI": ("standing/shirt-3", "Short 1", None, None, {"Skin": "#E2B088", "Top": "#B8A9F5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Serious", 1), ("MA_froh", "MA", "Smile", 0),
    ("MA_denkt", "MA", "Suspicious", 0), ("MA_sorge", "MA", "Concerned|Serious", 0), ("MA_schreck", "MA", "Fear", 0),
    ("MA_ernst", "MA", "Serious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Calm", 1), ("RI_froh", "RI", "Smile", 0),
    ("RI_denkt", "RI", "Serious", 0), ("RI_sorge", "RI", "Concerned|Serious", 0), ("RI_skeptisch", "RI", "Suspicious", 0),
    ("RI_luegt", "RI", "Smile", 1),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        # easing-1 blickt im Original nach links, shirt-3 nach rechts: Grundansicht blickt immer nach links
        orig_links = pose in ORIGINAL_LINKS
        for suffix, gespiegelt in (("", not orig_links), ("_r", orig_links)):
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
