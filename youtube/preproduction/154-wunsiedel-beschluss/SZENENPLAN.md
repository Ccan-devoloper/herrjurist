# Folge 154 · Wunsiedel-Beschluss: Darf ein Gesetz eine Meinung verbieten? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_154.py`](src/skript_154.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall · Grundrechte. Ablauf nach Themenplan und Auftrag: Einstieg im Grundrechte-Seminar mit der Frage „Darf ein Gesetz eine bestimmte Meinung verbieten?“ → der echte Fall sachlich (Wunsiedel, Anmeldung, Verbot des Landratsamts, drei Instanzen, Verfassungsbeschwerde) → Sachverhalt → I. Schutzbereich (Wortlautkarte Art. 5 Abs. 1 Satz 1 GG; auch NS-Gedankengut nicht ausgenommen; Art. 8 GG im Maßstab des Art. 5, Verweis auf Folge 028) → II. Eingriff (Wortlautkarte § 130 Abs. 4 StGB) → III. Rechtfertigung (Wortlautkarte Art. 5 Abs. 2 GG; Sonderrechtslehre, Abwägungslehre, Verbindung durch das BVerfG, Meinungsneutralität; § 130 Abs. 4 kein allgemeines Gesetz, auch kein Ehrschutz) → Wunsiedel-Ausnahme (Leitsatz 1 als Zitatkarte; Begründung aus der Geschichte) → Grenzen der Ausnahme (Leitsatz 2) → Verhältnismäßigkeit, enger Begriff des öffentlichen Friedens, Vermutung, Wechselwirkung in einem Satz mit Verweis auf Folge 146 → Anwendung im Fall und Ergebnis (Tenor) → zurück ins Seminar → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:43,8 (5.968 vertonte Zeichen).

