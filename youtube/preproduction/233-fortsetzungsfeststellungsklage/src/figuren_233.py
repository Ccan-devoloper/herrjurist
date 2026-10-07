"""Figuren für Folge 233 (Fortsetzungsfeststellungsklage) aus der LexVerse-Figma-Bibliothek (Open Peeps, CC0). Alle Figuren
fiktiv, die Demo neutral (Thema Radwege, Schilder ohne Parolen).
Jördis (JO, um 28, Leiterin der Demo; Stimme lucy): standing/easing-1 (offene Jacke Türkis #7FD6D0 über weißem Shirt, Hose
  Dunkelblau #3A4A6B), Kopf Long (Haar Dunkelbraun #5A3A28), Haut #EBC4A2, keine Brille, kein Bart.
Herr Hinze (HI, um 50, Polizeihauptkommissar; Stimme stephan): standing/blazer-4 (Jacke Polizeiblau #2F3E66, Hemd Hellblau
  #C9DAF5, Hose Polizeiblau), Kopf Short 3, Haut #E2B48F – sachlich, ruhig.
Nebenfiguren ohne Namen und ohne Stimme (Mund immer zu): ein Teilnehmer, der Farbe sprüht (SP, um 30): standing/pointing_finger-1
  (erhobene Hand hält die Sprühdose; Oberteil Grau #8A8F99), Kopf Shaved 2, Haut #D9A47E – unauffällig, keine Täterkarikatur;
  eine Radfahrerin (RA, um 35): sitting/bike, Kopf Bun, Haut #C68E6A; eine ältere Teilnehmerin (AL, um 65): standing/resting-2
  (Hose Lila #B8A9F5), Kopf Gray Bun, Brille Glasses 2, Haut #F0C8A8.
Posen nicht aus 228–231 (robot_dance-2/-3, polka_dots, crossed_legs, closed_legs-1, blazer-2, blazer-3, easing-2, walking-1,
pointing_finger-2, shirt-3, shirt-4, walking-2); keine Prothesen-Posen (shirt-1/-2, blazer-1/-2), keine Polka Dots, keine Bärte.
Präfixe JO_/HI_/SP_/RA_/AL_ (nie ER_). Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt
nach links, Suffix _r blickt nach rechts.
Grundmimik immer mit geschlossenem Mund (FOLGE-ABLAUF.md). Sprechende Ansichten (JO_ruft, HI_spricht, Lexi) zusätzlich mit
a/o/e: Augen der Grundmimik + Mund Explaining / Concerned Fear / Hectic, Schnitt bei 60 %."""
import os, sys
BIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../openpeeps-erweiterung/figma-bibliothek")
sys.path.insert(0, BIB)
from lexpeeps import figur
import lexi as LX

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../peeps/op_233")
MUND = {"a": "Explaining", "o": "Concerned Fear", "e": "Hectic"}

P = {
    "JO": ("standing/easing-1", "Long", None, None, {"Skin": "#EBC4A2", "Jacket": "#7FD6D0", "Top": "#FFFFFF",
                                                     "Pants": "#3A4A6B", "Hair": "#5A3A28"}),
    "HI": ("standing/blazer-4", "Short 3", None, None, {"Skin": "#E2B48F", "Jacket": "#2F3E66", "Top": "#C9DAF5",
                                                        "Pants": "#2F3E66"}),
    "SP": ("standing/pointing_finger-1", "Shaved 2", None, None, {"Skin": "#D9A47E", "Top": "#8A8F99", "Pants": "#4A4A55"}),
    "RA": ("sitting/bike", "Bun", None, None, {"Skin": "#C68E6A"}),
    "AL": ("standing/resting-2", "Gray Bun", None, "Glasses 2", {"Skin": "#F0C8A8", "Pants": "#B8A9F5"}),
}

LISTE = [
    ("JO_ruhig", "JO", "Calm", 0), ("JO_froh", "JO", "Smile", 0), ("JO_sorge", "JO", "Concerned|Serious", 0),
    ("JO_ernst", "JO", "Serious", 0), ("JO_denkt", "JO", "Suspicious", 0), ("JO_muede", "JO", "Tired", 0),
    ("JO_schreck", "JO", "Awe", 0), ("JO_entschl", "JO", "Driven", 0),
    ("JO_ruft", "JO", "Concerned|Serious", 1),
    ("HI_ruhig", "HI", "Calm", 0), ("HI_ernst", "HI", "Serious", 0), ("HI_streng", "HI", "Solemn", 0),
    ("HI_denkt", "HI", "Suspicious", 0),
    ("HI_spricht", "HI", "Serious", 1),
    ("SP_ruhig", "SP", "Serious", 0), ("SP_denkt", "SP", "Suspicious", 0),
    ("RA_froh", "RA", "Smile", 0), ("RA_sorge", "RA", "Concerned|Serious", 0),
    ("AL_froh", "AL", "Smile", 0), ("AL_sorge", "AL", "Concerned|Serious", 0),
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
