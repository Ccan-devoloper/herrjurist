"""Figuren für Folge 101 (Gesetzgebungsverfahren) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Der Bundesratspräsident (um 60, ohne Namen, Funktionsrolle): standing/crossed_arms-1 (blauer Pullover, verschränkte
Arme, schwarze Hose – die Hose ist in dieser Pose nicht einfärbbar), Kopf Gray Medium, Brille Glasses 3.
Frau Hensel (um 45, Landesministerin, stimmt „Ja“): standing/pointing_finger-1 (erhobener Zeigefinger wie beim Handzeichen;
schwarzes Outfit, die Pose hat keine einfärbbare Kleidung), Kopf Medium Bangs 2.
Herr Rieger (um 35, Landesminister, stimmt „Nein“): standing/robot_dance-2 (schwarzer Pullover, Hand zur Seite,
Hose Braun), Kopf Short 2.
Frau Kähler (um 30, Sachbearbeiterin in einer Meldebehörde, heitere Nebenrolle): standing/polka_dots (gepunktetes
Oberteil, Hose Rot), Kopf Long Bangs.
Posen nicht aus den letzten drei Folgen 098/099 (blazer-1/-3, resting-2, shirt-4, walking-3; 100 lag nicht vor);
crossed_arms-1 zuletzt in 096. robot_dance-2 (Rieger) hat Lexis Haltung (robot_dance-1), aber eigenes Outfit und
Kopf; beide stehen nie zusammen im Bild. Keine Bärte, keine Prothesen-Posen. Alle Posen blicken im Original nach rechts; die Grundansicht
ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Driven, Awe, Contempt bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten (…_redet…, Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_101")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "PR": ("standing/crossed_arms-1", "Gray Medium", None, "Glasses 3", {"Skin": "#EBC2A0", "Top": "#8DB3F2", "Pants": "#4A5568", "Hair": "#C4C4CC"}),
    "HS": ("standing/pointing_finger-1", "Medium Bangs 2", None, None, {"Skin": "#F1C6A5"}),
    "RI": ("standing/robot_dance-2", "Short 2", None, None, {"Skin": "#C68E62", "Pants": "#9A7B5B"}),
    "KA": ("standing/polka_dots", "Long Bangs", None, None, {"Skin": "#E8B894", "Pants": "#F07A6A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("PR_ruhig", "PR", "Calm", 0), ("PR_redet", "PR", "Serious", 1), ("PR_entschlossen", "PR", "Driven", 0),
    ("HS_ruhig", "HS", "Calm", 0), ("HS_redet", "HS", "Driven", 1), ("HS_froh", "HS", "Smile", 0),
    ("HS_denkt", "HS", "Suspicious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_aerger", "RI", "Contempt", 0),
    ("RI_denkt", "RI", "Suspicious", 0),
    ("KA_ruhig", "KA", "Calm", 0), ("KA_redet", "KA", "Smile", 1), ("KA_froh", "KA", "Smile Big|Smile", 0),
    ("KA_denkt", "KA", "Suspicious", 0), ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_redetstaunt", "KA", "Awe", 1),
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
