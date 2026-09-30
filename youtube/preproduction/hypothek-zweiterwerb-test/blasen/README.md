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
