"""Figuren für Folge 054 (Rechtsbehelfe in der Zwangsvollstreckung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Frau Hollmann (Inhaberin einer Autowerkstatt, Gläubigerin, um 60): standing/polka_dots (gepunktete Bluse, grüne Hose),
Kopf Gray Bun. Herr Steinbach (Schuldner, um 45): standing/pointing_finger-2 (erhobener Zeigefinger: „Aber ich habe doch
längst bezahlt!“), schwarzes Oberteil, blaue Hose, Kopf Short 4 (pointing_finger-1 verworfen: Kleidung
nur als schwarze Tuschfläche, nicht einfärbbar). Frau Weidner (seine Schwester, Dritte, um 35): standing/resting-2
(lila Hose), Kopf Medium Straight. Gerichtsvollzieher (um 55, ohne Namen): standing/shirt-4 (dunkles Hemd, dunkle Hose),
Kopf No Hair 1, Brille Glasses 4. Keine Prothesen-Posen, keine Bärte (Mund bleibt frei).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben
der Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile,
Serious, Driven, Fear, Contempt, Suspicious bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der
Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_054")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HO": ("standing/polka_dots", "Gray Bun", None, None, {"Skin": "#F0C8A8", "Pants": "#8FD694"}),
    "ST": ("standing/pointing_finger-2", "Short 4", None, None, {"Skin": "#D9A07A", "Pants": "#8DB3F2"}),
    "WE": ("standing/resting-2", "Medium Straight", None, None, {"Skin": "#E8B98F", "Pants": "#B8A9F5"}),
    "GV": ("standing/shirt-4", "No Hair 1", None, "Glasses 4", {"Skin": "#C99470", "Pants": "#3A3A48"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HO_ruhig", "HO", "Calm", 0), ("HO_redet", "HO", "Serious", 1), ("HO_streng", "HO", "Suspicious", 0),
    ("HO_sorge", "HO", "Concerned|Serious", 0), ("HO_froh", "HO", "Smile", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_redet", "ST", "Driven", 1), ("ST_schreck", "ST", "Fear", 0),
    ("ST_sorge", "ST", "Concerned|Serious", 0), ("ST_froh", "ST", "Smile", 0), ("ST_denkt", "ST", "Serious", 0),
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Driven", 1), ("WE_sorge", "WE", "Concerned|Serious", 0),
    ("WE_froh", "WE", "Smile", 0), ("WE_denkt", "WE", "Serious", 0),
    ("GV_ruhig", "GV", "Calm", 0), ("GV_redet", "GV", "Serious", 1), ("GV_denkt", "GV", "Suspicious", 0),
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
