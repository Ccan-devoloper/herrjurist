#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import { videoAusBild } from "../src/videoai.mjs";

function argumente(argv) {
  const erg = {};
  for (let i = 0; i < argv.length; i += 1) {
    const teil = argv[i];
    if (!teil.startsWith("--")) continue;
    const [roh, inline] = teil.slice(2).split("=", 2);
    const wert = inline ?? argv[i + 1];
    erg[roh] = wert;
    if (inline === undefined) i += 1;
  }
  return erg;
}

const args = argumente(process.argv.slice(2));
const bild = args.bild || null;
const imageUrl = args["image-url"] || null;
const ausgabe = args.ausgabe || "out/fal-video-test/test.mp4";
const dauer = Number(args.dauer || 6);

const prompt = args.prompt || [
  "Subtle premium editorial character animation.",
  "Preserve the exact illustrated character identity, face, body proportions, outfit, colors and line style.",
  "Natural blinking and breathing, a small cautious head turn and minimal hand movement.",
  "Very gentle camera push-in.",
  "No morphing, no new objects, no text, no logos, no style change, no camera shake.",
].join(" ");

if (!bild && !imageUrl) {
  console.error("Bitte --bild <datei> oder --image-url <url> angeben.");
  process.exit(2);
}

try {
  console.log(`fal.ai Test: ${dauer}s, 1080p, 9:16, ohne generiertes Audio`);
  const ergebnis = await videoAusBild({
    bild,
    imageUrl,
    prompt,
    ausgabe,
    dauer,
    aufloesung: "1080p",
    seitenverhaeltnis: "9:16",
    fps: 25,
  });

  const meta = path.join(path.dirname(ausgabe), "ergebnis.json");
  await fs.writeFile(meta, JSON.stringify({
    ...ergebnis,
    prompt,
    erzeugtAm: new Date().toISOString(),
  }, null, 2) + "\n");

  console.log(`Fertig: ${ergebnis.ausgabe}`);
  console.log(`Metadaten: ${meta}`);
} catch (fehler) {
  console.error(fehler?.stack || fehler);
  process.exit(1);
}
