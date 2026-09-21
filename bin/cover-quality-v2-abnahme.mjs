#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { charakterMotivZeichnen, charaktereFuer } from "../src/charakterbild.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { reelBauen } from "../src/reel.mjs";
import { budgetStarten } from "../src/budget.mjs";
import { kontextSetzen, kontextLoeschen } from "../src/anbieter.mjs";
import { budgetSetzen } from "../src/kosten.mjs";
import { CONFIG } from "../src/config.mjs";
import { ffmpegPfad } from "../src/stimme.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "cover-quality-v2");
const coversDir = path.join(out, "covers");
const reelDir = path.join(out, "reel");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(coversDir, { recursive: true });
fs.mkdirSync(reelDir, { recursive: true });

const faelle = [
  {
    nr: 1, fach: "bgbat", klausur: 1, fachLabel: "BGB AT",
    thema: "Eigenschaftsirrtum ist kein Motivirrtum – merk dir die Ausnahme",
    titelZeilen: ["Eigenschaftsirrtum", "ist kein Motivirrtum", "Merk dir", "die Ausnahme"],
    coverText: "§ 119 II ist die Ausnahme", icon: "vertrag",
    bildSzene: "mistaken quality token separated from motive cloud",
    erwartet: ["form7", "rex"],
  },
  {
    nr: 2, fach: "schuld", klausur: 1, fachLabel: "Schuldrecht",
    thema: "§ 280 I BGB: das Grundschema",
    titelZeilen: ["§ 280 I BGB:", "das Grundschema"],
    coverText: "Vier Punkte in Reihenfolge", icon: "dokument",
    bildSzene: "broken obligation circuit traced through four checkpoints",
    erwartet: ["rex", "flux"],
  },
  {
    nr: 3, fach: "sachen", klausur: 1, fachLabel: "Sachenrecht",
    thema: "Welche Norm gibt dem Eigentümer den Anspruch auf Herausgabe gegen den Besitzer?",
    titelZeilen: ["Welche Norm gibt", "dem Eigentümer", "Herausgabe gegen", "den Besitzer?"],
    coverText: "Anspruch aus § 985 BGB", icon: "schluessel",
    bildSzene: "heavy property crate transferred from possessor side",
    erwartet: ["brakk", "form7"],
  },
  {
    nr: 4, fach: "arbeit", klausur: 1, fachLabel: "Arbeitsrecht",
    thema: "Wie prüfst du die betriebsbedingte Kündigung?",
    titelZeilen: ["Wie prüfst du", "die betriebsbedingte", "Kündigung?"],
    coverText: "KSchG in drei Stufen", icon: "dokument",
    bildSzene: "employment file passes three decision gates",
    erwartet: ["zylla", "flux"],
  },
  {
    nr: 5, fach: "zpo", klausur: 1, fachLabel: "ZPO / Vollstreckung",
    thema: "Vollstreckungsklausel und Klauselrechtsbehelfe",
    titelZeilen: ["Vollstreckungsklausel", "und Klauselrechtsbehelfe"],
    coverText: "Titel → Klausel → Rechtsbehelf", icon: "schriftrolle",
    bildSzene: "sealed enforcement document routed through remedy gate",
    erwartet: ["form7", "flux"],
  },
  {
    nr: 6, fach: "strafat", klausur: 2, fachLabel: "Strafrecht AT",
    thema: "Wann beginnt der Versuch?",
    titelZeilen: ["Wann beginnt", "der Versuch?"],
    coverText: "§ 22 StGB ist die Schwelle", icon: "blitz",
    bildSzene: "hand stops at threshold before irreversible action",
    erwartet: ["rex", "mara"],
  },
  {
    nr: 7, fach: "strafbt", klausur: 2, fachLabel: "Strafrecht BT",
    thema: "§ 142 StGB richtig aufbauen",
    titelZeilen: ["§ 142 StGB", "richtig aufbauen"],
    coverText: "Unfallort zuerst definieren", icon: "auto",
    bildSzene: "damaged vehicle beside glowing accident boundary",
    erwartet: ["rex", "mara"],
  },
  {
    nr: 8, fach: "vwgo", klausur: 3, fachLabel: "Öffentliches Recht",
    thema: "Aufschiebende Wirkung nach § 80 VwGO",
    titelZeilen: ["Aufschiebende Wirkung", "nach § 80 VwGO"],
    coverText: "Erst § 80 I, dann Ausnahmen", icon: "stopp",
    bildSzene: "administrative order paused behind procedural barrier",
    erwartet: ["mara", "form7"],
  },
  {
    nr: 9, fach: "methodik", klausur: 0, fachLabel: "Methodik & Mindset",
    thema: "Streitstände nur dort, wo sie entscheidungserheblich sind",
    titelZeilen: ["Streitstände nur dort,", "wo sie", "entscheidungserheblich sind"],
    coverText: "Nur wenn der Streit trägt", icon: "waage",
    bildSzene: "decision tree keeps only outcome changing dispute",
    erwartet: ["form7", "flux"],
  },
  {
    nr: 10, fach: "wochenrueckblick", klausur: 4, fachLabel: "Wochenrückblick",
    thema: "7 Themen der Woche – wo du beim Wiederholen was übersiehst",
    titelZeilen: ["7 Themen der Woche", "Wo übersiehst du", "beim Wiederholen", "noch etwas?"],
    coverText: "Lücken finden statt abhaken", icon: "kreislauf",
    bildSzene: "weekly review grid reveals one overlooked checkpoint",
    erwartet: ["zylla", "form7"],
  },
];

