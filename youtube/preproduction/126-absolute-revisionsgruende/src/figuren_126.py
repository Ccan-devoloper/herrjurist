"""Figuren für Folge 126 (Absolute Revisionsgründe § 338 StPO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Vorsitzender Richter der Strafkammer (um 60, Funktionsrolle ohne Namen; Stimme helmut): standing/blazer-1 (schwarzes Sakko
wie eine Robe, schwarzes Shirt, Hose Grau #4A4A55; die Pose hat eine Unterschenkelprothese – hier bewusst beim Richter, nicht
bei einer Täterrolle), Kopf Gray Short, Brille Glasses 3, ohne Bart.
Justizwachtmeister (um 50, Funktionsrolle, spricht nicht): standing/shirt-3 (Hemd Dunkelblau #3B4A6B wie eine Dienstkleidung,
schwarze Hose), Kopf Pomp (Haar #3A2A20).
Lene (Anfang 20, Jurastudentin, Zuschauerin; Stimme ela_froh): standing/walking-1 (T-Shirt Lila #B8A9F5, schwarze Hose),
Kopf Medium Bangs 2 (Haar #7A4B32).
Rechtsanwalt Strobel (um 35, Verteidiger; Stimme niklas): standing/blazer-4 (schwarzes Sakko wie eine Robe, weißes Shirt,
schwarze Hose), Kopf Flat Top.
Herr Lemke (um 45, Angeklagter, spricht nicht): standing/resting-1 (Pullover Grau #9AA3B2, schwarze Hose), Kopf Short 2
(Haar #5A4636), ohne Bart, ohne Prothese, kein Herkunfts- oder Hautfarben-Klischee.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Solemn, Smile, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe). Figurenpräfix nie ER_."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_126")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "VR": ("standing/blazer-1", "Gray Short", None, "Glasses 3", {"Skin": "#F0CDB4", "Jacket": "#2B2B2B", "Pants": "#4A4A55"}),
    "WM": ("standing/shirt-3", "Pomp", None, None, {"Skin": "#EFC9A8", "Top": "#3B4A6B", "Hair": "#3A2A20"}),
    "LE": ("standing/walking-1", "Medium Bangs 2", None, None, {"Skin": "#F2D3B8", "Top": "#B8A9F5", "Hair": "#7A4B32"}),
    "ST": ("standing/blazer-4", "Flat Top", None, None, {"Skin": "#D9A47E", "Jacket": "#2B2B2B", "Top": "#FFFFFF"}),
    "LM": ("standing/resting-1", "Short 2", None, None, {"Skin": "#E8B894", "Top": "#9AA3B2", "Hair": "#5A4636"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("VR_ruhig", "VR", "Calm", 0), ("VR_redet", "VR", "Serious", 1), ("VR_denkt", "VR", "Suspicious", 0),
    ("VR_streng", "VR", "Solemn", 0),
    ("WM_ruhig", "WM", "Calm", 0), ("WM_ernst", "WM", "Serious", 0),
    ("LE_ruhig", "LE", "Calm", 0), ("LE_redet", "LE", "Concerned|Serious", 1), ("LE_denkt", "LE", "Suspicious", 0),
    ("LE_froh", "LE", "Smile", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_redet", "ST", "Serious", 1), ("ST_denkt", "ST", "Suspicious", 0),
    ("ST_froh", "ST", "Smile", 0), ("ST_ernst", "ST", "Solemn", 0),
    ("LM_ruhig", "LM", "Calm", 0), ("LM_sorge", "LM", "Concerned|Serious", 0), ("LM_muede", "LM", "Tired", 0),
    ("LM_denkt", "LM", "Suspicious", 0),
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
