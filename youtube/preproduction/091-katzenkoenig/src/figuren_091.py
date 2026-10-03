"""Figuren für Folge 091 (Katzenkönig-Fall, mittelbare Täterschaft) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Echter Fall mit anderen Namen; keine realen Personen nachgebildet, keine Karikaturen, keine bösen Mimiken (kein Contempt,
kein Angry). Das Opfer wird nicht als Figur gezeigt (FOLGE-ABLAUF Abschnitt 1).
Irmgard (um 40, treibende Kraft): standing/robot_dance-3 (Oberteil Rosa #F6A5C0, Hose #3B3B4F), Kopf Long Bangs,
  Haut #F3CFB3.
Wolfram (um 45): standing/shirt-4 (schwarzes Hemd, Hose Sand #C9B48A), Kopf Short 1, Brille Glasses 4, Haut #D9A07A.
Ulrich (um 50, Polizeibeamter, Vordermann): standing/walking-1 (Oberteil Blau #8DB3F2; pointing_finger-1 verworfen: Körper ganz schwarz), Kopf No Hair 2,
  Haut #E8BE9A, ohne Bart.
Posen in 087–089 und im Testvideo (blazer-3, shirt-3, crossed_arms-1, easing-1) nicht verwendet. Alle Posen blicken im
Original nach rechts; Suffix _r = Original (blickt nach rechts), ohne Suffix gespiegelt (blickt nach links, zur Tafel).
Grundmimik immer mit geschlossenem Mund; sprechende Ansichten zusätzlich a/o/e (Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_091")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "IR": ("standing/robot_dance-3", "Long Bangs", None, None, {"Skin": "#F3CFB3", "Top": "#F6A5C0", "Pants": "#3B3B4F"}),
    "WO": ("standing/shirt-4", "Short 1", None, "Glasses 4", {"Skin": "#D9A07A", "Pants": "#C9B48A"}),
    "UL": ("standing/walking-1", "No Hair 2", None, None, {"Skin": "#E8BE9A", "Top": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("IR_ruhig", "IR", "Calm", 0), ("IR_redet", "IR", "Serious", 1), ("IR_ernst", "IR", "Serious", 0),
    ("IR_still", "IR", "Solemn", 0), ("IR_kuehl", "IR", "Suspicious", 0),
    ("WO_ruhig", "WO", "Calm", 0), ("WO_redet", "WO", "Serious", 1), ("WO_ernst", "WO", "Serious", 0),
    ("WO_still", "WO", "Solemn", 0), ("WO_kuehl", "WO", "Suspicious", 0),
    ("UL_ruhig", "UL", "Calm", 0), ("UL_staunt", "UL", "Awe", 0), ("UL_redet", "UL", "Concerned|Serious", 1),
    ("UL_zweifel", "UL", "Concerned|Serious", 0), ("UL_glaubt", "UL", "Driven", 0), ("UL_denkt", "UL", "Serious", 0),
    ("UL_schuld", "UL", "Tired", 0), ("UL_still", "UL", "Solemn", 0),
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
