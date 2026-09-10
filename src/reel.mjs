/* ==========================================================================
   Reels: aus einem Reel-Skript (Szenen mit Bildschirmtext + Sprechertext)
   wird ein 9:16-Video mit Sprecherstimme, mitlaufenden Untertiteln und
   dezentem Klangbett.

   Ablauf: Stimme je Szene erzeugen (stimme.mjs) → Zeitplan aus den
   Audiodauern → Frames mit Chromium rendern (JS-gesteuerte Animation, Bild
   für Bild deterministisch) → ffmpeg: H.264/AAC MP4 + Cover-JPEG.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { browserStarten, coverRendern } from "./render.mjs";
import { css, klausurCss, buntCss } from "./vorlagen.mjs";
import { stil as stilLaden, iconSvg } from "./stile.mjs";
import { FAECHER } from "./inhalte.mjs";
import { CONFIG } from "./config.mjs";
import { sprechen, ffmpegPfad, anbieterFuerText, offlineAnbieter } from "./stimme.mjs";

/* Höhe des animierten Bereichs: ein Drittel des 9:16-Bildes. */
const OBEN = 640;

/* Die drei Animationen (Canvas, deterministisch je Zeitpunkt). Physik wird beim
   Laden der Seite in festen Schritten vorausberechnet, damit jedes Bild exakt
   reproduzierbar ist. Koordinaten beziehen sich auf 1080 × OBEN. */
