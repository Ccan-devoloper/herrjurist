"""Figuren für Folge 209 (Schadensersatz statt der Leistung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Jörn (JO, um 30, Käufer der Felgen, privat; Stimme niklas): standing/easing-2 (offenes Hemd Rot #F07A6A über schwarzem
  Shirt der Pose, Hose Blau #8DB3F2, Turnschuhe), Kopf Short 1, Haut #F2D0B4, kein Bart.
Ingolf (IN, um 60, Inhaber des Reifenhandels, Verkäufer; Stimme helmut): standing/shirt-3 (Hemd Gelb #F9D56E, schwarze Hose
  der Pose), Kopf No Hair 3, Brille Glasses 4, Haut #EBC3A2, kein Bart. Kein Bösewicht: vertröstet, ist überrascht.
Herta (HE, um 35, Inhaberin eines anderen Reifenhandels; Stimme ela_froh, ein freundlicher Satz): standing/pointing_finger-2
  (schwarzes Oberteil der Pose, Hose Grün #8FD694, zeigt auf die Felgen), Kopf Medium Straight, Haut #C99572.
Posen der letzten drei Folgen (206: pointing_finger-1, robot_dance-2, resting-1; 207: blazer-3, walking-1, shirt-4; 208:
robot_dance-3, walking-2, blazer-4) nicht verwendet; robot_dance-1 bleibt Lexi; blazer-1, blazer-2, shirt-1/2 (Prothesen)
verworfen; keine Polka Dots, keine Bärte. Präfixe JO_/IN_/HE_ (nie ER_). Alle Posen blicken im Original nach rechts;
Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten JO_redet (Serious), JO_fordert
(Serious), IN_redet (Smile), IN_klagt (Concerned|Serious), HE_redet (Smile Big|Smile) und Lexi zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_209")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "JO": ("standing/easing-2", "Short 1", None, None, {"Skin": "#F2D0B4", "Jacket": "#F07A6A", "Pants": "#8DB3F2"}),
    "IN": ("standing/shirt-3", "No Hair 3", None, "Glasses 4", {"Skin": "#EBC3A2", "Top": "#F9D56E"}),
    "HE": ("standing/pointing_finger-2", "Medium Straight", None, None, {"Skin": "#C99572", "Pants": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JO_ruhig", "JO", "Calm", 0), ("JO_froh", "JO", "Smile", 0), ("JO_ernst", "JO", "Serious", 0),
    ("JO_denkt", "JO", "Suspicious", 0), ("JO_sorge", "JO", "Concerned|Serious", 0), ("JO_muede", "JO", "Tired", 0),
    ("JO_freut", "JO", "Smile Big|Smile", 0),
    ("JO_redet", "JO", "Serious", 1), ("JO_fordert", "JO", "Serious", 1),
    ("IN_ruhig", "IN", "Calm", 0), ("IN_froh", "IN", "Smile", 0), ("IN_sorge", "IN", "Concerned|Serious", 0),
    ("IN_schreck", "IN", "Fear", 0), ("IN_denkt", "IN", "Suspicious", 0), ("IN_still", "IN", "Solemn", 0),
    ("IN_staunt", "IN", "Awe", 0),
    ("IN_redet", "IN", "Smile", 1), ("IN_klagt", "IN", "Concerned|Serious", 1),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_froh", "HE", "Smile", 0), ("HE_redet", "HE", "Smile Big|Smile", 1),
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
