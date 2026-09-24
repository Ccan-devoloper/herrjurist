#!/usr/bin/env node
/**
 * Wendet manuell hochgeladene Vorproduktions-Cover providerfrei an.
 *
 * - Quelle: instagram-assets/vorproduktion/coverbilder/*.png
 * - Opaque PNGs werden als fertige Cover lokal ins jeweilige Zielformat gesetzt.
 * - PNGs mit echter Transparenz werden als Freisteller in die vorhandene
 *   Herr-Jurist-Covervorlage eingesetzt und mit Chromium neu gerendert.
 * - Es werden keinerlei Text-, Bild-, QA- oder Voice-Provider aufgerufen.
 */
import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";

import { Hosting } from "../src/hosting.mjs";
import { beitragRendern, browserBeenden, coverRendern } from "../src/render.mjs";
import { coverDaten } from "../src/reel.mjs";

const ZUORDNUNG = new Map([
  ["chatgpt image 24. sept. 2026, 03_59_53.png", ["2026-09-24", "b3"]],
  ["drittwirkung-action-cover.png", ["2026-09-24", "b1"]],
  ["vormerkung-action-cover.png", ["2026-09-24", "b2"]],
  ["lebensgefährlich und tötungsvorsatz.png", ["2026-09-25", "b2"]],
  ["verfassungsbeschwerde_grundrecht verletzt.png", ["2026-09-25", "b3"]],
  ["verhaeltnismaessigkeit-cover (1).png", ["2026-09-26", "b2"]],
  ["vor der klausur noch stoff nachholen.png", ["2026-09-26", "b3"]],
  ["wochenrückblick.png", ["2026-09-27", "b1"]],
  ["zwangsvollstreckung-cover.png", ["2026-09-27", "b2"]],
  ["§ 224_gefährlich_reicht_nicht.png", ["2026-09-27", "b3"]],
  ["gestohlen und gutgläubig gekauft.png", ["2026-09-28", "b1"]],
  ["fahrlässigkeitsdelik.png", ["2026-09-28", "b2"]],
  ["va erledigt.png", ["2026-09-28", "b3"]],
].map(([name, ziel]) => [name.toLowerCase(), ziel]));

/* Gezielte Layoutkorrekturen für manuell gelieferte Charakter-Szenen. Die
   Werte steuern nur lokale Geometrie; kein Provider wird aufgerufen. */
const RENDER_PROFIL = new Map([
  /* Problemcover bekommen keine Sticker-Skalierung mehr, sondern eine
     explizite Edge-to-Edge-Breite mit leichtem Beschnitt ("bleed"). So
     spannt das freigestellte Motiv die untere Coverbuehne wirklich von
     Kante zu Kante auf. */
  ["2026-09-25/b2", { width: 1160, x: 0.50, edge: true }],
  ["2026-09-25/b3", { width: 1160, x: 0.50, edge: true }],
  ["2026-09-26/b3", { width: 1120, x: 0.50, edge: true }],
  ["2026-09-28/b3", { width: 1140, x: 0.51, edge: true }],
]);

function triggerSlots() {
  const env = String(process.env.IG_COVER_SLOTS || "").trim();
  if (env) return new Set(env.split(",").map((x) => x.trim()).filter(Boolean));
  try {
    const trigger = fs.readFileSync(path.resolve("vorproduktion/coverbilder.trigger"), "utf8");
    const zeilen = trigger.split(/\r?\n/).filter((x) => /^slots=/.test(x.trim()));
    if (!zeilen.length) return null;
    return new Set(zeilen.at(-1).replace(/^slots=/, "").split(",").map((x) => x.trim()).filter(Boolean));
  } catch {
    return null;
  }
}

