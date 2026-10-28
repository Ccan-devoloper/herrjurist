"""Figuren für Folge 268 (Reparatur oder neues Gerät? Nacherfüllung § 439 BGB) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Undine (UN, um 35, Käuferin, Verbraucherin; Stimme sabrina): standing/crossed_arms-2 (schwarzes Oberteil der Pose, Hose
Blau #8DB3F2), Kopf Long, Haut #F2C9A0. Kein Dutt (Lexi), keine Brille.
Herr Stelzer (ST, um 45, Inhaber des Handyladens; Stimme marc): standing/blazer-3 (Blazer Lila #B8A9F5, schwarzes Shirt der
Pose, Hose dunkel #2E2E3A), Kopf Short 4, Brille Glasses 2, Haut #E3A47E, kein Bart.
Posen nicht aus den letzten drei Folgen 265–267 (resting-2, shirt-1, walking-2, blazer-2, crossed_arms-1, shirt-3,
easing-2, polka_dots, robot_dance-3, walking-3) und nicht aus den parallel laufenden 269–271 (blazer-1, pointing_finger-1,
resting-2, blazer-4, resting-1, robot_dance-2, easing-1); keine Polka Dots, keine Bärte.
Lexi nach lexi.py (robot_dance-1).
Präfix UN_/ST_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (UN_redet, UN_redet2, ST_redet, ST_redet2,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_268")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "UN": ("standing/crossed_arms-2", "Long", None, None, {"Skin": "#F2C9A0", "Pants": "#8DB3F2"}),
    "ST": ("standing/blazer-3", "Short 4", None, "Glasses 2", {"Skin": "#E3A47E", "Jacket": "#B8A9F5", "Pants": "#2E2E3A"}),
}

LISTE = [
    ("UN_ruhig", "UN", "Calm", 0), ("UN_froh", "UN", "Smile", 0), ("UN_strahlt", "UN", "Smile Big|Smile", 0),
    ("UN_denkt", "UN", "Suspicious", 0), ("UN_sorge", "UN", "Concerned|Serious", 0), ("UN_ernst", "UN", "Serious", 0),
    ("UN_staunt", "UN", "Awe", 0), ("UN_aerger", "UN", "Very Angry", 0), ("UN_muede", "UN", "Tired", 0),
    ("UN_redet", "UN", "Serious", 1), ("UN_redet2", "UN", "Very Angry", 1),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_froh", "ST", "Smile", 0), ("ST_redet", "ST", "Smile", 1),
    ("ST_redet2", "ST", "Serious", 1), ("ST_denkt", "ST", "Suspicious", 0), ("ST_ernst", "ST", "Serious", 0),
    ("ST_sorge", "ST", "Concerned|Serious", 0), ("ST_staunt", "ST", "Awe", 0),
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
