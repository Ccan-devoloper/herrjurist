"""Figuren für Folge 028 (Brokdorf-Beschluss) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Herr Böhm (um 50, Mitarbeiter beim Landrat des Kreises Steinburg, Versammlungsbehörde): standing/shirt-4 (schwarzes Hemd,
dunkle Hose), Kopf Short 1, Glasses 3. Elke (um 55, Anwohnerin in der Wilstermarsch, will friedlich demonstrieren):
standing/resting-1 (lila Pullover), Kopf Gray Medium. Keine Bärte, keine Prothesen-Posen, keine realen Personen.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious bzw. „Augen|geschlossener
Mund“ (Concerned|Serious). Sprechende Ansichten (BO_redet, EL_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_028")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BO": ("standing/shirt-4", "Short 1", None, "Glasses 3", {"Skin": "#E8B98F", "Pants": "#3D3D58"}),
    "EL": ("standing/resting-1", "Gray Medium", None, None, {"Skin": "#F1C6A5", "Top": "#B8A9F5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BO_ruhig", "BO", "Calm", 0), ("BO_redet", "BO", "Serious", 1), ("BO_ernst", "BO", "Serious", 0),
    ("BO_denkt", "BO", "Suspicious", 0),
    ("EL_ruhig", "EL", "Smile", 0), ("EL_redet", "EL", "Smile", 1), ("EL_froh", "EL", "Cute", 0),
    ("EL_sorge", "EL", "Concerned|Serious", 0), ("EL_denkt", "EL", "Suspicious", 0), ("EL_ernst", "EL", "Serious", 0),
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
