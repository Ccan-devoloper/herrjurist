#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { Hosting } from "../src/hosting.mjs";
import { beitragRendern, browserBeenden } from "../src/render.mjs";
import { lernPalette } from "../src/stile.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(hier, "..");
const out = path.join(root, "out", "cover-v2-last-feed-dryrun");
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

function latestPublishedCarousel(hosting) {
  const dir = path.join(hosting.stateDir, "plaene");
  const dates = fs.readdirSync(dir).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort().reverse();
  const found = [];
  for (const file of dates) {
    const plan = JSON.parse(fs.readFileSync(path.join(dir, file), "utf8"));
    for (const b of plan.beitraege || []) {
      if (b.status !== "veroeffentlicht" || b.format === "reel" || !b.veroeffentlicht) continue;
      found.push({ datum: plan.datum, ...b });
    }
    if (found.length) break;
  }
  found.sort((a,b) => String(b.veroeffentlicht).localeCompare(String(a.veroeffentlicht)));
  if (!found.length) throw new Error("Kein veröffentlichter Feed-Karussellbeitrag gefunden.");
  return found[0];
}

function liveCover(hosting, datum, slot) {
  const dir = path.join(hosting.dir, "bilder", datum);
  const prefix = `${datum}-${slot}-01-`;
  const files = fs.readdirSync(dir).filter((f) => f.startsWith(prefix) && /\.jpe?g$/i.test(f)).sort();
  if (!files.length) throw new Error(`Kein veröffentlichtes Cover für ${datum} ${slot} gefunden.`);
  return path.join(dir, files.at(-1));
}

function extractScene(src, dst, hex) {
  const py = `
from PIL import Image
from collections import deque
import sys
src,dst,bghex=sys.argv[1:4]
im=Image.open(src).convert("RGB")
w,h=im.size
left=int(w*0.10); top=int(h*0.43); right=w; bottom=int(h*0.96)
im=im.crop((left,top,right,bottom))
cw,ch=im.size
bg=tuple(int(bghex[i:i+2],16) for i in (1,3,5))
rgba=im.convert("RGBA")
px=rgba.load()
mask=[[False]*cw for _ in range(ch)]
for y in range(ch):
    for x in range(cw):
        r,g,b,_=px[x,y]
        d=((r-bg[0])**2+(g-bg[1])**2+(b-bg[2])**2)**0.5
        fg=d>58
        if (y < ch*0.22 and x < cw*0.76) or (x < cw*0.30 and y < ch*0.72):
            fg=False
        mask[y][x]=fg
seen=[[False]*cw for _ in range(ch)]
keep=set()
for y0 in range(ch):
  for x0 in range(cw):
    if seen[y0][x0] or not mask[y0][x0]: continue
    q=deque([(x0,y0)]); seen[y0][x0]=True; comp=[]; minx=maxx=x0; miny=maxy=y0
    while q:
      x,y=q.popleft(); comp.append((x,y)); minx=min(minx,x); maxx=max(maxx,x); miny=min(miny,y); maxy=max(maxy,y)
      for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 0<=nx<cw and 0<=ny<ch and not seen[ny][nx] and mask[ny][nx]:
          seen[ny][nx]=True; q.append((nx,ny))
    area=len(comp); bw=maxx-minx+1; bh=maxy-miny+1; cx=(minx+maxx)/2
    good=(area>=1100 and (bw>=55 or bh>=55))
    if cx < cw*0.34 and area < 5000: good=False
    if miny < ch*0.24 and area < 4500: good=False
    if good: keep.update(comp)
for y in range(ch):
  for x in range(cw):
    r,g,b,_=px[x,y]
    px[x,y]=(r,g,b,255 if (x,y) in keep else 0)
if not keep:
  raise SystemExit("Scene extraction produced no foreground.")
xs=[p[0] for p in keep]; ys=[p[1] for p in keep]; m=18
box=(max(0,min(xs)-m),max(0,min(ys)-m),min(cw,max(xs)+m+1),min(ch,max(ys)+m+1))
rgba.crop(box).save(dst)
`;
  execFileSync("python3", ["-c", py, src, dst, hex], { stdio: "inherit" });
}

const hosting = new Hosting({ pushen: false }).vorbereiten();
const pick = latestPublishedCarousel(hosting);
const contentPath = path.join(hosting.stateDir, "inhalte", `${pick.datum}-${pick.slot}.json`);
const inhalt = JSON.parse(fs.readFileSync(contentPath, "utf8"));
if (!Array.isArray(inhalt.folien) || !inhalt.folien.length) throw new Error("Letzter Feed-Beitrag hat keine Folien.");

const original = liveCover(hosting, pick.datum, pick.slot);
fs.copyFileSync(original, path.join(out, "original-live.jpg"));
const scene = path.join(out, "scene-extracted.png");
const palette = lernPalette(inhalt.fach);
extractScene(original, scene, palette.grund);

const title = inhalt.folien.find((f) => f.art === "titel");
title.bild = `data:image/png;base64,${fs.readFileSync(scene).toString("base64")}`;
title.bildQuelle = null;
title.bildFrei = true;
title.bildTyp = "charakter";
title.bildBreite = 900;
title.bildHoehe = 760;
title.coverHinweisPlan = { noteX: 0.28, noteY: 0.18, targetX: 0.72, targetY: 0.58, rotationDeg: -4, bend: 0 };

const renderDir = path.join(out, "rendered");
const files = await beitragRendern(inhalt, renderDir, { variante: 0 });
const report = {
  generatedAt: new Date().toISOString(),
  commit: process.env.GITHUB_SHA || null,
  source: {
    datum: pick.datum, slot: pick.slot, format: pick.format,
    themaId: pick.themaId, themaTitel: pick.themaTitel,
    publishedAt: pick.veroeffentlicht,
    liveCover: path.relative(hosting.dir, original)
  },
  targetContract: "cover-quality-v2 no-arrow / fb2fc680",
  providerCostUsd: 0,
  externalProviderCalls: false,
  sourceImageAlreadyPublished: true,
  note: "Offline renderer regression: the already-published cover is used only to recover a scene surrogate. No OpenAI/Anthropic/image/search provider is called.",
  outputs: files.map((f) => path.relative(out, f))
};
fs.writeFileSync(path.join(out, "manifest.json"), JSON.stringify(report, null, 2));
fs.writeFileSync(path.join(out, "README.txt"), [
  "Herr Jurist – zero-cost last-feed dry run",
  `Source: ${pick.datum} ${pick.slot} · ${pick.themaTitel}`,
  "Target: Cover Quality v2 no-arrow (fb2fc680 contract)",
  "Provider cost: $0.00",
  "The original live cover and the extracted scene surrogate are included for comparison."
].join("\n"));
await browserBeenden();
console.log(JSON.stringify(report, null, 2));
