# Folge 150 · Elfes-Urteil: Allgemeine Handlungsfreiheit nach Art. 2 I GG – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_150.py`](src/skript_150.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Klassiker-Fall · Grundrechte. Ablauf: moderner Einstieg (Torben, Passversagung nach § 7 Abs. 1 Nr. 1 PassG) → Frage → der echte Fall sachlich (Wilhelm Elfes, Passantrag 1953, Wortlautkarte § 7 Abs. 1 lit. a PaßG 1952, BVerwG, Verfassungsbeschwerde) → Sachverhalt → I. Art. 11 GG (Wortlautkarte, Ausreise nicht erfasst) → II. Art. 2 Abs. 1 GG (Wortlautkarte; Kernbereich vs. umfassende Handlungsfreiheit; Ausreisefreiheit als Ausfluss; Auffanggrundrecht) → III. Schranke verfassungsmäßige Ordnung (jede formell und materiell verfassungsmäßige Norm; kein Leerlauf; unantastbarer Bereich; Passgesetz, Bestimmtheit, enge Auslegung) → Ergebnis (zurückgewiesen; Begründungspflicht) → Bedeutung (Leitsatz 4, Reiten im Walde, Verhältnismäßigkeit) → zurück zu Torben (Wortlautkarte § 7 PassG heute) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:26,5 (5.690 vertonte Zeichen).

