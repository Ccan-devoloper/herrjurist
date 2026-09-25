#!/usr/bin/env node
/**
 * Vollstaendige Review-Vorproduktion OHNE kostenpflichtige Provider.
 *
 * - keine Autor-/Faktencheck-Aufrufe
 * - keine OpenAI-/Anthropic-/ElevenLabs-Aufrufe
 * - keine Cover-/Charakterbild-Generierung
 * - Reels sprechen ausschliesslich mit Piper offline
 * - alle Karussellseiten und alle 9 Stories werden lokal mit Chromium gerendert
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

for (const key of ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY", "PEXELS_API_KEY"]) {
  if (String(process.env[key] || "").trim()) {
    throw new Error(`Kostenfreier Vorproduktionslauf verweigert Provider-Secret: ${key}`);
  }
}
if (String(process.env.IG_STIMME || "").toLowerCase() !== "piper") {
  throw new Error("Kostenfreier Vorproduktionslauf verlangt IG_STIMME=piper.");
}
if (String(process.env.IG_BILD_KI || "").toLowerCase() !== "false") {
  throw new Error("Kostenfreier Vorproduktionslauf verlangt IG_BILD_KI=false.");
}
if (String(process.env.IG_CHARAKTERE || "").toLowerCase() !== "false") {
  throw new Error("Kostenfreier Vorproduktionslauf verlangt IG_CHARAKTERE=false.");
}

/* Derselbe Workflow kann fuer einen gezielten Reel-Patch genutzt werden.
   Die Triggerdatei entscheidet, bevor die normale Mehrtages-Review startet. */
const overlayTriggerPfad = new URL("../vorproduktion/review-render-only.trigger", import.meta.url);
if (fs.existsSync(overlayTriggerPfad)) {
  const trigger = JSON.parse(fs.readFileSync(overlayTriggerPfad, "utf8"));
  if (trigger.modus === "reel-overlay-patch") {
    const { reelOverlayPatchen } = await import("./vorproduktion-reel-overlay-patch.mjs");
    const tage = Array.isArray(trigger.tage) ? trigger.tage : [];
    const slots = Array.isArray(trigger.slots) && trigger.slots.length ? trigger.slots : ["b3"];
    const manifest = await reelOverlayPatchen({ tage, slots });
    console.log(JSON.stringify({ ok: true, ...manifest }, null, 2));
    process.exit(0);
  }
  if (trigger.modus === "cover-only-patch") {
    const { coverOnlyPatchen } = await import("./vorproduktion-cover-only-patch.mjs");
    const tage = Array.isArray(trigger.tage) ? trigger.tage : [];
    const slots = Array.isArray(trigger.slots) && trigger.slots.length ? trigger.slots : ["b1", "b2", "b3"];
    const manifest = await coverOnlyPatchen({ tage, slots });
    console.log(JSON.stringify({ ok: true, ...manifest }, null, 2));
    process.exit(0);
  }
}

const { Hosting } = await import("../src/hosting.mjs");
const { beitragRendern, storyRendern, browserBeenden } = await import("../src/render.mjs");
const { reelBauen } = await import("../src/reel.mjs");
const { ICONS } = await import("../src/stile.mjs");
const { ZUORDNUNG } = await import("../src/icons.mjs");
const { quizPruefen } = await import("./vorproduktion-quiz-regel.mjs");

const tage = process.argv.slice(2).filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x));
if (!tage.length) throw new Error("Mindestens ein Datum YYYY-MM-DD ist erforderlich.");

const hosting = new Hosting({ pushen: true }).vorbereiten();
const temp = fs.mkdtempSync(path.join(os.tmpdir(), "herrjurist-ohne-coverbilder-"));
const manifest = {
  version: 1,
  erzeugtAm: new Date().toISOString(),
  modus: "lokal-ohne-provider-und-ohne-coverbilder",
  providerKostenUsd: 0,
  textProviderKostenUsd: 0,
  faktencheckProviderKostenUsd: 0,
  bildgenerierungKostenUsd: 0,
  coverbilder: false,
  tage: [],
};

function fachDaten(beitrag = {}) {
  return {
    fach: beitrag.fach || "methodik",
    klausur: beitrag.klausur ?? 0,
    fachLabel: beitrag.fachLabel || "Examenswissen",
  };
}

