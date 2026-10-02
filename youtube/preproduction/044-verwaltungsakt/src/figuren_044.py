"""Figuren für Folge 044 (Verwaltungsakt § 35 VwVfG) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Frau Wiegand (um 62, betreibt einen Kaffeewagen auf dem Marktplatz): standing/polka_dots (gepunkteter Pullover), Kopf Gray Bun.
Herr Lorenz (um 48, Ordnungsamt, Beamter): standing/blazer-3 (blaues Jackett), Kopf Short 1, Brille Glasses.
Polizist Göbel (um 28): standing/walking-1 (dunkelblaues Shirt wie eine Uniform), Kopf Short 4.
Amtsleiterin Kessler (um 38, Ordnungsamt): standing/crossed_arms-2 (verschränkte Arme), Kopf Medium Bangs 3.
Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Smile, Serious, Suspicious, Solemn, Driven, Cute bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (…_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_044")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "WI": ("standing/polka_dots", "Gray Bun", None, None, {"Skin": "#F0C8A8"}),
    "LO": ("standing/blazer-3", "Short 1", None, "Glasses", {"Skin": "#E6B48F", "Jacket": "#8DB3F2"}),
    "GO": ("standing/walking-1", "Short 4", None, None, {"Skin": "#D9A07A", "Top": "#3D4A7A"}),
    "KE": ("standing/crossed_arms-2", "Medium Bangs 3", None, None, {"Skin": "#F1C6A5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WI_ruhig", "WI", "Smile", 0), ("WI_redet", "WI", "Concerned|Serious", 1), ("WI_sorge", "WI", "Concerned|Serious", 0),
    ("WI_denkt", "WI", "Suspicious", 0), ("WI_entschl", "WI", "Driven", 0), ("WI_froh", "WI", "Cute", 0),
    ("LO_ruhig", "LO", "Serious", 0), ("LO_redet", "LO", "Serious", 1), ("LO_denkt", "LO", "Solemn", 0),
    ("GO_ruhig", "GO", "Serious", 0), ("GO_redet", "GO", "Driven", 1), ("GO_denkt", "GO", "Suspicious", 0),
    ("KE_ruhig", "KE", "Smile", 0), ("KE_redet", "KE", "Serious", 1),
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
