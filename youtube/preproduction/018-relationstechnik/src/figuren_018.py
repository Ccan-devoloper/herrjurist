"""Figuren für Folge 018 (Relationstechnik, Kühlschrank-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Referendarin (um 27, bearbeitet die Akte): standing/polka_dots (grünes Oberteil, dunkle Hose), Kopf Long.
Herr Brenner (Händler, Kläger, um 50): standing/easing-1 (blaue Jacke, gelbes Shirt), Kopf Short 5, Brille Glasses 4.
Frau Lehmann (Café-Inhaberin, Beklagte, um 45): standing/pointing_finger-2 (schwarzes Oberteil, rote Hose), Kopf Medium Bangs 2.
Fahrer (Zeuge, Brenners Mitarbeiter, um 60): standing/walking-3 (schwarz), Kopf Gray Short. Kein Bart (Mund bleibt frei).
Richterin (ohne Text, Beweisaufnahme): standing/blazer-4 (dunkles Kostüm), Kopf Gray Medium.
Keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links,
Suffix _r nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Driven, Fear,
Contempt, Suspicious bzw. „Augen|geschlossener Mund“ (Concerned|Serious).
Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 %)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_018")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "RF": ("standing/polka_dots", "Long", None, None, {"Skin": "#E8B98F", "Top": "#8FD694", "Pants": "#3A3A48"}),
    "BR": ("standing/easing-1", "Short 5", None, "Glasses 4", {"Skin": "#E0AC84", "Jacket": "#8DB3F2", "Top": "#F9D56E"}),
    "LE": ("standing/pointing_finger-2", "Medium Bangs 2", None, None, {"Skin": "#D9A07A", "Pants": "#F07A6A"}),
    "FA": ("standing/walking-3", "Gray Short", None, None, {"Skin": "#F0C8A8"}),
    "RI": ("standing/blazer-4", "Gray Medium", None, None, {"Skin": "#B07552", "Jacket": "#3A3A48", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RF_ruhig", "RF", "Calm", 0), ("RF_fragt", "RF", "Concerned|Serious", 1), ("RF_denkt", "RF", "Serious", 0),
    ("RF_froh", "RF", "Smile", 0), ("RF_redet", "RF", "Driven", 1),
    ("BR_ruhig", "BR", "Calm", 0), ("BR_redet", "BR", "Suspicious", 1), ("BR_aerger", "BR", "Contempt", 0),
    ("BR_froh", "BR", "Smile", 0), ("BR_denkt", "BR", "Serious", 0),
    ("LE_ruhig", "LE", "Calm", 0), ("LE_redet", "LE", "Driven", 1), ("LE_sorge", "LE", "Concerned|Serious", 0),
    ("LE_trotz", "LE", "Contempt", 0), ("LE_denkt", "LE", "Serious", 0), ("LE_schreck", "LE", "Fear", 0),
    ("FA_ruhig", "FA", "Calm", 0), ("FA_redet", "FA", "Serious", 1),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_denkt", "RI", "Serious", 0),
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
