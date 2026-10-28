# Folge 178 · Hass im Netz: Wann schützt die Meinungsfreiheit? Fall Künast – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_178.py`](src/skript_178.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall · StGB BT. Ablauf nach Auftrag: 1. Hook (fiktiv, Sprechstunde: Stadträtin, Pille „derbe sexistische Beschimpfungen“, Auskunftswunsch; Frage „Muss eine Politikerin so etwas nicht aushalten?“) → 2. der echte Fall sachlich (Beitrag mit falschem Zitat, Kommentare, Auskunftsantrag beim LG Berlin, LG/KG: 12 von 22, 10 verneint, BVerfG 19.12.2021, Tenor) → Sachverhalt → 3. Grundrechte (**Wortlautkarten Art. 5 Abs. 1 Satz 1 und Abs. 2 GG**, § 185 als allgemeines Gesetz in einem Satz mit Verweis auf 146/134, Persönlichkeitsrecht, **Wortlautkarte § 193 StGB**) → 4. Kern (Abwägung als Regel; Menschenwürde, Formalbeleidigung, Schmähung als enge Ausnahmen; Fehler des KG; Kriterien) → 5. **Wortlautkarte § 188 Abs. 1 StGB** (bis hin zur kommunalen Ebene), § 192a in einem Satz → 6. Lösung des Hooks (Tendenz) → zurück in der Sprechstunde → 7. Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi). Hauptfilm 6:43,2 (5.797 vertonte Zeichen, 121 Bildhalte).

## Sensibilität (Auftrag, höchste Stufe; Muster 154/175)

