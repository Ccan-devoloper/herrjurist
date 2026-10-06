"""Figuren für Folge 205 (Recht auf Vergessen) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv;
der Beschwerdeführer des echten Falls und alle realen Beteiligten werden NICHT dargestellt. Herr Dornbusch bildet den
Grundfall nur nach und ist bewusst kein Täter-Klischee: freundlicher älterer Herr, Brille, gewöhnliche Kleidung, keine
„finstere“ Mimik.
Herr Dornbusch (DO, um 65, Nachbar; Stimme william): standing/shirt-3 (Hemd Lila #B8A9F5, schwarze Hose der Pose), Kopf Gray Short (Haar #B5B5B5),
Brille Glasses 3, Haut #EDC3A3, kein Bart.
Gerhild (GE, um 40, neue Nachbarin; Stimme sabrina): standing/resting-2 (Oberteil der Pose, Hose Türkis #7FD6D0), Kopf
Medium Bangs 2 (Haar #7A4E2D), Haut #D9A47E.
Herr Stöver (ST, um 50, Archivleiter des Verlags; Stimme marc): standing/easing-1 (offene Jacke Gelb #F9D56E über weißem Shirt, schwarze Hose), Kopf Short 4,
Haut #F0C8A8, kein Bart.
Posen nicht aus 201–203 (pointing_finger-2, blazer-4, robot_dance-3, blazer-3, shirt-4, crossed_arms-1); keine Polka Dots,
keine Bärte, keine Prothesen-Posen (shirt-1 und blazer-1 deshalb verworfen).
Präfix DO_/GE_/ST_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (DO_redet, GE_redet, ST_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_205")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "DO": ("standing/shirt-3", "Gray Short", None, "Glasses 3", {"Skin": "#EDC3A3", "Top": "#B8A9F5", "Hair": "#B5B5B5"}),
    "GE": ("standing/resting-2", "Medium Bangs 2", None, None, {"Skin": "#D9A47E", "Pants": "#7FD6D0", "Hair": "#7A4E2D"}),
    "ST": ("standing/easing-1", "Short 4", None, None, {"Skin": "#F0C8A8", "Jacket": "#F9D56E", "Top": "#FFFFFF"}),
}

LISTE = [
    ("DO_ruhig", "DO", "Smile", 0), ("DO_redet", "DO", "Smile", 1), ("DO_sorge", "DO", "Concerned|Serious", 0),
    ("DO_ernst", "DO", "Serious", 0), ("DO_muede", "DO", "Tired", 0), ("DO_froh", "DO", "Cute", 0),
    ("DO_bittet", "DO", "Serious", 1),
    ("GE_ruhig", "GE", "Calm", 0), ("GE_redet", "GE", "Awe", 1), ("GE_denkt", "GE", "Suspicious", 0),
    ("GE_staunt", "GE", "Awe", 0), ("GE_froh", "GE", "Smile", 0), ("GE_ernst", "GE", "Serious", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_redet", "ST", "Serious", 1), ("ST_denkt", "ST", "Suspicious", 0),
    ("ST_froh", "ST", "Smile", 0), ("ST_ernst", "ST", "Serious", 0),
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
