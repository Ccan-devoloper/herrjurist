"""Figuren für Folge 145 (Hauskauf: Kaufvertrag, Auflassung, Grundbuch) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Ute (UT, um 40, Käuferin): standing/resting-1 (Pullover Blau #8DB3F2, schwarze Hose), Kopf Bangs (Haar Braun #6B4A2E),
  Haut #F1C9A8.
Joachim (JO, um 40, Käufer): standing/easing-1 (offene Jacke Rot #F07A6A, Shirt Weiß, Hose schwarz – Hosenfarbe der Pose nicht einfärbbar), Kopf Short 1,
  Haut #D9A07A, kein Bart.
Herr Ackermann (AK, um 65, Verkäufer): standing/crossed_arms-1 (Pullover Grün #8FD694, Hose schwarz – nicht einfärbbar), Kopf No Hair 3,
  Brille Glasses 2, Haut #EDC3A3, kein Bart.
Notarin (NO, um 50, ohne Namen): standing/blazer-3 (Blazer Lila #B8A9F5, Oberteil schwarz, Hose Dunkelgrau #3D3D48), Kopf
  Medium 3 (Haar Dunkelbraun #3B2A20), Brille Glasses 3, Haut #C99470.
Posen der letzten drei Folgen (142: easing-2, resting-2; 143: shirt-4, easing-2; 144: walking-2, shirt-3) und 139
(robot_dance-3, pointing_finger-2) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine
Bärte, keine Karikatur. Präfixe UT_/JO_/AK_/NO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Old bzw. „Augen|geschlossener
Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (UT_redet, JO_redet, AK_redet, AK_streng, NO_redet, NO_streng,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_145")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "UT": ("standing/resting-1", "Bangs", None, None, {"Skin": "#F1C9A8", "Top": "#8DB3F2", "Pants": "#151515", "Hair": "#6B4A2E"}),
    "JO": ("standing/easing-1", "Short 1", None, None, {"Skin": "#D9A07A", "Jacket": "#F07A6A", "Top": "#FFFFFF",
                                                        "Pants": "#4A5A85", "Hair": "#2B2118"}),
    "AK": ("standing/crossed_arms-1", "No Hair 3", None, "Glasses 2", {"Skin": "#EDC3A3", "Top": "#8FD694", "Pants": "#7A5B3C"}),
    "NO": ("standing/blazer-3", "Medium 3", None, "Glasses 3", {"Skin": "#C99470", "Jacket": "#B8A9F5", "Top": "#FFFFFF",
                                                              "Pants": "#3D3D48", "Hair": "#3B2A20"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("UT_ruhig", "UT", "Calm", 0), ("UT_redet", "UT", "Smile", 1), ("UT_froh", "UT", "Smile Big|Smile", 0),
    ("UT_denkt", "UT", "Suspicious", 0), ("UT_staunt", "UT", "Awe", 0), ("UT_laechelt", "UT", "Smile", 0),
    ("JO_ruhig", "JO", "Calm", 0), ("JO_redet", "JO", "Smile Big|Smile", 1), ("JO_froh", "JO", "Smile Big|Smile", 0),
    ("JO_denkt", "JO", "Suspicious", 0), ("JO_staunt", "JO", "Awe", 0), ("JO_laechelt", "JO", "Smile", 0),
    ("JO_sorge", "JO", "Concerned|Serious", 0),
    ("AK_ruhig", "AK", "Old", 0), ("AK_streng", "AK", "Serious", 1), ("AK_redet", "AK", "Smile", 1),
    ("AK_denkt", "AK", "Suspicious", 0), ("AK_ernst", "AK", "Serious", 0), ("AK_froh", "AK", "Smile", 0),
    ("NO_ruhig", "NO", "Calm", 0), ("NO_redet", "NO", "Smile", 1), ("NO_streng", "NO", "Serious", 1),
    ("NO_denkt", "NO", "Suspicious", 0), ("NO_laechelt", "NO", "Smile", 0), ("NO_ernst", "NO", "Serious", 0),
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
