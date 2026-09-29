# Test: Open-Peeps-Figuren statt Personen-Emojis

**Stand 29.09.2026.** Vergleichsfolien (Fall, Irrtümer) und ein 29-s-Clip der Fallszene mit der v2-Tonspur. Figuren aus **Open Peeps** (Pablo Stanley, laut Projekt CC0; Lizenz vor Serieneinsatz auf openpeeps.com gegenlesen, die Seite war aus der Produktionsumgebung gesperrt), bezogen über das npm-Paket `react-peeps` 0.1.10 (MIT, Code). `export.js` rendert je Figur Pose + Gesicht + Haar als SVG (weiße Füllung, schwarze Kontur); Gesichtswechsel laufen als harter Schnitt auf der Wortmarke (ruhig → Angst bei „Messer“ → Wut bei „schlägt“ → Schreck bei „Handy“; B: laufend → verletzt → zeigend).

Nebenbei behoben: Renderer klemmte Sprites mit negativer Position an den Bildrand (`setze()` schneidet jetzt korrekt). v2 und Reel enthielten keine solchen Elemente und sind nicht betroffen (geprüft).
