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
- **Kontingent:** Das Skript prüft `user/subscription` und bricht ab, wenn der enthaltene Rest nicht reicht. Eine automatische Mehrnutzung gibt es nicht.
- **Wiederverwendung:** Jedes Segment wird nach Text, Sprecher, Modell und Einstellungen gecacht (`../el_cache`, nicht im Repo). Unveränderter Text wird nicht erneut bezahlt.
- **Zeitmarken:** Die `[marke]`-Positionen kommen aus den Zeichen-Zeitmarken von `/with-timestamps`. Ausgabe sind `stimme.wav` (48 kHz) und `cues.json` im selben Format wie bei der Piper-Vertonung.

**Aufruf** im `src`-Ordner eines Videos: `python3 synth_el.py skript_xy`
