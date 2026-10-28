# Folge 254 · § 123 VwGO: Einstweilige Anordnung – Prüfungsschema – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_254.py`](src/skript_254.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Verwaltungsprozessrecht, Themenplan-Format „Schema“; Voraussetzung laut Plan: Verpflichtungsklage (Folge 093, nur verwiesen); Abgrenzung zu § 80 V VwGO (Folge 082, nur verwiesen, § 123 V als Vorrangregel).
**Fall** (Hook des Themenplans „Das Stadtfest ist in zehn Tagen, die Stadt verweigert dir den Standplatz“): Die Stadt veranstaltet ihr Stadtfest als festgesetztes Volksfest (§§ 60b, 69 GewO). Magda backt dort seit Jahren Waffeln, es ist ihr wichtigstes Geschäft im Jahr. Herr Eckstein vom Marktamt lehnt ihren Antrag ab, weil sie die Stadt in einem Leserbrief kritisiert hat; laut Lageplan sind noch 3 Plätze frei. Die Ablehnung kommt schriftlich, das Fest beginnt in 10 Tagen, eine Klage dauerte Monate. Bundesrecht (VwGO, ZPO, GewO, GG) – kein Landesrecht, keine Länderliste nötig.
**Ablauf:** Fall → Frage → Sachverhalt → A. Zulässigkeit: I. Verwaltungsrechtsweg, II. Statthaftigkeit (Wortlautkarte § 123 V; Hauptsache Verpflichtungsklage; Verweise 082/093), Sicherungs- vs. Regelungsanordnung (Wortlautkarte § 123 I), III. Antragsbefugnis analog § 42 II, IV. Rechtsschutzbedürfnis (Vorbefassung), Antrag vor Klageerhebung → B. Begründetheit: Glaubhaftmachung (Wortlautkarten § 123 III, § 920 II, § 294 I ZPO), I. Anordnungsanspruch (Wortlautkarte § 70 I, III GewO; Subsumtion), II. Anordnungsgrund, III. Vorwegnahme der Hauptsache (Grundsatz, Ausnahme BVerwG/BVerfG, Subsumtion) → Beschluss → Stadtfest → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 5:50,9 (5.064 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Magda (MA), um 30 | Standbetreiberin (Waffeln), Antragstellerin – sympathisch | Pose `standing/resting-1` (Oberteil Apricot `#F6B58A`, dunkle Hose der Pose), Kopf `Long Curly`, Haut `#F2C9A6`; Mimiken `Smile` (froh), `Calm`, `Concerned\|Serious` (Sorge, redet), `Awe` (Schreck), `Suspicious` (denkt), `Driven` (entschlossen), `Tired`, `Smile Big\|Smile` (strahlt) | `ela_froh` (Frau, jung, fröhlich) |
| Herr Eckstein (EC), um 60 | Sachbearbeiter im Marktamt der Stadt | Pose `standing/shirt-3` (Hemd Hellblau `#C9DAF5`), Kopf `Short 1`, Brille `Glasses 3`, Haut `#E8B898`; Mimiken `Calm`, `Serious`, `Solemn` (streng, redet), `Suspicious` | `helmut` (Mann, älter) |
| der Richter (RI), um 38 | Verwaltungsgericht (Funktionsrolle ohne Namen) | Brustbild `body/Blazer Black Tee` (Jacke Schwarz `#2B2B33`) hinter der Richterbank, Kopf `Short 4`, Haut `#D9A07A`; `Serious` (redet), `Calm` | `niklas` (Mann, jung) |
| ein Kind (KI), um 8 | Kundin am Waffelstand (ohne Namen, spricht nicht) | Pose `standing/walking-1` (Oberteil Grün `#8FD694`), Kopf `Bangs`, Haut `#C68E6A`, Höhe 270 px (≈ 61 % der Erwachsenen) | – |
| Lexi | Klausurtipp, Schema, Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Marktamt: Magda (links) blickt nach rechts zu Herrn Eckstein hinter der Theke, er nach links zu ihr. Gericht: Magda blickt nach rechts zum Richter, der nach links blickt. Stadtfest: Magda hinter der Standtheke, das Kind kommt von rechts und blickt nach links zum Stand. Tafelszenen: alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `MA_redet`, `EC_redet`, `RI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots.
- **Posen nicht aus 251–253** (dort `easing-1`, `resting-2`, `pointing_finger-2`, `blazer-3`, `walking-2`, `robot_dance-2`, `crossed_arms-1`; 250: `shirt-4`, `crossed_arms-2`). `robot_dance-3` für Magda verworfen (Silhouette zu nah an Lexi `robot_dance-1`).
- **Stimmen nur aus dem Pool:** `ela_froh` (Magda, keine ernste Rolle), `helmut`, `niklas`; `julia` nicht gebraucht. Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Magda, Eckstein – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per `grep -rliw` in keiner Text-/Codedatei unter `youtube/` (08.10.2026); verworfen: „Ida“ (in 173 und 249 wegen englischer Lesart verworfen). Eingetragen als „254: Magda, Eckstein“ vor der Vertonung. Kein Genitiv eines Namens im Sprechtext (Standschild „Waffeln“ statt „Magdas Waffeln“). Der Richter nennt Magda „die Antragstellerin“.
- **Darstellung:** Stadtfest fiktiv; Magda sympathisch; Herr Eckstein sachlich, keine Karikatur; Gericht als Richterbank und Waage, kein Richterhammer. Alle Menschen Open Peeps (auch das Kind), keine Icon-Gesichter.
- Figuren-PNGs: `../peeps/op_254/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 253 (Jauchegrube), 252 (Anklageschrift), 251 (Onlineshop), 233 (Marktplatz mit Demo), 082 (Imbissbude, Gericht mit Waage). Hier neu: **Amtstheke im Marktamt mit Lageplan des Stadtfests** (programmatisch), **Richterbank mit Brustbild des Richters**, **Waffelstand mit gestreifter Markise und Riesenrad**. Das Verwaltungsgericht (Waage) kehrt wie in 082 bewusst wieder, weil der Eilantrag dort entschieden wird. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Marktamt** `fall`–`monate` | Theke mit Herrn Eckstein, Magda davor; Waffeln; Lageplan mit 3 freien Plätzen; Blase Eckstein (Leserbrief, kein Platz); Blase Magda; Bescheid mit Stempel; Sanduhr | tabler:`calendar-event` (Gelb), fluent-hc:`waffle` (Gelb), fluent-hc:`newspaper`, tabler:`ban`, tabler:`file-text`, ph:`stamp` (Rot), tabler:`hourglass`; Lageplan und Theke programmatisch | `Fall · Im Marktamt: Das Stadtfest ist in 10 Tagen` (ab 0,0 s) … `Fall · Keine Zeit` | Grundbild · Waffeln · Geschäft · Lageplan · frei · Eckstein · Blase · Zeitung · Verbot · Blase Magda · Bescheid · Stempel · Monate | Stempel (`szene_254stempel_1`) |
| **A2 Frage** `frage`–`frage2` | Tafel | tabler:`hourglass`, fluent-hc:`classical-building` | `Die Frage · …` | 2 | – |
| **B Sachverhalt** `sv` | Karte zum Nachlesen (≈ 9,8 s) | – | `Sachverhalt` | 1 | – |
| **C A. I.–II.** `zul`–`verweis` | Rechtsweg, Wortlautkarte § 123 V, Vorrang §§ 80, 80a, Hauptsache Verpflichtungsklage, (−) aufschiebende Wirkung, (+) § 123, Verweise | fluent-hc:`classical-building`, tabler:`file-text`, `certificate`, `circle-check` | `A. Zulässigkeit › I. …`, `› II. Statthaftigkeit, § 123 Abs. 5 VwGO` … | 11 | – |
| **D Art der Anordnung** `wl1`–`ma_r` | Wortlautkarte § 123 I (Marker Veränderung / Regelung / wesentliche Nachteile), Blöcke Satz 1/Satz 2, Subsumtion | tabler:`lock`, `arrows-split`, fluent-hc:`waffle` | `… › Satz 1: Sicherungsanordnung`, `› Satz 2: Regelungsanordnung`, `› hier: Regelungsanordnung` | 8 | – |
| **E A. III.–IV.** `befugt`–`zul2` | Antragsbefugnis, Rechtsschutzbedürfnis, Vorbefassung, vor Klageerhebung, zulässig | tabler:`certificate`, `building`, `file-text`, `circle-check` | `A. Zulässigkeit › III. …`, `› IV. …`, `› Ergebnis: zulässig` | 8 | – |
| **F Glaubhaftmachung** `begr`–`mittel` | Wortlautkarten § 123 III, § 920 II, § 294 I ZPO; Mittel im Fall | fluent-hc:`balance-scale`, tabler:`book`, `writing-sign`, `map` | `B. Begründetheit › …` | 9 | – |
| **G B. I. Anordnungsanspruch** `aa`–`null` | Maßstab, Wortlautkarte § 70 I, III GewO, Platzmangel (−), Leserbrief (−), kein Spielraum | tabler:`scale`, fluent-hc:`circus-tent`, tabler:`map`, fluent-hc:`newspaper`, tabler:`circle-check` | `B. Begründetheit › I. Anordnungsanspruch › …` | 12 | – |
| **H II. Anordnungsgrund, III. Vorwegnahme** `ag`–`verbot` | Eilbedürftigkeit, Vorwegnahme, Grundsatz | tabler:`calendar-event`, `hourglass`, `ban` | `B. Begründetheit › II. …`, `› III. …` | 10 | – |
| **I Ausnahme** `ausn`–`beides` | zwei Voraussetzungen, Art. 19 IV GG, Subsumtion | tabler:`hourglass-empty`, `scale`, `shield-check` | `B. Begründetheit › III. Vorwegnahme › …` | 9 | – |
| **J Beschluss** `erg`–`ri1` | Richterbank, Waage, Richter mit Blase, Magda strahlt | fluent-hc:`balance-scale`; Richterbank programmatisch | `Ergebnis · Der Beschluss, § 123 Abs. 4 VwGO` | 3 | – |
| **K Stadtfest** `ende` | Waffelstand mit Markise, Riesenrad, Sonne; Kind kommt zum Stand | fluent-hc:`ferris-wheel`, `waffle`, tabler:`sun` | `Ergebnis · 10 Tage später auf dem Stadtfest` | 4 | – |
| **L Klausurtipp** `tipp`–`tipp2` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 6 | – |
| **M Klausurschema** `sch`–`s8` | progressiv A. I.–IV., B. I.–III. | – | `Klausurschema › …` | 11 | – |
| **N Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | 5 | – |

## Sachverhaltskarte

„Die Stadt veranstaltet jedes Jahr ihr Stadtfest, festgesetzt als Volksfest nach der Gewerbeordnung. Magda verkauft dort seit Jahren Waffeln; das Fest ist ihr wichtigstes Geschäft im Jahr. Auch diesmal beantragt sie einen Standplatz. / Herr Eckstein vom Marktamt lehnt ab: „Sie haben die Stadt in einem Leserbrief kritisiert. Für Sie gibt es dieses Jahr keinen Platz.“ Laut Lageplan sind noch 3 Plätze frei. Die Ablehnung erhält Magda schriftlich. / Das Fest beginnt in 10 Tagen. Eine Klage würde Monate dauern.“ – Frage: „Wie kommt Magda schnell zu ihrem Standplatz?“ (kein Fiktiv-Hinweis)
