/* Wochenbrief-Mail (Design „C – Lila Bühne“, passend zur Landingpage). Kurze Mail mit PDF-Link;
   die Fälle selbst stehen nur im PDF. Tabellen und Inline-Stile für Mailprogramme. */

const F = "Nunito,'Segoe UI',Arial,sans-serif";
const FARBE = { zivil: '#2D5BE3', straf: '#FF7A45', oeff: '#18B877', methode: '#7C5CFF' };
const HELL = { zivil: '#8DB3F2', straf: '#F9A66C', oeff: '#8FD694', methode: '#C9B8FF' };
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
const pille = (t, bg = '#fff') => `<span style="display:inline-block;background:${bg};border:solid #111;border-width:2px 4px 4px 2px;border-radius:99px;white-space:nowrap;padding:3px 11px;font:800 13px ${F};color:#111">${esc(t)}</span>`;
const datumKurz = iso => { const [j, m, t] = iso.split('-'); return `${+t}.${+m}.${j}`; };

export function wochenbriefBetreff(a) { return a.betreff ?? `${a.hook.join(' ')} – Wochenbrief ${String(a.nr).padStart(2, '0')}`; }
export function wochenbriefVorschautext(a) {
  const n = a.faelle.filter(f => f.bereich !== 'methode').length;
  return `Dein Wochenbrief als PDF: ${n} Minifälle mit Lösung, Definitionen und Streitständen.`;
}

export function rendereWochenbriefMail(a, { pdfUrl, seiten }) {
  const nr = String(a.nr).padStart(2, '0');
  const letzte = a.hook.length - 1;
  const hook = a.hook.map((z, i) => i === letzte ? `<span style="background:#FFDE59;color:#111;padding:0 6px;border-radius:6px">${esc(z)}</span>` : esc(z)).join(' ');
  const kopf = `<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>${pille('LexVerse', '#FFDE59')} ${pille('by herrjurist')}</td><td align="right">${pille(`Nr. ${nr} · ${datumKurz(a.datum)}`)}</td></tr></table>`;
  const karten = Object.keys(a.bereiche).map(k => {
    const zeilen = a.faelle.filter(f => f.bereich === k).map(f => `<p style="margin:6px 0 0;font:700 14px/1.35 ${F};color:#111"><b style="color:${FARBE[k]}">${esc(f.nr)}</b>&nbsp; ${esc(f.titel)}</p>`).join('');
    return `<td valign="top" width="50%" style="padding:6px"><div style="background:#fff;border:3px solid #111;border-radius:16px;padding:12px"><span style="display:inline-block;background:${HELL[k]};border:2px solid #111;border-radius:8px;padding:2px 8px;font:900 13px ${F};color:#111">${esc(a.bereiche[k].titel)}</span>${zeilen}</div></td>`;
  });
  const zeilen = [];
  for (let i = 0; i < karten.length; i += 2) zeilen.push(`<tr>${karten[i]}${karten[i + 1] ?? '<td width="50%"></td>'}</tr>`);
  const knopf = `<table role="presentation" cellpadding="0" cellspacing="0" align="center"><tr><td style="background:#FFDE59;border:solid #111;border-width:3px 6px 6px 3px;border-radius:14px"><a href="${esc(pdfUrl)}" style="display:inline-block;padding:16px 30px;font:900 19px ${F};color:#111;text-decoration:none">📄 Jetzt als PDF öffnen</a></td></tr></table>`;

  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Wochenbrief ${nr}</title></head>
<body style="margin:0;padding:0;background:#FFF8EC"><div style="display:none;max-height:0;overflow:hidden;opacity:0">${esc(wochenbriefVorschautext(a))}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FFF8EC"><tr><td align="center" style="padding:24px 10px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;border:4px solid #111;border-radius:24px;overflow:hidden;background:#FFF8EC">
<tr><td style="background:#7C5CFF;padding:24px 24px 28px">${kopf}
<p style="margin:20px 0 4px;font:400 22px 'Gochi Hand','Comic Sans MS',cursive;color:#FFDE59">Dein Wochenbrief ist da!</p>
<h1 style="margin:0 0 14px;font:900 36px/1.22 ${F};color:#fff">${hook}</h1>
<p style="margin:0 0 22px;font:700 16px/1.5 ${F};color:#fff">${esc(a.deck)}</p>
${knopf}
<p style="margin:12px 0 0;font:700 13px/1.4 ${F};color:#EDE7FF;text-align:center">${seiten ? `${seiten} Seiten · ` : ''}zum Lesen am Handy oder Ausdrucken</p></td></tr>
<tr><td style="padding:22px 18px 6px"><p style="margin:0 0 6px 6px;font:900 17px ${F};color:#111">Das steckt drin</p><table role="presentation" width="100%" cellpadding="0" cellspacing="0">${zeilen.join('')}</table></td></tr>
<tr><td style="padding:10px 24px 24px"><div style="background:#FFF3B0;border:3px solid #111;border-radius:16px;padding:14px 16px;font:700 15px/1.5 ${F};color:#111"><b>So holst du am meisten raus:</b> Minifall lesen → kurz selbst lösen → mit der Lösung direkt darunter vergleichen.</div>
<p style="margin:16px 0 0;font:600 11px/1.5 ${F};color:#5C5C68">Lernmaterial zur Examensvorbereitung, keine Rechtsberatung.</p></td></tr>
</table>
<p style="margin:14px 0 0;font:600 11px/1.5 ${F};color:#5C5C68">Du bekommst diese Mail, weil du dich für den Wochenbrief eingetragen hast. <a href="{{ unsubscribe }}" style="color:#5C5C68">Abmelden</a></p>
</td></tr></table></body></html>`;
}
