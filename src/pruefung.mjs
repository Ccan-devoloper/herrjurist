/* ==========================================================================
   Qualitäts- und Eigenständigkeitsprüfung.

   1. Kein 1:1-Text: Jede Folge von N Wörtern des Beitrags darf nicht wörtlich
      aus den Stichpunkten des Themenpools stammen (Shingle-Vergleich). Die
      Titel bleiben ausgenommen – die Frage IST das Thema und soll wörtlich
      auf der ersten Folie stehen.
   2. Keine gesperrten Namen (Sperrliste, sonst frei erfundene Fälle).
   3. Keine Quellenbezüge (Seite, Folie, Mitschrift, Fallnummer).
   4. Formale Grenzen: Überschriften, Folientexte, Caption, Hashtags.
   Rückgabe: { ok, fehler: [...] } – der Autor bekommt die Fehler als Feedback
   und formuliert neu.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { THEMEN } from "../daten/themen.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
/* Der Themenpool ist die einzige Textquelle des Bots – er ist der Korpus. */

export const SHINGLE_LAENGE = 8;   // Wörter
/* Aufbau: keine leere Folie, jede Folie mit Titel und Inhalt, genau eine
   CTA-Folie am Ende. Leere Kacheln sind der sichtbarste Fehler im Feed. */
export function folieLeer(f) {
  const text = (f.text || "").trim().length;
  const punkte = (f.punkte || []).filter((p) => String(p).trim()).length;
  const schritte = (f.schritte || []).filter((x) => (typeof x === "string" ? x.trim() : x?.titel?.trim())).length;
  switch (f.art) {
    case "titel": return !(f.titel || "").trim();
    case "cta": return false;
    case "text": return text < 30 && punkte < 2;
    case "schritte": return schritte < 2;
    case "vergleich": return !(f.links?.punkte?.length >= 1 && f.rechts?.punkte?.length >= 1);
    case "rechnung": return !(f.formel || "").trim() && (f.zeilen || []).length < 2;
    case "karte": return schritte < 3 && punkte < 3;
    case "merke": return text < 20;
    default: return text < 30 && punkte < 2 && schritte < 2;
  }
}

export function pruefeAufbau(folien) {
  const fehler = [];
  folien.forEach((f, i) => {
    if (f.art !== "cta" && !(f.titel || "").trim()) fehler.push(`Folie ${i + 1} (${f.art}): kein Titel`);
    if (folieLeer(f)) fehler.push(`Folie ${i + 1} (${f.art}): kein Inhalt – jede Folie braucht Text, Punkte oder Schritte`);
    if (f.art === "titel" && i > 0) fehler.push(`Folie ${i + 1}: nur Folie 1 darf die Art „titel“ haben`);
  });
  const ctas = folien.map((f, i) => (f.art === "cta" ? i : -1)).filter((i) => i >= 0);
  if (ctas.length > 1) fehler.push(`Nur eine CTA-Folie erlaubt (gefunden: ${ctas.length})`);
  if (ctas.length && ctas.at(-1) !== folien.length - 1) fehler.push("Die CTA-Folie muss die letzte sein");
  return fehler;
}

export const GRENZEN = {
  titelZeichen: 110,
  folienTextZeichen: 600,   // der Renderer passt Text automatisch ein; erst deutliche Überlänge kostet eine Neufassung
  storyTextZeichen: 260,
  captionZeichen: 2200,
  hashtagsMax: 30,
  folienMin: 3,
  folienMax: 10,
};

const SPERRLISTE_DATEI = path.resolve(hier, "../config/namen-sperrliste.json");

