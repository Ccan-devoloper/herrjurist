"""Figuren für Folge 129 (Mängelrechte Werkvertrag, undichtes Dach) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Beate (um 35, Hauseigentümerin, Bestellerin): standing/pointing_finger-2 (schwarzes Langarmoberteil der Pose, Hose Lila
#B8A9F5, schwarze Schuhe), Kopf Long (schwarzes langes Haar), Haut #F2C9A5, keine Brille. Stimme ela_froh.
Herr Wenzel (um 60, Dachdecker, Unternehmer): standing/shirt-4 (schwarzes Hemd der Pose, Arbeitshose Grau #5B5F66, weiße
Schuhe), Kopf No Hair 3 (Glatze mit weißem Haarkranz), Haut #E0A57E, kein Bart, keine Brille. Stimme helmut.
(hat-beanie verworfen: die Mütze liegt in der Hautfläche und würde hautfarben.)
Abwechslung: Posen nicht aus 126–128 (blazer-1, shirt-3, walking-1, blazer-4, blazer-2, crossed_arms-2, easing-1,
resting-2); keine Polka Dots, keine Bärte, keine Prothesen-Posen (shirt-1/-2 verworfen), keine Karikatur.
Präfix BE_/WE_ (nie ER_). Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts (Kopfprobe am
Kontaktbild). Grundmimik immer mit geschlossenem Mund (Calm, Serious, Smile, Suspicious, Awe bzw. „Augen|geschlossener
Mund“). Sprechende Ansichten (BE_redet, WE_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining /
Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_129")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "BE": ("standing/pointing_finger-2", "Long", None, None, {"Skin": "#F2C9A5", "Pants": "#B8A9F5"}),
    "WE": ("standing/shirt-4", "No Hair 3", None, None, {"Skin": "#E0A57E", "Pants": "#5B5F66"}),
}

LISTE = [
    ("BE_ruhig", "BE", "Calm", 0), ("BE_froh", "BE", "Smile Big|Smile", 0), ("BE_redet", "BE", "Concerned|Serious", 1),
    ("BE_sorge", "BE", "Concerned|Serious", 0), ("BE_denkt", "BE", "Suspicious", 0), ("BE_staunt", "BE", "Awe", 0),
    ("BE_aerger", "BE", "Rage|Serious", 0), ("BE_zufrieden", "BE", "Smile", 0),
    ("WE_ruhig", "WE", "Calm", 0), ("WE_redet", "WE", "Smile", 1), ("WE_froh", "WE", "Smile Big|Smile", 0),
    ("WE_ernst", "WE", "Serious", 0), ("WE_denkt", "WE", "Suspicious", 0),
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