- **Keine** der Beschimpfungen wörtlich, angedeutet oder verpixelt; nur die Text-Pille „derbe sexistische Beschimpfungen“. Kommentare erscheinen als leere, neutrale Sprechblasen-Icons (Tabler `message-circle`).
- Keine Figur, kein Porträt und kein Personen-Icon der Politikerin, des Bloggers, der Kommentierenden, von Richtern oder Plattformpersonen; das Bild im Beitrag nur als Bild-Icon (Tabler `photo`), das Zitat nur als Anführungszeichen-Icon (Tabler `quote`), Inhalt nicht wiedergegeben.
- Parteipolitisch neutral: keine Parteinamen, -farben, -logos; „Künast“ nur als Fallbezeichnung. Keine Plattformnamen, keine Social-Media-Logos.
- Die Stadträtin des Hooks ist erfunden und erscheint **nicht als Figur**, nur als Text auf dem Bericht. Ruhige Mimiken (Calm, Serious, Suspicious, Solemn), kein Lachen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Mattes (MA), um 23 | fiktiver Jurastudent, bringt den Bericht in die Sprechstunde | `standing/resting-1` (Pullover Grün `#8FD694`, schwarze Hose aus der Pose), Kopf `Short 4`, Haut `#E8B98F`, ohne Brille, ohne Bart. Mimiken `Calm` (ruhig), `Serious` (redet), `Suspicious` (denkt), `Solemn` (ernst) | `niklas` (Mann, jung) |
| Professor Ruhland (RU), um 60 | fiktiver Lehrstuhlinhaber | `standing/shirt-3` (weißes Hemd, schwarze Hose aus der Pose), Kopf `No Hair 2` (Haarkranz), Brille `Glasses 3`, Haut `#E3B08C`, kein Bart. Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Solemn` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool: `niklas`, `helmut`; `ela_froh` (ernstes Thema) und `julia` nicht verwendet. Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Mattes, Ruhland – eindeutig deutsch, nicht auf der Liste vergebener Namen und vor Produktionsbeginn in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt: je 0 Treffer; „Jannik“ und „Jonas“ wegen Treffern verworfen). Gesprochen wird nur „Professor Ruhland“ (Segment 1); „Mattes“ steht nur auf dem Namensschild und als Sprechername in den Untertiteln. Zusätzlich gesprochen: „Fall Künast“ (2×) und „Lüth-Urteil“ (Namensprüfung).
- **Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. Sprechstunde: Mattes links blickt nach rechts zu Professor Ruhland, er blickt nach links zu Mattes. Tafelszenen: alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `MA_redet`, `RU_redet` (je beide Richtungen) und Lexi. 36 Figuren-PNGs in `../peeps/op_178/` (nicht im Repository, im Drive-Master).
- `Gray Medium` für den Professor verworfen (rote Standardhaarfarbe, wirkte nicht wie ein älterer Mann).

**Abweichung von den letzten Folgen (174–177):** Posen `resting-1` und `shirt-3` in 174–176 nicht verwendet (174: `crossed_arms-1/-2`, `resting-2`, `shirt-4`; 175: `easing-1`, `pointing_finger-1`; 176: `blazer-1`, `pointing_finger-2`; 177, nach Produktionsende geprüft: `blazer-3`, `robot_dance-2`); keine Polka Dots, keine Prothesen-Posen, keine Bärte. Gleiche Stimmen wie 175 (niklas, helmut) – durch den Pool vorgegeben. **Schauplatz neu:** Sprechstunde im Büro mit Bücherregal (Grundformen), Schreibtisch mit Laptop und ausgedrucktem Bericht – anders als die Seminarräume in 154 (Tisch und Gesetzbuch) und 175 (Whiteboard, Pult). Kehrt in K zurück, weil die Geschichte zur Ausgangsfrage zurückkehrt. Kontaktbogen-Vergleich `out/vergleich_175_176_178.png`. Tageslicht/Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Sprechstunde** `fall`→`ru1` | Regal, Schreibtisch mit Laptop; Mattes legt den Ausdruck auf den Tisch (gleitet 0,5 s); Bericht-Karte: „Beitrag über eine Stadträtin“, drei leere Sprechblasen, Pille „derbe sexistische Beschimpfungen“, „Auskunft: Wer hat das geschrieben?“; Mattes fragt (Blase), Ruhland antwortet (Blase), Fundstelle Fall Künast | tabler `device-laptop`, `file-text`, `message-circle`; Regal/Tisch aus Grundformen | `Fall · Die Sprechstunde` (ab 0,0 s) → `· Beschimpfungen unter einem Beitrag` → `· Die Auskunft` → `Die Frage · Muss sie das aushalten?` → `Die Frage · Der Fall Künast` | 8 | Blatt auf Tisch (`szene_178papier_1`, Freesound CC0 429333) |
| **B1 Der echte Fall** `echt`→`vor` | ohne Figuren; Pillen zum Wort, Icons auf der Bodenlinie | tabler `photo`, `quote`, `message-circle` (3×), `building-bank`, `database`, `scale` | `Der echte Fall · Der Beitrag` → `· Die Kommentare` → `· Der Antrag auf Auskunft` → `· Die Voraussetzung` | 8 | – |
| **B2 Instanzen** `lg`→`frage` | Tafel mit Kreuz/Haken je Instanz, grüner Block BVerfG, Tenor, Frage; Requisit rechts, ohne Figuren | tabler `building-bank`, `gavel`, `scale`, `message-circle` | `Der echte Fall · Landgericht` → `· Landgericht und Kammergericht` → `· 10 Kommentare: Nein` → `· Bundesverfassungsgericht` → `Die Frage · Wann schützt die Meinungsfreiheit?` | 9 | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D1 Grundrechte** `a5`→`a52` | **Wortlautkarten Art. 5 Abs. 1 Satz 1 GG** (Marker „äußern“, „verbreiten“) und **Art. 5 Abs. 2 GG** (Marker „Schranken“, „allgemeinen Gesetze“), Haken „auch polemische oder verletzende Werturteile“; Mattes | tabler `message-circle`, `shield-check`, `book` | `1. Grundrechte · Art. 5 Abs. 1 Satz 1 GG` → `› auch verletzende Werturteile` → `› Schranken, Art. 5 Abs. 2 GG` | 7 | – |
| **D2 Strafnorm und § 193** `p185`→`p193` | Block „§ 185 StGB ist ein allgemeines Gesetz“ (Verweis auf die Folgen zu Lüth und Beleidigung), Block Persönlichkeitsrecht, **Wortlautkarte § 193 StGB** (Auszug, Marker „Wahrnehmung berechtigter Interessen“); Ruhland | tabler `book-2`, `shield`, `scale` | `› § 185 StGB als allgemeines Gesetz` → `› Gegenüber: Persönlichkeitsrecht` → `› § 193 StGB, Wahrnehmung berechtigter Interessen` | 4 | – |
| **E1 Kern** `kern`→`eng` | gelber Block „Normalfall: Abwägung“, drei Pillen zum Wort (Menschenwürde, Formalbeleidigung, Schmähung), Block „eng“; Ruhland | tabler `scale`, `alert-triangle`, `zoom-question` | `2. Abwägung · Der Kern` → `› Normalfall: Abwägung` → `› Ausnahmen ohne Abwägung` → `› Ausnahmen eng` | 8 | – |
| **E2 Die drei Ausnahmen** `schmaeh`→`offen` | drei Farbblöcke (Schmähung, Formalbeleidigung, Menschenwürde), Kreuz „ausfällige Kritik allein: noch keine Schmähung“ beim Wort „nicht“, grüner Block „Sonst: umfassende Abwägung“, „mit offenem Ergebnis“; beide Figuren | – | `› Schmähung` → `› Formalbeleidigung` → `› Menschenwürde` → `› sonst: umfassende Abwägung` | 7 | – |
| **F Der Fehler** `fehler`→`politik` | KG-Obersatz, roter Block „gleichgesetzt“, Haken/Kreuz zum Wort, Kreuze „Abwägungsausfall“, „als Politikerin hinnehmen“; beide Figuren | – | `3. Der Fehler · im Fall Künast` → `› Beleidigung = Schmähkritik?` → `› Sachbezug grenzt die Schmähung ab` → `› Abwägungsausfall` → `› „als Politikerin hinnehmen“` | 10 | – |
| **G1 Kriterien** `krit`→`schutz` | (+)/(−) für das Gewicht der Meinungsfreiheit, Haken Machtkritik, Kreuz „nicht jede Beschimpfung“, Bundesminister/Lokalpolitiker, gelber Block öffentliches Interesse; beide Figuren | – | `4. Kriterien · der Abwägung` → `› Beitrag zur Meinungsbildung?` → `› Machtkritik` → `› nicht jede Beschimpfung` → `› Position der Person` → `› öffentliches Interesse am Schutz` | 8 | – |
| **G2 Form, Anlass, Wirkung** `form`→`wirk` | zwei Blöcke, zwei Zeilen zum Wort; Mattes, Requisit wechselt | tabler `writing`, `search`, `world`, `messages` | `› Form: schriftlich` → `› Anlass` → `› Verbreitung und Wirkung` | 5 | – |
| **H § 188, § 192a** `p188`→`p192a` | **Wortlautkarte § 188 Abs. 1 StGB** vollständig, fünf Marker zum Wort; Haken „neu …“, Block § 192a, Kreuz „das Geschlecht nennt die Vorschrift nicht“; Ruhland | – | `5. § 188 und § 192a StGB · § 188 StGB` → `› bis zur kommunalen Ebene` → `› seit dem Gesetz gegen Hasskriminalität` → `› § 192a StGB` | 13 | – |
| **I Lösung** `loes`→`tend` | Kreuz „nicht vorschnell“, drei rote Pillen zum Wort, Zeile Stadträtin/Ministerin, grüner Block „Viel spricht …“; beide Figuren | – | `6. Lösung · die Stadträtin` → `› Schmähkritik nicht vorschnell` → `› Abwägung` → `› Stadträtin` → `› Ergebnis: Tendenz` | 9 | – |
| **K Zurück in der Sprechstunde** `ma2`, `ru2` | Schauplatz A, Bericht vollständig; Mattes fragt, Ruhland antwortet (Blasen); Pille „nicht ohne Abwägung“ | wie A | `Zurück in der Sprechstunde · Die Frage` → `· Die Antwort` | 4 | – |
| **L Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, drei Schritte, Kreuz zum Fehlersatz; Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst der Sinn: Tatsache oder Werturteil?` → `· Schmähkritik nur ausnahmsweise` → `· sonst Abwägung bei § 193 StGB` → `· Sachbezug heißt nicht zulässig` | 7 | – |
| **M Prüfschema** `sch`→`k4` | breite Karte, acht Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | 9 | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | 4 | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („19.12.2021“, „12 von 22“, „§ 188 Abs. 1 StGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: der Ausdruck gleitet auf den Schreibtisch.
**Geräusch:** ein Handlungsgeräusch (Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Anfang 2019 veröffentlicht ein Blogger auf einer Social-Media-Plattform einen Beitrag mit dem Bild einer bekannten Politikerin und einem ihr zugeschriebenen Zitat, das so nicht von ihr stammt. Im April und Mai 2019 kommentieren zahlreiche Nutzer den Beitrag, viele mit derben sexistischen Beschimpfungen.
>
> Die Politikerin beantragt beim Landgericht Berlin, der Plattform die Auskunft über die Daten der Verfasser von 22 Kommentaren zu gestatten (§ 14 Abs. 3 TMG a. F., heute § 21 TDDDG). Das setzt voraus, dass die Kommentare etwa den Tatbestand des § 185 StGB erfüllen und nicht gerechtfertigt sind.
>
> Das Landgericht hält zunächst alle Kommentare für zulässig. Nach Abhilfe und Beschwerde gestatten Landgericht und Kammergericht die Auskunft zu 12 Kommentaren, zu 10 nicht: keine Schmähkritik. Die Politikerin erhebt Verfassungsbeschwerde (BVerfG, 1 BvR 1073/20).
>
> **Wann schützt Art. 5 Abs. 1 GG solche Kommentare?**

Kein Fiktiv-Hinweis; beim echten Fall stehen Gericht, Datum und Aktenzeichen auf dem Bericht, den Tafeln und den Fundstellenzeilen.
