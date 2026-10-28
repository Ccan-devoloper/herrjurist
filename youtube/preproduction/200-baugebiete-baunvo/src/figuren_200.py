"""Figuren für Folge 200 (Baugebiete BauNVO: neue Siedlung mit Kita im Norden und Ladenlokal im Süden) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Frau Möhring (MO, um 35, gründet die Kita; Stimme lucy): standing/shirt-3 (Hemdbluse Rosé #F2A7C3, schwarze Hose),
  Kopf Long Curly (schwarzes Haar), Haut #E8B48F, keine Brille.
Herr Tiemann (TI, um 30, Tätowierer mit eigenem Studio; Stimme stephan): standing/resting-2 (schwarzer Pullover, Hose
  Blau #8DB3F2, Hände entspannt; robot_dance-3 verworfen, weil die Geste wie Lexi wirkt), Kopf Short 1, Haut #D9A47E, kein Bart, keine sichtbaren Tätowierungen (kein Klischee).
Zwei Kinder aus der Siedlung (KA, KB, um 5; sprechen nicht, ohne Namen): standing/walking-1 (T-Shirt Rot #F07A6A), Kopf
  Buns, Haut #F0C8A8; standing/walking-2 (schwarzes T-Shirt, Hose Grün #8FD694), Kopf Short 2, Haut #C58E64; Mimik Cute
  bzw. Smile; im Bild über `hoehe` auf etwa 58 % der Erwachsenenhöhe skaliert (Vorgabe 02.10.2026).
Posen der letzten drei Folgen (197: easing-1, blazer-1; 198: easing-1, resting-1; 199: easing-2, pointing_finger-1) und
von 196 (robot_dance-2, blazer-4, crossed_arms-2) nicht verwendet; robot_dance-1 bleibt Lexi; keine Polka Dots, keine
Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe MO_/TI_/KA_/KB_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Solemn, Suspicious, Serious, Cute bzw.
„Augen|geschlossener Mund“ (Smile Big|Smile, Concerned|Serious). Sprechende Ansichten MO_redet, TI_redet, TI_redet2 (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_200")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "MO": ("standing/shirt-3", "Long Curly", None, None, {"Skin": "#E8B48F", "Top": "#F2A7C3"}),
    "TI": ("standing/resting-2", "Short 1", None, None, {"Skin": "#D9A47E", "Pants": "#8DB3F2"}),
    "KA": ("standing/walking-1", "Buns", None, None, {"Skin": "#F0C8A8", "Top": "#F07A6A"}),
    "KB": ("standing/walking-2", "Short 2", None, None, {"Skin": "#C58E64", "Pants": "#8FD694"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("MO_ruhig", "MO", "Calm", 0), ("MO_froh", "MO", "Smile", 0), ("MO_stolz", "MO", "Smile Big|Smile", 0),
    ("MO_denkt", "MO", "Solemn", 0), ("MO_sorge", "MO", "Concerned|Serious", 0),
    ("MO_redet", "MO", "Smile Big|Smile", 1),
    ("TI_ruhig", "TI", "Calm", 0), ("TI_froh", "TI", "Smile", 0), ("TI_skeptisch", "TI", "Suspicious", 0),
    ("TI_sorge", "TI", "Concerned|Serious", 0), ("TI_ernst", "TI", "Serious", 0),
    ("TI_redet", "TI", "Calm", 1), ("TI_redet2", "TI", "Smile", 1),
    ("KA_froh", "KA", "Cute", 0), ("KB_froh", "KB", "Smile", 0),
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
