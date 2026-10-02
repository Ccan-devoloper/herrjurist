"""Figuren für Folge 032 (Verhältnismäßigkeit, Spraydosen-Verbot) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, keine realen Personen.
Herr Kühn (um 50, Inhaber eines Farbengeschäfts): standing/pointing_finger-2 (schwarzer Pullover, Zeigefinger), Kopf Short 3,
Brille Glasses 2. Frauke (um 28, Wandmalerin, Kundin): standing/easing-1 (offenes Hemd, Turnschuhe), Kopf Medium Bangs 2.
Frau Dörr (um 35, Ordnungsamt): standing/blazer-2 (Jackett), Kopf Medium Straight.
Keine Bärte. blazer-2 zeigt eine Beinprothese; sie gehört hier zur Behördenmitarbeiterin (keine Täterrolle).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Serious, Smile, Suspicious, Cute, Tired, Solemn bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). „Calm“ wird nicht verwendet, weil es bei diesen Köpfen die Augen schließt.
Sprechende Ansichten (KU_redet, FR_redet, DO_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_032")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "KU": ("standing/pointing_finger-2", "Short 3", None, "Glasses 2", {"Skin": "#E3B48C", "Pants": "#8DB3F2"}),
    "FR": ("standing/easing-1", "Medium Bangs 2", None, None,
           {"Skin": "#F1C6A5", "Jacket": "#8FD694", "Top": "#B8A9F5"}),
    "DO": ("standing/blazer-2", "Medium Straight", None, None, {"Skin": "#D9A07A", "Jacket": "#8DB3F2", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KU_ruhig", "KU", "Smile", 0), ("KU_redet", "KU", "Serious", 1), ("KU_sorge", "KU", "Concerned|Serious", 0),
    ("KU_denkt", "KU", "Suspicious", 0), ("KU_froh", "KU", "Cute", 0), ("KU_muede", "KU", "Tired", 0),
    ("FR_ruhig", "FR", "Smile", 0), ("FR_redet", "FR", "Serious", 1), ("FR_sorge", "FR", "Concerned|Serious", 0),
    ("FR_denkt", "FR", "Suspicious", 0), ("FR_froh", "FR", "Cute", 0),
    ("DO_ruhig", "DO", "Serious", 0), ("DO_redet", "DO", "Serious", 1), ("DO_denkt", "DO", "Solemn", 0),
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
