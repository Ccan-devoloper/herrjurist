"""Figuren für Folge 225 (Staatshaftungsrecht Überblick: Zaun, Abschleppen, Laden) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Bergner (um 60, Inhaber eines Fahrradladens): standing/shirt-2 (schwarzes Hemd, Shorts Beige #C9A66B,
Beinprothese – positive, beiläufige Darstellung, keine Täterrolle), Kopf Gray Short (hell, Originalfarbe), ohne Brille, Haut #E8B48E.
Frau Wilmsen (um 45, Tiefbauamt der Stadt): standing/crossed_arms-1 (Pullover Rot #F07A6A, Hose schwarz),
Kopf Long Bangs, ohne Brille (Abgrenzung zu Lexi), Haut #D9A07A. Sachlich, keine Bösewichtin.
Bauhof-Mitarbeiter (ohne Namen, spricht nicht): standing/walking-2 (schwarzes Shirt, Hose Dunkelgrau #4A4A58),
Mütze hat-beanie (Originalfarbe), Haut #C98E66.
Keine Bärte, keine Karikatur, keine Polka Dots. Posen nicht aus 222–224 (easing-1/-2, resting-1/-2, robot_dance-2/-3,
crossed_arms-2, shirt-3/-4, blazer-1/-3, walking-1, pointing_finger-2).
Präfix BE_/WI_/BH_ (nie ER_). Grundansicht gespiegelt (blickt nach links), _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md); sprechende Ansichten (BE_redet, WI_redet, Lexi) mit a/o/e."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_225")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "BE": ("standing/shirt-2", "Gray Short", None, None, {"Skin": "#E8B48E", "Shorts": "#C9A66B",
                                                        "Prosthesis": "#B8B8B8"}),
    "WI": ("standing/crossed_arms-1", "Long Bangs", None, None, {"Skin": "#D9A07A", "Top": "#F07A6A"}),
    "BH": ("standing/walking-2", "hat-beanie", None, None, {"Skin": "#C98E66", "Pants": "#4A4A58"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BE_ruhig", "BE", "Calm", 0), ("BE_staunt", "BE", "Awe", 0), ("BE_sorge", "BE", "Concerned|Serious", 0),
    ("BE_denkt", "BE", "Suspicious", 0), ("BE_froh", "BE", "Smile Big|Smile", 0), ("BE_ernst", "BE", "Serious", 0),
    ("BE_redet", "BE", "Concerned|Serious", 1),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_ernst", "WI", "Serious", 0), ("WI_denkt", "WI", "Suspicious", 0),
    ("WI_froh", "WI", "Smile", 0), ("WI_redet", "WI", "Serious", 1),
    ("BH_ruhig", "BH", "Calm", 0), ("BH_sorge", "BH", "Concerned|Serious", 0), ("BH_erschrocken", "BH", "Fear", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    nur = sys.argv[1:]          # optional: nur bestimmte Personen (Vorschau)
    n = 0
    for name, p, mimik, mund in LISTE:
        if nur and p not in nur:
            continue
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    if not nur:
        # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
        for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
            a = LX.AUSSEHEN
            for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
                figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
