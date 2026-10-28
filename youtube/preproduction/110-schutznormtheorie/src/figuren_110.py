"""Figuren für Folge 110 (Schutznormtheorie) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Brüning (um 68, Nachbarin, Klägerin): standing/shirt-4 (schwarze Bluse der Pose, Hose Lila #B8A9F5), Kopf Medium Bangs 2
(graues Haar #C9C6C0), Brille Glasses 2.
Frau Hoppe (um 28, Betreiberin der Shisha-Bar, Adressatin der Erlaubnis): standing/easing-1 (offenes hellblaues Hemd der Pose
über lila Shirt, schwarze Hose), Kopf Bangs 2 (dunkles Haar #2E2420; bewusst kein Dutt, um sie von Lexi zu unterscheiden).
Der Richter (um 50, Verwaltungsgericht, Funktionsrolle): standing/blazer-1 (dunkelblauer Blazer #3D4E6E, schwarzes Oberteil,
Hose Weiß; die Pose hat eine Beinprothese – bewusst bei einer positiven Rolle), Kopf Short 5, Brille Glasses.
Posen bewusst anders als in 107–109 (shirt-3, resting-2, blazer-3, robot_dance-3, pointing_finger-1, crossed_arms-1,
easing-2, walking-3) und 105/106 (resting-1, walking-2, blazer-2, blazer-4, crossed_arms-2); keine Polka-Dots, keine Bärte.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Tired bzw. „Augen|geschlossener
Mund“ (Concerned|Serious, Cheeky|Smile). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik +
Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_110")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "BR": ("standing/shirt-4", "Medium Bangs 2", None, "Glasses 2", {"Skin": "#F2D3B8", "Pants": "#B8A9F5", "Hair": "#C9C6C0"}),
    "HO": ("standing/easing-1", "Bangs 2", None, None, {"Skin": "#E3B48E", "Hair": "#2E2420"}),
    "RI": ("standing/blazer-1", "Short 5", None, "Glasses", {"Skin": "#C68E62", "Jacket": "#3D4E6E", "Pants": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Concerned|Serious", 1), ("BR_sorge", "BR", "Concerned|Serious", 0),
    ("BR_denkt", "BR", "Suspicious", 0), ("BR_froh", "BR", "Smile", 0), ("BR_muede", "BR", "Tired", 0),
    ("HO_ruhig", "HO", "Calm", 0), ("HO_redet", "HO", "Smile", 1), ("HO_stolz", "HO", "Cheeky|Smile", 0),
    ("HO_denkt", "HO", "Suspicious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1),
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
