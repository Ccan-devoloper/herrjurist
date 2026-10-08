# Folge 248 · Gesellschafterhaftung GbR § 721 BGB: Haften die Mitglieder privat? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_248.py`](src/skript_248.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Gesellschaftsrecht, Format Schema. Beispielfall nach dem Plan-Hook: Das Architekturbüro von Philipp und Mathilde (GbR) kauft beim Tischler Herrn Altmann Möbel für 18.000 €; Alma tritt im März ein, Mathilde scheidet Ende April aus; im Juli verlangt Herr Altmann das Geld von Philipp privat; das Büro hat ein fälliges Gegenhonorar von 3.000 €. Ablauf: Fall (Büro Februar–April → Büro Juli) → Sachverhalt → I. Schuld der GbR (§ 705 Abs. 2, § 433 Abs. 2; Verweis 173) → II. § 721 (Wortlaut, Rechtsstand) → Merkmale (persönlich, unbeschränkt, unmittelbar/primär, gesamtschuldnerisch, akzessorisch; Verweis 120) → III. § 721a (Wortlaut, Zeitleiste) → IV. § 721b Abs. 1 und 2 (Wortlaut, Aufrechnung 3.000 €) → V. § 728b (Wortlaut, Zeitleiste Mathilde) → VI. § 722 Abs. 2 (Wortlaut) → VII. Innenausgleich (§ 716 Abs. 1, § 426) → Ergebnis im Büro → Klausurtipp (Lexi) → Prüfungsschema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:22,6 bei 5.742 Skriptzeichen (5.723 vertont; Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Philipp (PH), um 35 | Architekt, Gesellschafter, wird in Anspruch genommen | `standing/blazer-3` (Sakko Petrol `#3E6E8E`, schwarzes Shirt, Hose Hellgrau `#C9CCD3`), Kopf `Short 4`, Haut `#E2AE88`, kein Bart; Mimiken `Calm`, `Smile`, `Smile Big\|Smile`, `Suspicious`, `Serious`, `Concerned\|Serious` (auch redet), `Awe` | `niklas` (Mann, jung) |
| Alma (AL), um 28 | Architektin, tritt im März ein | `standing/pointing_finger-2` (schwarzes Oberteil, Hose Grün `#8FD694`), Kopf `Long Curly`, Haut `#C68E6A`; Mimiken `Calm`, `Smile`, `Smile Big\|Smile` (auch redet), `Suspicious`, `Awe`, `Serious`, `Concerned\|Serious` | `ela_froh` (Frau, jung, fröhlich – nur der heitere Eintrittssatz) |
| Mathilde (MA), um 63 | Architektin, scheidet Ende April aus (Ruhestand); spricht nicht | `standing/blazer-4` (Blazer Lila `#B8A9F5`, Oberteil Weiß, schwarze Hose), Kopf `Gray Medium` (Haar Grau `#CFCFCF`), Brille `Glasses 3`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile`, `Suspicious`, `Serious`, `Awe` | – |
| Herr Altmann (AT), um 65 | Tischler, Verkäufer, Gläubiger | `standing/crossed_arms-1` (Pullover Sand `#C9A46A`, schwarze Hose), Kopf `No Hair 2`, Brille `Glasses`, Haut `#EBC29E`; Mimiken `Calm`, `Serious` (auch redet), `Suspicious`, `Smile`, `Awe` – bestimmt, sachlich, keine Karikatur | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht reserviert und in keiner bisherigen Folge (Volltextsuche `grep -rlw` über `.py/.md/.json/.txt/.csv` in `youtube/`, 08.10.2026: Philipp 0, Alma 0, Mathilde 0, Altmann 0; verworfen wegen früherer Verwendung: Jonas, Anton, Lothar, Hendrik; wegen möglicher englischer oder uneindeutiger Lesart: Kolja, Thies, Piet, Martin). Eingetragen in `namen_reserviert.txt` („248: Philipp, Alma, Mathilde, Altmann“). Keine Genitivformen im Sprechtext.
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia; `julia` nicht besetzt, `ela_froh` nur für Almas fröhlichen Eintrittssatz.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. A1: Philipp und Mathilde (`_r`) zu Alma bzw. Herrn Altmann, Herr Altmann und Alma nach links zu ihnen. A2/Ergebnis: Alma und Philipp (`_r`) zu Herrn Altmann an der Tür, er nach links. Tafelfolien: alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `PH_redet`, `AL_redet`, `AT_redet` (je links/rechts) und Lexi. Figuren-PNGs: `../peeps/op_248/` (80 Dateien, nicht im Repository, im Drive-Master).
- Keine Prothesen-Posen (`blazer-1`, `blazer-2`, `shirt-1`, `shirt-2` verworfen), keine Bärte, keine Polka Dots, keine realen Personen oder Firmen.