const ANIMATIONEN = String.raw`
const cv = document.getElementById("oben"), g = cv.getContext("2d");
function rng(seed) { let s = seed >>> 0; return () => { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; }; }
const DT = 1 / 240;

/* ---- Labyrinth: Kugel rollt auf dem Lösungsweg, dann das nächste ---- */
const COLS = 13, ROWS = 7, CELL = 76, OX = (1080 - COLS * CELL) / 2, OY = (H - ROWS * CELL) / 2;
function labyrinth(seed) {
  const r = rng(seed); const z = Array.from({ length: COLS * ROWS }, () => ({ n: 1, s: 1, e: 1, w: 1, v: false }));
  const id = (x, y) => y * COLS + x; const st = [[0, 0]]; z[0].v = true;
  while (st.length) {
    const [x, y] = st[st.length - 1]; const nb = [];
    if (y > 0 && !z[id(x, y - 1)].v) nb.push([x, y - 1, "n", "s"]); if (y < ROWS - 1 && !z[id(x, y + 1)].v) nb.push([x, y + 1, "s", "n"]);
    if (x > 0 && !z[id(x - 1, y)].v) nb.push([x - 1, y, "w", "e"]); if (x < COLS - 1 && !z[id(x + 1, y)].v) nb.push([x + 1, y, "e", "w"]);
    if (!nb.length) { st.pop(); continue; }
    const [nx, ny, a, b] = nb[Math.floor(r() * nb.length)]; z[id(x, y)][a] = 0; z[id(nx, ny)][b] = 0; z[id(nx, ny)].v = true; st.push([nx, ny]);
  }
  const prev = new Array(COLS * ROWS).fill(-1); const q = [0]; prev[0] = 0;
  while (q.length) { const c = q.shift(); const x = c % COLS, y = (c / COLS) | 0; const zc = z[c];
    for (const [dx, dy, wand] of [[0, -1, "n"], [0, 1, "s"], [1, 0, "e"], [-1, 0, "w"]]) { if (zc[wand]) continue; const n = id(x + dx, y + dy); if (prev[n] >= 0) continue; prev[n] = c; q.push(n); } }
  const pfad = []; let c = COLS * ROWS - 1; while (c !== 0) { pfad.push([c % COLS, (c / COLS) | 0]); c = prev[c]; } pfad.push([0, 0]); pfad.reverse();
  return { z, pfad };
}
const SPEED = 3.2, PAUSE = 0.9; const labys = [], labyZeit = [];
function labyFuer(t) {
  let k = 0, start = 0;
  for (;;) {
    if (!labys[k]) { labys[k] = labyrinth(7 + k * 131); labyZeit[k] = (labys[k].pfad.length - 1) / SPEED + PAUSE; }
    if (t < start + labyZeit[k]) return { L: labys[k], lokal: t - start, k };
    start += labyZeit[k]; k++;
  }
}
function zeichneLabyrinth(t) {
  const { L, lokal, k } = labyFuer(t);
  g.clearRect(0, 0, 1080, H);
  const fade = Math.max(0, Math.min(1, lokal / 0.35, (labyZeit[k] - lokal) / 0.35));
  g.globalAlpha = fade; g.lineCap = "round"; g.lineJoin = "round"; g.strokeStyle = FARBEN.wand; g.lineWidth = 5; g.beginPath();
  for (let y = 0; y < ROWS; y++) for (let x = 0; x < COLS; x++) { const c = L.z[y * COLS + x]; const px = OX + x * CELL, py = OY + y * CELL;
    if (c.n) { g.moveTo(px, py); g.lineTo(px + CELL, py); } if (c.w) { g.moveTo(px, py); g.lineTo(px, py + CELL); }
    if (x === COLS - 1 && c.e) { g.moveTo(px + CELL, py); g.lineTo(px + CELL, py + CELL); } if (y === ROWS - 1 && c.s) { g.moveTo(px, py + CELL); g.lineTo(px + CELL, py + CELL); } }
  g.stroke();
  const zx = OX + (COLS - 0.5) * CELL, zy = OY + (ROWS - 0.5) * CELL; const puls = 0.5 + 0.5 * Math.sin(t * 5);
  g.strokeStyle = FARBEN.ziel; g.lineWidth = 4; g.beginPath(); g.arc(zx, zy, 16 + 6 * puls, 0, Math.PI * 2); g.stroke();
  g.fillStyle = FARBEN.ziel; g.beginPath(); g.arc(zx, zy, 7, 0, Math.PI * 2); g.fill();
  const pos = Math.min(L.pfad.length - 1, lokal * SPEED); const i = Math.floor(pos), f = pos - i;
  const a = L.pfad[i], b = L.pfad[Math.min(L.pfad.length - 1, i + 1)];
  const bx = OX + (a[0] + (b[0] - a[0]) * f + 0.5) * CELL, by = OY + (a[1] + (b[1] - a[1]) * f + 0.5) * CELL;
  g.strokeStyle = FARBEN.spur; g.globalAlpha = 0.28 * fade; g.lineWidth = 16; g.beginPath();
  for (let j = 0; j <= i; j++) { const p = L.pfad[j]; const x = OX + (p[0] + 0.5) * CELL, y = OY + (p[1] + 0.5) * CELL; j ? g.lineTo(x, y) : g.moveTo(x, y); }
  g.lineTo(bx, by); g.stroke(); g.globalAlpha = fade;
  g.save(); g.translate(bx, by); g.rotate(pos * 0.9);
  g.fillStyle = FARBEN.ball; g.beginPath(); g.arc(0, 0, 21, 0, Math.PI * 2); g.fill();
  g.fillStyle = FARBEN.text; g.globalAlpha *= 0.55; g.beginPath(); g.arc(9, -6, 6, 0, Math.PI * 2); g.fill();
  g.restore(); g.globalAlpha = 1;
}

/* ---- Marble Run: Kugeln über versetzte Rampen ---- */
function simMarble(sekunden) {
  const RAMPEN = []; const n = 4, links = 70, rechts = 1010, oben = 48, abstand = 128, gefaelle = 82;
  for (let i = 0; i < n; i++) { const y0 = oben + i * abstand, y1 = y0 + gefaelle; RAMPEN.push(i % 2 === 0 ? { x0: links, y0, x1: rechts - 150, y1 } : { x0: rechts, y0, x1: links + 150, y1 }); }
  const states = []; const balls = []; let spawn = 0; const r = 17, G = 1500; const rr = rng(99);
  for (let t = 0; t < sekunden; t += DT) {
    if (t >= spawn) { balls.push({ x: links + 30, y: 20, vx: 60 + rr() * 40, vy: 0, c: balls.length % 2 }); spawn = t + 2.2; }
    for (const b of balls) {
      b.vy += G * DT; b.x += b.vx * DT; b.y += b.vy * DT;
      for (const R of RAMPEN) {
        const dx = R.x1 - R.x0, dy = R.y1 - R.y0, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L, nx = -uy, ny = ux;
        const px = b.x - R.x0, py = b.y - R.y0; const along = px * ux + py * uy; const dist = px * nx + py * ny;
        if (along < -r || along > L + r) continue;
        const nsign = ny < 0 ? 1 : -1; const d = dist * nsign;
        if (d < r && d > -r * 0.5) { const vn = (b.vx * nx + b.vy * ny) * nsign;
          if (vn < 0) { b.x += (r - d) * nx * nsign; b.y += (r - d) * ny * nsign; const vt = b.vx * ux + b.vy * uy; const vn2 = -vn * 0.25; b.vx = ux * vt + nx * nsign * vn2; b.vy = uy * vt + ny * nsign * vn2; b.vx *= 0.999; b.vy *= 0.999; } }
      }
      if (b.x < r + 20) { b.x = r + 20; b.vx = Math.abs(b.vx) * 0.5; } if (b.x > 1060 - r) { b.x = 1060 - r; b.vx = -Math.abs(b.vx) * 0.5; }
    }
    for (let i = balls.length - 1; i >= 0; i--) if (balls[i].y > H + 40) balls.splice(i, 1);
    states.push(balls.map((b) => ({ x: b.x, y: b.y, c: b.c })));
  }
  return { states, RAMPEN, r };
}
let MARBLE = null;
function zeichneMarble(t) {
  if (!MARBLE) MARBLE = simMarble(GESAMT + 1);
  const st = MARBLE.states[Math.min(MARBLE.states.length - 1, Math.round(t / DT))];
  g.clearRect(0, 0, 1080, H); g.lineCap = "round"; g.strokeStyle = FARBEN.wand; g.lineWidth = 10;
  for (const R of MARBLE.RAMPEN) { g.beginPath(); g.moveTo(R.x0, R.y0); g.lineTo(R.x1, R.y1); g.stroke(); g.fillStyle = FARBEN.ziel; g.beginPath(); g.arc(R.x1, R.y1, 9, 0, Math.PI * 2); g.fill(); }
  g.strokeStyle = FARBEN.wand; g.lineWidth = 8; g.beginPath(); g.arc(540, H - 40, 90, Math.PI * 0.08, Math.PI * 0.92); g.stroke();
  for (const b of st) { g.fillStyle = b.c ? FARBEN.spur : FARBEN.ball; g.beginPath(); g.arc(b.x, b.y, MARBLE.r, 0, Math.PI * 2); g.fill(); g.fillStyle = FARBEN.text; g.globalAlpha = 0.5; g.beginPath(); g.arc(b.x + 6, b.y - 6, 5, 0, Math.PI * 2); g.fill(); g.globalAlpha = 1; }
}

/* ---- Kugel springt in rotierenden Ringen mit Lücke ---- */
function simRing(sekunden) {
  const CX = 540, CY = H / 2, G = 1300, r = 17;
  const RINGE = [{ R: 105, w: 1.1, off: 0.3 }, { R: 150, w: -0.8, off: 2.1 }, { R: 195, w: 0.65, off: 4.0 }, { R: 240, w: -0.5, off: 1.2 }];
  const LUECKE = 1.05; const states = []; let ball = { x: CX, y: CY - 30, vx: 170, vy: 0 }; let frei = 0, reset = 0, resetZeit = 0; const trail = [];
  for (let t = 0; t < sekunden; t += DT) {
    ball.vy += G * DT; ball.x += ball.vx * DT; ball.y += ball.vy * DT;
    for (let i = frei; i < RINGE.length; i++) {
      const ring = RINGE[i]; const dx = ball.x - CX, dy = ball.y - CY; const d = Math.hypot(dx, dy);
      if (d + r >= ring.R) {
        const ang = Math.atan2(dy, dx); const gap = ((ring.off + ring.w * t) % (Math.PI * 2) + Math.PI * 2) % (Math.PI * 2);
        const diff = Math.abs(((ang - gap) % (Math.PI * 2) + Math.PI * 3) % (Math.PI * 2) - Math.PI);
        if (diff < LUECKE / 2 && i === frei) { frei++; continue; }
        const nx = dx / d, ny = dy / d; const vn = ball.vx * nx + ball.vy * ny;
        if (vn > 0) { ball.vx -= 2 * vn * nx; ball.vy -= 2 * vn * ny; ball.vx *= 1.015; ball.vy *= 1.015; ball.x = CX + nx * (ring.R - r - 0.5); ball.y = CY + ny * (ring.R - r - 0.5); }
        break;
      }
    }
    if (frei >= RINGE.length && Math.hypot(ball.x - CX, ball.y - CY) > 330 && !resetZeit) resetZeit = t + 0.5;
    if (resetZeit && t >= resetZeit) { ball = { x: CX, y: CY - 30, vx: 150 + 40 * reset, vy: 0 }; frei = 0; reset++; resetZeit = 0; trail.length = 0; }
    trail.push([ball.x, ball.y]); if (trail.length > 40) trail.shift();
    states.push({ x: ball.x, y: ball.y, frei, gaps: RINGE.map((ring) => ring.off + ring.w * t), trail: trail.filter((_, j) => j % 4 === 0) });
  }
  return { states, RINGE, CX, CY, r, LUECKE };
}
let RING = null;
function zeichneRing(t) {
  if (!RING) RING = simRing(GESAMT + 1);
  const st = RING.states[Math.min(RING.states.length - 1, Math.round(t / DT))];
  g.clearRect(0, 0, 1080, H); g.lineCap = "round";
  RING.RINGE.forEach((ring, i) => { if (i < st.frei) return; const gap = st.gaps[i];
    g.strokeStyle = i === st.frei ? FARBEN.ball : FARBEN.text; g.globalAlpha = i === st.frei ? 1 : 0.22; g.lineWidth = i === st.frei ? 10 : 7;
    g.beginPath(); g.arc(RING.CX, RING.CY, ring.R, gap + RING.LUECKE / 2, gap - RING.LUECKE / 2 + Math.PI * 2); g.stroke(); g.globalAlpha = 1; });
  g.strokeStyle = FARBEN.spur; g.lineWidth = 6; g.globalAlpha = 0.5; g.beginPath();
  st.trail.forEach((p, j) => (j ? g.lineTo(p[0], p[1]) : g.moveTo(p[0], p[1]))); g.lineTo(st.x, st.y); g.stroke(); g.globalAlpha = 1;
  g.fillStyle = FARBEN.ball; g.beginPath(); g.arc(st.x, st.y, RING.r, 0, Math.PI * 2); g.fill();
  g.fillStyle = FARBEN.text; g.globalAlpha = 0.5; g.beginPath(); g.arc(st.x + 5, st.y - 5, 5, 0, Math.PI * 2); g.fill(); g.globalAlpha = 1;
}
const ZEICHNER = { labyrinth: zeichneLabyrinth, marble: zeichneMarble, ring: zeichneRing, keine: () => {} };
`;

