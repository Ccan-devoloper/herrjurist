# Folge 071 · Unterlassungsdelikt Schema: Unechtes Unterlassen § 13 StGB – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_071.py`](src/skript_071.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB AT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Ein Vater sieht vom Liegestuhl aus, wie sein Kleinkind in den Gartenteich fällt, und bleibt sitzen“), **sehr zurückhaltend**: kein Kind im Wasser, kein Ertrinken, kein Leid. Das Kind erscheint nur als abstraktes Icon an Land (Tabler `mood-kid`), der Sturz nur als Ball und Wellen-Symbol auf dem Teich, danach Rettungswagen-Symbol und Pille „Ihm fehlt nichts.“ Lutz bleibt im Liegestuhl sitzen und nimmt den Tod seines zweijährigen Sohnes billigend in Kauf (nur Sachverhaltsangabe, keine Motive); die Nachbarin Gesa zieht den Jungen nach etwa einer Minute heraus. Ablauf: Fall → Frage → Sachverhalt → Vorab Tun/Unterlassen → Vorprüfung (keine Vollendung, Versuch strafbar) → Wortlautkarte § 13 Abs. 1 → I. Tatentschluss: 1. Erfolg, 2. Nichtvornahme trotz Möglichkeit, 3. Quasikausalität (+ objektive Zurechnung), 4. Garantenstellung (Beschützergarant; Überwachergarant und Ingerenz als Überblick), 5. Entsprechungsklausel → II. Ansetzen, III. Rechtswidrigkeit, IV. Schuld/Zumutbarkeit, V. kein Rücktritt → Ergebnis, Strafmilderung → Abwandlung §§ 222, 13 → Abgrenzung § 323c → Klausurtipp → Prüfschema (vollendetes Delikt, Hinweis Versuch) → Merksatz. Hauptfilm 6:17,8.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Lutz, um 35 | Vater, sorgeberechtigt | im Liegestuhl `sitting/one_leg_up-1`, stehend `standing/walking-2` (beide schwarzes T-Shirt, Jeans Blau `#8DB3F2`, weiße Sneaker; gleiches Outfit), Kopf `Short 1`, Haut `#F0C8A8`, ohne Bart. Mimiken `Calm`, `Smile` (redet), `Serious` (sieht es / ernst), `Solemn` (betroffen), `Concerned\|Serious` (Sorge) | `niklas` (Mann, jung) |
| Gesa, um 30 | Nachbarin, rettet den Jungen | `standing/walking-1` (rotes T-Shirt `#F07A6A`, schwarze Hose) im ganzen Video, Kopf `Long`, Haut `#E2B088`. Mimiken `Fear` (bemerkt den Jungen), `Serious` (springt über den Zaun), `Smile` (redet; erleichtert), `Calm` | `ela_froh` (Frau, jung) |
| Sohn, 2 Jahre | – | **keine Figur**, nur Tabler-Icon `mood-kid` (Gelb) an Land | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Blickrichtung:** Alle drei Posen blicken im Original nach rechts (Kontaktbild `figuren_kontaktbogen.png`); Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. In der Fallszene blickt Lutz (`LS_…_r`) vom Liegestuhl nach rechts zum Teich, Gesa (Grundansicht) von rechts nach links zum Teich. **Vater sachlich:** keine bösen Mimiken (kein `Contempt`, kein `Angry`), keine Klischees, kein Getränk in der Hand. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `LS_redet`, `GE_redet` (je links/rechts) und Lexi. **Stimmen** nur aus dem Pool (niklas, ela_froh; helmut und julia nicht benötigt; 068 sprach julia/helmut). **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan oder Abnahmebogen unter `youtube/` (Volltextsuche): Lutz, Gesa. Figuren-PNGs: `../peeps/op_071/` (48 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 068 (Waldrand in der Dämmerung, Hochsitz; `blazer-4`, `walking-3`), 067 (Straße/Fahrrad), 058 (Wohnung). 071: **Garten am Sommernachmittag mit Liegestuhl, Teich und Zaun zum Nachbargarten** – neuer Schauplatz; Sitzpose `one_leg_up-1` erstmals, `walking-2`/`walking-1` mit neuen Köpfen und Farben. Tageslicht auf Cremegrund (der Fall verlangt keinen Nachtverlauf).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Garten** `fall`→`frage2` | Bodenlinie; links Baum und Liegestuhl (Gestell aus Linienzügen, gelbe Stoffbahn) mit Lutz; Mitte Teich (Ellipse Blau); Sohn-Icon und Ball links vom Teich; rechts Zaun, dahinter Gesa | tabler:`sun` (Gelb), `fence` ×2 (Holz), `mood-kid` (Gelb), `ball-football`; fluent:`deciduous-tree`, `water-wave`, `ambulance`; Pfeil „wenige Schritte“ | `Fall · Sommernachmittag im Garten` (ab 0,0 s) → `Fall · Der Ball rollt ins Wasser` → `Fall · Lutz bleibt sitzen` → `Fall · Die Nachbarin hilft` → `Fall · Die Frage` | Garten mit Lutz ab 0,0 s · „im Liegestuhl“ · Sohn-Icon, Ball, Teich · Lutz redet (Blase) · Ball rollt in den Teich · Sohn-Icon verschwindet, Wellen-Symbol, „Der Junge fällt in den Teich.“ · „sieht es genau“, Pfeil „wenige Schritte: sicher zu retten“ · „Er bleibt sitzen.“ · „hält den Tod für möglich, nimmt ihn billigend in Kauf“ · Gesa erschrocken hinter dem Zaun · Gesa läuft zum Teich, „springt über den Zaun“ · Wellen weg, Sohn-Icon in Gesas Armen, „zieht ihn heraus“ · Gesa redet (Blase) · Rettungswagen, „zur Kontrolle“, „Ihm fehlt nichts.“ · zwei Fragepillen | Ball plumpst ins Wasser (`szene_071plumps_1`, Freesound CC0 867462) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Vorab und Vorprüfung** `tun`→`versuch` | Tafel; Lutz und Gesa rechts | tabler:`armchair`, `mood-kid`, `scale` | `Vorab · Tun oder Unterlassen?` → `Vorab › Unterlassen` → `A. Versuchter Totschlag durch Unterlassen › Vorprüfung: keine Vollendung` → `… › Vorprüfung: Versuch strafbar` → `A. … , §§ 212, 13, 22, 23 StGB` | Zeile für Zeile, Haken/Kreuz, Block | – |
| **D § 13 Abs. 1** `p13`→`entspr` | **Wortlautkarte § 13 Abs. 1** (Marker „einen Erfolg abzuwenden“, „rechtlich dafür einzustehen hat“, „durch ein Tun entspricht“) | tabler:`shield`, `scale` | `A. … › § 13 Abs. 1 StGB` → `› § 13 Abs. 1: Garantenstellung` → `› § 13 Abs. 1: Entsprechung` | Karte + 3 Marker, 2 Haken | – |
| **E Tatentschluss 1.–2.** `tat`→`moegl2` | Tafel | tabler:`bulb`, `lifebuoy`; fluent:`water-wave` | `A. … › I. Tatentschluss` → `› 1. Erfolg` → `› 1. Erfolg: bedingter Vorsatz` → `› 2. Nichtvornahme trotz Möglichkeit` | Zeile für Zeile, Haken | – |
| **F 3. Quasikausalität** `quasi`→`zurech` | Tafel, gelber Block „mit an Sicherheit grenzender Wahrscheinlichkeit“ | tabler:`lifebuoy`, `mood-kid` | `› 3. Quasikausalität` → `› 3. Quasikausalität: Rettung sicher` → `› 3. objektive Zurechnung` | Block, Fundstellen, Haken | – |
| **G 4. Garantenstellung** `garant`→`ing` | Tafel, grüner Kasten Beschützergarant, lila Kasten Überblick Überwachergarant | tabler:`shield`, `shield-check`, `alert-triangle` | `› 4. Garantenstellung` → `› 4. Beschützergarant: Vater` → `› 4. Überblick: Überwachergarant` → `› 4. Überblick: Ingerenz` | Kästen, Haken, Pille „eigene Folgen“ | – |
| **H 5. Entsprechungsklausel** `entspr2`, `verh` | Tafel | tabler:`scale` | `› 5. Entsprechungsklausel` → `› 5. Entsprechung (+)` | Zeilen, Haken | – |
| **I II.–V.** `ansetz`→`rueck` | Tafel; Lutz und Gesa | fluent:`water-wave`; tabler:`lifebuoy`, `mood-kid` | `A. … › II. unmittelbares Ansetzen` → `› III. Rechtswidrigkeit` → `› IV. Schuld: Zumutbarkeit` → `› V. kein Rücktritt, § 24 StGB` | Haken/Kreuz am Wort | – |
| **J Ergebnis** `erg`, `milder` | Tafel, grüner Block | tabler:`gavel`, `scale` | `Ergebnis · Lutz strafbar nach §§ 212, 13, 22, 23 StGB` → `Strafmilderung · § 13 Abs. 2, § 23 Abs. 2 StGB` | Block, zwei Zeilen | – |
| **K Abwandlung** `ab` | hellrote Tafel, nur Lutz | tabler:`eye-off` | `Abwandlung · fahrlässige Tötung durch Unterlassen, §§ 222, 13 StGB` | Zeilen, Haken | – |
| **L Abgrenzung § 323c** `p323`, `echt` | hell-lila Tafel; Lutz und Gesa | tabler:`users` | `Abgrenzung › unterlassene Hilfeleistung, § 323c StGB` → `› echtes Unterlassungsdelikt` | Zeilen, Pille „eigene Folge“ | – |
| **M Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | Zeile für Zeile | – |
| **N Prüfschema** `sch`→`s5` | breite Karte: Vorab; I. Tatbestand 1. objektiv a)–e), 2. subjektiv; II.; III.; IV.; Block „Versuch“ | – | `Prüfschema` → je Gliederungspunkt ein Pfadstand bis `Prüfschema › Versuch` | 13 Aufbaustufen | – |
| **O Merksatz** `merke`→`m3` | Lexi erklärt (redet), drei Sätze mit Marker | – | `Merksatz` | Satz für Satz, Marker | – |

