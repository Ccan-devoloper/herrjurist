/* LexVerse-Wochenbrief: Ausgabe 02 ist der Gestaltungs-Master. Kein Kit-/Versandzugang. */

const LOGO = 'https://raw.githubusercontent.com/Ccan-devoloper/herrjurist/instagram-assets/newsletter/lexverse-portal-v1.png';
const HERO = 'https://raw.githubusercontent.com/Ccan-devoloper/herrjurist/instagram-assets/newsletter/header-universe-v1.jpg';
const FONT = "'Inter Herrjurist',Inter,Arial,Helvetica,sans-serif";
const COLORS = { zivilrecht: '#3154E6', strafrecht: '#FF7950', oeffentliches_recht: '#1FC68C', methodik: '#3154E6' };
const MASTER_MARKERS = ['A.', 'I.', 'II.', 'B.', 'I.', 'II.'];
const LEVELS = [
  Array.from('ABCDEFGH', x => `${x}.`),
  ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.'],
  Array.from({ length: 30 }, (_, i) => `${i + 1}.`),
  Array.from('abcdefgh', x => `${x})`),
  Array.from('abcdefgh', x => `${x}${x})`),
];
const escapeHtml = value => String(value).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
const text = (value, min = 1, max = 5000) => typeof value === 'string' && value.trim().length >= min && value.trim().length <= max;
const url = value => { try { return new URL(value).protocol === 'https:'; } catch { return false; } };

export function pruefeGliederung(solution) {
  const errors = [];
  if (!Array.isArray(solution) || solution.length < 4) return ['Mindestens A., B. und eine weitere Ebene sind erforderlich.'];
  const root = { marker: 'Wurzel', children: [] };
  const stack = [];
  solution.forEach((line, i) => {
    const marker = line?.marker;
    const level = LEVELS.findIndex(labels => labels.includes(marker));
    if (level < 0) { errors.push(`Zeile ${i + 1}: unbekannter Gliederungspunkt ${String(marker)}`); return; }
    if (!text(line?.text, 8)) errors.push(`Zeile ${i + 1}: Obersatz/Ergebnis fehlt.`);
    const parent = level === 0 ? root : stack[level - 1];
    if (!parent) { errors.push(`${marker}: Oberpunkt fehlt.`); return; }
    const expected = LEVELS[level][parent.children.length];
    if (marker !== expected) errors.push(`${marker}: nach ${parent.marker} folgt ${expected ?? 'kein weiterer Punkt'}.`);
    const node = { marker, children: [] };
    parent.children.push(node);
    stack[level] = node;
    stack.length = level + 1;
  });
  function inspect(node) {
    if (node.children.length === 1) errors.push(`${node.marker}: ${node.children[0].marker} steht ohne Gegenstück.`);
    node.children.forEach(inspect);
  }
  inspect(root);
  if (!root.children.some(node => node.children.length)) errors.push('Mindestens eine Ebene I./II. muss den Prüfungsgang konkretisieren.');
  return errors;
}

