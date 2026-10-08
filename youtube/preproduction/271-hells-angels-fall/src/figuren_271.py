"""Figuren für Folge 271 (Hells-Angels-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Elmar (EL, Ende 30, führendes Mitglied eines Rockerclubs, frühmorgens zu Hause; Stimme niklas): standing/resting-1
  (schlichter Pullover Graublau #7A8CA8, schwarze Hose der Pose), Kopf Short 1, Haut #E3B08C, kein Bart, keine Brille –
  keine Kutte, keine Abzeichen, kein Klischee; die Pose hält nichts in den Händen (keine Waffe im Bild).
Gabi (GA, Mitte 30, seine Verlobte; Stimme julia): standing/easing-1 (offenes Hemd Altrosa #E7A0B4, Oberteil Weiß,
  schwarze Hose der Pose), Kopf Medium Straight, Haut #F0C8A8.
Posen nicht aus 267/269 (robot_dance-3, walking-3, polka_dots, easing-2, blazer-1, pointing_finger-1, resting-2) und
nicht aus 266 (crossed_arms-1, blazer-2, shirt-3); keine Prothesen-Posen (shirt-1, shirt-2, blazer-1, blazer-2),
keine Polka Dots, keine Bärte.
Präfix EL_/GA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (EL_ruft, EL_klagt, GA_ruft, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_271")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "EL": ("standing/resting-1", "Short 1", None, None, {"Skin": "#E3B08C", "Top": "#7A8CA8"}),
    "GA": ("standing/easing-1", "Medium Straight", None, None, {"Skin": "#F0C8A8", "Jacket": "#E7A0B4", "Top": "#FFFFFF"}),
}

LISTE = [
    ("EL_ruhig", "EL", "Calm", 0), ("EL_muede", "EL", "Tired", 0), ("EL_ernst", "EL", "Serious", 0),
    ("EL_sorge", "EL", "Concerned|Serious", 0), ("EL_angst", "EL", "Fear", 0), ("EL_schreck", "EL", "Awe", 0),
    ("EL_denkt", "EL", "Suspicious", 0), ("EL_still", "EL", "Solemn", 0), ("EL_augen", "EL", "Eyes Closed", 0),
    ("EL_ruft", "EL", "Fear", 1), ("EL_klagt", "EL", "Concerned|Serious", 1),
    ("GA_ruhig", "GA", "Calm", 0), ("GA_angst", "GA", "Fear", 0), ("GA_schreck", "GA", "Awe", 0),
    ("GA_sorge", "GA", "Concerned|Serious", 0), ("GA_ernst", "GA", "Serious", 0), ("GA_still", "GA", "Solemn", 0),
    ("GA_ruft", "GA", "Fear", 1),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
