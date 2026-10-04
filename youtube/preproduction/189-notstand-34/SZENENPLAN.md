# Folge 189 · Rechtfertigender Notstand § 34 StGB: Schema mit Berghütten-Fall – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_189.py`](src/skript_189.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · StGB AT, Format **Schema** mit Fall. Plan-Hook: Ein Wanderer bricht bei einem Wettersturz die Tür einer verschlossenen Berghütte auf, um nicht zu erfrieren. Samstag, 17:40 Uhr, 2.150 m, −12 °C, kein Netz, Tal 3 Stunden; Hütte von Frau Moser, Schild „Betreten verboten“; Schloss kaputt; am Morgen: neues Schloss 380 €.
Ablauf: Fall (Bergweg → Hütte → Nacht → Morgen) → Sachverhalt → Tatbestand §§ 303, 123 kurz → Wortlautkarte § 34 S. 1, 2 → 1. Notstandslage (Gefahr, gegenwärtig; BGH 1 StR 483/02 Rn. 27) → 2. Notstandshandlung (nicht anders abwendbar: geeignet, erforderlich) → 3. Interessenabwägung → 4. Angemessenheit S. 2 → 5. subjektives Rechtfertigungselement → § 904 BGB (Wortlautkarte; Aggressivnotstand; Ersatz, Blase Frau Moser) → § 228 BGB (Wortlautkarte; Defensivnotstand) → Vorrang (h. M.) → Abgrenzung § 32 (Verweis 033) und § 35 (Haustyrann) → Lösung → Blase Korbinian → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Abgrenzung zu den Referenzfolgen:** 033 (Notwehr) wird nicht wiederholt, nur in einem Satz verwiesen; 062 (Einwilligung) nicht berührt (mutmaßliche Einwilligung bewusst ausgespart, Schild als erklärter Gegenwille); 061 (polizeilicher Notstand) ist Polizeirecht und nicht Thema.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Korbinian (KO), Mitte 30 | Wanderer, bricht die Tür auf | `standing/blazer-4` als Anorak (Jacke Rot `#F07A6A`, Oberteil Gelb `#F9D56E`, schwarze Hose der Pose), Kopf `hat-beanie` (Wollmütze), Haut `#F0C8A8`, kein Bart, keine Brille; Mimiken `Calm`, `Serious`, `Concerned\|Serious`, `Fear`, `Tired`, `Driven`, `Smile`, `Suspicious`; redet: `Concerned\|Serious`, redet2: `Smile` | `marc` (Mann, mittel) |
| Frau Moser (MO), um 55 | Eigentümerin der Hütte | `standing/crossed_arms-2` (verschränkte Arme, schwarzes Oberteil, Hose Grün `#8FD694`), Kopf `Gray Bun`, Haut `#E9BC98`; `Calm`, `Serious`, `Suspicious`, `Concerned\|Serious`, `Smile`, `Very Angry`; redet: `Serious`, redet2: `Smile` | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Text-/Code-Datei unter `youtube/` (Volltextsuche 04.10.2026): Korbinian, Moser.
- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig); `william` und `sabrina` nicht gebraucht. Vorfolge 188 (christian, lucy), 187 (helmut, niklas), 186 (hilde, stephan, lucy): keine Überschneidung.
- **Posen** nicht aus 186–188 (easing-1/-2, doctor-nurse-01, resting-1, blazer-3, pointing_finger-1/-2, crossed_arms-1); keine Polka Dots, keine Prothesen-Posen, keine Bärte, keine Karikatur. Alle Grundmimiken mit geschlossenem Mund; Mundzustände a/o/e für `KO_redet`, `KO_redet2`, `MO_redet`, `MO_redet2` (je links/rechts) und Lexi. 70 Figuren-PNGs in `../peeps/op_189/`.
- **Blickrichtung:** Grundansicht blickt nach links, `_r` nach rechts. A2: Korbinian blickt nach links zur Hütte; A4/N2: Frau Moser (`_r`) und Korbinian einander zugewandt; in Tafelszenen blicken alle nach links zur Tafel.

