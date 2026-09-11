/* ==========================================================================
   Motive freistellen.

   Ein Foto als Rechteck auf die Kachel zu kleben sieht nach Baukasten aus.
   Freigestellt – Hintergrund weg, das Motiv läuft unten rechts aus dem Bild –
   sieht es nach Gestaltung aus. Genau so sind die bisherigen Beiträge des
   Kanals aufgebaut.

   Gemacht wird das von rembg (u2net) lokal auf dem Runner; kein Dienst, keine
   Kosten. Fehlt rembg oder taugt das Ergebnis nicht, gibt es kein Bild – dann
   bleibt die Icon-Bühne. Ein halb ausgeschnittenes Motiv wäre schlimmer als
   gar keines.
   ========================================================================== */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { ffmpegPfad } from "./stimme.mjs";

export function rembgVorhanden() {
  return spawnSync("sh", ["-c", "command -v rembg"], { stdio: "ignore" }).status === 0;
}

/**
 * Deckung: Anteil der Fläche, den das freigestellte Motiv einnimmt (0–1).
 * Nahe 1 heißt: Es wurde nichts entfernt (der Hintergrund blieb stehen).
 * Nahe 0 heißt: Es wurde alles entfernt. Beides ist unbrauchbar.
 */
export function deckung(pngPfad) {
  const r = spawnSync(ffmpegPfad(), ["-hide_banner", "-loglevel", "error", "-i", pngPfad,
    "-vf", "alphaextract,scale=48:48", "-f", "rawvideo", "-pix_fmt", "gray", "-"], { maxBuffer: 1 << 20 });
  if (r.status !== 0 || !r.stdout?.length) return null;
  let summe = 0;
  for (const b of r.stdout) summe += b;
  return summe / (r.stdout.length * 255);
}

/**
 * Schneidet die durchsichtigen Ränder weg, sodass das Motiv das Bild ausfüllt.
 * Ohne diesen Schritt bleibt das freigestellte Motiv so klein wie im
 * Originalfoto – bei einem stehenden Menschen in einer Querformat-Aufnahme
 * sind das schnell 80 Prozent Luft.
 */
export function zuschneiden(pngPfad) {
  /* Der Alphakanal wird auf ein grobes Raster verkleinert und darin die
     Umrandung des Motivs gesucht. cropdetect wäre der naheliegende Weg, meldet
     bei durchsichtigen Rändern aber nichts – hier zählt jedes Pixel selbst. */
  const N = 96;
  const r = spawnSync(ffmpegPfad(), ["-hide_banner", "-loglevel", "error", "-i", pngPfad,
    "-vf", `alphaextract,scale=${N}:${N}`, "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"], { maxBuffer: 1 << 22 });
  if (r.status !== 0 || r.stdout?.length !== N * N) return pngPfad;
  let l = N, o = N, re = -1, u = -1;
  for (let y = 0; y < N; y++) for (let x = 0; x < N; x++) {
    if (r.stdout[y * N + x] < 24) continue;      // fast durchsichtig
    if (x < l) l = x; if (x > re) re = x;
    if (y < o) o = y; if (y > u) u = y;
  }
  if (re < 0 || u < 0) return pngPfad;
  const masse = spawnSync(ffmpegPfad(), ["-hide_banner", "-i", pngPfad, "-f", "null", "-"], { encoding: "utf8" });
  const g = String(masse.stderr || "").match(/,\s(\d+)x(\d+)/);
  if (!g) return pngPfad;
  const [B, H] = [Number(g[1]), Number(g[2])];
  /* Etwas Luft stehen lassen, sonst klebt das Motiv am Rand. */
  const luft = 2;
  const x = Math.max(0, Math.floor(((l - luft) / N) * B));
  const y = Math.max(0, Math.floor(((o - luft) / N) * H));
  const bb = Math.min(B - x, Math.ceil(((re - l + 1 + 2 * luft) / N) * B));
  const hh = Math.min(H - y, Math.ceil(((u - o + 1 + 2 * luft) / N) * H));
  if (bb < 32 || hh < 32 || (bb >= B * 0.98 && hh >= H * 0.98)) return pngPfad;
  const ziel = pngPfad.replace(/\.png$/, "-eng.png");
  const s2 = spawnSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-i", pngPfad, "-vf", `crop=${bb}:${hh}:${x}:${y}`, ziel], { encoding: "utf8" });
  if (s2.status !== 0 || !fs.existsSync(ziel)) return pngPfad;
  fs.rmSync(pngPfad, { force: true });
  return ziel;
}

