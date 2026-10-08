"""Figuren für Folge 283 (§ 80a VwGO: Der Bagger rollt – Eilrechtsschutz des Nachbarn) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv.
Herr Brodbeck (BR, um 60, Bauherr eines Mehrfamilienhauses; Stimme william): standing/blazer-4 (Sakko Braungrau #8A7560
  über hellem Shirt #F2EEE6, dunkle Hose), Kopf No Hair 2 (Halbglatze), Brille Glasses 4, Haut #E3B48E, kein Bart.
Frau Fehling (FE, um 40, Nachbarin mit Haus und Garten; Stimme laura_ruhig): standing/easing-2 (offenes Hemd Orange #F9A66C
  über schwarzem Shirt, blaue Hose #4A6FA5), Kopf Medium 2, Haar Dunkelbraun, Haut #F0C8A8, keine Brille.
Posen der letzten drei Folgen (280: resting-1, shirt-3, resting-2; 281: shirt-4, resting-1; 282: easing-1, blazer-3,
crossed_arms-2) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Bärte, keine Prothesen-Pose, keine
Karikatur. Präfixe BR_/FE_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile bzw. „Augen|geschlossener Mund“
(Concerned|Serious, Smile Big|Smile). Sprechende Ansichten BR_redet, BR_redet2, FE_redet, FE_redet2 (und Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_283")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "BR": ("standing/blazer-4", "No Hair 2", None, "Glasses 4",
           {"Skin": "#E3B48E", "Jacket": "#8A7560", "Top": "#F2EEE6", "Pants": "#3E4A6B"}),
    "FE": ("standing/easing-2", "Medium 2", None, None,
           {"Skin": "#F0C8A8", "Jacket": "#F9A66C", "Top": "#FFFFFF", "Pants": "#4A6FA5", "Hair": "#5A3E2B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_froh", "BR", "Smile", 0), ("BR_denkt", "BR", "Suspicious", 0),
    ("BR_ernst", "BR", "Serious", 0), ("BR_zuversicht", "BR", "Smile Big|Smile", 0),
    ("BR_redet", "BR", "Calm", 1), ("BR_redet2", "BR", "Smile", 1),
    ("FE_ruhig", "FE", "Calm", 0), ("FE_sorge", "FE", "Concerned|Serious", 0), ("FE_denkt", "FE", "Suspicious", 0),
    ("FE_ernst", "FE", "Serious", 0), ("FE_froh", "FE", "Smile", 0),
    ("FE_redet", "FE", "Serious", 1), ("FE_redet2", "FE", "Calm", 1),
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
