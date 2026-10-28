"""Figuren für Folge 065 (Betrug § 263, Online-Kleinanzeige) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Detlef (um 45, Verkäufer): standing/shirt-4 (dunkles Hemd der Pose, Hose Blau #8DB3F2), Kopf Short 4, ohne Bart, Haut #E8B48C;
gewöhnlicher Privatverkäufer, keine Karikatur, keine Herkunfts- oder Hautfarbenzuschreibung, keine "fiese" Mimik.
Waltraud (um 65, Käuferin): standing/polka_dots (gepunktete Bluse, Hose Grün #8FD694), Kopf Gray Bun, Brille Glasses 2,
Haut #F0C8A8.
Keine Prothesen-Posen, keine Bärte (Mund bleibt frei). Beide Posen blicken im Original nach rechts: Grundansicht gespiegelt
(blickt nach links, zur Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md):
Calm, Smile, Serious, Suspicious, Fear, Driven bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_065")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "DE": ("standing/shirt-4", "Short 4", None, None, {"Skin": "#E8B48C", "Pants": "#8DB3F2"}),
    "WA": ("standing/polka_dots", "Gray Bun", None, "Glasses 2", {"Skin": "#F0C8A8", "Pants": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("DE_ruhig", "DE", "Calm", 0), ("DE_redet", "DE", "Smile", 1), ("DE_froh", "DE", "Smile", 0),
    ("DE_denkt", "DE", "Suspicious", 0), ("DE_ernst", "DE", "Serious", 0), ("DE_sorge", "DE", "Concerned|Serious", 0),
    ("DE_eifrig", "DE", "Driven", 0),
    ("WA_ruhig", "WA", "Calm", 0), ("WA_redet", "WA", "Calm", 1), ("WA_froh", "WA", "Smile", 0),
    ("WA_denkt", "WA", "Suspicious", 0), ("WA_ernst", "WA", "Serious", 0), ("WA_sorge", "WA", "Concerned|Serious", 0),
    ("WA_schreck", "WA", "Fear", 0), ("WA_entsetzt", "WA", "Concerned|Serious", 1),
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
