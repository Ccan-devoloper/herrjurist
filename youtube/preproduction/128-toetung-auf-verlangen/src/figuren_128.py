"""Figuren für Folge 128 (Tötung auf Verlangen oder Suizidhilfe, Gisela-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps,
CC0). Fiktiver Beispielfall; die Beteiligten des Gisela-Falls (BGHSt 19, 135) und des Falls BGH 6 StR 68/21 erscheinen nicht
als Figuren. Keine Karikatur, keine bösen Mimiken, ruhige und würdige Darstellung (Thema Suizid), keine Bärte, keine Prothesen.
Hedwig (um 70, schwer krank): standing/easing-1 (offenes Hemd Grün #8FD694 über Shirt Lila #B8A9F5, schwarze Hose),
  Kopf Gray Bun (Haar grau), Haut #EBC3A0. Stimme hilde.
Wilfried (um 70, ihr Mann): standing/resting-2 (schwarzer Pullover, Hose Blau #8DB3F2, ruhige Haltung), Kopf Gray Short,
  Brille Glasses 3, Haut #D9A47E. Stimme stephan.
Abwechslung: Posen nicht aus 124–126 (shirt-4, walking-2, bike, easing-2, crossed_arms-1, blazer-1, blazer-4, resting-1,
shirt-3, walking-1); easing-1 zuletzt 123, resting-2 zuletzt 122. Kein Polka-Dots-Muster. Verworfen: robot_dance-3
(gleiche Silhouette wie Lexi), crossed_arms-2 (wirkt mit ernster Mimik abweisend). Calm/Smile für Hedwig nicht verwendet
(lächelnde Mimik passt nicht zum Thema).
Präfix HE_/WF_ (nie ER_). Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts (Original).
Grundmimik immer mit geschlossenem Mund (Calm, Serious, Solemn, Tired bzw. „Augen|geschlossener Mund“).
Sprechende Ansichten (HE_redet, WF_redet, Lexi) zusätzlich a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear /
Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_128")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HE": ("standing/easing-1", "Gray Bun", None, None, {"Skin": "#EBC3A0", "Jacket": "#8FD694", "Top": "#B8A9F5"}),
    "WF": ("standing/resting-2", "Gray Short", None, "Glasses 3", {"Skin": "#D9A47E", "Pants": "#8DB3F2"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_muede", "HE", "Tired", 0), ("HE_ernst", "HE", "Serious", 0), ("HE_still", "HE", "Solemn", 0),
    ("HE_redet", "HE", "Serious", 1),
    ("WF_ruhig", "WF", "Calm", 0), ("WF_ernst", "WF", "Serious", 0), ("WF_still", "WF", "Solemn", 0),
    ("WF_sorge", "WF", "Concerned|Serious", 0), ("WF_redet", "WF", "Solemn", 1),
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
