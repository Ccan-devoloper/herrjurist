# Folge 019 · Sitzblockade Nötigung: Klimakleber & die Zweite-Reihe-Rechtsprechung – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_019.py`](src/skript_019.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Fiktive Sitzblockade mit Festkleben → Frage → Sachverhalt → I. Tatbestand (Gewalt: Wortlaut § 240 I, BVerfGE 92, 1 und erste Reihe; Zweite-Reihe-Rspr. BGHSt 41, 182, gebilligt durch BVerfG 2011; Festkleben: BVerfGE 104, 92, OLG Karlsruhe 2025, BayObLG 2025 offen; Mittäterschaft, Erfolg, Vorsatz) → II. Rechtswidrigkeit (§ 34, Art. 8 GG, Wortlaut § 240 II, Kriterien BVerfGE 104, 92) → Abwägung im Fall, Schuld, Ergebnis → Gegenfall → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hanna (HA), Mitte 20 | klebt ihre Hand fest | `sitting/hands_back-1`, Kopf `Long`, Hose Lila `#B8A9F5`, Haut `#E8B98F`; Mimiken `Calm`, `Driven` (redet), `Serious`, `Smile` | `lucy` (Frau, jung) |
| Lukas (LU), Anfang 20 | sitzt nur daneben (Mittäter) | `sitting/one_leg_up-2`, Kopf `Short 2`, Oberteil Grün `#8FD694`, Haut `#C99470`; `Calm`, `Serious`, `Suspicious` | spricht nicht |
| zwei weitere Sitzende | ohne Rolle und Namen | `sitting/mid-1` (Kopf `Afro`, Hose Orange), `sitting/closed_legs-1` (Kopf `Bangs`, Brille, Jacke Türkis); `Calm` | – |
| Dieter (DI), um 45 | erster Fahrer | `standing/shirt-3`, Kopf `Short 3`, Brille `Glasses 3`, Hemd Rot `#F07A6A`, Haut `#E6B48F`; `Calm`, `Fear`, `Concerned|Serious` (redet), `Serious`, `Tired` | `stephan` (Mann, mittel) |
| Sabine (SA), um 40 | Fahrerin in der zweiten Reihe | `standing/crossed_arms-2`, Kopf `Medium Bangs`, Hose Blau `#8DB3F2`, Haut `#8D5A3B`; `Calm`, `Suspicious` (redet), `Very Angry`, `Tired`, `Serious` | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HA_redet`, `DI_redet`, `SA_redet` (je links/rechts) und Lexi. `Concerned` nur als `Concerned|Serious`.
- Grundansicht blickt nach links (Tafelszenen), `_r` nach rechts (Sitzende blicken in der Fallszene zum ankommenden Verkehr). Am Kontaktbild geprüft.
- Keine Bärte, keine Prothesen-Posen, keine Karikaturen. Die Gruppe ist erfunden; keine reale Gruppe, keine Transparente, keine Slogans außer Hannas einem Satz.
- **Namen mit eindeutig deutscher Aussprache:** Hanna, Lukas, Dieter, Sabine. Stimmen nur aus dem Pool (lucy, stephan, laura_ruhig; `timo` nicht gebraucht, weil Lukas nicht spricht).
- Figuren-PNGs: `../peeps/op_019/` (68 Dateien, im Drive-Master).

**Abweichung von den letzten Folgen:** 018 Arbeitszimmer/Café/Sitzungssaal, 017 Wohnung/Briefkasten, 016 Amtsstube. Hier erstmals eine Straßenszene bei Tag mit Sitzblockade und Stau (001 war ein nächtliches Autorennen; die Autos sind dieselben Tabler-Icons, aber Tageslicht, Stau statt Rennen). Neue Figuren und Posen (sitzende Open-Peeps-Posen).

**Politische Neutralität:** Das Anliegen der Gruppe wird nur benannt („Für mehr Klimaschutz!“), nicht bewertet; im Video ausdrücklich: „Das politische Anliegen selbst darf das Gericht nicht bewerten.“

## Szenen (alle auf Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Blockade / erste Reihe** `fall`→`d1` | Ringstraße von der Seite; Berufsverkehr fährt durch; vier Personen setzen sich; Hanna klebt; Dieter hält | tabler:`sun`, `car` (Grau/Gelb/Rot), `droplet` (Kleber, Gelb) | `Fall · Die Blockade` (ab 0,0 s) → `Fall · Die erste Reihe` | Verkehr · Berufsverkehr · Ringstraße · Sitzende · Plan · Spuren · Kleber · Lukas sitzt nur · Hanna redet · Auto fährt ein · „als Erster“ · Dieter steigt aus · Dieter redet | Bremsen (`szene_019bremse_1`) |
| **B Die zweite Reihe / Frage** `sabine`→`frage` | Stau: Auto Dieter, Auto Sabine, Sabine stehend, zwei Autos dahinter; Mittelinsel links, Gehweg rechts | tabler:`car` ×4, `trees`, `calendar-off`, `clock`; fluent-hc:`police-car` | `Fall · Die zweite Reihe` → `Fall · Die Frage` | Sabine kommt · Stau · Mittelinsel · Gehweg · Sabine redet · nicht angekündigt · 50 Minuten · Polizei · Frage | Autotür (`szene_019tuer_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D Gewalt: erste Reihe** `pruef`→`dieter2` | Tafel links mit **Wortlautkarte § 240 I** (Marker „mit Gewalt“), Dieter rechts | tabler:`car` | `Nötigung, § 240 StGB › I. Tatbestand` → `§ 240 StGB › I. 1. Gewalt` → `… › BVerfGE 92, 1 (Art. 103 II GG)` → `… › erste Reihe: Dieter` | Wortlaut · Marker · Definition · früher · 1995 · Anwesenheit · keine Gewalt · Art. 103 · Kreuz Dieter | – |
| **E Zweite Reihe** `zweite`→`bv11` | Tafel, rechts Mini-Kette Blockade → rotes Auto → blaues Auto, Sabine | tabler:`car` ×2 | `… › zweite Reihe: Sabine (BGHSt 41, 182)` → `… › BVerfG 2011: mittelbare Täterschaft` | BGH · Hindernis · Werkzeug · BVerfG 2011 · mittelbare Täterschaft | – |
| **F Festkleben** `kleber`→`offen` | Tafel, Hanna rechts mit Kleber an der Hand | tabler:`droplet`, `link` | `… › Festkleben` → `… › Festkleben: offen` | 2001 · Anketten · OLG 2025 · Festkleben = Gewalt · Folge · BayObLG · offen · ungeklärt | – |
| **G Lukas, Erfolg, Vorsatz** `lukas2`→`vorsatz` | Tafel, Lukas und Sabine | tabler:`clock` | `… › Mittäterschaft, § 25 II StGB` → `… › I. 2. Nötigungserfolg` → `… › I. 3. Vorsatz` | 4 Halte | – |
| **H Rechtswidrigkeit** `rw`→`inhalt` | Tafel mit § 34, Art. 8, dann **Wortlautkarte § 240 II** (Marker „verwerflich“), dann Kriterienliste; Hanna und Lukas | – | `… › II. Rechtswidrigkeit` → `… › Art. 8 GG` → `… › Verwerflichkeit, § 240 II StGB` → `… › Abwägung (BVerfGE 104, 92)` | ≈ 12 Halte | – |
| **I Abwägung im Fall, Ergebnis** `subs`→`erg` | Tafel, Sabine | tabler:`clock`, `calendar-off`, `ban`, `car` | `… › Abwägung im Fall` → `… › III. Schuld · Ergebnis` | 7 Halte | – |
| **J Gegenfall** `gegen`→`gegen2` | kurze Blockade, ein Auto, Umleitung | tabler:`calendar`, `route`, `scale` | `Gegenfall · kurze, angekündigte Blockade` | 6 Halte | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Gewalt je Reihe prüfen` | 6 Halte | – |
| **L Klausurschema** `sch`→`k3` | breite Karte, progressiv | – | `Klausurschema` | 9 Halte | – |
| **M Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | 6 Halte | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei fahrenden Autos.
**Geräusche:** zwei Handlungsgeräusche (Freesound CC0), Herkunft in `geraeusche_herkunft.json`.
**Wortlautkarten** (Vorgabe Kanalinhaber vom 01.10.2026, nach Vertonung umgesetzt, nur Bild): § 240 I StGB (bis „nötigt, …“) und § 240 II StGB vollständig, wörtlich nach gesetze-im-internet.de, mit Normangabe; Marker synchron zu „Gewalt“ bzw. „Verwerflichkeit“.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Montag, 8 Uhr, Berufsverkehr auf der Ringstraße: Hanna, Lukas und zwei weitere Personen setzen sich nach gemeinsamem Plan quer über alle Fahrspuren auf die Fahrbahn, um den Verkehr anzuhalten. Hanna klebt ihre Hand mit Sekundenkleber auf dem Asphalt fest, Lukas sitzt nur daneben. Angekündigt ist die Aktion nicht.
>
> Dieter hält als Erster, um niemanden zu überfahren. Hinter ihm hält Sabine, dahinter staut es sich über einen Kilometer. Links liegt eine Mittelinsel, rechts der Gehweg; ausweichen kann niemand. Nach 50 Minuten hat die Polizei Hannas Hand gelöst und die Straße geräumt.
>
> *(Fiktiver Fall, alle Personen erfunden.)*
>
> **Haben sich die vier wegen Nötigung (§ 240 StGB) strafbar gemacht?**
