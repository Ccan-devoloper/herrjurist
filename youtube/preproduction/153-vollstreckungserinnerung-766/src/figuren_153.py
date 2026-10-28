"""Figuren für Folge 153 (Vollstreckungserinnerung § 766 ZPO) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle fiktiv.
Herr Mühlbauer (MB, um 30, Schuldner; Stimme niklas): standing/easing-1 (offenes lila Hemd #B8A9F5 über weißem Shirt,
dunkle Hose #3A3A48), Kopf Short 5, keine Brille. robot_dance-2 verworfen: gleiche Haltung wie Lexi (robot_dance-1).
Der Gerichtsvollzieher (GV, um 60, ohne Namen; Stimme helmut): standing/resting-2 (schwarzes Oberteil, Hose Grau #6B6B78),
Kopf Gray Short (helles graues Haar, Originalfarbe), Brille Glasses 2. Sachlich, keine Uniform, keine Abzeichen.
Frau Bergmann (BE, um 45, Konditorin, Gläubigerin; spricht nicht): standing/resting-1 (Oberteil Grün #8FD694, schwarze Hose),
Kopf Bun.
Posen nicht aus 147–150 (pointing_finger-2, easing-2, robot_dance-3, walking-3, blazer-4, crossed_arms-2, shirt-3, blazer-3);
keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Polka Dots, keine Bärte. Präfix MB_/GV_/BE_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Smile, Fear, Solemn bzw.
Concerned|Serious. Sprechende Ansichten (MB_redet, GV_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic, Schnitt bei 60 % der Gesichtshöhe."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_153")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MB": ("standing/easing-1", "Short 5", None, None, {"Skin": "#D9A07A", "Jacket": "#B8A9F5", "Top": "#FFFFFF",
                                                      "Pants": "#3A3A48"}),
    "GV": ("standing/resting-2", "Gray Short", None, "Glasses 2", {"Skin": "#E8B98F", "Pants": "#6B6B78"}),
    "BE": ("standing/resting-1", "Bun", None, None, {"Skin": "#F0C8A8", "Top": "#8FD694"}),
}

LISTE = [
    ("MB_ruhig", "MB", "Calm", 0), ("MB_redet", "MB", "Serious", 1), ("MB_denkt", "MB", "Suspicious", 0),
    ("MB_froh", "MB", "Smile", 0), ("MB_sorge", "MB", "Concerned|Serious", 0), ("MB_schreck", "MB", "Fear", 0),
    ("GV_ruhig", "GV", "Calm", 0), ("GV_redet", "GV", "Serious", 1), ("GV_denkt", "GV", "Suspicious", 0),
    ("GV_ernst", "GV", "Solemn", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_froh", "BE", "Smile", 0), ("BE_sorge", "BE", "Concerned|Serious", 0),
    ("BE_denkt", "BE", "Suspicious", 0),
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