/**
 * Stellt ein Bild frei.
 * @returns {{pfad:string, deckung:number}|null} null = nicht brauchbar
 */
export function freistellen(quelle, { min = 0.06, max = 0.82, modell = process.env.IG_BILDER_MODELL || "isnet-general-use" } = {}) {
  if (!rembgVorhanden()) return null;
  const ziel = path.join(os.tmpdir(), `frei-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  /* Modell ausdrücklich wählen: rembg 2.0.8x lädt sonst „bria-rmbg“, ein
     Gigabyte, und schneidet mit weichem Saum. isnet-general-use (180 MB)
     liefert im Vergleich die sauberste Kante - ohne Alpha-Matting, das auf
     farbigem Grund einen hellen Schein um das Motiv legt. */
  const r = spawnSync("rembg", ["i", "-m", modell, quelle, ziel], { encoding: "utf8", timeout: 180000 });
  if (r.status !== 0 || !fs.existsSync(ziel)) {
    console.warn(`  ! Freistellen fehlgeschlagen: ${(r.stderr || "").slice(0, 160)}`);
    return null;
  }
  const d = deckung(ziel);
  /* Zu viel übrig heißt: Der Hintergrund wurde nicht erkannt, das Motiv steht
     weiter im Kasten. Zu wenig heißt: Es ist nichts mehr da. */
  if (d == null || d > max || d < min) {
    console.log(`  → freigestelltes Motiv verworfen (Deckung ${d == null ? "?" : (d * 100).toFixed(0) + " %"}) – Titelfolie bleibt beim Icon.`);
    fs.rmSync(ziel, { force: true });
    return null;
  }
  /* Ein Motiv, das oben oder seitlich vom Fotorand abgeschnitten ist, wirkt
     auf der Kachel wie ein Fehler: Der Richterhammer endet in der Luft, der
     Kopf fehlt. Unten darf es anschneiden - da läuft es ohnehin aus der
     Kachel. */
  const rand = randkontakt(ziel);
  if (rand && (rand.oben > 0.04 || rand.links > 0.12 || rand.rechts > 0.12)) {
    console.log(`  → freigestelltes Motiv verworfen (vom Fotorand angeschnitten: oben ${(rand.oben * 100).toFixed(0)} %, links ${(rand.links * 100).toFixed(0)} %, rechts ${(rand.rechts * 100).toFixed(0)} %) – Titelfolie bleibt beim Icon.`);
    fs.rmSync(ziel, { force: true });
    return null;
  }
  /* Deckung wird am ungeschnittenen Bild gemessen (dort sagt sie etwas über
     die Qualität der Freistellung), zugeschnitten wird danach. */
  return { pfad: zuschneiden(ziel), deckung: d };
}

/**
 * Anteil der deckenden Pixel in der äußersten Reihe je Bildrand (0–1).
 * Berührt das Motiv den oberen oder einen seitlichen Rand, ist es im Foto
 * angeschnitten.
 */
export function randkontakt(pngPfad) {
  const N = 96;
  const r = spawnSync(ffmpegPfad(), ["-hide_banner", "-loglevel", "error", "-i", pngPfad,
    "-vf", `alphaextract,scale=${N}:${N}`, "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"], { maxBuffer: 1 << 22 });
  if (r.status !== 0 || r.stdout?.length !== N * N) return null;
  const deckend = (x, y) => r.stdout[y * N + x] >= 128;
  let oben = 0, unten = 0, links = 0, rechts = 0;
  for (let i = 0; i < N; i++) { if (deckend(i, 0)) oben++; if (deckend(i, N - 1)) unten++; if (deckend(0, i)) links++; if (deckend(N - 1, i)) rechts++; }
  return { oben: oben / N, unten: unten / N, links: links / N, rechts: rechts / N };
}
