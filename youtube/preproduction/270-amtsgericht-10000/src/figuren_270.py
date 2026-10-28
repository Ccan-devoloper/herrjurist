"""Figuren für Folge 270 (Amtsgericht bis 10.000 €: in der Tischlerei) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, keine realen Personen; die Tischlerei Haberkorn ist erfunden.
Herr Haberkorn (HA, um 55, Tischlermeister; Stimme christian): standing/resting-1 (Arbeitspullover Moosgrün #6B8F71, schwarze
  Hose der Pose, Hand am Bund = entspannt, sympathisch), Kopf Short 4 (dunkles Haar), Haut #E3B48C. Kein Bart.
Irmela (IR, Mitte 20, Referendarin, seine Tochter; Stimme lucy): standing/robot_dance-2 (schwarzes Oberteil, Hose Lila #B8A9F5,
  offene Hand = erklärt), Kopf Bangs 2 (schwarzer Bob), Haut #F1C9A5.
Frau Bergfeld (BE, um 65, Büro der Tischlerei; Stimme hilde): standing/blazer-4 (Blazer Türkis #7FD6D0, Hose #3D4A5C, Hand an der
  Hüfte), Kopf Gray Medium (Haar #C8C8C8), Brille Glasses 2, Haut #EDC3A0.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots; keine Pose der letzten drei Folgen 266/267/269
(crossed_arms-1, blazer-1/-2, shirt-3, robot_dance-3, walking-3, polka_dots, easing-2, pointing_finger-1, resting-2) und nicht
robot_dance-1 (Lexi). Präfix HA_/IR_/BE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt
und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious bzw. „Augen|geschlossener Mund“
(Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear /
Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_270")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HA": ("standing/resting-1", "Short 4", None, None, {"Skin": "#E3B48C", "Top": "#6B8F71"}),
    "IR": ("standing/robot_dance-2", "Bangs 2", None, None, {"Skin": "#F1C9A5", "Pants": "#B8A9F5"}),
    "BE": ("standing/blazer-4", "Gray Medium", None, "Glasses 2", {"Skin": "#EDC3A0", "Hair": "#C8C8C8", "Jacket": "#7FD6D0",
                                                                    "Pants": "#3D4A5C"}),
}

LISTE = [
    ("HA_ruhig", "HA", "Calm", 0), ("HA_sorge", "HA", "Concerned|Serious", 0), ("HA_denkt", "HA", "Suspicious", 0),
    ("HA_froh", "HA", "Smile", 0),
    ("HA_redet", "HA", "Concerned|Serious", 1), ("HA_redetfroh", "HA", "Smile", 1),
    ("IR_ruhig", "IR", "Calm", 0), ("IR_denkt", "IR", "Suspicious", 0), ("IR_froh", "IR", "Smile", 0),
    ("IR_liest", "IR", "Serious", 0),
    ("IR_redet", "IR", "Smile", 1),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_denkt", "BE", "Suspicious", 0), ("BE_sorge", "BE", "Concerned|Serious", 0),
    ("BE_froh", "BE", "Smile", 0),
    ("BE_redet", "BE", "Serious", 1),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
