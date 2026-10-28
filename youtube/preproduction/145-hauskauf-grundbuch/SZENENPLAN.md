# Folge 145 · Hauskauf in drei Schritten: Kaufvertrag, Auflassung, Grundbuch – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_145.py`](src/skript_145.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Sachenrecht, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Ihr unterschreibt beim Notar – ab wann gehört euch das Haus eigentlich?“): Ute und Joachim kaufen von Herrn Ackermann (eingetragener Eigentümer) ein Haus. Bei einer Notarin werden Kaufvertrag und Auflassung im selben Termin erklärt; Herr Ackermann will zunächst „erst, wenn der Kaufpreis bezahlt ist“, die Notarin lehnt die Bedingung ab und sagt zu, die Eintragung erst nach Zahlung zu beantragen. Wochen später Fälligkeitsmitteilung, Zahlung, Antrag, Eintragung.

Ablauf: Fall (Notarin, Einigung, Unterschrift) → Wochen später / Frage → Sachverhalt → Aufbau (drei Schritte) → 1. Kaufvertrag (Wortlautkarte § 311b Abs. 1 S. 1, Zweck, § 125 S. 1) → Heilung (Wortlautkarte § 311b Abs. 1 S. 2), Trennungsprinzip (Verweis 005) → 2. Auflassung (Wortlautkarte § 925 Abs. 1 S. 1, S. 2, Vertretung, Regelfall) → § 925 Abs. 2 (Wortlautkarte), Rechtsklarheit → Kontrast Eigentumsvorbehalt (Verweis 139), Vorlagesperre → 3. Eintragung (Wortlautkarte § 873 Abs. 1, Zeitstrahl) → Zwischenzeit (Auflassungsvormerkung § 883, Fälligkeitsmitteilung) → Ergebnis (vor dem Haus) → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm ≈ 5:56 (5.071 Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ute, um 40 | Käuferin | `standing/resting-1` (Pullover Blau `#8DB3F2`, schwarze Hose), Kopf `Bangs` (Haar Braun `#6B4A2E`), Haut `#F1C9A8`; Mimiken `Calm`, `Smile` (redet), `Smile Big|Smile`, `Suspicious`, `Awe` | `sabrina` (Frau, mittel) |
| Joachim, um 40 | Käufer | `standing/easing-1` (offene Jacke Rot `#F07A6A`, Shirt Weiß, schwarze Hose), Kopf `Short 1`, Haut `#D9A07A`, kein Bart; Mimiken `Calm`, `Smile Big|Smile` (redet froh), `Smile`, `Suspicious`, `Awe`, `Concerned|Serious` | `marc` (Mann, mittel) |
| Herr Ackermann, um 65 | Verkäufer, eingetragener Eigentümer | `standing/crossed_arms-1` (Pullover Grün `#8FD694`, schwarze Hose), Kopf `No Hair 3`, Brille `Glasses 2`, Haut `#EDC3A3`, kein Bart; Mimiken `Old` (ruhig), `Serious` (redet streng), `Smile` (redet einlenkend), `Suspicious`, `Smile` | `william` (Mann, älter) |
| Notarin, um 50 | beurkundet, nimmt die Auflassung entgegen (ohne Namen, Namensschild „Notarin“) | `standing/blazer-3` (Blazer Lila `#B8A9F5`, Oberteil Schwarz, Hose Dunkelgrau `#3D3D48`), Kopf `Medium 3` (Haar Dunkelbraun), Brille `Glasses 3`, Haut `#C99470`; Mimiken `Calm`, `Smile` (redet), `Serious` (redet bestimmt), `Suspicious` | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep -rlw` über alle `.py/.md/.json` in `youtube/`: Ute 0, Joachim 0, Ackermann 0 Treffer; „Hannes“ und „Doris“ wegen Treffern verworfen) und nicht in der Koordinatorliste. Im Sprechtext kein Genitiv eines Namens („die Bedingung von Herrn Ackermann“).
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig; Vorfolge 144 (niklas, ela_froh) ohne Überschneidung. Erzählerin/Lexi Carla ohne Rolle.
- Präfixe `UT_`/`JO_`/`AK_`/`NO_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Bei der Notarin blickt Herr Ackermann (links) nach rechts, Ute und Joachim (rechts) nach links; die Notarin blickt zu den Käufern (rechts), bei ihrer Antwort an Herrn Ackermann nach links. Vor dem Haus blicken Ute und Joachim nach links zum Haus; in den Tafelszenen blicken alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `UT_redet`, `JO_redet`, `AK_streng`, `AK_redet`, `NO_redet`, `NO_streng` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. **Keine weiteren Menschen im Bild** (Grundbuchamt nur als Grundbuch-Symbol).
- **Abwechslung:** Posen nicht aus 142 (`easing-2`, `resting-2`), 143 (`shirt-4`, `easing-2`), 144 (`walking-2`, `shirt-3`) und nicht aus 139 (`robot_dance-3`, `pointing_finger-2`); keine Polka Dots. Figurenrezepte verglichen.
- Figuren-PNGs: `../peeps/op_145/` (94 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `besetzung_145.png` im Master.

**Abweichung von den letzten Folgen:** 142 (Nachbargrundstück, Beseitigung), 143 (Flughafen, Versammlung), 144 (Laden/Verfügungsbewusstsein); 139 (Möbelhaus/Wohnzimmer). 076 hatte einen kurzen Notartermin mit Unterschrift-Symbol als eine von drei Stationen; hier ist der Notartermin der Hauptschauplatz mit Tisch, vier Figuren und Dialog über die Bedingung, dazu eine Hausszene „Wochen später“ mit gelbem Haus, Baum und Grundbuch-Symbol. Leitmotive: **gelbes Haus** (Phosphor `house`) und **blaues Grundbuch** (Tabler `book-2`), Zeitstrahl „Unterschrift → Eintragung“. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Bei der Notarin** `fall`–`jo1` | ab 0,0 s Ute und Joachim mit Namensschildern, Haus und Pille „Ute und Joachim kaufen ein Haus“; Herr Ackermann bei „gehört“, Pille „Eigentümer im Grundbuch“ und Grundbuch; Notarin hinter dem Tisch bei „Zu dritt“; Kaufvertrag auf dem Tisch bei „liest“; Blasen Notarin (Frage), Ackermann (Bedingung), Notarin (Ablehnung, Antrag erst nach Zahlung), Ackermann (ohne Bedingung), Ute („Ja, wir sind uns einig.“); Unterschrift-Symbol und „Alle unterschreiben“; Blase Joachim „Ab heute gehört uns das Haus!“ | ph:`house` (Gelb); tabler:`book-2` (Blau), `contract`, `writing-sign`; Tisch programmatisch (Gelb) | `Fall · Der Hauskauf` → `Fall · Bei der Notarin` → `Fall · Die Einigung` → `Fall · Die Unterschrift` | `szene_145unterschrift_1` bei „unterschreiben“ |
| **A2 Wochen später / Frage** `spaet`–`o3` | Haus mit Baum, Ute und Joachim; Brief bei „teilt“, „Kaufpreis fällig“, Münzen und „Ute und Joachim zahlen“, Grundbuch und „Grundbuch: Ute und Joachim“; Frage-Pille, drei Optionen zum Wort (Unterschrift?, Zahlung?, Eintragung?) | ph:`house`, `tree`; tabler:`mail-opened`, `coins`, `book-2`, `writing-sign` | `Fall · Wochen später` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Aufbau** `plan`–`s3` | 1. Kaufvertrag / 2. Auflassung / 3. Eintragung ins Grundbuch zum Wort; Ute, Joachim | ph:`house`, `handshake`; tabler:`contract`, `book-2` | `Hauskauf › Aufbau` | – |
| **D 1. Kaufvertrag** `k1`–`nichtig` | Wortlautkarte § 311b Abs. 1 S. 1 (2 Marker), Zweck (V ZR 213/17 Rn. 12), ✗ „ohne Beurkundung: nichtig, § 125 S. 1 BGB“; Ute, Herr Ackermann | tabler:`contract`, `writing-sign`, `shield-check`, `ban` | `1. Kaufvertrag › § 311b Abs. 1 S. 1 BGB` → `› Formmangel, § 125 S. 1 BGB` | – |
| **E Heilung / Trennung** `heil`–`verw` | Wortlautkarte § 311b Abs. 1 S. 2 (3 Marker); ✓ Pflicht, das Eigentum zu verschaffen (§ 433 Abs. 1 S. 1), ✗ übertragen: noch nichts, Verweis „Abstraktionsprinzip“; Joachim, Herr Ackermann | tabler:`file-check`, `contract`, `arrows-split-2`; ph:`house` | `1. Kaufvertrag › Heilung, § 311b Abs. 1 S. 2 BGB` → `› noch kein Eigentum` | – |
| **F 2. Auflassung** `a1`–`regel` | Wortlautkarte § 925 Abs. 1 S. 1 (4 Marker), „zuständig: jeder Notar“, ✓ Vertretung (XII ZR 107/17 Rn. 19), ✓ im selben Termin (V ZR 213/17 Rn. 13); Notarin, Joachim | ph:`handshake`, `seal-check`; tabler:`users`, `file-certificate`, `calendar-event` | `2. Auflassung › § 925 Abs. 1 S. 1 BGB` → `› Vertretung` → `› im Fall` | – |
| **G § 925 Abs. 2** `w9252`–`klar` | Wortlautkarte (3 Marker), ✗ „erst, wenn der Kaufpreis bezahlt ist“: unwirksam; „Warum so streng?“ Grundbuch / Rechtssicherheit und Rechtsklarheit (vgl. V ZB 126/14 Rn. 10); Notarin, Herr Ackermann | tabler:`hourglass`, `ban`, `book-2` | `2. Auflassung › § 925 Abs. 2 BGB` → `› Warum so streng?` | – |
| **H Sofa ja – Haus nein** `sofa`–`sperre` | grüne Box Eigentumsvorbehalt (§ 449 Abs. 1, Verweis), Box „Grundstück: anderer Schutz des Verkäufers“, ✓ Antrag erst nach Zahlungsnachweis (V ZR 213/17 Rn. 20 f.); Herr Ackermann, Notarin | tabler:`sofa` (Blau); ph:`house`, `seal-check` | `2. Auflassung › Kontrast: bewegliche Sachen` → `› Schutz des Verkäufers` | – |
| **I 3. Eintragung** `e1`–`dauer` | Wortlautkarte § 873 Abs. 1 mit „…“ (3 Marker), Block „Eigentum erst mit der Eintragung“, Zeitstrahl Unterschrift → Eintragung, „Wochen oder Monate“; Ute, Joachim | tabler:`book-2`, `hourglass`; ph:`house` | `3. Eintragung › § 873 Abs. 1 BGB` → `› bis dahin` | – |
| **J Zwischenzeit** `vorm`–`faellig` | Auflassungsvormerkung § 883 (Abs. 2 S. 1 sinngemäß), Verweis eigene Folge; Praxis Fälligkeitsmitteilung (Vertragsbeispiele); Ute, Joachim | tabler:`bookmark`, `shield-lock`, `mail-opened` | `3. Eintragung › Zwischenzeit: Vormerkung, § 883 BGB` → `› Praxis: Fälligkeit` | – |
| **K Ergebnis** `erg`–`r4` | Tafel mit Haken/Kreuzen zum Wort; rechts Haus, Ute und Joachim, Grundbuch und „Eigentümer: Ute und Joachim“ bei „gehört“ | ph:`house`; tabler:`book-2` | `Ergebnis` → `Ergebnis › mit der Eintragung` | – |
| **L Klausurtipp** `tipp`–`t5` | hellgelbe Tafel, Lexi warnt; Reihenfolge 1.–4. zum Wort; Einigsein, § 873 Abs. 2 | Warnsymbol (Streamline Freehand) | `Klausurtipp · Reihenfolge` → `Klausurtipp · Einigsein` | – |
| **M Klausurschema** `sch`–`kV` | breite Karte, I. Einigung (1. gleichzeitige Anwesenheit, 2. ohne Bedingung), II. Eintragung, III. Einigsein, IV. Berechtigung, daneben Kaufvertrag (§ 311b Abs. 1 S. 1) | – | `Klausurschema` → `› I. Einigung (Auflassung)` → `› II. Eintragung` → `› III. Einigsein` → `› IV. Berechtigung` → `› Kaufvertrag als Rechtsgrund` | – |
| **N Merksatz** `merke`–`mk3` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation, kein Zoom.
**Blasen:** Stil C (`bausteine.blase`, stiller Rückfall per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen. Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Ute und Joachim kaufen von Herrn Ackermann ein Haus. Herr Ackermann ist als Eigentümer im Grundbuch eingetragen. Bei einer Notarin wird der Kaufvertrag beurkundet.
>
> Im selben Termin erklären alle die Auflassung. Herr Ackermann will zunächst, dass das Eigentum erst nach Zahlung des Kaufpreises übergeht. Die Notarin sagt, eine Bedingung gehe nicht; sie werde die Eintragung erst nach Zahlung beantragen. Daraufhin erklären alle die Auflassung ohne Bedingung und unterschreiben.
>
> Wochen später teilt die Notarin mit, dass der Kaufpreis fällig ist. Ute und Joachim zahlen. Danach beantragt die Notarin die Eintragung, und das Grundbuchamt trägt die beiden als Eigentümer ein.
>
> **Ab wann gehört Ute und Joachim das Haus?**
