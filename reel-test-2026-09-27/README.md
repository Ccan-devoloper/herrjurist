# Testreel, 27. September 2026

§ 224 Abs. 1 Nr. 2 StGB als visuelle Micro-Story mit Rex, Mara und Form-7. Fünf Shots, zwei kurze Textmomente, eine durchgehende ElevenLabs-Stimme. Ausgabe ist ein GitHub-Actions-Artefakt; keine Veröffentlichung.

Die fünf Szenenbilder wurden für diesen Test aus den Charakter-Referenzen und dem vorhandenen Tagescover erstellt. `render.mjs` erzeugt die Stimme und schneidet das 9:16-Video mit ffmpeg.

## Variante 3: feste Bildausschnitte und Geräusche

`render-v3.mjs` verwendet acht unterschiedliche Motive in elf kurzen Bildabschnitten. Zwei Nahaufnahmen sind sofortige, statische Umschnitte. Es gibt keinen frameweisen Zoom. Die zusätzliche Bildfolge zeigt Maras Schmerz, die Metallbeschaffenheit des Bechers, Form-7s Prüfung von Gegenstand und Einsatz sowie den Treffer im Detail. Die ElevenLabs-Stimme bleibt dieselbe; der Workflow versucht zwei kurze ElevenLabs-Soundeffekte (Metall/Visier und Scanner). Falls die SFX-API nicht verfügbar ist, werden einfache FFmpeg-Töne als technische Reserve erzeugt. Geräusche liegen deutlich unter der Stimme.

Lokal kann dieselbe Fassung mit `REEL_VOICE_PATH`, `REEL_IMPACT_PATH` und `REEL_SCANNER_PATH` aus vorhandenen Tonspuren gerendert werden; der GitHub-Testworkflow erstellt die aktuellen ElevenLabs-Spuren neu.

## Variante 4: Hook, Treffer und Schluss

`render-v4.mjs` kürzt die Sprecherfassung und verwendet ein neues eigenständiges Schlussmotiv. Der Treffer bekommt getrennte ElevenLabs-Spuren für den schweren Schlag und das kurze Visierknacken sowie einen knappen Tiefton. Beide Treffergeräusche beginnen genau auf dem sichtbaren Kontakt; beim Replay sind sie leiser. Die vormals schwarzen Textkästen entfallen: Der Einstieg hat eine zweistufige Comic-Überschrift, die Norm und der Merksatz sitzen klein im Hologramm. Der Schnitt endet kurz nach dem gesprochenen Merksatz.
