/* ==========================================================================
   Wissensbasis: das Jura-Gesamtwissen als Belegstelle beim Schreiben.

   Der Themenpool (daten/themen.mjs) ist bewusst ein Geruest - Titel, Normen,
   zwei Stichworte. Das reicht, damit ein Beitrag entsteht, aber es reicht
   nicht immer, damit er im Detail stimmt: Fristen, Reihenfolgen, Tenorformeln
   und Streitstaende muss das Modell sonst aus dem Gedaechtnis holen.

   Hier liegt der Volltext dazu. Vor dem Schreiben sucht der Autor das Kapitel
   zum Thema heraus und bekommt es als Quelle mit, damit er Zahlen und
   Reihenfolgen nicht erfindet. Der Faktencheck bekommt dieselbe Stelle und
   prueft dagegen. Was uebernommen werden darf und was nicht, steht unten bei
   belegstelle() - kurz: Schemata ja, Faelle mit geaenderten Namen, Prosa in
   eigenen Worten.

   VERSCHLUESSELT: Das Repo ist oeffentlich, das Material ist es nicht. Die
   Baende liegen als .enc im Verzeichnis daten/wissen - AES-256-GCM, Schluessel
   aus IG_WISSEN_KEY (GitHub-Actions-Secret), gleiche Bauart wie der
   Token-Tresor in instagram.mjs. Ohne Schluessel ist die Datei ein
   Zufallshaufen; wer das Repo im Browser oeffnet, sieht nichts.

   Ohne Schluessel laeuft der Bot weiter wie vorher - nur eben ohne
   Belegstelle. Das ist Absicht: Eine fehlende Wissensbasis darf keinen
   Beitrag ausfallen lassen.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import zlib from "node:zlib";
import { fileURLToPath } from "node:url";
import { CONFIG } from "./config.mjs";

const HIER = path.dirname(fileURLToPath(import.meta.url));
export const WISSEN_ORDNER = path.join(HIER, "..", "daten", "wissen");

/* --- Tresor: identisch gebaut zum Token-Tresor ---------------------------- */
export function wissenSchluessel(geheim = CONFIG.wissen?.schluessel) {
  if (!geheim) return null;
  return crypto.createHash("sha256").update(String(geheim)).digest();
}

/* Vor dem Verschlüsseln wird komprimiert, danach nicht mehr: AES-Ausgabe ist
   Zufall, da holt git kein Byte mehr heraus. Seit dem Vollrepetitorium sind
   die Bände zehn Megabyte Klartext – ungepackt trüge jeder Clone das voll. */
export function wissenVerschluesseln(text, geheim) {
  const key = wissenSchluessel(geheim);
  if (!key) throw new Error("IG_WISSEN_KEY fehlt");
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv("aes-256-gcm", key, iv);
  const enc = Buffer.concat([c.update(zlib.gzipSync(Buffer.from(text, "utf8"), { level: 9 })), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), enc]);
}

export function wissenEntschluesseln(buf, geheim) {
  const key = wissenSchluessel(geheim);
  if (!key) return null;
  const iv = buf.subarray(0, 12), tag = buf.subarray(12, 28), enc = buf.subarray(28);
  const d = crypto.createDecipheriv("aes-256-gcm", key, iv);
  d.setAuthTag(tag);
  let roh = Buffer.concat([d.update(enc), d.final()]);
  /* Ältere Tresore liegen ungepackt vor; die gzip-Kennung unterscheidet
     beide, denn kein Band beginnt mit den Bytes 1f 8b. */
  if (roh[0] === 0x1f && roh[1] === 0x8b) roh = zlib.gunzipSync(roh);
  return roh.toString("utf8");
}

/* --- Index ---------------------------------------------------------------
   Ein Kapitel ist eine "# 12. Ueberschrift"-Zeile und alles bis zur naechsten.
   Die Nummern sind innerhalb eines Bandes eindeutig, also ist "4/12" ein
   stabiler Schluessel, den ein Thema in seinem Feld `wissen` nennen kann. */

let zwischenspeicher = null;

function bandLesen(ordner, datei, geheim) {
  const roh = fs.readFileSync(path.join(ordner, datei));
  /* Klartext (Tests, lokale Arbeitskopie) oder Tresor - beides lesbar. */
  if (datei.endsWith(".enc")) return wissenEntschluesseln(roh, geheim);
  return roh.toString("utf8");
}

