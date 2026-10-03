# Folge 121 · Verkehrszeichen als Verwaltungsakt: Kannst du ein Schild anfechten? – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_121.py`](src/skript_121.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Alltagsfall), fiktiver Fall nach dem Plan-Hook, Beispielland Nordrhein-Westfalen (kein Vorverfahren), offen gelegt. Über Nacht steht vor dem Haus von Frau Wittmann, die dort seit zwanzig Jahren parkt, ein dauerhaftes absolutes Haltverbot (Zeichen 283). Die Straßenverkehrsbehörde nennt nur „Sicherheit und Ordnung des Verkehrs“. Ablauf: Fall → Frage → Sachverhalt → 1. Rechtsnatur (Wortlaut § 35 S. 2 VwVfG, Dauerverwaltungsakt, Verweis 044) → 2. Bekanntgabe und Wirksamkeit (§ 43 I VwVfG, Aufstellen, Sichtbarkeitsgrundsatz nur als Verweis auf 064) → 3. Zulässigkeit (Rechtsweg, Anfechtungsklage, Klagebefugnis Art. 2 I GG, Vorverfahren NRW, Jahresfrist ab erster Begegnung, Klagegegner, keine aufschiebende Wirkung, Eilantrag) → 4. Begründetheit (§ 113 I 1 VwGO, Wortlaut § 45 I 1 StVO, formell, Wortlaut § 45 IX S. 1 und S. 3 StVO, ruhender Verkehr, zwingend erforderlich, Ermessen) → Subsumtion und Ergebnis (Klage begründet, Aufhebung, kein Bescheidungsurteil) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:31,9 (5.829 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Wittmann (WI), um 65 | Anwohnerin, Klägerin | Pose `standing/polka_dots` (Pullover mit Polka Dots, blaue Hose `#8DB3F2`), Kopf `Gray Bun`, Haut `#EFC9A8`; Mimiken `Calm` (ruhig), `Concerned|Serious` (Sorge; redet in A), `Rage|Serious` (Ärger; redet in B), `Suspicious` (denkt), `Driven` (entschlossen), `Smile` (froh beim Ergebnis) | `hilde` (Frau, älter) |
| Herr Buchholz (BU), um 45 | Straßenverkehrsbehörde der Stadt | Pose `standing/shirt-3` (türkisfarbenes Hemd, schwarze Hose), Kopf `Short 5`, Haut `#C98F6B`; Mimiken `Calm`, `Serious` (ernst, redet), `Suspicious` (denkt) | `stephan` (Mann, mittel) |
| Frau Wolter (WO), um 30 | Nachbarin | Pose `standing/walking-3` (schwarzes Shirt, schwarze Hose), Kopf `Medium Bangs`, Haut `#F2D3B8`; Mimik `Calm` (redet) | `lucy` (Frau, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Frau Wittmann blickt nach links zum Schild, Frau Wolter (links) nach rechts zu Schild und Nachbarin; Szene B: Frau Wittmann (links, Telefon) nach rechts, Herr Buchholz (rechts, Hörer) nach links; an Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WI_redet`, `WI_aerger_redet`, `BU_redet`, `WO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** hilde, stephan, lucy; `christian` nicht besetzt (klingt wie stephan). Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Wittmann, Buchholz, Wolter (nicht in der Liste früherer Namen).
- Figuren-PNGs: `../peeps/op_121/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 118 (Stadthalle, Rathaus), 119 (Täter/Teilnehmer) und 120 (Gesamtschuld) mit eigenen Schauplätzen; Posen dort `robot_dance-3`, `resting-1`, `crossed_arms-2`, `easing-2`, `blazer-3`, `pointing_finger-1`, `crossed_arms-1`, `walking-2`, `blazer-4`. Hier `polka_dots`, `shirt-3`, `walking-3` (Polka Dots in den letzten drei Folgen nicht verwendet). Schauplatz: Wohnstraße mit Haus und neuem Haltverbotsschild, Telefonat Haus/Amt im geteilten Bild. Der Abschleppfall (064) spielte vor einer Apotheke; hier geht es um die Klage gegen das Schild selbst, nicht ums Abschleppen. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Das neue Schild** `fall`–`wo1` | Wohnstraße, Haus; Frau Wittmann kommt aus dem Haus; früher ihr Auto vor dem Haus, heute das Schild; Nachbarin kommt vorbei; Blasen Wittmann, Wolter | tabler:`home` (Gelb), `car` (Rosa, nur „immer direkt vor dem Haus“), Zeichen 283 (stilisiert, s. u.) am Mast | `Fall · Das neue Schild` (ab 0,0 s) | Straße mit Haus · Wittmann · seit 20 Jahren · Auto · Pille · Schild · heute · absolutes Haltverbot · Blase · Wolter · Blase | Haustür (`szene_121tuer_1`), als Frau Wittmann aus dem Haus kommt |
| **B Der Anruf bei der Stadt** `amt`–`bu2` | geteiltes Bild: links Frau Wittmann mit Handy, rechts Herr Buchholz mit Hörer vor dem Amtsgebäude; drei Blasen | fluent-hc:`mobile-phone`, tabler:`phone`, `building` (Blau) | `Fall · Der Anruf bei der Stadt` | Wittmann · Buchholz · Behörde · Blase bu1 · Blase wi2 · Blase bu2 | – |
| **C Frage** `frage`/`frage2` | großes Schild, Frau Wittmann entschlossen | Zeichen 283 | `Fall · Kann man ein Schild anfechten?` | Schild · Frage · Erfolg? | – |
| **D Sachverhalt** `sv` | Karte vollständig, 9,8 s | – | `Sachverhalt` | 1 | – |
| **E Rechtsnatur** `natur`–`dauer` | Tafel, Wortlautkarte § 35 S. 2 (drei Marker), 3. Variante, Verweis 044, Block Dauer-VA | Zeichen 283 | `1. Rechtsnatur: …` → `… › Dauerverwaltungsakt` | Titel · ✓ · Karte · Marker · Zeilen · Block | – |
| **F Bekanntgabe und Wirksamkeit** `bekannt`–`wirksam` | § 43 I, ✗ Brief, ✗ ortsübliche Bekanntmachung, Aufstellen, Sichtbarkeit (Verweis 064), ✓ wirksam | tabler:`mail`, Zeichen 283, tabler:`eye` | `2. Bekanntgabe und Wirksamkeit: …` | Zeilen · ✗ · ✗ · Block | – |
| **G Zulässigkeit** `zul`–`befugt` | ✓ Rechtsweg, ✓ Anfechtungsklage, Klagebefugnis, Block Art. 2 I GG | tabler:`gavel` | `3. Zulässigkeit: …` → `… › Klagebefugnis` | Zeilen · ✓ · Block | – |
| **H Vorverfahren und Frist** `vorv`–`gegner` | NRW ohne Vorverfahren, andere Länder, Jahresfrist, Block erste Begegnung, ✗ kein Neubeginn, Klagegegner | tabler:`calendar`, `building` | `… › Vorverfahren: in NRW nicht nötig` → `… › Klagefrist` → `… › Klagegegner` | Zeilen · Block · ✗ | – |
| **I Aufschiebende Wirkung?** `aufsch`/`eil` | hellgelb, Warnsymbol, Block sofort vollziehbar, § 80 II 1 Nr. 2 analog, Eilantrag | Zeichen 283, tabler:`hourglass` | `… › keine aufschiebende Wirkung` | Zeilen · Block | – |
| **J Begründetheit** `begr`–`formell` | § 113 I 1, Wortlautkarte § 45 I 1 StVO (3 Marker), ✓ formell, ✓ Anhörung | tabler:`building` | `4. Begründetheit: …` → `… › Rechtsgrundlage` → `… › formell` | Zeilen · Karte · Marker · ✓ | – |
| **K § 45 IX StVO** `wl45`–`ruhend` | Wortlautkarte S. 1 und S. 3 (5 Marker), fließender Verkehr, Block ruhender Verkehr | Zeichen 283 | `… › § 45 IX StVO` → `… › qualifizierte Gefahrenlage` → `… › Haltverbot: ruhender Verkehr` | Karte · Marker · Zeile · Block | – |
| **L Satz 1: zwingend erforderlich** `zwingend`/`ermessen` | zartblaue Tafel: zurückhaltend, Ermessen, Verhältnismäßigkeit | Zeichen 283, tabler:`scale` | `… › zwingend erforderlich` → `… › Ermessen` | Zeilen | – |
| **M Und hier?** `hier`–`keinbesch` | pauschaler Grund, ✗ keine Umstände, Darlegung, Zeitpunkt, Block rechtswidrig, Block Klage begründet, kein Bescheidungsurteil | – | `… › Subsumtion` → `… › maßgeblicher Zeitpunkt` → `Ergebnis: Klage begründet` | Zeilen · ✗ · Blöcke | – |
| **N Klausurtipp** `tipp`/`tipp2` | Lexi warnt: Schild gilt bis zur Aufhebung (Bußgeld, Abschleppen, Verweis 064); Satz 3 nicht beim Haltverbot | Warnsymbol (Streamline Freehand) | `Klausurtipp · Das Schild gilt bis zur Aufhebung` | Zeilen | – |
| **O Klausurschema** `sch`–`q2d` | Schema baut sich auf | – | `Klausurschema` | Titel · I. · 1.–4. · II. · 1.–4. | – |
| **P Merksatz** `merke`/`m2` | Lexi erklärt, drei Marker | – | `Merksatz` | Zeilen · Marker | – |

**Zeichen 283:** stilisierte, korrekte Darstellung des amtlichen Zeichens (Auftrag): kreisrund, blauer Grund (Palette Blau), roter Rand und rotes Kreuz (Palette Dunkelrot), Tuschekontur; geometrisch gezeichnet wie `karte()`/`linienzug()` (`z283_bild()` in `folien_121.py`), keine fremde Bilddatei; Mast als Tuschelinie.
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Haustür), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Prüfpfad-Reihenfolge:** wie das Schema: 1. Rechtsnatur, 2. Bekanntgabe und Wirksamkeit, 3. Zulässigkeit, 4. Begründetheit, Ergebnis (im Schema sind 1. und 2. unter I.1 „Anfechtungsklage: Schild = Allgemeinverfügung“ zusammengefasst, wie gesprochen).

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Nordrhein-Westfalen: Frau Wittmann parkt seit 20 Jahren direkt vor ihrem Haus. Über Nacht lässt die Stadt dort ein dauerhaftes absolutes Haltverbot aufstellen (Zeichen 283), gut sichtbar. Frau Wittmann sieht es am nächsten Morgen zum ersten Mal. Auf ihre Nachfrage nennt Herr Buchholz von der Straßenverkehrsbehörde nur einen pauschalen Grund: „Sicherheit und Ordnung des Verkehrs“. Besondere Umstände an der Stelle nennt die Stadt auch später nicht. Frau Wittmann will gegen das Schild klagen.
>
> **Kann sie das Schild anfechten – und hat sie Erfolg?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen und Zahlen in Ziffern („§ 45 Abs. 9 Satz 1 StVO“, „1 Jahr“, „Folge 44“), gesprochen als Wörter. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Wortlautkarten (§ 35 Satz 2 VwVfG, § 45 Abs. 1 Satz 1 StVO, § 45 Abs. 9 Satz 1 und 3 StVO als Auszug mit „…“) sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe).
