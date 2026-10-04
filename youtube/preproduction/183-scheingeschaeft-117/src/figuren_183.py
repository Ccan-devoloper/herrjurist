"""Figuren für Folge 183 (Scheingeschäft § 117 BGB: Schwarzgeld beim Hauskauf) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Markus (MA, um 40, Käufer): standing/shirt-3 (Hemd Blau #8DB3F2, Hose schwarz – Hosenfarbe der Pose nicht einfärbbar),
  Kopf Short 2 (Haar Dunkelbraun #3B2A20), Haut #E8B896, kein Bart.
Frau Meinhardt (MH, um 65, Verkäuferin): standing/robot_dance-3 (Oberteil Rot #F07A6A, Hose Dunkelblau #4A5A85),
  Kopf Gray Bun, Brille Glasses 4, Haut #F1C9A8.
Notar (NT, um 55, ohne Namen und ohne Rede, neutral): standing/blazer-4 (Sakko Grau #9A9AA8, Hemd Weiß, Hose schwarz),
  Kopf No Hair 1, Brille Glasses 2, Haut #B5835F.
Posen der letzten drei Folgen (180: easing-1, crossed_arms-1, resting-2, shirt-4; 181: easing-2, resting-2; 182: blazer-3,
pointing_finger-2, resting-1) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine
Bärte, keine Karikatur, keine „fiese“ Verkäuferin. Präfixe MA_/MH_/NT_ (nie ER_). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Old bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (MA_redet, MA_ernst, MH_redet, MH_streng, Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_183")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "MA": ("standing/shirt-3", "Short 2", None, None, {"Skin": "#E8B896", "Top": "#8DB3F2", "Hair": "#3B2A20"}),
    "MH": ("standing/robot_dance-3", "Gray Bun", None, "Glasses 4", {"Skin": "#F1C9A8", "Top": "#F07A6A", "Pants": "#4A5A85"}),
    "NT": ("standing/blazer-4", "No Hair 1", None, "Glasses 2", {"Skin": "#B5835F", "Jacket": "#9A9AA8", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MA_ruhig", "MA", "Calm", 0), ("MA_redet", "MA", "Smile", 1), ("MA_ernst", "MA", "Serious", 1),
    ("MA_froh", "MA", "Smile Big|Smile", 0), ("MA_denkt", "MA", "Suspicious", 0), ("MA_staunt", "MA", "Awe", 0),
    ("MA_laechelt", "MA", "Smile", 0), ("MA_sorge", "MA", "Concerned|Serious", 0),
    ("MH_ruhig", "MH", "Old", 0), ("MH_redet", "MH", "Smile", 1), ("MH_streng", "MH", "Serious", 1),
    ("MH_froh", "MH", "Smile", 0), ("MH_denkt", "MH", "Suspicious", 0), ("MH_ernst", "MH", "Serious", 0),
    ("MH_sorge", "MH", "Concerned|Serious", 0), ("MH_staunt", "MH", "Awe", 0),
    ("NT_ruhig", "NT", "Calm", 0), ("NT_laechelt", "NT", "Smile", 0), ("NT_ernst", "NT", "Serious", 0),
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
