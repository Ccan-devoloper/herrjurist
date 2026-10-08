"""Figuren für Folge 258 (Anwaltsklausur: Besprechungszimmer einer Kanzlei) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv, keine realen Personen, keine Kanzleinamen.
Isolde (IS, Mitte 20, Referendarin in der Anwaltsstation; Stimme lucy): standing/pointing_finger-2 (schwarzes Oberteil,
  hellblaue Hose #8DB3F2, schwarze Schuhe, erhobener Zeigefinger = erklärt), Kopf Medium Bangs (schwarzes Haar), Haut #F1C9A5.
Frau Steinhoff (ST, um 70, Mandantin; Stimme hilde): standing/crossed_arms-2 (schwarzes Oberteil, lila Hose #B8A9F5,
  verschränkte Arme = verärgert), Kopf Gray Medium (Haar grau #C8C8C8), Brille Glasses 4, Haut #EDC3A0.
Herr Hohlfeld (HO, um 55, Rechtsanwalt und Ausbilder; Stimme stephan): standing/blazer-3 (Sakko graublau #5B6B8C über
  schwarzem Shirt, Hose #3D3D48, Hand an der Hüfte), Kopf Short 2 (Haar grau meliert #6E6E78), Brille Glasses 2, Haut #DDA882.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots; keine Pose aus den Folgen 253–256
(crossed_arms-1, resting-1/-2, shirt-3, Blazer Black Tee, walking-1/-3, robot_dance-3, blazer-4, easing-2).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Driven, Suspicious, Very Angry bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_258")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "IS": ("standing/pointing_finger-2", "Medium Bangs", None, None, {"Skin": "#F1C9A5", "Pants": "#8DB3F2"}),
    "ST": ("standing/crossed_arms-2", "Gray Medium", None, "Glasses 4", {"Skin": "#EDC3A0", "Hair": "#C8C8C8", "Pants": "#B8A9F5"}),
    "HO": ("standing/blazer-3", "Short 2", None, "Glasses 2", {"Skin": "#DDA882", "Hair": "#6E6E78", "Jacket": "#5B6B8C",
                                                               "Pants": "#3D3D48"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("IS_ruhig", "IS", "Calm", 0), ("IS_denkt", "IS", "Suspicious", 0), ("IS_schreibt", "IS", "Driven", 0),
    ("IS_froh", "IS", "Smile", 0), ("IS_liest", "IS", "Serious", 0),
    ("IS_redet", "IS", "Serious", 1),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_sorge", "ST", "Concerned|Serious", 0), ("ST_aerger", "ST", "Very Angry", 0),
    ("ST_froh", "ST", "Smile", 0),
    ("ST_redet", "ST", "Concerned|Serious", 1), ("ST_redetfroh", "ST", "Smile", 1),
    ("HO_ruhig", "HO", "Calm", 0), ("HO_denkt", "HO", "Suspicious", 0), ("HO_froh", "HO", "Smile", 0),
    ("HO_redet", "HO", "Serious", 1), ("HO_redetfroh", "HO", "Smile", 1),
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
