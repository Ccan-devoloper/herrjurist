"""Figuren für Folge 102 (Anfechtungsurteil Tenor) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Rehbein (um 60, betreibt eine Wäscherei, Klägerin): standing/polka_dots (weiße Bluse mit schwarzen Punkten, dunkelblaue
Hose), Kopf Gray Medium (grau eingefärbt).
Herr Zimmermann (um 45, Gebührenabteilung der Stadt): standing/shirt-3 (hellblaues Hemd, schwarze Hose), Kopf Short 2,
Brille Glasses 3.
Der Richter (um 55, Verwaltungsgericht): standing/easing-2 (dunkelgraues offenes Hemd über schwarzem Shirt, dunkle Hose),
Kopf No Hair 2, Brille Glasses 2.
Posen bewusst anders als in 096–099 (resting-1/2, easing-1, blazer-1/3/4, crossed_arms-1, pointing_finger-2, walking-1/3,
shirt-4) und 093 (robot_dance-2, pointing_finger-1). Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Driven, Solemn, Smile bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_102")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RE": ("standing/polka_dots", "Gray Medium", None, None, {"Skin": "#F2C7A8", "Pants": "#3D4A7A", "Hair": "#C4C4CC"}),
    "ZI": ("standing/shirt-3", "Short 2", None, "Glasses 3", {"Skin": "#E0AC88", "Top": "#8DB3F2"}),
    "RI": ("standing/easing-2", "No Hair 2", None, "Glasses 2", {"Skin": "#D9A07A", "Jacket": "#4A4A55", "Pants": "#3A3A48"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RE_ruhig", "RE", "Calm", 0), ("RE_redet", "RE", "Driven", 1), ("RE_sorge", "RE", "Concerned|Serious", 0),
    ("RE_aerger", "RE", "Rage|Serious", 0), ("RE_denkt", "RE", "Suspicious", 0), ("RE_froh", "RE", "Smile", 0),
    ("ZI_ruhig", "ZI", "Calm", 0), ("ZI_redet", "ZI", "Serious", 1), ("ZI_denkt", "ZI", "Solemn", 0),
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
