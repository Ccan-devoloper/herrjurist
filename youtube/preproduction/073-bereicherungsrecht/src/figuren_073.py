"""Figuren für Folge 073 (Bereicherungsrecht, Fehlüberweisung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Ursula (Überweisende, um 70): nur standing/polka_dots (Oberteil mit Punkten, lila Hose), Kopf Gray Bun, Brille Glasses 4,
kein Bart.
Rüdiger (Empfänger, um 45): nur standing/shirt-4 (schwarzes Hemd, hellblaue Hose), Kopf Short 5, kein Bart.
Keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Serious/Smile“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_073")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

UR_F = {"Skin": "#F2D0B5", "Pants": "#B8A9F5"}
RD_F = {"Skin": "#D9A27A", "Pants": "#8DB3F2"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "UR": ("standing/polka_dots", "Gray Bun", None, "Glasses 4", UR_F),
    "RD": ("standing/shirt-4", "Short 5", None, None, RD_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("UR_ruhig", "UR", "Calm", 0), ("UR_schreck", "UR", "Fear", 0), ("UR_redet", "UR", "Concerned|Serious", 1),
    ("UR_sorge", "UR", "Concerned|Serious", 0), ("UR_denkt", "UR", "Suspicious", 0), ("UR_froh", "UR", "Smile", 0),
    ("UR_ernst", "UR", "Serious", 0),
    ("RD_ruhig", "RD", "Calm", 0), ("RD_grinst", "RD", "Smile Big|Smile", 1), ("RD_froh", "RD", "Smile", 0),
    ("RD_redet", "RD", "Serious", 1), ("RD_denkt", "RD", "Suspicious", 0), ("RD_sorge", "RD", "Concerned|Serious", 0),
    ("RD_ertappt", "RD", "Fear", 0),
]

if __name__ == "__main__":
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