function titelVon(beitrag = {}) {
  return beitrag.kurztitel
    || beitrag.folien?.find((f) => f.art === "titel")?.titel
    || beitrag.szenen?.[0]?.titel
    || "Neuer Beitrag";
}

function teaserFuer(slot, beitrag, beitragSlot) {
  return {
    slot,
    art: "teaser",
    ...fachDaten(beitrag),
    titel: titelVon(beitrag),
    text: "Der vollständige Beitrag ist jetzt im Feed.",
    pille: "Jetzt im Feed",
    beitragSlot,
    abgeleitet: true,
    freigabeBetreiber: false,
    vorproduktionStatus: "review",
    textProviderKostenUsd: 0,
    faktencheckProviderKostenUsd: 0,
    bildStatus: "bewusst-ausgelassen",
  };
}

function dateiRelativ(pfad) {
  return path.relative(hosting.dir, pfad).split(path.sep).join("/");
}

function expliziteIconKeysPruefen(wert, pfad = "inhalte") {
  if (!wert || typeof wert !== "object") return;
  if (typeof wert.icon === "string" && wert.icon.trim()) {
    const key = wert.icon.trim();
    if (!(key in ICONS) && !(key in ZUORDNUNG)) {
      throw new Error(`Unbekannter Icon-Key vor Renderstart: ${key} (${pfad}.icon)`);
    }
  }
  if (Array.isArray(wert.icons)) {
    if (Array.isArray(wert.punkte) && wert.icons.length !== wert.punkte.length) {
      throw new Error(`CTA-Icon-Anzahl passt nicht zu CTA-Punkten (${pfad})`);
    }
    for (const keyRaw of wert.icons) {
      const key = String(keyRaw || "").trim();
      if (!key || (!(key in ICONS) && !(key in ZUORDNUNG))) {
        throw new Error(`Unbekannter CTA-Icon-Key vor Renderstart: ${key || "<leer>"} (${pfad}.icons)`);
      }
    }
  }
  for (const [key, kind] of Object.entries(wert)) {
    if (key === "icon" || key === "icons") continue;
    if (Array.isArray(kind)) kind.forEach((x, i) => expliziteIconKeysPruefen(x, `${pfad}.${key}[${i}]`));
    else if (kind && typeof kind === "object") expliziteIconKeysPruefen(kind, `${pfad}.${key}`);
  }
}

for (const datum of tage) {
  const tagPfad = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
  if (!fs.existsSync(tagPfad)) throw new Error(`Vorproduktion fehlt: ${datum}`);
  const tag = JSON.parse(fs.readFileSync(tagPfad, "utf8"));
  expliziteIconKeysPruefen(tag.inhalte, `${datum}.inhalte`);
  quizPruefen(tag, datum);
}

