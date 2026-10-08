"""Figuren für Folge 263 (Übergesetzlicher entschuldigender Notstand: Stellwerk, Nachbarstellwerk, Schienenplan) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv.
Frau Seefeld (SE, Ende 20, Stellwerksmitarbeiterin; Stimme julia): standing/easing-1 (offene Jacke Orange #F9A66C wie eine
  Warnjacke, Oberteil Weiß, schwarze Hose der Pose), Kopf Medium Bangs 2 (Haar Braun #8A5A3C), Haut #EDC3A0, keine Brille.
Herr Nordmann (NO, um 60, Fahrdienstleiter im Nachbarstellwerk; Stimme helmut): standing/shirt-4 (schwarzes Hemd der Pose,
  Hose Blau #8DB3F2), Kopf No Hair 3 (Haarkranz Grau #B4B4B4), Haut #E3B48C, kein Bart, keine Brille.
Gleisarbeiter (GA, namenlos, nur als Silhouetten mit Abstand im Schienenplan): standing/walking-2, walking-3, shirt-4,
  easing-1, walking-1 (Kopf hat-hip), einheitlich in Grau #6E7482 gefüllt (Open-Peeps-Umriss, kein Gesicht erkennbar,
  geschlossene Grundmimik Calm). Kein Opfer- oder Unfallbild.
Posen der letzten drei Folgen (259: blazer-4, sitting/bike, resting-1, crossed_arms-1; 260: robot_dance-3,
sitting/one_leg_up-2; 261: resting-2, shirt-3, easing-2) nicht für die Hauptfiguren verwendet; Farben Orange/Weiß und
Schwarz/Blau statt Gelb/Lila (259), Ocker/Anthrazit (260), Grün/Türkis/Schwarz (261). Keine Polka Dots, keine
Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Bärte, keine Karikatur. Präfixe SE_/NO_/GA_ (nie ER_).
Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Fear, Tired, Solemn, Driven, Eyes Closed,
Suspicious bzw. „Augen|geschlossener Mund“ (Concerned|Serious). Sprechende Ansichten SE_redet, SE_redet2, NO_redet (und Lexi)
zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX
from PIL import Image

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_263")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}
GRAU = (110, 116, 130)

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "SE": ("standing/easing-1", "Medium Bangs 2", None, None, {"Skin": "#EDC3A0", "Jacket": "#F9A66C", "Top": "#FFFFFF",
                                                               "Hair": "#8A5A3C"}),
    "NO": ("standing/shirt-4", "No Hair 3", None, None, {"Skin": "#E3B48C", "Pants": "#8DB3F2", "Hair": "#B4B4B4"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("SE_ruhig", "SE", "Calm", 0), ("SE_ernst", "SE", "Serious", 0), ("SE_sorge", "SE", "Concerned|Serious", 0),
    ("SE_angst", "SE", "Fear", 0), ("SE_muede", "SE", "Tired", 0), ("SE_fest", "SE", "Driven", 0),
    ("SE_still", "SE", "Solemn", 0), ("SE_zu", "SE", "Eyes Closed", 0), ("SE_skeptisch", "SE", "Suspicious", 0),
    ("SE_redet", "SE", "Concerned|Serious", 1), ("SE_redet2", "SE", "Solemn", 1),
    ("NO_ruhig", "NO", "Calm", 0), ("NO_ernst", "NO", "Serious", 0), ("NO_sorge", "NO", "Concerned|Serious", 0),
    ("NO_redet", "NO", "Concerned|Serious", 1),
]
SILH = [("GA_1", "standing/walking-2"), ("GA_2", "standing/walking-3"), ("GA_3", "standing/shirt-4"),
        ("GA_4", "standing/easing-1"), ("GA_5", "standing/walking-1")]


def silhouette(im):
    """Open-Peeps-Figur als einfarbige Silhouette (Alpha bleibt, Farbe einheitlich Grau)."""
    a = im.getchannel("A")
    s = Image.new("RGBA", im.size, GRAU + (255,))
    s.putalpha(a)
    return s


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
    for name, pose in SILH:
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            silhouette(figur(pose, "hat-hip", "Calm", None, None, {}, hoehe=600, spiegeln=bool(gespiegelt))).save(
                f"{ZIEL}/{name}{suffix}.png"); n += 1
    # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
    for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
        a = LX.AUSSEHEN
        for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
            figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
