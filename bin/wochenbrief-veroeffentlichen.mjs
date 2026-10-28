#!/usr/bin/env node
/* Wochenbrief-PDFs liegen verschlüsselt im öffentlichen Repo (newsletter/wochenbriefe/*.pdf.enc), damit
   künftige Ausgaben nicht vor dem Versandtag lesbar sind. Dieses Skript entschlüsselt alle Ausgaben, deren
   Versandtag (Europe/Berlin) erreicht ist, nach landingpage/wochenbrief/JJJJ-MM-TT.pdf – vor jedem Deploy.

   node bin/wochenbrief-veroeffentlichen.mjs                 # entschlüsseln (Schlüssel: WOCHENBRIEF_SCHLUESSEL)
   node bin/wochenbrief-veroeffentlichen.mjs --verschluesseln in.pdf JJJJ-MM-TT   # neue Ausgabe ablegen */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const ablage = path.join(root, 'newsletter/wochenbriefe');
const ziel = path.join(root, 'landingpage/wochenbrief');
const schluessel = () => {
  const k = Buffer.from(process.env.WOCHENBRIEF_SCHLUESSEL ?? '', 'base64');
  if (k.length !== 32) throw new Error('WOCHENBRIEF_SCHLUESSEL fehlt oder ist kein 32-Byte-Schlüssel (base64).');
  return k;
};
const heuteBerlin = () => new Intl.DateTimeFormat('sv-SE', { timeZone: 'Europe/Berlin' }).format(new Date());

const [modus, eingabe, datum] = process.argv.slice(2);
if (modus === '--verschluesseln') {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(datum ?? '')) throw new Error('Aufruf: --verschluesseln in.pdf JJJJ-MM-TT');
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv('aes-256-gcm', schluessel(), iv);
  const daten = Buffer.concat([c.update(fs.readFileSync(eingabe)), c.final()]);
  fs.mkdirSync(ablage, { recursive: true });
  fs.writeFileSync(path.join(ablage, `${datum}.pdf.enc`), Buffer.concat([iv, c.getAuthTag(), daten]));
  console.log(`✓ verschlüsselt: newsletter/wochenbriefe/${datum}.pdf.enc`);
} else {
  if (!fs.existsSync(ablage)) process.exit(0);
  const heute = heuteBerlin();
  const faellig = fs.readdirSync(ablage).filter(n => n.endsWith('.pdf.enc') && n.slice(0, 10) <= heute).sort();
  if (!faellig.length) { console.log('Keine fälligen Wochenbriefe.'); process.exit(0); }
  const k = schluessel();
  fs.mkdirSync(ziel, { recursive: true });
  for (const n of faellig) {
    const roh = fs.readFileSync(path.join(ablage, n));
    const d = crypto.createDecipheriv('aes-256-gcm', k, roh.subarray(0, 12));
    d.setAuthTag(roh.subarray(12, 28));
    fs.writeFileSync(path.join(ziel, n.replace(/\.enc$/, '')), Buffer.concat([d.update(roh.subarray(28)), d.final()]));
  }
  console.log(`✓ ${faellig.length} Wochenbrief-PDF(s) veröffentlicht, zuletzt ${faellig.at(-1).slice(0, 10)}`);
}