**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026, `bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („Sohn, 2 Jahre“, „§ 13 Abs. 1 StGB“, „2-jährigen“ auf der Sachverhaltskarte).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Ball rollt in den Teich, Gesa läuft vom Zaun zum Teich (A).
**Geräusche:** ein Handlungsgeräusch (Ball plumpst ins Wasser), Freesound CC0 867462, Herkunft in `geraeusche_herkunft.json`. Kein Geräusch beim Sturz des Kindes, keine Sirene.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT; Baum, Wellen-Symbol, Rettungswagen), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Liegestuhl und Teich aus Grundformen der Bausteine (Linienzug, Ellipse wie `ring`/`karte`), keine gezeichneten Figurenteile.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> An einem heißen Sommernachmittag liegt Lutz in seinem Garten im Liegestuhl. Er ist allein mit seinem 2-jährigen Sohn, für den er sorgeberechtigt ist. Der Junge spielt mit einem Ball; ein paar Meter weiter liegt ein flacher Gartenteich.
>
> Der Ball rollt ins Wasser, der Junge läuft hinterher und fällt in den Teich. Lutz sieht das genau. Mit wenigen Schritten könnte er seinen Sohn sicher herausholen, das weiß er. Er bleibt sitzen; er hält es für möglich, dass sein Sohn ertrinkt, und nimmt das billigend in Kauf. Nach etwa einer Minute bemerkt die Nachbarin Gesa den Jungen, springt über den Zaun und zieht ihn heraus. Ihm fehlt nichts.
>
> **Hat sich Lutz strafbar gemacht?**
