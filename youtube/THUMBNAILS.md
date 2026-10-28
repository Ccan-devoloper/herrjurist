# Thumbnail-Standard LexVerse

Stand: 30.09.2026, vom Kanalinhaber freigegeben. Jedes Thumbnail entsteht mit dem Generator [`thumbnails/thumbnail.py`](thumbnails/thumbnail.py) aus einer JSON-Spezifikation. Beispiele stehen in [`thumbnails/beispiele.json`](thumbnails/beispiele.json), die Belege zu Empfehlungen, Studien und Vergleichskanälen in [`thumbnails/recherche.md`](thumbnails/recherche.md).

## Ziel

Ein Blick auf das Thumbnail genügt, um zu wissen, worum es geht. Bei Fallvideos weckt es Neugier, bei Lernvideos zeigt es sofort das Thema. Lernende, die „Schema § 224“ suchen, sollen das Video in der Trefferliste als das richtige erkennen. Das Thumbnail verspricht nur, was das Video einlöst; YouTube misst Test & Compare an der Wiedergabezeit, nicht an Klicks.

## Feste Gestaltung

| Element | Regel |
|---|---|
| Format | 1280 × 720 px, JPG unter 2 MB |
| Hintergrund | kräftige Farbe je Rechtsgebiet mit leichter Vignette: **Strafrecht** `#D7263D` · **Zivilrecht** `#1B6FD1` · **Öffentliches Recht** `#139A62` · **2. Examen** `#6B3FD0` · **Methodik** `#E08A00` |
| Text | Nunito Black (`fonts/Nunito.ttf`), Großbuchstaben, weiß mit 15 px dunkler Kontur und Schatten, oben links. **2–4 Wörter**, höchstens 16 Zeichen je Zeile, **genau ein Wort gelb** `#FFD23F`. Keine kleinen Schriften, keine Untertitel, kein Datum, keine Folgennummer |
| Figuren | Open-Peeps-Figuren (Zeichenstil der Videos) rechts als Oberkörper, unten angeschnitten, nie seitlich; 1–3 Figuren mit deutlicher Mimik; normale menschliche Hauttöne; weiße Aufkleberkontur, Linien verstärkt für die kleine Anzeige |
| Motive | farbige Emojis aus „Fluent Emoji Flat“ (MIT) mit weißer Kontur. Gehaltene Gegenstände sitzen an der Hand, freie Motive stehen groß im freien Raum |
| Logo | **kein Logo** im Thumbnail. Der Kanal ist in Suche und Feed über das Kanalbild erkennbar; das Logo kommt als Branding-Wasserzeichen in YouTube Studio ins Video |
| Unten rechts | dort liegt die Zeitanzeige: nur Figur oder Motiv, nie Text |

## Zwei Vorlagen

**Fall** (Montag, „Der Fall“, und fallartige Klausurpraxis): Hook als Frage oder Zuspitzung („WER IST *TÄTER?“, „MORD MIT DEM *AUTO?“), dazu eine erkennbare Szene: Figuren mit Mimik und gehaltenem Gegenstand, links unten das Hauptmotiv des Falls (Katze mit Krone, Rennwagen mit Knall).

**Lern** (Schema, Streitstand, Abgrenzung, Klausurfehler, Methodik, 2. Examen): Oben das Thema oder die Norm genau so, wie Lernende sie suchen („§ 224 STGB“, „ZV-GRUNDSCHEMA“, „ANFECHTUNGSKLAGE“). Links darunter die weiße Karte mit dunklem Kopf, der die Videoart nennt: `SCHEMA`, `STREIT`, `ABGRENZUNG`, `FEHLER`, `SCHRITTE` (Methodik), `MUSTER` (Formulierung, Tenor), `TAKTIK` (Zweckmäßigkeit), `SONDERFALL`, `DEFINITION` oder `ÜBERBLICK`. Rechts Figuren aus dem typischen Fall, in der Mitte optional ein Themenmotiv. Die Karte ist das Wiedererkennungszeichen aller Lernvideos.

## Layout-Automatik und Prüfungen

Der Generator setzt alles selbst und bricht mit einer Fehlermeldung ab, statt ein fehlerhaftes Bild zu liefern:

