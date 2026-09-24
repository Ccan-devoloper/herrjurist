#!/usr/bin/env node
/**
 * Erzeugt Layout-Karten (*.jpg.layout.json) fuer BEREITS gerenderte
 * Vorproduktions-Folien und Stories im Asset-Zweig.
 *
 * Der Dashboard-Editor macht damit gebackene Texte direkt anklickbar.
 * Vorgehen je Datei: identisch neu rendern (0 Provideraufrufe, reine
 * Chromium-Typografie), das Ergebnis pixelweise mit der gespeicherten
 * Folie vergleichen und die Layout-Karte NUR uebernehmen, wenn beide
 * uebereinstimmen. Cover mit Motiv/hochgeladenem Bild und anders
 * reparierte Folien fallen so automatisch heraus - lieber keine Karte
 * als eine falsche. Die gespeicherten JPEGs werden nie angefasst.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import crypto from "node:crypto";

import { Hosting } from "../src/hosting.mjs";
import { htmlZuJpeg, kontext, browserStarten, browserBeenden, carouselBildregeln } from "../src/render.mjs";
import { folieHtml, storyHtml, MASSE } from "../src/vorlagen.mjs";

const args = process.argv.slice(2);
const explizit = args.filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x));
/* Ab dieser mittleren Kanalabweichung (0-255) gilt die Folie als anders
   gerendert und bekommt keine Karte. Antialiasing liegt weit darunter,
   ein Motiv- oder Coverbild weit darueber. */
const SCHWELLE = Number(process.env.IG_LAYOUT_DIFF_SCHWELLE || 8);

const hosting = new Hosting({ pushen: process.env.IG_NO_PUSH !== "true" }).vorbereiten();
const temp = fs.mkdtempSync(path.join(os.tmpdir(), "herrjurist-editor-layouts-"));
const sha256 = (p) => crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");

const vorproduktionsDir = path.join(hosting.dir, "vorproduktion");
const tage = explizit.length ? explizit : fs.readdirSync(vorproduktionsDir)
  .filter((n) => /^\d{4}-\d{2}-\d{2}\.json$/.test(n))
  .map((n) => n.slice(0, 10))
  .sort();

let diffPage = null;
async function bildAbstand(pfadA, pfadB) {
  const b = await browserStarten();
  if (!diffPage) diffPage = await b.newPage();
  const lade = (p) => `data:image/jpeg;base64,${fs.readFileSync(p).toString("base64")}`;
  return diffPage.evaluate(async ([a, bb]) => {
    const bild = (u) => new Promise((res, rej) => { const i = new Image(); i.onload = () => res(i); i.onerror = rej; i.src = u; });
    const [ia, ib] = await Promise.all([bild(a), bild(bb)]);
    const W = 90;
    const H = Math.max(1, Math.round(W * ia.height / ia.width));
    const c = document.createElement("canvas");
    c.width = W; c.height = H;
    const ctx = c.getContext("2d", { willReadFrequently: true });
    ctx.drawImage(ia, 0, 0, W, H);
    const da = ctx.getImageData(0, 0, W, H).data;
    ctx.clearRect(0, 0, W, H);
    ctx.drawImage(ib, 0, 0, W, H);
    const db = ctx.getImageData(0, 0, W, H).data;
    let s = 0;
    for (let i = 0; i < da.length; i += 4) {
      s += Math.abs(da[i] - db[i]) + Math.abs(da[i + 1] - db[i + 1]) + Math.abs(da[i + 2] - db[i + 2]);
    }
    return s / (da.length / 4) / 3;
  }, [lade(pfadA), lade(pfadB)]);
}

let geschrieben = 0;
let uebersprungen = 0;
let gefehlt = 0;
const protokoll = [];

/* Frisch rendern, vergleichen, Karte neben die gespeicherte Datei legen. */
async function karteFuer(html, masse, gespeichert, kennung) {
  if (!fs.existsSync(gespeichert)) { gefehlt++; return; }
  const ziel = path.join(temp, `${crypto.randomBytes(6).toString("hex")}.jpg`);
  try {
    await htmlZuJpeg(html, masse, ziel);
  } catch (e) {
    uebersprungen++;
    protokoll.push(`${kennung}: Render-Fehler (${String(e?.message || e).slice(0, 120)})`);
    return;
  }
  const layoutPfad = `${ziel}.layout.json`;
  if (!fs.existsSync(layoutPfad)) { uebersprungen++; protokoll.push(`${kennung}: keine Layoutdaten`); return; }
  const abstand = await bildAbstand(ziel, gespeichert);
  if (!(abstand <= SCHWELLE)) {
    uebersprungen++;
    protokoll.push(`${kennung}: Abweichung ${abstand.toFixed(1)} > ${SCHWELLE} (Motiv-/Coverfolie oder anders repariert)`);
    return;
  }
  const layout = JSON.parse(fs.readFileSync(layoutPfad, "utf8"));
  layout.quellSha256 = sha256(gespeichert);
  layout.abstand = Math.round(abstand * 100) / 100;
  fs.writeFileSync(`${gespeichert}.layout.json`, JSON.stringify(layout) + "\n");
  geschrieben++;
}

try {
  for (const datum of tage) {
    const quelle = path.join(vorproduktionsDir, `${datum}.json`);
    if (!fs.existsSync(quelle)) continue;
    const tag = JSON.parse(fs.readFileSync(quelle, "utf8"));
    const fertig = path.join(vorproduktionsDir, datum, "fertig");
    if (!fs.existsSync(fertig)) continue;

    for (const [slot, roh] of Object.entries(tag.inhalte || {})) {
      if (Array.isArray(roh?.folien)) {
        const inhalt = structuredClone(roh);
        carouselBildregeln(inhalt);
        /* Gleiche Kontextwahl wie der Vorproduktions-Render (variante 0). */
        const ctx = kontext({ fach: inhalt.fach, klausur: inhalt.klausur, fachLabel: inhalt.fachLabel, variante: 0 });
        const n = inhalt.folien.length;
        for (let i = 0; i < n; i++) {
          const name = `${inhalt.slug || "beitrag"}-${String(i + 1).padStart(2, "0")}.jpg`;
          await karteFuer(
            folieHtml(inhalt.folien[i], ctx, i + 1, n),
            MASSE.beitrag,
            path.join(fertig, slot, name),
            `${datum}/${slot}/${name}`,
          );
        }
      } else if (/^s\d+$/.test(slot) && roh?.art) {
        const story = structuredClone(roh);
        const ctx = kontext({ fach: story.fach, klausur: story.klausur, fachLabel: story.fachLabel, variante: 0 });
        const name = `${slot}-${story.art}.jpg`;
        await karteFuer(storyHtml(story, ctx), MASSE.story, path.join(fertig, "stories", name), `${datum}/stories/${name}`);
      }
    }
  }
} finally {
  await browserBeenden().catch(() => {});
  fs.rmSync(temp, { recursive: true, force: true });
}

if (geschrieben) {
  hosting.commit(`Editor-Layouts fuer ${tage.join(" + ")}`);
  await hosting.push();
}

console.log(JSON.stringify({ ok: true, tage, geschrieben, uebersprungen, gefehlt, schwelle: SCHWELLE, protokoll }, null, 2));
