# Folge 086 · AGB-Kontrolle Schema §§ 305 ff. BGB: So prüfst du in 7 Schritten – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_086.py`](src/skript_086.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Schuldrecht AT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Im Kleingedruckten des Fitnessstudios steht eine Mindestlaufzeit von drei Jahren“): Mira bucht im Januar online ein Kurs-Abo im Fitnessstudio von Rolf (jede Woche 2 Kurse mit Trainer, 30 € im Monat), Hinweis auf die AGB mit Link, Haken gesetzt. Anfang Juli will sie zum Monatsende kündigen; Rolf verweist auf das Kleingedruckte: Mindestlaufzeit 36 Monate.

Ablauf: Fall (Anmeldung online, Kündigung im Studio, Kleingedrucktes) → Frage → Sachverhalt → 7 Schritte → I. Anwendungsbereich § 310 → II. AGB-Begriff (Wortlautkarte § 305 Abs. 1 S. 1, Vielzahl) → III. Einbeziehung § 305 Abs. 2, 3, § 305b → IV. überraschende Klausel § 305c Abs. 1 → V. Auslegung § 305c Abs. 2 → VI. Inhaltskontrolle (§ 307 Abs. 3, Reihenfolge § 309 → § 308 → § 307; Wortlautkarte § 309 Nr. 9 a; reiner Gerätevertrag = Miete; Nr. 9 b seit 1.3.2022; § 312k) → VII. Rechtsfolge (Wortlautkarten § 306 Abs. 1 und 2, Verbot der geltungserhaltenden Reduktion, Abs. 3) → Ergebnis (§§ 620, 621 Nr. 3) → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:52,6 (5.742 Zeichen vertont); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Mira (MI), um 28 | Verbraucherin, bucht das Kurs-Abo | `standing/walking-1` (rosa T-Shirt `#F6A5C0`, schwarze Hose, weiße Turnschuhe), Kopf `Medium Straight`, Haut `#C99272`; Mimiken `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Awe` (staunt beim Lesen der 36 Monate) | `lucy` (Frau, jung) |
| Rolf (RO), um 50 | betreibt das Fitnessstudio, Unternehmer | `standing/crossed_arms-1` (blaues Langarmshirt `#8DB3F2`, schwarze Hose, verschränkte Arme), Kopf `Short 2`, Haut `#F2C7A8`; `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner einschließlich der laufenden Folgen 084/085 und gegen die Koordinatorliste): Mira, Rolf. „Lena“ (Testproduktion Bilanzierung) und „Ralf“ (Folge 007) verworfen. Kein Genitiv eines Namens im Sprechtext („im Fitnessstudio von Rolf“).
- **Stimmen nur aus dem Pool:** `lucy`, `stephan`; `christian` nicht eingesetzt (klingt wie `stephan`), `hilde` nicht gebraucht. Einziges Dialogpaar Mira–Rolf (lucy/stephan).
- Präfixe `MI_`/`RO_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In der Studioszene blickt Mira (links) nach rechts zu Rolf, Rolf nach links zu ihr; in der Wohnung blickt Mira nach links zum Laptop; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MI_redet`, `RO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. Keine weiteren Menschen im Bild (Trainer nur als Wort und Pille, kein Personen-Icon; Requisit „users-group“ steht für die Kursgruppe bzw. „alle Mitglieder“ als Symbol, nicht als Figur).
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 083 (`easing-1`, `resting-1`, `blazer-4`, `sitting/bike`), 084 (`blazer-3`, `resting-2`), 085 (`robot_dance-3`, `blazer-3`); keine Polka Dots.
- Figuren-PNGs: `../peeps/op_086/` (42 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 083 (Garage, Park, Straße mit Fahrrad), 084 (Nötigung), 085 (Außenbereich, Wald). Hier neu: Wohnung mit Sofa und Schreibtisch, Laptop und Buchungsseite als Bildschirmausschnitt; Fitnessstudio mit Hantelstange und Kettlebell; AGB-Auszug als Karte. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Anmeldung** `fall`–`haken` | Wohnung: Sofa, Schreibtisch mit Laptop, Mira ab 0,0 s; Buchungsseite: Hantel bei „Fitnessstudio“, Pille „Januar“, „2 Kurse pro Woche mit Trainer“, „30 € im Monat“, „Es gelten unsere AGB.“ + Link + „AGB lesen“, Haken „Ich akzeptiere die AGB.“, „Jetzt buchen“ | ph:`couch` (Lila), tabler:`desk` (Gelb), `device-laptop`, `barbell` (Grün), `calendar-event`, `link`, `square-check` (Grün) | `Fall · Die Anmeldung online` (ab 0,0 s) → `Fall · Hinweis auf die AGB` | `szene_086klick_1` bei „Jetzt buchen“ |
| **A2 Kündigung** `juli`–`frage2` | Pille „Anfang Juli“, Kalender „keine Zeit mehr“; Mira geht zu Rolf ins Studio (Bewegung); Blasen Mira „Ich möchte kündigen, / zum Ende des Monats.“ und Rolf „Das geht nicht. Lies das / Kleingedruckte: / Mindestlaufzeit 3 Jahre.“; AGB-Karte „§ 4 Laufzeit – Die Mindestlaufzeit beträgt 36 Monate.“ mit Marker; Pillen „3 Jahre gebunden?“, „Prüfung in 7 Schritten“ | tabler:`calendar-event`, `barbell`, `dumbbell` (Grün), `building-store` (Blau) | `Fall · Die Kündigung` → `Fall · Das Kleingedruckte` → `Fall · Die Frage` | `szene_086schritte_1`, als Mira ins Studio geht |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C 7 Schritte** `sieben`–`s7` | I.–VII. zum Wort | tabler:`list-numbers` | `AGB-Kontrolle › 7 Schritte` | – |
| **D I. Anwendungsbereich** `anw`–`anw3` | § 310, ✗ Erb-/Familien-/Gesellschaftsrecht, Unternehmer eingeschränkt, ✓ Verbraucherin/Unternehmer, Block „Verbrauchervertrag: alles gilt“ | tabler:`filter`, `user-check` | `› I. Anwendungsbereich, § 310 BGB` | – |
| **E II. AGB-Begriff** `begr`–`begr2` | Wortlautkarte § 305 Abs. 1 S. 1 (4 Marker), Vielzahl (BGH XI ZR 35/24 Rn. 16), ✓ alle Mitglieder, ✓ nichts ausgehandelt | tabler:`file-text`, `copy`, `users-group` | `› II. AGB-Begriff, § 305 Abs. 1 BGB` | – |
| **F III. Einbeziehung** `einb`–`indiv` | drei Voraussetzungen, ✓ online, Abs. 3, Block § 305b | tabler:`square-check`, `link`, `writing` | `› III. Einbeziehung, § 305 Abs. 2 BGB` → `III. Einbeziehung › Vorrang der Individualabrede, § 305b BGB` | – |
| **G IV. Überraschung** `ueber`–`ulang` | § 305c Abs. 1, ✓ üblich, ✓ offen unter „Laufzeit“, Block „3 Jahre zu lang? Frage der Inhaltskontrolle“ | tabler:`search`, `file-text`, `hourglass` | `› IV. keine überraschende Klausel, § 305c Abs. 1 BGB` | – |
| **H V. Auslegung** `ausl`–`asub` | einheitliche Auslegung (Rn. 20), § 305c Abs. 2, ✓ eindeutig | tabler:`zoom-in`, `file-check`; ph:`scales` | `› V. Auslegung, § 305c Abs. 2 BGB` | – |
| **I VI. Inhaltskontrolle** `ink`–`r307` | § 307 Abs. 3, ✓ kontrollfähig (XII ZR 42/10 Rn. 15), drei Farbblöcke § 309 / § 308 / § 307 | ph:`scales`; tabler:`list-numbers` | `› VI. Inhaltskontrolle` → `VI. Inhaltskontrolle › Reihenfolge` | – |
| **J § 309 Nr. 9 a** `w309`–`drei` | Wortlautkarte (2 Marker), reiner Gerätevertrag = Miete (Rn. 16–18), ✓ Kurse mit Trainer, roter Block „3 Jahre länger als 2: Klausel unwirksam“ | tabler:`calendar-time`, `barbell`, `users-group`, `calendar-x` | `VI. Inhaltskontrolle › § 309 Nr. 9 a BGB` → `§ 309 Nr. 9 a BGB › Kurse mit Trainer` | – |
| **K Nr. 9 b, § 312k** `bc`, `button` | Verlängerung, 1 Monat, Art. 229 § 60 EGBGB; ✓ Kündigungsbutton | tabler:`refresh`, `click` | `VI. Inhaltskontrolle › § 309 Nr. 9 b BGB` → `Kündigungsbutton · § 312k BGB` | – |
| **L VII. Rechtsfolge** `rf`–`abs3h` | Wortlautkarten § 306 Abs. 1 und Abs. 2 (je 1 Marker), ✗ nicht gekürzt, Verbot der geltungserhaltenden Reduktion (VIII ZR 262/09 Rn. 24), Abs. 3 | ph:`scales`; tabler:`file-check`, `book`, `eraser`, `alert-triangle` | `› VII. Rechtsfolge, § 306 BGB` → `VII. Rechtsfolge › keine geltungserhaltende Reduktion` | – |
| **M Ergebnis** `erg`–`erg3` | Block „Kurs-Abo bleibt wirksam, aber ohne Mindestlaufzeit“, §§ 620, 621 Nr. 3, ✓ Ende 31.7. | tabler:`file-check`, `calendar-event` | `Ergebnis · Kurs-Abo ohne Mindestlaufzeit` | – |
| **N Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Reihenfolge und Kontrollfähigkeit` | – |
| **O Klausurschema** `sch`–`k7` | breite Karte, I.–VII. Zeile für Zeile mit Untermerkmalen | – | `Klausurschema` → `› III. Einbeziehung` → `› VI. Inhaltskontrolle` → `› VII. Rechtsfolge` | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegung nur, als Mira ins Studio geht.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahl als Ziffer („3 Jahre“). Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Mira bucht im Januar 2026 online ein Kurs-Abo im Fitnessstudio von Rolf: jede Woche 2 Kurse mit Trainer, 30 Euro im Monat. Vor dem Klick auf „Jetzt buchen“ weist die Seite auf die AGB hin, mit Link zum Lesen. Mira setzt den Haken „Ich akzeptiere die AGB“.
>
> In den AGB, die Rolf für alle Mitglieder verwendet, steht unter der Überschrift „Laufzeit“: „Die Mindestlaufzeit beträgt 36 Monate.“ Ausgehandelt wurde nichts.
>
> Anfang Juli will Mira zum Ende des Monats kündigen. Rolf sagt: „Das geht nicht. Mindestlaufzeit 3 Jahre.“
>
> **Ist Mira 3 Jahre gebunden?**
