/* ==========================================================================
   Rendert Folien und Stories mit Chromium (Playwright) als JPEG.
   Instagram akzeptiert für Bilder nur JPEG; 1080×1350 (4:5) und 1080×1920.
   ========================================================================== */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { chromium } from "playwright";
import { folieHtml, storyHtml, coverHtml, MASSE } from "./vorlagen.mjs";
import { stil as stilLaden, stilFuer } from "./stile.mjs";
import { FAECHER } from "./inhalte.mjs";
import { CONFIG } from "./config.mjs";

let browser = null;

export async function browserStarten() {
  if (browser) return browser;
  const executablePath = process.env.CHROMIUM_PATH || undefined;
  browser = await chromium.launch({ executablePath, args: ["--font-render-hinting=none"] });
  return browser;
}

export async function browserBeenden() {
  if (browser) { await browser.close(); browser = null; }
}

export function kontext(opt = {}) {
  const basis = opt.stil || CONFIG.marke.stil;
  const wechsel = CONFIG.marke.stilWechsel && !CONFIG.marke.farbeJeKlausur;
  const stilName = opt.variante != null ? stilFuer(basis, opt.variante, wechsel) : basis;
  return {
    stil: stilLaden(stilName),
    farbeJeKlausur: CONFIG.marke.farbeJeKlausur,
    handle: opt.handle ?? CONFIG.marke.handle,
    fach: opt.fach || null,
    fachLabel: opt.fachLabel || (opt.fach ? FAECHER[opt.fach]?.label : "Examenswissen") || "Examenswissen",
    /* ?? statt ||: Klausurtag 0 ist ein gültiger Wert (Mindset, Kopfsache)
       und darf nicht zu 3 werden - sonst erscheint ein Mindset-Beitrag in der
       Farbe und mit dem Etikett des dritten Prüfungstags. */
    klausur: opt.klausur ?? (opt.fach ? FAECHER[opt.fach]?.klausur : 3) ?? 3,
  };
}

