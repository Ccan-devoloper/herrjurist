/* LexVerse-Wochenbrief als PDF-Vorlage (A4, druckfertig). Aus einer Ausgabe-JSON entsteht HTML,
   das bin/wochenbrief-pdf.mjs mit Chromium in ein PDF druckt. Aufbau:
   Titelseite mit Inhaltsverzeichnis → je Fall ab neuer Seite: Wissen, Minifall und direkt darunter die
   Lösung mit Definitionen, Streitständen und Fehlerklassikern → Methodenseiten → 60-Sekunden-Check. */

const BEREICHE = {
  zivil: { farbe: '#2D5BE3', hell: '#8DB3F2', zart: '#E6EEFC' },
  straf: { farbe: '#FF7A45', hell: '#F9A66C', zart: '#FFEBDD' },
  oeff: { farbe: '#18B877', hell: '#8FD694', zart: '#E3F6E6' },
  methode: { farbe: '#7C5CFF', hell: '#C9B8FF', zart: '#EFEAFF' },
};

const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
// (+) und (−) in der Gliederung hervorheben
const ergebnis = s => esc(s).replace(/\((\+|−|-)\)/g, (_, z) => `<b class="${z === '+' ? 'plus' : 'minus'}">(${z})</b>`);
const datumDe = iso => new Intl.DateTimeFormat('de-DE', { timeZone: 'UTC', day: 'numeric', month: 'long', year: 'numeric' }).format(new Date(`${iso}T00:00:00Z`));

function pille(text, bg = '#fff') { return `<span class="pille" style="background:${bg}">${esc(text)}</span>`; }

function kopfzeile(a, f) {
  const b = BEREICHE[f.bereich];
  return `<div class="kopf" style="background:${b.farbe}">
    <span class="kopf-nr">${esc(f.nr)}</span>
    <span class="kopf-feld">${esc(a.bereiche[f.bereich].titel)} · ${esc(f.feld)}</span>
    <span class="kopf-aus">Wochenbrief ${String(a.nr).padStart(2, '0')}</span>
  </div>`;
}

function normen(f) {
  if (!f.normen?.length) return '';
  return `<div class="normen"><b>Im Gesetz:</b> ${f.normen.map(n => `<a href="${esc(n.url)}">${esc(n.label)}</a>`).join(' · ')}</div>`;
}

function figur(f, bild) {
  if (!f.figur) return '';
  return `<div class="figur"><img src="${bild(f.figur)}" alt="">${f.sprechblase ? `<div class="blase">${esc(f.sprechblase)}</div>` : ''}</div>`;
}

function fallseite(a, f, bild) {
  const b = BEREICHE[f.bereich];
  return `<section class="seite fall" style="--farbe:${b.farbe};--hell:${b.hell};--zart:${b.zart}">
    ${kopfzeile(a, f)}
    <h2><span class="mark">${esc(f.titel)}</span></h2>
    <p class="einstieg">${esc(f.einstieg)}</p>
    ${f.klassiker ? `<p class="klassiker"><span>Klausurklassiker</span> ${esc(f.klassiker)}</p>` : ''}
    <div class="spalten">
      <div class="box wissen">${pille('Das musst du wissen')}<p>${esc(f.wissen)}</p></div>
      <div class="box minifall">${pille('Minifall · du bist dran')}<p>${esc(f.minifall)}</p>${figur(f, bild)}</div>
    </div>
    ${loesung(f)}
    ${normen(f)}
  </section>`;
}

function methodenseite(a, f, bild) {
  const b = BEREICHE[f.bereich];
  const absatz = t => {
    // „1. … 2. … 3. …“ als Schrittliste setzen
    const schritte = t.split(/\s(?=\d\.\s)/);
    if (/^1\.\s/.test(t) && schritte.length > 1) return `<ol class="schritte">${schritte.map(s => `<li>${esc(s.replace(/^\d\.\s*/, ''))}</li>`).join('')}</ol>`;
    const [titel, ...rest] = t.split(/:\s/);
    return rest.length && titel.length < 30 ? `<p><b>${esc(titel)}:</b> ${esc(rest.join(': '))}</p>` : `<p>${esc(t)}</p>`;
  };
  return `<section class="seite fall methode" style="--farbe:${b.farbe};--hell:${b.hell};--zart:${b.zart}">
    ${kopfzeile(a, f)}
    <h2><span class="mark">${esc(f.titel)}</span></h2>
    <p class="einstieg">${esc(f.einstieg)}</p>
    <div class="spalten">
      <div class="box wissen">${pille('So gehst du vor')}${(f.text || []).map(absatz).join('')}</div>
      <div class="box minifall kurz">${figur(f, bild)}</div>
    </div>
    ${normen(f)}
  </section>`;
}

