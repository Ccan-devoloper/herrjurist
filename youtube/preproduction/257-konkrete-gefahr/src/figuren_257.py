"""Figuren für Folge 257 (Konkrete Gefahr: Mann mit offenem Benzinkanister vor einem Mehrfamilienhaus) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, keine Karikatur, keine Klischees.
Herr Fichtner (um 60, Hausbewohner, will den Rasenmäher auftanken; Stimme helmut): standing/shirt-4 (schwarzes Hemd,
Hose Beige #B89A72), Kopf No Hair 3 (Haarkranz Grau #BDBDBD), Haut #EBC29E, kein Bart – freundlich, sorglos, nicht stereotyp.
Polizistin Eilers (um 30; Stimme julia): standing/easing-1 (Jacke Dunkelblau #2F3E6B über hellblauem Shirt #8DB3F2, schwarze
Hose; uniformähnlich, ohne Abzeichen, Wappen oder Waffe), Kopf Medium 2, Haut #D9A07A.
Nachbar Sebastian (um 25, ruft die Polizei; Stimme niklas): standing/robot_dance-2 (schwarzes Oberteil, Hose Schiefergrau
#3D4A5C; ausgestreckte Hand hält das Handy), Kopf Medium 1, Haut #F2D0B4.
Posen nicht aus den letzten drei Folgen 254–256 (resting-1/-2, shirt-3, walking-1/-3, robot_dance-3, blazer-4, easing-2)
und nicht aus der Parallelfolge 258 (pointing_finger-2, crossed_arms-2, blazer-3); keine Polka Dots, keine Bärte,
keine Prothesen-Posen. Präfix FI_/EI_/SE_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (FI_redet, EI_redet, SE_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_257")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "FI": ("standing/shirt-4", "No Hair 3", None, None, {"Skin": "#EBC29E", "Pants": "#B89A72", "Hair": "#BDBDBD"}),
    "EI": ("standing/easing-1", "Medium 2", None, None, {"Skin": "#D9A07A", "Jacket": "#2F3E6B", "Top": "#8DB3F2", "Pants": "#2E3440"}),
    "SE": ("standing/robot_dance-2", "Medium 1", None, None, {"Skin": "#F2D0B4", "Pants": "#3D4A5C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("FI_ruhig", "FI", "Calm", 0), ("FI_redet", "FI", "Calm", 1), ("FI_froh", "FI", "Smile", 0),
    ("FI_denkt", "FI", "Suspicious", 0), ("FI_sorge", "FI", "Concerned|Serious", 0), ("FI_still", "FI", "Solemn", 0),
    ("EI_ruhig", "EI", "Calm", 0), ("EI_redet", "EI", "Serious", 1), ("EI_ernst", "EI", "Serious", 0),
    ("EI_denkt", "EI", "Suspicious", 0), ("EI_froh", "EI", "Smile", 0), ("EI_fest", "EI", "Driven", 0),
    ("SE_ruhig", "SE", "Calm", 0), ("SE_redet", "SE", "Concerned|Serious", 1), ("SE_sorge", "SE", "Concerned|Serious", 0),
    ("SE_denkt", "SE", "Suspicious", 0), ("SE_froh", "SE", "Smile", 0),
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
