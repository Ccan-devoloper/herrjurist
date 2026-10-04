# Folge 187 · Bagger trifft Stromkabel: Reiner Vermögensschaden – kein Ersatz? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_187.py`](src/skript_187.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Deliktsrecht, Klassiker-Fall. Hook nach Plan: „Ein Bagger beschädigt ein Stromkabel – eine Fabrik zwei Kilometer weiter steht einen Tag still.“ Fiktiver Fall nach dem Vorbild des Stromkabel-Falls (BGHZ 29, 65): Fiete (Tiefbauunternehmer, fährt selbst den Bagger) reißt am Rand eines Gewerbegebiets ein Stromkabel des Netzbetreibers auf; die Fahrradfabrik von Gotthard 2 km weiter steht 1 Tag still, Produktionsausfall 48.000 €, nichts geht kaputt. Ablauf: Fall → Frage, Klassiker → Sachverhalt → § 823 Abs. 1 BGB (Wortlautkarte) → Vermögen fehlt (Haftungsbegrenzung, § 826) → Prüfungsweg → I. Eigentum → Gegenfall Substanzschaden → II. Gewerbebetrieb (Begriff, Auffangtatbestand, Betriebsbezogenheit) → Betriebsbezogenheit im Fall → § 823 Abs. 2 (ein Satz) → Ergebnis → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 5:18,4.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Fiete (FI), um 30 | Inhaber eines kleinen Tiefbauunternehmens, fährt den Bagger | `standing/easing-1` (offenes Arbeitshemd Orange `#F9A66C` über weißem Shirt, schwarze Hose, weiße Schuhe), Kopf `Short 3` (dunkelbraun), Haut `#F0C4A0`, keine Brille, kein Bart; Mimiken `Calm`, `Serious`, `Concerned\|Serious` (redet, verteidigt sich), `Suspicious`, `Smile`, `Tired`, `Solemn`, `Fear` | `niklas` (Mann, jung) |
| Gotthard (GO), um 60 | Chef der Fahrradfabrik, verlangt Ersatz | `standing/pointing_finger-1` (dunkler Pullover und Hose – Pose ohne einfärbbare Kleidung), Kopf `Gray Short` (helles kurzes Haar), Brille `Glasses 3`, Haut `#D9A27A`, kein Bart; Mimiken `Calm`, `Fear` (Stromausfall), `Rage\|Serious` (redet), `Very Angry`, `Suspicious`, `Concerned\|Serious`, `Serious`, `Tired`, `Solemn` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (niklas, helmut); ela_froh (nicht für ernste Rollen) und julia (möglichst meiden) nicht gebraucht – deshalb ist die Fabrikleitung abweichend vom Thumbnail-Plan („Fabrikchefin“) ein Mann (Thumbnail angepasst). Junge und ältere Männerstimme klar unterscheidbar.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan, Rechtsstand oder Abnahmebogen unter `youtube/preproduction/` (Volltextsuche 04.10.2026): Fiete, Gotthard – nie im Genitiv („die Fahrradfabrik von Gotthard“). Namensschilder Fiete Orange, Gotthard Blau (wie die Fabrik).
**Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. Szene A1: Gotthard steht rechts vor seiner Fabrik und blickt nach links zur Baustelle; Szene A2: Fiete (links) blickt nach rechts zu Gotthard, Gotthard blickt nach links zu Fiete. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `FI_redet`, `GO_redet` (je links/rechts) und Lexi. Figuren-PNGs: `../peeps/op_187/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen (184: `sitting/mid-2`, `blazer-1`; 185: `resting-2`, `closed_legs-2`, `walking-1`, `walking-2`, `crossed_arms-2`, `shirt-4`, `robot_dance-2`, `mid-1`; 186: `easing-2`, `doctor-nurse-01`, `resting-1`, `blazer-3`) und deren Farbpaare (`blazer-2`, `crossed_arms-1`) nicht verwendet; Prothesen-Posen (`shirt-1`, `shirt-2`, `blazer-2`) für Fiete als Schädiger verworfen. Keine Polka Dots, keine Bärte, keine Karikatur.
- Schauplatz neu: **Baustelle am Gewerbegebiet in Seitenansicht** mit Erdreich im Schnitt, Stromkabel als dunkle Linie mit Blitz-Icons (Tabler `bolt`/`bolt-off`), Bagger (Tabler `backhoe`), Fabrik (Tabler `building-factory-2`). 158 hatte eine Wohnstraße, 149 einen Parkplatz.
- Kein Unfall mit Personen: Die Schaufel reißt das Kabel auf (rote Risslinien, Lücke im Kabel), danach erlöschen die Blitze und die Fabrik wird grau.
- Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Baustelle und Fabrik** `fall`–`heil` | Erdreich im Schnitt, Kabel, Bagger links, Pylonen; Fiete steht neben dem Bagger, steigt ein (Schild unter dem Bagger), Graben und Erdhaufen; Kabel aufgerissen; Fabrik 2 km weiter, Gotthard davor; Stromausfall | tabler:`backhoe` (Gelb), `traffic-cone` (Orange), `bolt`/`bolt-off`, `building-factory-2` (Blau, dann Grau), `bike`, `clock-pause`, `settings` (Grün); Erdreich, Kabel, Graben, Risslinien, Pfeil programmatisch | `Fall · Baustelle am Gewerbegebiet` (ab 0,0 s) → `Fall · Das Stromkabel` → `Fall · Die Fahrradfabrik` → `Fall · Stromausfall` | Baustelle ab 0,0 s · Fiete · Graben · Leitungspläne · Kabel aufgerissen · Netzbetreiber · Fabrik · 2 km · Gotthard · Stromausfall · 1 Tag · nichts kaputt | `szene_187bagger_1` (Freesound CC0 606934) beim Graben, `szene_187maschine_1` (Freesound CC0 482740) beim Stromausfall |
| **A2 Am Graben** `g1`–`klass` | Bagger, Graben, Fiete und Gotthard einander zugewandt, Fabrik grau im Hintergrund | tabler:`backhoe`, `building-factory-2` | `Fall · Gotthard verlangt Ersatz` → `Fall · Die Frage` → `Fall · Ein Klassiker` | Gotthard redet · Fiete redet · Frage · Klassiker mit Fundstelle | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C § 823 Abs. 1 BGB** `norm`–`schema` | **Wortlautkarte** (wörtlich vorgelesen), Marker auf den sechs Rechtsgütern zum Wort; Verweis Folge „Deliktsrecht“; Block „Rechtsgutsverletzung“ | tabler:`book`, `list-check` | `Die Norm: § 823 Abs. 1 BGB` → `› geschützte Rechtsgüter` → `› hier: Rechtsgutsverletzung` | Karte + 6 Marker + 2 Zeilen | – |
| **D Vermögen fehlt** `liste`–`ausn` | Block Rechtsgüter, Kreuz „Vermögen“, Gesetzgeber (XI ZR 51/10 Rn. 26), uferlose Haftung, § 826 | tabler:`list-check`, `wallet`, `scale`, `users-group`, `alert-triangle` | `Die Norm › bestimmte Rechtsgüter` → `Das Vermögen fehlt › …` | Zeile für Zeile | – |
| **E Prüfungsweg** `pruef`–`p2` | zwei Blöcke I./II. | tabler:`building-factory-2`, `settings` | `Prüfung · …` → `› I. Eigentum` → `› II. Gewerbebetrieb` | 3 | – |
| **F I. Eigentum** `eig`–`eigerg` | Haken Kabel/Netzbetreiber, Maschinen unversehrt, zwei Kreuze (nur Unterbrechung; keine Einwirkung), roter Block | tabler:`settings`, `plug-off`, `clock-pause`, `backhoe` | `I. Eigentum › …` (6 Stände) | Zeile für Zeile | – |
| **G Gegenfall** `gegen`–`gg3` | Frage-Block, Asphaltmischwerk, drei Haken | tabler:`bolt-off`, `cpu`, `receipt-euro`, `package-off` | `Gegenfall · Substanzschaden › …` | Zeile für Zeile | – |
| **H II. Gewerbebetrieb** `gew`–`bez` | Begriff, Haken sonstiges Recht, Block Auffangtatbestand, gelber Block Betriebsbezogenheit | tabler:`building-factory-2`, `book`, `shield-check`, `target` | `II. Gewerbebetrieb › …` | Zeile für Zeile | – |
| **I Im Fall** `subs`–`bgh2` | Schaubild: Kabel mit vier Abnehmern des Gewerbegebiets und Bagger, Blitze erlöschen bei allen; Kreuz „kein betriebsbezogener Eingriff“ mit Fundstelle BGHZ 29, 65 | tabler:`building-store`, `building-factory-2`, `building-warehouse`, `building`, `backhoe`, `bolt-off`, `plug-off`, `users-group`, `gavel` | `II. Gewerbebetrieb › im Fall` → `› rein zufällig getroffen` → `› Stromkabel-Fall: nicht betriebsbezogen` | Zeile für Zeile | – |
| **J § 823 Abs. 2** `abs2` | zwei Zeilen, Kreuz „nicht ersichtlich“, Verweis Folge „Schutzgesetz“ | tabler:`book` | `§ 823 Abs. 2 BGB · Schutzgesetz?` | 4 | – |
| **K Ergebnis** `erg`–`vertrag` | roter Block, Haken Netzbetreiber, Gegenfall, offene Frage | tabler:`gavel`, `plug-off`, `package-off`, `building` | `Ergebnis · …` | Zeile für Zeile | – |
| **L Klausurtipp** `tipp`–`tp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Zeile für Zeile | – |
| **M Prüfschema** `sch`–`c3` | breite Karte, I.–III. mit Untermerkmalen | – | `Prüfschema` → je Gliederungspunkt | 4 Aufbaustufen | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („48.000 €“, „2 km“, „1 Tag“, „§ 823 Abs. 1 BGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Erdreich, Kabel, Graben, Erdhaufen, Risslinien, Leitung und Pfeil aus Grundformen (`erdreich()`, `kabel()`, `grube()`, `haufen()`, `funken()`, `netzbild()` in `folien_187.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Fiete führt ein kleines Tiefbauunternehmen. Am Rand eines Gewerbegebiets hebt er mit seinem Bagger einen Graben aus. In die Leitungspläne hat er vorher nicht geschaut. Die Schaufel reißt ein Stromkabel auf, das dem örtlichen Netzbetreiber gehört und das ganze Gewerbegebiet versorgt.
>
> Zwei Kilometer weiter liegt die Fahrradfabrik von Gotthard. Dort fällt der Strom aus; die Fertigung steht einen ganzen Tag still. Kaputt geht dabei nichts, am nächsten Morgen laufen die Maschinen wieder.
>
> Gotthard sagt zu Fiete: „Ein Tag Stillstand kostet mich 48.000 €. Das zahlen Sie!“ Fiete antwortet: „Ich habe ein Kabel getroffen, nicht Ihre Fabrik!“
>
> **Kann Gotthard von Fiete die 48.000 € aus § 823 BGB verlangen?**
