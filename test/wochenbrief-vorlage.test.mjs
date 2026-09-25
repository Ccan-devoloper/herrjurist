import test from 'node:test';
import assert from 'node:assert/strict';
import { pruefeGliederung, pruefeWochenbrief, rendereWochenbrief } from '../newsletter/wochenbrief-vorlage.mjs';

function validDraft() {
  return {
    version: 1, status: 'draft',
    issue: {
      number: 2, date: '2026-09-27', subject: 'Ein Kaufpreis, zwei Prüfungsstationen – der Wochenbrief',
      preheader: 'Drei Fälle aus dem Wochenrückblick mit Lösungen für deine Klausur.',
      hook: 'Ware geliefert. Kaufpreis offen – was prüfst du?',
      deck: 'Diese Woche übst du am Fall, welche Prüfung in der Klausur zuerst kommt.',
      weekly_post_url: 'https://www.instagram.com/p/WOCHENRUECKBLICK/',
      topic_count: 1,
      quick_check: ['Welcher Anspruch ist zuerst zu prüfen?', 'Wo prüfst du den Einwand im Aufbau?', 'Wie lautet das Ergebnis für die Beteiligten?'],
    },
    sections: [{
      area: 'zivilrecht', title: 'Zivilrecht', subtitle: 'Rechtsfolge und Gegenanspruch sauber prüfen',
      cases: [{
        id: '01', field: 'SCHULDRECHT', headline: 'Kann V den Kaufpreis für das Buch verlangen?', exams: [1, 2],
        intro: 'Eine fällige Kaufpreisforderung muss zunächst entstehen. Anschließend wird eine mögliche Erfüllung geprüft.',
        relevance: 'Bei einem Kaufpreisverlangen ist zunächst ein wirksamer Kaufvertrag nach § 433 Abs. 2 BGB zu prüfen. Anschließend folgen Fälligkeit und Einwendungen. Hat der Käufer bereits gezahlt, kann der Anspruch durch Erfüllung nach § 362 Abs. 1 BGB untergegangen sein. Entstehung und Erlöschen bleiben im Gutachten getrennte Prüfungsschritte.',
        fact: 'V verkauft K ein Buch für zwanzig Euro und liefert es am vereinbarten Tag. K bezahlt trotz Fälligkeit nicht. Kann V von K den Kaufpreis verlangen?',
        solution: [
          { marker: 'A.', text: 'Anspruch des V aus § 433 Abs. 2 BGB entstanden' },
          { marker: 'I.', text: 'Wirksamer Kaufvertrag über das Buch für zwanzig Euro' },
          { marker: 'II.', text: 'Kaufpreisforderung fällig nach der Abrede der Parteien' },
          { marker: 'B.', text: 'Anspruch nicht durch Zahlung nach § 362 BGB erloschen' },
        ],
        trap: 'Die Übergabe des Buchs erfüllt nicht zugleich die Kaufpreisschuld des Käufers.',
        instagram_post_url: 'https://www.instagram.com/p/THEMENBEITRAG/',
        sources: [{ label: '§ 433 BGB', url: 'https://www.gesetze-im-internet.de/bgb/__433.html' }],
      }],
    }],
  };
}

test('vollständiger Entwurf rendert Logo, Examensbadges, Quellen und Einrückung', () => {
  const draft = validDraft();
  assert.deepEqual(pruefeWochenbrief(draft), []);
  const html = rendereWochenbrief(draft);
  assert.match(html, /lexverse-portal-v1.png/);
  assert.match(html, /by herrjurist/);
  assert.match(html, /1\. Staatsexamen/);
  assert.match(html, /2\. Staatsexamen/);
  assert.match(html, /padding:5px 0 5px 22px/);
  assert.match(html, /gesetze-im-internet\.de/);
});

test('einsame und übersprungene Ebenen werden auch tief in der Skizze verworfen', () => {
  const solution = validDraft().sections[0].cases[0].solution;
  solution.splice(2, 0, { marker: '1.', text: 'Alleinstehender Unterpunkt ohne Gegenstück' });
  assert.match(pruefeGliederung(solution).join(' '), /ohne Gegenstück/);
  solution[2].marker = '2.';
  assert.match(pruefeGliederung(solution).join(' '), /folgt 1\./);
});

test('ein Thema ohne Herkunftsbeitrag oder Rechtsquelle scheitert und HTML wird escaped', () => {
  const draft = validDraft();
  draft.sections[0].cases[0].instagram_post_url = '';
  draft.sections[0].cases[0].sources = [];
  assert.match(pruefeWochenbrief(draft).join(' '), /instagram_post_url.*sources/);
  assert.throws(() => rendereWochenbrief(draft));
  draft.sections[0].cases[0].instagram_post_url = 'https://www.instagram.com/p/THEMENBEITRAG/';
  draft.sections[0].cases[0].sources = [{ label: '§ 433 BGB', url: 'https://www.gesetze-im-internet.de/bgb/__433.html' }];
  draft.sections[0].cases[0].headline = 'Erhält K <script>alert(1)</script> seine Fahrtkosten?';
  assert.ok(!rendereWochenbrief(draft).includes('<script>'));
});

test('Themenzahl und Entwurfsstatus sind verbindlich', () => {
  const draft = validDraft();
  draft.issue.topic_count = 8;
  draft.status = 'publish';
  assert.match(pruefeWochenbrief(draft).join(' '), /status muss draft.*8 Themen angekündigt/);
});
