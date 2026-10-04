"""Figuren für Folge 173 (GbR nach MoPeG; Band, Musikgeschäft) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Bente (BT, um 25, Gitarristin; Stimme lucy): standing/resting-1 (Pullover Lila #B8A9F5, schwarze Hose), Kopf Medium Straight,
  Haut #F2C9A4.
Gerrit (GE, um 28, Schlagzeuger; Stimme stephan): standing/easing-2 (offene Jacke Grün #8FD694 über schwarzem Shirt, Hose
  Dunkelblau #2E3550), Kopf Short 3, Haut #D9A07A, kein Bart.
Ingo (IN, um 35, Bassist mit festem Gehalt; Stimme christian): standing/shirt-3 (Hemd Blau #8DB3F2, schwarze Hose), Kopf
  Short 5, Brille Glasses, Haut #EDC3A3, kein Bart.
Frau Bornemann (BO, um 60, Inhaberin des Musikgeschäfts, Verkäuferin; Stimme hilde): standing/blazer-4 (Blazer Dunkelgrün
  #2E5E4E, Oberteil Weiß), Kopf Gray Bun, Brille Glasses 3, Haut #F0C8A8.
Posen der letzten drei Folgen (169: doctor-nurse-02, shirt-4; 170: robot_dance-3, blazer-2; 171: sitting/bike, easing-1,
blazer-3, pointing_finger-2, blazer-1) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2),
keine Bärte, keine Karikatur. Präfixe BT_/GE_/IN_/BO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht
ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Fear, Awe, Tired, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten BT_redet, GE_redet, IN_redet, BO_redet,
BO_streng (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_173")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "BT": ("standing/resting-1", "Medium Straight", None, None, {"Skin": "#F2C9A4", "Top": "#B8A9F5"}),
    "GE": ("standing/easing-2", "Short 3", None, None, {"Skin": "#D9A07A", "Jacket": "#8FD694", "Pants": "#2E3550"}),
    "IN": ("standing/shirt-3", "Short 5", None, "Glasses", {"Skin": "#EDC3A3", "Top": "#8DB3F2"}),
    "BO": ("standing/blazer-4", "Gray Bun", None, "Glasses 3", {"Skin": "#F0C8A8", "Jacket": "#2E5E4E", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BT_ruhig", "BT", "Calm", 0), ("BT_froh", "BT", "Smile Big|Smile", 0), ("BT_redet", "BT", "Smile", 1),
    ("BT_skeptisch", "BT", "Suspicious", 0), ("BT_ernst", "BT", "Serious", 0), ("BT_sorge", "BT", "Concerned|Serious", 0),
    ("GE_ruhig", "GE", "Calm", 0), ("GE_froh", "GE", "Smile Big|Smile", 0), ("GE_redet", "GE", "Smile", 1),
    ("GE_skeptisch", "GE", "Suspicious", 0), ("GE_ernst", "GE", "Serious", 0), ("GE_staunt", "GE", "Awe", 0),
    ("IN_ruhig", "IN", "Calm", 0), ("IN_froh", "IN", "Smile", 0), ("IN_redet", "IN", "Concerned|Serious", 1),
    ("IN_schreck", "IN", "Fear", 0), ("IN_skeptisch", "IN", "Suspicious", 0), ("IN_ernst", "IN", "Serious", 0),
    ("IN_muede", "IN", "Tired", 0), ("IN_sorge", "IN", "Concerned|Serious", 0),
    ("BO_ruhig", "BO", "Calm", 0), ("BO_froh", "BO", "Smile", 0), ("BO_redet", "BO", "Smile", 1),
    ("BO_streng", "BO", "Serious", 1), ("BO_skeptisch", "BO", "Suspicious", 0),
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
