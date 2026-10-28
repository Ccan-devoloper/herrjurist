# Folge 240 · Schwerer Raub § 250: Spielzeugpistole & Labello-Fall – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_240.py`](src/skript_240.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · StGB BT · Streitstand. Hook nach Plan („Ein Räuber bedroht eine Bäckereiverkäuferin mit einer täuschend echt aussehenden Spielzeugpistole“). Fiktiver Fall: Wiltrud steht früh am Morgen allein hinter der Theke einer Bäckerei; Alois zieht eine täuschend echte schwarze Pistole aus der Jacke („Keine Bewegung! Das Geld aus der Kasse nehme ich mir selbst.“), nimmt 300 € aus der offenen Kasse und rennt hinaus; an der Tür fällt ihm die Pistole aus der Jacke, Bäckermeister Ottfried hebt sie auf: Spielzeug aus Plastik. Abwandlung (Labello-Fall): Lippenpflegestift von hinten in den Rücken.
Ablauf: Fall → Frage → Sachverhalt → A. Raub § 249 bejaht (Verweis 087; § 255 ein Satz) → B. § 250 Abs. 1 Nr. 1 (Wortlautkarte) → a) Waffe? (BGHSt 45, 92) – nein → b) Scheinwaffe (BT-Drucks. 13/9064 S. 18; 4 StR 394/06 Rn. 6) – ja → C. Grenze: Abwandlung Labello (Fallszene), offensichtlich ungefährlich, objektiver Betrachter, Wasserpistole (2 StR 618/10), Streitstand/Kritik (4 StR 394/06 Rn. 8) → D. § 250 Abs. 2 Nr. 1 (Wortlautkarte) – verwendet, aber keine Waffe (4 StR 227/07 Rn. 3) → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:19,5 (5.441 gesprochene Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Wiltrud (WI), um 45 | Bäckereiverkäuferin, bedroht; spricht nicht | `standing/easing-1` (offene Jacke Lila `#B8A9F5`, Oberteil Weiß, schwarze Hose der Pose), Kopf `Medium Straight` (schwarzes Haar), Haut `#F0C8A0`; Mimiken `Calm`, `Fear`, `Concerned\|Serious`, `Suspicious`, `Serious`, `Awe`, `Smile`, `Tired` – alle mit geschlossenem Mund | – |
| Alois (AL), um 25 | Täter; unauffälliger junger Mann, ohne Maske, Kapuze oder „fiese“ Mimik | `standing/walking-1` (T-Shirt Blau `#8DB3F2`, schwarze Hose der Pose), Kopf `Short 3`, Haut `#E3B58E`, kein Bart; Mimiken `Serious` (auch redet), `Solemn`, `Suspicious`, `Calm`, `Fear`, `Concerned\|Serious` | `niklas` (Mann, jung) |
| Ottfried (OT), um 60 | Bäckermeister, Inhaber; findet die Pistole | `standing/shirt-3` (Hemd Grün `#8FD694`, schwarze Hose der Pose), Kopf `Gray Short`, Brille `Glasses 2`, Haut `#E7B995`, kein Bart; Mimiken `Awe` (auch redet), `Suspicious`, `Calm`, `Serious`, `Smile`, `Concerned\|Serious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (niklas, helmut, ela_froh, julia): niklas und helmut. `ela_froh` nicht (ernste Rolle), `julia` vermieden – Wiltrud spricht deshalb nicht; ihre Reaktion zeigt die Mimik.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Namensliste des Auftrags, nicht in `namen_reserviert.txt` und in keinem `.py/.md/.json/.txt/.csv` unter `youtube/` (Volltextsuche 07.10.2026: Alois 0, Wiltrud 0, Ottfried 0 Treffer; verworfen: Kaspar, Gerhard, Hubert, Veit – schon verwendet; Mathis, Leif, Liane, Agnes – Aussprache nicht eindeutig deutsch). Reserviert als „240: Alois, Wiltrud, Ottfried“. Nie im Genitiv (Skript-Assertion). Namensschilder Wiltrud Blau, Alois Grün, Ottfried Gelb, Lexi Gelb.
**Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. Fallszene: Alois vor der Theke blickt nach rechts zu Wiltrud, Wiltrud hinter der Theke blickt nach links zu ihm; auf der Flucht blickt Alois nach links zur Tür; Ottfried blickt zuerst nach links auf die Pistole am Boden, nach dem Aufheben nach rechts zu Wiltrud. Labello-Abwandlung: beide hinter der Theke, Alois hinter Wiltrud, beide blicken nach links. Tafelszenen: alle nach links zur Tafel. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `AL_redet`, `OT_redet` (je links/rechts) und Lexi. Figuren-PNGs `../peeps/op_240/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten Folgen nicht verwendet (235: walking-3, blazer-4; 236: crossed_arms-2, blazer-3; 237: easing-2, blazer-3); 238 und 239 entstehen parallel. Zuerst geprüfte Pose `resting-1` für Wiltrud verworfen (Bauchpartie konnte als Schwangerschaft gelesen werden). robot_dance-1 bleibt Lexi; keine Prothesen-Posen (blazer-1/-2, shirt-1/-2), keine Polka Dots, keine Bärte. Kleidung neu: lila Jacke/weiß (Wiltrud), blaues T-Shirt (Alois), grünes Hemd (Ottfried).
- **Schauplatz neu:** Bäckerei von innen (Rückwand, Ladentür mit Glasfenster, Brotregal mit Backwaren – Fluent Emoji High Contrast `bread`, `baguette-bread`, `croissant`, `pretzel`, gelb gefüllt –, Tür zur Backstube, Verkaufstheke mit Vitrine, Kasse Tabler `cash-register`). Gegenüber 087 (Wochenmarkt), 111 (Elektromarkt) und 236 (Elektrogeschäft) neu.
- **Darstellung (Vorgabe Auftrag):** keine echte Waffe; die Spielzeugpistole erscheint nur als stilisiertes, neutral graues Symbol (Fluent Emoji High Contrast `water-pistol`, Mündung nach links, nie auf eine Person gerichtet) – über Alois, am Boden, in Ottfrieds Hand nach unten links. Lippenpflegestift als neutrale Grundform (weiße Kappe, blaue Hülse, keine Marke; „Labello“ nur als Fallbezeichnung auf Pillen/Tafeln). Keine Gewalt, kein Körperkontakt im Bild. Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Fall** `fall`–`frage2` | ab 0,0 s Bäckerei vollständig; Hook-Pillen „Räuber bedroht Bäckereiverkäuferin“, „Pistole sieht täuschend echt aus“, „früh am Morgen“; Wiltrud hinter der Theke bei ihrem Namen; Alois bei „Alois“ vor der Theke; Pistolensymbol über Alois und Pille „schwarze Pistole aus der Jacke“ bei „Pistole“; Blase Alois „Keine Bewegung! Das Geld aus / der Kasse nehme ich mir selbst.“; Wiltrud weicht zurück (x 1640 → 1740), Pille „hält die Pistole für echt“; Geldschein über der Kasse bei „Kasse“, „300 €“; Alois an der Ladentür, „will das Geld behalten“; Pistole am Boden, „Pistole fällt aus der Jacke“; Ottfried bei „Ottfried“, Schild „Backstube“; Pistole in Ottfrieds Hand bei „hebt“; Blase Ottfried „Die ist ja aus Plastik. / Ein Spielzeug, aber täuschend echt.“, „Spielzeug aus Plastik“; „Wiltrud unverletzt“; Fragepillen | fluent-emoji-high-contrast: `water-pistol`, `bread`, `baguette-bread`, `croissant`, `pretzel`; tabler: `cash-register`, `cash-banknote` | `Fall · Die Bäckerei` → `… Alois kommt herein` → `… Die Pistole` → `… Alois droht` → `… Griff in die Kasse` → `… Flucht mit dem Geld` → `… Die Pistole an der Tür` → `… Ein Spielzeug aus Plastik` → `Fall · Die Frage` | `szene_240tuerglocke_1` bei „Alois“ (Auftritt), `szene_240kasse_1` bei „Kasse“ |
| **B Sachverhalt** `sv` | Karte vollständig (34 px), ≈ 10 s, ohne Fiktiv-Hinweis, mit Abwandlung | – | `Sachverhalt` | – |
| **C Raub § 249** `raub`–`r6` | Tafel: ✓ Sache, ✓ Wegnahme, ✓ Drohung, • Spielzeug schadet nicht (2 StR 618/10 Rn. 4), ✓ Finalität/Vorsatz/Zueignungsabsicht, ✓ Raub (+), Verweis 087, Block § 255/„gleich einem Räuber“; Alois und Wiltrud | tabler: `scale`, `cash-banknote`, `alert-triangle` | `A. Raub, § 249 StGB › …` | – |
| **D1 § 250 Abs. 1 Nr. 1** `q`–`w1b` | **Wortlautkarte § 250 Abs. 1 Nr. 1 a, b (Auszug)** mit fünf Markern; Block „a) und b): zwei Wege für Alois“; Pistolensymbol; Ottfried und Wiltrud | tabler: `scale`; `water-pistol` | `B. Qualifikation, § 250 StGB` → `B. § 250 Abs. 1 Nr. 1 StGB › …` | – |
| **D2 Buchstabe a** `na`–`na3` | Block Waffenbegriff (BGHSt 45, 92 Rn. 5), • Spielzeugpistolen ausgeklammert (Rn. 6), ✗ kein gefährliches Werkzeug, ✗ Buchstabe a scheidet aus; Ottfried und Alois | `water-pistol` | `B. … › a) …` | – |
| **E Buchstabe b** `nb`–`nb5` | • 6. StrRG 1998, • Rechtsausschuss „z. B. eine Spielzeugpistole“ (BT-Drucks. 13/9064 S. 18), Block BGH (4 StR 394/06 Rn. 6; 4 StR 61/23 Rn. 5), ✓ Verwendungsabsicht, ✓ Drohwirkung vom Gegenstand, ✓ Buchstabe b erfüllt; Alois und Wiltrud | `water-pistol` | `B. § 250 Abs. 1 Nr. 1 StGB › b) …` | – |
| **F Abwandlung Labello** `lab`–`lab2` | Bäckerei; Wiltrud hinter der Theke, Alois hinter ihr; Pillen „Labello-Fall (BGH NStZ 1997, 184)“, „Abwandlung: keine Pistole“; Lippenpflegestift oben, „Lippenpflegestift, von hinten in den Rücken“; „hält ihn für die Spitze eines Messers“; Wiltrud ruhig → erschrocken → besorgt | Lippenpflegestift (Grundform) | `C. Grenze › …` | – |
| **G1 Grenze** `lab3`–`lab6` | Block „äußerlich offensichtlich ungefährlich: nicht Buchstabe b“, • Täuschung im Vordergrund, • objektiver Betrachter, ✗ grellbunte Wasserpistole; Wiltrud allein mit Namensschild | Lippenpflegestift; tabler: `eye`; `water-pistol` (rosa/gelb gefüllt = grellbunt) | `C. Grenze › …` | – |
| **G2 Streitstand** `krit`–`krit3` | Block Kritik (Teile der Literatur), • BGH räumt Spannung zum Wortlaut ein, Block „BGH hält an der Grenze fest, wie vom Gesetzgeber erwartet“; Ottfried und Wiltrud | tabler: `scale` | `C. Grenze › …` | – |
| **H § 250 Abs. 2 Nr. 1** `abs2`–`v3` | **Wortlautkarte § 250 Abs. 2 Nr. 1 (Auszug)**, ✓ Verwenden auch als Drohmittel (BGHSt 45, 92 Rn. 7), ✗ keine Waffe, Block st. Rspr. (4 StR 227/07 Rn. 3); Alois und Ottfried | tabler: `scale`; `water-pistol` | `D. § 250 Abs. 2 Nr. 1 StGB › …` | – |
| **I Ergebnis** `erg`–`erg3` | Bäckerei; Ottfried mit der Spielzeugpistole, Wiltrud hinter der Theke; Pillen „Spielzeugpistole: § 250 Abs. 1 Nr. 1 b StGB“, „Mindeststrafe: 3 Jahre, nicht 5“, „Lippenpflegestift: Raub, § 249 StGB“ mit Stift | `water-pistol`, Lippenpflegestift | `Ergebnis · …` | – |
| **J Klausurtipp** `tipp`–`tipp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **K Klausurschema** `sch`–`s3` | breite Karte, I.–III., jede Zeile zum Wort | – | `Klausurschema › …` | – |
| **L Merksatz** `merke`–`mk3` | Lexi erklärt (redet), fünf Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund, wortgleich mit dem Gesprochenen.
**Bewertungszeichen:** Haken nur bei gesprochener Bejahung, Kreuz bei gesprochener Verneinung (Buchstabe a, keine Waffe, Wasserpistole); Kriterien als neutrale Punkte.
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji High Contrast (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Bäckerei, Theke, Regal, Türen und Lippenpflegestift aus Grundformen (`folien_240.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Früh am Morgen steht Wiltrud allein hinter der Theke einer Bäckerei. Alois kommt herein und zieht eine schwarze Pistole aus der Jacke, die täuschend echt aussieht: „Keine Bewegung! Das Geld aus der Kasse nehme ich mir selbst.“ Wiltrud hält die Pistole für echt und weicht zurück. Alois greift in die offene Kasse, nimmt 300 € und rennt hinaus; er will das Geld behalten.
>
> An der Tür fällt ihm die Pistole aus der Jacke. Bäckermeister Ottfried hebt sie auf: eine leichte Spielzeugpistole aus Kunststoff, aber täuschend echt. Wiltrud ist unverletzt.
>
> Abwandlung: Alois hat keine Pistole. Er drückt Wiltrud von hinten einen Lippenpflegestift in den Rücken; sie hält ihn für die Spitze eines Messers. Im Übrigen wie oben.
>
> **Hat Alois einen schweren Raub nach § 250 StGB begangen?**
