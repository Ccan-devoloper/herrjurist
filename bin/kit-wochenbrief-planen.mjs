#!/usr/bin/env node
// Plant ausschließlich die in newsletter/kit-versandplan.json freigegebenen
// Kit-Entwürfe. Der GitHub-Secret-Schlüssel wird niemals ausgegeben.
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';

const API = 'https://api.kit.com/v4/broadcasts';
const PLAN = new URL('../newsletter/kit-versandplan.json', import.meta.url);

export function berlinParts(date) {
  const parts = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'Europe/Berlin', year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', hourCycle: 'h23',
  }).formatToParts(date);
  const p = Object.fromEntries(parts.map(({ type, value }) => [type, value]));
  return { date: `${p.year}-${p.month}-${p.day}`, hour: Number(p.hour), minute: Number(p.minute) };
}

export function dueEntry(entries, now) {
  const today = berlinParts(now).date;
  const due = entries.filter(e => e.date === today);
  if (due.length > 1) throw new Error(`Mehr als ein Wochenbrief für ${today} im Plan.`);
  return due[0] || null;
}

export function validatePlan(entries) {
  const ids = new Set(), dates = new Set();
  let previousDate = '';
  for (const e of entries) {
    if (!Number.isInteger(e.id) || !Number.isInteger(e.issue) || !/^\d{4}-\d{2}-\d{2}$/.test(e.date) ||
        typeof e.subject !== 'string' || !e.subject.trim() || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/.test(e.send_at)) {
      throw new Error('Ungültiger Eintrag im Kit-Versandplan.');
    }
    if (ids.has(e.id) || dates.has(e.date) || e.date <= previousDate) throw new Error('Doppelte oder unsortierte Kit-ID/Datum im Versandplan.');
    ids.add(e.id); dates.add(e.date);
    previousDate = e.date;
    const stamp = new Date(e.send_at);
    const local = berlinParts(stamp);
    if (Number.isNaN(stamp.getTime()) || local.date !== e.date || local.hour !== 9 || local.minute !== 0 || stamp.getUTCDay() !== 0) {
      throw new Error(`Zeit oder Wochentag von Wochenbrief ${e.issue} stimmt nicht (09:00 Europe/Berlin).`);
    }
  }
}

async function kitRequest(fetchImpl, path, apiKey, options = {}) {
  const response = await fetchImpl(`${API}/${path}`, {
    ...options,
    headers: { 'X-Kit-Api-Key': apiKey, 'Content-Type': 'application/json' },
  });
  if (!response.ok) throw new Error(`Kit API ${response.status} bei ${options.method || 'GET'} /broadcasts/${path}.`);
  return response.json();
}

function assertReady(b, e, expectedFrom) {
  if (b.subject !== e.subject) throw new Error(`Betreff von Wochenbrief ${e.issue} weicht vom freigegebenen Plan ab.`);
  if (b.email_address?.toLowerCase() !== expectedFrom.toLowerCase()) throw new Error(`Absender von Wochenbrief ${e.issue} ist nicht KIT_FROM_ADDRESS.`);
  if (b.subscriber_filter?.length !== 1 || b.subscriber_filter[0]?.all?.length !== 1 ||
      b.subscriber_filter[0].all[0]?.type !== 'all_subscribers') {
    throw new Error(`Wochenbrief ${e.issue} richtet sich nicht an alle Abonnenten.`);
  }
  if (!b.content?.includes(`WOCHENBRIEF ${String(e.issue).padStart(2, '0')} ·`) ||
      Buffer.byteLength(b.content, 'utf8') > 72000) {
    throw new Error(`Wochenbrief ${e.issue}: Kennzeichnung fehlt oder HTML ist zu groß.`);
  }
  if (!b.preview_text || !b.email_template?.id || !b.thumbnail_url) {
    throw new Error(`Wochenbrief ${e.issue} ist in Kit unvollständig.`);
  }
}

export async function scheduleDue({ entries, now, apiKey, expectedFrom, fetchImpl = fetch, dryRun = false }) {
  validatePlan(entries);
  const e = dueEntry(entries, now);
  if (!e) {
    const today = berlinParts(now).date;
    if (today >= entries[0].date && new Date(`${today}T12:00:00Z`).getUTCDay() === 0) {
      throw new Error(`Kein freigegebener Kit-Wochenbrief für ${today} im Versandplan.`);
    }
    return { action: 'none' };
  }
  if (!apiKey || !expectedFrom) throw new Error('KIT_API_KEY (Secret) und KIT_FROM_ADDRESS (Variable) fehlen.');
  const target = new Date(e.send_at);
  const { broadcast: b } = await kitRequest(fetchImpl, String(e.id), apiKey);
  if (!b) throw new Error(`Kit lieferte keinen Wochenbrief ${e.issue}.`);
  if (b.status === 'scheduled') {
    if (new Date(b.send_at).getTime() !== target.getTime()) throw new Error(`Wochenbrief ${e.issue} ist für einen anderen Termin geplant.`);
    return { action: 'already_scheduled', issue: e.issue, date: e.date };
  }
  if (b.status === 'completed' || b.status === 'sending') return { action: 'already_sent', issue: e.issue, date: e.date };
  if (b.status !== 'draft') throw new Error(`Wochenbrief ${e.issue} hat unerwarteten Status ${b.status}.`);
  if (target.getTime() - now.getTime() < 20 * 60 * 1000) {
    throw new Error(`Wochenbrief ${e.issue}: weniger als 20 Minuten bis zum Versand; keine verspätete Terminierung.`);
  }
  assertReady(b, e, expectedFrom);
  if (dryRun) return { action: 'dry_run', issue: e.issue, date: e.date };

  const payload = {
    email_template_id: b.email_template.id,
    email_address: b.email_address,
    subject: b.subject,
    preview_text: b.preview_text,
    description: b.description,
    content: b.content,
    thumbnail_url: b.thumbnail_url,
    thumbnail_alt: b.thumbnail_alt || 'LexVerse-Wochenbrief',
    public: true,
    published_at: e.send_at,
    send_at: e.send_at,
  };
  const { broadcast: updated } = await kitRequest(fetchImpl, String(e.id), apiKey, {
    method: 'PUT', body: JSON.stringify(payload),
  });
  if (updated?.status !== 'scheduled' || new Date(updated.send_at).getTime() !== target.getTime()) {
    throw new Error(`Kit hat die Terminierung von Wochenbrief ${e.issue} nicht bestätigt.`);
  }
  return { action: 'scheduled', issue: e.issue, date: e.date };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const entries = JSON.parse(fs.readFileSync(PLAN, 'utf8')).broadcasts;
  const dryRun = process.argv.includes('--dry-run');
  if (process.env.KIT_TEST_NOW && !dryRun) throw new Error('KIT_TEST_NOW ist nur im Dry Run erlaubt.');
  const now = process.env.KIT_TEST_NOW ? new Date(process.env.KIT_TEST_NOW) : new Date();
  if (Number.isNaN(now.getTime())) throw new Error('KIT_TEST_NOW ist kein ISO-Zeitpunkt.');
  scheduleDue({
    entries, now, apiKey: process.env.KIT_API_KEY,
    expectedFrom: process.env.KIT_FROM_ADDRESS,
    dryRun,
  }).then(result => console.log(JSON.stringify(result))).catch(error => {
    console.error(error.message);
    process.exitCode = 1;
  });
}
