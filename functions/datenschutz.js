// Cloudflare Pages Function: GET /datenschutz – Datenschutzerklärung für Landingpage und Wochenbrief.
// Verantwortliche Stelle aus ANBIETER, ANSCHRIFT, KONTAKT (siehe _lib/rechtliches.js).
import { angaben, seite } from "./_lib/rechtliches.js";

export function onRequestGet({ env }) {
  const { block } = angaben(env);
  return seite("Datenschutz", `<h1>Datenschutzerklärung</h1>
<p>für diese Seite und den Wochenbrief von LexVerse by herrjurist</p>

<h2>1. Verantwortliche Stelle</h2>
${block}

<h2>2. Aufruf dieser Seite</h2>
<p>Die Seite wird über Cloudflare Pages ausgeliefert (Cloudflare, Inc., San Francisco, USA). Beim Aufruf verarbeitet Cloudflare technisch notwendige Daten wie IP-Adresse, Zeitpunkt und aufgerufene Adresse, um die Seite auszuliefern und vor Angriffen zu schützen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Wir setzen keine Cookies, keine Analyse- und keine Werbewerkzeuge ein. Schriften und Bilder liegen auf unserem eigenen Server.</p>

<h2>3. Anmeldung zum Wochenbrief</h2>
<p>Wenn du dich einträgst, verarbeiten wir deine E-Mail-Adresse, freiwillig deinen Vornamen und den Zeitpunkt der Anmeldung. Damit schicken wir dir einmal pro Woche den Wochenbrief mit Minifällen und Klausurwissen. Rechtsgrundlage ist deine Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
<p>Die Anmeldung wird zunächst im Speicher von Cloudflare abgelegt und dann an unseren Versanddienst Brevo übertragen. So geht keine Anmeldung verloren, wenn Brevo kurz nicht erreichbar ist.</p>

<h2>4. Versanddienst Brevo</h2>
<p>Der Versand läuft über Brevo (Sendinblue GmbH, Köpenicker Straße 126, 10179 Berlin). Brevo verarbeitet deine Daten in unserem Auftrag auf Servern in der EU. Brevo wertet aus, ob eine Mail geöffnet und welcher Link angeklickt wurde. Das hilft uns, den Wochenbrief zu verbessern. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Du kannst dem jederzeit über die Abmeldung widersprechen.</p>

<h2>5. Auftragsverarbeiter und Übermittlung in die USA</h2>
<p>Mit Brevo und Cloudflare bestehen Verträge zur Auftragsverarbeitung (Art. 28 DSGVO). Soweit Cloudflare Daten in den USA verarbeitet, geschieht das auf Grundlage des EU-US Data Privacy Framework bzw. der Standardvertragsklauseln der EU-Kommission (Art. 45, 46 Abs. 2 lit. c DSGVO).</p>

<h2>6. Speicherdauer und Abmeldung</h2>
<p>Deine Daten speichern wir, bis du dich abmeldest. Der Link zum Abmelden steht in jeder Mail. Danach löschen wir die Adresse. Damit wir dich nicht versehentlich erneut anschreiben, kann Brevo sie auf einer Sperrliste behalten. Den Zwischenspeicher bei Cloudflare leeren wir regelmäßig.</p>

<h2>7. Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). Eine Einwilligung kannst du jederzeit für die Zukunft widerrufen (Art. 7 Abs. 3 DSGVO). Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren.</p>

<p style="margin-top:2rem;color:#5c5c68">Stand: Oktober 2026</p>`);
}
