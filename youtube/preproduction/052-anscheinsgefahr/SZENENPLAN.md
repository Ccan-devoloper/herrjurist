# Folge 052 · Anscheinsgefahr: Hilfeschrei aus dem Fernseher – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_052.py`](src/skript_052.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall, Übungsfall nach dem Hook des Themenplans), Beispielland Nordrhein-Westfalen. Sonntagabend kurz vor elf hört Frau Jäger aus der Nachbarwohnung eine Frau um Hilfe schreien; Polizist Ahrens klingelt, klopft, ruft, niemand öffnet; ein Schlüsseldienst bricht das Schloss auf; drinnen läuft bei Herrn Böttcher nur ein Krimi in voller Lautstärke; Wochen später 250 € Kosten und ein kaputtes Schloss. Ablauf: Fall → Frage → Sachverhalt → Landesrecht (Beispiel NRW) und zwei Ebenen → 1. Ebene: 1. Ermächtigungsgrundlage (Wortlaut § 41 I 1 Nr. 4, Abs. 2) → Art. 13 VII GG (Wortlaut) → 2. formell → 3. materiell: Gefahr (Wortlaut § 8 I), konkrete/gegenwärtige Gefahr → Anscheinsgefahr ex ante → Abgrenzung Putativgefahr, Gefahrenverdacht → Verhältnismäßigkeit, Ersatzvornahme im Sofortvollzug, Ergebnis → 2. Ebene: Kosten ex post (§ 52 I) → Subsumtion Böttcher → Entschädigung (Wortlaut § 39 I OBG) → Gegenfall OLG Köln (Zeitschaltuhr, Mitverschulden) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:39,4 (5.719 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Jäger (JA), um 45 | Nachbarin, ruft die Polizei | Pose `standing/crossed_arms-2` (schwarzes Oberteil, lila Hose, verschränkte Arme), Kopf `Bun`, Haut `#D9A07A`; Mimiken `Serious` (ruhig), `Concerned|Serious` (Sorge, redet), `Suspicious` (denkt) | `sabrina` (Frau, mittel) |
| Polizist Ahrens (AH), um 30 | Polizeivollzugsbeamter | Pose `standing/shirt-3` (blaues Hemd `#8DB3F2` wie eine Uniform, schwarze Hose), Kopf `Short 5`, Haut `#C68C66`; Mimiken `Serious`, `Driven` (entschlossen, redet), `Suspicious` (denkt), `Smile` (froh) | `niklas` (Mann, jung) |
| Herr Böttcher (BO/BS), um 72 | Mieter, schaut den Krimi | stehend `standing/walking-1`, sitzend `sitting/mid-2` (beide blaues T-Shirt `#8DB3F2`, schwarze Hose, weiße Schuhe – gleiches Outfit), Kopf `No Hair 2`, Haut `#F0C8A8`; Mimiken `Old` (ruhig), `Awe` (staunt, redet sitzend), `Concerned|Serious` (Sorge, redet), `Suspicious` (denkt), `Tired` (müde) | `helmut` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Jäger blickt nach rechts zur Wand und zur Nachbarwohnung; Szene B: Ahrens blickt nach links zur Tür; Szene C: Böttcher blickt zuerst nach links zum Fernseher, beim Sprechen nach rechts zu Ahrens, der nach links zu ihm blickt; Szene D: Böttcher blickt nach links zum Kostenbescheid; an Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `JA_redet`, `AH_redet`, `BO_redet`, `BS_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 nicht verwendet).
- **Stimmen nur aus dem Pool** helmut, sabrina, niklas, laura_klar (laura_klar nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Jäger, Ahrens, Böttcher (nicht in der Liste früherer Namen). Genitive vermieden („aus der Wohnung von Herrn Böttcher“).
- Figuren-PNGs: `../peeps/op_052/` (68 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 049 Café und Förderstelle, 050/051 andere Schauplätze. Hier: Mietshaus bei Nacht (Fenster mit Mond, Stehlampe, Trennwand zur Nachbarwohnung), Hausflur mit Treppe und Wohnungstür, Wohnzimmer mit Fernseher auf Kommode und Sessel. Posen: `crossed_arms-2` zuletzt 044 (andere Person, Kopf, Rolle), `shirt-3` zuletzt 047, `walking-1` zuletzt 044, `sitting/mid-2` in 040–051 nicht verwendet.
**Nacht:** Der Fall spielt zur Nachtzeit (§ 41 Abs. 2 PolG NRW ist Prüfungsthema). Der Grund bleibt Creme (Tageslicht-Standard); die Nacht zeigen Fenster mit Mond (Tabler `window`, `moon-stars`) und die Pille „Sonntagabend, kurz vor elf“.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Mietshaus** `fall`–`ja1` | Wohnung Jäger, Trennwand, Nachbarwohnung; Schreie, Stille, wieder Schreie; Anruf | tabler:`window`, `moon-stars`, ph:`lamp`, tabler:`ear`, ph:`speaker-high` (Rot), tabler:`device-mobile`, Wand (Karte) | `Fall · Sonntagabend im Mietshaus` (ab 0,0 s) | Grundbild · Ohr · Schreie · Wohnung Böttcher · „Hilfe!“ · still · wieder Schreie · Blase Jäger | – |
| **B Hausflur** `polizei`–`tuer` | Treppe, Tür „Böttcher“; Ahrens klingelt, klopft, ruft; niemand öffnet; es schreit weiter; Blase Ahrens; Schlüsseldienst öffnet | tabler:`stairs`, `door` → ph:`door-open`, tabler:`bell-ringing`, ph:`hand-fist`, `speaker-high`, ph:`toolbox`, tabler:`lock-x` | `Fall · Die Polizei an der Tür` | Flur · Ahrens · klingelt · klopft · ruft · niemand öffnet · „Hilfe!“ · Blase · Schlüsseldienst · Schloss · Tür offen | Klingel (`szene_052klingel_1`), Klopfen (`szene_052klopfen_1`), Schloss (`szene_052schloss_1`) |
| **C Wohnzimmer** `drin`/`bo1` | Fernseher auf Kommode, Sessel, Böttcher sitzt, Ahrens in der Tür; Blase Böttcher | ph:`television` (Blau), fluent-hc:`clapper-board`, ph:`speaker-high`, ph:`armchair` (Lila), Kommode (Karte) | `Fall · In der Wohnung` | Wohnzimmer · Krimi · volle Lautstärke · Blase · Ahrens denkt | – |
| **D Wochen später** `bescheid`–`bo2` | gleiches Wohnzimmer (Rückkehr an denselben Ort, Fernseher aus), Kostenbescheid, kaputtes Schloss, Blase Böttcher | tabler:`file-euro`, `lock-x` | `Fall · Wochen später` | Bescheid · 250 € · Schloss kaputt · Sorge · Blase | – |
| **E Frage** `frage`/`frage2` | zwei Fragen | ph:`door-open`, fluent-hc:`clapper-board` | `Fall · Durfte die Polizei hinein? Wer zahlt?` | Frage 1 · Krimi · Frage 2 | – |
| **F Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **G Landesrecht** `land`–`sek` | Tafel; Ahrens | tabler:`map`, ph:`door-open`, tabler:`file-euro` | `Prüfung · Landesrecht, Beispiel Nordrhein-Westfalen` → `Prüfung · zwei Ebenen` | Beispiel NRW · andere Länder · 1. Ebene · 2. Ebene | – |
| **H Ermächtigungsgrundlage** `egl`–`nacht` | ✗ Generalklausel, ✓ Standardbefugnis; Wortlautkarte § 41 I 1 Nr. 4 mit fünf Markern; Abs. 2 | ph:`door-open`, tabler:`moon-stars` | `1. Ebene: Betreten › 1. Ermächtigungsgrundlage` → `… § 41 I 1 Nr. 4 PolG NRW` → `… › Nachtzeit, § 41 II PolG NRW` | Zeilen · Karte · Marker · ✓ nachts | – |
| **I Art. 13 GG** `art13`–`formell` | Wortlautkarte Art. 13 VII (Auslassung), Marker; formell; Böttcher | tabler:`home`, fluent-hc:`police-car-light` | `… › Art. 13 VII GG` → `1. Ebene: Betreten › 2. formell: Zuständigkeit, § 1 I PolG NRW` | Karte · drei Marker · ✓ zuständig | – |
| **J Gefahr** `gefahr`–`gegenw` | Wortlautkarte § 8 I, Definitionen | fluent-hc:`police-car-light` | `… › 3. materiell: Gefahr, § 8 I PolG NRW` → `… gegenwärtige Gefahr, § 41 I 1 Nr. 4` | Marker · vier Zeilen · gegenwärtig | – |
| **K Anscheinsgefahr** `problem`–`subs` | Tafel; ex ante; Subsumtion mit drei ✓ | ph:`eye` | `… › keine Gefahr?` → `… › Anscheinsgefahr, ex ante` | Titel · ex ante · Definition · Block · ✓ ✓ ✓ · Lebensgefahr | – |
| **L Abgrenzung** `schein`–`verdacht` | Tafel zartrot; Putativgefahr mit Gegenbeispiel ✗; Gefahrenverdacht | ph:`music-notes`, tabler:`ad`, ph:`question` | `… › Abgrenzung: Putativgefahr` → `… › Abgrenzung: Gefahrenverdacht` | Definition · Filmmusik/Werbung · ✗ · Verdacht | – |
| **M Verhältnismäßigkeit** `verh`–`erg1` | Tafel; ✓; Vollzug; Ergebnis | ph:`toolbox`, tabler:`shield-check` | `… › Verhältnismäßigkeit, § 2 PolG NRW` → `… › Vollzug: Ersatzvornahme, §§ 50 II, 52 PolG NRW` → `Ergebnis der ersten Ebene` | ✓ · Ersatzvornahme · Block grün | – |
| **N Kosten** `ebene2`–`zurech` | Tafel; ex post; § 52 I; Anscheinsstörer; Böttcher | tabler:`file-euro` | `2. Ebene · Kosten › Maßstab ex post` → `2. Ebene · Kosten, § 52 I PolG NRW` → `… › Anscheinsstörer` | ex post · „auf Kosten“ · Maßstab | – |
| **O Subsumtion Kosten** `bo_subs`/`zahlt` | Tafel; Böttcher müde | ph:`television`, `speaker-high` | `2. Ebene · Kosten › Herr Böttcher` | drei Zeilen · ✓ Verantwortungsbereich · Block gelb | – |
| **P Entschädigung** `entsch`–`bo_ent` | Wortlautkarte § 39 I OBG, Marker; ✗ b; a analog; ✗ Böttcher | tabler:`lock-x` | `2. Ebene · Entschädigung, § 67 PolG NRW, § 39 I OBG NRW` → `… › Anscheinsstörer wie Nichtstörer` | § 67 · Karte · Marker · ✗ · analog · ✗ | – |
| **Q Gegenfall** `gegen`–`mitv` | Tafel zartrot, echter Fall OLG Köln; Icons rechts statt Figuren | ph:`suitcase-rolling`, `timer`, `television`, tabler:`door` → ph:`door-open`, fluent-hc:`balance-scale` | `Gegenfall · OLG Köln: Zeitschaltuhr` → `… › Entschädigung, § 39 I a OBG NRW` → `… › Mitverschulden, § 40 IV OBG NRW` | Urlaub · Uhr · Fernseher · Tür · ✓ · mittelbar · Mitverschulden · ein Drittel | – |
| **R Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Ebenen trennen` | drei Hinweise | – |
| **S Klausurschema** `sch`–`q7` | Schema baut sich auf | – | `Klausurschema` | Titel · A · 1.–3. · dann · B · Kosten · Entschädigung | – |
| **T Merksatz** `merke`/`m2` | Lexi erklärt, Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** drei Handlungsgeräusche in Szene B (Klingel, Klopfen, Schloss), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Keine Gewaltgeräusche, kein Eintreten der Tür.
**Gewalt:** keine Gewaltbilder; das Aufbrechen ist nur durch Werkzeugkasten, Schloss-Symbol und offene Tür angedeutet. Die Schreie kommen aus dem Krimi; im Bild nur Lautsprecher-Symbol und Pille „Hilfe!“.

