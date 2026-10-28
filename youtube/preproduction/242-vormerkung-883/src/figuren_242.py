"""Figuren für Folge 242 (Vormerkung, §§ 883 ff. BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Mats (MA, um 32, Erstkäufer, Vormerkungsberechtigter; Stimme niklas): standing/walking-2 (schwarzes T-Shirt der Pose,
  Hose Grün #8FD694, weiße Schuhe), Kopf Flat Top, Haut #D9A07A, kein Bart, keine Brille.
Herr Stenzel (ST, um 65, Verkäufer, eingetragener Eigentümer; Stimme helmut): standing/blazer-3 (Sakko Camel #D6A06E,
  Oberteil Schwarz, Hose Dunkelgrau #3D3D48), Kopf No Hair 2, Brille Glasses 2, Haut #E9BE9C, kein Bart. Keine Karikatur,
  kein Bösewicht-Klischee: freundlich, später nachdenklich.
Frau Ostendorf (OS, um 38, Zweitkäuferin, „Meistbietende“; Stimme ela_froh): standing/pointing_finger-2 (schwarzes Oberteil
  der Pose, Hose Rot #F07A6A, schwarze Stiefel), Kopf Long, Haut #F1C6A5.
Posen der letzten drei Folgen (239: resting-2, shirt-4, easing-1; 240: easing-1, walking-1, shirt-3; 241: easing-2,
crossed_arms-2, blazer-4) nicht verwendet; robot_dance-1 bleibt Lexi; Prothesen-Posen (blazer-1, blazer-2, shirt-1/2)
verworfen; keine Polka Dots, keine Bärte. Präfixe MA_/ST_/OS_ (nie ER_). Alle Posen blicken im Original nach rechts;
Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten MA_redet (Smile), ST_redet (Smile),
OS_redet (Smile Big|Smile) und Lexi zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_242")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "MA": ("standing/walking-2", "Flat Top", None, None, {"Skin": "#D9A07A", "Pants": "#8FD694"}),
    "ST": ("standing/blazer-3", "No Hair 2", None, "Glasses 2", {"Skin": "#E9BE9C", "Jacket": "#D6A06E", "Pants": "#3D3D48"}),
    "OS": ("standing/pointing_finger-2", "Long", None, None, {"Skin": "#F1C6A5", "Pants": "#F07A6A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_froh", "MA", "Smile", 0), ("MA_freut", "MA", "Smile Big|Smile", 0),
    ("MA_sorge", "MA", "Concerned|Serious", 0), ("MA_schreck", "MA", "Fear", 0), ("MA_denkt", "MA", "Suspicious", 0),
    ("MA_staunt", "MA", "Awe", 0), ("MA_ernst", "MA", "Serious", 0),
    ("MA_redet", "MA", "Smile", 1),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_froh", "ST", "Smile", 0), ("ST_denkt", "ST", "Suspicious", 0),
    ("ST_ernst", "ST", "Serious", 0), ("ST_still", "ST", "Solemn", 0), ("ST_sorge", "ST", "Concerned|Serious", 0),
    ("ST_redet", "ST", "Smile", 1),
    ("OS_froh", "OS", "Smile", 0), ("OS_ruhig", "OS", "Calm", 0), ("OS_denkt", "OS", "Suspicious", 0),
    ("OS_ernst", "OS", "Serious", 0), ("OS_sorge", "OS", "Concerned|Serious", 0), ("OS_staunt", "OS", "Awe", 0),
    ("OS_redet", "OS", "Smile Big|Smile", 1),
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
