#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { CHARAKTERE, charakterMotivZeichnen, charaktereFuer } from "../src/charakterbild.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { budgetStarten } from "../src/budget.mjs";
import { kontextSetzen, kontextLoeschen, openaiAufruf } from "../src/anbieter.mjs";
import { budgetSetzen } from "../src/kosten.mjs";
import { CONFIG } from "../src/config.mjs";
import { titelZeilen } from "../src/vorlagen.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "cover-quality-v2-oer-dryrun");
const coversDir = path.join(out, "covers");
const motifsDir = path.join(out, "motifs");
const promptPath = path.join(root, "prompts", "herrjurist-daily-finalization.txt");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(coversDir, { recursive: true });
fs.mkdirSync(motifsDir, { recursive: true });

const exactPrompt = fs.readFileSync(promptPath, "utf8");
const promptSha256 = crypto.createHash("sha256").update(exactPrompt).digest("hex");
const events = [];
const telemetrie = { aufruf(e) { events.push({ zeit: new Date().toISOString(), ...e }); } };
const budget = budgetStarten({
  deckel: { core: 0.35, engagement: 0, research: 0 },
  bisher: { core: 0, engagement: 0, research: 0 },
  protokoll: () => {},
});
budgetSetzen({ limitUsd: 0.35, antwortLimitUsd: 0.35 });
kontextSetzen({ budget, telemetrie, journal: null, kanal: "herrjurist-oer-prompt-dryrun", datum: "2026-09-22" });

const round = (n) => Number(Number(n || 0).toFixed(6));
const sum = (list, field = "actualUsd") => round(list.reduce((a, x) => a + (Number.isFinite(Number(x?.[field])) ? Number(x[field]) : 0), 0));
const responseText = (a) => typeof a?.output_text === "string"
  ? a.output_text
  : (a?.output || []).flatMap((o) => o?.content || []).filter((x) => x?.type === "output_text" || x?.type === "text").map((x) => x?.text || "").join("\n");

function dataUri(p) { return `data:image/png;base64,${fs.readFileSync(p).toString("base64")}`; }
function dimensions(p) {
  const raw = execFileSync("ffprobe", ["-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","json",p], { encoding:"utf8" });
  const s = JSON.parse(raw)?.streams?.[0] || {};
  return { width:Number(s.width||0), height:Number(s.height||0) };
}
function cleanup(m) { for (const p of new Set([m?.pfad,m?.ohneRand].filter(Boolean))) fs.rmSync(p,{force:true}); }

const COVER_SCHEMA = {
  type:"object", additionalProperties:false,
  properties:{
    titel:{type:"string"},
    titelZeilen:{type:"array",minItems:2,maxItems:4,items:{type:"string"}},
    coverBadge:{type:"string"},
    coverText:{type:"string"},
    coverRegie:{
      type:"object",additionalProperties:false,
      properties:{
        charaktere:{type:"array",minItems:1,maxItems:2,items:{type:"string",enum:Object.keys(CHARAKTERE)}},
        kernidee:{type:"string"},
        handlung:{type:"string"},
        hinweisRegie:{type:"string"},
        alternative:{type:"string"}
      },
      required:["charaktere","kernidee","handlung","hinweisRegie","alternative"]
    },
    bildSzene:{type:"string"},
    bildSzeneAlt:{type:"string"}
  },
  required:["titel","titelZeilen","coverBadge","coverText","coverRegie","bildSzene","bildSzeneAlt"]
};

async function promptTrockenlauf() {
  const params={
    model:"gpt-5.4-mini",
    reasoning:{effort:"low"},
    max_output_tokens:3000,
    instructions:[
      "DRY-RUN SCOPE OVERRIDE: Apply the user's exact prompt only to ONE Herr-Jurist cover.",
      "Do not publish, do not alter schedules, do not write any repository state, and do not create stories/reels or Examenscampus content.",
      "The single cover must be Öffentliches Recht.",
      "Use this selected test topic: Anhörung vor belastendem Verwaltungsakt nach § 28 VwVfG.",
      "Return only the structured cover editorial data requested by the schema.",
      "Respect the user's visual/editorial rules exactly, especially semantic title lines, dynamic character choice, coverText, coverRegie.hinweisRegie, and Golden-Reference quality.",
      "The image model itself will later generate NO text and NO arrows; visual QA will plan annotation placement; the renderer will draw the exact coverText and arrow."
    ].join("\n"),
    input:[{role:"user",content:[{type:"input_text",text:exactPrompt}]}],
    text:{format:{type:"json_schema",name:"herrjurist_oer_prompt_dryrun",strict:true,schema:COVER_SCHEMA}}
  };
  const a=await openaiAufruf({
    zweck:"bildregie",modell:"gpt-5.4-mini",params,optional:false,
    admissionInputTokens:6500,slot:"oer-dryrun-regie",promptVersion:"exact-daily-prompt-oer-dryrun-v2"
  });
  const raw=responseText(a);
  const d=JSON.parse(raw.slice(raw.indexOf("{"),raw.lastIndexOf("}")+1));
  d.coverText=String(d.coverText||"").replace(/\s+/g," ").trim().slice(0,48);
  d.coverBadge=String(d.coverBadge||"").replace(/\s+/g," ").trim().slice(0,32);
  d.titel=String(d.titel||"").replace(/\s+/g," ").trim().slice(0,160);
  d.titelZeilen=(d.titelZeilen||[]).map(x=>String(x||"").replace(/\s+/g," ").trim()).filter(Boolean).slice(0,4);
  d.titelZeilen=titelZeilen(d.titel,d.titelZeilen);
  if(d.titelZeilen.length<2) throw new Error("Prompt dry-run returned fewer than 2 semantic title lines.");
  return d;
}

