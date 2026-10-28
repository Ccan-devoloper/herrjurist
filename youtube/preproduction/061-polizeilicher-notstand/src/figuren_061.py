"""Figuren für Folge 061 (Polizeilicher Notstand) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Brandt (um 35, Mieterin, Mutter von zwei Kindern): standing/resting-1 (blauer Pullover, schwarze Hose), Kopf Long.
Herr Bauer (um 65, Vermieter): standing/blazer-3 (grünes Sakko, schwarzes Shirt, graue Hose), Kopf Gray Short.
Herr Schmitz (um 30, Ordnungsamt): standing/easing-2 (hellblaues Hemd offen über Schwarz, gelbe Hose), Kopf Short 2.
Keine Bärte, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Serious, Tired, Suspicious, Driven, Calm, Old, Smile bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_061")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

BLAU = "#8DB3F2"
GRUEN = "#8FD694"
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BR": ("standing/resting-1", "Long", None, None, {"Skin": "#E8B98F", "Top": BLAU, "Hair": "#6B4A3A"}),
    "BA": ("standing/blazer-3", "Gray Short", None, None, {"Skin": "#F0C8A8", "Jacket": GRUEN, "Pants": "#9A9AA6"}),
    "SC": ("standing/easing-2", "Short 2", None, None, {"Skin": "#D9A07A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BR_ruhig", "BR", "Serious", 0), ("BR_sorge", "BR", "Concerned|Serious", 0), ("BR_redet", "BR", "Concerned|Serious", 1),
    ("BR_muede", "BR", "Tired", 0), ("BR_froh", "BR", "Smile", 0),
    ("BA_ruhig", "BA", "Old", 0), ("BA_aerger", "BA", "Suspicious", 0), ("BA_redet", "BA", "Serious", 1),
    ("BA_denkt", "BA", "Serious", 0), ("BA_froh", "BA", "Smile", 0),
    ("SC_ruhig", "SC", "Calm", 0), ("SC_denkt", "SC", "Suspicious", 0), ("SC_redet", "SC", "Driven", 1),
    ("SC_ernst", "SC", "Serious", 0),
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
