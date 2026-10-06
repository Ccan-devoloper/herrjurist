"""Figuren für Folge 204 (Sachrüge StPO; Kanzlei und Oldtimer-Verkauf im Rückblick) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Wichmann (WI, um 50, Angeklagter und Mandant; Stimme stephan): standing/shirt-3 (Hemd Graublau #A9C4D9, schwarze Hose,
  weiße Schuhe), Kopf Short 4, Haut #E5B48C, kein Bart, keine Brille.
Rechtsanwältin Hellmers (HE, um 35, Verteidigerin; Stimme lucy): standing/crossed_arms-2 (schwarzer Pullover, verschränkte Arme, Hose Lila #B8A9F5),
  Kopf Medium Bangs (dunkelbraunes Haar #4A3426), Haut #F2CDB0, keine Brille.
Frau Danner (DA, um 65, Käuferin des Oldtimers; Stimme hilde): standing/easing-2 (offene Jacke Grün #8FD694 über schwarzem
  Shirt, Hose Anthrazit #5A5A6A), Kopf Gray Bun, Brille Glasses 2, Haut #EFC9A9.
Posen der letzten drei Folgen (201: pointing_finger-2, blazer-4; 202: robot_dance-3, blazer-3, shirt-4; 203: crossed_arms-1,
pointing_finger-2) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine
Karikatur, keine Täter-Klischees (Angeklagter in Alltagskleidung, neutrale Mimik). Präfixe WI_/HE_/DA_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten WI_redet, WI_redet2, HE_redet, DA_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_204")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "WI": ("standing/shirt-3", "Short 4", None, None, {"Skin": "#E5B48C", "Top": "#A9C4D9"}),
    "HE": ("standing/crossed_arms-2", "Medium Bangs", None, None, {"Skin": "#F2CDB0", "Pants": "#B8A9F5", "Hair": "#4A3426"}),
    "DA": ("standing/easing-2", "Gray Bun", None, "Glasses 2", {"Skin": "#EFC9A9", "Jacket": "#8FD694", "Pants": "#5A5A6A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WI_ruhig", "WI", "Calm", 0), ("WI_ernst", "WI", "Serious", 0), ("WI_sorge", "WI", "Concerned|Serious", 0),
    ("WI_skeptisch", "WI", "Suspicious", 0), ("WI_froh", "WI", "Smile", 0),
    ("WI_redet", "WI", "Smile", 1), ("WI_redet2", "WI", "Concerned|Serious", 1),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_ernst", "HE", "Serious", 0), ("HE_froh", "HE", "Smile", 0),
    ("HE_skeptisch", "HE", "Suspicious", 0), ("HE_still", "HE", "Solemn", 0), ("HE_redet", "HE", "Serious", 1),
    ("DA_ruhig", "DA", "Calm", 0), ("DA_froh", "DA", "Smile", 0), ("DA_sorge", "DA", "Concerned|Serious", 0),
    ("DA_redet", "DA", "Smile", 1),
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