export function normalisieren(text) {
  return String(text)
    .toLowerCase()
    .replace(/[„“"'»«‚‘’]/g, " ")
    .replace(/[^a-z0-9äöüß§%€.,\s-]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function woerter(text) {
  return normalisieren(text).split(" ").filter((w) => w.length > 0);
}

/* FNV-1a, 32 Bit – klein genug für ein Set aus Zahlen. */
function hash(s) {
  let h = 0x811c9dc5;
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193); }
  return h >>> 0;
}

function shingles(text, n = SHINGLE_LAENGE) {
  const w = woerter(text);
  const out = [];
  for (let i = 0; i + n <= w.length; i++) out.push(w.slice(i, i + n).join(" "));
  return out;
}

let korpusCache = null;

/* Baut einmal je Prozess den Shingle-Index über alle Datendateien der Webseite. */
export function korpus() {
  if (korpusCache) return korpusCache;
  const index = new Set();
  /* Nur die Stichpunkte, nie die Titel: Die Frage auf Folie 1 soll wörtlich
     die Frage des Themas sein – sie hier aufzunehmen würde jeden Beitrag
     als Abschreiben werten. */
  let n = 0;
  for (const t of THEMEN) {
    const teile = [...(t.kern?.lernziele || []), ...(t.kern?.pruefschritte || []), t.kern?.merksatz || "", ...(t.kern?.fehler || [])];
    for (const teil of teile) { if (!teil) continue; n++; for (const sh of shingles(teil)) index.add(hash(sh)); }
  }
  const namen = new Set();
  let sperrliste = [];
  if (fs.existsSync(SPERRLISTE_DATEI)) sperrliste = JSON.parse(fs.readFileSync(SPERRLISTE_DATEI, "utf8"));
  for (const eintrag of sperrliste) namen.add(eintrag);
  korpusCache = { index, namen: [...namen], dateien: n };
  return korpusCache;
}

/* Liefert alle wörtlichen Übernahmen (SHINGLE_LAENGE Wörter am Stück) eines Textes. */
export function uebernahmen(text, k = korpus()) {
  const treffer = [];
  for (const s of shingles(text)) if (k.index.has(hash(s))) treffer.push(s);
  return [...new Set(treffer)];
}

/* Ab wie vielen Wörtern am Stück eine Übereinstimmung als Übernahme gilt.
   Fachsprache ist standardisiert: „Wirtschaftsgüter, die unmittelbar dem
   Betrieb der Personengesellschaft dienen“ ist Gesetzeswortlaut und lässt sich
   nicht sinnvoll umschreiben – acht solche Wörter am Stück sind Zufall, nicht
   Abschreiben. Wer wirklich abschreibt, trifft ganze Sätze: Dann greifen
   mehrere Shingles ineinander und der zusammenhängende Lauf wird lang. */
const UEBERNAHME_WOERTER = 13;

/* Fasst benachbarte Treffer zu zusammenhängenden Läufen zusammen.
   Zwei Shingles gehören zum selben Lauf, wenn sie sich überlappen. */
export function uebernahmeLaeufe(text, k = korpus()) {
  const w = woerter(text);
  const treffer = new Set();
  for (let i = 0; i + SHINGLE_LAENGE <= w.length; i++) {
    if (k.index.has(hash(w.slice(i, i + SHINGLE_LAENGE).join(" ")))) treffer.add(i);
  }
  const laeufe = [];
  let start = null, ende = null;
  for (const i of [...treffer].sort((a, b) => a - b)) {
    if (start === null) { start = i; ende = i + SHINGLE_LAENGE; continue; }
    if (i <= ende) { ende = Math.max(ende, i + SHINGLE_LAENGE); continue; }
    laeufe.push({ text: w.slice(start, ende).join(" "), woerter: ende - start });
    start = i; ende = i + SHINGLE_LAENGE;
  }
  if (start !== null) laeufe.push({ text: w.slice(start, ende).join(" "), woerter: ende - start });
  return laeufe;
}

export function gesperrteNamen(text, k = korpus()) {
  const t = ` ${String(text)} `;
  return k.namen.filter((n) => new RegExp(`(^|[^a-zäöüß])${n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}([^a-zäöüß]|$)`, "u").test(t));
}

const QUELLENBEZUG = /\b(laut Quelle|Quelle|Seite \d+|Folie|Mitschrift|Skript|Originalfall|Fall \d{2,3}|Hausaufgabe|Musterlösung der Finanzverwaltung|Frame)\b/i;

/* Normen sind wörtlich erlaubt – sie sind Gesetzestext-Zitate, keine Übernahme.
   Deshalb werden Normzitate (auch ohne Gesetzesangabe, in beliebiger
   Reihenfolge von Abs./S./Nr./Buchst.) vor dem Shingle-Vergleich entfernt. */
const NORM = /(?:§§?|Art\.|Artikel|R|H)\s*\d+(?:\.\d+)?[a-z]?(?:\s*(?:\(\d+[a-z]?\)|[a-z]{2}\)|Abs\.|Absatz|S\.|Satz|Nr\.|Nummer|Buchst\.|Buchstabe|Hs\.|Halbsatz|Alt\.|Var\.|lit\.)\s*[\da-z]*\)?)*(?:\s*(?:i\.?\s?V\.?\s?m\.?|iVm|in Verbindung mit)\s*(?:§§?\s*)?\d+[a-z]?(?:\s*(?:Abs\.|S\.|Nr\.|Buchst\.)\s*[\da-z]+)*)?\s*(?:BGB|StGB|StPO|ZPO|GG|VwGO|VwVfG|HGB|GmbHG|AktG|InsO|GVG|ArbGG|KSchG|BetrVG|MuSchG|BEEG|TVG|ProdHaftG|StVG|StVO|OWiG|JGG|GewO|BauGB|BImSchG|PolG|SGB|AEUV|EUV|GRCh|EMRK|BVerfGG|RVG|BRAO|FamFG|WEG|ErbbauRG)?\b/g;
export function ohneNormen(text) {
  return String(text).replace(NORM, " NORM ").replace(/\b(Abs|S|Nr|Buchst|Hs|Alt)\.\s*\d+[a-z]?/g, " NORM ").replace(/\(\d+[a-z]?\)/g, " NORM ");
}

