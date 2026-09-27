# 30.09. § 136a StPO — animierte Prüffassung v5

Ausgangsstand ist die freigegebene Story, Sprecherfassung und Bildfolge aus `reel-2026-09-30-v4/`. Diese Prüffassung ersetzt keinen geplanten Slot. Produktion per GitHub Actions mit `.github/workflows/reel-cartoon-20260930-v5.yml` auf `codex/reel-test-20260930-v5-motion`.

## Korrektur aus Sichtprüfung

- Lange ruhige Einstellungen brauchen kleines, motiviertes Spiel **innerhalb** des Bildes, nicht zusätzliche willkürliche Nah-Weit-Schnitte.
- 4,63–5,36 s: Brakk schließt den Mund und spannt den Kiefer an; die Kamera bleibt stehen.
- 6,89–8,48 s: neu generierte Brakk-Pose mit leicht vorgebeugter Schulter und festerem Griff; Zylla kämpft kurz gegen zufallende Augenlider.
- 10,55–12,60 s: generierte Zylla-Variante öffnet die Augen und formt müde Silben, synchron zur Aussage. Dieselbe Pose sorgt bei 14,27–15,43 s, 17,20–19,07 s und 19,92–20,77 s für sparsame Reaktionen im Normteil; Brakk reagiert bei 15,51–16,06 s.
- 21,3 s: knapper Lichtakzent auf dem rechtlichen Schild ohne Kamerazittern. Nach dem X auf der weiterhin unterschriebenen Urkunde bei ca. 24,38 s sinkt Brakks Hand und sein Gesicht bei 26,00 s; letzter Fokus auf Papier und Reaktion ab 26,99 s.
- Die Normtexte `§ 136a StPO / ERMÜDUNG` und `§ 136a Abs. 3 StPO / EINWILLIGUNG` sind weiterhin Teil der generierten Bilder, keine nachträgliche Schreibfläche. Dokument, Aufschrift, rotes X und Unterschrift bleiben im Bild.
- Die bereits freigegebenen einwortigen Captions bleiben unverändert; der Screenshot mit 2–4-Wort-Chunks war ausdrücklich von der früheren Änderungsbitte ausgenommen.

## Bilder, Ton und Export

Die drei neuen Cels `02-brakk-tense`, `04-zylla-glance` und `08-brakk-deflated` wurden als eng geführte Edits der vorhandenen Bilder mit den Golden References für Brakk und Zylla erstellt. Alle anderen Cels werden aus `reel-2026-09-30-v4/masters/` bezogen. `make_frames.py` steuert die Posen mit kurzen Überblendungen und begrenzten Gesichtsmasken; der Hintergrund bleibt still und der Bildausschnitt zittert nicht. Die Texte auf Papier und Projektion werden nicht compositorseitig neu gesetzt.

`render.mjs` generiert mit den etablierten ElevenLabs-Stimmen (`PhufIH7nYh2Up1uej6aY`, `JiW03c2Gt43XNUQAumRP`, `xLCJR8xcZX2YjImGFyGw`) und den acht handlungsgebundenen Geräuschen; Sprecher, Brakks „Jetzt rede!“ und Zyllas Seufzer behalten ihre jeweiligen Einsätze. Der Export ist 1080×1920 H.264/AAC, 30 fps und ungefähr 28 Sekunden.

## Qualitätskontrolle

V5 anhand der Gesamt-MP4 und Kontaktbögen gegen die bisherigen Standbilder, Figurenidentitäten, Requisiten, exakten Bildtext, Zeitpunkt der Reaktion und Caption-Position prüfen. Speziell die langsamen Abschnitte 3,7–12,9 s, 13,6–21,3 s und 21,3–27,8 s in Echtzeit ansehen. Keine Freigabe allein anhand der generierten Einzelbilder.
