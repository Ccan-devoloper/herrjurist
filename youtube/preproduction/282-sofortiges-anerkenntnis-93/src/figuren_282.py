"""Figuren für Folge 282 (Sofortiges Anerkenntnis § 93 ZPO: Gartenbau Fink gegen Frau Mehlhorn) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv, keine realen Personen; die Gartenbau Fink GmbH ist erfunden.
Frau Mehlhorn (ME, um 35, Kundin und Beklagte; Stimme julia): standing/easing-1 (Jacke Koralle #F07A6A, Oberteil Weiß, schwarze
  Hose der Pose, Hände locker = sympathisch, unaufgeregt), Kopf Long Curly (schwarzes Haar), Haut #F1C9A5.
Herr Rosenbaum (RO, um 35, Rechtsanwalt, Beklagtenvertreter; Stimme niklas): standing/blazer-3 (Blazer Marine #44557A, Hose
  #2E3440, Hand an der Hüfte), Kopf Short 2, Haut #B07552. Keine Brille, kein Bart.
Herr Fink (FI, um 60, Inhaber der Gartenbau Fink GmbH; Stimme helmut): standing/crossed_arms-2 (schwarzes Oberteil der Pose,
  Arbeitshose Moosgrün #6B8F71; verschränkte Arme = ungeduldig, nicht feindselig), Kopf No Hair 3 (Haarkranz Grau #A8A8A8),
  Haut #EDC3A0. Kein Bart.
Keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Polka Dots; keine Pose der letzten drei Folgen 279/280/281
(robot_dance-3, sitting/mid-2, blazer-4, resting-1, shirt-3, resting-2, shirt-4) und nicht robot_dance-1 (Lexi).
Präfix ME_/RO_/FI_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links (Figur rechts), Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Driven bzw. „Augen|geschlossener
Mund“ (Concerned|Serious). Sprechende Ansichten zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear /
Hectic (Schnitt bei 60 % der Gesichtshöhe)."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_282")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "ME": ("standing/easing-1", "Long Curly", None, None, {"Skin": "#F1C9A5", "Jacket": "#F07A6A",
                                                         "Top": "#FFFFFF"}),
    "RO": ("standing/blazer-3", "Short 2", None, None, {"Skin": "#B07552", "Jacket": "#44557A", "Pants": "#2E3440"}),
    "FI": ("standing/crossed_arms-2", "No Hair 3", None, None, {"Skin": "#EDC3A0", "Hair": "#A8A8A8", "Pants": "#6B8F71"}),
}

LISTE = [
    ("ME_ruhig", "ME", "Calm", 0), ("ME_sorge", "ME", "Concerned|Serious", 0), ("ME_denkt", "ME", "Suspicious", 0),
    ("ME_froh", "ME", "Smile", 0), ("ME_ernst", "ME", "Serious", 0),
    ("ME_redet", "ME", "Concerned|Serious", 1), ("ME_redetfest", "ME", "Serious", 1),
    ("RO_ruhig", "RO", "Calm", 0), ("RO_denkt", "RO", "Suspicious", 0), ("RO_froh", "RO", "Smile", 0),
    ("RO_ernst", "RO", "Serious", 0),
    ("RO_redet", "RO", "Serious", 1), ("RO_redetfroh", "RO", "Smile", 1),
    ("FI_ruhig", "FI", "Calm", 0), ("FI_eilig", "FI", "Driven", 0), ("FI_denkt", "FI", "Suspicious", 0),
    ("FI_redet", "FI", "Driven", 1),
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
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
