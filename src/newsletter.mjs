/* ==========================================================================
   Newsletter – gemeinsame Logik für den Cloudflare-Worker (Anmeldeseite) und
   den GitHub-Actions-Lauf (Versand, Liste).

   Die Liste liegt AES-256-GCM-verschlüsselt im Asset-Zweig. Das ist keine
   Kür: Das Repository ist öffentlich. Eine Datei mit E-Mail-Adressen im
   Klartext wäre dort für jeden lesbar und obendrein dauerhaft in der
   Git-Historie – ein Datenleck, das sich nicht zurücknehmen lässt. Der
   Schlüssel steht nur in den Secrets.

   Anmeldung läuft über Double-Opt-In: Wer die Adresse einträgt, landet noch
   auf keiner Liste. Erst der Klick im Bestätigungslink schreibt sie. Das ist
   in Deutschland der belastbare Weg (§ 7 UWG, Einwilligung nach Art. 6
   Abs. 1 lit. a DSGVO) – und ganz praktisch hält es Tippfehler und fremde
   Adressen draußen, die eine Liste sonst still vergiften.

   Zustandslos bis zur Bestätigung: Der Bestätigungslink trägt die Adresse
   signiert in sich (HMAC-SHA256). Deshalb braucht die Anmeldung keine
   Datenbank und keinen Speicherplatz – und ein Angreifer kann sich ohne den
   Schlüssel keinen gültigen Link bauen.
   ========================================================================== */

import crypto from "node:crypto";

export const ZWECKE = { doi: "doi", datei: "datei", abmelden: "abmelden" };

/* Ein Geheimnis, drei Verwendungen – jede mit eigener Ableitung. Derselbe
   Schlüssel für Signatur und Verschlüsselung wäre schlechte Praxis; die
   getrennte Ableitung kostet nichts und hält die Zwecke sauber auseinander. */
export function schluessel(geheim, zweck) {
  if (!geheim) throw new Error("NEWSLETTER_SECRET fehlt");
  return crypto.createHash("sha256").update(`herrjurist-newsletter-v1|${zweck}|${geheim}`).digest();
}

const b64url = (buf) => Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const vonB64url = (s) => Buffer.from(String(s).replace(/-/g, "+").replace(/_/g, "/"), "base64");

/* Vergleich in konstanter Zeit. Ein früher Abbruch verrät über die Laufzeit,
   wie viele Zeichen stimmten. */
function gleich(a, b) {
  const x = Buffer.from(String(a)), y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
}

export function tokenBauen({ email, zweck = ZWECKE.doi, gueltigMs = 48 * 3600e3 }, geheim, jetzt = Date.now()) {
  const nutzlast = b64url(JSON.stringify({ e: String(email).toLowerCase(), z: zweck, exp: jetzt + gueltigMs }));
  const sig = b64url(crypto.createHmac("sha256", schluessel(geheim, "token")).update(nutzlast).digest());
  return `${nutzlast}.${sig}`;
}

/* Gibt die Adresse zurück oder null. Kein Werfen: Ein abgelaufener oder
   verdrehter Link ist der Normalfall (Mail von gestern, Zeilenumbruch im
   Mailprogramm) und soll eine freundliche Seite zeigen, keinen Fehler. */
export function tokenLesen(token, geheim, { zweck = ZWECKE.doi, jetzt = Date.now() } = {}) {
  const [nutzlast, sig] = String(token || "").split(".");
  if (!nutzlast || !sig) return null;
  const soll = b64url(crypto.createHmac("sha256", schluessel(geheim, "token")).update(nutzlast).digest());
  if (!gleich(soll, sig)) return null;
  let d;
  try { d = JSON.parse(vonB64url(nutzlast).toString("utf8")); } catch { return null; }
  if (d?.z !== zweck) return null;
  if (!Number.isFinite(d?.exp) || d.exp < jetzt) return null;
  return String(d.e || "").toLowerCase() || null;
}

/* --- Adressprüfung -------------------------------------------------------- */
/* Bewusst nachsichtig: Die Aufgabe ist, Unsinn und Kopfzeilen-Einschleusung
   abzuwehren, nicht RFC 5322 nachzubauen. Ob die Adresse existiert, beweist
   ohnehin erst der Klick in der Bestätigungsmail. */
