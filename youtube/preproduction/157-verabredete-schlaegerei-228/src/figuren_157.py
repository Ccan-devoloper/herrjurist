"""Figuren für Folge 157 (Verabredete Schlägerei, § 228 StGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, ruhig stehende Erwachsene in Alltagskleidung; keine Vereinsfarben, Schals, Logos, keine
Hooligan-Klischees. Die realen Beteiligten der BGH-Fälle werden nicht dargestellt.
Sönke (um 35, verabredet für Gruppe A; Stimme stephan): standing/resting-2 (schwarzes Oberteil, Hose Blau #8DB3F2),
Kopf Short 4, Haut #E2B088, kein Bart, keine Brille.
Inken (um 30, antwortet für Gruppe B; Stimme lucy): standing/walking-1 (Oberteil Lila #B8A9F5, schwarze Hose),
Kopf Long Curly, Haut #F2CDB0, keine Brille.
Posen nicht aus 154–156 (crossed_arms-2, blazer-3, blazer-4, walking-3, easing-2, shirt-3, walking-2, robot_dance-2,
pointing_finger-2); keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Polka Dots, keine Bärte; robot_dance-1 bleibt Lexi.
Präfix SO_/IN_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (SO_redet, SO_protest, IN_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_157")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "SO": ("standing/resting-2", "Short 4", None, None, {"Skin": "#E2B088", "Pants": "#8DB3F2"}),
    "IN": ("standing/walking-1", "Long Curly", None, None, {"Skin": "#F2CDB0", "Top": "#B8A9F5"}),
}

LISTE = [
    ("SO_ruhig", "SO", "Calm", 0), ("SO_redet", "SO", "Serious", 1), ("SO_denkt", "SO", "Suspicious", 0),
    ("SO_sorge", "SO", "Concerned|Serious", 0), ("SO_protest", "SO", "Driven", 1), ("SO_ernst", "SO", "Solemn", 0),
    ("IN_ruhig", "IN", "Calm", 0), ("IN_redet", "IN", "Serious", 1), ("IN_denkt", "IN", "Suspicious", 0),
    ("IN_sorge", "IN", "Concerned|Serious", 0), ("IN_froh", "IN", "Smile", 0), ("IN_ernst", "IN", "Solemn", 0),
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
