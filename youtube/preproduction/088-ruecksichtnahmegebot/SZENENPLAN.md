# Folge 088 · Rücksichtnahmegebot: Der Riesenbau neben deinem Einfamilienhaus – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_088.py`](src/skript_088.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Themenplan-Format „Klassiker-Fall“). Übungsfall nach dem Hook: Frau Kolbe wohnt seit 40 Jahren in ihrem eingeschossigen Einfamilienhaus am Stadtrand (kein Bebauungsplan, ringsum Einfamilienhäuser). Herr Reimers erhält die Baugenehmigung für einen achtgeschossigen Wohnblock (25 m hoch, 50 m lang, 14 m vor ihrem Haus, quer vor dem Garten; Abstandsflächen eingehalten). Der Garten läge im Schatten, Frau Kolbe klagt. Ablauf: Fall → Frage → Sachverhalt → A. Drittanfechtung, Klagebefugnis, Schutznormtheorie, § 113 I 1 → B. drittschützende Normen im Überblick (Abstandsflächen, Gebietserhaltungsanspruch, Maß) → Rücksichtnahmegebot: Herkunft (§ 35 III; Wortlautkarte § 34 I 1; Wortlautkarte § 15 I 2 BauNVO; § 31 II) → Maßstab (BVerwGE 52, 122) → im Fall: Schatten, Abstandsflächen als Indiz, Einfügen → erdrückende Wirkung → zurück am Garten: Subsumtion, Ergebnis, Eilrechtsschutz (Verweis) → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 5:58,1 (5.365 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Kolbe (KO), um 70 | Eigentümerin des Einfamilienhauses, Klägerin | Pose `standing/easing-2` (lila Jacke `#B8A9F5`, schwarzes Oberteil, graue Hose `#6A6A76`), Kopf `Gray Medium` (Haar `#C8C8C8`), Brille `Glasses 2`, Haut `#F2C9A8`; Mimiken `Smile` (ruhig, redet), `Smile Big|Smile` (froh), `Suspicious` (denkt), `Concerned|Serious` (Sorge), `Rage|Serious` (Protest, redet), `Tired` (nicht verwendet) | `hilde` (Frau, älter) |
| Herr Reimers (RE), um 45 | Bauherr des Wohnblocks | Pose `standing/resting-1` (roter Pullover `#F07A6A`, schwarze Hose), Kopf `Short 3` (Haar `#4A3428`), Haut `#E8B48E`; Mimiken `Smile` (ruhig, redet), `Suspicious` (denkt), `Serious` (ernst) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Gartenszenen: Frau Kolbe blickt nach rechts zu Herrn Reimers und zum Block, er nach links zu ihr; an den Tafeln alle nach links. In der Maßstab-Szene stehen beide rechts neben der Tafel (Abwägung zwischen Nachbarin und Bauherr).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KO_redet`, `KO_protest`, `RE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, kein Muster.
- **Stimmen nur aus dem Pool** (`hilde`, `stephan`; `christian` nicht gebraucht – klingt wie `stephan`; `lucy` zu jung für die Rollen); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Kolbe, Reimers (nicht in der Liste früherer Namen; `grep -w` über alle Folgenordner ohne Treffer). Namen nie im Genitiv mit -s.
- Frau Kolbe ist keine „Querulantin“: Sie wehrt sich sachlich und behält recht. Herr Reimers ist kein Bösewicht: Er baut Wohnungen und hält die Abstandsflächen ein; am Ende denkt er nach.
- Figuren-PNGs: `../peeps/op_088/` (48 Dateien, nicht im Repository, im Drive-Master). Gartenszenen mit kleinerer Figurenhöhe (390 px), damit der Block (600 px) die Menschen deutlich überragt.

