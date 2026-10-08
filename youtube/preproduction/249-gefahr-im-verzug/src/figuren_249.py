"""Figuren für Folge 249 (Gefahr im Verzug, Art. 13 II GG: Polizei klingelt am Sonntagabend ohne Beschluss) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Ines (um 30, Grafikerin, Bewohnerin; Stimme lucy): standing/easing-2 (offenes Hemd Türkis #7FD6D0 über schwarzem Shirt,
dunkelgraue Hose #3D3D48), Kopf Medium Straight (Haar #5A3A28), Haut #F2D0B4.
Kommissar Bader (um 45, Ermittlungsperson; Stimme stephan): standing/blazer-2 (Sakko Graublau #4A5568 über weißem Shirt,
in Zivil, ohne Abzeichen, Wappen oder Waffe), Kopf Short 2 (Haar #3B2C22), Haut #E2B48E, kein Bart.
Kommissarin Ebner (um 35, Ermittlungsperson, spricht nicht): standing/shirt-3 (Hemd Hellblau #8DB3F2, schwarze Hose),
Kopf Bangs 2 (Haar #2B2018), Haut #C68E6A.
Bereitschaftsrichterin (um 60, Funktionsrolle, zu Hause mit dem Diensttelefon, spricht nicht): standing/resting-1
(Pullover Lila #B8A9F5), Kopf Gray Medium, Glasses 2, Haut #EBC29E.
Sachlich, keine Karikatur, keine bösen Mimiken; keine Bärte, keine Polka Dots. Posen nicht aus den letzten drei Folgen
246–248 (resting-2, crossed_arms-1/-2, blazer-3/-4, easing-1, walking-1, pointing_finger-2); Lexi bleibt robot_dance-1.
blazer-2 zeigt eine Beinprothese (Polizist, keine Täterrolle). Präfix IN_/BA_/EB_/RI_ (nie ER_). Alle Posen blicken im
Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt
nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (IN_redet, BA_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_249")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "IN": ("standing/easing-2", "Medium Straight", None, None, {"Skin": "#F2D0B4", "Top": "#7FD6D0", "Hair": "#5A3A28", "Pants": "#3D3D48"}),
    "BA": ("standing/blazer-2", "Short 2", None, None, {"Skin": "#E2B48E", "Jacket": "#4A5568", "Top": "#FFFFFF", "Hair": "#3B2C22"}),
    "EB": ("standing/shirt-3", "Bangs 2", None, None, {"Skin": "#C68E6A", "Top": "#8DB3F2", "Hair": "#2B2018"}),
    "RI": ("standing/resting-1", "Gray Medium", None, "Glasses 2", {"Skin": "#EBC29E", "Top": "#B8A9F5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("IN_ruhig", "IN", "Calm", 0), ("IN_redet", "IN", "Concerned|Serious", 1), ("IN_schreck", "IN", "Awe", 0),
    ("IN_denkt", "IN", "Suspicious", 0), ("IN_sorge", "IN", "Concerned|Serious", 0), ("IN_still", "IN", "Solemn", 0),
    ("IN_froh", "IN", "Smile", 0), ("IN_fest", "IN", "Driven", 0),
    ("BA_ruhig", "BA", "Calm", 0), ("BA_redet", "BA", "Serious", 1), ("BA_ernst", "BA", "Serious", 0),
    ("BA_denkt", "BA", "Suspicious", 0), ("BA_still", "BA", "Solemn", 0), ("BA_sorge", "BA", "Concerned|Serious", 0),
    ("EB_ruhig", "EB", "Calm", 0), ("EB_ernst", "EB", "Serious", 0), ("EB_denkt", "EB", "Suspicious", 0),
    ("EB_still", "EB", "Solemn", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_wartet", "RI", "Tired", 0), ("RI_froh", "RI", "Smile", 0),
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
