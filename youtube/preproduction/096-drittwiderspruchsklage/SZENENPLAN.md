# Folge 096 · Drittwiderspruchsklage § 771 ZPO: Wenn fremde Sachen gepfändet werden – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_096.py`](src/skript_096.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZV, Themenplan-Format „Schema“, Voraussetzung Folge 054 (Rechtsbehelfe in der ZV), Klageschema wie Folge 078. Übungsfall nach dem Plan-Hook: Frau Wendland gibt ihr Ölgemälde während einer Renovierung ihrem Enkel Herrn Vollmer (Student) zur Aufbewahrung, beide unterschreiben einen Zettel („Das Bild gehört Frau Wendland“). Herr Vollmer schuldet dem Fahrradhändler Herrn Gebhardt 1.800 €; aus dem rechtskräftigen Urteil des Amtsgerichts pfändet die Gerichtsvollzieherin das Gemälde in seiner Wohnung; Versteigerung in drei Wochen. Aufbau: A. Zulässigkeit (Statthaftigkeit mit **Wortlautkarte § 771 I**; Abgrenzung § 766/§ 805 je ein Satz, Verweis auf 054; Zuständigkeit örtlich § 771 I/§ 802, sachlich Streitwert § 6 ZPO, BGH IX ZR 69/05 Rn. 2; Parteien § 771 II; Rechtsschutzbedürfnis) → B. Begründetheit (Eigentum, BGH V ZR 267/17 Rn. 6; Verwahrung; Beweislast mit **Wortlautkarten § 1006 I 1 und III BGB**; Einwendungen) → Tenor → Klausurtipp (Lexi) → Eilantrag (**Wortlautkarte § 769 I** auszugsweise, Glaubhaftmachung, § 775 Nr. 2, § 770) → Schema → Merksatz. Hauptfilm 5:59,2 (5.182 Zeichen; Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Wendland (WE), um 78 | Großmutter, Eigentümerin, Klägerin | Pose `standing/resting-1` (blauer Pullover `#8DB3F2`, schwarze Hose), Kopf `Gray Medium` (Haar `#C4C4CC`), Brille `Glasses`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile`, `Smile Big|Smile`, `Driven` (entschlossen, redet streng), `Concerned|Serious`, `Suspicious` | `hilde` (Frau, älter) |
| Herr Vollmer (VO), um 23 | Student, Enkel, Schuldner | Pose `standing/easing-1` (offenes grünes Hemd `#8FD694` über weißem Shirt, dunkle Hose `#3A3A48`), Kopf `Pomp`, Haut `#E2B08C`; Mimiken `Calm`, `Smile`, `Fear`, `Concerned|Serious` (redet, Sorge), `Suspicious` | `stephan` (Mann, mittel) |
| Gerichtsvollzieherin (GV), um 35, ohne Namen | Vollstreckungsorgan, sachlich | Pose `standing/blazer-4` (dunkelblauer Blazer `#3D4A7A`, weißes Oberteil), Kopf `Medium Bangs 3`, Haut `#B07552`; Mimiken `Calm`, `Serious` (redet), `Solemn` | `lucy` (Frau, jung) |
| Herr Gebhardt (GE), um 50 | Fahrradhändler, Gläubiger, Beklagter (spricht nicht) | Pose `standing/crossed_arms-1` (türkisfarbener Pullover `#9ED9DC`, schwarze Hose), Kopf `Short 1`, Brille `Glasses 3`, Haut `#F2CDB0`; Mimiken `Calm`, `Suspicious`, `Serious` (neutral, keine „fiese“ Darstellung) | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (zur Tafel bzw. zum Gegenüber), `_r` blickt nach rechts (Frau Wendland in ihrer Wohnung, Herr Gebhardt im Laden, Herr Vollmer in seiner Wohnung). **Keine Prothesen-Posen**, keine Bärte, keine Muster, **alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WE_redet`, `WE_redetstreng`, `VO_redet`, `GV_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem Pool (stephan, hilde, lucy; `christian` nicht verwendet, stephan und christian nie Dialogpartner). **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge und nicht in der Liste vergebener Namen (`grep -rlw` über alle Folgenordner ohne Treffer): Wendland, Vollmer, Gebhardt. Figuren-PNGs: `../peeps/op_096/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 093 (Verpflichtungsklage), 094 (Sirius-Fall), 095 (Abnahme): dort Posen `robot_dance-2`, `blazer-3`, `pointing_finger-1`, `polka_dots`, `easing-2`, `shirt-3`, Köpfe u. a. `Gray Bun`, `Short 3`, `Long Curly`. Hier `resting-1`, `easing-1`, `blazer-4`, `crossed_arms-1` mit `Gray Medium`, `Pomp`, `Medium Bangs 3`, `Short 1`; kein Muster.
- 054 (gleicher Rechtsbehelf, dort Fernseher der Schwester, Siegel, Autowerkstatt) und 078 (Tischlerei, Wohnungstür, Kanzlei, `blazer-4` als Rechtsanwältin mit Kopf `Long`, dunklem Sakko): hier neuer Fall (Gemälde der Großmutter, Renovierung, Fahrradladen, Studentenwohnung mit Schreibtisch), `blazer-4` als Gerichtsvollzieherin mit anderem Kopf, Hautton und dunkelblauem Blazer. Wohnungstür als Kartenbaustein wie 078, aber in anderer Szene (Innenansicht mit Schreibtisch und Gemälde).
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Wohnung Wendland** `fall`→`w1` | Bodenlinie; Leiter und Eimer (Renovierung), Frau Wendland links (blickt nach rechts), Gemälde in der Mitte, Herr Vollmer rechts | tabler:`ladder` (Holz), `bucket`, `building-lighthouse` (im Gemälde: Goldrahmen und Leinwand als Kartenbausteine, kein Gemälde-Icon vorhanden), `note` | `Fall · Das Gemälde der Großmutter` (ab 0,0 s) → `Fall · Der Zettel` | Renovierung · Gemälde · „nur zur Aufbewahrung“ · Enkel kommt · Zettel · Zettel-Pille · Blase | Stift auf Papier (`szene_096stift_1`) |
| **B Fahrradladen** `schuld`→`gv` | zwei Fahrräder, Herr Gebhardt (blickt nach rechts), Herr Vollmer rechts | tabler:`bike`, `cash-banknote` (Grün), `file-certificate` | `Fall · Die Schulden` → `Fall · Urteil und Vollstreckungsauftrag` | Laden · Gebhardt · 1.800 € · Urteil · Auftrag | – |
| **C Wohnung Vollmer** `klingel`→`frage2` | Gemälde an der Wand über dem Schreibtisch, Herr Vollmer (blickt nach rechts), Wohnungstür, Gerichtsvollzieherin bzw. später Frau Wendland rechts | tabler:`desk` (Holz), `books`, `bell-ringing` (Gelb), `calendar-event`; Tür aus `karte` | `Fall · Die Pfändung` → `Fall · Die Großmutter` → `Fall · Die Frage` | Klingel · GV-Blase · „gepfändet“ · Vollmer-Blase · GV-Blase · Versteigerung · Wendland kommt · Wendland-Blase · zwei Frage-Pillen | Türklingel (`szene_096klingel_1`) |
| **D Sachverhalt** `sv` | Karte vollständig (≈ 9,7 s) | – | `Sachverhalt` | 1 | – |
| **E Statthaftigkeit** `zul`→`dritt` | Tafel mit **Wortlautkarte § 771 I** (Marker „Dritter“, „die Veräußerung hinderndes Recht“, „im Wege der Klage“, „in dessen Bezirk“); Frau Wendland | Gemälde | `A. Zulässigkeit` → `› 1. Statthaftigkeit` → `› 1. Statthaftigkeit, § 771 Abs. 1 ZPO` | Titel · Karte · vier Marker · Dritte · Eigentum · Block + Haken | – |
| **F Abgrenzung** `a766`→`verw` | Tafel; Gerichtsvollzieherin | tabler:`list-check`, `home`, `coin` | `› 1. Statthaftigkeit › Abgrenzung` | § 766 · Gewahrsam + BGH · richtig gehandelt · § 805 · Video-Pille | – |
| **G Zuständigkeit, Parteien** `zust`→`bekl` | Tafel; Frau Wendland und Herr Gebhardt | tabler:`map-pin`, `cash-banknote`, `building-bank` | `› 2. Zuständigkeit` → `…, § 802 ZPO` → `› sachlich: Streitwert` → `› Parteien, § 771 Abs. 2 ZPO` | örtlich · ausschließlich · sachlich · § 6 · BGH · geringerer Wert · Amtsgericht · Beklagter · Streitgenossen | – |
| **H Rechtsschutzbedürfnis** `rsb`→`rsb3` | Tafel mit Zeitstrahl (Beginn: Pfändung, Ende: Verwertung, „jetzt“); Frau Wendland | tabler:`hourglass` | `› 3. Rechtsschutzbedürfnis` → `› Ergebnis: zulässig` | Beginn · solange · Ende · jetzt · Haken · Block | – |
| **I Begründetheit: Eigentum** `begr`→`verwahr` | Tafel; Frau Wendland und Herr Vollmer | Gemälde | `B. Begründetheit` → `› 1. die Veräußerung hinderndes Recht: Eigentum` | Recht · Eigentum · Übergriff + BGH · Verwahrung · Haken | – |
| **J Beweislast** `beweis`→`zettel2` | Tafel mit **Wortlautkarten § 1006 I 1 und § 1006 III BGB**; Frau Wendland und Herr Gebhardt | tabler:`scale`, `note` | `› 1. Beweislast` → `› … › Eigentumsvermutung, § 1006 BGB` → `› 1. Eigentum steht fest` | Beweislast · Karte 1 · Marker · Enkel · zeigen · mittelbare Besitzerin · Karte 2 · Marker · Block | – |
| **K Einwendungen** `einw`→`keine` | Tafel; Frau Wendland und Herr Gebhardt | tabler:`file-certificate` | `› 2. keine Einwendungen des Beklagten` → `› Ergebnis: begründet` | Einwendungen? · Beispiel + BGH · schuldet nichts · keine · Block | – |
| **L Tenor** `tenor` | Tafel mit grünem Tenorblock; Frau Wendland und Herr Gebhardt | Fluent HC:`balance-scale` | `Tenor (Klausurkonvention)` | Tenor · unzulässig | – |
| **M Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · den Eilantrag nicht vergessen` | Klage allein · nicht auf · zugleich · § 771 III | – |
| **N Eilantrag** `wl769`→`p770` | **Wortlautkarte § 769 I 1, 3** (Auszug, Marker „auf Antrag“, „gegen oder ohne“, „glaubhaft zu machen“); Frau Wendland und Gerichtsvollzieherin | tabler:`hand-stop`, `file-text`, Fluent HC:`balance-scale` | `Eilantrag › einstweilige Einstellung, § 769 ZPO` → `› Glaubhaftmachung` → `› Vorlage, § 775 Nr. 2 ZPO` → `› Entscheidung im Urteil, § 770 ZPO` | Karte · Marker · Zettel/eV · § 294 · Beschluss · § 775 Nr. 2 · Urteil · § 770 | – |
| **O Klausurschema** `sch`→`sC` | breite Karte, baut sich auf | – | `Klausurschema` → `› A. Zulässigkeit` → `› B. Begründetheit` → `› Eilantrag` | Titel · A · 1 · 2 · sachlich · 3 · B · 1 · 2 · Eilantrag | – |
| **P Merksatz** `merke`→`m2` | Lexi erklärt (redet), zwei Merkzeilen mit Marker | – | `Merksatz` | Gewahrsam · Drittwiderspruchsklage | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („1.800 €“, „3 Wochen“, „§ 771 Abs. 1“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_096stift_1` beim Unterschreiben des Zettels, `szene_096klingel_1` beim Klingeln), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Frau Wendland lässt ihre Wohnung renovieren. So lange gibt sie ihr Ölgemälde ihrem Enkel, dem Studenten Herrn Vollmer, nur zur Aufbewahrung. Auf einem Zettel, den beide unterschreiben, halten sie fest: Das Bild gehört Frau Wendland.
>
> Herr Vollmer schuldet dem Fahrradhändler Herrn Gebhardt 1.800 €. Aus einem rechtskräftigen Urteil des Amtsgerichts lässt Herr Gebhardt vollstrecken. Die Gerichtsvollzieherin pfändet das Gemälde in der Wohnung von Herrn Vollmer; die Versteigerung soll in 3 Wochen stattfinden.
>
> Frau Wendland schuldet Herrn Gebhardt nichts. Annahme: Der Zettel ist echt; das Gemälde ist mehr wert als 1.800 €.
>
> **Wie wehrt sich Frau Wendland – und wie rechtzeitig?**
