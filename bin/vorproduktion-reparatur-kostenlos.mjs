#!/usr/bin/env node
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { Hosting } from "../src/hosting.mjs";
import { chromium } from "playwright";
import { storyHtml, coverHtml, MASSE } from "../src/vorlagen.mjs";
import { stil as stilLaden } from "../src/stile.mjs";
import { CONFIG } from "../src/config.mjs";
import { beitragRendern, browserBeenden as renderBrowserBeenden } from "../src/render.mjs";

for (const key of ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY", "PEXELS_API_KEY"]) {
  if (process.env[key]) throw new Error(`Kostenlose Reparatur verweigert Provider-Secret: ${key}`);
}

const specPfad = process.argv[2] || "vorproduktion/reparatur.trigger";
const spec = JSON.parse(fs.readFileSync(specPfad, "utf8"));
const hosting = new Hosting({ pushen: true }).vorbereiten();
const temp = fs.mkdtempSync(path.join(os.tmpdir(), "hj-reparatur-kostenlos-"));

function coverDatenLokal(reel) {
  return {
    titel: reel.kurztitel || reel.szenen?.[0]?.titel || "Reel",
    titelZeilen: reel.titelZeilen || null,
    coverBadge: reel.coverBadge || "Reel",
    coverText: reel.coverText || null,
    coverHinweisPlan: reel.coverHinweisPlan || null,
    icon: reel.szenen?.find((s) => s.icon)?.icon || "paragraf",
    bild: reel.bild || null,
    bildFrei: reel.bildFrei !== false,
    bildQuelle: null,
    bildBreite: reel.bildBreite || null,
    bildHoehe: reel.bildHoehe || null,
    bildTyp: reel.bildTyp || null,
    fach: reel.fach,
    klausur: reel.klausur,
    fachLabel: reel.fachLabel || "Examenswissen",
  };
}

let browser = null;
async function browserStarten() {
  if (!browser) browser = await chromium.launch({ args: ["--font-render-hinting=none"] });
  return browser;
}
function ctxFuer(x = {}) {
  return {
    stil: stilLaden("bunt"),
    farbeJeKlausur: CONFIG.marke.farbeJeKlausur,
    handle: CONFIG.marke.handle,
    fach: x.fach || null,
    fachLabel: x.fachLabel || "Examenswissen",
    klausur: x.klausur ?? 3,
  };
}
function storyTitelEinpassenLokal() {
  const wurzel = document.querySelector(".story:not(.cover)");
  const titel = wurzel?.querySelector("h1");
  if (!wurzel || !titel) return;

  const text = String(titel.textContent || "").trim().replace(/\s+/g, " ");
  if (!text || text.length > 44) return;

  titel.style.width = "max-content";
  titel.style.maxWidth = "100%";
  titel.style.textWrap = "wrap";

  const zeilen = () => {
    const cs = getComputedStyle(titel);
    const lh = parseFloat(cs.lineHeight);
    const innen = titel.clientHeight
      - parseFloat(cs.paddingTop || 0)
      - parseFloat(cs.paddingBottom || 0);
    return lh > 0 ? Math.max(1, Math.round(innen / lh)) : 1;
  };
  const horizontalPasst = () => {
    const root = wurzel.getBoundingClientRect();
    const rs = getComputedStyle(wurzel);
    const links = root.left + parseFloat(rs.paddingLeft || 0);
    const rechts = root.right - parseFloat(rs.paddingRight || 0);
    const b = titel.getBoundingClientRect();
    return titel.scrollWidth <= titel.clientWidth + 1 && b.left >= links - 1 && b.right <= rechts + 1;
  };

  let groesse = parseFloat(getComputedStyle(titel).fontSize);
  const mindest = 50;
  let n = 0;
  while ((zeilen() > 2 || !horizontalPasst()) && groesse > mindest + 0.5 && n++ < 24) {
    groesse = Math.max(mindest, groesse * 0.96);
    titel.style.fontSize = `${groesse}px`;
  }
  if (zeilen() > 2 || !horizontalPasst()) {
    throw new Error(`Kurzer Story-Titel passt trotz Auto-Fit nicht in die Markenpille: ${text}`);
  }
}