export function pruefeWochenbrief(draft) {
  const errors = [];
  const requireText = (value, name, min, max) => { if (!text(value, min, max)) errors.push(`${name}: ${min}–${max} Zeichen erforderlich.`); };
  if (draft?.version !== 1) errors.push('version muss 1 sein.');
  if (draft?.status !== 'draft') errors.push('status muss draft sein; diese Vorlage dient ausschließlich Entwürfen.');
  const issue = draft?.issue ?? {};
  if (!Number.isInteger(issue.number) || issue.number < 1) errors.push('issue.number muss positiv sein.');
  if (!/^\d{4}-\d{2}-\d{2}$/.test(issue.date ?? '') || Number.isNaN(Date.parse(`${issue.date}T00:00:00Z`))) errors.push('issue.date benötigt ein gültiges ISO-Datum.');
  requireText(issue.subject, 'issue.subject', 15, 110);
  requireText(issue.preheader, 'issue.preheader', 25, 180);
  requireText(issue.hook, 'issue.hook', 15, 130);
  requireText(issue.deck, 'issue.deck', 30, 220);
  if (!Number.isInteger(issue.topic_count) || issue.topic_count < 1) errors.push('issue.topic_count muss der Zahl der Themen entsprechen.');
  if (!Array.isArray(issue.quick_check) || issue.quick_check.length !== 3 || issue.quick_check.some(q => !text(q, 12, 180))) errors.push('issue.quick_check benötigt drei konkrete Wiederholungsfragen.');
  const sections = draft?.sections;
  if (!Array.isArray(sections) || sections.length < 1) errors.push('sections: mindestens ein Rechtsgebiet erforderlich.');
  const ids = new Set();
  const allCases = [];
  (Array.isArray(sections) ? sections : []).forEach((section, s) => {
    const at = `sections[${s}]`;
    if (!['zivilrecht', 'strafrecht', 'oeffentliches_recht'].includes(section?.area)) errors.push(`${at}.area: zivilrecht, strafrecht oder oeffentliches_recht.`);
    requireText(section?.title, `${at}.title`, 5, 90);
    requireText(section?.subtitle, `${at}.subtitle`, 10, 130);
    if (!Array.isArray(section?.cases) || section.cases.length < 1) errors.push(`${at}.cases fehlt.`);
    (Array.isArray(section?.cases) ? section.cases : []).forEach((item, c) => {
      const where = `${at}.cases[${c}]`;
      allCases.push(item);
      if (!/^\d{2}$/.test(item?.id ?? '') || ids.has(item.id)) errors.push(`${where}.id: eindeutige zweistellige Nummer erforderlich.`);
      else ids.add(item.id);
      requireText(item?.field, `${where}.field`, 2, 60);
      requireText(item?.headline, `${where}.headline`, 15, 100);
      requireText(item?.intro, `${where}.intro`, 45, 500);
      requireText(item?.relevance, `${where}.relevance`, 160, 1350);
      if (Boolean(item?.fact) === Boolean(item?.question)) errors.push(`${where}: genau ein Minifall oder eine fachliche Prüffrage erforderlich.`);
      if (item?.fact) requireText(item.fact, `${where}.fact`, 60, 1100);
      if (item?.question) requireText(item.question, `${where}.question`, 30, 1100);
      if (Boolean(item?.trap) === Boolean(item?.note)) errors.push(`${where}: genau ein Fallstrick oder Merksatz erforderlich.`);
      requireText(item?.trap || item?.note, `${where}.trap/note`, 20, 550);
      if (!Array.isArray(item?.exams) || item.exams.length < 1 || item.exams.length > 2 || new Set(item.exams).size !== item.exams.length || item.exams.some(n => n !== 1 && n !== 2)) errors.push(`${where}.exams: [1], [2] oder [1,2] erforderlich.`);
      if (!Array.isArray(item?.sources) || item.sources.length < 1 || item.sources.some(ref => !text(ref?.label, 3, 100) || !url(ref?.url))) errors.push(`${where}.sources: mindestens eine überprüfbare Norm/Entscheidung mit HTTPS-Link.`);
      pruefeGliederung(item?.solution).forEach(error => errors.push(`${where}.solution: ${error}`));
      if (JSON.stringify(item?.solution?.map(line => line.marker)) !== JSON.stringify(MASTER_MARKERS)) errors.push(`${where}.solution: Ausgabe 02 verlangt A./I./II./B./I./II.`);
    });
  });
  const methods = Array.isArray(draft?.methods) ? draft.methods : [];
  methods.forEach((item, i) => {
    const where = `methods[${i}]`;
    if (!/^\d{2}$/.test(item?.id ?? '') || ids.has(item.id)) errors.push(`${where}.id: eindeutige zweistellige Nummer erforderlich.`);
    else ids.add(item.id);
    requireText(item?.field, `${where}.field`, 2, 60);
    requireText(item?.headline, `${where}.headline`, 15, 100);
    requireText(item?.intro, `${where}.intro`, 45, 500);
    if (!Array.isArray(item?.steps) || item.steps.length < 2 || item.steps.length > 4 || item.steps.some(step => !text(step, 18, 500))) errors.push(`${where}.steps: zwei bis vier konkrete Schritte erforderlich.`);
    requireText(item?.note, `${where}.note`, 20, 500);
    if (item?.fact || item?.solution) errors.push(`${where}: Methodik und Kopfsache sind keine Fälle.`);
    if (!Array.isArray(item?.exams) || item.exams.length < 1 || item.exams.length > 2 || new Set(item.exams).size !== item.exams.length || item.exams.some(n => n !== 1 && n !== 2)) errors.push(`${where}.exams: [1], [2] oder [1,2] erforderlich.`);
  });
  [...allCases, ...methods].forEach((item, i) => { if (item?.id !== String(i + 1).padStart(2, '0')) errors.push(`Thema ${i + 1}: laufende Nummer ${String(i + 1).padStart(2, '0')} erwartet.`); });
  if (allCases.length + methods.length !== issue.topic_count) errors.push(`Wochenrückblick: ${issue.topic_count} Themen angekündigt, ${allCases.length + methods.length} Themen vorhanden.`);
  return errors;
}