function bandZerlegen(text, band) {
  const kapitel = [];
  /* "# Teil A - ..." trennt in Band 9 die Fallgruppen: kein eigenes Kapitel,
     aber der Zusammenhang, in dem die folgenden Faelle stehen. */
  let teil = "";
  let jetzt = null;
  for (const zeile of text.split("\n")) {
    const ueber = /^# (.+)$/.exec(zeile);
    if (ueber) {
      const nummer = /^(\d+[a-z]?)\.\s+(.*)$/.exec(ueber[1]);
      if (nummer) {
        jetzt = { id: `${band.nr}/${nummer[1]}`, band: band.nr, bandTitel: band.titel, teil, nr: nummer[1], titel: nummer[2].trim(), zeilen: [] };
        kapitel.push(jetzt);
        continue;
      }
      if (/^Teil /.test(ueber[1])) { teil = ueber[1].trim(); continue; }
      if (/^Band /.test(ueber[1])) continue;
    }
    if (jetzt) jetzt.zeilen.push(zeile);
  }
  return kapitel.map((k) => ({ ...k, text: k.zeilen.join("\n").trim(), zeilen: undefined }));
}

export function wissenIndex({ geheim, ordner = WISSEN_ORDNER, neu = false } = {}) {
  if (zwischenspeicher && !neu) return zwischenspeicher;
  if (!fs.existsSync(ordner)) return (zwischenspeicher = []);
  const dateien = fs.readdirSync(ordner).filter((d) => /\.txt(\.enc)?$/.test(d)).sort();
  const alle = [];
  for (const datei of dateien) {
    const nr = Number(/band-(\d+)/.exec(datei)?.[1] || 0);
    let text;
    try {
      text = bandLesen(ordner, datei, geheim);
    } catch (e) {
      /* Falscher oder fehlender Schluessel: kein Grund, den Lauf abzubrechen.
         Der Beitrag entsteht dann ohne Belegstelle wie vor dieser Aenderung. */
      console.warn(`  ! Wissensbasis ${datei} nicht lesbar (${e.message}) – schreibe ohne Belegstelle`);
      continue;
    }
    if (!text) continue;
    const titel = /^# (Band .+)$/m.exec(text)?.[1] || `Band ${nr}`;
    alle.push(...bandZerlegen(text, { nr, titel }));
  }
  return (zwischenspeicher = alle);
}

export function wissenLeeren() { zwischenspeicher = null; }

/* --- Suche ---------------------------------------------------------------
   Zuerst der Zeiger am Thema (`wissen: "4/2"`), dann ein Wortabgleich. Der
   Abgleich ist absichtlich stumpf und deterministisch: Beim Nachrendern
   desselben Beitrags muss dieselbe Stelle herauskommen. */

/* Füllwörter. "ohne" musste hier hinein, weil sonst "Vertrag ohne Rechtswahl"
   auf "Geschäftsführung ohne Auftrag" traf - ein gemeinsames Wort, zwei
   Welten. */
const STOPP = new Set(["und", "oder", "aber", "der", "die", "das", "den", "dem", "des", "ein", "eine", "einer", "eines", "einem", "einen",
  "wie", "was", "wann", "warum", "wer", "wen", "wem", "wessen", "wo", "wozu", "wohin", "welche", "welches", "welcher", "welchen",
  "man", "sich", "ist", "sind", "wird", "werden", "war", "waren", "worin", "womit", "wobei", "wodurch", "worauf",
  "im", "in", "am", "an", "auf", "bei", "mit", "von", "vom", "zum", "zur", "für", "fuer", "nach", "aus", "als", "nur", "noch",
  "ohne", "über", "ueber", "unter", "durch", "gegen", "seine", "ihre", "ihrer", "einen", "etwa", "dabei", "dazu", "damit",
  "prueft", "prüft", "gilt", "gibt", "hat", "haben", "kann", "darf", "muss", "müssen", "steht", "dass", "sie", "wenn",
  "liegt", "vor", "zwischen", "beim", "dann", "auch", "schon", "immer", "nicht", "kein", "keine", "sein", "lange",
  "besteht", "geht", "macht", "lässt", "laesst", "bleibt", "wirkt", "funktioniert", "bedeutet", "heisst", "heißt"]);

/* Grobe Grundformen: Der Titel fragt nach "Voraussetzungen", das Kapitel
   heisst "Voraussetzung". Ohne diesen Schnitt gehen solche Treffer verloren. */
function stamm(w) {
  return w.replace(/(ungen|heiten|keiten|schaften)$/, "ung")
    .replace(/(en|er|es|em|te|ten|s)$/, "")
    .replace(/(ung)$/, "ung");
}

