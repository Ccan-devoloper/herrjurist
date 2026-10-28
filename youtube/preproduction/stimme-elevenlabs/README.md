# Sprecherstimme über ElevenLabs (Test, Stand 30.09.2026)

- **Sprecher:** Moritz Wegner (`PhufIH7nYh2Up1uej6aY`), der Erzähler aus `youtube-15-continuation-audio.yml`. Einstellungen wie dort: Stabilität 0,42, Ähnlichkeit 0,82, Stil 0,38, Tempo 1,08.
- **Erzählerin:** Carla Blum (`rKiu7lQ4c5P3az3745s3`) ist Standard (seit 30.09.2026). Moritz Wegner ist Reserve.
- **Modell:** `eleven_v4` mit `apply_text_normalization: "off"`. Im Hörvergleich gegen `eleven_multilingual_v2` klang v4 deutlich besser.
- **Aussprache:**
  - Paragrafenzahlen stehen im Skript in Hunderter-Form als Wort („elfhundertachtunddreißig“). Ziffern liest v4 als „tausendeinhundert…“.
  - Gesetzesabkürzungen werden automatisch mit Punkten gesprochen (BGB → „B.G.B.“). So klang es in den Hörproben am natürlichsten.
  - Ein Lautschrift-Wörterbuch „Herrjurist Gesetze“ (BGB, HGB) liegt als Reserve im ElevenLabs-Konto.
- **Zugang in Claude-Code-Sitzungen:**
  - `api.elevenlabs.io` muss in den erlaubten Domains der Umgebung stehen.
  - Unter API-Anmeldedaten ist ein benutzerdefinierter Header `xi-api-key` einzutragen, ohne Präfix.
- **Kontingent:** Das Skript prüft `user/subscription` (Werte sind **Credits**, nicht Zeichen) und schätzt den Bedarf mit 0,15 Credits je Zeichen (gemessen: 0,12 bei `eleven_v4`). Reicht der Rest nicht, bricht es ab; eine automatische Mehrnutzung gibt es nicht. Nach jeder Vertonung wird der tatsächliche Verbrauch ausgegeben.
- **Lautheit:** Jedes Segment wird auf −19 LUFS angeglichen (`angleichen()`, ±10 dB; Spitzen über −1 dBFS fängt seit 01.10.2026 ein Vorschau-Limiter ab, Verfahren aus Folge 002), damit Erzählerin und Figuren gleich laut sind. Folge 001 vorher: Carla −18,8, Jonas −21,8, Max −15,6 LUFS.
- **Wiederverwendung:** Jedes Segment wird nach Text, Sprecher, Modell und Einstellungen gecacht (`../el_cache`, nicht im Repo). Unveränderter Text wird nicht erneut bezahlt.
- **Zeitmarken:** Die `[marke]`-Positionen kommen aus den Zeichen-Zeitmarken von `/with-timestamps`. Ausgabe sind `stimme.wav` (48 kHz) und `cues.json` im selben Format wie bei der Piper-Vertonung.
- **Bereinigung (seit 01.10.2026):** `entstoeren()` schaltet kurze Restlaute (≤ 0,2 s nach ≥ 0,2 s Stille) am Segmentende stumm und blendet jedes Segment 8 ms ein und 15 ms aus. Die Länge bleibt gleich, deshalb gelten die Cue-Zeiten weiter. Anlass war Folge 001, Segment 18: ein abgeschnittener Ansatz nach „…vor.“, hörbar als „Abbrechen“.

**Aufruf** im `src`-Ordner eines Videos: `python3 synth_el.py skript_xy`
