# Folge 166 · Trierer Weinversteigerung: Erklärungsbewusstsein beim Winken? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_166.py`](src/skript_166.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall · BGB AT. Ablauf: Hook in der Versteigerung (Winken, Zuschlag, Widerspruch, Wortlaut § 156) → Frage → Klassiker (Lehrbuchfall 1899, BGH 1984 Sparkassen-Bürgschaft) → Sachverhalt → I. Tatbestand der Willenserklärung (objektiv mit Wortlautkarten §§ 133, 157; subjektiv: Handlungswille, Erklärungsbewusstsein, Geschäftswille) → II. Streit (Willenstheorie mit § 118 und § 122 analog; Gegenansicht; BGH-Formel wörtlich; Wahlrecht) → Subsumtion → III. Anfechtung (Wortlautkarten § 119 Abs. 1, § 121 Abs. 1 S. 1; Willensmangel erkennbar; Sparkasse 15 Tage zu spät) → § 142, Wortlautkarte § 122 → Lösung im Saal → Klausurtipp → Prüfschema → Merksatz. Skript 5.682 Zeichen, Hauptfilm 6:28,2.

**Status 04.10.2026:** vertont (5.661 Zeichen, 25 Segmente), gerendert und geprüft: Hauptfilm 6:28,2, 18 Folien, 121 eigenständige Bildhalte (Ergebnis in [`ABNAHME.md`](ABNAHME.md)). Gegenüber der Planung: Szene C1 in zwei Folien geteilt (Anspruch/Gliederung; §§ 133, 157 und Subsumtion), E2 ohne Figuren (nur Requisiten), Titel D1 „Ohne Erklärungsbewusstsein?“ (Breite).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ekkehard (EK), um 40 | Zuschauer, winkt seiner Freundin zu | `standing/resting-2` (Hand unten) und `standing/pointing_finger-2` (erhobene Hand) – beide „-2“-Reihe mit festem schwarzem Oberteil, Hose Blau `#8DB3F2`, Kopf `Short 1`, Haut `#E3B08A`, ohne Bart/Brille. Mimiken `Smile` (ruhig), `Concerned\|Serious` (redet/sorgt sich), `Suspicious` (denkt), `Cute` (froh/winkt), `Awe` (staunt, mit erhobener Hand beim Zuschlag) | `christian` (Mann, mittel) |
| Frau Haller (HA), um 60 | Auktionatorin, versteigert Fässer aus ihrem eigenen Weinkeller | `standing/blazer-3` (Blazer Türkis `#7FD6D0`, Hose `#4A4A58`), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#F0C8A8`. Mimiken `Smile` (ruhig/redet), `Suspicious`, `Cute`, `Serious` | `hilde` (Frau, älter) |
| Reinhild (RE), um 40 | Ekkehards Freundin an der Tür, spricht nicht | `standing/walking-1` (Oberteil Orange `#F9A66C`), Kopf `Long Curly` (Haar `#6B4226`), Haut `#C98E66`. Mimiken `Smile`, `Cute`, `Awe` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Frau Haller links am Pult blickt nach rechts in den Saal (`_r`); Ekkehard in der Mitte blickt zunächst zu ihr (links), entdeckt Reinhild und winkt nach rechts (`EK_winkt_r`), nach dem Zuschlag wieder zu Frau Haller (links); Reinhild rechts an der Tür blickt nach links zu ihm. Tafelszenen: alle nach links zur Tafel. Kontaktbild `out/besetzung_166.png` gesichtet.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `EK_redet`, `HA_redet` (je links/rechts) und Lexi. Reinhild spricht nicht.
- **Stimmen** nur aus dem Pool: hilde und christian; stephan nicht verwendet (keine Paarung stephan/christian), lucy nicht verwendet (Vorfolge 146).
- **Namen:** Ekkehard, Haller, Reinhild – eindeutig deutsch, nicht in der Liste vergebener Namen und in keinem Szenenplan/Skript/Abnahmebogen unter `youtube/preproduction` (Volltextsuche 04.10.2026; Hubert, Wilhelm, Gerhard, Anton, Gerold verworfen). Isay wird nur als Fundstelle gezeigt, nicht gesprochen.
- Figuren-PNGs: `../peeps/op_166/` (50 Dateien, nicht im Repository, im Drive-Master).
- **Statur:** `resting-2` und `pointing_finger-2` haben in der Bibliothek leicht verschiedene Körperformen und Schuhe; Oberteil, Hose, Kopf und Hautton sind gleich (Kombination derselben „-2“-Reihe nach MASTERSTANDARD-09 § 2). Bewusst so, weil keine Pose mit gesenkter Hand dieselbe Körperform hat.

