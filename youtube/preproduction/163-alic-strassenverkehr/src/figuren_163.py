"""Figuren für Folge 163 (a.l.i.c. im Straßenverkehr: Kneipenabend, Nachtfahrt, Polizeikontrolle) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv; im echten BGH-Fall treten keine Figuren auf.
Leopold (um 60, fährt nach dem Kneipenabend heim; Stimme william): standing/easing-2 (offenes Hemd Türkis #7FD6D0 über
schwarzem Shirt, Hose Grau #6B6B78), Kopf No Hair 3 (Glatze mit grauem Haarkranz #BDB6AE), Haut #EBC2A0, kein Bart, keine Brille.
Polizistin (um 40, Funktionsrolle ohne Namen; Stimme laura_ruhig): standing/easing-1 (Jacke Dunkelblau #2F3D63,
Oberteil Hellblau #8DB3F2 – uniformähnlich), Kopf Long Bangs (Haar dunkelbraun #3B2A20), Haut #D7A27C.
Freund und Freundin (Kneipe, sprechen nicht, nur in A1): standing/walking-3 (schwarz, Haut #E2B48E, Kopf Short 3) und standing/robot_dance-2 (Hose Lila #B8A9F5, Kopf Medium Bangs 2, Haar #A0522D, Haut #F2D0B5).
Sachlich, keine Karikatur, kein Trunkenheitsklischee (kein Schwanken, keine roten Nasen); keine Prothesen-Posen, keine
Bärte, keine Polka Dots. Posen nicht aus 159–161 (robot_dance-3, crossed_arms-1, crossed_arms-2, sitting/closed_legs-2,
resting-1, blazer-3) und nicht aus 158 (shirt-4, easing-1 nur bei der Polizistin mit Uniformfarben; anderer Kopf, andere
Farben als Burkhard in 158). Lexi bleibt robot_dance-1.
Präfix LE_/PO_/FR_/FN_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (LE_redet, LE_froh_redet, PO_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_163")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "LE": ("standing/easing-2", "No Hair 3", None, None, {"Skin": "#EBC2A0", "Jacket": "#7FD6D0", "Pants": "#6B6B78",
                                                         "Hair": "#BDB6AE"}),
    "PO": ("standing/easing-1", "Long Bangs", None, None, {"Skin": "#D7A27C", "Jacket": "#2F3D63", "Top": "#8DB3F2",
                                                          "Hair": "#3B2A20"}),
    "FR": ("standing/walking-3", "Short 3", None, None, {"Skin": "#E2B48E"}),
    "FN": ("standing/robot_dance-2", "Medium Bangs 2", None, None, {"Skin": "#F2D0B5", "Pants": "#B8A9F5", "Hair": "#A0522D"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("LE_froh", "LE", "Smile", 0), ("LE_froh_redet", "LE", "Smile", 1), ("LE_ruhig", "LE", "Calm", 0),
    ("LE_redet", "LE", "Serious", 1), ("LE_denkt", "LE", "Suspicious", 0), ("LE_sorge", "LE", "Concerned|Serious", 0),
    ("LE_still", "LE", "Solemn", 0), ("LE_muede", "LE", "Tired", 0),
    ("PO_ruhig", "PO", "Calm", 0), ("PO_redet", "PO", "Serious", 1), ("PO_ernst", "PO", "Serious", 0),
    ("FR_froh", "FR", "Smile", 0), ("FN_froh", "FN", "Smile", 0),
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
