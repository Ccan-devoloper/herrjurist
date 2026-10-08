"""Figuren für Folge 273 (Freischuss: Fakultätsflur mit Aushang) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Leonore (LE, Anfang 20, Jurastudentin in NRW, siebtes Fachsemester; Stimme julia): standing/crossed_arms-2 (Arme
  verschränkt, schwarzes Oberteil der Pose, Hose Blau #8DB3F2, schwarze Schuhe), Kopf Medium Bangs 2 (Haar Kastanienbraun
  #7A4A2E), Haut #F2CBA8, keine Brille, kein Bart.
Rasmus (RA, Mitte 20, Freund, hat das Examen im letzten Jahr früh geschrieben; Stimme niklas): standing/shirt-4 (schwarzes
  Hemd der Pose, Hose Sand #D9B48F, weiße Schuhe), Kopf Short 3 (schwarzes Haar; die Frisur ist nicht einfärbbar), Haut #D9A27A, keine Brille,
  kein Bart.
Posen der letzten Folgen nicht verwendet (269: blazer-1, pointing_finger-1, resting-2; 270: resting-1, robot_dance-2,
blazer-4; 271: resting-1, easing-1; Methodik-Vorgänger 237: easing-2, blazer-3; 201: siehe dort). robot_dance-1 bleibt
Lexi; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe LE_/RA_
(nie ER_). Beide Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r
blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Suspicious, Serious, Driven, Awe bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten LE_redet, LE_redet2, RA_redet,
RA_redet2 (und Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_273")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "LE": ("standing/crossed_arms-2", "Medium Bangs 2", None, None, {"Skin": "#F2CBA8", "Pants": "#8DB3F2", "Hair": "#7A4A2E"}),
    "RA": ("standing/shirt-4", "Short 3", None, None, {"Skin": "#D9A27A", "Pants": "#D9B48F"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("LE_ruhig", "LE", "Calm", 0), ("LE_sorge", "LE", "Concerned|Serious", 0), ("LE_denkt", "LE", "Suspicious", 0),
    ("LE_froh", "LE", "Smile", 0), ("LE_entschlossen", "LE", "Driven", 0), ("LE_staunt", "LE", "Awe", 0),
    ("LE_ernst", "LE", "Serious", 0),
    ("LE_redet", "LE", "Concerned|Serious", 1), ("LE_redet2", "LE", "Driven", 1), ("LE_redetfroh", "LE", "Smile", 1),
    ("RA_ruhig", "RA", "Calm", 0), ("RA_froh", "RA", "Smile", 0), ("RA_ernst", "RA", "Serious", 0),
    ("RA_denkt", "RA", "Suspicious", 0), ("RA_stolz", "RA", "Smile Big|Smile", 0),
    ("RA_redet", "RA", "Calm", 1), ("RA_redetfroh", "RA", "Smile", 1),
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
