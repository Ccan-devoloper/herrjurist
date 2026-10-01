# Reel-Test „Zu viel Wechselgeld“ (Themenplan Nr. 399)

Probe, ob sich die YouTube-Folgen als 30-Sekunden-Reels für Instagram umsetzen lassen. Format 1080 × 1920, 30 fps, 32,4 s, Stimme Carla (ElevenLabs `eleven_v4`, 407 Zeichen).

- **Aufbau:**
  - Hook mit Bild und Text ab dem ersten Frame: „50 € statt 5 €“.
  - Frage „Betrug?“, dann die zweimalige Verneinung mit Norm: § 263 und § 246 StGB, jeweils durchgestrichen.
  - Wendung „Aber!“ mit § 812 BGB.
  - Schluss: Lexi mit Aufforderung zum Folgen.
- **Untertitel** sind Wort für Wort ins Bild eingebrannt, das aktive Wort gelb, alles in Schriftform (§ 812 BGB, 45). Reels laufen meist ohne Ton; für YouTube-Langvideos gilt das nicht.
- **Sichere Zonen:** Wichtiges steht zwischen y ≈ 230 und 1560, weil Instagram oben die Kopfzeile und unten Text und Buttons einblendet.
- **Geräusche:** nur Handlungsgeräusche (Kasse, Münzen), Freesound CC0, siehe `geraeusche_herkunft.json`. Musik lässt sich in der Instagram-App aus der lizenzierten Bibliothek ergänzen.
- **Rechtslage (h. M.):**
  - Kein Betrug durch Unterlassen, weil es beim bloßen Leistungsaustausch keine Aufklärungspflicht gibt.
  - Keine Unterschlagung, weil das Geld übereignet wurde und damit nicht fremd ist.
  - Rückzahlung nach § 812 I 1 Alt. 1 BGB.

Erzeugen (Arbeitsordner mit `src/` = diese Skripte, `sfx/` = Geräusche als WAV):
`python3 …/stimme-elevenlabs/synth_el.py skript_reel carla` und dann `python3 reel.py` (Standbilder: `--bild 0.0,9.5`). Figuren und Emojis kommen aus `youtube/thumbnails/thumbnail.py`. Das MP4 liegt nicht im Repository.
