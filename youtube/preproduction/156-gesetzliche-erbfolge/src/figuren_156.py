"""Figuren für Folge 156 (Gesetzliche Erbfolge; die Familie im Esszimmer) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv. Der Erblasser Kurt und sein vorverstorbener Sohn Andreas erscheinen NICHT als Figuren (nur als Namen im
Stammbaum, grauer Rahmen).
Christa (CH, um 75, Ehefrau, Witwe; spricht nicht): standing/easing-2 (Jacke Dunkelblau #2E3550, schwarzes Oberteil, Hose Grau
  #8A8A96), Kopf Gray Bun (Haar #DCD7D7), Brille Glasses 4, Haut #F0C8A8.
Verena (VE, um 45, Tochter; spricht nicht): standing/shirt-3 (Hemdbluse Blau #8DB3F2, schwarze Hose), Kopf Long, Haut #E8B48F.
Mathilda (MA, um 6, Tochter von Verena; spricht nicht): standing/walking-2 (schwarzes T-Shirt, Hose Rot #F07A6A), Kopf Buns
  (zwei Haarknoten), Mimik Cute/Calm; als Kind über `hoehe` auf etwa 58 % der Erwachsenenhöhe skaliert (Folien).
Severin (SE, um 20, Enkel, Sohn des vorverstorbenen Andreas; Stimme niklas): standing/robot_dance-2 (schwarzer Pullover, Hose
  Grün #8FD694, offene Hand), Kopf Short 4, Haut #D9A47E.
Egbert (EG, um 75, Bruder von Kurt, 2. Ordnung; Stimme helmut): standing/pointing_finger-2 (schwarzer Pullover, Hose Beige
  #D6B48A, erhobener Zeigefinger), Kopf No Hair 2, Brille Glasses 3, Haut #EBC3A0, kein Bart.
Posen der letzten Folgen (152: walking-1, shirt-4; 153: easing-1, resting-2, resting-1; 154: crossed_arms-2, blazer-3;
155: blazer-4, walking-3, sitting/hands_back-1) nicht verwendet; robot_dance-1 ist Lexi vorbehalten; keine Polka Dots, keine
Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe CH_/VE_/MA_/SE_/EG_ (nie ER_). Alle Posen blicken
im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Solemn, Tired, Suspicious, Smile, Cute bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten SE_redet, EG_redet (und Lexi) zusätzlich mit a/o/e:
Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_156")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "CH": ("standing/easing-2", "Gray Bun", None, "Glasses 4", {"Skin": "#F0C8A8", "Jacket": "#2E3550", "Pants": "#8A8A96",
                                                               "Hair": "#DCD7D7"}),
    "VE": ("standing/shirt-3", "Long", None, None, {"Skin": "#E8B48F", "Top": "#8DB3F2"}),
    "MA": ("standing/walking-2", "Buns", None, None, {"Skin": "#E8B48F", "Pants": "#F07A6A"}),
    "SE": ("standing/robot_dance-2", "Short 4", None, None, {"Skin": "#D9A47E", "Pants": "#8FD694"}),
    "EG": ("standing/pointing_finger-2", "No Hair 2", None, "Glasses 3", {"Skin": "#EBC3A0", "Pants": "#D6B48A"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("CH_ruhig", "CH", "Calm", 0), ("CH_still", "CH", "Solemn", 0), ("CH_muede", "CH", "Tired", 0),
    ("CH_ernst", "CH", "Serious", 0), ("CH_froh", "CH", "Smile", 0),
    ("VE_ruhig", "VE", "Calm", 0), ("VE_still", "VE", "Solemn", 0), ("VE_ernst", "VE", "Serious", 0),
    ("VE_sorge", "VE", "Concerned|Serious", 0), ("VE_froh", "VE", "Smile", 0),
    ("MA_ruhig", "MA", "Calm", 0), ("MA_suess", "MA", "Cute", 0),
    ("SE_ruhig", "SE", "Calm", 0), ("SE_still", "SE", "Solemn", 0), ("SE_sorge", "SE", "Concerned|Serious", 0),
    ("SE_redet", "SE", "Concerned|Serious", 1), ("SE_froh", "SE", "Smile", 0), ("SE_ernst", "SE", "Serious", 0),
    ("EG_ruhig", "EG", "Calm", 0), ("EG_redet", "EG", "Suspicious", 1), ("EG_skeptisch", "EG", "Suspicious", 0),
    ("EG_still", "EG", "Solemn", 0), ("EG_muede", "EG", "Tired", 0),
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
