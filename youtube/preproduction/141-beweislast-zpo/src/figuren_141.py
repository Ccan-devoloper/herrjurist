"""Figuren für Folge 141 (Beweislast ZPO, non liquet beim Barkredit) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0).
Alle Figuren fiktiv.
Herr Wiedemann (WI, um 65, Darlehensgeber, Kläger; Stimme helmut): standing/blazer-4 (Sakko Blau #8DB3F2, Shirt Weiß,
  schwarze Hose), Kopf No Hair 2, Brille Glasses 2, Haut #EDC3A3, kein Bart.
Frau Krause (KR, um 35, Darlehensnehmerin, Beklagte; spricht nicht): standing/crossed_arms-2 (verschränkte Arme – sie
  bestreitet; schwarzes Oberteil, Hose Lila #B8A9F5), Kopf Long Curly (Haar #4A3222), Haut #F0C29E.
Herr Reichert (RT, um 30, Zeuge des Klägers; Stimme niklas): standing/easing-1 (offenes Hemd Grün #8FD694 über gelbem
  Shirt #F9D56E, schwarze Hose), Kopf Short 3, Haut #E0AC84, kein Bart.
Frau Fischer (FI, um 30, Zeugin der Beklagten; Stimme julia): standing/robot_dance-2 (schwarzes Oberteil, Hose Grün
  #8FD694; offene Hand), Kopf Medium Straight, Brille Glasses 3, Haut #C68E6A.
Richterin (RI, um 55, ohne Namen und Text): standing/blazer-3 (dunkles Sakko #3A3A48, Hose Graublau #5B6B8C),
  Kopf Gray Bun, Haut #F2D3BD.
Posen der letzten drei Folgen (138: resting-1, blazer-1; 139: robot_dance-3, pointing_finger-2; 140: crossed_arms-1,
walking-1) nicht verwendet (easing-1 zuletzt in 018 mit anderer Farbe und anderem Kopf); keine Polka Dots, keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine
Karikatur. Präfixe WI_/KR_/RT_/FI_/RI_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist
gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Driven, Tired, Fear bzw.
„Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten (WI_redet, RT_redet, FI_redet, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_141")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "WI": ("standing/blazer-4", "No Hair 2", None, "Glasses 2", {"Skin": "#EDC3A3", "Jacket": "#8DB3F2", "Top": "#FFFFFF"}),
    "KR": ("standing/crossed_arms-2", "Long Curly", None, None, {"Skin": "#F0C29E", "Pants": "#B8A9F5", "Hair": "#4A3222"}),
    "RT": ("standing/easing-1", "Short 3", None, None, {"Skin": "#E0AC84", "Jacket": "#8FD694", "Top": "#F9D56E"}),
    "FI": ("standing/robot_dance-2", "Medium Straight", None, "Glasses 3", {"Skin": "#C68E6A", "Pants": "#8FD694"}),
    "RI": ("standing/blazer-3", "Gray Bun", None, None, {"Skin": "#F2D3BD", "Jacket": "#3A3A48", "Pants": "#5B6B8C"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("WI_ruhig", "WI", "Calm", 0), ("WI_redet", "WI", "Driven", 1), ("WI_ernst", "WI", "Serious", 0),
    ("WI_froh", "WI", "Smile", 0), ("WI_denkt", "WI", "Suspicious", 0), ("WI_sorge", "WI", "Concerned|Serious", 0),
    ("WI_muede", "WI", "Tired", 0),
    ("KR_ruhig", "KR", "Calm", 0), ("KR_ernst", "KR", "Serious", 0), ("KR_skeptisch", "KR", "Suspicious", 0),
    ("KR_sorge", "KR", "Concerned|Serious", 0), ("KR_froh", "KR", "Smile", 0), ("KR_schreck", "KR", "Fear", 0),
    ("RT_ruhig", "RT", "Calm", 0), ("RT_redet", "RT", "Serious", 1), ("RT_denkt", "RT", "Suspicious", 0),
    ("RT_ernst", "RT", "Serious", 0),
    ("FI_ruhig", "FI", "Calm", 0), ("FI_redet", "FI", "Serious", 1), ("FI_denkt", "FI", "Suspicious", 0),
    ("FI_ernst", "FI", "Serious", 0),
    ("RI_ruhig", "RI", "Calm", 0), ("RI_ernst", "RI", "Serious", 0), ("RI_denkt", "RI", "Suspicious", 0),
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
