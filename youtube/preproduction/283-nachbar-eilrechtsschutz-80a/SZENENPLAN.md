# Folge 283 · § 80a VwGO: Der Bagger rollt – Eilrechtsschutz des Nachbarn – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_283.py`](src/skript_283.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Öffentliches Recht/Baurecht · Schema. Voraussetzungen 082 (Grundschema § 80 V) und 113 (Nachbarklage) nur vorausgesetzt bzw. verwiesen; 254 (§ 123) ein Satz mit Verweis; 274/277 nicht wiederholt; Abgrenzung zu 090 in RECHTSSTAND.md.
**Ablauf:** Fall (Garten und Bauplatz) → Fragen → Sachverhalt → 1. Warum stoppt der Widerspruch nichts? (§ 212a Abs. 1 BauGB, § 80 Abs. 2 S. 1 Nr. 3 VwGO, Wortlautkarten) → 2. Statthaftigkeit (Doppelwirkung, § 80a Abs. 3, § 80 Abs. 5 S. 1 – Wortlautkarten; Anordnung; § 123 Abs. 5; § 80a Abs. 1 Nr. 2 – Wortlautkarte) → 3. übrige Zulässigkeit (Rechtsweg, Antragsbefugnis analog § 42 Abs. 2, Rechtsbehelf eingelegt, § 80 Abs. 5 S. 2) → 4. Begründetheit (Interessenabwägung, Erfolgsaussichten summarisch, Folgenabwägung, Wertung § 212a; Subsumtion Rücksichtnahme/Abstandsflächen; Antrag abgelehnt) → Ergebnis im Garten (eigenes Risiko) → Gegenfall (Abstandsfläche verletzt) → 5. umgekehrter Fall (§ 80a Abs. 1 Nr. 1 – Wortlautkarte) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:30,8 (5.713 vertonte Zeichen); Begründung in ABNAHME.md.

## Darstellung (Vorgabe Koordinator)

