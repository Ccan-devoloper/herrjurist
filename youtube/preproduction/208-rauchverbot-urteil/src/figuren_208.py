"""Figuren für Folge 208 (Rauchverbot-Urteil) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv;
die realen Beschwerdeführer werden NICHT dargestellt. Keine Zigarette in der Hand, keine Tabakmarke.
Alfons (AL, um 55, Wirt einer Einraumkneipe; Stimme marc): standing/robot_dance-3 (einladende Geste; Oberteil Orange
#F9A66C, Hose Grau #5A5A66), Kopf No Hair 2, Haut #E8B48F, kein Bart – sympathisch, freundliche Mimiken.
Herr Stadler (SA, um 65, Stammgast; Stimme william): standing/walking-2 (schwarzes Shirt der Pose, Hose Blau #8DB3F2; er
geht ins große Lokal), Kopf Gray Short (Haar #9A9A9A), Brille Glasses 2, Haut #F0C8A8, kein Bart.
Frau Kaltenbach (KA, um 40, Betreiberin einer Großraumdiskothek ab 18; Stimme sabrina): standing/blazer-4 (Blazer Rosa
#F6A5C0, weißes Oberteil, schwarze Hose), Kopf Long Bangs (Haar #3A2A20), Haut #F1C9A5.
Posen nicht aus 203–205 (crossed_arms-1/-2, pointing_finger-2, easing-1/-2, shirt-3, resting-2) und nicht aus den parallel
entstehenden 206/207; keine Polka Dots, keine Bärte, keine Prothesen-Posen.
Präfix AL_/SA_/KA_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach
links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (AL_redet, SA_redet, KA_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_208")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "AL": ("standing/robot_dance-3", "No Hair 2", None, None, {"Skin": "#E8B48F", "Top": "#F9A66C", "Pants": "#5A5A66"}),
    "SA": ("standing/walking-2", "Gray Short", None, "Glasses 2", {"Skin": "#F0C8A8", "Pants": "#8DB3F2", "Hair": "#9A9A9A"}),
    "KA": ("standing/blazer-4", "Long Bangs", None, None, {"Skin": "#F1C9A5", "Jacket": "#F6A5C0", "Top": "#FFFFFF", "Hair": "#3A2A20"}),
}

LISTE = [
    ("AL_ruhig", "AL", "Smile", 0), ("AL_froh", "AL", "Cute", 0), ("AL_sorge", "AL", "Concerned|Serious", 0),
    ("AL_ernst", "AL", "Serious", 0), ("AL_denkt", "AL", "Suspicious", 0), ("AL_muede", "AL", "Tired", 0),
    ("AL_redet", "AL", "Concerned|Serious", 1),
    ("SA_ruhig", "SA", "Calm", 0), ("SA_redet", "SA", "Calm", 1), ("SA_froh", "SA", "Smile", 0),
    ("KA_ruhig", "KA", "Calm", 0), ("KA_redet", "KA", "Serious", 1), ("KA_ernst", "KA", "Serious", 0),
    ("KA_denkt", "KA", "Suspicious", 0), ("KA_froh", "KA", "Smile", 0), ("KA_sorge", "KA", "Concerned|Serious", 0),
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
