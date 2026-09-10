/* Schwarz/Weiß-Wechsel: Welche Variante bekommt der nächste Beitrag?
   Maßgeblich ist, was tatsächlich auf Instagram liegt – das zuletzt
   veröffentlichte Bild wird geladen und seine Helligkeit gemessen. Erst wenn
   das nicht geht (Trockenlauf, Netz, ffmpeg fehlt), zählt das Ledger. */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { ffmpegPfad } from "./stimme.mjs";
import { naechsteVariante } from "./planer.mjs";

/* Mittlere Helligkeit eines Bildes (0–255) über ffmpeg – Skalierung auf 1×1 Pixel. */
export function helligkeit(datei) {
  const r = spawnSync(ffmpegPfad(), ["-hide_banner", "-loglevel", "error", "-i", datei, "-frames:v", "1", "-vf", "scale=1:1:flags=area", "-pix_fmt", "gray", "-f", "rawvideo", "-"], { maxBuffer: 1 << 20 });
  if (r.status !== 0 || !r.stdout?.length) throw new Error(`ffmpeg: ${r.stderr?.toString().trim() || "keine Ausgabe"}`);
  return r.stdout[0];
}

/* 0 = dunkel (kanzlei), 1 = hell (kanzlei-hell). */
export const varianteAusHelligkeit = (wert) => (wert >= 128 ? 1 : 0);

export async function varianteErmitteln({ ig, ledger, trocken = false, log = () => {} }) {
  const ausLedger = naechsteVariante(ledger);
  if (trocken || !ig) return ausLedger;
  try {
    const letzter = await ig.letzterBeitrag();
    if (!letzter?.bildUrl) return ausLedger;
    const res = await fetch(letzter.bildUrl);
    if (!res.ok) throw new Error(`Bild ${res.status}`);
    const datei = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "ig-letzter-")), "bild.jpg");
    fs.writeFileSync(datei, Buffer.from(await res.arrayBuffer()));
    const wert = helligkeit(datei);
    fs.rmSync(path.dirname(datei), { recursive: true, force: true });
    const naechste = 1 - varianteAusHelligkeit(wert);
    if (naechste !== ausLedger) log(`  Wechsel: letzter Beitrag auf Instagram ist ${wert >= 128 ? "hell" : "dunkel"} (${wert}) – Ledger sagte anders, Instagram gilt.`);
    return naechste;
  } catch (e) {
    log(`  Wechsel: Helligkeit des letzten Beitrags nicht messbar (${e.message}) – Ledger gilt.`);
    return ausLedger;
  }
}
