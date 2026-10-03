"""Figuren für Folge 090 (Drittanfechtung Baugenehmigung, Eilrechtsschutz §§ 80a, 80 V VwGO) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle fiktiv.
Frau Dorn (um 30, Nachbarin, Antragstellerin): standing/easing-1 (grüne offene Jacke, weißes Oberteil, schwarze Hose),
Kopf Long Bangs (dunkelbraun).
Herr Weber (um 60, Bauherr, Beigeladener): standing/crossed_arms-2 (schwarzer Pullover, braune Hose, verschränkte Arme),
Kopf No Hair 1, Brille Glasses 2.
Rechtsanwalt Falk (um 32): standing/blazer-4 (dunkelblaues Sakko, weißes Oberteil, schwarze Hose), Kopf Short 1.
Keine Bärte, keine Prothesen-Posen, kein Muster. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt
und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Rage|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_090")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "DO": ("standing/easing-1", "Long Bangs", None, None,
           {"Skin": "#F2C7A8", "Hair": "#5A3A26", "Jacket": "#8FD694", "Top": "#FFFFFF"}),
    "WE": ("standing/crossed_arms-2", "No Hair 1", None, "Glasses 2", {"Skin": "#EDB98A", "Pants": "#8A6A4A"}),
    "FA": ("standing/blazer-4", "Short 1", None, None,
           {"Skin": "#D9A07A", "Hair": "#2E2420", "Jacket": "#3D4E6E", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("DO_ruhig", "DO", "Calm", 0), ("DO_redet", "DO", "Concerned|Serious", 1), ("DO_sorge", "DO", "Concerned|Serious", 0),
    ("DO_denkt", "DO", "Suspicious", 0), ("DO_aerger", "DO", "Rage|Serious", 0), ("DO_froh", "DO", "Smile Big|Smile", 0),
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Serious", 1), ("WE_denkt", "WE", "Suspicious", 0),
    ("WE_muede", "WE", "Tired", 0),
    ("FA_ruhig", "FA", "Smile", 0), ("FA_redet", "FA", "Serious", 1), ("FA_denkt", "FA", "Solemn", 0),
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
