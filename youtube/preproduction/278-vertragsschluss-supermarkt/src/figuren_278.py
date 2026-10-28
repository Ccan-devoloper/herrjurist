"""Figuren für Folge 278 (Vertragsschluss Supermarkt: Wann kaufst du die Milch?) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Erhard (EH, um 40, Kunde; Stimme stephan): standing/walking-1 (T-Shirt Grün #8FD694, Hose schwarz der Pose), Kopf Short 5,
Haut #E3B08C, keine Brille, kein Bart – geht durch den Gang.
Frau Kesting (KE, um 30, Filialleiterin; Stimme lucy): standing/blazer-3 (Blazer Lila #B8A9F5, Oberteil schwarz der Pose,
Hose Grau #5A5F6E), Kopf Medium Bangs, Haut #C99470, keine Brille – sachlich, keine Karikatur.
Posen nicht aus den letzten drei Folgen 274–276 (easing-2, resting-2, shirt-3, robot_dance-2, pointing_finger-2); keine
Polka Dots, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2), keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix EH_/KE_ (nie ER_). Beide Posen blicken im Original nach rechts (Gesicht); die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (EH_redet, KE_redet, Lexi) zusätzlich
mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_278")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "EH": ("standing/walking-1", "Short 5", None, None, {"Skin": "#E3B08C", "Top": "#8FD694"}),
    "KE": ("standing/blazer-3", "Medium Bangs", None, None, {"Skin": "#C99470", "Jacket": "#B8A9F5", "Pants": "#5A5F6E"}),
}

LISTE = [
    ("EH_ruhig", "EH", "Calm", 0), ("EH_redet", "EH", "Concerned|Serious", 1), ("EH_froh", "EH", "Smile", 0),
    ("EH_schreck", "EH", "Fear", 0), ("EH_staunt", "EH", "Awe", 0), ("EH_denkt", "EH", "Suspicious", 0),
    ("EH_ernst", "EH", "Serious", 0), ("EH_sorge", "EH", "Concerned|Serious", 0), ("EH_still", "EH", "Solemn", 0),
    ("EH_erleichtert", "EH", "Smile Big|Smile", 0),
    ("KE_ruhig", "KE", "Calm", 0), ("KE_redet", "KE", "Serious", 1), ("KE_froh", "KE", "Smile", 0),
    ("KE_denkt", "KE", "Suspicious", 0), ("KE_ernst", "KE", "Serious", 0), ("KE_sorge", "KE", "Concerned|Serious", 0),
    ("KE_staunt", "KE", "Awe", 0),
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