function outline(solution) {
  return `<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border:1px solid #DCE2EA;border-radius:9px;background:#FFFFFF;font-family:${FONT};font-size:14px;line-height:1.5;color:#1F2B40">${solution.map(({ marker, text: content }, index) => {
    const roman = marker === 'I.' || marker === 'II.';
    const top = index === 0 ? 11 : 5;
    const bottom = index === solution.length - 1 ? 11 : 5;
    return `<tr><td valign="top" width="54" style="padding:${top}px 0 ${bottom}px ${roman ? 35 : 13}px;font-weight:800;white-space:nowrap;color:#101827">${escapeHtml(marker)}</td><td valign="top" style="padding:${top}px 13px ${bottom}px ${roman ? 22 : 0}px;color:#1F2B40">${escapeHtml(content)}</td></tr>`;
  }).join('')}</table>`;
}

function article(item, color) {
  const badges = item.exams.map(n => `<span style="display:inline-block;padding:5px 9px;margin:0 5px 4px 0;background:#F0F3F8;color:#101827;border-radius:5px;font-family:${FONT};font-size:11px;font-weight:800">${n}. Staatsexamen</span>`).join('');
  const references = item.sources.map(ref => `<a href="${escapeHtml(ref.url)}" style="color:#163b74;text-decoration:underline">${escapeHtml(ref.label)}</a>`).join(' · ');
  const prompt = item.fact || item.question;
  const promptLabel = item.fact ? 'MINIFALL' : 'KLAUSURFRAGE';
  const noteLabel = item.trap ? 'FALLE' : 'MERKE';
  return `<tr><td style="padding:0 24px;background:#FFFFFF;font-family:${FONT}"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr><td style="padding:28px 0 31px;border-bottom:1px solid #DCE2EA">
    <div style="display:inline-block;background:${color};color:${color === COLORS.zivilrecht ? '#FFFFFF' : '#101827'};border-radius:8px;padding:6px 11px;font-size:11px;font-weight:900;letter-spacing:.6px">${escapeHtml(item.id)} / ${escapeHtml(item.field)}</div>
    <div style="margin:10px 0 0">${badges}</div>
    <h3 style="font-family:${FONT};font-size:25px;line-height:1.16;letter-spacing:-.7px;color:#101827;margin:13px 0;font-weight:900">${escapeHtml(item.headline)}</h3>
    <div style="font-size:15px;line-height:1.55;color:#263449;margin:0 0 16px">${escapeHtml(item.intro)}</div>
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#FFFBE3;border-left:5px solid #F4E500;border-radius:9px"><tr><td style="padding:12px 15px;font-family:${FONT}"><div style="font-size:10px;letter-spacing:1px;font-weight:900;color:#101827;margin-bottom:5px">WARUM PRÜFUNGSRELEVANT?</div><div style="font-size:13px;line-height:1.5;color:#172235">${escapeHtml(item.relevance)}</div></td></tr></table>
    <div style="font-size:11px;letter-spacing:1.1px;font-weight:900;color:#101827;margin:23px 0 8px">${promptLabel} <span style="color:${color}">●</span> DU BIST DRAN</div>
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#F4F7FA;border-left:4px solid ${color};border-radius:9px"><tr><td style="padding:15px 16px;font-family:${FONT};font-size:15px;line-height:1.55;color:#172235">${escapeHtml(prompt)}</td></tr></table>
    <div style="font-size:11px;letter-spacing:1.1px;font-weight:900;color:#101827;margin:22px 0 8px">LÖSUNGSSKIZZE</div>
    ${outline(item.solution)}
    <div style="font-size:13px;line-height:1.5;color:#334155;padding-top:14px"><strong style="color:#101827">${noteLabel}:</strong> ${escapeHtml(item.trap || item.note)}</div>
    <div style="font-size:12px;line-height:1.6;color:#334155;padding-top:10px">Rechtsgrundlagen: ${references}</div>
  </td></tr></table></td></tr>`;
}

