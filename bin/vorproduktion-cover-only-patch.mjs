#!/usr/bin/env node
/**
 * Rendert die sichtbaren Cover bereits vorhandener Vorproduktion neu.
 * Verknuepfte Story-Teaser werden aus dem fertigen Cover mitgezogen; keine
 * Videos, Sprach- oder Bildprovider.
 *
 * Gedacht fuer reine Layout-Aenderungen: Fachband/Titel/Badge/Freisteller
 * koennen damit in Sekunden statt ueber einen kompletten Mehrtages-Render
 * aktualisiert werden.
 */
import fs from "node:fs";
import path from "node:path";

import { Hosting } from "../src/hosting.mjs";
import { browserBeenden, coverRendern, htmlZuJpeg, kontext, storyRendern } from "../src/render.mjs";
import { coverDaten } from "../src/reel.mjs";
import { folieHtml, MASSE } from "../src/vorlagen.mjs";

function coverPfad(hosting, datum, slot, reel) {
  const dir = path.join(hosting.dir, "vorproduktion", datum, "fertig", slot);
  fs.mkdirSync(dir, { recursive: true });
  return path.join(dir, reel ? `${datum}-${slot}-cover.jpg` : `${datum}-${slot}-01.jpg`);
}

async function teaserAktualisieren(hosting, tag, datum, beitragSlot, beitrag, coverPfad) {
  const ziele = (tag.plan?.stories || []).filter((s) => s.art === "teaser" && s.beitragSlot === beitragSlot && s.slot);
  if (!ziele.length) return;
  const titel = beitrag.kurztitel || beitrag.folien?.[0]?.titel || beitrag.szenen?.[0]?.titel || "Neuer Beitrag";
  const coverBild = `data:image/jpeg;base64,${fs.readFileSync(coverPfad).toString("base64")}`;
  const storyDir = path.join(hosting.dir, "vorproduktion", datum, "fertig", "stories");
  fs.mkdirSync(storyDir, { recursive: true });
  for (const p of ziele) {
    await storyRendern({
      slot: p.slot, art: "teaser", beitragSlot,
      fach: beitrag.fach, klausur: beitrag.klausur, fachLabel: beitrag.fachLabel,
      ueberzeile: "Neuer Beitrag", titel, pille: "Jetzt im Feed", coverBild,
    }, path.join(storyDir, `${p.slot}-teaser.jpg`), { variante: 0 });
  }
}

function ohneBild(obj) {
  obj.coverBildAuslassen = true;
  obj.bild = null;
  obj.bildQuelle = null;
  obj.bildCharaktere = [];
  return obj;
}

export async function coverOnlyPatchen({ tage = [], slots = ["b1", "b2", "b3"] } = {}) {
  const hosting = new Hosting({ pushen: true }).vorbereiten();
  const manifest = {
    version: 1,
    erzeugtAm: new Date().toISOString(),
    modus: "cover-only-providerfrei",
    providerKostenUsd: 0,
    tage: [],
  };

  try {
    for (const datum of tage) {
      const tagPfad = path.join(hosting.dir, "vorproduktion", `${datum}.json`);
      if (!fs.existsSync(tagPfad)) throw new Error(`Vorproduktion fehlt: ${datum}`);
      const tag = JSON.parse(fs.readFileSync(tagPfad, "utf8"));
      const mTag = { datum, cover: [] };

      for (const slot of slots) {
        const beitrag = structuredClone(tag.inhalte?.[slot]);
        if (!beitrag) throw new Error(`${datum} ${slot}: Beitrag fehlt`);

        if (Array.isArray(beitrag.folien)) {
          const titel = ohneBild(beitrag.folien.find((f) => f.art === "titel") || beitrag.folien[0]);
          const ctx = kontext({
            fach: beitrag.fach,
            klausur: beitrag.klausur,
            fachLabel: beitrag.fachLabel,
            variante: beitrag.variante,
          });
          const ziel = coverPfad(hosting, datum, slot, false);
          await htmlZuJpeg(folieHtml(titel, ctx, 1, beitrag.folien.length), MASSE.beitrag, ziel);
          await teaserAktualisieren(hosting, tag, datum, slot, beitrag, ziel);
          mTag.cover.push({ slot, format: beitrag.format || "carousel", datei: path.basename(ziel) });
          continue;
        }

        if (Array.isArray(beitrag.szenen)) {
          ohneBild(beitrag);
          const ziel = coverPfad(hosting, datum, slot, true);
          await coverRendern(coverDaten(beitrag, { gesamt: 60 }), ziel);
          await teaserAktualisieren(hosting, tag, datum, slot, beitrag, ziel);
          mTag.cover.push({ slot, format: "reel", datei: path.basename(ziel) });
          continue;
        }

        throw new Error(`${datum} ${slot}: unbekanntes Beitragsformat`);
      }

      manifest.tage.push(mTag);
    }

    fs.writeFileSync(
      path.join(hosting.dir, "vorproduktion", "cover-only-patch-manifest.json"),
      JSON.stringify(manifest, null, 2) + "\n",
    );
    hosting.commit(`Rendere Cover-only ${tage.join(" + ")} providerfrei`);
    await hosting.push();
    return manifest;
  } finally {
    await browserBeenden().catch(() => {});
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const tage = process.argv.slice(2).filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x));
  if (!tage.length) throw new Error("Mindestens ein Datum YYYY-MM-DD ist erforderlich.");
  const manifest = await coverOnlyPatchen({ tage });
  console.log(JSON.stringify({ ok: true, ...manifest }, null, 2));
}
