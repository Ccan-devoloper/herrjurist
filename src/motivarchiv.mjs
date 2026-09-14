/**
 * Archiv der gezeichneten Motive.
 *
 * Ein Motiv kostet Geld, ein Themenpool wiederholt sich. Beides zusammen
 * heisst: Was einmal gezeichnet wurde, kann spaeter noch einmal dienen - aber
 * nur mit deutlichem Abstand. Zweimal dasselbe Bild in einer Woche faellt auf
 * und wirkt wie ein Baukasten; zweimal im Quartal bemerkt niemand.
 *
 * Abgelegt wird das Motiv OHNE farbigen Rand. Der Rand haengt am Rechtsgebiet
 * beziehungsweise am Klausurtag und wird bei jeder Verwendung neu gezogen -
 * so passt dasselbe Motiv spaeter auch in einer anderen Farbe.
 */
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { ffmpegPfad } from "./stimme.mjs";

const INDEX = "motive.json";

/* Wortmengen statt Zeichenketten: „person reviewing notes at a desk" und
   „person reviewing notes at desk" sind dasselbe Motiv. Fuellwoerter zaehlen
   nicht mit, sonst heben sie jeden Vergleich kuenstlich an. */
const FUELL = new Set(["a", "an", "the", "of", "on", "in", "at", "with", "and", "to", "for", "from", "by", "over", "under", "into", "onto", "its", "his", "her", "their", "is", "are"]);
export function woerterMenge(text) {
  return new Set(String(text || "").toLowerCase().replace(/[^a-zäöüß0-9\s-]/g, " ").split(/[\s-]+/).filter((x) => x.length > 1 && !FUELL.has(x)));
}

/** Aehnlichkeit zweier Szenen: geteilte Woerter gegen alle Woerter (0-1). */
export function aehnlichkeit(a, b) {
  const A = woerterMenge(a), B = woerterMenge(b);
  if (!A.size || !B.size) return 0;
  let gemeinsam = 0;
  for (const x of A) if (B.has(x)) gemeinsam++;
  return gemeinsam / (A.size + B.size - gemeinsam);
}

const tage = (von, bis) => Math.round((new Date(`${bis}T12:00:00Z`) - new Date(`${von}T12:00:00Z`)) / 86400000);

/**
 * Sucht ein Motiv, das zur Szene passt und lange genug her ist.
 * @returns {{eintrag:object, aehnlich:number, alter:number}|null}
 */
export function passendesMotiv(archiv, szene, datum, { mindestTage = 90, schwelle = 0.85, themaId = null } = {}) {
  let bestes = null;
  for (const e of archiv?.motive || []) {
    const zuletzt = e.zuletzt || e.gezeichnet;
    if (!zuletzt) continue;
    const alter = tage(zuletzt, datum);
    /* Die Sperrfrist hält dasselbe Bild aus dem Feed fern - sie gilt aber
       nicht für den Beitrag, zu dem das Motiv gehört. Wird derselbe Beitrag
       noch einmal gerendert, weil er berichtigt und neu gestellt wird, ist
       sein eigenes Motiv die richtige Wahl, nicht ein frisch gezeichnetes.

       Am 14.09. fehlte die Ausnahme: Die Neuveröffentlichung des
       Erbrechtsbeitrags zeichnete dieselbe Szene ein zweites Mal. Das kostete
       nicht nur 0,01 $ - es lieferte auch die Figur mit dem abgeschnittenen
       Kopf, während das brauchbare Motiv im Archiv lag. */
    const eigenes = themaId && e.themaId && e.themaId === themaId;
    if (!eigenes && alter < mindestTage) continue;
    const a = aehnlichkeit(szene, e.szene);
    if (a < schwelle) continue;
    /* Bei gleicher Passung das aeltere - es war am laengsten nicht zu sehen. */
    if (!bestes || a > bestes.aehnlich || (a === bestes.aehnlich && alter > bestes.alter)) bestes = { eintrag: e, aehnlich: a, alter };
  }
  return bestes;
}

export function archivLaden(dir) {
  const p = path.join(dir, INDEX);
  try { return fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, "utf8")) : { motive: [] }; } catch { return { motive: [] }; }
}

export function archivSpeichern(dir, archiv) {
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, INDEX), JSON.stringify(archiv, null, 2));
}

/**
 * PNG nach WebP, mit Transparenz. Eine flache Illustration schrumpft dabei auf
 * etwa ein Fuenftel - das entscheidet darueber, ob das Archiv anderthalb Jahre
 * tragen kann oder nach vier Monaten anfaengt, Brauchbares hinauszuwerfen.
 * Klappt es nicht (ffmpeg ohne libwebp), bleibt es beim PNG.
 */
export function nachWebp(quelle, ziel) {
  const s = spawnSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-i", quelle, "-c:v", "libwebp", "-lossless", "0", "-q:v", "88", "-frames:v", "1", ziel], { encoding: "utf8", timeout: 60000 });
  if (s.status !== 0 || !fs.existsSync(ziel) || fs.statSync(ziel).size < 500) { fs.rmSync(ziel, { force: true }); return null; }
  return ziel;
}

/** Legt ein frisch gezeichnetes Motiv ab (ohne Rand). */
export function motivAblegen(dir, archiv, { szene, quelle, datum, breite, hoehe, themaId = null, max = 1500 }) {
  if (!dir || !fs.existsSync(quelle)) return archiv;
  fs.mkdirSync(dir, { recursive: true });
  const kennung = `${datum}-${Math.random().toString(36).slice(2, 8)}`;
  let name = `${kennung}.webp`;
  if (!nachWebp(quelle, path.join(dir, name))) { name = `${kennung}.png`; fs.copyFileSync(quelle, path.join(dir, name)); }
  archiv.motive = [...(archiv.motive || []), { datei: name, szene, themaId, gezeichnet: datum, zuletzt: datum, benutzt: 1, breite: breite || null, hoehe: hoehe || null }];
  /* Deckel gegen ein Archiv, das mit den Jahren den Zweig sprengt: Das am
     laengsten ungenutzte faellt zuerst. */
  while (archiv.motive.length > max) {
    const alt = archiv.motive.reduce((a, b) => ((a.zuletzt || a.gezeichnet) <= (b.zuletzt || b.gezeichnet) ? a : b));
    fs.rmSync(path.join(dir, alt.datei), { force: true });
    archiv.motive = archiv.motive.filter((m) => m !== alt);
  }
  archivSpeichern(dir, archiv);
  return archiv;
}

/** Vermerkt, dass ein archiviertes Motiv heute wieder verwendet wurde. */
export function verwendungVermerken(dir, archiv, eintrag, datum) {
  eintrag.zuletzt = datum;
  eintrag.benutzt = (eintrag.benutzt || 1) + 1;
  archivSpeichern(dir, archiv);
  return archiv;
}
