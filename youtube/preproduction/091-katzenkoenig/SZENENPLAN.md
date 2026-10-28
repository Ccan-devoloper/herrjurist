# Folge 091 · Katzenkönig-Fall: Mittelbare Täterschaft – Täter hinter dem Täter – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_091.py`](src/skript_091.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Strafrecht/StGB AT, Themenplan-Format „Klassiker-Fall“. Der **echte Fall** (BGH, Urt. v. 15.9.1988 – 4 StR 352/88, BGHSt 35, 347) vereinfacht und mit anderen Namen erzählt; die Vereinfachung wird gesprochen („Wir erzählen ihn vereinfacht und mit anderen Namen“) und auf der Sachverhaltskarte genannt. Neue, vollständige Folge; Skript, Namen, Besetzung und Tonspur **nicht** aus dem Testvideo `katzenkoenig-test/` übernommen (dort Messer, Sturz und Opferfigur – hier bewusst nicht). **Zurückhaltend:** kein Messer, kein Angriff, keine Verletzung im Bild; der „Katzenkönig“ nur als Krone in Ulrichs Gedankenblase (nicht gruselig); das Opfer wird **nicht als Figur** gezeigt (FOLGE-ABLAUF Abschnitt 1: Opfer realer Taten nicht als Comicfigur), nur ihr Blumenladen und ein grünes Herz bei „Sie überlebt“; Glaube nicht verspottet (Kerze als neutrales Ritualsymbol, keine Grimassen). Ablauf: Fall → Frage → Sachverhalt → echter Fall → A. Ulrich: versuchter Mord → Rechtswidrigkeit § 34 → Schuld § 35 → Wortlautkarte § 17 → B. Irmgard und Wolfram: Wortlautkarte § 25 Abs. 1 → Streit Verantwortungsprinzip/BGH → BGH-Formel (wörtlich) → Subsumtion → warum der Streit zählt → Ergebnis → Klausurtipp → Klausurschema → Merksatz. Hauptfilm 6:53,9.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Irmgard, um 40 | treibende Kraft, Hintermann (im Urteil H.) | `standing/robot_dance-3` (Oberteil Rosa `#F6A5C0`, Hose `#3B3B4F`), Kopf `Long Bangs`, Haut `#F3CFB3`. Mimiken `Calm`, `Serious` (redet), `Suspicious` (kühl), `Solemn` | `sabrina` (Frau, mittel) |
| Wolfram, um 45 | Hintermann (im Urteil P.) | `standing/shirt-4` (schwarzes Hemd, Hose Sand `#C9B48A`), Kopf `Short 1`, Brille `Glasses 4`, Haut `#D9A07A`, ohne Bart. Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Solemn` | `marc` (Mann, mittel) |
| Ulrich, um 50 | Polizeibeamter, Vordermann (im Urteil R.) | `standing/walking-1` (Oberteil Blau `#8DB3F2`), Kopf `No Hair 2`, Haut `#E8BE9A`, ohne Bart. Mimiken `Calm`, `Awe` (staunt), `Concerned\|Serious` (Zweifel, redet), `Driven` (glaubt), `Serious` (denkt), `Tired` (Schuld), `Solemn` | `william` (Mann, älter) |
| Opfer | die Frau aus dem Blumenladen | **keine Figur** (nur Blumenladen-Icon, Blumen, Herz) | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem zugeteilten Pool (william, sabrina, marc, laura_ruhig); `laura_ruhig` nicht gebraucht (nur drei Sprechrollen). Testvideo sprach laura_klar/stephan/niklas.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste, nicht Barbara/Peter/Richard/Nora und in keiner Datei unter `youtube/` (`grep -rlw`): Irmgard, Wolfram, Ulrich. Kein Genitiv eines Namens („Strafbarkeit von Ulrich“).
- **Blickrichtung:** Alle Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Wohnung: Irmgard und Wolfram links blicken nach rechts zu Ulrich, Ulrich rechts blickt nach links zu ihnen. Laden: Ulrich blickt zum Laden (`_r`), bei der Flucht nach links weg; bei der Frage blickt Ulrich nach rechts zu Irmgard und Wolfram, die nach links zu ihm blicken. Tafelszenen: alle zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `IR_redet`, `WO_redet`, `UL_redet` (je beide Blickrichtungen) und Lexi. 62 Figuren-PNGs in `../peeps/op_091/` (nicht im Repository, im Drive-Master). `pointing_finger-1` für Ulrich verworfen (Körper ganz schwarz, Oberteil nicht einfärbbar).

