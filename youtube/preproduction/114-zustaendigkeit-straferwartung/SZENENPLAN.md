# Folge 114 · Straferwartung Zuständigkeit: Strafrichter, Schöffengericht, LG – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_114.py`](src/skript_114.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook, erzählt aus Sicht der Staatsanwältin: Herr Hartung (34, zweimal wegen Betrugs vorbestraft) kassiert in Erlenstadt (erfunden) als angeblicher Terrassenbauer von Februar bis Juli 2026 zwölf Anzahlungen, zusammen 40.000 €, und lebt davon; Herr Grote ist einer der Kunden (3.500 €). Im September bestimmt Staatsanwältin Eggert das zuständige Gericht. Ablauf: Fall → Frage → Sachverhalt → zwei Fragen (sachlich, örtlich) → I. sachlich als Treppe (Strafrichter § 25 Nr. 2 GVG im Wortlaut, Schöffengericht § 28, Strafbann § 24 Abs. 2, Landgericht § 24 Abs. 1 Satz 1 Nr. 2 im Wortlaut und § 74 Abs. 1, Nr. 3, Sonderzuweisungen Schwurgericht/OLG) → Straferwartung (Vergehen § 12 StGB, Strafrahmen § 263 Abs. 1/3, gewerbsmäßig, großes Ausmaß, Vorstrafen § 46, Gesamtstrafe §§ 53, 54) → Prognose der Staatsanwältin und Ergebnis Schöffengericht → II. örtlich §§ 7, 8, 3, 13 StPO → III. Gericht in der Anklage → Klausurtipp → Schema als Treppe → Merksatz. Hauptfilm 6:42,6 (5.558 Zeichen), Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Grote (GR), um 70 | Kunde, Geschädigter (eine der zwölf Taten) | Pose `standing/crossed_arms-1` (Pullover Lila `#B8A9F5`, schwarze Hose), Kopf `No Hair 3` (Glatze, grauer Haarkranz `#C4C4C4`), Brille `Glasses 4`, ohne Bart, Haut `#F0CDB0`; Mimiken `Calm`, `Smile Big\|Smile`, `Concerned\|Serious` (redet, Sorge), `Tired`, `Suspicious` | `helmut` (Mann, älter) |
| Herr Hartung (HA), 34 | angeblicher Terrassenbauer, Beschuldigter | Pose `standing/walking-2` (schwarzes T-Shirt, grüne Arbeitshose `#8FD694`, Turnschuhe), Kopf `Short 4`, ohne Bart, Haut `#E3B48E`; Mimiken `Calm`, `Smile` (redet), `Cheeky\|Smile` (cool nach der Anzahlung), `Suspicious`, `Fear` (Schreck bei Strafrahmen/Vorstrafen), `Serious` | `niklas` (Mann, jung) |
| Staatsanwältin Eggert (EG), um 40 | bestimmt das Gericht, Abschlussverfügung | Pose `standing/blazer-4` (blauer Blazer `#8DB3F2`, weißes Oberteil, schwarze Hose), Kopf `Medium Straight`, ohne Brille, Haut `#D9A47E`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Smile`, `Solemn` | `julia` (Frau, jung bis mittel, sachlich) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (zur Tafel, zum Haus, zum Schreibtisch), `_r` blickt nach rechts (Grote zu Hartung in A1). Keine Prothesen-Posen, keine Bärte, keine Polka Dots. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `GR_redet`, `HA_redet`, `EG_redet` (je links/rechts) und Lexi. Täterrolle ohne Herkunfts- oder Hautfarben-Klischee, Alltagskleidung, keine „fiese“ Figur. **Alle Menschen als Open Peeps**: die elf weiteren Kunden erscheinen nicht als Personen, sondern als elf Häuser (Icons von Gebäuden, keine Gesichter). Stimmen ausschließlich aus dem Pool (`ela_froh` nicht verwendet, weil keine heitere Rolle); `julia` für die Staatsanwältin, weil sie die einzige ernste Frauenstimme im Pool ist – Rollenverteilung anders als in 112 (dort `julia` Gläubigerin, `helmut` Schuldner; hier `helmut` Geschädigter, `niklas` Beschuldigter). **Namen mit eindeutig deutscher Aussprache**, nicht in der Liste vergebener Namen und in keiner früheren Folge verwendet (Repo-Suche): Grote, Hartung, Eggert („Albers“ verworfen, weil in 006 vergeben). Figuren-PNGs: `../peeps/op_114/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 112 (Fahrradwerkstatt, Gustav/Klara, `pointing_finger-2`, `walking-1`), 111 (`easing-1`, `pointing_finger-2`), 110 (`shirt-4`, `easing-1`, `blazer-1`). 114: Garten mit Haus, Zaun und Pflanze; elf Häuser als Kundschaft; Schreibtisch der Staatsanwaltschaft mit fallender Akte (wie in 039 der Ort „Staatsanwaltschaft“, weil die Geschichte dort spielt; anderes Personal, andere Pose und Farbe). Neue Posen (`crossed_arms-1`, `walking-2`, `blazer-4` in Blau statt Lila), Leitmotiv Treppe (Stufenleiter) statt Zeitstrahl. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Im Garten** `fall`→`h1` | Haus links, Zaun, Pflanze; Grote links blickt nach rechts, Hartung rechts blickt nach links | tabler:`home` (Gelb), `fence`, `plant-2` (Grün), `tools`, `cash-banknote` (Grün) | `Fall · Im Garten von Herrn Grote` → `Fall · Die Anzahlung` | Garten ab 0,0 s · „Wunsch: eine neue Terrasse“ · Hartung tritt auf · „selbstständiger Handwerker“ · Werkzeug · Scheine in Grotes Hand · Scheine wandern · „Anzahlung: 3.500 €“ · Hartung cool · Blase Hartung | Geldscheine (`szene_114geld_1`) |
| **A2 Gebaut wird nie** `nie`→`elf` | derselbe Garten, Grote allein rechts | tabler:`phone-off`, 11 × `home` | `Fall · Gebaut wird nie` → `Fall · Elf weitere Kunden` | „Gebaut wird nie.“ · Blase Grote · Telefon abgeschaltet · elf Häuser · „Februar bis Juli 2026“ · Grote müde | – |
| **A3 Staatsanwaltschaft** `akte`→`frage2` | Schreibtisch, Akte fällt; Eggert rechts | tabler:`desk` (Holz), `folders` (Gelb) | `Fall · Bei der Staatsanwaltschaft` → `Fall · Die Frage` | September · Akte · Eggert mit Schild · 12 Anzahlungen · 40.000 € · nie Material · 2 Vorstrafen · Blase Eggert · Frage sachlich · Frage örtlich | Akte auf dem Tisch (`szene_114akte_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Zwei Fragen** `plan`→`plan3` | Tafel, Hartung und Eggert | tabler:`gavel`, `map-pin`, `hourglass` | `Zuständigkeit › zwei Fragen` → `› die Straferwartung` | I. sachlich · II. örtlich · Prognose | – |
| **D Die Treppe** `st1`→`st4b` | Tafel mit vier Stufen, oben wechselnd Wortlautkarten und Zeilen | tabler:`stairs-up`, `gavel`, `building-bank`, `building-fortress` | `I. Sachlich › die Treppe` → `› Strafrichter, § 25 Nr. 2 GVG` → `› Schöffengericht, § 28 GVG` → `› Strafbann, § 24 Abs. 2 GVG` → `› Landgericht, § 24 Abs. 1 Satz 1 Nr. 2 GVG` → `› … Nr. 3 GVG` → `› Sonderzuweisungen` | Stufe Strafrichter · Wortlaut § 25 mit drei Markern · Stufe Schöffengericht · Strafbann · Stufe Landgericht · Wortlaut § 24 Abs. 1 Satz 1 Nr. 2 mit vier Markern · § 74 · Nr. 3 · Schwurgericht · Stufe OLG | – |
| **G1 Vergehen, Strafrahmen** `e1`→`e4` | Tafel | tabler:`hourglass`, `scale`, `file-text` | `› Straferwartung` → `› Vergehen, § 12 StGB` → `› Strafrahmen, § 263 StGB` | 1. Vergehen (Haken) · besonders schwerer Fall (Haken) · 2. Strafrahmen · 6 Monate bis 10 Jahre, Hartung erschrickt | – |
| **G2 gewerbsmäßig** `e5`→`e8` | Tafel | tabler:`cash-banknote`, `x` | `› Regelbeispiel: gewerbsmäßig` → `› großes Ausmaß?` | Definition BGH (3 Zeilen) · lebte von den Anzahlungen (Haken) · erfüllt · Nr. 2 (Kreuz) · 5.000 € je Tat | – |
| **H Vorstrafen, Gesamtstrafe** `e9`→`e11a` | Tafel, zwölf Kästchen | tabler:`file-text` (Rot), `stack-2`, `sum` | `› Vorstrafen, § 46 Abs. 2 StGB` → `› Gesamtstrafe, §§ 53, 54 StGB` | Vorstrafen · 12 Einzelstrafen · Gesamtstrafe · § 54 · Asperationsprinzip | – |
| **I Prognose, Ergebnis** `e12`→`f5` | Tafel mit Jahresachse 0–5 | tabler:`hourglass`, `stairs-up`, `gavel` | `› Prognose der Staatsanwältin` → `I. Sachlich › Ergebnis` → `› Amtsgericht – Schöffengericht` | Einzelstrafen · Einschätzung · Band 2,5–3,5 J. · Grenze 2 J. · Strafbann 4 J. · drei Kreuze · Schöffengericht | – |
| **J II. Örtlich** `o1`→`o4` | Tafel mit Bezirkskarte, zwölf Tatort-Pins, Haus | tabler:`map-pin`, `map-pins`, `home`, `map-2` | `II. Örtlich › §§ 7 ff. StPO` → `› Tatort` → `› Wohnsitz` → `› Zusammenhang` | Tatort · 12 Pins · Wohnsitz · Haus · Zusammenhang | – |
| **K III. Anklage** `an1`→`an3` | Tafel, Entwurf der Anklageschrift; Eggert redet | – | `III. Anklage › Gericht, § 200 Abs. 1 Satz 2 StPO` → `› Klausurkonvention` | § 200 · Spruchkörper · Blase Eggert und Entwurf zum Wort · Konvention | – |
| **L Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Straferwartung begründen` → `· bewegliche Zuständigkeit` | Zeile für Zeile | – |
| **M Klausurschema** `sch`→`k3` | Schema mit kleiner Treppe | – | `Klausurschema` → `› I. Sachlich` → `› II. Örtlich` → `› III. Anklage` | I. · 1.–4. (bei 3. drei Stufen zum Wort) · II. · III. | – |
| **N Merksatz** `merke`→`mk3` | Lexi erklärt (redet), drei Marker | – | `Merksatz` | Satz 1 · Satz 2 · Satz 3 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; zwei Bewegungen (Geldscheine, fallende Akte). Das erste Bild nach dem Intro zeigt ab 0,0 s den Garten mit Haus, Zaun, Grote mit Namensschild, Datumspille und Prüfpfad.
**Geräusche:** zwei Handlungsgeräusche, Freesound CC0 (über die API ohne Schlüssel erreichbar), unter eigenem Namen in `sfx3/`, Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Hartung (34) bietet in Erlenstadt als selbstständiger Handwerker den Bau von Terrassen an. Von Februar bis Juli 2026 nimmt er von 12 Kunden in Erlenstadt Anzahlungen zwischen 2.000 und 5.000 Euro, zusammen 40.000 Euro, darunter 3.500 Euro von Herrn Grote. Bauen wollte er nie, Material bestellte er nicht. Er hatte kein anderes Einkommen und lebte von dem Geld.
>
> Herr Hartung wohnt in Erlenstadt. Er ist zweimal wegen Betrugs vorbestraft (2019 Geldstrafe, 2022 zehn Monate Freiheitsstrafe mit Bewährung, Bewährungszeit 2025 abgelaufen).
>
> Im September 2026 liegt die Akte bei Staatsanwältin Eggert. Die Taten sind nachweisbar. Bearbeitervermerk: Bestimmen Sie das zuständige Gericht.
>
> **Zu welchem Gericht erhebt die Staatsanwältin Anklage?**
