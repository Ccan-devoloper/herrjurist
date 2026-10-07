"""Figuren für Folge 241 (Strauß-Karikatur) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv;
die reale Person (der damalige bayerische Ministerpräsident) und der reale Zeichner werden NICHT dargestellt.
Meinrad (ME, um 45, Karikaturist; Stimme christian): standing/easing-2 (offene Jacke Lila #B8A9F5 über schwarzem Shirt,
Hose Grau #6B6B78), Kopf Short 4, Haut #E2B48E, kein Bart, keine Brille.
Henriette (HE, um 30, Redakteurin des Satiremagazins; Stimme lucy): standing/crossed_arms-2 (schwarzes Oberteil, Hose
Grün #8FD694), Kopf Long Curly, Haut #F0C8A8.
Ministerpräsidentin Achenbach (AC, um 60; Stimme hilde): standing/blazer-4 (Blazer Blau #8DB3F2, Oberteil Weiß),
Kopf Gray Bun, Brille Glasses 3, Haut #EDC3A3.
Posen nicht aus den letzten drei Folgen 238–240 (crossed_arms-1, resting-1, robot_dance-2/-3, walking-1, easing-1,
resting-2, shirt-3, shirt-4); keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 verworfen), keine Polka Dots, keine Bärte.
Präfix ME_/HE_/AC_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (ME_redet, HE_redet, AC_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_241")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "ME": ("standing/easing-2", "Short 4", None, None, {"Skin": "#E2B48E", "Jacket": "#B8A9F5", "Pants": "#6B6B78"}),
    "HE": ("standing/crossed_arms-2", "Long Curly", None, None, {"Skin": "#F0C8A8", "Pants": "#8FD694"}),
    "AC": ("standing/blazer-4", "Gray Bun", None, "Glasses 3", {"Skin": "#EDC3A3", "Jacket": "#8DB3F2", "Top": "#FFFFFF"}),
}

LISTE = [
    ("ME_ruhig", "ME", "Smile", 0), ("ME_redet", "ME", "Serious", 1), ("ME_zeichnet", "ME", "Driven", 0),
    ("ME_froh", "ME", "Cute", 0), ("ME_sorge", "ME", "Concerned|Serious", 0), ("ME_ernst", "ME", "Serious", 0),
    ("ME_denkt", "ME", "Suspicious", 0),
    ("HE_ruhig", "HE", "Smile", 0), ("HE_redet", "HE", "Smile", 1), ("HE_froh", "HE", "Cute", 0),
    ("HE_denkt", "HE", "Suspicious", 0), ("HE_ernst", "HE", "Serious", 0),
    ("AC_ruhig", "AC", "Calm", 0), ("AC_redet", "AC", "Serious", 1), ("AC_aerger", "AC", "Rage|Serious", 0),
    ("AC_ernst", "AC", "Solemn", 0), ("AC_denkt", "AC", "Suspicious", 0), ("AC_froh", "AC", "Smile", 0),
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
