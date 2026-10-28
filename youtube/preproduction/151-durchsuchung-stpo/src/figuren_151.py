"""Figuren für Folge 151 (Durchsuchung StPO, Polizei klingelt nachts ohne Beschluss) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Helene (um 30, Wohnungsinhaberin, Verdacht der Hehlerei; Stimme lucy): standing/easing-1 (Strickjacke Lila #B8A9F5 über
weißem Shirt, schwarze Hose, weiße Schuhe – Hauskleidung am späten Abend), Kopf Long Curly (Haar #6B4430), Haut #F2D0B4.
Polizeikommissar Steiger (um 45; Stimme stephan): standing/shirt-4 (dunkles Hemd, Hose Dunkelblau #2F3E5C – neutral wie
Dienstkleidung, ohne Abzeichen, Wappen oder Waffe), Kopf Short 5 (Haar #4A3628), Haut #E8B894, kein Bart, keine Brille.
Sachlich, keine Karikatur, keine bösen Mimiken; keine Prothesen-Posen, keine Bärte, keine Polka Dots. Posen nicht aus den
letzten drei Folgen 148–150 (robot_dance-3, walking-3, blazer-4, crossed_arms-2, shirt-3, blazer-3); Lexi bleibt robot_dance-1.
Präfix HE_/ST_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (HE_redet, ST_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_151")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "HE": ("standing/easing-1", "Long Curly", None, None, {"Skin": "#F2D0B4", "Top": "#FFFFFF", "Jacket": "#B8A9F5", "Hair": "#6B4430"}),
    "ST": ("standing/shirt-4", "Short 5", None, None, {"Skin": "#E8B894", "Pants": "#2F3E5C", "Hair": "#4A3628"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Concerned|Serious", 1), ("HE_schreck", "HE", "Fear", 0),
    ("HE_denkt", "HE", "Suspicious", 0), ("HE_sorge", "HE", "Concerned|Serious", 0), ("HE_still", "HE", "Solemn", 0),
    ("HE_muede", "HE", "Tired", 0), ("HE_froh", "HE", "Smile", 0),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_redet", "ST", "Serious", 1), ("ST_ernst", "ST", "Serious", 0),
    ("ST_denkt", "ST", "Suspicious", 0), ("ST_still", "ST", "Solemn", 0), ("ST_sorge", "ST", "Concerned|Serious", 0),
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
