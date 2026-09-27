import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { dueEntry, scheduleDue, validatePlan } from '../bin/kit-wochenbrief-planen.mjs';

const entries = JSON.parse(fs.readFileSync(new URL('../newsletter/kit-versandplan.json', import.meta.url), 'utf8')).broadcasts;
const issue = entries[0];
const before = new Date('2026-10-11T05:20:00Z');
const content = '<h1>WOCHENBRIEF 04 · 11. OKTOBER 2026</h1><p>Inhalt</p>';

function draft(overrides = {}) {
  return {
    id: issue.id, status: 'draft', send_at: null, subject: issue.subject,
    email_address: 'newsletter@lexverse.de', preview_text: 'Klausurwissen',
    description: 'Wochenbrief 04', content, thumbnail_url: 'https://example.org/logo.png',
    thumbnail_alt: null, public: false, published_at: null,
    email_template: { id: 5537850 },
    subscriber_filter: [{ all: [{ type: 'all_subscribers' }] }],
    ...overrides,
  };
}

function fakeKit(b, calls, senderVerified = true) {
  return async (url, options) => {
    calls.push({ url, options });
    if (url.endsWith('/account')) {
      return { ok: true, json: async () => ({ account: { sending_addresses: [
        { email_address: 'newsletter@lexverse.de', is_verified: senderVerified },
      ] } }) };
    }
    const updated = options.method === 'PUT'
      ? { ...b, status: 'scheduled', send_at: issue.send_at, email_address: JSON.parse(options.body).email_address }
      : b;
    return { ok: true, json: async () => ({ broadcast: updated }) };
  };
}

function args(b, calls, overrides = {}) {
  return { entries, now: before, apiKey: 'test-only', expectedFrom: 'newsletter@lexverse.de', fetchImpl: fakeKit(b, calls), ...overrides };
}

test('Plan berücksichtigt Berliner Datum und die Zeitumstellung', () => {
  assert.doesNotThrow(() => validatePlan(entries));
  assert.equal(entries.length, 53);
  assert.equal(dueEntry(entries, before)?.issue, 4);
  assert.equal(dueEntry(entries, new Date('2026-10-24T23:30:00Z'))?.issue, 6);
  assert.equal(entries.find(e => e.date === '2027-03-21')?.send_at, '2027-03-21T08:00:00Z');
  assert.equal(entries.find(e => e.date === '2027-03-28')?.send_at, '2027-03-28T07:00:00Z');
  assert.equal(entries.at(-1).date, '2027-10-10');
  assert.equal(dueEntry(entries, new Date('2026-10-10T05:20:00Z')), null);
});

test('Entwurf wird mit korrektem Termin und Inhalt genau einmal geplant', async () => {
  const calls = [];
  const result = await scheduleDue(args(draft(), calls));
  assert.equal(result.action, 'scheduled');
  assert.equal(calls.length, 3);
  const payload = JSON.parse(calls[2].options.body);
  assert.equal(payload.send_at, issue.send_at);
  assert.equal(payload.email_address, 'newsletter@lexverse.de');
  assert.equal(payload.content, content);
  assert.equal(payload.public, true);
  assert.equal(calls[2].options.headers['X-Kit-Api-Key'], 'test-only');
});

test('Dry Run und bereits terminierte Ausgabe lösen keinen PUT aus', async () => {
  const calls = [];
  assert.equal((await scheduleDue(args(draft(), calls, { dryRun: true }))).action, 'dry_run');
  assert.equal(calls.length, 2);
  calls.length = 0;
  assert.equal((await scheduleDue(args(draft({ status: 'scheduled', send_at: issue.send_at }), calls, {
    now: new Date('2026-10-11T08:00:00Z'),
  }))).action, 'already_scheduled');
  assert.equal(calls.length, 1);
});

test('Unbestätigter Absender, anderes Publikum und später Lauf sperren den Versand', async () => {
  const senderCalls = [];
  await assert.rejects(scheduleDue(args(draft({ email_address: 'herrjurist@gmx.de' }), senderCalls, {
    fetchImpl: fakeKit(draft(), senderCalls, false),
  })), /nicht als bestätigter Absender/);
  assert.equal(senderCalls.length, 2);
  for (const b of [
    draft({ subscriber_filter: [{ all: [{ type: 'tag', ids: [1] }] }] }),
    draft({ subject: 'Falscher Betreff' }),
  ]) {
    const calls = [];
    await assert.rejects(scheduleDue(args(b, calls)));
    assert.equal(calls.length, 1);
  }
  const calls = [];
  await assert.rejects(scheduleDue(args(draft(), calls, { now: new Date('2026-10-11T06:45:00Z') })), /weniger als 20 Minuten/);
  assert.equal(calls.length, 1);
});

test('Ein verifizierter neuer Absender ersetzt den alten Entwurfsabsender', async () => {
  const calls = [];
  const result = await scheduleDue(args(draft({ email_address: 'herrjurist@gmx.de' }), calls));
  assert.equal(result.action, 'scheduled');
  assert.equal(JSON.parse(calls[2].options.body).email_address, 'newsletter@lexverse.de');
});

test('Ohne Secret oder ohne fälligen Eintrag wird nichts an Kit geschrieben', async () => {
  const calls = [];
  await assert.rejects(scheduleDue(args(draft(), calls, { apiKey: '' })), /KIT_API_KEY/);
  assert.equal(calls.length, 0);
  assert.equal((await scheduleDue(args(draft(), calls, { now: new Date('2026-10-12T05:20:00Z') }))).action, 'none');
  assert.equal(calls.length, 0);
  await assert.rejects(scheduleDue(args(draft(), calls, { now: new Date('2027-10-17T06:20:00Z') })), /Kein freigegebener/);
  assert.equal(calls.length, 0);
});
