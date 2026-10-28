"""Figuren für Folge 186 (Einstellung § 170 II StPO: Augenarztpraxis, Vernehmung, Staatsanwaltschaft, Briefkasten, Kanzlei) aus
der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Frau Rautenberg (RA, um 66, Patientin, Verletzte und Antragstellerin; Stimme hilde): standing/easing-2 (offene Jacke Orange
  #F9A66C, schwarzes Oberteil, Hose Anthrazit #3A3A44), Kopf Gray Medium mit grauem Haar #C9C9C9, Brille Glasses 4,
  Haut #F1C9A8, kein Bart.
Doktor Wallner (WA, um 50, Augenarzt, Beschuldigter; Stimme stephan, ein Satz): standing/doctor-nurse-01 (Arztkleidung der
  Pose mit Stethoskop, ohne Logo), Kopf Short 4, Haut #E3B08C, keine Brille, kein Bart; neutral, keine Karikatur.
Referendarin Hölscher (HO, um 28, Referendarin bei der Staatsanwaltschaft; Stimme lucy): standing/resting-1 (Oberteil Türkis
  #7FD6D0, schwarze Hose), Kopf Long Bangs, Haut #EDC3A0.
Rechtsanwältin (AN, um 45, Funktionsrolle ohne Namen, spricht nicht): standing/blazer-3 (Blazer Anthrazit #3A3A44, Hose
  Grau #9A9AA8), Kopf Bun, Haut #C68E62.
Posen der letzten drei Folgen (183: shirt-3, robot_dance-3, blazer-4; 184: sitting/mid-2, blazer-1; 185: resting-2,
sitting/closed_legs-2, walking-1, walking-2, crossed_arms-2, shirt-4) nicht verwendet; keine Polka Dots, keine Prothesen-Posen
(blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe RA_/WA_/HO_/AN_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn, Driven bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten RA_redet, RA_redet2, WA_redet, HO_redet,
HO_redet2 (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_186")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "RA": ("standing/easing-2", "Gray Medium", None, "Glasses 4",
           {"Skin": "#F1C9A8", "Jacket": "#F9A66C", "Pants": "#3A3A44", "Hair": "#C9C9C9"}),
    "WA": ("standing/doctor-nurse-01", "Short 4", None, None, {"Skin": "#E3B08C"}),
    "HO": ("standing/resting-1", "Long Bangs", None, None, {"Skin": "#EDC3A0", "Top": "#7FD6D0"}),
    "AN": ("standing/blazer-3", "Bun", None, None, {"Skin": "#C68E62", "Jacket": "#3A3A44", "Pants": "#9A9AA8"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RA_ruhig", "RA", "Calm", 0), ("RA_ernst", "RA", "Serious", 0), ("RA_sorge", "RA", "Concerned|Serious", 0),
    ("RA_muede", "RA", "Tired", 0), ("RA_fest", "RA", "Driven", 0), ("RA_froh", "RA", "Smile", 0),
    ("RA_skeptisch", "RA", "Suspicious", 0),
    ("RA_redet", "RA", "Concerned|Serious", 1), ("RA_redet2", "RA", "Driven", 1),
    ("WA_ruhig", "WA", "Calm", 0), ("WA_ernst", "WA", "Serious", 0), ("WA_sorge", "WA", "Concerned|Serious", 0),
    ("WA_froh", "WA", "Smile", 0),
    ("WA_redet", "WA", "Serious", 1),
    ("HO_froh", "HO", "Smile", 0), ("HO_eifrig", "HO", "Smile Big|Smile", 0), ("HO_ruhig", "HO", "Calm", 0),
    ("HO_skeptisch", "HO", "Suspicious", 0), ("HO_schreck", "HO", "Fear", 0), ("HO_ernst", "HO", "Serious", 0),
    ("HO_redet", "HO", "Smile Big|Smile", 1), ("HO_redet2", "HO", "Serious", 1),
    ("AN_ruhig", "AN", "Calm", 0), ("AN_ernst", "AN", "Serious", 0), ("AN_froh", "AN", "Smile", 0),
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