function normalisieren(s) {
  return String(s || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/§/g, " paragraph ")
    .replace(/[^a-z0-9]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function tokens(s) {
  return new Set(normalisieren(s).split(" ").filter((x) => x.length >= 3));
}

function aehnlichkeit(a, b) {
  const A = tokens(a), B = tokens(b);
  if (!A.size || !B.size) return 0;
  let gemeinsam = 0;
  for (const x of A) if (B.has(x)) gemeinsam++;
  return (2 * gemeinsam) / (A.size + B.size);
}

function pythonJson(code, args = []) {
  const out = execFileSync("python3", ["-c", code, ...args], { encoding: "utf8" });
  return JSON.parse(out);
}

function bildMeta(datei) {
  return pythonJson(
    `from PIL import Image
import json,sys
p=sys.argv[1]
im=Image.open(p).convert("RGBA")
a=im.getchannel("A")
hist=a.histogram()
n=max(1, im.width*im.height)
trans=sum(hist[:250])/n
bbox=a.getbbox()
print(json.dumps({
 "width":im.width,
 "height":im.height,
 "alphaMin":a.getextrema()[0],
 "alphaMax":a.getextrema()[1],
 "transparentFraction":trans,
 "alphaBBox":bbox
}))`,
    [datei],
  );
}

function freistellerZuschneiden(quelle, ziel, edge = false) {
  return pythonJson(
    `from PIL import Image
import json,sys,os
src,dst=sys.argv[1],sys.argv[2]
edge=sys.argv[3]=="1"
im=Image.open(src).convert("RGBA")
a=im.getchannel("A")
bbox=a.getbbox()
if not bbox:
    raise SystemExit("Freisteller ist vollständig transparent")
l,t,r,b=bbox
# Normale Freisteller behalten etwas Luft. Edge-to-Edge-Motive werden dagegen
# exakt auf ihre Alpha-Grenzen zugeschnitten; sonst erzeugt der Renderer
# erneut einen unsichtbaren Rand um das Motiv.
pad=0 if edge else max(8, round(max(r-l,b-t)*0.025))
l=max(0,l-pad); t=max(0,t-pad); r=min(im.width,r+pad); b=min(im.height,b+pad)
out=im.crop((l,t,r,b))
os.makedirs(os.path.dirname(dst),exist_ok=True)
out.save(dst,"PNG",optimize=True)
print(json.dumps({"width":out.width,"height":out.height,"crop":[l,t,r,b],"edgeCrop":edge}))`,
    [quelle, ziel, edge ? "1" : "0"],
  );
}

function vollcoverZuJpeg(quelle, ziel, breite, hoehe) {
  return pythonJson(
    `from PIL import Image,ImageOps,ImageFilter
import json,sys,os
src,dst=sys.argv[1],sys.argv[2]
tw,th=int(sys.argv[3]),int(sys.argv[4])
im=Image.open(src).convert("RGB")
ratio=im.width/im.height
target=tw/th
if abs(ratio-target)/target <= 0.018:
    out=im.resize((tw,th),Image.Resampling.LANCZOS)
    modus="resize"
else:
    bg=ImageOps.fit(im,(tw,th),method=Image.Resampling.LANCZOS,centering=(0.5,0.5)).filter(ImageFilter.GaussianBlur(28))
    fg=ImageOps.contain(im,(tw,th),method=Image.Resampling.LANCZOS)
    x=(tw-fg.width)//2; y=(th-fg.height)//2
    bg.paste(fg,(x,y))
    out=bg
    modus="contain-blur"
os.makedirs(os.path.dirname(dst),exist_ok=True)
out.save(dst,"JPEG",quality=95,optimize=True,progressive=True)
print(json.dumps({"width":tw,"height":th,"mode":modus,"sourceWidth":im.width,"sourceHeight":im.height}))`,
    [quelle, ziel, String(breite), String(hoehe)],
  );
}

function ocr(datei) {
  try {
    return execFileSync(
      "tesseract",
      [datei, "stdout", "-l", "deu+eng", "--psm", "6"],
      { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] },
    ).trim();
  } catch {
    return "";
  }
}

function sha256(datei) {
  return crypto.createHash("sha256").update(fs.readFileSync(datei)).digest("hex");
}

function titelFuer(tag, slot) {
  const plan = (tag.plan?.beitraege || tag.beitraege || []).find((x) => x.slot === slot);
  const inhalt = tag.inhalte?.[slot];
  const titel = inhalt?.folien?.find((x) => x.art === "titel")?.titel
    || inhalt?.folien?.[0]?.titel
    || inhalt?.szenen?.[0]?.titel
    || inhalt?.titel
    || "";
  return [titel, plan?.themaTitel || "", inhalt?.kurztitel || "", inhalt?.coverText || ""]
    .filter(Boolean)
    .join(" ");
}

function zielPfad(basis, datum, slot, inhalt) {
  const dir = path.join(basis, "vorproduktion", datum, "fertig", slot);
  if (Array.isArray(inhalt?.szenen)) return path.join(dir, `${datum}-${slot}-cover.jpg`);
  return path.join(dir, `${datum}-${slot}-01.jpg`);
}

function motivSetzen(obj, dataUrl, meta, profil = null) {
  obj.bild = dataUrl;
  obj.bildQuelle = null;
  obj.bildFrei = true;
  obj.bildBreite = meta.width;
  obj.bildHoehe = meta.height;
  obj.bildTyp = "charakter";
  obj.coverBildAuslassen = false;
  if (profil?.scale != null) obj.coverBildScale = profil.scale;
  if (profil?.width != null) obj.coverBildBreite = profil.width;
  if (profil?.x != null) obj.coverBildX = profil.x;
  if (profil?.edge === true) obj.coverBildEdgeToEdge = true;
  delete obj.coverHinweisPlan;
}

const hosting = new Hosting({ pushen: true }).vorbereiten();
const coverDir = path.join(hosting.dir, "vorproduktion", "coverbilder");
if (!fs.existsSync(coverDir)) throw new Error(`Coverbilder-Ordner fehlt: ${coverDir}`);

const slotsFilter = triggerSlots();
const pngs = fs.readdirSync(coverDir)
  .filter((x) => /\.png$/i.test(x))
  .filter((name) => {
    if (!slotsFilter?.size) return true;
    const ziel = ZUORDNUNG.get(name.toLowerCase());
    return ziel ? slotsFilter.has(`${ziel[0]}/${ziel[1]}`) : false;
  })
  .sort((a, b) => a.localeCompare(b, "de"));

if (!pngs.length) throw new Error("Keine passenden PNG-Coverbilder gefunden.");
if (slotsFilter?.size) console.log(`Gezielter Coverlauf: ${[...slotsFilter].join(", ")}`);

const tage = new Map();
for (const datum of ["2026-09-24", "2026-09-25", "2026-09-26", "2026-09-27", "2026-09-28"]) {
  const p = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
  tage.set(datum, JSON.parse(fs.readFileSync(p, "utf8")));
}

const belegt = new Set([...ZUORDNUNG.values()].map(([d, s]) => `${d}/${s}`));
const kandidaten = [];
for (const [datum, tag] of tage) {
  for (const slot of ["b1", "b2", "b3"]) {
    const key = `${datum}/${slot}`;
    if (belegt.has(key)) continue;
    kandidaten.push({ datum, slot, text: titelFuer(tag, slot) });
  }
}

const zuordnung = new Map(ZUORDNUNG);
for (const name of pngs) {
  if (zuordnung.has(name.toLowerCase())) continue;
  const datei = path.join(coverDir, name);
  const erkannt = ocr(datei);
  const quelle = `${name} ${erkannt}`;
  const rang = kandidaten
    .map((k) => ({ ...k, score: aehnlichkeit(quelle, k.text) }))
    .sort((a, b) => b.score - a.score);
  const bester = rang[0];
  if (!bester || bester.score < 0.18) {
    throw new Error(`Keine sichere Zuordnung für „${name}“. OCR: ${erkannt || "(leer)"}`);
  }
  zuordnung.set(name.toLowerCase(), [bester.datum, bester.slot]);
  belegt.add(`${bester.datum}/${bester.slot}`);
  const i = kandidaten.findIndex((x) => x.datum === bester.datum && x.slot === bester.slot);
  if (i >= 0) kandidaten.splice(i, 1);
  console.log(`OCR-Zuordnung: ${name} -> ${bester.datum} ${bester.slot} · Score ${bester.score.toFixed(2)} · „${erkannt.replace(/\s+/g, " ").slice(0, 160)}“`);
}

const temp = fs.mkdtempSync(path.join(os.tmpdir(), "herrjurist-coverbilder-"));
let bisher = null;
try {
  bisher = JSON.parse(fs.readFileSync(path.join(hosting.dir, "vorproduktion", "coverbilder-anwendung.json"), "utf8"));
} catch { /* erster Lauf */ }

const manifest = {
  version: 2,
  angewandtAm: new Date().toISOString(),
  modus: "providerfrei-hochgeladene-coverbilder",
  providerAufrufe: 0,
  providerKostenUsd: 0,
  eintraege: Array.isArray(bisher?.eintraege) ? structuredClone(bisher.eintraege) : [],
};

try {
  for (const name of pngs) {
    const key = name.toLowerCase();
    const ziel = zuordnung.get(key);
    if (!ziel) throw new Error(`Keine Zuordnung für ${name}`);
    const [datum, slot] = ziel;
    const profil = RENDER_PROFIL.get(`${datum}/${slot}`) || null;
    const tag = tage.get(datum);
    const inhalt = structuredClone(tag.inhalte?.[slot]);
    if (!inhalt) throw new Error(`${datum} ${slot}: Inhalt fehlt`);

    const quelle = path.join(coverDir, name);
    const meta = bildMeta(quelle);
    const freigestellt = meta.alphaMin < 250 && meta.transparentFraction > 0.005;
    const target = zielPfad(hosting.dir, datum, slot, inhalt);
    fs.mkdirSync(path.dirname(target), { recursive: true });

    let renderMeta;
    if (freigestellt) {
      const zugeschnitten = path.join(temp, `${datum}-${slot}-motiv.png`);
      const crop = freistellerZuschneiden(quelle, zugeschnitten, profil?.edge === true);
      const dataUrl = `data:image/png;base64,${fs.readFileSync(zugeschnitten).toString("base64")}`;

      if (Array.isArray(inhalt.folien)) {
        delete inhalt.coverFinalUrl;
        delete inhalt.coverFinalSha256;
        const titel = inhalt.folien.find((x) => x.art === "titel") || inhalt.folien[0];
        motivSetzen(titel, dataUrl, crop, profil);
        const dir = path.join(temp, datum, slot);
        const gerendert = await beitragRendern(inhalt, dir);
        fs.copyFileSync(gerendert[0], target);
        renderMeta = { mode: "freisteller-covervorlage", profil, ...crop };
      } else if (Array.isArray(inhalt.szenen)) {
        delete inhalt.coverFinalUrl;
        motivSetzen(inhalt, dataUrl, crop, profil);
        const daten = coverDaten(inhalt, { gesamt: 60 });
        await coverRendern(daten, target);
        renderMeta = { mode: "freisteller-reel-covervorlage", profil, safeArea: { top: 285, bottom: 1635 }, ...crop };
      } else {
        throw new Error(`${datum} ${slot}: unbekanntes Inhaltsformat`);
      }
    } else {
      const reel = Array.isArray(inhalt.szenen);
      renderMeta = vollcoverZuJpeg(quelle, target, 1080, reel ? 1920 : 1350);
    }

    const entry = {
      quelle: `vorproduktion/coverbilder/${name}`,
      quelleSha256: sha256(quelle),
      datum,
      slot,
      titel: titelFuer(tag, slot),
      freigestellt,
      quelleMeta: meta,
      render: renderMeta,
      ziel: path.relative(hosting.dir, target).split(path.sep).join("/"),
      zielSha256: sha256(target),
      providerKostenUsd: 0,
    };
    const alt = manifest.eintraege.findIndex((x) => x.datum === datum && x.slot === slot);
    if (alt >= 0) manifest.eintraege.splice(alt, 1, entry);
    else manifest.eintraege.push(entry);
    manifest.eintraege.sort((a, b) => `${a.datum}/${a.slot}`.localeCompare(`${b.datum}/${b.slot}`));
    console.log(`✓ ${name} -> ${datum} ${slot} · ${freigestellt ? "Freisteller neu gerendert" : "Vollcover lokal angepasst"}`);

    tag.renderVorschau = {
      ...(tag.renderVorschau || {}),
      coverbilderAngewandt: {
        ...(tag.renderVorschau?.coverbilderAngewandt || {}),
        stand: manifest.angewandtAm,
        providerKostenUsd: 0,
        slots: [
          ...new Set([
            ...(tag.renderVorschau?.coverbilderAngewandt?.slots || []),
            slot,
          ]),
        ].sort(),
      },
    };
  }
} finally {
  await browserBeenden().catch(() => {});
}

for (const [datum, tag] of tage) {
  fs.writeFileSync(
    path.join(hosting.dir, "vorproduktion", `${datum}.json`),
    JSON.stringify(tag, null, 2) + "\n",
  );
}

fs.writeFileSync(
  path.join(hosting.dir, "vorproduktion", "coverbilder-anwendung.json"),
  JSON.stringify(manifest, null, 2) + "\n",
);

const committed = hosting.commit(`Wende ${manifest.eintraege.length} hochgeladene Vorproduktions-Cover providerfrei an`);
if (!committed) throw new Error("Keine Änderungen am Asset-Zweig erzeugt.");
await hosting.push();

console.log(JSON.stringify({
  ok: true,
  anzahl: manifest.eintraege.length,
  providerAufrufe: 0,
  providerKostenUsd: 0,
  ziele: manifest.eintraege.map((x) => x.ziel),
}, null, 2));