/* Vollflächiger Clip: Inhalt als Karte in der Tagesfarbe, Untertitel als weiße
   Karte darunter, Seite selbst transparent – der Clip wird per ffmpeg
   dahintergelegt. */
function overlayCss(ctx) {
  const stil = ctx.stil;
  const p = (stil.familie || stil.id) === "bunt" ? (stil.tagFarben?.[ctx.klausur] || stil.tagFarben?.[3]) : { grund: stil.farben.grund, dunkel: stil.farben.text, hell: stil.farben.flaeche };
  return `
.reel{background:transparent}
canvas#oben,.trenner{display:none}
.reel::before{content:"";position:absolute;left:54px;top:150px;width:972px;height:1010px;border-radius:44px;background:${p.grund};box-shadow:0 30px 80px rgba(0,0,0,.35)}
.reel::after{content:"";position:absolute;left:54px;top:1220px;width:972px;height:330px;border-radius:44px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35)}
.fortschritt{top:290px;left:106px;right:106px;background:rgba(255,255,255,.45);z-index:1}
.reel .kopf{top:194px;left:106px;right:106px;z-index:1}
.szene{top:330px;left:106px;right:106px;height:700px;z-index:1}
.szene>*{max-width:100%}
.schritt>div:last-child{min-width:0;flex:1}
.schritt h2,.merke-titel,.ctablock h2{max-width:100%}
.reel .fuss{top:1078px;bottom:auto;left:106px;right:106px;z-index:1}
.untertitel{top:1220px;height:330px;left:104px;right:104px;padding:0 20px;z-index:2}
.reel .untertitel .block{color:#111;text-shadow:none}
.reel .untertitel .w,.familie-bunt .untertitel .w{color:#111}
.reel .untertitel .w.jetzt,.familie-bunt .untertitel .w.jetzt,.reel .untertitel .w.jetzt{color:${p.dunkel}}`;
}