**Sensibilität (Vorgabe Koordinator, höchste Stufe):** Rudolf Heß wird einmal im Sprechtext sachlich genannt („führender Nationalsozialist“, Rn. 19), „Stellvertreter Hitlers“ wird nicht verwendet. Keine Figur für Heß, den Veranstalter, Behörden- oder Gerichtspersonen oder Teilnehmer; die Veranstaltung wird nicht gezeigt. Keine NS-Symbole, Fahnen, Uniformen, Fackeln, Marschbilder, Parolen, keine Zitate von Teilnehmern, Transparenten oder des Mottos. Der echte Fall (B1, B2) nur mit neutralen Icons (Ortsmarke, Kalender, Behördengebäude, Verbotszeichen, Gesetzbuch, Richterhammer, Gericht). Kein Pro und Contra zur Ideologie; die Figuren sind eine Studentin und ein Professor, die die Rechtsfrage besprechen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Swantje (SW), um 23 | fiktive Jurastudentin im Grundrechte-Seminar, fragt nach | `standing/crossed_arms-2` (schwarzes Oberteil, Hose Hellblau `#8DB3F2`), Kopf `Long Bangs`, Haut `#EBC3A0`, ohne Brille. Mimiken `Smile` (ruhig), `Serious` (redet), `Suspicious` (denkt), `Cute` (froh), `Concerned\|Serious` (Sorge) | `lucy` (Frau, jung) |
| Professor Ahlborn (AH), um 55 | fiktiver Seminarleiter | `standing/blazer-3` (Jackett Grün `#8FD694`, Hose Grau `#6B6B78`), Kopf `No Hair 1`, Brille `Glasses`, Haut `#E2B48E`, kein Bart. Mimiken `Smile`, `Serious` (redet/ernst), `Suspicious`, `Cute` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1/K (Seminar): Swantje links blickt nach rechts zu Professor Ahlborn (`_r`), er blickt nach links zu ihr. Tafelszenen: alle nach links zur Tafel. Kontaktbild `out/besetzung_154.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `SW_redet`, `AH_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool: `lucy` und `christian` (stephan nicht verwendet, also keine Paarung stephan/christian); Erzählerin/Lexi Carla ohne Rolle. Abweichung zur Vorfolge 153 (niklas, helmut) und zu 151 (lucy, stephan).
- **Namen:** Swantje, Ahlborn – eindeutig deutsch, nicht in der Liste vergebener Namen und in keinem Skript/Szenenplan/Abnahmebogen/Themenplan unter `youtube/` (Volltextsuche 04.10.2026; „Hannes“, „Greta“, „Merle“, „Lina“ wegen früherer Folgen verworfen). Gesprochen wird nur „Professor Ahlborn“ (Segment 1); Swantje steht auf dem Namensschild. Zusätzlich gesprochen: die realen Namen Heß und Lüth, der Ort Wunsiedel (Namensprüfung).
- `robot_dance-3` für Swantje verworfen (zu ähnlich zu Lexis `robot_dance-1`).
- Figuren-PNGs: `../peeps/op_154/` (40 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 151 (`easing-1`, `shirt-4`), 152 (`walking-1`, `shirt-4`), 153 (`easing-1`, `resting-2`, `resting-1`) – hier `crossed_arms-2` und `blazer-3`; keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplatz **Seminarraum mit Seminartafel, Tisch und Gesetzbuch** – neu gegenüber 151–153; kehrt in K zurück, weil die Geschichte zur Ausgangsfrage zurückkehrt.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Grundrechte-Seminar** `fall`→`klassiker` | Seminartafel, Tisch; Professor Ahlborn legt ein Gesetzbuch auf den Tisch (gleitet von seiner Seite, 0,6 s), fragt (Blase); Swantje antwortet (Blase); Tafel zeigt den Wunsiedel-Beschluss | tabler `book-2` (Rot), `scale`; Tisch aus Grundformen (`tisch()`) | `Fall · Das Grundrechte-Seminar` (ab 0,0 s) → `Die Frage · Darf ein Gesetz eine Meinung verbieten?` → `Die Frage · Der Wunsiedel-Beschluss` | 5 | Buch auf Tisch (`szene_154buch_1`, Freesound CC0 387929) |
| **B1 Wunsiedel 2005** `stadt`→`grund` | ohne Figuren; Pillen zum Wort, Icons auf der Bodenlinie | tabler `map-pin`, `calendar-event`, `building`, `ban`, `book-2` | `Der echte Fall · Wunsiedel` → `· Die Anmeldung` → `· Das Verbot` | 7 | – |
| **B2 Instanzen** `klage`→`frage` | Tafel, drei Instanzen mit Kreuz, Verfassungsbeschwerde, Rüge, Frage; Requisit rechts, ohne Figuren | tabler `gavel`, `building-bank`, `message` | `Der echte Fall · Drei Instanzen` → `· Verfassungsbeschwerde` → `· Die Frage` | 7 | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D I. Schutzbereich** `a5`→`brok` | **Wortlautkarte Art. 5 Abs. 1 Satz 1 GG**, Zeilen mit Haken, blauer Block Art. 8, Pille Brokdorf; Swantje | tabler `message`, `scale`, `shield-check`, `book`, `link` | `I. Schutzbereich · Art. 5 Abs. 1 Satz 1 GG` → `› jede Meinung` → `› auch nationalsozialistisches Gedankengut` → `› Art. 8 GG im Maßstab des Art. 5 GG` | 9 | – |
| **E II. Eingriff** `p130`, `eingriff` | **Wortlautkarte § 130 Abs. 4 StGB**, fünf Marker zum Wort; Professor Ahlborn | tabler `book-2`, `alert-triangle` | `II. Eingriff · § 130 Abs. 4 StGB` → `› knüpft am Meinungsinhalt an (+)` | 8 | – |
| **F III. Allgemeine Gesetze** `a52`→`blind` | **Wortlautkarte Art. 5 Abs. 2 GG**, Frage, zwei Lehrblöcke, grüner Block, Pille „meinungsneutral“; beide Figuren | tabler `book`, `ban`, `scale`, `circle-check`, `eye-off` | `III. Rechtfertigung · Art. 5 Abs. 2 GG` → `› Sonderrechtslehre` → `› Abwägungslehre` → `› Kombination durch das BVerfG` → `› meinungsneutral` | 8 | – |
| **G Kein allgemeines Gesetz** `bverwg`→`ehre` | Tafel: BVerwG ja, BVerfG nein, Haken/Kreuze, roter Block „Sonderrecht“, Ehrschutz (Kreuz zum „nicht“) | tabler `gavel`, `building-bank`, `ban` | `› § 130 Abs. 4 StGB allgemein?` → `› nur eine Haltung zum Nationalsozialismus` → `› Sonderrecht` → `› auch kein Ehrschutz` | 11 | – |
| **H1 Wunsiedel-Ausnahme** `sw2`→`identi` | Swantje fragt (Blase), Professor Ahlborn antwortet (Blase); gelber Block; **Zitatkarte Leitsatz 1** mit drei Markern; Begründungszeilen | – | `› Sonderrecht verfassungswidrig?` → `› die Wunsiedel-Ausnahme` → `› Grund der Ausnahme` | 11 | – |
| **H2 Grenzen** `ah3`→`vhm` | Professor Ahlborn warnt (Blase); Zeilen mit Kreuzen (Kreuz zum „nicht“) und Haken | tabler `message`, `scale` | `› Grenzen der Ausnahme` → `› kein Verbot wegen geistiger Wirkung` → `› auch Sonderrecht verhältnismäßig` | 7 | – |
| **I1 Verhältnismäßigkeit** `zweck`→`gea` | Tafel, drei Pillen geeignet/erforderlich/angemessen zum Wort; beide Figuren | tabler `scale`, `ban`, `shield-check` | `› Verhältnismäßigkeit: öffentlicher Friede` → `› nicht: Schutz vor Beunruhigung` → `› Friedlichkeit` → `› geeignet, erforderlich, angemessen` | 9 | – |
| **I2 Vermutung, Wechselwirkung** `verm`→`ww` | gelber Block, Ausnahmezeile, rosa Block Wechselwirkung (Verweis Folge 146); Swantje | tabler `scale`, `search`, `arrows-exchange` | `› Störung vermutet` → `› untypische Fälle` → `› Auslegung: Wechselwirkung` | 4 | – |
| **J Anwendung, Ergebnis** `anw`→`erg` | Tafel mit Haken/Kreuz, grüner Ergebnisblock (Tenor) | tabler `search`, `scale`, `gavel` | `Anwendung im Fall · Billigung durch eine Ehrung?` → `› nicht: Lob nur der Person` → `› Würdigung vertretbar` → `Ergebnis · Verfassungsbeschwerde zurückgewiesen` | 8 | – |
| **K Zurück im Seminar** `sw3`, `ah4` | Schauplatz A1; Swantje fragt, Professor Ahlborn antwortet (Blasen); Tafel ergänzt die Antwort | tabler `book-2`, `scale` | `Zurück im Seminar · Die Frage` → `· Die Antwort` | 3 | – |
| **L Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst: allgemeines Gesetz?` → `· sonst Sonderrecht` → `· Ausnahme nicht übertragen` | 7 | – |
| **M Prüfschema** `sch`→`k6` | breite Karte, acht Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | 9 | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | 4 | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („20.8.2005“, „§ 130 Abs. 4 StGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: das Gesetzbuch gleitet auf den Tisch.
**Geräusch:** ein Handlungsgeräusch (Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> In der Stadt Wunsiedel liegt das Grab von Rudolf Heß. Ein Veranstalter meldet dort für jedes Jahr bis 2010 eine Gedenkveranstaltung für Heß unter freiem Himmel an, auch für den 20. August 2005.
>
> Mit Bescheid vom 29. Juni 2005 verbietet das Landratsamt die Veranstaltung und jede Ersatzveranstaltung (§ 15 Abs. 1 VersG): Es drohe eine Straftat nach § 130 Abs. 4 StGB, der seit dem 1. April 2005 gilt. Eilanträge bleiben erfolglos. Die Klage scheitert vor dem Verwaltungsgericht (9.5.2006), dem Bayerischen Verwaltungsgerichtshof (26.3.2007) und dem Bundesverwaltungsgericht (25.6.2008).
>
> Der Veranstalter erhebt Verfassungsbeschwerde: § 130 Abs. 4 StGB sei kein allgemeines Gesetz, weil er sich gegen eine bestimmte politische Richtung wende.
>
> **Ist § 130 Abs. 4 StGB mit Art. 5 Abs. 1 und 2 GG vereinbar?**

Kein Fiktiv-Hinweis; die Quelle des echten Falls (BVerfG, Datum, Aktenzeichen, Fundstelle) steht auf der Seminartafel und den Fundstellenzeilen.
