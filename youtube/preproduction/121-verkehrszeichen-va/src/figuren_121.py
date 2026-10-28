"""Figuren für Folge 121 (Verkehrszeichen als Verwaltungsakt) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Wittmann (um 65, Anwohnerin, Klägerin): standing/polka_dots (Pullover mit Polka Dots, blaue Hose), Kopf Gray Bun.
Herr Buchholz (um 45, Straßenverkehrsbehörde der Stadt): standing/shirt-3 (türkisfarbenes Hemd, schwarze Hose), Kopf Short 5.
Frau Wolter (um 30, Nachbarin): standing/walking-3 (schwarzes Shirt, schwarze Hose), Kopf Medium Bangs.
Posen in 118–120 nicht verwendet (dort robot_dance-3, resting-1, crossed_arms-2, easing-2, blazer-3, pointing_finger-1,
crossed_arms-1, walking-2, blazer-4); Polka Dots in den letzten drei Folgen nicht verwendet. Keine Bärte, keine Prothesen-Posen.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Driven, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_121")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WI": ("standing/polka_dots", "Gray Bun", None, None, {"Skin": "#EFC9A8", "Pants": "#8DB3F2"}),
    "BU": ("standing/shirt-3", "Short 5", None, None, {"Skin": "#C98F6B"}),
    "WO": ("standing/walking-3", "Medium Bangs", None, None, {"Skin": "#F2D3B8", "Hair": "#7A4B32"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WI_ruhig", "WI", "Calm", 0), ("WI_denkt", "WI", "Suspicious", 0), ("WI_sorge", "WI", "Concerned|Serious", 0),
    ("WI_redet", "WI", "Concerned|Serious", 1), ("WI_aerger", "WI", "Rage|Serious", 0),
    ("WI_aerger_redet", "WI", "Rage|Serious", 1), ("WI_entschl", "WI", "Driven", 0), ("WI_froh", "WI", "Smile", 0),
    ("BU_ruhig", "BU", "Calm", 0), ("BU_ernst", "BU", "Serious", 0), ("BU_redet", "BU", "Serious", 1),
    ("BU_denkt", "BU", "Suspicious", 0),
    ("WO_ruhig", "WO", "Calm", 0), ("WO_redet", "WO", "Calm", 1),
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
