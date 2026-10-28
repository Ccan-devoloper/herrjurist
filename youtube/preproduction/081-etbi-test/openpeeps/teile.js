// Rendert je Figur zwei deckungsgleiche SVGs: Körper (Füllung Magenta = Farbflächen-Marker) und Kopf (Füllung = Hautfarbe)
const React = require('react');
const { renderToStaticMarkup } = require('react-dom/server');
const Peep = require('react-peeps').default;
const fs = require('fs');
const specs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3];
for (const s of specs) {
  const vb = s.bust ? undefined : { x: '-600', y: '-100', width: '3000', height: '4500' };
  const base = { body: s.body, face: s.face, hair: s.hair, facialHair: s.facialHair || 'None', accessory: s.accessory || 'None', strokeColor: '#111111', viewBox: vb };
  const svgK = renderToStaticMarkup(React.createElement(Peep, { ...base, backgroundColor: '#FF00FF' }));
  const svgH = renderToStaticMarkup(React.createElement(Peep, { ...base, backgroundColor: s.haut || '#F2C9A5' }));
  const fix = (x) => x.includes('xmlns=') ? x : x.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
  // Top-Level: <svg><g> [Körper-g] [Kopf-g] </g></svg> – jeweils das andere Teil entfernen
  const split = (svg) => {
    const start = svg.indexOf('<g>') + 3;
    let depth = 0, i = start, parts = [];
    let cur = i;
    const re = /<\/?g[^>]*>/g; re.lastIndex = start;
    let m;
    while ((m = re.exec(svg))) {
      if (m[0].startsWith('</')) { if (depth === 0) break; depth--; if (depth === 0) { parts.push([cur, re.lastIndex]); cur = re.lastIndex; } }
      else if (!m[0].endsWith('/>')) { if (depth === 0) cur = m.index; depth++; }
    }
    return parts;
  };
  const pk = split(svgK), ph = split(svgH);
  if (pk.length < 2) throw new Error('Struktur unerwartet: ' + s.name);
  const nurKoerper = svgK.slice(0, pk[1][0]) + svgK.slice(pk[pk.length - 1][1]);
  const nurKopf = svgH.slice(0, ph[0][0]) + svgH.slice(ph[0][1]);
  fs.writeFileSync(`${out}/${s.name}_koerper.svg`, fix(nurKoerper));
  fs.writeFileSync(`${out}/${s.name}_kopf.svg`, fix(nurKopf));
}
console.log(specs.length, 'Figuren');
