"""Figuren für Folge 222 (Aktenauszug Assessorklausur, Klausurraum) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Hermine (Referendarin, Ende 20): standing/easing-1 (lila offene Jacke, weißes Oberteil, schwarze Hose), Kopf Long Curly.
Aufsicht (um 60, ohne Namen): standing/resting-1 (graublauer Pullover, schwarze Hose), Kopf No Hair 1, Brille Glasses 4.
Herr Rehberg (Kläger, Mitte 30): standing/robot_dance-2 (schwarzer Pullover, dunkelblaue Hose), Kopf Flat Top, ohne Bart.
Frau Pohlmann (Beklagte, Vermieterin, um 60): standing/crossed_arms-2 (schwarzes Oberteil, ockerfarbene Hose), Kopf Gray Bun
(graues Haar), Brille Glasses 3. Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots; keine Pose aus 216–219.
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Driven, Suspicious, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_222")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HE": ("standing/easing-1", "Long Curly", None, None, {"Skin": "#EDBF96", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}),
    "AU": ("standing/resting-1", "No Hair 1", None, "Glasses 4", {"Skin": "#F0C8A8", "Top": "#6B7A8F"}),
    "RB": ("standing/robot_dance-2", "Flat Top", None, None, {"Skin": "#D9A47E", "Pants": "#3D4A6B"}),
    "PO": ("standing/crossed_arms-2", "Gray Bun", None, "Glasses 3", {"Skin": "#E8B48E", "Hair": "#C8C8C8", "Pants": "#C9A66B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_liest", "HE", "Serious", 0), ("HE_schreibt", "HE", "Driven", 0),
    ("HE_denkt", "HE", "Suspicious", 0), ("HE_froh", "HE", "Smile", 0),
    ("HE_redet", "HE", "Concerned|Serious", 1), ("HE_frohredet", "HE", "Smile", 1),
    ("AU_ruhig", "AU", "Calm", 0), ("AU_redet", "AU", "Serious", 1),
    ("RB_ruhig", "RB", "Calm", 0), ("RB_redet", "RB", "Serious", 1),
    ("PO_ruhig", "PO", "Calm", 0), ("PO_redet", "PO", "Suspicious", 1),
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
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
