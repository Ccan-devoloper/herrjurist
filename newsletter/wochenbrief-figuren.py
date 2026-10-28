"""Open-Peeps-Figuren für eine Wochenbrief-Ausgabe (CC0): Titelbild mit vier Brustbildern und je Fall eine Figur.

    python3 newsletter/wochenbrief-figuren.py ausgabe.json ZIELORDNER

Die Auswahl ist pro Ausgabe und Fall fest (Seed aus Nummer und Fall), also bei jedem Lauf gleich.
Schreibt hero.png und fNN.png und trägt "bild"/"figur" in die Ausgabe-JSON ein.
"""
import json, os, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "op", "ressourcen", "peeps-bibliothek"))
from lexpeeps import figur
from PIL import Image

KOEPFE = ["Afro", "Bangs", "Bangs 2", "Bantu Knots", "Bun", "Buns", "Cornrows", "Dreads 1", "Flat Top", "Gray Bun",
          "Gray Short", "Hijab", "Long", "Long Afro", "Long Bangs", "Long Curly", "Medium 1", "Medium 2", "Medium 3",
          "Medium Bangs", "Medium Straight", "Mohawk", "No Hair 1", "Pomp", "Short 1", "Short 2", "Short 3", "Short 4",
          "Short 5", "Turban", "Twists", "Twists 2"]
KOERPER = ["Button Shirt 1", "Button Shirt 2", "Coffee", "Device", "Explaining", "Hoodie", "Paper", "Pointing Up",
           "Polo and Sweater", "Sporty Tee", "Striped Tee", "Sweater", "Sweater Dots", "Tee 1", "Tee Arms Crossed", "Turtleneck"]
GESICHTER = ["Concerned", "Concerned Fear", "Suspicious", "Explaining", "Hectic", "Serious", "Cheeky", "Awe", "Driven", "Smile"]
HAUT = ["#F3D0B5", "#E8B48F", "#C58E64", "#B07A55", "#8D5A3B", "#5E3A26"]
HAAR = ["#1E1E1E", "#3B2A1E", "#A0522D", "#D8B26E", "#7A7A7A"]
FARBEN = ["#8DB3F2", "#F9A66C", "#8FD694", "#C9B8FF", "#F9D56E", "#F7A8C4", "#9ED9E0"]


def person(rnd, gesicht=None, hoehe=600):
    return figur("body/" + rnd.choice(KOERPER), rnd.choice(KOEPFE), gesicht or rnd.choice(GESICHTER),
                 bart=rnd.choice([None, None, None, "Full", "Moustache 1"]) if False else None,
                 brille=rnd.choice([None, None, None, "Glasses", "Glasses 2"]),
                 farben={"Skin": rnd.choice(HAUT), "Hair": rnd.choice(HAAR), "Top": rnd.choice(FARBEN), "Clothes": rnd.choice(FARBEN)},
                 hoehe=hoehe)


def main(pfad, ziel):
    a = json.load(open(pfad, encoding="utf-8"))
    os.makedirs(ziel, exist_ok=True)
    rnd = random.Random(f"wb{a['nr']}-hero")
    leute = [person(rnd, g, 560) for g in ("Explaining", "Smile", "Concerned", "Cheeky")]
    # Titelbild: vier Brustbilder leicht überlappend nebeneinander, unten bündig
    breite = sum(p.width for p in leute) - 60 * (len(leute) - 1)
    hoehe = max(p.height for p in leute)
    hero = Image.new("RGBA", (breite, hoehe), (0, 0, 0, 0))
    x = 0
    for p in leute:
        hero.alpha_composite(p, (x, hoehe - p.height)); x += p.width - 60
    hero.save(os.path.join(ziel, "hero.png"), optimize=True)
    a["bild"] = "hero.png"
    for f in a["faelle"]:
        r = random.Random(f"wb{a['nr']}-{f['nr']}")
        person(r, None, 300).save(os.path.join(ziel, f"f{f['nr']}.png"), optimize=True)
        f["figur"] = f"f{f['nr']}.png"
    json.dump(a, open(pfad, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