1. **Textlage:** Der Text steht entweder neben den Figuren (mindestens 100 px Schrift) oder einzeilig über die volle Breite mit den Figuren darunter. Gewählt wird, was Schrift und Figuren zusammen größer macht (Schriftgröße × Figurenhöhe^1,5). Passt keins, wird die Figurenzone schmaler; zuletzt läuft der Text mehrzeilig über die volle Breite. Zeilen mit höchstens 12 Zeichen passen fast immer neben die Figuren und ergeben die größten Figuren.
2. **Lernvorlage:** Bliebe unter dem Text weniger als 380 px für die Karte, läuft der Text über die volle Breite. Die Karte steht am linken Rand und wird so groß wie der freie Raum. Ein Mittelmotiv kommt nur dazu, wenn es mindestens 200 px groß werden kann; Kleinkram wird weggelassen.
3. **Prüfungen:** Text und Figuren berühren sich nicht (echte Maske inklusive Kontur und Schatten); keine Figur ist seitlich angeschnitten; freie Motive überlappen weder Text noch Figuren noch gehaltene Gegenstände (14 px Abstand); gehaltene Gegenstände liegen vollständig im Bild; der Text ragt nicht über den Rand; Figuren werden nicht kleiner als 660 px Gesamthöhe (sonst Text kürzen).
4. **Regelprüfung vor dem Rendern:** Gebiet, Vorlage und Kartenkopf gültig, 1–3 Zeilen, ein gelbes Wort, alle Emoji-Namen im Satz vorhanden. Hinweise (kein Abbruch): mehr als 4 Wörter, Zeilen über 16 Zeichen, Kleinbuchstaben, mehr als 3 Figuren.

## Spezifikation (JSON)

```json
{
  "k": "katzenkoenig",
  "typ": "fall",
  "gebiet": "Strafrecht",
  "titel": "Katzenkönig-Fall: Mittelbare Täterschaft – Täter hinter dem Täter",
  "text": ["WER IST", "*TÄTER?"],
  "figuren": [
    {"pose": "standing/blazer-3", "kopf": "Long", "gesicht": "Cheeky", "farben": {"Skin": "#F1C6A5", "Jacket": "#B784D1"}, "spiegeln": true},
    {"pose": "standing/robot_dance-1", "kopf": "Short 2", "gesicht": "Driven", "farben": {"Skin": "#E9BE98", "Top": "#9BD88A"}, "spiegeln": true,
     "haelt": {"emoji": "kitchen-knife", "g": 190, "drehung": -25, "hand": "links", "spiegeln": true}}
  ],
  "motiv": {"teile": [["cat-face", 1.0, 0, 0.3, 0], ["crown", 0.58, 0.21, 0.0, -6]], "g": 300},
  "varianten": {"B": {"text": ["*KATZEN~", "KÖNIG"]}}
}
```

- `text`: Zeilen wie gewünscht umbrochen, `*` vor dem gelben Wort. Läuft der Text einzeilig über die volle Breite, werden die Zeilen verbunden: `~` am Zeilenende ist eine reine Silbentrennung („ANFECHTUNGS~“ + „KLAGE“ → „ANFECHTUNGSKLAGE“, mehrzeilig als Strich gezeigt), `-` ein echter Bindestrich („RASER-“ + „FALL“ → „RASER-FALL“).
- `karte` (nur `lern`): Kartenkopf, siehe oben.
- `figuren`: Teile aus der Open-Peeps-Bibliothek (`openpeeps-erweiterung/figma-bibliothek`, siehe README dort) oder `{"lexi": "erklaert_auf", "spiegeln": true}` für die Moderatorin. Optional `gross` (Größenfaktor) und `sichtbar` (sichtbarer Anteil der Figur, Standard 0,6). Die erste Figur der Liste steht rechts außen und zuvorderst. Für gehaltene Gegenstände Posen mit ausgestrecktem Arm nehmen (`robot_dance-1`, `shirt-1`); `pointing_finger` hat schwarze Kleidung.
- `haelt`: Emoji, Größe `g` in px, `drehung` in Grad, `hand` `links`/`rechts` (Bildseite), `spiegeln` z. B. damit ein Messer am Griff gehalten wird.
- `motiv`: `{"emoji": "shield"}` oder zusammengesetzt `{"teile": [[name, anteil, dx, dy, drehung], …]}`, `g` = Zielgröße (Fall 420, Lern 300; wird bei Platzmangel kleiner).
- `layout` (selten nötig): `fig_links` (Beginn der Figurenzone, 650), `hoehe` (Figurenhöhe, 1000), `ueberlappung` (0,62).
- `varianten`: geänderte Felder für die Test-&-Compare-Varianten; Ausgabe als `<k>_B.jpg`.

