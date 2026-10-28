# Blasen im Pinselstil (Variante E)

- **Form:** Comical.js 0.4.2 (SIL/Bloom, MIT), Stile `speech` und `thought`. Der Schwanz zeigt auf den Mund, die Gedankenpunkte laufen zum Kopf.
- **Kontur:** perfect-freehand 1.2.3 (MIT). Die Comical-Kontur wird abgetastet und als Pinselstrich (ca. 4,5–6,5 px) neu gezeichnet.
- **Einzige Änderung an Comical.js:** In der ArcTail-Klasse von `dist/index.js` wird `const tailWidth = 18;` zu `window.TAILW || 18`. `blase_e.js` setzt `TAILW = 58`, damit der Schwanz bei 1080p nicht nadeldünn wirkt.

## Einrichtung

`npm i`, dann erzeugen:
- `comical_p.js` per `sed 's/const tailWidth = 18;/const tailWidth = window.TAILW || 18;/' node_modules/comicaljs/dist/index.js`
- `pf.js`: `perfect-freehand/dist/cjs/index.js` in `var PF={};(function(exports){…})(PF);` eingewickelt

## Aufruf

`bausteine.blase(...)` ruft `node blase_e.js spec.json out.png` auf und cacht das Ergebnis nach Spec-Hash. Die Browser-Pipeline zeichnet nur die Blase. Den Text setzt der Renderer in Nunito.

## Stil C (Serienstandard für Sprechblasen seit 02.10.2026)

`blase_c.js` zeichnet den Blasenkörper aus Comical.js ohne Schwanz und setzt einen eigenen, leicht gebogenen Keil-Schwanz an (Basis `basis`, Standard 44 px, Krümmung `bogen`, Standard 0,10). paper.js (MIT) vereint beides zu **einer** Fläche, perfect-freehand zieht sie einmal nach. Dadurch entstehen am Schwanzansatz keine Schleifen und Doppelstriche mehr. `bausteine.blase` nutzt Stil C für Sprechblasen, solange `BLASEN_STIL` nicht auf `e` gesetzt ist. Liegt die Spitze innerhalb der Blase, fällt es auf `blase_e.js` zurück. Denkblasen laufen immer über `blase_e.js`. Folgen bis 058 bleiben unverändert.
