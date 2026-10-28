"""Figuren für Folge 224 (Zeugnisverweigerungsrecht § 52 StPO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Frau Wehner (um 30, Zeugin, Stimme lucy): standing/easing-2 (offene Jacke Rosé #F2A7B8, schwarzes Oberteil der Pose,
  Hose Hellblau #8DB3F2), Kopf Medium Bangs 2.
Herr Störmer (um 35, Verlobter, Beschuldigter, spricht nicht): standing/resting-2 (schwarzes Oberteil der Pose, Hose
  Schiefergrau #6B7A8F), Kopf Short 5, ohne Bart.
Herr Ladewig (um 30, Mitbewohner, Beschuldigter in einem anderen Verfahren, spricht nicht): standing/walking-1 (Oberteil
  Senf #E8A03A, schwarze Hose der Pose), Kopf Pomp, ohne Bart.
Polizist (um 45, Stimme christian): standing/blazer-1 (Jacke Dunkelblau #33507A wie eine Uniformjacke, ohne Abzeichen,
  Hose #2B2B35; die Pose zeigt eine Unterschenkelprothese – beim Polizisten, nicht bei einer Täterrolle), Kopf No Hair 3.
Ermittlungsrichter (um 55, spricht nicht): standing/robot_dance-3 (Oberteil Schwarz #2B2B2B wie eine Robe, Hose #3A3A44),
  Kopf Short 4, Brille Glasses 4.
Richterin (Vorsitzende, um 60, Stimme hilde): standing/pointing_finger-2 (schwarzes Oberteil der Pose wie eine Robe, Hose
  #2B2B35, erhobener Zeigefinger bei der Belehrung), Kopf Gray Medium, Brille Glasses 3.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Solemn, Smile, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe). Figurenpräfix nie ER_ (Ermittlungsrichter: EJ)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_224")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WE": ("standing/easing-2", "Medium Bangs 2", None, None, {"Skin": "#E3B08C", "Jacket": "#F2A7B8", "Pants": "#8DB3F2"}),
    "ST": ("standing/resting-2", "Short 5", None, None, {"Skin": "#F2D3B8", "Pants": "#6B7A8F"}),
    "LA": ("standing/walking-1", "Pomp", None, None, {"Skin": "#C98E6A", "Top": "#E8A03A"}),
    "PZ": ("standing/blazer-1", "No Hair 3", None, None, {"Skin": "#EBC29E", "Jacket": "#33507A", "Pants": "#2B2B35"}),
    "EJ": ("standing/robot_dance-3", "Short 4", None, "Glasses 4", {"Skin": "#8D5A3C", "Top": "#2B2B2B", "Pants": "#3A3A44"}),
    "RI": ("standing/pointing_finger-2", "Gray Medium", None, "Glasses 3", {"Skin": "#F0CDB2", "Pants": "#2B2B35", "Hair": "#BDBDBD"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Serious", 1), ("WE_sorge", "WE", "Concerned|Serious", 0),
    ("WE_denkt", "WE", "Suspicious", 0), ("WE_froh", "WE", "Smile", 0), ("WE_ernst", "WE", "Serious", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_froh", "ST", "Smile", 0), ("ST_sorge", "ST", "Concerned|Serious", 0),
    ("ST_denkt", "ST", "Suspicious", 0), ("ST_muede", "ST", "Tired", 0),
    ("LA_ruhig", "LA", "Calm", 0), ("LA_froh", "LA", "Smile", 0), ("LA_sorge", "LA", "Concerned|Serious", 0),
    ("LA_denkt", "LA", "Suspicious", 0),
    ("PZ_ruhig", "PZ", "Calm", 0), ("PZ_redet", "PZ", "Calm", 1), ("PZ_ernst", "PZ", "Serious", 0),
    ("PZ_denkt", "PZ", "Suspicious", 0),
    ("EJ_ruhig", "EJ", "Calm", 0), ("EJ_ernst", "EJ", "Serious", 0), ("EJ_denkt", "EJ", "Suspicious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_ernst", "RI", "Serious", 0),
    ("RI_denkt", "RI", "Suspicious", 0),
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