const events = [];
const telemetrie = {
  aufruf(eintrag) {
    events.push({ zeit: new Date().toISOString(), ...eintrag });
  },
};

const budget = budgetStarten({
  deckel: { core: 8, engagement: 0, research: 0 },
  bisher: { core: 0, engagement: 0, research: 0 },
  protokoll: () => {},
});
budgetSetzen({ limitUsd: 8, antwortLimitUsd: 8 });
kontextSetzen({ budget, telemetrie, journal: null, kanal: "herrjurist-cover-quality-v2", datum: "acceptance" });

const round = (n) => Number(Number(n || 0).toFixed(6));
const sum = (liste, feld) => round(liste.reduce((a, x) => a + (Number.isFinite(Number(x?.[feld])) ? Number(x[feld]) : 0), 0));
const ids = (ziel) => charaktereFuer(ziel).map((x) => x.id);

function usage(liste) {
  return {
    inputTokens: sum(liste, "inputTokens"),
    outputTokens: sum(liste, "outputTokens"),
    cacheReadTokens: sum(liste, "cacheReadTokens"),
    imageInputTokens: sum(liste, "imageInputTokens"),
    textInputTokens: sum(liste, "textInputTokens"),
    imageOutputTokens: sum(liste, "imageOutputTokens"),
  };
}

function telemetryFuer(slot) {
  const liste = events.filter((e) => e.slot === slot);
  const bild = liste.filter((e) => e.purpose === "bild" || e.purpose === "erklaerbild");
  const qa = liste.filter((e) => e.purpose === "bild-qa");
  return {
    imageCostUsd: sum(bild, "actualUsd"),
    visionQaCostUsd: sum(qa, "actualUsd"),
    totalCostUsd: sum(liste, "actualUsd"),
    tokenUsage: usage(liste),
    unknownSpend: liste.some((e) => e.spendUnknown),
    calls: liste,
  };
}

function dateiDaten(pfad) {
  return `data:image/png;base64,${fs.readFileSync(pfad).toString("base64")}`;
}

function motivAufraeumen(motiv) {
  for (const p of new Set([motiv?.pfad, motiv?.ohneRand].filter(Boolean))) fs.rmSync(p, { force: true });
}

