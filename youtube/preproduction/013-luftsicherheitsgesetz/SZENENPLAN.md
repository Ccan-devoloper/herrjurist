# Folge 013 · Luftsicherheitsgesetz: Darf der Staat ein Flugzeug abschießen? – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_013.py`](src/skript_013.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Erfundener Entführungsfall unter § 14 III LuftSiG a. F. → Verfassungsbeschwerde eines Vielfliegers → A. Zulässigkeit → B. Begründetheit (Schutzbereich Leben, Eingriff, Rechtfertigung: formell Wehrverfassung mit Plenum 2012, materiell Menschenwürde mit Einwänden und Schutzpflicht) → Ergebnis → Gegenfall nur Täter an Bord → Rechtslage heute (§ 15a LuftSiG, Drohnen) und Strafrecht (offen, Streit) → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Verteidigungsminister Lorenz (LO), um 60 | muss über den Abschuss entscheiden (fiktiv, keine reale Person) | Pose `standing/blazer-3`, Kopf `Gray Short`, Brille `Glasses 4`; Jackett Blau `#8DB3F2`, Hose `#3D3D58`, Haut `#E6B48F`; Mimiken `Calm`, `Serious` (redet), `Solemn` (denkt), `Concerned|Serious` (Sorge) | `helmut` (Mann, älter) |
| Die Pilotin (PI), um 30 | Pilotin der Alarmrotte, meldet per Funk | Brustbild `body/Sporty Tee` im Funkbild, Kopf `Bun`; Oberteil Grün `#8FD694` (Saum), Haut `#8D5A3B`; Mimiken `Calm`, `Serious` (redet) | `lucy` (Frau, jung) |
| Herr Seiler (SE), um 45 | Vielflieger, Beschwerdeführer | Pose `standing/resting-2`, Kopf `Short 4`, Brille `Glasses 2`; Hose Lila `#B8A9F5`, Haut `#C58E64`; Mimiken `Calm`, `Driven` (redet), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Smile` (froh) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel bzw. Szene, `_r` blickt nach rechts (nicht verwendet).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `LO_redet`, `PI_redet`, `SE_redet` und Lexi.
- Keine Bärte (kein Bart über dem Mund); keine Prothesen-Posen.
- Stimmen nur aus dem zugeteilten Pool (helmut, lucy, stephan; julia nicht benötigt).
- **Namen mit eindeutig deutscher Aussprache:** Lorenz, Seiler (gesprochen nur von der Erzählerin); die Pilotin bleibt ohne Namen.
- Abweichung vom Plan-Hook („die Ministerin“): ein Minister, weil der Pool keine Frauenstimme mittleren Alters enthält.
- Figuren-PNGs: `../peeps/op_013/` (48 Dateien, nicht im Repository, im Drive-Master).

**Sensibles Thema (Terroranschlag, Tod Unbeteiligter):**
- Flugzeuge nur als Linien-Icon (tabler `plane`), keine Passagiere als Figuren an Bord, keine Explosion, kein Treffer.
- Abschuss nur als Frage: rot gestrichelter Pfeil mit Fragezeichen (Szene A: angekündigter Kurs auf das Stadion; Szene C: „Darf ich den Abschuss befehlen?“).
- Kein realer Anschlag im Bild oder Ton, keine realen Politiker.
- Geräusche ohne Waffen- oder Explosionsklang.

**Abweichung von den letzten Folgen:**
- 004: Ministerbüro/Parteitag; 007: Wohnhaus; 008: Stadtpark (Grundrechtsprüfung).
- Hier: Himmel mit Wolken, Alarmrotte mit Funkbild, Lagezentrum, Flughafen; erstmals Menschenwürde/Objektformel und Wehrverfassung.
- Drei neue Figuren. Stimmen helmut, lucy und stephan waren in 004 und 008 nicht besetzt.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Entführung** `lage`→`drohung` | Himmel; Passagierflugzeug fliegt ins Bild; Stadion am Boden rechts | tabler:`cloud` ×3 (Weiß), tabler:`plane` (Weiß, Bewegung), tabler:`alert-triangle` (Rot), tabler:`building-stadium` (Grün); Pillen „auf dem Weg nach Berlin“, „140 Menschen an Bord“, „in der Gewalt von Entführern“, „volles Fußballstadion“; Fragepfeil | `Fall · Die Entführung` (ab 0,0 s) | Himmel · Flugzeug fliegt ein · Berlin · 140 · Entführer · Stadion · Kurs-Pfeil mit „?“ | – |
| **B Die Alarmrotte** `jets`→`p1` | zwei Kampfflugzeuge steigen auf und fliegen neben die Maschine; Funkbild der Pilotin rechts | tabler:`plane` (Weiß + 2× Grau, Bewegung), tabler:`cloud`, tabler:`headset` (Gelb), Karte als Funkbild (Hellblau); Pillen „Luftwaffe“, „warnen“, „abdrängen“, „Pilotin“ | `Fall · Die Alarmrotte` | Maschine · Jets steigen auf · Luftwaffe · warnen · abdrängen · Funkbild · Pilotin redet, Blase „Keine Reaktion. Die Maschine hält Kurs auf das Stadion.“ | Jet beim Aufsteigen (`szene_013jet_1`), Funkrauschen beim Funkbild (`szene_013funk_1`) |
| **C Die Entscheidung** `minister`→`einzig` | Lagezentrum: Schreibtisch mit Radarbildschirm, Lorenz rechts | tabler:`desk` (Gelb), `device-desktop`, `radar-2` (Grün), `plane` (Weiß/Grau) + Fragepfeil, `book` (Gelb); Karte „Luftsicherheitsgesetz (2005)“ | `Fall · Die Entscheidung` | Lagezentrum · Name · Lorenz redet, Blase „140 an Bord, 50.000 im Stadion. Darf ich den Abschuss befehlen?“ · Fragepfeil · Gesetzeskarte · § 14 III · „als einziges Mittel“ | – |
| **D Der Vielflieger / Die Frage** `seiler`→`frage` | Flughafen links, Koffer, Seiler rechts | tabler:`building-airport` (Blau), `plane-departure`, `luggage` (Lila), `calendar-repeat`, fluent-hc:`classical-building` „Karlsruhe“ | `Fall · Der Vielflieger` → `Fall · Die Frage` | Seiler · „fast jede Woche“ · Seiler redet, Blase „Dann dürfte der Staat auch mein Flugzeug abschießen. Dagegen wehre ich mich in Karlsruhe.“ · Karlsruhe · drei Frage-Pillen | – |
| **E Sachverhalt** `sv` | Sachverhaltskarte vollständig, ≈ 10 s (5 s Lesepause) | – | `Sachverhalt` | 1 | – |
| **F Zulässigkeit** `zul`→`oft` | Tafel links, Seiler rechts | classical-building, `file-text` „§ 14 III LuftSiG“, `plane-departure`, `calendar-repeat` | `A. Zulässigkeit › Verfassungsbeschwerde, Art. 94 I Nr. 4a GG` → `› Beschwerdegegenstand: Gesetz` → `› Beschwerdebefugnis` | Zeilen je Merkmal, Haken bei „hinreichend wahrscheinlich“ (≈ 9 Halte) | – |
| **G Schutzbereich, Eingriff, Schranke** `sb`→`jeder` | Tafel, Seiler | `activity-heartbeat` (Rot), `plane`, `book` „Gesetz“ | `B. Begründetheit › I. Schutzbereich: Leben, Art. 2 II 1 GG` → `› II. Eingriff` → `› III. Rechtfertigung: Gesetzesvorbehalt` | ≈ 8 Halte | – |
| **H Formell: Wehrverfassung** `formell`→`plenum` | Tafel, Lorenz klein rechts | `shield` „Bundeswehr“ (Grau), `alert-triangle` „Unglücksfall“, `plane` (Grau) + Kreuz, classical-building „Plenum 2012“ | `B. › III. 1. formell: Wehrverfassung` → `… Art. 87a II GG` → `… Art. 35 II 2, III GG` → `… Plenum 2012` | Kreuz bei „erlaubt … nicht“, Block Plenum (≈ 9 Halte) | – |
| **I Materiell: Menschenwürde** `mw`→`objekt2` | Tafel, Seiler | `user-shield` (Gelb), `plane`, `building-stadium`, `box` „Objekt?“ | `B. › III. 2. materiell: Menschenwürde, Art. 1 I GG` | Objektformel, ausweglos, Mittel zur Rettung, roter Block (≈ 7 Halte) | – |
| **J Einwände** `ohnehin`→`einw` | Tafel, Seiler | `hourglass`, `box`, `ticket` | `B. › III. 2. materiell: Einwände` | drei Einwände mit Kreuz (≈ 7 Halte) | – |
| **K Schutzpflicht, Ergebnis** `schutz`→`nichtig` | Tafel, Seiler | `building-stadium` + `shield`, classical-building, `gavel` | `B. › III. 2. materiell: Schutzpflicht` → `B. Begründetheit › Ergebnis` | ≈ 5 Halte, grüner Ergebnisblock | – |
| **L Gegenfall nur Entführer** `taeter`→`trotzdem` | Tafel, Lorenz | `plane` „nur Entführer“, `scale` | `Gegenfall · Nur Entführer an Bord` | drei Haken, roter Block „Trotzdem ganz nichtig“ (≈ 6 Halte) | – |
| **M Heute und Strafrecht** `heute`→`streit` | Tafel, Lorenz | `plane` „Menschen an Bord“, `drone` „unbemannt“ (Grau), `scale` | `Rechtslage heute · LuftSiG (Stand 2026)` → `Rechtslage heute · § 15a LuftSiG` → `Strafrecht · offen gelassen` | ≈ 8 Halte | – |
| **N Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Würde vor Abwägung` | 3 Zeilen | – |
| **O Klausurschema** `sch`→`k7` | Schema baut sich auf | – | `Klausurschema` | A, Befugnis, B, I., II., III., 1., 2., (−)/(+) | – |
| **P Merksatz** `merke`→`m2` | Lexi erklärt, Merksatz mit Marker | – | `Merksatz` | Satz 1, Marker, Satz 2, Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim einfliegenden Passagierflugzeug und den aufsteigenden Kampfflugzeugen.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_013jet_1`, `szene_013funk_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Entführer bringen ein Passagierflugzeug mit 140 Menschen an Bord in ihre Gewalt und kündigen an, es in ein volles Fußballstadion zu steuern. Zwei Kampfflugzeuge der Luftwaffe warnen die Maschine und versuchen, sie abzudrängen; ohne Erfolg. Verteidigungsminister Lorenz fragt sich, ob er den Abschuss befehlen darf. § 14 Abs. 3 LuftSiG (Fassung 2005) erlaubt, als einziges Mittel mit Waffengewalt auf ein Flugzeug einzuwirken, das gegen das Leben von Menschen eingesetzt werden soll.
>
> Herr Seiler fliegt fast jede Woche. Er erhebt Verfassungsbeschwerde unmittelbar gegen § 14 Abs. 3 LuftSiG.
>
> *(Frei nach BVerfGE 115, 118 – 1 BvR 357/05; Personen erfunden.)*
>
> **Ist die Verfassungsbeschwerde zulässig und begründet?**

## Hinweis zu Blasentext und Ziffern

Blasen schreiben Zahlen als Ziffern („140 an Bord, 50.000 im Stadion.“), gesprochen „Hundertvierzig …, fünfzigtausend …“. Sonst ist der Blasentext wortgleich mit dem Gesprochenen.