async function htmlZuJpeg(html, masse, zielPfad, skala = Number(process.env.IG_RENDER_SKALA || 1), messen = null) {
  const b = await browserStarten();
  const page = await b.newPage({ viewport: { width: masse.breite, height: masse.hoehe }, deviceScaleFactor: skala });
  const tmp = path.join(os.tmpdir(), `ig-${process.pid}-${Math.random().toString(36).slice(2)}.html`);
  fs.writeFileSync(tmp, html);
  let kasten = null;
  try {
    await page.goto(`file://${tmp}`, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(einpassen);
    await page.evaluate(coverTitelGeometriePruefen);
    await page.evaluate(coverHinweisAusPlanPlatzieren);
    await page.waitForTimeout(60);
    /* NACH dem Einpassen messen: Der Text wird dort verkleinert, bis alles
       oberhalb der Fußzeile bleibt - vorher gemessen wäre der Kasten falsch. */
    if (messen) kasten = await page.locator(messen).first().boundingBox().catch(() => null);
    fs.mkdirSync(path.dirname(zielPfad), { recursive: true });
    await page.screenshot({ path: zielPfad, type: "jpeg", quality: skala < 1 ? 80 : 92, fullPage: false });
  } finally {
    await page.close();
    fs.rmSync(tmp, { force: true });
  }
  return messen ? { pfad: zielPfad, kasten } : zielPfad;
}

/* Titelpillen sind feste Marken-Geometrie. Anders als normale Folientexte
   werden sie nicht nachträglich kleingerechnet. Falls eine semantische Zeile
   trotz der vorherigen Zeilen-Normalisierung noch aus der Pille läuft, ist das
   ein redaktioneller Fehler und kein Anlass für stilles CSS-Schrumpfen. */
function coverTitelGeometriePruefen() {
  const wurzel = document.querySelector(".folie.art-titel");
  const titel = wurzel?.querySelector("h1.titel-stack");
  if (!wurzel || !titel) return;
  const root = wurzel.getBoundingClientRect();
  const rechts = root.right - 52;
  const fehler = [];
  for (const zeile of titel.querySelectorAll(".titel-zeile")) {
    const box = zeile.getBoundingClientRect();
    if (zeile.scrollWidth > zeile.clientWidth + 1 || box.right > rechts + 1) {
      fehler.push(String(zeile.textContent || "").trim());
    }
  }
  if (fehler.length) throw new Error(`Cover-Titelzeile passt nicht in die feste Markenpille: ${fehler.join(" | ")}`);
}

/* Setzt die Handschrift exakt nach dem von der visuellen KI-QA gelieferten
   Plan. Keine Zonensuche und kein eigenes Kompositions-Scoring: Der Renderer
   mappt nur die normalisierten KI-Koordinaten auf das tatsächlich dargestellte
   transparente Motiv und hält Text/Pfeil innerhalb der technischen Safe Area. */
function coverHinweisAusPlanPlatzieren() {
  const wurzel = document.querySelector(".folie.art-titel");
  const hinweis = wurzel?.querySelector(".cover-hinweis");
  const svg = wurzel?.querySelector(".cover-hinweis-pfeil");
  const pfad = svg?.querySelector(".cover-hinweis-kurve");
  const spitze = svg?.querySelector(".cover-hinweis-spitze");
  const img = wurzel?.querySelector(".frei.charakter img, .frei img");
  if (!wurzel || !hinweis || !svg || !pfad || !spitze || !img?.complete || !img.naturalWidth || !img.naturalHeight) return;

  const root = wurzel.getBoundingClientRect();
  const ir = img.getBoundingClientRect();
  const scale = Math.min(ir.width / img.naturalWidth, ir.height / img.naturalHeight);
  const dw = img.naturalWidth * scale;
  const dh = img.naturalHeight * scale;
  const cs = getComputedStyle(img);
  const pos = String(cs.objectPosition || "50% 50%").toLowerCase().split(/\s+/);
  const faktor = (wert, achse) => {
    if (wert === "left" || wert === "top") return 0;
    if (wert === "right" || wert === "bottom") return 1;
    if (wert === "center") return 0.5;
    if (/%$/.test(wert)) return Math.max(0, Math.min(1, parseFloat(wert) / 100));
    const n = parseFloat(wert);
    return Number.isFinite(n) ? Math.max(0, Math.min(1, n / Math.max(1, achse))) : 0.5;
  };
  const ox = ir.left + (ir.width - dw) * faktor(pos[0] || "50%", ir.width);
  const oy = ir.top + (ir.height - dh) * faktor(pos[1] || pos[0] || "50%", ir.height);

  const n = (k, f) => Number.isFinite(Number(hinweis.dataset[k])) ? Number(hinweis.dataset[k]) : f;
  const geplantX = ox + n("noteX", 0.25) * dw;
  const geplantY = oy + n("noteY", 0.28) * dh;
  const tx = ox + n("targetX", 0.5) * dw;
  const ty = oy + n("targetY", 0.55) * dh;
  const rotation = Math.max(-12, Math.min(12, n("rotation", -4)));
  const bend = Math.max(-1, Math.min(1, n("bend", 0.35)));

  const titel = wurzel.querySelector("h1.titel-stack, h1");
  const badge = wurzel.querySelector(".cover-badge");
  const fuss = wurzel.querySelector(".fuss");
  const minTop = Math.max(titel?.getBoundingClientRect().bottom || root.top, badge?.getBoundingClientRect().bottom || root.top) + 14;
  const maxBottom = (fuss?.getBoundingClientRect().top || root.bottom - 18) - 12;
  const minLeft = root.left + 24;
  const maxRight = root.right - 24;

  /* Transparenzmaske des tatsaechlichen KI-Motivs. Data-URI/PNG-Motive koennen
     direkt gelesen werden. Falls ein Browser das Canvas wegen der Bildquelle
     sperrt, bleibt die Platzierung geometrisch sicher und faellt auf die
     KI-Wunschposition zurueck. */
  let alpha = null;
  let alphaBreite = 0;
  let alphaHoehe = 0;
  try {
    const canvas = document.createElement("canvas");
    alphaBreite = img.naturalWidth;
    alphaHoehe = img.naturalHeight;
    canvas.width = alphaBreite;
    canvas.height = alphaHoehe;
    const ctx = canvas.getContext("2d", { willReadFrequently: true });
    ctx.drawImage(img, 0, 0);
    alpha = ctx.getImageData(0, 0, alphaBreite, alphaHoehe).data;
  } catch {
    alpha = null;
  }

  const alphaAn = (px, py) => {
    if (!alpha) return 0;
    if (px < ox || px > ox + dw || py < oy || py > oy + dh) return 0;
    const ix = Math.max(0, Math.min(alphaBreite - 1, Math.round((px - ox) / Math.max(1, dw) * (alphaBreite - 1))));
    const iy = Math.max(0, Math.min(alphaHoehe - 1, Math.round((py - oy) / Math.max(1, dh) * (alphaHoehe - 1))));
    return alpha[(iy * alphaBreite + ix) * 4 + 3] / 255;
  };

  const belegungRechteck = (cx, cy, breite, hoehe) => {
    if (!alpha) return 0;
    const randX = 16, randY = 12;
    const l = cx - breite / 2 - randX;
    const r = cx + breite / 2 + randX;
    const o = cy - hoehe / 2 - randY;
    const u = cy + hoehe / 2 + randY;
    let belegt = 0, gesamt = 0;
    const spalten = 13, zeilen = 7;
    for (let yy = 0; yy < zeilen; yy++) {
      const py = o + (u - o) * (yy + 0.5) / zeilen;
      for (let xx = 0; xx < spalten; xx++) {
        const px = l + (r - l) * (xx + 0.5) / spalten;
        gesamt++;
        if (alphaAn(px, py) > 0.12) belegt++;
      }
    }
    return gesamt ? belegt / gesamt : 0;
  };

  /* Zuerst nur zur Groessenmessung an der KI-Wunschposition rendern. Danach
     wird die naechste wirklich freie Flaeche gesucht. */
  hinweis.style.left = `${geplantX - root.left}px`;
  hinweis.style.top = `${geplantY - root.top}px`;
  hinweis.style.transform = `translate(-50%,-50%) rotate(${rotation}deg)`;
  let hr = hinweis.getBoundingClientRect();
  const noteW = Math.max(80, hr.width);
  const noteH = Math.max(42, hr.height);

  const passtTechnisch = (cx, cy) =>
    cx - noteW / 2 >= minLeft
    && cx + noteW / 2 <= maxRight
    && cy - noteH / 2 >= minTop
    && cy + noteH / 2 <= maxBottom;

  const kandidatScore = (cx, cy) => {
    if (!passtTechnisch(cx, cy)) return Infinity;
    const belegung = belegungRechteck(cx, cy, noteW, noteH);
    const abstandPlan = Math.hypot(cx - geplantX, cy - geplantY);
    const abstandZiel = Math.hypot(cx - tx, cy - ty);
    /* Belegung dominiert deutlich. Distanz ist nur Tie-Breaker, damit der
       Hinweis moeglichst nahe an der KI-Idee und der Handlung bleibt. */
    return belegung * 100000 + abstandPlan * 0.34 + abstandZiel * 0.08;
  };

  let x = geplantX;
  let y = geplantY;
  let besterScore = kandidatScore(x, y);

  if (alpha) {
    const schrittX = 34;
    const schrittY = 30;
    const startX = minLeft + noteW / 2;
    const endeX = maxRight - noteW / 2;
    const startY = minTop + noteH / 2;
    const endeY = maxBottom - noteH / 2;
    for (let cy = startY; cy <= endeY; cy += schrittY) {
      for (let cx = startX; cx <= endeX; cx += schrittX) {
        const score = kandidatScore(cx, cy);
        if (score < besterScore) {
          besterScore = score;
          x = cx;
          y = cy;
        }
      }
    }
  }

  /* Letzte technische Korrektur an der Safe Area; keine kreative Zonenlogik. */
  x = Math.max(minLeft + noteW / 2, Math.min(maxRight - noteW / 2, x));
  y = Math.max(minTop + noteH / 2, Math.min(maxBottom - noteH / 2, y));
  hinweis.style.left = `${x - root.left}px`;
  hinweis.style.top = `${y - root.top}px`;
  hinweis.style.transform = `translate(-50%,-50%) rotate(${rotation}deg)`;
  hr = hinweis.getBoundingClientRect();

  const cx = (hr.left + hr.right) / 2;
  const cy = (hr.top + hr.bottom) / 2;
  const dx = tx - cx, dy = ty - cy;
  const hw = Math.max(1, hr.width / 2 + 8), hh = Math.max(1, hr.height / 2 + 8);
  const ax = Math.abs(dx) > 0.001 ? hw / Math.abs(dx) : Infinity;
  const ay = Math.abs(dy) > 0.001 ? hh / Math.abs(dy) : Infinity;
  const edge = Math.min(ax, ay, 1);
  const startX = cx + dx * edge;
  const startY = cy + dy * edge;
  const laenge = Math.max(1, Math.hypot(tx - startX, ty - startY));
  const normalX = -(ty - startY) / laenge;
  const normalY = (tx - startX) / laenge;

  const pfeilGeometrie = (biegung) => {
    const mx = (startX + tx) / 2;
    const my = (startY + ty) / 2;
    const krumm = Math.min(155, laenge * 0.30) * biegung;
    return {
      ctrlX: mx + normalX * krumm,
      ctrlY: my + normalY * krumm,
      biegung,
    };
  };

  const punktAufKurve = (g, t) => {
    const q = 1 - t;
    return {
      x: q * q * startX + 2 * q * t * g.ctrlX + t * t * tx,
      y: q * q * startY + 2 * q * t * g.ctrlY + t * t * ty,
    };
  };

  const pfeilScore = (g) => {
    if (!alpha) return Math.abs(g.biegung - bend);
    let kollision = 0;
    let ausserhalb = 0;
    /* Die letzten 18 % duerfen in das Zielobjekt laufen - genau dort soll die
       Pfeilspitze ja landen. Der restliche Pfeil soll rechnerisch frei bleiben. */
    for (let i = 1; i <= 20; i++) {
      const t = i / 25; // bis 0.80
      const p = punktAufKurve(g, t);
      if (p.x < minLeft || p.x > maxRight || p.y < minTop || p.y > maxBottom) ausserhalb++;
      if (alphaAn(p.x, p.y) > 0.12) kollision++;
      /* Auch etwas neben der Mittellinie pruefen: ein 7px-Strich braucht
         realen Freiraum, nicht nur einen einzigen transparenten Pixelpfad. */
      if (alphaAn(p.x + normalX * 7, p.y + normalY * 7) > 0.12) kollision++;
      if (alphaAn(p.x - normalX * 7, p.y - normalY * 7) > 0.12) kollision++;
    }
    return kollision * 1000 + ausserhalb * 5000 + Math.abs(g.biegung - bend) * 18;
  };

  const biegungen = [...new Set([
    bend,
    Math.max(-1, Math.min(1, bend + 0.28)),
    Math.max(-1, Math.min(1, bend - 0.28)),
    Math.max(-1, Math.min(1, bend + 0.55)),
    Math.max(-1, Math.min(1, bend - 0.55)),
    0,
    0.75,
    -0.75,
  ].map((z) => Number(z.toFixed(2))))];

  let g = pfeilGeometrie(biegungen[0]);
  let gScore = pfeilScore(g);
  for (const b of biegungen.slice(1)) {
    const kandidat = pfeilGeometrie(b);
    const score = pfeilScore(kandidat);
    if (score < gScore) {
      g = kandidat;
      gScore = score;
    }
  }

  hinweis.dataset.freeScore = String(Number(besterScore.toFixed(2)));
  hinweis.dataset.arrowFreeScore = String(Number(gScore.toFixed(2)));

  const rel = (a, b) => [a - root.left, b - root.top].map((v) => Number(v.toFixed(1)));
  const [sx2, sy2] = rel(startX, startY);
  const [cx2, cy2] = rel(g.ctrlX, g.ctrlY);
  const [tx2, ty2] = rel(tx, ty);
  pfad.setAttribute("d", `M ${sx2} ${sy2} Q ${cx2} ${cy2} ${tx2} ${ty2}`);

  /* Offene, handgezeichnete Pfeilspitze wie in den Golden References. */
  const tangentX = tx - g.ctrlX;
  const tangentY = ty - g.ctrlY;
  const tangentLen = Math.max(1, Math.hypot(tangentX, tangentY));
  const ux = tangentX / tangentLen;
  const uy = tangentY / tangentLen;
  const nx = -uy;
  const ny = ux;
  const kopfLaenge = 30;
  const fluegel = 16;
  const basisX = tx - ux * kopfLaenge;
  const basisY = ty - uy * kopfLaenge;
  const [a1x, a1y] = rel(basisX + nx * fluegel, basisY + ny * fluegel);
  const [a2x, a2y] = rel(basisX - nx * fluegel, basisY - ny * fluegel);
  spitze.setAttribute("d", `M ${a1x} ${a1y} L ${tx2} ${ty2} L ${a2x} ${a2y}`);
}

/* Läuft im Browser: verkleinert Text, bis nichts mehr über den rechten Rand
   hinausragt und der Inhalt oberhalb der Fußzeile bleibt. */
function einpassen() {
  const wurzel = document.querySelector(".folie, .story");
  if (!wurzel) return;
  const px = (el) => parseFloat(getComputedStyle(el).fontSize);
  /* Untergrenzen: Ein Titel auf der ersten Folie darf nie unter 64 px fallen –
     darunter ist er im Feed-Vorschaubild nicht mehr zu entziffern, und dann
     nützt der beste Text nichts. Der Rest der Kachel darf weiter schrumpfen. */
  const untergrenze = (el) => (el.tagName === "H1" ? 64 : 28);
  const setze = (el, f) => { el.style.fontSize = `${Math.max(untergrenze(el), px(el) * f)}px`; };
  /* 1. Einzelne Zeilen/Blöcke, die breiter als ihr Platz sind (lange Wörter).
        Neben dem eigenen Überlauf zählt der rechte Rand der Kachel: Elemente
        mit „width:fit-content“ (im bunten Stil etwa die Titelpille) wachsen
        sonst über die Kachel hinaus, ohne selbst zu überlaufen. */
  const innenRechts = wurzel.getBoundingClientRect().right - parseFloat(getComputedStyle(wurzel).paddingRight || 0);
  /* Breitestes einzelnes Wort eines Elements. scrollWidth genuegt dafuer
     nicht: Ein Kasten mit width:fit-content und einer Hoechstbreite - im
     bunten Stil traegt die Story-Ueberschrift beides - meldet scrollWidth
     gleich clientWidth, obwohl das Wort darin laengst ueber den farbigen
     Grund hinausragt. Genau so stand am 13.09. „Vollstreckungsklausel" 50
     Pixel weit neben seiner Pille. Gemessen wird deshalb direkt am Text. */
  const breitestesWort = (el) => {
    const bereich = document.createRange();
    let breit = 0;
    const lauf = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let k = lauf.nextNode(); k; k = lauf.nextNode()) {
      const text = k.nodeValue;
      for (const treffer of text.matchAll(/\S+/g)) {
        bereich.setStart(k, treffer.index);
        bereich.setEnd(k, treffer.index + treffer[0].length);
        breit = Math.max(breit, bereich.getBoundingClientRect().width);
      }
    }
    return breit;
  };
  for (const el of wurzel.querySelectorAll("h1:not(.titel-stack),h2,h3,.merke,.norm,.zahl-unter,.karte .t,.pille,.ueberzeile,.formel,.zeile")) {
    let n = 0;
    const passtNicht = () => el.scrollWidth > el.clientWidth + 1
      || el.getBoundingClientRect().right > innenRechts + 1
      || breitestesWort(el) > el.clientWidth + 1;
    while (passtNicht() && n++ < 20) setze(el, 0.94);
  }
  /* 2. Gesamthöhe: Fußzeile muss innerhalb der Kachel bleiben. Liegt ein Foto
        auf der Kachel, ist dessen Oberkante die Grenze – sonst schiebt sich
        der Titel darüber und wird unlesbar. */
  const fuss = wurzel.querySelector(".fuss");
  const foto = wurzel.querySelector(".foto");
  const frei = wurzel.querySelector(".frei");
  /* Beim freigestellten Motiv darf der Text bis zu dessen Oberkante laufen –
     es ist transparent, ein bisschen Ueberlappung oben schadet nicht. */
  const grenze = foto ? foto.getBoundingClientRect().top - 16
    : wurzel.getBoundingClientRect().bottom - 24;
  const textElemente = [...wurzel.querySelectorAll("h1:not(.titel-stack),h2,h3,p,li,.text,.merke,.norm,.zahl,.zahl-unter,.karte,.optionen div,.rechnung,.spalte,.unter,.hinweis,.pfeil")];
  let n = 0;
  /* Absolut gesetzte Buehnenelemente zaehlen nicht als Inhalt: Das farbige
     Zeichen neben dem Motiv (frei-zeichen) steht bewusst unterhalb der
     Textgrenze - wuerde es mitgezaehlt, schrumpfte der Titel 14 Runden lang
     bis auf die Untergrenze, obwohl er laengst passt. */
  const ausser = (c) => ["geist", "illu", "foto", "frei", "frei-zeichen", "bildquelle", "cover-hinweis", "cover-hinweis-pfeil", "fuss"].some((k) => c.classList.contains(k));
  const passt = () => {
    const unten = Math.max(...textElemente.map((e) => e.getBoundingClientRect().bottom));
    const kinderUnten = Math.max(...[...wurzel.children].filter((c) => !ausser(c)).map((c) => c.getBoundingClientRect().bottom));
    const fussOk = foto || frei || !fuss || fuss.getBoundingClientRect().bottom <= wurzel.getBoundingClientRect().bottom - 8;
    return unten <= grenze + 24 && kinderUnten <= grenze + 24 && fussOk && wurzel.scrollHeight <= wurzel.clientHeight + 1;
  };
  while (!passt() && n++ < 14) for (const el of textElemente) setze(el, 0.95);
}

