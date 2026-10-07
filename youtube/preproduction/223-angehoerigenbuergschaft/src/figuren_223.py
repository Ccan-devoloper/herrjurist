"""Figuren für Folge 223 (Angehörigenbürgschaft, § 138 Abs. 1 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Anneke (um 32, Bürgin, Ehefrau von Gero, ohne eigenes Einkommen): standing/shirt-3 (türkisfarbene Bluse, schwarze Hose),
Kopf Medium Straight (dunkelbraun). Sachlich und selbstbestimmt, keine Karikatur.
Gero (um 35, Tischlermeister, Hauptschuldner): standing/shirt-4 (schwarzes Hemd, blaue Arbeitshose), Kopf Short 4.
Herr Wittkamp (um 60, Firmenkundenberater der Bank): standing/blazer-3 (schiefergrauer Blazer, weißes Shirt, dunkle Hose), Kopf No Hair 2,
Brille Glasses 3. Sachlich, keine „fiese“ Bankfigur, kein Logo.
Keine Bärte. Posen und Köpfe nicht aus den Folgen 220–222 (robot_dance-2, walking-3, blazer-4, resting-1, pointing_finger-1,
crossed_arms-2, sitting/mid-1, blazer-2, polka_dots, easing-1; Köpfe Short 1/2/3, Long, Long Curly, Gray Short, Gray Bun,
Bun 2, Bangs, Bangs 2, No Hair 1, Flat Top); keine Polka Dots. Präfix AN_/GE_/WI_ (nie ER_). Grundansicht gespiegelt
(blickt nach links), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md); sprechende Ansichten (…_redet) und Lexi zusätzlich mit a/o/e
(Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_223")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "AN": ("standing/shirt-3", "Medium Straight", None, None, {"Skin": "#F0C8A8", "Top": "#7FD6D0", "Hair": "#5A3A28"}),
    "GE": ("standing/shirt-4", "Short 4", None, None, {"Skin": "#E3B08C", "Pants": "#6F8FC9", "Hair": "#3A2A20"}),
    "WI": ("standing/blazer-3", "No Hair 2", None, "Glasses 3", {"Skin": "#EBC29E", "Jacket": "#6B7A8F", "Top": "#FFFFFF",
                                                                "Pants": "#3D3D58"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("AN_ruhig", "AN", "Calm", 0), ("AN_redet", "AN", "Serious", 1), ("AN_sorge", "AN", "Concerned|Serious", 0),
    ("AN_denkt", "AN", "Suspicious", 0), ("AN_froh", "AN", "Smile", 0), ("AN_muede", "AN", "Tired", 0),
    ("GE_ruhig", "GE", "Calm", 0), ("GE_redet", "GE", "Serious", 1), ("GE_froh", "GE", "Smile Big|Smile", 0),
    ("GE_sorge", "GE", "Concerned|Serious", 0), ("GE_muede", "GE", "Tired", 0),
    ("WI_ruhig", "WI", "Calm", 0), ("WI_redet", "WI", "Serious", 1), ("WI_froh", "WI", "Smile", 0),
    ("WI_ernst", "WI", "Solemn", 0),
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
