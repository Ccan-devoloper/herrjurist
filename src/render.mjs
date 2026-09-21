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
    await page.evaluate(coverHinweisPlatzieren);
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

/* Positioniert den handschriftlichen Cover-Hinweis erst NACH dem Text-Fit.
   Es gibt bewusst keine festen Koordinaten pro Fach oder Szene: mehrere
   plausible Zonen werden anhand des tatsaechlich gerenderten Motivs bewertet.
   Die Wunschzone aus der Regie ist nur ein kleiner Bonus. */
function coverHinweisPlatzieren() {
  const wurzel = document.querySelector(".folie.art-titel");
  const hinweis = wurzel?.querySelector(".cover-hinweis");
  if (!wurzel || !hinweis) return;

  const text = hinweis.querySelector(".cover-hinweis-text");
  const pfeil = hinweis.querySelector(".cover-hinweis-pfeil");
  if (!text || !pfeil) return;

  const root = wurzel.getBoundingClientRect();
  const titel = wurzel.querySelector("h1.titel-stack, h1");
  const badge = wurzel.querySelector(".cover-badge");
  const kopf = wurzel.querySelector(".kopf");
  const fuss = wurzel.querySelector(".fuss");
  const img = wurzel.querySelector(".frei.charakter img, .frei img");

  const clamp = (n, a, b) => Math.max(a, Math.min(b, n));
  const flaeche = (a, b, rand = 0) => {
    if (!a || !b) return 0;
    const l = Math.max(a.left - rand, b.left);
    const r = Math.min(a.right + rand, b.right);
    const o = Math.max(a.top - rand, b.top);
    const u = Math.min(a.bottom + rand, b.bottom);
    return Math.max(0, r - l) * Math.max(0, u - o);
  };
  const abstand2 = (a, b) => (a.x - b.x) ** 2 + (a.y - b.y) ** 2;

  /* Transparente PNG wirklich auswerten statt den ganzen 940px-Motivkasten
     als belegt anzusehen. So darf Handschrift in echte Negativflaeche neben
     Armen/Props rutschen, ohne Gesichter oder Koerper zu ueberdecken. */
  const motivPunkte = [];
  let bildKasten = null;
  if (img?.complete && img.naturalWidth && img.naturalHeight) {
    const r = img.getBoundingClientRect();
    const scale = Math.min(r.width / img.naturalWidth, r.height / img.naturalHeight);
    const dw = img.naturalWidth * scale;
    const dh = img.naturalHeight * scale;
    const ox = r.left + (r.width - dw) / 2;
    const oy = r.top + (r.height - dh) / 2;
    bildKasten = { left: ox, top: oy, right: ox + dw, bottom: oy + dh, width: dw, height: dh };
    try {
      const n = 72;
      const canvas = document.createElement("canvas");
      canvas.width = n; canvas.height = n;
      const ctx = canvas.getContext("2d", { willReadFrequently: true });
      ctx.drawImage(img, 0, 0, n, n);
      const daten = ctx.getImageData(0, 0, n, n).data;
      for (let y = 0; y < n; y += 2) for (let x = 0; x < n; x += 2) {
        if (daten[(y * n + x) * 4 + 3] < 42) continue;
        motivPunkte.push({
          x: ox + ((x + 0.5) / n) * dw,
          y: oy + ((y + 0.5) / n) * dh,
        });
      }
    } catch {
      /* Data-URI-Motive sind same-origin; der Fallback bleibt fuer exotische
         Quellen trotzdem funktionsfaehig. */
    }
  }

  const blocker = [titel, badge, kopf, fuss].filter(Boolean).map((e) => e.getBoundingClientRect());
  const obereGrenze = Math.max(
    root.top + 150,
    titel?.getBoundingClientRect().bottom || root.top,
    badge?.getBoundingClientRect().bottom || root.top,
  ) + 24;
  const untereGrenze = (fuss?.getBoundingClientRect().top || root.bottom - 24) - 18;

  const basisY = clamp(obereGrenze - root.top + 36, 520, 760);
  const zonen = {
    "left-mid": { x: 50, y: basisY },
    "left-low": { x: 54, y: clamp(untereGrenze - root.top - 270, basisY + 80, 900) },
    "right-mid": { x: root.width - 365, y: basisY + 10 },
    "right-low": { x: root.width - 365, y: clamp(untereGrenze - root.top - 270, basisY + 90, 900) },
  };
  const bevorzugt = String(hinweis.dataset.zone || "auto");
  const reihenfolge = Object.keys(zonen).sort((a, b) =>
    (a === bevorzugt ? -1 : 0) - (b === bevorzugt ? -1 : 0)
  );

  const varianten = [];
  const groessen = [52, 48, 44];
  const drehungen = [-5, -2, 3];
  const yOffsets = [0, -42, 42];

  for (const zone of reihenfolge) {
    for (const font of groessen) {
      for (const rot of drehungen) {
        for (const dy of yOffsets) {
          const pos = zonen[zone];
          hinweis.style.left = `${pos.x}px`;
          hinweis.style.top = `${pos.y + dy}px`;
          hinweis.style.bottom = "auto";
          hinweis.style.fontSize = `${font}px`;
          text.style.transform = `rotate(${rot}deg)`;
          pfeil.style.display = "none";

          const r = hinweis.getBoundingClientRect();
          let score = 0;

          /* Canvas-Rand ist die einzige echte Geometriegrenze. */
          if (r.left < root.left + 24) score += (root.left + 24 - r.left) * 900;
          if (r.right > root.right - 24) score += (r.right - (root.right - 24)) * 900;
          if (r.top < root.top + 100) score += (root.top + 100 - r.top) * 900;
          if (r.bottom > root.bottom - 90) score += (r.bottom - (root.bottom - 90)) * 900;

          /* Markenbestandteile sollen praktisch frei bleiben, sind aber als
             Score statt starrem IF modelliert. */
          for (const b of blocker) score += flaeche(r, b, 8) * 2.4;

          /* Motivkollision wird anhand der Alpha-Maske bewertet. Ein paar
             Randpixel sind okay; viel Figur unter dem Text ist teuer. */
          let treffer = 0;
          for (const p of motivPunkte) {
            if (p.x >= r.left - 8 && p.x <= r.right + 8 && p.y >= r.top - 8 && p.y <= r.bottom + 8) treffer++;
          }
          score += treffer * 115;

          /* Regie-Zone ist nur Praeferenz, kein Befehl. */
          if (bevorzugt !== "auto" && zone !== bevorzugt) score += 520;

          /* Ein Pfeil soll weder 20px noch eine halbe Kachel lang werden. */
          if (motivPunkte.length) {
            const mitte = { x: (r.left + r.right) / 2, y: (r.top + r.bottom) / 2 };
            let min = Infinity;
            for (const p of motivPunkte) min = Math.min(min, Math.sqrt(abstand2(mitte, p)));
            score += Math.abs(clamp(min, 120, 360) - 215) * 1.2;
          }

          /* Groessere Handschrift bevorzugen, solange sie nicht kollidiert. */
          score += (52 - font) * 9;
          varianten.push({ score, zone, font, rot, x: pos.x, y: pos.y + dy });
        }
      }
    }
  }

  varianten.sort((a, b) => a.score - b.score);
  const best = varianten[0];
  if (!best) return;
  hinweis.style.left = `${best.x}px`;
  hinweis.style.top = `${best.y}px`;
  hinweis.style.bottom = "auto";
  hinweis.style.fontSize = `${best.font}px`;
  text.style.transform = `rotate(${best.rot}deg)`;

  const r = hinweis.getBoundingClientRect();
  const mitte = { x: (r.left + r.right) / 2, y: (r.top + r.bottom) / 2 };
  let ziel = null;
  let dist = Infinity;
  for (const p of motivPunkte) {
    /* Pfeilziel nicht unter die Schrift legen. */
    if (p.x >= r.left - 18 && p.x <= r.right + 18 && p.y >= r.top - 18 && p.y <= r.bottom + 18) continue;
    const d = abstand2(mitte, p);
    if (d < dist) { dist = d; ziel = p; }
  }
  if (!ziel && bildKasten) ziel = { x: (bildKasten.left + bildKasten.right) / 2, y: (bildKasten.top + bildKasten.bottom) / 2 };
  if (!ziel) { pfeil.style.display = "none"; return; }

  const dx = ziel.x - mitte.x;
  const dy = ziel.y - mitte.y;
  let start = { x: mitte.x, y: mitte.y };
  if (Math.abs(dx) >= Math.abs(dy)) start.x = dx >= 0 ? r.right + 4 : r.left - 4;
  else start.y = dy >= 0 ? r.bottom + 4 : r.top - 4;

  const vx = ziel.x - start.x;
  const vy = ziel.y - start.y;
  const laenge = Math.hypot(vx, vy);
  const winkel = Math.atan2(vy, vx) * 180 / Math.PI;
  const skalierung = clamp(laenge / 142, 0.72, 1.38);
  pfeil.style.display = "block";
  pfeil.style.left = `${start.x - r.left - 12}px`;
  pfeil.style.top = `${start.y - r.top - 14}px`;
  /* Das Marken-SVG zeigt in seiner Grundform etwa 31 Grad nach rechts unten. */
  pfeil.style.transform = `rotate(${winkel - 31}deg) scale(${skalierung})`;
  hinweis.dataset.gewaehlteZone = best.zone;
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
  for (const el of wurzel.querySelectorAll("h1,h2,h3,.merke,.norm,.zahl-unter,.karte .t,.pille,.ueberzeile,.formel,.zeile")) {
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
    : frei ? frei.getBoundingClientRect().top + 120
    : wurzel.getBoundingClientRect().bottom - 24;
  const textElemente = [...wurzel.querySelectorAll("h1,h2,h3,p,li,.text,.merke,.norm,.zahl,.zahl-unter,.karte,.optionen div,.rechnung,.spalte,.unter,.hinweis,.pfeil")];
  let n = 0;
  /* Absolut gesetzte Buehnenelemente zaehlen nicht als Inhalt: Das farbige
     Zeichen neben dem Motiv (frei-zeichen) steht bewusst unterhalb der
     Textgrenze - wuerde es mitgezaehlt, schrumpfte der Titel 14 Runden lang
     bis auf die Untergrenze, obwohl er laengst passt. */
  const ausser = (c) => ["geist", "illu", "foto", "frei", "frei-zeichen", "bildquelle", "cover-hinweis", "fuss"].some((k) => c.classList.contains(k));
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
  const bildFelder = ["bild", "bildQuelle", "bildFrei", "bildBreite", "bildHoehe", "bildTyp"];
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
    const html = folieHtml(beitrag.folien[i], ctx, i + 1, n);
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
