import test from 'node:test';
import assert from 'node:assert/strict';
import { pruefeGliederung, pruefeWochenbrief, rendereWochenbrief } from '../newsletter/wochenbrief-vorlage.mjs';

function validDraft() {
  return {
    version: 1, status: 'draft',
    issue: {
      number: 2, date: '2026-09-27', subject: 'Ein Irrtum, zwei Rechtsfolgen – der Wochenbrief',
      preheader: 'Drei Fälle aus dem Wochenrückblick mit Lösungen für deine Klausur.',
      hook: 'Der falsche Preis. Die richtige Anspruchsgrundlage.',
      deck: 'Diese Woche übst du am Fall, welche Prüfung in der Klausur zuerst kommt.',
      weekly_post_url: 'https://www.instagram.com/p/WOCHENRUECKBLICK/',
      topic_count: 1,
      quick_check: ['Welcher Anspruch ist zuerst zu prüfen?', 'Wo prüfst du den Einwand im Aufbau?', 'Wie lautet das Ergebnis für die Beteiligten?'],
    },
    sections: [{
      area: 'zivilrecht', title: 'Zivilrecht', subtitle: 'Rechtsfolge und Gegenanspruch sauber prüfen',
      cases: [{
        id: '01', field: 'BGB AT', headline: 'Wer zahlt die vergebliche Fahrt des Käufers?', exams: [1, 2],
        intro: 'Ein Erklärungsirrtum beseitigt nach wirksamer Anfechtung den Vertrag. Der Vertrauensschaden kann bleiben.',
        relevance: 'Die Wirksamkeit der Anfechtung verlangt einen tauglichen Grund, eine Erklärung gegenüber dem richtigen Gegner und eine fristgerechte Geltendmachung. Der Vertrag fällt dann ex tunc weg; erst gesondert folgt die Prüfung eines begrenzten Vertrauensschadens nach § 122 BGB.',
        fact: 'V verschreibt sich beim Kaufpreis. K fährt für dreißig Euro zur Abholung. V ficht den Vertrag sofort an. Kann K Ersatz für die Fahrt verlangen?',
        solution: [
          { marker: 'A.', text: 'Wirksame Anfechtung durch V prüfen' },
          { marker: 'I.', text: 'Erklärungsirrtum beim Preis; Anfechtungsgrund bejahen' },
          { marker: 'II.', text: 'Erklärung gegenüber K und Frist; ex tunc nichtiger Vertrag' },
          { marker: 'B.', text: 'Anspruch des K auf Vertrauensschaden prüfen' },
        ],
        trap: 'Der Vertrauensschaden fällt nicht allein deshalb weg, weil der Vertrag nichtig ist.',
        instagram_post_url: 'https://www.instagram.com/p/THEMENBEITRAG/',
        sources: [{ label: '§ 122 BGB', url: 'https://www.gesetze-im-internet.de/bgb/__122.html' }],
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
  draft.sections[0].cases[0].sources = [{ label: '§ 122 BGB', url: 'https://www.gesetze-im-internet.de/bgb/__122.html' }];
  draft.sections[0].cases[0].headline = 'Erhält K <script>alert(1)</script> seine Fahrtkosten?';
  assert.ok(!rendereWochenbrief(draft).includes('<script>'));
});

test('Themenzahl und Entwurfsstatus sind verbindlich', () => {
  const draft = validDraft();
  draft.issue.topic_count = 8;
  draft.status = 'publish';
  assert.match(pruefeWochenbrief(draft).join(' '), /status muss draft.*8 Themen angekündigt/);
});