function sectionHtml(section) {
  const color = COLORS[section.area];
  const first = section.cases[0]?.id;
  const last = section.cases.at(-1)?.id;
  return `<tr><td style="padding:17px 24px 0;background:#FFFFFF;font-family:${FONT}"><table role="presentation" width="100%" style="background:${color};border-radius:13px"><tr><td style="padding:15px 17px;color:${color === COLORS.zivilrecht ? '#FFFFFF' : '#101827'};font-family:${FONT}"><div style="font-size:20px;font-weight:900">${escapeHtml(section.title)} · ${first}–${last}</div><div style="font-size:12px;line-height:1.4;margin-top:4px;font-weight:600">${escapeHtml(section.subtitle)}</div></td></tr></table></td></tr>${section.cases.map(item => article(item, color)).join('')}`;
}

function methodHtml(item) {
  const badges = item.exams.map(n => `<span style="display:inline-block;padding:5px 9px;margin:0 5px 4px 0;background:#F0F3F8;color:#101827;border-radius:5px;font-family:${FONT};font-size:11px;font-weight:800">${n}. Staatsexamen</span>`).join('');
  const steps = item.steps.map((step, i) => `<br><strong>${i + 1}.</strong> ${escapeHtml(step)}`).join('');
  return `<tr><td style="padding:0 24px;background:#FFFFFF;font-family:${FONT}"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr><td style="padding:28px 0 31px;border-bottom:1px solid #DCE2EA"><div style="display:inline-block;background:#3154E6;color:#FFFFFF;border-radius:8px;padding:6px 11px;font-size:11px;font-weight:900;letter-spacing:.6px">${escapeHtml(item.id)} / ${escapeHtml(item.field)}</div><div style="margin:10px 0 0">${badges}</div><h3 style="font-family:${FONT};font-size:25px;line-height:1.16;letter-spacing:-.7px;color:#101827;margin:13px 0;font-weight:900">${escapeHtml(item.headline)}</h3><div style="font-size:15px;line-height:1.55;color:#1F2937;margin:0 0 14px">${escapeHtml(item.intro)}</div><table role="presentation" width="100%" style="background:#F4F7FA;border-left:4px solid #3154E6;border-radius:9px"><tr><td style="padding:14px 15px;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;color:#1F2937"><strong style="font-size:11px;letter-spacing:.6px">DIREKT ANWENDEN</strong>${steps}</td></tr></table><div style="font-size:13px;line-height:1.5;color:#334155;padding-top:12px"><strong>Merke:</strong> ${escapeHtml(item.note)}</div></td></tr></table></td></tr>`;
}

function methodsHtml(methods, subtitle) {
  if (!methods.length) return '';
  return `<tr><td style="padding:17px 24px 0;background:#FFFFFF;font-family:${FONT}"><table role="presentation" width="100%" style="background:#3154E6;border-radius:13px"><tr><td style="padding:15px 17px;color:#FFFFFF;font-family:${FONT}"><div style="font-size:20px;font-weight:900">Klausurtechnik &amp; Kopfsache · ${methods[0].id}–${methods.at(-1).id}</div><div style="font-size:12px;line-height:1.4;margin-top:4px;font-weight:600">${escapeHtml(subtitle || 'Werkzeuge für die nächste Klausur')}</div></td></tr></table></td></tr>${methods.map(methodHtml).join('')}`;
}