function dimensionen(pfad) {
  const raw = execFileSync("ffprobe", [
    "-v", "error", "-select_streams", "v:0",
    "-show_entries", "stream=width,height", "-of", "json", pfad,
  ], { encoding: "utf8" });
  const s = JSON.parse(raw)?.streams?.[0] || {};
  return { width: Number(s.width || 0), height: Number(s.height || 0) };
}

function kontaktbogen(pfade, ziel) {
  const args = ["-y", "-hide_banner", "-loglevel", "error"];
  for (const p of pfade) args.push("-i", p);
  const skalen = pfade.map((_, i) => `[${i}:v]scale=324:432[v${i}]`).join(";");
  const layout = pfade.map((_, i) => `${(i % 5) * 324}_${Math.floor(i / 5) * 432}`).join("|");
  const eingaben = pfade.map((_, i) => `[v${i}]`).join("");
  args.push("-filter_complex", `${skalen};${eingaben}xstack=inputs=${pfade.length}:layout=${layout}[out]`, "-map", "[out]", "-frames:v", "1", "-q:v", "2", ziel);
  execFileSync(ffmpegPfad(), args, { stdio: ["ignore", "pipe", "pipe"] });
}

async function coverAbnahme() {
  const ergebnisse = [];
  const coverPfade = [];
  for (const fall of faelle) {
    const slot = `cover-${String(fall.nr).padStart(2, "0")}`;
    const ziel = {
      format: "carousel",
      fach: fall.fach,
      klausur: fall.klausur,
      fachLabel: fall.fachLabel,
      slug: slot,
      titel: fall.thema,
      kurztitel: fall.thema,
      bildSzene: fall.bildSzene,
      coverText: fall.coverText,
    };
    const gewaehlt = ids(ziel);
    if (JSON.stringify(gewaehlt) !== JSON.stringify(fall.erwartet)) {
      throw new Error(`${slot}: Charakterwahl ${gewaehlt.join("+")} statt ${fall.erwartet.join("+")}`);
    }

    const motiv = await charakterMotivZeichnen(ziel, { zweck: "bild", slot });
    if (!motiv) throw new Error(`${slot}: kein Charakterbild hat beide QA-Stufen bestanden`);
    try {
      const folie = {
        art: "titel",
        titel: fall.thema,
        titelZeilen: fall.titelZeilen,
        icon: fall.icon,
        coverText: fall.coverText,
        bild: dateiDaten(motiv.pfad),
        bildFrei: true,
        bildBreite: motiv.breite || null,
        bildHoehe: motiv.hoehe || null,
        bildTyp: "charakter",
        bildCharaktere: motiv.charaktere,
      };
      const beitrag = {
        format: "schema",
        fach: fall.fach,
        klausur: fall.klausur,
        fachLabel: fall.fachLabel,
        slug: slot,
        folien: [folie],
      };
      const [render] = await beitragRendern(beitrag, coversDir, { variante: 0 });
      const datei = path.join(coversDir, `${slot}.jpg`);
      if (render !== datei) fs.renameSync(render, datei);
      const dim = dimensionen(datei);
      if (dim.width !== 1080 || dim.height !== 1440) throw new Error(`${slot}: falsches Format ${dim.width}x${dim.height}`);
      coverPfade.push(datei);
      const tel = telemetryFuer(slot);
      if (tel.unknownSpend) throw new Error(`${slot}: unbekannter Providerverbrauch in Telemetrie`);
      ergebnisse.push({
        nr: fall.nr,
        testfall: fall.thema,
        hook: fall.thema,
        titelZeilen: fall.titelZeilen,
        coverText: fall.coverText,
        fach: fall.fach,
        charaktere: motiv.charaktere,
        charakterIds: motiv.charakterIds,
        expectedCharacterIds: fall.erwartet,
        quality: motiv.quality,
        attempt: motiv.attempt,
        qaFirstPass: motiv.qaFirstPass,
        qaAttempts: motiv.qaAttempts,
        imageCostUsd: tel.imageCostUsd,
        visionQaCostUsd: tel.visionQaCostUsd,
        totalCostUsd: tel.totalCostUsd,
        tokenUsage: tel.tokenUsage,
        path: path.relative(root, datei),
        dimensions: dim,
      });
    } finally {
      motivAufraeumen(motiv);
    }
  }
  const kontakt = path.join(out, "kontaktbogen-10-cover.jpg");
  kontaktbogen(coverPfade, kontakt);
  return { ergebnisse, kontakt: path.relative(root, kontakt) };
}

