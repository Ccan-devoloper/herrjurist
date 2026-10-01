# Folge 025 · Auschwitzlüge: Warum sie nicht von der Meinungsfreiheit geschützt ist – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_025.py`](src/skript_025.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Der echte Fall wird sachlich nacherzählt (Auflage der Landeshauptstadt München für eine Versammlung am 12.5.1991, BVerfG-Beschluss vom 13.4.1994 – 1 BvR 23/94, BVerfGE 90, 241). Den Kern tragen zwei fiktive Figuren: Herr Möller (Versammlungsbehörde) erteilt die Auflage, die Referendarin Svenja fragt nach der Meinungsfreiheit. Ablauf: Fall → Frage → Sachverhalt → Maßstab (Art. 5 statt Art. 8) → Wortlaut Art. 5 I 1 → I. Schutzbereich (Meinung, Tatsachenbehauptung, erwiesen unwahr, Mischäußerung) → Subsumtion → Gegenbeispiel Kriegsschuld → hilfsweise: II. Eingriff → III. Rechtfertigung (Wortlaut Art. 5 II, § 5 Nr. 4 VersG, persönliche Ehre/§ 185 StGB, Abwägung) → Ergebnis → heute: Wortlaut § 130 III StGB, Wunsiedel-Ausnahme → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:33,6 (5.659 Zeichen). Mehr als fünf Minuten wegen der drei Wortlautkarten (Art. 5 I 1, Art. 5 II GG vorgelesen, § 130 III StGB mit Merkmalen), der zweistufigen Prüfung des Gerichts (Schutzbereich verneint, hilfsweise Rechtfertigung mit § 5 Nr. 4 VersG, § 185 StGB und Abwägung) und der heutigen Rechtslage mit Wunsiedel-Ausnahme (Vorgabe Kanalinhaber 01.10.2026: bis 7 Minuten, wo der Stoff es erfordert).

## Würde und Zurückhaltung

