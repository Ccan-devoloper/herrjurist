# Folge 201 · Lernplan Examen: So teilst du 12 Monate Vorbereitung ein – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_201.py`](src/skript_201.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Lernen, Format „Schritte“, ohne Normprüfung. Rahmen nach dem Plan-Hook („Examen in einem Jahr – womit fängst du an?“): Die Jurastudentin Fenna steht in der WG-Küche vor einem leeren Wandkalender; Nils, der das Examen im letzten Jahr geschrieben hat, plant mit ihr rückwärts. Sechs Schritte mit einer **12-Monats-Tafel** (12 Monatsspalten, Bahnen Stoff/Wiederholung/Klausuren, Zahlen als Ziffern), die von Schritt 2 bis 6 Stück für Stück wächst: 1. Bestandsaufnahme (Wortlautkarte § 5a Abs. 2 S. 3 DRiG, Landesrecht am Beispiel NRW, Ampel) → 2. rückwärts planen (Freiversuch, Endspurt, Puffermonat, 9 Monate Stoff) → 3. Stoffphase (Gewichtung als Empfehlung) → 4. Wiederholung (Faustregel, Verweis 123) → 5. Klausuren von Anfang an (Verweise 045, 117) → 6. Puffer, Pausen, Endspurt → Beispielwoche (Wochenplan als Tafel) → Ergebnis (Plan hängt an der Wand) → Klausurtipp (Lexi) → Lernplan I.–VI. → Merksatz (Lexi).
**Länge:** Hauptfilm 6:06,1 (5.086 vertonte Zeichen), Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Fenna (FE), Mitte 20 | Jurastudentin in NRW, ein Jahr vor den Klausuren | Pose `standing/pointing_finger-2` (schwarzes Oberteil, Hose Türkis `#7FD6D0`, schwarze Schuhe, Zeigefinger erhoben – sie plant), Kopf `Medium Straight` (dunkles Haar), keine Brille, Haut `#F0C8A8`; Mimiken `Concerned\|Serious` (ratlos, redet f1), `Suspicious` (denkt), `Calm`, `Smile`, `Smile Big\|Smile` (stolz), `Driven` (entschlossen), `Serious` (fragt f2), `Smile` (redet froh f3) | `lucy` (Frau, jung) |
| Nils (NI), um 28 | Referendar, Examen im letzten Jahr | Pose `standing/blazer-4` (Sakko Blau `#8DB3F2` über weißem Shirt, dunkle Hose, Hand an der Hüfte), Kopf `Short 3`, kein Bart, Haut `#D9A47E`; Mimiken `Calm`, `Smile`, `Serious`, `Smile` (redet n1), `Calm` (redet n2, n3) | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Beide Posen blicken im Original nach rechts (Kontaktbild `out/besetzung_201.png`: Gesicht links vom Hinterkopf in der gespiegelten Grundansicht). Grundansicht gespiegelt = blickt nach links (Fenna zum Wandkalender, Nils zu Fenna, alle Tafelszenen), `_r` = blickt nach rechts (Fenna zu Nils ab „Mit dem Ende“ und im Ergebnis).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `FE_redet`, `FE_fragt`, `FE_redetfroh`, `NI_redet`, `NI_redet2` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur, kein Klischee (Fenna weder überfordert-hysterisch noch Streberin; Nils kein Besserwisser, er erzählt von schwachen ersten Klausuren).
- **Stimmen nur aus dem Pool** hilde, christian, lucy, stephan: `lucy` (Fenna, einzige junge Frauenstimme im Pool; auch in 200 besetzt, unvermeidbar), `christian` (Nils; `stephan` aus der Vorfolge 200 vermieden). Keine Stephan/Christian-Paarung. `hilde` ohne Rolle.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Datei unter `youtube/` (Volltextsuche 06.10.2026: Fenna 0, Nils 0 Treffer; verworfen: Henrike, Jannik, Wiebke, Greta, Hendrik – schon vergeben). Kein Genitiv eines Namens im Sprechtext („die Ausgangslage von Fenna“, „der Plan von Fenna“).
- Präfixe `FE_`/`NI_` (nie `ER_`). Figuren-PNGs: `../peeps/op_201/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 198–200 verglichen): 198 (`easing-1`, `resting-1`), 199 (`easing-2`, `pointing_finger-1`), 200 (`shirt-3`, `resting-2`, `walking-1`, `walking-2`; Rosé-Bluse, blaue Hose). 201: `pointing_finger-2` und `blazer-4` – nicht in 198–200; türkise Hose und blaues Sakko dort nicht. Schauplatz neu: **WG-Küche mit Wandkalender**, Tisch mit Bücherstapel und zwei Tassen (kein Lerntisch mit Lampe wie 123, kein Klausursaal wie 045, kein Prüfungsraum wie 117). Leitmotiv: der leere Kalender wird zur 12-Monats-Tafel und hängt am Ende als „Lernplan“ an derselben Wand. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Küche** `fall`→`n1` | Bodenlinie, Wandkalender links (12 leere Monatsfelder), Fenna davor (blickt zum Kalender), Tisch; Nils kommt rechts dazu | programmatisch: Wandkalender, Tisch (Holz); tabler:`books` (Gelb), `coffee` ×2 (Weiß) | `Fall · Noch 1 Jahr bis zum Examen` → `… Womit fängt Fenna an?` → `… Nils kommt dazu` → `… Rückwärts planen, vom Examen aus` | ab 0,0 s Küche, Kalender, Tisch, Fenna mit Schild, Pille · „leer“ · Bücher · Blase Fenna · Nils mit Schild · Pille „Examen im letzten Jahr geschrieben“ · Tassen · Fenna dreht sich zu Nils · Blase Nils | – (kein passendes CC0-Geräusch für Tassen) |
| **A2 Einstieg** `hook`→`sechs` | Tafel, Fenna und Nils rechts | tabler:`calendar`, `book`, `list-check` | `Einstieg · Examen in 1 Jahr: Womit fängst du an?` → `… nicht das 1. Kapitel, sondern ein Plan` → `… 6 Schritte` | Titel · Kreuz „mit dem ersten Kapitel“ · Haken „mit einem Plan“ · Block „6 Schritte“ · Ziffern 1–6 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt · Die Ausgangslage von Fenna` | 1 | – |
| **C1 Schritt 1** `s1`→`p5ae` | Tafel mit **Wortlautkarte § 5a Abs. 2 S. 3 DRiG**, sieben Marker zum Wort | tabler:`zoom-question`, `book`, `list-check` | `Schritt 1 · Bestandsaufnahme: Was wird geprüft?` → `… Rahmen: Deutsches Richtergesetz` → `… Pflichtfächer, § 5a Abs. 2 S. 3 DRiG` → `… dazu Europarecht, Methoden, Grundlagen` | ≈ 12 | – |
| **C2 Landesrecht** `land`→`eigen` | Tafel: sechs Klausurkarten (3 Blau Zivilrecht, 2 Grün Öffentliches Recht, 1 Rot Strafrecht), 5 Stunden, Stoffkatalog | tabler:`file-text` (in den Karten), `map-pin`, `clock`, `list-check` | `… Das Nähere regelt das Landesrecht` → `… Beispiel Nordrhein-Westfalen: 6 Klausuren` → `… je 5 Stunden` → `… Stoffkatalog, § 11 Abs. 2 JAG NRW` → `… dein Land, deine Prüfungsordnung` | ≈ 8 | – |
| **C3 Ampel** `ampel`→`arot` | Tafel mit drei Ampelzeilen | fluent-hc:`vertical-traffic-light` | `… die Ampel` → `… Strafrecht grün` → `… Zivilrecht gelb` → `… Öffentliches Recht rot` | 5 | – |
| **D Schritt 2** `s2`→`neun` | **12-Monats-Tafel** erscheint: Monate 1–12, Examen (Flagge) am Ende von Monat 12, Freiversuch-Zeilen, Pfeil „rückwärts“, Endspurt 11–12, Puffer 10, Stoff 1–9 | tabler:`flag` (Rot), `lifebuoy`, `calendar`, `file-certificate` | `Schritt 2 · rückwärts planen` → `› 12 Monate` → `› Examen am Ende von Monat 12` → `› Freiversuch, § 5d Abs. 5 S. 2 DRiG` → `› Meldefrist: Landesrecht` → `› Endspurt: 8 Wochen` → `› 1 Puffermonat` → `› 9 Monate Stoff` | ≈ 17 | – |
| **E Schritt 3** `s3`→`proz` | dieselbe Tafel: Stoffbahn färbt sich Gebiet für Gebiet (Zivilrecht 1–4 Blau, Öffentliches Recht 5–7 Grün, Strafrecht 8–9 Rot) | tabler:`books`, `scale`, `gavel` | `Schritt 3 · die Stoffphase` → `› Empfehlung, keine Regel` → … → `› Prozessrecht im jeweiligen Block` | ≈ 10 | – |
| **F Schritt 4** `s4`→`alt` | dieselbe Tafel: Wiederholungsbahn 1–10 (Lila) „jeden Tag die 1. Stunde“, Pillen 1 Tag / 1 Woche / 1 Monat | tabler:`repeat`, `brain`, `cards`, `clock` | `Schritt 4 · das Wiederholungssystem` → … → `› auch fertige Gebiete` | ≈ 15 | – |
| **G Schritt 5** `s5`→`v117` | dieselbe Tafel: Klausurbahn 1–10 (Pink) „1 Klausur pro Woche“; Blase Nils | tabler:`writing`, `clock`, `file-check` | `Schritt 5 · Klausuren von Anfang an` → … → `› typische Fehler: Folge 117` | ≈ 13 | – |
| **H Schritt 6** `s6`→`spurt2` | dieselbe Tafel: Urlaub (Strand) unter Monat 6, Ring um den Puffer, Ring um den Endspurt, „2 pro Woche“; Blasen Fenna und Nils | tabler:`lifebuoy`, `sun`, `flag`; fluent-hc:`beach-with-umbrella` | `Schritt 6 · Puffer und Pausen` → … → `› Endspurt: 2 Klausuren pro Woche` | ≈ 12 | – |
| **I Beispielwoche** `wp`→`wp7` | Wochenplan als Tabelle (Mo–So × 1. Stunde/vormittags/nachmittags), Zelle für Zelle zum Wort | tabler:`calendar-week`, `cards`, `books`, `writing`, `list-check`, `clock`, `sun` | `Beispielwoche · Stoffphase` → … → `› Sonntag: frei` | ≈ 14 | – |
| **J Ergebnis** `erg`, `f3` | zurück in die Küche: der fertige Lernplan hängt mit Reißzwecke am Wandkalender; Fenna dreht sich zu Nils (Blase), Pillen „Monat 1: Zivilrecht“, „Samstag: 1. Klausur“ | fluent-hc:`pushpin` (Rot); Plan programmatisch | `Ergebnis · Der Plan hängt an der Wand` → `› Monat 1: Zivilrecht, Samstag: 1. Klausur` | 5 | Reißzwecke (`szene_201reisszwecke_1`, Freesound 446634) |
| **K Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · üben wie im Examen` → … → `› Fehlerliste aus den Korrekturen` | 5 | – |
| **L Lernplan** `sch`→`k6` | breite Karte, I.–VI. Punkt für Punkt, Farbpillen wie in der Tafel | – | `Lernplan · 6 Schritte` → `› I. …` … `› VI. Puffer und Endspurt` | 7 | – |
| **M Merksatz** `merke`→`m3` | Lexi erklärt (redet), vier Marker | – | `Merksatz` | 7 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Figurenbewegung, kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Reißzwecke beim Aufhängen des Plans). Freesound-API über den Proxy am 06.10.2026 gesperrt (HTTP 403) → vorhandene CC0-Datei aus `sfx3/` unter eigenem Namen kopiert, Herkunft in `geraeusche_herkunft.json`. Tassen, Bücher, Haken, Marker und Schiebeblenden stumm.
**Wortlautkarte** (FOLGE-ABLAUF Abschnitt 2): § 5a Abs. 2 S. 3 DRiG wörtlich mit Normangabe, Auslassungen „…“; gesprochen die Merkmale (Kernbereiche wörtlich, Rest „dazu europarechtliche Bezüge, Methoden und Grundlagen“), Marker synchron zum Wort.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Fenna studiert Jura in Nordrhein-Westfalen. In 12 Monaten will sie die Klausuren der staatlichen Pflichtfachprüfung schreiben.
>
> Die Vorlesungen hat sie gehört. Eine Klausur über 5 Stunden hat sie noch nie geschrieben.
>
> Im Strafrecht fühlt sie sich sicher, im Zivilrecht halbwegs, im Öffentlichen Recht kaum.
>
> Sie kann an 6 Tagen pro Woche lernen; 1 Tag soll frei bleiben.
>
> **Wie teilt Fenna die 12 Monate ein?**
