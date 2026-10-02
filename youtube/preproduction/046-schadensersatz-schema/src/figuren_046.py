"""Figuren für Folge 046 (Schadensersatz Schema, Waschmaschinen-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Fiktive Figuren (keine realen Personen, keine Karikaturen):
- Gisela (GI, um 60, Käuferin, Verbraucherin): standing/resting-1 (Oberteil Lila #B8A9F5, schwarze Hose), Kopf Gray Bun,
  Brille Glasses 4, Haut #F0C8A8; nur diese eine Pose, damit das Outfit konstant bleibt. Stimme hilde.
- Herr Kranz (KR, um 30, Elektrohändler, liefert und schließt selbst an): standing/shirt-4 (dunkles Hemd, Arbeitshose
  Blau #5A6E9A), Kopf Short 5, kein Bart, keine Brille, Haut #E2B08C. Stimme timo.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Tired, Very Angry bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (GI_redet, KR_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_046")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

GI_F = {"Skin": "#F0C8A8", "Top": "#B8A9F5"}
KR_F = {"Skin": "#E2B08C", "Pants": "#5A6E9A"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "GI": ("standing/resting-1", "Gray Bun", None, "Glasses 4", GI_F),
    "KR": ("standing/shirt-4", "Short 5", None, None, KR_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("GI_ruhig", "GI", "Calm", 0), ("GI_froh", "GI", "Smile", 0), ("GI_schreck", "GI", "Fear", 0),
    ("GI_sorge", "GI", "Concerned|Serious", 0), ("GI_redet", "GI", "Fear", 1), ("GI_aerger", "GI", "Very Angry", 0),
    ("GI_denkt", "GI", "Suspicious", 0), ("GI_ernst", "GI", "Serious", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_froh", "KR", "Smile", 0), ("KR_redet", "KR", "Concerned|Serious", 1),
    ("KR_sorge", "KR", "Concerned|Serious", 0), ("KR_schreck", "KR", "Fear", 0), ("KR_ernst", "KR", "Serious", 0),
    ("KR_muede", "KR", "Tired", 0), ("KR_denkt", "KR", "Suspicious", 0),
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
