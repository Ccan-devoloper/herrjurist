"""Figuren für Folge 041 (Verfassungsbeschwerde Schema) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Wendt (32, Hobbyimkerin): standing/resting-1 (grüner Pullover), Kopf Long.
Herr Hübner (um 60, Ordnungsamt): standing/robot_dance-2 (dunkles Oberteil, ausgestreckte Hand = übergibt den Bescheid),
  Kopf Gray Short (Haar grau), Brille Glasses.
Richterin Reuter (um 60, Bundesverwaltungsgericht): standing/resting-2 (schwarzes Oberteil wie Robe), Kopf Gray Medium
  (Haar grau), Brille Glasses 2.
Herr Seifert (um 45, Hobbyimker im Nachbarort, Gegenfall): standing/crossed_arms-1 (oranger Pullover), Kopf Short 3.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Solemn, Driven, Calm bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_041")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
GRAU_HAAR = "#D6D6D6"

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WE": ("standing/resting-1", "Long", None, None, {"Skin": "#F1C6A5", "Top": "#8FD694"}),
    "HU": ("standing/robot_dance-2", "Gray Short", None, "Glasses", {"Skin": "#E6B48F", "Pants": "#3D3D58", "Hair": GRAU_HAAR}),
    "RE": ("standing/resting-2", "Gray Medium", None, "Glasses 2", {"Skin": "#F0C8A8", "Pants": "#3D3D58", "Hair": GRAU_HAAR}),
    "SE": ("standing/crossed_arms-1", "Short 3", None, None, {"Skin": "#B07552", "Top": "#F9A66C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WE_ruhig", "WE", "Smile", 0), ("WE_redet", "WE", "Serious", 1), ("WE_sorge", "WE", "Concerned|Serious", 0),
    ("WE_denkt", "WE", "Suspicious", 0), ("WE_entschl", "WE", "Driven", 0),
    ("HU_ruhig", "HU", "Calm", 0), ("HU_redet", "HU", "Serious", 1),
    ("RE_ruhig", "RE", "Serious", 0), ("RE_redet", "RE", "Solemn", 1),
    ("SE_ruhig", "SE", "Smile", 0), ("SE_redet", "SE", "Driven", 1), ("SE_denkt", "SE", "Suspicious", 0),
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
