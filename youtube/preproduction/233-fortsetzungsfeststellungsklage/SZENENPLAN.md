# Folge 233 · Fortsetzungsfeststellungsklage § 113 I 4 VwGO – Prüfungsschema – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_233.py`](src/skript_233.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Verwaltungsprozessrecht, Themenplan-Format „Schema“; Voraussetzung laut Plan: Folge 069 (Anfechtungsklage), dazu 057 (Klagearten) und 028 (Brokdorf, nur verwiesen). Folge 234 behandelt Tenor und Assessor-Perspektive – hier **keine Tenorierung**.
**Fall** (nach dem Hook „Die Polizei hat deine Demo aufgelöst …“, Beispielland Nordrhein-Westfalen): Samstagmittag auf dem Marktplatz. Jördis leitet eine angemeldete (in NRW: angezeigte) Demo für mehr Radwege. Ein einzelner Teilnehmer sprüht Farbe an eine Hauswand und hört trotz Jördis' Bitte nicht auf. Polizeihauptkommissar Hinze löst die ganze Versammlung auf. Alle gehen nach Hause. Jördis plant die nächste Demo am selben Ort; die Polizei würde wieder so handeln. Zwei Wochen später klagt Jördis beim Verwaltungsgericht.
**Ablauf:** Fall → Klage → Frage → Sachverhalt → Erledigung (Wortlautkarte § 43 II VwVfG) → A. Zulässigkeit: I. Rechtsweg, II. statthafte Klageart (Wortlautkarte § 113 I 4 VwGO; direkt/analog, Streit, Verpflichtungssituation), III. Fortsetzungsfeststellungsinteresse (vier Fallgruppen), IV. Klagebefugnis, V. Vorverfahren, VI. Frist (Streit), VII. übrige → B. Begründetheit (Wortlautkarte § 13 II 1 VersG NRW; Bund § 15 III VersG; formell; materiell mit milderem Mittel § 14 III VersG NRW und Brokdorf-Verweis; Rechtsverletzung Art. 8 GG) → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 6:35,1 (5.737 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Jördis (JO), um 28 | Leiterin der Demo, Klägerin | Pose `standing/easing-1` (offene Jacke Türkis `#7FD6D0` über weißem Shirt), Kopf `Long` (Haar `#5A3A28`), Haut `#EBC4A2`, 94 % Höhe; Mimiken `Smile` (froh), `Awe` (Schreck), `Concerned\|Serious` (Sorge, redet), `Serious`, `Suspicious` (denkt), `Tired` (müde), `Driven` (entschlossen) | `lucy` (Frau, jung) |
| Herr Hinze (HI), um 50 | Polizeihauptkommissar der Kreispolizeibehörde | Pose `standing/blazer-4` (Jacke Polizeiblau `#2F3E66`, Hemd Hellblau `#C9DAF5`), Kopf `Short 3`, Haut `#E2B48F`; Mimiken `Serious` (ernst, redet), `Solemn` (streng), `Calm`, `Suspicious` | `stephan` (Mann, mittel) |
| ein Teilnehmer (SP), um 30 | sprüht Farbe (ohne Namen, spricht nicht) | Pose `standing/pointing_finger-1` (erhobene Hand hält die Dose; dunkle Kleidung der Pose), Kopf `Shaved 2`, Haut `#D9A47E`; `Serious`, `Suspicious` | – |
| Radfahrerin (RA), um 35 | Teilnehmerin (ohne Namen, spricht nicht) | `sitting/bike`, Kopf `Bun`, Haut `#C68E6A`; `Smile`, `Concerned\|Serious` | – |
| ältere Teilnehmerin (AL), um 65 | Teilnehmerin (ohne Namen, spricht nicht) | `standing/resting-2` (Hose Lila `#B8A9F5`), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#F0C8A8`; `Smile`, `Concerned\|Serious` | – |
| Lexi | Klausurtipp, Schema, Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Fallszene: der Teilnehmer blickt nach links zur Hauswand; Jördis blickt zunächst nach links zu ihm, ab „Hinze“ nach rechts zu Herrn Hinze, der nach links zu ihr blickt; die Gehenden blicken in Laufrichtung. Tafelszenen: alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `JO_ruft`, `HI_spricht` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots.
- **Posen nicht aus 228–231** (dort u. a. robot_dance-2/-3, polka_dots, crossed_legs, closed_legs-1, blazer-2, blazer-3, easing-2, walking-1/-2, pointing_finger-2, shirt-3/-4); Kontaktbögen der Vorfolgen und Figurenrezepte verglichen.
- **Stimmen nur aus dem Pool** (`lucy`, `stephan`; `hilde`, `christian` nicht gebraucht; stephan und christian nie gemeinsam). Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Jördis, Hinze – eindeutig deutsch (ö), nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per `grep -rliw` in keiner Text-/Codedatei unter `youtube/` (07.10.2026); verworfen: Henrike (in 106/127/146/159 als zu nah an „Henrik“ verworfen), Birte (123, 157), Elske (zu nah an Elke/028), Kirsten (zu nah an Kerstin), Lisbeth (zu nah an Liesel). Eingetragen als „233: Jördis, Hinze“ vor der Vertonung. Kein Genitiv eines Namens im Sprechtext.
- **Darstellung:** Demo neutral (Thema Radwege, Schild „Mehr Radwege“ ohne Parole), Polizei sachlich; der sprühende Teilnehmer unauffällig, keine Täterkarikatur; Farbe nur als rote Schlieren, kein Schriftzug. Alle Menschen Open Peeps, keine Icon-Gesichter.
- Figuren-PNGs: `../peeps/op_233/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 231 Stadtpark bei Nacht, 230 Schwimmbad/Behörde, 229 Werkstatt/Hof, 228 Gericht/Wohnung; 069 (Anfechtungsklage) Gewerbegebiet mit Foodtruck, 028 Wilstermarsch. Hier neu: **Marktplatz mit Hausfassade** (programmatisch), Demo mit Radfahrerin. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Marktplatz** `fall`–`naechst` | Hausfassade (programmatisch), Demo mit Schild, Radfahrerin, ältere Teilnehmerin; Teilnehmer sprüht, Farbe an der Wand; Herr Hinze kommt, Blase; Blase Jördis; alle gehen; nächste Demo | tabler:`sun` (Gelb), tabler:`spray` (Grün), tabler:`ban`, tabler:`calendar-event`, tabler:`repeat`; Schild programmatisch | `Fall · Samstagmittag auf dem Marktplatz` (ab 0,0 s) … `Fall · Die nächste Demo` | Demo · Pille · Sprühen · Farbe · Bitte · Hinze · Blase · Verbot · Blase Jördis · Weggehen · leerer Platz · Kalender · Wiederholung | Sprühstoß (`szene_233spray_1`), Schritte (`szene_233schritte_1`) |
| **A2 Verwaltungsgericht** `klage` | Gebäude, Jördis mit Klage | fluent-hc:`classical-building`, tabler:`file-text` | `Fall · Die Klage` | Gericht · Klage | – |
| **A3 Frage** `frage`–`frage2` | Tafel | tabler:`hourglass`, fluent-hc:`classical-building` | `Die Frage · …` | Frage · Schema · Beispiel NRW | – |
| **B Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **C Erledigung** `va`–`leer` | Tafel, Wortlautkarte § 43 II VwVfG | tabler:`speakerphone`, `hourglass`, `ban` | `Ausgangslage · Erledigung › …` | VA · Karte · Marker · erledigt · ins Leere | – |
| **D1 Rechtsweg, Klageart** `rweg`–`wl113` | Tafel, Wortlautkarte § 113 I 4 VwGO | fluent-hc:`classical-building`, tabler:`file-text` | `A. Zulässigkeit › I. …`, `› II. Statthafte Klageart, § 113 Abs. 1 Satz 4 VwGO` | Titel · Rechtsweg · Karte · 3 Marker | – |
| **D2 direkt/analog** `direkt`–`verpfl` | vier Blöcke | tabler:`file-text`, `hourglass`, `arrows-split`, `certificate` | `… › II. … › direkt / entsprechend / a. A. / Verpflichtung` | 4 Blöcke + Fundstellen | – |
| **E1–E3 Fortsetzungsfeststellungsinteresse** `ffi`–`tief4` | Maßstab, vier Fallgruppen mit (+)/(−) | tabler:`scale`, `repeat`, `calendar-event`, `user-x`, `coin`, `hourglass`, `clock-hour-4`, `users-group` | `A. Zulässigkeit › III. Fortsetzungsfeststellungsinteresse › 1.–4. …` | je Merkmal ein Halt | – |
| **F IV.–VII.** `kb`–`zul` | Klagebefugnis, Vorverfahren, Frist (Streit), übrige, zulässig | tabler:`users-group`, `file-text`, `calendar-time`, `circle-check` | `A. Zulässigkeit › IV. … › VII. …`, `Ergebnis: zulässig` | 7 Stufen | – |
| **G1 Begründetheit** `begr`–`formell` | Obersatz, Wortlautkarte § 13 II 1 VersG NRW, Bundesrecht, formell | fluent-hc:`balance-scale`, tabler:`book`, `speakerphone` | `B. Begründetheit › I. Rechtswidrigkeit › 1./2.` | Obersatz · Karte · 3 Marker · Bund · formell | – |
| **G2 materiell, Ergebnis** `mat`–`erg` | Gefahr, milderes Mittel, Brokdorf-Verweis, rechtswidrig, Art. 8 GG, Ergebnis | tabler:`spray`, `user-minus`, `users-group`, `circle-check`, fluent-hc:`balance-scale` | `B. Begründetheit › I. 3. …`, `› II. Rechtsverletzung`, `Ergebnis · zulässig und begründet` | 6 Stufen | – |
| **H Klausurtipp** `tipp`–`tipp4` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp › …` | 5 Stufen | – |
| **I Klausurschema** `sch`–`s9` | progressiv A. I.–VII., B. I.–II. | – | `Klausurschema › …` | 12 Stufen | – |
| **J Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Samstagmittag auf dem Marktplatz einer Stadt in Nordrhein-Westfalen: Jördis leitet eine ordnungsgemäß angezeigte Demonstration für mehr Radwege mit rund 40 Menschen. Alle sind friedlich, bis ein einzelner Teilnehmer Farbe an eine Hauswand sprüht. Jördis bittet ihn aufzuhören, er macht weiter. / Polizeihauptkommissar Hinze von der Kreispolizeibehörde löst daraufhin die ganze Versammlung auf: „Wegen der Farbe an der Wand: Die Versammlung ist aufgelöst.“ Andere Maßnahmen ergreift er nicht. Alle gehen nach Hause. / Jördis plant weitere Demos am selben Ort; die Polizei erklärt, sie würde wieder so handeln. Weitere Folgen hat die Auflösung nicht. 2 Wochen später erhebt Jördis Klage beim Verwaltungsgericht.“ – Frage: „Hat die Klage Erfolg?“ (kein Fiktiv-Hinweis)