**Abweichung von den letzten Folgen:** 087 Wochenmarkt/Bushaltestelle (Posen `polka_dots`, `robot_dance-2`), 088 Baurecht (`easing-2`, `resting-1`), 089 Abtretung (`shirt-3`, `easing-2`, `walking-2`); Testvideo `blazer-3`, `shirt-3`, `crossed_arms-1`, `easing-1`. 091: **Wohnung mit Kerzentisch** und **Straße vor einem Blumenladen am späten Abend** (Mond, Cremegrund; keine Nachtfläche nötig) – neue Schauplätze; Posen `robot_dance-3`, `shirt-4`, `walking-1` in 087–089 nicht verwendet; keine Polka Dots.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Wohnung** `fall`→`glaubt` | Bodenlinie, Tisch (Grundformen `karte`) mit Kerze; links Irmgard und Wolfram, rechts Ulrich, Namensschilder ab 0,0 s | tabler: `id-badge-2`, `candle` (Gelb), `crown` (Gelb) in Ulrichs Gedankenblase, `flower` (Rot) in Irmgards Gedankenblase, `thumb-up`, `world` (Blau), `scale` (Gelb) | `Fall · Irmgard, Wolfram und Ulrich` (ab 0,0 s) → `· Der Katzenkönig` → `· Das Motiv` → `· Das Menschenopfer` → `· Ein Leben gegen Millionen` | Grundbild · Polizeibeamter · leicht zu beeinflussen · Kerze/„Tricks und Rituale“ · Krone · „seit Jahrtausenden …“ · Irmgard kühl, Blumen-Gedanke · „Hass und Eifersucht“ · Wolfram einverstanden · Irmgard redet · Millionen · Ulrich redet · Wolfram redet · Ulrich glaubt, Waage | Streichholz beim Erscheinen der Kerze (`szene_091streichholz_1`, Freesound CC0 423809) |
| **A2 Blumenladen** `tat`→`frage2` | Bodenlinie, Mond, Ulrich vor dem Blumenladen; **kein Angriff im Bild**; Flucht nach links (Tür-Icon); Herz; bei der Frage treten Irmgard und Wolfram dazu | tabler: `moon`, `building-store` (Weiß), `flower` (Rot), `plant-2` (Grün), `door-exit`, `heart` (Grün) | `Fall · Im Blumenladen` → `· Sie überlebt` → `· Die Frage` | Mond · Laden · „sie ahnt nichts“ · Flucht/„andere helfen ihr“ · Herz „Sie überlebt.“ · Frage-Pillen | Ladentürglocke beim Erscheinen des Ladens (`szene_091glocke_1`, Freesound CC0 192761) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Der echte Fall** `echt`→`bgh2` | Tafel; rechts alle drei, Krone, Hammer | tabler: `crown`, `gavel` | `Der echte Fall · Katzenkönig, BGHSt 35, 347` → `› Schuldsprüche bestätigt` | Zeile für Zeile, Haken, gelber Block | – |
| **D A. Ulrich** `ua`→`rt` | Tafel; Ulrich allein | tabler: `heart`, `eye-off`, `door-exit` | `A. Ulrich › Versuchter Mord` → `› Heimtücke` → `› Rücktritt` | Zeilen, Haken, Kreuz | – |
| **E § 34** `n34`→`bew` | Tafel, gelber Block; Ulrich | tabler: `scale` | `A. Ulrich › Rechtswidrigkeit, § 34 StGB` → `› Bewertungsirrtum` | Kreuze, Block | – |
| **F § 35** `n35`→`abs2` | Tafel; Ulrich | tabler: `world` | `A. Ulrich › Schuld › § 35 StGB` → `› § 35 Abs. 2 StGB` | Haken je Personengruppe, Kreuze | – |
| **G § 17** `p17`→`uerg` | **Wortlautkarte § 17** (Marker „die Einsicht, Unrecht zu tun“, „nicht vermeiden konnte“, „kann die Strafe … gemildert werden“); Ulrich | tabler: `world`, `id-badge-2` | `› Verbotsirrtum, § 17 StGB` → `› Verbotsirrtum vermeidbar` → `A. Ulrich › Ergebnis: schuldhaft` | Karte, Marker, Zeilen, grüner Block | – |
| **H § 25 Abs. 1** `hb`→`prob` | **Wortlautkarte § 25 Abs. 1** (Marker „durch einen anderen“); Irmgard und Wolfram | – | `B. Irmgard und Wolfram` → `› § 25 Abs. 1 Alt. 2 StGB` → `› Vordermann voll verantwortlich` | Kreuz, Karte, Zeilen, roter Block | – |
| **I Streit** `vp`→`herr` | Tafel mit lila (Verantwortungsprinzip) und grünem Kasten (BGH), gelber Block; Irmgard und Wolfram | – | `› Streit › Verantwortungsprinzip` → `› Streit › BGH` → `› Streit › Tatherrschaft` | Kästen, Zeilen, Block | – |
| **J BGH-Formel** `formel`→`thdt` | **Zitatkarte BGHSt 35, 347, 354** (wörtlich, Marker zum gesprochenen Wort); alle drei | – | `› Die Formel des BGH` → `› Täter hinter dem Täter` | Karte, drei Marker, grüner Block | – |
| **K Subsumtion** `subs`→`gem` | Tafel; Irmgard und Wolfram | tabler: `crown`, `clipboard-list`, `bulb` | `› Subsumtion` → `› Tatherrschaft kraft überlegenen Wissens` | Haken, Block, Zeile | – |
| **L Warum der Streit zählt** `heimt`, `nb` | Tafel mit rotem (Anstiftung) und grünem Kasten (Täter) | – | `› Warum der Streit zählt` → `› niedrige Beweggründe` | Kästen, Kreuz, Haken | – |
| **M Ergebnis** `erg`, `erg2` | Tafel, grüner und blauer Block; alle drei | tabler: `gavel` | `Ergebnis · Irmgard und Wolfram: mittelbare Täter` → `› Ulrich: versuchter Mord` | 2 | – |
| **N Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | Zeile für Zeile | – |
| **O Klausurschema** `sch`→`sb3` | breite Karte: A. (Vorprüfung/Tatentschluss/Ansetzen, Rechtswidrigkeit, Schuld, Rücktritt), B. (Tatentschluss mit Streit und niedrigen Beweggründen, Ansetzen, Rechtswidrigkeit und Schuld) | – | `Klausurschema` → je Gliederungspunkt ein Pfadstand | 13 Aufbaustufen | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen; Gedankenblasen nur mit Symbol (Krone, Blume). **Zahlen** auf Tafeln, Pillen und Karte als Ziffern („15.9.1988“, „alle 3“, „§ 49 Abs. 1“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Streichholz, Ladenglocke), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Tisch aus Grundformen (`karte`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Irmgard und Wolfram bringen den leicht beeinflussbaren Polizeibeamten Ulrich mit Tricks und Ritualen dazu, an den „Katzenkönig“ zu glauben, der seit Jahrtausenden das Böse verkörpere. Aus Hass und Eifersucht will Irmgard die Frau ihres früheren Freundes töten lassen; Wolfram ist einverstanden.
>
> Sie reden Ulrich ein, der Katzenkönig verlange die Frau als Menschenopfer, sonst vernichte er Millionen Menschen; das Tötungsverbot gelte für sie nicht. Ulrich erkennt, dass das Mord wäre, hält die Tat zur Rettung der Menschheit aber für erlaubt. Nach den Anweisungen von Wolfram greift er die ahnungslose Frau in ihrem Blumenladen von hinten an, um sie zu töten. Als andere ihr helfen, flieht er und rechnet mit ihrem Tod. Sie überlebt.
>
> Nach BGHSt 35, 347 (Katzenkönig), vereinfacht, andere Namen.
>
> **Wie haben sich Ulrich, Irmgard und Wolfram strafbar gemacht?**