**Setting (neu):** Bergkulisse mit Schneekappen, Schneeboden, Berghütte mit Satteldach, Schild auf Pfosten, Innenraum mit Fenster und Bank, Morgen mit Sonne. Gegenüber 186 (Praxis/Behörde), 187 (Baustelle/Stromkabel), 188 (Bauamt) neu. Cremegrund durchgehend (Tageslicht-Standard; Dämmerung/Nacht nur über Mond-Icon im Hüttenfenster).
**Darstellung:** Wetter als ruhige Icons (Schneeflocken, Wind), keine Verletzungen; Aufbrechen nur als Icon (Werkzeug, offene Tür, kaputtes Schloss), keine Anleitung; keine Logos.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Bergweg** `fall`→`tal` | Berge, Schnee; Korbinian erscheint bei „Korbinian“; Schneesturm, kein Netz, 3 Stunden | tabler:`snowflake`, `wind`, `device-mobile-off`; Pillen „Samstag, 17:40 Uhr“, „2.150 m“, „Schneesturm · −12 °C“, „bis ins Tal: 3 Stunden“ | `Fall · Bergtour auf 2.150 m` (ab 0,0 s) → `· Wettersturz` → `· kein Netz, Tal 3 Stunden` | – |
| **A2 Berghütte** `huette`→`kaputt` | Hütte (Tür zu, Schloss), Schild „Betreten verboten“, Blase Korbinian, Tür offen, Werkzeug, kaputtes Schloss | tabler:`lock`, `tool`, `lock-open-off`, `snowflake` | `Fall · die Berghütte von Frau Moser` → `· im Winter verschlossen` → `· Gefahr zu erfrieren` → `· Tür aufgebrochen` | Tür knarrt auf (`szene_189tuer_1`, bei `auf`) |
| **A3 Nacht** `nacht` | Innenraum, Mond im Fenster, Korbinian erleichtert | tabler:`moon-stars`, `snowflake` | `Fall · die Nacht in der Hütte` | – |
| **A4 Morgen** `morgen`→`frage3` | Hütte mit offener Tür, Sonne, Frau Moser (verärgert), Beleg, Blase Moser, drei Fragepillen | tabler:`sun`, `receipt` | `Fall · am nächsten Morgen` → `· Wer bezahlt das Schloss?` → `· die Fragen` | – |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,8 s), kein Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Tatbestand** `tb`→`rw` | Haken § 303, § 123, Vorsatz; Block II. Rechtswidrigkeit | tabler:`gavel`, `lock-open-off`, `door-enter`, `scale` | `A. Korbinian, §§ 303, 123 StGB › I. Tatbestand …` → `› II. Rechtswidrigkeit` | – |
| **D Wortlaut § 34** `p34`→`s2` | Wortlautkarte S. 1, 2 vollständig, Marker zur Merkmalsnennung | tabler:`alert-triangle`, `scale`, `circle-check` | `A. Korbinian › II. Rechtswidrigkeit › § 34 StGB · …` | – |
| **E 1. Notstandslage** `lage`→`lage_ok` | a) Gefahr, b) gegenwärtig (BGH Rn. 27) | tabler:`alert-triangle`, `heartbeat`, `clock`, `snowflake` | `… › 1. Notstandslage › a) / b)` | – |
| **F 2. Notstandshandlung** `handl`→`nur` | a) geeignet, b) erforderlich, drei Kreuze (Notruf, Abstieg, Unterkunft), Haken „nur die Tür“ | tabler:`route`, `home`, `device-mobile-off`, `door` | `… › 2. Notstandshandlung › …` | – |
| **G 3. Interessenabwägung** `abwaeg`→`ueber` | Blöcke geschützt/beeinträchtigt, Haken; Frau Moser und Korbinian | tabler:`scale`, `heartbeat`, `lock-open-off`, `heart` | `… › 3. Interessenabwägung › …` | – |
| **H 4. Angemessenheit** `angem`→`angem_ok` | Ausnahme (verbreitete Ansicht), Haken | tabler:`circle-check`, `user-x` | `… › 4. Angemessenheit, S. 2 › …` | – |
| **I 5. subjektives Element** `subj`→`erg34` | drei Haken, Block „§ 34 StGB: Voraussetzungen (+)“ | tabler:`brain`, `snowflake-off`, `shield-check` | `… › 5. subjektives Rechtfertigungselement › …` → `… › Voraussetzungen (+)` | – |
| **J § 904 BGB** `bgb`→`mo2` | Wortlautkarte S. 1, 2; danach Aggressivnotstand, Verbot unbeachtlich, S. 2 wörtlich; Blase Frau Moser | tabler:`book`, `cloud-snow`, `door`, `ban`, `receipt` | `Zivilrechtlicher Notstand › § 904 BGB …` | – |
| **K § 228 BGB** `p228`→`tuer` | Wortlautkarte, Gefahr von der Sache (Hund), Kreuz „Tür bedroht nicht“ | tabler:`hammer`, `dog`, `door` | `Zivilrechtlicher Notstand › § 228 BGB …` | – |
| **L Vorrang** `spez` | h. M.: §§ 228, 904 BGB vor § 34 bei Eingriffen in Sachen | tabler:`book`, `arrow-right`, `scale` | `Verhältnis: §§ 228, 904 BGB vor § 34 StGB (h. M.)` | – |
| **M Abgrenzung** `p32`→`ht` | § 32 (Kreuz), Verweis Notwehrschema, § 35, BGH Haustyrann | tabler:`cloud-snow`, `scale`, `gavel` | `Abgrenzung › …` | – |
| **N1 Lösung** `lsg`→`ersatz` | zwei Haken, Block „straflos“, Block „Ersatz“ | tabler:`gavel`, `shield-check`, `receipt` | `Lösung › …` | – |
| **N2 Morgen** `ko2` | Hütte, Frau Moser lächelt, Blase Korbinian | tabler:`sun` | `Lösung › Korbinian zahlt das Schloss` | – |
| **O Klausurtipp** `tipp`→`k3` | hellgelbe Tafel, drei Blöcke, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **P Klausurschema** `sch`→`s5` | breite Karte, fünf Punkte progressiv | – | `Klausurschema › …` | – |
| **Q Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 21 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Tür zu → offen, Schloss → kaputt, Nacht → Morgen).
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 34 S. 1, 2; § 904 S. 1, 2; § 228 S. 1, 2 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe; gesprochen werden die Merkmale (bei § 904 S. 2 wörtlich), Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstag, 17:40 Uhr, auf 2.150 m: Korbinian (Mitte 30) ist allein auf Bergtour, als ein Wettersturz einsetzt – Schneesturm, −12 °C. Sein Handy hat kein Netz, bis ins Tal sind es 3 Stunden, eine andere Unterkunft gibt es nicht.
>
> Er erreicht eine Berghütte, die Frau Moser gehört. Sie ist im Winter verschlossen; ein Schild verbietet das Betreten. Um nicht zu erfrieren, bricht Korbinian die Tür auf; das Schloss ist danach kaputt. In der Hütte übersteht er die Nacht.
>
> Am nächsten Morgen kommt Frau Moser. Ein neues Schloss kostet 380 €. Sie fragt: „Wer bezahlt mir jetzt das neue Schloss?“
>
> **Hat Korbinian sich strafbar gemacht – und muss er das Schloss bezahlen?**
