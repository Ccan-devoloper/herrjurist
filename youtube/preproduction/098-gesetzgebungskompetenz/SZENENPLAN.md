# Folge 098 · Gesetzgebungskompetenz: Bund oder Land? Art. 70 ff. GG – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_098.py`](src/skript_098.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Schema. Beispielfall nach dem Hook des Themenplans („Ein Land verbietet etwas, das der Bund längst geregelt hat – wer darf das Gesetz überhaupt machen?“), Vorbild offengelegt: Berliner Mietendeckel (BVerfG, Beschl. v. 25.3.2021 – 2 BvF 1/20). Der Landtag eines Landes beschließt eine Mietobergrenze von 9 €/m² für frei finanzierte Wohnungen; die Landesministerin stellt sie vor. Vermieter Herr Henke verlangt von Frau Dahlke nach dem BGB die Zustimmung zur Erhöhung auf 10 €/m². Ablauf: Fall → Frage (Bund oder Land?) → Sachverhalt → Einordnung in die formelle Verfassungsmäßigkeit (Verweis Verfahrensarten, Folge 036) → 1. Grundsatz Art. 70 I (Wortlautkarte) → 2. ausschließliche Gesetzgebung Art. 71, 73 → 3. konkurrierende Gesetzgebung: a) Kompetenztitel (Hauptzweck, Art. 74 I Nr. 1), Einwand Wohnungswesen mit Rechtsstand (Föderalismusreform 2006, Art. 125a I, Wortlautauszug), b) Sperrwirkung Art. 72 I (Wortlautkarte), c) Erforderlichkeitsklausel Art. 72 II (Wortlautkarte, BVerfGE 106, 62), d) Abweichungsrecht Art. 72 III → 4. ungeschriebene Kompetenzen (ein Satz) → Ergebnis (nichtig) → Klausurtipp (Art. 31 GG) → Klausurschema → Merksatz.
**Länge:** Hauptfilm 6:27,6 (5.604 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Die Landesministerin (ohne Namen, um 45) | stellt das Landesgesetz vor; Funktionsrolle | Pose `standing/blazer-3` (Blazer Lila `#B8A9F5`, schwarzes Oberteil, Hose `#3A3A48`), Kopf `Long`, Haut `#D9A47E`; Mimiken `Calm`, `Smile` (redet), `Driven` (entschlossen) | `julia` (Frau, jung; ruhig) |
| Frau Dahlke (um 30) | Mieterin | Pose `standing/shirt-4` (schwarze Bluse, Hose Blau `#8DB3F2`), Kopf `Long Curly`, Haut `#E8B894`; Mimiken `Calm`, `Smile`, `Serious` (liest), `Driven` (redet), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Smile` (redet froh) | `ela_froh` (Frau, jung; heitere, nicht ernste Rolle) |
| Herr Henke (um 65) | Vermieter | Pose `standing/resting-2` (schwarzer Pullover, Hand an der Hüfte, Hose Khaki `#C9A06E` – zuerst graublau, wegen der Ähnlichkeit zu Herbert in Folge 097 geändert), Kopf `Gray Short` (Haar grau `#C4C4CC`), Brille `Glasses 2`, Haut `#EBC2A0`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Smile` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Ministerin blickt nach links zum Pult und zum Landtag; Szene B: Frau Dahlke (links) blickt nach rechts zu Herrn Henke, er nach links zu ihr; an den Tafeln blicken alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `LM_redet`, `DA_redet`, `DA_redetfroh`, `HE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (blazer-1/-2 und shirt-1/-2 deshalb verworfen), keine Muster.
- **Stimmen nur aus dem Pool** (`julia`, `ela_froh`, `helmut`; `niklas` nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle. Vorfolge 097: `william`, `marc` – keine Überschneidung.
- **Namen mit eindeutig deutscher Aussprache, neu:** Dahlke, Henke (nicht in der Liste vergebener Namen; `grep -w` über alle Skripte, Szenenpläne und Abnahmebögen ohne Treffer; „Albers“ wegen Folge 006, „Brandl“ wegen der Nähe zu „Brandt“, „Lehnert“ wegen der Nähe zu „Lennart“ verworfen). Die Ministerin bleibt namenlos.
- Kein Fiktiv-Hinweis; keine realen Personen (Berlin nur als Vorbild); keine weiteren Menschen im Bild (Landtag nur als Gebäude).
- Figuren-PNGs: `../peeps/op_098/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 097 (Wohnstraße mit Garage), 096 (Wohnungen, Fahrradladen), 095 (Badezimmer); Wohnungstür hier ohne Innenraum, kein Garten, keine Straße. Hier neu: **Landtag mit Rednerpult** und **Wohnungstür von Frau Dahlke**. Posen `blazer-3`, `shirt-4`, `resting-2` in 095–097 nicht verwendet (dort `easing-1/-2`, `shirt-3`, `resting-1`, `blazer-4`, `crossed_arms-1`, `pointing_finger-2`, `walking-1`). Tageslicht auf Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Landtag** `fall`–`lm1` | Landtagsgebäude, Gesetz, Pult, Ministerin mit Sprechblase | tabler:`building-bank` (Weiß), `file-text`, `podium` | `Fall · Das neue Landesgesetz` (ab 0,0 s) | Gebäude · Gesetz · „beschlossen“ · Ministerin · Blase | – |
| **B Wohnung** `brief`–`vorbild` | Tür, Frau Dahlke öffnet den Brief, Herr Henke; Pillen „bisher 9 €“, „BGB: Zustimmung zur Erhöhung auf 10 €“, „ortsübliche Vergleichsmiete“; Blasen Dahlke – Henke; Blöcke „Bund?“/„Land?“, Pille Vorbild | tabler:`door`; fluent-hc:`envelope` | `Fall · Die Mieterhöhung`, `Fall · Bund oder Land?` | Tür · Brief · Henke · Pillen · Sorge · zwei Blasen · Bund/Land · Vorbild | Brief wird geöffnet (`szene_098brief_1`) |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Einordnung** `einord`–`verw` | formelle Verfassungsmäßigkeit: I. Zuständigkeit, II. Verfahren, III. Form; Weg nach Karlsruhe | fluent-hc:`classical-building` | `Formelle Verfassungsmäßigkeit des Landesgesetzes` → `… › I. Gesetzgebungskompetenz` → `… › Exkurs: Weg nach Karlsruhe` | Zeilen zum Wort | – |
| **E 1. Grundsatz** `wl70`–`voll` | Wortlautkarte Art. 70 I (zwei Marker), Frage, keine Doppelzuständigkeit | fluent-hc:`puzzle-piece` | `I. Gesetzgebungskompetenz › 1. Grundsatz, Art. 70 I GG` | Karte · Marker · Zeilen | – |
| **F 2. ausschließlich** `aus`–`aus3` | Art. 71, 73, Beispiele, Ermächtigung, Kreuz „Miete“ | tabler:`world` | `… › 2. ausschließliche Gesetzgebung, Art. 71, 73 GG` | Zeilen · Block · Kreuz | – |
| **G 3. a) Kompetenztitel** `konk`–`nr1` | Zuordnung nach Hauptzweck, Haken Art. 74 I Nr. 1 | tabler:`home-dollar` + Pille „Mietobergrenze“ | `… › 3. konkurrierende Gesetzgebung, Art. 72, 74 GG` → `› a) Kompetenztitel` → `› a) Kompetenztitel: Art. 74 I Nr. 1 GG` | Zeilen · Block · Haken | – |
| **H Einwand Wohnungswesen** `wohn`–`fort` | Föderalismusreform 2006, Kreuz, Wortlautauszug Art. 125a I (zwei Marker) | tabler:`building-bank` + Pille „das Land“; Ministerin | `… › a) Einwand: Wohnungswesen` → `Rechtsstand · Föderalismusreform 2006, Art. 125a I GG` | Zeilen · Kreuz · Karte · Marker | – |
| **I 3. b) Sperrwirkung** `wl72`–`egal` | Wortlautkarte Art. 72 I (zwei Marker), §§ 556–561 BGB mit Haken, „gesperrt“ | tabler:`lock` + Pille „gesperrt“ | `… › b) Sperrwirkung, Art. 72 I GG` | Karte · Marker · Zeilen · Block | – |
| **J 3. c) Erforderlichkeit** `wl722`–`n1` | Wortlautkarte Art. 72 II (vier Marker), Kriterien, Kreuz Nr. 1 | tabler:`list-check` | `… › c) Erforderlichkeitsklausel, Art. 72 II GG` | Karte · Marker · Zeilen · Kreuz | – |
| **K 3. d) Abweichung, 4. ungeschrieben** `abw`–`unge` | Katalog, lex posterior, Kreuz Mietrecht, ungeschriebene Kompetenzen | tabler:`deer` → `trees` | `… › d) Abweichungsrecht, Art. 72 III GG` → `I. Gesetzgebungskompetenz › 4. ungeschriebene Kompetenzen` | Zeilen · Kreuz · Block | – |
| **L Ergebnis** `erg`–`da2` | nichtig, Vorbild, BGB; Blase Frau Dahlke | – | `Ergebnis · Landesgesetz nichtig` | Kreuz · Block · Zeilen · Haken · Blase | – |
| **M Klausurtipp** `tipp`–`tipp2` | Lexi warnt: nicht vorschnell Art. 31 GG | Warnsymbol (Streamline Freehand) | `Klausurtipp · Erst die Kompetenz, nicht Art. 31 GG` | Zeilen · Block | – |
| **N Klausurschema** `sch`–`s6` | progressiv 1.–5., danach II./III. | – | `Klausurschema · Gesetzgebungskompetenz` | 11 Aufbaustufen | – |
| **O Merksatz** `merke`, `m2` | Lexi erklärt, Marker | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Der Landtag eines Landes beschließt ein Gesetz: Die Miete für frei finanzierte Wohnungen darf höchstens 9 € pro Quadratmeter betragen. Eine Woche später verlangt Herr Henke von seiner Mieterin Frau Dahlke, die bisher 9 € zahlt, nach dem BGB die Zustimmung zu einer Erhöhung auf 10 €, die ortsübliche Vergleichsmiete. – Frau Dahlke: ‚Mehr als 9 € verbietet doch das neue Landesgesetz!‘ Herr Henke: ‚Die Miethöhe hat der Bund längst im BGB geregelt. Da hat das Land nichts zu sagen.‘“ – Frage: „Durfte das Land dieses Gesetz erlassen?“ (kein Fiktiv-Hinweis)
