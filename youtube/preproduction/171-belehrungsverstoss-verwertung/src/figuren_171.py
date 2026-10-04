"""Figuren für Folge 171 (Belehrungsverstoß/Verwertung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Herr Pieper (Mitte 20, Beschuldigter; Stimme niklas): auf dem Rad sitting/bike, stehend standing/easing-1 – gleiche Kleidung
(Jacke Senf #E8A03A, weißes Oberteil, schwarze Hose der Posen), Kopf Short 4, ohne Bart, ohne Prothese; das blaue Damenrad
(Rahmen #8DB3F2) ist Teil der Rad-Pose. Kein Herkunfts- oder Hautfarben-Klischee, Alltagskleidung, keine Mütze.
Polizeihauptmeister Lohmeyer (um 55; Stimme helmut): standing/blazer-3 (Jacke Dunkelblau #33507A wie eine Uniformjacke, ohne
Wappen oder Abzeichen, Hose #2B2B35), Kopf No Hair 2, Brille Glasses.
Besitzerin des Rades (um 40, Funktionsrolle; Stimme ela_froh, eine kurze aufgeregte Zeile): standing/pointing_finger-2
(zeigt auf ihr Rad; schwarzes Oberteil, Hose Lila #B8A9F5), Kopf Medium Bangs 3.
Verteidigerin (um 45, Funktionsrolle, spricht nicht): standing/blazer-1 (Jacke Schwarz #2B2B2B wie eine Robe, Hose #3A3A44;
die Pose zeigt eine Unterschenkelprothese – bei der Verteidigerin, nicht bei der Täterrolle), Kopf Long Curly, Brille Glasses 2.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Solemn, Smile, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe). Figurenpräfix nie ER_."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_171")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

PI_F = {"Skin": "#EBC29E", "Top": "#FFFFFF", "Jacket": "#E8A03A", "Bicycle Frame": "#8DB3F2"}
# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "PIR": ("sitting/bike", "Short 4", None, None, PI_F),                  # Pieper auf dem Rad
    "PI": ("standing/easing-1", "Short 4", None, None, PI_F),              # Pieper stehend
    "LO": ("standing/blazer-3", "No Hair 2", None, "Glasses", {"Skin": "#E3B08C", "Jacket": "#33507A", "Pants": "#2B2B35"}),
    "BE": ("standing/pointing_finger-2", "Medium Bangs 3", None, None, {"Skin": "#C98E6A", "Pants": "#B8A9F5"}),
    "VE": ("standing/blazer-1", "Long Curly", None, "Glasses 2", {"Skin": "#F2D3B8", "Jacket": "#2B2B2B", "Pants": "#3A3A44"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("PIR_ruhig", "PIR", "Calm", 0), ("PIR_sorge", "PIR", "Concerned|Serious", 0), ("PIR_redet", "PIR", "Tired", 1),
    ("PI_ruhig", "PI", "Calm", 0), ("PI_redet", "PI", "Tired", 1), ("PI_sorge", "PI", "Concerned|Serious", 0),
    ("PI_denkt", "PI", "Suspicious", 0), ("PI_muede", "PI", "Tired", 0), ("PI_froh", "PI", "Smile", 0),
    ("LO_ruhig", "LO", "Calm", 0), ("LO_redet", "LO", "Serious", 1), ("LO_denkt", "LO", "Suspicious", 0),
    ("LO_ernst", "LO", "Solemn", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Concerned|Serious", 1), ("BE_ernst", "BE", "Serious", 0),
    ("VE_ruhig", "VE", "Calm", 0), ("VE_denkt", "VE", "Suspicious", 0), ("VE_froh", "VE", "Smile", 0),
    ("VE_ernst", "VE", "Serious", 0),
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
