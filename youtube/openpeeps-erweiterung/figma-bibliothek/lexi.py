"""Lexi – feste Moderatorin von LexVerse (Stimme: Carla Blum). Aussehen in jedem Video identisch.

    python3 lexi.py AUSGABEORDNER      # rendert alle Posen/Mimiken als PNG (freigestellt, 1400 px hoch)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lexpeeps import figur

AUSSEHEN = dict(kopf="Bun 2", brille="Glasses 5", bart=None,
                farben={"Skin": "#C58E64", "Top": "#F9D56E", "bandana": "#F6A5C0"})   # Hautton am 30.09.2026 vom Kanalinhaber gewählt
# Nur Posen mit einfärbbarem Oberteil und schlanker Statur -> gleiches Outfit in jeder Szene
POSEN = {
    "ruhig":             ("standing/crossed_arms-1", "Calm"),
    "freut":             ("standing/crossed_arms-1", "Cute"),
    "nachdenklich":      ("standing/crossed_arms-1", "Serious"),
    "skeptisch":         ("standing/crossed_arms-1", "Suspicious"),
    "erklaert_zu":       ("standing/robot_dance-1", "Smile"),        # Mund zu  } Paar für Mundbewegung
    "erklaert_auf":      ("standing/robot_dance-1", "Explaining"),   # Mund auf }
    "warnt_zu":          ("standing/robot_dance-1", "Serious"),
    "warnt_auf":         ("standing/robot_dance-1", "Concerned Fear"),
    "kommt":             ("standing/walking-1", "Smile"),
}


def lexi(pose, hoehe=1400, spiegeln=False):
    p, gesicht = POSEN[pose]
    return figur(p, AUSSEHEN["kopf"], gesicht, AUSSEHEN["bart"], AUSSEHEN["brille"], farben=AUSSEHEN["farben"],
                 hoehe=hoehe, spiegeln=spiegeln)


if __name__ == "__main__":
    ziel = sys.argv[1]; os.makedirs(ziel, exist_ok=True)
    for name in POSEN:
        for sp in (0, 1):
            lexi(name, spiegeln=bool(sp)).save(os.path.join(ziel, f"LEXI_{name}{'_l' if sp else ''}.png"))
    print(len(POSEN) * 2, "Bilder ->", ziel)
