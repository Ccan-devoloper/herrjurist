# Folge 074 · Ermessensfehler: Was darf das Gericht kontrollieren? (§ 114 VwGO) – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_074.py`](src/skript_074.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“; Voraussetzung laut Plan: Folge 069 (Anfechtungsklage), Rechtsfolge mit Verweis auf Folge 057 (Klagearten). Übungsfall nach dem Hook („Das machen wir grundsätzlich nie.“), Beispielland Nordrhein-Westfalen: Frau Kampmann beantragt für ihr Café in der Altstadt eine Sondernutzungserlaubnis für vier Tische auf dem breiten Gehweg; Herr Hornung von der Stadt lehnt pauschal ab; sie klagt; im Prozess schiebt die Stadt Gründe nach. Ablauf: Fall → Klage und Frage → Sachverhalt → Sondernutzung (§ 18 StrWG NRW, Ermessen) → gebunden oder Ermessen (muss/kann/soll) → Rechtsfolgenseite (Entschließungs-/Auswahlermessen, Beurteilungsspielraum ein Satz) → Wortlautkarte § 40 VwVfG → Wortlautkarte § 114 Satz 1 VwGO (nur Rechtsfehler) → a) Nichtgebrauch, b) Fehlgebrauch, c) Überschreitung → Reduzierung auf null → Fall: Ermessensausfall, § 39 I 3 → Nachschieben (Wortlautkarte § 114 Satz 2) → Verpflichtungsklage, Bescheidungsurteil § 113 V 2 (Richterin) → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 6:23,5 (5.551 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Kampmann (KA), um 35 | betreibt ein kleines Café, Klägerin | Pose `standing/easing-1` (korallrote Jacke `#F07A6A` über weißem Shirt, schwarze Hose), Kopf `Medium Bangs 2` (kastanienbraunes Haar `#8A4B2A`), Haut `#F2C7A8`; Mimiken `Smile` (ruhig), `Driven` (redet), `Cute` (hofft), `Concerned|Serious` (Sorge), `Rage|Serious` (Ärger), `Suspicious` (denkt), `Smile Big|Smile` (froh) | `ela_froh` (Frau, jung) |
| Herr Hornung (HO), um 60 | Sachbearbeiter der Stadt | Pose `standing/blazer-4` (graues Jackett `#7A7A86`, hellblaues Hemd `#8DB3F2`), Kopf `No Hair 2`, Brille `Glasses 3`, Haut `#E8B998`; Mimiken `Serious` (ruhig, redet), `Solemn` (denkt) | `helmut` (Mann, älter) |
| die Richterin (RI), um 45 | Verwaltungsgericht (Funktionsrolle ohne Namen) | Pose `standing/resting-2` (schwarzes Oberteil, dunkelblaue Hose `#3D4A7A`), Kopf `Medium Straight` (Haar `#2E2420`), Brille `Glasses 4`, Haut `#C99272`; Mimiken `Calm` (ruhig), `Serious` (redet) | `julia` (Frau, jung, ruhig) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Frau Kampmann blickt nach rechts zu Herrn Hornung, er nach links zu ihr; Szene B: Frau Kampmann blickt nach links zum Verwaltungsgericht; Szene O: Frau Kampmann blickt nach rechts zur Richterin, die nach links zu ihr blickt; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KA_redet`, `HO_redet`, `RI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** (`ela_froh`, `helmut`, `julia`; `niklas` nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Kampmann, Hornung (nicht in der Liste früherer Namen; `grep` über alle Folgen einschließlich der parallel laufenden 072/073 ohne Treffer; „Hellwig“ wurde verworfen, weil 072 ihn nutzt). Die Richterin bleibt namenlos.
- Herr Hornung ist kein Bösewicht: sachlich, nur pauschal; Frau Kampmann empört, am Ende froh über den Teilerfolg.
- Figuren-PNGs: `../peeps/op_074/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 069 (Gewerbegebiet mit Foodtruck, Fabrikhalle; Verwaltungsgericht mit Waage), 072 und 073 (Strafprozess bzw. Zivilrecht). Hier **Altstadt mit Café und Gehweg** (Tabler `building-store`, vier Phosphor-`picnic-table`, die zunächst halbtransparent als „beantragt“ erscheinen). Das Verwaltungsgericht (Säulengebäude, Waage) kehrt bewusst wieder, weil die Klage dort spielt – andere Besetzung (Kampmann/Richterin statt Ebeling), andere Posen (`easing-1`, `blazer-4`, `resting-2` in 069/072/073 nicht als Fallfigur verwendet). Kein Richterhammer (deutsche Gerichte verwenden keinen). Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Altstadt** `fall`–`ka1` | Café, Sonne, Frau Kampmann; Antrag; vier Tische (halbtransparent, beantragt); Herr Hornung bringt die Antwort; Blasen Hornung/Kampmann; Kreuz auf den Tischen | tabler:`building-store` (Gelb) + Pille „Café“, tabler:`sun`, tabler:`file-text` (Antrag, Bescheid), ph:`picnic-table` ×4 (Weiß, 40 %) + Pille „4 Tische auf dem Gehweg“ | `Fall · Das Café in der Altstadt` (ab 0,0 s), `Fall · Die Antwort der Stadt` | Altstadt · hofft · Antrag · Tische · Pille · Hornung · Bescheid · Blase · Sorge · Kreuz · Blase Kampmann | Papier (`szene_074brief_1`), als der Bescheid erscheint |
| **B Verwaltungsgericht** `klage`–`frage2` | Frau Kampmann mit Klage vor dem Gericht; zwei Fragen | fluent-hc:`classical-building`, tabler:`file-text` + Pille „Klage“ | `Fall · Die Klage`, `Fall · Was darf das Gericht kontrollieren?` | Gericht · Klage · Frage 1 · Frage 2 | – |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Sondernutzung** `norm`–`land` | § 18 StrWG NRW, Ermessen (OVG NRW), Länderhinweis; Frau Kampmann | tabler:`building-store` + Pille „Café“ | `Grundlage · Sondernutzung, § 18 StrWG NRW` | Gemeingebrauch · Sondernutzung · Erlaubnis · Fundstelle · Ermessen · Länderhinweis | – |
| **E gebunden/Ermessen** `geb`–`soll` | muss/ist zu, kann, soll (9 B 79.09); Herr Hornung | tabler:`scale` | `1. Räumt die Norm Ermessen ein? › gebunden oder Ermessen` | muss · zwingend · kann · soll · atypisch · Fundstelle | – |
| **F Rechtsfolgenseite** `rfs`–`bsr` | ob/wie, Beurteilungsspielraum (3 B 11.16); Frau Kampmann | ph:`picnic-table` ×4 + Pillen „ob?“/„wie?“ | `… › Rechtsfolgenseite` | Tische · ob · Entschließung · wie · Auswahl · Tatbestand · voll · Ausnahme | – |
| **G § 40 VwVfG** `wl40`–`nrw40` | Wortlautkarte, zwei Marker; NRW gleichlautend; Herr Hornung | tabler:`building` + Pille „Stadt“ | `… › Bindung, § 40 VwVfG` | Karte · Marker Zweck · Marker Grenzen · NRW | – |
| **H § 114 Satz 1 VwGO** `wl114`–`nicht` | Wortlautkarte (vollständig), zwei Marker; nur Rechtsfehler; Richterin | fluent-hc:`classical-building` | `2. Ermessensfehler › Kontrolle, § 114 Satz 1 VwGO` | Karte · Marker · Marker · Rechtsfehler · zweckmäßiger · kein eigenes Ermessen | – |
| **I a) Nichtgebrauch** `drei`–`f1b` | Ermessensausfall, „grundsätzlich nie“; Herr Hornung | tabler:`eye-off` + Pille „Einzelfall“, Kreuz | `… › a) Ermessensnichtgebrauch` | Titel · Block · Ausfall · übt nicht aus · gebunden · Fundstelle · Zitat · pauschal · Auge · Kreuz | – |
| **J b) Fehlgebrauch** `f2`–`f2c` | sachfremd, Defizit, straßenbezogene Gründe, Konkurrenzschutz; Frau Kampmann | tabler:`building-store` (Blau) + Pille „Wirt nebenan“, Kreuz | `… › b) Ermessensfehlgebrauch` | Block · sachfremd · Defizit · Straße · Verkehr · Stadtbild · Wirt · Konkurrenz · Kreuz · Ärger | – |
| **K c) Überschreitung** `f3`–`f3c` | Erlaubnis für immer, § 18 II StrWG NRW; Grundrechte, Auflage; Herr Hornung | tabler:`infinity` + Pille „für immer?“ + Kreuz; tabler:`walk` + Pille „Durchgang frei“ | `… › c) Ermessensüberschreitung` | Block · Rechtsfolge · für immer · Zeit/Widerruf · Kreuz · Grundrechte · Auflage · Durchgang · unverhältnismäßig | – |
| **L Reduzierung auf null** `null`–`null2` | eine Entscheidung, direkte Verpflichtung (1 B 16.13); Richterin | fluent-hc:`balance-scale` | `3. Ermessensreduzierung auf null` | Titel · eine Entscheidung · verpflichten | – |
| **M Fall: Ermessensausfall** `zurueck`–`begr` | Subsumtion; § 39 I 3; Frau Kampmann | tabler:`file-text` + Pille „„grundsätzlich nie““ | `2. Ermessensfehler › im Fall: Ermessensausfall` | nie · Gehweg · befasst · Ausfall · Begründung · Gesichtspunkte · erkennen | – |
| **N Nachschieben** `prozess`–`heilung` | Wortlautkarte § 114 Satz 2, Marker; nicht heilbar (8 C 25.19, 1 C 14.10); Herr Hornung | tabler:`walk` + Pille „Fußgänger“, Kreuz | `4. Nachschieben, § 114 Satz 2 VwGO` | Fußgänger · Karte · Marker · vervollständigen · nicht heilbar · Kreuz · Anfang · erstmals · Fundstellen | – |
| **O Urteil** `vk`–`neu` | Verwaltungsgericht: Frau Kampmann, Richterin; Pillen Verpflichtungsklage, nicht spruchreif, Bescheidungsurteil, Verweis; Blase; Teilerfolg | fluent-hc:`balance-scale` | `5. Folge › Bescheidungsurteil, § 113 V 2 VwGO`, `Ergebnis · Das Urteil` | Pillen · denkt · Blase · Teilerfolg · froh · abwägen | – |
| **P Klausurtipp** `tipp`–`tipp2` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Ermessen bei der Rechtsfolge` | 3 Stufen | – |
| **Q Klausurschema** `sch`–`s8` | progressiv 1.–5. mit a)–c) | – | `Klausurschema · Ermessensentscheidung` | 9 Aufbaustufen | – |
| **R Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Frau Kampmann betreibt ein kleines Café in der Altstadt einer Stadt in Nordrhein-Westfalen. Sie beantragt bei der Stadt eine Sondernutzungserlaubnis: Von Mai bis September will sie 4 Tische auf den breiten Gehweg vor dem Café stellen. Herr Hornung von der Stadt übergibt den schriftlichen Bescheid. Die Stadt lehnt ab, einzige Begründung: „Das machen wir grundsätzlich nie.“ Frau Kampmann erhebt rechtzeitig Klage beim Verwaltungsgericht und verlangt die Erlaubnis. Im Prozess trägt die Stadt erstmals vor, Fußgänger bräuchten dort Platz.“ – Frage: „Hat die Klage Erfolg?“ (kein Fiktiv-Hinweis)
