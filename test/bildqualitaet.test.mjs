import test from "node:test";
import assert from "node:assert/strict";

import { komponentenAusAlpha, komponentenVerdacht, freistellerRandVerdacht, RAND_UNTEN_MAX } from "../src/freistellen.mjs";
import { pexelsKartenFallbackErlaubt } from "../src/bilder.mjs";
import { bildAuftrag } from "../src/bildki.mjs";
import { folieHtml } from "../src/vorlagen.mjs";
import { kontext } from "../src/render.mjs";

test("Bild-QA: mehrere getrennte Hauptmotive werden als Collage verworfen", () => {
  const N = 8, alpha = Buffer.alloc(N * N);
  const set = (x, y) => { alpha[y * N + x] = 255; };
  for (const [ox, oy] of [[0,0],[3,0],[6,0]]) {
    set(ox, oy); set(ox + 1, oy); set(ox, oy + 1); set(ox + 1, oy + 1);
  }
  const profil = komponentenAusAlpha(alpha, N, { minPixel: 1 });
  assert.equal(profil.anzahl, 3);
  assert.match(komponentenVerdacht(profil), /3 getrennte/);
});

test("Bild-QA: breiter Anschnitt am unteren Fotorand wird verworfen", () => {
  assert.equal(freistellerRandVerdacht({ oben:0, links:0, rechts:0, unten:RAND_UNTEN_MAX - 0.05 }), null);
  assert.match(freistellerRandVerdacht({ oben:0, links:0, rechts:0, unten:RAND_UNTEN_MAX + 0.2 }), /unten/);
});

test("Bild-Pipeline: Pexels-Karte ist kein automatischer Fallback vor Bild-KI", () => {
  assert.equal(pexelsKartenFallbackErlaubt({ kiAktiv:true, rechteckErlaubt:true }), false);
  assert.equal(pexelsKartenFallbackErlaubt({ kiAktiv:false, rechteckErlaubt:false }), false);
  assert.equal(pexelsKartenFallbackErlaubt({ kiAktiv:false, rechteckErlaubt:true }), true);
});

test("Bild-Pipeline: KI-Auftrag erzwingt ein einzelnes Motiv statt Objekt-Collage", () => {
  const prompt = bildAuftrag("calendar, folder and calculator on a desk", { look:"foto" });
  assert.match(prompt, /single most important subject/i);
  assert.match(prompt, /never make a collage/i);
});

test("Bild-Layout: Fotokarten werden vollständig gezeigt statt mit cover abgeschnitten", () => {
  const html = folieHtml({ art:"titel", titel:"Test", icon:"kalender", bild:"data:image/jpeg;base64,AA==", bildFrei:false }, kontext({ fach:null, klausur:1 }), 1, 1);
  assert.match(html, /\.foto img\{[^}]*object-fit:contain/);
  assert.doesNotMatch(html, /\.foto img\{[^}]*object-fit:cover/);
  assert.match(html, /\.frei\{position:absolute;right:36px;bottom:34px/);
});
