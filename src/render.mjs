/* ==========================================================================
   Rendert Folien und Stories mit Chromium (Playwright) als JPEG.
   Instagram akzeptiert für Bilder nur JPEG; 1080×1350 (4:5) und 1080×1920.
   ========================================================================== */

import fs from "node:fs";
import crypto from "node:crypto";
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
    await page.evaluate(coverTitelEinpassen);
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

/* Cover-Titel haben wenige klar definierte Markengrößen. Für Reel-Cover
   reichte die Zeichenanzahl allein nicht: breite Buchstabenfolgen liefen trotz
   plausibler Zeilenlänge rechts aus dem 1080er Canvas. Deshalb messen wir die
   reale Browser-Geometrie und reduzieren nur den gesamten Titelblock in kleinen
   Schritten. Unterhalb der Lesbarkeitsgrenze wird hart abgebrochen. */
function coverTitelEinpassen() {
  const wurzel = document.querySelector(".folie.art-titel, .story.cover");
  const titel = wurzel?.querySelector("h1.titel-stack");
  if (!wurzel || !titel) return;

  const root = wurzel.getBoundingClientRect();
  const cs = getComputedStyle(wurzel);
  const rechts = root.right - Math.max(24, parseFloat(cs.paddingRight || 0));
  const links = root.left + Math.max(24, parseFloat(cs.paddingLeft || 0));
  const mindest = wurzel.matches(".story.cover") ? 84 : 78;

  const passt = () => [...titel.querySelectorAll(".titel-zeile")].every((zeile) => {
    const box = zeile.getBoundingClientRect();
    return zeile.scrollWidth <= zeile.clientWidth + 1
      && box.left >= links - 1
      && box.right <= rechts + 1;
  });

  let groesse = parseFloat(getComputedStyle(titel).fontSize);
  let n = 0;
  while (!passt() && groesse > mindest + 0.5 && n++ < 16) {
    groesse = Math.max(mindest, groesse * 0.94);
    titel.style.fontSize = `${groesse}px`;
  }
  titel.dataset.autoFitPx = String(Math.round(groesse * 10) / 10);
}

/* Harte Endkontrolle für BEIDE Covertypen. Früher wurde nur
   .folie.art-titel geprüft; .story.cover (Reels) konnte deshalb unbemerkt
   abgeschnitten exportiert werden und bestand sogar den Layout-Preflight. */
function coverTitelGeometriePruefen() {
  const wurzel = document.querySelector(".folie.art-titel, .story.cover");
  const titel = wurzel?.querySelector("h1.titel-stack");
  if (!wurzel || !titel) return;
  const root = wurzel.getBoundingClientRect();
  const cs = getComputedStyle(wurzel);
  const rechts = root.right - Math.max(24, parseFloat(cs.paddingRight || 0));
  const links = root.left + Math.max(24, parseFloat(cs.paddingLeft || 0));
  const fehler = [];
  for (const zeile of titel.querySelectorAll(".titel-zeile")) {
    const box = zeile.getBoundingClientRect();
    if (zeile.scrollWidth > zeile.clientWidth + 1 || box.left < links - 1 || box.right > rechts + 1) {
      fehler.push(String(zeile.textContent || "").trim());
    }
  }
  if (fehler.length) {
    const art = wurzel.matches(".story.cover") ? "Reel-Cover" : "Beitrags-Cover";
    throw new Error(`${art}-Titel passt nicht in die feste Markenpille: ${fehler.join(" | ")}`);
  }
}

/* Setzt den handschriftlichen Hinweis nach dem von der visuellen KI-QA
   gelieferten Plan. Cover-v2 zeichnet bewusst keinen Pfeil mehr. */
function coverHinweisAusPlanPlatzieren() {
  const wurzel = document.querySelector(".folie.art-titel");
  const hinweis = wurzel?.querySelector(".cover-hinweis");
  const img = wurzel?.querySelector(".frei.charakter img, .frei img");
  if (!wurzel || !hinweis || !img?.complete || !img.naturalWidth || !img.naturalHeight) return;

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

  hinweis.dataset.freeScore = String(Number(besterScore.toFixed(2)));
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
async function freigegebenesBeitragsCoverLaden(beitrag, ziel) {
  const u = new URL(String(beitrag?.coverFinalUrl || ""));
  if (u.protocol !== "https:" || u.hostname !== "raw.githubusercontent.com") {
    throw new Error("Freigegebenes Beitrags-Cover muss von raw.githubusercontent.com stammen.");
  }
  const erwartet = String(beitrag?.coverFinalSha256 || "").toLowerCase();
  if (!/^[a-f0-9]{64}$/.test(erwartet)) {
    throw new Error("Freigegebenes Beitrags-Cover braucht coverFinalSha256.");
  }
  const r = await fetch(u);
  if (!r.ok) throw new Error(`Freigegebenes Beitrags-Cover nicht ladbar: HTTP ${r.status}`);
  const daten = Buffer.from(await r.arrayBuffer());
  const jpeg = daten.length > 10_000 && daten[0] === 0xff && daten[1] === 0xd8;
  if (!jpeg) throw new Error("Freigegebenes Beitrags-Cover ist keine plausible JPEG-Datei.");
  const ist = crypto.createHash("sha256").update(daten).digest("hex");
  if (ist !== erwartet) {
    throw new Error(`Freigegebenes Beitrags-Cover hat falschen SHA-256: erwartet ${erwartet}, erhalten ${ist}`);
  }
  fs.mkdirSync(path.dirname(ziel), { recursive: true });
  fs.writeFileSync(ziel, daten);
  return ziel;
}

/* Rendert alle Folien eines Beitrags → Liste der JPEG-Pfade. */
export async function beitragRendern(beitrag, zielVerzeichnis, opt = {}) {
  carouselBildregeln(beitrag);
  const ctx = kontext({ ...opt, fach: beitrag.fach, klausur: beitrag.klausur, fachLabel: beitrag.fachLabel, variante: opt.variante ?? beitrag.variante });
  const pfade = [];
  const n = beitrag.folien.length;
  for (let i = 0; i < n; i++) {
    const folie = beitrag.folien[i];
    const ziel = path.join(zielVerzeichnis, `${beitrag.slug || "beitrag"}-${String(i + 1).padStart(2, "0")}.jpg`);
    if (i === 0 && beitrag.coverFinalUrl) {
      pfade.push(await freigegebenesBeitragsCoverLaden(beitrag, ziel));
      continue;
    }
    const html = folieHtml(folie, ctx, i + 1, n);
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
