# Folge 127 · Costa/ENEL: Anwendungsvorrang – EU-Recht verdrängt deutsches Recht – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_127.py`](src/skript_127.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Öffentliches Recht/Europarecht, Themenplan-Format „Klassiker-Fall“. Einstieg mit dem Übungsfall nach dem Plan-Hook (Hedwig, Herr Lammert), dann der **echte Fall** Costa/ENEL sachlich (Herr Costa nur namentlich, **keine Figur**, keine Karikatur), Simmenthal II, Fratelli Costanzo, Anwendungs- statt Geltungsvorrang, Rechtsgrundlage (Erklärung Nr. 17, Art. 4 Abs. 3 EUV), Grenzen aus deutscher Sicht, Lösung des Übungsfalls mit Art. 288 Abs. 2 AEUV, Ergebnis, Klausurtipp, Schema, Merksatz. Die Voraussetzungsfolge „van Gend & Loos“ ist nicht produziert; die unmittelbare Geltung wird deshalb in der Lösung selbst erklärt (Wortlautkarte Art. 288 Abs. 2 AEUV). Hauptfilm 6:31,9.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hedwig, um 40 | Inhaberin einer kleinen Limonadenmanufaktur | `standing/blazer-2` (Blazer Grün `#8FD694`, Oberteil Weiß, Prothese aus der Originalpose), Kopf `Long Curly`, Haut `#EBC3A0`. Mimiken `Calm`, `Smile` (froh), `Awe` (staunt), `Concerned\|Serious` (Sorge, redet), `Suspicious` (denkt) | `sabrina` (Frau, mittel) |
| Herr Lammert, um 55 | Lebensmittelüberwachung (das „Amt“) | `standing/crossed_arms-2` (schwarzes Oberteil, Hose Marine `#3B4A6B`), Kopf `No Hair 1`, Brille `Glasses 2`, Haut `#E2B48E`, ohne Bart. Mimiken `Calm`, `Serious` (ernst, redet), `Suspicious` (denkt), `Solemn` (still), `Awe` (staunt), `Smile` (freundlich) | `william` (Mann, älter) |
| Flaminio Costa | Kläger im echten Fall | **keine Figur**, nur namentlich (Tafel, Sprechtext) | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem zugeteilten Pool (william, sabrina, marc, laura_ruhig); zwei Sprechrollen, marc und laura_ruhig nicht gebraucht. Vorfolge 126: helmut, ela_froh, niklas – keine Überschneidung.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner Text-/Codedatei unter `youtube/` (`rg -lw` in *.py, *.md, *.json, *.csv, *.txt): **Hedwig**, **Lammert**. „Henrike“ verworfen (in 106 als zu nah an „Henrik“ notiert). Kein Genitiv eines Namens im Sprechtext.
- **Blickrichtung:** Alle Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Manufaktur: Hedwig links blickt nach rechts zu Herrn Lammert, Herr Lammert rechts blickt nach links zu ihr. Tafelszenen: beide zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HE_redet`, `LA_redet` (je beide Blickrichtungen) und Lexi. 46 Figuren-PNGs in `../peeps/op_127/` (nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 124 (walking-2, shirt-4, sitting/bike; Unterführung/Straße), 125 (easing-2, crossed_arms-1; Elektroladen), 126 (blazer-1, shirt-3, walking-1, blazer-4, resting-1; Gerichtssaal). 127: **Limonadenmanufaktur mit Arbeitstisch** – neuer Schauplatz; Posen `blazer-2` und `crossed_arms-2` dort nicht verwendet; keine Polka Dots. Der Ergebnis-Halt (H3) kehrt bewusst in die Manufaktur zurück, weil dort die Frage des Falls entschieden wird.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Manufaktur** `fall`→`frage2` | Bodenlinie, Arbeitstisch (Grundformen `karte`) mit Zitrone; Hedwig links ab 0,0 s mit Namensschild; Flaschen erscheinen bei „Limonade“, Süßstoff-Würfel; oben EU-Verordnung (erlaubt) und Gesetz (verboten); Tür rechts, Herr Lammert kommt zur Kontrolle; drei Sprechblasen; Frage-Pillen | tabler: `lemon`, `bottle` (Gelb), `cube` (Weiß), `file-certificate` (Blau), `book` (Rot), `ban`, `door` (Holz), `clipboard-check` | `Fall · Hedwig und ihre Limonade` → `· Die EU-Verordnung erlaubt` → `· Das deutsche Gesetz verbietet` → `· Die Kontrolle` → `· Die Frage` | Grundbild · Flaschen/Hedwig froh · Süßstoff · Verordnung · Gesetz · Tür/Lammert · Lammert redet · Hedwig redet · Lammert redet · Frage 1–3 | Flaschenklirren (`szene_127flaschen_1`, Freesound CC0 816964), Klopfen beim Erscheinen der Tür (`szene_127klopfen_1`, CC0 193827) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C1 Der echte Fall** `costa`→`vorl` | Tafel; rechts Pille + Requisit im Wechsel (keine Figur) | tabler: `scale`, `bolt`, `file-invoice`, `building-bank` | `Der echte Fall · Costa/ENEL, EuGH 1964` → `› Die Stromrechnung` → `› Die Vorlage an den Gerichtshof` | Zeilen zum Wort, gelber Block | – |
| **C2 Italien gegen den Gerichtshof** `ital`→`ro` | roter Kasten (Regierung, Verfassungsgericht), grüner Kasten (eigene Rechtsordnung), Kreuz im roten Kasten bei „anders“ | tabler: `building-bank`, `scale`, `world` | `Costa/ENEL › Italien: das italienische Gesetz gilt` → `› EuGH: eigene Rechtsordnung` | Kästen und Zeilen | – |
| **C3 Kernsatz** `zitat`, `spaet` | **Zitatkarte** Slg. 1964, 1253, 1270 (Marker „autonomen Rechtsquelle“, „keine wie immer gearteten …“), grüner Block | tabler: `arrow-big-up-lines`, `calendar-time` | `Costa/ENEL › Der Kernsatz` → `› Vorrang auch vor späterem Recht` | Karte, 2 Marker, Block | – |
| **D Simmenthal/Costanzo** `simm`→`behoerd` | Tafel, Haken, blauer Block (Costanzo) | tabler: `scale`, `meat`, `gavel`, `building-community` | `Simmenthal II · EuGH 1978` → `› jedes Gericht lässt unangewendet` → `Fratelli Costanzo › auch die Verwaltung` | Zeilen, Haken, Block | – |
| **E Anwendungsvorrang** `gueltig`→`rest` | Tafel mit lila (Art. 31 GG) und grünem Kasten (EU-Recht), gelber Block; Hedwig und Herr Lammert | – | `Anwendungsvorrang › Das Gesetz bleibt gültig` → `› nicht Geltungsvorrang` → `› ohne Kollision weiter angewendet` | Zeilen, Kästen, Mimikwechsel | – |
| **F1 Erklärung Nr. 17** `grund`→`gut` | Kreuz „kein Vorrangartikel“, **Wortlautkarte** (auszugsweise), Gutachten-Zitat | – | `Rechtsgrundlage › kein Vorrangartikel` → `› Erklärung Nr. 17` → `› Gutachten zur Erklärung Nr. 17` | Karte, Marker, Zeilen | – |
| **F2 Art. 4 Abs. 3 EUV** `a43`→`ausdr` | **Wortlautkarte** UAbs. 2/3 (Marker „ergreifen alle geeigneten Maßnahmen“, „unterlassen alle Maßnahmen“), grüner Block | – | `Rechtsgrundlage › Art. 4 Abs. 3 EUV, loyale Zusammenarbeit` → `› Nichtanwendung als Ausdruck der Loyalität` | Karte, Marker, Block | – |
| **G Grenzen** `grenz`, `nurbv` | Tafel, gelber Block | – | `Grenzen aus deutscher Sicht › Ultra-vires- und Identitätskontrolle` → `› nur das BVerfG stellt fest` | Zeilen, Block | – |
| **H1 Lösung I** `zurueck`→`quelle` | **Wortlautkarte Art. 288 Abs. 2 AEUV** (vorgelesen; Marker „allgemeine Geltung“, „verbindlich“, „gilt unmittelbar in jedem Mitgliedstaat“), Haken | – | `Lösung · Hedwig und Herr Lammert` → `› I. unmittelbare Geltung, Art. 288 Abs. 2 AEUV` | Karte, Marker, Haken | – |
| **H2 Lösung II/III** `kol`→`bleibt` | Tafel, Kreuz (Auslegung nicht möglich), Haken, grüner Block | – | `Lösung › II. Kollision` → `› III. Rechtsfolge: Anwendungsvorrang` | Zeilen, Haken, Block | – |
| **H3 Ergebnis** `erg` | zurück in der Manufaktur: Hedwig froh, Herr Lammert freundlich, Verordnung mit Haken | tabler: `file-certificate`, `bottle`, `lemon`, `cube` | `Ergebnis · Das Amt hält sich an die EU-Verordnung` | 3 | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst unionsrechtskonform auslegen` → `· unanwendbar, nicht nichtig` | Zeile für Zeile | – |
| **J Klausurschema** `sch`→`k4` | breite Karte, I.–IV. Punkt für Punkt | – | `Klausurschema` → je Gliederungspunkt ein Pfadstand | 9 Aufbaustufen | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln, Pillen und Karte als Ziffern („15.7.1964“, „1.925 Lire“, „Art. 267 AEUV“, „2 Regeln, 1 Widerspruch“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Flaschen, Klopfen), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Tisch aus Grundformen.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Hedwig betreibt eine kleine Limonadenmanufaktur und süßt ihre neue Limonade mit einem neuen Süßstoff. Eine EU-Verordnung lässt genau diesen Süßstoff für Limonaden ausdrücklich zu. Ein deutsches Gesetz verbietet ihn dagegen.
>
> Herr Lammert von der Lebensmittelüberwachung kommt zur Kontrolle. Er will Hedwig den Verkauf der Limonade untersagen: Er sei an das deutsche Gesetz gebunden. Hedwig beruft sich auf die EU-Verordnung.
>
> **Woran hält sich das Amt – und was wird aus dem deutschen Gesetz?**
