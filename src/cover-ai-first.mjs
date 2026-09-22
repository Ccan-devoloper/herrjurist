/* global FormData, Blob */
/**
 * AI-first Herr-Jurist Cover.
 *
 * Das Bildmodell komponiert das FERTIGE 4:5-Cover als Einheit: Fachband,
 * Titelpillen, Badge, Handschrift/Pfeil und Charakterszene. Der Renderer darf
 * dieses Bild danach nur noch technisch auf 1080x1350 ausgeben.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execFileSync } from "node:child_process";
import { CONFIG } from "./config.mjs";
import { ffmpegPfad } from "./stimme.mjs";
import { lernPalette } from "./stile.mjs";
import { bildAufruf, openaiAufruf, openaiBildEditSenden } from "./anbieter.mjs";
import { charaktereFuer, bildKostenUsd } from "./charakterbild.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const charakterBasis = path.join(root, "assets", "charaktere");
const goldenZip = path.join(root, "assets", "referenzen", "cover-v2", "reference-images.zip");

const GOLDEN = [
  "01-strafrecht-at-versuch.jpg",
  "04-oeffentliches-recht-vwgo-80.jpg",
  "08-zpo-zulaessigkeit.jpg",
];

function fachBand(ziel = {}) {
  const f = String(ziel.fach || "").toLowerCase();
  if (f === "strafat") return "Strafrecht AT";
  if (["strafbt"].includes(f)) return "Strafrecht BT";
  if (["stpo","anklage","revision"].includes(f)) return "Strafprozessrecht";
  if (["bgbat"].includes(f)) return "BGB AT";
  if (["schuld","schuldbt","delikt"].includes(f)) return "Schuldrecht";
  if (f === "sachen") return "Sachenrecht";
  if (["zpo","zwangsv","assessorz"].includes(f)) return "ZPO";
  if (["staat","grundr"].includes(f)) return "Öffentliches Recht AT";
  if (["verwalt","verwbt","vwgo","assessoroer"].includes(f)) return "Verwaltungsrecht";
  if (f === "arbeit") return "Arbeitsrecht";
  if (f === "methodik") return "Klausur- und Lernmethodik";
  return String(ziel.fachLabel || "Jura").trim().slice(0, 42);
}

function fachPille(ziel = {}) {
  const f = String(ziel.fach || "").toLowerCase();
  if (/^straf|stpo|anklage|revision/.test(f)) return "Strafrecht";
  if (["staat","grundr","verwalt","verwbt","vwgo","europa","assessoroer"].includes(f)) return "Öffentliches Recht";
  if (["methodik","mindset"].includes(f)) return "Methodik";
  if (["arbeit","famerb","handelsg","ipr"].includes(f)) return "Nebenfach";
  return "Zivilrecht";
}

function coverFelder(ziel = {}) {
  const folie = ziel?.folien?.find?.((f) => f.art === "titel") || {};
  const titelZeilen = (folie.titelZeilen || []).map((x) => String(x || "").replace(/\s+/g, " ").trim()).filter(Boolean).slice(0, 4);
  const titel = String(folie.titel || ziel.titel || ziel.kurztitel || "").replace(/\s+/g, " ").trim();
  return {
    titel,
    titelZeilen: titelZeilen.length ? titelZeilen : [titel],
    badge: String(folie.coverBadge || ziel.coverBadge || "").replace(/\s+/g, " ").trim().slice(0, 36),
    note: String(folie.coverText || ziel.coverText || "").replace(/\s+/g, " ").trim().slice(0, 48),
    band: fachBand(ziel),
    fachPille: fachPille(ziel),
    counter: Array.isArray(ziel.folien) && ziel.folien.length > 1 ? `1/${ziel.folien.length}` : "",
  };
}

function regie(ziel = {}) {
  const r = ziel.coverRegie || {};
  return {
    kernidee: String(r.kernidee || "").replace(/\s+/g, " ").trim(),
    handlung: String(r.handlung || ziel.bildSzene || "").replace(/\s+/g, " ").trim(),
    hinweis: String(r.hinweisRegie || "").replace(/\s+/g, " ").trim(),
    alternative: String(r.alternative || ziel.bildSzeneAlt || "").replace(/\s+/g, " ").trim(),
  };
}

function charRef(char) {
  const b64 = fs.readFileSync(path.join(charakterBasis, char.datei), "utf8").trim();
  const p = path.join(os.tmpdir(), `hj-ai-cover-char-${char.id}-${process.pid}-${Date.now()}.jpg`);
  fs.writeFileSync(p, Buffer.from(b64, "base64"));
  return p;
}

function goldenRef(name) {
  if (!fs.existsSync(goldenZip)) return null;
  try {
    const liste = execFileSync("unzip", ["-Z1", goldenZip], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).split(/\r?\n/).filter(Boolean);
    const entry = liste.find((x) => x === name || x.endsWith(`/${name}`));
    if (!entry) return null;
    const bytes = execFileSync("unzip", ["-p", goldenZip, entry], { encoding: null, maxBuffer: 20 * 1024 * 1024, stdio: ["ignore", "pipe", "ignore"] });
    const p = path.join(os.tmpdir(), `hj-ai-cover-golden-${path.basename(name)}-${process.pid}-${Date.now()}.jpg`);
    fs.writeFileSync(p, bytes);
    return p;
  } catch {
    return null;
  }
}

function antwortBild(daten) {
  const b64 = daten?.data?.[0]?.b64_json;
  if (!b64) return null;
  const p = path.join(os.tmpdir(), `hj-ai-cover-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  fs.writeFileSync(p, Buffer.from(b64, "base64"));
  return p;
}

function crop4x5(src) {
  const dst = src.replace(/\.png$/, "-4x5.png");
  execFileSync(ffmpegPfad(), [
    "-y", "-loglevel", "error", "-i", src,
    "-vf", "crop=1024:1280:0:128,scale=1080:1350:flags=lanczos",
    "-frames:v", "1", dst,
  ]);
  return dst;
}

function prompt(ziel, chars, retryHint = "", alternative = false) {
  const f = coverFelder(ziel);
  const r = regie(ziel);
  const p = lernPalette(ziel.fach, { grund: "#FB902F", dunkel: "#351A0A", hell: "#FFF0E0" });
  const scene = alternative && r.alternative ? r.alternative : r.handlung;
  const charNames = chars.map((x) => x.name).join(", ");
  const lines = f.titelZeilen.map((x, i) => `TITLE PILL ${i + 1}: <<<${x}>>>`).join("\n");
  return [
    "Create the FINAL complete Herr Jurist Instagram feed cover, not a transparent vignette and not a mockup.",
    "Output portrait 1024x1536. The FINAL 4:5 cover is the CENTRAL 1024x1280 crop (remove 128 px from top and bottom). Keep every important text element, face, hand, prop and footer safely inside that central crop. Continue the background as full bleed outside it.",
    "The first supplied images are canonical character identity references. Match those exact recurring identities, but redraw them in a new pose. The last supplied images are Golden Reference COVERS: copy their brand language, visual density, proportions and polish, but NEVER their characters, props, legal topic or exact staging.",
    `Use EXACTLY ${chars.length} recurring character(s): ${charNames}. No additional people, robots, faces or duplicate characters.`,
    `BACKGROUND: solid subject color ${p.grund}. DARK BRAND COLOR: ${p.dunkel}. LIGHT BADGE COLOR: ${p.hell}.`,
    "Brand composition must match the Golden References: dark clipped subject ribbon flush top-left; huge white bold headline in separate dark rounded pills; small light editorial badge directly below; short handwritten note with one loose curved open-head arrow; one large expressive 2D cartoon scene dominating the lower half; small light subject pill bottom-right; dark circular carousel counter top-right only when specified.",
    "Keep the title block compact and dominant. Headline pills should be very large, with minimal vertical gaps, generous horizontal padding, and no overflow. Do not shrink the whole composition into a small sticker.",
    "Render ALL specified text exactly. German spelling, punctuation, § sign, abbreviations and capitalization must be character-perfect. Do not invent any additional readable text anywhere.",
    `SUBJECT RIBBON EXACT TEXT: <<<${f.band}>>>`,
    lines,
    `EDITORIAL BADGE EXACT TEXT: <<<${f.badge}>>>`,
    `HANDWRITTEN NOTE EXACT TEXT: <<<${f.note}>>>`,
    `BOTTOM SUBJECT PILL EXACT TEXT: <<<${f.fachPille}>>>`,
    f.counter ? `TOP-RIGHT COUNTER EXACT TEXT: <<<${f.counter}>>>` : "NO carousel counter on this single-cover test.",
    `LEGAL CORE: ${r.kernidee}`,
    `SCENE DIRECTION: ${scene}`,
    `HANDWRITTEN NOTE / ARROW DIRECTION: ${r.hinweis}`,
    "The handwritten note and arrow are part of the visual composition. Put them in the most natural negative space near the action. The arrow should be a smooth dark hand-drawn curve with a simple OPEN two-stroke arrowhead, like the Golden References, and clearly point to the legally meaningful prop/action without crossing a face.",
    "Keep the legal metaphor instantly understandable. Use few strong props. Preserve full readable anatomy and strong silhouettes. Premium 2D editorial sci-fi comedy cartoon, clean ink outlines, polished cel shading, expressive faces, no photorealism, no 3D.",
    "For sensitive criminal-law topics, use only symbolic/legal-study imagery. Do not depict injury, death, self-harm acts, medical crisis or graphic content.",
    retryHint ? `QUALITY RETRY: ${retryHint}` : "",
  ].filter(Boolean).join("\n");
}

const QA_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    ok: { type: "boolean" },
    textExact: { type: "boolean" },
    brandOk: { type: "boolean" },
    layoutOk: { type: "boolean" },
    identityOk: { type: "boolean" },
    sceneOk: { type: "boolean" },
    anatomyOk: { type: "boolean" },
    cropSafe: { type: "boolean" },
    extraReadableText: { type: "boolean" },
    issues: { type: "array", items: { type: "string" } },
    retryHint: { type: "string" },
  },
  required: ["ok","textExact","brandOk","layoutOk","identityOk","sceneOk","anatomyOk","cropSafe","extraReadableText","issues","retryHint"],
};

function responseText(a) {
  if (typeof a?.output_text === "string") return a.output_text;
  return (a?.output || []).flatMap((o) => o?.content || []).filter((x) => x?.type === "output_text" || x?.type === "text").map((x) => x?.text || "").join("\n");
}

async function qa(candidate, ziel, chars, charRefs, goldenRefs, slot) {
  const f = coverFelder(ziel);
  const expected = [
    f.band, ...f.titelZeilen, f.badge, f.note, f.fachPille, ...(f.counter ? [f.counter] : []),
  ].filter(Boolean);
  const content = [
    { type: "input_text", text: [
      "You are the final visual gate for a finished Herr Jurist Instagram cover.",
      "Image 1 is the generated FINAL 4:5 cover. The next images are canonical recurring-character references, followed by Golden Reference covers.",
      `Selected character identities: ${chars.map((x) => x.name).join(", ")}.`,
      `The ONLY intended readable strings are exactly: ${JSON.stringify(expected)}.`,
      "Set textExact=false for ANY typo, missing/extra character, wrong §/number/abbreviation, changed capitalization, merged title lines, missing required string, or altered handwritten note.",
      "Set extraReadableText=true for any other readable words/numbers/logos/gibberish not in the intended list.",
      "brandOk requires the same visual language as the Golden References: clipped dark subject ribbon, dominant dark rounded headline pills with white type, light badge, handwritten note + curved open-head arrow, large polished lower character scene, small bottom-right subject pill, and only the specified counter.",
      "layoutOk requires a compact title block, no text/pill overflow, no clipped ribbon, no dead upper-middle gap, large lower scene, and annotation integrated into negative space without covering faces or the central legal prop.",
      "identityOk requires the selected recurring characters to remain recognisably the same as their canonical references and no extra/duplicate characters.",
      "sceneOk requires the requested legal idea to be legible at a glance. For sensitive criminal-law topics, reject graphic or self-harm imagery; symbolic study metaphors are correct.",
      "Set ok=true only if every criterion passes. retryHint should be short, concrete and directly actionable.",
    ].join("\n") },
    { type:"input_image", image_url:`data:image/png;base64,${fs.readFileSync(candidate).toString("base64")}`, detail:"high" },
    ...charRefs.map((p) => ({ type:"input_image", image_url:`data:image/jpeg;base64,${fs.readFileSync(p).toString("base64")}`, detail:"high" })),
    ...goldenRefs.map((p) => ({ type:"input_image", image_url:`data:image/jpeg;base64,${fs.readFileSync(p).toString("base64")}`, detail:"high" })),
  ];

  const a = await openaiAufruf({
    zweck:"bild-qa",
    modell:CONFIG.bilder.charaktere.qaModell,
    params:{
      model:CONFIG.bilder.charaktere.qaModell,
      reasoning:{effort:"low"},
      max_output_tokens:800,
      input:[{role:"user",content}],
      text:{format:{type:"json_schema",name:"herrjurist_ai_first_cover_qa",strict:true,schema:QA_SCHEMA}},
    },
    optional:true,
    admissionInputTokens:28000,
    slot:`${slot || "cover"}-ai-first-qa`,
    promptVersion:"ai-first-cover-qa-v1",
  });
  const raw=responseText(a);
  const d=JSON.parse(raw.slice(raw.indexOf("{"),raw.lastIndexOf("}")+1));
  const hard = d.textExact && d.brandOk && d.layoutOk && d.identityOk && d.sceneOk && d.anatomyOk && d.cropSafe && !d.extraReadableText;
  return {...d,ok:Boolean(d.ok && hard)};
}

let lastImageStart=0;
async function rateWait() {
  const ms=Math.max(0,lastImageStart+Number(CONFIG.bilder.charaktere.minAbstandMs||13000)-Date.now());
  if(ms>0) await new Promise((r)=>setTimeout(r,ms));
  lastImageStart=Date.now();
}

async function editCall(refs, promptText, quality) {
  for(let attempt=0;attempt<3;attempt++){
    const form=new FormData();
    form.append("model",CONFIG.bilder.charaktere.modell);
    refs.forEach((p,i)=>{
      const type=/\.png$/i.test(p)?"image/png":"image/jpeg";
      form.append("image[]",new Blob([fs.readFileSync(p)],{type}),`ref-${i+1}${type==="image/png"?".png":".jpg"}`);
    });
    form.append("prompt",promptText);
    form.append("quality",quality);
    form.append("size","1024x1536");
    form.append("output_format","png");
    try{
      await rateWait();
      return await openaiBildEditSenden({form,key:CONFIG.bilder.ki.key,zeitlimitMs:CONFIG.bilder.charaktere.zeitlimitMs});
    }catch(e){
      if(Number(e?.status)!==429||attempt===2) throw e;
      await new Promise((r)=>setTimeout(r,Math.max(13000,Number(e?.retryAfter||0)*1000)));
    }
  }
}

export function aiCoverAktiv() {
  return Boolean(CONFIG.bilder?.charaktere?.aktiv && CONFIG.bilder?.ki?.key);
}

export async function aiCoverZeichnen(ziel,{slot=null}={}) {
  if(!aiCoverAktiv()||!ziel) return null;
  const chars=charaktereFuer(ziel).slice(0,2);
  if(!chars.length) return null;
  const charRefs=[],goldenRefs=[];
  let raw=null,cropped=null;
  const qaAttempts=[];
  try{
    for(const ch of chars) charRefs.push(charRef(ch));
    for(const name of GOLDEN){
      const p=goldenRef(name);
      if(p) goldenRefs.push(p);
    }
    const refs=[...charRefs,...goldenRefs];
    let correction="";
    const attempts=[
      {quality:CONFIG.bilder.charaktere.guete||"high",reserve:Math.max(0.14,Number(CONFIG.bilder.charaktere.reserveUsd||0.12)),alternative:false},
      {quality:CONFIG.bilder.charaktere.retryGuete||"xhigh",reserve:Math.max(0.26,Number(CONFIG.bilder.charaktere.retryReserveUsd||0.24)),alternative:true},
    ];
    for(let i=0;i<attempts.length;i++){
      const a=attempts[i];
      const promptText=prompt(ziel,chars,correction,a.alternative);
      const res=await bildAufruf({
        zweck:"bild",modell:CONFIG.bilder.charaktere.modell,optional:true,
        preisUsd:a.reserve,slot:slot||ziel.slug||ziel.themaId||"ai-first-cover",
        senden:()=>editCall(refs,promptText,a.quality),
        kostenAusAntwort:bildKostenUsd,
      });
      raw=antwortBild(res);
      if(!raw){
        qaAttempts.push({attempt:i+1,quality:a.quality,ok:false,issues:["Bildantwort ohne PNG"]});
        correction="Return one complete final portrait cover as a PNG.";
        continue;
      }
      try{
        cropped=crop4x5(raw);
      }catch(e){
        qaAttempts.push({attempt:i+1,quality:a.quality,ok:false,issues:[`4:5 crop failed: ${String(e?.message||e).slice(0,120)}`]});
        correction="Keep all required cover content safely inside the central 4:5 crop.";
        fs.rmSync(raw,{force:true}); raw=null;
        continue;
      }
      fs.rmSync(raw,{force:true}); raw=null;
      const q=await qa(cropped,ziel,chars,charRefs,goldenRefs,slot);
      qaAttempts.push({attempt:i+1,quality:a.quality,...q});
      if(q.ok){
        return {
          pfad:cropped,breite:1080,hoehe:1350,quality:a.quality,attempt:i+1,
          qaFirstPass:i===0,qaAttempts,qa:q,
          charakterIds:chars.map((x)=>x.id),charaktere:chars.map((x)=>x.name),
          prompt:promptText,
        };
      }
      correction=String(q.retryHint||q.issues?.join("; ")||"Fix all visual QA issues.").slice(0,900);
      fs.rmSync(cropped,{force:true}); cropped=null;
    }
    return null;
  } finally {
    if(raw) fs.rmSync(raw,{force:true});
    if(cropped) fs.rmSync(cropped,{force:true});
    for(const p of [...charRefs,...goldenRefs]) fs.rmSync(p,{force:true});
  }
}
