# Open Peeps – vollständige Bibliothek aus der Figma-Community-Datei

- **Quelle:** „Open Peeps by Pablo Stanley (Community)“, Figma-Seite *Symbols*. Die Seite wurde am 30.09.2026 einmalig als SVG exportiert und in Einzelteile zerlegt. Figma wird danach nicht mehr gebraucht.
- **Lizenz:** Open Peeps von Pablo Stanley steht unter **CC0**. Freie Nutzung, auch kommerziell, ohne Namensnennung.
- **Umfang:** 185 Teile, jedes als eigene SVG mit passendem Rahmen. Die Übersicht mit Figma-Namen und Maßen steht in `index.json`.
- **Besonderheit gegenüber react-peeps:** Die Teile sind hier bereits im **offiziellen Multicolor-Stil** eingefärbt. Das betrifft Kleidung, Hautton und farbige Haare (rot, blond, grau) sowie Kopftücher und OP-Hauben.

| Ordner | Inhalt |
|---|---|
| `pose/` | 26 stehende Posen, 3 Arzt/Pflege-Posen, 11 sitzende Posen (u. a. Fahrrad, Rollstuhl) |
| `body/` | 29 Oberkörper für Brustbilder |
| `face/` | 30 Gesichter und 3 Gesichter mit Maske |
| `head/` | rund 50 Frisuren und Kopfbedeckungen, farbig |
| `facial-hair/` | 16 Bärte und Schnurrbärte |
| `accessories/`, `mask/` | Brillen, Sonnenbrillen, Augenklappe, Masken |
| `a_person/` | Vorlagen für Brustbild, sitzend und stehend (zeigen, wie die Teile übereinanderliegen) |
| `peep-78*` | zwei Beispielfiguren aus der Datei |

**Zusammensetzung:** Die Posen enthalten nur den Hals. Kopf (Frisur mit Kopfform), Gesicht und Bart werden wie in Figma übereinandergelegt, nach der Lage in `a_person/`.

## Figurengenerator `lexpeeps.py`

```python
from lexpeeps import figur
bild = figur("standing/robot_dance-1", "Long Curly", "Explaining", bart=None, brille=None,
             farben={"Top": "#B8A9F5", "Skin": "#B07552"}, hoehe=1400, spiegeln=False)   # PIL-Bild, freigestellt
```

- **Zusammensetzung:** Pose, Kopf, Gesicht, Bart und Brille werden exakt wie in den Figma-Vorlagen „a person/…“ zusammengesetzt. Die Rahmenpositionen stehen in `rahmen.py`, die Abstände für Gesicht, Bart und Brille entsprechen react-peeps. Geprüft ist das an der Vorlage, die Abweichung liegt unter 0,05 Einheiten.
- **Einfärben:** Umgefärbt wird über die Figma-Flächennamen: `Skin`, `Top`, `Pants`, `Jacket`, `Shoes`, `Hair`, `Clothes`, `bandana`, `hijab`, `Turban`, `Hat` usw.
- **Farbregel bei Posen:** In Figma hat `…-1` ein farbiges Oberteil und eine schwarze Hose, `…-2` ist umgekehrt. Für ein einheitliches Outfit einer Figur deshalb Posen aus derselben Reihe kombinieren.
- **Aliens (LexVerse):** Gesichter `Cyclops` oder `Monster`, immer mit normaler menschlicher Hautfarbe (Vorgabe des Kanalinhabers).
- **Mundzustände für Figurenrede:** `gesicht="Serious|Explaining"` nimmt Augen und Nase aus `Serious` und die Mundpartie aus `Explaining`. Der Schnitt liegt quer bei 60 % der Gesichtshöhe (`MUNDSCHNITT`). Bewährt haben sich die Mundformen `Explaining` (a, weit offen), `Concerned Fear` (o, rund) und `Hectic` (e, breit mit Zähnen). Die Grundmimik ist der geschlossene Mund.
- **Abhängigkeiten:** `cairosvg`, `svgpathtools`, `Pillow`.

## Lexi – Moderatorin von LexVerse (festgelegt 30.09.2026)

`lexi.py` legt ihr Aussehen verbindlich fest. Es ist in jedem Video identisch:
- **Aussehen:** Dutt mit rosa Haarband, runde Brille („Glasses 5“), gelbes Oberteil, schwarze Hose, Haut `#C58E64`
- **Stimme:** Carla Blum

**Posen und Mimiken:**
- ruhig, freut, nachdenklich, skeptisch
- erklärt und warnt, jeweils mit offenem und geschlossenem Mund für die Mundbewegung
- kommt ins Bild

Jede Pose gibt es gespiegelt mit dem Suffix `_l`. Verwendet werden nur Posen mit einfärbbarem Oberteil und schlanker Statur.

**Einsatz:** 2–3 feste Auftritte pro Video: Klausurtipp, Merksatz, optional Intro oder Outro. Nicht durchgehend im Bild.