export function emailGueltig(email) {
  const s = String(email || "").trim();
  if (s.length < 6 || s.length > 254) return false;
  if (/[\s<>,;"\\\r\n]/.test(s)) return false;
  return /^[^@]+@[^@.]+(\.[^@.]+)+$/.test(s);
}

export const adresseNormal = (email) => String(email || "").trim().toLowerCase();

/* --- Liste ---------------------------------------------------------------- */
export const LISTE_LEER = { version: 1, eintraege: [] };
export const MAX_EINTRAEGE = 5000;

export function listeLesen(text, geheim) {
  if (!text || !String(text).trim()) return structuredClone(LISTE_LEER);
  const buf = vonB64url(String(text).trim());
  const iv = buf.subarray(0, 12), tag = buf.subarray(12, 28), enc = buf.subarray(28);
  const d = crypto.createDecipheriv("aes-256-gcm", schluessel(geheim, "liste"), iv);
  d.setAuthTag(tag);
  const klar = JSON.parse(Buffer.concat([d.update(enc), d.final()]).toString("utf8"));
  return { version: 1, eintraege: Array.isArray(klar?.eintraege) ? klar.eintraege : [] };
}

export function listeSchreiben(liste, geheim) {
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv("aes-256-gcm", schluessel(geheim, "liste"), iv);
  const enc = Buffer.concat([c.update(JSON.stringify(liste), "utf8"), c.final()]);
  return b64url(Buffer.concat([iv, c.getAuthTag(), enc]));
}

/* Bestätigte Anmeldung eintragen. Zweimal derselbe Klick ändert nichts – ein
   Bestätigungslink liegt bis zu 48 Stunden im Postfach und wird erfahrungs-
   gemäß auch mal zweimal angetippt. */
export function eintragen(liste, email, { jetzt = new Date(), quelle = "landingpage" } = {}) {
  const adresse = adresseNormal(email);
  const eintraege = liste.eintraege || [];
  const da = eintraege.find((e) => e.adresse === adresse);
  if (da) {
    if (da.abgemeldet) { delete da.abgemeldet; da.bestaetigt = jetzt.toISOString(); return { liste: { ...liste, eintraege }, neu: true, erneut: true }; }
    return { liste: { ...liste, eintraege }, neu: false, erneut: false };
  }
  if (eintraege.length >= MAX_EINTRAEGE) throw new Error(`Liste voll (${MAX_EINTRAEGE}) – im Testbetrieb gewollt.`);
  eintraege.push({ adresse, bestaetigt: jetzt.toISOString(), quelle });
  return { liste: { ...liste, eintraege }, neu: true, erneut: false };
}

/* Abmeldung: Der Eintrag wird markiert, nicht gelöscht. Wer sich abmeldet,
   darf nicht durch eine spätere Wiederanmeldung von fremder Hand zurück auf
   die Liste geraten, ohne erneut zu bestätigen – und der Nachweis, dass
   abgemeldet wurde, ist bei einer Beschwerde das, was zählt. Die Adresse
   bleibt dafür nötig; sie steht verschlüsselt. */
export function austragen(liste, email, { jetzt = new Date() } = {}) {
  const adresse = adresseNormal(email);
  const eintraege = liste.eintraege || [];
  const da = eintraege.find((e) => e.adresse === adresse);
  if (!da) return { liste: { ...liste, eintraege }, geaendert: false };
  if (da.abgemeldet) return { liste: { ...liste, eintraege }, geaendert: false };
  da.abgemeldet = jetzt.toISOString();
  return { liste: { ...liste, eintraege }, geaendert: true };
}

export const aktiveAdressen = (liste) => (liste?.eintraege || []).filter((e) => !e.abgemeldet).map((e) => e.adresse);

/* --- Mailtexte ------------------------------------------------------------
   Klartext, keine Bilder, kein HTML-Gerüst. Eine Bestätigungsmail mit Grafik
   und Tracking landet häufiger im Spam als eine, die aussieht, als hätte sie
   ein Mensch getippt – und mehr braucht sie nicht. */
export function doiMail({ bestaetigenUrl, marke = "Herr Jurist" }) {
  return {
    betreff: `Bitte bestätigen: deine Examens-Übersicht von ${marke}`,
    text: [
      "Fast geschafft.",
      "",
      "Klicke einmal auf diesen Link, dann bekommst du die Übersicht sofort angezeigt",
      "und stehst auf der Liste für neue Ausgaben:",
      "",
      bestaetigenUrl,
      "",
      "Der Link gilt 48 Stunden.",
      "",
      "Du hast das nicht angefordert? Dann ignoriere diese Mail einfach – ohne",
      "Klick wird nichts gespeichert und du bekommst nichts weiter von uns.",
      "",
      marke,
    ].join("\n"),
  };
}

export function willkommenMail({ uebersichtUrl, abmeldenUrl, marke = "Herr Jurist" }) {
  return {
    betreff: `Deine Examens-Übersicht – ${marke}`,
    text: [
      "Danke für die Bestätigung. Hier ist deine Übersicht:",
      "",
      uebersichtUrl,
      "",
      "Die Seite lässt sich im Browser über „Drucken → Als PDF sichern“ speichern,",
      "damit du sie offline auf dem Handy oder Tablet dabei hast.",
      "",
      "Du stehst jetzt auf der Liste und bekommst neue Ausgaben, sobald es welche",
      "gibt. Abmelden geht jederzeit mit einem Klick:",
      abmeldenUrl,
      "",
      marke,
    ].join("\n"),
  };
}
