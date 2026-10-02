# Folge 084 · Nötigung § 240 Schema: Gewalt, Drohung & Verwerflichkeit – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_084.py`](src/skript_084.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Format „Schema“. Fall nach dem Plan-Hook (Kaution gegen Rücknahme der Bauamtsbeschwerde) → Frage → Sachverhalt → Wortlautkarte § 240 Abs. 1 → I. Tatbestand: Gewalt (kurz, Verweis auf Folge 019), Drohung, Drohung mit einem Unterlassen, empfindliches Übel, Nötigungserfolg, Kausalität, Vorsatz → II. Rechtswidrigkeit in zwei Stufen mit Wortlautkarte § 240 Abs. 2 → Mittel-Zweck-Relation und fehlender Zusammenhang (Inkonnexität) → Gegenfall (Klage auf offene Miete) → III. Schuld, IV. § 240 Abs. 4 (ein Satz), Ergebnis → Abgrenzung § 253 (ein Satz) → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi). Vorlagen: 019 (Nötigung, Gewaltbegriff – hier nur verwiesen; Drohung und Verwerflichkeit vertieft), 075 (StGB BT, Stil C), 051 (Delikt als Schema).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gesine (GS), um 35 | Mieterin, ausgezogen | `standing/resting-2`, Kopf `Long Bangs` (schwarzes Haar), schwarzes Oberteil, Hose Grün `#8FD694`, schwarze Schuhe, Haut `#F0C8A8`. Mimiken `Calm`, `Serious`, `Concerned|Serious` (Sorge; redet), `Tired`, `Smile` (nicht verwendet) | `julia` (Frau, jung) |
| Gernot (GE), um 60 | Vermieter, sachlich | `standing/blazer-3` (Sakko Blau `#8DB3F2`, dunkelgraue Hose), Kopf `Gray Short`, Haut `#E3B48C`. Mimiken `Calm`, `Serious` (redet), `Solemn`, `Suspicious` (skeptisch, nicht böse) | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Fallszenen: Gesine zu Gernot).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `GS_redet`, `GE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`blazer-2` und `shirt-1/2` deshalb nicht gewählt), keine Karikatur: Gernot im Sakko mit ruhiger, ernster Mimik. 42 Figuren-PNGs in `../peeps/op_084/` (Drive-Master).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan oder Abnahmebogen unter `youtube/` (Volltextsuche 02.10.2026): Gesine, Gernot.
- **Stimmen** nur aus dem zugeteilten Pool (helmut, julia; niklas und ela_froh nicht gebraucht). Vorfolge 083 (hilde, christian, lucy): keine Überschneidung.

**Abweichung von den letzten Folgen (Kontaktbögen 081–083 verglichen, `out/vergleich_081_082_083_084.png`):** 081 Straße/Auto, Tabea im Polka-Dots-Kleid; 082 Imbissbude; 083 Fahrradverleih und Haus. Hier neu: Auszug aus der Mietwohnung (Haus mit Umzugskartons und Baustellenschild), Bauamt (klassisches Amtsgebäude), Briefkasten mit Rücknahmebrief, Überweisung der Kaution als wandernder Geldschein. Posen `resting-2` und `blazer-3` in 081–083 nicht verwendet; kein Polka-Dots-Muster.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Fall** `fall`→`s1` | Haus „Mietwohnung“ mit Umzugskartons, Gesine; Gernot (Vermieter) kommt dazu; Pillen „Gernot schuldet ihr die Kaution: 1.500 €“, „Forderungen gegen Gesine: keine“; Geldschein zwischen beiden; „vor dem Auszug: Beschwerde beim Bauamt“, Baustellenschild am Haus „lockeres Balkongeländer“, Bauamt mit Brief; Gernot spricht (Blase), Gesine antwortet (Blase) | fluent:`house`, `package`, `euro-banknote`, `construction`, `classical-building`, `envelope` | `Fall · Der Auszug` (ab 0,0 s) → `Fall · Die Kaution` → `Fall · Die Beschwerde beim Bauamt` → `Fall · Gernots Bedingung` | ≈ 11 | – |
| **A2 Rücknahme** `zurueck`→`frage` | Gesine am Briefkasten „an das Bauamt“; Brief gleitet in den Kasten, Pille „Rücknahme der Beschwerde“; Gernot überweist: Geldschein wandert zu Gesine, Pfeil „überweist 1.500 €“; Frage | fluent:`postbox`, `envelope-with-arrow`, `euro-banknote` | `Fall · Gesine zieht die Beschwerde zurück` → `Fall · Gernot überweist die Kaution` → `Fall · Die Frage` | ≈ 6 | Brief in den Briefkasten (`szene_084brief_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,4 s | – | `Sachverhalt` | 1 | – |
| **C § 240 Abs. 1** `pruef`→`erfolg0` | Wortlautkarte (Marker gelb Nötigungsmittel, blau Nötigungserfolg), zwei Blöcke | fluent:`balance-scale`, `envelope-with-arrow`; tabler:`alert-triangle` | `A. Nötigung, § 240 StGB` → `… › I. Tatbestand › Nötigungsmittel` → `… › Nötigungserfolg` | ≈ 7 | – |
| **D Gewalt** `gewalt`→`g_nein` | Definition, Verweis auf Folge 019, Gewalt (−) | tabler:`hand-stop`, `hand-off`; fluent:`automobile` | `… › 1. Nötigungsmittel: Gewalt` → `… › 1. Gewalt (−)` | ≈ 6 | – |
| **E Drohung** `drohung`→`einfluss` | Definition, Übel, 1.500 € bleiben aus, Gernot entscheidet | tabler:`hourglass`; fluent:`euro-banknote`, `key` | `… › 1. Nötigungsmittel: Drohung` → `… › 1. Drohung: Einfluss des Täters` | ≈ 10 | – |
| **F Unterlassen** `unterl`→`pflicht` | nicht zahlen, Unterlassen genügt, Pflicht zur Rückzahlung | tabler:`cash-off`, `scale` | `… › 1. Drohung mit einem Unterlassen` → `… › 1. Unterlassen: Pflicht zur Rückzahlung` | ≈ 6 | – |
| **G empfindlich** `empf`→`e_ja` | Definition, besonnene Selbstbehauptung, empfindlich (+) | tabler:`scale`, `shield`; fluent:`euro-banknote` | `… › 1. Drohung: empfindliches Übel?` → `… › 1. empfindliches Übel (+)` | ≈ 10 | – |
| **H Erfolg, Kausalität, Vorsatz** `erfolg`→`tb_ja` | Rücknahme, wegen der Drohung, Vorsatz, Tatbestand (+) | fluent:`envelope-with-arrow`; tabler:`link`, `brain` | `… › 2. Nötigungserfolg` → `… › 3. Kausalität` → `… › subjektiv: Vorsatz` → `… › I. Tatbestand (+)` | ≈ 6 | – |
| **I Rechtswidrigkeit** `rw`→`sozial` | zwei Stufen, Rechtfertigungsgründe, Wortlautkarte § 240 Abs. 2 (Marker „Androhung des Übels“, „angestrebten Zweck“, „verwerflich“), „sozial unerträglich“ | tabler:`shield`, `alert-triangle`; fluent:`balance-scale` | `… › II. Rechtswidrigkeit` → `… › 1. Rechtfertigungsgründe` → `… › 2. Verwerflichkeit, § 240 Abs. 2` → `… › sozial unerträglich` | ≈ 11 | – |
| **J Mittel-Zweck** `mz`→`v_ja` | Kästen Mittel/Zweck, kein Zusammenhang (zerrissene Kette), Lehre: Inkonnexität, verwerflich (+) | tabler:`cash-off`; fluent:`classical-building`, `broken-chain` | `… › 2. Mittel-Zweck-Relation` → … → `… › 2. verwerflich (+)` | ≈ 14 | – |
| **K Gegenfall** `gegen`→`gegen2` | offene Miete, Klage, Zusammenhang, nicht verwerflich (blaue Tafel) | fluent:`receipt`, `link`; tabler:`gavel` | `Gegenfall · Klage auf die offene Miete` → `… · Mittel und Zweck hängen zusammen` → `… · nicht verwerflich` | ≈ 9 | – |
| **L Schuld, Abs. 4, Ergebnis** `schuld`→`erg` | Gernot allein neben der Tafel | tabler:`gavel` | `A. § 240 StGB › III. Schuld` → `… › IV. besonders schwerer Fall` → `Ergebnis · Gernot: Nötigung, § 240 StGB` | ≈ 7 | – |
| **M Abgrenzung § 253** `erpr`→`erpr3` | kein Vermögensnachteil, keine Bereicherungsabsicht | fluent:`envelope`, `euro-banknote` | `Abgrenzung · Erpressung, § 253 StGB?` → `… (−)` | ≈ 7 | – |
| **N Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | ≈ 8 | – |
| **O Klausurschema** `sch`→`k5` | breite Karte, progressiv | – | `Klausurschema › …` | 11 | – |
| **P Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 9 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim Brief und beim überwiesenen Geldschein. Folie A2 beginnt erst bei „will“, damit Gesines Satzende nicht in die Schiebeblende fällt.
**Geräusche:** ein Handlungsgeräusch (Brief in den Briefkasten, Freesound CC0), Herkunft in `geraeusche_herkunft.json`. Keine Geräusche bei Überweisung (kein hörbarer Vorgang) und bei Tafeln.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 240 Abs. 1 vollständig (Merkmale gesprochen, Marker zum Wort) und § 240 Abs. 2 vollständig (wörtlich gesprochen), wörtlich nach gesetze-im-internet.de mit Normangabe.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Gesine ist aus ihrer Mietwohnung ausgezogen. Ihr Vermieter Gernot schuldet ihr noch die Kaution von 1.500 €; Forderungen gegen sie hat er keine. Kurz vor dem Auszug hatte Gesine sich beim Bauamt über das lockere Balkongeländer beschwert.
>
> Gernot sagt: „Ihre Kaution bekommen Sie erst, wenn Sie die Beschwerde beim Bauamt zurückziehen.“ Gesine will ihr Geld. Sie zieht die Beschwerde zurück, und Gernot überweist die Kaution.
>
> **Hat Gernot sich strafbar gemacht?**
