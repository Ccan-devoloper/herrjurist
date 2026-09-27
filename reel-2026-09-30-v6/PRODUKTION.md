# 30.09. § 136a StPO — Prüffassung v6: Sinngruppen und Schlussbewegung

Testbranch `codex/reel-test-20260930-v6-captions`; automatischer Render `.github/workflows/reel-cartoon-20260930-v6.yml`. Ausgangspunkt sind Figuren, Text und Animationscels der V5; unveränderte Keyframes der V4 bleiben per Repo-Fallback eingebunden. Kein geplanter Reel-Slot wird vor Prüfung ersetzt.

## Änderungen nach erneuter Sichtprüfung

1. Sprecheruntertitel sind kurze, vorher redigierte Sinngruppen statt einzeln springender Wörter. Beispiele: „Brakk hält Zylla“ / „die ganze Nacht wach.“ / „Stunde um Stunde.“ Die genaue Ein- und Ausblendung kommt aus den ElevenLabs-Zeichenzeiten. Normen bleiben juristisch korrekt (`§ 136a`, `Abs. 3:`), Brakks „Jetzt rede!“ ist eine eigene Einblendung; Zyllas wortloser Seufzer bleibt ohne Caption. Erstes „Unterschrieben.“, „Warum?“ und „Zurück.“ stehen bewusst allein als Hook/Punktuation. Die freigegebene Schriftart, Farbe, Kontur und Position unten bleiben; die Wortskalierung ist entfernt, eine dezente Blende von 70 ms genügt. Die Sinngruppen sind vorerst ein Test und ändern die allgemeine Captions-Leitlinie nicht ohne Freigabe.
2. Im Normabschnitt ist die bereits als Bildteil generierte Projektion kurz und reduziert (`§ 136a StPO / ERMÜDUNG`, dann `§ 136a Abs. 3 StPO / EINWILLIGUNG`). Die Caption während der ersten Projektion ist lediglich `§ 136a`; die übrige Erklärung folgt überwiegend auf den Figurenbildern. Die Normgrafik selbst und ihr Text wurden nicht nachträglich aufgeklebt oder geändert.
3. Der Recorder-Einschub ist eng auf Gerät und Hand kadriert und dauert nur 0,61 Sekunden um das tatsächliche Klickgeräusch herum. Er ist damit motivierter Teil von „Das Gerät nimmt auf.“ statt ein zufälliger Spätsprung.
4. Im Schlussabschnitt kommt nach dem roten X und Brakks Reaktion eine einzige zusätzliche kleine Bewegung: Zylla hebt den Stift von derselben unterschriebenen Urkunde weg. Die neue Pose `09-pen-away.jpg` wurde aus dem V5-Schlussbild mit Zylla-Golden-Reference generiert. Text, Signatur und X wurden bei der Bildbearbeitung mitgeneriert und geprüft; die Perspektive bleibt gleich.

## Render und Qualitätskontrolle

`render.mjs` rendert auf GitHub die bestehende Erzählstimme, Brakks Stimme und Zyllas Seufzer mit den bekannten ElevenLabs Voice IDs, die bestehenden acht SFX und die neue 30-fps-Animation. Die lokale Vorschau benutzte exakt die vom V5-GitHub-Lauf erzeugten Audiodateien, um nur Bild/Caption zu vergleichen; für die zu prüfende Ausgabe zählt der neue GitHub-Export. Projektziel ca. 27,8 Sekunden, 1080 × 1920, H.264/AAC.

Vor Freigabe vollständiges Video mit Ton und Lesbarkeit prüfen; insbesondere Recorder-Klick samt 0,61-s-Insert, Bildtext und Caption-Konkurrenz 13–21 s, Signatur und X sowie den Stiftabschluss. Nicht nur anhand einzelner Stills freigeben.
