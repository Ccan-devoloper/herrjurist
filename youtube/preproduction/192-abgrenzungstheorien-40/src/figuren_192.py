"""Figuren für Folge 192 (Abgrenzungstheorien: Kleingartenanlage, Tafeln) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Frau Kirschner (KI, um 70, Kleingärtnerin, Pächterin der Stadt; Stimme hilde): standing/shirt-3 (Hemd Orange #F9A66C, schwarze
  Hose), Kopf Gray Medium (Haar Hellgrau #D2D2D2), Haut #F2CDB2, keine Brille, kein Bart.
Elsa (EL, Anfang 20, Nachbarin aus der Parzelle nebenan, Jurastudentin; Stimme lucy): standing/blazer-2 (Blazer Blau #8DB3F2,
  Shirt Türkis, schwarze Hose, Beinprothese der Originalpose), Kopf Medium Bangs 3, Haut #E7B48F.
Posen der letzten Folgen (186: easing-2, doctor-nurse-01, resting-1, blazer-3; 187: easing-1, pointing_finger-1; 188:
pointing_finger-2, crossed_arms-1; 189: blazer-4, crossed_arms-2; 190: resting-1, resting-2, walking-2) nicht verwendet; keine
Polka Dots, keine Bärte, keine Karikatur. Präfixe KI_/EL_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Calm, Driven, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten KI_redet, KI_fragt, EL_redet, EL_erklaert (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_192")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KI": ("standing/shirt-3", "Gray Medium", None, None, {"Skin": "#F2CDB2", "Top": "#F9A66C", "Hair": "#D2D2D2"}),
    "EL": ("standing/blazer-2", "Medium Bangs 3", None, None, {"Skin": "#E7B48F", "Jacket": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KI_ruhig", "KI", "Smile", 0), ("KI_liest", "KI", "Serious", 0), ("KI_sorge", "KI", "Concerned|Serious", 0),
    ("KI_entschlossen", "KI", "Driven", 0), ("KI_denkt", "KI", "Suspicious", 0), ("KI_ernst", "KI", "Solemn", 0),
    ("KI_redet", "KI", "Driven", 1), ("KI_fragt", "KI", "Concerned|Serious", 1),
    ("EL_ruhig", "EL", "Calm", 0), ("EL_froh", "EL", "Smile", 0), ("EL_denkt", "EL", "Suspicious", 0),
    ("EL_ernst", "EL", "Serious", 0),
    ("EL_redet", "EL", "Serious", 1), ("EL_erklaert", "EL", "Smile", 1),
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
