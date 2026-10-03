"""Figuren für Folge 100 (Rücktritt vom Versuch, § 24 StGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Heiner (Mitte 40, Einbrecher, tritt zurück): standing/robot_dance-3 (salbeigrünes Oberteil, Hose Schiefergrau, weiße
    Turnschuhe), Kopf „Short 3“, Haut hell. Die ausgestreckte Hand hält den stilisierten Hebel am Fensterrahmen.
    Keine Karikatur, kein Bart, keine Prothese, kein schwarzes „Einbrecher-Outfit“.
Annegret (um 50, Wohnungsinhaberin): standing/crossed_arms-1 (Oberteil Koralle, schwarze Hose der Pose), Kopf
    „Medium Bangs“, Haut mittel. (Zuerst crossed_arms-2 mit schwarzem Oberteil und blauer Hose – zu nah an Jochen aus
    Folge 099, deshalb gewechselt; crossed_arms-1 zuletzt in 096, nicht in 097–099.)
Posen nicht aus den Folgen 097–099 (pointing_finger-2, walking-1, blazer-3, resting-2, shirt-4, blazer-1, walking-3);
keine Polka Dots. Präfix HN_/AN_ (nie ER_, weil bausteine.peep_voll ER_* nach op_we umleitet).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Driven, Solemn, Tired, Suspicious, Awe, Smile
bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (HN_redet, AN_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_100")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

HN_F = {"Skin": "#E8B892", "Top": "#A7C4A0", "Pants": "#5A6275", "Hair": "#6B4A2E"}
AN_F = {"Skin": "#B98260", "Top": "#F28C6B", "Hair": "#5A3A28"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HN": ("standing/robot_dance-3", "Short 3", None, None, HN_F),
    "AN": ("standing/crossed_arms-1", "Medium Bangs", None, None, AN_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HN_ruhig", "HN", "Calm", 0), ("HN_angespannt", "HN", "Driven", 0), ("HN_redet", "HN", "Concerned|Serious", 1),
    ("HN_reue", "HN", "Solemn", 0), ("HN_muede", "HN", "Tired", 0), ("HN_ernst", "HN", "Serious", 0),
    ("HN_denkt", "HN", "Suspicious", 0), ("HN_erleichtert", "HN", "Awe", 0), ("HN_froh", "HN", "Smile", 0),
    ("AN_ruhig", "AN", "Calm", 0), ("AN_redet", "AN", "Concerned|Serious", 1), ("AN_ernst", "AN", "Serious", 0),
    ("AN_genervt", "AN", "Suspicious", 0), ("AN_staunt", "AN", "Awe", 0), ("AN_froh", "AN", "Smile", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    nur = sys.argv[1:]
    n = 0
    for name, p, mimik, mund in LISTE:
        if nur and name not in nur:
            continue
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    if not nur:
        # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
        for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
            a = LX.AUSSEHEN
            for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
                figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
