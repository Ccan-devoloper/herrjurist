"""Figuren für Folge 275 (Zusammengesetzte Urkunde: das vertauschte Preisschild im Baumarkt) aus der LexVerse-Figma-
Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Karlheinz (KH, um 60, Kunde im Baumarkt; Stimme helmut): standing/shirt-3 (Hemd Senfgelb #E8C25A, schwarze Hose der Pose,
  helle Schuhe), Kopf Gray Short (Haar Grau #B9B9C2), Haut #EDC3A3, keine Brille, kein Bart; gewöhnlicher Kunde, keine
  „fiese“ Täterfigur.
Frau Gundlach (GU, um 30, Kassiererin; Stimme ela_froh): standing/robot_dance-2 (offene Hand: „bitte“; schwarzes
  Oberteil der Pose, Hose Rot #F07A6A, weiße Schuhe), Kopf Medium 3 (dunkles Haar, nicht einfärbbar), Haut #D9A27A, keine
  Brille. Verworfen: pointing_finger-1 (Oberteil und Hose nicht getrennt einfärbbar, Figur wirkte als schwarze Fläche).
Posen der letzten Folgen nicht verwendet (271: resting-1, easing-1; 272: robot_dance-3, crossed_arms-1, blazer-3;
273: crossed_arms-2, shirt-4; 274: easing-2, resting-2). robot_dance-1 bleibt Lexi; keine Polka Dots, keine
Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe KH_/GU_ (nie ER_). Beide Posen blicken im
Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Smile, Suspicious, Serious, Driven, Awe bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten KH_redet, GU_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_275")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "KH": ("standing/shirt-3", "Gray Short", None, None, {"Skin": "#EDC3A3", "Top": "#E8C25A", "Hair": "#B9B9C2"}),
    "GU": ("standing/robot_dance-2", "Medium 3", None, None, {"Skin": "#D9A27A", "Pants": "#F07A6A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("KH_ruhig", "KH", "Calm", 0), ("KH_froh", "KH", "Smile", 0), ("KH_denkt", "KH", "Suspicious", 0),
    ("KH_ernst", "KH", "Serious", 0), ("KH_sorge", "KH", "Concerned|Serious", 0), ("KH_eifrig", "KH", "Driven", 0),
    ("KH_redet", "KH", "Smile", 1),
    ("GU_ruhig", "GU", "Calm", 0), ("GU_froh", "GU", "Smile", 0), ("GU_denkt", "GU", "Suspicious", 0),
    ("GU_ernst", "GU", "Serious", 0), ("GU_staunt", "GU", "Awe", 0),
    ("GU_redet", "GU", "Smile", 1),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    nur = sys.argv[1:]          # optional: nur diese Namen (Probe)
    n = 0
    for name, p, mimik, mund in LISTE:
        if nur and name not in nur:
            continue
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    if not nur:
        # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
        for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
            a = LX.AUSSEHEN
            for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
                figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
