#!/usr/bin/env node
// Temporary editorial audit. Exports only topics used in Wochenbrief 14–56,
// encrypted to a one-time public key. Neither the secret nor plaintext is logged.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { THEMEN } from '../daten/themen.mjs';

const used = new Set();
for (let day = new Date('2026-12-14T12:00:00Z'); day <= new Date('2027-10-09T12:00:00Z'); day.setUTCDate(day.getUTCDate() + 1)) {
  const weekday = day.getUTCDay();
  if (weekday === 0) continue;
  const date = day.toISOString().slice(0, 10);
  const data = JSON.parse(fs.readFileSync(`vorproduktion/${date}.json`, 'utf8'));
  for (const entry of data.plan.beitraege) used.add(entry.themaId);
}
const selected = THEMEN.map((topic, i) => ({ ...topic, id: topic.id || `${topic.fach}-${String(i + 1).padStart(3, '0')}` }))
  .filter(topic => used.has(topic.id));
const found = new Set(selected.map(topic => topic.id));
if (found.size !== used.size) throw new Error(`Themenpool-Abgleich unvollständig: ${found.size}/${used.size}`);
const clear = Buffer.from(JSON.stringify(selected));
const key = crypto.randomBytes(32), iv = crypto.randomBytes(12);
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
const ciphertext = Buffer.concat([cipher.update(clear), cipher.final()]);
const publicKey = fs.readFileSync('newsletter/themenpool-audit-public-temp.pem');
const envelope = {
  algorithm: 'RSA-OAEP-SHA256 + AES-256-GCM',
  key: crypto.publicEncrypt({ key: publicKey, oaepHash: 'sha256' }, key).toString('base64'),
  iv: iv.toString('base64'), tag: cipher.getAuthTag().toString('base64'),
  ciphertext: ciphertext.toString('base64'),
};
const target = path.join(process.env.RUNNER_TEMP || '.', 'themenpool-audit.enc.json');
fs.writeFileSync(target, JSON.stringify(envelope), { mode: 0o600 });
console.log(`${selected.length} benutzte Themen sicher verschlüsselt; kein Klartext im Actions-Log.`);
