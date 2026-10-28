"""Figuren für Folge 234 (Fortsetzungsfeststellungsklage: Tenor und Feststellungsinteresse) aus der LexVerse-Figma-Bibliothek
(Open Peeps, CC0). Alle Figuren fiktiv, die Mahnwache neutral (Erhalt der Stadtbücherei, Schild ohne Parole).
Herr Strauch (ST, um 65, Veranstalter und Leiter der Mahnwache, Kläger; Stimme william): standing/crossed_arms-2 (schwarzer
  Pullover der Pose, Hose Khaki #9A7650), Kopf Gray Short, Brille Glasses 3, Haut #EDBE9C, kein Bart.
Polizeihauptkommissar Nagel (NA, um 45; Stimme marc): standing/shirt-3 (Diensthemd Mittelblau #4F6FA8, Hose Dunkelblau
  #26324F), Kopf Short 1, Haut #C99272 – sachlich, ruhig.
Richterin Bollmann (BO, um 50, Vorsitzende; Stimme sabrina): standing/blazer-3 (Robe Schwarz #262626 über schwarzem
  Oberteil der Pose, Hose #262626), Kopf Medium Straight (schwarzes Haar der Vorlage), Haut #E8C0A0.
Nebenfiguren ohne Namen und ohne Stimme (Mund immer zu): eine Teilnehmerin (TA, um 30): standing/easing-2 (Jacke Lila #B8A9F5,
  Hose Dunkelblau #3A4A6B), Kopf Long Curly, Haut #B98260, hält das Schild; ein Teilnehmer (TM, um 40): standing/resting-1
  (Oberteil Grün #8FD694, Hose #4A4A55), Kopf Short 4, Haut #8D5A3B.
Posen und Kleidung nicht aus 231–233 (robot_dance-3, walking-2, easing-1, blazer-4, pointing_finger-1, resting-2, sitting/bike,
crossed_arms-1, resting-1 nur für die Nebenfigur; 232 trägt resting-1 mit anderer Farbe); keine Prothesen-Posen
(shirt-1/-2, blazer-1/-2), keine Polka Dots, keine Bärte. Präfixe ST_/NA_/BO_/TA_/TM_ (nie ER_). Alle Posen blicken im
Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (ST_ruft, NA_spricht, BO_spricht, Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_234")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "ST": ("standing/crossed_arms-2", "Gray Short", None, "Glasses 3", {"Skin": "#EDBE9C", "Pants": "#9A7650"}),
    "NA": ("standing/shirt-3", "Short 1", None, None, {"Skin": "#C99272", "Top": "#4F6FA8", "Pants": "#26324F"}),
    "BO": ("standing/blazer-3", "Medium Straight", None, None, {"Skin": "#E8C0A0", "Jacket": "#262626", "Top": "#FFFFFF",
                                                               "Pants": "#262626", "Hair": "#7A4E32"}),
    "TA": ("standing/easing-2", "Long Curly", None, None, {"Skin": "#B98260", "Jacket": "#B8A9F5", "Pants": "#3A4A6B"}),
    "TM": ("standing/resting-1", "Short 4", None, None, {"Skin": "#8D5A3B", "Top": "#8FD694", "Pants": "#4A4A55"}),
}

LISTE = [
    ("ST_ruhig", "ST", "Calm", 0), ("ST_froh", "ST", "Smile", 0), ("ST_ernst", "ST", "Serious", 0),
    ("ST_sorge", "ST", "Concerned|Serious", 0), ("ST_denkt", "ST", "Suspicious", 0), ("ST_entschl", "ST", "Driven", 0),
    ("ST_muede", "ST", "Tired", 0), ("ST_schreck", "ST", "Awe", 0),
    ("ST_ruft", "ST", "Concerned|Serious", 1),
    ("NA_ruhig", "NA", "Calm", 0), ("NA_ernst", "NA", "Serious", 0), ("NA_streng", "NA", "Solemn", 0),
    ("NA_denkt", "NA", "Suspicious", 0),
    ("NA_spricht", "NA", "Serious", 1),
    ("BO_ruhig", "BO", "Calm", 0), ("BO_ernst", "BO", "Serious", 0), ("BO_froh", "BO", "Smile", 0),
    ("BO_denkt", "BO", "Suspicious", 0),
    ("BO_spricht", "BO", "Serious", 1),
    ("TA_froh", "TA", "Smile", 0), ("TA_sorge", "TA", "Concerned|Serious", 0),
    ("TM_froh", "TM", "Smile", 0), ("TM_sorge", "TM", "Concerned|Serious", 0),
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
