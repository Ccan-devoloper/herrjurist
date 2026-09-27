# Testreel, 27. September 2026

§ 224 Abs. 1 Nr. 2 StGB als visuelle Micro-Story mit Rex, Mara und Form-7. Fünf Shots, zwei kurze Textmomente, eine durchgehende ElevenLabs-Stimme. Ausgabe ist ein GitHub-Actions-Artefakt; keine Veröffentlichung.

Die fünf Szenenbilder wurden für diesen Test aus den Charakter-Referenzen und dem vorhandenen Tagescover erstellt. `render.mjs` erzeugt die Stimme und schneidet das 9:16-Video mit ffmpeg.

## Variante 3: feste Bildausschnitte und Geräusche

`render-v3.mjs` verwendet acht unterschiedliche Motive in elf kurzen Bildabschnitten. Zwei Nahaufnahmen sind sofortige, statische Umschnitte. Es gibt keinen frameweisen Zoom. Die zusätzliche Bildfolge zeigt Maras Schmerz, die Metallbeschaffenheit des Bechers, Form-7s Prüfung von Gegenstand und Einsatz sowie den Treffer im Detail. Die ElevenLabs-Stimme bleibt dieselbe; der Workflow versucht zwei kurze ElevenLabs-Soundeffekte (Metall/Visier und Scanner). Falls die SFX-API nicht verfügbar ist, werden einfache FFmpeg-Töne als technische Reserve erzeugt. Geräusche liegen deutlich unter der Stimme.

Lokal kann dieselbe Fassung mit `REEL_VOICE_PATH`, `REEL_IMPACT_PATH` und `REEL_SCANNER_PATH` aus vorhandenen Tonspuren gerendert werden; der GitHub-Testworkflow erstellt die aktuellen ElevenLabs-Spuren neu.

## Variante 4: Hook, Treffer und Schluss

`render-v4.mjs` kürzt die Sprecherfassung und verwendet ein neues eigenständiges Schlussmotiv. Der Treffer bekommt getrennte ElevenLabs-Spuren für den schweren Schlag und das kurze Visierknacken sowie einen knappen Tiefton. Beide Treffergeräusche beginnen genau auf dem sichtbaren Kontakt; beim Replay sind sie leiser. Die vormals schwarzen Textkästen entfallen: Der Einstieg hat eine zweistufige Comic-Überschrift, die Norm und der Merksatz sitzen klein im Hologramm. Der Schnitt endet kurz nach dem gesprochenen Merksatz.

## Variante 5: ursprünglicher Text, Comic-Grafiken und Maras Aufschrei

`render-v5.mjs` nimmt den vollständigen Sprechertext der 23-Sekunden-Fassung zurück. Die neue Merkszene beginnt exakt mit dem gesprochenen „Merke“. Ein scharfer Treffer-Effekt plus Visierknacken liegt auf dem ersten Kontakt, gefolgt von einem kurzen generierten weiblichen Aufschrei; beim Replay ertönt nur der Treffer in reduzierter Stärke. Die grafischen Aufkleber `overlays/comic-burst.webp` und `overlays/law-hologram.webp` sind eigens gezeichnete transparente Bildmotive. Exakte deutsche Überschrift und Norm werden beim Rendern in die Grafik gesetzt, damit die Zeichen verlässlich stimmen. Im Schlussbild bleibt die Norm groß lesbar.

Die ausgewählten ElevenLabs-Spuren und ihre Zeichenzeiten liegen in `audio-v5/`, sodass der GitHub-Testzweig die geprüfte Tonmischung reproduzierbar rendert. Der vordere Schlag ist gezielt im mittleren Frequenzbereich verstärkt, das Visierknacken beginnt ohne den generierten Vorlauf, und Maras kurzer Aufschrei folgt 250 Millisekunden danach. Das erste gesprochene Wort beginnt 520 Millisekunden nach dem Kontakt.

## Variante 6: integrierte Norm und passende Mara-Stimme

`render-v6.mjs` hält Skript, Timing, Schläge, Scanner und die übrigen Bilder von Variante 5 bei. Das neue Bild `shots/shot-11-law-projection.jpg` zeigt eine einzige große Projektion aus Form-7s Hand; die korrekte Norm ist in dieser Projektion gesetzt. Der zuvor überlagerte Norm-Aufkleber entfällt. Der generierte Soundeffekt-Aufschrei wird nicht verwendet. `audio-v6/mara-hit.mp3` ist stattdessen ein kurzer ElevenLabs-v3-Sprechlaut („Au!“) der tieferen deutschen Frauenstimme Selena. Er beginnt rund 60 ms nach dem sichtbaren ersten Treffer und klingt vor dem Erzähler wieder ab. Die gesonderten Stimmproben sind in `mara-voice-generate.mjs` dokumentiert.

## Variante 7: Aufschrei auf der Treffer-Nahaufnahme

`render-v7.mjs` verwendet dieselben Bilder, den Sprechertext und die Schlussprojektion. Der kurze Laut am Reel-Anfang entfällt. `audio-v7/mara-close-cry.mp3` ist eine intensivere ElevenLabs-v3-Stimmprobe derselben Mara-Stimme; sie setzt beim Schnitt auf `shot-08-impact-close.jpg` bei rund 13,10 Sekunden ein. Ein kurzes Visierknacken betont den Bildkontakt. Der Erzähler wird während des etwa 1,5 Sekunden langen Aufschreis leicht abgesenkt. Der Video-Render prüft anschließend die vollständige MP4-Datei.

## Variante 8: gezeichnete Anime-Trefferfolge

`render-v8.mjs` hält die Gesamtlänge, Sprecherfassung, Figurenwelt und übrigen Szenen von Variante 7 bei. Drei neue Zeichnungen ergänzen den etwa 2,5 Sekunden langen Replay-Moment: `shot-12-anticipation.jpg` zeigt den Becher 7 Frames vor dem Treffer, `shot-13-impact-frame.jpg` ist eine kontrastreiche 2-Frame-Kontaktzeichnung und `shot-14-reaction.jpg` zeigt Maras offene, schmerzhafte Reaktion mit herabfallender Zigarette und Visier-Splittern. Die bisherige Nahaufnahme wird nach dem Kontakt 11 Frames gehalten. Die Audiozeiten folgen den tatsächlich gerenderten Framegrenzen: kräftiger Schlag, Visierknacken und ElevenLabs-Aufschrei beginnen auf dem Kontaktframe bei etwa 13,13 Sekunden. Die Sprecherstimme wird während des Kontakts und der Reaktion kurz abgesenkt. Es gibt keinen fortlaufenden Kamera-Zoom.
