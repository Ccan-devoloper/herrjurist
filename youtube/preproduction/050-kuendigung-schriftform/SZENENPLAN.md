# Folge 050 · Kündigung per WhatsApp wirksam? Schriftform nach § 623 BGB – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_050.py`](src/skript_050.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Arbeitsrecht, Themenplan-Format „Klausurfehler“. Übungsfall nach dem Plan-Hook: Werkstattinhaberin Frau Kuhlmann unterschreibt die Kündigung ihres Mechanikers Bastian, fotografiert sie und schickt das Foto per WhatsApp; das Original bleibt im Ordner. Fünf Wochen später klagt Bastian, Frau Kuhlmann beruft sich auf die Klagefrist. Prüfung der Wirksamkeit: I. Kündigungserklärung, II. Schriftform (Wortlaut § 623 BGB, Zweck, Rechtsstand 2026, Wortlaut § 126 I BGB, Zugang der Urkunde, Foto/Fax/E-Mail, § 125 S. 1, § 242), III. Zugang (§ 130, Original im Briefkasten), IV. Vertretung (§ 174, Ausblick mit Werkstattleiterin Frau Petersen), V. Klagefrist (Wortlaut § 4 S. 1 KSchG, § 7 KSchG), Ergebnis, Klausurtipp (Klagefrist als Fehlerquelle; gesetzliche vs. vereinbarte Schriftform, § 127 II), Schema I.–V., Merksatz. Zugang (§ 130) knüpft an Folge 017 an.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Kuhlmann (KU), um 60 | Inhaberin der Fahrradwerkstatt, Arbeitgeberin | `standing/crossed_arms-1` (blaues Oberteil `#8DB3F2`, schwarze Hose), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile` (redet), `Serious` (redet streng), `Smile Big|Smile` (froh), `Suspicious` (denkt), `Concerned|Serious` (Sorge), `Contempt` (Ärger) | `hilde` (Frau, älter) |
| Bastian (BA), um 25 | Mechaniker, Arbeitnehmer | `standing/walking-2` (schwarzes T-Shirt, dunkelblaue Arbeitshose `#3D4A7A`), Kopf `Short 2`, Haut `#E6B48F`; Mimiken `Calm`, `Serious` (redet), `Fear` (Schreck), `Suspicious`, `Smile`, `Smile Big|Smile`, `Concerned|Serious` | `timo` (Mann, jung) |
| Frau Petersen (PE), um 45 | Werkstattleiterin, nur im Ausblick § 174 | `standing/easing-1` (rote Jacke `#F07A6A`, weißes Oberteil), Kopf `Medium Straight`, Haut `#C68E6A`; Mimiken `Calm`, `Smile` (redet), `Suspicious` | `lea` (Frau, mittel; harmloser Satz) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, `_r` blickt nach rechts. Blickrichtungen: A Kuhlmann zum Schreibtisch; B Bastian zum vibrierenden Handy; C Bastian zu Kuhlmann (`_r`), Kuhlmann zu Bastian; Tafelfolien: Figur links (X1) blickt nach rechts zur Partnerin/zum Partner, Figur rechts (X2) und Einzelfiguren zur Tafel nach links; M Petersen zu Bastian (`_r`). Keine Prothesen-Posen, keine Bärte. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KU_redet`, `KU_streng`, `BA_redet`, `PE_redet` (je links/rechts) und Lexi. Stimmen nur aus dem Pool (timo, stephan, lea, hilde; `stephan` nicht benötigt). Namen mit eindeutig deutscher Aussprache und nicht vergeben (Kuhlmann, Bastian, Petersen; auch nicht in den parallelen Folgen 048/049). Figuren-PNGs: `../peeps/op_050/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 048 (Versäumnisurteil: Gericht), 049 (Behörde, Rücknahme), 043 (Werbeagentur/Möbelhaus), 017 (Café/Briefkasten). 050: Fahrradwerkstatt mit Rad, Werkzeug und Schreibtisch, Bastians Wohnzimmer (Sofa, Lampe, Handy) und das Arbeitsgericht von außen. Neue Posen `crossed_arms-1`, `walking-2`, `easing-1`; Stimmen hilde/timo/lea anders als in 049 (ela_warm, william, julia).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Werkstatt** `fall`→`ku1` | Boden, Fahrrad, Werkzeug, Schreibtisch; Kuhlmann rechts davon | tabler:`bike`, `tool`, `desk` (Holz), `writing-sign`, `file-text`, `camera`, `device-mobile-message`, `folder` | `Fall · Die Kündigung` (ab 0,0 s) → `Fall · Das Foto` | Werkstatt + Kuhlmann · Stift · Kündigung + Pille · „an Bastian“ · Kamera + „Foto“ · Kuhlmann redet, Blase · „per WhatsApp an Bastian“ · Ordner + „Original im Ordner“ | Stift (`szene_050stift_1`), Kameraauslöser (`szene_050kamera_1`) |
| **B Zu Hause** `whats`→`b1` | Freitagabend, Sofa, Lampe; Bastian, Handy vibriert, Chat-Karte | tabler:`sofa` (Lila), `lamp`, `device-mobile-vibration`, `photo` | `Fall · Die Nachricht` | Bastian · Handy + Chat-Karte · Schreck · Bastian redet, Blase | Handy vibriert (`szene_050vibration_1`) |
| **C Arbeitsgericht** `wochen`→`frage` | Gericht links, Bastian mit Klage, Kuhlmann rechts | tabler:`building-bank` (Blau), `file-text`, `hourglass` | `Fall · Fünf Wochen später` → `Fall · Die Frage` | Gericht + Bastian · „Arbeitsgericht“ · Klage + Kuhlmann · Kuhlmann redet, Blase, „3 Wochen?“ · Frage 1 · Frage 2 | – |
| **D Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **E Aufbau** `pruef` | Tafel mit I.–V. nacheinander | tabler:`device-mobile-message` | `Wirksamkeit der Kündigung` | Titel · I. · II. · III. · IV. · V. | – |
| **F I. Erklärung** `erkl` | Tafel, Kuhlmann allein | tabler:`file-text` | `I. Kündigungserklärung` | Satz · ✓ eindeutig, Kuhlmann froh | – |
| **G Wortlaut § 623** `form`→`zweck` | Wortlautkarte, Marker synchron, Zweck | tabler:`signature`, `shield-check` | `II. Schriftform › § 623 BGB` → `› Zweck` | Karte · 4 Marker · Zweck 1–3 · Fundstelle | – |
| **H Rechtsstand** `stand` | Tafel Rechtsstand 2. Oktober 2026 | tabler:`calendar-event`, `certificate` | `II. Schriftform › Rechtsstand 2. Oktober 2026` | ✓ unverändert · BEG IV · Zeugnis · Block „nicht geändert“ | – |
| **I Wortlaut § 126 I** `p126`→`zugeh` | Wortlautkarte, Urkunde wandert zu Bastian | tabler:`writing-sign`, `file-text` | `II. Schriftform › § 126 Abs. 1 BGB` → `› Zugang der Urkunde` | Karte · 3 Marker · Block · Fundstelle | – |
| **J Foto, Fax, E-Mail** `subs`→`mail` | Tafel, Bastian allein; wechselnde Requisiten | tabler:`photo`, `folder`, `printer`, `mail` | `II. Schriftform › Foto, Fax, E-Mail` | ✗ Foto · Abbild · Ordner · ✗ Fax · Fundstelle · ✗ E-Mail · elektronische Form | – |
| **K Rechtsfolge** `nichtig`→`treu` | Tafel, Block § 125 | tabler:`file-x` | `II. Schriftform › Rechtsfolge, § 125 S. 1 BGB` → `› Treu und Glauben` | ✗ · Block nichtig · Treu und Glauben 1–3 · Fundstelle | – |
| **L III. Zugang** `zug`→`frist_ab` | Tafel, Brief wandert in den Briefkasten | tabler:`device-mobile-message`, `mailbox`, `mail`, `hourglass` | `III. Zugang, § 130 BGB` | ✓ Handy · ✗ formgerecht · Original/Briefkasten · § 130 · Block Klagefrist | – |
| **M IV. Vertretung** `vertr`→`kennt` | Tafel, Petersen übergibt, redet | tabler:`file-certificate`, `hand-stop`, `message` | `IV. Vertretung › Ausblick` → `› Zurückweisung, § 174 BGB` | Petersen · Blase · ✗ Vollmachtsurkunde · § 174 S. 1 · Woche · Block S. 2 | – |
| **N V. Klagefrist** `klage`→`lauf` | Wortlautkarte § 4 S. 1 KSchG, § 7 | tabler:`hourglass`, `file-x` | `V. Klagefrist › § 4 S. 1 KSchG` → `› § 7 KSchG` → `› nur bei schriftlicher Kündigung` | Karte · Marker drei Wochen · § 7 · Marker „schriftlichen Kündigung“ · ✗ · Block · Fundstelle | – |
| **O Ergebnis** `erg` | Tafel, beide Figuren | tabler:`bike` | `Ergebnis · Kündigung nichtig` | nichtig · besteht fort | – |
| **P Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Fehlerquelle Klagefrist` → `· gesetzliche oder vereinbarte Schriftform` | Satz · § 7 · gesetzlich · vereinbart | – |
| **Q Klausurschema** `sch`→`k5` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I. · II. · Urkunde · nichtig · III. · IV. · V. | – |
| **R Merksatz** `merke`→`m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | Satz 1 + Marker · Satz 2 · Satz 3 + Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo ein Schriftstück unterwegs ist (Urkunde zu Bastian, Original in den Briefkasten).
**Geräusche:** drei Handlungsgeräusche aus Freesound CC0 (`szene_050stift_1`, `szene_050kamera_1`, `szene_050vibration_1`), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** wortgleich mit dem Gesprochenen. Tafeln verwenden Ziffern und Normzeichen. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 02.10.2026).

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Frau Kuhlmann führt eine kleine Fahrradwerkstatt und beschäftigt den Mechaniker Bastian. An einem Freitagabend unterschreibt sie eigenhändig eine Kündigung, fotografiert das Schreiben mit dem Handy und schickt das Foto per WhatsApp an Bastian. Er sieht die Nachricht sofort. Das unterschriebene Original legt Frau Kuhlmann in einen Ordner; Bastian erhält es nie.
>
> Fünf Wochen später erhebt Bastian Klage beim Arbeitsgericht. Frau Kuhlmann meint, die Kündigung gelte als wirksam, weil Bastian nicht innerhalb von drei Wochen geklagt habe.
>
> **Hat die Kündigung per WhatsApp das Arbeitsverhältnis beendet?**
