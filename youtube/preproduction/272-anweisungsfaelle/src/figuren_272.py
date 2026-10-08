"""Figuren für Folge 272 (Anweisungsfälle, Anzahlung per Überweisung an den Fliesenleger) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Tomke (TO, um 30; Stimme lucy): standing/robot_dance-3 (offene Hand: bittet, fragt), Oberteil Lila #B8A9F5, Hose
Dunkelblau #3A4A6B, Kopf Long, Haut #F0C8A8, keine Brille.
Herr Stemmler (ST, um 45; Stimme stephan): standing/crossed_arms-1 (verschränkte Arme, selbstsicher), Arbeitshemd Blau
#8DB3F2, Hose Dunkelgrau #4A4A55, Kopf Short 3, Haut #D9A47E, kein Bart – Fliesenleger, keine Karikatur.
Herr Feldhaus (FE, um 50; Stimme christian): standing/blazer-3 (Sakko Dunkelblau #3A4A6B, schwarzes Shirt der Pose, Hose
Grau #5A5A66), Kopf Gray Short, Brille Glasses 2, Haut #E8B894 – Bankberater einer namenlosen Bank.
Posen nicht aus den letzten drei Folgen 269–271 (blazer-1, pointing_finger-1, resting-1/2, blazer-4, robot_dance-2,
easing-1); keine Polka Dots, keine Prothesen-Posen (shirt-1, shirt-2, blazer-1, blazer-2), keine Bärte. Lexi nach lexi.py.
Präfix TO_/ST_/FE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (TO_redet, ST_redet, FE_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_272")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "TO": ("standing/robot_dance-3", "Long", None, None, {"Skin": "#F0C8A8", "Top": "#B8A9F5", "Pants": "#3A4A6B"}),
    "ST": ("standing/crossed_arms-1", "Short 3", None, None, {"Skin": "#D9A47E", "Top": "#8DB3F2", "Pants": "#4A4A55"}),
    "FE": ("standing/blazer-3", "Gray Short", None, "Glasses 2", {"Skin": "#E8B894", "Jacket": "#3A4A6B", "Pants": "#5A5A66"}),
}

LISTE = [
    ("TO_ruhig", "TO", "Calm", 0), ("TO_redet", "TO", "Concerned|Serious", 1), ("TO_froh", "TO", "Smile", 0),
    ("TO_sorge", "TO", "Concerned|Serious", 0), ("TO_denkt", "TO", "Suspicious", 0), ("TO_ernst", "TO", "Serious", 0),
    ("TO_staunt", "TO", "Awe", 0), ("TO_strahlt", "TO", "Smile Big|Smile", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_redet", "ST", "Smile", 1), ("ST_froh", "ST", "Smile", 0),
    ("ST_ernst", "ST", "Serious", 0), ("ST_denkt", "ST", "Suspicious", 0), ("ST_sorge", "ST", "Concerned|Serious", 0),
    ("FE_ruhig", "FE", "Calm", 0), ("FE_redet", "FE", "Serious", 1), ("FE_froh", "FE", "Smile", 0),
    ("FE_denkt", "FE", "Suspicious", 0), ("FE_ernst", "FE", "Serious", 0),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