/* Harte Markenregel: Nur das Cover eines Karussells darf ein Foto tragen.
   Alte gespeicherte Inhalte und spätere Prompt-Änderungen können damit kein
   Bild auf eine innere Lernfolie schleusen. */
export function carouselBildregeln(beitrag) {
  if (!beitrag?.folien?.length) return beitrag;
  const bildFelder = ["bild", "bildQuelle", "bildFrei", "bildBreite", "bildHoehe", "bildTyp", "coverHinweisPlan"];
  for (let i = 1; i < beitrag.folien.length; i++) {
    for (const feld of bildFelder) delete beitrag.folien[i][feld];
  }
  return beitrag;
}
/* Rendert alle Folien eines Beitrags → Liste der JPEG-Pfade. */
export async function beitragRendern(beitrag, zielVerzeichnis, opt = {}) {
  carouselBildregeln(beitrag);
  const ctx = kontext({ ...opt, fach: beitrag.fach, klausur: beitrag.klausur, fachLabel: beitrag.fachLabel, variante: opt.variante ?? beitrag.variante });
  const pfade = [];
  const n = beitrag.folien.length;
  for (let i = 0; i < n; i++) {
    const folie = beitrag.folien[i];
    const html = folieHtml(folie, ctx, i + 1, n);
    const ziel = path.join(zielVerzeichnis, `${beitrag.slug || "beitrag"}-${String(i + 1).padStart(2, "0")}.jpg`);
    pfade.push(await htmlZuJpeg(html, MASSE.beitrag, ziel));
  }
  return pfade;
}