async function reelAbnahme() {
  const basisReel = {
    format: "reel",
    fach: "schuld",
    klausur: 1,
    fachLabel: "Schuldrecht",
    slug: "reel-280-abnahme",
    kurztitel: "§ 280 I BGB: vier Schritte",
    coverText: "Vier Punkte in Reihenfolge",
    caption: "Abnahmereel ohne Veröffentlichung.",
    hashtags: [],
    szenen: [
      { art: "hook", titel: "§ 280 I BGB", text: "Wo beginnst du?", marken: ["Vier *Schritte*"], sprecher: "Paragraf 280 Absatz 1 BGB hat vier Kernpunkte. Wir gehen sie in Reihenfolge durch.", bildSzene: "broken obligation circuit before four checkpoints", icon: "dokument" },
      { art: "schritt", nummer: 1, titel: "Schuldverhältnis", text: "Erst die Verbindung.", marken: ["*Schuldverhältnis* zuerst"], sprecher: "Erstens brauchst du ein Schuldverhältnis.", bildSzene: "contract link locked into first checkpoint", icon: "vertrag" },
      { art: "schritt", nummer: 2, titel: "Pflichtverletzung", text: "Dann die verletzte Pflicht.", marken: ["*Pflichtverletzung* prüfen"], sprecher: "Zweitens prüfst du die Pflichtverletzung.", bildSzene: "damaged duty circuit at second checkpoint", icon: "blitz" },
      { art: "merke", titel: "Vertretenmüssen + Schaden", text: "Danach Zurechnung und Schaden.", marken: ["*Vertretenmüssen*", "danach *Schaden*"], sprecher: "Danach folgen Vertretenmüssen und ein ersatzfähiger Schaden. Der Text bleibt im Renderer, nicht im Bildmodell.", bildSzene: "causation chain reaches final damage marker", icon: "warnung" },
    ],
  };
  const reelQa = [];
  for (let i = 0; i < basisReel.szenen.length; i++) {
    const slot = `reel-szene-${String(i + 1).padStart(2, "0")}`;
    const s = basisReel.szenen[i];
    const ziel = { ...basisReel, ...s, format: "reel-szene", slug: slot };
    const gewaehlt = ids(ziel);
    const erwartet = ["rex", "flux"];
    if (JSON.stringify(gewaehlt) !== JSON.stringify(erwartet)) throw new Error(`${slot}: Charakterwahl ${gewaehlt.join("+")} statt rex+flux`);
    const motiv = await charakterMotivZeichnen(ziel, { zweck: "erklaerbild", slot });
    if (!motiv) throw new Error(`${slot}: kein Reel-Charakterbild hat beide QA-Stufen bestanden`);
    try {
      s.bild = dateiDaten(motiv.pfad);
      s.bildFrei = true;
      s.bildTyp = "charakter";
      s.bildCharaktere = motiv.charaktere;
      const tel = telemetryFuer(slot);
      if (tel.unknownSpend) throw new Error(`${slot}: unbekannter Providerverbrauch in Telemetrie`);
      reelQa.push({
        scene: i + 1,
        title: s.titel,
        charaktere: motiv.charaktere,
        charakterIds: motiv.charakterIds,
        quality: motiv.quality,
        attempt: motiv.attempt,
        qaFirstPass: motiv.qaFirstPass,
        qaAttempts: motiv.qaAttempts,
        imageCostUsd: tel.imageCostUsd,
        visionQaCostUsd: tel.visionQaCostUsd,
        totalCostUsd: tel.totalCostUsd,
        tokenUsage: tel.tokenUsage,
      });
    } finally {
      motivAufraeumen(motiv);
    }
  }

  basisReel.bild = basisReel.szenen[0].bild;
  basisReel.bildFrei = true;
  basisReel.bildTyp = "charakter";
  basisReel.bildCharaktere = basisReel.szenen[0].bildCharaktere;
  const gebaut = await reelBauen(basisReel, reelDir, {
    datum: "2026-09-21",
    layout: "erklaer",
    clip: null,
    framesBehalten: false,
  });
  if (!fs.existsSync(gebaut.video) || !fs.existsSync(gebaut.cover)) throw new Error("Reel-Ausgabe fehlt");
  const videoDim = dimensionen(gebaut.video);
  const coverDim = dimensionen(gebaut.cover);
  if (videoDim.width !== 1080 || videoDim.height !== 1920) throw new Error(`Reel: falsches Videoformat ${videoDim.width}x${videoDim.height}`);
  return {
    video: path.relative(root, gebaut.video),
    cover: path.relative(root, gebaut.cover),
    dimensions: videoDim,
    coverDimensions: coverDim,
    durationSeconds: round(gebaut.dauer),
    layout: gebaut.layout,
    voiceProvider: gebaut.anbieter,
    voiceReal: gebaut.echt,
    textOutsideAiImage: true,
    scenes: reelQa,
    totalCostUsd: round(reelQa.reduce((a, x) => a + x.totalCostUsd, 0)),
  };
}

