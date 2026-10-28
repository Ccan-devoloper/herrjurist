# Folge 020 · Grundrechtsprüfung Schema: Schutzbereich, Eingriff, Rechtfertigung – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_020.py`](src/skript_020.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“. Ein frei erfundener, länderneutraler Alltagsfall nach dem Hook des Themenplans trägt das ganze Schema: Die Stadt verbietet per Verordnung das Skateboardfahren in der Fußgängerzone von 8 bis 20 Uhr; die sechzigjährige Gudrun fährt dort jeden Morgen zur Arbeit. Ablauf: Fall → Frage → Sachverhalt → Vorfragen (Bindung Art. 1 III, welches Grundrecht) → Wortlaut Art. 2 I → I. Schutzbereich → II. Eingriff (klassisch, moderner Eingriffsbegriff am Osho-Beschluss) → III. Rechtfertigung: 1. Schranke (verfassungsmäßige Ordnung), 2. Schranken-Schranken (formell; Zitiergebot mit Wortlaut Art. 19 I, nicht einschlägig; materiell: Bestimmtheit, Verhältnismäßigkeit in vier Stufen, Wesensgehalt mit Wortlaut Art. 19 II) → Ergebnis → Gegenfall (Verbot rund um die Uhr) → Klausurtipp (Aufbaukonvention, typische Fehler) → Schema → Merksatz.
**Länge:** Hauptfilm 6:37 (5.485 Zeichen). Mehr als fünf Minuten wegen der drei Wortlautkarten (Art. 2 I, 19 I, 19 II GG, vorgelesen), der vollständigen Schranken-Schranken (formell, Zitiergebot, Bestimmtheit, vier Stufen der Verhältnismäßigkeit, Wesensgehalt) und des zusätzlichen Gegenfalls zur Erforderlichkeit (Vorgabe Kanalinhaber vom 01.10.2026: bis 7 Minuten, wo der Stoff es erfordert).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gudrun (GU), um 60 | Skaterin, Grundrechtsträgerin | Pose `standing/easing-2` (offene Jacke, Turnschuhe), Kopf `Gray Medium` (Haar `#C9C9CF`); Jacke Orange `#F9A66C`, Hose Blau `#8DB3F2`, Haut `#F1C6A5`; Mimiken `Calm` (ruhig), `Smile` (froh), `Rage|Serious` (redet, empört), `Suspicious` (denkt), `Fear` (Schreck), `Concerned|Serious` (Sorge), `Tired` (müde), `Serious` (ernst) – alle mit geschlossenem Mund; Skateboard tabler:`skateboard` | `lisa` (Frau, älter) |
| Frau Krüger (KR), um 75 | Passantin, steht für den Schutzzweck | Pose `standing/crossed_arms-2` (verschränkte Arme), Kopf `Gray Bun`, Brille `Glasses 2`; Hose Lila `#B8A9F5`, Haut `#EBC4A0`; Mimiken `Calm`, `Fear` (Schreck), `Very Angry` (redet), `Smile` | `elinor` (Frau, älter, „ruppige Tante“) |
| Herr Brückner (BR), um 45 | Ordnungsamt, hängt das Verbotsschild auf | Pose `standing/blazer-3`, Kopf `Short 4`; Jackett Blau `#8DB3F2`, Hose `#3D3D58`, Haut `#D9A07A`; Mimiken `Calm`, `Serious` (redet), `Smile` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel bzw. zu Herrn Brückner), `_r` blickt nach rechts (Brückner zu Gudrun, Krüger zum heranrollenden Skater).
- **Alle Grundmimiken mit geschlossenem Mund** (FOLGE-ABLAUF); Mundzustände a/o/e nur in `GU_redet`, `KR_redet`, `BR_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** lisa, elinor, marc (william nicht benötigt); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache:** Gudrun, Krüger, Brückner (Umlaute erzwingen die deutsche Lesart; nicht Hartmann/Lehmann/Sommer aus 016).
- Figuren-PNGs: `../peeps/op_020/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 016: Wohnzimmer 1983, Haustür, Datenfluss; 008 (letzte Grundrechte-Schemafolge): Stadtpark mit Eiswagen, Art. 12 I und Art. 3 I.
- Hier: Fußgängerzone mit Läden, Laterne und Baum, Verbotsschild am Pfosten, rollende Skateboards; erstmals die allgemeine Handlungsfreiheit (nicht das Persönlichkeitsrecht aus 016) und die vollständigen Schranken-Schranken einschließlich Zitiergebot und Wesensgehalt; drei Wortlautkarten.
- Drei neue Figuren, neue Posen gegenüber 016 (`easing-2`, `crossed_arms-2`, `blazer-3`).
- Landesrecht: nur als unterstellte Ermächtigungsgrundlage („Landesgesetz“), kein Land genannt.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht; der Gegenfall zeigt „nachts“ nur mit einem Mond-Icon).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Fußgängerzone** `fall`–`gudrun` | Bodenlinie, zwei Läden, Laterne, Baum, Sonne; Gudrun rollt auf dem Brett von rechts herein | tabler:`building-store` (Rosa, Blau), `lamp` (Gelb), `tree` (Grün), `sun` (Gelb), `skateboard` (Gelb), `briefcase` (Orange) | `Fall · In der Fußgängerzone` | Straße mit Gudrun ab 0,0 s · Gudrun angekommen · „Fußgängerzone“ · „Gudrun, 60“ · „mit dem Skateboard“ · „zur Arbeit“ | Brett rollt an (`szene_020skateboard`) |
| **B Mittags** `mittag`–`k1` | dieselbe Straße, drei Fußgänger, ein Skater rollt knapp vorbei; Frau Krüger erschrickt, zweiter Skater rollt dicht an ihr vorbei, sie schimpft | tabler:`walk` (Grün, Lila, Blau), `skateboarding` (Orange, Blau, gespiegelt) | `Fall · Mittags in der Fußgängerzone` | „Mittags: voll“ · Fußgänger · Skater fährt · „knapp vorbei“ · Krüger · Krüger erschrickt · Skater an ihr vorbei · Blase | zwei Vorbeifahrten (`szene_020vorbei`) |
| **C Das Verbot / Die Frage** `stadt`–`frage` | Rathaus „Stadt“, Verordnung; Pfosten mit Verbotsschild „8–20 Uhr“ und Zusatz „Bußgeld“; Brückner (blickt zu Gudrun), Gudrun mit Brett am Boden | tabler:`building-bank` (Grau), `file-text`, `skateboard-off` (Rot), `skateboard` | `Fall · Das Verbot` → `Fall · Die Frage` | Stadt · Verordnung · Brückner · Schild · Blase Brückner · „Bußgeld“ · Gudrun erschrickt · Blase Gudrun · Frage-Pille · Schutzbereich/Eingriff/Rechtfertigung | – |
| **D Sachverhalt** `sv` | Sachverhaltskarte vollständig, ≈ 9,8 s (5 s Lesepause) | – | `Sachverhalt` | 1 | – |
| **E Vorfragen** `bind`–`auffang` | Tafel links, Gudrun rechts | `building-bank`, `skateboard` | `Vorfrage › Grundrechtsbindung, Art. 1 III GG` → `› Welches Grundrecht passt?` → `› Art. 2 I GG, allgemeine Handlungsfreiheit` | Bindung (✓) · Frage · nicht beruflich (✗) · nicht demonstrieren (✗) · Block Art. 2 I · „greift, wo …“ | – |
| **F Wortlaut Art. 2 I** `wortlaut` | Wortlautkarte, vorgelesen, Marker zum Wort | `book` | `Art. 2 I GG › Wortlaut` | Karte · Marker Jeder/freie Entfaltung/Persönlichkeit/Rechte anderer/verfassungsmäßige Ordnung/Sittengesetz | – |
| **G I. Schutzbereich** `sb`–`skaten` | Tafel, Gudrun | `user`, `walk`, `horse`, `skateboard` | `Art. 2 I GG › I. Schutzbereich` → `› persönlich` → `› sachlich` | jeder · Gudrun (✓) · jede Form · Gewicht · Reiten im Walde · Skaten (✓) · eröffnet | – |
| **H II. Eingriff klassisch** `ein`–`verbot` | Tafel, Gudrun müde, Verbotsschild | `skateboard-off` | `› II. Eingriff` → `› klassischer Eingriff` | vier Merkmale einzeln · Gebot/Verbot · Osho Rn. 68 · alle vier (✓) · „Bußgeld“ | – |
| **I II. Eingriff modern** `modern`–`hier` | Tafel, Bundesregierung/Äußerung als Icons | `building-bank`, `speakerphone` (Gelb), Schild | `› moderner Eingriffsbegriff` → `› hier: klassischer Eingriff (+)` | weiter · Osho · Äußerungen · religiöse Bewegung · Art. 4 · nichts verboten · Block faktisch/mittelbar · moderner Begriff · hier (✓) | – |
| **J III. 1. Schranke** `rf`–`leicht` | Tafel, Herr Brückner | `book`, `file-text` | `› III. Rechtfertigung` → `› 1. Schranke: verfassungsmäßige Ordnung` | Schranke · Vorbehalt · jede Rechtsnorm · Elfes · Block „leicht erreicht“ · „Entscheidend …“ | – |
| **K 2. Schranken-Schranken formell** `ss`–`formell` | Tafel, Brückner | `file-certificate` | `› 2. Schranken-Schranken` → `› formell` | Frage · Zuständigkeit · Verfahren · Form · unterstellt (✓) | – |
| **L Zitiergebot** `zitier`–`nicht` | Wortlautkarte Art. 19 I, Marker zum Wort, Gudrun | `phone` (Blau), `skateboard` | `› formell › Zitiergebot, Art. 19 I 2 GG` → `› Zitiergebot: nicht bei Art. 2 I GG` | Karte · Marker „das Grundrecht unter / Angabe des Artikels nennen“ · Marker „durch Gesetz oder auf Grund eines Gesetzes“ · Fernmeldegeheimnis (✓) · nicht Art. 2 I (✗) | – |
| **M Bestimmtheit** `best`–`klar` | Tafel, Schild am Pfosten, Gudrun liest | Schild | `› materiell › Bestimmtheit` | Maßstab · Ramelow · Skateboard/Fußgängerzone/8–20 Uhr (✓✓✓) · „Das ist klar.“ | – |
| **N Verhältnismäßigkeit** `vhm`–`tag` | Tafel, Frau Krüger | `first-aid-kit` (Rot), `gauge` (Gelb), `clock` | `› Verhältnismäßigkeit` → `› legitimer Zweck` → `› geeignet` → `› erforderlich` | Zweck (✓) · geeignet (✓) · Möglichkeit · erforderlich · Schritttempo (✗) · eindeutig · nur tagsüber (✓) | – |
| **O Angemessenheit** `angem`–`schutz` | Tafel; Gudrun trägt das Brett, Waage, Frau Krüger | `skateboard`, `scale` (Gelb) | `› angemessen` | Maßstab · Gudruns Last · abends/sonst · Waage · Gesundheit vieler · Block angemessen (✓) | – |
| **P Wesensgehalt, Ergebnis** `wesen`–`erg` | Wortlautkarte Art. 19 II, Ergebnisblock, Gudrun besorgt | – | `› materiell › Wesensgehalt, Art. 19 II GG` → `Ergebnis: Art. 2 I GG nicht verletzt` | Karte · Marker Wesensgehalt · unberührt (✓) · Ergebnisblock | – |
| **Q Gegenfall** `gegen`–`gegen3` | Tafel, Schild „0–24 Uhr“, Mond | Schild, `moon` (Gelb) | `Gegenfall · Verbot rund um die Uhr` → `Gegenfall › erforderlich?` | rund um die Uhr · nachts leer (Mond) · nur Fußgänger? · Verbot am Tag (✓) · Block nicht erforderlich (✗) | – |
| **R Klausurtipp** `tipp`–`kurz` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Aufbau` → `Klausurtipp · typische Aufbaufehler` | Konvention · trotzdem einhalten · drei Fehler (✗) · kurz prüfen | – |
| **S Klausurschema** `sch`–`s32w` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` | I · II · III · 1. · 2. · a) · b) · Verhältnismäßigkeit mit vier Stufen einzeln · Wesensgehalt | – |
| **T Merksatz** `merke`–`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb der Folien harte Schnitte und Pops; Bewegungen: Gudrun rollt herein (A), zwei Skater rollen vorbei (B).
**Geräusche:** drei Handlungsgeräusche aus zwei Freesound-CC0-Dateien (`szene_020skateboard_1`, `szene_020vorbei_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Gudrun (60) fährt jeden Morgen mit ihrem Skateboard durch die Fußgängerzone ihrer Stadt zur Arbeit. Mittags ist die Fußgängerzone voll; immer wieder rollen Skater knapp an Fußgängern vorbei, Frau Krüger kann gerade noch ausweichen. Die Stadt erlässt daraufhin eine Verordnung: In der Fußgängerzone ist Skateboardfahren von 8 bis 20 Uhr verboten, Verstöße kosten ein Bußgeld. Herr Brückner vom Ordnungsamt hängt das Schild auf. Gudrun meint: „Skaten ist doch kein Verbrechen! Das ist meine Freiheit!“
>
> Annahmen: Die Verordnung beruht auf einer wirksamen landesrechtlichen Grundlage und ist formell rechtmäßig. Gudrun skatet nicht beruflich und will nicht demonstrieren. (Fall und Personen sind erfunden.)
>
> **Verletzt das Verbot Gudrun in ihren Grundrechten?**