export function rendereWochenbrief(draft) {
  const errors = pruefeWochenbrief(draft);
  if (errors.length) throw new Error(`Entwurf nicht freigabefähig:\n- ${errors.join('\n- ')}`);
  const issue = draft.issue;
  const methods = draft.methods || [];
  const legalCount = draft.sections.reduce((sum, section) => sum + section.cases.length, 0);
  const date = new Intl.DateTimeFormat('de-DE', { timeZone: 'UTC', day: 'numeric', month: 'long', year: 'numeric' }).format(new Date(`${issue.date}T00:00:00Z`));
  const questions = issue.quick_check.map((q, i) => `${i + 1}. ${escapeHtml(q)}`).join('<br>');
  const rendered = `<style type="text/css">@font-face{font-family:'Inter Herrjurist';src:url('https://raw.githubusercontent.com/Ccan-devoloper/herrjurist/main/fonts/Inter.ttf') format('truetype');font-style:normal;font-weight:100 900}</style>
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;background:#F5F7FA;margin:0;padding:0"><tr><td align="center" style="padding:0"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width:690px;width:100%;background:#FFFFFF;border-collapse:collapse;margin:0 auto">
<tr><td align="left" style="background:#FFFFFF;padding:9px 24px 1px;font-family:${FONT}"><img src="${LOGO}" width="300" alt="LexVerse – Portalmonogramm" style="display:block;border:0;width:100%;max-width:300px;height:auto"><div style="text-align:left"><span style="display:inline-block;background:#F4E500;color:#101827;border-radius:20px;padding:8px 11px;font-size:11px;font-weight:900">by herrjurist</span></div></td></tr>
<tr><td style="background:#FFFFFF;padding:16px 24px 21px;font-family:${FONT}"><div style="font-size:11px;font-weight:800;letter-spacing:.9px;color:#334155;margin-bottom:9px">WOCHENBRIEF ${String(issue.number).padStart(2, '0')} · ${escapeHtml(date.toUpperCase())}</div><h1 style="font-family:${FONT};font-size:35px;line-height:1.11;letter-spacing:-1.2px;font-weight:900;margin:0;color:#101827">${escapeHtml(issue.hook)}</h1><p style="font-size:16px;line-height:1.45;color:#293950;margin:13px 0 0">${escapeHtml(issue.deck)}</p></td></tr>
<tr><td style="padding:0;background:#101418"><img src="${HERO}" width="690" height="300" alt="Mara, Rex, FORM-7, Flux, Zylla und Brakk im intergalaktischen LexVerse" style="display:block;border:0;width:100%;max-width:690px;height:auto"></td></tr>
<tr><td style="background:#101418;padding:18px 24px 21px;font-family:${FONT}"><div style="font-size:20px;color:#FFFFFF;font-weight:900">Erst du. Dann die Skizze.</div><p style="font-size:14px;line-height:1.55;color:#E5EAF0;margin:7px 0 0">Bei den ${legalCount} Fachthemen: erst selbst entscheiden, dann die Skizze lesen. Die ${methods.length} Werkzeuge für Klausurtechnik und Kopfsache kannst du direkt anwenden.</p></td></tr>
${draft.sections.map(sectionHtml).join('')}
${methodsHtml(methods, draft.method_subtitle)}
<tr><td style="background:#101418;padding:25px 24px;font-family:${FONT}"><div style="display:inline-block;background:#F4E500;border-radius:8px;padding:6px 10px;color:#101827;font-size:11px;font-weight:900">DEIN 60-SEKUNDEN-CHECK</div><p style="color:#FFFFFF;font-size:15px;line-height:1.75;margin:14px 0 0">${questions}</p></td></tr>
<tr><td style="background:#FFFFFF;padding:23px 24px 28px;font-family:${FONT}"><p style="font-size:15px;line-height:1.55;color:#101827;margin:0 0 12px"><strong>Bei welchem Thema musstest du stoppen?</strong> Antworte einfach mit der Nummer. Bis zur nächsten Ausgabe!</p><p style="font-size:15px;font-weight:900;color:#101827;margin:0">Herr Jurist</p><p style="font-size:12px;line-height:1.5;color:#334155;margin:17px 0 0">Lernmaterial zur Examensvorbereitung, keine Rechtsberatung. Die verlinkten Normen und Entscheidungen dienen der eigenen Nachprüfung.</p></td></tr>
</table></td></tr></table>`;
  if (Buffer.byteLength(rendered, 'utf8') > 100000) throw new Error('Wochenbrief-HTML ist zu groß für den Versandplan.');
  return rendered;
}