try {
  for (const datum of tage) {
    const tagPfad = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
    if (!fs.existsSync(tagPfad)) throw new Error(`Vorproduktion fehlt: ${datum}`);
    const tag = JSON.parse(fs.readFileSync(tagPfad, "utf8"));
    const out = path.join(temp, datum);
    fs.mkdirSync(out, { recursive: true });
    const mTag = { datum, feed: [], stories: [] };

    for (const slot of ["b1", "b2", "b3"]) {
      const beitrag = structuredClone(tag.inhalte?.[slot]);
      if (!beitrag) throw new Error(`${datum} ${slot}: Beitrag fehlt`);
      beitrag.coverBildAuslassen = true;
      beitrag.bild = null;
      beitrag.bildQuelle = null;
      beitrag.bildCharaktere = [];
      if (Array.isArray(beitrag.folien)) {
        const titel = beitrag.folien.find((f) => f.art === "titel") || beitrag.folien[0];
        titel.coverBildAuslassen = true;
        titel.bild = null;
        titel.bildQuelle = null;
        titel.bildCharaktere = [];
        const ziel = path.join(out, slot);
        fs.mkdirSync(ziel, { recursive: true });
        const dateien = await beitragRendern(beitrag, ziel, { variante: 0 });
        mTag.feed.push({
          slot,
          format: beitrag.format,
          titel: titelVon(beitrag),
          coverBild: false,
          dateien: dateien.map((p) => path.basename(p)),
        });
      } else if (Array.isArray(beitrag.szenen)) {
        const ziel = path.join(out, slot);
        fs.mkdirSync(ziel, { recursive: true });
        const reel = await reelBauen(beitrag, ziel, {
          datum,
          layout: "erklaer",
          clip: null,
          framesBehalten: false,
        });
        mTag.feed.push({
          slot,
          format: "reel",
          titel: titelVon(beitrag),
          coverBild: false,
          dateien: [path.basename(reel.cover), path.basename(reel.video)],
          reel: {
            dauer: reel.dauer,
            stimme: reel.anbieter,
            layout: reel.layout,
            szenen: reel.szenen,
          },
        });
      } else {
        throw new Error(`${datum} ${slot}: unbekanntes Beitragsformat`);
      }
    }

    /* Teaser s1-s3 werden aus den bereits finalisierten Feed-Beitraegen
       deterministisch abgeleitet. Dadurch sind wirklich alle neun Stories
       als Review-Datei sichtbar, ohne einen Autor-Aufruf. */
    for (const p of tag.plan?.stories || []) {
      if (p.art !== "teaser" || !p.beitragSlot || !p.slot) continue;
      const beitrag = tag.inhalte?.[p.beitragSlot];
      if (!beitrag) throw new Error(`${datum} ${p.slot}: Feed-Bezug ${p.beitragSlot} fehlt`);
      tag.inhalte[p.slot] = teaserFuer(p.slot, beitrag, p.beitragSlot);
    }

    const storyDir = path.join(out, "stories");
    fs.mkdirSync(storyDir, { recursive: true });
    for (const p of tag.plan?.stories || []) {
      if (!p.slot) continue;
      const story = structuredClone(tag.inhalte?.[p.slot]);
      if (!story) throw new Error(`${datum} ${p.slot}: Story-Inhalt fehlt`);
      /* Ohne Freisteller bleibt der Teaser bewusst bildlos; ein komplettes
         Cover ist kein Ersatz fuer das Motiv. Der spaetere Cover-Patch setzt
         den Freisteller, sobald er vorhanden ist. */
      story.bild = null;
      story.bildQuelle = null;
      const ziel = path.join(storyDir, `${p.slot}-${story.art}.jpg`);
      await storyRendern(story, ziel, { variante: 0 });
      mTag.stories.push({ slot: p.slot, art: story.art, datei: path.basename(ziel) });
    }

    if (mTag.stories.length !== 9) {
      throw new Error(`${datum}: erwartet 9 Stories, gerendert ${mTag.stories.length}`);
    }

    tag.renderVorschau = {
      status: "fertig",
      erzeugtAm: new Date().toISOString(),
      pfad: `vorproduktion/${datum}/fertig`,
      providerKostenUsd: 0,
      textProviderKostenUsd: 0,
      faktencheckProviderKostenUsd: 0,
      bildgenerierungKostenUsd: 0,
      coverbilder: false,
      reelStimme: "piper-offline",
      freigabeBetreiber: false,
    };
    tag.kostenPolicy = {
      ...(tag.kostenPolicy || {}),
      autorUsd: 0,
      faktencheckUsd: 0,
      sonstigeTextKiUsd: 0,
      bildgenerierungErlaubt: false,
      bildkostenUsd: 0,
      providerKostenUsd: 0,
      bilderStatus: "bewusst-ausgelassen",
    };

    const ziel = path.join(hosting.dir, "vorproduktion", datum, "fertig");
    fs.rmSync(ziel, { recursive: true, force: true });
    fs.mkdirSync(path.dirname(ziel), { recursive: true });
    fs.cpSync(out, ziel, { recursive: true });
    fs.writeFileSync(tagPfad, JSON.stringify(tag, null, 2) + "\n");
    mTag.pfad = dateiRelativ(ziel);
    manifest.tage.push(mTag);
  }

  fs.writeFileSync(
    path.join(hosting.dir, "vorproduktion", "render-ohne-coverbilder-manifest.json"),
    JSON.stringify(manifest, null, 2) + "\n",
  );

  hosting.commit(`Rendere kostenfreie Vorproduktion ${tage.join(" + ")} ohne Coverbilder`);
  await hosting.push();
} finally {
  await browserBeenden().catch(() => {});
  fs.rmSync(temp, { recursive: true, force: true });
}

console.log(JSON.stringify({
  ok: true,
  tage,
  providerKostenUsd: 0,
  bildgenerierungKostenUsd: 0,
  coverbilder: false,
  storiesJeTag: 9,
  ziel: tage.map((d) => `vorproduktion/${d}/fertig`),
}, null, 2));
