"""Figuren für Folge 052 (Anscheinsgefahr) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Jäger (um 45, Nachbarin): standing/crossed_arms-2 (schwarzes Oberteil, lila Hose, verschränkte Arme), Kopf Bun.
Polizist Ahrens (um 30): standing/shirt-3 (blaues Hemd wie eine Uniform, schwarze Hose), Kopf Short 5.
Herr Böttcher (um 72, Mieter): standing/walking-1 (blaues T-Shirt, schwarze Hose, weiße Schuhe), Kopf No Hair 2, Mimik Old;
im Wohnzimmer sitzend sitting/mid-2 (gleiches Outfit: blaues T-Shirt, schwarze Hose, weiße Schuhe; gleicher Kopf und Hautton).
Keine Bärte, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Old, Serious, Suspicious, Driven, Awe, Tired, Smile bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_red…, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_052")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

BLAU = "#8DB3F2"
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "JA": ("standing/crossed_arms-2", "Bun", None, None, {"Skin": "#D9A07A"}),
    "AH": ("standing/shirt-3", "Short 5", None, None, {"Skin": "#C68C66", "Top": BLAU}),
    "BO": ("standing/walking-1", "No Hair 2", None, None, {"Skin": "#F0C8A8", "Top": BLAU}),
    "BS": ("sitting/mid-2", "No Hair 2", None, None, {"Skin": "#F0C8A8", "Top": BLAU}),   # Herr Böttcher sitzend
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JA_ruhig", "JA", "Serious", 0), ("JA_sorge", "JA", "Concerned|Serious", 0), ("JA_redet", "JA", "Concerned|Serious", 1),
    ("JA_denkt", "JA", "Suspicious", 0),
    ("AH_ruhig", "AH", "Serious", 0), ("AH_entschl", "AH", "Driven", 0), ("AH_redet", "AH", "Driven", 1),
    ("AH_denkt", "AH", "Suspicious", 0), ("AH_froh", "AH", "Smile", 0),
    ("BO_ruhig", "BO", "Old", 0), ("BO_staunt", "BO", "Awe", 0), ("BO_sorge", "BO", "Concerned|Serious", 0),
    ("BO_redet", "BO", "Concerned|Serious", 1), ("BO_denkt", "BO", "Suspicious", 0), ("BO_muede", "BO", "Tired", 0),
    ("BS_ruhig", "BS", "Old", 0), ("BS_staunt", "BS", "Awe", 0), ("BS_redet", "BS", "Awe", 1),
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
