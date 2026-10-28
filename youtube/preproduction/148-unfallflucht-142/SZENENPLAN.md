# Folge 148 · Unfallflucht § 142: Wie lange muss ich warten? Zettel reicht nicht – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_148.py`](src/skript_148.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · StGB BT, Themenplan-Format „Schema“. Fall nach dem Plan-Hook („Eine Autofahrerin schrammt nachts beim Ausparken ein anderes Auto, klemmt einen Zettel unter den Scheibenwischer und fährt weiter“): Gerlinde parkt kurz vor Mitternacht auf einem öffentlichen Parkplatz aus, schrammt das Auto von Bernhard (Schramme an der Tür, rund 400 €), schreibt Name und Telefonnummer auf einen Zettel, klemmt ihn unter den Scheibenwischer und fährt sofort weiter; am Morgen findet Bernhard Schramme und Zettel. Ablauf: Fall → Fragen → Sachverhalt → Wortlautkarte § 142 Abs. 1 → I. 1. Unfall im Straßenverkehr → I. 2. Unfallbeteiligte (Wortlautkarte Abs. 5) → I. 3. Entfernen: Nr. 1 / Nr. 2 Wartepflicht (Faktoren, OLG Dresden) → Zettel, I. 4. Vorsatz → Wortlautkarten Abs. 2 und Abs. 3 S. 1 → Abs. 2 Nr. 2 und BVerfG (Gegenvariante) → Wortlautkarte Abs. 4 (tätige Reue) → Ergebnis → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 5:48,7.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gerlinde, um 60 | parkt aus, schrammt, lässt einen Zettel da, fährt weiter | `standing/robot_dance-3` (Oberteil Rot `#F07A6A`, Hose Anthrazit `#3A3A48`, weiße Schuhe, offene Handgeste), Kopf `Gray Bun`, Brille `Glasses 3`, Haut `#F0CDB4`. Mimiken `Fear` (Schreck beim Kratzer), `Calm` (redet), `Solemn`, `Suspicious`, `Concerned|Serious`, `Tired` (Ergebnis). Auto Rot | `hilde` (Frau, älter) |
| Bernhard, um 45 | Halter des geschrammten Autos, findet Schramme und Zettel | `standing/walking-3` (schwarzes Shirt und Hose, weiße Schuhe, gehend), Kopf `Pomp` (dunkel), Haut `#E2B08C`, kein Bart, keine Brille. Mimiken `Suspicious` (findet), `Serious` (redet, ernst), `Concerned|Serious`, `Solemn`, `Calm`. Auto Blau | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Blickrichtung:** Alle Posen blicken im Original nach rechts (Kontaktbild `out/besetzung_148.png`); Grundansicht gespiegelt (nach links), `_r` nach rechts. Parkplatz: Bernhards Auto steht links in der hinteren Reihe, Gerlinde steigt rechts davon aus und blickt nach links zur Tür; am Morgen steht Bernhard rechts neben seinem Auto und blickt nach links zur Schramme. Tafelszenen: Figuren rechts, blicken nach links. **Sachlich:** keine bösen Mimiken, keine Karikatur, keine Prothesen-Posen. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `GL_redet`, `BE_redet` (je links/rechts) und Lexi. **Stimmen** nur aus dem Pool (hilde, christian; stephan und lucy nicht benötigt, stephan also nie mit christian in einer Szene); Vorfolgen 146 (lucy, stephan) und 147 (helmut) nutzten andere Stimmen. **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und als Figurenname in keinem Skript, Szenenplan oder Abnahmebogen unter `youtube/preproduction/` (Volltextsuche 04.10.2026): Gerlinde, Bernhard (nie im Genitiv gesprochen). Figuren-PNGs: `../peeps/op_148/` (46 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 145 (`resting-1`, `easing-1`, `crossed_arms-1`, `blazer-3`), 146 (`resting-1`, `crossed_arms-1`), 147 (`pointing_finger-2`, `easing-2`), 140 (`crossed_arms-1`, `walking-1`; Landstraße über eine Kuppe), 130 (Kontrollstelle am Ortsausgang), 124 (Dorfstraße). 148: **öffentlicher Parkplatz in Seitenansicht** (Asphaltfläche mit schrägen Buchtenstrichen, P-Schild, Laterne mit Lichtkegel) – neue Kulisse; Posen `robot_dance-3`, `walking-3` in 145–147 nicht verwendet; keine Polka Dots, keine Bärte. **Nacht** in Szene A1, weil der Fall nachts spielt und gerade die Leere des Parkplatzes (niemand feststellungsbereit) die Wartepflicht trägt; A2 kehrt am Morgen an denselben Ort zurück (Bernhard findet Schramme und Zettel).

## Szenen (Cremegrund, A1 Nachtverlauf)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Nachts auf dem Parkplatz** `fall`→`weg` | Nachtverlauf, Mond, Laterne mit Lichtkegel, P-Schild; Bernhards blaues Auto (hinten) und Gerlindes rotes Auto in der Parkbucht ab 0,0 s; Gerlinde parkt aus (1,2 s), streift Bernhards Auto (Kratzspur), fährt weiter vor (1,0 s) und hält; Ring um die Schramme; Gerlinde steigt aus (Schreck), redet (Blase), Zettel unter dem Scheibenwischer; sie steigt ein, ihr Auto fährt weg (0,6 s) | tabler:`car` (Blau, Rot), `parking` (Blau), `note` (Weiß); `mond()`, `laterne()`, `lichtkegel()` (ostil), `parkplatz()`, `schramme()`, `ring()` | `Fall · Nachts auf dem Parkplatz` (ab 0,0 s) → `· Gerlinde parkt aus` → `· Die Schramme` → `· Niemand zu sehen` → `· Der Zettel` → `· Gerlinde fährt weiter` | Kulisse ab 0,0 s · Ausparken · Kratzspur + „schrammt das Auto von Bernhard“ · Ring + „lange Schramme an der Tür“ · Gerlinde + „weit und breit niemand“ · Blase · Zettel + Pille · „fährt sofort weiter“, Wegfahren · leere Bucht | Kratzen (`szene_148kratzer_1`, Freesound CC0 337843), Wegfahren (`szene_148wegfahrt_1`, Freesound CC0 119829); kein Aufprall |
| **A2 Am nächsten Morgen** `morgen`→`frage2` | derselbe Parkplatz bei Tag; Bernhards Auto mit Schramme und Zettel; Bernhard rechts | tabler:`car`, `parking`, `sun`, `trees`, `note` | `Fall · Am nächsten Morgen` → `Fall · Die Frage` | Bernhard · Ringe um Schramme und Zettel · Blase · zwei Fragepillen | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut Abs. 1** `p142`→`nr2` | **Wortlautkarte § 142 Abs. 1 (vollständig)**, fünf Marker; beide Figuren | tabler:`book`, `user`, `hourglass` | `§ 142 StGB › Wortlaut Abs. 1` → `› Abs. 1 Nr. 1: Anwesenheit` → `› Abs. 1 Nr. 2: Wartepflicht` | Karte + Marker | – |
| **D I. 1. Unfall** `unfall`→`schr` | Tafel mit Definition, Haken Parkplatz, belangloser Schaden, grüner Block; Bernhard | tabler:`car`, `parking`, `coin`, `currency-euro` | `… › I. 1. Unfall im Straßenverkehr` → `› Parkplatz` → `› nicht völlig belanglos` → `(+)` | Zeile für Zeile | – |
| **E I. 2. Abs. 5** `abs5`→`ger5` | **Wortlautkarte Abs. 5**, zwei Marker, Haken; Gerlinde | tabler:`book`, `car` | `… › I. 2. Unfallbeteiligte, Abs. 5` → `› Gerlinde (+)` | Karte + Marker, Haken | – |
| **F I. 3. Entfernen** `entf`→`null` | Tafel Nr. 1 (Kreuz „niemand da“), Nr. 2 Wartepflicht, Faktoren, gelber Block OLG Dresden, Kreuz „gar nicht gewartet“; Gerlinde | tabler:`car`, `user`, `moon`, `hourglass`, `clock` | `… › I. 3. Entfernen › Nr. 1 …` → `› Nr. 2: Wartepflicht` → `› angemessene Zeit` → `› Gerlinde: nicht gewartet` | Zeile für Zeile | – |
| **G Zettel, Vorsatz** `zett`→`vors` | Tafel „Und der Zettel?“, Kreuz „kein Ersatz“, lila Block Vorsatz; Bernhard | tabler:`note`, `users`, `note-off`, `id` | `… › Zettel? › nur zwei Wege` → `› kein Ersatz` → `› I. 4. Vorsatz (+)` | Zeile für Zeile | – |
| **H1 Abs. 2** `abs2` | **Wortlautkarte Abs. 2**, Marker Nr. 1; Gerlinde | tabler:`hourglass`, `phone-call` | `… › Abs. 2 Nr. 1: nach der Wartefrist` | Karte + Marker, Zeilen | – |
| **H2 Abs. 3** `abs3`→`nurtel` | **Wortlautkarte Abs. 3 S. 1**, sieben Marker, Haken/Kreuz | tabler:`phone-call`, `id`, `car`, `hourglass`, `note` | `… › Abs. 3: nachträglich ermöglichen` → `› Meldung nach dem Warten` → `› Zettel nur Name, Telefon` | Marker Wort für Wort | – |
| **I Abs. 2 Nr. 2, BVerfG** `abs22`→`gegen` | Wortlautkarte Abs. 2 (Marker Nr. 2), Kreuz, Fundstellen, lila Block Gegenvariante | tabler:`book`, `eye-off`, `scale` | `… › Abs. 2 Nr. 2 …` → `› unbemerkter Unfall` → `› Analogieverbot, Art. 103 Abs. 2 GG` → `Gegenvariante: nicht bemerkt` | Zeile für Zeile | – |
| **J Abs. 4** `abs4`→`vier` | **Wortlautkarte Abs. 4**, zehn Marker, zwei Haken | tabler:`heart-handshake`, `parking`, `coin`, `clock-24`, `scale` | `… › Abs. 4: tätige Reue` → je Voraussetzung → `› Parkunfall` → `› 400 €: nicht bedeutend` | Marker zum Wort | – |
| **K Ergebnis** `rws`→`erg2` | Haken II./III., gelber Block § 142 Abs. 1 Nr. 2, Ausblick, lila Block Abs. 4; beide | tabler:`gavel`, `phone-call` | `II. Rechtswidrigkeit · III. Schuld` → `Ergebnis · § 142 Abs. 1 Nr. 2 StGB` → `Ergebnis · Ausblick …` | 7 | – |
| **L Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | je Punkt | 4 Punkte | – |
| **M Prüfschema** `sch`→`s3` | breite Karte, grüner Kasten Entfernen/Abs. 2 | – | je Gliederungspunkt | 9 Aufbaustufen | – |
| **N Merksatz** `merke`→`m3` | Lexi erklärt (redet), drei Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`, stiller Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („400 €“, „10 Minuten“, „24 Stunden“, „§ 142 Abs. 1 Nr. 2“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur in A1 (Gerlindes Auto als Folge kurzer Positionen, Icon nicht umgezeichnet).
**Darstellung:** kein Aufprall, keine Verletzten; das Streifen ist eine Vorbeifahrt mit Kratzspur und Ring. Fahrzeuge neutral (Tabler-Icon, keine Marke, kein Kennzeichen).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Klausurtipp Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Parkplatz, Kratzspur, Laterne, Mond und Lichtkegel aus Grundformen (`parkplatz()`, `schramme()` in `folien_148.py`; `laterne()`, `mond()`, `lichtkegel()` aus `etb2/src/ostil.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Gerlinde parkt kurz vor Mitternacht auf einem öffentlichen Parkplatz aus. Dabei schrammt sie das geparkte Auto von Bernhard; an der Tür bleibt eine lange Schramme, die Reparatur kostet rund 400 €. Gerlinde bemerkt das sofort. Weit und breit ist niemand zu sehen.
>
> Sie schreibt ihren Namen und ihre Telefonnummer auf einen Zettel, klemmt ihn unter den Scheibenwischer und fährt sofort weiter.
>
> Am nächsten Morgen findet Bernhard die Schramme und den Zettel.
>
> **Strafbarkeit von Gerlinde nach § 142 StGB? Wie lange hätte sie warten müssen?**
