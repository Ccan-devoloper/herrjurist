#!/usr/bin/env node
/* ==========================================================================
   Newsletter-Gegenstelle im Actions-Lauf.

   Der Worker kann kein SMTP – Cloudflare Workers sprechen kein Mailprotokoll.
   Er stößt deshalb nur einen repository_dispatch an; hier wird die Mail mit
   denselben SMTP-Zugängen verschickt, die der Wochenbericht ohnehin nutzt.
   Kein weiterer Dienst, keine weitere Rechnung, kein weiteres Konto.

   Die Adresse kommt NICHT als freies Feld herein, sondern im signierten
   Token. Wer den Dispatch auslöst, kann sie also nicht austauschen – und im
   Protokoll steht sie nur maskiert, denn die Läufe eines öffentlichen
   Repositories sind öffentlich lesbar.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import nodemailer from "nodemailer";
import {
  tokenBauen, tokenLesen, listeLesen, listeSchreiben, eintragen, austragen,
  aktiveAdressen, doiMail, willkommenMail,
} from "../src/newsletter.mjs";

const arg = (name, standard = "") => {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : standard;
};

const geheim = process.env.NEWSLETTER_SECRET || "";
const basis = String(process.env.NEWSLETTER_URL || "").replace(/\/+$/, "");
const marke = process.env.IG_MARKE || "Herr Jurist";
const ereignis = arg("ereignis", process.env.NL_EREIGNIS || "");
const token = process.env.NL_TOKEN || "";
const datei = arg("datei", "state/newsletter.enc");
const zahlenDatei = arg("zahlen", "state/newsletter-zahlen.json");

/* Im Protokoll eines öffentlichen Repositories darf keine vollständige
   Adresse stehen. Genug zum Wiedererkennen, zu wenig zum Anschreiben. */
const maskiert = (email) => {
  const [n, d = ""] = String(email).split("@");
  return `${n.slice(0, 1)}${"*".repeat(Math.max(2, n.length - 1))}@${d}`;
};

function versand() {
  const host = process.env.SMTP_HOST, user = process.env.SMTP_USER;
  if (!host || !user) return null;
  return nodemailer.createTransport({
    host, port: Number(process.env.SMTP_PORT || 587),
    secure: Number(process.env.SMTP_PORT || 587) === 465,
    auth: { user, pass: process.env.SMTP_PASS },
  });
}

async function mailen(an, { betreff, text }) {
  const transport = versand();
  if (!transport) { console.log("  ! SMTP nicht eingerichtet – Mail nicht verschickt."); return false; }
  await transport.sendMail({ from: process.env.SMTP_FROM || process.env.SMTP_USER, to: an, subject: betreff, text });
  return true;
}

const listeLaden = () => listeLesen(fs.existsSync(datei) ? fs.readFileSync(datei, "utf8") : "", geheim);

function listeSichern(liste) {
  fs.mkdirSync(path.dirname(datei), { recursive: true });
  fs.writeFileSync(datei, listeSchreiben(liste, geheim));
  const aktiv = aktiveAdressen(liste).length;
  fs.writeFileSync(zahlenDatei, `${JSON.stringify({
    stand: new Date().toISOString(),
    aktiv,
    abgemeldet: (liste.eintraege || []).length - aktiv,
  }, null, 2)}\n`);
  console.log(`  Liste: ${aktiv} aktiv, ${(liste.eintraege || []).length - aktiv} abgemeldet.`);
}

async function main() {
  if (!geheim) throw new Error("NEWSLETTER_SECRET fehlt – ohne das Geheimnis ist kein Token prüfbar.");
  if (!basis && ereignis !== "zeigen") throw new Error("NEWSLETTER_URL fehlt – ohne die Adresse des Workers gäbe es Links ins Leere.");

  if (ereignis === "newsletter-anmeldung") {
    const email = tokenLesen(token, geheim, { zweck: "doi" });
    if (!email) { console.log("  ! Token ungültig oder abgelaufen – nichts getan."); return; }
    await mailen(email, doiMail({ bestaetigenUrl: `${basis}/ja?t=${encodeURIComponent(token)}`, marke }));
    console.log(`  ✉ Bestätigungsmail an ${maskiert(email)} – noch nichts gespeichert.`);
    return;
  }

  if (ereignis === "newsletter-bestaetigt") {
    const email = tokenLesen(token, geheim, { zweck: "doi" });
    if (!email) { console.log("  ! Token ungültig oder abgelaufen – nichts getan."); return; }
    const { liste, neu } = eintragen(listeLaden(), email, { quelle: "landingpage" });
    listeSichern(liste);
    if (neu) {
      const dateiToken = tokenBauen({ email, zweck: "datei", gueltigMs: 365 * 24 * 3600e3 }, geheim);
      const abToken = tokenBauen({ email, zweck: "abmelden", gueltigMs: 365 * 24 * 3600e3 }, geheim);
      await mailen(email, willkommenMail({
        uebersichtUrl: `${basis}/uebersicht?t=${encodeURIComponent(dateiToken)}`,
        abmeldenUrl: `${basis}/abmelden?t=${encodeURIComponent(abToken)}`,
        marke,
      }));
      console.log(`  ✓ ${maskiert(email)} bestätigt und eingetragen, Willkommensmail raus.`);
    } else {
      console.log(`  · ${maskiert(email)} stand schon auf der Liste – keine zweite Mail.`);
    }
    return;
  }

  /* Von Hand: Wer steht drauf? Läuft nur lokal mit dem Geheimnis in der Hand -
     im Actions-Lauf hat dieser Zweig nichts zu suchen und wird dort auch nicht
     aufgerufen. Ohne ihn wäre die verschlüsselte Liste eine Einbahnstraße. */
  if (ereignis === "zeigen") {
    const liste = listeLaden();
    for (const e of liste.eintraege || []) {
      console.log(`${e.abgemeldet ? "abgemeldet" : "aktiv     "}  ${e.bestaetigt?.slice(0, 10) || "?"}  ${e.adresse}`);
    }
    console.log(`\n${aktiveAdressen(liste).length} aktiv von ${(liste.eintraege || []).length} insgesamt.`);
    return;
  }

  if (ereignis === "newsletter-abmeldung") {
    const email = tokenLesen(token, geheim, { zweck: "abmelden" });
    if (!email) { console.log("  ! Token ungültig oder abgelaufen – nichts getan."); return; }
    const { liste, geaendert } = austragen(listeLaden(), email);
    listeSichern(liste);
    console.log(geaendert ? `  ✓ ${maskiert(email)} abgemeldet.` : `  · ${maskiert(email)} war nicht (mehr) auf der Liste.`);
    return;
  }

  throw new Error(`Unbekanntes Ereignis: ${ereignis}`);
}

main().catch((e) => { console.error(`✗ ${e.message}`); process.exit(1); });
