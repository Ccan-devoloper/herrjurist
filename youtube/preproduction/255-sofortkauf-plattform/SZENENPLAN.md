# Folge 255 · „Sofort kaufen“ geklickt: Ist der Verkäufer an den Preis gebunden? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_255.py`](src/skript_255.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · BGB AT · Alltagsfall. Aufbau nach Auftrag: Hook (Kamera für 900 €, wert 2.500 €) → Einstellen mit „Sofort kaufen“ und Plattformregel → Klick und Zahlung → Vergleichspreise am Abend → Anfechtung an der Haustür → Frage → Sachverhalt → Anspruch § 433 Abs. 1 Satz 1, zwei Stufen → I. Vertragsschluss (Abgrenzung Folge 251 in einem Satz; Sofort kaufen = Angebot zum festen Preis, BGH VIII ZR 59/16; Auslegung §§ 133, 157 mit Plattformregeln; ad incertas personas; Wortlautkarte § 145, Bindung ausschließbar, hier verbindlich; Annahme durch Klick; Verweis Folge 014) → II. Anfechtung (Erklärung § 143; Wortlautkarte § 119 Abs. 1: Wille = Erklärung; Wortlautkarte § 119 Abs. 2: Wert keine Eigenschaft, nur wertbildende Umstände; Motivirrtum wie Kalkulationsirrtum; Risiko beim Verkäufer) → Ergebnis → Gegenfall 90 statt 900 € (Erklärungsirrtum, Verweis 251, § 122) → Klausurtipp (Lexi) → Prüfungsschema → Merksatz (Lexi). Hauptfilm 6:13,5 (5.415 vertonte Zeichen). Vorlagen: 251 (Werkzeuge, Hilfsfunktionen, Wortlautkarten, Abgrenzung), 014 (nur verwiesen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung:** Personen fiktiv; keine echten Plattformen oder Kameramarken (Anzeige nur mit „Plattform“ überschrieben, Kamera als Tabler-Icon ohne Herstellerkennzeichen); kein Fiktiv-Hinweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Eichler (EI), um 50 | privater Verkäufer, ficht an | `standing/robot_dance-3` (Pullover Blau `#8DB3F2`, Hose Grau `#5A5F6E`), Kopf `Short 3`, Brille `Glasses 3`, Haut `#E3B48C`, kein Bart. Mimiken `Calm`, `Concerned\|Serious` (redet/Sorge), `Smile`, `Suspicious`, `Serious`, `Fear` (Schreck), `Awe`, `Solemn` | `stephan` (Mann, mittel) |
| Frau Hegemann (HE), um 30 | Käuferin, verlangt die Kamera | `standing/blazer-4` (Blazer Lila `#B8A9F5`, Shirt Weiß, schwarze Hose der Pose), Kopf `Medium Straight`, Haut `#D9A27E`, keine Brille. Mimiken `Calm`, `Driven` (redet), `Smile`, `Smile Big\|Smile`, `Suspicious`, `Serious`, `Concerned\|Serious`, `Awe` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy): besetzt `stephan` und `lucy`; `hilde`, `christian` nicht besetzt (stephan und christian also nie gemeinsam). Vorfolge 251 nutzte `marc`/`sabrina`.
- **Blickrichtung:** Beide Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1/A3: Herr Eichler blickt nach links zur Handy-Anzeige. A2: Frau Hegemann blickt nach links zur Anzeige. A4/Ergebnis: Herr Eichler (`_r`) an der Tür und Frau Hegemann (Grundansicht) blicken einander an. Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`, `Smile Big|Smile`); Mundzustände a/o/e nur in `EI_redet`, `HE_redet` (je links/rechts) und Lexi. 54 Figuren-PNGs in `../peeps/op_255/` (nicht im Repository, im Drive-Master).
- **Klischeeprüfung:** Verkäufer sachlich, kein „gieriger“ Verkäufer, Käuferin ohne Häme; keine Prothesen-Posen, keine Polka Dots, keine Bärte; Frau Hegemann ohne Dutt (Abgrenzung zu Lexi). Hinweis: `robot_dance-3` hat dieselbe offene Handgeste wie Lexis `robot_dance-1`; Herr Eichler ist durch Geschlecht, Frisur, Brille und Blau klar unterscheidbar und steht nie mit Lexi im Bild.
- **Namen:** Eichler, Hegemann – eindeutig deutsche Aussprache, nicht in der Liste vergebener Namen, per `grep -rliw` in keiner `*.py/*.md/*.json/*.csv/*.txt` unter `youtube/` (verworfen: Albers, Wunderlich – im Repo vorhanden; Fröhlich – in 254 und Adjektiv), in `namen_reserviert.txt` als „255: Eichler, Hegemann“ eingetragen. Gesprochen nur von der Erzählerin.

**Abweichung von den letzten Folgen (251–254):** Posen `robot_dance-3`, `blazer-4` – in 251 (`easing-1`, `resting-2`), 252 (`pointing_finger-2`, `blazer-3`, `walking-2`, `robot_dance-2`), 253 (`crossed_arms-1`), 254 (`resting-1`, `shirt-3`, `walking-1`) nicht verwendet; keine Polka Dots. Schauplätze **Wohnzimmer bei Herrn Eichler** (Handy-Anzeige als Bildschirm-Zoom, Sofa, Stehlampe, Fenster), **Park am Mittag** (Bank, Baum), **Haustür** – neu gegenüber 251 (Schreibtisch/Monitor, Lager, Telefonat). Das Wohnzimmer kehrt am Abend zurück (gleicher Ort, Fenster dunkler, Lampe gelb), die Haustür im Ergebnis, weil der Streit dort entschieden wird. Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Wohnzimmer** `fall`→`regel` | ab 0,0 s Handy-Anzeige „Plattform“ mit Kamera, Herr Eichler mit Namensschild, Sofa, Lampe, Fenster; „900 €“ zum Wort, Pille „Wert: 2.500 €?“ (Hook), „Montagmorgen“, „fester Preis“, Schaltfläche „Sofort kaufen“, Block „Regel der Plattform: Klick auf ‚Sofort kaufen‘ = Kauf“ | tabler `camera`, `sofa`, `lamp`; Handy, Fenster aus Grundformen | `Fall · Bei Herrn Eichler zu Hause` → `· Kamera für 900 € mit „Sofort kaufen“` → `· Regel der Plattform: Klick = Kauf` | – |
| **A2 Park** `park`→`zahlt` | Bank, Baum, Frau Hegemann mit Namensschild; Anzeige; Klick (Hand-Icon), Schaltfläche wird „gekauft“ (grün); „bezahlt: 900 €“ + Münze | tabler `tree`, `hand-click`, `coin-euro` | `Fall · Am Mittag: …` (3 Stände) | – |
| **A3 Wohnzimmer abends** `abend`→`modell` | „Andere Angebote“ (2.450/2.500/2.550 €), Pille „rund 2.500 €“, Schreck; Checkliste „Modell: gewusst“, „Zustand: gewusst“, Kreuz „Marktpreis: unterschätzt“ | tabler `camera` | `Fall · Am Abend …` (3 Stände) | – |
| **A4 Haustür** `tuer`→`frage3` | Hauswand, Tür, Klingel (Glocke zu „abholen“); Blase Eichler „Ich habe den Wert völlig unterschätzt. Ich fechte den Kauf an.“, Blase Hegemann „Ich habe auf Sofort kaufen geklickt und bezahlt. Ich will die Kamera.“; drei Frage-Pillen | tabler `bell-ringing`, `tree` | `Fall · Am nächsten Tag an der Haustür` → … → `Die Frage · …` (3 Stände) | Türklingel (`szene_255klingel_1`, Freesound CC0 157250) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | – |
| **C Anspruch** `ansp`→`aufbau2` | Hegemann gegen Eichler, Übergabe und Übereignung, § 433 Abs. 1 Satz 1, Stufen 1/2; beide | tabler `camera`, `list-check` | `Anspruch · …` (3 Stände) | – |
| **D1 Angebot** `ang`→`jeder` | Block Folge 251 (Shopseite nur Einladung), Haken „Sofort kaufen: Angebot zum festen Preis“ + VIII ZR 59/16 Rn. 12, „Auslegung nach §§ 133, 157 BGB mit den Regeln der Plattform“ + VIII ZR 305/10 Rn. 15, „Kauf mit dem Klick, ohne neue Entscheidung“, Block „Angebot an jeden, der zuerst klickt: ad incertas personas“; Eichler | tabler `help-circle`, `building-store`, `camera`, `users` | `I. Vertragsschluss · …` (5 Stände) | – |
| **D2 § 145** `w145`→`nicht` | **Wortlautkarte § 145** (Marker „gebunden“, „ausgeschlossen“), Block „Bindung ausschließen oder einschränken: zulässig“ + Rn. 17, Kreuz „nichts dergleichen erklärt“, Haken „Angebot verbindlich“; Eichler | tabler `lock`, `lock-open` | `I. Vertragsschluss › …` (3 Stände) | – |
| **D3 Annahme** `klick2`→`v014` | Haken „Klick: Annahme ohne Vorbehalt“ + Rn. 23, grüner Block „Kaufvertrag geschlossen: Kamera für 900 €“, Block Verweis Folge 014; Hegemann | tabler `hand-click`, `file-text` | (3 Stände) | – |
| **E § 119 Abs. 1** `anf`→`kein1` | Haken „Anfechtungserklärung gegenüber Frau Hegemann“ (§ 143), „Anfechtungsgrund?“, **Wortlautkarte § 119 Abs. 1** (Marker „über deren Inhalt“, „überhaupt nicht abgeben“), „gewollt: 900 € = erklärt: 900 €“, Kreuz „kein Inhaltsirrtum, kein Erklärungsirrtum“; Eichler | tabler `message`, `equal` | `II. Anfechtung · …` (4 Stände) | – |
| **F § 119 Abs. 2** `w1192`→`hier2` | **Wortlautkarte § 119 Abs. 2** (Marker „Eigenschaften“, „wesentlich angesehen“), Kreuz „Wert selbst: keine solche Eigenschaft“ + OLG Düsseldorf, Haken „nur Umstände, die den Wert bilden: etwa Modell und Zustand“, Block „darüber nicht geirrt, nur Marktpreis falsch eingeschätzt“; Eichler | tabler `camera`, `coin-euro`, `chart-line` | (4 Stände) | – |
| **G Motivirrtum** `motiv`→`risiko` | Block Motivirrtum, Kreuz „wie Kalkulationsirrtum: grundsätzlich keine Anfechtung“ + VIII ZR 79/04, Block BGH zur Auktion + VIII ZR 42/14 Rn. 12, Haken „fester Preis: Risiko ebenso beim Verkäufer“; Eichler | tabler `brain`, `calculator`, `alert-triangle` | (3 Stände) | – |
| **H Ergebnis** `erg`, `erg2` | Haustür ohne Blasen; Haken „an seinen Preis gebunden“, Haken „Kamera für 900 € übergeben und übereignen“ + Fundstellen | wie A4 | `Ergebnis · …` (2 Stände) | – |
| **I Gegenfall** `gegen`→`p122` | „gewollt: 900 €“ → „in der Anzeige: 90 €“, Haken Erklärungsirrtum § 119 Abs. 1 Alt. 2 + VIII ZR 79/04 S. 7, Verweis Folge 251, „unverzüglich angefochten: nichtig“, Block § 122; beide | tabler `keyboard`, `check`, `coin-euro` | `Gegenfall · …` (3 Stände) | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | – |
| **L Prüfungsschema** `sch`→`s3` | breite Karte, 7 Zeilen + Untertitel zum Wort | – | `Prüfungsschema` → je Gliederungspunkt | – |
| **M Merksatz** `merke`, `merk2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), jeweils auf der Blickseite der Figur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Türklingel, als Frau Hegemann zum Abholen klingelt; die Glocke erscheint an der Klingel). Freesound-API am 08.10.2026 gesperrt (HTTP 403), deshalb bitgleiche Kopie einer vorhandenen CC0-Datei aus `sfx3` unter eigenem Namen, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Handy, Bank, Hauswand, Tür, Fenster programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Eichler stellt am Montagmorgen seine seltene Kamera auf einer Plattform ein: fester Preis 900 €, Schaltfläche „Sofort kaufen“. Nach den Regeln der Plattform kommt der Kauf zustande, sobald jemand darauf klickt.
>
> Am Mittag klickt Frau Hegemann auf „Sofort kaufen“ und zahlt die 900 €.
>
> Am Abend sieht Herr Eichler, dass vergleichbare Kameras rund 2.500 € kosten. Modell und Zustand seiner Kamera kannte er genau; nur den Marktpreis hat er unterschätzt.
>
> Am nächsten Tag erklärt er Frau Hegemann an der Haustür, er fechte den Kauf an. Sie verlangt die Kamera.
>
> **Muss Herr Eichler die Kamera für 900 € liefern?**
