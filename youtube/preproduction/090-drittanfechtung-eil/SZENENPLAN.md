# Folge 090 · Drittanfechtung Baugenehmigung: Eilrechtsschutz nach §§ 80a, 80 V – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_090.py`](src/skript_090.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · VwGO-Praxis, Themenplan-Format „Schema“, Voraussetzung Folge 082 (§ 80 V Grundschema), Verweis auf Folge 088 (Rücksichtnahmegebot, drittschützende Normen). Anwaltsklausur aus Sicht der Nachbarin. Übungsfall nach dem Hook: Neben dem kleinen Haus von Frau Dorn wächst der Rohbau eines Mehrfamilienhauses mit 4 Geschossen (Herr Weber, Baugenehmigung der Stadt); die 12,5 m hohe Wand steht 3 m vor ihrer Grenze (NRW: 0,4 H = 5 m nötig). Frau Dorn klagt (NRW: ohne Widerspruch), Herr Weber baut weiter, Rechtsanwalt Falk stellt den Eilantrag. Ablauf: Fall → Kanzlei/Frage → Sachverhalt → Problem (§ 80 I 1, **Wortlautkarte § 212a I BauGB**, § 80 II 1 Nr. 3) → Antrag (**Wortlautkarte § 80a III VwGO**, Anordnung) → A. Zulässigkeit (Statthaftigkeit, Antragsbefugnis, Rechtsschutzbedürfnis mit § 80 VI, Beiladung § 65 II) → B. Begründetheit (Interessenabwägung im Dreieck, § 212a-Wertung, Erfolgsaussichten, Folgenabwägung; Maßstab nur drittschützende Normen; Abstandsflächen mit Skizze) → Ergebnis, Tenor → Baustelle: Baustopp, Sicherungsmaßnahmen → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:42 (5.899 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Dorn (DO), um 30 | Nachbarin, Klägerin und Antragstellerin | Pose `standing/easing-1` (grüne offene Jacke `#8FD694`, weißes Oberteil, schwarze Hose), Kopf `Long Bangs` (Haar `#5A3A26`), Haut `#F2C7A8`; Mimiken `Calm` (ruhig), `Concerned|Serious` (Sorge, redet), `Suspicious` (denkt), `Rage|Serious` (Ärger), `Smile Big|Smile` (froh) | `julia` (Frau, jung) |
| Herr Weber (WE), um 60 | Bauherr, Beigeladener | Pose `standing/crossed_arms-2` (schwarzer Pullover, braune Hose `#8A6A4A`, verschränkte Arme), Kopf `No Hair 1`, Brille `Glasses 2`, Haut `#EDB98A`; Mimiken `Calm`, `Serious` (redet), `Suspicious` (denkt), `Tired` (müde) | `helmut` (Mann, älter) |
| Rechtsanwalt Falk (FA), um 32 | Anwalt der Nachbarin | Pose `standing/blazer-4` (dunkelblaues Sakko `#3D4E6E`, weißes Oberteil, schwarze Hose), Kopf `Short 1`, Haut `#D9A07A`; Mimiken `Smile` (ruhig), `Serious` (redet), `Solemn` (denkt) | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Baustelle: Frau Dorn blickt nach rechts zum Rohbau und zu Herrn Weber, er blickt nach links zu ihr; Kanzlei: Dorn nach rechts, Falk nach links; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `DO_redet`, `WE_redet`, `FA_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, kein Muster.
- **Stimmen nur aus dem Pool** (`julia`, `helmut`, `niklas`; `ela_froh` nicht gebraucht – die fröhliche Stimme passt nicht zur besorgten Nachbarin); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Dorn, Weber, Falk (nicht in der Liste früherer Namen; `grep -w` über alle Folgenordner ohne Treffer). Namen nie im Genitiv mit -s.
- Herr Weber ist kein Bösewicht: Er hat eine Genehmigung, baut im Vertrauen darauf und plant am Ende um. Frau Dorn wehrt sich sachlich.
- Figuren-PNGs: `../peeps/op_090/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 087 (`polka_dots`, `robot_dance-2`), 088 (`easing-2`, `resting-1`; Einfamilienhaus mit Wohnblock aus Tabler `building`), 089 (`shirt-3`, `easing-2`, `walking-2`). Hier neue Posen `easing-1`, `crossed_arms-2`, `blazer-4` mit anderen Farben und Köpfen, kein Muster. Schauplatz **Baustelle**: Haus mit Garten (Fluent HC `house-with-garden`, gelb) und ein **wachsender Rohbau aus Mauerstücken** (Tabler `wall`, rot, je Geschoss zwei Stücke; das 4. Geschoss erst gestrichelt geplant, dann gemauert), Kelle (Tabler `trowel`), gestrichelte Grundstücksgrenze, Schatten über dem Haus; Kanzlei mit Schreibtisch (Tabler `desk`) und Aktentasche (`briefcase`); Abstandsflächen als **Schnittskizze** auf der Tafel; Baustopp mit Absperrung (Tabler `barrier-block`). Gegenüber 088 bewusst kein Wohnblock-Icon und kein Garten mit Blumen. Tageslicht-Cremegrund. Die Baustelle kehrt beim Baustopp zurück, weil dort die Folge des Beschlusses sichtbar wird.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Baustelle** `fall`–`weiter` | Haus, Frau Dorn; Rohbau wächst (3 Geschosse, 4. geplant), Herr Weber; Schatten; Grenze; Blasen Dorn/Weber; Klage; 4. Geschoss wird gemauert | fluent-hc:`house-with-garden` (Gelb), `classical-building`; tabler:`wall` (Rot), `sun`, `file-certificate`, `trowel` (Gelb); Grenze als Strichlinie, Schattenfläche | `Fall · Das Haus mit Garten` (ab 0,0 s) → `Der Rohbau nebenan` → `Kein Tageslicht mehr` → `Zu nah an der Grenze?` → `Die Klage` → `Es wird weiter gebaut` | Haus · Rohbau · Weber · geplant · Schatten · Sorge · Grenze · Blase Dorn · Blase Weber · Genehmigung · Klage + Gericht · NRW/Land · 4. Geschoss + Kelle | Kelle/Mörtel (`szene_090mauer_1`) beim Wort „gemauert“ |
| **B Kanzlei** `kanzlei`–`frage` | Dorn links, Falk rechts, Schreibtisch | tabler:`desk`, `briefcase`, `file-certificate` | `Fall · In der Kanzlei` → `Fall · Die Frage` | Kanzlei · Falk kommt · Blase Falk · zwei Fragen | – |
| **C Sachverhalt** `sv` | Karte vollständig (≈ 9,8 s) | – | `Sachverhalt` | 1 | – |
| **D Problem** `grund`–`darf` | Tafel, **Wortlautkarte § 212a I BauGB**; Dorn, dann Weber | tabler:`hand-stop` (Grün) → `wall` (Rot) | `Problem · Aufschiebende Wirkung, § 80 I 1 VwGO` → `§ 212a I BauGB` → `§ 80 II 1 Nr. 3 VwGO` | Grundsatz · Karte · Marker · Bau läuft · Nr. 3 · „darf weiterbauen“ | – |
| **E Antrag** `wl80a`–`anord` | Tafel, **Wortlautkarte § 80a III VwGO**; Falk | fluent-hc:`classical-building` | `Antrag · § 80a III VwGO` → `Antrag · § 80a III 2 i. V. m. § 80 V 1 Alt. 1 VwGO` | Karte · Marker · Antrag · Block „anordnen“ · nicht wiederherstellen | – |
| **F A. Zulässigkeit I.–II.** `zul`–`abst` | Tafel; Dorn | tabler:`file-certificate` | `A. Zulässigkeit › I. Statthaftigkeit` → `› II. Antragsbefugnis, § 42 II VwGO analog` | Titel · Hauptsache · Block § 80a · § 123 V · Antragsbefugnis · Abstandsflächen + Haken · Pille Video | – |
| **G A. III., Beiladung** `rsb`–`beil` | Tafel; Dorn, Weber kommt als Beigeladener | tabler:`user-plus` (Orange) | `› III. Rechtsschutzbedürfnis` → `› § 80 VI VwGO?` → `Beteiligte › Beiladung des Bauherrn, § 65 II VwGO` | Klage erhoben · nützt · § 80 VI · Abgaben · Beiladung · einheitlich | – |
| **H B. Interessenabwägung** `begr`–`offen` | Tafel; Dorn und Weber; Waage | fluent-hc:`balance-scale` | `B. Begründetheit › Interessenabwägung` → `› Wertung des § 212a I BauGB` → `› Erfolgsaussichten, summarisch` → `› Folgenabwägung` | Abwägung · Aussetzung · Vollzug · Wertung · Erfolgsaussichten · Folgenabwägung | – |
| **I Maßstab** `nurdritt`–`mass` | Tafel; Dorn | tabler:`scale` | `B. Begründetheit › Maßstab: nur drittschützende Normen` → `› Maß der baulichen Nutzung?` | nicht + Kreuz · sondern + Haken · Maß · offen · Rücksichtnahme | – |
| **J Abstandsflächen** `abf`–`rueck` | Tafel mit **Schnittskizze** (Wand 12,5 m, Grenze, Abstandsfläche 5 m, davon 2 m rot auf ihrem Grundstück, Haus); Dorn; Pillen rechts | fluent-hc:`house-with-garden` (Skizze) | `B. Begründetheit › Erfolgsaussichten › Abstandsflächen` → `› Beispiel NRW` → `› im Fall` → `› Ergebnis` | Schutz · NRW 0,4 H · Skizze · 5 m · 3 m · 2 m rot · keine Abweichung · Block verletzt · Rücksichtnahme offen | – |
| **K Ergebnis/Tenor** `ergeb`–`tenor` | Tafel mit Tenorblock; Dorn froh | fluent-hc:`classical-building` | `Ergebnis · Aussetzungsinteresse überwiegt` → `Ergebnis · Tenor (Klausurkonvention)` | überwiegt · Tenor · Kosten | – |
| **L Baustelle ruht** `stopp`–`we2` | Rohbau mit Absperrung; Dorn froh, Weber denkt/müde, Blase Weber | tabler:`barrier-block` (Rot), `wall`, `sun`; fluent-hc:`house-with-garden` | `Ergebnis · Die Baustelle ruht` → `Ergebnis · Sicherungsmaßnahmen, § 80a III 1, I Nr. 2 VwGO` | Absperrung · Pillen · Weber müde · Blase | – |
| **M Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Rechtswidrig ist nicht genug` → `Klausurtipp · Prüfprogramm der Genehmigung` | nie + Kreuz · immer · Prüfprogramm · NRW | – |
| **N Klausurschema** `sch`–`s8` | breite Karte, baut sich auf | – | `Klausurschema · Eilantrag nach §§ 80a III, 80 V VwGO` | Titel · A · I · II · III · Beiladung · B · I · II · III · C. Tenor | – |
| **O Merksatz** `merke`–`m2` | Lexi erklärt (redet), Merksatz mit Markern | – | `Merksatz` | zwei Sätze, vier Marker | – |

**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („4 Geschosse“, „12,5 m“, „0,4 H“, „§ 212a“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops.
**Geräusch:** ein Handlungsgeräusch aus Freesound CC0 (`szene_090mauer_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Frau Dorn wohnt in einem kleinen Haus mit Garten. Ringsum stehen zweigeschossige Häuser; einen Bebauungsplan gibt es nicht. Die Stadt erteilt Herrn Weber die Baugenehmigung für ein Mehrfamilienhaus mit 4 Geschossen auf dem Nachbargrundstück. Die Hauswand zu Frau Dorn ist 12,5 m hoch und steht 3 m vor ihrer Grenze; eine Abweichung von den Abstandsflächen hat die Stadt nicht zugelassen.
>
> Herr Weber baut sofort. Frau Dorn erhebt Klage beim Verwaltungsgericht (in NRW ohne Widerspruch). Herr Weber baut weiter; Frau Dorn geht zu Rechtsanwalt Falk.
>
> **Warum hält die Klage den Bau nicht auf? Wie prüfst du den Eilantrag?**
