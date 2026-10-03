# Folge 101 · Formelle Verfassungsmäßigkeit: So entsteht ein Bundesgesetz – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_101.py`](src/skript_101.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Schema. Beispielfall nach dem Hook des Themenplans („Ein Gesetz wird nachts ohne ordnungsgemäße Beteiligung des Bundesrats beschlossen – ist es wirksam?“), Vorbild offengelegt: Zuwanderungsgesetz (BVerfG, Urt. v. 18.12.2002 – 2 BvF 1/02). Kurz vor Mitternacht beschließt der Bundestag ein Gesetz der Bundesregierung: Die Meldebehörden der Länder bearbeiten Anträge nur noch digital, nach einem festen Verfahren ohne Abweichungsmöglichkeit (zustimmungsbedürftig, Art. 84 I 6 GG). Im Bundesrat sagt für ein Land Ministerin Hensel „Ja“, Minister Rieger „Nein“; der Präsident wertet das als Ja. Der Bundespräsident fertigt aus, das Gesetz wird im elektronischen Bundesgesetzblatt verkündet; Frau Kähler (Meldebehörde) freut sich auf den 1. März. Ablauf: Fall → Frage (wirksam?) → Sachverhalt → Einordnung (formelle Verfassungsmäßigkeit, I. Zuständigkeit in zwei Sätzen, Verweis Folge 098) → II. Verfahren: 1. Initiative (Art. 76) → 2. Beschluss des Bundestages (Wortlautkarte Art. 77 I 1, Art. 42 II, Beschlussfähigkeit § 45 GO-BT) → 3. Bundesrat: Einspruchs- oder Zustimmungsgesetz (Art. 84 I 6), Vermittlungsausschuss, Einspruch, Zurückweisung (Art. 77 II–IV), Zustandekommen (Wortlautkarte Art. 78), Stimmabgabe (Wortlautkarte Art. 51 III 2, Art. 52 III 1) → III. Form (Auszug Art. 82 I, Art. 58, Prüfungsrecht ein Satz, elektronisches BGBl., Art. 82 II) → Ergebnis (nichtig) → Klausurtipp (Lexi: GO-Verstoß, Evidenz) → Klausurschema als Weg des Gesetzes → Merksatz (Lexi).
**Länge:** Hauptfilm 7:00,5 (6.031 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Der Bundesratspräsident (ohne Namen, um 60) | leitet die Abstimmung, wertet die Stimmen als Ja; Funktionsrolle | Pose `standing/crossed_arms-1` (blauer Pullover `#8DB3F2`, schwarze Hose – in dieser Pose nicht einfärbbar), Kopf `Gray Medium` (Haar `#C4C4CC`), Brille `Glasses 3`, Haut `#EBC2A0`; Mimiken `Calm`, `Serious` (redet), `Driven` | `helmut` (Mann, älter) |
| Frau Hensel (um 45) | Landesministerin, stimmt „Ja“ | Pose `standing/pointing_finger-1` (erhobener Zeigefinger wie beim Handzeichen; schwarzes Outfit, Pose ohne einfärbbare Kleidung), Kopf `Medium Bangs 2`, Haut `#F1C6A5`; `Calm`, `Driven` (redet), `Smile`, `Suspicious` | `julia` (Frau, jung; ruhig-sachlich) |
| Herr Rieger (um 35) | Landesminister, stimmt „Nein“ | Pose `standing/robot_dance-2` (schwarzer Pullover, Hand zur Seite, Hose Braun `#9A7B5B`), Kopf `Short 2`, Haut `#C68E62`; `Calm`, `Serious` (redet), `Contempt` (Ärger), `Suspicious` | `niklas` (Mann, jung) |
| Frau Kähler (um 30) | Sachbearbeiterin in einer Meldebehörde, heitere Nebenrolle | Pose `standing/polka_dots` (weißes Oberteil mit schwarzen Punkten, Hose Rot `#F07A6A`), Kopf `Long Bangs`, Haut `#E8B894`; `Calm`, `Smile` (redet), `Smile Big|Smile`, `Suspicious`, `Concerned|Serious`, `Awe` (redet erstaunt) | `ela_froh` (Frau, jung; nur heitere/erstaunte Sätze) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Szene B: der Präsident (links) blickt nach rechts zu den Ländervertretern, Hensel und Rieger blicken nach links zu ihm; Szene C: Frau Kähler blickt nach links zum Laptop; an den Tafeln blicken alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `PR_redet`, `HS_redet`, `RI_redet`, `KA_redet`, `KA_redetstaunt` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine weiteren Menschen im Bild (Bundestag nur als Gebäude mit leeren Sesseln, der Bundespräsident nur als Unterschrift).
- **Stimmen nur aus dem Pool** (`helmut`, `julia`, `niklas`, `ela_froh`), alle vier eingesetzt; Erzählerin/Lexi Carla ohne Rolle. Vorfolge 098 nutzte `julia`, `ela_froh`, `helmut` – der Pool hat nur vier Stimmen, eine Überschneidung war nicht vermeidbar; die Figuren und Sätze sind neu.
- **Namen mit eindeutig deutscher Aussprache, neu:** Hensel, Rieger, Kähler (nicht in der Liste vergebener Namen; `grep -rlw` über alle Skripte und Dokumente in `preproduction/` ohne Treffer; keine bekannten Politikernamen). Präsident ohne Namen. Präfixe `PR_`, `HS_`, `RI_`, `KA_` (nie `ER_`).
- Kein Fiktiv-Hinweis; keine realen Personen, Parteien oder Länder (das Vorbild nur als „Zuwanderungsgesetz, BVerfG 2002“).
- Figuren-PNGs: `../peeps/op_101/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 098 (Landtag mit Rednerpult, Wohnungstür), 099 (Straße mit Auto, Bankschalter), 100 (Rücktritt, parallel produziert). Hier neu: **Bundestag bei Nacht** (Gebäude, Mond, leere Sessel), **Bundesrat mit Pult** und **Meldebehörde mit Laptop/elektronischem Bundesgesetzblatt**. Das Pult aus 098 kehrt bewusst zurück (Parlament), steht aber neben dem Präsidenten statt vor einer Ministerin. Posen nicht aus 098/099 (`blazer-1/-3`, `resting-2`, `shirt-4`, `walking-3`) und nicht aus 100 (`robot_dance-3`, `crossed_arms-2`); keine Muster in 098–100, Polka Dots zuletzt in 081. Tageslicht-Cremegrund auch in der Nachtszene (Nacht nur über Mond und Pille „kurz vor Mitternacht“).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Bundestag** `fall`–`mehrheit` | Gebäude bei Nacht, Pillen Entwurf/Stellungnahme/Gesetz, leere Sessel, „Mehrheit: Ja“ | fluent-hc:`classical-building`; tabler:`moon-stars` (Gelb), `armchair` | `Fall · Nachts im Bundestag` (ab 0,0 s) | Gebäude · Entwurf · Stellungnahme · Gesetz · Verfahren · Sessel · Beschlussfähigkeit · Mehrheit | – |
| **B Bundesrat** `br`–`knapp` | Präsident am Pult, Hensel, Rieger; Blasen Präsident – Hensel – Rieger – Präsident; „4 Stimmen“, „keine Mehrheit“ | tabler:`podium` | `Fall · Abstimmung im Bundesrat` | Präsident · Hensel · Rieger · vier Blasen · Mimiken · Block · Pille | – |
| **C Ausfertigung** `aus`–`vorbild` | Unterschrift, Laptop (BGBl.), Frau Kähler mit Blase, Frage, Vorbild | tabler:`signature`, `device-laptop` | `Fall · Ausgefertigt und verkündet` → `Fall · Ist das Gesetz wirksam?` | Unterschrift · Laptop · Internet · Kähler · Blase · Frage · Vorbild | Unterschrift (`szene_101unterschrift_1`) |
| **D Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **E Einordnung** `einord`–`verw` | I. Zuständigkeit, II. Verfahren, III. Form; Meldewesen Art. 73 I Nr. 3; Verweis 098 | fluent-hc:`classical-building` | `Formelle Verfassungsmäßigkeit des Bundesgesetzes` → `… › I. Zuständigkeit, Art. 73 I Nr. 3 GG` | Zeilen zum Wort | – |
| **F 1. Initiative** `ini`–`ini3` | drei Initianten, Vorverfahren, Fall | tabler:`route` → `file-text` | `II. Verfahren › 1. Gesetzesinitiative, Art. 76 GG` | Zeilen · Haken | – |
| **G 2. Beschluss** `bt`–`bt2` | Wortlautkarte Art. 77 I 1 (zwei Marker), Art. 42 II, § 45 GO-BT, Haken | fluent-hc:`classical-building` → tabler:`moon-stars` | `… › 2. Beschluss des Bundestages, Art. 77 I 1 GG` → `… › Beschlussfähigkeit, § 45 GO-BT` | Karte · Marker · Zeilen · Haken | – |
| **H 3. Bundesrat** `brt`–`b84b` | Einspruchs-/Zustimmungsgesetz, Art. 84 I 6, Haken | fluent-hc:`ballot-box-with-ballot` | `II. Verfahren › 3. Beteiligung des Bundesrates › Einspruchs- oder Zustimmungsgesetz` | Zeilen · Block · Haken | – |
| **I Ablauf** `vma`–`zug` | Vermittlungsausschuss, Einspruch, Zurückweisung, Zustimmung | tabler:`arrows-split` | `… › Vermittlungsausschuss, Einspruch, Art. 77 II–IV GG` | Zeilen · Blöcke | – |
| **J Art. 78** `wl78`–`z4` | Wortlautkarte Art. 78 (vier Marker) | fluent-hc:`check-box-with-check` | `… › Zustandekommen, Art. 78 GG` | Karte · Marker | – |
| **K Stimmabgabe** `st`–`keine` | Art. 52 III 1, Wortlautkarte Art. 51 III 2, Pillen „Ja“/„Nein“, Kreuz, BVerfG, keine Mehrheit | – | `… › Stimmabgabe, Art. 51 III 2, 52 III 1 GG` | Zeilen · Karte · Marker · Pillen · Kreuz · Block | – |
| **L III. Form** `form1`–`heil` | Auszug Art. 82 I (fünf Marker), Art. 58, Prüfung, BGBl. elektronisch, Art. 82 II, Kreuz | tabler:`signature` → `device-laptop` | `Formelle Verfassungsmäßigkeit › III. Form, Art. 82 GG` → `III. Form › Verkündung im elektronischen BGBl.` → `III. Form › Inkrafttreten, Art. 82 II GG` | Karte · Marker · Zeilen · Kreuz | – |
| **M Ergebnis** `erg`–`ka2` | nichtig, Vorbild, Blase Frau Kähler | – | `Ergebnis · Gesetz nichtig` | Kreuz · Block · Zeilen · Blase | – |
| **N Klausurtipp** `tipp`–`tipp3` | Lexi warnt: GO-Verstoß, Evidenz | Warnsymbol (Streamline Freehand) | `Klausurtipp · Welche Fehler machen nichtig?` | Zeilen · Block · Haken | – |
| **O Klausurschema** `sch`–`s5` | Weg des Gesetzes: Stationen I.–III., Ergebnis | tabler:`flag` | `Klausurschema · Formelle Verfassungsmäßigkeit` | 11 Stationen | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, Marker | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Kurz vor Mitternacht beschließt der Bundestag ein Gesetz der Bundesregierung (der Bundesrat hatte Stellung genommen): Die Meldebehörden der Länder bearbeiten Anträge nur noch digital, nach einem festen Verfahren ohne Abweichungsmöglichkeit. Niemand bezweifelt die Beschlussfähigkeit. – Im Bundesrat sagt für ein Land mit 4 Stimmen Ministerin Hensel ‚Ja‘, Minister Rieger ‚Nein‘. Der Präsident wertet das als Ja: Zustimmung. Ohne die 4 Stimmen gäbe es keine Mehrheit. Der Bundespräsident fertigt aus, das Gesetz wird im Bundesgesetzblatt verkündet.“ – Frage: „Ist das Gesetz wirksam zustande gekommen?“ (kein Fiktiv-Hinweis)
