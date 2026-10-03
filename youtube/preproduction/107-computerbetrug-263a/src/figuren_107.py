"""Figuren für Folge 107 (Computerbetrug § 263a, fremde Karte am Geldautomaten) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0).
Heiko (um 30, nimmt die Karte, hebt ab): standing/shirt-3 (Hemd Grün #8FD694, schwarze Hose der Pose), Kopf Short 2,
ohne Bart, Haut #E3B48E; gewöhnlicher Mitbewohner, keine Karikatur, keine Herkunfts- oder Hautfarbenzuschreibung, keine
„fiese“ Mimik, keine Prothesen-Pose.
Meike (um 30, Kontoinhaberin): standing/resting-2 (schwarzer Pullover der Pose, Hose Lila #B8A9F5), Kopf Medium Bangs,
Haut #F0C8A8.
Gedachte Bankangestellte (Funktionsrolle ohne Namen, spricht nicht): standing/blazer-3 (Blazer Blau #8DB3F2, Hose
#4A4A55), Kopf Medium 1, Brille Glasses 2, Haut #C68E62.
Alle Posen blicken im Original nach rechts: Grundansicht gespiegelt (blickt nach links, zur Tafel), Suffix _r blickt nach
rechts. Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Serious, Suspicious, Fear, Driven bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund
Explaining / Concerned Fear / Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_107")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

# Person: (Pose, Kopf, Bart, Brille, Farben)
P = {
    "HE": ("standing/shirt-3", "Short 2", None, None, {"Skin": "#E3B48E", "Top": "#8FD694"}),
    "MK": ("standing/resting-2", "Medium Bangs", None, None, {"Skin": "#F0C8A8", "Pants": "#B8A9F5"}),
    "BA": ("standing/blazer-3", "Medium 1", None, "Glasses 2", {"Skin": "#C68E62", "Jacket": "#8DB3F2", "Pants": "#4A4A55"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HE_ruhig", "HE", "Calm", 0), ("HE_redet", "HE", "Calm", 1), ("HE_denkt", "HE", "Suspicious", 0),
    ("HE_ernst", "HE", "Serious", 0), ("HE_froh", "HE", "Smile", 0), ("HE_sorge", "HE", "Concerned|Serious", 0),
    ("HE_eifrig", "HE", "Driven", 0),
    ("MK_ruhig", "MK", "Calm", 0), ("MK_redet", "MK", "Concerned|Serious", 1), ("MK_schreck", "MK", "Fear", 0),
    ("MK_ernst", "MK", "Serious", 0), ("MK_denkt", "MK", "Suspicious", 0), ("MK_froh", "MK", "Smile", 0),
    ("BA_ruhig", "BA", "Calm", 0), ("BA_denkt", "BA", "Suspicious", 0), ("BA_ernst", "BA", "Serious", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", True), ("_r", False)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=gespiegelt).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