const HINWEIS = { definition: 'Definition', streit: 'Streitstand', fehler: 'Fehlerklassiker', merke: 'Merke' };

function hinweis(h) {
  return `<div class="hinweis ${esc(h.typ)}"><div class="h-kopf"><span class="h-typ">${HINWEIS[h.typ] ?? esc(h.typ)}</span> ${esc(h.titel.replace(/^(Fehlerklassiker|Streitstand|Merke|Definition):\s*/, ''))}</div><p>${esc(h.text)}</p></div>`;
}

function loesung(f) {
  return `<div class="loesung">
    <div class="l-kopf"><span class="pille" style="background:var(--hell)">Lösung</span><span class="l-sub">Kurzgliederung im Klausurschema</span></div>
    <div class="gliederung">${f.gliederung.map(z => `<div class="zeile e${z.ebene}"><div>${ergebnis(z.text).replace(/^(\S+)\s/, '<span class="m">$1</span> ')}</div>${(z.hinweise || []).map(hinweis).join('')}</div>`).join('')}</div>
    ${f.falle ? `<div class="falle"><b>⚠ Falle:</b> ${esc(f.falle)}</div>` : ''}
  </div>`;
}

export function rendereWochenbriefPdfHtml(a, { bild = name => name, schriften = 'fonts/' } = {}) {
  const faelle = a.faelle.filter(f => f.minifall);
  const methoden = a.faelle.filter(f => !f.minifall);
  const reihenfolge = Object.keys(a.bereiche);
  const inhalt = reihenfolge.map(k => {
    const liste = a.faelle.filter(f => f.bereich === k);
    if (!liste.length) return '';
    return `<div class="inhalt-gruppe" style="--farbe:${BEREICHE[k].farbe}"><div class="inhalt-titel">${esc(a.bereiche[k].titel)}</div>
      ${liste.map(f => `<div class="inhalt-zeile"><span class="i-nr">${esc(f.nr)}</span><span class="i-titel">${esc(f.titel)}</span><span class="i-seite" data-fall="${esc(f.nr)}"></span></div>`).join('')}</div>`;
  }).join('');
  const farben = ['zivil', 'straf', 'oeff'].map(k => BEREICHE[k].hell);

  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Wochenbrief ${String(a.nr).padStart(2, '0')} · LexVerse</title>
<style>
@font-face{font-family:Nunito;font-weight:400 799;src:url(${schriften}nunito-700.woff2)}
@font-face{font-family:Nunito;font-weight:800 1000;src:url(${schriften}nunito-900.woff2)}
@font-face{font-family:Gochi;src:url(${schriften}gochi-hand.woff2)}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font:500 10.5pt/1.45 Nunito,sans-serif;color:#16161d;background:#FFF8EC}
a{color:#583EBE;font-weight:800;text-decoration:none}
.seite{width:210mm;height:297mm;padding:16mm 16mm 14mm;position:relative;overflow:hidden;break-after:page;background:#FFF8EC}
.pille{display:inline-block;border:solid #16161d;border-width:1.5px 3px 3px 1.5px;border-radius:99px;padding:1.5px 9px;font:800 8.5pt Nunito}
.hand{font-family:Gochi,cursive}
/* Titelseite */
.titel{background:#7C5CFF;color:#fff;padding:0}
.titel .oben{padding:16mm 16mm 0}
.titel .meta{display:flex;justify-content:space-between;align-items:center}
.titel .meta .pille{color:#16161d}
.titel .hand{color:#FFDE59;font-size:20pt;margin:12mm 0 2mm;display:block;transform:rotate(-1.5deg)}
.titel h1{font:900 42pt/1.15 Nunito;margin:0;max-width:130mm}
.titel h1 span{color:#16161d;padding:0 8px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.titel .deck{font:700 12pt/1.5 Nunito;margin:6mm 0 0;max-width:92mm}
.titel .held{position:absolute;right:10mm;top:104mm;width:86mm;z-index:1}
.titel .unten{position:absolute;left:0;right:0;bottom:0;height:150mm;background:#FFF8EC;color:#16161d;padding:16mm 16mm 12mm}
.titel .welle{position:absolute;left:0;right:0;top:-9mm;height:10mm;background:radial-gradient(10mm 7mm at 10mm 0,#7C5CFF 98%,transparent) 0 0/20mm 10mm repeat-x}
.schritte3{display:flex;gap:4mm;margin-bottom:7mm}
.schritte3 div{flex:1;background:#fff;border:solid #16161d;border-width:1.5px 4px 4px 1.5px;border-radius:12px;padding:3mm;text-align:center;font:800 9.5pt/1.3 Nunito}
.schritte3 b{display:inline-block;font:900 15pt Nunito;padding:0 7px;border-radius:7px;margin-bottom:1mm}
.inhalt{columns:2;column-gap:8mm}
.inhalt-gruppe{break-inside:avoid;margin-bottom:4mm}
.inhalt-titel{font:900 10pt Nunito;color:var(--farbe);border-bottom:2px solid var(--farbe);margin-bottom:1.5mm;padding-bottom:.5mm}
.inhalt-zeile{display:flex;gap:2mm;font:700 9pt/1.35 Nunito;padding:.8mm 0}
.i-nr{color:var(--farbe);font-weight:900;width:5mm}.i-titel{flex:1}.i-seite{color:#5c5c68;font-weight:900}
/* Fallseite: beginnt auf neuer Seite und darf auf die nächste fließen */
.fall{height:auto;min-height:297mm;overflow:visible;box-decoration-break:clone;-webkit-box-decoration-break:clone;padding-bottom:12mm}
.kopf{display:flex;align-items:center;gap:3mm;color:#fff;border:2px solid #16161d;border-radius:12px;padding:2mm 4mm;font:800 10pt Nunito}
.kopf-nr{background:#fff;color:#16161d;border-radius:7px;padding:0 6px;font:900 11.5pt Nunito}
.kopf-feld{flex:1}.kopf-aus{opacity:.85}
.fall h2{font:900 20pt/1.25 Nunito;margin:5mm 0 2.5mm}
.mark{background:var(--hell);padding:0 5px;border-radius:7px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.einstieg{font:600 11.5pt/1.5 Nunito;margin:0 0 2.5mm;color:#2d2d36}
.klassiker{font:700 10.5pt/1.45 Nunito;margin:0 0 4mm}
.klassiker span{background:#FFDE59;border-radius:5px;padding:.3mm 5px;font-weight:900;margin-right:2px}
.spalten{display:grid;grid-template-columns:1fr 1fr;gap:5mm;break-inside:avoid}
.box{border:2px solid #16161d;border-radius:14px;padding:4mm;font:500 10.5pt/1.5 Nunito;display:flex;flex-direction:column}
.box p{margin:2.5mm 0 0}
.box>.pille{align-self:flex-start}
.wissen{background:#fff}
.minifall{background:var(--zart);border-color:var(--farbe);border-width:2px 5px 5px 2px}
.minifall>p{font:800 11pt/1.5 Nunito}
.figur{margin-top:auto;display:flex;align-items:flex-end;gap:2mm;padding-top:3mm}
.figur img{height:30mm;width:auto}
.blase{background:#fff;border:2px solid #16161d;border-radius:14px 14px 14px 3px;padding:2mm 3.5mm;font:800 10pt/1.3 Nunito;margin-bottom:18mm}
.minifall.kurz{justify-content:flex-end}
.loesung{margin-top:6mm}
.l-kopf{display:flex;align-items:center;gap:3mm;margin-bottom:3mm}
.l-sub{font:700 9.5pt Nunito;color:#5c5c68}
.gliederung{border-left:3px solid var(--farbe);padding-left:4mm;font:500 10.5pt/1.5 Nunito}
.zeile{margin:1mm 0;break-inside:avoid}
.gliederung .m{font-weight:900;display:inline-block;min-width:7.5mm}
.e0>div:first-child{font-weight:800}.e1{margin-left:5.5mm}.e2{margin-left:11mm}.e3{margin-left:16.5mm}.e4{margin-left:22mm}
.plus{color:#138a4e}.minus{color:#D73C2D}
.hinweis{margin:2mm 0 3mm 7.5mm;border:1.5px solid #16161d;border-radius:10px;padding:2.5mm 3.5mm;font:500 9.8pt/1.45 Nunito;background:#fff;break-inside:avoid}
.hinweis p{margin:1mm 0 0}
.h-kopf{font:800 9.8pt/1.35 Nunito}
.h-typ{display:inline-block;border-radius:5px;padding:0 5px;margin-right:3px;font:900 8.5pt/1.6 Nunito;letter-spacing:.03em;text-transform:uppercase}
.definition{background:#F3F7FF}.definition .h-typ{background:#8DB3F2}
.streit{background:#F6F1FF}.streit .h-typ{background:#C9B8FF}
.fehler{background:#FFF3EE}.fehler .h-typ{background:#F9A66C}
.merke{background:#FFFBE3}.merke .h-typ{background:#FFDE59}
.falle{margin-top:4mm;background:#FFF0EA;border:2px solid #16161d;border-radius:12px;padding:3mm 4mm;font:700 10.5pt/1.45 Nunito;break-inside:avoid}
.falle b{color:#D73C2D}
.normen{margin-top:5mm;font:600 9pt Nunito;color:#5c5c68}
.methode .wissen p{margin:2.5mm 0 0}
.schritte{margin:3mm 0 0;padding-left:5mm;font-weight:800}
.schritte li{margin:1.5mm 0}
/* Schluss */
.check{background:#FFF3B0;border:2px solid #16161d;border-radius:14px;padding:5mm;break-inside:avoid}
.check ol{margin:3mm 0 0;padding-left:6mm;font:800 11.5pt/1.5 Nunito}.check li{margin:2mm 0}
</style></head><body>

<section class="seite titel">
  <div class="oben">
    <div class="meta"><span>${pille('LexVerse', '#FFDE59')} ${pille('by herrjurist')}</span>${pille(`Wochenbrief ${String(a.nr).padStart(2, '0')} · ${datumDe(a.datum)}`)}</div>
    <span class="hand">Für Studium, 1. und 2. Staatsexamen</span>
    <h1>${a.hook.map((z, i) => `<span style="background:${farben[i % 3]}">${esc(z)}</span>`).join('<br>')}</h1>
    <p class="deck">${esc(a.deck)}</p>
  </div>
  ${a.bild ? `<img class="held" src="${bild(a.bild)}" alt="">` : ''}
  <div class="unten"><div class="welle"></div>
    <div class="schritte3">
      <div><b style="background:#8DB3F2">1</b><br>Minifall lesen</div>
      <div><b style="background:#F9A66C">2</b><br>Kurz selbst lösen</div>
      <div><b style="background:#8FD694">3</b><br>Mit der Lösung direkt darunter vergleichen</div>
    </div>
    <div class="inhalt">${inhalt}<div class="inhalt-gruppe" style="--farbe:#16161d"><div class="inhalt-titel">Zum Schluss</div><div class="inhalt-zeile"><span class="i-nr">✓</span><span class="i-titel">60-Sekunden-Check</span><span class="i-seite" data-loesungsteil></span></div></div></div>
  </div>
</section>

${faelle.map(f => fallseite(a, f, bild)).join('')}
${methoden.map(f => methodenseite(a, f, bild)).join('')}

<section class="seite schlussseite" id="schluss">
  <div class="check"><span class="pille" style="background:#FFDE59">Dein 60-Sekunden-Check</span><ol>${a.check.map(q => `<li>${esc(q)}</li>`).join('')}</ol></div>
</section>
</body></html>`;
}
