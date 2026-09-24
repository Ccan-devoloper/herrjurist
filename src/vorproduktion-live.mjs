import fs from "node:fs";
import path from "node:path";

const files = (dir, re) => fs.readdirSync(dir, { withFileTypes: true })
  .filter((e) => e.isFile() && re.test(e.name))
  .map((e) => path.join(dir, e.name))
  .sort();

const url = (vp, p) => `${vp.basisUrl}/${path.relative(vp.assetDir, p).split(path.sep).map(encodeURIComponent).join("/")}`;

export function vorproduktionLaden(hosting, datum) {
  const rel = path.join("vorproduktion", `${datum}.json`);
  const p = path.join(hosting.dir, rel);
  if (!fs.existsSync(p)) return null;
  const tag = JSON.parse(fs.readFileSync(p, "utf8"));
  if (tag?.datum !== datum || !Array.isArray(tag?.plan?.beitraege) || !Array.isArray(tag?.plan?.stories) || !tag?.inhalte) {
    throw new Error(`Vorproduktion ${datum} unvollstaendig; kein kostenpflichtiger Fallback.`);
  }
  const fertigRel = tag?.renderVorschau?.pfad || path.join("vorproduktion", datum, "fertig");
  const fertigDir = path.join(hosting.dir, fertigRel);
  if (!fs.existsSync(fertigDir)) throw new Error(`Vorproduktion ${datum} ohne Fertig-Assets; kein kostenpflichtiger Fallback.`);
  const vp = { tag, rel, assetDir: hosting.dir, basisUrl: hosting.basisUrl, fertigRel, fertigDir };

  for (const b of tag.plan.beitraege) {
    const d = path.join(fertigDir, b.slot);
    if (!fs.existsSync(d) || !tag.inhalte[b.slot]) throw new Error(`Vorproduktion ${datum}: ${b.slot} unvollstaendig; kein kostenpflichtiger Fallback.`);
    if (b.format === "reel") {
      if (!files(d, /\.mp4$/i).length || !files(d, /\.jpe?g$/i).length) throw new Error(`Vorproduktion ${datum}: Reel ${b.slot} unvollstaendig; kein kostenpflichtiger Fallback.`);
    } else if (!files(d, /\.jpe?g$/i).length) throw new Error(`Vorproduktion ${datum}: Bilder ${b.slot} fehlen; kein kostenpflichtiger Fallback.`);
  }
  const sd = path.join(fertigDir, "stories");
  for (const s of tag.plan.stories) {
    if (!fs.existsSync(sd) || !files(sd, new RegExp(`^${s.slot}-.*\\.jpe?g$`, "i")).length) throw new Error(`Vorproduktion ${datum}: Story ${s.slot} fehlt; kein kostenpflichtiger Fallback.`);
    if (s.art !== "teaser" && !tag.inhalte[s.slot]) throw new Error(`Vorproduktion ${datum}: Story-Inhalt ${s.slot} fehlt; kein kostenpflichtiger Fallback.`);
  }
  return vp;
}

const merge = (neu, alt) => alt?.status === "veroeffentlicht"
  ? { ...neu, status: alt.status, medienId: alt.medienId, veroeffentlicht: alt.veroeffentlicht, kanaele: alt.kanaele, interaktiv: alt.interaktiv }
  : neu;

export function planAusVorproduktion(vp, alt = null) {
  const b = new Map((alt?.beitraege || []).map((e) => [e.slot, e]));
  const s = new Map((alt?.stories || []).map((e) => [e.slot, e]));
  const base = (e) => ({ ...e, status: "geplant" });
  return {
    datum: vp.tag.datum, erzeugt: alt?.erzeugt || new Date().toISOString(), anlass: vp.tag.plan.anlass || null, abendAnlass: vp.tag.plan.abendAnlass || null, trocken: false,
    vorproduktion: { aktiv: true, quelle: vp.rel.replaceAll("\\", "/"), fertig: vp.fertigRel.replaceAll("\\", "/"), kostenfrei: true },
    beitraege: vp.tag.plan.beitraege.map((e) => merge(base(e), b.get(e.slot))),
    stories: vp.tag.plan.stories.map((e) => merge(base(e), s.get(e.slot))),
  };
}

export function inhalteUebernehmen(hosting, vp, plan) {
  const done = new Set([...(plan.beitraege || []), ...(plan.stories || [])].filter((e) => e.status === "veroeffentlicht").map((e) => e.slot));
  let n = 0;
  for (const [slot, roh] of Object.entries(vp.tag.inhalte)) {
    if (done.has(slot)) continue;
    const x = structuredClone(roh);
    Object.assign(x, { freigabeBetreiber: true, liveVerknuepft: true, vorproduktionStatus: "live-vorrang", vorproduktionQuelle: vp.rel.replaceAll("\\", "/") });
    hosting.jsonSchreiben(`inhalte/${vp.tag.datum}-${slot}.json`, x); n++;
  }
  return n;
}

export function feedAssets(vp, e) {
  const d = path.join(vp.fertigDir, e.slot);
  if (e.format === "reel") {
    const videoPfad = files(d, /\.mp4$/i)[0];
    const coverPfad = files(d, /cover.*\.jpe?g$/i)[0] || files(d, /\.jpe?g$/i)[0];
    return { videoPfad, coverPfad, videoUrl: url(vp, videoPfad), coverUrl: url(vp, coverPfad) };
  }
  const bildPfade = files(d, /\.jpe?g$/i);
  return { bildPfade, bildUrls: bildPfade.map((p) => url(vp, p)) };
}

export function storyAsset(vp, slot) {
  const p = files(path.join(vp.fertigDir, "stories"), new RegExp(`^${slot}-.*\\.jpe?g$`, "i"))[0];
  return { bildPfad: p, bildUrl: url(vp, p) };
}