let motiv=null;
try {
  const redaktion=await promptTrockenlauf();
  const ziel={
    format:"pruefungsfrage",
    fach:"verwalt",
    klausur:3,
    fachLabel:"Öffentliches Recht",
    themaId:"dryrun-oer-28-vwvfg",
    slug:"single-oer-dryrun",
    titel:redaktion.titel,
    kurztitel:redaktion.titel,
    coverText:redaktion.coverText,
    coverRegie:redaktion.coverRegie,
    bildSzene:redaktion.bildSzene,
    bildSzeneAlt:redaktion.bildSzeneAlt,
  };
  const selectedCharacterIds=charaktereFuer(ziel).map(x=>x.id);
  motiv=await charakterMotivZeichnen(ziel,{zweck:"bild",slot:"single-oer-dryrun"});
  if(!motiv) throw new Error("No public-law character motif passed technical + visual QA.");

  const motifFile=path.join(motifsDir,"single-oer-dryrun.png");
  fs.copyFileSync(motiv.pfad,motifFile);
  const folie={
    art:"titel",
    titel:redaktion.titel,
    titelZeilen:redaktion.titelZeilen,
    icon:"paragraf",
    coverBadge:redaktion.coverBadge,
    coverText:redaktion.coverText,
    bild:dataUri(motifFile),
    bildFrei:true,
    bildBreite:motiv.breite||null,
    bildHoehe:motiv.hoehe||null,
    bildTyp:"charakter",
    bildCharaktere:motiv.charaktere,
    coverHinweisPlan:motiv.annotationPlan||null,
  };
  const beitrag={
    format:"pruefungsfrage",fach:"verwalt",klausur:3,fachLabel:"Öffentliches Recht",
    slug:"single-oer-dryrun",coverRegie:redaktion.coverRegie,folien:[folie]
  };
  const [rendered]=await beitragRendern(beitrag,coversDir,{variante:0});
  const coverFile=path.join(coversDir,"cover.jpg");
  if(rendered!==coverFile) fs.renameSync(rendered,coverFile);
  const dim=dimensions(coverFile);
  if(dim.width!==1080||dim.height!==1350) throw new Error(`Wrong cover format ${dim.width}x${dim.height}`);

  if(events.some(e=>e.spendUnknown)) throw new Error("Provider spend contains unknown cost.");
  const report={
    generatedAt:new Date().toISOString(),
    dryRun:true,
    published:false,
    promptPath:"prompts/herrjurist-daily-finalization.txt",
    promptSha256,
    branch:process.env.GITHUB_REF_NAME||"feature/cover-quality-v2",
    commit:process.env.GITHUB_SHA||null,
    scope:"exact uploaded daily prompt; execution constrained to one Herr Jurist public-law cover",
    topic:{title:"Anhörung vor belastendem Verwaltungsakt nach § 28 VwVfG",fach:"verwalt",fachLabel:"Öffentliches Recht",normen:["§ 28 VwVfG"]},
    editorial:redaktion,
    cover:{
      selectedCharacterIds,
      renderedCharacterIds:motiv.charakterIds,
      renderedCharacters:motiv.charaktere,
      quality:motiv.quality,
      attempt:motiv.attempt,
      qaFirstPass:motiv.qaFirstPass,
      qaAttempts:motiv.qaAttempts,
      annotationPlan:motiv.annotationPlan||null,
      imagePath:path.relative(root,coverFile),
      motifPath:path.relative(root,motifFile),
      motifDimensions:{width:Number(motiv.breite||0),height:Number(motiv.hoehe||0)},
      dimensions:dim
    },
    costUsd:{
      director:sum(events.filter(e=>e.purpose==="bildregie")),
      image:sum(events.filter(e=>e.purpose==="bild"||e.purpose==="erklaerbild")),
      visionQa:sum(events.filter(e=>e.purpose==="bild-qa")),
      total:sum(events)
    },
    calls:events
  };
  fs.writeFileSync(path.join(out,"manifest.json"),JSON.stringify(report,null,2));
  fs.writeFileSync(path.join(out,"README.txt"),[
    "Herrjurist · exact-prompt dry-run · one public-law cover",
    `Topic: ${report.topic.title}`,
    `Prompt SHA-256: ${promptSha256}`,
    `Cover: ${path.relative(root,coverFile)}`,
    `Provider cost: $${report.costUsd.total.toFixed(6)}`,
    "No publishing. No daily-plan mutation. Exactly one final cover artifact."
  ].join("\n")+"\n");
  console.log(JSON.stringify({topic:report.topic.title,title:redaktion.titel,costUsd:report.costUsd,characters:motiv.charakterIds,annotationPlan:motiv.annotationPlan,attempt:motiv.attempt},null,2));
} catch(e) {
  fs.writeFileSync(path.join(out,"error.txt"),String(e?.stack||e));
  fs.writeFileSync(path.join(out,"calls.json"),JSON.stringify(events,null,2));
  throw e;
} finally {
  if(motiv) cleanup(motiv);
  await browserBeenden().catch(()=>{});
  kontextLoeschen();
}
