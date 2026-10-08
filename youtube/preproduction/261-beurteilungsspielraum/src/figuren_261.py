"""Figuren für Folge 261 (Beurteilungsspielraum: Klausur, Korrekturzimmer, Zuhause, Verwaltungsgericht) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, keine realen Personen, kein echtes Prüfungsamt.
Jorinde (JO, Anfang 20, Examenskandidatin; Stimme lucy): standing/resting-2 (schwarzes Oberteil, grüne Hose #8FD694,
  Hände an den Hüften), Kopf Long Curly (dunkle Locken), Haut #F2CDB0. Nicht pointing_finger-1: gleiche Pose wie
  pointing_finger-2 (Isolde, Folge 258).
Herr Ellerbrock (EL, um 60, Prüfer; Stimme christian): standing/shirt-3 (türkisfarbenes Hemd #7FD6D0, schwarze Hose),
  Kopf Gray Short, Brille Glasses 3, Haut #E3B08A.
Die Richterin (RI, um 60, Verwaltungsgericht, ohne Namen; Stimme hilde): standing/easing-2 (dunkle Jacke und Hose #2E2E36),
  Kopf Gray Bun, Brille Glasses 4, Haut #D8A07A.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots; keine Pose aus den letzten drei Folgen
258–260 (pointing_finger-2, crossed_arms-1/-2, blazer-3/-4, resting-1, robot_dance-3); resting-2 und easing-2 zuletzt in 256
(dort andere Köpfe und Farben), shirt-3 zuletzt in 254. Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, _r nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Driven, Suspicious bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_261")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "JO": ("standing/resting-2", "Long Curly", None, None, {"Skin": "#F2CDB0", "Pants": "#8FD694"}),
    "EL": ("standing/shirt-3", "Gray Short", None, "Glasses 3", {"Skin": "#E3B08A", "Top": "#7FD6D0"}),
    "RI": ("standing/easing-2", "Gray Bun", None, "Glasses 4", {"Skin": "#D8A07A", "Jacket": "#2E2E36", "Pants": "#2E2E36"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("JO_ruhig", "JO", "Calm", 0), ("JO_denkt", "JO", "Suspicious", 0), ("JO_froh", "JO", "Smile", 0),
    ("JO_sorge", "JO", "Concerned|Serious", 0), ("JO_entschl", "JO", "Driven", 0), ("JO_liest", "JO", "Serious", 0),
    ("JO_redet", "JO", "Driven", 1),
    ("EL_ruhig", "EL", "Calm", 0), ("EL_streng", "EL", "Serious", 0), ("EL_denkt", "EL", "Suspicious", 0),
    ("EL_redet", "EL", "Serious", 1),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_denkt", "RI", "Suspicious", 0),
    ("RI_redet", "RI", "Serious", 1),
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
