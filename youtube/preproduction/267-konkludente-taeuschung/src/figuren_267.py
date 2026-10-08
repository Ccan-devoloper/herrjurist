"""Figuren für Folge 267 (Konkludente Täuschung beim Betrug) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Baldur (um 40, Restaurantgast; Stimme stephan): standing/robot_dance-3 (Oberteil Lila #B8A9F5, Hose Dunkelgrau #3D4A5C),
Kopf Flat Top, Haut #E6B08A – Alltagskleidung, ruhige Mimik, keine „fiese“ Täterfigur.
Kellnerin Kaja (um 25; Stimme lucy): standing/walking-3 (schwarzes Oberteil, schwarze Hose wie Servicekleidung), Kopf Long,
Haut #F3CDAE.
Ortrud (um 75, Privatperson; Stimme hilde): standing/polka_dots (gepunktete Bluse, Hose Hellblau #8DB3F2), Kopf Gray Bun,
Brille Glasses, Haut #F1CCAE.
Herr Weinert (um 50, betreibt ein Internetportal; Stimme christian): standing/easing-2 (Hemdjacke Graublau #7FA0C8 über
schwarzem Shirt, Hose Dunkelgrau #4A5260), Kopf Short 5, Haut #DFAE88 – gewöhnlicher Geschäftsmann, kein Klischee.
Keine Bärte, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2). Posen nicht aus den letzten drei Folgen 263, 264, 266
(easing-1, shirt-3, shirt-4, resting-1, blazer-2, blazer-4, robot_dance-2, crossed_arms-1, crossed_arms-2); Polka Dots
zuletzt vor 263. Lexi bleibt robot_dance-1. Präfix BA_/KJ_/OD_/WN_ (nie ER_). Alle Posen blicken im Original nach rechts;
die Grundansicht ist gespiegelt und blickt nach links (Figur rechts neben der Tafel), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (BA_redet, BA_redet2, KJ_redet, OD_redet,
WN_redet, Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_267")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "BA": ("standing/robot_dance-3", "Flat Top", None, None, {"Skin": "#E6B08A", "Top": "#B8A9F5", "Pants": "#3D4A5C"}),
    "KJ": ("standing/walking-3", "Long", None, None, {"Skin": "#F3CDAE"}),
    "OD": ("standing/polka_dots", "Gray Bun", None, "Glasses", {"Skin": "#F1CCAE", "Pants": "#8DB3F2"}),
    "WN": ("standing/easing-2", "Short 5", None, None, {"Skin": "#DFAE88", "Jacket": "#7FA0C8", "Pants": "#4A5260"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("BA_ruhig", "BA", "Calm", 0), ("BA_redet", "BA", "Smile", 1), ("BA_redet2", "BA", "Concerned|Serious", 1),
    ("BA_froh", "BA", "Smile", 0), ("BA_isst", "BA", "Eating Happy", 0), ("BA_denkt", "BA", "Suspicious", 0),
    ("BA_sorge", "BA", "Concerned|Serious", 0), ("BA_ernst", "BA", "Serious", 0), ("BA_still", "BA", "Solemn", 0),
    ("KJ_ruhig", "KJ", "Calm", 0), ("KJ_redet", "KJ", "Smile", 1), ("KJ_froh", "KJ", "Smile", 0),
    ("KJ_staunt", "KJ", "Awe", 0), ("KJ_ernst", "KJ", "Serious", 0), ("KJ_sorge", "KJ", "Concerned|Serious", 0),
    ("OD_ruhig", "OD", "Calm", 0), ("OD_redet", "OD", "Smile", 1), ("OD_froh", "OD", "Smile", 0),
    ("OD_liest", "OD", "Suspicious", 0), ("OD_staunt", "OD", "Awe", 0), ("OD_sorge", "OD", "Concerned|Serious", 0),
    ("OD_ernst", "OD", "Serious", 0),
    ("WN_ruhig", "WN", "Calm", 0), ("WN_redet", "WN", "Calm", 1), ("WN_denkt", "WN", "Suspicious", 0),
    ("WN_ernst", "WN", "Serious", 0), ("WN_still", "WN", "Solemn", 0), ("WN_froh", "WN", "Smile", 0),
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
