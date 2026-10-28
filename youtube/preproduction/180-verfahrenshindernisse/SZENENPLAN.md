# Folge 180 · Verfahrenshindernisse StPO: Strafantrag, Verjährung & Co. – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_180.py`](src/skript_180.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Format **Klausurfehler**. Beispielfall nach dem Plan-Hook („Der Nachbar hat wegen einer Beleidigung erst vier Monate später Anzeige und Strafantrag gestellt“): Mi, 11.3.2026, beleidigende Äußerung im Treppenhaus; Do, 12.3.2026, Schubser an den Briefkästen (Prellung; **kein Bild der Handlung**); Mo, 13.7.2026, Anzeige und Strafantrag bei der Polizei; August 2026, Abschlussverfügung durch Referendarin Hartlieb. Roter Faden: vier Klausurfehler im Entwurf der Referendarin, je als Karte **falsch – richtig – Fundstelle**.
Ablauf: Fall (Treppenhaus → Polizeiwache → Staatsanwaltschaft) → Sachverhalt → Aufbau (4 Hindernisse, 2 prozessuale Taten, Verweis 039) → Strafantrag § 194 Abs. 1 S. 1 (Wortlaut), § 230, § 77, Form § 158 Abs. 2 StPO → Frist § 77b (Wortlaut) → Kalender Juni 2026 → **Fehler 1** → § 230 Abs. 1 S. 1 (Wortlaut), Nr. 234 RiStBV → Beleidigung: absolutes Antragsdelikt, Hartlieb will Interesse bejahen → **Fehler 2** → Verjährung § 78 Abs. 3 Nr. 4, 5 (Wortlaut), §§ 78a, 78c → **Fehler 3** → Strafklageverbrauch Art. 103 Abs. 3 GG (Wortlaut, BVerfG) → Verfügung § 170 Abs. 2 S. 1 StPO (Wortlaut), §§ 374, 376 StPO, Hartlieb korrigiert → **Fehler 4** → Fehlertabelle → Prüfschema mit Reihenfolge (Klausurpraxis) → Klausurtipp (Lexi) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:52,2 bei 5.731 gesprochenen Zeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Ostwald (OS), um 68 | Nachbar, Verletzter, stellt den Strafantrag | `standing/easing-1` (offene Strickjacke Blau `#8DB3F2`, weißes Shirt, schwarze Hose, weiße Schuhe), Kopf `Gray Short` mit grauem Haar `#BDBDBD`, Brille `Glasses 4`, kein Bart, Haut `#F0CDB4`; Mimiken `Calm`, `Serious` (redet), `Concerned\|Serious`, `Fear`, `Tired`, `Smile` | `helmut` (Mann, älter; ein Satz) |
| Herr Stolte (ST), um 40 | Beschuldigter, spricht nicht | `standing/crossed_arms-1` (Pullover Koralle `#F07A6A`, schwarze Hose, weiße Schuhe), Kopf `Short 3`, kein Bart, Haut `#E2B190`; Mimiken `Calm`, `Contempt` (bei der beleidigenden Äußerung), `Suspicious`, `Serious`, `Tired` | – |
| Referendarin Hartlieb (HA), um 27 | Referendarin bei der Staatsanwaltschaft, macht die Klausurfehler | `standing/resting-2` (schwarzes Oberteil, Hose Lila `#B8A9F5`, Hand in der Hüfte), Kopf `Medium Bangs 3`, Haut `#EDC3A0`; Mimiken `Smile`, `Smile Big\|Smile` (eifrig, redet), `Serious` (redet2), `Calm`, `Suspicious`, `Fear`, `Solemn` | `ela_froh` (Frau, jung; eifrig-heiter) |
| Polizeibeamtin (PB), um 35, Funktionsrolle, spricht nicht | nimmt Anzeige und Antrag auf | `standing/shirt-4` (schwarzes Hemd, Hose Dunkelblau `#2B3A55`, **ohne Abzeichen/Logo**), Kopf `Bun`, Haut `#D9A07A`; `Calm`, `Serious` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Datei unter `youtube/` (Volltextsuche 04.10.2026: Ostwald 0, Stolte 0, Hartlieb 0 Treffer). Nie im Genitiv.
- **Stimmen nur aus dem Pool** (niklas, helmut, ela_froh, julia): Hauptstimme der Fallfiguren ist `ela_froh` (Referendarin, eifrig und heiter – keine ernste Rolle im Sinne einer Tat- oder Opferschilderung; sie spricht drei kurze Sätze); `helmut` nur für den einen Satz des älteren Nachbarn (Alter passt, kein Ersatz im Pool). `niklas` (175/178) und `julia` nicht verwendet.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Treppenhaus: Stolte (`_r`) und Ostwald blicken einander an; Polizeiwache: Beamtin (`_r`) blickt zu Ostwald, er zu ihr; Staatsanwaltschaft: Hartlieb blickt zum Schreibtisch mit der Akte; Tafelfolien: alle blicken zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `OS_redet`, `HA_redet`, `HA_redet2` (je links/rechts) und Lexi.
- Figuren-PNGs: `../peeps/op_180/` (72 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_180.png`.
- Keine Prothesen-Posen, keine Bärte, keine Polka Dots, keine Karikatur; der Beschuldigte in Alltagskleidung, ohne Herkunfts- oder Hautfarben-Klischee, keine „fiese“ Täterfigur; Polizei ohne Logo; keine realen Personen.
- Verworfen im Bau: Hartlieb zuerst in `robot_dance-3` – Silhouette zu nah an Lexi (`robot_dance-1`), deshalb `resting-2`.

**Abweichung von den letzten Folgen:** 177 (`blazer-3`, `robot_dance-2`), 178 (`resting-1`, `shirt-3`), 179 (`blazer-4`, `shirt-3`, `crossed_arms-2`). 180: `easing-1`, `crossed_arms-1`, `resting-2`, `shirt-4` in keiner der drei Vorfolgen; Kleidung Blau/Koralle/Lila: Grün (178 Mattes, 179 Wöhler) bewusst vermieden, Stolte deshalb im Bau von Grün auf Koralle umgefärbt. Schauplätze neu: Treppenhaus mit Treppe, Geländer und Briefkästen, Polizeiwache mit Tresen, Staatsanwaltschaft mit Schreibtisch, Fenster und Aktenstapel; Kalender Juni 2026 (Muster 168, neuer Monat). Kontaktbögen von 177, 178, 179 und 168 verglichen.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Treppenhaus** `fall`→`schub` | Wand, Treppe links mit Geländer, Briefkästen rechts; Stolte und Ostwald ab 0,0 s mit Namensschildern, Fahrrad zwischen ihnen | ph:`bicycle-bold` (Weiß); `treppenhaus()` | `Fall · Im Treppenhaus` (ab 0,0 s) → `· die beleidigende Äußerung` → `· am nächsten Tag` | Grundbild · beide ernst · Pille „Streit ums Fahrrad“ · Pille „beleidigende Äußerung“ (Stolte abfällig, Ostwald erschrocken) · Pille „Am nächsten Tag (12.3.): Schubser … Prellung“ (Ostwald besorgt) | – |
| **A2 Polizeiwache** `juli`→`os1` | Tresen, Polizeibeamtin dahinter, Ostwald | tabler:`calendar-event`, `clipboard-text` | `Fall · Juli: auf der Polizeiwache` → `· Anzeige und Strafantrag` | Grundbild · „4 Monate später“ · „Montag, 13.7.2026“ · Blase Ostwald · Protokoll/Pille „Anzeige und Strafantrag“ | – |
| **A3 Staatsanwaltschaft** `akte`→`frage2` | Schreibtisch, Fenster, Aktenstapel, Hartlieb | tabler:`folders` (Gelb) | `Fall · August: bei der Staatsanwaltschaft` → `· die Abschlussverfügung` → `· ein Klausurfehler?` → `· die Fragen` | Akte landet · „Abschlussverfügung“ · Blase Hartlieb · „Entwurf: Anklage“ · „Ein typischer Klausurfehler!“ (Hartlieb erschrocken) · 2 Fragen | Aktenstapel (`szene_180akte_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Aufbau** `aufbau`→`taten` | Tafel, Hartlieb + Ostwald | tabler:`ban`, `file-text`, `users`, `hourglass`, `gavel`, `calendar-event` | `Aufbau · Verfahrenshindernisse` → `› 1.`–`› 4.` → `· zwei prozessuale Taten` | 4 Blöcke nacheinander · 2 Taten · Verweis 039 | – |
| **D Strafantrag** `p194`→`form` | Wortlautkarte § 194 Abs. 1 S. 1, Ostwald | tabler:`file-text`, `hand-stop`, `user-check`, `id` | `Strafantrag › § 194 Abs. 1 S. 1 StGB` → `› Körperverletzung: § 230 StGB` → `› antragsberechtigt: § 77 Abs. 1 StGB` → `› Form: § 158 Abs. 2 StPO` | Karte · Marker · § 230 · ✓ § 77 · Herr Ostwald · Form | – |
| **E Antragsfrist** `p77b`, `beginn` | Wortlautkarte § 77b (vorgelesen), Hartlieb | tabler:`hourglass`, `user-check` | `Antragsfrist › § 77b Abs. 1 S. 1 StGB: 3 Monate` → `› Beginn: § 77b Abs. 2 S. 1 StGB` | Karte · 6 Marker · Block „3 Monate ab Kenntnis …“ | – |
| **F Kalender Juni 2026** `kenn`→`spaet` | Kalender (Grundform), Ostwald | tabler:`user-check`, `calendar-event`, `calendar-x` | `Antragsfrist › Kenntnis: Mi, 11.3.2026` → `› Ende: Do, 11.6.2026, 24 Uhr` → `› Schubser: Ende Fr, 12.6.2026` → `› Antrag am 13.7.2026: zu spät (-)` | Zeile Kenntnis · Kalender · 11 „Ende“ · Zeile Schubser · 12 „Ende“ · ✗ 13.7. | – |
| **Fehler 1** `f1`, `f1r` | hellgelbe Fehlerkarte, Hartlieb | Warnsymbol | `Klausurfehler 1 › …` | falsch · richtig + Fundstelle | – |
| **G § 230** `p230`→`bejaht` | Wortlautkarte, Hartlieb + Stolte | tabler:`scale`, `lock-open`, `file-text`, `shield-check` | `Öffentliches Interesse › § 230 Abs. 1 S. 1 StGB` → `› relatives Antragsdelikt` → `› vorbestraft: Nr. 234 RiStBV` → `› bejaht (+)` | Karte · 4 Marker · relativ · hilft · Vorstrafe + RiStBV · ✓ bejaht | – |
| **H Beleidigung** `absol`→`ha2` | Tafel, Hartlieb (Blase) | tabler:`message-off`, `lock` | `› und die Beleidigung?` → `› § 194: absolutes Antragsdelikt` → `› Ausnahmen S. 2, 3: nicht einschlägig` → `› auch bei der Beleidigung?` | Frage · ✗ kein Ausweg · Block absolut · Ausnahmen · ✗ Treppenhaus · Blase Hartlieb | – |
| **Fehler 2** `f2`, `f2r` | Fehlerkarte | – | `Klausurfehler 2 › …` | 2 | – |
| **I Verjährung** `p78`→`nichtv` | Wortlautkarte § 78 Abs. 3 Nr. 4, 5, Hartlieb | tabler:`hourglass`, `message-off`, `hand-stop`, `report`, `calendar-check` | `Verjährung › § 78 Abs. 3 StGB` → `› Beleidigung: 3 Jahre (Nr. 5)` → `› öffentliche Beleidigung: 5 Jahre (Nr. 4)` → `› Körperverletzung: 5 Jahre (Nr. 4)` → `› Beginn: § 78a` → `› Unterbrechung: § 78c` → `› nicht verjährt` | Karte · 4 Marker · 3 Rahmen-Zeilen · § 78a · § 78c · ✓ | – |
| **Fehler 3** `f3`, `f3r` | Fehlerkarte | – | `Klausurfehler 3 › …` | 2 | – |
| **J Strafklageverbrauch** `p103`→`keins` | Wortlautkarte Art. 103 Abs. 3 GG, Stolte | tabler:`gavel`, `file-x` | `Strafklageverbrauch › Art. 103 Abs. 3 GG` → `› rechtskräftiges Strafurteil?` → `› hier keines (-)` | Karte · 2 Marker · Sperre · BVerfG · ✗ | – |
| **K Verfügung** `p170`→`ha3` | Wortlautkarte § 170 Abs. 2 S. 1, Hartlieb (Blase) + Stolte | tabler:`folder`, `file-x`, `file-check` | `Verfügung › § 170 Abs. 2 S. 1 StPO` → `› Tat 1, Beleidigung: Einstellung` → `› Tat 2, Körperverletzung: Anklage` → `› der korrigierte Entwurf` | Karte · Tat 1 · Einstellung · Tat 2 · § 376 · Anklage · Blase | – |
| **Fehler 4** `f4`, `f4r` | Fehlerkarte | – | `Klausurfehler 4 › …` | 2 | – |
| **L Fehlertabelle** `tab`→`t4` | breite Tabelle falsch/richtig/Fundstelle | Haken/Kreuz | `Fehlertabelle · …` | Kopf · 4 Zeilen | – |
| **M Prüfschema** `sch`→`reihe` | breite Karte, Aufbau Punkt für Punkt | Warnsymbol | `Prüfschema › I.`–`III.` → `· Reihenfolge: Klausurpraxis` | 8 Stufen + Hinweis | – |
| **N Klausurtipp** `tipp`→`k3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol | `Klausurtipp · 3 Fragen` → `› 1.`–`› 3.` | 3 Fragen nacheinander | – |
| **O Merksatz** `merke`, `m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 2 Sätze, 3 Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 21 Folien; innerhalb harte Schnitte und Pops; keine Figurenbewegung, kein Zoom.
**Geräusch:** ein Handlungsgeräusch aus Freesound CC0 (Aktenstapel), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), Auslassungen mit „…“, amtliche Schreibung („unterläßt“, „daß“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Am Mittwoch, 11. März 2026, streiten Herr Stolte und sein Nachbar Herr Ostwald im Treppenhaus ihres Mietshauses über ein Fahrrad. Herr Stolte macht dabei eine beleidigende Äußerung. Am Donnerstag, 12. März 2026, schubst er Herrn Ostwald an den Briefkästen; Herr Ostwald erleidet eine Prellung am Arm, ein ärztliches Attest liegt vor.
>
> Herr Ostwald erkennt Herrn Stolte jeweils sofort. Erst am Montag, 13. Juli 2026, erstattet er bei der Polizei Anzeige und stellt Strafantrag wegen beider Taten. Herr Stolte ist wegen Körperverletzung vorbestraft.
>
> Im August 2026 entwirft Referendarin Hartlieb bei der Staatsanwaltschaft die Abschlussverfügung.
>
> **Welche Verfahrenshindernisse bestehen – und was verfügt die Staatsanwaltschaft?**
