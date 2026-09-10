/* ==========================================================================
   Rendert Folien und Stories mit Chromium (Playwright) als JPEG.
   Instagram akzeptiert für Bilder nur JPEG; 1080×1350 (4:5) und 1080×1920.
   ========================================================================== */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { chromium } from "playwright";
import { folieHtml, storyHtml, coverHtml, MASSE } from "./vorlagen.mjs";
import { stil as stilLaden, stilFuer } from "./stile.mjs";
import { FAECHER } from "./inhalte.mjs";
import { CONFIG } from "./config.mjs";

let browser = null;

export async function browserStarten() {
  if (browser) return browser;
  const executablePath = process.env.CHROMIUM_PATH || undefined;
  browser = await chromium.launch({ executablePath, args: ["--font-render-hinting=none"] });
  return browser;
}

export async function browserBeenden() {
  if (browser) { await browser.close(); browser = null; }
}

export function kontext(opt = {}) {
  const basis = opt.stil || CONFIG.marke.stil;
  const wechsel = CONFIG.marke.stilWechsel && !CONFIG.marke.farbeJeKlausur;
  const stilName = opt.variante != null ? stilFuer(basis, opt.variante, wechsel) : basis;
  return {
    stil: stilLaden(stilName),
    farbeJeKlausur: CONFIG.marke.farbeJeKlausur,
    handle: opt.handle ?? CONFIG.marke.handle,
    fachLabel: opt.fachLabel || (opt.fach ? FAECHER[opt.fach]?.label : "Steuerberaterexamen") || "Steuerberaterexamen",
    klausur: opt.klausur || (opt.fach ? FAECHER[opt.fach]?.klausur : 3) || 3,
  };
}

async function htmlZuJpeg(html, masse, zielPfad, skala = Number(process.env.IG_RENDER_SKALA || 1)) {
  const b = await browserStarten();
  const page = await b.newPage({ viewport: { width: masse.breite, height: masse.hoehe }, deviceScaleFactor: skala });
  const tmp = path.join(os.tmpdir(), `ig-${process.pid}-${Math.random().toString(36).slice(2)}.html`);
  fs.writeFileSync(tmp, html);
  try {
    await page.goto(`file://${tmp}`, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(einpassen);
    await page.waitForTimeout(60);
    fs.mkdirSync(path.dirname(zielPfad), { recursive: true });
    await page.screenshot({ path: zielPfad, type: "jpeg", quality: skala < 1 ? 80 : 92, fullPage: false });
  } finally {
    await page.close();
    fs.rmSync(tmp, { force: true });
  }
  return zielPfad;
}

/* Läuft im Browser: verkleinert Text, bis nichts mehr über den rechten Rand
   hinausragt und der Inhalt oberhalb der Fußzeile bleibt. */
function einpassen() {
  const wurzel = document.querySelector(".folie, .story");
  if (!wurzel) return;
  const px = (el) => parseFloat(getComputedStyle(el).fontSize);
  /* Untergrenzen: Ein Titel auf der ersten Folie darf nie unter 56 px fallen –
     darunter ist er im Feed-Vorschaubild nicht mehr zu entziffern, und dann
     nützt der beste Text nichts. Der Rest der Kachel darf weiter schrumpfen. */
  const untergrenze = (el) => (el.tagName === "H1" ? 56 : 28);
  const setze = (el, f) => { el.style.fontSize = `${Math.max(untergrenze(el), px(el) * f)}px`; };
  /* 1. Einzelne Zeilen/Blöcke, die breiter als ihr Platz sind (lange Wörter).
        Neben dem eigenen Überlauf zählt der rechte Rand der Kachel: Elemente
        mit „width:fit-content“ (im bunten Stil etwa die Titelpille) wachsen
        sonst über die Kachel hinaus, ohne selbst zu überlaufen. */
  const innenRechts = wurzel.getBoundingClientRect().right - parseFloat(getComputedStyle(wurzel).paddingRight || 0);
  for (const el of wurzel.querySelectorAll("h1,h2,h3,.merke,.norm,.zahl-unter,.karte .t,.pille,.ueberzeile,.formel,.zeile")) {
    let n = 0;
    while ((el.scrollWidth > el.clientWidth + 1 || el.getBoundingClientRect().right > innenRechts + 1) && n++ < 20) setze(el, 0.94);
  }
  /* 2. Gesamthöhe: Fußzeile muss innerhalb der Kachel bleiben. Liegt ein Foto
        auf der Kachel, ist dessen Oberkante die Grenze – sonst schiebt sich
        der Titel darüber und wird unlesbar. */
  const fuss = wurzel.querySelector(".fuss");
  const foto = wurzel.querySelector(".foto");
  const grenze = foto ? foto.getBoundingClientRect().top - 16 : wurzel.getBoundingClientRect().bottom - 24;
  const textElemente = [...wurzel.querySelectorAll("h1,h2,h3,p,li,.text,.merke,.norm,.zahl,.zahl-unter,.karte,.optionen div,.rechnung,.spalte,.unter,.hinweis,.pfeil")];
  let n = 0;
  const ausser = (c) => c.classList.contains("geist") || c.classList.contains("illu") || c.classList.contains("foto") || c.classList.contains("bildquelle") || c.classList.contains("fuss");
  const passt = () => {
    const unten = Math.max(...textElemente.map((e) => e.getBoundingClientRect().bottom));
    const kinderUnten = Math.max(...[...wurzel.children].filter((c) => !ausser(c)).map((c) => c.getBoundingClientRect().bottom));
    const fussOk = foto || !fuss || fuss.getBoundingClientRect().bottom <= wurzel.getBoundingClientRect().bottom - 8;
    return unten <= grenze + 24 && kinderUnten <= grenze + 24 && fussOk && wurzel.scrollHeight <= wurzel.clientHeight + 1;
  };
  while (!passt() && n++ < 14) for (const el of textElemente) setze(el, 0.95);
}

/* Rendert alle Folien eines Beitrags → Liste der JPEG-Pfade. */
export async function beitragRendern(beitrag, zielVerzeichnis, opt = {}) {
  const ctx = kontext({ ...opt, fach: beitrag.fach, klausur: beitrag.klausur, fachLabel: beitrag.fachLabel, variante: opt.variante ?? beitrag.variante });
  const pfade = [];
  const n = beitrag.folien.length;
  for (let i = 0; i < n; i++) {
    const html = folieHtml(beitrag.folien[i], ctx, i + 1, n);
    const ziel = path.join(zielVerzeichnis, `${beitrag.slug || "beitrag"}-${String(i + 1).padStart(2, "0")}.jpg`);
    pfade.push(await htmlZuJpeg(html, MASSE.beitrag, ziel));
  }
  return pfade;
}

export async function storyRendern(story, zielPfad, opt = {}) {
  const ctx = kontext({ ...opt, fach: story.fach, klausur: story.klausur, fachLabel: story.fachLabel, variante: opt.variante ?? story.variante });
  return htmlZuJpeg(storyHtml(story, ctx), MASSE.story, zielPfad);
}

/* Cover eines Reels (Standbild für Feed und Profilraster). */
export async function coverRendern(daten, zielPfad, opt = {}) {
  const ctx = kontext({ ...opt, fach: daten.fach, klausur: daten.klausur, fachLabel: daten.fachLabel });
  return htmlZuJpeg(coverHtml(daten, ctx), MASSE.story, zielPfad);
}
