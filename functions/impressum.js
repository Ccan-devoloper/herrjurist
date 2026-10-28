// Cloudflare Pages Function: GET /impressum – Angaben aus ANBIETER, ANSCHRIFT, KONTAKT (siehe _lib/rechtliches.js)
import { angaben, seite } from "./_lib/rechtliches.js";

export function onRequestGet({ env }) {
  const { block } = angaben(env);
  return seite("Impressum", `<h1>Impressum</h1>
<h2>Angaben gemäß § 5 DDG</h2>
${block}
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
${block}
<h2>Hinweis</h2>
<p>Die Inhalte des Wochenbriefs und dieser Seite dienen der Ausbildung und allgemeinen Information. Sie sind keine Rechtsberatung im Einzelfall.</p>
<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>`);
}
