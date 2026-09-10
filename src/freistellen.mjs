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
 * Stellt ein Bild frei.
 * @returns {{pfad:string, deckung:number}|null} null = nicht brauchbar
 */
export function freistellen(quelle, { min = 0.06, max = 0.82 } = {}) {
  if (!rembgVorhanden()) return null;
  const ziel = path.join(os.tmpdir(), `frei-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  const r = spawnSync("rembg", ["i", quelle, ziel], { encoding: "utf8", timeout: 120000 });
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
  return { pfad: ziel, deckung: d };
}
