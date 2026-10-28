"""Figuren für Folge 189 (Rechtfertigender Notstand § 34 StGB: Bergweg im Schneesturm, Berghütte, Morgen danach) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Korbinian (KO, Mitte 30, Wanderer; Stimme marc): standing/blazer-4 als Anorak (Jacke Rot #F07A6A, Oberteil Gelb #F9D56E,
  schwarze Hose der Pose), Kopf hat-beanie (Wollmütze), Haut #F0C8A8, keine Brille, kein Bart.
Frau Moser (MO, um 55, Eigentümerin der Hütte, bewirtschaftet sie im Sommer; Stimme laura_ruhig): standing/crossed_arms-2
  (verschränkte Arme, schwarzes Oberteil der Pose, Hose Grün #8FD694), Kopf Gray Bun, Haut #E9BC98, kein Bart.
Posen der letzten drei Folgen (186: easing-2, doctor-nurse-01, resting-1, blazer-3; 187: easing-1, pointing_finger-1;
188: pointing_finger-2, crossed_arms-1) nicht verwendet; Farben Rot/Gelb/Grün statt Orange/Türkis/Anthrazit (186),
Orange-Jacke (187), Rosa (188). Keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine
Karikatur. Präfixe KO_/MO_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Driven, Eyes Closed
bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten KO_redet, KO_redet2, MO_redet,
MO_redet2 (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_189")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KO": ("standing/blazer-4", "hat-beanie", None, None, {"Skin": "#F0C8A8", "Jacket": "#F07A6A", "Top": "#F9D56E"}),
    "MO": ("standing/crossed_arms-2", "Gray Bun", None, None, {"Skin": "#E9BC98", "Pants": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KO_ruhig", "KO", "Calm", 0), ("KO_ernst", "KO", "Serious", 0), ("KO_sorge", "KO", "Concerned|Serious", 0),
    ("KO_angst", "KO", "Fear", 0), ("KO_muede", "KO", "Tired", 0), ("KO_fest", "KO", "Driven", 0),
    ("KO_froh", "KO", "Smile", 0), ("KO_schlaf", "KO", "Eyes Closed", 0), ("KO_skeptisch", "KO", "Suspicious", 0),
    ("KO_redet", "KO", "Concerned|Serious", 1), ("KO_redet2", "KO", "Smile", 1),
    ("MO_ruhig", "MO", "Calm", 0), ("MO_ernst", "MO", "Serious", 0), ("MO_skeptisch", "MO", "Suspicious", 0),
    ("MO_sorge", "MO", "Concerned|Serious", 0), ("MO_froh", "MO", "Smile", 0), ("MO_aerger", "MO", "Very Angry", 0),
    ("MO_redet", "MO", "Serious", 1), ("MO_redet2", "MO", "Smile", 1),
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
