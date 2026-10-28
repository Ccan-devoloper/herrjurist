"""Figuren für Folge 254 (§ 123 VwGO, einstweilige Anordnung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren
fiktiv, keine Karikaturen.
Magda (MA, um 30, Standbetreiberin, backt Waffeln; Stimme ela_froh): standing/resting-1 (Oberteil Apricot #F6B58A, dunkle Hose
  der Pose), Kopf Long Curly (Locken), Haut #F2C9A6 – freundlich, sympathisch. (robot_dance-3 verworfen: zu nah an Lexi.)
Herr Eckstein (EC, um 60, Sachbearbeiter im Marktamt der Stadt; Stimme helmut): standing/shirt-3 (Hemd Hellblau #C9DAF5,
  dunkle Hose der Pose), Kopf Short 1, Brille Glasses 3, Haut #E8B898 – sachlich, kein Bösewicht.
Der Richter (RI, um 38, Verwaltungsgericht, Funktionsrolle ohne Namen; Stimme niklas): Brustbild body/Blazer Black Tee
  (Jacke Schwarz #2B2B33 wie eine Robe) hinter der Richterbank, Kopf Short 4, Haut #D9A07A.
Ein Kind (KI, um 8, Kundin am Stand, ohne Namen und ohne Stimme, Mund immer zu): standing/walking-1 (Oberteil Grün #8FD694),
  Kopf Bangs (Haar #3B2A20), Haut #C68E6A; im Bild etwa 60 % der Erwachsenenhöhe.
Posen nicht aus 251–253 (easing-1, resting-2, pointing_finger-2, blazer-3, walking-2, robot_dance-2, crossed_arms-1, shirt-4,
crossed_arms-2 in 250); keine Prothesen-Posen (shirt-1/-2, blazer-1/-2), keine Polka Dots, keine Bärte.
Präfixe MA_/EC_/RI_/KI_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (MA_redet, EC_redet, RI_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_254")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "MA": ("standing/resting-1", "Long Curly", None, None, {"Skin": "#F2C9A6", "Top": "#F6B58A"}),
    "EC": ("standing/shirt-3", "Short 1", None, "Glasses 3", {"Skin": "#E8B898", "Top": "#C9DAF5"}),
    "RI": ("body/Blazer Black Tee", "Short 4", None, None, {"Skin": "#D9A07A", "Jacket": "#2B2B33"}),
    "KI": ("standing/walking-1", "Bangs", None, None, {"Skin": "#C68E6A", "Top": "#8FD694", "Hair": "#3B2A20"}),
}

LISTE = [
    ("MA_froh", "MA", "Smile", 0), ("MA_ruhig", "MA", "Calm", 0), ("MA_sorge", "MA", "Concerned|Serious", 0),
    ("MA_schreck", "MA", "Awe", 0), ("MA_denkt", "MA", "Suspicious", 0), ("MA_entschl", "MA", "Driven", 0),
    ("MA_muede", "MA", "Tired", 0), ("MA_strahlt", "MA", "Smile Big|Smile", 0),
    ("MA_redet", "MA", "Concerned|Serious", 1),
    ("EC_ruhig", "EC", "Calm", 0), ("EC_ernst", "EC", "Serious", 0), ("EC_streng", "EC", "Solemn", 0),
    ("EC_denkt", "EC", "Suspicious", 0),
    ("EC_redet", "EC", "Solemn", 1),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_ernst", "RI", "Serious", 0),
    ("RI_redet", "RI", "Serious", 1),
    ("KI_froh", "KI", "Smile", 0), ("KI_strahlt", "KI", "Cute", 0),
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
