"""Figuren für Folge 075 (Mordmerkmale) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Fall 1: Norbert (um 50, Täter aus Wut): standing/crossed_arms-1 (Pullover Blau #8DB3F2, schwarze Hose), Kopf Short 2, Haut #E8B894.
        Horst (um 55, Nachbar, spricht nicht): standing/resting-1 (Pullover Rot #F07A6A, schwarze Hose), Kopf Short 4, Haut #D9A27A.
Fall 2: Dietmar (um 75, Onkel): standing/shirt-3 (Hemd Lila #B8A9F5, schwarze Hose), Kopf Short 4_2 (graues Haar), Haut #EDC1A0.
        Friederike (um 30, Nichte, Täterin aus Habgier): standing/easing-2 (Jacke Grün #8FD694, schwarze Hose), Kopf Long (dunkelbraun), Haut #F0C8A8.
Täter und Opfer neutral, keine Gewaltpose, keine Waffe; keine Prothesen-Posen; keine Bärte. Alle Posen blicken im Original nach
rechts; die Grundansicht blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Very Angry, Solemn, Tired,
„Concerned|Serious“. Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic
(Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_075")
ORIGINAL_LINKS = set()
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "NO": ("standing/crossed_arms-1", "Short 2", None, None, {"Skin": "#E8B894", "Top": "#8DB3F2", "Hair": "#5A3E2B"}),
    "HO": ("standing/resting-1", "Short 4", None, None, {"Skin": "#D9A27A", "Top": "#F07A6A", "Hair": "#3B2A20"}),
    "DI": ("standing/shirt-3", "Short 4_2", None, None, {"Skin": "#EDC1A0", "Top": "#B8A9F5", "Hair": "#BFBFBF", "Fill": "#BFBFBF"}),
    "FR": ("standing/easing-2", "Long", None, None, {"Skin": "#F0C8A8", "Jacket": "#8FD694", "Pants": "#151515", "Hair": "#4A3022"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("NO_ruhig", "NO", "Calm", 0), ("NO_ernst", "NO", "Serious", 0), ("NO_aerger", "NO", "Suspicious", 0),
    ("NO_wut", "NO", "Very Angry", 1), ("NO_muede", "NO", "Tired", 0), ("NO_still", "NO", "Solemn", 0),
    ("HO_ruhig", "HO", "Calm", 0), ("HO_ernst", "HO", "Serious", 0), ("HO_sorge", "HO", "Concerned|Serious", 0),
    ("DI_ruhig", "DI", "Calm", 0), ("DI_redet", "DI", "Smile", 1), ("DI_froh", "DI", "Smile", 0), ("DI_ernst", "DI", "Serious", 0),
    ("FR_ruhig", "FR", "Calm", 0), ("FR_froh", "FR", "Smile", 0), ("FR_denkt", "FR", "Suspicious", 0),
    ("FR_redet", "FR", "Serious", 1), ("FR_ernst", "FR", "Serious", 0), ("FR_still", "FR", "Solemn", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        orig_links = pose in ORIGINAL_LINKS
        for suffix, gespiegelt in (("", not orig_links), ("_r", orig_links)):
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
