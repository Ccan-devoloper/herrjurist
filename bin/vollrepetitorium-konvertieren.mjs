#!/usr/bin/env node
/* ==========================================================================
   Vollrepetitorium (HTML) → Band-Textdateien für den Wissens-Tresor.

   node bin/vollrepetitorium-konvertieren.mjs <gesamtwissen.html> <zielordner>

   Die Quelle ist die kumulative HTML-Arbeitsansicht des Jura-Gesamtwissens
   (pandoc-Ausgabe, ein Dokument mit "Band N"-Überschriften). Heraus kommen
   *.txt-Dateien im Tresor-Format von src/wissen.mjs:

     # Band 3 - Strafrecht
     # Teil A - ...           (nur wo die Quelle Teile hat, Band 9)
     # 16. Diebstahl und Unterschlagung
     Fließtext, Listen, Tabellen als Zeilen …

   Nur "# " am Zeilenanfang ist für bandZerlegen() bedeutsam; Unterüber-
   schriften werden deshalb zu "## ", "### ", "#### " und bleiben Fließtext.

   Kapitelgrenzen je nach Band verschieden, weil die Quelle über die Updates
   mehrere Konventionen angesammelt hat:
   - Band 1-10: nummerierte h1 (und in Band 9 die nummerierten Fall-h2).
   - Konsolidierte Bände: nummerierte h2 ("12. Titel") oder Band-Punkt-
     Nummern ("22.3 Titel" → Kapitel 3).
   - Seitenaudit-Bände: Seiten-Nummern ("4110 – Titel" → Kapitel 4110, so
     bleibt die Seitenkennung als stabile Kapitelnummer erhalten).
   - Atlas-/Lexikonbände ohne solche Nummern: h2 (oder, wenn es kaum h2
     gibt, h3) werden der Reihe nach durchnummeriert – ohne das verlöre
     bandZerlegen() den gesamten Bandinhalt, denn Text vor dem ersten
     Kapitel fällt dort weg.

   Nicht übernommen wird, was kein Wissen ist: Inhaltsverzeichnis und
   Audit-Kopf vor Band 1, die Abschnitte "Gesamtarbeitsstand" und
   "Audit-Anhang" hinter dem letzten Band sowie Zwischenstands-Notizen
   innerhalb der Bände. Das ist Arbeitsprotokoll der Quelle, keine
   Belegstelle – und der Audit-Anhang allein wäre größer als alle Bände.

   Der Klartext gehört NICHT ins Repository (.gitignore sperrt ihn):
   danach bin/wissen-tresor.mjs packen bzw. der Workflow "Wissen
   einpflegen" mit bin/wissen-einpflegen.mjs.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";

const [, , quelle, ziel] = process.argv;
if (!quelle || !ziel) {
  console.error("Aufruf: node bin/vollrepetitorium-konvertieren.mjs <gesamtwissen.html> <zielordner>");
  process.exit(1);
}

/* --- HTML-Kleinteile ------------------------------------------------------ */

const ENTITAETEN = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " ", shy: "", auml: "ä", ouml: "ö", uuml: "ü", Auml: "Ä", Ouml: "Ö", Uuml: "Ü", szlig: "ß", sect: "§", ndash: "–", mdash: "—", hellip: "…", bdquo: "„", ldquo: "“", rdquo: "”", laquo: "«", raquo: "»", eacute: "é", egrave: "è", agrave: "à", middot: "·", times: "×", rarr: "→", larr: "←", euro: "€" };

