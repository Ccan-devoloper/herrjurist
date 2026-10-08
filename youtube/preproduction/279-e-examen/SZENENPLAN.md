# Folge 279 · E-Examen Jura: Klausuren am Computer schreiben – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_279.py`](src/skript_279.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Examen. Rahmen nach dem Plan-Hook („Statt Stift jetzt Tastatur – was ändert sich wirklich?“): In einem fiktiven Prüfungssaal stehen Laptops auf den Tischen. Die Jurastudentin Telse (Nordrhein-Westfalen) schreibt bald ihre Examensklausuren; ihr Bruder Jost hat das zweite Examen in Bayern schon am Laptop geschrieben. Aufbau nach Auftrag: Hook → Sachverhalt → Was ist das E-Examen (Wortlautkarte § 5d Abs. 6 DRiG, Tafel mit den geprüften Ländern NRW und Bayern) → Was ändert sich (Gliederung, Korrigieren und Umstellen, Rechtschreibprüfung, Zeit, Lesbarkeit) → Was bleibt (Papier, Gesetzestexte als Bücher, Gutachtenstil, Schwerpunkte) → Vorbereitung (Probeklausuren am Rechner, zehn Finger, Demoportale, Tastatur) → Ergebnis (Saal) → Klausurtipp (Lexi) → E-Examen in 5 Schritten → Merksatz (Lexi).
**Länge:** Hauptfilm ≈ 5:04 (4.337 vertonte Zeichen), im Regelrahmen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Telse (TE/TS), Anfang 20 | Jurastudentin in NRW, bald Pflichtfachprüfung | stehend `standing/robot_dance-3` (offene Geste; Oberteil Lila `#B8A9F5`, Hose Schwarz `#151515`, weiße Schuhe), sitzend am Laptop `sitting/mid-2` (Oberteil Lila, schwarze Hose der Pose) – gleiche Kleidung; Kopf `Long Bangs` (schwarzes Haar, nicht einfärbbar), Haut `#F2CBA8`, keine Brille, kein Bart; Mimiken `Suspicious` (denkt), `Concerned\|Serious` (Sorge, redet t1), `Smile`, `Smile Big\|Smile` (lacht), `Awe` (staunt), `Driven`, `Calm` (sitzend redet t2) | `ela_froh` (Frau, jung, fröhlich) |
| Jost (JO), Ende 20 | Bruder, 2. Examen in Bayern am Laptop | `standing/blazer-4` (Sakko Petrol `#8CCBC0`, Shirt Weiß, schwarze Hose der Pose), Kopf `Short 1` (schwarzes Haar), Haut `#B07552`, keine Brille, kein Bart; Mimiken `Calm` (redet j1), `Smile` (redet j2/j3), `Serious`, `Suspicious` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Beide Posen blicken im Original nach rechts. Grundansicht gespiegelt = blickt nach links (Jost im Saal, alle Tafelszenen), `_r` = blickt nach rechts (Telse im Saal zu den Laptops und zu Jost; sitzend zum Laptop).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `TE_redet`, `TE_redet2`, `TS_redet`, `JO_redet`, `JO_redetfroh` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur, kein Klischee (Telse neugierig und planvoll, Jost hilfsbereit, kein Besserwisser).
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: Telse `ela_froh` (julia war Vorfolge 273), Jost `niklas` (einzige junge Männerstimme im Pool). `helmut` (älter) passt zu keiner Rolle.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht in `namen_reserviert.txt`, Volltextsuche (`*.py, *.md, *.json, *.csv, *.txt, *.srt`) unter `youtube/preproduction` und `youtube/themenplanung` am 08.10.2026: Telse 0, Jost 0 Treffer (verworfen: Ida, Ortwin, Hilde, Hanne, Lothar – schon in Dateien; Liselotte – zu nah an „Lotte“; Arnold – englische Lesart möglich). Reservierung „279: Telse, Jost“ vor der Vertonung angehängt. Kein Genitiv eines Namens („die Ausgangslage von Telse“).
- Präfixe `TE_`/`TS_`/`JO_` (nie `ER_`). Figuren-PNGs: `../peeps/op_279/` (76 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 273–277 verglichen; 278 hat noch kein Figurenrezept): 273 (`crossed_arms-2`, `shirt-4`), 274 (`easing-2`, `resting-2`), 275 (`shirt-3`, `robot_dance-2`), 276 (`easing-2`, `pointing_finger-2`), 277 (`blazer-2`, `easing-1`). 279: `robot_dance-3`, `blazer-4`, `sitting/mid-2` – dort nicht verwendet; lila Oberteil und petrolfarbenes Sakko dort nicht. Schauplatz neu: **fiktiver Prüfungssaal mit zwei Tischen, Laptops (Tabler `device-laptop`) und Gesetzesbüchern (Tabler `books`)** – nicht der Fakultätsflur aus 273. Leitmotiv: Laptop im Saal → Bildschirm-Skizze (Gliederung, Umstellen, Rechtschreibung) → Ausdruck mit Korrekturrand → Telse tippt am Laptop. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Prüfungssaal** `fall`→`j1` | Saal: zwei Tische mit Laptop und Büchern; Telse links (blickt nach rechts), Jost kommt rechts dazu | tabler:`device-laptop`, `books`; Tische programmatisch; Ring um die Laptops | `Fall · Prüfungssaal kurz vor dem Examen` → `· tippen oder mit der Hand schreiben?` → `· mehr als die Tastatur, das Wichtigste bleibt` | ab 0,0 s Saal mit Telse und Schild · Ring · Pille NRW · Jost mit Schild · Pille Bayern · Blase t1 · Pille „Hand oder Laptop?“ · Blase j1 | – |
| **A2 Einstieg** `hook`→`wie` | Tafel: Stift → Tastatur, „E-Examen: Examensklausuren am Computer“, 4 Fragen | tabler:`pencil`, `keyboard`, `device-laptop`, `list-check` | `Einstieg · statt Stift jetzt Tastatur` → … | ≈ 9 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt · Die Ausgangslage von Telse` | 1 | – |
| **C Rechtsgrundlage** `was`→`land` | Wortlautkarte § 5d Abs. 6 DRiG, Marker „Landesrecht“, „elektronisch“, „dürfen“ synchron; „Ob und wie: Das entscheidet dein Land“ | tabler:`help`, `book`, `device-laptop`, `map-pin` | `Rechtsgrundlage · Wo ist das E-Examen geregelt?` → … | ≈ 9 | – |
| **D Länder** `nrw`→`beide` | Tafel NRW / Bayern zeilenweise in Sprechreihenfolge mit Fundstellen; Haken „gestellter Laptop, kein eigener“ | tabler:`map-pin`, `arrows-exchange`, `lock`, `device-laptop` | `Länder › NRW: …` → `› Bayern: …` | ≈ 9 | – |
| **E1 Was ändert sich** `aend`→`j2` | Tafel links, Bildschirm-Skizze rechts (Gliederung A./I./1., markierter Absatz mit Pfeil, Wellenlinie unter „Gutachten“); Haken/Kreuz NRW/Bayern; Blase Jost | tabler:`device-laptop`, `list-numbers`, `arrows-move-vertical`, `text-spellcheck` | `Was ändert sich · …` → `› 1. Gliederung` → `› 2. Korrigieren und Umstellen` → `› Rechtschreibprüfung` → `› selbst Korrektur lesen` | ≈ 12 | – |
| **E2 Zeit und Lesbarkeit** `zeit`→`les2` | Bayern keine Uhr (Kreuz), Hinweis, Abgabe per Klick, NRW automatisch gespeichert (Haken); Lesbarkeit; Ausdruck-Skizze mit Korrekturrand | tabler:`clock-off`, `click`, `device-floppy`, `eye`, `printer` | `Was ändert sich › 3. Zeit` → … → `› Bayern: Ausdruck mit Korrekturrand` | ≈ 11 | – |
| **F Was bleibt** `bleibt`→`mehr` | Haken Aufgabentext/Gesetzestexte, „2. Examen NRW: auch Kommentare“, Kreuz „nicht elektronisch“; Pillen Gutachtenstil/Argumente/Schwerpunkte; „Mehr Text ist nicht automatisch besser“ | tabler:`shield-check`, `file-text`, `books`, `scale`, `target` | `Was bleibt · gleich?` → … | ≈ 11 | – |
| **G Vorbereitung** `vorb`→`tast` | Probeklausuren am Rechner, 10 Finger, Demoportal NRW/Bayern nebeneinander, Tastatur Bayern | tabler:`school`, `writing`, `keyboard`, `device-laptop` | `Vorbereitung · …` → … | ≈ 13 | – |
| **H Ergebnis** `erg`→`j3` | zurück in den Saal (Rückkehr, weil die Geschichte am Laptop schließt): Telse setzt sich auf einen Hocker an den Laptop (sitzende Pose, gleiche Kleidung) und tippt – Zeilen erscheinen auf dem Bildschirm; Blasen Telse und Jost | wie A1, Hocker programmatisch | `Ergebnis · Telse probiert den Laptop aus` → … | ≈ 7 | Tippen (`szene_279tippen_1`) |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Konzeptpapier → Laptop, „Schwerpunkte markieren“, Lexi warnt | tabler:`clipboard-text`, `device-laptop`, Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | ≈ 6 | – |
| **J Schema** `sch`→`k5` | breite Karte, I.–V. Punkt für Punkt | – | `E-Examen · 5 Schritte` → `› I. …` … | 6 | – |
| **K Merksatz** `merke`→`m3` | Lexi erklärt, fünf Marker | – | `Merksatz` | 7 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Telse tippt), Freesound 215744 (CC0), Herkunft in `geraeusche_herkunft.json`.
**Darstellung:** fiktiver Prüfungssaal, Laptop-Symbole (Tabler), Bildschirm- und Ausdruck-Skizzen programmatisch, keine echten Logos, keine Software- oder Gerätemarken.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Telse studiert Jura in Nordrhein-Westfalen. Bald schreibt sie die Aufsichtsarbeiten der staatlichen Pflichtfachprüfung.
>
> Bisher hat sie alle Klausuren mit der Hand geschrieben.
>
> Ihr Bruder Jost hat das 2. Examen in Bayern schon am Laptop geschrieben.
>
> **Soll Telse am Laptop schreiben? Und was ändert sich dann für sie?**