function alleTexte(beitrag) {
  const teile = [];
  for (const f of beitrag.folien || []) {
    teile.push(f.titel || "", f.text || "", ...(f.punkte || []), ...(f.schritte || []).map((s) => (typeof s === "string" ? s : `${s.titel || ""} ${s.text || ""}`)), f.links?.text || "", f.rechts?.text || "", ...(f.links?.punkte || []), ...(f.rechts?.punkte || []));
  }
  teile.push(beitrag.caption || "");
  for (const s of beitrag.stories || []) teile.push(s.titel || "", s.text || "", ...(s.optionen || []));
  return teile.filter(Boolean);
}

export function pruefeBeitrag(beitrag, opt = {}) {
  const fehler = [];
  const k = opt.korpus || korpus();
  const texte = alleTexte(beitrag);
  const gesamt = texte.join("\n");

  /* 1. Wörtliche Übernahmen: erst ein langer Lauf oder mehrere Fundstellen
        sind Abschreiben, ein einzelner Fachsprachen-Treffer ist es nicht. */
  const laeufe = uebernahmeLaeufe(ohneNormen(gesamt), k);
  const deutlich = laeufe.filter((l) => l.woerter >= UEBERNAHME_WOERTER);
  if (deutlich.length || laeufe.length >= 2) fehler.push(`Wörtliche Übernahme aus der Webseite (bitte in eigenen Worten formulieren): ${(deutlich.length ? deutlich : laeufe).slice(0, 3).map((d) => `„${d.text}“`).join(" · ")}`);

  /* 2. Namen aus den Fällen */
  const namen = gesperrteNamen(gesamt, k);
  if (namen.length) fehler.push(`Gesperrte Fallnamen verwendet (bitte andere, frei erfundene Namen): ${[...new Set(namen)].join(", ")}`);

  /* 3. Quellenbezüge */
  if (QUELLENBEZUG.test(gesamt)) fehler.push(`Bezug auf Kursquelle/Seiten/Fallnummern entfernen: ${gesamt.match(QUELLENBEZUG)[0]}`);

  /* 4. Formales */
  if (beitrag.folien) {
    if (beitrag.folien.length < GRENZEN.folienMin || beitrag.folien.length > GRENZEN.folienMax) fehler.push(`Folienzahl ${beitrag.folien.length} außerhalb ${GRENZEN.folienMin}–${GRENZEN.folienMax}`);
    beitrag.folien.forEach((f, i) => {
      if ((f.titel || "").length > GRENZEN.titelZeichen) fehler.push(`Folie ${i + 1}: Titel zu lang (${f.titel.length} > ${GRENZEN.titelZeichen})`);
      const textLaenge = (f.text || "").length + (f.punkte || []).join(" ").length + (f.schritte || []).map((s) => (typeof s === "string" ? s : `${s.titel} ${s.text}`)).join(" ").length;
      if (textLaenge > GRENZEN.folienTextZeichen) fehler.push(`Folie ${i + 1}: Text zu lang (${textLaenge} > ${GRENZEN.folienTextZeichen} Zeichen)`);
    });
    if (!beitrag.folien[0]?.titel) fehler.push("Folie 1 braucht einen Titel (die Frage/den Aufhänger)");
    fehler.push(...pruefeAufbau(beitrag.folien));
  }
  if (beitrag.caption != null) {
    if (beitrag.caption.length > GRENZEN.captionZeichen) fehler.push(`Caption zu lang (${beitrag.caption.length})`);
    if ((beitrag.hashtags || []).length > GRENZEN.hashtagsMax) fehler.push("Zu viele Hashtags");
  }
  for (const s of beitrag.stories || []) {
    const l = (s.text || "").length;
    if (l > GRENZEN.storyTextZeichen) fehler.push(`Story „${s.titel || s.art}“: Text zu lang (${l} > ${GRENZEN.storyTextZeichen})`);
  }

  return { ok: fehler.length === 0, fehler };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const k = korpus();
  console.log(`Korpus: ${k.dateien} Dateien, ${k.index.size} Shingles, ${k.namen.length} gesperrte Namen`);
  console.log(k.namen.slice(0, 40).join(", "));
}
