#!/usr/bin/env node
/* ==========================================================================
   Vorschau der Newsletter-Seiten – ohne Cloudflare, ohne Bereitstellung.

   Der Worker ist eine einzige fetch-Funktion. Sie lässt sich hier mit einer
   nachgebauten Umgebung aufrufen und das Ergebnis als HTML ablegen; mit
   Playwright entstehen zusätzlich Bildschirmfotos. So lässt sich am Aussehen
   arbeiten, ohne jedes Mal zu deployen und ohne dass echte Mails fliegen.

   Aufruf:  node bin/newsletter-vorschau.mjs [--bilder]
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import worker, { tokenBauen } from "../newsletter/worker.mjs";

const ZIEL = "out/newsletter";
const GEHEIM = "vorschau-geheimnis";
const UMGEBUNG = {
  NEWSLETTER_SECRET: GEHEIM,
  GITHUB_REPO: "Ccan-devoloper/herrjurist",
  GITHUB_TOKEN: "",
  MARKE: "Herr Jurist",
  ANBIETER: "Vorname Nachname (Platzhalter)",
  ANSCHRIFT: "Straße 1, 12345 Ort (Platzhalter)",
  KONTAKT: "kontakt@example.de (Platzhalter)",
};
/* Der Worker schickt Ereignisse an GitHub. In der Vorschau darf das nichts
   auslösen. waitUntil allein genügt dafür nicht: Die Anfrage entsteht schon
   beim Aufruf, nicht erst beim Einlösen. Deshalb wird der Weg nach GitHub
   hier abgefangen - sonst liefe die Vorschau gegen die echte Schnittstelle. */
const ctx = { waitUntil() {} };
const echtesFetch = globalThis.fetch;
globalThis.fetch = async (eingabe, init) => {
  const adresse = String(eingabe?.url || eingabe);
  if (adresse.includes("api.github.com")) {
    console.log(`  (abgefangen: ${JSON.parse(init.body).event_type} → GitHub)`);
    return new Response(null, { status: 204 });
  }
  return echtesFetch(eingabe, init);
};

async function hole(pfad, opt = {}) {
  const antwort = await worker.fetch(new Request(`https://vorschau.test${pfad}`, {
    headers: { "cf-connecting-ip": "203.0.113.7" }, ...opt,
  }), UMGEBUNG, ctx);
  return { status: antwort.status, html: await antwort.text() };
}

const seiten = [];
async function ablegen(name, pfad, opt) {
  const { status, html } = await hole(pfad, opt);
  const datei = path.join(ZIEL, `${name}.html`);
  fs.writeFileSync(datei, html);
  seiten.push({ name, datei, status, groesse: html.length });
  console.log(`  ${status}  ${name.padEnd(14)} ${(html.length / 1024).toFixed(1)} kB  ${datei}`);
}

fs.mkdirSync(ZIEL, { recursive: true });
console.log("Seiten:");
await ablegen("start", "/");
await ablegen("uebersicht", `/uebersicht?t=${encodeURIComponent(await tokenBauen("max@beispiel.de", "datei", 3600e3, GEHEIM))}`);
await ablegen("bestaetigt", `/ja?t=${encodeURIComponent(await tokenBauen("max@beispiel.de", "doi", 3600e3, GEHEIM))}`);
await ablegen("abgelaufen", "/ja?t=kaputt");
await ablegen("impressum", "/impressum");
await ablegen("datenschutz", "/datenschutz");

/* Der Postweg lässt sich hier nicht nachstellen (dafür braucht es GitHub und
   SMTP), das Formular selbst aber schon: Ohne gültiges Ticket weist der
   Worker ab - genau das soll er. */
const abgewiesen = await hole("/anmelden", {
  method: "POST",
  body: new URLSearchParams({ email: "max@beispiel.de", ticket: "erfunden" }),
});
console.log(`\nFormular ohne gültiges Ticket: ${abgewiesen.html.includes("noch einmal absenden") ? "abgewiesen ✓" : "DURCHGELASSEN ✗"}`);

if (process.argv.includes("--bilder")) {
  const { chromium } = await import("playwright");
  /* PLAYWRIGHT_CHROMIUM: Notausgang, wenn der Browser nicht dort liegt, wo
     Playwright ihn erwartet (vorinstallierte Umgebungen, anderer Cache). */
  const eigenerBrowser = process.env.PLAYWRIGHT_CHROMIUM || "";
  const browser = await chromium.launch(eigenerBrowser ? { executablePath: eigenerBrowser } : {});
  for (const s of seiten) {
    const seite = await browser.newPage({ viewport: { width: 430, height: 932 }, deviceScaleFactor: 2 });
    await seite.goto(`file://${path.resolve(s.datei)}`, { waitUntil: "load" });
    await seite.waitForTimeout(400);
    const bild = path.join(ZIEL, `${s.name}.png`);
    await seite.screenshot({ path: bild, fullPage: s.name !== "uebersicht" });
    console.log(`  Bild: ${bild}`);
    await seite.close();
  }

  /* Der Gegenwert der Anmeldung ist am Ende ein PDF, das jemand auf dem Handy
     oder ausgedruckt durchgeht. Das entsteht beim Leser über „Drucken → Als
     PDF sichern“ - also muss hier auch genau dieser Weg geprüft werden und
     nicht nur, wie die Seite am Bildschirm aussieht. */
  const druck = await browser.newPage();
  await druck.goto(`file://${path.resolve(ZIEL, "uebersicht.html")}`, { waitUntil: "load" });
  await druck.emulateMedia({ media: "print" });
  await druck.pdf({ path: path.join(ZIEL, "uebersicht.pdf"), format: "A4", printBackground: false });
  console.log(`  PDF:  ${path.join(ZIEL, "uebersicht.pdf")}`);
  await druck.close();
  await browser.close();
}
