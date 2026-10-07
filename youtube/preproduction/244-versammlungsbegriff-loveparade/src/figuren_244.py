"""Figuren für Folge 244 (Versammlungsbegriff: Ist die Love Parade eine Demo?) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv; kein echter Veranstalter, keine Marken, keine Drogen- oder Alkoholklischees.
Herr Brendel (BR, um 30, Veranstalter des Sound-Umzugs; Stimme niklas): standing/robot_dance-3 (Pullover Koralle #F07A6A,
  Hose Anthrazit #3D3D48), Kopf Pomp, Haut #E9B994, kein Bart.
Herr Zander (ZA, um 60, Mitarbeiter der Stadt, Straßenbehörde; Stimme helmut): standing/crossed_arms-1 (Pullover Tannengrün
  #4F7A63, schwarze Hose der Pose), Kopf No Hair 1, Brille Glasses, Haut #F0C8A8 – sachlich.
Frau Lechner (LE, um 30, Organisatorin des Umzugs gegen die Schließung des Jugendzentrums – Gegenfall; Stimme ela_froh):
  standing/resting-1 (Oberteil Hellblau #8DB3F2), Kopf Long Bangs, Haut #C68E6A.
Nebenfiguren ohne Namen und ohne Stimme (Mund immer zu): Tänzerin TA (standing/robot_dance-2, Hose Hellblau, Kopf Bun,
  Haut #F2D0B5), Tänzer TB (standing/polka_dots, Oberteil Grün #8FD694, Hose #3A4A6B, Kopf Afro, Haut #8D5A3B),
  Teilnehmer TC im Gegenfall (standing/walking-3, Kopf Medium 1, Haut #D9A47E), hält das Transparent.
Posen der Hauptfiguren nicht aus 239–243 (dort resting-2, shirt-4, easing-1, walking-1, shirt-3, easing-2, crossed_arms-2,
blazer-4, walking-2, blazer-3, pointing_finger-1/-2, blazer-2, shirt-1, walking-3, robot_dance-2); robot_dance-2 und walking-3
nur für namenlose Nebenfiguren in anderen Farben. Keine Prothesen-Posen, keine Bärte; Polka Dots nur bei einer Nebenfigur
(in 239–243 nicht verwendet). Präfixe BR_/ZA_/LE_/TA_/TB_/TC_ (nie ER_). Alle Posen blicken im Original nach rechts; die
Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (BR_redet, ZA_spricht, LE_spricht, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_244")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "BR": ("standing/robot_dance-3", "Pomp", None, None, {"Skin": "#E9B994", "Top": "#F07A6A", "Pants": "#3D3D48"}),
    "ZA": ("standing/crossed_arms-1", "No Hair 1", None, "Glasses", {"Skin": "#F0C8A8", "Top": "#4F7A63"}),
    "LE": ("standing/resting-1", "Long Bangs", None, None, {"Skin": "#C68E6A", "Top": "#8DB3F2"}),
    "TA": ("standing/robot_dance-2", "Bun", None, None, {"Skin": "#F2D0B5", "Pants": "#8DB3F2"}),
    "TB": ("standing/polka_dots", "Afro", None, None, {"Skin": "#8D5A3B", "Top": "#8FD694", "Pants": "#3A4A6B"}),
    "TC": ("standing/walking-3", "Medium 1", None, None, {"Skin": "#D9A47E"}),
}

LISTE = [
    ("BR_ruhig", "BR", "Calm", 0), ("BR_froh", "BR", "Smile", 0), ("BR_freut", "BR", "Smile Big|Smile", 0),
    ("BR_entschl", "BR", "Driven", 0), ("BR_denkt", "BR", "Suspicious", 0), ("BR_sorge", "BR", "Concerned|Serious", 0),
    ("BR_ernst", "BR", "Serious", 0), ("BR_muede", "BR", "Tired", 0), ("BR_schreck", "BR", "Awe", 0),
    ("BR_redet", "BR", "Driven", 1),
    ("ZA_ruhig", "ZA", "Calm", 0), ("ZA_ernst", "ZA", "Serious", 0), ("ZA_streng", "ZA", "Solemn", 0),
    ("ZA_denkt", "ZA", "Suspicious", 0), ("ZA_froh", "ZA", "Smile", 0),
    ("ZA_spricht", "ZA", "Serious", 1),
    ("LE_froh", "LE", "Smile", 0), ("LE_ruhig", "LE", "Calm", 0), ("LE_entschl", "LE", "Driven", 0),
    ("LE_freut", "LE", "Smile Big|Smile", 0),
    ("LE_spricht", "LE", "Smile", 1),
    ("TA_froh", "TA", "Smile", 0), ("TA_cute", "TA", "Cute", 0),
    ("TB_froh", "TB", "Smile", 0), ("TB_cute", "TB", "Cute", 0),
    ("TC_froh", "TC", "Smile", 0), ("TC_entschl", "TC", "Driven", 0),
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
