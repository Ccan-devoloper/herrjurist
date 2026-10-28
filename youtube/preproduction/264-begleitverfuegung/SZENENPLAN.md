# Folge 264 · Begleitverfügung StA: Haft, Pflichtverteidiger, Mitteilungen – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_264.py`](src/skript_264.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Themenplan-Format „Formulierung“ mit selbst formuliertem Muster. Beispielfall nach dem Plan-Hook („Der Beschuldigte sitzt seit drei Monaten in Untersuchungshaft, als deine Anklage fertig ist“): Referendarin Ortlieb hat die Anklage gegen Herrn Wittig fertig (Einbruch ins Baumarktlager, Werkzeug für 7.800 €); Wittig sitzt seit dem 9.7.2026 wegen Fluchtgefahr in Untersuchungshaft und hat eine Pflichtverteidigerin; eine zweite Anzeige (E-Bike von Herrn Dengler) trägt keinen hinreichenden Tatverdacht. Oberstaatsanwältin Pfaff fragt nach der Begleitverfügung. Gleiche erfundene Staatsanwaltschaft Ahornstadt wie Folge 252 (Voraussetzung), neuer Fall.
Ablauf: Fall → Frage → Sachverhalt → Wozu (Abgrenzung zur Anklage, kein Widerspruch, Form je Land) → **Muster I.–VI.** (Kopf mit Vermerk „Haft“ und I. Vermerk § 169a [Wortlaut] → II. Teileinstellung § 170 Abs. 2 [Wortlautkarte], § 154, Bescheid § 171 S. 1 [Wortlautkarte] mit Belehrung → III. Haft: Fortdauerantrag in der Anklage, Sechsmonatsfrist § 121 Abs. 1 [Wortlautkarte] → IV. Pflichtverteidigung § 140 Abs. 1 Nr. 4, 5 [Wortlautkarte] → V. Mitteilungen und Asservate → VI. Anklage mit den Akten an das Gericht) → zwei typische Fehler → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Hauptfilm 6:34,3 (5.782 Zeichen; Segment 4 einmal nachvertont), Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Referendarin Ortlieb (OR), um 27 | schreibt Anklage und Begleitverfügung | Pose `standing/resting-1` (Oberteil Grün `#8FD694`, schwarze Hose), Kopf `Long Bangs`, ohne Brille, Haut `#F2C9A8`; Mimiken `Calm`, `Concerned\|Serious` (redet, Sorge), `Suspicious`, `Smile`, `Driven`, `Awe` | `lucy` (Frau, jung) |
| Oberstaatsanwältin Pfaff (PF), um 60 | Ausbilderin | Pose `standing/blazer-4` (Blazer Marineblau `#3D5A80`, weißes Oberteil, schwarze Hose), Kopf `Gray Medium` (Haar `#C9C9C9`), Brille `Glasses 2`, Haut `#EDC3A0`; Mimiken `Calm`, `Serious` (redet), `Smile` (redet2), `Suspicious`, `Solemn` | `hilde` (Frau, älter) |
| Herr Wittig (WI), 38 | Beschuldigter in Untersuchungshaft, spricht nicht | Pose `standing/robot_dance-2` (schwarzes Oberteil, Jeans `#5B7DB1`), Kopf `Short 1`, Haut `#E9B996`; Mimiken `Calm`, `Serious`, `Solemn` | – |
| Herr Dengler (DE), um 50 | Anzeigeerstatter, Verletzter (E-Bike) | Pose `standing/crossed_arms-2` (schwarzes Oberteil, Hose `#6B7A8F`), Kopf `Short 2`, Brille `Glasses 3`, Haut `#DDA885`; Mimiken `Calm`, `Suspicious` (redet), `Tired` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (zur Tafel), `_r` blickt nach rechts (Ortlieb im Büro zu Pfaff, Dengler im Hof zu Wittig). Keine Prothesen-Posen, keine Bärte, keine Polka Dots. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `OR_redet`, `PF_redet`, `PF_redet2`, `DE_redet` (je links/rechts) und Lexi. Beschuldigter in Alltagskleidung mit ruhiger Mimik, ohne Herkunfts- oder Hautfarben-Klischee; **Haft nur als Symbol** (Akte mit rotem Vermerk „Haft“), keine Zelle, keine Person hinter Gittern; keine Tatszene, keine Gewalt. Stimmen nur aus dem Pool (`christian` nicht gebraucht; `stephan` spricht nur in Szene B2 ohne `christian`). **Namen:** Ortlieb, Pfaff, Wittig, Dengler – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per `grep -rliw` unter `youtube/` ohne Treffer (verworfen: Buchner – Treffer in 034, Hellmann/Kerner – zu nah an Hellmers/Kerber); vor der Vertonung als „264: Ortlieb, Pfaff, Wittig, Dengler“ eingetragen. Neben der Tafel heißt das Schild „OStAin Pfaff“ (volle Schildbreite passt nicht neben Ortlieb, per Assertion geprüft), in den Fallszenen „Oberstaatsanwältin Pfaff“. Figuren-PNGs: `../peeps/op_264/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** Posen nicht aus 261–263 (`resting-2`, `shirt-3/-4`, `easing-1/-2`, `blazer-3`, `pointing_finger-2`, `walking-1/-2/-3`). Gegenüber 252 (Voraussetzung, Büro mit Fenster, Bücherregal, Lampe, sitzender Referendar; Erdgeschosswohnung) hier: Büro mit Aktenschrank, Wandkalender, Pflanze, Stehtisch mit Akte (Haftvermerk) und fertiger Anklage; Baumarktlager mit Kamera und Transporter; Hof mit Zaun und Fahrrad. Musterblatt der Verfügung (weiß, rote Randlinie) mit rotem Vermerk „Haft“. Cremegrund durchgehend.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Büro** `fall`→`o1` | Aktenschrank, Wandkalender, Tisch mit Akte, Pflanze, Tür rechts; Ortlieb neben dem Tisch, Pfaff in der Tür | tabler:`archive`, `calendar-event`, `plant-2` (Grün), `door` (Holz → hell, offen), `folder` (Gelb), `file-check`; Tisch als `karte`/`linienzug`; Pille „Haft“ (Rot) | `Fall · Staatsanwaltschaft Ahornstadt` → … → `Fall · Was gehört hinein?` | Büro ab 0,0 s · Ortlieb · Anklage · Haftvermerk · Tür auf, Pfaff · Pfaff redet (Blase) · Ortlieb redet (Blase) | Tür öffnet sich (`szene_264tuer_1`) |
| **B1 In der Akte** `akte`→`fest` | Akte mit Haftvermerk; Baumarktlager, Werkzeug, Kamera, Transporter; Herr Wittig | tabler:`folders`, `building-warehouse` (Gelb), `tools` (Blau), `device-cctv`, `truck`, `plane-departure`, `file-text`, `folder`, `briefcase`; Ring | `Fall · In der Akte` → `· Einbruch ins Baumarktlager` → … → `· 9.7.2026: Festnahme, Pflichtverteidigerin` | 10 | – |
| **B2 Anzeige Dengler** `dengler`→`nur` | Hof mit Zaun und Fahrrad; Dengler (redet), Wittig | tabler:`fence`, ph:`bicycle-bold` (Blau, verschwindet; Ring), tabler:`file-check` | `Fall · Anzeige von Herrn Dengler` → … → `· angeklagt: nur der Einbruch` | 5 | – |
| **B3 Frage** `frage` | zurück im Büro | wie A | `Fall · Die Frage` | 3 Pillen zum Wort | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **D Wozu** `wozu`→`land` | Tafel: Anklage vs. Verfügung, Kreuz „nie ein Widerspruch“, Länderhinweis; Ortlieb, Pfaff | tabler:`clipboard-list`, `building-bank` (Blau), `x`, `map-pin` (Rot) | `Begleitverfügung › …` | 5 | – |
| **E Kopf, I.** `kopf`→`v1f` | Musterblatt (Kopf, „Verfügung“, Vermerk „Haft“, I.), Wortlautkarte § 169a, Block Akteneinsicht | tabler:`rubber-stamp`, `file-check`, `eye` | `Muster › Kopf: Vermerk „Haft“` → `› I. …` | 8 | – |
| **F1 II.** `e`→`e154` | Wortlautkarte § 170 Abs. 2 (vier Marker), Musterblatt II., Block § 154 | ph:`bicycle-bold`, tabler:`file-x`, `mail`, `scale`, `clipboard-list` | `Muster › II. Teileinstellung › …` | 10 | – |
| **F2 II. Bescheid** `e4`, `e5` | Wortlautkarte § 171 S. 1 (drei Marker), Musterblatt Bescheid und Belehrung; Dengler neben Ortlieb | tabler:`mail`, `calendar-event` | `› Bescheid, § 171 StPO` → `› Belehrung des Verletzten` | 6 | – |
| **G1 III. Haft** `h`→`h3` | Musterblatt III., Haken „passen zusammen“ | tabler:`folder` + Pille „Haft“, `scale`, `file-text`, `check` | `Muster › III. Haft › …` | 7 | – |
| **G2 Sechsmonatsfrist** `h121`→`h6` | Wortlautkarte § 121 Abs. 1 (sieben Marker), Musterblatt Frist | tabler:`hourglass`, `calendar-event`, `building-bank` | `› Sechsmonatsfrist …` → `› Frist notieren, Vorlage an das OLG` | 11 | – |
| **H IV.** `pv`→`pv4` | Wortlautkarte § 140 Abs. 1 Nr. 4, 5 (sechs Marker), Musterblatt IV. | tabler:`briefcase`, `building-bank`, `folder` + Pille „Haft“, `file-text` | `Muster › IV. Pflichtverteidigung › …` | 13 | – |
| **I V.** `mi`→`as2` | Musterblatt V. 1.–4., Fundstellen, Block | tabler:`mail-forward`, `briefcase`, `mailbox`, `tools`, `device-usb` | `Muster › V. Mitteilungen und Asservate › …` | 9 | – |
| **J VI.** `vi`→`p2` | Musterblatt VI., Haken § 199, Block; Pfaff liest gegen (Blase) | tabler:`building-bank`, `folders` | `Muster › VI. …` → `Fall · Pfaff liest gegen` | 5 | – |
| **K Fehler** `fehler`→`f2c` | zwei Fehler mit Kreuz, Block „Widerspruch“, Haken „Frist ruht“ | tabler:`alert-triangle`, `file-x`, ph:`bicycle-bold`, tabler:`hourglass`, `building-bank` | `Typische Fehler › …` | 12 | – |
| **L Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 6 | – |
| **M Schema** `sch`→`s6` | I.–VI. | – | `Schema › …` | 7 | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 6 (Marker zum Wort) | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom. Das erste Bild nach dem Intro zeigt ab 0,0 s das Büro (Aktenschrank, Kalender, Tisch mit Akte, Pflanze, geschlossene Tür, Titelpille, Prüfpfad).
**Geräusche:** ein Handlungsgeräusch (Tür, wenn Pfaff hereinschaut). Freesound-API über den Proxy am 08.10.2026 erreichbar (HTTP 200); Datei neu zugeschnitten, Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Herr Wittig (38) soll in der Nacht zum 21. Juni 2026 in das Lager eines Baumarkts in Ahornstadt eingebrochen sein und Werkzeug für 7.800 € mitgenommen haben. Eine Kamera zeigt ihn; das Werkzeug findet die Polizei in seinem Transporter. Es ist fotografiert, die Aufnahme liegt auf einem USB-Stick bei den Akten.
>
> Weil er seine Wohnung gekündigt und einen Flug gebucht hat, erlässt das Amtsgericht Haftbefehl wegen Fluchtgefahr. Am 9. Juli wird er festgenommen und vorgeführt; seitdem ist er in Untersuchungshaft und hat eine Pflichtverteidigerin.
>
> Herr Dengler zeigt ihn außerdem an: Im Mai sei aus seinem Hof ein E-Bike verschwunden. Als Beschuldigter vernommen, bestreitet Wittig; weitere Beweise gibt es nicht.
>
> Am 8. Oktober 2026 ist die Anklage zum Schöffengericht wegen des Einbruchs fertig.
>
> **Was gehört in die Begleitverfügung – ohne Widerspruch zur Anklage?**
