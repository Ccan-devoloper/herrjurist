# Ablauf einer Folge (Serienstandard Open Peeps, Vorlage Folge 001)

Diese Datei beschreibt die Produktion einer Folge vom Themenplan bis zur Drive-Ablage. Sie gilt zusätzlich zu `MASTERSTANDARD-09.md` (Serienstandard), `ABNAHME-16x9.md`, `VIDEOLEITLINIEN-16x9.md`, `STANDARDINTRO.md`, `SOUNDBIBLIOTHEK.md` und `PRODUKTION-START.md`. Die vollständige Referenzfolge ist [`preproduction/001-raser-fall/`](preproduction/001-raser-fall/). Für den Bild- und Tafelstil dient zusätzlich der Katzenkönig (`preproduction/katzenkoenig-test/`) als Vorlage.

## 0. Umgebung

`bash youtube/preproduction/etb2/einrichten.sh` richtet Schriften, Icons, Pinselblasen und Python-Pakete ein. Intro und Outro holt `rclone copy "lexverse:LexVerse Produktion/_Quellen" youtube/preproduction/_quellen --include "00-*.mp4"`, falls sie fehlen. Zusätzlich gebraucht werden `pip install pyloudnorm faster-whisper`.

Ordner je Folge: `youtube/preproduction/NNN-kurzname/` mit `src/` (Skript, Figuren, Folien, Renderer, Timeline). Ausgaben landen in `out/` (nicht im Repository).

## 1. Recherche und Rechtsstand

- Themenplan-Zeile lesen (`themenplanung/themenplan-780.csv`: Titel, Hook, Kernfrage, Normen, Leitentscheidung, Rechtsstand-Hinweis, Fundstelle) sowie die Fundstelle im Gesamtwissen (`tools/gesamtwissen_index.py`; Quelle in `LexVerse Produktion/_Quellen/`, „UNCERTIFIED“).
- **Jede Aussage an Primärquellen prüfen:** gesetze-im-internet.de, bundesgerichtshof.de, bundesverfassungsgericht.de, Landesportale, EUR-Lex. Volltexte lesen, Randnummern notieren. Was nicht abrufbar ist, als „nicht online verifiziert“ kennzeichnen; keine Zitate aus dem Gedächtnis.
- Der Themenplan kann irren (Folge 001: das gemeingefährliche Mittel war vom BGH verneint). Abweichungen in `RECHTSSTAND.md` festhalten und **dem Koordinator melden**; die Plan-CSV nicht selbst ändern.
- `RECHTSSTAND.md` nach dem Muster von 001: Normen mit URL, Entscheidungen mit Az./Rn./URL, Aussage-Beleg-Tabelle je Cue, „bewusst nicht behauptet“, offene Einschränkungen.
- Bei Landesrecht gilt `VIDEOLEITLINIEN-16x9.md` (länderneutral, Normen aller 16 Länder in der Beschreibung).
- Reale Personen (Politiker, Angeklagte, Opfer) werden nicht als Figuren dargestellt: fiktive Namen oder reine Funktionsrollen („die Ministerin“). Keine Karikaturen. Opfer realer Taten nicht als Comicfigur.

## 2. Skript (`src/skript_NNN.py`)

- Aufbau wie `001-raser-fall/src/skript_raser.py`: `SEGMENTE` mit `[marke]`-Cues, `STIMMEN` für Figurenrede. Lexi (Klausurtipp, Merksatz) spricht mit der Erzählerstimme ohne Rolle.
- Etwa 4.000–4.500 Zeichen, also rund fünf Minuten. Zahlen und Paragrafen als Wörter („Paragraf zweihundertelf“, „neunundsechzigjährige“). Keine Verabschiedung. Das letzte Wort beendet den Sachgedanken.
- Jedes Format beginnt mit einem konkreten Fall. Bei Examenswissen und Methodik ist das ein Beispielfall, an dem das Schema entlangläuft.
- **Namen einheitlich aussprechen (Vorgabe Kanalinhaber, 01.10.2026):** Jeder Figurenname klingt im ganzen Video gleich, bei Erzählerin und Figuren, nie mal deutsch, mal englisch. Deshalb Namen mit eindeutig deutscher Aussprache wählen; englisch lesbare Namen (Tom, Kim, Mike, Ryan, Jamie …) vermeiden. Nach der Vertonung jede Nennung prüfen (Spracherkennung mit Wortzeiten, Nennungen einzeln ausschneiden und vergleichen) und abweichende Segmente gezielt neu vertonen, notfalls mit lautlicher Schreibweise im Sprechtext. Ergebnis je Name in ABNAHME.md festhalten.
- Rollen aus dem Ensemble (`stimme-elevenlabs/besetzung.json`), passend zu Alter und Geschlecht. Lea nicht bei Gewalt. Nicht dieselben Stimmen wie in der Vorfolge, wenn es sich vermeiden lässt.

