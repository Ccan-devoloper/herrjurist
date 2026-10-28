# Folge 277 · § 34 BauGB: Wann fügt sich ein Neubau ein? Innenbereich erklärt – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_277.py`](src/skript_277.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Öffentliches Recht/Baurecht · Schema. Voraussetzungsfolge 200 (Baugebiete der BauNVO, nur Verweissatz), 188 (Baugenehmigung) nicht wiederholt, 274 (Gebietserhaltungsanspruch/Nachbarschutz) nur Verweissatz. Übungsfall nach dem Plan-Hook („In einer Straße mit Einfamilienhäusern will ein Investor einen sechsstöckigen Wohnblock bauen“).
**Ablauf:** Fall → Fragen → Sachverhalt → 1. Anwendbarkeit (§ 30 Abs. 1, § 34/§ 35, Ortsteil, Bebauungszusammenhang) → 2. Einfügen: § 34 Abs. 1 (Wortlautkarte), nähere Umgebung und Rahmen, Art über § 34 Abs. 2 (Wortlautkarte), Maß (Rahmenüberschreitung, Spannungen, Vorbildwirkung), Bauweise/Grundstücksfläche, Erschließung → 3. Rücksichtnahme (ein Satz, Verweis 274) → 4. § 34 Abs. 3b (Wortlautkarte), Zustimmung nach § 36a (Wortlautkarte) → Ergebnis (zurück in der Straße) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:27,4 (5.627 vertonte Zeichen); Begründung in ABNAHME.md.

## Darstellung (Vorgabe Koordinator)

