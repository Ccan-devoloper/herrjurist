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
export function passendesMotiv(archiv, szene, datum, { mindestTage = 90, schwelle = 0.6 } = {}) {
  let bestes = null;
  for (const e of archiv?.motive || []) {
    const zuletzt = e.zuletzt || e.gezeichnet;
    if (!zuletzt) continue;
    const alter = tage(zuletzt, datum);
    if (alter < mindestTage) continue;
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

/** Legt ein frisch gezeichnetes Motiv ab (ohne Rand). */
export function motivAblegen(dir, archiv, { szene, quelle, datum, breite, hoehe, max = 300 }) {
  if (!dir || !fs.existsSync(quelle)) return archiv;
  fs.mkdirSync(dir, { recursive: true });
  const name = `${datum}-${Math.random().toString(36).slice(2, 8)}.png`;
  fs.copyFileSync(quelle, path.join(dir, name));
  archiv.motive = [...(archiv.motive || []), { datei: name, szene, gezeichnet: datum, zuletzt: datum, benutzt: 1, breite: breite || null, hoehe: hoehe || null }];
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