## 3. Szenenplan und Figuren

- `SZENENPLAN.md` wie in 001: Besetzung (Pose, Kopf, Farben, Stimme), Szenentabelle (Ort, Requisiten als Iconset:Name, Tafel/Prüfpfad, Bildhalte, Geräusch), Sachverhaltskarte, Abweichungen zu den Vorfolgen.
- `src/figuren_NNN.py` nach `figuren_raser.py`, eigener Ausgabeordner `../../peeps/op_NNN`. Jede Ansicht gibt es links- und rechtsblickend. Die Blickrichtung im Kontaktbild prüfen: Die Figur rechts blickt zur Tafel nach links. Sprechende Ansichten bekommen Mundzustände a/o/e. Posen mit Prothesen nicht reflexhaft für Täter verwenden.
- **Grundmimik immer mit geschlossenem Mund** (Ruheform, Pausen, fremde Stimme). Offenen Mund haben: Blank (klein), Cheeky (klein, Zunge), Concerned, Concerned Fear, Explaining, Hectic, Loving Grin 1, Loving Grin 2, Rage, Smile Big, Smile LOL, Smile Teeth Gap. Diese nur als „Augen|Mund“ mit geschlossenem Mund verwenden, z. B. `"Concerned|Serious"`, `"Smile Big|Smile"`, `"Cheeky|Smile"`, `"Rage|Serious"`. Die Mundzustände entstehen dann aus `f"{mimik.split('|')[0]}|{m}"` (siehe `004-neutralitaetspflicht/src/figuren_004.py`). Geschlossen sind: Angry with Fang, Awe, Calm, Contempt, Cute, Driven, Eating Happy, Eyes Closed, Fear, Old, Serious, Smile, Solemn, Suspicious, Tired, Very Angry.
- Requisiten nur aus den Iconsets unter `preproduction/blasen/` (Tabler, Phosphor, Fluent Emoji, Pepicons, Streamline Freehand). Lizenzen notieren; CC BY braucht eine Namensnennung in der Beschreibung.

## 4. Vertonung

- Im `src`-Ordner: `python3 ../../stimme-elevenlabs/synth_el.py skript_NNN`.
- Die Sperre sorgt dafür, dass nie zwei Vertonungen gleichzeitig laufen. Das Kontingent wird in Credits geprüft.
- Jedes Segment wird auf −19 LUFS angeglichen (`angleichen()`), Restlaute am Segmentende werden stummgeschaltet (`entstoeren()`). Die Ausgabe nennt Gains und den tatsächlichen Credit-Verbrauch; Verbrauch und Zeichen im Abnahmebogen notieren.
- **Nie nur für Tests vertonen.** Erst das Skript fertigstellen, dann einmal vertonen. Nachbesserungen nur segmentweise, der Cache verhindert, dass unveränderte Segmente neu bezahlt werden.
- Danach `ffmpeg -i ../stimme.wav -ac 2 -ar 48000 ../stimme_48k.wav`.

## 5. Folien und Render

- `src/folien_NNN.py` nach `folien_raser.py` (Bausteine aus `etb2/src/bausteine.py`). `src/render_NNN.py` ist eine Kopie von `render_raser.py`; nur Import und Videoname ändern. Darin sind `--vorschau`, `--frames`, `--manifest`, das harte `cut` und der Schutz für Sprites außerhalb des Bildes schon enthalten.
- **Rechtsstand Grundgesetz:** Seit 28.12.2024 (BGBl. 2024 I Nr. 439) stehen die Zuständigkeiten des BVerfG in Art. 94 GG (Organstreit Art. 94 I Nr. 1 usw.); Art. 93 GG regelt Status und Organisation des Gerichts.
- Gemeinsame Dateien (`etb2/src/*`, `synth_el.py`, `tools/*`) nicht ändern. Fehlt etwas, kommt eine eigene Hilfsfunktion in den Folienordner, und der Koordinator bekommt Bescheid.
- Pflichtregeln (per Assertion geprüft):
  - Jede Cue-Marke hat ein Bildelement.
  - Kein Element erscheint im Wisch.
  - Tafelzeilen bis x ≤ 1170 (Schema ≤ 1820).
  - Figuren sind nie seitlich oder oben angeschnitten.
  - Nur `szene_*`-Geräusche.
