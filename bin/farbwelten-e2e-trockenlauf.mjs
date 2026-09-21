#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

import { THEMEN } from "../daten/themen.mjs";
import { beitragSchreiben, entwurfsspeicher } from "../src/autor.mjs";
import { titelbild } from "../src/bilder.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { budgetStarten } from "../src/budget.mjs";
import { kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import { budgetSetzen, abschluss as kostenAbschluss } from "../src/kosten.mjs";
import { telemetrieStarten } from "../src/telemetrie.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "farbwelten-e2e");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });
entwurfsspeicher(path.join(out, "entwuerfe"));

const datum = "2026-09-21";

function strategieLaden() {
  try {
    return JSON.parse(execFileSync(
      "git", ["show", "origin/instagram-assets:state/strategie.json"],
      { cwd: root, encoding: "utf8" },
    ));
  } catch {
    return {};
  }
}
const strategie = strategieLaden();

function themaNormalisieren(thema) {
  const t = structuredClone(thema || {});
  t.prioritaet ||= "mittel";
  t.normen = Array.isArray(t.normen) ? t.normen : [];
  t.kern = (t.kern && typeof t.kern === "object") ? t.kern : {};
  return t;
}

function themaFinden({ fach, muster, name, fallbackTitel }) {
  const kandidaten = THEMEN.filter((t) => t?.fach === fach);
  const thema = kandidaten.find((t) => muster.test(String(t?.titel || "")));
  if (thema) return themaNormalisieren(thema);
  /* Einige publizierte Titel sind bereits die redaktionelle Verpackung eines
     breiteren Pool-Themas. Fuer den E2E-Kostentest darf der konkrete Titel
     trotzdem als Themen-Skelett laufen; Faktencheck und Wissensbasis bleiben
     identisch zum Produktionspfad. */
  if (fallbackTitel) return themaNormalisieren({
    id: `dryrun-${fach}`,
    fach,
    titel: fallbackTitel,
    prioritaet: "mittel",
    normen: [],
    kern: {},
  });
  const verfuegbar = kandidaten.slice(0, 50).map((t) => t.titel).join(" | ");
  throw new Error(`Thema fuer ${name} nicht gefunden. Kandidaten in ${fach}: ${verfuegbar}`);
}

const faelle = [
  {
    key: "01-bgb-at", name: "BGB AT", fach: "bgbat", format: "vergleich",
    muster: /Eigenschaftsirrtum|Motivirrtum/i,
    fallbackTitel: "Eigenschaftsirrtum ist kein Motivirrtum – merk dir die Ausnahme",
    farbe: { grund: "#8AF0A6", dunkel: "#0A2B1C" },
  },
  {
    key: "02-schuldrecht", name: "Schuldrecht", fach: "schuld", format: "schema",
    muster: /Schadensersatzanspruch.*Leistung|Leistungsstörung|280/i,
    fallbackTitel: "§ 280 I BGB: das Grundschema",
    farbe: { grund: "#6DBEFD", dunkel: "#092653" },
  },
  {
    key: "03-sachenrecht", name: "Sachenrecht", fach: "sachen", format: "pruefungsfrage",
    muster: /Herausgabe.*Besitzer|985 BGB|Eigentümer.*Besitzer/i,
    fallbackTitel: "Welche Norm gibt dem Eigentümer den Anspruch auf Herausgabe gegen den Besitzer?",
    farbe: { grund: "#E8D0A0", dunkel: "#372B11" },
  },
  {
    key: "04-nebenfaecher", name: "Zivilrechtliche Nebenfaecher", fach: "arbeit", format: "spickzettel",
    muster: /betriebsbedingte Kündigung/i,
    fallbackTitel: "Wie prüfst du die betriebsbedingte Kündigung?",
    farbe: { grund: "#15DDDB", dunkel: "#052234" },
  },
  {
    key: "05-zpo", name: "ZPO / Vollstreckung / Assessor ZR", fach: "zpo", format: "schema",
    muster: /Vollstreckungsklausel|Klauselrechtsbehelfe|Voraussetzungen der Zwangsvollstreckung/i,
    fallbackTitel: "Vollstreckungsklausel und Klauselrechtsbehelfe",
    farbe: { grund: "#388FEA", dunkel: "#081941" },
  },
  {
    key: "06-straf-at", name: "Strafrecht AT", fach: "strafat", format: "pruefungsfrage",
    muster: /unmittelbare.*Ansetzen.*Versuch|Versuch.*unmittelbar|Wann beginnt der Versuch/i,
    fallbackTitel: "Wann beginnt der Versuch?",
    farbe: { grund: "#D97371", dunkel: "#461214" },
  },
  {
    key: "07-straf-bt", name: "Strafrecht BT / StPO / Assessor Strafrecht", fach: "strafbt", format: "klausurtechnik",
    muster: /142 StGB|unerlaubte.*Unfallort|Entfernen vom Unfallort/i,
    fallbackTitel: "§ 142 StGB richtig aufbauen",
    farbe: { grund: "#FB902F", dunkel: "#351A0A" },
  },
  {
    key: "08-oeffentliches-recht", name: "Oeffentliches Recht", fach: "vwgo", format: "pruefungsfrage",
    muster: /aufschiebende Wirkung|80 VwGO/i,
    fallbackTitel: "Aufschiebende Wirkung nach § 80 VwGO",
    farbe: { grund: "#E41D78", dunkel: "#330122" },
  },
  {
    key: "09-methodik", name: "Methodik & Mindset", fach: "methodik", format: "schema",
    muster: /Streitstände/i,
    fallbackTitel: "Streitstände nur dort, wo sie entscheidungserheblich sind",
    farbe: { grund: "#36E6B2", dunkel: "#11183A" },
  },
];

const wochenfall = {
  key: "10-wochenrueckblick",
  name: "Fachuebergreifender Wochenrueckblick",
  fach: "wochenrueckblick",
  format: "wochenrueckblick",
  farbe: { grund: "#F1EBDD", dunkel: "#171717" },
  wochenThemen: [
    "Eigenschaftsirrtum und Motivirrtum",
    "§ 280 I BGB: Grundschema",
    "§ 985 BGB",
    "betriebsbedingte Kündigung",
    "Vollstreckungsklausel und Klauselrechtsbehelfe",
    "Versuchsbeginn",
    "§ 80 VwGO: aufschiebende Wirkung",
  ],
};

const budget = budgetStarten({
  deckel: { core: 5, engagement: 1, research: 1 },
  bisher: { core: 0, engagement: 0, research: 0 },
  protokoll: (zeile) => console.log(`[budget] ${zeile}`),
});
budgetSetzen({ limitUsd: 5, antwortLimitUsd: 1, bisher: 0, bisherAntworten: 0 });

const telemetrie = telemetrieStarten({
  datum,
  kanal: "herrjurist-farbwelten-e2e",
  dir: out,
  breakGlass: false,
  providerGuardUsd: null,
});
kontextSetzen({
  budget,
  telemetrie,
  journal: null,
  kanal: "herrjurist-farbwelten-e2e",
  datum,
});

function summe(rows, feld) {
  return rows.reduce((a, r) => a + (Number(r?.[feld]) || 0), 0);
}
function usage(rows) {
  const byProvider = {};
  const byPurpose = {};
  for (const r of rows) {
    const p = r.provider || "unbekannt";
    const z = r.purpose || "unbekannt";
    const add = (o, k) => {
      o[k] ||= { aufrufe: 0, usd: 0, inputTokens: 0, outputTokens: 0, cacheReadTokens: 0, cacheWriteTokens: 0 };
      o[k].aufrufe++;
      o[k].usd += Number(r.actualUsd ?? r.usd ?? 0) || 0;
      o[k].inputTokens += Number(r.inputTokens || 0);
      o[k].outputTokens += Number(r.outputTokens || 0);
      o[k].cacheReadTokens += Number(r.cacheReadTokens || 0);
      o[k].cacheWriteTokens += Number(r.cacheWriteTokens || 0);
    };
    add(byProvider, p); add(byPurpose, z);
  }
  for (const gruppe of [byProvider, byPurpose]) {
    for (const v of Object.values(gruppe)) v.usd = Number(v.usd.toFixed(6));
  }
  return {
    aufrufe: rows.length,
    usd: Number(summe(rows, "actualUsd").toFixed(6)),
    inputTokens: summe(rows, "inputTokens"),
    outputTokens: summe(rows, "outputTokens"),
    cacheReadTokens: summe(rows, "cacheReadTokens"),
    cacheWriteTokens: summe(rows, "cacheWriteTokens"),
    byProvider, byPurpose,
  };
}

async function erzeugen(fall, nr) {
  const start = telemetrie.anzahl();
  const thema = fall.fach === "wochenrueckblick" ? null : themaFinden(fall);
  const beitrag = await beitragSchreiben({
    format: fall.format,
    thema,
    datum,
    recherche: null,
    wochenThemen: fall.wochenThemen || null,
    anlass: null,
    strategie,
  });
  beitrag.slug = `farbtest-${String(nr).padStart(2, "0")}-${fall.fach}`;

  const titelfolie = beitrag.folien?.find((x) => x.art === "titel");
  if (!titelfolie) throw new Error(`${fall.name}: keine Titelfolie`);

  const motiv = await titelbild(beitrag, null, {
    randFarbe: null,
    zweck: "bild",
    slot: `farbtest-${nr}`,
  });
  if (!motiv) throw new Error(`${fall.name}: kein Charakterbild erzeugt`);
  titelfolie.bild = motiv.bild;
  titelfolie.bildQuelle = motiv.quelle;
  titelfolie.bildFrei = motiv.frei !== false;
  titelfolie.bildBreite = motiv.breite || null;
  titelfolie.bildHoehe = motiv.hoehe || null;
  titelfolie.bildTyp = motiv.typ || "charakter";
  titelfolie.bildCharaktere = motiv.charaktere || null;
  titelfolie.bildPrompt = motiv.prompt || null;
  titelfolie.bildKostenUsd = motiv.kostenUsd ?? null;

  const fallOut = path.join(out, fall.key);
  fs.mkdirSync(fallOut, { recursive: true });
  const bilder = await beitragRendern(beitrag, fallOut, { variante: 0 });
  const cover = bilder[0] || null;

  fs.writeFileSync(path.join(fallOut, "beitrag.json"), JSON.stringify(beitrag, null, 2));

  const rows = telemetrie.zeilen().slice(start);
  return {
    nr,
    key: fall.key,
    gruppe: fall.name,
    fach: beitrag.fach,
    format: fall.format,
    themaId: thema?.id || null,
    themaTitel: thema?.titel || "Wochenrueckblick aus sieben Themen",
    hook: titelfolie.titel,
    titelZeilen: titelfolie.titelZeilen || null,
    coverText: beitrag.coverText || titelfolie.coverText || null,
    charaktere: motiv.charaktere || [],
    bildKostenUsd: motiv.kostenUsd ?? null,
    farbe: fall.farbe,
    cover: cover ? path.relative(out, cover) : null,
    slides: bilder.map((p) => path.relative(out, p)),
    usage: usage(rows),
  };
}

const manifest = [];
const alleFaelle = [...faelle, wochenfall];
const nurKey = String(process.env.IG_FARBTEST_ONLY || "").trim();
const auswahl = nurKey ? alleFaelle.filter((f) => f.key === nurKey) : alleFaelle;
if (nurKey && !auswahl.length) throw new Error(`IG_FARBTEST_ONLY unbekannt: ${nurKey}`);
try {
  for (const fall of auswahl) {
    const nr = alleFaelle.indexOf(fall) + 1;
    console.log(`\n=== ${nr}/10 · ${fall.name} ===`);
    try {
      const result = await erzeugen(fall, nr);
      manifest.push({ ok: true, ...result });
      console.log(`OK · ${result.hook} · ${result.usage.usd.toFixed(4)} #!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

import { THEMEN } from "../daten/themen.mjs";
import { beitragSchreiben, entwurfsspeicher } from "../src/autor.mjs";
import { titelbild } from "../src/bilder.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { budgetStarten } from "../src/budget.mjs";
import { kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import { budgetSetzen, abschluss as kostenAbschluss } from "../src/kosten.mjs";
import { telemetrieStarten } from "../src/telemetrie.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "farbwelten-e2e");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });
entwurfsspeicher(path.join(out, "entwuerfe"));

const datum = "2026-09-21";

function strategieLaden() {
  try {
    return JSON.parse(execFileSync(
      "git", ["show", "origin/instagram-assets:state/strategie.json"],
      { cwd: root, encoding: "utf8" },
    ));
  } catch {
    return {};
  }
}
const strategie = strategieLaden();

function themaNormalisieren(thema) {
  const t = structuredClone(thema || {});
  t.prioritaet ||= "mittel";
  t.normen = Array.isArray(t.normen) ? t.normen : [];
  t.kern = (t.kern && typeof t.kern === "object") ? t.kern : {};
  return t;
}

function themaFinden({ fach, muster, name, fallbackTitel }) {
  const kandidaten = THEMEN.filter((t) => t?.fach === fach);
  const thema = kandidaten.find((t) => muster.test(String(t?.titel || "")));
  if (thema) return themaNormalisieren(thema);
  /* Einige publizierte Titel sind bereits die redaktionelle Verpackung eines
     breiteren Pool-Themas. Fuer den E2E-Kostentest darf der konkrete Titel
     trotzdem als Themen-Skelett laufen; Faktencheck und Wissensbasis bleiben
     identisch zum Produktionspfad. */
  if (fallbackTitel) return themaNormalisieren({
    id: `dryrun-${fach}`,
    fach,
    titel: fallbackTitel,
    prioritaet: "mittel",
    normen: [],
    kern: {},
  });
  const verfuegbar = kandidaten.slice(0, 50).map((t) => t.titel).join(" | ");
  throw new Error(`Thema fuer ${name} nicht gefunden. Kandidaten in ${fach}: ${verfuegbar}`);
}

const faelle = [
  {
    key: "01-bgb-at", name: "BGB AT", fach: "bgbat", format: "vergleich",
    muster: /Eigenschaftsirrtum|Motivirrtum/i,
    fallbackTitel: "Eigenschaftsirrtum ist kein Motivirrtum – merk dir die Ausnahme",
    farbe: { grund: "#8AF0A6", dunkel: "#0A2B1C" },
  },
  {
    key: "02-schuldrecht", name: "Schuldrecht", fach: "schuld", format: "schema",
    muster: /Schadensersatzanspruch.*Leistung|Leistungsstörung|280/i,
    fallbackTitel: "§ 280 I BGB: das Grundschema",
    farbe: { grund: "#6DBEFD", dunkel: "#092653" },
  },
  {
    key: "03-sachenrecht", name: "Sachenrecht", fach: "sachen", format: "pruefungsfrage",
    muster: /Herausgabe.*Besitzer|985 BGB|Eigentümer.*Besitzer/i,
    fallbackTitel: "Welche Norm gibt dem Eigentümer den Anspruch auf Herausgabe gegen den Besitzer?",
    farbe: { grund: "#E8D0A0", dunkel: "#372B11" },
  },
  {
    key: "04-nebenfaecher", name: "Zivilrechtliche Nebenfaecher", fach: "arbeit", format: "spickzettel",
    muster: /betriebsbedingte Kündigung/i,
    fallbackTitel: "Wie prüfst du die betriebsbedingte Kündigung?",
    farbe: { grund: "#15DDDB", dunkel: "#052234" },
  },
  {
    key: "05-zpo", name: "ZPO / Vollstreckung / Assessor ZR", fach: "zpo", format: "schema",
    muster: /Vollstreckungsklausel|Klauselrechtsbehelfe|Voraussetzungen der Zwangsvollstreckung/i,
    fallbackTitel: "Vollstreckungsklausel und Klauselrechtsbehelfe",
    farbe: { grund: "#388FEA", dunkel: "#081941" },
  },
  {
    key: "06-straf-at", name: "Strafrecht AT", fach: "strafat", format: "pruefungsfrage",
    muster: /unmittelbare.*Ansetzen.*Versuch|Versuch.*unmittelbar|Wann beginnt der Versuch/i,
    fallbackTitel: "Wann beginnt der Versuch?",
    farbe: { grund: "#D97371", dunkel: "#461214" },
  },
  {
    key: "07-straf-bt", name: "Strafrecht BT / StPO / Assessor Strafrecht", fach: "strafbt", format: "klausurtechnik",
    muster: /142 StGB|unerlaubte.*Unfallort|Entfernen vom Unfallort/i,
    fallbackTitel: "§ 142 StGB richtig aufbauen",
    farbe: { grund: "#FB902F", dunkel: "#351A0A" },
  },
  {
    key: "08-oeffentliches-recht", name: "Oeffentliches Recht", fach: "vwgo", format: "pruefungsfrage",
    muster: /aufschiebende Wirkung|80 VwGO/i,
    fallbackTitel: "Aufschiebende Wirkung nach § 80 VwGO",
    farbe: { grund: "#E41D78", dunkel: "#330122" },
  },
  {
    key: "09-methodik", name: "Methodik & Mindset", fach: "methodik", format: "schema",
    muster: /Streitstände/i,
    fallbackTitel: "Streitstände nur dort, wo sie entscheidungserheblich sind",
    farbe: { grund: "#36E6B2", dunkel: "#11183A" },
  },
];

const wochenfall = {
  key: "10-wochenrueckblick",
  name: "Fachuebergreifender Wochenrueckblick",
  fach: "wochenrueckblick",
  format: "wochenrueckblick",
  farbe: { grund: "#F1EBDD", dunkel: "#171717" },
  wochenThemen: [
    "Eigenschaftsirrtum und Motivirrtum",
    "§ 280 I BGB: Grundschema",
    "§ 985 BGB",
    "betriebsbedingte Kündigung",
    "Vollstreckungsklausel und Klauselrechtsbehelfe",
    "Versuchsbeginn",
    "§ 80 VwGO: aufschiebende Wirkung",
  ],
};

const budget = budgetStarten({
  deckel: { core: 5, engagement: 1, research: 1 },
  bisher: { core: 0, engagement: 0, research: 0 },
  protokoll: (zeile) => console.log(`[budget] ${zeile}`),
});
budgetSetzen({ limitUsd: 5, antwortLimitUsd: 1, bisher: 0, bisherAntworten: 0 });

const telemetrie = telemetrieStarten({
  datum,
  kanal: "herrjurist-farbwelten-e2e",
  dir: out,
  breakGlass: false,
  providerGuardUsd: null,
});
kontextSetzen({
  budget,
  telemetrie,
  journal: null,
  kanal: "herrjurist-farbwelten-e2e",
  datum,
});

function summe(rows, feld) {
  return rows.reduce((a, r) => a + (Number(r?.[feld]) || 0), 0);
}
function usage(rows) {
  const byProvider = {};
  const byPurpose = {};
  for (const r of rows) {
    const p = r.provider || "unbekannt";
    const z = r.purpose || "unbekannt";
    const add = (o, k) => {
      o[k] ||= { aufrufe: 0, usd: 0, inputTokens: 0, outputTokens: 0, cacheReadTokens: 0, cacheWriteTokens: 0 };
      o[k].aufrufe++;
      o[k].usd += Number(r.actualUsd ?? r.usd ?? 0) || 0;
      o[k].inputTokens += Number(r.inputTokens || 0);
      o[k].outputTokens += Number(r.outputTokens || 0);
      o[k].cacheReadTokens += Number(r.cacheReadTokens || 0);
      o[k].cacheWriteTokens += Number(r.cacheWriteTokens || 0);
    };
    add(byProvider, p); add(byPurpose, z);
  }
  for (const gruppe of [byProvider, byPurpose]) {
    for (const v of Object.values(gruppe)) v.usd = Number(v.usd.toFixed(6));
  }
  return {
    aufrufe: rows.length,
    usd: Number(summe(rows, "actualUsd").toFixed(6)),
    inputTokens: summe(rows, "inputTokens"),
    outputTokens: summe(rows, "outputTokens"),
    cacheReadTokens: summe(rows, "cacheReadTokens"),
    cacheWriteTokens: summe(rows, "cacheWriteTokens"),
    byProvider, byPurpose,
  };
}

async function erzeugen(fall, nr) {
  const start = telemetrie.anzahl();
  const thema = fall.fach === "wochenrueckblick" ? null : themaFinden(fall);
  const beitrag = await beitragSchreiben({
    format: fall.format,
    thema,
    datum,
    recherche: null,
    wochenThemen: fall.wochenThemen || null,
    anlass: null,
    strategie,
  });
  beitrag.slug = `farbtest-${String(nr).padStart(2, "0")}-${fall.fach}`;

  const titelfolie = beitrag.folien?.find((x) => x.art === "titel");
  if (!titelfolie) throw new Error(`${fall.name}: keine Titelfolie`);

  const motiv = await titelbild(beitrag, null, {
    randFarbe: null,
    zweck: "bild",
    slot: `farbtest-${nr}`,
  });
  if (!motiv) throw new Error(`${fall.name}: kein Charakterbild erzeugt`);
  titelfolie.bild = motiv.bild;
  titelfolie.bildQuelle = motiv.quelle;
  titelfolie.bildFrei = motiv.frei !== false;
  titelfolie.bildBreite = motiv.breite || null;
  titelfolie.bildHoehe = motiv.hoehe || null;
  titelfolie.bildTyp = motiv.typ || "charakter";
  titelfolie.bildCharaktere = motiv.charaktere || null;
  titelfolie.bildPrompt = motiv.prompt || null;
  titelfolie.bildKostenUsd = motiv.kostenUsd ?? null;

  const fallOut = path.join(out, fall.key);
  fs.mkdirSync(fallOut, { recursive: true });
  const bilder = await beitragRendern(beitrag, fallOut, { variante: 0 });
  const cover = bilder[0] || null;

  fs.writeFileSync(path.join(fallOut, "beitrag.json"), JSON.stringify(beitrag, null, 2));

  const rows = telemetrie.zeilen().slice(start);
  return {
    nr,
    key: fall.key,
    gruppe: fall.name,
    fach: beitrag.fach,
    format: fall.format,
    themaId: thema?.id || null,
    themaTitel: thema?.titel || "Wochenrueckblick aus sieben Themen",
    hook: titelfolie.titel,
    titelZeilen: titelfolie.titelZeilen || null,
    coverText: beitrag.coverText || titelfolie.coverText || null,
    charaktere: motiv.charaktere || [],
    bildKostenUsd: motiv.kostenUsd ?? null,
    farbe: fall.farbe,
    cover: cover ? path.relative(out, cover) : null,
    slides: bilder.map((p) => path.relative(out, p)),
    usage: usage(rows),
  };
}

);
    } catch (e) {
      manifest.push({ ok: false, nr, key: fall.key, gruppe: fall.name, fehler: e?.stack || String(e) });
      console.error(`FEHLER · ${fall.name}: ${e.message}`);
    }
  }
} finally {
  await browserBeenden().catch(() => {});
  kontextLoeschen();
}

const rows = telemetrie.zeilen();
const gesamt = usage(rows);
const kosten = kostenAbschluss();
const ergebnis = {
  erzeugt: new Date().toISOString(),
  modus: "echter Provider-Trockenlauf ohne Instagram-Publishing",
  branch: process.env.GITHUB_REF_NAME || null,
  commit: process.env.GITHUB_SHA || null,
  erfolgreich: manifest.filter((x) => x.ok).length,
  gesamtFaelle: manifest.length,
  nurKey: nurKey || null,
  manifest,
  telemetry: gesamt,
  legacyKosten: kosten,
};
fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(ergebnis, null, 2));
console.log("\n=== GESAMT ===");
console.log(JSON.stringify({
  erfolgreich: ergebnis.erfolgreich,
  gesamt: ergebnis.gesamtFaelle,
  usd: gesamt.usd,
  inputTokens: gesamt.inputTokens,
  outputTokens: gesamt.outputTokens,
  cacheReadTokens: gesamt.cacheReadTokens,
  byProvider: gesamt.byProvider,
}, null, 2));
if (ergebnis.erfolgreich !== ergebnis.gesamtFaelle) process.exitCode = 2;
