"""Figuren für Folge 181 (Cassis de Dijon und Reinheitsgebot; Getränkehändler und Lebensmittelkontrolleurin) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, Erwachsene. Reale Beteiligte (Rewe-Zentral) sind keine Figuren.
Herr Brodersen (BD, um 45, betreibt einen Getränkehandel; Stimme christian): standing/easing-2 (offenes Hemd Lila #B8A9F5,
  schwarzes Shirt aus der Pose, Hose Anthrazit #3A3A44, weiße Schuhe), Kopf Short 1, Haut #E8B98F, keine Brille, kein Bart.
Frau Timmermann (TM, um 30, Lebensmittelüberwachung; Stimme lucy): standing/resting-2 (schwarzer Pullover aus der Pose, Hose
  Blau #5E7FB8, schwarze Schuhe), Kopf Medium Straight, Brille Glasses, Haut #F2C9A4.
Posen der letzten Folgen (176: blazer-1, pointing_finger-2; 177: blazer-3, robot_dance-2; 178: resting-1, shirt-3; 179:
blazer-4, shirt-3, crossed_arms-2; parallel 180: easing-1, crossed_arms-1, robot_dance-3, shirt-4) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Bärte, keine
Prothesen-Posen. Präfixe BD_/TM_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten BD_redet, TM_redet, TM_einsicht (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_181")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "BD": ("standing/easing-2", "Short 1", None, None, {"Skin": "#E8B98F", "Jacket": "#B8A9F5", "Pants": "#3A3A44"}),
    "TM": ("standing/resting-2", "Medium Straight", None, "Glasses", {"Skin": "#F2C9A4", "Pants": "#5E7FB8"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BD_ruhig", "BD", "Calm", 0), ("BD_redet", "BD", "Serious", 1), ("BD_ernst", "BD", "Serious", 0),
    ("BD_froh", "BD", "Smile", 0), ("BD_denkt", "BD", "Suspicious", 0), ("BD_sorge", "BD", "Concerned|Serious", 0),
    ("BD_staunt", "BD", "Awe", 0), ("BD_entschlossen", "BD", "Driven", 0),
    ("TM_ruhig", "TM", "Calm", 0), ("TM_redet", "TM", "Serious", 1), ("TM_einsicht", "TM", "Smile", 1),
    ("TM_ernst", "TM", "Serious", 0), ("TM_froh", "TM", "Smile", 0), ("TM_denkt", "TM", "Suspicious", 0),
    ("TM_staunt", "TM", "Awe", 0), ("TM_still", "TM", "Solemn", 0),
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
