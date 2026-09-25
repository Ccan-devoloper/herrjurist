#!/usr/bin/env node
/**
 * Gibt den vom Planer erzeugten Plan (bin/vorproduktion-vorbereiten.mjs mit
 * IG_NO_PUSH=true) kompakt aus: Slots, Zeiten, Formate, Themen-IDs, Titel,
 * Normen. Bewusst OHNE die Kern-Texte des verschlüsselten Themenpools – die
 * Inhalte werden redaktionell neu geschrieben.
 */
import fs from "node:fs";
import path from "node:path";
import { themenpool } from "../src/inhalte.mjs";
import { CONFIG } from "../src/config.mjs";

const tage = process.argv.slice(2).filter((d) => /^\d{4}-\d{2}-\d{2}$/.test(d));
const dir = path.resolve(CONFIG.hosting.verzeichnis, "vorproduktion");
const pool = new Map(themenpool().map((t) => [t.id, t]));
const meta = (id) => {
  const t = pool.get(id);
  if (!t) return {};
  return { titel: t.titel, fach: t.fach, klausur: t.klausur, typ: t.typ, normen: t.normen || [], streit: Boolean(t.streit), prioritaet: t.prioritaet };
};
console.log("===== JAHRESPLAN START =====");
for (const d of tage) {
  const tag = JSON.parse(fs.readFileSync(path.join(dir, `${d}.json`), "utf8"));
  const out = {
    datum: d,
    beitraege: tag.plan.beitraege.map((b) => ({ slot: b.slot, zeit: b.zeit, format: b.format, themaId: b.themaId, ...(b.lang != null ? { lang: b.lang } : {}), ...meta(b.themaId), ...(b.format === "wochenrueckblick" ? { titel: "Wochenrückblick", fach: "wochenrueckblick", klausur: 4 } : {}) })),
    stories: tag.plan.stories.map((s) => s.beitragSlot
      ? { slot: s.slot, zeit: s.zeit, art: "teaser", beitragSlot: s.beitragSlot }
      : { slot: s.slot, zeit: s.zeit, art: s.art, themaId: s.themaId, ...meta(s.themaId) }),
  };
  console.log("JP " + JSON.stringify(out));
}
console.log("===== JAHRESPLAN ENDE =====");
