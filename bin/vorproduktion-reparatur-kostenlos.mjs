#!/usr/bin/env node
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { Hosting } from "../src/hosting.mjs";
import { storyRendern, coverRendern, browserBeenden } from "../src/render.mjs";

for (const key of ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY"]) {
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
    const m = { stories: [], reelCovers: [] };

    for (const slot of eintrag.stories || []) {
      const story = structuredClone(tag.inhalte?.[slot]);
      if (!story) throw new Error(`${datum} ${slot}: Story fehlt`);
      const ziel = path.join(hosting.dir, "vorproduktion", datum, "fertig", "stories", `${slot}-${story.art}.jpg`);
      await storyRendern(story, ziel, { variante: 0 });
      m.stories.push(path.relative(hosting.dir, ziel));
    }

    for (const slot of eintrag.reelCovers || []) {
      const reel = structuredClone(tag.inhalte?.[slot]);
      if (!reel?.szenen) throw new Error(`${datum} ${slot}: Reel fehlt`);
      const slug = reel.slug || `${datum}-${slot}`;
      const alt = path.join(hosting.dir, "vorproduktion", datum, "fertig", slot, `${slug}-cover.jpg`);
      if (!fs.existsSync(alt)) throw new Error(`${datum} ${slot}: bestehendes Cover fehlt`);

      const freigestellt = path.join(temp, `${datum}-${slot}-foreground.png`);
      execFileSync("python3", [
        path.resolve("bin/cover-foreground-local.py"),
        "--input", alt,
        "--output", freigestellt,
        "--crop-y", "900",
      ], { stdio: "inherit" });

      const puffer = fs.readFileSync(freigestellt);
      const daten = coverDatenLokal(reel);
      daten.bild = `data:image/png;base64,${puffer.toString("base64")}`;
      daten.bildFrei = true;
      daten.bildTyp = "charakter";
      daten.bildBreite = 1080;
      daten.bildHoehe = 1020;
      daten.coverHinweisPlan = null;

      await coverRendern(daten, alt, { variante: 0 });
      m.reelCovers.push(path.relative(hosting.dir, alt));
    }

    tag.renderVorschau = {
      ...(tag.renderVorschau || {}),
      letzteKostenloseReparatur: {
        stand: new Date().toISOString(),
        stories: eintrag.stories || [],
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
  await browserBeenden().catch(() => {});
  fs.rmSync(temp, { recursive: true, force: true });
}

console.log(JSON.stringify(manifest, null, 2));