export async function storyRendern(story, zielPfad, opt = {}) {
  const ctx = kontext({ ...opt, fach: story.fach, klausur: story.klausur, fachLabel: story.fachLabel, variante: opt.variante ?? story.variante });
  return htmlZuJpeg(storyHtml(story, ctx), MASSE.story, zielPfad);
}

/* Interaktive Fassung einer Story: rendert wie storyRendern und misst
   zusätzlich den freigehaltenen Streifen für den Umfrage-Sticker. Bewusst eine
   eigene Funktion statt eines weiteren Rückgabewerts von storyRendern - die
   Zusage "gibt einen Pfad zurück" haben dort schon mehrere Aufrufer. */
export async function storyRendernInteraktiv(story, zielPfad, opt = {}) {
  const ctx = kontext({ ...opt, fach: story.fach, klausur: story.klausur, fachLabel: story.fachLabel, variante: opt.variante ?? story.variante });
  const { pfad, kasten } = await htmlZuJpeg(
    storyHtml({ ...story, interaktiv: true }, ctx), MASSE.story, zielPfad,
    Number(process.env.IG_RENDER_SKALA || 1), ".umfrageplatz",
  );
  return { pfad, platz: kasten, masse: MASSE.story };
}

/* Cover eines Reels (Standbild für Feed und Profilraster). */
export async function coverRendern(daten, zielPfad, opt = {}) {
  const ctx = kontext({ ...opt, fach: daten.fach, klausur: daten.klausur, fachLabel: daten.fachLabel });
  return htmlZuJpeg(coverHtml(daten, ctx), MASSE.story, zielPfad);
}
