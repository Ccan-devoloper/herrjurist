"""Figuren für Folge 231 (Erlaubnistatbestandsirrtum) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Bärbel (BA, Mitte 40, Joggerin; Stimme sabrina): standing/walking-2 (schwarzes Laufshirt der Pose, Leggings Beere #C2457A),
  Kopf Bun, Haut #EDC3A0, keine Brille, kein Bart – verängstigt, nicht hysterisch.
Helge (HE, um 65, Spaziergänger und Finder; Stimme william): standing/robot_dance-3 (offene Hand: reicht das Handy; Pullover
  Ocker #D9A066, Hose Graublau #5A6B7A), Kopf No Hair 2, Brille Glasses, Haut #E3B08C, kein Bart – sympathisch, kein Klischee.
Posen nicht aus 228–230 (robot_dance-2, polka_dots, crossed_legs, closed_legs-1, blazer-2, shirt-3, blazer-3, easing-2,
walking-1, pointing_finger-2) und nicht aus 226/227 (resting-1, blazer-4, crossed_arms-2, walking-3, pointing_finger-1,
easing-1); keine Prothesen-Posen (shirt-1, shirt-2, blazer-1, blazer-2), keine Polka Dots, keine Bärte.
Präfix BA_/HE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (BA_ruft, HE_ruft, HE_klagt, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_231")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "BA": ("standing/walking-2", "Bun", None, None, {"Skin": "#EDC3A0", "Pants": "#C2457A"}),
    "HE": ("standing/robot_dance-3", "No Hair 2", None, "Glasses", {"Skin": "#E3B08C", "Top": "#D9A066", "Pants": "#5A6B7A"}),
}

LISTE = [
    ("BA_ruhig", "BA", "Calm", 0), ("BA_froh", "BA", "Smile", 0), ("BA_angst", "BA", "Fear", 0),
    ("BA_sorge", "BA", "Concerned|Serious", 0), ("BA_ernst", "BA", "Serious", 0), ("BA_denkt", "BA", "Suspicious", 0),
    ("BA_muede", "BA", "Tired", 0), ("BA_schreck", "BA", "Awe", 0),
    ("BA_ruft", "BA", "Fear", 1),
    ("HE_ruhig", "HE", "Calm", 0), ("HE_froh", "HE", "Smile", 0), ("HE_sorge", "HE", "Concerned|Serious", 0),
    ("HE_ernst", "HE", "Serious", 0), ("HE_denkt", "HE", "Suspicious", 0), ("HE_augen", "HE", "Eyes Closed", 0),
    ("HE_muede", "HE", "Tired", 0),
    ("HE_ruft", "HE", "Smile", 1), ("HE_klagt", "HE", "Eyes Closed", 1),
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
