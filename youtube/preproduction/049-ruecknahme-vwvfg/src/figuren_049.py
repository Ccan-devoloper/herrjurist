"""Figuren für Folge 049 (Rücknahme § 48 VwVfG) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Hofmann (um 32, betreibt ein kleines Café): standing/robot_dance-3 (rotes Oberteil, gelbe Hose), Kopf Long.
Herr Wagner (um 60, Sachbearbeiter der Förderstelle): standing/resting-1 (lila Pullover), Kopf Gray Short, Brille Glasses 2.
Frau Ebert (um 38, Prüferin der Förderstelle): standing/crossed_arms-1 (grünes Oberteil, verschränkte Arme), Kopf Medium Bangs 3.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Solemn, Driven, Cute bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (…_redet…, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_049")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HO": ("standing/robot_dance-3", "Long", None, None, {"Skin": "#F2C9A9", "Top": "#F07A6A"}),
    "WA": ("standing/resting-1", "Gray Short", None, "Glasses 2", {"Skin": "#E6B48F", "Top": "#B8A9F5"}),
    "EB": ("standing/crossed_arms-1", "Medium Bangs 3", None, None, {"Skin": "#C68C66", "Top": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HO_ruhig", "HO", "Smile", 0), ("HO_froh", "HO", "Smile Big|Smile", 0), ("HO_redfroh", "HO", "Smile Big|Smile", 1),
    ("HO_sorge", "HO", "Concerned|Serious", 0), ("HO_redet", "HO", "Concerned|Serious", 1), ("HO_denkt", "HO", "Suspicious", 0),
    ("HO_entschl", "HO", "Driven", 0), ("HO_cute", "HO", "Cute", 0),
    ("WA_ruhig", "WA", "Serious", 0), ("WA_redet", "WA", "Serious", 1), ("WA_denkt", "WA", "Solemn", 0),
    ("EB_ruhig", "EB", "Serious", 0), ("EB_redet", "EB", "Serious", 1), ("EB_denkt", "EB", "Suspicious", 0),
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
