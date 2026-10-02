# Folge 061 · Polizeilicher Notstand: Muss ein Vermieter Obdachlose aufnehmen? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_061.py`](src/skript_061.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall, Übungsfall nach dem Hook des Themenplans), Beispielland Nordrhein-Westfalen. Im Dezember droht Frau Brandt und ihren zwei Kindern nach Räumungsurteil die Obdachlosigkeit; das Ordnungsamt prüft nur die eigenen Notunterkünfte und weist die Familie gegen den Willen von Herrn Bauer für drei Monate wieder in ihre Wohnung ein. Ablauf: Fall → Frage → Sachverhalt → Landesrecht und Zuständigkeit → Ermächtigungsgrundlage und Gefahr → Verantwortliche/Nichtstörer → Wortlaut § 19 I OBG NRW → Nr. 1, 2 → Nr. 3 (Kern) → Nr. 4, Dauer (§ 19 II), Verhältnismäßigkeit → Ergebnis und Variante → Entschädigung (Wortlaut § 39 I OBG NRW) → Folgenbeseitigung nach Fristablauf → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 5:58,7 (5.266 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Brandt (BR), um 35 | Mieterin, Mutter von zwei Kindern | Pose `standing/resting-1` (blauer Pullover `#8DB3F2`, schwarze Hose), Kopf `Long`, Haut `#E8B98F`; Mimiken `Serious` (ruhig), `Concerned|Serious` (Sorge, redet), `Tired` (müde), `Smile` | `julia` (Frau, jung, ruhig) |
| Herr Bauer (BA), um 65 | Vermieter und Eigentümer | Pose `standing/blazer-3` (grünes Sakko `#8FD694`, schwarzes Shirt, graue Hose `#9A9AA6`), Kopf `Gray Short`, Haut `#F0C8A8`; Mimiken `Old` (ruhig), `Suspicious` (Ärger), `Serious` (denkt, redet), `Smile` (froh) | `helmut` (Mann, älter) |
| Herr Schmitz (SC), um 30 | Sachbearbeiter im Ordnungsamt | Pose `standing/easing-2` (hellblaues Hemd offen über Schwarz, gelbe Hose), Kopf `Short 2`, Haut `#D9A07A`; Mimiken `Calm`, `Suspicious` (denkt), `Driven` (redet), `Serious` | `niklas` (Mann, jung) |
| zwei Kinder | – | keine Comicfiguren: zwei Linien-Icons Fluent Emoji High Contrast `child` mit Pille „2 Kinder“ | – |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Brandt blickt nach rechts zu Herrn Bauer, Bauer nach links zu ihr; Szene B: Brandt blickt nach rechts zum Schreibtisch, Schmitz nach links; Szene C: Bauer blickt nach links zu Briefkasten und Wohnung; an Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `BR_redet`, `BA_redet`, `SC_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia (ela_froh nicht gebraucht: keine weitere Sprechrolle; „fröhlich“ passt zu keiner Figur); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Brandt, Bauer, Schmitz (nicht in der Liste früherer Namen). Genitive vermieden („Wohnung von Herrn Bauer“).
- Familie und Vermieter sachlich: Jobverlust als neutraler Grund der Mietschulden, kein Klischee; Herr Bauer verärgert, aber nicht als Bösewicht (am Ende froh, in der Variante nachdenklich).
- Figuren-PNGs: `../peeps/op_061/` (54 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 052 Mietshaus bei Nacht (Trennwand, Hausflur, Fernseher), 054 Wohnung mit Fernseher/Sideboard, 059 Laden. Hier: Wohnzimmer im Winter (Fenster mit Schneeflocken, Sofa), Ordnungsamt (Schreibtisch, Computer, Tastatur), Haus mit Briefkasten. Posen: `resting-1` zuletzt 056 (andere Person), `blazer-3` zuletzt 055 (anderes Sakko, Kopf, Rolle), `easing-2` in 052–059 nicht verwendet. Tageslicht-Cremegrund; der Winter erscheint über Schneeflocken und die Pille „Dezember“.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Wohnung** `fall`–`br1` | Frau Brandt, Kinder, Herr Bauer; Miete offen, Räumungsurteil, Räumungstermin; Blase Brandt | tabler:`window` (Blau), `snowflake`, `sofa` (Lila), `receipt-euro`, `gavel`, `calendar-event` (Rot); fluent-hc:`child` | `Fall · Dezember, die Mietwohnung` (ab 0,0 s) | Grundbild · Kinder · Bauer · Miete offen · Sorge · Urteil · Ärger · 15.1. · Blase | – |
| **B Ordnungsamt** `amt`–`sc1` | Schreibtisch, Computer; Schmitz prüft, alles belegt, Hotels nicht gefragt; Blase Schmitz | tabler:`device-desktop`, `keyboard`; ph:`bed`; fluent-hc:`hotel`, `child` | `Fall · Beim Ordnungsamt` | Brandt · Schmitz · Tastatur · belegt · Hotels · nicht gefragt · Blase | Tastatur (`szene_061tastatur_1`) |
| **C Verfügung** `verf`–`ba1` | Haus, beschlagnahmt, Familie eingewiesen 3 Monate; Briefkasten, Ordnungsverfügung; Blase Bauer | ph:`house`, tabler:`mailbox` (Blau), `file-text`; fluent-hc:`child` | `Fall · Die Verfügung` | Haus · beschlagnahmt · Familie · 3 Monate · Briefkasten · Verfügung · Blase | Briefkasten (`szene_061brief_1`) |
| **D Frage** `frage`/`frage2` | zwei Fragen | ph:`house`, fluent-hc:`child`, tabler:`coin-euro` | `Fall · Muss Herr Bauer die Familie aufnehmen?` | Frage 1 · Kinder · Frage 2 | – |
| **E Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **F Landesrecht** `land`/`zust` | Tafel; Schmitz | tabler:`map`, `building` | `Prüfung · Landesrecht, Beispiel NRW` → `Prüfung › formell: Zuständigkeit` | NRW · andere Länder · zuständig | – |
| **G Grundlage und Gefahr** `egl`–`winter` | § 14 I, Gefahr, Obdachlosigkeit, unfreiwillig, ✓ Winter; Brandt | tabler:`snowflake`, `heart` (Rot) | `Ermächtigungsgrundlage …` → `materiell › Gefahr …` | sechs Zeilen · Block · ✓ | – |
| **H Gegen wen?** `stoerer`–`pol6` | § 17, ✗ verursacht, Block Nichtstörer, § 19, § 6 PolG; Bauer | tabler:`users`, ph:`house` | `materiell › Adressat …` (3 Stände) | Zeilen · ✗ · Block · § 19 · § 6 | – |
| **I Wortlaut § 19 I** `wl19`–`n4` | Wortlautkarte, sechs Marker zum Wort | fluent-hc:`balance-scale` | `polizeilicher Notstand › Wortlaut …` → `… Nr. 1–4` | Karte · 6 Marker | – |
| **J Nr. 1, 2** `s1`–`s2` | ✓ gegenwärtig, ✓ erheblich, ✓ Nr. 2; Brandt | tabler:`calendar-event`, `heart`; fluent-hc:`child` | `… Nr. 1 …` → `… Nr. 2 …` | Zeilen · ✓ ✓ ✓ | – |
| **K Nr. 3** `s3`–`s3neg` | Tafel zartrot, Kernproblem, ✗ Block „Nr. 3 nicht erfüllt“; Schmitz | ph:`bed`, fluent-hc:`hotel`, tabler:`coin-euro` | `… Nr. 3: eigene Abwehr durch die Stadt` | sieben Zeilen · ✗ | – |
| **L Nr. 4, Dauer, Verhältnismäßigkeit** `s4`–`verh` | ✓ Nr. 4, Wortlaut § 19 II, Pille 6 Monate, § 15; Bauer | tabler:`hourglass`, `gavel` | `… Nr. 4` → `… Dauer, § 19 II` → `Ermessen › Verhältnismäßigkeit` | Zeilen · Pille | – |
| **M Ergebnis/Variante** `erg`–`dulden` | Block rot, Variante, Block gelb; Bauer froh, dann nachdenklich | fluent-hc:`hotel`, ph:`house` | `Ergebnis` → `Variante …` | Block · zwei Zeilen · Variante · dulden | – |
| **N Entschädigung** `entsch`–`regress` | Wortlautkarte § 39 I, drei Marker; ✓ beide Fälle; Miete; danach; Rückgriff | tabler:`coin-euro` | `Entschädigung, § 39 I` → `… Rückgriff, § 42 II` | Karte · Marker · ✓ · Zeilen | – |
| **O Fristablauf** `ende`–`streit` | Folgenbeseitigung, ✗ OLG Köln, a. A. VG Köln | tabler:`hourglass`, `door-exit` | `Nach Fristablauf › …` | Zeilen · ✗ | – |
| **P Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Verfügungen trennen` | drei Hinweise | – |
| **Q Klausurschema** `sch`–`q6` | Schema baut sich auf | – | `Klausurschema` | Titel · 1. · 2. · 3. · Adressat · Nr. 1–4 · 4. · Befristung · Entschädigung · Folgenbeseitigung | – |
| **R Merksatz** `merke`/`m2` | Lexi erklärt, Marker | – | `Merksatz` | Satz 1 · Marker · Zeilen · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** zwei Handlungsgeräusche (Tastatur in Szene B, Briefkastendeckel in Szene C), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Prüfpfad-Reihenfolge:** Die Zuständigkeit wird im Sprechtext vor der Ermächtigungsgrundlage genannt (ein Satz); der Pfad nummeriert deshalb erst im Schema („1. Ermächtigungsgrundlage, 2. formell …“) und verwendet davor dieselben Begriffe ohne Nummer.

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Nordrhein-Westfalen, Dezember: Frau Brandt wohnt mit ihren zwei Kindern zur Miete bei Herrn Bauer. Nach einem Jobverlust konnte sie die Miete monatelang nicht zahlen. Herr Bauer hat gekündigt und ein Räumungsurteil erstritten; der Gerichtsvollzieher räumt am 15. Januar. Frau Brandt findet keine Wohnung. Herr Schmitz vom Ordnungsamt prüft die Notunterkünfte der Stadt: alle belegt. Bei Hotels und Pensionen fragt er nicht nach. Die Stadt beschlagnahmt die Wohnung und weist die Familie für drei Monate wieder ein. Herr Bauer wehrt sich.
>
> **Muss Herr Bauer die Familie aufnehmen? Bekommt er Geld?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen, Zahlen und Daten in Ziffern („§ 19 Abs. 1 OBG NRW“, „15.1.“, „3 Monate“, „6 Monate“), gesprochen als Wörter. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Wortlautkarten § 19 Abs. 1 und § 39 Abs. 1 OBG NRW sowie die Zitatzeilen § 19 Abs. 2 OBG NRW sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe).
