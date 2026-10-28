"""Figuren für Folge 162 (Analogie) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Ilona (IL, um 30, wird von ihrem Nachbarn beleidigt, Klägerin; Stimme lucy): standing/easing-1 (offenes Hemd Pink #F6A5C0,
Oberteil Weiß, schwarze Hose), Kopf Long Bangs (schwarzes Haar; Hose und Haar sind in Pose/Kopf nicht umfärbbar), Haut #F1C9A5,
keine Brille.
Bertold (BE, um 45, Nachbar, Beklagter; Stimme christian): standing/blazer-4 (Sakko Ocker #C9A27A, Oberteil Weiß,
schwarze Hose), Kopf Short 5, Haut #E2B48E, kein Bart. Ruhige Mimik, keine Karikatur, keine Drohgebärde.
Richterin (RI, um 60, ohne Namen; Stimme hilde): sitting/closed_legs-1 (Jacke Schwarz #2B2B33 als Robe, Oberteil Weiß),
Kopf Gray Bun, Brille Glasses 4, Haut #EFC6A6; sitzt in beiden Gerichtsszenen hinter dem Richtertisch, der sie ab der
Schulter verdeckt (pointing_finger-1 und walking-3 verworfen: Kleidung dort nicht umfärbbar, ganz schwarz).
Posen nicht aus den letzten drei Folgen (159: robot_dance-3, crossed_arms-1; 160: crossed_arms-1, sitting/closed_legs-2,
resting-1; 161: blazer-3, resting-1, crossed_arms-1, crossed_arms-2); robot_dance-1 bleibt Lexi; keine Polka Dots, keine
Prothesen-Posen (shirt-1/-2, blazer-1/-2 ausgeschlossen), keine Bärte.
Präfix IL_/BE_/RI_ (nie ER_). Blickrichtung im Kontaktbild geprüft (besetzung_162.png): Grundansicht gespiegelt, Suffix _r
ungespiegelt; welche Seite das Gesicht zeigt, steht in SZENENPLAN.md.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (IL_redet, BE_redet, RI_redet, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_162")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "IL": ("standing/easing-1", "Long Bangs", None, None,
           {"Skin": "#F1C9A5", "Jacket": "#F6A5C0", "Top": "#FFFFFF", "Pants": "#3B3B4F", "Hair": "#7A4A2A"}),
    "BE": ("standing/blazer-4", "Short 5", None, None, {"Skin": "#E2B48E", "Jacket": "#C9A27A", "Top": "#FFFFFF"}),
    "RI": ("sitting/closed_legs-1", "Gray Bun", None, "Glasses 4", {"Skin": "#EFC6A6", "Jacket": "#2B2B33", "Top": "#FFFFFF"}),
}

LISTE = [
    ("IL_ruhig", "IL", "Calm", 0), ("IL_redet", "IL", "Serious", 1), ("IL_sorge", "IL", "Concerned|Serious", 0),
    ("IL_denkt", "IL", "Suspicious", 0), ("IL_froh", "IL", "Smile", 0), ("IL_strahlt", "IL", "Smile Big|Smile", 0),
    ("IL_traurig", "IL", "Tired", 0),
    ("BE_ruhig", "BE", "Calm", 0), ("BE_redet", "BE", "Serious", 1), ("BE_verachtet", "BE", "Contempt", 0),
    ("BE_denkt", "BE", "Suspicious", 0), ("BE_sorge", "BE", "Concerned|Serious", 0), ("BE_ernst", "BE", "Solemn", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_redet", "RI", "Serious", 1), ("RI_denkt", "RI", "Suspicious", 0),
    ("RI_froh", "RI", "Smile", 0),
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