let status = "ok";
let fehler = null;
try {
  const cover = await coverAbnahme();
  const reel = await reelAbnahme();
  const totalActualUsd = sum(events, "actualUsd");
  const report = {
    generatedAt: new Date().toISOString(),
    branch: process.env.GITHUB_REF_NAME || "feature/cover-quality-v2",
    commit: process.env.GITHUB_SHA || null,
    model: CONFIG.bilder.charaktere.modell,
    feedQuality: [CONFIG.bilder.charaktere.guete, CONFIG.bilder.charaktere.retryGuete],
    reelQuality: [CONFIG.bilder.charaktere.reelGuete, CONFIG.bilder.charaktere.reelRetryGuete],
    qaModel: CONFIG.bilder.charaktere.qaModell,
    covers: cover.ergebnisse,
    contactSheet: cover.kontakt,
    reel,
    totalActualUsd,
    unknownSpend: events.some((e) => e.spendUnknown),
    telemetry: events,
  };
  fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(report, null, 2));
  fs.writeFileSync(path.join(out, "README.txt"), [
    "Herrjurist cover-quality-v2 REAL acceptance artifact",
    `Commit: ${report.commit || "local"}`,
    `10 covers: ${cover.ergebnisse.length}`,
    `Contact sheet: ${cover.kontakt}`,
    `Reel: ${reel.video}`,
    `Measured provider cost: $${totalActualUsd.toFixed(6)}`,
    "No Instagram/Meta publishing was performed.",
  ].join("\n") + "\n");
  console.log(JSON.stringify({
    ok: true,
    covers: cover.ergebnisse.length,
    firstPass: cover.ergebnisse.filter((x) => x.qaFirstPass).length,
    retries: cover.ergebnisse.filter((x) => !x.qaFirstPass).length,
    reelScenes: reel.scenes.length,
    reelVoice: reel.voiceProvider,
    costUsd: totalActualUsd,
    out,
  }, null, 2));
} catch (e) {
  status = "failed";
  fehler = e;
  fs.writeFileSync(path.join(out, "FAILED.txt"), String(e?.stack || e));
  throw e;
} finally {
  await browserBeenden().catch(() => {});
  kontextLoeschen();
  if (status !== "ok") console.error(String(fehler?.stack || fehler || "Abnahme fehlgeschlagen"));
}
