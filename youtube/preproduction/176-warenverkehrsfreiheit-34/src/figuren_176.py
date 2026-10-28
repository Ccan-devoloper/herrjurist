"""Figuren für Folge 176 (Warenverkehrsfreiheit Art. 34 AEUV; Getränkegroßhändlerin und Lebensmittelkontrolleur) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, Erwachsene.
Frau Trautmann (TR, um 40, betreibt einen Getränkegroßhandel, Parallelimporteurin; Stimme laura_ruhig):
  standing/blazer-1 (Blazer Koralle #F07A6A, schwarzes Shirt aus der Pose, Hose Anthrazit #3A3A44, Beinprothese aus der
  Pose, weiße Schuhe), Kopf Medium 3 (dunkles halblanges Haar), Haut #F2C9A4, keine Brille. robot_dance-3 verworfen
  (Armhaltung wie Lexi).
Herr Kleinschmidt (KL, um 60, Lebensmittelüberwachung; Stimme william): standing/pointing_finger-2 (schwarzer Pullover aus der
  Pose, Hose Graublau #5E6E8C, schwarze Schuhe), Kopf Gray Short, Brille Glasses 2, Haut #E3B08C, kein Bart.
Posen der letzten drei Folgen (173: resting-1, easing-2, shirt-3, blazer-4; 174: crossed_arms-1, resting-2, shirt-4,
crossed_arms-2; 175: easing-1, pointing_finger-1) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots; Prothesen-Pose
nur für die Händlerin (keine Täterrolle), keine Bärte. Präfixe TR_/KL_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten TR_redet, KL_redet, KL_einsicht (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_176")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "TR": ("standing/blazer-1", "Medium 3", None, None, {"Skin": "#F2C9A4", "Jacket": "#F07A6A", "Pants": "#3A3A44"}),
    "KL": ("standing/pointing_finger-2", "Gray Short", None, "Glasses 2", {"Skin": "#E3B08C", "Pants": "#5E6E8C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TR_ruhig", "TR", "Calm", 0), ("TR_redet", "TR", "Serious", 1), ("TR_ernst", "TR", "Serious", 0),
    ("TR_froh", "TR", "Smile", 0), ("TR_denkt", "TR", "Suspicious", 0), ("TR_sorge", "TR", "Concerned|Serious", 0),
    ("TR_staunt", "TR", "Awe", 0), ("TR_entschlossen", "TR", "Driven", 0),
    ("KL_ruhig", "KL", "Calm", 0), ("KL_redet", "KL", "Serious", 1), ("KL_einsicht", "KL", "Calm", 1),
    ("KL_ernst", "KL", "Serious", 0), ("KL_froh", "KL", "Smile", 0), ("KL_denkt", "KL", "Suspicious", 0),
    ("KL_staunt", "KL", "Awe", 0), ("KL_still", "KL", "Solemn", 0),
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
