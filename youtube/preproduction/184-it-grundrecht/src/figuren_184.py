"""Figuren für Folge 184 (Staatstrojaner und IT-Grundrecht) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren
fiktiv, Erwachsene. Keine realen Behörden, keine Uniform, kein Logo: die Polizei erscheint nur als Kommissar in Zivil.
Herr Weinhold (WH, um 35, Beschuldigter; Stimme niklas): sitting/mid-2 (grünes T-Shirt #8FD694, schwarze Hose aus der Pose,
  weiße Schuhe) – sitzt am Schreibtisch auf einem Hocker (Tabler-Icon im Folienskript), Kopf Pomp, Haut #E3B08C, keine
  Brille, kein Bart. Keine Prothesen-Pose für den Beschuldigten.
Kriminalhauptkommissar Hollstein (HS, um 55; Stimme helmut): standing/blazer-1 (Sakko Schiefergrau #6E7F99 über schwarzem
  Shirt, Hose Anthrazit #3A3A44, Beinprothese aus der Pose – bewusst beim Ermittler, nicht beim Beschuldigten), Kopf No Hair 2,
  Brille Glasses 2, Haut #F0C8A8, kein Bart.
Posen der letzten Folgen (181: easing-2, resting-2; 182: blazer-3, pointing_finger-2, resting-1; 183: shirt-3, robot_dance-3,
blazer-4; 180: easing-1, crossed_arms-1, resting-2, shirt-4) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots.
Präfixe WH_/HS_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links,
Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Driven, Solemn, Fear bzw.
„Augen|geschlossener Mund“ (Cheeky|Smile, Concerned|Serious). Sprechende Ansichten WH_redet, HS_redet, HS_beschluss (und
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_184")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "WH": ("sitting/mid-2", "Pomp", None, None, {"Skin": "#E3B08C", "Top": "#8FD694"}),
    "HS": ("standing/blazer-1", "No Hair 2", None, "Glasses 2", {"Skin": "#F0C8A8", "Jacket": "#6E7F99", "Pants": "#3A3A44"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WH_ruhig", "WH", "Calm", 0), ("WH_redet", "WH", "Cheeky|Smile", 1), ("WH_selbst", "WH", "Cheeky|Smile", 0),
    ("WH_denkt", "WH", "Suspicious", 0), ("WH_sorge", "WH", "Concerned|Serious", 0), ("WH_ernst", "WH", "Serious", 0),
    ("WH_schreck", "WH", "Fear", 0), ("WH_tippt", "WH", "Driven", 0),
    ("HS_ruhig", "HS", "Calm", 0), ("HS_redet", "HS", "Serious", 1), ("HS_ernst", "HS", "Serious", 0),
    ("HS_denkt", "HS", "Suspicious", 0), ("HS_entschlossen", "HS", "Driven", 0), ("HS_froh", "HS", "Smile", 0),
    ("HS_still", "HS", "Solemn", 0), ("HS_beschluss", "HS", "Calm", 1), ("HS_staunt", "HS", "Awe", 0),
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