- Keine leugnende Aussage im Wortlaut, weder gesprochen noch auf Tafeln oder in Blasen; nur abstrakt („die Judenverfolgung leugnen“).
- Keine NS-Symbole, keine Lager-, Opfer- oder Gewaltbilder, keine Fotos. Ruhige Bilder: Saal mit Stühlen, Behördenzimmer, Gerichtsgebäude-Icons, Tafeln.
- Veranstalter (Partei), Redner, Richter und Politiker treten nicht als Figuren auf und werden nicht genannt; die Stadt erscheint nur als Gebäude-Icon.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Möller (MO), um 58 | Versammlungsbehörde, erteilt die Auflage (Behördenfigur) | Pose `standing/blazer-4` (Jackett Blau `#8DB3F2`, schwarze Hose), Kopf `Gray Short` (helles Haar), Brille `Glasses 2`, Haut `#E6B48F`; Mimiken `Calm` (ruhig), `Serious` (redet/ernst), `Suspicious` (denkt) | `william` (Mann, älter) |
| Svenja (SV), um 26 | Referendarin in der Verwaltungsstation | Pose `standing/easing-1` (Jacke Orange `#F9A66C`), Kopf `Medium Bangs`, Haut `#F1C6A5`; Mimiken `Calm`, `Concerned|Serious` (redet), `Suspicious` (denkt), `Smile` (froh), `Serious` (ernst) | `julia` (Frau, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel bzw. zum Gegenüber), `_r` blickt nach rechts (Möller zu Svenja).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `MO_redet`, `SV_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** niklas, elinor, william, julia: verwendet william und julia; Erzählerin/Lexi Carla ohne Rolle. Keine Überschneidung mit 023 (lisa, christian, stephan).
- **Namen mit eindeutig deutscher Aussprache:** Möller (Umlaut), Svenja; beide nicht in früheren Folgen vergeben. Beide nur von der Erzählerin gesprochen.
- Figuren-PNGs: `../peeps/op_025/` (40 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 023: Anfechtung (Zivilrecht); 020: Fußgängerzone/Skateverbot; 016: Wohnzimmer 1983/Haustür.
- Hier: Versammlungssaal mit Stuhlreihen und Rednertafel, Zimmer der Versammlungsbehörde mit Schreibtisch und Auflagenkarte mit Stempel, Instanzenstufen zum Gerichtsgebäude; erstmals Art. 5 GG und die Unterscheidung Meinung/Tatsache.
- Zwei neue Figuren, Posen `blazer-4` und `easing-1` (nicht in 020–023).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Einladung** `fall`–`erwart` | Saal: Tür, sechs Stühle, Rednertafel; Einladung; Stadt als Gebäude | tabler:`door` (Orange), `armchair` (Lila), `presentation`, `mail-opened`, `building-bank` (Grau); Pillen „München, Frühjahr 1991“, „Parteiverband“, „Einladung zur Versammlung“, „Saal“, „Stadt München“, „erwartet:“, „Leugnung der Judenverfolgung“ | `Fall · Die Einladung` (ab 0,0 s) | Saal ab 0,0 s · Parteiverband · Einladung · Saal · Stadt · erwartet · Leugnung | – |
| **B Die Auflage** `moeller`–`s1` | Behördenzimmer; Möller (links, blickt nach rechts), Schreibtisch, Svenja (rechts); Auflagenkarte links | tabler:`table` (Orange), `files`, `lamp`, `rubber-stamp` (Rot, senkt sich) | `Fall · Die Auflage` | Möller · Namen · Blase Möller · Karte + Stempel · vier Auflagenpunkte zum Wort · Svenja denkt · Blase Svenja | Stempel `szene_025stempel_1` |
| **C Der Weg nach Karlsruhe / Die Frage** `klage`–`frage` | drei Instanzstufen mit Kreuzen, Dokument gleitet zum Bundesverfassungsgericht | tabler:`building-bank` (Grau), `file-text` (bewegt), fluent-hc:`classical-building` | `Fall · Der Weg nach Karlsruhe` → `Fall · Die Frage` | findet statt · drei Gerichte · Kreuze · BVerfG + Dokument · Pille · zwei Fragen | Umschlag `szene_025brief_1` |
| **D Sachverhalt** `sv` | Sachverhaltskarte vollständig (≈ 10 s) | – | `Sachverhalt` | 1 | – |
| **E Maßstab** `mass`/`gegenst` | Tafel, Svenja | `users-group`, `message-circle` | `Maßstab: Art. 5 I GG, nicht Art. 8 GG` | ✓ Art. 5 · ✗ Art. 8 · bestimmte Äußerungen | – |
| **F Wortlaut Art. 5 I 1** `wl5` | Wortlautkarte, vorgelesen, Marker zum Wort | `book` | `Art. 5 I GG › Wortlaut` | Karte · sieben Marker | – |
| **G Meinung** `sb`–`egal` | Tafel, Svenja | `message-circle` | `Art. 5 I GG › I. Schutzbereich` → `› Meinung` | Titel · Definition · nicht wahr/unwahr · (+)(+) · froh | – |
| **H Tatsachenbehauptung** `tats`–`pflicht` | Tafel, Herr Möller | `search`, `bulb`, `ban` (Rot), `scale` | `… › Tatsachenbehauptung` → `… › erwiesen unwahre Tatsachen` | prüfbar · ✓ geschützt soweit · Block nicht geschützt · kein schützenswertes Gut · Wahrheitspflicht | – |
| **I Tatsache und Wertung** `misch`–`ganz` | Tafel, Svenja | `puzzle` | `… › Tatsache und Wertung verbunden` | Pillen Tatsache + Wertung · trennen nur … · Block insgesamt Meinung | – |
| **J Subsumtion** `subs`–`nicht` | Tafel, Svenja ernst | `files`, `gavel`, `books` | `… › Leugnung der Judenverfolgung` | Tatsachenbehauptung · drei Belege einzeln · Block nicht geschützt ✗ | – |
| **K Gegenbeispiel** `schuld`/`ereig` | Tafel, Möller | `scale`, `calendar` | `… › Gegenbeispiel: Schuldfragen` | Kriegsschuld · komplexe Beurteilungen (+) · Ereignis = Tatsache | – |
| **L Hilfsweise / II. Eingriff** `hilfs`/`ein` | Tafel, Svenja | `message-circle`, `clipboard-text` | `… › hilfsweise: im Zusammenhang geschützt` → `Art. 5 I GG › II. Eingriff` | Zusammenhang · ✓ geschützt · Block Eingriff ✓ | – |
| **M Wortlaut Art. 5 II** `wl52` | Wortlautkarte, vorgelesen | `book` | `… › III. Rechtfertigung › Wortlaut Art. 5 II GG` | Karte · fünf Marker | – |
| **N § 5 Nr. 4 VersG** `grundl`–`streng` | Tafel, Möller | `file-certificate`, `armchair`, `search` | `… › Grundlage: § 5 Nr. 4 VersG` | Norm · geschlossene Räume · Verbot … · milderes Mittel · Prognose · Strafbarkeit | – |
| **O Persönliche Ehre** `ehre`–`antrag` | Tafel, Svenja | `shield-check` (Grün), `users-group` (Blau) | `… › Schranke: persönliche Ehre, § 185 StGB` | § 185 · Gruppe · Achtungsanspruch · Menschenwürde · kein Strafantrag | – |
| **P Abwägung** `abw`–`vnicht` | Tafel, Möller | `scale` | `… › Abwägung` | unwahr · nicht schwer · Block Persönlichkeitsschutz · Vermutung · ✗ greift nicht | – |
| **Q Ergebnis** `erg`/`offen` | Tafel, Svenja | fluent-hc:`classical-building`, `gavel` | `Ergebnis · Beschluss vom 13.4.1994` | Block · verworfen · offensichtlich unbegründet · Zulässigkeit offen | – |
| **R Wortlaut § 130 III** `heute`/`wl130` | Wortlautkarte (Zitat), Merkmale markiert zum Wort | `book` | `Rechtslage heute › § 130 III StGB` | Karte · Marker Völkermord, Herrschaft, öffentlich, Versammlung, billigt, leugnet, verharmlost, Eignung | – |
| **S Wunsiedel-Ausnahme** `sonder`–`frieden` | Tafel, Möller | `file-text`, classical-building, `shield-check` | `… › kein allgemeines Gesetz` → `… › Wunsiedel-Ausnahme` → `… › Gefahr für den öffentlichen Frieden` | ✗ kein allgemeines Gesetz · Block Wunsiedel · Abs. 4 · 2018 Abs. 3 · ✗ geistige Wirkung · ✓ Frieden · indiziert | – |
| **T Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Tatsache oder Meinung` | drei Punkte einzeln | – |
| **U Klausurschema** `sch`–`k3c` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` | I · 1. · 2. · 3. · II · III · 1. · Wunsiedel · 2. | – |
| **V Merksatz** `merke`/`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 22 Folien; innerhalb harte Schnitte und Pops; zwei Bewegungen (Stempel senkt sich, Dokument gleitet zum Gericht).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_025stempel_1`, `szene_025brief_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Frühjahr 1991: Ein Parteiverband lädt zu einer Versammlung in einem Saal in München ein. Nach der Einladung und dem angekündigten Redner erwartet die Stadt als Versammlungsbehörde, dass dort die Judenverfolgung im Dritten Reich geleugnet wird. Sie erteilt eine Auflage: Der Verband muss dafür sorgen, dass die Judenverfolgung auf der Versammlung nicht geleugnet oder bezweifelt wird, zu Beginn auf die Strafbarkeit hinweisen, solche Beiträge sofort unterbinden und notfalls die Versammlung unterbrechen oder auflösen (§ 5 Nr. 4 VersG). Die Versammlung findet statt. Die Klage des Verbands bleibt in drei Instanzen ohne Erfolg; er erhebt Verfassungsbeschwerde.
>
> *(Nach BVerfGE 90, 241 – 1 BvR 23/94. Herr Möller und Svenja sind erfunden; Veranstalter und Redner werden nicht genannt.)*
>
> **Verletzt die Auflage die Meinungsfreiheit (Art. 5 I 1 GG)?**

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Jahreszahlen und Normen in Ziffern („1991“, „§ 185 StGB“), gesprochen als Wörter. Kleine graue Fundstellenzeilen sind Belege, kein Sprechtext. Wortlautkarten sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe).
