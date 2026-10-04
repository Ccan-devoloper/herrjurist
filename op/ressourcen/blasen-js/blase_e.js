// Sprech-/Gedankenblase im Pinselstil: Form aus Comical.js (MIT), Kontur mit perfect-freehand (MIT) nachgezogen.
// Aufruf: node blase_e.js spec.json out.png   spec: {art, x, y, w, h, tip:[x,y], mid:[x,y], fill}
const { chromium } = require('playwright-core');
const fs = require('fs');
(async () => {
  const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || require('playwright-core').chromium.executablePath(), args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  p.on('pageerror', e => { console.error('ERR', e.message); process.exit(1); });
  await p.goto('file://' + __dirname + '/leer.html');
  await p.evaluate(async (s) => {
    window.TAILW = 58;
    const {Comical, Bubble} = window.ComicalJS;
    Bubble.defaultBorderWidth = 0.01;
    const par = document.getElementById('p');
    const d = document.createElement('div'); d.className = 'b';
    Object.assign(d.style, {left: s.x + 'px', top: s.y + 'px', width: s.w + 'px', height: s.h + 'px'});
    par.appendChild(d);
    const sp = Bubble.getDefaultBubbleSpec(d, s.art === 'denk' ? 'thought' : 'speech');
    sp.tails = [{tipX: s.tip[0], tipY: s.tip[1], midpointX: s.mid[0], midpointY: s.mid[1], autoCurve: false}];
    sp.backgroundColors = [s.fill || '#ffffff']; sp.shadowOffset = 0;
    new Bubble(d).setBubbleSpec(sp);
    Comical.startEditing([par]);
    await new Promise(r => setTimeout(r, 300));
    Comical.stopEditing();
    await new Promise(r => setTimeout(r, 200));
    const svg = par.querySelector('svg.comical-generated');
    Object.assign(svg.style, {position: 'absolute', left: 0, top: 0});
    const ns = 'http://www.w3.org/2000/svg';
    const over = document.createElementNS(ns, 'svg');
    over.setAttribute('width', 1920); over.setAttribute('height', 1080);
    Object.assign(over.style, {position: 'absolute', left: 0, top: 0});
    par.appendChild(over);
    for (const el of svg.querySelectorAll('path,circle,ellipse')) {
      const f = el.getAttribute('fill');
      if (!((f && f !== 'none' && !/url\(/.test(f)) || (el.getAttribute('stroke') && el.getAttribute('stroke') !== 'none'))) continue;
      const L = el.getTotalLength(); if (L < 10) continue;
      const m = el.getCTM(), pts = [], steps = Math.max(24, Math.round(L / 6));
      for (let i = 0; i <= steps; i++) {
        const q = el.getPointAtLength(L * i / steps);
        pts.push([m.a * q.x + m.c * q.y + m.e, m.b * q.x + m.d * q.y + m.f]);
      }
      const st = PF.getStroke(pts.concat([pts[1]]), {size: L < 120 ? 4.5 : 6.5, thinning: 0.55, smoothing: 0.6, streamline: 0.35,
                                                     simulatePressure: true, last: true, start: {taper: 0}, end: {taper: 0}});
      const path = document.createElementNS(ns, 'path');
      path.setAttribute('d', 'M' + st.map(q => q[0].toFixed(1) + ' ' + q[1].toFixed(1)).join('L') + 'Z');
      path.setAttribute('fill', '#151515'); over.appendChild(path);
    }
  }, spec);
  await p.screenshot({ path: process.argv[3], omitBackground: true });
  await b.close();
})();
