"""Figuren für Folge 196 (Flugreise-Fall) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Personen fiktiv.
Till (TI, 17, fliegt ohne Ticket weiter; Stimme niklas): standing/robot_dance-2 (schwarzer Pullover, Jeans #3F6FB5, weiße
  Schuhe), Kopf Pomp (dunkles Haar), Haut #F0C8A0, keine Brille, kein Bart. Offene Handgeste, sympathisch, nicht kriminalisiert.
Ruprecht (RU, um 60, Stationsleiter der Fluggesellschaft; Stimme helmut): standing/blazer-4 (Uniform-Sakko Navy #2F4A7A,
  weißes Shirt, schwarze Hose), Kopf No Hair 2 (Haarkranz Grau #BDBDBD), Brille Glasses 4, Haut #E6B897, kein Bart.
Mutter (MU, um 45, gesetzliche Vertreterin, spricht nicht): standing/crossed_arms-2 (schwarzes Oberteil, Hose Lila #B8A9F5),
  Kopf Medium 3 (Haar #5A3A22), Haut #F2CDB2.
Posen der letzten Folgen (190: resting-1/-2, walking-2; 191: easing-2, walking-1; 192: shirt-3, blazer-2; 193: shirt-3,
shirt-4; parallel 194: robot_dance-3, blazer-3; 195: pointing_finger-2, crossed_arms-1, blazer-3) nicht verwendet;
robot_dance-1 bleibt Lexi; keine Polka Dots, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2), keine Bärte. Präfixe TI_/RU_/MU_
(nie ER_). Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Awe, Fear, Serious, Suspicious, Tired, Solemn, Cute
bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten TI_redet (Smile), TI_klagt (Concerned|Serious),
RU_redet (Serious) und Lexi zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_196")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "TI": ("standing/robot_dance-2", "Pomp", None, None, {"Skin": "#F0C8A0", "Top": "#F07A6A", "Pants": "#3F6FB5", "Hair": "#7A4E2D"}),
    "RU": ("standing/blazer-4", "No Hair 2", None, "Glasses 4", {"Skin": "#E6B897", "Jacket": "#2F4A7A", "Top": "#FFFFFF",
                                                                 "Hair": "#BDBDBD"}),
    "MU": ("standing/crossed_arms-2", "Medium 3", None, None, {"Skin": "#F2CDB2", "Pants": "#B8A9F5", "Hair": "#5A3A22"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("TI_ruhig", "TI", "Calm", 0), ("TI_froh", "TI", "Smile", 0), ("TI_staunt", "TI", "Awe", 0), ("TI_schreck", "TI", "Fear", 0),
    ("TI_redet", "TI", "Smile", 1), ("TI_klagt", "TI", "Concerned|Serious", 1), ("TI_sorge", "TI", "Concerned|Serious", 0),
    ("TI_denkt", "TI", "Suspicious", 0), ("TI_muede", "TI", "Tired", 0), ("TI_still", "TI", "Solemn", 0),
    ("TI_ernst", "TI", "Serious", 0), ("TI_cute", "TI", "Cute", 0),
    ("RU_ruhig", "RU", "Calm", 0), ("RU_redet", "RU", "Serious", 1), ("RU_ernst", "RU", "Serious", 0),
    ("RU_denkt", "RU", "Suspicious", 0), ("RU_froh", "RU", "Smile", 0),
    ("MU_ruhig", "MU", "Calm", 0), ("MU_ernst", "MU", "Serious", 0), ("MU_still", "MU", "Solemn", 0), ("MU_denkt", "MU", "Suspicious", 0),
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
