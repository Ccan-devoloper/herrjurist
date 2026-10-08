"""Figuren für Folge 256 (Retterfälle, BGHSt 39, 322) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Siegbert (SI, Anfang 60, Hauseigentümer, Brandstifter; spricht nicht): standing/easing-2 (Jacke Oliv #7E8C5A, Hose Grau
  #5C6370), Kopf No Hair 2, Haut #E8BC98, keine Brille, kein Bart – ruhig und unauffällig, keine fiese Täterfigur.
Arndt (AR, um 40, Nachbar, Retter; Stimme marc): standing/walking-3 (dunkles Shirt und Hose der Pose), Kopf Short 3,
  Haut #D9A47E, kein Bart – entschlossen und hilfsbereit (Driven, Calm, Serious), respektvoll gezeigt.
Liesbeth (LI, um 35, Mieterin, Mutter; Stimme sabrina): standing/resting-2 (Hose Blau #8DB3F2), Kopf Long Bangs, Haut
  #F2C9A6, keine Brille.
Zwei Kinder (K1 um 8, K2 um 6; ohne Namen, sprechen nicht): Vorgabe Koordinator „Kinder nur als Silhouetten in Sicherheit“ –
  echte Open-Peeps-Figuren (standing/walking-2 mit Kopf Buns, standing/crossed_arms-2 mit Kopf Short 2), danach als
  einfarbige Silhouette (Schiefergrau) eingefärbt; im Bild über `hoehe` auf etwa 62 bzw. 55 % der Erwachsenenhöhe.
Posen nicht aus 253–255 (crossed_arms-1, resting-1, shirt-3, walking-1, robot_dance-3, blazer-4, Blazer Black Tee) für die
Hauptfiguren; keine Prothesen-Posen (shirt-1, shirt-2, blazer-1, blazer-2), keine Polka Dots, keine Bärte.
Präfixe SI_/AR_/LI_/K1_/K2_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r blickt nach rechts (Kontaktbild out/richtung.png).
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (AR_redet, LI_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
import numpy as np
from PIL import Image
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_256")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
SILHOUETTE = (96, 108, 128)

P = {
    "SI": ("standing/easing-2", "No Hair 2", None, None, {"Skin": "#E8BC98", "Jacket": "#7E8C5A", "Pants": "#5C6370"}),
    "AR": ("standing/walking-3", "Short 3", None, None, {"Skin": "#D9A47E"}),
    "LI": ("standing/resting-2", "Long Bangs", None, None, {"Skin": "#F2C9A6", "Pants": "#8DB3F2"}),
    "K1": ("standing/walking-2", "Buns", None, None, {"Skin": "#F0C8A8"}),
    "K2": ("standing/crossed_arms-2", "Short 2", None, None, {"Skin": "#E3B48C"}),
}

LISTE = [
    ("SI_ruhig", "SI", "Calm", 0), ("SI_ernst", "SI", "Serious", 0), ("SI_denkt", "SI", "Suspicious", 0),
    ("SI_muede", "SI", "Tired", 0), ("SI_sorge", "SI", "Concerned|Serious", 0), ("SI_feierlich", "SI", "Solemn", 0),
    ("SI_staunt", "SI", "Awe", 0), ("SI_zu", "SI", "Eyes Closed", 0),
    ("AR_ruhig", "AR", "Calm", 0), ("AR_froh", "AR", "Smile", 0), ("AR_entschlossen", "AR", "Driven", 0),
    ("AR_sorge", "AR", "Concerned|Serious", 0), ("AR_redet", "AR", "Driven", 1),
    ("LI_ruhig", "LI", "Calm", 0), ("LI_froh", "LI", "Smile", 0), ("LI_angst", "LI", "Fear", 0),
    ("LI_schreck", "LI", "Awe", 0), ("LI_sorge", "LI", "Concerned|Serious", 0), ("LI_feierlich", "LI", "Solemn", 0),
    ("LI_redet", "LI", "Fear", 1),
    ("K1_kind", "K1", "Cute", 0), ("K2_kind", "K2", "Calm", 0),
]


def silhouette(im):
    a = np.asarray(im)[..., 3]
    out = np.zeros((*a.shape, 4), np.uint8)
    out[..., :3] = SILHOUETTE
    out[..., 3] = a
    return Image.fromarray(out)


if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    n = 0
    for name, p, mimik, mund in LISTE:
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            im = figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt))
            if p in ("K1", "K2"):
                im = silhouette(im)
            im.save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
