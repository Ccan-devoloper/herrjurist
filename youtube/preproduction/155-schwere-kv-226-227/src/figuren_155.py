"""Figuren für Folge 155 (Schwere Körperverletzung § 226, Todesfolge § 227; Freitagabend vor einer Bar) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, Erwachsene, kein Milieu-Klischee.
Roswitha (um 45, schlägt Ludger mit der Faust ins Gesicht; Stimme sabrina): standing/blazer-4 (Blazer Lila #B8A9F5, weißes
Oberteil, schwarze Hose, weiße Schuhe), Kopf Medium 3 (Haar dunkelbraun #4A3222), Haut #E0AC86, keine Brille, kein Bart.
Sachlich, keine Dämonisierung: keine bösen Mimiken (kein Contempt, kein Angry, kein Rage), nur Calm/Serious/Suspicious/
Fear/Solemn/Concerned|Serious.
Ludger (um 50, Opfer; Stimme marc): standing/walking-3 (schwarzes T-Shirt, schwarze Hose, weiße Schuhe), Kopf Short 3 (Haar
#6B5440), Haut #F0C8A8, kein Bart, keine Brille. Nach dem Sturz sitzt er auf dem Pflaster: sitting/hands_back-1 mit gleicher
Kleidung (schwarzes T-Shirt, Hose #2B2B2B statt Hellblau), Mimik Tired bzw. Fear (keine Verletzungsdetails, kein Blut).
Keine Prothesen-Posen, keine Bärte, keine Polka Dots. Posen und Kleidung nicht aus 150–153 (shirt-3, blazer-3, easing-1,
shirt-4, walking-1, resting-1, resting-2) und nicht aus 038/042 (closed_legs-1, walking-1, doctor-nurse-02,
pointing_finger-2, walking-2, easing-2).
Präfix LU_/LS_/RO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (LU_redet, RO_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_155")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "RO": ("standing/blazer-4", "Medium 3", None, None, {"Skin": "#E0AC86", "Jacket": "#B8A9F5", "Top": "#FFFFFF",
                                                          "Hair": "#4A3222"}),
    "LU": ("standing/walking-3", "Short 3", None, None, {"Skin": "#F0C8A8", "Hair": "#6B5440"}),
    "LS": ("sitting/hands_back-1", "Short 3", None, None, {"Skin": "#F0C8A8", "Hair": "#6B5440", "Pants": "#2B2B2B"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("RO_ruhig", "RO", "Calm", 0), ("RO_redet", "RO", "Serious", 1), ("RO_denkt", "RO", "Suspicious", 0),
    ("RO_schreck", "RO", "Fear", 0), ("RO_still", "RO", "Solemn", 0), ("RO_sorge", "RO", "Concerned|Serious", 0),
    ("RO_ernst", "RO", "Serious", 0),
    ("LU_ruhig", "LU", "Calm", 0), ("LU_redet", "LU", "Serious", 1), ("LU_still", "LU", "Solemn", 0),
    ("LU_sorge", "LU", "Concerned|Serious", 0),
    ("LS_benommen", "LS", "Tired", 0), ("LS_schreck", "LS", "Fear", 0),
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
