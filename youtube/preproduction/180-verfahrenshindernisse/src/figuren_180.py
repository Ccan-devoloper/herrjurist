"""Figuren für Folge 180 (Verfahrenshindernisse: Treppenhaus, Polizeiwache, Staatsanwaltschaft) aus der LexVerse-Figma-
Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Herr Ostwald (OS, um 68, Nachbar und Verletzter, stellt den Strafantrag; Stimme helmut): standing/easing-1 (Strickjacke Blau
  #8DB3F2 offen, weißes Shirt, schwarze Hose, weiße Schuhe), Kopf Gray Short mit grauem Haar #BDBDBD, Brille Glasses 4,
  Haut #F0CDB4, kein Bart.
Herr Stolte (ST, um 40, Beschuldigter, spricht nicht): standing/crossed_arms-1 (Pullover Grün #8FD694, schwarze Hose,
  weiße Schuhe), Kopf Short 3, Haut #E2B190, kein Bart, keine Brille; Alltagskleidung, keine „fiese“ Täterfigur.
Referendarin Hartlieb (HA, um 27, Referendarin bei der Staatsanwaltschaft; Stimme ela_froh, eifrig): standing/resting-2
  (schwarzes Oberteil der Pose, Hose Lila #B8A9F5, Hand in der Hüfte), Kopf Medium Bangs 3, Haut #EDC3A0. (robot_dance-3
  verworfen: Silhouette zu nah an Lexi, robot_dance-1.)
Polizeibeamtin (PB, um 35, Funktionsrolle ohne Namen, spricht nicht): standing/shirt-4 (schwarzes Hemd, Hose Dunkelblau
  #2B3A55, ohne Abzeichen oder Logo), Kopf Bun, Haut #D9A07A.
Posen der letzten drei Folgen (177: blazer-3, robot_dance-2; 178: resting-1, shirt-3; 179: blazer-4, shirt-3,
crossed_arms-2) nicht verwendet; keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine
Karikatur. Präfixe OS_/ST_/HA_/PB_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Suspicious, Fear, Tired, Smile, Solemn, Contempt bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten OS_redet, HA_redet, HA_redet2 (und
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_180")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "OS": ("standing/easing-1", "Gray Short", None, "Glasses 4",
           {"Skin": "#F0CDB4", "Jacket": "#8DB3F2", "Top": "#FFFFFF", "Hair": "#BDBDBD"}),
    "ST": ("standing/crossed_arms-1", "Short 3", None, None, {"Skin": "#E2B190", "Top": "#8FD694"}),
    "HA": ("standing/resting-2", "Medium Bangs 3", None, None, {"Skin": "#EDC3A0", "Pants": "#B8A9F5"}),
    "PB": ("standing/shirt-4", "Bun", None, None, {"Skin": "#D9A07A", "Pants": "#2B3A55"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("OS_ruhig", "OS", "Calm", 0), ("OS_ernst", "OS", "Serious", 0), ("OS_sorge", "OS", "Concerned|Serious", 0),
    ("OS_schreck", "OS", "Fear", 0), ("OS_muede", "OS", "Tired", 0), ("OS_froh", "OS", "Smile", 0),
    ("OS_redet", "OS", "Serious", 1),
    ("ST_ruhig", "ST", "Calm", 0), ("ST_abfaellig", "ST", "Contempt", 0), ("ST_skeptisch", "ST", "Suspicious", 0),
    ("ST_ernst", "ST", "Serious", 0), ("ST_muede", "ST", "Tired", 0),
    ("HA_froh", "HA", "Smile", 0), ("HA_eifrig", "HA", "Smile Big|Smile", 0), ("HA_ruhig", "HA", "Calm", 0),
    ("HA_skeptisch", "HA", "Suspicious", 0), ("HA_schreck", "HA", "Fear", 0), ("HA_ernst", "HA", "Serious", 0),
    ("HA_still", "HA", "Solemn", 0),
    ("HA_redet", "HA", "Smile Big|Smile", 1), ("HA_redet2", "HA", "Serious", 1),
    ("PB_ruhig", "PB", "Calm", 0), ("PB_ernst", "PB", "Serious", 0),
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
