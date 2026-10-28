# Folge 213 · Öffentliche Sicherheit im Polizeirecht: Was die Polizei schützt – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_213.py`](src/skript_213.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Schema mit Fall, Beispielland Nordrhein-Westfalen. Frau Schulze sprüht ein buntes Bild aus Blumen und Wellen auf das Tor ihrer eigenen Garage; Nachbar Herr Gebauer ruft die Polizei; Herr Neumann fordert sie auf aufzuhören: „Das ist meine Garage.“ Ablauf: Fall → Frage → Sachverhalt → Generalklausel (Wortlaut § 8 Abs. 1 PolG NRW), Merkmal öffentliche Sicherheit → drei Schutzgüter (BVerfGE 69, 315 [352]) → Legaldefinition Sachsen (Wortlaut § 4 Nr. 1 SächsPVDG), Regel bei drohender Straftat, öffentliche Ordnung → Fall: 1. Rechtsordnung (Wortlaut § 303 Abs. 2 StGB, Gestaltungssatzung), 2. Rechte des Einzelnen (Wortlaut § 903 Satz 1 BGB), 3. Staat, Ergebnis → Gegenfall Mietgarage → Kreide: nur private Rechte → Subsidiarität (Wortlaut § 1 Abs. 2 PolG NRW) → Länder-Overlay (NRW, Brandenburg, Sachsen) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:34,5 (5.645 Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Schulze (SC), um 35 | Garagenbesitzerin, im Gegenfall Mieterin | Pose `standing/robot_dance-3` (Oberteil Koralle `#F07A6A`, Hose Anthrazit, ausgestreckter Arm = sprüht), Kopf `Bangs` (braun), Haut `#E8B894`; Mimiken `Calm`, `Smile`, `Serious`, `Suspicious`, `Concerned\|Serious`; redet mit `Driven` | `sabrina` (Frau, mittel) |
| Herr Neumann (NE), um 40 | Polizei (Streife) | Pose `standing/easing-1` (Jacke Dunkelblau `#3D4A7A`, Hemd Hellblau, dunkle Hose wie eine Uniform), Kopf `Shaved 2`, Haut `#D9A07A`; `Calm`, `Serious`, `Suspicious`, `Smile`; redet mit `Serious` | `marc` (Mann, mittel) |
| Herr Gebauer (GB), um 70 | Nachbar, ruft die Polizei | Pose `standing/walking-2` (schwarzes Oberteil, Hose Beige `#C9A66B`), Kopf `No Hair 2`, `Glasses 4`, Haut `#F2CDB0`; `Suspicious`, `Concerned\|Serious`, `Tired`, `Calm`; redet mit `Concerned\|Serious` | `william` (Mann, älter) |
| Frau Dietz (DI), um 60 | Vermieterin und Eigentümerin im Gegenfall | Pose `standing/shirt-1` (Hemd Lila `#B8A9F5`, schwarze Hose, Beinprothese – kein Täterbezug), Kopf `Gray Medium`, `Glasses 2`, Haut `#F0D0B0`; `Calm`, `Very Angry`, `Serious`; redet mit `Very Angry` | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Wohnstraße: Herr Gebauer (links) blickt nach rechts zur Garage, Frau Schulze, Herr Neumann und Frau Dietz blicken nach links zur Garage bzw. zu Frau Schulze; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `SC_redet`, `NE_redet`, `GB_redet`, `DI_redet` (je links/rechts) und Lexi. Keine Bärte.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, in keiner Text-/Code-Datei unter `youtube/` (Volltextsuche 06.10.2026: Schulze, Gebauer, Dietz 0 Treffer; Neumann nur als Autorenname in einer Fundstelle von 124) und vor der Vertonung in `namen_reserviert.txt` eingetragen.
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig; Erzählerin/Lexi Carla ohne Rolle. Die beiden Frauenstimmen sprechen nie in derselben Szene nacheinander (Schulze in A, Dietz in H).
- **Darstellung:** Graffiti neutral (Blumen und Wellen, kein Schriftzug, kein Tag, kein Logo, keine Gang-Klischees); Frau Schulze freundlich, Herr Neumann sachlich und höflich („bitte“), Herr Gebauer besorgt, keine Karikatur.
- Figuren-PNGs: `../peeps/op_213/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 210 (Fahrradladen, Landgericht), 211 und 212 (andere Schauplätze, Posen `resting-1/-2`, `blazer-3/-4`, `shirt-3/-4`, `pointing_finger-1/-2`, `robot_dance-2`, `easing-2`). Hier neu: **Wohnstraße mit Garage und Nachbarhaus bei Tag**, Streifenwagen; Posen `robot_dance-3`, `easing-1`, `walking-2`, `shirt-1` (in 210–212 nicht verwendet), keine Polka Dots. Gegenüber 077 (Stadtpark bei Nacht) Tageslicht und anderer Ort.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Wohnstraße** `fall`–`frage` | Garage (programmatisch), Haus des Nachbarn; Frau Schulze sprüht Wellen, dann Blumen; Herr Gebauer telefoniert, Blase; Streifenwagen, Herr Neumann, Blasen Neumann und Schulze; Frage | ph:`house` (Weiß/Blau), tabler:`sun` (Gelb), `spray` (Rot), `flower` (Gelb/Rot/Lila); fluent-hc:`mobile-phone`; ph:`police-car` (Weiß/Blau); Wellen als Palettenlinien | `Fall · Die Wohnstraße` (ab 0,0 s) → `… Das bunte Garagentor` → `… Der Nachbar ruft an` → `… Die Polizei kommt` → `… „Das ist meine Garage“` → `… Darf die Polizei einschreiten?` | Straße · Welle · Pillen · Blumen · Gebauer · Telefon · Blase · Wagen · Neumann · Blasen · Frage | Sprühstoß (`szene_213spray_1`) bei „sprüht“; Autotür (`szene_213tuer_1`) bei „steigt“ |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Generalklausel** `gk`–`merkmal` | ✗ Standardmaßnahme, Landesrecht, Wortlautkarte § 8 Abs. 1 (3 Marker), Block Merkmal | ph:`police-car`, tabler:`shield` | `Ermächtigungsgrundlage · Generalklausel` → `… Beispiel NRW` → `… § 8 Abs. 1 PolG NRW` → `… Merkmal: öffentliche Sicherheit` | Zeilen · Karte · Marker · Block | – |
| **D Drei Schutzgüter** `drei`–`bverfg` | 3 Farbblöcke, Rechtsgüter, Brokdorf-Fundstelle | tabler:`shield`, `gavel`, `heart`, `building-bank` | `Öffentliche Sicherheit · 3 Schutzgüter` → `› 1. …` → `› 2. …` → `› 3. …` → `› BVerfG, Brokdorf-Beschluss` | Blöcke · Zeilen · Fundstelle | – |
| **E Legaldefinition Sachsen** `sachsen`–`ordnung` | Wortlautkarte § 4 Nr. 1 SächsPVDG, Regel, Abgrenzung öffentliche Ordnung | tabler:`book`, `alert-triangle`, `users` | `› Legaldefinition in Sachsen` → `› Regel: drohende Straftat` → `Abgrenzung · öffentliche Ordnung` | Karte · Zeilen | – |
| **F 1. Rechtsordnung** `pr1`–`rok` | Wortlautkarte § 303 Abs. 2 (5 Marker), ✓ groß und dauerhaft, ✗ fremd, keine Straftat, Gestaltungssatzung ✗, Block | tabler:`spray` | `Fall › 1. Rechtsordnung: …` | Karte · Marker · Zeilen · Blöcke | – |
| **G 2. Rechte des Einzelnen, 3. Staat, Ergebnis** `pr2`–`erg` | Wortlautkarte § 903 Satz 1 BGB (3 Marker), ✗ Nachbar, ✗ Staat, ✗ öffentliche Ordnung, Block keine Gefahr | – | `Fall › 2. Rechte des Einzelnen` → `… § 903 BGB` → `Fall › 3. Staat` → `Fall › öffentliche Ordnung` → `Ergebnis · keine Gefahr` | Karte · Marker · Zeilen · Block | – |
| **H Gegenfall Mietgarage** `gegen`/`di1` | Wohnstraße wie A (gleicher Bildausschnitt, Bild schon gesprüht), Pillen Mieterin/Eigentümerin, Frau Dietz, Blase | wie A ohne Streifenwagen | `Gegenfall · Die Garage ist gemietet` → `… Die Vermieterin` | Szene · Pillen · Dietz · Blase | – (Bild schon vorhanden, keine sichtbare Handlung) |
| **I Gegenfall: Subsumtion** `gfremd`–`gdarf` | ✓ fremd, ✓ unbefugt, ✓ dauerhaft, Block § 303 Abs. 2, verletzt, ✓ konkrete Gefahr, Block darf einschreiten | – | `Gegenfall › fremde Sache` → … → `› Polizei darf einschreiten` | Zeilen · Blöcke | – |
| **J Nur private Rechte?** `subs`–`privat` | Kreide, Regen, ✗ § 303, Mietvertrag und Eigentum, Block private Rechte | tabler:`cloud-rain`, `contract` | `Schutz privater Rechte · nur private Rechte?` → `› Kreide statt Lack` → `› Mietvertrag, Eigentum` | Zeilen · Block | – |
| **K Subsidiarität** `wl12`–`straf` | Wortlautkarte § 1 Abs. 2 PolG NRW (5 Marker), ✗ kein Fall für die Polizei, ✓ bei Straftat Rechtsordnung | tabler:`gavel` | `Schutz privater Rechte › § 1 Abs. 2 PolG NRW` → `› Gericht erreichbar` → `› bei drohender Straftat: Rechtsordnung` | Karte · Marker · Zeilen | – |
| **L Länder-Overlay** `tab`–`teigen` | Tabelle NRW/Brandenburg/Sachsen, Zellen beim Wort, Antrag Sachsen | tabler:`map-2` | `Länder-Overlay · gleiche Struktur, andere Nummern` → `› NRW` → `› Brandenburg` → `› Sachsen: zusätzlich Antrag` → `› dein Landesgesetz` | Kopf · Zeilen · Zellen · Hinweis | – |
| **M Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Rechtsordnung zuerst` → `› jedes Merkmal genau lesen` → `› Subsidiaritätsklausel` | Zeilen | – |
| **N Klausurschema** `sch`–`q5` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` → `› 1. …` … `› 5. Ergebnis` | Titel · 1.–5. mit Unterzeilen | – |
| **O Merksatz** `merke`–`m3` | Lexi erklärt, 5 Marker | – | `Merksatz` | Zeilen · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusche:** zwei Handlungsgeräusche (Sprühstoß, Autotür), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Prüfpfad-Reihenfolge:** wie das Schema: 1. Rechtsordnung, 2. Rechte des Einzelnen, 3. Staat, 4. Subsidiarität (bei rein privaten Rechten), 5. Ergebnis.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Nordrhein-Westfalen, Samstagvormittag: Frau Schulze sprüht mit Sprühlack ein großes, buntes Bild aus Blumen und Wellen auf das Tor ihrer Garage. Haus und Garage gehören ihr; das steht fest. Eine Gestaltungssatzung oder eine andere Vorschrift über die äußere Gestaltung hat ihre Gemeinde nicht erlassen.
>
> Ihr Nachbar Herr Gebauer findet das Bild hässlich und ruft die Polizei: „Hier beschmiert jemand eine Garage.“ Herr Neumann von der Polizei fordert Frau Schulze auf, sofort mit dem Sprühen aufzuhören. Sie antwortet: „Das ist meine Garage.“
>
> **Darf die Polizei einschreiten?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen und Zahlen in Ziffern („§ 303 Abs. 2 StGB“, „3 Schutzgüter“), gesprochen als Wörter. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Wortlautkarten (§ 8 Abs. 1 und § 1 Abs. 2 PolG NRW, § 4 Nr. 1 SächsPVDG, § 303 Abs. 2 StGB, § 903 Satz 1 BGB) sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe).