**Abweichung von den letzten Folgen:** 162 (`easing-1`, `blazer-4`, `closed_legs-1`), 163 (`easing-1/-2`, `walking-3`, `robot_dance-2`), 164 (`shirt-3`, `blazer-4`), 146 (`resting-1`, `crossed_arms-1`) – hier `resting-2`, `pointing_finger-2`, `blazer-3`, `walking-1`; keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplatz **Versteigerungssaal mit Pult, Fass auf Gestell und Saaltür** – neu gegenüber 162–164 und 146.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte (Ziel) | Geräusch |
|---|---|---|---|---|---|
| **A1 Die Versteigerung** `fall`→`e1` | Saal: links Pult mit Frau Haller, daneben Fass auf Gestell mit Pille „Los: 1 Fass Riesling“; Mitte Ekkehard; rechts Saaltür. Pillen „Wer die Hand hebt, bietet.“ (`regel`), „Gebot: 850 €“ → „900 €?“ (Blase Haller), Reinhild erscheint an der Tür (`rein`), Ekkehard winkt (`wink`, Pose mit erhobener Hand), Blase Haller „900 € vom Herrn in der Mitte! / Zum Ersten, zum Zweiten, / und zugeschlagen!“, Hammer-Icon beim Wort „zugeschlagen“, Ekkehard staunt, dann redet (Blase „Moment! Ich habe nicht geboten. / Ich habe nur meiner Freundin zugewinkt!“) | tabler `podium`, `barrel`, `door`, `gavel` | `Fall · Die Weinversteigerung` (ab 0,0 s) → `Fall · Der Zuschlag` (`h2`) → `Fall · Der Widerspruch` (`e1`) | 12 | Hammerschlag beim Zuschlag (`szene_166hammer_1`, Freesound CC0 618138) |
| **A2 Die Frage** `p156`, `frage` | Tafel: **Wortlautkarte § 156 S. 1 BGB** (Marker „Zuschlag“), Pille „War das Winken ein Gebot?“; Ekkehard (denkt), Frau Haller (ernst) rechts | tabler `gavel` | `Die Frage · § 156 BGB: Vertrag durch Zuschlag` → `Die Frage · Gebot ohne Erklärungsbewusstsein?` | 3 | – |
| **A3 Der Klassiker** `klassiker`→`mitt` | Tafel ohne Figuren rechts nur Requisit: Block „Lehrbuchfall, 1899 – kein Gerichtsfall“ mit Fundstelle „H. Isay, Die Willenserklärung im Thatbestande des Rechtsgeschäfts, 1899, S. 25“; Block „BGH, Urt. v. 7.6.1984 – IX ZR 66/83, BGHZ 91, 324“; Brief-Pille „„… die selbstschuldnerische Bürgschaft … übernommen““ (Zitat Schreiben 8.9.1981), Pille „wollte nur mitteilen“ | tabler `book`, `building-bank`, `mail` | `Der Klassiker · Lehrbuchfall von 1899` → `Der Klassiker · BGH, 7.6.1984: die Sparkasse` | 5 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C1 Objektiver Tatbestand** `tb`→`objok` | Tafel: Anspruch „Frau Haller gegen Ekkehard: 900 €, § 433 Abs. 2 BGB“, Gliederung „objektiv / subjektiv“, **Wortlautkarten § 133 und § 157 BGB** (Marker „wirkliche Wille“, „Treu und Glauben“, „Verkehrssitte“), Zeile „erhobene Hand = Ich biete mehr“, Haken „objektiv: Gebot (+)“; Frau Haller und Ekkehard rechts | tabler `eye`, `hand-stop`→ (Hand-Icon) | `I. Willenserklärung · Anspruch auf 900 €` → `› objektiver Tatbestand` → `› §§ 133, 157 BGB` → `› objektiv: Gebot (+)` | 6 | – |
| **C2 Subjektiver Tatbestand** `st`→`frage2` | Tafel mit drei Zeilen: Handlungswille (Haken), Erklärungsbewusstsein (Kreuz bei „fehlt“), Geschäftswille (Kreuz); Pille „Willenserklärung ohne Erklärungsbewusstsein?“; Ekkehard allein (denkt → sorge) | – | `I. … › subjektiv: Handlungswille (+)` → `› Erklärungsbewusstsein (−)` → `› Geschäftswille (−)` → `› ohne Erklärungsbewusstsein?` | 6 | – |
| **D1 Der Streit** `wt`→`et2` | zwei Blöcke nebeneinander bzw. untereinander: „Willenstheorie: unverzichtbar – § 118 – allenfalls § 122 analog“ (Hellrot), „Gegenansicht: Schutz von Empfänger und Verkehr – zunächst wirksam, anfechtbar“ (Hellgrün); Fundstelle BGHZ 91, 324, 327 f.; beide Figuren | tabler `scale` | `II. Der Streit · Willenstheorie` → `› § 118 BGB` → `› Gegenansicht` | 5 | – |
| **D2 Die BGH-Formel** `bghz`→`pot` | **Zitatkarte Leitsatz BGHZ 91, 324** in Originalschreibung, Marker „hätte erkennen und vermeiden können“ (`formel`), „tatsächlich so verstanden“ (`verst`); Pille „potentielles Erklärungsbewusstsein“; Fundstelle „bestätigt: BGH, 14.2.2023 – XI ZR 537/21, Rn. 29“ | tabler `building-bank` | `II. … › BGH: Zurechnung` → `› Empfänger hat so verstanden` → `› potentielles Erklärungsbewusstsein` | 4 | – |
| **D3 Die Wahl** `wahl`→`p118` | Schaubild: Ekkehard → zwei Pfeile: „anfechten → Vertrauensschaden ersetzen“ / „festhalten → Gegenleistung“; Zeile „§ 118 passt nicht: bewusst keine Bindung“ (BGHZ 91, 324, 329 f.) | tabler `arrows-split` | `II. … › Wahlrecht des Erklärenden` → `› § 118 passt nicht` | 4 | – |
| **D4 Subsumtion** `sub`→`kv` | Tafel mit zwei Haken (erkennbar/vermeidbar; Frau Haller hat so verstanden), grüner Block „Willenserklärung (+) – Kaufvertrag mit dem Zuschlag“; beide Figuren | tabler `gavel` | `II. … › Ekkehard: erkennbar` → `› Frau Haller: so verstanden` → `› Kaufvertrag (+)` | 4 | – |
| **E1 Anfechtung § 119** `anf`→`analog` | **Wortlautkarte § 119 Abs. 1 (Auszug)**, Marker „überhaupt nicht abgeben wollte“; Zeile BGH 329; Pille „Anfechtung analog § 119 BGB“ (Fundstelle V ZB 9/13 Rn. 9); Ekkehard allein (froh) | – | `III. Anfechtung · § 119 Abs. 1 BGB` → `› BGH: auch ohne Erklärungsbewusstsein` → `› analog § 119 BGB` | 4 | – |
| **E2 Unverzüglich, Willensmangel** `p121`→`tage` | **Wortlautkarte § 121 Abs. 1 S. 1** (Marker „unverzüglich“), Zeile „Willensmangel muss erkennbar sein“ (BGHZ 91, 324, 331 f.), Block Sparkasse: „24.9.1981: nur bestritten“ (Kreuz), „6.10.1981: 15 Tage nach Kenntnis – zu spät“ (Kreuz) | tabler `calendar`, `mail` | `III. … › § 121: unverzüglich` → `› Willensmangel erkennbar` → `› Sparkasse: zu spät` | 5 | – |
| **E3 Folgen** `eok`→`deckel` | Haken „Ekkehard: sofort, mit Grund“; Zeile „§ 142 Abs. 1: von Anfang an nichtig“; **Wortlautkarte § 122 Abs. 1 (Auszug)** mit Markern „auf die Gültigkeit … vertraut“, „nicht über den Betrag des Interesses“; Pille „z. B. Kosten des erneuten Ausbietens“; beide Figuren | tabler `barrel` | `III. … › Anfechtung wirksam` → `› § 142: nichtig` → `› § 122: Vertrauensschaden` → `› höchstens das Erfüllungsinteresse` | 6 | – |
| **F Lösung im Saal** `loes`→`loes3` | Schauplatz A1 (die Geschichte kehrt in den Saal zurück): Prüfliste mit Haken auf einer Karte über dem Fass, Pillen „keine 900 €“, „Vertrauensschaden“; Ekkehard froh, Frau Haller denkt | wie A1 | `Lösung · Willenserklärung (+)` → `· angefochten` → `· Vertrauensschaden` | 4 | – |
| **G Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Prüfungsort: subjektiver Tatbestand` → `Klausurtipp · erst dann die Anfechtung` | 4 | – |
| **H Prüfschema** `sch`→`k6` | breite Karte, Zeilen zum Wort (I. Kaufvertrag: Gebot und Zuschlag, § 156 – objektiv – subjektiv – potentielles Erklärungsbewusstsein; II. Nichtigkeit, § 142 I, Anfechtung analog § 119 I, § 121; III. § 122) | – | `Prüfschema` → je Gliederungspunkt | 7 | – |
| **I Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker („zurechnen“, „Vertrauensschaden“) | – | `Merksatz` | 3 | – |

Summe Ziel ≈ 83 Bildhalte (Soll bei ≈ 6:30 rund 59).

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausschließen wie in 146), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („900 €“, „§ 156“, „7.6.1984“, „1899“).
**Übergänge:** stumme Schiebeblenden nur zwischen den Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Reinhild kommt an die Tür (≈ 1,0 s).
**Geräusch:** ein Handlungsgeräusch (Hammerschlag beim Zuschlag, sichtbares Hammer-Icon). Freesound CC0 als `sfx3/szene_166hammer_1.wav`, Herkunft in `geraeusche_herkunft.json`; sonst stumm.
**Wein:** nur Fass-Icon (tabler `barrel`), keine Gläser, niemand trinkt; keine echten Weingüter oder Auktionshäuser; keine Kinder.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Auktionatorin Frau Haller versteigert Fässer aus ihrem eigenen Weinkeller. Im Saal gilt: Wer die Hand hebt, bietet. Für ein Fass Riesling sind 850 € geboten. Ekkehard ist nur zum Zusehen mitgekommen. Als er an der Tür seine Freundin Reinhild entdeckt, hebt er die Hand, um ihr zuzuwinken.
>
> Frau Haller hält das für ein Gebot über 900 € und erteilt Ekkehard den Zuschlag. Sofort ruft er: „Moment! Ich habe nicht geboten. Ich habe nur meiner Freundin zugewinkt!“ Frau Haller verlangt 900 €.
>
> **Muss Ekkehard zahlen?**

Kein Fiktiv-Hinweis; beim BGH-Fall stehen Gericht, Datum und Aktenzeichen auf der Tafel.
