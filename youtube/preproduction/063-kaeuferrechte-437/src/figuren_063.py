"""Figuren für Folge 063 (Käuferrechte § 437 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Manfred (Käufer, Verbraucher, um 65): nur standing/shirt-3 (hellblaues Hemd, schwarze Hose), Kopf Gray Short, kein Bart.
Frau Kemper (Inhaberin des Elektrogeschäfts, um 45): nur standing/blazer-4 (grüner Blazer, hellblaues Oberteil, schwarze
Hose), Kopf Long, kein Bart. Keine Prothesen-Posen (Kopfprobe: shirt-1/-2, blazer-1/-2 verworfen).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Smile/Serious“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_063")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

MA_F = {"Skin": "#EDC4A0"}
KM_F = {"Skin": "#C99272"}
# Person: (Pose, Kopf, Bart, Brille, Farben, Grundansicht gespiegelt?)
P = {
    "MA": ("standing/shirt-3", "Gray Short", None, None, MA_F, 1),
    "KM": ("standing/blazer-4", "Long", None, None, KM_F, 1),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_froh", "MA", "Smile Big|Smile", 0), ("MA_redet", "MA", "Serious", 1),
    ("MA_aerger", "MA", "Very Angry", 1), ("MA_denkt", "MA", "Suspicious", 0), ("MA_sorge", "MA", "Concerned|Serious", 0),
    ("MA_zufrieden", "MA", "Smile", 0),
    ("KM_ruhig", "KM", "Calm", 0), ("KM_froh", "KM", "Smile", 0), ("KM_redet", "KM", "Smile", 1),
    ("KM_denkt", "KM", "Suspicious", 0), ("KM_ernst", "KM", "Serious", 0), ("KM_sorge", "KM", "Concerned|Serious", 0),
]

if __name__ == "__main__":
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben, sp = P[p]
        for suffix, gespiegelt in (("", sp), ("_r", 1 - sp)):
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
