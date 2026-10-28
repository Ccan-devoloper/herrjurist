"""Figuren für Folge 108 (Bescheidungsurteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Herr Haberland (um 50, Wirt des Gasthauses am Marktplatz, Kläger): standing/robot_dance-3 (korallrotes Oberteil, dunkelblaue
Hose), Kopf Short 3 (dunkles Haar).
Frau Seeger (um 60, Sachbearbeiterin der Stadt): standing/pointing_finger-1 (schwarzes Kostüm; durchgehendes Oberteil der Pose, Einfärbung greift nicht), Kopf Gray Bun,
Brille Glasses 4.
Die Richterin (um 35, Verwaltungsgericht): standing/crossed_arms-1 (dunkelgraues Oberteil, dunkle Hose), Kopf Long (dunkles
Haar), Brille Glasses 2.
Posen bewusst anders als in 102 (polka_dots, shirt-3, easing-2) und 105–107 (resting-1/2, walking-2, blazer-2/3/4,
crossed_arms-2, shirt-3). Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Driven, Solemn, Smile, Cute bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_108")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HA": ("standing/robot_dance-3", "Short 3", None, None, {"Skin": "#E8B998", "Top": "#F07A6A", "Pants": "#3D4A7A", "Hair": "#6B4A2E"}),
    "SE": ("standing/pointing_finger-1", "Gray Bun", None, "Glasses 4", {"Skin": "#F2C7A8", "Top": "#B8A9F5", "Pants": "#4A4A55"}),
    "RI": ("standing/crossed_arms-1", "Long", None, "Glasses 2", {"Skin": "#D9A07A", "Top": "#4A4A55", "Pants": "#3A3A48", "Hair": "#2E2420"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Driven", 1), ("HA_hofft", "HA", "Cute", 0),
    ("HA_sorge", "HA", "Concerned|Serious", 0), ("HA_aerger", "HA", "Rage|Serious", 0), ("HA_denkt", "HA", "Suspicious", 0),
    ("HA_froh", "HA", "Smile", 0),
    ("SE_ruhig", "SE", "Calm", 0), ("SE_redet", "SE", "Serious", 1), ("SE_denkt", "SE", "Solemn", 0),
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
