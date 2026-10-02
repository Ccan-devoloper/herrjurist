"""Figuren für Folge 079 (Lederspray-Fall, Sondersitzung der Geschäftsführung) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Keine Prothesen-Posen für die Täterrollen (blazer-1/-2, shirt-1/-2 deshalb nicht verwendet).
Eberhard (um 60, Geschäftsführer, dominant): standing/pointing_finger-2 (schwarzer Pullover, Hose Marine #4A5A85),
  Kopf No Hair 3, Brille Glasses 2, Haut #E2B08C, ohne Bart.
Almut (um 50, Geschäftsführerin): standing/blazer-3 (Blazer Lila #B8A9F5, Hose #3B3B4F), Kopf Medium Bangs 3,
  Haut #F0C8A8.
Hauke (um 35, Geschäftsführer): standing/blazer-4 (Blazer Blau #8DB3F2, Oberteil Weiß), Kopf Short 2, Haut #E8BE9A.
Laborleiterin (um 40): standing/doctor-nurse-02 (Laborkittel), Kopf Long, Haut #C68A62.
Sachlich, keine Dämonisierung: keine bösen Mimiken (kein Contempt, kein Angry). Alle Posen blicken im Original nach
rechts; Grundansicht gespiegelt (blickt nach links, zur Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit
geschlossenem Mund (FOLGE-ABLAUF.md); sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_079")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "EB": ("standing/pointing_finger-2", "No Hair 3", None, "Glasses 2", {"Skin": "#E2B08C", "Pants": "#4A5A85"}),
    "AL": ("standing/blazer-3", "Medium Bangs 3", None, None, {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Pants": "#3B3B4F"}),
    "HA": ("standing/blazer-4", "Short 2", None, None, {"Skin": "#E8BE9A", "Jacket": "#8DB3F2", "Top": "#FFFFFF"}),
    "LL": ("standing/doctor-nurse-02", "Long", None, None, {"Skin": "#C68A62"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("EB_ruhig", "EB", "Calm", 0), ("EB_redet", "EB", "Serious", 1), ("EB_ernst", "EB", "Serious", 0),
    ("EB_skeptisch", "EB", "Suspicious", 0), ("EB_still", "EB", "Solemn", 0), ("EB_sorge", "EB", "Concerned|Serious", 0),
    ("AL_ruhig", "AL", "Calm", 0), ("AL_redet", "AL", "Calm", 1), ("AL_ernst", "AL", "Serious", 0),
    ("AL_still", "AL", "Solemn", 0), ("AL_sorge", "AL", "Concerned|Serious", 0),
    ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Concerned|Serious", 1), ("HA_ernst", "HA", "Serious", 0),
    ("HA_still", "HA", "Solemn", 0), ("HA_sorge", "HA", "Concerned|Serious", 0), ("HA_zweifel", "HA", "Suspicious", 0),
    ("LL_ernst", "LL", "Serious", 0), ("LL_redet", "LL", "Serious", 1),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
