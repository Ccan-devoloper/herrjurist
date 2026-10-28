"""Figuren für Folge 195 (Kostenentscheidung ZPO: Werklohnklage Malermeister gegen Hauseigentümerin) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Dressler (DR, um 50, Malermeister, Kläger; Stimme marc): standing/pointing_finger-2 (schwarzes Oberteil, helle Malerhose
  #F2EFE8; pointing_finger-1 verworfen: dort ist die ganze Kleidung schwarz und nicht einfärbbar), Kopf Short 3 (Haar #6B4A2E), Haut #EBBE9B, keine Brille, kein Bart.
Frau Lindau (LI, um 45, Hauseigentümerin, Beklagte; Stimme sabrina): standing/crossed_arms-1 (Oberteil Koralle #F07A6A, schwarze
  Hose), Kopf Medium Straight (Haar #3B2A20), Haut #D9A07A.
Richterin am Amtsgericht (RI, um 55, ohne Namen; Stimme laura_ruhig): standing/blazer-3 (dunkler Blazer #3A3A48 wie eine Robe,
  dunkle Hose), Kopf Medium 2 (Haar Grau #A9A9A9), Brille Glasses 2, Haut #F0C8A8.
Posen der letzten Folgen (191: easing-2, walking-1; 192: shirt-3, blazer-2; 193: shirt-3, shirt-4) nicht verwendet; keine
Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur. Präfixe DR_/LI_/RI_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Suspicious, Very Angry bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten DR_redet, DR_fragt, LI_redet, RI_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_195")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "DR": ("standing/pointing_finger-2", "Short 3", None, None, {"Skin": "#EBBE9B", "Pants": "#F2EFE8", "Hair": "#6B4A2E"}),
    "LI": ("standing/crossed_arms-1", "Medium Straight", None, None, {"Skin": "#D9A07A", "Top": "#F07A6A", "Hair": "#3B2A20"}),
    "RI": ("standing/blazer-3", "Medium 2", None, "Glasses 2", {"Skin": "#F0C8A8", "Jacket": "#3A3A48", "Pants": "#3A3A48",
                                                            "Hair": "#A9A9A9"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("DR_ruhig", "DR", "Calm", 0), ("DR_froh", "DR", "Smile", 0), ("DR_denkt", "DR", "Serious", 0),
    ("DR_sorge", "DR", "Concerned|Serious", 0), ("DR_skeptisch", "DR", "Suspicious", 0),
    ("DR_redet", "DR", "Driven", 1), ("DR_fragt", "DR", "Concerned|Serious", 1),
    ("LI_ruhig", "LI", "Calm", 0), ("LI_froh", "LI", "Smile", 0), ("LI_denkt", "LI", "Serious", 0),
    ("LI_sorge", "LI", "Concerned|Serious", 0), ("LI_aerger", "LI", "Very Angry", 0),
    ("LI_redet", "LI", "Suspicious", 1),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_denkt", "RI", "Suspicious", 0), ("RI_redet", "RI", "Serious", 1),
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
