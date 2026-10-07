"""Figuren für Folge 228 (Sekundäre Darlegungslast § 138 ZPO, Filesharing über den Familienanschluss) aus der
LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren fiktiv, Familie sympathisch, keine Täterfigur.
Herr Mehnert (HM, um 52, Anschlussinhaber, Beklagter; Stimme marc): standing/robot_dance-2 (schwarzer Pullover,
  Hose Blau #8DB3F2, offene Hand: er erklärt), Kopf Short 1, Brille Glasses, Haut #E8B48E, kein Bart.
Frau Mehnert (FM, um 50, Ehefrau; Stimme sabrina): standing/polka_dots (Oberteil mit Punkten, Hose Grün #8FD694),
  Kopf Bangs 2 (Haar #4A3222), Haut #C68E6A.
Sohn (SO, 24, spricht nicht): sitting/crossed_legs (Pullover Gelb #F9D56E, schwarze Hose) – sitzt auf dem Sofa,
  Kopf Medium 1, Haut #D9A47E.
Tochter (TO, 21, spricht nicht): sitting/closed_legs-1 (Jacke Lila #B8A9F5 über Ringelshirt, schwarze Hose) – sitzt auf
  einem Sitzkissen, Kopf Buns, Haut #D9A47E.
Anwältin der Filmfirma (AW, um 40; Stimme laura_ruhig): standing/blazer-2 (Blazer Dunkelblau #3A4A6B, Shirt Weiß,
  Beinprothese – beiläufig, sachliche Rolle, keine Täterin), Kopf Medium Bangs 3, Haut #F2D3BD.
Posen der Folgen 223–225 (und der parallel laufenden 226/227) nicht verwendet: dort blazer-1/-3/-4, shirt-2/-3/-4,
easing-1/-2, pointing_finger-1/-2, resting-1/-2, robot_dance-1/-3, walking-1/-2/-3, crossed_arms-1/-2. Polka Dots
zuletzt nicht in 223–227. Keine Bärte, keine Karikatur.
Präfixe HM_/FM_/SO_/TO_/AW_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und
blickt nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md): Calm, Serious, Smile, Suspicious, Awe, Fear, Tired bzw.
„Augen|geschlossener Mund“ (Concerned|Serious, Smile Big|Smile). Sprechende Ansichten (HM_redet, FM_redet, AW_redet,
Lexi) zusätzlich mit a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_228")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {   # Person: (Pose, Kopf, Bart, Brille, Farben)
    "HM": ("standing/robot_dance-2", "Short 1", None, "Glasses", {"Skin": "#E8B48E", "Pants": "#8DB3F2"}),
    "FM": ("standing/polka_dots", "Bangs 2", None, None, {"Skin": "#C68E6A", "Pants": "#8FD694", "Hair": "#4A3222"}),
    "SO": ("sitting/crossed_legs", "Medium 1", None, None, {"Skin": "#D9A47E", "Top": "#F9D56E"}),
    "TO": ("sitting/closed_legs-1", "Buns", None, None, {"Skin": "#D9A47E", "Jacket": "#B8A9F5"}),
    "AW": ("standing/blazer-2", "Medium Bangs 3", None, None, {"Skin": "#F2D3BD", "Jacket": "#3A4A6B", "Top": "#FFFFFF",
                                                             "Prosthesis": "#B8B8B8"}),
}

# (Name, Person, Grundmimik, mit Mundzuständen); jede Ansicht zusätzlich als _r (blickt nach rechts)
LISTE = [
    ("HM_ruhig", "HM", "Calm", 0), ("HM_redet", "HM", "Serious", 1), ("HM_ernst", "HM", "Serious", 0),
    ("HM_froh", "HM", "Smile", 0), ("HM_denkt", "HM", "Suspicious", 0), ("HM_sorge", "HM", "Concerned|Serious", 0),
    ("HM_staunt", "HM", "Awe", 0), ("HM_schreck", "HM", "Fear", 0),
    ("FM_ruhig", "FM", "Calm", 0), ("FM_redet", "FM", "Calm", 1), ("FM_froh", "FM", "Smile", 0),
    ("FM_denkt", "FM", "Suspicious", 0), ("FM_sorge", "FM", "Concerned|Serious", 0),
    ("SO_ruhig", "SO", "Calm", 0), ("SO_froh", "SO", "Smile", 0), ("SO_staunt", "SO", "Awe", 0),
    ("SO_denkt", "SO", "Suspicious", 0),
    ("TO_ruhig", "TO", "Calm", 0), ("TO_froh", "TO", "Smile Big|Smile", 0), ("TO_staunt", "TO", "Awe", 0),
    ("TO_denkt", "TO", "Suspicious", 0),
    ("AW_ruhig", "AW", "Calm", 0), ("AW_redet", "AW", "Serious", 1), ("AW_ernst", "AW", "Serious", 0),
    ("AW_denkt", "AW", "Suspicious", 0), ("AW_froh", "AW", "Smile", 0),
]

if __name__ == "__main__":
    os.makedirs(ZIEL, exist_ok=True)
    nur = sys.argv[1:]          # optional: nur bestimmte Personen (Vorschau)
    n = 0
    for name, p, mimik, mund in LISTE:
        if nur and p not in nur:
            continue
        pose, kopf, bart, brille, farben = P[p]
        for suffix, gespiegelt in (("", 1), ("_r", 0)):
            figur(pose, kopf, mimik, bart, brille, farben, hoehe=1200, spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}.png"); n += 1
            if mund:
                for k, m in MUND.items():
                    figur(pose, kopf, f"{mimik.split('|')[0]}|{m}", bart, brille, farben, hoehe=1200,
                          spiegeln=bool(gespiegelt)).save(f"{ZIEL}/{name}{suffix}_{k}.png"); n += 1
    if not nur:
        # Lexi (feste Moderatorin, Stimme Carla), blickt nach links zur Tafel
        for name, (pose, mimik) in {"LX_erklaert": ("standing/robot_dance-1", "Smile"), "LX_warnt": ("standing/robot_dance-1", "Serious")}.items():
            a = LX.AUSSEHEN
            for k, g in {"": mimik, **{"_" + k: f"{mimik}|{m}" for k, m in MUND.items()}}.items():
                figur(pose, a["kopf"], g, a["bart"], a["brille"], a["farben"], hoehe=1200, spiegeln=True).save(f"{ZIEL}/{name}{k}.png"); n += 1
    print(n, "Figurenbilder ->", ZIEL)
