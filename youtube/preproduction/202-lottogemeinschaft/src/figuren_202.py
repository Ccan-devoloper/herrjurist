"""Figuren für Folge 202 (Lottogemeinschaft) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Hilmar (HI, um 55, gibt den Schein ab, vergisst ihn einmal; Stimme william): standing/robot_dance-3 (Pullover Grün #8FD694,
  Hose Dunkelblau #3D3D58, weiße Schuhe, offene Hand), Kopf Gray Short (graues Haar), Brille Glasses 4, Haut #E8B894, kein Bart.
Erna (EN, um 45, Kollegin; Stimme sabrina): standing/blazer-3 (Blazer Rot #F07A6A über schwarzem Oberteil, Hose Schiefer
  #3F4A5A, Hand an der Hüfte), Kopf Medium 3, Haut #C99470, keine Brille.
Ulf (UL, um 35, Kollege; Stimme marc): standing/shirt-4 (schwarzes Hemd, Hose Gelb #F9D56E; Blau verworfen, weil Herr Tiemann in 200 schwarzes Oberteil mit blauer Hose trug), Kopf Medium 1, Haut #F0C8A8.
Posen der letzten Folgen (197: easing-1, blazer-1; 198: easing-1, resting-1; 199: easing-2, pointing_finger-1; 200: shirt-3,
resting-2, walking-1, walking-2) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen, keine
Bärte. Präfixe HI_/EN_/UL_ (nie ER_). Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach
links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Tired, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten HI_klagt (Concerned|Serious),
EN_redet (Smile Big|Smile), EN_froh_redet (Smile), UL_redet (Serious) und Lexi zusätzlich mit a/o/e: Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_202")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HI": ("standing/robot_dance-3", "Gray Short", None, "Glasses 4", {"Skin": "#E8B894", "Top": "#8FD694", "Pants": "#3D3D58"}),
    "EN": ("standing/blazer-3", "Medium 3", None, None, {"Skin": "#C99470", "Jacket": "#F07A6A", "Pants": "#3F4A5A"}),
    "UL": ("standing/shirt-4", "Medium 1", None, None, {"Skin": "#F0C8A8", "Pants": "#F9D56E"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HI_ruhig", "HI", "Calm", 0), ("HI_froh", "HI", "Smile", 0), ("HI_sorge", "HI", "Concerned|Serious", 0),
    ("HI_schreck", "HI", "Fear", 0), ("HI_muede", "HI", "Tired", 0), ("HI_still", "HI", "Solemn", 0),
    ("HI_ernst", "HI", "Serious", 0), ("HI_denkt", "HI", "Suspicious", 0), ("HI_klagt", "HI", "Concerned|Serious", 1),
    ("EN_ruhig", "EN", "Calm", 0), ("EN_froh", "EN", "Smile", 0), ("EN_staunt", "EN", "Awe", 0),
    ("EN_ernst", "EN", "Serious", 0), ("EN_denkt", "EN", "Suspicious", 0), ("EN_sorge", "EN", "Concerned|Serious", 0),
    ("EN_freut", "EN", "Smile Big|Smile", 0), ("EN_redet", "EN", "Smile Big|Smile", 1), ("EN_froh_redet", "EN", "Smile", 1),
    ("UL_ruhig", "UL", "Calm", 0), ("UL_froh", "UL", "Smile", 0), ("UL_ernst", "UL", "Serious", 0),
    ("UL_denkt", "UL", "Suspicious", 0), ("UL_staunt", "UL", "Awe", 0), ("UL_redet", "UL", "Serious", 1),
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
