"""Figuren für Folge 064 (Abschleppfall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Kaiser (um 40, Fahrerin und Halterin): standing/walking-2 (schwarzes Shirt, blaue Hose), Kopf Medium Straight.
Herr Meier (um 55, Verkehrsüberwachung im Ordnungsamt): standing/pointing_finger-1 (schwarzes Oberteil), Kopf Gray Short.
Herr Becker (um 30, Abschleppdienst): standing/crossed_arms-1 (orangefarbenes Arbeitsshirt), Kopf Short 4.
Keine Bärte, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Calm, Driven, Tired, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_064")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KA": ("standing/walking-2", "Medium Straight", None, None, {"Skin": "#F1C6A5", "Pants": "#8DB3F2", "Hair": "#7A4B32"}),
    "ME": ("standing/pointing_finger-1", "Gray Short", None, None, {"Skin": "#E6B48F", "Hair": "#B4B4BC"}),
    "BE": ("standing/crossed_arms-1", "Short 4", None, None, {"Skin": "#D9A07A", "Top": "#F9A66C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KA_froh", "KA", "Smile", 0), ("KA_redet", "KA", "Smile", 1), ("KA_sorge", "KA", "Concerned|Serious", 0),
    ("KA_aerger", "KA", "Rage|Serious", 0), ("KA_aerger_redet", "KA", "Rage|Serious", 1), ("KA_denkt", "KA", "Suspicious", 0),
    ("KA_muede", "KA", "Tired", 0),
    ("ME_ruhig", "ME", "Calm", 0), ("ME_ernst", "ME", "Serious", 0), ("ME_redet", "ME", "Serious", 1),
    ("ME_denkt", "ME", "Suspicious", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Calm", 1),
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
