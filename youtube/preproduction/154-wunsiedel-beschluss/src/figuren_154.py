"""Figuren für Folge 154 (Wunsiedel-Beschluss) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv;
reale Beteiligte (Rudolf Heß, der Veranstalter, Behörden- und Gerichtspersonen) werden NICHT dargestellt, auch keine
Teilnehmer einer Versammlung.
Swantje (um 23, Jurastudentin; Stimme lucy): standing/crossed_arms-2 (schwarzes Oberteil, Hose Hellblau #8DB3F2),
Kopf Long Bangs, keine Brille (robot_dance-3 verworfen: zu ähnlich zu Lexis robot_dance-1).
Professor Ahlborn (um 55, leitet das Grundrechte-Seminar; Stimme christian): standing/blazer-3 (Jackett Grün #8FD694,
Hose Grau #6B6B78), Kopf No Hair 1, Brille Glasses, kein Bart.
Posen nicht aus 151–153 (easing-1, shirt-4, walking-1, resting-1, resting-2); keine Prothesen-Posen (blazer-1/-2,
shirt-1/-2), keine Polka Dots, keine Bärte.
Präfix SW_/AH_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (SW_redet, AH_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_154")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "SW": ("standing/crossed_arms-2", "Long Bangs", None, None, {"Skin": "#EBC3A0", "Pants": "#8DB3F2"}),
    "AH": ("standing/blazer-3", "No Hair 1", None, "Glasses", {"Skin": "#E2B48E", "Jacket": "#8FD694", "Pants": "#6B6B78"}),
}

LISTE = [
    ("SW_ruhig", "SW", "Smile", 0), ("SW_redet", "SW", "Serious", 1), ("SW_denkt", "SW", "Suspicious", 0),
    ("SW_froh", "SW", "Cute", 0), ("SW_sorge", "SW", "Concerned|Serious", 0),
    ("AH_ruhig", "AH", "Smile", 0), ("AH_redet", "AH", "Serious", 1), ("AH_denkt", "AH", "Suspicious", 0),
    ("AH_froh", "AH", "Cute", 0), ("AH_ernst", "AH", "Serious", 0),
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