**Abweichung von den letzten Folgen:** 245 (Wohnzimmer/Stube; `shirt-4`, `shirt-3`), 246 (`resting-2`, `crossed_arms-2`), 247 (`easing-1`, `walking-1`). 248: Architekturbüro (neu; Folge 173 Proberaum/Musikgeschäft, 120 WG), Posen `blazer-3`, `pointing_finger-2`, `blazer-4`, `crossed_arms-1` in keiner der drei Vorfolgen; Kleidung ohne Muster.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Büro, Februar–April** `fall`–`rund` | Architekturbüro (Fenster, Pflanze); ab 0,0 s Philipp und Mathilde mit Namensschild; ab „Februar“ neue Möbel (Regal, Tisch, Lampe) und Herr Altmann; ab „März“ Alma, Blase Alma („Ab heute bin ich dabei! …“); ab „Ende April“ Karton bei Mathilde, Pille „scheidet aus · Ruhestand“, Rundschreiben | tabler:`plant-2`, `desk` (Holz), `lamp-2`, `books`, `archive`, `box`, `mail`; Regal aus Grundformen | `Fall · Das Architekturbüro` → `· Februar: Möbel für 18.000 €` → `· März: Alma tritt ein` → `· Ende April: Mathilde scheidet aus` | Grundbild · GbR-Pille · Möbel + Herr Altmann · Pillen · Alma · Blase · Karton · Rundschreiben | Karton `szene_248karton_1` (mathilde) |
| **A2 Büro, Juli** `juli`–`frage2` | Rechnung und leeres Sparschwein auf dem Tisch; Herr Altmann an der Tür; Blase Altmann („Die 18.000 € sind seit Wochen fällig …“), Blase Philipp („Die Möbel hat doch das Büro gekauft …“); zwei Fragepillen | tabler:`receipt-euro`, `pig-money`; Tür aus Grundformen | `Fall · Juli: Rechnung offen, Konto leer` → `· „Dann zahlen Sie eben privat!“` → `· Philipp: „Das Büro hat gekauft“` → `Die Frage · …` | Grundbild · Rechnung · Konto · Klopfen + Altmann · Blase · Blase · Frage 1 · Frage 2 | Klopfen `szene_248klopfen_1` (Herr Altmann an der Tür) |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,8 s), ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C I. Wer schuldet?** `gbr`–`schuld` | Tafel; Philipp, Alma | tabler:`help-circle`, `users-group`, `receipt-euro` | `I. Schuld der Gesellschaft · Wer schuldet?` → `› rechtsfähige GbR, § 705 Abs. 2 BGB` → `› Verweis: Video zur GbR` → `› Käuferin: die GbR, § 433 Abs. 2 BGB` | Titel · Zeile · Haken · Verweis · Block | – |
| **D II. § 721** `p721`–`frueher` | Wortlautkarte (4 Marker), Block „früher: entsprechend dem OHG-Recht“, BGH-Fundstelle, Block „seit 1.1.2024“; Philipp | tabler:`users`, `scale`, `calendar-event` | `II. Haftung, § 721 BGB · …` → `› Satz 1` → `› Satz 2` → `› seit 1.1.2024 im Gesetz` | Karte · 4 Marker · 2 Blöcke | – |
| **E II. Merkmale** `merk`–`akz` | fünf Haken nacheinander, Verweis 120; Philipp, Herr Altmann | tabler:`wallet`, `infinity`, `arrow-right`, `users`, `link` | `› persönlich` → `› unbeschränkt` → `› unmittelbar und primär` → `› als Gesamtschuldner, § 421 BGB` → `› akzessorisch` | 7 Stufen | – |
| **F III. § 721a** `eintr`–`afall` | Wortlautkarte (3 Marker), Zeitleiste Februar/März, ✓ Altschuld, ✗ Abrede, Block „Alma haftet mit“; Alma | tabler:`user-plus`, `receipt-euro`, `file-x` | `III. Eintritt: Alma, § 721a BGB · …` → `› Altschulden` → `› Kauf im Februar, Eintritt im März` → `› interne Abrede …` → `› Alma haftet mit (+)` | Karte · Marker · Zeitleiste · Haken · Kreuz · Block | – |
| **G1 IV. § 721b Abs. 1** `einw`–`w721b` | Wortlautkarte, Pillen „Erfüllung“, „Verjährung“; Philipp | tabler:`shield` | `IV. Einwendungen, § 721b BGB · …` → `› Abs. 1` | Karte · Marker · Pillen | – |
| **G2 IV. § 721b Abs. 2** `abs2`–`rest` | Wortlautkarte (3 Marker), ✓ Aufrechnung 3.000 €, ✓ verweigern, Block „18.000 € − 3.000 € = 15.000 € offen“; Philipp, Herr Altmann | tabler:`hand-stop`, `arrows-exchange`, `receipt-euro` | `› Abs. 2` → `› Aufrechnung …` → `› 3.000 € verweigern` → `› offen: 15.000 €` | Karte · Marker · 2 Haken · Block | – |
| **H1 V. § 728b** `aus`–`fest` | Wortlautkarte (4 Marker), ✓ „festgestellt: etwa durch Urteil“; Mathilde | tabler:`user-minus`, `hourglass`, `file-certificate` | `V. Ausgeschieden: Mathilde, § 728b BGB · …` → `› fällig binnen 5 Jahren` → `› festgestellt …` | Karte · Marker · Haken | – |
| **H2 V. Zeitleiste** `frist`–`mfall2` | Frist ab Kenntnis; Zeitleiste Februar – Ende April – Rundschreiben – Ende Juni; ✓ begründet, ✓ fällig, Block „rechtzeitige Klage“; Mathilde | tabler:`mail`, `calendar-event`, `file-certificate` | `› Frist ab Kenntnis …` → `› begründet vor dem Ausscheiden …` → `› rechtzeitige Klage …` | Zeilen · 4 Zeitpunkte · Haken · Block | – |
| **I VI. § 722 Abs. 2** `vollstr`–`beide` | Wortlautkarte (2 Marker), ✗ Titel nur gegen die GbR, ✓ Titel gegen Philipp, Block „zusammen verklagen“; Philipp, Herr Altmann | tabler:`building-bank`, `file-certificate`, `users-group` | `VI. Vollstreckung, § 722 Abs. 2 BGB · …` → `› Titel gegen die GbR reicht nicht` → `› Titel gegen Philipp selbst` → `› … zusammen verklagen` | Karte · Marker · Kreuz · Haken · Block | – |
| **J VII. Innenausgleich** `innen`–`abr2` | ✓ § 716 Abs. 1, ✓ § 426 nachrangig, Block „Abrede mit Alma“; Philipp, Alma | tabler:`cash-banknote`, `arrow-back-up`, `file-text` | `VII. Innenausgleich · …` → `› Ersatz von der GbR` → `› Mitgesellschafter nur nachrangig` → `› Abrede mit Alma` | 4 Stufen | – |
| **K Ergebnis** `erg`–`erg3` | zurück im Büro (Juli-Aufbau, Grund: Rückkehr zum Fall); drei Ergebniszeilen mit Haken | tabler:`cash-banknote` | `Ergebnis · …` | 3 Stufen | – |
| **L Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet), zwei Blöcke § 721a/§ 728b | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 5 Stufen | – |
| **M Prüfungsschema** `sch`–`s5` | breite Karte, Aufbau Punkt für Punkt | – | `Prüfungsschema › …` | Titel · 1. · 2. · 3. · 4. · Vollstreckung | – |
| **N Merksatz** `merke`/`merk2` | Lexi erklärt (redet), vier Marker | – | `Merksatz` | Satz 1 + Marker · Satz 2 + Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; keine Bewegung (kein Zoom).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen, Zahlen als Ziffern („18.000 €“, „3.000 €“). Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Philipp und Mathilde betreiben gemeinsam ein Architekturbüro als Gesellschaft bürgerlichen Rechts; im Gesellschaftsregister ist es nicht eingetragen. Im Februar kaufen sie für das Büro beim Tischler Herrn Altmann Arbeitstische und Regale für 18.000 €, zahlbar Ende Juni. Beide unterschreiben den Kaufvertrag für das Büro.
>
> Im März tritt Alma als dritte Gesellschafterin ein. Intern vereinbart sie mit den anderen, für alte Schulden nicht einzustehen. Ende April scheidet Mathilde aus; Herr Altmann erfährt davon durch ein Rundschreiben.
>
> Im Juli ist die Rechnung offen und das Konto des Büros leer. Herr Altmann verlangt die 18.000 € von Philipp aus dessen Privatvermögen. Das Büro hat gegen Herrn Altmann ein fälliges, noch offenes Honorar von 3.000 € für die Pläne seiner Werkstatt.
>
> **Muss Philipp zahlen, und haften auch Alma und Mathilde?**
