"""Figuren für Folge 125 (Verbrauchsgüterkauf, gebrauchter Fernseher) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Dirk (um 40, Käufer, Verbraucher): standing/easing-2 (offenes Hemd Blau #8DB3F2 über schwarzem Shirt, Hose Grau #5B5F66,
Turnschuhe), Kopf Short 3, Haut #D9A47E, keine Brille, kein Bart. Stimme marc.
Frau Tillmann (um 55, Inhaberin eines Ladens für gebrauchte Elektrogeräte, Unternehmerin): standing/crossed_arms-1
(Pullover Rot #F07A6A, schwarze Hose, verschränkte Arme – passt zu „Gekauft wie gesehen“), Kopf Gray Medium (Haar grau #B9B4AE), Brille
Glasses 4, Haut #E6B994. Stimme laura_ruhig.
Abwechslung: Posen nicht aus 121–123 (polka_dots, shirt-3, walking-3, walking-1, resting-2, easing-1, blazer-3) und nicht
wie das Händlerpersonal der Kaufrechtsfolge 063 (shirt-3, blazer-4). easing-2 zuletzt 119 (Jacke grün, Hose gelb),
crossed_arms-1 zuletzt 120 (Oberteil blau). Keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur.
Präfix DI_/TI_ (nie ER_). Grundansicht gespiegelt (blickt nach links), Suffix _r blickt nach rechts (Kopfprobe am
Kontaktbild). Grundmimik immer mit geschlossenem Mund (Calm, Serious, Smile, Suspicious, Awe, Tired bzw.
„Augen|geschlossener Mund“). Sprechende Ansichten (DI_redet, TI_redet, Lexi) zusätzlich mit a/o/e: Augen der
Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_125")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "DI": ("standing/easing-2", "Short 3", None, None, {"Skin": "#D9A47E", "Jacket": "#8DB3F2", "Pants": "#5B5F66"}),
    "TI": ("standing/crossed_arms-1", "Gray Medium", None, "Glasses 4", {"Skin": "#E6B994", "Top": "#F07A6A", "Hair": "#B9B4AE"}),
}

LISTE = [
    ("DI_ruhig", "DI", "Calm", 0), ("DI_froh", "DI", "Smile Big|Smile", 0), ("DI_redet", "DI", "Concerned|Serious", 1),
    ("DI_denkt", "DI", "Suspicious", 0), ("DI_sorge", "DI", "Concerned|Serious", 0), ("DI_muede", "DI", "Tired", 0),
    ("TI_ruhig", "TI", "Calm", 0), ("TI_redet", "TI", "Serious", 1), ("TI_froh", "TI", "Smile", 0),
    ("TI_denkt", "TI", "Suspicious", 0), ("TI_ernst", "TI", "Serious", 0), ("TI_staunt", "TI", "Awe", 0),
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
