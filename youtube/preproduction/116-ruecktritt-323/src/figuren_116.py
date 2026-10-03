"""Figuren für Folge 116 (Rücktritt § 323 BGB, Online-Shop) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Leni (um 35, Verbraucherin, Käuferin, Gläubigerin): standing/easing-1 (offene Jacke Orange #F9A66C (nicht Grün: 115 Karsten trägt ein grünes Hemd), Oberteil Weiß,
schwarze Hose, Turnschuhe), Kopf Long Curly (schwarzes Haar), keine Brille.
Ottmar (um 60, Inhaber des Online-Shops, Verkäufer, Schuldner): standing/robot_dance-2 (schwarzes Oberteil, Hose Blau
#8DB3F2; die geöffnete Hand passt zur Bitte um Geduld), Kopf No Hair 2 (Halbglatze), Brille Glasses 3, kein Bart.
Keine Prothesen-Pose, keine Bärte, keine Karikatur.
Posen, Farben und Muster nicht aus den Folgen 113–115 (resting-1, shirt-1, crossed_arms-1, walking-2, blazer-4, shirt-3,
sitting/crossed_legs, resting-2, blazer-3) und nicht aus 112 (pointing_finger-2, walking-1); keine Polka Dots.
Präfix LE_/OT_ (nie ER_, weil bausteine.peep_voll ER_* in den Ordner op_we umleitet). Alle Posen blicken im Original nach
rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Tired bzw. „Augen|
geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten (LE_redet, LE_bestimmt, OT_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_116")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

LE_F = {"Skin": "#D9A47E", "Jacket": "#F9A66C", "Top": "#FFFFFF"}
OT_F = {"Skin": "#F0CDB0", "Pants": "#8DB3F2"}
# Person/Pose: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "LE": ("standing/easing-1", "Long Curly", None, None, LE_F),
    "OT": ("standing/robot_dance-2", "No Hair 2", None, "Glasses 3", OT_F),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("LE_ruhig", "LE", "Calm", 0), ("LE_redet", "LE", "Smile", 1), ("LE_bestimmt", "LE", "Serious", 1),
    ("LE_froh", "LE", "Smile Big|Smile", 0), ("LE_sorge", "LE", "Concerned|Serious", 0), ("LE_denkt", "LE", "Suspicious", 0),
    ("LE_muede", "LE", "Tired", 0),
    ("OT_ruhig", "OT", "Calm", 0), ("OT_redet", "OT", "Concerned|Serious", 1), ("OT_sorge", "OT", "Concerned|Serious", 0),
    ("OT_denkt", "OT", "Suspicious", 0), ("OT_staunt", "OT", "Awe", 0), ("OT_froh", "OT", "Smile Big|Smile", 0),
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
