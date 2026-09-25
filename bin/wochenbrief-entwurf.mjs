#!/usr/bin/env node
/* Lokaler Entwurf: pruefen oder E-Mail-HTML erzeugen. Keine API, kein Versand. */
import fs from 'node:fs';
import path from 'node:path';
import { pruefeWochenbrief, rendereWochenbrief } from '../newsletter/wochenbrief-vorlage.mjs';

const [input, output] = process.argv.slice(2);
if (!input || process.argv.includes('--help') || (output && output.startsWith('--'))) {
  console.log('Aufruf: node bin/wochenbrief-entwurf.mjs /lokaler-pfad/entwurf.json [/lokaler-pfad/entwurf.html]');
  process.exit(input ? 0 : 2);
}

try {
  const draft = JSON.parse(fs.readFileSync(input, 'utf8'));
  const errors = pruefeWochenbrief(draft);
  if (errors.length) throw new Error(errors.map(e => `- ${e}`).join('\n'));
  console.log(`✓ ${draft.issue.topic_count} Themen und Lösungsskizzen geprüft (formale Regeln).`);
  if (output) {
    const target = path.resolve(output);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, rendereWochenbrief(draft));
    console.log(`✓ Nur lokale HTML-Vorschau: ${target}`);
  }
} catch (error) {
  console.error(`✗ Entwurf nicht verwendbar:\n${error.message}`);
  process.exitCode = 1;
}
