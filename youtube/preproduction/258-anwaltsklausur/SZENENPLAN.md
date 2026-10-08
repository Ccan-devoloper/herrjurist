# Folge 258 · Anwaltsklausur Aufbau: Gutachten, Zweckmäßigkeit, Schriftsatz – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_258.py`](src/skript_258.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · Klausurtechnik, Format Schema, ohne vollständige Fallprüfung. Beispielfall nach dem Plan-Hook („Die Mandantin will nicht wissen, wer recht hat, sondern was sie jetzt konkret tun soll“): Frau Steinhoff hat einem Gartenbaubetrieb 3.000 € für eine Terrasse angezahlt, fertig sein sollte sie Ende April (E-Mail), passiert ist nichts. In der Kanzlei: Referendarin Isolde und ihr Ausbilder Rechtsanwalt Hohlfeld.
Ablauf nach Auftrag: 1. Hook (Fall, Frage) → Sachverhalt → 2. Perspektivwechsel (parteiisch, aber gebunden; § 43a Abs. 3 BRAO, § 43a Abs. 4/5 BRAO als Wortlautkarten) → 3. Aufbau: vorweg Mandantenbegehren, I. Gutachten (§ 323 Abs. 1 BGB als Wortlautkarte, § 346 BGB, Amtsgericht), II. Zweckmäßigkeit, III. Praktischer Teil (je nach Bearbeitervermerk, Verweis 222) → 4. echte Zweckmäßigkeit vs. zweites Gutachten (Tafel Zeit, Kosten, Beweisbarkeit, Vergleich, Eilrechtsschutz, sicherster Weg) → Ergebnis in der Kanzlei → 5. Kurzblick Zivil (§ 253 Abs. 2 ZPO), Öffentliches Recht (§ 81 Abs. 1 S. 1 VwGO), Strafrecht (§ 137 Abs. 1 S. 1 StPO, Verweis 039) → 6. Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:34,5 (5.545 vertonte Zeichen, davon 82 nachvertont). Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Isolde (IS), Mitte 20 | Referendarin in der Anwaltsstation, durchgehende Figur | Pose `standing/pointing_finger-2` (schwarzes Oberteil, hellblaue Hose `#8DB3F2`, schwarze Schuhe, erhobener Zeigefinger), Kopf `Medium Bangs` (schwarzes Haar), Haut `#F1C9A5`; Mimiken `Calm`, `Suspicious` (denkt), `Driven` (schreibt), `Serious` (liest, redet), `Smile` (froh) | `lucy` (Frau, jung) |
| Frau Steinhoff (ST), um 70 | Mandantin | Pose `standing/crossed_arms-2` (schwarzes Oberteil, lila Hose `#B8A9F5`, verschränkte Arme), Kopf `Gray Medium` (Haar `#C8C8C8`), Brille `Glasses 4`, Haut `#EDC3A0`; `Calm`, `Concerned\|Serious` (Sorge, redet), `Very Angry` (Ärger), `Smile` (froh, redet froh) | `hilde` (Frau, älter) |
| Herr Hohlfeld (HO), um 55 | Rechtsanwalt, Ausbilder | Pose `standing/blazer-3` (Sakko graublau `#5B6B8C` über schwarzem Shirt, Hose `#3D3D48`, Hand an der Hüfte), Kopf `Short 2` (dunkles Haar), Brille `Glasses 2`, Haut `#DDA882`; `Calm`, `Suspicious`, `Serious` (redet), `Smile` (froh, redet froh) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts. Grundansicht gespiegelt = blickt nach links, `_r` = nach rechts. Kanzlei: Frau Steinhoff links blickt nach rechts zu Isolde und Herrn Hohlfeld, beide blicken nach links zu ihr. Perspektivwechsel: Frau Steinhoff (links) blickt zu Isolde, Isolde nach links zu ihr und zur Tafel. Übrige Tafelszenen: Figuren blicken nach links zur Tafel. Kontaktbild `out/besetzung_258.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `IS_redet`, `ST_redet`, `ST_redetfroh`, `HO_redet`, `HO_redetfroh` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur. Der Gartenbaubetrieb erscheint nicht als Figur (nur erwähnt), deshalb kein Icon-Gesicht als Mensch.
- **Stimmen nur aus dem Pool** stephan, hilde, christian, lucy; christian nicht verwendet (damit nie stephan und christian in einer Szene).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, `rg -w` unter `youtube/` 0 Treffer (Isolde, Steinhoff, Hohlfeld); verworfen: Ida (in 173/249/254 wegen englischer Lesart verworfen), Birte (Verwechslung mit „bitte“, 123/157/233), Gesche (zu nah an Gesa/Gesine), Kiefer (1 Treffer in 246). Eingetragen als „258: Isolde, Steinhoff, Hohlfeld“ vor der Vertonung. Kein Genitiv eines Namens.
- Präfixe `IS_`/`ST_`/`HO_`/`LX_` (nie `ER_`). Figuren-PNGs: `../peeps/op_258/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 253–256 verglichen): 253 (`crossed_arms-1`), 254 (`resting-1`, `shirt-3`, `Blazer Black Tee`, `walking-1`), 255 (`robot_dance-3`, `blazer-4`), 256 (parallel: `easing-2`, `walking-3`, `resting-2`). 258: `pointing_finger-2`, `crossed_arms-2`, `blazer-3` – dort nicht verwendet; Farben (hellblaue Hose, lila Hose, graublaues Sakko) und Köpfe neu gegenüber 253–255. Schauplatz: **Besprechungszimmer einer Kanzlei** mit Fenster, Wandregal, Pflanze und Schreibtisch (Kanzleien gab es u. a. in 066, 078, 090 – dort mit Aktentasche/Schriftsatz am Schreibtisch des Verteidigers; hier ein Mandantengespräch zu dritt mit Kontoauszug und Rückblick-Karte „im Garten“). Rückkehr in die Kanzlei in Szene H, weil die Beratung dort schließt. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Kanzlei** `fall`→`frage2` | Besprechungszimmer; Frau Steinhoff ab 0,0 s, legt den Kontoauszug auf den Tisch (Fall 0,35 s); Isolde und Herr Hohlfeld treten bei ihrer Nennung auf; Rückblick-Karte „im Garten“ während Frau Steinhoff spricht; Hook und Frage als Pillen | tabler:`window`, `books`, `plant-2`, `desk`, `receipt-euro`, `fence`, `calendar-x`; Regal programmatisch | `Fall · In der Kanzlei` → `Fall · Was soll ich jetzt tun?` → `Einstieg · Die Frage` | 16 | Kontoauszug auf den Tisch (`szene_258auszug_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C1 Perspektivwechsel** `pers`→`is1` | Tafel Richter/Anwalt, Pillen „parteiisch“/„aber nicht grenzenlos“; Blasen Frau Steinhoff („Betrüger“) und Isolde (sachlich, wahr) mit Haken | – | `Perspektivwechsel · Richter oder Anwalt` → `› parteiisch, aber gebunden` | 9 | – |
| **C2 § 43a Abs. 3 BRAO** `w43`→`herab` | Wortlautkarte, drei Marker, drei Haken-Zeilen | tabler:`scale` | `§ 43a Abs. 3 BRAO › Sachlichkeit` | 7 | – |
| **C3 § 43a Abs. 4/5 BRAO** `abs4`→`abs5` | zwei Wortlautkarten, Marker, Pille „auch für Referendare …“ | tabler:`users`, `school` | `§ 43a Abs. 4 BRAO › widerstreitende Interessen` → `§ 43a Abs. 5 BRAO › auch für Referendare` | 7 | – |
| **D Aufbau** `auf`→`f222` | Tafel: 3 Stufen + 1 Frage, Mandantenbegehren, Stufen I.–III. als Treppe, Bearbeitervermerk, Verweis 222; Frau Steinhoff und Isolde | – | `Aufbau · in der Regel drei Stufen` → `› vorweg: das Mandantenbegehren` → `› I. Gutachten, II. Zweckmäßigkeit, III. Praktischer Teil` → `› der Bearbeitervermerk entscheidet` | 13 | – |
| **E I. Gutachten** `gut`→`vorb` | § 346, Wortlautkarte § 323 Abs. 1 BGB (Marker), Kreuz „noch keine Frist“, Amtsgericht (§ 23 Nr. 1 GVG), „bereitet die Maßnahme vor“ | tabler:`coin-euro`, `hourglass`, `building-bank` | `I. Gutachten › materiell: Rücktritt` → `› prozessual` → `› bereitet die Maßnahme vor` | 12 | – |
| **F II. Zweckmäßigkeit** `zw`→`vor` | zwei Spalten: zweites Gutachten (Kreuz) / echte Zweckmäßigkeit (sicher, schnell, kostengünstig, Haken); „Sicherheit geht vor“ | tabler:`alert-triangle`, `route` | `II. Zweckmäßigkeit › kein zweites Gutachten` → `› sicher, schnell, kostengünstig` | 12 | – |
| **G Zweckmäßigkeit am Fall** `t1`→`t7` | Tabelle Zeit/Kosten (§ 91 Abs. 1 ZPO)/Beweisbarkeit (Haken)/Vergleich/Eilrechtsschutz (§ 917 Abs. 1 ZPO, Kreuz)/sicherster Weg, Pillen Fallbezug | tabler:`clock`, `coin-euro`, `receipt-euro`, ph:`handshake`, tabler:`lock`, `route` | `II. Zweckmäßigkeit › Zeit` … `› der sicherste Weg` → `› Fallbezug statt zweitem Gutachten` | 14 | – |
| **H Ergebnis** `is2`→`ho2` | zurück in der Kanzlei; Fristschreiben auf dem Tisch; Blasen Isolde, Frau Steinhoff („Endlich ein Plan.“), Herr Hohlfeld | tabler:`mail` | `Ergebnis · der Plan für Frau Steinhoff` | 5 | – |
| **I III. Praktischer Teil** `prak`→`pf3` | drei Formen je nach Bearbeitervermerk; zwei Schreiben bei Frau Steinhoff; Hinweis im Brief | tabler:`file-text`, `mail`, `file-pencil`, `file-description`, `mail-opened` | `III. Praktischer Teil › je nach Bearbeitervermerk` → `› bei Frau Steinhoff` | 10 | – |
| **J1 Zivilrecht** `drei`→`zr` | Wortlautkarte § 253 Abs. 2 ZPO mit fünf Markern | tabler:`list-check`, `file-text` | `Kurzblick · alle drei Rechtsgebiete` → `› Zivilrecht: Klageschrift, § 253 ZPO` | 8 | – |
| **J2 Öffentliches Recht** `oer` | Pillen Widerspruch/Klage/Eilantrag, Wortlautkarte § 81 Abs. 1 S. 1 VwGO | tabler:`building-bank` | `Kurzblick › Öffentliches Recht: § 81 VwGO` | 6 | – |
| **J3 Strafrecht** `sr`→`f39` | Wortlautkarte § 137 Abs. 1 S. 1 StPO, Revisionsklausur, Verweis 39 | tabler:`briefcase`, `file-search` | `Kurzblick › Strafrecht: Verteidiger, § 137 StPO` → `› Revisionsklausur` | 6 | – |
| **K Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand), tabler:`hourglass`, `equal` | `Klausurtipp · Zeit für den praktischen Teil` | 6 | – |
| **L Schema** `sch`→`k3a` | breite Karte, Vorweg + I.–III. Punkt für Punkt | – | `Schema · Anwaltsklausur` → `› vorweg …` → `› I.` → `› II.` → `› III.` | 9 | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt, vier Marker | – | `Merksatz` | 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; einzige Bewegung: Kontoauszug fällt 0,35 s auf den Tisch; kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Kontoauszug auf den Tisch). Freesound-API am 08.10.2026 über den Proxy gesperrt (HTTP 403) → vorhandene CC0-Datei aus `sfx3/` unter eigenem Namen kopiert, Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Steinhoff hat einem Gartenbaubetrieb für eine neue Terrasse 3.000 € angezahlt. Fertig sein sollte die Terrasse Ende April; das steht in einer E-Mail. Die Zahlung belegt ihr Kontoauszug. Passiert ist nichts. Eine Frist hat sie dem Betrieb noch nicht gesetzt.
>
> In der Kanzlei sagt sie: „Ich will mein Geld zurück. Was soll ich jetzt tun?“ Rechtsanwalt Hohlfeld zur Referendarin: „Sie schreiben das Gutachten, Isolde. Und am Ende steht ein Vorschlag, was wir tun.“
>
> **Wie baust du die Anwaltsklausur auf, und was ist echte Zweckmäßigkeit statt eines zweiten Gutachtens?**
