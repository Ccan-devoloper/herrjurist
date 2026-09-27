# Freigegebener Reel-Standard

Die Referenz ist das 24,03-s-Reel zu § 224 Abs. 1 Nr. 2 StGB aus `reel-test-2026-09-27/render-v8.mjs` (GitHub Actions 36285669693). Die vollständigen, im Dashboard sichtbaren Vorproduktionsinfos stehen im Feld `inhalte.b3.infoVorproduktion` der 28.09.-Tagesdatei. Diese Datei beschreibt die Umsetzung für künftige Folgen.

## Dramaturgie und Schnitt

1. Mit einer verständlichen Handlung und einer offenen Klausurfrage beginnen. Die Auflösung stufenweise liefern, die Norm vor dem Merksatz deutlich zeigen. Keine künstliche Kürzung auf Kosten der Erklärung.
2. Die Figuren Rex, Mara und Form-7 im gleichen handgezeichneten orangefarbenen Sci-Fi-Comic halten. Neue Szenen als zusammengehörige Motive mit klarer Körperhaltung und Handlungsrichtung generieren. Form-7 und die Normprojektion ausreichend groß zeichnen. Merke hat ein eigenständiges Schlussbild.
3. 1080 × 1920, 30 fps. Der freigegebene Schnitt nutzt 14 Bildbeats in 24,03 s; mit eigenständigen Nah-, Detail- und Reaktionsmotiven. Den Bildwechsel an Aussage und Handlung ausrichten. Keine Pflichtzahl an Bildern: Bei längerem Text zusätzliche sinnhafte Motive erzeugen, keine hektischen Füllschnitte.
4. Standbilder je Beat fixieren. Kein kontinuierliches `zoompan`, keine Interpolation oder per-Frame-Crop. Ein einzelner harter Sprung in eine feste 1,13-fache Nähe für den Hook ist erwünscht. Bei einem erzählerischen Höhepunkt darf eine kurze Erwartung (hier 7 Frames), ein Kontaktbild (hier 2 Frames), ein enger Hold (hier 11 Frames) und ein gut lesbares Reaktionsbild folgen. Die konkrete Folge der neuen Handlung anpassen.
5. Plakative Schrift nur in dafür vorgesehenen illustrierten Flächen; z. B. Comic-Burst oder Form-7-Projektion. Wenige Wörter, Anton und Space Grotesk, handzeichnungsnaher Kontrast. Den exakten Normtext erst im Schnitt setzen, damit die Buchstaben stimmen. Kein billiges freischwebendes Textkästchen über einer zufälligen Szene.

## Stimme und Geräusche

- Sprecher aus ElevenLabs mit der aktuellen freigegebenen Stimme; V8: `PhufIH7nYh2Up1uej6aY`, `eleven_multilingual_v2`, stability 0.42, similarity 0.80, style 0.36, speed 1.06. ElevenLabs-Timestamps bestimmen Satzgrenzen, 0,52 s Voice-Vorlauf im V8. Jede neue Folge hat ihre eigenen tatsächlichen Zeiten.
- **Paragraphenzahlen paarweise aussprechen:** `§ 224` → „Paragraf zwei vierundzwanzig“; `§ 113` → „Paragraf eins dreizehn“; `§ 1923` → „Paragraf neunzehn dreiundzwanzig“. Jahreszahlen normal, z. B. 1923 → „neunzehnhundertdreiundzwanzig“. Die V8-Altaufnahme spricht § 224 noch lang; das genehmigte Video wird dadurch nicht stillschweigend geändert. In neuem TTS stets die kurze Lautung ausschreiben und anhören.
- Geräusche aus ElevenLabs für das sichtbare Ereignis generieren. Der Becherschlag: heller, lauter, harter Attack plus kurzes Visierknacken, kein sanftes Klirren und kein bloß dumpfer Bass. Im V8 liegt der Replay-Kontakt bei 13,133 s. Erzähler am Kontakt leicht absenken, SFX limiterbegrenzt mischen. Bei anderer Handlung eigene passende Geräusche, zum Beispiel holografisches Zerbrechen; den Schlageffekt nicht kopieren.
- Maras Aufschrei im V8 stammt aus Eleven v3, Stimme „Selena“, als kurze kräftige erwachsene Reaktion. Er beginnt **auf dem sichtbaren Kontaktframe** und klingt über der Reaktion aus. Kein generischer Standardschrei, kein vorgezogener Einsatz. Wo niemand getroffen wird, keinen Schrei erfinden.

## Vor Freigabe

- Fachinhalt mit geltendem Normtext und Rechtsprechung abgleichen; konkrete Voraussetzungen und Unsicherheiten sauber formulieren.
- Das ganze Reel auf dem Handyformat mit Ton ansehen: klare Handlung, ruhige Standbilder, richtige Aussprache, sauberer SFX-Kontakt, lesbare Textflächen und eigenständiges Merke-Bild.
- `ffprobe`: 1080 × 1920, 30 fps, H.264/AAC, vollständige Dauer. Timing-JSON und MP4 gemeinsam prüfen. Produktionsdateien und Code versionsgebunden lassen, damit die Aufnahme reproduzierbar bleibt.
- Die VA-Fortsetzungsfeststellungsklage vom 28.09. wird als **separate Prüffassung** gerendert. Der Live-Slot 28.09. enthält ausschließlich das freigegebene §-224-V8-Reel, bis der Betreiber etwas anderes ausdrücklich freigibt.
