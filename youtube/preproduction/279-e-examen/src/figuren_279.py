"""Figuren für Folge 279 (E-Examen: fiktiver Prüfungssaal mit Laptops) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Telse (TE, Anfang 20, Jurastudentin in Nordrhein-Westfalen; Stimme ela_froh): stehend standing/robot_dance-3 (offene Geste,
  Oberteil Lila #B8A9F5, Hose Schwarz #151515 eingefärbt, weiße Schuhe), sitzend am Laptop sitting/mid-2 (Oberteil Lila
  #B8A9F5, schwarze Hose der Pose) – gleiche Kleidung; Kopf Long Bangs (schwarzes Haar, nicht einfärbbar), Haut #F2CBA8,
  keine Brille, kein Bart.
Jost (JO, Ende 20, Bruder, hat das zweite Examen in Bayern am Laptop geschrieben; Stimme niklas): standing/blazer-4 (Sakko
  Petrol #8CCBC0, Shirt Weiß #FFFFFF, schwarze Hose der Pose), Kopf Short 1 (schwarzes Haar), Haut #B07552, keine Brille,
  kein Bart.
Posen der letzten drei Folgen nicht verwendet (276: easing-2, pointing_finger-2; 277: blazer-2, easing-1; 278: noch ohne
Figurenrezept; zusätzlich 273–275: crossed_arms-2, shirt-4, easing-2, resting-2, shirt-3, robot_dance-2). robot_dance-1
bleibt Lexi; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe
TE_/JO_ (nie ER_). Die Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links,
Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Suspicious, Serious, Driven, Cute bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten TE_redet, TE_redet2, JO_redet,
JO_redetfroh (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt
bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_279")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "TE": ("standing/robot_dance-3", "Long Bangs", None, None, {"Skin": "#F2CBA8", "Top": "#B8A9F5", "Pants": "#151515"}),
    "TS": ("sitting/mid-2", "Long Bangs", None, None, {"Skin": "#F2CBA8", "Top": "#B8A9F5"}),
    "JO": ("standing/blazer-4", "Short 1", None, None, {"Skin": "#B07552", "Jacket": "#8CCBC0", "Top": "#FFFFFF"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TE_ruhig", "TE", "Calm", 0), ("TE_sorge", "TE", "Concerned|Serious", 0), ("TE_denkt", "TE", "Suspicious", 0),
    ("TE_froh", "TE", "Smile", 0), ("TE_entschlossen", "TE", "Driven", 0), ("TE_staunt", "TE", "Cute", 0),
    ("TE_lacht", "TE", "Smile Big|Smile", 0),
    ("TE_redet", "TE", "Concerned|Serious", 1), ("TE_redet2", "TE", "Driven", 1),
    ("TS_tippt", "TS", "Calm", 0), ("TS_froh", "TS", "Smile", 0), ("TS_redet", "TS", "Calm", 1),
    ("JO_ruhig", "JO", "Calm", 0), ("JO_froh", "JO", "Smile", 0), ("JO_ernst", "JO", "Serious", 0),
    ("JO_denkt", "JO", "Suspicious", 0), ("JO_stolz", "JO", "Smile Big|Smile", 0),
    ("JO_redet", "JO", "Calm", 1), ("JO_redetfroh", "JO", "Smile", 1),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    nur = sys.argv[1:]          # optional: nur diese Namen (Probe)
    n = 0
    for name, p, mimik, mund in LISTE:
        if nur and name not in nur:
            continue
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    if not nur:
        # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
        for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
            a = LX.AUSSEHEN
            for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
                figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
