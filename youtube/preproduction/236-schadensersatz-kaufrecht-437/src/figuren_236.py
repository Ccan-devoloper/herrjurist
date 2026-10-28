"""Figuren für Folge 236 (Schadensersatz Kaufrecht, § 437 Nr. 3 BGB) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Personen fiktiv.
Katharina (KA, um 35, Käuferin, privat; Stimme lucy): standing/crossed_arms-2 (schwarzes Oberteil der Pose, Hose Lila #B8A9F5,
  schwarze Schuhe), Kopf Long Curly, Haut #EAC1A0, kein Bart, keine Brille.
Raimund (RM, um 50, Inhaber eines Elektrogeschäfts, Verkäufer, Händler – nicht Hersteller; Stimme stephan): standing/blazer-3
  (Sakko Blau #8DB3F2, Oberteil Weiß, Hose Grau #8A8F99), Kopf Short 5, Brille Glasses 3, Haut #D9A47E, kein Bart.
  Kein Bösewicht: freundlich, bietet ein neues Gerät an.
Posen der letzten Folgen (231: walking-2, robot_dance-3; 232: resting-1, easing-1, crossed_arms-1; 233: easing-1, blazer-4,
pointing_finger-1, sitting/bike, resting-2; 235: walking-3, blazer-4) nicht verwendet; robot_dance-1 bleibt Lexi; Prothesen-
Posen (blazer-1, blazer-2, shirt-1/2) verworfen; keine Polka Dots, keine Bärte. Präfixe KA_/RM_ (nie ER_). Alle Posen blicken
im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Solemn, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten KA_redet (Concerned|Serious),
RM_redet (Smile), RM_erklaert (Calm) und Lexi zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_236")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KA": ("standing/crossed_arms-2", "Long Curly", None, None, {"Skin": "#EAC1A0", "Pants": "#B8A9F5"}),
    "RM": ("standing/blazer-3", "Short 5", None, "Glasses 3", {"Skin": "#D9A47E", "Jacket": "#8DB3F2", "Top": "#FFFFFF",
                                                              "Pants": "#8A8F99"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KA_ruhig", "KA", "Calm", 0), ("KA_froh", "KA", "Smile", 0), ("KA_freut", "KA", "Smile Big|Smile", 0),
    ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_schreck", "KA", "Fear", 0), ("KA_ernst", "KA", "Serious", 0),
    ("KA_denkt", "KA", "Suspicious", 0), ("KA_muede", "KA", "Tired", 0), ("KA_staunt", "KA", "Awe", 0),
    ("KA_redet", "KA", "Concerned|Serious", 1),
    ("RM_ruhig", "RM", "Calm", 0), ("RM_froh", "RM", "Smile", 0), ("RM_sorge", "RM", "Concerned|Serious", 0),
    ("RM_denkt", "RM", "Suspicious", 0), ("RM_still", "RM", "Solemn", 0), ("RM_staunt", "RM", "Awe", 0),
    ("RM_schreck", "RM", "Fear", 0), ("RM_freut", "RM", "Smile Big|Smile", 0),
    ("RM_redet", "RM", "Smile", 1), ("RM_erklaert", "RM", "Calm", 1),
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
