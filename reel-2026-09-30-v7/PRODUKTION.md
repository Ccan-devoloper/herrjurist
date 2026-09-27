# 30.09. § 136a StPO – Prüffassung v7

Testbranch codex/reel-test-20260930-v7-ruhiger-schnitt. Kein geplanter Reel-Slot wird vor Nutzerprüfung ersetzt.

## Redaktion

Hook: Zylla hat ihre Einwilligung unterschrieben, die Aussage bleibt dennoch unverwertbar. Eine kurze Rückblende zeigt, dass Brakk sie gezielt die ganze Nacht wach hält und sie immer wieder wegnickt. Aufnahme-Klick vor dem Tischschlag; Brakk sagt „Nicht einschlafen! Rede endlich!“, Zylla antwortet hörbar und erschöpft „Ich war’s.“ Anschließend erscheint ihre Einwilligung. Die Normprojektionen nennen § 136a StPO und Abs. 3, die Pointe lautet: Auch Einwilligung heilt die unverwertbare Aussage nicht.

Der Sprechertext wurde für die gespielte Form gekürzt und zeitlich freigestellt. Die bekannte Erzählerstimme Moritz bleibt für Kontinuität; Brakk und Zylla behalten ihre Figurenstimmen. Eleven v3 steuert Zyllas erschöpfte Darbietung, während der Erzähler bei Multilingual v2 bleibt. Zyllas sehr leise generierte Sprachspur wird in der Mischung angehoben, damit „Ich war’s“ verständlich bleibt. Die Figurenlaute und gesprochenen Worte werden nur an sichtbarer Handlung eingesetzt. Die ElevenLabs-Takes des ersten erfolgreichen Renderlaufs (29,73 s) sind als Audiodateien und zugehörige Zeichenzeiten im Testbranch fixiert, damit die natürliche Schwankung neuer TTS-Durchläufe nicht über 30 s führt.

## Bild, Ton und QA

30 fps, vertikal 1080 × 1920, Ziel höchstens etwa 30 s. Keine digitalen Zooms, keine schnellen Ganzbildüberblendungen oder Übergänge zwischen nicht registrierten generierten Figuren. Stattdessen halten Einstellungen über ganze Gedanken: Unterschrift, nächtliche Übermüdung, Aufnahme und Schlag, Geständnis, Einwilligung, § 136a, Abs. 3 und Pointe. Die erste Normprojektion steht zunächst fast drei Sekunden, dann folgt ein ruhiger Rückschnitt auf Zyllas erschöpftes Gesicht. Der Schlag besitzt ein eigenständig aus dem Slam-Keyframe generiertes Nachschlag-Cel und eine deutlich längere Reaktion. Recorder-Wellenform erscheint erst in der späteren Geständnis-Einstellung nach dem Klick. Die Schlagwirkung kommt von präzisem Ton, Schlagpose und Halten des Bildes, nicht von Kamera-Zittern.

Alle Bildtexte (Einwilligung und juristische Hologramme) stammen aus den generierten Masters der V4; die neue Reaktionspose ist ohne neuen Bildtext generiert. Captions werden weiterhin aus den exakten ElevenLabs-Zeichenzeiten als ruhige Sinngruppen unten gesetzt, mit juristischer Schriftform § 136a und Abs. 3. Tatsächlich gesprochene Figurenworte werden mitbeschriftet, wortlose Laute nicht.

Golden References: references/golden/brakk-quarzfaust.jpg und references/golden/zylla-glitch.jpg. Die neue Nachschlagpose wurde mit beiden verglichen. Der Zeichenstil soll konturierter 2D-Cartoon bleiben, nur die Übergänge und Aktionsinszenierung sind vom Anime-Kino inspiriert.

Vor Freigabe das gesamte GitHub-Video mit Ton prüfen: exakte Abfolge Klick → Schlag → Brakk → Zylla → Einwilligung, die Schlaghaltung von ungefähr zwei Sekunden, keine Gesichts-Doppelkonturen, keine unerwünschten Zooms, Text auf Bild und Captions lesbar, und Schlussaussage rechtlich korrekt. Die v7-Bildgestaltung verwendet weiterhin vorhandene V4-Keyframes und erreicht deshalb noch keine durchgängig neue zeichnerische Stilfassung.