**Neutralität (Vorgabe Koordinator):** Wilhelm Elfes tritt nicht als Figur auf, kein Porträt, keine Partei- oder Organisationslogos; sein Wirken und der Grund der Passversagung nur nach dem Volltext (<33>), ohne Wertung. Szene B1 nur mit neutralen Icons (Rathaus, Mikrofon, Globus, Reisepass). Im echten Fall stehen keine Figuren im Bild. Herr Haupt ist sachlich, kein Bösewicht (keine bösen Mimiken).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Torben (TB), um 30 | fiktiver Antragsteller, will zu einer Konferenz ins Ausland | `standing/shirt-3` (Hemd Grün `#8FD694`, schwarze Hose), Kopf `Short 4` (Haar `#4A3222`), Haut `#EBC0A0`, ohne Brille, ohne Bart. Mimiken `Calm` (ruhig), `Serious` (redet), `Suspicious` (denkt), `Smile` (froh), `Concerned\|Serious` (Sorge) | `niklas` (Mann, jung) |
| Herr Haupt (HP), um 60 | fiktiver Sachbearbeiter der Passbehörde, versagt den Pass | `standing/blazer-3` (Sakko Blau `#8DB3F2`, schwarzes Oberteil, Hose Grau `#6B6B78`), Kopf `No Hair 2` (Haar `#9C9C9C`), Brille `Glasses 3`, Haut `#E2B08C`, ohne Bart; steht hinter dem Schalter. Mimiken wie Torben | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1/I1: Herr Haupt hinter dem Schalter blickt nach rechts zu Torben (`_r`), Torben nach links zu ihm. Tafelszenen: alle nach links zur Tafel. Kontaktbild `out/besetzung_150.png`.
- **Alle Grundmimiken mit geschlossenem Mund** (`Calm`, `Serious`, `Suspicious`, `Smile`, `Concerned|Serious`); Mundzustände a/o/e nur in `TB_redet`, `HP_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool (niklas, helmut, ela_froh, julia): niklas und helmut (jung/älter, gut unterscheidbar); ela_froh (heiter) und julia (möglichst vermeiden) nicht verwendet. Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Torben, Haupt – eindeutig deutsch, nicht in der Liste vergebener Namen und in keinem Szenenplan/Skript/Abnahmebogen unter `youtube/preproduction` (Volltextsuche 04.10.2026; „Ole“ vor der Vertonung verworfen, weil mehrdeutig lesbar). „Haupt“ steht nur auf dem Namensschild (nicht gesprochen). Gesprochen wird zusätzlich der reale Name Elfes (Namensprüfung).
- Figuren-PNGs: `../peeps/op_150/` (40 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 147 (`pointing_finger-2`, `easing-2`), 148 (`robot_dance-3`, `walking-3`), 149 (`blazer-4`, `crossed_arms-2`), 146 (`resting-1`, `crossed_arms-1`) – hier `shirt-3` und `blazer-3`; keine Polka Dots, keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2`), keine Bärte. Schauplatz **Passbehörde mit Schalter** – neu gegenüber 146–149 (Filmblog/Hamburg, Gericht, Straße/Unfall, Halter). Der Schauplatz kehrt in I1 wieder, weil die Geschichte zum Einstiegsfall zurückkehrt.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Passbehörde** `fall`→`o1` | Schalter (Grundformen) mit Herrn Haupt dahinter, Schild „Passbehörde“; Torben denkt an die Reise, geht zum Schalter, Antrag, Stempel, Reisepass, Haupt redet (Blase), Torben redet (Blase) | tabler `building`, `plane-departure`, `file-text`; Streamline Freehand `office-stamp-document`; Reisepass aus Grundformen mit tabler `world`; Pillen „Konferenz im Ausland“, „Antrag: neuer Reisepass“, „Pass versagt“, „§ 7 Abs. 1 Nr. 1 PassG“ | `Fall · Torben bei der Passbehörde` (ab 0,0 s) → `· Der Pass wird versagt` → `· Welches Grundrecht?` | 10 | Schritte (`szene_150schritte_1`, Freesound CC0 707246), Stempel (`szene_150stempel_1`, Freesound CC0 470710) |
| **A2 Die Frage** `frage0`, `klassiker` | Tafel, beide Figuren | tabler `plane-departure`, `scale` | `Die Frage · Schützt das Grundgesetz die Ausreise?` → `· Das Elfes-Urteil` | 3 | – |
| **B1 Wilhelm Elfes** `elfes`→`versagt` | Stationen ohne Figuren: Rathaus, Mikrofon/Globus, Reisepass mit Kreuz; Pillen zum Wort | tabler `building-community`, `microphone-2`, `world`; Reisepass | `Der echte Fall · Wilhelm Elfes` → `· Der Passantrag 1953` | 11 | – |
| **B2 Passgesetz 1952** `norm`→`frage` | **Wortlautkarte § 7 Abs. 1 lit. a PaßG** (nach <34>), BVerwG, Verfassungsbeschwerde, Frage | tabler `book`, `gavel`, `building-bank`, `scale` | `Der echte Fall · § 7 Abs. 1 Buchst. a PaßG` → `· Bundesverwaltungsgericht` → `· Verfassungsbeschwerde` → `· Die Frage` | 8 | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **D I. Art. 11 GG** `urteil`→`nein11` | Tafel, **Wortlautkarte Art. 11 Abs. 1 GG**, Kreuz, roter Block; Torben | tabler `building-bank`, `map`, `fence`, `plane-off` | `I. Freizügigkeit · BVerfG, 16.1.1957` → `… · Wortlaut` → `› nicht die Ausreise` → `› Schranken des Abs. 2` → `› Ausreise nicht erfasst (−)` | 8 | – |
| **E1 Art. 2 Abs. 1 GG** `a2` | **Wortlautkarte Art. 2 Abs. 1 GG**, vier Marker; Herr Haupt | tabler `book`, `fence` | `II. Allgemeine Handlungsfreiheit, Art. 2 Abs. 1 GG · Wortlaut` | 5 | – |
| **E2 Reichweite** `kern`→`ausfl` | Tafel: Gegenansicht (Kreuz), Gegenfrage, Haken „umfassend“, Zitat „tun und lassen“, Pille Ausfluss; beide Figuren | tabler `user`, `users-group`, `plane-departure` | `II. … › Gegenansicht: nur ein Kernbereich` → `› Handlungsfreiheit im umfassenden Sinn` → `› Ausreisefreiheit als Ausfluss` | 7 | – |
| **E3 Auffanggrundrecht** `auff`, `auff2` | drei Blöcke „besonderes Grundrecht“, Pfeil, Block Art. 2 Abs. 1, Pille | tabler `shield-check`, `lifebuoy` | `II. … › Verhältnis zu den besonderen Grundrechten` → `› Auffanggrundrecht` | 4 | – |
| **F1 Schranke** `schranke`→`kernber` | Tafel, gelber und lila Block; Herr Haupt | tabler `fence`, `book`, `shield-check`, `lock` | `III. Schranke: verfassungsmäßige Ordnung` → `› jede verfassungsmäßige Rechtsnorm` → `› kein Leerlauf` → `› unantastbarer Bereich` | 7 | – |
| **F2 Passgesetz** `passg`→`eng` | Tafel mit Haken, rotem Bedenken-Block | tabler `book`, `id-badge-2`, `alert-triangle`, `gavel`, `shield-check` | `III. … › Passgesetz` → `› „sonstige erhebliche Belange“` → `› enge Auslegung` | 8 | – |
| **G Ergebnis** `erg`→`begr` | Tafel; Torben | tabler `circle-check`, `building-bank`, `file-text` | `Ergebnis · Vorschrift verfassungsgemäß` → `· Verfassungsbeschwerde zurückgewiesen (−)` → `· Anspruch auf Begründung` | 5 | – |
| **H Bedeutung** `tor`→`verh` | Tafel; beide Figuren | tabler `building-bank`, `search`, `horse`, `scale` | `Bedeutung · Verfassungsbeschwerde für jedermann` → `· am ganzen Grundgesetz messbar` → `· Reiten im Walde, 1989` → `· Maßstab: Verhältnismäßigkeit` | 6 | – |
| **I1 Zurück zum Fall** `o2` | Schauplatz A1; Torben redet (Blase) | wie A1 | `Zurück zum Fall · Torben` | 1 | – |
| **I2 § 7 PassG heute** `heute`→`abs2` | **Wortlautkarte § 7 Abs. 1 Nr. 1, Abs. 2 Satz 1 PassG**, Marker zum Wort, Haken, grüne Pille; beide Figuren | tabler `book`, `user`, `search`, `scale` | `Zurück zum Fall · § 7 Abs. 1 Nr. 1 PassG heute` → `· Art. 2 Abs. 1 GG betroffen` → `· bestimmte Tatsachen` → `· Verhältnismäßigkeit, § 7 Abs. 2 PassG` | 9 | – |
| **J Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Art. 2 Abs. 1 GG zuletzt` → `· Auffanggrundrecht` | 7 | – |
| **K Prüfschema** `sch`→`k6` | breite Karte, 8 Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | 9 | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | 4 | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („16.1.1957“, „1953“, „§ 7 Abs. 1 Nr. 1 PassG“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Torben geht zum Schalter (1,2 s).
**Geräusche:** zwei Handlungsgeräusche (Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Stempel und Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Schalter und Reisepass aus Grundformen (`schalter()`, `reisepass()` in `folien_150.py`), kein Hoheitszeichen.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Wilhelm Elfes ist nach dem Krieg Oberbürgermeister von Mönchengladbach, später dort Oberstadtdirektor. Er kritisiert öffentlich, auch im Ausland, die Politik der Bundesregierung, vor allem zur Wehrpolitik und zur Frage der Wiedervereinigung. 1953 beantragt er die Verlängerung seines Reisepasses.
>
> Die Passbehörde lehnt am 6. Juni 1953 ohne nähere Begründung ab, gestützt auf § 7 Abs. 1 Buchst. a PaßG: Der Pass ist zu versagen, wenn Tatsachen die Annahme rechtfertigen, der Antragsteller gefährde die innere oder äußere Sicherheit oder sonstige erhebliche Belange der Bundesrepublik. Das Bundesverwaltungsgericht stützt die Versagung auf seine Teilnahme an einem Friedenskongress in Wien im Dezember 1952 und eine dort verlesene Erklärung. Elfes bleibt in allen Instanzen erfolglos und erhebt Verfassungsbeschwerde.
>
> **Verletzt die Passversagung Elfes in seinen Grundrechten?**

Kein Fiktiv-Hinweis; die Quelle des echten Falls (BVerfG, Datum, Aktenzeichen) steht auf den Tafeln.
