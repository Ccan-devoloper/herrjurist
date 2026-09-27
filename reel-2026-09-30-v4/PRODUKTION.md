# 30.09.2026 – § 136a StPO, Cartoon-Prüffassung v4

**Status:** alleinige Prüffassung auf `codex/reel-test-20260930-v4`. Den freigegebenen 30.09.-Slot nicht vor Sichtung und Zustimmung austauschen.

## Verbindliche Quelle und Korrektur

Die projektweiten Regeln stehen im Repository `Ccan-devoloper/herrjurist`, Branch `instagram-assets`, unter `vorproduktion/REEL-LEITLINIEN.md`. Diese Datei wurde am 27.09.2026 mit den bislang nur implizit vereinbarten Anforderungen präzisiert: am Referenzcartoon orientierter Figurenstil, Anime nur für Schnitt/Bewegung, Text bereits im generierten Bild, keine lange statische Normfolie, aktiv geprüfte passende Charakteräußerungen, Dokumentenkontinuität.

In v3 gab es zwar eine vorliegende Charakterstimmen-Regel, aber der konkrete Schnitt enthielt nur den Erzähler. Der dortige Text wurde programmatisch in die zuvor leeren Papier- und Hologrammflächen gesetzt, und der Schluss zeigte ein unsigniertes Formular. Eine 2D-Cartoonwelt war in der Datei genannt; der genaue Rick-and-Morty-nahe Zeichenduktus war nicht ausdrücklich von Anime-Inszenierung abgegrenzt. Diese Implementierungsfehler sind keine Ausnahme von den Nutzerwünschen.

## Neue Bildkette

Die zehn hochauflösenden 9:16-Schlüsselbilder unter `masters/` sind mit ImageGen anhand der Golden References für **Zylla Glitch** und **Brakk Quarzfaust** entstanden. Die vom Nutzer angehängten Cartoonreferenzen gaben den vereinfachten 2D-Duktus vor. Gegenüber v3: starke schwarze Konturen, flächige Farben, vereinfachte Gesichtsanatomie, kein Anime-Painting. Brakks Kristalle, Arbeitskleidung und weißes Unterhemd sowie Zyllas genau zwei Antennen, grüne Haut, lilafarbene Jacke und Herz-Shirt wurden für jede Einstellung erneut geprüft. Fachfarbe Strafrecht: Orange.

1. `01-consent` zeigt bereits das unterschriebene Blatt. Die exakten Worte `EINWILLIGUNG` und `Aussage verwerten` sowie die Signatur sind **Teil der generierten Papierillustration**.
2. `01-reject` ergänzt den roten Scanner-Stopp in genau derselben Einstellung; der Text und die Unterschrift bleiben erhalten.
3. `02-interrogation` / `02-later-tired`: dieselbe Kameraposition, Uhrzeit ändert sich, Zyllas Augen schließen sich. Ein echter erschöpfter Seufzer liegt auf ihrem sichtbaren Müdigkeitsmoment.
4. `03-slam`: Brakk ruft „Jetzt rede!“ und schlägt einmal mit der Faust auf den **Tisch**. Aufschlag, Schlaggeräusch und Zyllas Zusammenzucken werden gemeinsam gesetzt.
5. `04-statement`: Zylla spricht erschöpft weiter, das kleine Gerät zeichnet auf.
6. `05-law1` projiziert `§ 136a StPO / ERMÜDUNG` kurz aus dem Aufnahmegerät **als generierten Teil dieser Szene**. Die Figuren bleiben groß. Danach zurück auf Zyllas Reaktion.
7. `06-law2` zeigt aus demselben Gerät `§ 136a Abs. 3 StPO / EINWILLIGUNG`, ebenfalls im Bild generiert und kurz im Schnitt.
8. `07-shield` / `08-cross` zeigen das **gleiche bereits unterschriebene Formular** und dieselben lesbaren Worte. Ein gezeichneter Rechtsschutzschild stoppt die aufgezeichnete Aussage. Erst zur Schlusspointe erscheint das rote X auf dem Blatt, ohne die Signatur zu verdecken.

Schnittziel: etwa 30 Sekunden, 1080 × 1920, 30 fps. Kein kontinuierlicher Zoom und kein globales Wackeln; einzelne begründete Uhr-, Rekorder- und Papier-Nahaufnahmen. Brakks Schlag und das X sind kurze Animationen aus eng aufeinanderfolgenden Zuständen. `make_frames.py` setzt **keine** Schrift in Szene oder Papier; nur `render.mjs` erzeugt die separat freigegebenen Captions unten.

## Ton, Norm und Captions

- Erzähler: bisher freigegebene ElevenLabs-Stimme Moritz Wegner `PhufIH7nYh2Up1uej6aY`, Deutsch, `eleven_multilingual_v2`.
- Brakk: neu ausgewählte deutsche tiefe Stimme „Helmut Stieglbauer – Deep and Dynamic“ `JiW03c2Gt43XNUQAumRP`, „Jetzt rede!“ auf Brakks gezeichnetem offenen Mund vor dem Tischschlag.
- Zylla: junge deutsche Charakterstimme „Skittle Bee – Fresh and Interested“ `xLCJR8xcZX2YjImGFyGw`, nur ein erschöpfter nonverbaler Seufzer. Kein Wort-Caption für den Laut.
- Effektaufnahmen aus ElevenLabs, gekoppelt an Scanner, Rückblende, Uhr/Raum, Tischkontakt, Aufnahme, kurze Projektion, Schild und Papierkreuz. Tischschlag laut und mit scharfem Attack, Endmischung begrenzt.
- Normaussprache unter § 200 klassisch: „Paragraf einhundertsechsunddreißig A“. Schrift in Caption und Bild `§ 136a`; im zweiten Hologramm `§ 136a Abs. 3 StPO`.
- Ruhige Wort-für-Wort-Captions in Nimbus Sans, weiß/fett, mittig unten mit `MarginV 280`, nur gesprochene Erzähler- und Figurenwörter. Brakks „Jetzt rede!“ erhält Captions, Zyllas Seufzer nicht.

**Abnahme:** finale MP4 komplett mit Ton auf Handygröße ansehen. Besonders Schrift und Unterschrift in erstem und letztem Bild, beide Hologrammnormen, zeitliche Trennung zwischen Brakks Ruf, Faustkontakt und Zyllas Aussage, Natürlichkeit beider Charakterstimmen, Lautheitsverhältnis, goldene Figurentreue und ruhigen Schnitt prüfen. Ein technisch erfolgreicher GitHub-Lauf ersetzt diese kreative Abnahme nicht.