**Abweichung von den letzten Folgen:** 085 (Fichtenwald, Bauaufsichtsbehörde), 086 (AGB-Kontrolle), 087 (Raub; in Arbeit). Hier **Einfamilienhaus mit Garten** (Tabler `home`, gelb; Zaun `fence`; Fluent HC `sunflower`, `tulip`, welkt im Schatten zu `wilted-flower`), **Wohnblock** (Tabler `building`, blau, 600 px) mit Sonne dahinter und **halbtransparenter Schattenfläche** über dem Garten (Lichtwirkung, kein Requisit), Baugenehmigung (Tabler `file-certificate`), Gericht (Fluent HC `classical-building`, klein, nur beim Ergebnis), Waage (Fluent HC `balance-scale`) beim Maßstab. Posen `easing-2` und `resting-1` in 084–086 nicht verwendet (083: `easing-1`/`resting-1` mit anderen Farben und Köpfen); kein Polka-Dots-Muster. Tageslicht-Cremegrund. Der Garten kehrt zur Subsumtion zurück, weil die Wertung dort sichtbar wird.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Garten** `fall`–`frage` | Haus, Garten, Frau Kolbe; Herr Reimers mit Denkblase Wohnblock, Blase; Baugenehmigung; Block erscheint mit Maßen; Schatten, Blume welkt; Blase Kolbe; Frage | tabler:`home` (Gelb), `fence`, `sun`, `building` (Blau), `file-certificate`; fluent-hc:`sunflower`, `tulip`, `wilted-flower`; Pillen | `Fall · Das Haus am Stadtrand` (ab 0,0 s), `Fall · Der Wohnblock nebenan`, `Fall · Die Baugenehmigung`, `Fall · Kann sie die Genehmigung zu Fall bringen?` | Haus · Pillen · Reimers · Denkblase · Blase · Sorge · Genehmigung · Block · Maße · Schatten · Blase · Frage | Papier (`szene_088papier_1`), als die Baugenehmigung erscheint |
| **B Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **C A. Zulässigkeit** `klage`–`objektiv` | Drittanfechtung, § 42 II, Schutznormtheorie, § 113 I 1 | tabler:`file-certificate` + Pille | `A. Zulässigkeit › …`, `B. Begründetheit › Verletzung eigener Rechte, § 113 I 1 VwGO` | Zeilen · Block · Kreuz · Zitat | – |
| **D Drittschützende Normen** `ueber`–`bleibt` | Abstandsflächen, Gebietserhaltungsanspruch, Maß; es bleibt die Rücksichtnahme | tabler:`building-community` | `B. Begründetheit › Drittschützende Normen › …`, `B. Begründetheit › Rücksichtnahmegebot` | Zeilen · 3 Kreuze · Block | – |
| **E Herkunft I** `herkunft`–`einf` | kein Paragraf, § 35 III, Wortlautkarte § 34 I 1 | fluent-hc:`house`, `houses` | `Rücksichtnahmegebot › Herkunft (› Außenbereich, § 35 III › Innenbereich, § 34 I 1)` | Zeilen · Karte · Marker · Zeile | – |
| **F Herkunft II** `wl15`–`befr` | Wortlautkarte § 15 I 2 BauNVO, § 31 II | tabler:`map` (Grün) | `… › Plangebiet, § 15 I 2 BauNVO`, `… › Befreiung, § 31 II BauGB` | Karte · Marker · Zeilen | – |
| **G Maßstab** `mst`–`zumut` | BVerwGE 52, 122, Je-desto-Formel; Kolbe und Reimers | fluent-hc:`balance-scale` | `Rücksichtnahmegebot › Maßstab (: Abwägung der Zumutbarkeit)` | Zeilen · Reimers · Block | – |
| **H Schatten, Abstandsflächen** `schat`–`regel` | Verschattung, Indiz, Einfügen | tabler:`home`, `building`, `sun` | `Rücksichtnahmegebot › Im Fall › Verschattung / Abstandsflächen als Indiz / fügt sich nicht ein` | Zeilen · Kreuz · Block | – |
| **I Erdrückende Wirkung** `erdr`–`hoehe` | Definition, abriegeln, gleiche Höhe, 8 gegen 1 | tabler:`home`, `building` | `… › erdrückende Wirkung?` | Zeilen · Pillen · Block | – |
| **J Zurück am Garten** `fall2`–`ko2` | Subsumtion mit Maßen, rücksichtslos, Ergebnis mit Gericht, Eilrechtsschutz, Blase Kolbe | wie A, fluent-hc:`classical-building` | `… › erdrückende Wirkung`, `…: rücksichtslos`, `Ergebnis · Die Klage ist begründet`, `Ergebnis · Eilrechtsschutz` | Maße · Pillen · rücksichtslos · Gericht · Eilrechtsschutz · Blase | – |
| **K Klausurtipp** `tipp`–`tipp3` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Klagebefugnis und Begründetheit trennen` | Zeilen | – |
| **L Klausurschema** `sch`–`s8` | progressiv: A I.–II., B I. 1.–3., II. | – | `Klausurschema · Nachbarklage, Rücksichtnahmegebot` | 9 Aufbaustufen | – |
| **M Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Frau Kolbe wohnt seit 40 Jahren in ihrem eingeschossigen Einfamilienhaus am Stadtrand. Ringsum stehen nur ein- und zweigeschossige Einfamilienhäuser; einen Bebauungsplan gibt es nicht. Auf dem Nachbargrundstück südlich ihres Gartens will Herr Reimers einen Wohnblock mit 8 Geschossen und 40 Wohnungen bauen: 25 m hoch, 50 m lang, 14 m vor ihrem Haus, quer vor dem ganzen Garten. Die Abstandsflächen nach der Landesbauordnung hält der Bau ein. Die Bauaufsichtsbehörde erteilt die Baugenehmigung. Frau Kolbe erhebt Klage beim Verwaltungsgericht.“ – Frage: „Kann Frau Kolbe die Baugenehmigung zu Fall bringen?“ (kein Fiktiv-Hinweis)
