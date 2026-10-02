"""Figuren für Folge 037 (Arbeitnehmerhaftung, Firmenwagen) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Fiktive Figuren (keine realen Personen, keine Karikaturen):
- Imke (IM, um 30, Außendienstmitarbeiterin): standing/easing-1 (offene Jacke Blau #7FB2F0, weißes Oberteil, schwarze Hose),
  Kopf Medium Straight; nur diese eine Pose, damit das Outfit konstant bleibt. Stimme julia.
- Herr Schäfer (SC, um 55, Inhaber des Werkzeughandels, Arbeitgeber): standing/blazer-3 (dunkler Anzug #3D3D58),
  Kopf Short 4_2 mit grauem Haar, Brille Glasses 2, kein Bart. Stimme christian.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Fear, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten (IM_redet, IM_schreck_redet,
SC_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_037")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

IM_F = {"Skin": "#E9BE98", "Top": "#FFFFFF", "Jacket": "#7FB2F0", "Hair": "#3A2A20"}
SC_F = {"Skin": "#D9A07A", "Jacket": "#3D3D58", "Pants": "#3D3D58", "Hair": "#C9C9C9"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "IM": ("standing/easing-1", "Medium Straight", None, None, IM_F),
    "SC": ("standing/blazer-3", "Short 4_2", None, "Glasses 2", SC_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("IM_ruhig", "IM", "Calm", 0), ("IM_froh", "IM", "Smile", 0), ("IM_schreck", "IM", "Fear", 1),
    ("IM_sorge", "IM", "Concerned|Serious", 0), ("IM_redet", "IM", "Concerned|Serious", 1), ("IM_ernst", "IM", "Serious", 0),
    ("IM_denkt", "IM", "Suspicious", 0), ("IM_zufrieden", "IM", "Smile Big|Smile", 0), ("IM_muede", "IM", "Tired", 0),
    ("SC_ruhig", "SC", "Calm", 0), ("SC_streng", "SC", "Serious", 0), ("SC_redet", "SC", "Serious", 1),
    ("SC_denkt", "SC", "Suspicious", 0), ("SC_froh", "SC", "Smile", 0), ("SC_sorge", "SC", "Concerned|Serious", 0),
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
