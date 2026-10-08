"""Figuren für Folge 266 (Meldeauflage auf Grundlage der polizeilichen Generalklausel: Fußballfan muss sich am Spieltag
auf der Polizeiwache melden) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, keine Karikatur,
keine Klischees: kein Vereinsschal, keine Vereinsfarben, keine Tattoos, keine Waffen, kein Gewaltbild.
Herr Schütte (um 35, Fußballfan mit Meldeauflage; Stimme niklas): standing/crossed_arms-1 (Pullover Senfgelb #E3A857,
schwarze Hose), Kopf Short 4, Haut #E8B48F, kein Bart – ein gewöhnlicher Mann, nicht als „Schläger“ gezeichnet.
Polizistin Feddersen (um 30, Wache; Stimme julia): standing/blazer-2 (Jacke Dunkelblau #2F3E6B über hellblauem Shirt
#8DB3F2, Hose #2E3440; uniformähnlich ohne Abzeichen, Wappen oder Waffe; Beinprothese der Pose, keine Täterrolle),
Kopf Medium Bangs 3, Haut #C98E6A.
Wachleiter Rabe (um 60; Stimme helmut): standing/shirt-3 (Hemd Hellblaugrau #C9D6E8, schwarze Hose), Kopf No Hair 1,
Brille „Glasses“, Haut #EBC29E.
Posen nicht aus den letzten drei Folgen 262–264 (easing-1, blazer-3, pointing_finger-2, shirt-4, resting-1, blazer-4,
robot_dance-2, crossed_arms-2); keine Polka Dots, keine Bärte. Präfix SC_/FE_/RA_ (nie ER_). Alle Posen blicken im
Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (SC_redet, FE_redet, RA_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_266")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "SC": ("standing/crossed_arms-1", "Short 4", None, None, {"Skin": "#E8B48F", "Top": "#E3A857"}),
    "FE": ("standing/blazer-2", "Medium Bangs 3", None, None, {"Skin": "#C98E6A", "Jacket": "#2F3E6B", "Top": "#8DB3F2", "Pants": "#2E3440"}),
    "RA": ("standing/shirt-3", "No Hair 1", None, "Glasses", {"Skin": "#EBC29E", "Top": "#C9D6E8"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SC_ruhig", "SC", "Calm", 0), ("SC_redet", "SC", "Serious", 1), ("SC_skeptisch", "SC", "Suspicious", 0),
    ("SC_sorge", "SC", "Concerned|Serious", 0), ("SC_still", "SC", "Solemn", 0), ("SC_froh", "SC", "Smile", 0),
    ("SC_muede", "SC", "Tired", 0),
    ("FE_ruhig", "FE", "Calm", 0), ("FE_redet", "FE", "Smile", 1), ("FE_ernst", "FE", "Serious", 0),
    ("FE_froh", "FE", "Smile", 0), ("FE_denkt", "FE", "Suspicious", 0),
    ("RA_ruhig", "RA", "Calm", 0), ("RA_redet", "RA", "Serious", 1), ("RA_ernst", "RA", "Serious", 0),
    ("RA_denkt", "RA", "Suspicious", 0), ("RA_fest", "RA", "Driven", 0), ("RA_froh", "RA", "Smile", 0),
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