const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

/* Alle Szenen mit einem Anbieter sprechen und daraus den Zeitplan bauen. */
async function szenenSprechen(reel, audioDir, anbieter, stimmeId = null) {
  const szenen = [];
  let t = 0;
  for (const [i, s] of reel.szenen.entries()) {
    /* Der Hook wird betont gesprochen und bekommt danach einen Moment Stille –
       erst dieser Bruch macht aus einem Satz einen Aufhänger. */
    const istHook = s.art === "hook" || i === 0;
    const stimme = await sprechen(s.sprecher, path.join(audioDir, `szene-${String(i + 1).padStart(2, "0")}.mp3`), { betonung: istHook ? "hook" : null, anbieter, stimmeId });
    const vorlauf = i === 0 ? 0.25 : 0.25;
    const nachlauf = s.art === "cta" ? 1.2 : istHook ? 0.85 : 0.55;
    const dauer = vorlauf + stimme.dauer + nachlauf;
    szenen.push({ ...s, index: i, start: t, dauer, audioStart: t + vorlauf, audio: stimme.datei, woerter: stimme.woerter.map((w) => ({ ...w, von: w.von + t + vorlauf, bis: w.bis + t + vorlauf })), echt: stimme.echt, anbieter: stimme.anbieter });
    t += dauer;
  }
  return { szenen, gesamt: Math.min(t, CONFIG.reel.maxSekunden), echt: szenen.every((s) => s.echt), anbieter: szenen[0]?.anbieter || "aus", stimmeId: szenen[0]?.stimmeId || null };
}

/* Zeitplan: jede Szene = kurzer Vorlauf + Sprechdauer + Nachlauf.
   Der Anbieter wird einmal für das ganze Reel bestimmt – nach dem, was das
   ElevenLabs-Monatsguthaben noch trägt (stimme.mjs). */
export async function zeitplanErstellen(reel, audioDir, opt = {}) {
  const zeichen = reel.szenen.reduce((a, s) => a + String(s.sprecher || "").length, 0);
  const anbieter = opt.anbieter || (await anbieterFuerText(zeichen));
  const plan = await szenenSprechen(reel, audioDir, anbieter, opt.stimmeId || null);
  /* Ist das Guthaben mitten im Reel ausgegangen, sprechen jetzt zwei Stimmen im
     selben Video. Dann lieber alles noch einmal offline – das kostet nichts. */
  if (new Set(plan.szenen.map((s) => s.anbieter)).size > 1) return szenenSprechen(reel, audioDir, offlineAnbieter());
  plan.stimmeName = anbieter === "elevenlabs" ? opt.stimmeName || null : null;
  return plan;
}

/* Animation des oberen Drittels: täglich rotierend (Labyrinth → Marble Run → Ring). */
export function animationFuer(datum) {
  const liste = CONFIG.reel.animationen;
  if (CONFIG.reel.animation && liste.includes(CONFIG.reel.animation)) return CONFIG.reel.animation;
  const tage = Math.floor(Date.UTC(+datum.slice(0, 4), +datum.slice(5, 7) - 1, +datum.slice(8, 10)) / 86400000);
  return liste[((tage % liste.length) + liste.length) % liste.length];
}

/* Hintergrund-Clip des Tages aus einem Verzeichnis (sortiert, täglich rotierend). */
export function hintergrundClip(verzeichnis, datum) {
  if (!verzeichnis || CONFIG.reel.hintergrund === "animation" || !fs.existsSync(verzeichnis)) return null;
  const clips = fs.readdirSync(verzeichnis).filter((f) => /\.(mp4|mov|webm)$/i.test(f)).sort();
  if (!clips.length) return null;
  const tage = Math.floor(Date.UTC(+datum.slice(0, 4), +datum.slice(5, 7) - 1, +datum.slice(8, 10)) / 86400000);
  return path.join(verzeichnis, clips[((tage % clips.length) + clips.length) % clips.length]);
}