function lokalEinpassen() {
  const wurzel = document.querySelector(".story");
  if (!wurzel) return;
  const px = (el) => parseFloat(getComputedStyle(el).fontSize);
  const setze = (el, f) => { el.style.fontSize = `${Math.max(el.tagName === "H1" ? 64 : 28, px(el) * f)}px`; };
  const innenRechts = wurzel.getBoundingClientRect().right - parseFloat(getComputedStyle(wurzel).paddingRight || 0);
  const elemente = [...wurzel.querySelectorAll("h1,h2,h3,.text,.norm,.karte,.karte .t,.karte .u,.ueberzeile")];
  for (const el of elemente) {
    let n = 0;
    while ((el.scrollWidth > el.clientWidth + 1 || el.getBoundingClientRect().right > innenRechts + 1) && n++ < 16) setze(el, 0.94);
  }
}
function coverTitelEinpassenLokal() {
  const wurzel = document.querySelector(".story.cover");
  const titel = wurzel?.querySelector("h1.titel-stack");
  if (!wurzel || !titel) return;
  const root = wurzel.getBoundingClientRect();
  const cs = getComputedStyle(wurzel);
  const rechts = root.right - Math.max(24, parseFloat(cs.paddingRight || 0));
  const links = root.left + Math.max(24, parseFloat(cs.paddingLeft || 0));
  const passt = () => [...titel.querySelectorAll(".titel-zeile")].every((z) => {
    const b = z.getBoundingClientRect();
    return z.scrollWidth <= z.clientWidth + 1 && b.left >= links - 1 && b.right <= rechts + 1;
  });
  let groesse = parseFloat(getComputedStyle(titel).fontSize);
  let n = 0;
  while (!passt() && groesse > 84.5 && n++ < 16) {
    groesse = Math.max(84, groesse * 0.94);
    titel.style.fontSize = `${groesse}px`;
  }
  if (!passt()) throw new Error("Reel-Cover-Titel passt auch nach lokalem Auto-Fit nicht.");
}
async function htmlZuJpegLokal(html, ziel, masse = MASSE.story) {
  const b = await browserStarten();
  const page = await b.newPage({ viewport: { width: masse.breite, height: masse.hoehe } });
  const tmpHtml = path.join(temp, `seite-${Math.random().toString(36).slice(2)}.html`);
  fs.writeFileSync(tmpHtml, html);
  try {
    await page.goto(`file://${tmpHtml}`, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(storyTitelEinpassenLokal);
    await page.evaluate(lokalEinpassen);
    await page.evaluate(coverTitelEinpassenLokal);
    fs.mkdirSync(path.dirname(ziel), { recursive: true });
    await page.screenshot({ path: ziel, type: "jpeg", quality: 92, fullPage: false });
  } finally {
    await page.close();
    fs.rmSync(tmpHtml, { force: true });
  }
}
async function storyRendernLokal(story, ziel) {
  return htmlZuJpegLokal(storyHtml(story, ctxFuer(story)), ziel, MASSE.story);
}
async function coverRendernLokal(daten, ziel) {
  return htmlZuJpegLokal(coverHtml(daten, ctxFuer(daten)), ziel, MASSE.story);
}
function teaserFuer(slot, beitrag, beitragSlot) {
  return {
    slot,
    art: "teaser",
    fach: beitrag.fach,
    klausur: beitrag.klausur,
    fachLabel: beitrag.fachLabel || "Examenswissen",
    titel: beitrag.kurztitel || beitrag.folien?.[0]?.titel || beitrag.szenen?.[0]?.titel || "Neuer Beitrag",
    text: "Der vollständige Beitrag ist jetzt im Feed.",
    pille: "Jetzt im Feed",
    beitragSlot,
    abgeleitet: true,
    freigabeBetreiber: false,
    vorproduktionStatus: "review",
    textProviderKostenUsd: 0,
    faktencheckProviderKostenUsd: 0,
    bildStatus: "bereits-vorhandenes-feed-asset-keine-neugenerierung",
  };
}

const manifest = {
  stand: new Date().toISOString(),
  modus: "lokal-ohne-provider",
  providerKostenUsd: 0,
  bildgenerierungKostenUsd: 0,
  tage: {},
};

try {
  for (const [datum, eintrag] of Object.entries(spec.tage || {})) {
    const tagPfad = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
    const tag = JSON.parse(fs.readFileSync(tagPfad, "utf8"));
    const m = { stories: [], teasers: [], carouselSlides: [], reelCovers: [] };

    for (const slot of eintrag.teasers || []) {
      const plan = (tag.plan?.stories || []).find((x) => x.slot === slot);
      if (!plan?.beitragSlot) throw new Error(`${datum} ${slot}: Teaser-Plan oder beitragSlot fehlt`);
      const beitrag = tag.inhalte?.[plan.beitragSlot];
      if (!beitrag) throw new Error(`${datum} ${slot}: Feed-Bezug ${plan.beitragSlot} fehlt`);
      const story = teaserFuer(slot, beitrag, plan.beitragSlot);
      tag.inhalte[slot] = story;
      const ziel = path.join(hosting.dir, "vorproduktion", datum, "fertig", "stories", `${slot}-teaser.jpg`);
      await storyRendernLokal(story, ziel);
      m.teasers.push(path.relative(hosting.dir, ziel));
    }

    for (const [slot, seiten] of Object.entries(eintrag.carouselSlides || {})) {
      const beitrag = structuredClone(tag.inhalte?.[slot]);
      if (!Array.isArray(beitrag?.folien)) throw new Error(`${datum} ${slot}: Karussell fehlt`);
      const tmpKarussell = path.join(temp, "carousel", datum, slot);
      fs.mkdirSync(tmpKarussell, { recursive: true });
      const gerendert = await beitragRendern(beitrag, tmpKarussell, { variante: 0 });
      for (const seite of seiten || []) {
        const index = Number(seite);
        if (!Number.isInteger(index) || index < 1 || index > beitrag.folien.length) {
          throw new Error(`${datum} ${slot}: ungueltige Foliennummer ${seite}`);
        }
        const slug = beitrag.slug || `${datum}-${slot}`;
        const ziel = path.join(hosting.dir, "vorproduktion", datum, "fertig", slot, `${slug}-${String(index).padStart(2, "0")}.jpg`);
        fs.mkdirSync(path.dirname(ziel), { recursive: true });
        fs.copyFileSync(gerendert[index - 1], ziel);
        m.carouselSlides.push(path.relative(hosting.dir, ziel));
      }
    }

    for (const slot of eintrag.stories || []) {
      const story = structuredClone(tag.inhalte?.[slot]);
      if (!story) throw new Error(`${datum} ${slot}: Story fehlt`);
      const ziel = path.join(hosting.dir, "vorproduktion", datum, "fertig", "stories", `${slot}-${story.art}.jpg`);
      await storyRendernLokal(story, ziel);
      m.stories.push(path.relative(hosting.dir, ziel));
    }

    for (const slot of eintrag.reelCovers || []) {
      const reel = structuredClone(tag.inhalte?.[slot]);
      if (!reel?.szenen) throw new Error(`${datum} ${slot}: Reel fehlt`);
      const slug = reel.slug || `${datum}-${slot}`;
      const alt = path.join(hosting.dir, "vorproduktion", datum, "fertig", slot, `${slug}-cover.jpg`);
      if (!fs.existsSync(alt)) throw new Error(`${datum} ${slot}: bestehendes Cover fehlt`);

      /* Reparaturen duerfen niemals auf bereits reparierten JPEGs stapeln:
         Dadurch wuerden alte Badge-/Footer-Artefakte von Lauf zu Lauf
         mitgeschleppt. Wenn der Trigger den urspruenglichen Git-Blob nennt,
         holen wir exakt dieses bereits bezahlte Ausgangscover aus der
         Asset-Historie. Das ist rein lokales Git, ohne Providerkontakt. */
      let quelle = alt;
      const quellBlob = String(eintrag.sourceCoverBlobs?.[slot] || "").trim();
      if (quellBlob) {
        if (!/^[a-f0-9]{40}$/i.test(quellBlob)) {
          throw new Error(`${datum} ${slot}: ungueltiger sourceCoverBlob`);
        }
        const original = path.join(temp, `${datum}-${slot}-original.jpg`);
        let bytes;
        try {
          bytes = execFileSync("git", ["cat-file", "blob", quellBlob], {
            cwd: hosting.dir,
            encoding: null,
            maxBuffer: 8 * 1024 * 1024,
          });
        } catch (e) {
          throw new Error(`${datum} ${slot}: Original-Blob ${quellBlob} nicht lokal verfuegbar: ${e.message}`);
        }
        if (!bytes?.length || bytes[0] !== 0xff || bytes[1] !== 0xd8) {
          throw new Error(`${datum} ${slot}: Original-Blob ist kein plausibles JPEG`);
        }
        fs.writeFileSync(original, bytes);
        quelle = original;
      }

      const freigestellt = path.join(temp, `${datum}-${slot}-foreground.png`);
      const lokalArgs = [
        path.resolve("bin/cover-foreground-local.py"),
        "--input", quelle,
        "--output", freigestellt,
        "--crop-y", "980",
      ];
      execFileSync("python3", lokalArgs, { stdio: "inherit" });

      const puffer = fs.readFileSync(freigestellt);
      const daten = coverDatenLokal(reel);
      daten.bild = `data:image/png;base64,${puffer.toString("base64")}`;
      daten.bildFrei = true;
      daten.bildTyp = "charakter";
      daten.bildBreite = 1080;
      daten.bildHoehe = 940;
      daten.coverHinweisPlan = null;

      await coverRendernLokal(daten, alt);
      m.reelCovers.push(path.relative(hosting.dir, alt));
    }

    tag.renderVorschau = {
      ...(tag.renderVorschau || {}),
      letzteKostenloseReparatur: {
        stand: new Date().toISOString(),
        stories: eintrag.stories || [],
        teasers: eintrag.teasers || [],
        carouselSlides: eintrag.carouselSlides || {},
        reelCovers: eintrag.reelCovers || [],
        providerKostenUsd: 0,
        bildgenerierungKostenUsd: 0,
      },
      freigabeBetreiber: false,
    };
    fs.writeFileSync(tagPfad, JSON.stringify(tag, null, 2) + "\n");
    manifest.tage[datum] = m;
  }

  fs.writeFileSync(
    path.join(hosting.dir, "vorproduktion", "render-reparatur-manifest.json"),
    JSON.stringify(manifest, null, 2) + "\n",
  );
  hosting.commit("Repariere Vorproduktions-Render lokal ohne Provider");
  await hosting.push();
} finally {
  if (browser) await browser.close().catch(() => {});
  await renderBrowserBeenden().catch(() => {});
  fs.rmSync(temp, { recursive: true, force: true });
}

console.log(JSON.stringify(manifest, null, 2));
