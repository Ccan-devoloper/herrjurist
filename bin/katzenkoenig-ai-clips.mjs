#!/usr/bin/env node
import { videoAusBild } from "../src/videoai.mjs";

const tests = [
  {
    bild: "assets/charaktere/mara-sternpfad.jpg.b64",
    ausgabe: "out/katzenkoenig-ai/mara.mp4",
    prompt: "Subtle premium 2D editorial cartoon animation. Preserve the exact character identity, face, body proportions, outfit, colors and line style. The older grey-haired female adventurer leans in slightly as if urgently whispering, one small controlled hand gesture, natural blinking and breathing, very gentle camera push-in, faint purple mystical ambience. No morphing, no new characters, no text, no logos, no dramatic pose change, no camera shake."
  },
  {
    bild: "assets/charaktere/form-7.jpg.b64",
    ausgabe: "out/katzenkoenig-ai/form7.mp4",
    prompt: "Subtle premium 2D editorial cartoon animation. Preserve the exact small pale blue and white hovering robot identity, proportions, antenna, ring logo, colors and line style. Gentle hover bob, one thoughtful head tilt, one small pointer-like hand gesture, natural eye movement, slow camera push-in, faint cool blue-purple ambience. No morphing, no new objects, no text, no logos, no camera shake."
  }
];

for (const t of tests) {
  console.log("\n---", t.ausgabe, "---");
  const r = await videoAusBild({
    ...t,
    dauer: 6,
    aufloesung: "1080p",
    seitenverhaeltnis: "9:16",
    fps: 25,
  });
  console.log(JSON.stringify(r));
}
