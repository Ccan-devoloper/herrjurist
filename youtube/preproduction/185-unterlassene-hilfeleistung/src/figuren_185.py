"""Figuren für Folge 185 (Unterlassene Hilfeleistung, Vorraum einer Bankfiliale) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv, keine realen Personen.
Älterer Mann (MA, um 80, Funktionsrolle ohne Namen, spricht nicht): standing/resting-2 (schwarzes Oberteil, Hose Grau
#9A9AA8), Kopf No Hair 3 (weißer Haarkranz), Haut #F0CDB4. Stehend Calm (vor dem Zusammenbruch) und Smile (erholt).
Liegend = dieselbe Figur mit Eyes Closed als Ganzes um 90° gedreht (nichts umgezeichnet); stabile Seitenlage =
sitting/closed_legs-2 (Jacke und Oberteil dunkel, Hose Grau #9A9AA8, gleiche Farben) um 90° gedreht, Eyes Closed.
Keine Verletzung, kein Blut.
Herr Brauer (BR, um 40, Stimme marc): standing/walking-1 (Shirt Grün #8FD694, schwarze Hose), Kopf Short 5, Haut #E8B48A.
Frau Hauser (HA, um 35, Stimme sabrina): standing/walking-2 (schwarzes Oberteil, Hose Lila #B8A9F5), Kopf Medium Bangs 2
(blond), Haut #F2C6A0.
Herr Kessel (KE, um 65, Stimme william): standing/crossed_arms-2 (schwarzes Oberteil, Hose Blau #8DB3F2), Kopf Gray Medium
(Haar grau #BDBDBD), Brille Glasses 2, Haut #EAC09C.
Frau Weigel (WE, um 55, spricht nicht): standing/shirt-4 (schwarzes Oberteil, Hose Orange #F9A66C), Kopf Medium 3,
Haut #C68E62.
Frau Bühler (BU, um 45, Stimme laura_ruhig, hilft): standing/robot_dance-2 und kniend sitting/mid-1 (je schwarzes
Oberteil, Hose Türkis #7FD6D0 – gleiches Outfit), Kopf Long, Haut #B97A56.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots. Posen nicht aus den letzten drei Folgen
182–184 (blazer-3, pointing_finger-2, resting-1, shirt-3, robot_dance-3, blazer-4, sitting/mid-2, blazer-1) und nicht
robot_dance-1 (Lexi). Präfix MA_/BR_/HA_/KE_/WE_/BU_ (nie ER_). Alle Posen blicken im Original nach rechts; die
Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (BR_redet, HA_redet, KE_redet,
BU_kniet_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_185")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "MA": ("standing/resting-2", "No Hair 3", None, None, {"Skin": "#F0CDB4", "Pants": "#9A9AA8"}),
    "MS": ("sitting/closed_legs-2", "No Hair 3", None, None, {"Skin": "#F0CDB4", "Pants": "#9A9AA8", "Top": "#3A3A44",
                                                            "Jacket": "#151515", "Shoes": "#151515"}),
    "BR": ("standing/walking-1", "Short 5", None, None, {"Skin": "#E8B48A", "Top": "#8FD694"}),
    "HA": ("standing/walking-2", "Medium Bangs 2", None, None, {"Skin": "#F2C6A0", "Pants": "#B8A9F5"}),
    "KE": ("standing/crossed_arms-2", "Gray Medium", None, "Glasses 2", {"Skin": "#EAC09C", "Pants": "#8DB3F2",
                                                                         "Hair": "#BDBDBD"}),
    "WE": ("standing/shirt-4", "Medium 3", None, None, {"Skin": "#C68E62", "Pants": "#F9A66C"}),
    "BU": ("standing/robot_dance-2", "Long", None, None, {"Skin": "#B97A56", "Pants": "#7FD6D0"}),
    "BK": ("sitting/mid-1", "Long", None, None, {"Skin": "#B97A56", "Pants": "#7FD6D0"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen, Drehung); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MA_steht", "MA", "Calm", 0, 0), ("MA_froh", "MA", "Smile", 0, 0),
    ("MA_liegt", "MA", "Eyes Closed", 0, 90), ("MA_seite", "MS", "Eyes Closed", 0, 90),
    ("BR_ruhig", "BR", "Calm", 0, 0), ("BR_redet", "BR", "Serious", 1, 0), ("BR_eilig", "BR", "Driven", 0, 0),
    ("BR_still", "BR", "Solemn", 0, 0),
    ("HA_ruhig", "HA", "Calm", 0, 0), ("HA_sorge", "HA", "Concerned|Serious", 0, 0), ("HA_redet", "HA", "Calm", 1, 0),
    ("HA_still", "HA", "Solemn", 0, 0),
    ("KE_ruhig", "KE", "Calm", 0, 0), ("KE_redet", "KE", "Suspicious", 1, 0), ("KE_denkt", "KE", "Suspicious", 0, 0),
    ("KE_still", "KE", "Solemn", 0, 0),
    ("WE_ruhig", "WE", "Calm", 0, 0), ("WE_sorge", "WE", "Concerned|Serious", 0, 0), ("WE_still", "WE", "Solemn", 0, 0),
    ("BU_ruhig", "BU", "Calm", 0, 0), ("BU_sorge", "BU", "Concerned|Serious", 0, 0), ("BU_froh", "BU", "Smile", 0, 0),
    ("BU_kniet", "BK", "Concerned|Serious", 0, 0), ("BU_kniet_redet", "BK", "Serious", 1, 0), ("BU_kniet_froh", "BK", "Smile", 0, 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund, dreh in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            def mach(gesicht):
                im = figur(pose, kopf, gesicht, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt))
                if dreh:   # liegend: Kopf zur Blickseite (Grundansicht: Kopf links), nur gedreht
                    im = im.rotate(dreh if gespiegelt else -dreh, expand=True)
                    im = im.crop(im.getbbox())
                return im
            mach(mimik).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    mach(f"{mimik.split('|')[0]}|{m}").save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
