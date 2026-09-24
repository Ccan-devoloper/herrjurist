#!/usr/bin/env node
/**
 * Gezielter, providerfreier Patch fuer bereits vorhandene Reels.
 *
 * Die Szenenbilder liegen im Asset-Zweig und werden als vollflaechige
 * transparente 1080x1920-Overlays in das Erklaervideo eingebettet.
 * Es werden nur das Ziel-Reel und seine lokal erzeugten Piper-Audiodateien
 * ersetzt; Cover, andere Feed-Slots und Stories bleiben unangetastet.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { Hosting } from "../src/hosting.mjs";
import { reelBauen } from "../src/reel.mjs";
import { browserBeenden } from "../src/render.mjs";

function providerfreiPruefen() {
  for (const key of ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY", "PEXELS_API_KEY"]) {
    if (String(process.env[key] || "").trim()) {
      throw new Error(`Reel-Overlay-Patch verweigert Provider-Secret: ${key}`);
    }
  }
  if (String(process.env.IG_STIMME || "").toLowerCase() !== "piper") {
    throw new Error("Reel-Overlay-Patch verlangt IG_STIMME=piper.");
  }
  if (String(process.env.IG_BILD_KI || "").toLowerCase() !== "false") {
    throw new Error("Reel-Overlay-Patch verlangt IG_BILD_KI=false.");
  }
  if (String(process.env.IG_CHARAKTERE || "").toLowerCase() !== "false") {
    throw new Error("Reel-Overlay-Patch verlangt IG_CHARAKTERE=false.");
  }
}

function pngMasse(pfad) {
  const b = fs.readFileSync(pfad);
  if (b.length < 24 || b[0] !== 0x89 || b.toString("ascii", 1, 4) !== "PNG") {
    throw new Error(`Overlay ist keine PNG-Datei: ${pfad}`);
  }
  return { breite: b.readUInt32BE(16), hoehe: b.readUInt32BE(20) };
}

function assetPfad(hosting, relativ) {
  const sauber = String(relativ || "").replaceAll("\\", "/").replace(/^\/+/, "");
  if (!sauber || sauber.split("/").includes("..")) throw new Error(`Ungueltiger Overlay-Pfad: ${relativ}`);
  const absolut = path.resolve(hosting.dir, sauber);
  const basis = path.resolve(hosting.dir) + path.sep;
  if (!absolut.startsWith(basis)) throw new Error(`Overlay verlaesst Asset-Zweig: ${relativ}`);
  if (!fs.existsSync(absolut)) throw new Error(`Overlay fehlt im Asset-Zweig: ${relativ}`);
  const { breite, hoehe } = pngMasse(absolut);
  if (breite !== 1080 || hoehe !== 1920) {
    throw new Error(`Overlay muss 1080x1920 sein: ${relativ} ist ${breite}x${hoehe}`);
  }
  return absolut;
}

export async function reelOverlayPatchen({ tage = [], slots = ["b3"] } = {}) {
  providerfreiPruefen();
  if (!tage.length) throw new Error("Mindestens ein Datum fuer den Reel-Overlay-Patch erforderlich.");
  const hosting = new Hosting({ pushen: true }).vorbereiten();
  const temp = fs.mkdtempSync(path.join(os.tmpdir(), "herrjurist-reel-overlay-"));
  const manifest = {
    version: 1,
    erzeugtAm: new Date().toISOString(),
    modus: "reel-overlay-patch-providerfrei",
    providerKostenUsd: 0,
    bildgenerierungKostenUsd: 0,
    stimme: "piper-offline",
    ziele: [],
  };

  try {
    for (const datum of tage) {
      const tagPfad = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
      if (!fs.existsSync(tagPfad)) throw new Error(`Vorproduktion fehlt: ${datum}`);
      const tag = JSON.parse(fs.readFileSync(tagPfad, "utf8"));

      for (const slot of slots) {
        const reel = structuredClone(tag.inhalte?.[slot]);
        if (!Array.isArray(reel?.szenen) || !reel.szenen.length) {
          throw new Error(`${datum} ${slot}: Reel-Szenen fehlen`);
        }
        delete reel.reelFinalUrl;
        delete reel.reelFinalDauer;
        delete reel.reelFinalLayout;
        delete reel.reelFinalStimmeAnbieter;
        delete reel.reelFinalStimmeId;
        delete reel.reelFinalStimmeName;

        const overlays = reel.szenen.map((szene, i) => {
          if (!szene.overlayQuelle) throw new Error(`${datum} ${slot} Szene ${i + 1}: overlayQuelle fehlt`);
          const absolut = assetPfad(hosting, szene.overlayQuelle);
          szene.overlay = absolut;
          return szene.overlayQuelle;
        });

        const ausgabe = path.join(temp, datum, slot);
        const gebaut = await reelBauen(reel, ausgabe, {
          datum,
          layout: "erklaer",
          clip: null,
          framesBehalten: false,
        });

        const zielDir = path.join(hosting.dir, "vorproduktion", datum, "fertig", slot);
        fs.mkdirSync(zielDir, { recursive: true });
        const zielVideo = path.join(zielDir, `${datum}-${slot}.mp4`);
        fs.copyFileSync(gebaut.video, zielVideo);

        const audioQuelle = path.join(ausgabe, "audio");
        const audioZiel = path.join(zielDir, "audio");
        fs.rmSync(audioZiel, { recursive: true, force: true });
        fs.cpSync(audioQuelle, audioZiel, { recursive: true });

        manifest.ziele.push({
          datum,
          slot,
          video: path.relative(hosting.dir, zielVideo).split(path.sep).join("/"),
          overlays,
          dauer: gebaut.dauer,
          szenen: gebaut.szenen,
          providerKostenUsd: 0,
        });
      }

      tag.renderVorschau ||= {};
      tag.renderVorschau.reelOverlayPatch = {
        stand: new Date().toISOString(),
        slots,
        providerKostenUsd: 0,
        bildgenerierungKostenUsd: 0,
        stimme: "piper-offline",
      };
      fs.writeFileSync(tagPfad, JSON.stringify(tag, null, 2) + "\n");
    }

    fs.writeFileSync(
      path.join(hosting.dir, "vorproduktion", "reel-overlay-patch-manifest.json"),
      JSON.stringify(manifest, null, 2) + "\n",
    );
    hosting.commit(`Reel-Szenenoverlays providerfrei anwenden: ${tage.join(" + ")} ${slots.join(",")}`);
    await hosting.push();
    return manifest;
  } finally {
    await browserBeenden().catch(() => {});
    fs.rmSync(temp, { recursive: true, force: true });
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const tage = process.argv.slice(2).filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x));
  const slotsArg = process.argv.find((x) => x.startsWith("--slots="));
  const slots = String(slotsArg?.slice(8) || "b3").split(",").map((x) => x.trim()).filter(Boolean);
  const manifest = await reelOverlayPatchen({ tage, slots });
  console.log(JSON.stringify({ ok: true, ...manifest }, null, 2));
}
