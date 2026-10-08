"""Figuren für Folge 277 (§ 34 BauGB: Wann fügt sich ein Neubau ein?) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Herr Kronberg (KR, um 45, Investor, will einen Wohnblock bauen; Stimme marc): standing/blazer-2 (Sakko Dunkelblau #4A6FA5
  über hellem Shirt, schwarze Hose; die Pose hat eine Beinprothese – als normale Figur, nicht als Täterzeichen), Kopf Short 4,
  Brille Glasses 2, Haut #E0AC88, kein Bart.
Frau Morgenstern (MO, um 55, Nachbarin in einem Einfamilienhaus; Stimme sabrina): standing/easing-1 (offene Bluse Grün
  #8FD694 über Lila-Shirt #B8A9F5, schwarze Hose), Kopf Medium Bangs 2, Haut #F0C8A8, keine Brille.
Posen der letzten Folgen (274: easing-2, resting-2; 275: shirt-3, robot_dance-2; 276: easing-2, pointing_finger-2) nicht
verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine Bärte, keine Karikatur. Präfixe KR_/MO_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile bzw. „Augen|geschlossener Mund“
(Concerned|Serious, Smile Big|Smile). Sprechende Ansichten KR_redet, KR_redet2, MO_redet, MO_redet2 (und Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_277")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KR": ("standing/blazer-2", "Short 4", None, "Glasses 2", {"Skin": "#E0AC88", "Jacket": "#4A6FA5", "Top": "#E8EEF6"}),
    "MO": ("standing/easing-1", "Medium Bangs 2", None, None, {"Skin": "#F0C8A8", "Jacket": "#8FD694", "Top": "#B8A9F5"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KR_ruhig", "KR", "Calm", 0), ("KR_froh", "KR", "Smile", 0), ("KR_denkt", "KR", "Suspicious", 0),
    ("KR_ernst", "KR", "Serious", 0), ("KR_zuversicht", "KR", "Smile Big|Smile", 0),
    ("KR_redet", "KR", "Smile", 1), ("KR_redet2", "KR", "Calm", 1),
    ("MO_ruhig", "MO", "Calm", 0), ("MO_sorge", "MO", "Concerned|Serious", 0), ("MO_denkt", "MO", "Suspicious", 0),
    ("MO_ernst", "MO", "Serious", 0), ("MO_froh", "MO", "Smile", 0),
    ("MO_redet", "MO", "Concerned|Serious", 1), ("MO_redet2", "MO", "Smile", 1),
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