Investor **nicht als Bösewicht**: Herr Kronberg will Wohnungen schaffen („Die Stadt braucht Wohnungen. Hier können 24 Familien ein Zuhause finden.“), lächelt, plant am Ende kooperativ neu. Anwohnerin **sachlich**: Frau Morgenstern hat „nichts gegen neue Nachbarn“ und fragt nur, ob sechs Stockwerke in die Straße passen; am Ende „Damit kann ich gut leben.“ Keine Karikatur, keine abwertenden Formulierungen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Kronberg (KR), um 45 | Investor, Bauherr | Pose `standing/blazer-2` (Sakko Dunkelblau `#4A6FA5` über hellem Shirt `#E8EEF6`, schwarze Hose; die Pose hat eine Beinprothese – als gewöhnliches Merkmal einer positiven Figur, nicht als Täterzeichen), Kopf `Short 4`, Brille `Glasses 2`, Haut `#E0AC88`; Mimiken `Calm`, `Smile`, `Suspicious`, `Serious`, `Smile Big\|Smile`; redet (`Smile`) und redet2 (`Calm`) mit a/o/e | `marc` (Mann, mittel) |
| Frau Morgenstern (MO), um 55 | Nachbarin (Einfamilienhaus nebenan) | Pose `standing/easing-1` (offene Bluse Grün `#8FD694` über Lila-Shirt `#B8A9F5`, schwarze Hose), Kopf `Medium Bangs 2` (blond), Haut `#F0C8A8`; Mimiken `Calm`, `Concerned\|Serious`, `Suspicious`, `Serious`, `Smile`; redet (`Concerned\|Serious`) und redet2 (`Smile`) mit a/o/e | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt, redet), Merksatz (erklärt, redet) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In der Straße stehen beide rechts vom Baugrundstück und blicken nach links zum Block; an den Tafeln blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KR_redet`, `KR_redet2`, `MO_redet`, `MO_redet2` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** `william`, `sabrina`, `marc`, `laura_ruhig`: verwendet `marc` und `sabrina`; `laura_ruhig` und `william` nicht (Vorfolge 274).
- **Namen** eindeutig deutsch und neu: Kronberg, Morgenstern (nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, Volltextsuche über `youtube/` ohne Treffer; eingetragen „277: Kronberg, Morgenstern“ vor der Vertonung).
- Figuren-PNGs: `../peeps/op_277/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 274 (`easing-2`, `resting-2`), 275 (`shirt-3`, `robot_dance-2`), 276 (`easing-2`, `pointing_finger-2`) – hier `blazer-2` und `easing-1`, keine Polka Dots, keine Bärte. Schauplatz **Wohnstraße am Stadtrand** mit Einfamilienhäusern (Tabler `home-2`, farbig), Gärten (`fence`, `trees`), altem Haus (grau), Bagger (`bulldozer`), Wohnblock als programmatisch gezeichnetes Geschossbild (6 Geschosse, Palettenfüllung, Tuschekontur; wie die Planausschnitte in 274 als eigene Fläche, kein Icon umgezeichnet), Bauantrag (`file-certificate`). Gegenüber 274 (Gewerbegebiet), 200 (Siedlung mit Planblatt) und 113 (Anbau) eigene Bildidee: Straßenansicht und Geschossdiagramm. Tageslicht-Cremegrund. Die Straße kehrt im Ergebnis zurück (Auflösung: Block gestrichelt, dann neu geplantes zweigeschossiges Haus).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Straße** `fall`–`frage2` | Einfamilienhäuser, Gärten; „kein Bebauungsplan“; Herr Kronberg kauft; Bagger reißt das alte Haus ab; Wohnblock 6 Geschosse/24 Wohnungen; Blase Kronberg; Frau Morgenstern, „Haus Morgenstern“, Blase mit Ring um den Block bei „Stockwerke“; Bauantrag; zwei Fragen | tabler:`home-2` (Gelb/Rosé/Hellblau, alt Grau), `fence`, `trees` (Grün), `bulldozer` (Gelb), `file-certificate` (Gelb); Block als Geschossbild | `Fall · Eine Straße mit Einfamilienhäusern` (ab 0,0 s) … `Fall · Fügt sich der Wohnblock ein?` (9 Stände) | Bagger (`szene_277bagger_1`) bei „abreißen“; Papier (`szene_277papier_1`), als der Bauantrag erscheint |
| **B Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | – |
| **C 1. Anwendbarkeit** `anw`–`strasse` | § 30 Abs. 1 (Kreuz „fehlt“), § 34 oder § 35, Ortsteil, Bebauungszusammenhang (4 C 5.14), Haken, „§ 34 BauGB ist anwendbar“ | tabler:`book`, `map-2`, `buildings`, `home-2`, `map-pin` | `1. Anwendbarkeit › …` (6) | – |
| **D 2. § 34 Abs. 1** `p34`–`w34b` | Wortlautkarte (7 Marker), Merkmalskacheln Art/Maß/Bauweise/Grundstücksfläche zum Wort, „Maßstab: Eigenart der näheren Umgebung“ | tabler:`book`, `road` | `2. Einfügen › …` (3) | – |
| **E Nähere Umgebung, Rahmen** `naeh`–`inn` | Straßenansicht (Geschossbilder, Baugrundstück gestrichelt, Ring), je Merkmal gesondert, Rahmen, im Rahmen (Haken) | tabler:`zoom-in`, `ruler-measure` | `2. Nähere Umgebung › …` (4) | – |
| **F Art, § 34 Abs. 2** `p2`–`v200` | Wortlautkarte (3 Marker), reines Wohngebiet (Haken), Wohngebäude allgemein zulässig (Haken), „Art: Der Block fügt sich ein.“, Verweis 200 | tabler:`book`, `home-2`, `building` | `2. a) Art der Nutzung › …` (4) | – |
| **G Maß** `mass`–`neinm` | Geschossdiagramm: Häuser 1–2 Geschosse, gestrichelter Rahmen, Block 6 Geschosse (Kreuz), gestrichelte Nachahmer bei „berufen“; Ausnahme (Spannungen); Kreuz „fügt sich nicht ein“ | tabler:`ruler-measure`, `buildings` | `2. b) Maß der baulichen Nutzung › …` (7) | – |
| **H Bauweise, Fläche, Erschließung** `bauw`, `ersch` | drei Haken; Zwischenstand-Kacheln Art ✓, Maß ✗, Bauweise ✓, Grundstücksfläche ✓ | tabler:`ruler-measure`, `road` | `2. c) …`, `2. d) Erschließung › gesichert` | – |
| **I 3. Rücksichtnahme** `rueck`, `v274` | Teil des Einfügens (4 C 7.15 Rn. 17), Nachbarhaus neben Block mit Sonne, Verweis 274 | tabler:`scale`, `shield`, `sun` | `3. Rücksichtnahme · …` (2) | – |
| **J 4. § 34 Abs. 3b** `p3b`–`befr` | „neu seit 30.10.2025“ mit BGBl.-Fundstelle, Wortlautkarte (5 Marker), Begründung (Maß), unbefristet anders als § 246e (Haken) | tabler:`calendar`, `home-2`, `hourglass` | `4. § 34 Abs. 3b BauGB › …` (5) | – |
| **K Zustimmung § 36a** `zust`–`rat` | Wortlautkarte S. 2, 4 (4 Marker), Gemeinderat verweigert (Kreuz), „keine Zustimmung, keine Abweichung“ | tabler:`writing-sign`, `clock`, `file-x` | `4. Zustimmung, § 36a BauGB › …` (3) | – |
| **L Ergebnis** `erg`–`mo2` | zurück in der Straße; Block gestrichelt „geplant: 6 Geschosse“; Kreuze „Maß: fügt sich nicht ein“, „ohne Zustimmung keine Abweichung“, „Baugenehmigung: abzulehnen“; Blase Kronberg, bei „zwei“ neues Haus „neu geplant: 2 Geschosse“; Blase Morgenstern | wie A | `Ergebnis · …` (4) | – |
| **M Klausurtipp** `tipp`–`k4` | Lexi warnt: Maßstäbe trennen, Spannungen/Vorbildwirkung, Abs. 3b erst danach, kein Anspruch auf Zustimmung | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (5) | – |
| **N Schema** `sch`–`s5` | progressiv 1. (zwei Zeilen), 2. a)–c), 3., 4., 5. | – | `Schema · …` (9) | – |
| **O Merksatz** `merke`–`m3` | Lexi erklärt, fünf Marker | – | `Merksatz` | – |