Bauherr und Nachbarin **fair**: Herr Brodbeck hat alles genehmigen lassen, will Wohnungen schaffen und baut „genau so, wie es genehmigt ist“; Frau Fehling wehrt sich sachlich gegen den Verlust der Abendsonne und wartet nach dem verlorenen Eilantrag auf das Hauptverfahren. Keine Karikatur, keine abwertende Mimik (keine Wut-Gesichter). Der **Bagger** (Tabler `backhoe`) ist das wiederkehrende Symbol: Fall, Tafel „§ 212a“, „kraft Gesetzes“, „Wertung des § 212a“, Ergebnis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Fehling (FE), um 40 | Nachbarin mit Haus und Garten, Antragstellerin | Pose `standing/easing-2` (offenes Hemd Orange `#F9A66C` über schwarzem Shirt, blaue Hose `#4A6FA5`), Kopf `Medium 2` (dunkelbraun), Haut `#F0C8A8`; Mimiken `Calm`, `Concerned\|Serious`, `Suspicious`, `Serious`, `Smile`; redet (`Serious`), redet2 (`Calm`) mit a/o/e | `laura_ruhig` (Frau, mittel) |
| Herr Brodbeck (BR), um 60 | Bauherr eines Mehrfamilienhauses | Pose `standing/blazer-4` (Sakko Braungrau `#8A7560` über hellem Shirt `#F2EEE6`, dunkle Hose), Kopf `No Hair 2` (Halbglatze), Brille `Glasses 4`, Haut `#E3B48E`, kein Bart; Mimiken `Calm`, `Smile`, `Suspicious`, `Serious`, `Smile Big\|Smile`; redet (`Calm`), redet2 (`Smile`) mit a/o/e | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt, redet), Merksatz (erklärt, redet) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Im Garten blickt Frau Fehling nach links zum Bauplatz; Herr Brodbeck blickt zum Bauplatz und wendet sich beim Sprechen nach rechts zu ihr (`_r`). An den Tafeln blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `BR_redet*`, `FE_redet*` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** `william`, `sabrina`, `marc`, `laura_ruhig`: verwendet `william`, `laura_ruhig`; `marc`/`sabrina` nicht (277, 280). Vorfolge 282: julia, niklas, helmut.
- **Namen** eindeutig deutsch und neu: Brodbeck, Fehling (nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, Volltextsuche über `youtube/` ohne Treffer; eingetragen „283: Brodbeck, Fehling“ vor der Vertonung). Nie im Genitiv mit -s.
- Figuren-PNGs: `../peeps/op_283/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** Posen 280 (`resting-1`, `shirt-3`, `resting-2`), 281 (`shirt-4`, `resting-1`), 282 (`easing-1`, `blazer-3`, `crossed_arms-2`) nicht verwendet; keine Polka Dots, keine Bärte, keine Prothesen-Pose. Schauplatz **Garten mit Abendsonne neben einem Bauplatz** (Tabler `sunset-2`, `fence` als Grenze, `trees`, `home-2`, `backhoe`, Erdhaufen und gestrichelter Gebäudeumriss programmatisch) – neu gegenüber 277 (Einfamilienhausstraße mit Wohnblock), 274 (Gewerbegebiet), 090 (Rohbau mit Kanzlei). Tafelgrafiken: Dreieck Behörde–Bauherr–Nachbarin, Zeitstrahl Genehmigung–Widerspruch–Eilantrag, Waage, Schnitt mit Abstandsfläche und Grenze (eingehalten / verletzt). Rückkehr in den Garten beim Ergebnis (Auflösung: Eilantrag abgelehnt, Rohbau wächst).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Garten** `fall`–`frage2` | Haus mit Garten, Frau Fehling ab 0,0 s; Baugenehmigung (Urkunde), gestrichelter Umriss 3 Geschosse; Bagger fährt ein; Blase Fehling (Ring um den Garten, Pille „Abendsonne“); Blase Brodbeck; Widerspruch (Brief), „je nach Land“; Bagger gräbt, Erdhaufen; zwei Fragen | tabler:`sunset-2` (Gelb), `fence`, `trees` (Grün), `home-2` (Rosé), `file-certificate` (Gelb), `backhoe` (Gelb), `mail` | `Fall · …` (8 Stände) | Bagger fährt ein (`szene_283bagger_1`) bei „rollt“; Schaufel gräbt (`szene_283graben_1`) bei „gräbt weiter“ |
| **B Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | – |
| **C 1. Warum?** `grund`–`darf` | Grundsatz § 80 I; Wortlautkarten § 212a I (3 Marker) und § 80 II 1 Nr. 3 (2 Marker); Haken „darf vorerst bauen“ | tabler:`book`, `backhoe`, `crane` | `1. Warum stoppt der Widerspruch nichts? › …` (4) | – |
| **D 2. Statthaftigkeit** `statt`–`w80a` | Dreieck Bauaufsicht → begünstigt/belastet; Wortlautkarte § 80a III (3 Marker), Zitierweise mit 7 VR 7.19 | tabler:`file-text`, `file-certificate`, `scale` | `2. Statthaftigkeit › …` (3) | – |
| **E Anordnung** `w805`–`p123` | Wortlautkarte § 80 V 1 (4 Marker), „Hier: Anordnung“, kraft Gesetzes (Haken), § 123 tritt zurück (Kreuz), Verweis 254 | tabler:`scale`, `backhoe`, `file-x` | 3 Stände | – |
| **F Behörde?** `beh` | Wortlautkarte § 80a I (Marker Nr. 2), möglich (Haken), Pflicht? nein (Kreuz), § 80 VI | tabler:`building-bank` | 1 Stand | – |
| **G 3. Zulässigkeit** `zul`–`v113` | Rechtsweg (Haken), Antragsbefugnis analog § 42 II, Rücksichtnahme (2 Haken), Verweis 113 | tabler:`file-text`, `building-bank`, `shield`, `sunset-2` | 5 Stände | – |
| **H Rechtsbehelf** `rbh`–`vor` | Zeitstrahl Genehmigung – Widerspruch (Haken) – Eilantrag; ohne Rechtsbehelf keine Wirkung (8 B 1108/15), Frist verstrichen (Kreuz, 7 B 334/26), Widerspruch eingelegt, § 80 V 2 | tabler:`file-certificate`, `mail`, `scale`, `hourglass`, `mail-opened` | 3 Stände | – |
| **I 4. Begründetheit** `begr`–`wert` | Waage: Fehling (Arbeiten ruhen) / Brodbeck (bauen); eigene Abwägung, Erfolgsaussichten summarisch, Folgenabwägung (7 VR 7.19), Wertung § 212a (7 B 359/25) | tabler:`scale`, `search`, `backhoe` | 5 Stände | – |
| **J Subsumtion** `nur`–`abgel` | Schnitt: Haus, Abstandsfläche (grün, eigenes Grundstück), Grenze, Garten, Abendsonne; Haken eingehalten; 4 B 52.15; Kreuz keine Rechtsverletzung; Interesse des Bauherrn überwiegt (10 B 645/23) | tabler:`shield`, `ruler-measure`, `sunset-2`, `file-x` | 6 Stände | – |
| **K Ergebnis im Garten** `fe2`–`risiko` | „Eilantrag abgelehnt“; Rohbau Erdgeschoss im Umriss; Blasen Fehling und Brodbeck; „auf eigenes Risiko“ | wie A | `Ergebnis · …` (3) | – |
| **L Gegenfall** `gegen` | Schnitt: Abstandsfläche (rot) ragt über die Grenze (Kreuz), Aussetzungsinteresse überwiegt, Gericht ordnet an (10 B 603/20) | tabler:`ruler-measure`, `barrier-block` | 1 Stand | – |
| **M 5. Umgekehrt** `umg`, `umg2` | Rechtsbehelf des Dritten mit aufschiebender Wirkung; Wortlautkarte § 80a I (Marker Nr. 1); Gericht § 80a III 1 (ohne Figuren: abstrakter Fall) | tabler:`mail`, `building-bank`, `scale` | 2 Stände | – |
| **N Klausurtipp** `tipp`–`k3` | Lexi warnt: Grund benennen (§ 212a), Anordnung statt Wiederherstellung, nur drittschützende Normen; „irgendwie rechtswidrig“ genügt nicht | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (4) | – |
| **O Schema** `sch`–`s2b` | progressiv A. I.–IV., B. I.–II. | – | `Schema · …` (9) | – |
| **P Merksatz** `merke`–`m3` | Lexi erklärt, vier Marker | – | `Merksatz` | – |

## Sachverhaltskarte

„Frau Fehling wohnt in einem Haus mit Garten. Ihr Nachbar, Herr Brodbeck, erhält von der Bauaufsichtsbehörde die Baugenehmigung für ein Mehrfamilienhaus mit 3 Geschossen und 6 Wohnungen. Kurz darauf rollt der Bagger und hebt die Baugrube aus. / Frau Fehling meint, das Haus nehme ihrem Garten die Abendsonne und verletze das Gebot der Rücksichtnahme. Sie legt fristgerecht Widerspruch ein; in ihrem Land ist dafür ein Vorverfahren vorgesehen. Herr Brodbeck baut weiter. / Das Haus hält die Abstandsflächen der Landesbauordnung zum Grundstück von Frau Fehling ein. Weitere Verstöße rügt sie nicht.“ – Frage: „Wie kommt Frau Fehling schnell zu einem Baustopp – und hat sie Erfolg?“ (kein Fiktiv-Hinweis)

## Gliederung im Bild und im Ton

Erklärung und Prüfpfad zählen gleich („Erstens: Warum stoppt der Widerspruch nichts?“ … „Fünftens, der umgekehrte Fall“; Pfade „1.“–„5.“). Im Schema steht der Klausuraufbau: A. Zulässigkeit (I. Rechtsweg, II. Statthaftigkeit, III. Antragsbefugnis, IV. Rechtsbehelf eingelegt), B. Begründetheit (I. Erfolgsaussichten, II. Wertung des § 212a) – dieselben Bezeichnungen wie in der Erklärung; Punkt 1 („Warum stoppt der Widerspruch nichts?“) erscheint im Schema als Begründung der „Anordnung“ (II.) und als „Wertung des § 212a“ (B. II.), der umgekehrte Fall (5.) ist kein Prüfungspunkt des Nachbarantrags.
