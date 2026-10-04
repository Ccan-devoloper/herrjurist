"""Figuren für Folge 147 (Anscheinsbeweis, Vermutung, Beweislastumkehr; Auffahrunfall) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Hertel (HE, um 60, Hintermann, fährt auf; Stimme helmut): standing/pointing_finger-2 (schwarzes Oberteil, Hose Türkis
  #7FD6D0, erhobener Zeigefinger – er behauptet die grundlose Vollbremsung), Kopf Short 2 (Haar Grau #9C9C9C), Brille
  Glasses 2, Haut #EAC0A0, kein Bart.
Frau Kretschmer (KR, um 40, Vorderfrau, Klägerin; spricht nicht): standing/easing-2 (offene Jacke Rot #F07A6A über schwarzem
  Shirt, Hose Dunkelgrau #3A3A48), Kopf Long Bangs (Haar #5A3A26), Haut #F2C9A8.
Posen der letzten drei Folgen (144: walking-2, shirt-3; 145: resting-1, easing-1, crossed_arms-1, blazer-3; 146: resting-1,
crossed_arms-1) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine
Karikatur. Präfixe HE_/KR_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile bzw. „Augen|geschlossener
Mund“ (Concerned|Serious). Sprechende Ansicht HE_redet (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_147")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HE": ("standing/pointing_finger-2", "Short 2", None, "Glasses 2", {"Skin": "#EAC0A0", "Pants": "#7FD6D0", "Hair": "#9C9C9C"}),
    "KR": ("standing/easing-2", "Long Bangs", None, None, {"Skin": "#F2C9A8", "Jacket": "#F07A6A", "Pants": "#3A3A48",
                                                         "Hair": "#5A3A26"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Serious", 1), ("HE_ernst", "HE", "Serious", 0),
    ("HE_denkt", "HE", "Suspicious", 0), ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_schreck", "HE", "Fear", 0),
    ("HE_muede", "HE", "Tired", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_ernst", "KR", "Serious", 0), ("KR_skeptisch", "KR", "Suspicious", 0),
    ("KR_sorge", "KR", "Concerned|Serious", 0), ("KR_froh", "KR", "Smile", 0), ("KR_schreck", "KR", "Fear", 0),
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