## Sachverhaltskarte

„In einer Straße am Stadtrand stehen nur Einfamilienhäuser mit Gärten, ein- oder zweigeschossig und mit Abstand zu den Grenzen; Läden oder Betriebe gibt es nicht. Einen Bebauungsplan gibt es nicht. / Herr Kronberg kauft dort ein Grundstück. Er will das alte Haus abreißen und einen Wohnblock mit 6 Geschossen und 24 Wohnungen bauen. Der Block hält Abstand zu den Grenzen und bleibt in der Bautiefe der Nachbarhäuser; die Erschließung ist gesichert. Frau Morgenstern wohnt nebenan. / Herr Kronberg beantragt die Baugenehmigung, notfalls mit einer Abweichung nach § 34 Abs. 3b BauGB. 2 Monate nach dem Ersuchen der Bauaufsichtsbehörde verweigert der Gemeinderat die Zustimmung: 6 Geschosse passen nicht zu seinen Vorstellungen für die Straße.“ – Frage: „Ist der Wohnblock bauplanungsrechtlich zulässig?“ (kein Fiktiv-Hinweis)

## Gliederung im Bild und im Ton

Erklärung und Prüfpfad zählen gleich („Erstens: Welche Vorschrift gilt?“ … „Viertens: … Absatz drei b“; Pfade „1.“–„4.“). Innerhalb von „2.“ tragen die Pfade die Buchstaben a) Art, b) Maß, c) Bauweise/Grundstücksfläche, d) Erschließung. **Bewusste Abweichung im Schema:** Dort steht die Rücksichtnahme als 2. c) *innerhalb* des Einfügens (so auch gesprochen: „Sie ist Teil des Einfügens“) und die Erschließung als eigener Punkt 3; Abs. 3b wird Punkt 4, das Ergebnis Punkt 5 – das ist der Klausuraufbau; die Bezeichnungen sind dieselben wie in der Erklärung.
