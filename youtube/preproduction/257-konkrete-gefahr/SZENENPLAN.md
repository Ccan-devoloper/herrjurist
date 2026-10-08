# Folge 257 · Konkrete Gefahr: Wie wahrscheinlich muss der Schaden sein? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_257.py`](src/skript_257.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Polizei- und Ordnungsrecht · Schema. Beispielfall nach dem **entschärften** Plan-Hook (Mehrfamilienhaus statt Flüchtlingsunterkunft): Samstagnachmittag, Herr Fichtner steht mit einem offenen Benzinkanister am Hauseingang und raucht; Nachbar Sebastian ruft die Polizei; Polizistin Eilers riecht Benzin und fordert ihn auf, die Zigarette auszumachen und den Kanister zu schließen. **Kein Feuer, keine Flamme, keine Explosion**; Herr Fichtner ist ein freundlicher, sorgloser älterer Hausbewohner (kein Klischee). Ablauf: Fall → Frage → Sachverhalt → Generalklausel (Wortlautkarte § 8 Abs. 1 PolG NRW; Schutzgüter Verweis 213) → Legaldefinition (Wortlautkarte § 2 Nr. 1 NPOG; BVerfGE 141, 220 Rn. 111) → 1.–3. Merkmale am Fall → 4. Je-desto-Formel (Zitatkarte BVerwG 3 C 16.11 Rn. 32) → am Fall und Grenze (Zitatkarte BVerfGE 115, 320 Rn. 136) → 5. Prognose ex ante (Anscheinsgefahr ein Satz, Verweis 052) → Ergebnis → Abgrenzung gegenwärtig/erheblich/dringend/abstrakt (§ 2 NPOG) → Gegenfall und abstrakte Gefahr (BVerwG 6 C 44.16 Rn. 23) → Länder-Overlay → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:35,4 (5.703 Zeichen Skript, 5.683 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Fichtner (FI), um 60 | Hausbewohner mit Benzinkanister, will den Rasenmäher auftanken | Pose `standing/shirt-4` (schwarzes Hemd, Hose Beige `#B89A72`), Kopf `No Hair 3` (grauer Haarkranz `#BDBDBD`), Haut `#EBC29E`, kein Bart; Mimiken `Calm`, `Smile` (sorglos), `Suspicious`, `Concerned\|Serious`, `Solemn`; redet mit `Calm` | `helmut` (Mann, älter) |
| Polizistin Eilers (EI), um 30 | Polizei (Streife), sachlich und höflich („bitte“) | Pose `standing/easing-1` (Jacke Dunkelblau `#2F3E6B` über hellblauem Shirt `#8DB3F2`, schwarze Hose; uniformähnlich ohne Abzeichen, Wappen oder Waffe), Kopf `Medium 2`, Haut `#D9A07A`; `Calm`, `Serious`, `Suspicious`, `Smile`, `Driven`; redet mit `Serious` | `julia` (Frau, jung) |
| Sebastian (SE), um 25 | Nachbar, ruft die Polizei | Pose `standing/robot_dance-2` (schwarzes Oberteil, Hose Schiefergrau `#3D4A5C`; ausgestreckte Hand mit Handy), Kopf `Medium 1`, Haut `#F2D0B4`; `Calm`, `Concerned\|Serious`, `Suspicious`; redet mit `Concerned\|Serious` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. Fall: Herr Fichtner (links, vor dem Haus) blickt nach rechts zu Eilers und Sebastian; Eilers und Sebastian blicken nach links zu ihm. An den Tafeln blicken alle nach links. Gegenfall: Fichtner auf der rechten Seite blickt nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `FI_redet`, `EI_redet`, `SE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Polka Dots, keine Prothesen-Posen.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt` und in keiner Datei unter `youtube/` (grep über *.py, *.md, *.csv, *.json, *.txt am 08.10.2026: Fichtner, Eilers, Sebastian je 0 Treffer; „Jonas“ wegen 34 Treffern und „Hecht“ wegen des Gleichklangs mit „Fichtner“ verworfen), vor der Vertonung als „257: Fichtner, Eilers, Sebastian“ eingetragen. Kein Name im Genitiv.
- **Stimmen nur aus dem Pool:** helmut, julia, niklas; `ela_froh` nicht verwendet (fröhliche Stimme passt zu keiner Rolle). Erzählerin/Lexi Carla ohne Rolle.
- Figuren-PNGs: `../peeps/op_257/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 254 (`resting-1`, `shirt-3`, `walking-1`), 255 (`robot_dance-3`, `blazer-4`), 256 (`easing-2`, `walking-3`, `resting-2`) und Parallelfolge 258 (`pointing_finger-2`, `crossed_arms-2`, `blazer-3`) – in 257 keine dieser Posen; Kleidung ohne Muster. Schauplatz neu: **Mehrfamilienhaus mit Gehweg bei Tag** (Fassade mit neun Fensterfeldern, Haustür), Streifenwagen (Tabler `car`). Gegenüber 213 (Wohnstraße mit Garage; dort ebenfalls `easing-1` für die Polizei, hier mit anderen Farben und anderem Kopf) und 052 (Mietshaus innen, Nacht) eigener Ort; die Rückkehr zum Haus im Gegenfall ist gewollt (gleicher Ort, veränderte Lage).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Mehrfamilienhaus** `fall`–`frage2` | Haus links, Gehweg; Fichtner (ab „Herr“) mit Kanister, Pille „Deckel offen“ mit Ring, Zigarette mit Rauch und Pille „raucht“; Sebastian mit Handy, Blase; Streifenwagen und Eilers (Pille „Polizei“), Pille „Es riecht nach Benzin.“; Blasen Eilers und Fichtner, Rasenmäher bei „Rasenmäher“; zwei Fragepillen | ph:`gas-can` (Rot), ph:`cigarette` (Weiß), tabler:`car` (Blau), `lawn-mower` (Grün), `sun` (Gelb); fluent-hc:`mobile-phone`; Haus und Gehweg programmatisch | `Fall · Samstagnachmittag vor dem Haus` (ab 0,0 s) → … → `Fall · Die Frage` (11 Stände) | ≈ 20 | Autotür (`szene_257tuer_1`) beim Erscheinen des Streifenwagens („Kurz darauf …“) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | 1 | – |
| **C Ermächtigungsgrundlage** `egl`–`kern` | ✗ keine Standardmaßnahme, ✓ Generalklausel, Landesrecht/Dogmatik, **Wortlautkarte § 8 Abs. 1 PolG NRW** (3 Marker), Verweis 213, Block Kernfrage; Eilers, Fichtner | ph:`cigarette`, tabler:`map-2`, `book`, `shield`, ph:`gas-can` | `Ermächtigungsgrundlage · …` (5) → `Konkrete Gefahr · die Kernfrage` | ≈ 12 | – |
| **D Legaldefinition** `def`–`bverfg` | **Wortlautkarte § 2 Nr. 1 NPOG** (5 Marker zum Wort), BVerfG-Zeilen mit Rn. 111 | tabler:`book`, `clock`, `building-bank`, ph:`gas-can`, `building-apartment` | `Konkrete Gefahr › …` (6) | ≈ 9 | – |
| **E Merkmale am Fall** `e1`–`e3` | 1.–3. mit Haken, Ausblick „4. hinreichende Wahrscheinlichkeit?“ | ph:`gas-can`, `building-apartment`, tabler:`clock` | `Konkrete Gefahr › 1. … › 3.` | ≈ 9 | – |
| **F Je-desto-Formel** `jd`–`jdk` | **Zitatkarte BVerwG 3 C 16.11 Rn. 32** (2 Marker), Balken „großer Schaden“ / „kleiner Schaden“ | tabler:`scale` | `… › 4. hinreichende Wahrscheinlichkeit › …` (3) | ≈ 7 | – |
| **G Am Fall, Grenze** `jdfall`–`grenze` | ✓ sehr großer Schaden, Tatsachenzeile, ✓ ernsthaft möglich, roter Block Grenze, **Zitatkarte BVerfGE 115, 320 Rn. 136** (2 Marker) | ph:`building-apartment`, `cigarette`, tabler:`alert-triangle` | `… › am Fall …` → `… › Grenze …` | ≈ 8 | – |
| **H Prognose ex ante** `exante`–`wasser` | Zeitpunkt, Amtswalter (Fundstellen), Tatsachen statt Vermutungen (Rn. 145), drei Haken zu Eilers’ Wahrnehmung, gelber Block Anscheinsgefahr/Folge 052 | tabler:`clock`, `list-check`, `droplet`, ph:`gas-can` | `Konkrete Gefahr › 5. Prognose ex ante › …` → `Anscheinsgefahr · Folge 052` | ≈ 12 | – |
| **I Ergebnis** `erg`–`darf` | grüner Block „konkrete Gefahr (+)“, ✓ Verursacher (§ 4 I), ✓ mildes Mittel (§ 2 I), gelber Block | tabler:`shield`, ph:`cigarette`, `cigarette-slash`, `gas-can` | `Ergebnis · …` (4) | ≈ 8 | – |
| **J Abgrenzung** `abgr`–`abgen` | vier farbige Begriffspillen mit Definition (§ 2 Nr. 2, 3, 4, 6 NPOG), ✓ am Fall erheblich, Zeile gegenwärtig | tabler:`list-details`, `clock`, `heart`, `alert-triangle`, `users`, `book` | `Abgrenzung › …` (7) | ≈ 11 | – |
| **K Gegenfall** `gegen`–`gabs2` | Rückkehr vor das Haus: Auto mit Kanister im Kofferraum, Fichtner raucht weit entfernt; ✗ keine konkrete Gefahr; Karte abstrakte Gefahr mit Fundstellen | tabler:`car`, `sun`, ph:`gas-can`, `cigarette` | `Gegenfall · …` (3) → `Abgrenzung › abstrakte Gefahr …` (2) | ≈ 10 | – (keine sichtbare Handlung mit Geräusch) |
| **L Länder-Overlay** `tab`–`tdein` | Tabelle Land/Generalklausel/Gefahrbegriff (NRW, Brandenburg, Niedersachsen, Sachsen), Hinweisblock, Portal-Fundstelle | – | `Länder-Overlay · …` (6) | 6 | – |
| **M Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (4) | ≈ 7 | – |
| **N Schema** `sch`–`s6` | breite Karte 1.–5. und „Danach“ | – | `Schema › …` (7) | 7 | – |
| **O Merksatz** `merke`, `m2` | Lexi erklärt (redet), fünf Marker | – | `Merksatz` | ≈ 7 | – |

**Blasen:** Stil C (Standard seit 02.10.2026; Assertion gegen stillen Rückfall auf Stil e). **Zahlen** auf Tafeln und Pillen in Ziffern („§ 8 Abs. 1“, „Folge 213“, „Folge 052“, „Rn. 32“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Autotür, Freesound CC0 629315); Freesound-API am 08.10.2026 über den Proxy HTTP 403, daher unveränderte Kopie der Datei aus Folge 213 unter eigenem Namen, Herkunft in `geraeusche_herkunft.json`. Kein Feuerzeug-, Flammen- oder Explosionsgeräusch.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor Icons (MIT: gas-can, cigarette, cigarette-slash, building-apartment), Fluent Emoji High Contrast (MIT: mobile-phone; Haken/Kreuz), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Haus, Gehweg, Balken programmatisch.
**Prüfpfad-Reihenfolge:** wie das Schema: 1. Sachlage im Einzelfall, 2. Schaden für ein Schutzgut, 3. in absehbarer Zeit, 4. hinreichende Wahrscheinlichkeit (Je-desto), 5. Prognose ex ante; danach besondere Gefahrbegriffe.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Nordrhein-Westfalen, Samstagnachmittag: Herr Fichtner steht mit einem Benzinkanister am Eingang eines Mehrfamilienhauses. Der Deckel ist offen, es riecht nach Benzin, und er raucht direkt neben dem Kanister. Sein Nachbar Sebastian ruft die Polizei.
>
> Polizistin Eilers fordert Herrn Fichtner auf, sofort die Zigarette auszumachen und den Kanister zu schließen. Er antwortet: „Ich will doch nur den Rasenmäher auftanken. Da passiert schon nichts.“
>
> **Durfte Polizistin Eilers das verlangen? Liegt eine konkrete Gefahr vor?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Wortlautkarten (§ 8 Abs. 1 PolG NRW, § 2 Nr. 1 NPOG) und Zitatkarten (BVerwG 3 C 16.11 Rn. 32, BVerfGE 115, 320 Rn. 136) sind als Zitat gekennzeichnet (Anführungszeichen, Fundstelle); die BVerfG-Zitatkarte steht wörtlich, gesprochen wird sie leicht verkürzt („Beeinträchtigung“). Die Abgrenzungstafel gibt die Definitionen des § 2 NPOG gekürzt wieder, so wie sie gesprochen werden.
