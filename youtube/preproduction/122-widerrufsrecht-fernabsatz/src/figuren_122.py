"""Figuren für Folge 122 (Widerrufsrecht Fernabsatz, getragene Sneaker) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Ilka (um 30, Verbraucherin, Käuferin): standing/walking-1 (geht – passt zum Nachmittag im Park; Shirt Lila #B8A9F5, schwarze
Hose, weiße Turnschuhe), Kopf Long (schwarz, glatt), Haut #E0AC86, keine Brille. Stimme sabrina.
Herr Riemann (um 55, Inhaber des Onlineshops, Unternehmer): standing/resting-2 (schwarzer Pullover, Hose Grau #5B5F66,
schwarze Schuhe), Kopf Short 2, Brille Glasses, Haut #C98F6B, kein Bart. Stimme william.
Abwechslung: Posen nicht aus 118–121 (robot_dance-3, resting-1, crossed_arms-1/-2, easing-2, blazer-3/-4,
pointing_finger-1, walking-2/-3, polka_dots, shirt-3) und nicht wie das Online-Shop-Personal in 116 (easing-1,
robot_dance-2; Ottmar Halbglatze, Brille, blaue Hose) bzw. 117 (shirt-4, pointing_finger-2). walking-1 zuletzt 112,
resting-2 zuletzt 115 (dort andere Figur). Keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur.
Präfix IL_/RI_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links,
Suffix _r blickt nach rechts. Grundmimik immer mit geschlossenem Mund (Calm, Serious, Smile, Suspicious, Awe, Tired bzw.
„Augen|geschlossener Mund“). Sprechende Ansichten (IL_redet, IL_bestimmt, RI_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_122")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "IL": ("standing/walking-1", "Long", None, None, {"Skin": "#E0AC86", "Top": "#B8A9F5"}),
    "RI": ("standing/resting-2", "Short 2", None, "Glasses", {"Skin": "#C98F6B", "Pants": "#5B5F66"}),
}

LISTE = [
    ("IL_ruhig", "IL", "Calm", 0), ("IL_froh", "IL", "Smile Big|Smile", 0), ("IL_redet", "IL", "Smile", 1),
    ("IL_bestimmt", "IL", "Serious", 1), ("IL_denkt", "IL", "Suspicious", 0), ("IL_sorge", "IL", "Concerned|Serious", 0),
    ("IL_muede", "IL", "Tired", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_denkt", "RI", "Suspicious", 0),
    ("RI_staunt", "RI", "Awe", 0), ("RI_ernst", "RI", "Serious", 0), ("RI_froh", "RI", "Smile", 0),
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
