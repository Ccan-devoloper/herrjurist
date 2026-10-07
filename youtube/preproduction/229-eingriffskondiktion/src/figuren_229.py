"""Figuren für Folge 229 (Eingriffskondiktion, Foto in fremder Werbung) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv; die reale Person des Klassikers (Paul Dahlke) wird NICHT dargestellt. Die Firma „Brauselust“ ist erfunden.
Kai Möbius (KA, um 28; Stimme niklas): standing/robot_dance-3 (Pullover Grün #8FD694, Hose Dunkelgrau #4A4A55; offene Hand,
auf der im Park die Flasche steht – shirt-3 verworfen, Hände in den Taschen), Kopf Short 4 (Haar der Bibliothek), Haut #E8B894,
kein Bart.
Marketingleiter Wendorf (WE, um 58; Stimme helmut): standing/blazer-3 (Sakko Dunkelgrün #4E7D5B, schwarzes Shirt der Pose,
Hose Grau #5A5A66), Kopf No Hair 3 (Haarkranz Grau #9A9A9A; Gray Medium verworfen, wirkt rot und weiblich), Brille Glasses 3, Haut #EBC29E, kein Bart – sachlich, keine Karikatur.
Kollegin (KO, um 30; Stimme ela_froh, heiterer Satz): standing/easing-2 (Jacke Rot #F07A6A, Hose Blaugrau #3A4A6B), Kopf
Medium Bangs 2 (Haar #2B2B2B), Haut #B07552.
Fotograf (FO, stumm, nur im Rückblick): standing/walking-1 (Shirt Blau #8DB3F2), Kopf hat-beanie (Mütze Gelb #F9D56E),
Haut #D9A47E.
Posen nicht aus 226–228 (resting-1, blazer-4, crossed_arms-1/2, walking-2/3, blazer-2, easing-1, pointing_finger-1,
robot_dance-2, shirt-2, polka_dots, sitzend); keine Polka Dots, keine Prothesen-Posen (shirt-1 und blazer-1 deshalb verworfen),
keine Bärte.
Präfix KA_/WE_/KO_/FO_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (KA_redet, WE_redet, KO_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_229")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "KA": ("standing/robot_dance-3", "Short 4", None, None, {"Skin": "#E8B894", "Top": "#8FD694", "Pants": "#4A4A55"}),
    "WE": ("standing/blazer-3", "No Hair 3", None, "Glasses 3", {"Skin": "#EBC29E", "Jacket": "#4E7D5B", "Pants": "#5A5A66",
                                                          "Hair": "#9A9A9A"}),
    "KO": ("standing/easing-2", "Medium Bangs 2", None, None, {"Skin": "#B07552", "Jacket": "#F07A6A", "Pants": "#3A4A6B",
                                                               "Hair": "#2B2B2B"}),
    "FO": ("standing/walking-1", "hat-beanie", None, None, {"Skin": "#D9A47E", "Top": "#8DB3F2", "Hat": "#F9D56E"}),
}

LISTE = [
    ("KA_ruhig", "KA", "Calm", 0), ("KA_redet", "KA", "Serious", 1), ("KA_ernst", "KA", "Serious", 0),
    ("KA_staunt", "KA", "Awe", 0), ("KA_froh", "KA", "Smile", 0), ("KA_denkt", "KA", "Suspicious", 0),
    ("KA_sorge", "KA", "Concerned|Serious", 0), ("KA_trinkt", "KA", "Eating Happy", 0),
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Calm", 1), ("WE_froh", "WE", "Smile", 0),
    ("WE_denkt", "WE", "Suspicious", 0), ("WE_ernst", "WE", "Serious", 0), ("WE_sorge", "WE", "Concerned|Serious", 0),
    ("KO_ruhig", "KO", "Calm", 0), ("KO_redet", "KO", "Cute", 1), ("KO_froh", "KO", "Smile", 0), ("KO_staunt", "KO", "Awe", 0),
    ("FO_ruhig", "FO", "Driven", 0),
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
