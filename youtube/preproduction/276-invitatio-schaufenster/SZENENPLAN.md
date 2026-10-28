# Folge 276 · Invitatio ad offerendum: Ist der Preis im Schaufenster ein Angebot? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_276.py`](src/skript_276.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · BGB AT · Abgrenzung. Aufbau nach Auftrag: Hook (Jacke für 20 statt 200 € im Schaufenster) → Laden: Verlangen und Ablehnung → Frage → Sachverhalt → Anspruch § 433 Abs. 1 Satz 1 (Wer hat angeboten?) → Wortlautkarte § 145, Rechtsbindungswille, invitatio → Wortlautkarten §§ 133, 157 (verständiger Empfänger) → Schaufenster/Katalog/Prospekt = invitatio (h. M.) mit Gründen (Vorrat, Zahlungsfähigkeit, Zahl der Kunden) → Angebot der Kundin, Ablehnung, § 146 → Abgrenzungstafeln (Selbstbedienungsladen mit Streit, SB-Tankstelle, Warenautomat, Onlineshop → Folge 251, Sofort kaufen → Folge 255) → Ergebnis mit Preisangabenrecht → Klausurtipp (Lexi) → Prüfungsschema → Merksatz (Lexi). Hauptfilm 5:58,0 (5.256 vertonte Zeichen). Vorlagen: 255 (Werkzeuge, Hilfsfunktionen, Wortlautkarten), 251/255 (nur Abgrenzung), 014 (nur verwiesen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung:** Personen fiktiv; Laden ohne Namen oder Marke (Ladenschild nur „Mode“), Jacken als Tabler-Icons, keine Logos; kein Fiktiv-Hinweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Edelgard (ED), um 65 | Kundin, verlangt die Jacke für 20 € | `standing/easing-2` (offene Jacke Rot `#F07A6A`, Shirt schwarz der Pose, Hose Grau `#5A5F6E`), Kopf `Gray Medium` (Haar `#D2D2D2`), Brille `Glasses 4`, Haut `#F0C8A8`. Mimiken `Calm`, `Smile` (redet), `Driven` (beharrt, redet), `Smile Big\|Smile`, `Awe`, `Suspicious`, `Serious`, `Concerned\|Serious`, `Solemn` | `hilde` (Frau, älter) |
| Herr Böckmann (BO), um 45 | Inhaber des Modegeschäfts | `standing/pointing_finger-2` (Pullover schwarz der Pose, Hose Blau `#8DB3F2`), Kopf `Short 2`, Haut `#C9946B`, keine Brille, kein Bart. Mimiken `Calm`, `Concerned\|Serious` (redet/Sorge), `Smile`, `Suspicious`, `Serious`, `Fear`, `Solemn` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy): besetzt `hilde` und `christian`; `stephan` und `lucy` nicht besetzt (stephan und christian also nie gemeinsam). Vorfolge 255 nutzte `stephan`/`lucy`.
- **Blickrichtung:** Beide Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Edelgard blickt nach links zum Schaufenster. A2/Ergebnis: Herr Böckmann (`_r`, Zeigefinger zu ihr) und Edelgard (Grundansicht) blicken einander an. Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`, `Smile Big|Smile`); Mundzustände a/o/e nur in `ED_redet`, `ED_beharrt`, `BO_redet` (je links/rechts) und Lexi. 62 Figuren-PNGs in `../peeps/op_276/` (nicht im Repository, im Drive-Master).
- **Klischeeprüfung:** Händler sachlich und freundlich (entschuldigt sich), keine Häme bei der Kundin; keine Prothesen-Posen, keine Polka Dots, keine Bärte; Edelgard ohne Dutt (Abgrenzung zu Lexi). Befund im Bau: `pointing_finger-1` lässt das Oberteil nicht einfärben (Tuschefläche deckt) → `pointing_finger-2` mit farbiger Hose.
- **Namen:** Edelgard, Böckmann – eindeutig deutsche Aussprache, nicht in der Liste vergebener Namen, `grep -rliw` über `youtube/` (`*.py/*.md/*.json/*.csv/*.txt`) ohne Treffer; verworfen: Mechthild (in 239/241/253/261 erwähnt), Fröhlich (in 255 verworfen, Adjektiv). Eingetragen in `namen_reserviert.txt` („276: Mechthild, Fröhlich“, danach Ersatzzeile „276: Edelgard, Böckmann“). Kein Genitiv eines Namens. Gesprochen nur von der Erzählerin.

**Abweichung von den letzten Folgen (251, 255, 270–273):** Posen `easing-2`, `pointing_finger-2` – dort nicht verwendet (251 `easing-1`/`resting-2`, 255 `robot_dance-3`/`blazer-4`, 270 `resting-1`/`robot_dance-2`/`blazer-4`, 271 `resting-1`/`easing-1`, 272 `robot_dance-3`/`crossed_arms-1`/`blazer-3`, 273 `crossed_arms-2`/`shirt-4`); keine Polka Dots. Schauplätze **Ladenfront mit Schaufenster** und **Verkaufsraum** (Kleiderstange, Theke mit Kasse, Ladentür mit Glocke) – neu gegenüber 251 (Schreibtisch/Monitor, Lager), 255 (Wohnzimmer, Park, Haustür). Der Verkaufsraum kehrt im Ergebnis zurück, weil der Streit dort entschieden wird. Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Schaufenster** `fall`→`null` | ab 0,0 s Ladenfront („Mode“), Schaufenster mit Bügel und lila Wolljacke, leeres Preisschild, Ladentür; „20 €“ zum Wort, Pille „statt 200 €?“; Edelgard mit Namensschild ab `edel`; „Samstagvormittag“, „Wolljacke“, „Preisschild: 20 €“, „gemeint: 200 €“, „eine Null fehlt“ | tabler `hanger`, `jacket` | `Fall · Vor dem Schaufenster` → … (4 Stände) | – |
| **A2 Im Laden** `laden`→`frage3` | Kleiderstange mit vier Jacken, Theke mit Kasse, Ladentür; Herr Böckmann; Glocke über der Tür, Edelgard kommt herein; Blasen Edelgard („Ich nehme die Jacke aus dem Schaufenster, für 20 €.“), Böckmann („Das tut mir leid, auf dem Schild fehlt eine Null. Die Jacke kostet 200 €.“), Edelgard („Im Schaufenster steht 20. Das ist Ihr Angebot, und ich nehme es an.“); drei Frage-Pillen | tabler `jacket`, `bell`; Phosphor `cash-register` | `Fall · Im Laden …` → `Die Frage · …` (7 Stände) | Ladenglocke (`szene_276glocke_1`, Freesound CC0 494565) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | – |
| **C Anspruch** `ansp`→`kern` | Edelgard gegen Herrn Böckmann, Übergabe und Übereignung, § 433 Abs. 1 Satz 1, Kaufvertrag aus Angebot und Annahme, Verweis Folge 014, „Wer hat überhaupt das Angebot gemacht?“; beide | tabler `jacket`, `file-text`, `help-circle` | `Anspruch · …` (4 Stände) | – |
| **D1 § 145** `w145`→`inv` | **Wortlautkarte § 145** (Marker „anträgt“, „gebunden“), Haken „Angebot: Erklärung, mit der man sich binden will“, „entscheidend: der Rechtsbindungswille“, Block invitatio + III ZR 220/25 Rn. 13; Böckmann | tabler `lock`, `hand-stop`, `mail-opened` | `I. Angebot · …` (3 Stände) | – |
| **D2 §§ 133, 157** `w133`→`horiz` | **Wortlautkarten § 133** (Marker „wirkliche Wille“) und **§ 157** (Marker „Treu und Glauben“, „Verkehrssitte“), Haken „Maßstab: verständiger Empfänger“, „hier: ein verständiger Passant vor dem Schaufenster“ + VIII ZR 79/04 S. 6; Edelgard | tabler `search`, `eye` | (3 Stände) | – |
| **E Schaufenster** `schauf`→`katalog` | Kreuz „kein Angebot“, Haken „nur Einladung (herrschende Meinung)“, „Gründe für Angebote an die Allgemeinheit“ + 1 StR 146/17 Rn. 21, drei Gründe (Vorrat, Bonität, Zahl der Kunden), Block „10 Kunden, 10-mal gebunden“, Block „ebenso: Katalog und Prospekt“ + III ZR 220/25, III ZR 62/11; Böckmann | tabler `building-store`, `package`, `coin-euro`, `users`, `book` | (5 Stände) | – |
| **F Wer hat angeboten?** `edang`→`leer` | Haken „Angebot: Edelgard im Laden“, Zitat, „Annahme? Das entscheidet Herr Böckmann.“, Kreuz „Er lehnt ab: ihr Angebot erlischt“ + § 146, Block „„Ich nehme Ihr Angebot an“ geht ins Leere: Es gab keins.“; beide | tabler `message`, `hand-stop`, `circle-off` | (3 Stände) | – |
| **G1 Selbstbedienung** `abgr`→`tank` | „Selbstbedienungsladen“, Kreuz „Herausnehmen aus dem Regal bindet noch nicht“ + VIII ZR 171/10 Rn. 15, „Wie der Vertrag an der Kasse entsteht: umstritten“, **Ansicht 1 und Ansicht 2 nebeneinander**, Block SB-Tankstelle + Rn. 13, 16; Edelgard | tabler `arrows-split`, `shopping-cart`, `gas-station`; Phosphor `cash-register` | `Abgrenzung · …` (5 Stände) | – |
| **G2 Automat und online** `auto`→`platt` | Haken „Warenautomat: Angebot an jeden“ (überwiegende Ansicht, Vorbehalte), Kreuz „Onlineshop: nur Einladung“ + Fundstellen, Block Folge 251, Haken „Sofort kaufen: Angebot des Verkäufers“ + VIII ZR 59/16 Rn. 12, Block Folge 255; Böckmann | tabler `coins`, `shopping-cart`, `hand-click` | (3 Stände) | – |
| **H Ergebnis** `erg`→`pangv` | Verkaufsraum wie A2 ohne Blasen; Kreuze „Preisschild im Schaufenster: kein Angebot“, „Herr Böckmann musste nicht annehmen“, „kein Anspruch auf die Jacke für 20 €“ + Fundstellen; Block PAngV + § 10 Abs. 1, § 20 Nr. 1 PAngV, „aber kein Kaufvertrag zu 20 €“ | wie A2 | `Ergebnis · …` (3 Stände) | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | – |
| **L Prüfungsschema** `sch`→`s2` | breite Karte, 7 Zeilen zum Wort | – | `Prüfungsschema` → je Gliederungspunkt | – |
| **M Merksatz** `merke`, `merk2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), jeweils über der sprechenden Figur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Ladenglocke, als Edelgard den Laden betritt; die Glocke erscheint über der Tür). Freesound-API am 08.10.2026 über den Proxy erreichbar; Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor Icons (MIT: `cash-register`, statt Tablers Kasse mit $-Zeichen), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Ladenfront, Schaufenster, Theke, Kleiderstange und Türen programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Edelgard sieht am Samstagvormittag im Schaufenster eines kleinen Modegeschäfts eine Wolljacke. Auf dem Preisschild stehen 20 €. Gemeint waren 200 €; beim Beschriften ist eine Null verloren gegangen.
>
> Im Laden sagt sie zu Herrn Böckmann, dem Inhaber: „Ich nehme die Jacke aus dem Schaufenster, für 20 €.“
>
> Herr Böckmann lehnt ab: Auf dem Schild fehle eine Null, die Jacke koste 200 €. Edelgard meint, das Preisschild im Schaufenster sei sein Angebot, und sie nehme es an.
>
> **Hat Edelgard Anspruch auf die Jacke für 20 €?**
