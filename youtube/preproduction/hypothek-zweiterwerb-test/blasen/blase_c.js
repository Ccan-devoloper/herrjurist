// Sprechblase Stil C (Serienstandard seit 02.10.2026): Blasenkörper aus Comical.js (MIT, ohne Schwanz) plus eigener,
// leicht gebogener Keil-Schwanz, mit paper.js (MIT) zu EINER Fläche vereint und einmal mit perfect-freehand (MIT)
// nachgezogen. Keine Innenlinie, keine Schleife am Ansatz. Denkblasen weiter über blase_e.js.
// Aufruf: node blase_c.js spec.json out.png   spec: {art:'sprech', x, y, w, h, tip:[x,y], basis?, bogen?}
const { chromium } = require('playwright-core');
const fs = require('fs');
(async () => {
  const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('pageerror', e => { console.error('ERR', e.message); process.exit(1); });
  await p.goto('file://' + __dirname + '/leer.html');
  await p.evaluate(async (s) => {
    const {Comical, Bubble} = window.ComicalJS;
    Bubble.defaultBorderWidth = 0.01;
    const par = document.getElementById('p');
    const d = document.createElement('div'); d.className = 'b';
    Object.assign(d.style, {left: s.x + 'px', top: s.y + 'px', width: s.w + 'px', height: s.h + 'px'});
    par.appendChild(d);
    const sp = Bubble.getDefaultBubbleSpec(d, 'speech'); sp.tails = []; sp.backgroundColors = ['#ffffff']; sp.shadowOffset = 0;
    new Bubble(d).setBubbleSpec(sp);
    Comical.startEditing([par]); await new Promise(r => setTimeout(r, 300));
    Comical.stopEditing(); await new Promise(r => setTimeout(r, 200));
    const svg = par.querySelector('svg.comical-generated'); svg.style.display = 'none';
    const el = [...svg.querySelectorAll('path')].filter(e => { const f = e.getAttribute('fill'); return f && f !== 'none' && !/url\(/.test(f); })
                 .sort((a, b) => b.getTotalLength() - a.getTotalLength())[0];
    paper.setup(new paper.Size(1920, 1080));
    const m = el.getCTM();
    let body = paper.project.importSVG(el.outerHTML.replace(/<path/, '<path xmlns="http://www.w3.org/2000/svg"'));
    body.transform(new paper.Matrix(m.a, m.b, m.c, m.d, m.e, m.f));
    if (body.children) body = body.children.reduce((x, y) => (Math.abs(y.area||0) > Math.abs(x.area||0) ? y : x));
    // Ansatzpunkt: Schnitt der Linie Mitte→Spitze mit dem Blasenrand
    const c = body.bounds.center, tip = new paper.Point(s.tip[0], s.tip[1]);
    const ray = new paper.Path.Line(c, tip);
    const hits = body.getIntersections(ray); ray.remove();
    if (!hits.length) throw new Error('Schwanzspitze liegt innerhalb der Blase');
    const hit = hits[0];
    const P = hit.point, off = body.getOffsetOf(P);
    const bw = s.basis || 44;
    const a = body.getPointAt((off - bw / 2 + body.length) % body.length), z = body.getPointAt((off + bw / 2) % body.length);
    const nach = c.subtract(P).normalize(14);           // Basis etwas ins Innere, damit die Vereinigung sauber ist
    const dir = tip.subtract(P), nrm = new paper.Point(-dir.y, dir.x).normalize(dir.length * (s.bogen || 0.10));
    const keil = new paper.Path({ closed: true });
    keil.moveTo(a.add(nach));
    keil.quadraticCurveTo(P.add(dir.multiply(0.55)).add(nrm).add(dir.normalize(-6)), tip);
    keil.quadraticCurveTo(P.add(dir.multiply(0.45)).add(nrm), z.add(nach));
    keil.closePath();
    let u = body.unite(keil);
    if (u.children) u = u.children.reduce((x, y) => (Math.abs(y.area) > Math.abs(x.area) ? y : x));
    const ns = 'http://www.w3.org/2000/svg';
    const over = document.createElementNS(ns, 'svg');
    over.setAttribute('width', 1920); over.setAttribute('height', 1080);
    Object.assign(over.style, {position: 'absolute', left: 0, top: 0}); par.appendChild(over);
    const fl = document.createElementNS(ns, 'path'); fl.setAttribute('d', u.pathData); fl.setAttribute('fill', '#ffffff'); over.appendChild(fl);
    const L = u.length, pts = [], steps = Math.round(L / 5);
    for (let i = 0; i <= steps; i++) { const q = u.getPointAt(L * i / steps); pts.push([q.x, q.y]); }
    const st = PF.getStroke(pts.concat([pts[1]]), {size: 6.5, thinning: 0.55, smoothing: 0.6, streamline: 0.35,
                                                   simulatePressure: true, last: true, start: {taper: 0}, end: {taper: 0}});
    const path = document.createElementNS(ns, 'path');
    path.setAttribute('d', 'M' + st.map(q => q[0].toFixed(1) + ' ' + q[1].toFixed(1)).join('L') + 'Z');
    path.setAttribute('fill', '#151515'); over.appendChild(path);
  }, spec);
  await p.screenshot({ path: process.argv[3], omitBackground: true });
  await b.close();
})();
