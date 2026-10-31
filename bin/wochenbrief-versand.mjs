#!/usr/bin/env node
/* Wochenbrief-Versand über Brevo. Die Kampagnen liegen als Entwürfe in Brevo; welche wann rausgeht, steht in
   newsletter/wochenbriefe/plan.json. Läuft aus .github/workflows/wochenbrief-versand.yml.

   node bin/wochenbrief-versand.mjs vorschau   # Freitag: Test der kommenden Ausgabe an WOCHENBRIEF_VORSCHAU_AN
   node bin/wochenbrief-versand.mjs senden     # Sonntag 10:00 Berlin: PDF prüfen, Kampagne sofort senden

   Einspruch: Die Kampagne in Brevo umbenennen, sodass „STOPP“ im Namen steht, oder löschen. Dann wird sie
   übersprungen. Versendet wird nur eine Kampagne, die in Brevo noch Entwurf ist. */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const plan = JSON.parse(fs.readFileSync(path.join(root, 'newsletter/wochenbriefe/plan.json'), 'utf8'));
const KEY = process.env.BREVO_API_KEY;
if (!KEY) throw new Error('BREVO_API_KEY fehlt.');
const brevo = async (methode, pfad, daten) => {
  const res = await fetch(`https://api.brevo.com/v3/${pfad}`, {
    method: methode, headers: { 'api-key': KEY, accept: 'application/json', 'content-type': 'application/json' },
    body: daten ? JSON.stringify(daten) : undefined,
  });
  const text = await res.text();
  if (!res.ok) throw new Error(`Brevo ${methode} ${pfad}: ${res.status} ${text.slice(0, 300)}`);
  return text ? JSON.parse(text) : null;
};
const berlin = (opts, d = new Date()) => new Intl.DateTimeFormat('sv-SE', { timeZone: 'Europe/Berlin', ...opts }).format(d);
const heute = berlin({});
const tagPlus = n => berlin({}, new Date(Date.now() + n * 864e5));

const modus = process.argv[2];
const datum = modus === 'vorschau' ? [1, 2, 3].map(tagPlus).find(t => plan.ausgaben.some(x => x.datum === t)) : heute;
const ausgabe = plan.ausgaben.find(x => x.datum === datum);
if (!ausgabe) { console.log(`Keine Ausgabe für ${datum ?? 'die nächsten Tage'} geplant.`); process.exit(0); }

let kampagne;
try { kampagne = await brevo('GET', `emailCampaigns/${ausgabe.kampagne}`); }
catch (e) { console.log(`Kampagne ${ausgabe.kampagne} nicht gefunden – übersprungen (${e.message}).`); process.exit(0); }
if (/stopp/i.test(kampagne.name)) { console.log(`„${kampagne.name}“ ist gestoppt – kein Versand.`); process.exit(0); }
if (kampagne.status !== 'draft') { console.log(`Kampagne hat Status „${kampagne.status}“ – nichts zu tun.`); process.exit(0); }

if (modus === 'vorschau') {
  const an = (process.env.WOCHENBRIEF_VORSCHAU_AN ?? '').split(',').map(s => s.trim()).filter(Boolean);
  if (!an.length) throw new Error('WOCHENBRIEF_VORSCHAU_AN fehlt.');
  await brevo('POST', `emailCampaigns/${ausgabe.kampagne}/sendTest`, { emailTo: an });
  console.log(`✓ Vorschau von Wochenbrief ${ausgabe.nr} (${ausgabe.datum}) an ${an.join(', ')} geschickt.`);
} else if (modus === 'senden') {
  const stunde = +berlin({ hour: '2-digit', hour12: false });
  if (stunde !== 10 && !process.env.SOFORT) { console.log(`Berlin ${stunde} Uhr – Versand erst um 10 Uhr.`); process.exit(0); }
  const pdf = `${process.env.LANDINGPAGE_URL}/wochenbrief/${ausgabe.datum}.pdf`;
  const kopf = await fetch(pdf, { method: 'HEAD' });
  if (!kopf.ok || !/pdf/.test(kopf.headers.get('content-type') ?? '')) throw new Error(`PDF nicht erreichbar (${kopf.status}): ${pdf} – Versand abgebrochen.`);
  await brevo('POST', `emailCampaigns/${ausgabe.kampagne}/sendNow`);
  console.log(`✓ Wochenbrief ${ausgabe.nr} (${ausgabe.datum}) wird versendet.`);
} else {
  console.log('Aufruf: node bin/wochenbrief-versand.mjs vorschau|senden'); process.exit(2);
}
