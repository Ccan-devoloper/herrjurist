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

**Lern** (Schema, Streitstand, Abgrenzung, Klausurfehler, Methodik, 2. Examen): Oben das Thema oder die Norm genau so, wie Lernende sie suchen („§ 224 STGB“, „ZV-GRUNDSCHEMA“, „ANFECHTUNGSKLAGE“). Links darunter die weiße Karte mit dunklem Kopf, der die Videoart nennt: `SCHEMA`, `STREIT`, `ABGRENZUNG`, `FEHLER`, `SCHRITTE`, `DEFINITION` oder `ÜBERBLICK`. Rechts Figuren aus dem typischen Fall, in der Mitte optional ein Themenmotiv. Die Karte ist das Wiedererkennungszeichen aller Lernvideos.

## Layout-Automatik und Prüfungen

Der Generator setzt alles selbst und bricht mit einer Fehlermeldung ab, statt ein fehlerhaftes Bild zu liefern:

1. **Text neben den Figuren**, solange er dort in mindestens 100 px passt. Sonst läuft er über die volle Breite, bei Wortteilen mit Bindestrich zu einem Wort verbunden („ANFECHTUNGS-“ + „KLAGE“), und die Figuren werden so weit verkleinert, dass Kopf und Oberkörper unter den Text passen.
2. **Lernvorlage:** Bliebe unter dem Text weniger als 380 px für die Karte, wechselt der Text auf die volle Breite. Die Karte steht am linken Rand und wird so groß wie der freie Raum. Ein Mittelmotiv kommt nur dazu, wenn es mindestens 200 px groß werden kann; Kleinkram wird weggelassen.
3. **Prüfungen:** Text und Figuren berühren sich nicht (echte Maske inklusive Kontur und Schatten); keine Figur ist seitlich angeschnitten; freie Motive überlappen weder Text noch Figuren noch gehaltene Gegenstände (14 px Abstand); gehaltene Gegenstände liegen vollständig im Bild; der Text ragt nicht über den Rand; Figuren werden nicht kleiner als 600 px Gesamthöhe (sonst Text kürzen).
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
  "varianten": {"B": {"text": ["*KATZEN-", "KÖNIG"]}}
}
```

- `text`: Zeilen wie gewünscht umbrochen, `*` vor dem gelben Wort; ein Zeilenende auf `-` verbindet zum Wort, wenn der Text einzeilig über die volle Breite läuft (Präfixe bis 3 Zeichen behalten den Bindestrich: „ZV-GRUNDSCHEMA“).
- `karte` (nur `lern`): Kartenkopf, siehe oben.
- `figuren`: Teile aus der Open-Peeps-Bibliothek (`openpeeps-erweiterung/figma-bibliothek`, siehe README dort) oder `{"lexi": "erklaert_auf", "spiegeln": true}` für die Moderatorin. Optional `gross` (Größenfaktor) und `sichtbar` (sichtbarer Anteil der Figur, Standard 0,6). Die erste Figur der Liste steht rechts außen und zuvorderst. Für gehaltene Gegenstände Posen mit ausgestrecktem Arm nehmen (`robot_dance-1`, `shirt-1`); `pointing_finger` hat schwarze Kleidung.
- `haelt`: Emoji, Größe `g` in px, `drehung` in Grad, `hand` `links`/`rechts` (Bildseite), `spiegeln` z. B. damit ein Messer am Griff gehalten wird.
- `motiv`: `{"emoji": "shield"}` oder zusammengesetzt `{"teile": [[name, anteil, dx, dy, drehung], …]}`, `g` = Zielgröße (Fall 420, Lern 300; wird bei Platzmangel kleiner).
- `layout` (selten nötig): `fig_links` (Beginn der Figurenzone, 650), `hoehe` (Figurenhöhe, 1000), `ueberlappung` (0,62).
- `varianten`: geänderte Felder für die Test-&-Compare-Varianten; Ausgabe als `<k>_B.jpg`.

## A/B-Test

Pro Folge zwei Varianten, in YouTube Studio über „Test & Compare“ gegeneinander getestet. Getestet wird ein **Prinzip**, keine Kleinigkeit: Frage gegen Fallname („WER IST TÄTER?“ gegen „KATZENKÖNIG“), Norm gegen Merkfrage („§ 224 STGB“ gegen „SCHUH = WAFFE?“), Thema gegen Aufforderung („NOTWEHR § 32“ gegen „NOTWEHR PRÜFEN“). Ergebnisse (Winner/Preferred/gleich) je Format sammeln und die Vorlagen danach nachschärfen.

## Benutzung

```sh
youtube/thumbnails/assets_holen.sh                 # einmalig: Emoji-Satz laden (npm, nicht im Repository)
python3 youtube/thumbnails/thumbnail.py youtube/thumbnails/beispiele.json --out AUSGABE --vorschau
```

`--vorschau` erzeugt zusätzlich einen Kontaktbogen und eine Handy-Feed-Ansicht (246 × 138 px mit Zeitstempel), `--nur k1,k2` rendert einzelne Folgen. Die fertigen JPGs gehören zum Upload bzw. in den Produktionsmaster auf Drive, nicht ins Repository. Pfade lassen sich mit `LEXVERSE_FONT`, `LEXVERSE_EMOJI` und `LEXVERSE_THUMB_CACHE` umstellen. Abhängigkeiten: Pillow (mit variablen Schriften), NumPy, SciPy, cairosvg, svgpathtools.
