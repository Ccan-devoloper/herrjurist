"""Figuren für Folge 132 (Widerspruchslösung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Herr Mangold (Mitte 20, Beschuldigter/Angeklagter; Stimme niklas): standing/robot_dance-3 (Pullover Grün #5FA866 – „der Mann im
grünen Pullover“, Hose Grau #4A4A55), Kopf Short 5, ohne Bart, ohne Prothese, kein Herkunfts- oder Hautfarben-Klischee.
Polizeikommissarin Kirchhoff (um 35; Stimme julia): standing/easing-2 (Jacke Dunkelblau #33507A wie eine Uniformjacke, Hose
#2B2B2B), Kopf Bun.
Rechtsanwalt Hufnagel (um 60, Verteidiger; Stimme helmut): standing/walking-3 (schwarze Kleidung wie eine Robe), Kopf Gray Short,
Brille Glasses.
Anwohnerin (um 30, Funktionsrolle; Stimme ela_froh, kurze aufgeregte Zeile): standing/shirt-2 (schwarzes Hemd, Shorts Hellblau
#8DB3F2; die Pose zeigt eine Unterschenkelprothese – bei einer Zeugin, nicht bei einer Täterrolle), Kopf Long Bangs.
Strafrichterin (um 55, Funktionsrolle, spricht nicht): standing/shirt-1 (Hemd #2B2B2B wie eine Robe; hinter dem Richtertisch,
Beine verdeckt), Kopf Gray Bun, Brille Glasses 3.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Solemn, Smile, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe). Figurenpräfix nie ER_."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_132")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MG": ("standing/robot_dance-3", "Short 5", None, None, {"Skin": "#F0CDB4", "Top": "#5FA866", "Pants": "#4A4A55"}),
    "KH": ("standing/easing-2", "Bun", None, None, {"Skin": "#E8B894", "Jacket": "#33507A", "Pants": "#2B2B2B"}),
    "HN": ("standing/walking-3", "Gray Short", None, "Glasses", {"Skin": "#EFC9A8"}),
    "AW": ("standing/shirt-2", "Long Bangs", None, None, {"Skin": "#D9A47E", "Shorts": "#8DB3F2"}),
    "RI": ("standing/shirt-1", "Gray Bun", None, "Glasses 3", {"Skin": "#F2D3B8", "Top": "#2B2B2B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MG_ruhig", "MG", "Calm", 0), ("MG_redet", "MG", "Concerned|Serious", 1), ("MG_sorge", "MG", "Concerned|Serious", 0),
    ("MG_denkt", "MG", "Suspicious", 0), ("MG_muede", "MG", "Tired", 0), ("MG_froh", "MG", "Smile", 0),
    ("KH_ruhig", "KH", "Calm", 0), ("KH_redet", "KH", "Serious", 1), ("KH_denkt", "KH", "Suspicious", 0),
    ("KH_ernst", "KH", "Solemn", 0),
    ("HN_ruhig", "HN", "Calm", 0), ("HN_redet", "HN", "Serious", 1), ("HN_denkt", "HN", "Suspicious", 0),
    ("HN_froh", "HN", "Smile", 0), ("HN_ernst", "HN", "Solemn", 0),
    ("AW_ruhig", "AW", "Calm", 0), ("AW_redet", "AW", "Concerned|Serious", 1),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_denkt", "RI", "Suspicious", 0), ("RI_ernst", "RI", "Serious", 0),
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