- Geräusche: höchstens zwei oder drei Handlungsgeräusche, aus Freesound CC0 (`https://freesound.org/apiv2/…`, Zugang über den Proxy) nach `preproduction/sfx3/szene_NNN<name>_1.wav` (**mit Folgennummer**, z. B. `szene_007tuer_1.wav`, Aufruf `szene(…, "007tuer*")`; 48 kHz mono). Vorhandene Dateien anderer Folgen nie überschreiben. Herkunft in `geraeusche_herkunft.json`.
- Ablauf:
  1. `--vorschau` (Kontaktbogen je Folie)
  2. `--frames` an allen Fallmomenten und Sprechfenstern
  3. Vollrender
  4. `--manifest` (mindestens 45 eigenständige Bildhalte; Bildhalt-Kontaktbögen erzeugen und **alle Bildhalte ansehen**)
  5. `python3 timeline_NNN.py` (Kopie von `timeline_raser.py`) → `CUE-TIMELINE.md`
- **Sichtprüfung inhaltlich:** Stimmt jedes Bild mit dem Sachverhalt überein (Ampel/Haltelinie, wer wo steht, wer spricht)? Gibt es Überlappungen, verdeckte Requisiten oder Bilder mitten im Wisch? Mundbewegung mit `--frames` in 0,1-s-Schritten an jedem Sprecher prüfen.

## 6. Endschnitt, Prüfung, Metadaten

- `python3 ../../../tools/schnitt.py --haupt ../out/NNN-Titel-Hauptfilm.mp4 --out ../out/NNN-Titel.mp4` (Intro und Outro aus `_quellen`, statische Pegel).
- `python3 ../../../tools/pruefe_folge.py .. --mp4 ../out/NNN-Titel.mp4 --asr` muss mit Exit 0 enden: Sprecherspanne ≤ 1,5 LU, keine Restlaute, Technik OK. Abweichungen der Spracherkennung einzeln bewerten (Ausspracheproblem oder Erkennungsfehler) und auffällige Stellen im Abnahmebogen als „bitte anhören“ mit Videozeit (+8 s) notieren.
- `python3 ../../../tools/youtube_metadaten.py --cues ../cues.json --kapitel ../kapitel.json --folge NNN --versatz 8.0 --out <scratch>`. Die Beschreibung auf fachliche Richtigkeit gegenlesen (Planbeschreibung kann falsch sein, dann dem Koordinator melden). Am Ende eine Lizenzzeile für die verwendeten Iconsets anhängen.
- Thumbnails: `LEXVERSE_EMOJI=…/blasen/fluent-emoji-flat/package/icons.json python3 thumbnails/aus_plan.py --render <scratch> --nr N-N` → `NNN.jpg` = `thumb_A.jpg`, `NNN_B.jpg` = `thumb_B.jpg`; 0 Fehler. Kontaktbogen ansehen.

## 7. Abnahmebogen, Master, Drive

- `ABNAHME.md` im Folgenordner, jede Zeile des Musters `ABNAHME-16x9.md` mit Belegen. Befunde und Korrekturen offen nennen. Freigabe bleibt `noch nicht bestanden`, bis der Kanalinhaber gesehen und gehört hat.
- `master.zip` wie bei 001:
  - Dokumente, Code (inkl. `etb2`), Figuren-PNGs, Bildhalt-Keyframes, Prüfbilder, `pruefbericht.json`
  - `stimme.wav` und `el_cache`, SFX mit Herkunft, Schriften, `LIESMICH.txt`
  - Mit `unzip -t` prüfen.
- Upload: `rclone copy <upload> "lexverse:LexVerse Produktion/NNN Kurztitel"`. Hochgeladen werden `NNN-Titel.mp4`, `NNN-Titel-Hauptfilm.mp4`, `master.zip`, `thumb_A.jpg`, `thumb_B.jpg`, `beschreibung.txt`, `kapitel.txt`, `untertitel.srt` und `metadaten.json`. Danach `rclone check` (0 Abweichungen); Ordner-ID und Ergebnis in `ABNAHME.md`. **Ordner nur mit rclone anlegen**, nie über den Drive-Connector.
- Im Repository nur Text und Code: `SZENENPLAN.md`, `RECHTSSTAND.md`, `ABNAHME.md`, `CUE-TIMELINE.md`, `cues.json`, `kapitel.json`, `bildhalt_manifest.json`, `pruefbericht.json`, `geraeusche_herkunft.json`, `src/*.py`. Danach `out/`, `stimme*.wav` und `el_cache` im Container aufräumen, sobald der Master in Drive bestätigt ist.
