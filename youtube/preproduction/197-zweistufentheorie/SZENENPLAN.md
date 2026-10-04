# Folge 197 · Zweistufentheorie: Stadthalle, Förderkredit und Kita-Platz – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_197.py`](src/skript_197.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Verwaltungsrecht AT · Streitstand. Beispielfall nach dem Plan-Hook („Die städtische Hallen-GmbH vermietet nur an Vereine, die dem Bürgermeister gefallen.“): Die Stadt betreibt ihre Stadthalle über eine eigene GmbH (alle Anteile bei der Stadt). Frau Lammers, Vorsitzende des Chors Liederkranz, möchte den großen Saal für das Frühjahrskonzert mieten; der Termin ist frei, der Schachclub hat dort im letzten Monat gespielt. Geschäftsführer Scheffler lehnt ab: Der Bürgermeister (fiktiv, ohne Partei, nicht im Bild) möchte den Chor nicht in der Halle. Ablauf: Fall → Frage → Sachverhalt → Problem (Rechtsweg? Anspruchsgegner?; Verweis Folge 192) → Zweistufentheorie (Ob/Wie) → 1. Stufe: § 8 Abs. 2, 4 GO NRW (Wortlaut) → Normtabelle, Art. 28 Abs. 2 S. 1 GG (Wortlaut) → Grenzen (Widmung, Kapazität, Art. 3 Abs. 1 GG) → 2. Stufe: Mietvertrag → Eigengesellschaft: Einwirkungsanspruch gegen die Stadt → Rechtsweg § 40 Abs. 1 S. 1 VwGO → Förderkredit, Kita-Platz → Streitstand/Kritik → Lösung → zurück im Foyer → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:06,2 (5.434 gesprochene Zeichen laut Vertonung); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Lammers (LA), um 60 | Vorsitzende des Chors Liederkranz | Pose `standing/easing-1` (offene Jacke Lila `#B8A9F5`, Shirt Weiß, schwarze Hose), Kopf `Gray Bun` (grauer Dutt), Brille `Glasses 2`, Haut `#F1C9A5`; Mimiken `Calm` (hofft), `Smile` (ruhig), `Concerned\|Serious` (Sorge), `Driven` (entschlossen), `Suspicious` (denkt), `Serious` (liest); sprechend `Calm` / `Smile` mit a/o/e | `hilde` (Frau, älter) |
| Herr Scheffler (SC), um 45 | Geschäftsführer der Stadthallen-GmbH | Pose `standing/blazer-1` (Blazer Grün `#8FD694`, Shirt Schwarz, Hose Dunkelgrau `#4A4A4A`, dunkle Socken der Originalpose), Kopf `Short 3`, Haut `#D9A07A`, kein Bart; Mimiken `Calm`, `Solemn` (verlegen), `Suspicious`, `Smile`, `Serious`; sprechend `Solemn` / `Smile` mit a/o/e | `christian` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Im Foyer blickt Frau Lammers nach rechts zu Herrn Scheffler, er nach links zu ihr; an den Tafeln blicken beide nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `LA_redet`, `LA_froh_redet`, `SC_redet`, `SC_freundlich_redet` (je links/rechts) und Lexi. Keine Bärte, keine Karikatur, keine Icon-Menschen (Kinderwagen-Icon statt Kindergesicht).
- **Stimmen nur aus dem Pool** (`hilde`, `christian`; `stephan` nicht verwendet, also keine Stephan/Christian-Paarung; `lucy` nicht gebraucht). Vorfolge 196 nutzte `niklas`/`helmut`, 192 `hilde`/`lucy`.
- **Namen mit eindeutig deutscher Aussprache, neu:** Lammers, Scheffler, Chor „Liederkranz“ (nicht in der Liste vergebener Namen; Volltextsuche unter `youtube/` ohne Treffer). Gesprochen wird nur „Frau Lammers“ (1 Nennung, Erzählerin); „Scheffler“ steht auf dem Namensschild und im Sachverhalt. Kein Genitiv. Der Bürgermeister bleibt ohne Namen.
- Kein Fiktiv-Hinweis; die Stadt bleibt namenlos.
- Figuren-PNGs: `../peeps/op_197/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 196 (Flughafen/Flugreise), 195 (Gericht/Kostenentscheidung), 194 (Beihilfe), 193 (Weiterfresserschaden), 192 (Kleingartenanlage). Hier neu: **Foyer der Stadthalle** von innen (Saaltür, Belegungsplan an der Wand, Empfangstheke mit Tischglocke); Folge 118 zeigte die Stadthalle von außen mit Tisch und Rathaus – andere Ansicht, eigenes Personal. Posen `easing-1` und `blazer-1` in 192–196 nicht verwendet (Rezepte geprüft: 193 shirt-3/-4, 194 blazer-3/robot_dance-3, 195 blazer-3/crossed_arms-1/pointing_finger-2, 196 blazer-4/crossed_arms-2/robot_dance-2); Farben Lila/Grün, keine Polka Dots. Neues Tafelelement: Dreiecksdiagramm Chor – Stadt – GmbH mit Pfeilen (✗ gegen die GmbH, Einwirkungsanspruch gegen die Stadt). Tageslicht auf Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Foyer** `fall`–`frage2` | Saaltür „Großer Saal“, Belegungsplan, Theke mit Tischglocke; Herr Scheffler ab 0,0 s; Pillen „Betreiberin: Stadthallen-GmbH“, „alle Anteile: die Stadt“; Frau Lammers kommt (Notensymbol), Blase Lammers, „Termin frei“, Blase Scheffler, Schachfigur + „letzter Monat: Schachturnier“, Frage, Antwort | tabler:`calendar-event`, `chess-knight`; fluent-hc:`bellhop-bell` (Gelb), `musical-notes` (Lila) | `Fall · Die Stadthalle der Stadt` (ab 0,0 s) → `Betreiberin: städtische GmbH` → `Der Chor fragt an` → `Frau Lammers möchte den Saal` → `Herr Scheffler lehnt ab` → `Der Schachclub durfte` → `Anspruch auf den Saal – gegen wen?` → `die Zweistufentheorie` | 10 | Tischglocke (`szene_197glocke_1`), als Frau Lammers an die Theke kommt |
| **B Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **C1 Problem** `prob`–`verweis` | Diagramm Stadt → Stadthallen-GmbH, zwei Fragen, Verweis auf Folge 192 | fluent-hc:`classical-building`; tabler:`building-community`, `question-mark`, `scale` | `Problem · …` → `› Rechtsweg? Anspruchsgegner?` → `› Abgrenzung: Folge Abgrenzungstheorien` | 5 | – |
| **C2 Zweistufentheorie** `zst`–`st2b` | Blöcke 1. Stufe Ob / 2. Stufe Wie, Haken | tabler:`list-check`; fluent-hc:`key`, `handshake` | `Zweistufentheorie · zwei Stufen` → … → `› 2. Stufe: privatrechtlicher Mietvertrag` | 5 | – |
| **D1 § 8 GO NRW** `go`, `go4` | Wortlautkarte § 8 Abs. 2, 4 GO NRW (vier Marker), ✓ Chor berechtigt | tabler:`book`; fluent-hc:`musical-notes` | `1. Stufe · Zulassungsanspruch · § 8 Abs. 2 GO NRW (Beispiel NRW)` → `› § 8 Abs. 4: Personenvereinigungen` | 7 | – |
| **D2 Länder, Art. 28** `tab`–`a28b` | Normtabelle (NRW, BY, NI, SN, BB, weitere), Wortlautkarte Art. 28 Abs. 2 S. 1 GG, ✓ Übertragung zulässig, ✓ Einfluss vorbehalten | tabler:`map`, `building-community`; fluent-hc:`classical-building` | `› andere Länder` → `› Selbstverwaltung, Art. 28 Abs. 2 GG` → `› Halle an eine GmbH: Einfluss vorbehalten` | 7 | – |
| **E Grenzen** `vor`–`kein` | Blöcke Widmung, Kapazität, Gleichbehandlung; ✓/✓/✗ | fluent-hc:`musical-notes`; tabler:`list-check`, `calendar-check`, `chess-knight`, `ban` | `1. Stufe › Grenzen des Anspruchs` → … → `› kein sachlicher Grund` | 8 | – |
| **F das Wie** `wie`, `wie2` | Mietvertrag-Block, Händedruck, Block Zivilgericht | fluent-hc:`handshake`; tabler:`writing-sign`, `gavel` | `2. Stufe · das Wie: Mietvertrag` → `› Streit darüber: Zivilgericht` | 3 | – |
| **G1 Eigengesellschaft** `gmbh`–`macht` | Dreieck Chor – Stadt – GmbH; roter Pfeil mit ✗, grüner Pfeil „Einwirkungsanspruch“, Pfeil „wirkt ein“, „100 % der Anteile“ | fluent-hc:`classical-building`, `musical-notes`, `key`; tabler:`building-community`, `book` | `Eigengesellschaft · …` → `› kein Anspruch gegen die GmbH` → `› Einwirkungsanspruch gegen die Stadt` → `› so auch das BVerwG` → `› alle Anteile: Einfluss gesichert` | 6 | – |
| **G2 Rechtsweg** `rweg` | GO = Sonderrecht → Block Verwaltungsrechtsweg § 40 Abs. 1 S. 1 VwGO | tabler:`book`; fluent-hc:`classical-building` | `Rechtsweg · Einwirkungsanspruch: § 40 Abs. 1 S. 1 VwGO` | 3 | – |
| **H Weitere Fälle** `weitere`–`kita` | Förderkredit (Ob/Wie-Blöcke), Kita-Platz (§ 24 SGB VIII, Betreuungsvertrag) | tabler:`list-check`, `coin-euro`, `baby-carriage` | `Weitere Fälle · …` → `› Förderkredit` → `› Kita-Platz: § 24 SGB VIII` | 7 | – |
| **I Streitstand** `krit`–`k4` | Pille „Meinung: Kritik aus der Lehre“, ✗ zwei Kritikpunkte, Block Gegenansicht, ✓ BVerwG, ✓ öffentliche Einrichtungen | tabler:`scale`, `arrows-split`, `writing-sign`; fluent-hc:`classical-building` | `Streitstand · …` → … → `› öffentliche Einrichtungen: Ob und Wie` | 7 | – |
| **J1 Lösung** `loes`–`l4` | Haken je Merkmal, ✗ kein sachlicher Grund, Block Ergebnis | tabler:`building-community`, `ban`; fluent-hc:`musical-notes`, `classical-building` | `Lösung · …` → `› Einwirkungsanspruch gegen die Stadt` | 9 | – |
| **J2 zurück im Foyer** `la2`, `sc2` | Blase Lammers, Blase Scheffler, Vertragsblatt auf der Theke | wie A; fluent-hc:`page-facing-up` | `Lösung · zurück im Foyer` → `Lösung · das Wie: der Mietvertrag` | 2 | – |
| **K Klausurtipp** `tipp`–`kt2` | Lexi warnt; zwei Blöcke | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 3 | – |
| **L Prüfschema** `sch`–`q4` | progressiv I.–IV. mit 1.–4. | – | `Prüfschema` → … → `› IV. das Wie` | 9 | – |
| **M Merksatz** `merke`, `mk2` | Lexi erklärt, drei Marker | – | `Merksatz` | 5 | – |

## Sachverhaltskarte

„Die Stadt (Beispielland Nordrhein-Westfalen) betreibt ihre Stadthalle über eine eigene GmbH; alle Anteile gehören der Stadt. Der große Saal ist für Konzerte und Veranstaltungen der örtlichen Vereine bestimmt. – Frau Lammers, Vorsitzende des Chors Liederkranz (Verein mit Sitz in der Stadt), möchte den Saal für das Frühjahrskonzert mieten. Der Termin ist frei. Im letzten Monat hat der Schachclub dort sein Turnier gespielt. – Geschäftsführer Scheffler lehnt ab: ‚Der Bürgermeister möchte Ihren Chor nicht in der Halle haben.‘“ – Frage: „Hat der Chor einen Anspruch auf den Saal – und gegen wen?“ (kein Fiktiv-Hinweis)