## Angaben je Folge im Themenplan

Für die 780 Folgen steht in `themenplanung/thumbs_*.json` je Folge nur eine kurze, abstrakte Angabe. [`thumbnails/aus_plan.py`](thumbnails/aus_plan.py) macht daraus die vollständige Spezifikation. Frisur, Hautton, Oberteilfarbe, Bart und Pose werden aus Folgennummer und Rolle abgeleitet: reproduzierbar, innerhalb eines Bildes verschieden, normale Hauttöne.

```json
{"nr": 1, "typ": "fall", "text": ["MORD MIT", "DEM *AUTO?"], "b": ["*RASER-", "FALL"],
 "figuren": [{"rolle": "Zeugin", "person": "w", "mimik": "aengstlich"},
             {"rolle": "Raser", "person": "m", "mimik": "frech", "haelt": "racing-car"}],
 "motiv": ["police-car-light"]}
```

- `typ`: `fall` für Klassiker- und Alltagsfälle, sonst `lern` mit `karte`.
- `b`: Text der Variante B.
- `figuren`: 1–2 Rollen, höchstens 3.
  - `person`: `w` oder `m`; `alt: true` für ältere Menschen.
  - `mimik`: eine aus `aus_plan.MIMIK`, etwa wuetend, aengstlich, frech, ernst, entschlossen, froh, skeptisch, staunend, besorgt oder erklaert.
  - `kleidung`: `anzug` (Richterin, Anwalt, Behörde) oder `arzt`.
  - `kopf` (Frisur, z. B. `Hijab`) und `haut` (`hell`, `mittel`, `dunkel` oder Farbwert): nur, wenn das Thema es verlangt; sonst wählt der Baukasten.
  - `haelt`: Emoji-Name oder `{"emoji", "g", "drehung", "spiegeln"}`.
  - `zur_person: true`: Die zweite Figur wendet sich der ersten zu und reicht ihr den Gegenstand.
  - `{"lexi": "erklaert"}`: die Moderatorin, sparsam und vor allem bei Methodik.
- `motiv`: ein oder zwei Emoji-Namen (Hauptmotiv plus kleiner Akzent oben rechts); nicht derselbe Gegenstand wie der gehaltene.

```sh
python3 youtube/thumbnails/aus_plan.py --render AUSGABE --nr 1-40      # Bilder plus Kontaktbögen zu je 12
python3 youtube/thumbnails/aus_plan.py --json alle.json               # vollständige Spezifikationen
```

## A/B-Test

Pro Folge zwei Varianten, in YouTube Studio über „Test & Compare“ gegeneinander getestet. Getestet wird ein **Prinzip**, keine Kleinigkeit: Frage gegen Fallname („WER IST TÄTER?“ gegen „KATZENKÖNIG“), Norm gegen Merkfrage („§ 224 STGB“ gegen „SCHUH = WAFFE?“), Thema gegen Aufforderung („NOTWEHR § 32“ gegen „NOTWEHR PRÜFEN“). Ergebnisse (Winner/Preferred/gleich) je Format sammeln und die Vorlagen danach nachschärfen.

## Benutzung

```sh
youtube/thumbnails/assets_holen.sh                 # einmalig: Emoji-Satz laden (npm, nicht im Repository)
python3 youtube/thumbnails/thumbnail.py youtube/thumbnails/beispiele.json --out AUSGABE --vorschau
```

`--vorschau` erzeugt zusätzlich einen Kontaktbogen und eine Handy-Feed-Ansicht (246 × 138 px mit Zeitstempel), `--nur k1,k2` rendert einzelne Folgen. Die fertigen JPGs gehören zum Upload bzw. in den Produktionsmaster auf Drive, nicht ins Repository. Pfade lassen sich mit `LEXVERSE_FONT`, `LEXVERSE_EMOJI` und `LEXVERSE_THUMB_CACHE` umstellen. Abhängigkeiten: Pillow (mit variablen Schriften), NumPy, SciPy, cairosvg, svgpathtools.