## Sachverhaltskarte (Szene F, erscheint vollständig)

> Sonntagabend, kurz vor 23 Uhr, Nordrhein-Westfalen: Frau Jäger hört durch die Wand aus der Nachbarwohnung, wie eine Frau um Hilfe schreit. Dort lebt Herr Böttcher allein. Sie ruft die Polizei. Polizist Ahrens klingelt, klopft und ruft; niemand öffnet, hinter der Tür schreit es weiter. Ein Schlüsseldienst bricht im Auftrag der Polizei das Schloss auf. Drinnen sitzt Herr Böttcher vor dem Fernseher: Ein Krimi läuft so laut, dass er Klingel und Rufe nicht gehört hat. Wochen später verlangt das Polizeipräsidium 250 Euro für den Schlüsseldienst. Das Schloss ist kaputt.
>
> **War das Betreten rechtmäßig? Wer trägt Kosten und Schaden?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen und Zahlen in Ziffern („§ 41 Abs. 1 Satz 1 Nr. 4 PolG NRW“, „250 €“), gesprochen als Wörter. Kleine graue Fundstellenzeilen sind Belege, kein Sprechtext. Die Wortlautkarten § 41 I 1 Nr. 4 PolG NRW, Art. 13 VII GG, § 8 I PolG NRW und § 39 I OBG NRW sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe, Auslassungen „…“); ihre Merkmale werden genannt und zum Wort markiert.