/* Untertitel-Blöcke: 3–4 Wörter, Bruch an Satzzeichen; der Text je Block steht
   fest – nur die Farbe des gerade gesprochenen Wortes wechselt. */
export function untertitelBloecke(szenen) {
  const bloecke = [];
  for (const s of szenen) {
    let akt = [];
    for (const w of s.woerter) {
      akt.push(w);
      if (akt.length >= 4 || /[.!?:;–]$/.test(w.wort) || (akt.length >= 3 && /,$/.test(w.wort))) { bloecke.push({ szene: s.index, woerter: akt }); akt = []; }
    }
    if (akt.length) bloecke.push({ szene: s.index, woerter: akt });
  }
  /* Einzelne Wörter an den Nachbarblock hängen (erst nach vorn, sonst nach hinten). */
  for (let i = bloecke.length - 1; i >= 0; i--) {
    if (bloecke[i].woerter.length !== 1) continue;
    const n = bloecke[i + 1], v = bloecke[i - 1];
    if (n && n.szene === bloecke[i].szene && n.woerter.length <= 4) { n.woerter.unshift(...bloecke[i].woerter); bloecke.splice(i, 1); }
    else if (v && v.szene === bloecke[i].szene && v.woerter.length <= 4) { v.woerter.push(...bloecke[i].woerter); bloecke.splice(i, 1); }
  }
  return bloecke.map((b) => ({ szene: b.szene, von: b.woerter[0].von, bis: b.woerter.at(-1).bis, w: b.woerter.map((x) => ({ t: x.wort, von: x.von, bis: x.bis })) }));
}

/* Die Seite: oberes Drittel Canvas-Animation, darunter Szenen und Untertitel;
   alles über setzeZeit(t) Bild für Bild deterministisch. */
