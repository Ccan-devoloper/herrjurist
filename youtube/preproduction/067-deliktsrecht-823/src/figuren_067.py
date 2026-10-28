"""Figuren für Folge 067 (§ 823 I BGB, Radfahrer auf dem Gehweg) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Martina (Fußgängerin, um 35): standing/walking-1 (geht, mit Brille „Glasses 2“), nach dem Sturz sitting/hands_back-2
(am Boden, ohne Brille – die Brille liegt zerbrochen daneben), danach standing/resting-1 (ohne Brille); alle mit lila
Oberteil und schwarzer Hose (Posenreihe mit farbigem Oberteil), Kopf Medium Bangs.
Stefan (Radfahrer, um 25): sitting/bike (fährt) und standing/easing-1 (steht), beide mit oranger Jacke und weißem Oberteil,
Kopf Short 3, kein Bart.
Erwin (Bäcker, um 65; Präfix EW_, weil bausteine.peep_voll „ER_“ dem Ordner op_we zuordnet): nur standing/crossed_arms-1 (weißes Oberteil, schwarze Hose), Kopf No Hair 2, kein Bart.
Keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der
Tafel), Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF); offene Mimiken nur als
„Augen|Serious/Smile“. Je sprechender Ansicht vier Mundzustände: zu (Grundmimik), a, o, e (lexpeeps 'Augen|Mund',
Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_067")
os.makedirs(ZIEL, exist_ok=True)
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

MT_F = {"Skin": "#F0C8A8", "Top": "#B8A9F5"}
ST_F = {"Skin": "#D9A27A", "Jacket": "#F9A66C", "Top": "#FFFFFF", "Bicycle Frame": "#8DB3F2"}
EW_F = {"Skin": "#E8B894", "Top": "#FFFFFF"}
# Ansicht: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "MT_g": ("standing/walking-1", "Medium Bangs", None, "Glasses 2", MT_F),
    "MT_b": ("sitting/hands_back-2", "Medium Bangs", None, None, MT_F),
    "MT_s": ("standing/resting-1", "Medium Bangs", None, None, MT_F),
    "ST_r": ("sitting/bike", "Short 3", None, None, ST_F),
    "ST_s": ("standing/easing-1", "Short 3", None, None, ST_F),
    "EW_s": ("standing/crossed_arms-1", "No Hair 2", None, None, EW_F),
}

# (Name, Ansicht, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts).
LISTE = [
    ("MT_geht", "MT_g", "Calm", 0), ("MT_schreck", "MT_g", "Fear", 0),
    ("MT_boden", "MT_b", "Concerned|Serious", 0), ("MT_boden_redet", "MT_b", "Concerned|Serious", 1),
    ("MT_ruhig", "MT_s", "Calm", 0), ("MT_denkt", "MT_s", "Suspicious", 0), ("MT_froh", "MT_s", "Smile", 0),
    ("MT_sorge", "MT_s", "Concerned|Serious", 0), ("MT_ernst", "MT_s", "Serious", 0),
    ("ST_faehrt", "ST_r", "Driven", 0), ("ST_rad_schreck", "ST_r", "Fear", 0),
    ("ST_redet", "ST_s", "Very Angry", 1), ("ST_ruhig", "ST_s", "Calm", 0), ("ST_denkt", "ST_s", "Suspicious", 0),
    ("ST_sorge", "ST_s", "Concerned|Serious", 0), ("ST_ertappt", "ST_s", "Fear", 0),
    ("EW_ruhig", "EW_s", "Calm", 0), ("EW_schaut", "EW_s", "Suspicious", 0), ("EW_redet", "EW_s", "Serious", 1),
    ("EW_froh", "EW_s", "Smile", 0),
]

if __name__ == "__main__":
    n = 0
    for name, v, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[v]
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
