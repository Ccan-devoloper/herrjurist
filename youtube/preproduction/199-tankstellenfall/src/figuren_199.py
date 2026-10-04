"""Figuren für Folge 199 (Tankstellenfall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Armin (AR, um 35, Kunde, hat das Portemonnaie vergessen, sympathisch und ehrlich; Stimme marc): standing/easing-2
  (offene Jacke Orange #F9A66C über schwarzem Shirt, Hose Schiefer #3F4A5A, weiße Turnschuhe), Kopf Short 4 (dunkles Haar),
  Haut #E3B08C, keine Brille, kein Bart.
Margarete (MA, um 50, Pächterin der Tankstelle an der Kasse; Stimme laura_ruhig): standing/pointing_finger-1 (schwarzes
  Langarmshirt und Hose, Zeigefinger erhoben), Kopf Medium Bangs 3 (dunkles Haar mit Pony), Brille Glasses 2, Haut #F2CDB2.
Posen der letzten drei Folgen (196: robot_dance-2, blazer-4, crossed_arms-2; 197: easing-1, blazer-1; 198: easing-1,
resting-1) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen, keine Bärte. Präfixe AR_/MA_
(nie ER_). Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Tired, Solemn
bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten AR_redet (Calm), AR_klagt (Concerned|Serious),
MA_redet (Calm), MA_froh_redet (Smile) und Lexi zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_199")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "AR": ("standing/easing-2", "Short 4", None, None, {"Skin": "#E3B08C", "Jacket": "#F9A66C", "Pants": "#3F4A5A"}),
    "MA": ("standing/pointing_finger-1", "Medium Bangs 3", None, "Glasses 2", {"Skin": "#F2CDB2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("AR_ruhig", "AR", "Calm", 0), ("AR_froh", "AR", "Smile", 0), ("AR_staunt", "AR", "Awe", 0), ("AR_schreck", "AR", "Fear", 0),
    ("AR_sorge", "AR", "Concerned|Serious", 0), ("AR_denkt", "AR", "Suspicious", 0), ("AR_muede", "AR", "Tired", 0),
    ("AR_still", "AR", "Solemn", 0), ("AR_ernst", "AR", "Serious", 0),
    ("AR_redet", "AR", "Calm", 1), ("AR_klagt", "AR", "Concerned|Serious", 1),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_froh", "MA", "Smile", 0), ("MA_ernst", "MA", "Serious", 0),
    ("MA_denkt", "MA", "Suspicious", 0), ("MA_redet", "MA", "Calm", 1), ("MA_froh_redet", "MA", "Smile", 1),
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
