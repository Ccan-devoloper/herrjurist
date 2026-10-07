"""Figuren für Folge 238 (Soldaten sind Mörder und ACAB; Fußballstadion) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv; Fans und Polizisten ohne Klischees, keine Vereinsfarben, keine Waffen, keine Helme.
Hannes (HA, um 30, Fan; Stimme marc): standing/walking-1 (T-Shirt Orange #F2A65A, schwarze Hose der Pose), Kopf Short 2,
  Haut #E9BC98, kein Bart.
Polizistin Roth (RO, um 40; Stimme laura_ruhig): standing/robot_dance-3 (Uniformhemd Blau #4A6FA5, Hose Dunkelblau #2B3550),
  Kopf Bun, Haut #E8B896.
Polizeikollege (KO, spricht nicht): standing/resting-1 (Hemd Blau #4A6FA5, schwarze Hose der Pose), Kopf Short 1, Haut #D9A47E.
Zwei Freunde von Hannes (F1, F2, sprechen nicht): standing/robot_dance-2 (schwarzes Oberteil der Pose, Hose Hellblau #8DB3F2),
  Kopf Bangs 2, Haut #C68E6A; standing/crossed_arms-1 (Oberteil Grün #8FD694), Kopf Short 4, Haut #F0C8A8.
Posen der letzten drei Folgen (235: walking-3, blazer-4; 236: crossed_arms-2, blazer-3; 237: easing-2, blazer-3; parallel 234:
crossed_arms-2, shirt-3, blazer-3, easing-2, resting-1) für die sprechenden Hauptfiguren nicht verwendet (resting-1 nur für den
stummen Kollegen); keine Polka Dots, keine Prothesen-Posen, keine Bärte. Präfixe HA_/RO_/KO_/F1_/F2_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Solemn, Suspicious, Awe, Driven bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten HA_redet, RO_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_238")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HA": ("standing/walking-1", "Short 2", None, None, {"Skin": "#E9BC98", "Top": "#F2A65A"}),
    "RO": ("standing/robot_dance-3", "Bun", None, None, {"Skin": "#E8B896", "Top": "#4A6FA5", "Pants": "#2B3550"}),
    "KO": ("standing/resting-1", "Short 1", None, None, {"Skin": "#D9A47E", "Top": "#4A6FA5"}),
    "F1": ("standing/robot_dance-2", "Bangs 2", None, None, {"Skin": "#C68E6A", "Pants": "#8DB3F2"}),
    "F2": ("standing/crossed_arms-1", "Short 4", None, None, {"Skin": "#F0C8A8", "Top": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HA_froh", "HA", "Smile", 0), ("HA_ruhig", "HA", "Calm", 0), ("HA_redet", "HA", "Calm", 1),
    ("HA_ernst", "HA", "Serious", 0), ("HA_staunt", "HA", "Awe", 0), ("HA_still", "HA", "Solemn", 0),
    ("HA_entschl", "HA", "Driven", 0), ("HA_sorge", "HA", "Concerned|Serious", 0),
    ("RO_ruhig", "RO", "Calm", 0), ("RO_redet", "RO", "Serious", 1), ("RO_ernst", "RO", "Serious", 0),
    ("RO_skeptisch", "RO", "Suspicious", 0), ("RO_still", "RO", "Solemn", 0), ("RO_froh", "RO", "Smile", 0),
    ("KO_ruhig", "KO", "Calm", 0), ("KO_ernst", "KO", "Serious", 0),
    ("F1_froh", "F1", "Smile", 0), ("F1_ruhig", "F1", "Calm", 0),
    ("F2_froh", "F2", "Smile", 0), ("F2_ruhig", "F2", "Calm", 0),
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
