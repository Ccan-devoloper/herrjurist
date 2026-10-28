# Folge 078 · Vollstreckungsabwehrklage § 767 ZPO – Prüfung im 2. Examen – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_078.py`](src/skript_078.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZV, Themenplan-Format „Schema“, Voraussetzung Folge 054 (Rechtsbehelfe in der ZV). Beispielfall nach dem Plan-Hook: Tischlermeister Rademacher baut Herrn Neubauer einen Einbauschrank für 3.600 €; Neubauer zahlt nicht; Amtsgericht: Verhandlung 4.3.2026, Urteil 18.3.2026, rechtskräftig; am 4.5.2026 überweist Neubauer den vollen Betrag (Bankbeleg); trotzdem klingelt im Juni die Gerichtsvollzieherin. Neubauer geht zu Rechtsanwältin Kellermann (Anwaltsklausur aus Schuldnersicht). Aufbau: A. Zulässigkeit (Statthaftigkeit mit **Wortlautkarte § 767 I**, Abgrenzung §§ 766/771 je ein Satz mit Verweis auf 054; Zuständigkeit § 802; Rechtsschutzbedürfnis, BGH I ZR 180/21 Rn. 11) → B. Begründetheit (Erfüllung § 362 BGB; Präklusion mit **Wortlautkarte § 767 II** und Zeitstrahl; Aufrechnung, BGH II ZR 170/17; § 767 III) → Tenor (Klausurkonvention) → Eilrechtsschutz (§ 769 mit Glaubhaftmachung und § 775 Nr. 2; **Wortlautkarte § 775 Nr. 5**, Nr. 4, § 776, § 770) → Klausurtipp → Schema → Merksatz. Hauptfilm 6:19,2 (5.625 Zeichen; Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Rademacher (RA), um 60 | Tischlermeister, Gläubiger (spricht nicht) | Pose `standing/easing-2` (offenes, holzbraunes Arbeitshemd `#D6A06E`, blaugraue Hose `#5A6A8A`), Kopf `Gray Short`, Brille `Glasses 3`, Haut `#F0C8A8`; Mimiken `Calm`, `Suspicious` (streng), `Smile`, `Concerned|Serious` (Sorge), `Serious` (denkt) | (`william` vorgesehen, keine Rede) |
| Herr Neubauer (NB), um 40 | Schuldner, Mandant | Pose `standing/robot_dance-3` (grünes Oberteil `#8FD694`, dunkle Hose, offene Hand für den Beleg), Kopf `Short 3`, Haut `#E8B98F`; Mimiken `Calm`, `Concerned|Serious` (redet, Sorge), `Suspicious`, `Smile`, `Fear` | `marc` (Mann, mittel) |
| Rechtsanwältin Kellermann (KM), um 45 | Anwältin des Schuldners | Pose `standing/blazer-4` (dunkles Sakko `#3A3A48`, weißes Oberteil), Kopf `Long`, Haut `#C99470`; Mimiken `Calm`, `Serious` (redet), `Smile`, `Suspicious` | `laura_ruhig` (Frau, mittel) |
| Gerichtsvollzieherin (GV), um 50, ohne Namen | Vollstreckungsorgan, sachlich | Pose `standing/blazer-3` (blaugraues Sakko `#5A6A8A`, dunkle Hose), Kopf `Bun`, Brille `Glasses 2`, Haut `#F2CDB0`; Mimiken `Calm`, `Serious` (redet), `Suspicious` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (zur Tafel bzw. zur Mitte), `_r` blickt nach rechts (Rademacher in der Tischlerei, Neubauer an der Tür und in der Kanzlei). **Keine Prothesen-Posen** (shirt-1/-2, blazer-1/-2 verworfen), keine Bärte, **alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `NB_redet`, `KM_redet`, `GV_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem zugeteilten Pool (william, sabrina, marc, laura_ruhig). Die Gerichtsvollzieherin ist eine Frau wie im Thumbnail-Eintrag (Plan: „Gerichtsvollzieherin“). **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge und nicht in den laufenden Folgen 076/077 vergeben: Rademacher, Neubauer, Kellermann. Figuren-PNGs: `../peeps/op_078/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 054 (Rechtsbehelfe ZV, gleicher Hook-Typ): dort Autowerkstatt, Wohnung mit Fernseher, Siegel; Posen `polka_dots`, `pointing_finger-2`, `resting-2`, `shirt-4`. Hier neuer Fall (Tischlerei mit Einbauschrank, Wohnungstür mit Klingel, Kanzlei), neues Personal, Gerichtsvollzieherin statt Gerichtsvollzieher, keine Pfändung im Bild (der Fall endet vor einer Vollstreckungsmaßnahme).
- 072 (Verfahrensrüge): `blazer-3` dort für den Richter (dunkles Sakko, Glatze) – hier für die Gerichtsvollzieherin mit Dutt, Brille und blaugrauem Sakko; `laura_ruhig` dort Rechtsanwältin Hellwig (`pointing_finger-2`) – hier Rechtsanwältin Kellermann mit anderer Pose, anderem Kopf und Hautton.
- 076/077 (parallel): andere Posen und Namen. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Tischlerei** `fall`→`beleg` | Bodenlinie; Rademacher links (blickt nach rechts), Einbauschrank in der Mitte, Neubauer rechts | Einbauschrank aus Tafelbausteinen (`karte`, Holztöne; kein Icon vorhanden), tabler:`hammer` (bewegt), `cash-off` (Rot), `building-bank` (Blau), `cash-banknote` (Grün, wandert zu Rademacher), `receipt` (in Neubauers Hand) | `Fall · Der Einbauschrank` (ab 0,0 s) → `Fall · Klage und Urteil` → `Fall · Die Überweisung` | Werkstatt · Schrank · Hammer · Neubauer kommt · „Einbauschrank: 3.600 €“ · „zahlt nicht“ · Amtsgericht · Verhandlung 4.3.2026 · Urteil 18.3.2026 · rechtskräftig · Überweisung wandert · Bankbeleg | Hammer (`szene_078hammer_1`) |
| **B Wohnungstür** `tuer`→`n1` | Neubauer links (blickt nach rechts) in der Tür, Gerichtsvollzieherin rechts vor der Tür | Tür aus `karte`, tabler:`bell-ringing` (Gelb) | `Fall · Die Gerichtsvollzieherin` | „Trotzdem: Vollstreckungsauftrag“ · „Juni 2026“ · GV kommt · Klingel · Neubauer öffnet · GV-Blase · Neubauer-Blase | Türklingel (`szene_078klingel_1`) |
| **C Kanzlei** `kanzlei`→`frage2` | Neubauer links (blickt nach rechts), Schreibtisch mit Beleg und Urteil, Kellermann rechts | tabler:`desk` (Holz), `receipt`, `file-text` | `Fall · In der Kanzlei` → `Fall · Die Frage` | Kanzlei · Beleg und Urteil · Kellermann kommt · Neubauer-Blase · Kellermann-Blase · zwei Frage-Pillen | – |
| **D Sachverhalt** `sv` | Karte vollständig (≈ 9,7 s) | – | `Sachverhalt` | 1 | – |
| **E A. Zulässigkeit: 1. Statthaftigkeit** `zul`→`verw` | Tafel mit **Wortlautkarte § 767 I** (Marker „Einwendungen“, „Anspruch selbst“, „Klage“); Neubauer und Kellermann | tabler:`file-certificate`, `receipt`, `list-check`, `users` | `A. Zulässigkeit` → `› 1. Statthaftigkeit` → `› 1. Statthaftigkeit › Abgrenzung` | Titel · Karte · Marker · Erfüllung · Haken „Klage statthaft“ · § 766 · § 771 · Pille „Video: Rechtsbehelfe in der Zwangsvollstreckung“ | – |
| **F Zuständigkeit, Rechtsschutzbedürfnis** `zust`→`rsb3` | Tafel; Neubauer und Rademacher | tabler:`building-bank`, `file-certificate` | `› 2. Zuständigkeit` → `› 2. Zuständigkeit, § 802 ZPO` → `› 3. Rechtsschutzbedürfnis` → `› Ergebnis: zulässig` | Prozessgericht · Amtsgericht · ausschließlich · RSB · „nicht davon ab …“ + BGH · „solange … Titel“ · Haken · Block „zulässig“ | – |
| **G B. Begründetheit** `begr`→`prae3` | Tafel mit **Wortlautkarte § 767 II** und Zeitstrahl; Neubauer und Rademacher | tabler:`cash-banknote`, `calendar-event` | `B. Begründetheit` → `› Einwendung: Erfüllung, § 362 BGB` → `› Präklusion, § 767 Abs. 2 ZPO` | Obersatz · Erfüllung · Haken erloschen · Karte · drei Marker · 4.3.2026 · 4.5.2026 · Haken „nicht ausgeschlossen“ | – |
| **H Aufrechnung, Abs. 3** `gest`→`abs3` | Tafel; Neubauer und Kellermann | tabler:`arrows-exchange`, `checkup-list` | `› Präklusion: Aufrechnung` → `› § 767 Abs. 3 ZPO` | Gestaltungsrechte · Kreuz + BGH · „auch wenn …“ · Abs. 3 | – |
| **I Tenor** `tenor`→`antrag` | Tafel mit grünem Tenorblock; Neubauer und Rademacher | tabler:`gavel` (Holz), `file-text` | `Tenor (Klausurkonvention)` → `Tenor › Klageantrag in der Anwaltsklausur` | Tenor · unzulässig · Antrag | – |
| **J § 769** `eil`→`nr2` | Tafel; Kellermann und Neubauer | tabler:`hourglass`, `hand-stop`, `receipt`, `file-text` | `Eilrechtsschutz › einstweilige Einstellung, § 769 ZPO` → `› Glaubhaftmachung …` → `› Vorlage bei der Gerichtsvollzieherin, § 775 Nr. 2 ZPO` | Klage allein · Antrag · Prozessgericht · Sicherheitsleistung · Glaubhaftmachung · Beleg/eV + § 294 · Vorlage · Einstellung | – |
| **K § 775 Nr. 5** `p775`→`p770` | Tafel mit **Wortlautkarte § 775 Einl. + Nr. 5**; Neubauer und Gerichtsvollzieherin | tabler:`receipt`, `file-invoice`, `lock`, `file-certificate`, `gavel` | `› Zahlungsbeleg, § 775 Nr. 5 ZPO` → `› Quittung, § 775 Nr. 4 ZPO` → `› Maßregeln bleiben, § 776 ZPO` → `› Titel bleibt` → `› § 770 ZPO` | Karte · drei Marker · Nr. 4 · § 776 · Titel bleibt · § 770 | – |
| **L Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · das richtige Datum` → `Klausurtipp · Klage und Eilantrag` | Datum · Schluss · nicht Verkündung · Zahlung dazwischen · Haken · Klage und Eilantrag | – |
| **M Klausurschema** `sch`→`sC` | breite Karte, baut sich auf | – | `Klausurschema` → `› A. Zulässigkeit` → `› B. Begründetheit` → `› Eilantrag` | Titel · A · 1 · 2 · 3 · B · 1 · 2 · „und Abs. 3“ · Eilantrag | – |
| **N Merksatz** `merke`→`m2` | Lexi erklärt (redet), zwei Merkzeilen mit Marker | – | `Merksatz` | Klage · Einstellung | – |

**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („3.600 €“, „4.3.2026“, „§ 767“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Hammer (A), Geldschein von Neubauer zu Rademacher (A).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_078hammer_1`, `szene_078klingel_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Tischlermeister Rademacher baut Herrn Neubauer einen Einbauschrank für 3.600 €. Neubauer zahlt nicht. Nach der mündlichen Verhandlung am 4.3.2026 verurteilt ihn das Amtsgericht am 18.3.2026 zur Zahlung; das Urteil wird rechtskräftig.
>
> Am 4.5.2026 überweist Neubauer den vollen Betrag; das Geld geht auf dem Konto von Rademacher ein. Seine Bank bestätigt die Überweisung mit einem Beleg. Trotzdem beauftragt Rademacher im Juni die Gerichtsvollzieherin.
>
> Neubauer geht zu Rechtsanwältin Kellermann. Annahme: Die Überweisung deckt alles, was das Urteil zuspricht.
>
> **Wie wehrt sich Neubauer – endgültig und sofort?**
