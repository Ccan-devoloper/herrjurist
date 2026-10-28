"""Figuren für Folge 248 (Gesellschafterhaftung GbR, Architekturbüro) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Philipp (PH, um 35, Architekt, Gesellschafter; Stimme niklas): standing/blazer-3 (Sakko Petrol #3E6E8E, schwarzes Shirt
der Pose, Hose Hellgrau #C9CCD3), Kopf Short 4, Haut #E2AE88, kein Bart, keine Brille.
Alma (AL, um 28, Architektin, tritt im März ein; Stimme ela_froh): standing/pointing_finger-2 (schwarzes Oberteil der Pose,
Hose Grün #8FD694), Kopf Long Curly, Haut #C68E6A.
Mathilde (MA, um 63, Architektin, scheidet Ende April aus; spricht nicht): standing/blazer-4 (Blazer Lila #B8A9F5, Oberteil
Weiß, schwarze Hose der Pose), Kopf Gray Medium (Haar Grau #CFCFCF), Brille Glasses 3, Haut #F0C8A8.
Herr Altmann (AT, um 65, Tischler, Gläubiger; Stimme helmut): standing/crossed_arms-1 (Pullover Sand #C9A46A, schwarze
Hose der Pose), Kopf No Hair 2 (Glatze mit wenig Haar), Brille Glasses, Haut #EBC29E – bestimmt, aber sachlich, keine Karikatur.
Posen nicht aus den letzten drei Folgen 245–247 (shirt-4, shirt-3, resting-2, crossed_arms-2, easing-1, walking-1);
keine Polka Dots, keine Prothesen-Posen (blazer-1, blazer-2, shirt-1, shirt-2 verworfen), keine Bärte. Lexi nach lexi.py.
Präfix PH_/AL_/MA_/AT_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (PH_redet, AL_redet, AT_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_248")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "PH": ("standing/blazer-3", "Short 4", None, None, {"Skin": "#E2AE88", "Jacket": "#3E6E8E", "Pants": "#C9CCD3"}),
    "AL": ("standing/pointing_finger-2", "Long Curly", None, None, {"Skin": "#C68E6A", "Pants": "#8FD694"}),
    "MA": ("standing/blazer-4", "Gray Medium", None, "Glasses 3", {"Skin": "#F0C8A8", "Jacket": "#B8A9F5", "Top": "#FFFFFF", "Hair": "#CFCFCF"}),
    "AT": ("standing/crossed_arms-1", "No Hair 2", None, "Glasses", {"Skin": "#EBC29E", "Top": "#C9A46A"}),
}

LISTE = [
    ("PH_ruhig", "PH", "Calm", 0), ("PH_redet", "PH", "Concerned|Serious", 1), ("PH_froh", "PH", "Smile", 0),
    ("PH_denkt", "PH", "Suspicious", 0), ("PH_ernst", "PH", "Serious", 0), ("PH_sorge", "PH", "Concerned|Serious", 0),
    ("PH_staunt", "PH", "Awe", 0), ("PH_strahlt", "PH", "Smile Big|Smile", 0),
    ("AL_ruhig", "AL", "Calm", 0), ("AL_redet", "AL", "Smile Big|Smile", 1), ("AL_froh", "AL", "Smile", 0),
    ("AL_strahlt", "AL", "Smile Big|Smile", 0), ("AL_denkt", "AL", "Suspicious", 0), ("AL_staunt", "AL", "Awe", 0),
    ("AL_ernst", "AL", "Serious", 0), ("AL_sorge", "AL", "Concerned|Serious", 0),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_froh", "MA", "Smile", 0), ("MA_denkt", "MA", "Suspicious", 0),
    ("MA_ernst", "MA", "Serious", 0), ("MA_staunt", "MA", "Awe", 0),
    ("AT_ruhig", "AT", "Calm", 0), ("AT_redet", "AT", "Serious", 1), ("AT_ernst", "AT", "Serious", 0),
    ("AT_denkt", "AT", "Suspicious", 0), ("AT_froh", "AT", "Smile", 0), ("AT_staunt", "AT", "Awe", 0),
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