function woerter(s) {
  return String(s || "").toLowerCase()
    .replace(/[§„“"»«(),.:;?!–—/]/g, " ")
    .split(/\s+/)
    .filter((w) => w.length >= 4 && !STOPP.has(w))
    .map(stamm)
    .filter((w) => w.length >= 4);
}

/* Normen sind der schaerfste Treffer: Wer "§ 767 Abs. 2 ZPO" im Titel hat,
   meint das Kapitel, in dem "767" vorkommt - und kein anderes. */
function normZeichen(normen = []) {
  const t = normen.join(" ");
  return [...new Set([...t.matchAll(/\b(\d{2,4}[a-z]?)\b/g)].map((m) => m[1]))];
  /* Nur zwei- bis vierstellige Nummern. Die Absatzzahlen aus "§ 244 Abs. 1
     Nr. 3 StGB" waeren sonst eigene Treffer, und die "1" steckt in jeder
     Paragraphennummer: So gewann bei "Wohnungseinbruchdiebstahl" das Kapitel
     "Revisionseinlegung, § 341 StPO". */
}

/* Nummer als eigenes Wort, nicht als Teilzeichenfolge: "§ 823" darf nicht in
   "§ 8231" oder in einer Jahreszahl treffen. */
const nummerDrin = (text, z) => new RegExp(`(?<!\\d)${z}(?!\\d)`).test(text);

/* Welches Rechtsgebiet trägt ein Kapitel? Ohne diese Schranke gewinnt bei
   "Wie tenoriert man ein Zivilurteil?" das Kapitel "Vorläufige
   Vollstreckbarkeit" aus dem Band zum Verwaltungsprozess: dieselben Wörter,
   das falsche Verfahren. Ein Beitrag mit der Quelle aus dem Nachbargebiet
   wäre schlimmer als einer ganz ohne Quelle.

   1 = Zivilrecht, 2 = Strafrecht, 3 = Öffentliches Recht, 0 = gebietsoffen. */
/* Ein Kapitel im Mittel 1000 Zeichen lang; alles jenseits davon ist ein
   Sammelband, kein Thema. Der Zeiger am Thema (`wissen`) darf trotzdem
   dorthin zeigen - nur von allein wird so ein Kapitel nicht gewählt. */
const SAMMELKAPITEL = 16000;
/* Bände 1-9 wie gehabt; ab Band 10 (Vollrepetitorium) sind nur die Bände
   eingetragen, deren Titel das Gebiet zweifelsfrei nennt. Die gemischten
   (2. Examen quer, Sitemap-Blöcke, Band 73 mit Landesrechts-Anhang) bleiben
   gebietsoffen - dort entscheidet Teil- oder Kapiteltitel. Die Audit-Bände
   51-64 und 67-73 sind der ZPO-Block des 2. Examens, 69/70 der einstweilige
   Rechtsschutz nach §§ 916 ff. ZPO - nicht der nach § 80 V VwGO. */
const BAND_GEBIET = {
  1: 1, 4: 1, 3: 2, 6: 2, 2: 3, 5: 3,
  11: 1, 12: 3, 13: 2, 18: 3, 19: 2, 22: 1, 23: 3, 24: 2, 25: 1, 26: 1,
  28: 1, 29: 3, 30: 2, 40: 3, 47: 1,
  51: 1, 52: 1, 53: 1, 54: 1, 55: 1, 56: 1, 57: 1, 58: 1, 59: 1, 60: 1,
  61: 1, 62: 1, 63: 1, 64: 1, 67: 1, 68: 1, 69: 1, 70: 1, 71: 1, 72: 1,
};
const TEIL_GEBIET = [[/Zivilrechtliche/i, 1], [/Strafrechtliche/i, 2], [/Öffentlich-rechtliche/i, 3]];
const TITEL_GEBIET = [
  [/BGB|Schuldrecht|Sachenrecht|Delikts|Bereicherungs|Handels|Gesellschafts|Arbeits|Familien|Erbrecht|Zivil/i, 1],
  [/Strafrecht|Strafprozess|StPO|Revision|Anklage/i, 2],
  [/Verwaltung|Polizei|Baurecht|Staatshaftung|Kommunal|Staatsorganisation|Grundrecht|Europarecht|Öffentlich/i, 3],
];

const REGISTER_BAENDE = new Set([7, 42, 43, 44, 45]);

/* Kapitel, die ein einzelnes Bundesland durchdeklinieren („… (Bayern)“):
   Als Belegstelle für ein allgemeines Thema wären sie genau die Fixierung
   auf ein Land, die der Kanal vermeidet – der Beitrag soll bundesweit
   tragen und auf Länderunterschiede nur hinweisen. Von allein wird so ein
   Kapitel darum nie gewählt; ein Zeiger am Thema darf weiter gezielt
   hinein zeigen, etwa für einen echten Ländervergleich. */
const LAND_KAPITEL = /\((Baden-Württemberg|Bayern|Berlin|Brandenburg|Bremen|Hamburg|Hessen|Mecklenburg-Vorpommern|Niedersachsen|Nordrhein-Westfalen|Rheinland-Pfalz|Saarland|Sachsen|Sachsen-Anhalt|Schleswig-Holstein|Thüringen)\)/;

export function kapitelGebiet(kapitel) {
  const fest = BAND_GEBIET[kapitel.band];
  if (fest) return fest;
  for (const [muster, g] of TEIL_GEBIET) if (muster.test(kapitel.teil || "")) return g;
  for (const [muster, g] of TITEL_GEBIET) if (muster.test(kapitel.titel)) return g;
  return 0;
}

export function wissenBewerten(thema, kapitel) {
  const suchWoerter = new Set(woerter(`${thema.titel} ${(thema.kern?.lernziele || []).join(" ")}`));
  if (!suchWoerter.size) return 0;
  const kapitelWoerter = new Set(woerter(kapitel.titel));
  let gemeinsam = 0;
  for (const w of kapitelWoerter) if (suchWoerter.has(w)) gemeinsam++;
  /* Zwei Maße nebeneinander: wie viele Wörter treffen (Menge) und welcher
     Anteil des Kapiteltitels getroffen ist (Genauigkeit). Ohne das zweite
     gewinnt der längste Titel, weil er die meisten Wörter mitbringt. */
  let punkte = gemeinsam * 3;
  if (kapitelWoerter.size) punkte += (gemeinsam / kapitelWoerter.size) * 8;

  /* Der Fließtext zählt mit, aber schwächer und nur einmal je Wort. Er
     entscheidet die Fälle, in denen die Überschrift das Thema nicht nennt -
     "§ 985 BGB" steht nicht im Titel "Eigentumsschutz und EBV", im Text aber
     auf jeder Zeile. */
  const rumpf = kapitel.text.toLowerCase();
  let imText = 0;
  for (const w of suchWoerter) if (rumpf.includes(w)) imText++;
  punkte += Math.min(imText, 8);

  for (const z of normZeichen(thema.normen)) {
    if (nummerDrin(kapitel.titel, z)) punkte += 6;
    else if (nummerDrin(rumpf, z)) punkte += 2;
  }
  return punkte;
}

export function wissenFuer(thema, opt = {}) {
  if (!thema?.titel) return null;
  const index = wissenIndex(opt);
  if (!index.length) return null;
  if (thema.wissen) {
    const treffer = index.find((k) => k.id === thema.wissen);
    if (treffer) return zuschneiden(treffer, opt);
  }
  const gebiet = thema.klausur || 0;
  const zweitesExamen = /2\./.test(thema.examen || "");
  let bestes = null, beste = 0, zweitbeste = 0;
  for (const k of index) {
    /* Register taugen nicht als Belegstelle: Band 7 (Register und Lexikon)
       und die Paritätsbände 42-45 (Lexikon- und Seitenlisten je Stichwort)
       sind Nachschlagelisten, keine Darstellung. Sie liegen der
       Vollständigkeit halber im Tresor; ein Zeiger am Thema darf weiter
       hinein zeigen, von allein gewählt werden sie nicht. */
    if (REGISTER_BAENDE.has(k.band)) continue;
    const land = LAND_KAPITEL.exec(k.titel);
    if (land && !thema.titel.includes(land[1])) continue;
    /* Sammelkapitel sind Behälter, keine Fundstellen: "Weitere Vollfälle"
       fasst 380 KB aus allen drei Gebieten zusammen und gewinnt allein durch
       seine Länge jeden Wortabgleich - der Auszug daraus wäre dann der erste
       Fall im Behälter, nicht der zum Thema. */
    if (k.text.length > SAMMELKAPITEL) continue;
    const kg = kapitelGebiet(k);
    if (gebiet && kg && kg !== gebiet) continue;
    let p = wissenBewerten(thema, k);
    /* Erstes und zweites Examen behandeln dieselben Stichworte verschieden -
       "Zuständigkeit" heisst im ersten Examen Rechtsweg und im zweiten die
       Wahl zwischen Schöffengericht und Landgericht. */
    const assessorBand = [4, 5, 6].includes(k.band);
    if (zweitesExamen === assessorBand) p += 2;
    /* Gleichstand: das zuerst gelesene Kapitel gewinnt, damit bei jedem Lauf
       dieselbe Stelle herauskommt. */
    if (p > beste) { zweitbeste = beste; beste = p; bestes = k; }
    else if (p > zweitbeste) zweitbeste = p;
  }
  const schwelle = opt.schwelle ?? CONFIG.wissen?.schwelle ?? 8;
  if (!bestes || beste < schwelle) return null;
  /* Der Abstand zum Zweitplatzierten entscheidet, nicht die Punktzahl allein.
     Ein fester Schwellwert trennt hier nichts: "Beweisverwertungsverbote"
     gewinnt mit 16 Punkten so deutlich wie "Familienrecht" mit 3. Liegen
     dagegen "Diebstahl und Unterschlagung" (14) und "Betrug" (13) fast
     gleichauf, ist keines von beiden die Stelle zum Thema "Wie grenzt man
     Diebstahl und Betrug ab?" - dann lieber gar keine Quelle. */
  const vorsprung = opt.vorsprung ?? CONFIG.wissen?.vorsprung ?? 1.2;
  if (zweitbeste > 0 && beste < zweitbeste * vorsprung) return null;
  return zuschneiden(bestes, opt);
}

/* Der Auszug wird gedeckelt: ein ganzes Kapitel aus Band 9 waere ein halber
   Roman, und jedes Zeichen kostet im Tagesbudget mit. Geschnitten wird an
   einer Absatzgrenze, nicht mitten im Satz. */
export function zuschneiden(kapitel, opt = {}) {
  const deckel = opt.zeichen ?? CONFIG.wissen?.zeichen ?? 4000;
  let text = kapitel.text;
  if (text.length > deckel) {
    const schnitt = text.lastIndexOf("\n", deckel);
    text = `${text.slice(0, schnitt > deckel * 0.6 ? schnitt : deckel).trim()}\n[…]`;
  }
  return { ...kapitel, text };
}

/* Der Block, der im Auftrag an das Modell landet.

   Die Regel ist bewusst dreigeteilt statt pauschal "nicht abschreiben". Ein
   anerkanntes Prüfungsschema ist Allgemeingut - es umzubauen, nur damit es
   anders aussieht, macht den Beitrag schlechter, nicht eigenständiger. Bei
   Fällen genügen andere Namen und Zahlen. Und die Erklärprosa schreibt der
   Bot selbst, aber nicht aus Rechtsgründen: Ein abgeschriebener
   Lehrbuchabsatz klingt auf Instagram wie ein Fremdkörper. */
export function belegstelle(thema, opt = {}) {
  const k = wissenFuer(thema, opt);
  if (!k) return "";
  const woher = `${k.bandTitel}${k.teil ? `, ${k.teil}` : ""}, Kapitel ${k.nr}: ${k.titel}`;
  return [
    `BELEGSTELLE AUS DEM HANDBUCH (${woher}).`,
    "Was darin steht, gilt: Zahlen, Fristen, Normen, Reihenfolgen und Streitstände daraus übernehmen. Was nicht darin steht, ist deshalb nicht falsch.",
    "So damit umgehen:",
    "– Prüfungsschemata, Aufbau und Definitionen dürfen der Belegstelle folgen. Ein anerkanntes Schema ist Allgemeingut; baue es nicht um, nur damit es anders aussieht – die Leute sollen es in der Klausur wiedererkennen.",
    "– Fälle und Beispiele darfst du übernehmen, aber ändere Namen, Orte, Beträge, Waren und Daten. Der Rechtskern bleibt, die Einkleidung wird deine.",
    "– Erklärenden Fließtext schreibe in eigenen Worten. Nicht aus Rechtsgründen, sondern weil dieser Kanal eine eigene Stimme hat: Ein abgeschriebener Lehrbuchabsatz klingt zwischen den anderen Beiträgen wie ein Fremdkörper.",
    k.text,
    "ENDE DER BELEGSTELLE.",
  ].join("\n");
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const index = wissenIndex();
  console.log(`${index.length} Kapitel aus ${new Set(index.map((k) => k.band)).size} Bänden`);
  for (const b of [...new Set(index.map((k) => k.band))].sort()) {
    const k = index.filter((x) => x.band === b);
    console.log(`  Band ${b}: ${k.length} Kapitel, ${k.reduce((a, x) => a + x.text.length, 0)} Zeichen`);
  }
}
