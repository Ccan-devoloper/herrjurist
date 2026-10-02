# Folge 085 · Außenbereich § 35 BauGB: Warum dein Ferienhaus im Wald verboten ist – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_085.py`](src/skript_085.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Themenplan-Format „Klassiker-Fall“). Übungsfall nach dem Hook: Frau Wiesner kauft ein Waldgrundstück weit draußen vor dem Dorf und will dort ein kleines Wochenendhaus bauen; kein Bebauungsplan, der Flächennutzungsplan stellt Wald dar; Herr Dreher von der Bauaufsichtsbehörde lehnt den Bauantrag ab. Ablauf: Fall → Ablehnung und Frage → Sachverhalt → zwei Ebenen, I. Vorhaben (§ 29) → II. Bereich (§ 30 – § 34 – § 35) → III. privilegiert? (§ 35 I Nr. 1, 5; Nr. 4 verneint) → IV. sonstiges Vorhaben (Wortlautkarte § 35 II) → 1. öffentliche Belange (Wortlautkarte § 35 III 1: Nr. 1, 5; Folgetafel Nr. 7) → 2. § 35 IV, 3. Erschließung, Ergebnis → zurück im Wald (Waldrecht, Rechtsschutz) → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 5:13,2 (4.367 gesprochene Zeichen, Regelrahmen).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Wiesner (WI), um 45 | hat ein Waldgrundstück gekauft, Bauherrin | Pose `standing/robot_dance-3` (grünes Oberteil `#8FD694`, dunkelblaue Hose `#3D4A7A`), Kopf `Medium 3`, Haut `#F1C6A5`; Mimiken `Smile` (ruhig, redet), `Smile Big|Smile` (froh), `Suspicious` (denkt), `Concerned|Serious` (Sorge), `Rage|Serious` (Protest, redet), `Tired` (seufzt, redet) | `laura_ruhig` (Frau, mittel) |
| Herr Dreher (DR), um 60 | Bauaufsichtsbehörde | Pose `standing/blazer-3` (braunes Jackett `#8A6E50`, schwarzes Shirt, graue Hose `#7A7A86`), Kopf `Gray Short`, Brille `Glasses`, Haut `#E8B48E`; Mimiken `Serious` (ruhig, redet), `Solemn` (denkt) | `william` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Szene A und K: Frau Wiesner allein im Wald (blickt nach links über ihr Grundstück); Szene B: Frau Wiesner blickt nach rechts zu Herrn Dreher, er nach links zu ihr; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WI_redet`, `WI_protest`, `WI_seufzt`, `DR_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** (`laura_ruhig`, `william`; `sabrina`, `marc` nicht gebraucht – beide in 082 besetzt); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Wiesner, Dreher (nicht in der Liste früherer Namen; `grep` über alle Folgenordner ohne Treffer). Namen nie im Genitiv mit -s.
- Frau Wiesner ist keine „Schwarzbauerin“: Sie stellt ordentlich einen Antrag, ist enttäuscht und nimmt das Ergebnis am Ende gelassen. Herr Dreher sachlich.
- Figuren-PNGs: `../peeps/op_085/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 082 (Imbissbude, Verwaltungsgericht), 083 (Zivilrecht), 081 (Übersicht). Hier **Fichtenwald** (Fluent HC `evergreen-tree`, grün) mit Sonne, Wochenendhaus als Gedanke und Requisit (Fluent HC `hut`, gelb), **Bauaufsichtsbehörde** (Tabler `building`) mit Bauantrag (`file-text`) und Flächennutzungsplan (`map`), Nachbarparzellen als weiße Hütten, Axt (Tabler `axe`) für das Waldrecht. Kein Gerichtsbild (Rechtsschutz nur ein Satz, Säulengebäude klein im Wald). Posen `robot_dance-3` und `blazer-3` in 082/083 nicht verwendet; kein Polka-Dots-Muster. Tageslicht-Cremegrund. Der Wald kehrt am Ende zurück, weil die Geschichte dorthin zurückkehrt.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Wald** `fall`–`wi1` | Fichtenwald weit draußen; Frau Wiesner auf ihrem Grundstück; Denkblase Wochenendhaus; Blase Wiesner | fluent-hc:`evergreen-tree` ×6 (Grün), tabler:`sun`, fluent-hc:`hut` (Gelb); Pillen | `Fall · Das Waldgrundstück` (ab 0,0 s) | Wald · Grundstück · Fichtenwald · Denkblase · klein · Blase | – |
| **B Bauaufsichtsbehörde** `antrag`–`frage` | Behörde, Frau Wiesner und Herr Dreher; Bauantrag; kein B-Plan, FNP Wald; Blase Dreher, Kreuz; Blase Wiesner (Protest); Frage | tabler:`building`, `file-text`, `map` (Grün) | `Fall · Der Bauantrag`, `Fall · Die Ablehnung`, `Fall · War die Ablehnung rechtmäßig?` | Antrag · Dreher · Behörde · B-Plan · FNP · Blase · Kreuz/Sorge · Protest · Frage | Papier (`szene_085papier_1`), als der Bauantrag erscheint |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Zwei Ebenen, I. Vorhaben** `ebenen`–`gelten` | Tafel; Frau Wiesner | fluent-hc:`hut` + Pille | `Grundlagen · Zwei Ebenen des Baurechts`, `I. Vorhaben, § 29 I BauGB` | 2 Blöcke · Vorhaben · Haken · Block | – |
| **E II. Bereich** `reihe`–`p35` | § 30 – § 34 – § 35 | fluent-hc:`evergreen-tree` ×2 + Pille | `II. Bereich (› § 30 BauGB: Bebauungsplan? › § 34 BauGB: Innenbereich? › Außenbereich, § 35 BauGB)` | Zeilen · 2 Kreuze · Block · Fundstelle | – |
| **F III. Privilegiert?** `abs1`–`sonst` | Nr. 1, Nr. 5, Rechtsfolge, Subsumtion, Nr. 4 | tabler:`tractor` (Gelb), `windmill`, fluent-hc:`hut` | `III. Privilegiert, § 35 I BauGB? (› Nr. 4 › nein: sonstiges Vorhaben)` | Zeilen · Icons · Kreuze · Block | – |
| **G IV. Sonstiges Vorhaben** `wl352`–`streng` | Wortlautkarte § 35 II, strenger Maßstab | fluent-hc:`hut` + Pille | `IV. Sonstiges Vorhaben, § 35 II BauGB` | Karte · 2 Marker · Zeile · Block | – |
| **H 1. Öffentliche Belange** `wl353`–`land` | Wortlautkarte § 35 III 1 (Auszug), Nr. 1, Nr. 5 | tabler:`map`, fluent-hc:`evergreen-tree`, `hut` | `IV. › 1. Öffentliche Belange, § 35 III 1 BauGB (› Nr. 1 Flächennutzungsplan › Nr. 5 natürliche Eigenart der Landschaft)` | Karte · 3 Marker · Zeilen · Icons | – |
| **I Nr. 7 Splittersiedlung** `split`–`beein` | Zitat Nr. 7, Definition, Vorbildwirkung | fluent-hc:`hut` (Gelb, Nachbarn Weiß) | `… › Nr. 7 Splittersiedlung`, `…: beeinträchtigt` | Zeilen · Hütten · Block · Kreuz | – |
| **J 2.–3., Ergebnis** `abs4`–`erg` | § 35 IV, Erschließung, Ergebnis; Herr Dreher | tabler:`file-text` + Kreuz | `IV. › 2. Begünstigt, § 35 IV BauGB?`, `IV. › 3. Erschließung`, `Ergebnis · Die Ablehnung war rechtmäßig` | Zeilen · Kreuz · Block · Haken | – |
| **K Zurück im Wald** `wald`–`wi3` | Waldrecht, Verpflichtungsklage, Blase Wiesner | Wald, tabler:`axe`, fluent-hc:`classical-building` | `Ergebnis · Waldrecht`, `Ergebnis · Rechtsschutz` | Sorge · Axt · Pillen · Gebäude · Blase | – |
| **L Klausurtipp** `tipp`–`tipp2` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Erst der Bereich, dann die Gruppe` | Zeilen | – |
| **M Klausurschema** `sch`–`s7` | progressiv: I.–IV. 1.–3. | – | `Klausurschema · § 35 BauGB` | 8 Aufbaustufen | – |
| **N Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Frau Wiesner kauft ein Waldgrundstück weit draußen vor dem Dorf, mitten im Fichtenwald. Dort will sie ein kleines Wochenendhaus bauen und stellt einen Bauantrag. Für die Fläche gilt kein Bebauungsplan; ringsum steht nur Wald. Der Flächennutzungsplan der Gemeinde stellt die Fläche als Wald dar. Das Waldstück ist in viele Parzellen geteilt. Herr Dreher von der Bauaufsichtsbehörde lehnt den Bauantrag ab.“ – Frage: „War die Ablehnung rechtmäßig?“ (kein Fiktiv-Hinweis)
