import fs from "node:fs";
import path from "node:path";
import { createHash } from "node:crypto";

/* Die Sichtfreigabe ersetzt NUR den pauschalen Zeichenzaehler, niemals
   Inhalts-, Befund- oder Quizpruefungen. Keine Netzwerk-/Provideraufrufe.
   Freigaben werden bewusst im Code-Zweig gepflegt, nicht aus frei
   editierbaren Story-Metadaten oder einem einfachen Boolean uebernommen. */
const REGISTER = new URL("../config/story-render-freigaben.json", import.meta.url);
const LAUF_FELDER = new Set([
  "freigabeBetreiber", "liveVerknuepft", "vorproduktionStatus", "vorproduktionQuelle",
]);

function kanonisch(wert) {
  if (Array.isArray(wert)) return wert.map(kanonisch);
  if (wert && typeof wert === "object") {
    return Object.fromEntries(Object.keys(wert).sort().map((k) => [k, kanonisch(wert[k])]));
  }
  return wert;
}

export function storyRenderInhaltSha256(story) {
  const inhalt = Object.fromEntries(Object.entries(story || {}).filter(([k]) => !LAUF_FELDER.has(k)));
  return createHash("sha256").update(JSON.stringify(kanonisch(inhalt))).digest("hex");
}

export function storyBildSha256(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

/* Separater, deterministischer Pruefkern fuer Offline-Tests.
   Der produktive Wrapper unten verwendet ausschliesslich das feste Register. */
export function pruefeStoryRenderFreigabe(story, vp, freigaben) {
  try {
    if (story?.manuellGeprueft !== true || !vp?.assetDir || !vp?.tag) return false;
    if (story.faktencheckOffen || (story.beanstandetFachlich || []).length) return false;
    if ((story.beanstandet || []).length && !story.befundeTypisiert) return false;
    const datum = vp.tag.datum;
    if (!/^\d{4}-\d{2}-\d{2}$/.test(datum || "") || !/^s\d+$/.test(story.slot || "")) return false;
    if (!/^[a-z]+$/.test(story.art || "")) return false;
    const erwartet = `vorproduktion/${datum}/fertig/stories/${story.slot}-${story.art}.jpg`;
    if (String(vp.fertigRel || "").replaceAll("\\", "/") !== `vorproduktion/${datum}/fertig`) return false;
    const plan = vp.tag.plan?.stories?.find((s) => s.slot === story.slot);
    if (!plan || plan.art !== story.art) return false;
    const f = (freigaben || []).find((x) => x.datum === datum && x.slot === story.slot && x.art === story.art);
    if (!f || f.pfad !== erwartet || f.visuellGeprueft !== true) return false;
    if (!f.freigegebenVon || !Number.isFinite(Date.parse(f.freigegebenAm || ""))) return false;
    if (!/^[a-f0-9]{64}$/.test(f.inhaltSha256 || "") || !/^[a-f0-9]{64}$/.test(f.bildSha256 || "")) return false;
    if (storyRenderInhaltSha256(story) !== f.inhaltSha256) return false;
    if (storyRenderInhaltSha256(vp.tag.inhalte?.[story.slot]) !== f.inhaltSha256) return false;
    const basis = fs.realpathSync(vp.assetDir);
    const datei = fs.realpathSync(path.join(basis, erwartet));
    const rel = path.relative(basis, datei);
    if (rel.startsWith("..") || path.isAbsolute(rel)) return false;
    const bytes = fs.readFileSync(datei);
    if (bytes.length < 4 || bytes[0] !== 0xff || bytes[1] !== 0xd8) return false;
    return storyBildSha256(bytes) === f.bildSha256;
  } catch {
    // Fehlende/geaenderte Assets oder Register: normale strenge Pruefung.
    return false;
  }
}

export function visuelleStoryLaengeFreigegeben(story, vp) {
  try {
    const register = JSON.parse(fs.readFileSync(REGISTER, "utf8"));
    if (register.version !== 1 || register.repository !== "Ccan-devoloper/herrjurist") return false;
    return pruefeStoryRenderFreigabe(story, vp, register.freigaben);
  } catch {
    return false;
  }
}
