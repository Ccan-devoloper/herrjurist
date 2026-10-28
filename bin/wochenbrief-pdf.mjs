#!/usr/bin/env node
/* Wochenbrief-PDF aus einer Ausgabe-JSON drucken. Keine API, kein Versand.
   Aufruf: node bin/wochenbrief-pdf.mjs ausgabe.json ausgabe.pdf [Bildordner] */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { rendereWochenbriefPdfHtml } from '../newsletter/wochenbrief-pdf.mjs';

const [input, output, bilder] = process.argv.slice(2);
if (!input || !output) {
  console.log('Aufruf: node bin/wochenbrief-pdf.mjs ausgabe.json ausgabe.pdf [Bildordner]');
  process.exit(2);
}
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const ausgabe = JSON.parse(fs.readFileSync(input, 'utf8'));
const bildBasis = pathToFileURL(path.resolve(bilder ?? path.dirname(input))).href + '/';
const html = rendereWochenbriefPdfHtml(ausgabe, {
  bild: name => /^https?:/.test(name) ? name : bildBasis + name,
  schriften: pathToFileURL(path.join(root, 'landingpage/fonts')).href + '/',
});
const tmp = path.resolve(output.replace(/\.pdf$/i, '') + '.html');
fs.writeFileSync(tmp, html);

// playwright aus dem Projekt oder global (NODE_PATH), wie in den übrigen Render-Skripten vorinstalliert
const { chromium } = await import('playwright').catch(() => createRequire(import.meta.url)('playwright'));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 794, height: 1123 } });
await page.goto(pathToFileURL(tmp).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
// Seitenzahlen eintragen: feste Seiten zählen, im fließenden Lösungsteil die Position messen
await page.evaluate(() => {
  const mm = 96 / 25.4, seiteH = 297 * mm;
  const seiten = [...document.querySelectorAll('section.seite')];
  const seitenNr = el => {
    const sec = el.closest('section.seite');
    let nr = 1;
    for (const s of seiten) { if (s === sec) break; nr += Math.max(1, Math.ceil(s.getBoundingClientRect().height / seiteH - 0.02)); }
    return nr + Math.floor((el.getBoundingClientRect().top - sec.getBoundingClientRect().top) / seiteH);
  };
  document.querySelectorAll('[data-fall]').forEach(s => {
    const k = document.querySelector(`section.fall .kopf-nr`) && [...document.querySelectorAll('section.fall')].find(x => x.querySelector('.kopf-nr').textContent === s.dataset.fall);
    if (k) s.textContent = 'S. ' + seitenNr(k);
  });
  document.querySelectorAll('[data-loesungsteil]').forEach(s => { s.textContent = 'S. ' + seitenNr(document.getElementById('schluss')); });
});
await page.pdf({ path: output, format: 'A4', printBackground: true, preferCSSPageSize: true });
await browser.close();
fs.rmSync(tmp);
console.log(`✓ PDF: ${path.resolve(output)}`);
