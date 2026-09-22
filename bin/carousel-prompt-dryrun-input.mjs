#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execFileSync } from "node:child_process";
import { themenpool, FAECHER } from "../src/inhalte.mjs";

const hier=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(hier,"..");
const out=path.join(root,"out","carousel-prompt-dryrun-input");
fs.rmSync(out,{recursive:true,force:true});
fs.mkdirSync(out,{recursive:true});

const pool=themenpool();
const text=(t)=>[
  t.titel,
  ...(t.normen||[]),
  ...(t.kern?.lernziele||[]),
  ...(t.kern?.pruefschritte||[]),
  t.kern?.merksatz,
  ...(t.kern?.fehler||[])
].filter(Boolean).join(" | ");

const matches=pool.filter((t)=>/willenserkl[aä]rung|empfangsbed[uü]rftig|zugang\s+einer\s+willenserkl[aä]rung|auslegung\s+von\s+willenserkl[aä]rungen/i.test(text(t)));
const bevorzugt=matches.filter((t)=>t.fach==="schuld");
const fallback=matches.filter((t)=>t.fach==="bgbat");
const auswahl=(bevorzugt.length?bevorzugt:fallback)[0]||null;

fs.writeFileSync(path.join(out,"matches.json"),JSON.stringify({
  requested:"Schuldrecht AT · Willenserklärung",
  selected:auswahl,
  matches:matches.map((t)=>({...t,fachLabel:FAECHER[t.fach]?.label||t.fach}))
},null,2));

const zip=path.join(root,"assets","referenzen","cover-v2","reference-images.zip");
const refs=path.join(out,"golden-references");
fs.mkdirSync(refs,{recursive:true});
execFileSync("unzip",["-j","-o",zip,"-d",refs],{stdio:"inherit"});
fs.copyFileSync(path.join(root,"assets/referenzen/cover-v2/README.md"),path.join(out,"README.md"));
fs.copyFileSync(path.join(root,"assets/referenzen/cover-v2/manifest.json"),path.join(out,"manifest.json"));
console.log(JSON.stringify({selected:auswahl?.id||null,title:auswahl?.titel||null,fach:auswahl?.fach||null,matchCount:matches.length},null,2));