function reelHtml(reel, plan, ctx) {
  const stil = ctx.stil;
  const szenenHtml = plan.szenen.map((s) => {
    let inhalt = "";
    if (s.art === "hook") inhalt = `<div class="hook"><h1>${esc(s.titel)}</h1>${s.unter ? `<p class="unter">${esc(s.unter)}</p>` : ""}</div>`;
    else if (s.art === "schritt") inhalt = `<div class="schritt"><div class="nummer">${esc(s.nummer)}</div><div><h2>${esc(s.titel)}</h2>${s.text ? `<p class="text">${esc(s.text)}</p>` : ""}</div></div>`;
    else if (s.art === "merke") inhalt = `<div class="merkeblock"><div class="ueber">Merksatz</div><h2 class="merke-titel">${esc(s.titel)}</h2>${s.norm ? `<div class="norm">${esc(s.norm)}</div>` : ""}</div>`;
    else if (s.art === "cta") inhalt = `<div class="ctablock"><h2>${esc(s.titel)}</h2>${s.text ? `<p class="text">${esc(s.text)}</p>` : ""}<span class="pille">Folgen</span></div>`;
    else inhalt = `<div class="schritt"><div><h2>${esc(s.titel)}</h2><p class="text">${esc(s.text || "")}</p></div></div>`;
    return `<section class="szene" data-i="${s.index}" data-start="${s.start}" data-dauer="${s.dauer}">${inhalt}</section>`;
  }).join("");
  const bloecke = untertitelBloecke(plan.szenen);
  const kl = { 1: "k1", 2: "k2", 3: "k3" }[ctx.klausur] || "k3";
  const bunt = (stil.familie || stil.id) === "bunt" ? (stil.tagFarben?.[ctx.klausur] || stil.tagFarben?.[3]) : null;
  const tagFarbe = ctx.farbeJeKlausur ? stil.farben[`k${ctx.klausur}`] || stil.farben.akzent : stil.farben.akzent;
  const farben = bunt ? { wand: "rgba(255,255,255,.55)", ball: bunt.dunkel, spur: "rgba(255,255,255,.9)", ziel: bunt.akzent2, text: "#ffffff" } : { wand: stil.farben.linie || "#333", ball: tagFarbe, spur: ctx.farbeJeKlausur ? tagFarbe : (stil.farben.k3 || stil.farben.akzent), ziel: ctx.farbeJeKlausur && ctx.klausur === 2 ? stil.farben.k1 : (stil.farben.k2 || "#ff6a3d"), text: stil.farben.text };
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>${css(stil, "story")}
${ctx.clip ? "html,body{background:transparent!important}" : ""}
.reel{position:relative;width:1080px;height:1920px;overflow:hidden;background:var(--grund);font-family:var(--sans)}
.stil-campus .reel{background:radial-gradient(1300px 1100px at 30% 10%,#243070 0%,#141a3a 55%,#0e1230 100%)}
canvas#oben{position:absolute;left:0;top:0;width:1080px;height:${OBEN}px;display:block}
.trenner{position:absolute;left:0;right:0;top:${OBEN}px;height:2px;background:var(--linie)}
.fortschritt{position:absolute;left:84px;right:84px;top:${OBEN + 36}px;height:8px;border-radius:999px;background:var(--linie);overflow:hidden}
.fortschritt i{display:block;height:100%;background:var(--akzent);width:0}
.reel .kopf{position:absolute;left:84px;right:84px;top:${OBEN + 66}px;display:flex;justify-content:space-between;align-items:center}
.szene{position:absolute;left:84px;right:84px;top:${OBEN + 150}px;height:600px;opacity:0;display:flex;flex-direction:column;justify-content:center}
.szene.aktiv{opacity:1}
.hook h1{font-size:96px;margin:0;line-height:1.02}
.hook .unter{margin-top:22px;font-size:40px;line-height:1.3;color:var(--text-weich)}
.schritt{display:flex;gap:34px;align-items:center}
.schritt .nummer{font-family:var(--titel);font-size:200px;line-height:.9;color:var(--akzent);font-weight:${stil.schrift.titelGewicht};min-width:150px}
.schritt h2{font-size:82px;margin:0;line-height:1.02}
.schritt .text{margin-top:18px;font-size:40px;line-height:1.3;color:var(--text-weich);max-width:760px}
.merkeblock .ueber{font-size:30px;letter-spacing:.1em;text-transform:uppercase;color:var(--text-weich);font-weight:700}
.merke-titel{font-size:78px;margin-top:16px;line-height:1.05}
.merkeblock .norm{margin-top:26px;font-family:var(--mono);font-size:36px;color:var(--akzent);line-height:1.3}
.stil-klausurbogen .merkeblock .norm{color:var(--rot)}
.ctablock h2{font-size:86px;margin:0}
.ctablock .text{margin-top:22px;font-size:40px;color:var(--text-weich)}
.ctablock .pille{margin-top:34px;font-size:36px;padding:18px 40px}
.untertitel{position:absolute;left:60px;right:60px;top:${OBEN + 780}px;height:280px;display:flex;align-items:center;justify-content:center;text-align:center}
.untertitel .block{font-family:var(--titel);font-size:84px;line-height:1.08;text-transform:uppercase;letter-spacing:.01em;font-weight:${stil.schrift.titelGewicht};transform-origin:50% 50%;will-change:transform}
.untertitel .w{color:var(--text)}
.untertitel .w.jetzt{color:var(--akzent)}
.stil-klausurbogen .untertitel .w.jetzt{color:var(--rot)}
.familie-kanzlei .untertitel .w.jetzt{color:var(--k3)}
.reel .fuss{position:absolute;left:84px;right:84px;bottom:70px;display:flex;justify-content:space-between}
${klausurCss(ctx)}${buntCss(ctx)}
${ctx.clip ? overlayCss(ctx) : ""}
</style></head><body class="stil-${stil.id} familie-${stil.familie || stil.id}"><div class="reel">
<canvas id="oben" width="1080" height="${OBEN}"></canvas>
<div class="trenner"></div>
<div class="fortschritt"><i id="balken"></i></div>
<div class="kopf"><span class="etikett ${kl}"><i class="punkt"></i>${esc(ctx.fachLabel)}</span><span class="zaehler" id="zaehler"></span></div>
${szenenHtml}
<div class="untertitel"><div class="block" id="block"></div></div>
<div class="fuss"><span class="handle">${esc(ctx.handle || "")}</span><span class="klausur">${esc({ 1: "Klausur 1 · Tag 1", 2: "Klausur 2 · Tag 2", 3: "Klausur 3 · Tag 3" }[ctx.klausur] || "")}</span></div>
</div>
<script>
const BLOECKE = ${JSON.stringify(bloecke)};
const GESAMT = ${plan.gesamt};
const ANIM = ${JSON.stringify(ctx.clip ? "keine" : ctx.animation)};
const FARBEN = ${JSON.stringify(farben)};
const H = ${OBEN};
const szenen = [...document.querySelectorAll(".szene")].map((el) => ({ el, start: +el.dataset.start, dauer: +el.dataset.dauer, kinder: [...el.querySelectorAll("h1,h2,p,.nummer,.norm,.pille,.ueber")] }));
const ease = (x) => 1 - Math.pow(1 - Math.min(1, Math.max(0, x)), 3);
${ANIMATIONEN}
/* Einpassen: Überschriften verkleinern, bis kein Wort umbrechen muss und die Szene in ihren Rahmen passt. */
(function einpassen() {
  for (const s of szenen) {
    s.el.classList.add("aktiv");
    for (const k of s.el.querySelectorAll("h1,h2")) {
      let px = parseFloat(getComputedStyle(k).fontSize);
      for (let i = 0; i < 12 && (k.scrollWidth > k.clientWidth + 1 || s.el.scrollHeight > s.el.clientHeight + 1); i++) { px *= 0.92; k.style.fontSize = px + "px"; }
    }
    for (let i = 0; i < 8 && s.el.scrollHeight > s.el.clientHeight + 1; i++) for (const k of s.el.querySelectorAll("h1,h2,p,.norm,.nummer")) k.style.fontSize = (parseFloat(getComputedStyle(k).fontSize) * 0.94) + "px";
    s.el.classList.remove("aktiv");
  }
})();
window.setzeZeit = function (t) {
  ZEICHNER[ANIM](t);
  document.getElementById("balken").style.width = (100 * Math.min(1, t / GESAMT)) + "%";
  let aktiv = -1;
  szenen.forEach((s, i) => {
    const lokal = t - s.start; const drin = lokal >= 0 && lokal < s.dauer;
    s.el.classList.toggle("aktiv", drin); if (drin) aktiv = i; if (!drin) return;
    const aus = s.dauer - lokal; const fade = aus < 0.25 ? aus / 0.25 : 1;
    s.kinder.forEach((k, j) => { const p = ease((lokal - 0.08 * j) / 0.42); k.style.opacity = String(p * fade); k.style.transform = "translateY(" + (30 * (1 - p)) + "px)"; });
  });
  document.getElementById("zaehler").textContent = aktiv >= 0 ? (aktiv + 1) + "/" + szenen.length : "";
  /* Untertitel: fester Block, nur die Farbe des aktuellen Wortes wechselt. */
  const block = document.getElementById("block");
  const b = BLOECKE.find((x) => t >= x.von && t < x.bis + 0.18);
  if (!b || (aktiv >= 0 && b.szene !== aktiv)) { block.innerHTML = ""; block.dataset.key = ""; return; }
  const key = String(b.von);
  if (block.dataset.key !== key) { block.dataset.key = key; block.innerHTML = b.w.map((w) => '<span class="w">' + w.t.replace(/[&<>]/g, "") + "</span>").join(" "); }
  const spans = block.querySelectorAll(".w");
  b.w.forEach((w, j) => spans[j] && spans[j].classList.toggle("jetzt", t >= w.von && t < w.bis));
  const p = ease((t - b.von) / 0.14);
  block.style.transform = "scale(" + (0.94 + 0.06 * p) + ")";
};
</script></body></html>`;
}

/* Frames rendern. */
async function framesRendern(html, plan, frameDir, fps, transparent = false) {
  fs.mkdirSync(frameDir, { recursive: true });
  const b = await browserStarten();
  const page = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const tmp = path.join(frameDir, "reel.html");
  fs.writeFileSync(tmp, html);
  await page.goto(`file://${tmp}`, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  const n = Math.ceil(plan.gesamt * fps);
  for (let f = 0; f < n; f++) {
    await page.evaluate((t) => window.setzeZeit(t), f / fps);
    if (transparent) await page.screenshot({ path: path.join(frameDir, `f${String(f).padStart(5, "0")}.png`), type: "png", omitBackground: true });
    else await page.screenshot({ path: path.join(frameDir, `f${String(f).padStart(5, "0")}.jpg`), type: "jpeg", quality: 88 });
  }
  await page.close();
  fs.rmSync(tmp, { force: true });
  return n;
}

/* Dezentes Klangbett: leiser Akkord mit langsamer Bewegung, tief gefiltert. */
function klangbettFilter(dauer) {
  return `aevalsrc='0.20*sin(2*PI*110*t)*(0.6+0.4*sin(2*PI*0.11*t))+0.14*sin(2*PI*164.8*t)*(0.6+0.4*sin(2*PI*0.07*t+1))+0.10*sin(2*PI*220*t)*(0.5+0.5*sin(2*PI*0.05*t+2))+0.06*sin(2*PI*329.6*t)*(0.5+0.5*sin(2*PI*0.09*t+3))':s=48000:d=${dauer.toFixed(2)},lowpass=f=900,highpass=f=60,afade=t=in:d=1.5,afade=t=out:st=${Math.max(0, dauer - 2).toFixed(2)}:d=2,volume=0.12`;
}

/* Angaben für das Cover: Thema, Fach und Dauer stehen schon im Reel-Skript,
   ein zusätzlicher KI-Aufruf ist dafür nicht nötig. */
export function coverDaten(reel, plan) {
  const sekunden = Math.round(plan?.gesamt || 0);
  return {
    titel: reel.kurztitel || reel.szenen?.[0]?.titel || "Reel",
    ueberzeile: sekunden ? `Reel · ${sekunden} Sekunden` : "Reel",
    dauerText: sekunden ? `In ${sekunden} Sekunden erklärt` : "",
    icon: reel.szenen?.find((s) => s.icon)?.icon || "paragraf",
    fach: reel.fach,
    klausur: reel.klausur,
    fachLabel: FAECHER[reel.fach]?.label,
  };
}

/**
 * Baut das Reel. Rückgabe: { video, cover, dauer, echt }
 */
export async function reelBauen(reel, ausgabeDir, opt = {}) {
  ausgabeDir = path.resolve(ausgabeDir);
  const fps = CONFIG.reel.fps;
  const datum = opt.datum || (String(reel.slug || "").match(/^\d{4}-\d{2}-\d{2}/) || [new Date().toISOString().slice(0, 10)])[0];
  const hell = CONFIG.marke.stil === "kanzlei" && opt.variante && !CONFIG.marke.farbeJeKlausur;
  const clip = opt.clip === null ? null : (opt.clip || hintergrundClip(opt.hintergrundDir, datum));
  const ctx = { stil: stilLaden(opt.stil || (hell ? "kanzlei-hell" : CONFIG.marke.stil)), handle: CONFIG.marke.handle, klausur: reel.klausur || FAECHER[reel.fach]?.klausur || 3, fachLabel: FAECHER[reel.fach]?.label || "Steuerberaterexamen", animation: opt.animation || animationFuer(datum), farbeJeKlausur: CONFIG.marke.farbeJeKlausur, clip };
  fs.mkdirSync(ausgabeDir, { recursive: true });
  const plan = await zeitplanErstellen(reel, path.join(ausgabeDir, "audio"), { stimmeId: opt.stimmeId || null, stimmeName: opt.stimmeName || null });
  const frameDir = path.join(ausgabeDir, "frames");
  const n = await framesRendern(reelHtml(reel, plan, ctx), plan, frameDir, fps, !!clip);

  const video = path.join(ausgabeDir, `${reel.slug || "reel"}.mp4`);
  const cover = path.join(ausgabeDir, `${reel.slug || "reel"}-cover.jpg`);
  const frames = path.join(frameDir, clip ? "f%05d.png" : "f%05d.jpg");
  /* Mit Clip: Eingabe 0 = geloopter Hintergrund, Eingabe 1 = transparente Frames. */
  const args = ["-y", "-hide_banner", "-loglevel", "error"];
  if (clip) args.push("-stream_loop", "-1", "-i", clip);
  args.push("-framerate", String(fps), "-i", frames);
  const vEingaben = clip ? 2 : 1;
  const audioEingaben = plan.szenen.filter((s) => s.audio);
  for (const s of audioEingaben) args.push("-i", s.audio);
  const filter = [];
  const mix = [];
  if (clip) filter.push(`[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=${fps},setpts=PTS-STARTPTS[bg]`, `[bg][1:v]overlay=0:0:shortest=1[vout]`);
  audioEingaben.forEach((s, k) => { filter.push(`[${k + vEingaben}:a]aresample=48000,adelay=${Math.round(s.audioStart * 1000)}|${Math.round(s.audioStart * 1000)},apad=whole_dur=${plan.gesamt.toFixed(2)}[v${k}]`); mix.push(`[v${k}]`); });
  if (CONFIG.reel.hintergrundmusik) { filter.push(`${klangbettFilter(plan.gesamt)}[bett]`); mix.push("[bett]"); }
  const videoMap = clip ? "[vout]" : "0:v";
  if (mix.length) {
    filter.push(`${mix.join("")}amix=inputs=${mix.length}:normalize=0:duration=first,alimiter=limit=0.95[aout]`);
    args.push("-filter_complex", filter.join(";"), "-map", videoMap, "-map", "[aout]", "-c:a", "aac", "-b:a", "160k", "-ar", "48000");
  } else {
    if (filter.length) args.push("-filter_complex", filter.join(";"));
    args.push("-map", videoMap, "-an");
  }
  args.push("-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", String(fps), "-t", plan.gesamt.toFixed(2), "-movflags", "+faststart", video);
  execFileSync(ffmpegPfad(), args, { stdio: ["ignore", "pipe", "pipe"] });
  /* Cover: eigenes Standbild mit Thema, Fach und Dauer. Im Feed und im
     Profilraster soll auf einen Blick zu sehen sein, worum es geht; ein Bild
     aus dem Video zeigt sonst nur den Hintergrundclip. Klappt das Rendern
     nicht, bleibt der bisherige Weg über ein Videobild. */
  try {
    await coverRendern(coverDaten(reel, plan), cover);
  } catch (e) {
    console.warn(`  ! Cover nicht gerendert (${e.message}) – nehme ein Bild aus dem Video.`);
    const coverFrame = Math.min(n - 1, Math.round(0.9 * fps));
    if (clip) execFileSync(ffmpegPfad(), ["-y", "-hide_banner", "-loglevel", "error", "-ss", (coverFrame / fps).toFixed(2), "-i", video, "-frames:v", "1", "-q:v", "3", cover], { stdio: ["ignore", "pipe", "pipe"] });
    else fs.copyFileSync(path.join(frameDir, `f${String(coverFrame).padStart(5, "0")}.jpg`), cover);
  }
  if (!opt.framesBehalten) fs.rmSync(frameDir, { recursive: true, force: true });
  return { video, cover, dauer: plan.gesamt, echt: plan.echt, anbieter: plan.anbieter, stimmeId: plan.stimmeId, stimmeName: plan.stimmeName || null, szenen: plan.szenen.length, animation: clip ? `Clip ${path.basename(clip)}` : ctx.animation };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const datei = process.argv[2] || new URL("../beispiele/reel.json", import.meta.url).pathname;
  const reel = JSON.parse(fs.readFileSync(datei, "utf8"));
  const ziel = process.argv[3] || new URL("../beispiele/reel-out", import.meta.url).pathname;
  const t0 = Date.now();
  const animArg = process.argv.find((a) => a.startsWith("--animation="))?.split("=")[1];
  const clipArg = process.argv.find((a) => a.startsWith("--clip="))?.split("=")[1];
  const r = await reelBauen(reel, ziel, { framesBehalten: process.argv.includes("--frames"), animation: animArg, variante: process.argv.includes("--hell") ? 1 : 0, clip: clipArg === "keine" ? null : clipArg });
  console.log(`${r.video} · ${r.dauer.toFixed(1)} s · ${r.szenen} Szenen · Stimme: ${r.anbieter} · Animation: ${r.animation} · ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  const { browserBeenden } = await import("./render.mjs");
  await browserBeenden();
}