function entschaerfen(s) {
  return s
    .replace(/&#x([0-9a-fA-F]+);/g, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(Number(d)))
    .replace(/&([a-zA-Z]+);/g, (t, n) => (n in ENTITAETEN ? ENTITAETEN[n] : t));
}

/* Eine Überschrift oder Tabellenzelle: Tags raus, Weißraum glätten. */
function zeileAus(htmlStueck) {
  return entschaerfen(htmlStueck.replace(/<[^>]+>/g, " ")).replace(/\s+/g, " ").trim();
}

/* Fließtext eines Abschnitts (zwischen zwei Überschriften) → Textzeilen.
   Tabellen zuerst, Zeile für Zeile mit " | " zwischen den Zellen; danach
   Absätze und Listenpunkte über Blockgrenzen. Verschachtelte Listen werden
   flach – für die Wortsuche und als Belegstelle reicht das. */
function textAus(htmlStueck) {
  let s = htmlStueck.replace(/<table[\s\S]*?<\/table>/g, (tabelle) => {
    const zeilen = [];
    const titel = /<caption[^>]*>([\s\S]*?)<\/caption>/.exec(tabelle);
    if (titel) zeilen.push(zeileAus(titel[1]));
    for (const tr of tabelle.matchAll(/<tr[^>]*>([\s\S]*?)<\/tr>/g)) {
      const zellen = [...tr[1].matchAll(/<t[dh][^>]*>([\s\S]*?)<\/t[dh]>/g)].map((z) => zeileAus(z[1]));
      if (zellen.some((z) => z)) zeilen.push(zellen.join(" | "));
    }
    return `\n${zeilen.join("\n")}\n`;
  });
  s = s
    .replace(/<li[^>]*>/g, "\n- ")
    .replace(/<(?:p|div|blockquote|figcaption|dt|dd)[^>]*>/g, "\n")
    .replace(/<br[^>]*>/g, "\n")
    .replace(/<[^>]+>/g, " ");
  const zeilen = [];
  for (let zeile of entschaerfen(s).split("\n")) {
    zeile = zeile.replace(/\s+/g, " ").trim();
    if (!zeile) continue;
    /* "# " am Anfang einer Textzeile wäre für bandZerlegen() ein Kapitel. */
    if (zeile.startsWith("# ")) zeile = `– ${zeile.slice(2)}`;
    zeilen.push(zeile);
  }
  return zeilen;
}

/* --- Kapitelmuster -------------------------------------------------------- */

const NUMMERIERT = /^(\d+[a-z]?)\.\s+(.+)$/;            // "16. Diebstahl …"
const SEITENNUMMER = /^(\d+)\s*[–—-]\s+(.+)$/;          // "4110 – Einspruch …"
const BAND_PUNKT = /^(\d+)\.(\d+)\s+(.+)$/;             // "22.3 Titel" → 3
/* Arbeitsprotokoll der Quelle, kein Wissen. */
const META = /^(Auditstatus|Großbatch|Zwischenstand|Gesamtarbeitsstand|Auditlage|Audit-?Anhang)/i;

/* Feste Dateinamen für die Bände, die es im Tresor schon gibt – so ersetzt
   die neue Fassung die alte, statt neben ihr zu liegen. */
const SLUGS = { 1: "zivilrecht", 2: "oeffentliches-recht", 3: "strafrecht", 4: "zivilrecht-assessor", 5: "oeffentliches-recht-assessor", 6: "strafrecht-assessor", 7: "register", 8: "einzelprobleme", 9: "faelle" };

function slug(nr, titel) {
  if (SLUGS[nr]) return SLUGS[nr];
  const s = titel
    .replace(/^Band \d+\s*[–—-]\s*/, "")
    .toLowerCase()
    .replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss")
    .replace(/jura[- ]online[- ]?/g, "").replace(/vollinhaltsaudit/g, "audit").replace(/seitenaudit/g, "audit")
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").replace(/-+/g, "-");
  const kurz = s.length > 48 ? s.slice(0, 48).replace(/-[^-]*$/, "") : s;
  return kurz.replace(/-+$/, "") || "band";
}

/* --- Dokument zerlegen ---------------------------------------------------- */

const html = fs.readFileSync(quelle, "utf8");

/* Alle Überschriften mit Position; dazwischen liegt Fließtext. */
const koepfe = [...html.matchAll(/<h([1-4])[^>]*>([\s\S]*?)<\/h\1>/g)]
  .map((m) => ({ ebene: Number(m[1]), titel: zeileAus(m[2]), von: m.index, bis: m.index + m[0].length }));

/* Bandgrenzen: eine h1 "Band N …" eröffnet einen Band, jede andere h1
   außerhalb der Nummern-/Teil-Muster (Titelseiten, "Gesamtarbeitsstand",
   "Audit-Anhang") schließt ihn. */
const baende = [];
let band = null;
for (let i = 0; i < koepfe.length; i++) {
  const k = koepfe[i];
  const ende = koepfe[i + 1]?.von ?? html.length;
  if (k.ebene === 1) {
    const istBand = /^Band (\d+)\b/.exec(k.titel);
    if (istBand) {
      band = { nr: Number(istBand[1]), titel: k.titel, koepfe: [] };
      baende.push(band);
      continue;
    }
    if (!NUMMERIERT.test(k.titel) && !/^Teil /.test(k.titel)) { band = null; continue; }
  }
  if (band) band.koepfe.push({ ...k, textBis: ende });
}

/* --- Bände schreiben ------------------------------------------------------ */

fs.mkdirSync(ziel, { recursive: true });
let kapitelGesamt = 0, zeichenGesamt = 0;
const bericht = [];

for (const b of baende) {
  /* Kapitelmodus des Bandes bestimmen (siehe Kopfkommentar). */
  const h1Kapitel = b.koepfe.filter((k) => k.ebene === 1 && NUMMERIERT.test(k.titel)).length;
  const h2 = b.koepfe.filter((k) => k.ebene === 2 && !META.test(k.titel));
  const zaehle = (muster) => h2.filter((k) => muster.test(k.titel)).length;
  let modus;
  if (h1Kapitel) modus = "h1";
  else if (h2.length && zaehle(NUMMERIERT) >= h2.length * 0.6) modus = "h2-nummer";
  else if (h2.length && zaehle(SEITENNUMMER) >= h2.length * 0.6) modus = "h2-seite";
  else if (h2.length && zaehle(BAND_PUNKT) >= h2.length * 0.6) modus = "h2-punkt";
  else if (h2.length >= 3) modus = "h2-folge";
  else if (b.koepfe.filter((k) => k.ebene === 3).length >= 3) modus = "h3-folge";
  else modus = "pauschal";

  const zeilen = [`# ${b.titel}`, ""];
  let laufnummer = 0, verworfen = 0;
  const nummern = [];
  if (modus === "pauschal") { zeilen.push(`# 1. ${b.titel.replace(/^Band \d+\s*[–—-]\s*/, "")}`, ""); nummern.push("1"); }

  /* Meta-Abschnitte fallen mitsamt Inhalt weg, bis eine gleich- oder
     höherrangige Überschrift den nächsten Abschnitt eröffnet. */
  let metaEbene = 0;

  for (const k of b.koepfe) {
    if (metaEbene && k.ebene > metaEbene) { verworfen += 1; continue; }
    metaEbene = 0;
    if (META.test(k.titel)) { metaEbene = k.ebene; verworfen += 1; continue; }

    let kapitel = null;
    if (k.ebene === 1) {
      const n = NUMMERIERT.exec(k.titel);
      if (n) kapitel = { nr: n[1], titel: n[2] };
      else if (/^Teil /.test(k.titel)) { zeilen.push(`# ${k.titel}`, ""); }
      else { zeilen.push(`## ${k.titel}`); }
    } else if (k.ebene === 2) {
      const n = NUMMERIERT.exec(k.titel), s = SEITENNUMMER.exec(k.titel), p = BAND_PUNKT.exec(k.titel);
      if ((modus === "h1" || modus === "h2-nummer") && n) kapitel = { nr: n[1], titel: n[2] };
      else if (modus === "h2-seite" && s) kapitel = { nr: s[1], titel: s[2] };
      else if (modus === "h2-punkt" && p && Number(p[1]) === b.nr) kapitel = { nr: p[2], titel: p[3] };
      else if (modus === "h2-folge") kapitel = { nr: String(++laufnummer), titel: k.titel };
      else zeilen.push(`## ${k.titel}`);
    } else if (k.ebene === 3 && modus === "h3-folge") {
      kapitel = { nr: String(++laufnummer), titel: k.titel };
    } else {
      zeilen.push(`${"#".repeat(k.ebene + 1)} ${k.titel}`);
    }
    if (kapitel) { zeilen.push(`# ${kapitel.nr}. ${kapitel.titel}`, ""); nummern.push(kapitel.nr); }
    zeilen.push(...textAus(html.slice(k.bis, k.textBis)), "");
  }

  const text = `${zeilen.join("\n").replace(/\n{3,}/g, "\n\n").trim()}\n`;
  const datei = `band-${b.nr}-${slug(b.nr, b.titel)}.txt`;
  fs.writeFileSync(path.join(ziel, datei), text);

  const doppelt = [...new Set(nummern.filter((n, i) => nummern.indexOf(n) !== i))];
  kapitelGesamt += nummern.length; zeichenGesamt += text.length;
  bericht.push({ datei, modus, kapitel: nummern.length, zeichen: text.length, doppelt, verworfen });
}

for (const z of bericht) {
  console.log(`  ${z.datei}  ${String(z.kapitel).padStart(4)} Kapitel  ${String(z.zeichen).padStart(8)} Zeichen  (${z.modus}${z.verworfen ? `, ${z.verworfen} Meta-Abschnitte verworfen` : ""})`);
  if (z.doppelt.length) console.log(`    ! doppelte Kapitelnummern: ${z.doppelt.join(", ")} – der Zeiger träfe immer das zuerst gelesene`);
}
console.log(`\n${baende.length} Bände, ${kapitelGesamt} Kapitel, ${(zeichenGesamt / 1024 / 1024).toFixed(2)} MB Klartext in ${ziel}.`);
console.log("Klartext nicht committen – einpacken mit: node bin/wissen-tresor.mjs packen " + ziel);
