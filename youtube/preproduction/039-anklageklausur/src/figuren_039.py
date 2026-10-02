"""Figuren für Folge 039 (Anklageklausur, Ladendiebstahl und Beleidigung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Herr Rösch (Beschuldigter, 24): standing/easing-1 (offenes blaues Hemd über weißem Shirt, schwarze Hose), Kopf Short 5, ohne Bart.
Herr Brehm (Ladendetektiv, um 50): standing/crossed_arms-2 (verschränkte Arme, schwarzer Pullover, graue Hose), Kopf No Hair 2,
Brille Glasses 3, ohne Bart (Mund bleibt frei).
Staatsanwältin (um 45, ohne Namen): standing/blazer-4 (lila Blazer, weißes Oberteil, schwarze Hose), Kopf Long, ohne Brille.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2 verworfen); kein Herkunfts- oder Hautfarben-Klischee bei der Täterrolle.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Fear, Contempt, Suspicious, Tired,
Very Angry bzw. „Augen|geschlossener Mund“ (Concerned|Serious, Cheeky|Smile). Sprechende Ansichten zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_039")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RO": ("standing/easing-1", "Short 5", None, None, {"Skin": "#F0C8A8", "Jacket": "#8DB3F2", "Top": "#FFFFFF"}),
    "BR": ("standing/crossed_arms-2", "No Hair 2", None, "Glasses 3", {"Skin": "#D9A47E", "Pants": "#5A5A6A"}),
    "SA": ("standing/blazer-4", "Long", None, None, {"Skin": "#C68E6A", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RO_ruhig", "RO", "Calm", 0), ("RO_cool", "RO", "Cheeky|Smile", 0), ("RO_redet", "RO", "Concerned|Serious", 1),
    ("RO_wut", "RO", "Very Angry", 1), ("RO_schreck", "RO", "Fear", 0), ("RO_denkt", "RO", "Suspicious", 0),
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Serious", 1), ("BR_aerger", "BR", "Contempt", 0),
    ("BR_denkt", "BR", "Suspicious", 0), ("BR_muede", "BR", "Tired", 0),
    ("SA_ruhig", "SA", "Calm", 0), ("SA_redet", "SA", "Driven", 1), ("SA_denkt", "SA", "Serious", 0),
    ("SA_froh", "SA", "Smile", 0), ("SA_skeptisch", "SA", "Suspicious", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
