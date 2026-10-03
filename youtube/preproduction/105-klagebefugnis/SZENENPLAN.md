# Folge 105 · Klagebefugnis § 42 II VwGO: Möglichkeitstheorie und Adressatentheorie – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_105.py`](src/skript_105.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Schema; Voraussetzungsfolge 069 (Anfechtungsklage), Verweise auf 088/090 (Dritte) und 093 (Verpflichtungsklage). Übungsfall nach dem Hook („Du bekommst einen Gebührenbescheid – dein Freund will aus Solidarität mitklagen“): Frau Nolte erhält für die Fällgenehmigung ihrer kranken Kastanie einen Gebührenbescheid über 180 €; ihr Freund Herr Wilke klagt aus Solidarität mit. Länderneutral, kein Landesrecht. Ablauf: Fall → Klagen und Frage → Sachverhalt → Einordnung, 1. Wortlaut § 42 II (Wortlautkarte, UmwRG ein Satz) → 2. eigene Rechte → 3. Möglichkeitstheorie → 4. Adressatentheorie (Wortlautkarte Art. 2 I GG) → 5. Dritte (Schutznormtheorie, Verweis) → 6. Zweck: keine Popularklage, Herr Wilke → Urteil (Richterin) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 4:51,0 (4.116 gesprochene Zeichen), im Regelrahmen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Nolte (NO), um 40 | Adressatin des Gebührenbescheids, Klägerin | Pose `standing/resting-1` (koralles Oberteil `#F07A6A`, schwarze Hose), Kopf `Medium Straight` (schwarzes Haar), Haut `#EBC2A0`; Mimiken `Calm` (ruhig), `Driven` (redet), `Concerned|Serious` (Sorge), `Rage|Serious` (Ärger), `Suspicious` (denkt), `Smile` (froh) | `sabrina` (Frau, mittel) |
| Herr Wilke (WI), um 45 | ihr Freund, klagt aus Solidarität mit | Pose `standing/walking-2` (schwarzes T-Shirt, hellblaue Hose `#8DB3F2`), Kopf `Short 1`, Brille `Glasses 4`, Haut `#C68E62`; Mimiken `Calm`, `Driven` (redet), `Suspicious` (denkt), `Concerned|Serious` (Sorge), `Tired` (geknickt) | `marc` (Mann, mittel) |
| die Richterin (RI), um 55 | Verwaltungsgericht (Funktionsrolle ohne Namen) | Pose `standing/blazer-2` (dunkelgrauer Blazer `#4A4A55`, hellgrünes Oberteil, Beinprothese), Kopf `Medium Bangs 3`, Brille `Glasses 2`, Haut `#D9A07A`; Mimiken `Calm`, `Serious` (redet) | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Frau Nolte blickt nach rechts zu Herrn Wilke, er nach links zu ihr; Szene B: beide blicken nach links zum Gericht; Szene J: die Richterin blickt nach rechts zu Herrn Wilke und Frau Nolte, beide nach links zu ihr; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `NO_redet`, `WI_redet`, `RI_redet` (je links/rechts) und Lexi. Keine Bärte. Prothese bei der Richterin (positive Rolle), nicht bei einer Täterrolle.
- **Stimmen nur aus dem Pool** `william`, `sabrina`, `marc`, `laura_ruhig`; verwendet `sabrina`, `marc`, `laura_ruhig` (Frauenstimmen nie im selben Redewechsel: Frau Nolte spricht nur in Szene A, die Richterin nur in Szene J). `william` nicht gebraucht. Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Nolte, Wilke (nicht in der Liste früherer Namen; `grep -w` über alle Folgenordner ohne Treffer). Die Richterin bleibt namenlos.
- Herr Wilke ist kein Querulant: Er will helfen, hat aber keine eigenen Rechte.
- Figuren-PNGs: `../peeps/op_105/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 101 (Bundestag/Bundesrat, `crossed_arms-1`, `pointing_finger-1`, `robot_dance-2`, `polka_dots`), 102 (Wäscherei, `polka_dots`, `shirt-3`, `easing-2`), 103 (`easing-1`, `pointing_finger-2`). Hier **Garten mit Kastanie und Zaun**; Posen `resting-1`, `walking-2`, `blazer-2` in 101–103 nicht verwendet; keine Polka-Dots. Das Verwaltungsgericht (Säulengebäude) kehrt bewusst zurück, weil die Klagen dort spielen. Kein Richterhammer. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Garten** `fall`–`wi1` | Kastanie, Zaun, Frau Nolte; Fällgenehmigung; Gebührenbescheid 180 €; Herr Wilke kommt; Blasen Nolte/Wilke | ph:`tree` (Grün), tabler:`fence` (Weiß), tabler:`license` (Genehmigung), tabler:`mail-opened` (Bescheid) | `Fall · Der Gebührenbescheid` (ab 0,0 s), `Fall · Der Freund will mitklagen` | Garten · kranke Kastanie · Genehmigung · Bescheid · 180 €/Sorge · Wilke · Blase Nolte/Ärger · Blase Wilke/froh | Papier (`szene_105papier_1`), als der Bescheid erscheint |
| **B Verwaltungsgericht** `klage`–`frage2` | Säulengebäude; zwei Klagen; Frage; beide denken | fluent-hc:`classical-building`, tabler:`file-text` | `Fall · Die Klagen`, `Fall · Sind beide klagebefugt?` | Gericht · Klage Nolte · Klage Wilke · gegen Bescheid · Frage · § 42 II | – |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Einordnung, 1. Wortlaut** `einord`–`umw` | Zulässigkeitsreihe; Wortlautkarte § 42 II mit drei Markern; UmwRG-Ausnahme; Nolte und Wilke | tabler:`scale` | `Klagebefugnis · Platz in der Zulässigkeit`, `… › 1. Wortlaut, § 42 II VwGO`, `… › 1. „soweit gesetzlich nichts anderes …“` | Titel · Reihe · Schema-Pille · Karte · 3 Marker · 3 UmwRG-Zeilen | – |
| **E 2. Eigene Rechte** `eigen`–`objektiv` | Tafel; subjektive Rechte; „nur objektiv rechtswidrig: genügt nicht“ + Kreuz | tabler:`user-check` (Grün) | `Klagebefugnis › 2. Verletzung eigener Rechte` | 6 | – |
| **F 3. Möglichkeitstheorie** `mt`–`mt3` | Frage; Möglichkeit; roter Kasten „ausgeschlossen nur, wenn …“ (6 C 2.23 Rn. 13); Begründetheit; Richterin | fluent-hc:`balance-scale` + Pille „möglich?“ | `Klagebefugnis › 3. Möglichkeitstheorie` | 9 | – |
| **G 4. Adressatentheorie** `adr`–`nolte` | Adressatin; Pflicht 180 €; Eingriff; Wortlautkarte Art. 2 I GG (2 Marker); BVerwG 6 B 20.10 Rn. 16, 9 B 4.19 Rn. 18; „Frau Nolte: klagebefugt“ + Haken; Nolte froh | tabler:`mail-opened` + Pille | `Klagebefugnis › 4. Adressatentheorie, Art. 2 I GG`, `… › 4. Frau Nolte: klagebefugt` | 11 | – |
| **H 5. Dritte** `dritt`–`nachbar` | Schutznorm-Kriterien (6 C 2.23 Rn. 24); Schutznormtheorie; Nachbar/Baugenehmigung; Verweis 088/090; Wilke denkt | tabler:`home` (Blau), tabler:`crane` (Gelb) | `Klagebefugnis › 5. Dritte: Schutznormtheorie` | 8 | – |
| **I 6. Zweck, Herr Wilke** `zweck`–`wilke3` | keine Popularklage; Herr Wilke: nicht Adressat, keine Schutznorm, kein eigenes Recht + Kreuz; Wilke sorgt sich | tabler:`users` + Pille „Allgemeininteresse“ | `Klagebefugnis › 6. Zweck: keine Popularklage`, `… › 6. Herr Wilke` | 10 | – |
| **J Urteil** `urteil`–`ri1` | Gericht; Richterin spricht zu Herrn Wilke; Pille „Herr Wilke: unzulässig“ + Kreuz; Wilke geknickt | fluent-hc:`classical-building` | `Ergebnis · Klage von Herrn Wilke unzulässig` | 4 | – |
| **K Klausurtipp** `tipp`–`vk` | Lexi warnt: ein Satz; Formulierungsbeispiel; „Mehr gehört da nicht hin.“; Verpflichtungsklage, Verweis 093 | Warnsymbol (Streamline Freehand) | `Klausurtipp · Klagebefugnis in einem Satz`, `Klausurtipp · Verpflichtungsklage` | 10 | – |
| **L Schema** `sch`–`s6` | progressiv 1.–6., Gliederungspunkt zur Marke, Inhalt zum Wort | – | `Schema · Klagebefugnis, § 42 II VwGO` | 13 | – |
| **M Merksatz** `merke`–`m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | 5 | – |

## Sachverhaltskarte

„Frau Nolte will die kranke Kastanie in ihrem Garten fällen lassen. Die Stadt erteilt ihr die Fällgenehmigung und setzt mit Gebührenbescheid an Frau Nolte eine Verwaltungsgebühr von 180 € fest. Frau Nolte hält die Gebühr für zu hoch. / Ihr Freund Herr Wilke wohnt in derselben Stadt. Er findet solche Gebühren ungerecht und will aus Solidarität mitklagen. Ein Widerspruchsverfahren ist nach dem Landesrecht nicht vorgesehen. Beide erheben fristgerecht Anfechtungsklage gegen den Gebührenbescheid.“ – Frage: „Sind Frau Nolte und Herr Wilke klagebefugt?“ (kein Fiktiv-Hinweis)
