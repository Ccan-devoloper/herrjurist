"""Figuren für Folge 219 (Aus- und Einbaukosten § 439 Abs. 3 BGB, Fliesen-Fall) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Oltmann (OL, um 45, Bauherr, Verbraucher; Stimme marc): standing/easing-2 (offenes Hemd Grün #8FD694 über schwarzem
Shirt, Hose Dunkelblau #3D4A6B, Turnschuhe), Kopf Short 5, Haut #E8B48E, keine Brille, kein Bart.
Frau Reinecke (RE, um 50, Inhaberin eines Fliesenhandels, Unternehmerin; Stimme laura_ruhig): standing/robot_dance-3
(Tunika Koralle #F07A6A, Hose #3D3D58, einladende Handgeste), Kopf Medium Bangs, Brille Glasses 2, Haut #D9A884.
Der Fliesenleger (FL, um 60, ohne Namen, Funktionsrolle; Stimme william): standing/walking-2 (schwarzes Shirt der Pose,
Arbeitshose Graublau #6B7A8F), Kopf Gray Short (Haar #A8A8A8), Haut #C98E66.
Abwechslung: Posen nicht aus 215–218 (robot_dance-2, resting-1, crossed_arms-1/-2, shirt-3, shirt-4, blazer-3, blazer-4,
resting-2, walking-1, easing-1, pointing_finger-2, one_leg_up-1). easing-2 zuletzt 125 (Hemd blau, Hose grau) – hier Grün/
Dunkelblau und anderer Kopf. Keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur.
Präfix OL_/RE_/FL_ (nie ER_). Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (Calm, Serious, Smile, Suspicious, Very Angry bzw. „Augen|geschlossener Mund“).
Sprechende Ansichten (OL_redet, RE_redet, FL_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_219")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "OL": ("standing/easing-2", "Short 5", None, None, {"Skin": "#E8B48E", "Jacket": "#8FD694", "Pants": "#3D4A6B"}),
    "RE": ("standing/robot_dance-3", "Medium Bangs", None, "Glasses 2", {"Skin": "#D9A884", "Top": "#F07A6A", "Pants": "#3D3D58"}),
    "FL": ("standing/walking-2", "Gray Short", None, None, {"Skin": "#C98E66", "Pants": "#6B7A8F", "Hair": "#A8A8A8"}),
}

LISTE = [
    ("OL_ruhig", "OL", "Calm", 0), ("OL_froh", "OL", "Smile Big|Smile", 0), ("OL_redet", "OL", "Serious", 1),
    ("OL_sorge", "OL", "Concerned|Serious", 0), ("OL_denkt", "OL", "Suspicious", 0), ("OL_aerger", "OL", "Very Angry", 0),
    ("RE_ruhig", "RE", "Calm", 0), ("RE_froh", "RE", "Smile", 0), ("RE_redet", "RE", "Serious", 1),
    ("RE_denkt", "RE", "Suspicious", 0), ("RE_ernst", "RE", "Serious", 0), ("RE_sorge", "RE", "Concerned|Serious", 0),
    ("FL_ruhig", "FL", "Calm", 0), ("FL_redet", "FL", "Serious", 1), ("FL_denkt", "FL", "Suspicious", 0),
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
