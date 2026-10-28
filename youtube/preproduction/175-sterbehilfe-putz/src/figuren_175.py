"""Figuren für Folge 175 (Sterbehilfe, Behandlungsabbruch, Fall Putz) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Fiktiver Rahmen: Strafrecht-Seminar. Reale Beteiligte (die Mutter, die Tochter, ihr Bruder, der Anwalt, Heim- und
Gerichtspersonen) werden NICHT dargestellt.
Thilo (um 23, Jurastudent; Stimme niklas): standing/easing-1 (offenes Hemd Lila #B8A9F5 über weißem Shirt, schwarze Hose),
  Kopf Short 1, Haut #EBC3A0, ohne Brille.
Professor Wedekind (um 60, leitet das Seminar; Stimme helmut): standing/pointing_finger-1 (ganz in Schwarz, Zeigefinger
  erhoben wie beim Erklären), Kopf No Hair 3 (grauer Haarkranz), Brille Glasses 4, Haut #E3B08C, kein Bart.
Posen nicht aus 172–174 (shirt-3, easing-2, robot_dance-2, resting-1, blazer-4, crossed_arms-1, resting-2, shirt-4,
crossed_arms-2); keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Polka Dots, keine Bärte, kein Arzt-/Pflegekittel.
Ruhige Mimiken (Thema Sterben): Calm, Serious, Solemn, Suspicious; kein Lachen.
Präfix TH_/WD_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (TH_redet, WD_redet, Lexi) zusätzlich
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_175")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "TH": ("standing/easing-1", "Short 1", None, None, {"Skin": "#EBC3A0", "Jacket": "#B8A9F5", "Top": "#FFFFFF"}),
    "WD": ("standing/pointing_finger-1", "No Hair 3", None, "Glasses 4", {"Skin": "#E3B08C"}),
}

LISTE = [
    ("TH_ruhig", "TH", "Calm", 0), ("TH_redet", "TH", "Serious", 1), ("TH_denkt", "TH", "Suspicious", 0),
    ("TH_ernst", "TH", "Solemn", 0),
    ("WD_ruhig", "WD", "Calm", 0), ("WD_redet", "WD", "Serious", 1), ("WD_denkt", "WD", "Suspicious", 0),
    ("WD_ernst", "WD", "Solemn", 0),
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
