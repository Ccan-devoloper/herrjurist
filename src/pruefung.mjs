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

/* Nachträglich gesperrte Namen (z. B. aus früheren Beiträgen) kommen in
   denselben Topf wie die Sperrliste: Prompt und Prüfung sehen sie gleich. */
export function namenSperren(liste) {
  const k = korpus();
  for (const n of liste || []) if (n && !k.namen.includes(n)) k.namen.push(n);
  return k.namen.length;
}

/* Erfundene Firmennamen in einem Text („Nordlicht GmbH“ → „Nordlicht“).
   Nur der Stamm zählt, damit auch „Nordlicht KG“ oder „Nordlicht AG“ als
   Wiederholung gilt. Gattungswörter und Artikel davor sind keine Namen. */
const FIRMENFORM = /(?:^|[^A-Za-zÄÖÜäöüß-])((?:[A-ZÄÖÜ][a-zäöüß]+(?:-[A-ZÄÖÜ][a-zäöüß]+)?)(?: [A-ZÄÖÜ][a-zäöüß]+)?) (?:GmbH & Co\. KG|GmbH|KG|AG|OHG|UG|GbR|e\. ?K\.|SE)(?![A-Za-zäöüß])/g;
const KEIN_FIRMENNAME = /^(?:Die|Der|Das|Des|Dem|Den|Eine?|Einer|Diese|Dieser|Jede|Jeder|Keine|Unsere|Ihre|Seine|Neue|Alte|Zwei|Drei|Vier|Beteiligung|Holding|Tochter|Mutter|Vertrieb|Handel|Bau|Immobilien|Verwaltung|Beratung|Kapital|Personen|Gesellschaft|Firma|Mini-Fall|Beispiel|Fall|Zwischen)$/;
export function firmenNamen(text) {
  const namen = new Set();
  for (const m of String(text).matchAll(FIRMENFORM)) {
    /* Voranstehende Artikel und Gattungswörter („Mini-Fall Nordlicht GmbH“) gehören nicht zum Namen. */
    const teile = m[1].trim().split(" ");
    while (teile.length > 1 && (KEIN_FIRMENNAME.test(teile[0]) || /(?:beispiel|fall|sachverhalt|firma)$/i.test(teile[0]))) teile.shift();
    const stamm = teile.join(" ");
    const letztes = stamm.split(" ").pop();
    if (KEIN_FIRMENNAME.test(stamm) || KEIN_FIRMENNAME.test(letztes) || /(?:ung|heit|keit|schaft)$/.test(letztes) || stamm.length < 4) continue;
    namen.add(stamm);
  }
  return [...namen];
}

/* Firmennamen aus allen bereits geschriebenen Inhalten der letzten Tage –
   bis zum Vortag, damit ein heute schon geschriebener Text sich nicht selbst
   sperrt, wenn er vor dem Veröffentlichen erneut geprüft wird. Ein
   erfundener Name ist nur dann unverdächtig, wenn er jedes Mal ein anderer
   ist: dieselbe „Nordlicht GmbH“ in zehn Beiträgen wirkt wie ein
   übernommener Fall. */
export function benutzteFirmen(inhalteDir, datum, tage = 180) {
  if (!inhalteDir || !fs.existsSync(inhalteDir)) return [];
  const ab = new Date(new Date(`${datum}T12:00:00Z`).getTime() - tage * 864e5).toISOString().slice(0, 10);
  const namen = new Set();
  for (const datei of fs.readdirSync(inhalteDir).sort()) {
    const tag = datei.slice(0, 10);
    if (!datei.endsWith(".json") || tag < ab || tag >= datum) continue;
    try { for (const n of firmenNamen(fs.readFileSync(path.join(inhalteDir, datei), "utf8"))) namen.add(n); } catch { /* defekte Datei zählt nicht */ }
  }
  return [...namen];
}

export function gesperrteNamen(text, k = korpus()) {
  const t = ` ${String(text)} `;
  return k.namen.filter((n) => new RegExp(`(^|[^a-zäöüß])${n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}([^a-zäöüß]|$)`, "u").test(t));
}

/* „Skript“ nur noch als Quellenangabe, nicht als blosses Wort: „laut Skript“
   ist ein Verweis auf das Kursmaterial, „nimm dir heute dein Skript vor“ ist
   ein Lerntipp. Auf dem Schwesterkanal kostete genau dieser Unterschied am
   16.09. eine Countdown-Story. */
const QUELLENBEZUG = /\b(laut Quelle|Quelle|Seite \d+|Folie|Mitschrift|(?:laut|im|aus dem|nach dem|siehe) Skript|Skript,? S\. ?\d+|Originalfall|Fall \d{2,3}|Hausaufgabe|Musterlösung der Finanzverwaltung|Frame)\b/i;

/* Vorstellungen vom Prüfungsablauf, die aus dem Steuerberaterexamen stammen und
   im Staatsexamen falsch sind. Als Regel steht das im Auftrag ans Modell, aber
   eine Regel ist eine Bitte - der Beitrag „Der Klassiker in der zweiten
   Klausurenrunde“ war schon draußen. Deshalb hier hart:

   - Reihenfolge: Welches Gebiet an welchem Tag drankommt, entscheidet jedes
     Land und jeder Durchgang neu. Es gibt keine „zweite Klausurenrunde“.
   - Punkte je Prüfungsschritt: Bewertet wird die Klausur als Ganzes (0 bis 18
     Notenpunkte). „Hier verlierst du die meisten Punkte“ verspricht eine
     Punkteverteilung, die es nicht gibt. Die Notenpunkte selbst bleiben
     erlaubt - deshalb steht „Punkte“ nur zusammen mit verlieren, kosten,
     bringen oder Verteilung in der Liste. */
const EXAMENSABLAUF = [
  [/\b(erste|zweite|dritte|vierte|fünfte|sechste)[nrms]?\s+(Klausurenrunde|Klausurrunde|Prüfungstag|Prüfungstages|Klausurtag)/i, "Es gibt keine feste Reihenfolge der Klausuren – welches Gebiet wann drankommt, entscheidet jedes Land neu."],
  [/\b(am|im)\s+(zweiten|dritten|vierten|fünften|sechsten)\s+(Tag|Prüfungstag)/i, "Es gibt keine feste Reihenfolge der Klausuren."],
  [/\bdie\s+(zweite|dritte|vierte|fünfte|sechste)\s+Klausur\b/i, "Die Klausuren sind nicht durchnummeriert – welches Gebiet wann drankommt, ist offen."],
  [/\b(verlierst|verlieren|verliert|kostet|kosten|bringt|bringen)\s+(dich\s+|du\s+)?(die\s+meisten\s+|am\s+meisten\s+|\d+\s+)?Punkte?\b/i, "Im Staatsexamen gibt es keine Punkte je Prüfungsschritt – schreib, was der Fehler anrichtet (Aufbau, Anspruchsgrundlage, Verständnis)."],
  [/\bPunkte(verteilung|vergabe)\b/i, "Eine Punkteverteilung je Prüfungspunkt gibt es im Staatsexamen nicht."],
  [/\bTextziffer\b/i, "„Textziffer“ ist Steuerberaterexamen, nicht Staatsexamen."],
  [/\bBuchungssatz\b/i, "Buchungssätze gehören nicht in einen Kanal zum juristischen Staatsexamen."],
  /* Das Grundgesetz und die europäischen Verträge kennen keine Paragrafen.
     Ein Reel zur Koalitionsfreiheit schrieb durchgehend „Paragraf 9“ statt
     „Art. 9 Abs. 3 GG“ - der Faktencheck hat es gefunden, aber erst nachdem
     das Skript geschrieben war. Hier kostet es nichts. Beide Schreibweisen
     prüfen: Auf dem Bildschirm steht „§“, im Sprechertext „Paragraf“. */
  [/(?:§§?\s*|\bParagra(?:f|ph)(?:en)?\s+)\d+[a-z]?(?:\s+(?:Abs\.|Absatz|S\.|Satz|Nr\.|Nummer|Alt\.|Alternative|Var\.|Variante|Hs\.|Halbsatz)\s*\d+[a-z]?)*\s+(?:GG|AEUV|EUV|EMRK|GRCh)\b/, "Grundgesetz und europäische Verträge werden mit Artikel zitiert, nicht mit Paragraf (Art. 9 Abs. 3 GG statt § 9 GG)."],
  /* Ankündigungen auf ein nächstes Mal: Der Feed sortiert nicht chronologisch,
     ein Beitrag wird Monate später gesehen, und eingelöst wird so ein
     Versprechen ohnehin nie. */
  [/\b(n(ä|ae)chste[ns]?\s+(Mal|Reel|Beitrag|Woche)\s+(zeige|erkl(ä|ae)re|geht|kommt|schauen|sehen)|Teil\s+2\s+folgt|dazu\s+mehr\s+im\s+n(ä|ae)chsten)/i, "Keine Ankündigung auf ein nächstes Mal – der Beitrag muss für sich stehen."],
];

/* ==========================================================================
   Normfallen: feste Zahlen, die im Gesetz stehen und nicht verhandelbar sind.

   Am 14.09. ging ein Beitrag zur gesetzlichen Erbfolge raus, der die Ehefrau
   neben zwei Kindern auf 3/4 setzte. Richtig ist 1/2. Der Fehler: § 1931
   Abs. 1 BGB gibt dem Ehegatten neben Verwandten ERSTER Ordnung ein Viertel
   und nur neben der zweiten Ordnung oder Großeltern die Hälfte - der Beitrag
   hatte beide Fälle vertauscht und dann noch § 1371 I BGB daraufgerechnet.

   Warum das durch alle Netze fiel:
   - Der Faktencheck ist ein Modell und hat es schlicht übersehen.
   - Die Quotensumme stimmte (3/4 + 1/8 + 1/8 = 1), eine Summenprobe hätte
     also nichts gemerkt.
   - Die Wissensbasis nennt die Quoten gar nicht, sie sagt nur, das
     Ehegattenerbrecht sei "mit dem Güterstand zu kombinieren".

   Gegen so etwas hilft kein weiteres Modell, sondern eine Handvoll fester
   Regeln, die rechnen statt zu urteilen. Sie kosten nichts, laufen vor jedem
   Modellaufruf und sind absichtlich eng: Lieber wenige Fälle sicher als viele
   halb. Wer eine neue Regel aufnimmt, nimmt eine auf, die er beweisen kann.
   ========================================================================== */

/* Ein Bruch, der einer Norm zugeordnet wird: "1/4 (§ 1931 I BGB)". Genau die
   Form, in der eine Quote auf den Fall angewendet wird - im Unterschied zum
   erklärenden Satz "neben der ersten Ordnung 1/4, neben der zweiten 1/2",
   der beide Zahlen nennen darf und muss. */
const QUOTE_ZU_NORM = /(\d+)\s*\/\s*(\d+)\s*\(\s*§+\s*(\d+[a-z]?)/g;

const ERSTE_ORDNUNG = /\b(Kind(er|es|ern)?|Abkömmling|Abkömmlinge|Sohn|Tochter|erste[nr]?\s+Ordnung)\b/i;
const ZWEITE_ORDNUNG = /\b(Eltern|Mutter|Vater|Geschwister|Bruder|Schwester|zweite[nr]?\s+Ordnung|Großeltern)\b/i;

export function normfallen(text) {
  const fehler = [];

  /* § 1931 Abs. 1 BGB: 1/4 neben der ersten Ordnung, 1/2 neben der zweiten
     oder neben Großeltern. Geprüft wird nur die angewendete Quote. */
  for (const [, zaehler, nenner, norm] of text.matchAll(QUOTE_ZU_NORM)) {
    if (norm !== "1931") continue;
    const anteil = Number(zaehler) / Number(nenner);
    const kinder = ERSTE_ORDNUNG.test(text);
    if (kinder && anteil !== 0.25) {
      fehler.push(`§ 1931 Abs. 1 BGB: Neben Verwandten der ersten Ordnung (hier: Kinder/Abkömmlinge) erbt der Ehegatte 1/4, nicht ${zaehler}/${nenner}. Die Hälfte gilt nur neben der zweiten Ordnung oder neben Großeltern.`);
    } else if (!kinder && ZWEITE_ORDNUNG.test(text) && anteil !== 0.5) {
      fehler.push(`§ 1931 Abs. 1 BGB: Neben Verwandten der zweiten Ordnung oder Großeltern erbt der Ehegatte 1/2, nicht ${zaehler}/${nenner}.`);
    }
  }

  /* § 1371 Abs. 1 BGB setzt Zugewinngemeinschaft voraus. Wer das Viertel
     aufschlägt, ohne den Güterstand zu nennen, rechnet auf einer Annahme,
     die im Sachverhalt nicht steht. */
  if (/§+\s*1371/.test(text) && !/Zugewinngemeinschaft|gesetzlich(en|er)\s+Güterstand/i.test(text)) {
    fehler.push("§ 1371 Abs. 1 BGB gilt nur bei Zugewinngemeinschaft – der Güterstand muss im Sachverhalt genannt sein, sonst steht die Quote auf einer Annahme.");
  }

  return fehler;
}

/* Normen sind wörtlich erlaubt – sie sind Gesetzestext-Zitate, keine Übernahme.
   Deshalb werden Normzitate (auch ohne Gesetzesangabe, in beliebiger
   Reihenfolge von Abs./S./Nr./Buchst.) vor dem Shingle-Vergleich entfernt. */
const NORM = /(?:§§?|Art\.|Artikel|R|H)\s*\d+(?:\.\d+)?[a-z]?(?:\s*(?:\(\d+[a-z]?\)|[a-z]{2}\)|Abs\.|Absatz|S\.|Satz|Nr\.|Nummer|Buchst\.|Buchstabe|Hs\.|Halbsatz|Alt\.|Var\.|lit\.)\s*[\da-z]*\)?)*(?:\s*(?:i\.?\s?V\.?\s?m\.?|iVm|in Verbindung mit)\s*(?:§§?\s*)?\d+[a-z]?(?:\s*(?:Abs\.|S\.|Nr\.|Buchst\.)\s*[\da-z]+)*)?\s*(?:BGB|StGB|StPO|ZPO|GG|VwGO|VwVfG|HGB|GmbHG|AktG|InsO|GVG|ArbGG|KSchG|BetrVG|MuSchG|BEEG|TVG|ProdHaftG|StVG|StVO|OWiG|JGG|GewO|BauGB|BImSchG|PolG|SGB|AEUV|EUV|GRCh|EMRK|BVerfGG|RVG|BRAO|FamFG|WEG|ErbbauRG)?\b/g;
/* Eine Norm ohne Gesetz ist auf der Buehne wertlos: „§ 20" sagt niemandem,
   welches Gesetz gemeint ist. Am 17.09. standen „§ 3 vs. § 7", „§ 20" und
   „§ 9 + § 11" auf den Stichwortzeilen eines Reels - das ErbStG stand nur im
   Datensatz, nicht im Bild. Gefunden wird jede Paragrafen- oder
   Artikelnennung, hinter der bis zum Ende der Zeile kein Gesetzeskuerzel mehr
   folgt. Aufzaehlungen („§ 9 + § 11 ErbStG") gelten damit als versorgt. */
/* Erkannt wird ein Gesetz auf drei Wegen: die bekannten Kuerzel, ein
   Kuerzel-Muster (Grossbuchstabe, Endung G/GB/O/V/StG/VO/R/H/AE - BGB, OWiG,
   UStAE, LBauO) und der volle Name („Grundgesetz“, „Versammlungsgesetz“,
   „Bauordnung“). Die Liste allein reichte nicht: Jedes Gesetz, das nicht
   darin stand, galt als fehlend, und seit der Sprechtext mitgeprueft wird,
   kostete das eine Neufassung oder das ganze Reel. Lieber ein nacktes „§ 3“
   uebersehen als ein richtiges Reel verwerfen. */
const GESETZ_KUERZEL = new RegExp([
  "\\b(?:BGB|StGB|StPO|ZPO|GG|VwGO|VwVfG|HGB|GmbHG|AktG|InsO|GVG|ArbGG|KSchG|BetrVG|MuSchG|BEEG|TVG|ProdHaftG|StVG|StVO|OWiG|JGG|GewO|BauGB|BImSchG|PolG|SGB|AEUV|EUV|GRCh|EMRK|BVerfGG|RVG|BRAO|FamFG|WEG|ErbbauRG)\\b",
  "\\b[A-ZÄÖÜ][A-Za-zÄÖÜäöü]{1,10}(?:GB|StG|StR|VO|AE|G|O|V|R|H)\\b",
  "\\b[A-ZÄÖÜ][A-Za-zÄÖÜäöü-]+(?:gesetz|gesetzbuch|ordnung|verordnung|richtlinie|vertrag|charta|konvention)\\b",
].join("|"));   // bewusst ohne "i": Mit ihm galt „Vorgang“ als Gesetz (V…g)
/* Auch die gesprochene Form zählt: „Paragraf 3“ ohne ErbStG ist für die Hörerin
   genauso ein halber Satz wie „§ 3“ ohne Gesetz für die Leserin. Das Campus-Reel
   vom 17.09. sagte „Paragraf 3 oder Paragraf 7 Absatz 1 Nummer 1“ – und nirgends
   im ganzen Sprechtext das Gesetz. */
export function normenOhneGesetz(text) {
  const t = String(text || "");
  const treffer = [];
  for (const m of t.matchAll(/(?:§§?|Art\.|Artikel|Paragraf(?:en)?)\s*\d+[a-z]?/g)) {
    if (!GESETZ_KUERZEL.test(t.slice(m.index + m[0].length))) treffer.push(m[0]);
  }
  return treffer;
}

export function ohneNormen(text) {
  return String(text).replace(NORM, " NORM ").replace(/\b(Abs|S|Nr|Buchst|Hs|Alt)\.\s*\d+[a-z]?/g, " NORM ").replace(/\(\d+[a-z]?\)/g, " NORM ");
}

/* Alles, was auf einer Kachel steht - und zwar wirklich alles.

   Bis zum 14.09. fehlten hier ausgerechnet die Felder der Rechenfolie:
   formel, zeilen, ergebnis. Die Folie, auf der die Zahlen stehen, war für
   jede Prüfung in dieser Datei unsichtbar - für die Übernahmeprüfung, für
   die Namenssperre, für die Examensablauf-Regeln. Aufgefallen ist es, als
   die falsche Erbquote durchlief: Der Faktencheck sah die Formel (siehe
   textAus in faktencheck.mjs), diese Prüfung nicht.

   Wer hier ein Feld ergänzt, ergänzt es auch in textAus - die beiden müssen
   dasselbe sehen. */
function alleTexte(beitrag) {
  const teile = [];
  for (const f of beitrag.folien || []) {
    teile.push(
      f.titel || "", f.untertitel || "", f.text || "", f.definition || "",
      ...(f.punkte || []),
      ...(f.schritte || []).map((s) => (typeof s === "string" ? s : `${s.titel || ""} ${s.text || ""}`)),
      f.formel || "", ...(f.zeilen || []), f.ergebnis || "", f.erklaerung || "",
      /* Jede Spalte am Stück: Überschrift, Text, Punkte. Vorher standen erst
         beide Überschriften und dann alle Punkte hintereinander - damit ging
         verloren, zu welcher Seite ein Punkt gehört, und genau das IST bei
         einer Vergleichsfolie die Aussage. Auf dem Schwesterkanal stand
         deshalb am 15.09. ein Punkt der linken Spalte im Prüftext direkt
         hinter der rechten Überschrift. */
      ...[f.links, f.rechts].filter(Boolean).flatMap((sp) => [sp.titel || "", sp.text || "", ...(sp.punkte || [])]),
    );
  }
  teile.push(beitrag.caption || "", beitrag.kurztitel || "");
  for (const s of beitrag.szenen || []) teile.push(s.titel || "", s.text || "", s.norm || "", s.sprecher || "", ...(s.marken || []));
  for (const s of beitrag.stories || []) {
    teile.push(s.ueberzeile || "", s.titel || "", s.text || "", s.norm || "", s.formel || "", s.zahl || "", s.richtigText || "", s.falsch || "", ...(s.optionen || []));
  }
  return teile.filter(Boolean);
}

/* Fallnamen ohne Sachverhalt.

   Am 16.09. erschien ein Karussell zur Leistungskondiktion, das ab Folie 2
   von „Finn" und „Nora" erzaehlte - Betraege, Ueberweisung, Reise. Wer die
   beiden sind, stand nur in der Caption, und die ist zugeklappt. Wer auf
   einer Folie handelt, muss auf einer Folie eingefuehrt worden sein.

   Gesucht wird die typische Fallhandlung: Name + Taetigkeitswort. Kopula
   („ist", „war") bleibt bewusst draussen - „Fraglich ist ..." ist kein Fall,
   sondern juristische Normalsprache. Zusaetzlich braucht es zwei
   verschiedene Namen oder zwei Handlungen, damit ein einzelner Satzanfang
   keinen fertigen Beitrag kippt. */
const FALLHANDLUNG = /(?:^|[.!?;:]\s+|\n)([A-ZÄÖÜ][a-zäöüß]{2,})\s+(?:hat|hatte|kauft|kaufte|verkauft|verkaufte|zahlt|zahlte|überweist|überwies|erhält|erhielt|bucht|buchte|klagt|klagte|gibt|gab|schuldet|schuldete|verlangt|verlangte|liefert|lieferte|bestellt|bestellte|vermietet|vermietete|erbt|erbte|schließt|schloss|meldet|meldete|beantragt|beantragte|veräußert|veräußerte|entnimmt|entnahm|bilanziert|bilanzierte|unterschreibt|unterschrieb|kündigt|kündigte|widerruft|widerrief|ficht|focht)\b/g;
const SACHVERHALT_TITEL = /^(sachverhalt|der sachverhalt|der fall|fall|ausgangsfall|worum es geht)\b/i;
/* Satzanfaenge, die wie ein Name aussehen, aber keiner sind. */
const KEIN_FALLNAME = new Set(["wichtig", "entscheidend", "fraglich", "problematisch", "ergänzend", "zusätzlich", "anders",
  "ebenso", "darüber", "hierbei", "dabei", "danach", "deshalb", "daher", "zudem", "allerdings", "jedoch", "sodann",
  "schließlich", "letztlich", "grundsätzlich", "ausnahmsweise", "folglich", "mithin", "insoweit", "insbesondere",
  "typisch", "klassisch", "denkbar", "möglich", "nötig", "erforderlich", "maßgeblich", "relevant", "umstritten",
  "strittig", "richtig", "falsch", "damit", "dazu", "dann", "hier", "dort", "jeder", "jede", "jedes", "niemand",
  "dieser", "diese", "dieses", "beide", "keiner", "keine", "wer", "was", "wann", "warum", "wie", "wenn", "aber",
  "auch", "noch", "erst", "nur", "sogar", "gerade", "eben", "trotzdem", "dennoch", "wichtige", "viele", "manche"]);

const folienText = (f) => [
  f.titel, f.untertitel, f.text, f.definition,
  ...(f.punkte || []),
  /* Schritt-Ueberschrift und Schritt-Text auf eigene Zeilen: In einer Zeile
     stuende „Etwas erlangt Finn hat 4.320 Euro ..." - der Name saesse mitten
     im Satz und die Fallhandlung bliebe unsichtbar. */
  ...(f.schritte || []).flatMap((s) => (typeof s === "string" ? [s] : [s.titel || "", s.text || ""])),
  f.ergebnis, f.erklaerung,
  ...[f.links, f.rechts].filter(Boolean).flatMap((sp) => [sp.titel, sp.text, ...(sp.punkte || [])]),
].filter(Boolean).join("\n");

export function fallnamenOhneSachverhalt(beitrag) {
  const folien = beitrag?.folien || [];
  if (folien.length < 2) return [];
  const istSachverhalt = (f) => SACHVERHALT_TITEL.test(String(f.titel || "").trim());
  /* Alles, was im Sachverhalt steht, gilt als vorgestellt. */
  const vorgestellt = new Set();
  for (const f of folien.filter(istSachverhalt)) {
    for (const m of folienText(f).matchAll(/\b([A-ZÄÖÜ][a-zäöüß]{2,})\b/g)) vorgestellt.add(m[1]);
  }
  const zaehler = new Map();
  for (const f of folien) {
    if (istSachverhalt(f)) continue;
    for (const m of folienText(f).matchAll(FALLHANDLUNG)) {
      const name = m[1];
      if (vorgestellt.has(name) || KEIN_FALLNAME.has(name.toLowerCase())) continue;
      zaehler.set(name, (zaehler.get(name) || 0) + 1);
    }
  }
  const namen = [...zaehler.keys()];
  const handlungen = [...zaehler.values()].reduce((a, b) => a + b, 0);
  return namen.length >= 2 || handlungen >= 2 ? namen : [];
}

/* --- Quiz-Invarianten (Safety 0a) ---------------------------------------
   Anlass ist ein echter Vorfall vom 16.09.2026 auf beiden Kanaelen: Eine
   Frage-Story und ihre Antwort-Story wurden getrennt neu geschrieben. Danach
   zeigte die Frage die Optionen A Wirtschaftsgut / B Rueckstellung /
   C Merkposten, die bereits bestehende Antwort trug dieselben Optionen in
   anderer Reihenfolge und markierte Index 1. Inhaltlich sagte die Frage damit
   C, die Antwort markierte B. Beim Schwesterkanal erschien die Antwort
   ausserdem einige Minuten VOR der endgueltigen Frage.

   Die Optionsfolge ist Semantik, nicht Darstellung: [A,B,C] ist nicht [A,C,B].
   Deshalb wird elementweise verglichen, nicht als Menge. Und der Index wird
   strukturell geprueft - das kostet nichts und faengt genau den Fall, in dem
   ein formal gueltiger Index auf die falsche Option zeigt, weil sich die
   Reihenfolge darunter geaendert hat.

   Diese Pruefung ist deterministisch. Sie ersetzt nicht die fachliche Frage,
   ob die markierte Option auch die richtige ist - dafuer muss der Faktencheck
   die Markierung ausdruecklich sehen (Safety 0b). */
export const QUIZ_OPTIONEN = 3;
const QUIZ_ARTEN = ["frage", "antwort"];

/** Schluessel, unter dem Frage und Antwort zusammengehoeren. */
export const paarSchluessel = (s) => s?.pairId || s?.themaId || null;

/**
 * Deterministische Befunde zu Quiz-Stories. Leeres Array heisst: in Ordnung.
 * @param {object[]} stories - Story-Objekte, gern gemischt mit anderen Arten.
 * @returns {string[]} Befunde im Klartext, je mit Slot in eckigen Klammern.
 */
export function quizBefunde(stories = []) {
  const fehler = [];
  const quiz = (stories || []).filter((s) => s && QUIZ_ARTEN.includes(s.art));
  for (const s of quiz) {
    const wo = `[${s.slot || s.art}]`;
    const opt = s.optionen;
    if (!Array.isArray(opt) || opt.length !== QUIZ_OPTIONEN) {
      fehler.push(`${wo} Quiz braucht genau ${QUIZ_OPTIONEN} Optionen (gefunden: ${Array.isArray(opt) ? opt.length : "keine"}).`);
      continue;
    }
    if (opt.some((o) => typeof o !== "string" || !o.trim())) {
      fehler.push(`${wo} Quiz enthaelt eine leere Option.`);
      continue;
    }
    /* Die Antwort MUSS markieren, die Frage darf. Ein Index ausserhalb der
       Liste ist immer ein Fehler - auch dann, wenn er nur um eins daneben
       liegt. */
    const markiert = s.richtig;
    if (s.art === "antwort" || markiert != null) {
      if (!Number.isInteger(markiert) || markiert < 0 || markiert >= opt.length) {
        fehler.push(`${wo} Markierte Option „${markiert}" liegt ausserhalb der ${opt.length} Optionen.`);
      }
    }
  }
  /* Paarpruefung: gleiche Optionen in gleicher Reihenfolge, gleiche Markierung. */
  const paare = new Map();
  for (const s of quiz) {
    const k = paarSchluessel(s);
    if (!k) continue;
    const eintrag = paare.get(k) || {};
    eintrag[s.art] = s;
    paare.set(k, eintrag);
  }
  for (const [, { frage, antwort }] of paare) {
    if (!frage || !antwort) continue;
    const a = frage.optionen, b = antwort.optionen;
    if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) continue;   // schon oben gemeldet
    const abweichung = a.findIndex((x, i) => x !== b[i]);
    if (abweichung >= 0) {
      fehler.push(`[${antwort.slot}] Antwort und Frage [${frage.slot}] tragen nicht dieselbe Optionsfolge: Platz ${abweichung + 1} ist „${b[abweichung]}" statt „${a[abweichung]}". Die Reihenfolge ist Teil der Aussage.`);
      continue;
    }
    if (frage.richtig != null && antwort.richtig != null && frage.richtig !== antwort.richtig) {
      fehler.push(`[${antwort.slot}] Frage [${frage.slot}] markiert Option ${frage.richtig + 1}, die Antwort Option ${antwort.richtig + 1}.`);
    }
  }
  return fehler;
}

/**
 * Darf diese Antwort-Story jetzt erscheinen? Eine Antwort ohne ihre Frage ist
 * fuer die Lesenden sinnlos; am 16.09. ging sie beim Schwesterkanal sogar
 * zuerst raus. Geplante Uhrzeiten sind keine Abhaengigkeit - der Zustand ist
 * es.
 * @returns {{status:"frei"|"warten"|"verfallen", frage:object|null, grund:string}}
 */
export function quizReihenfolge(antwortEintrag, planStories = []) {
  const k = paarSchluessel(antwortEintrag);
  const frage = (planStories || []).find((s) => s.art === "frage" && paarSchluessel(s) === k && k != null) || null;
  if (!frage) return { status: "frei", frage: null, grund: "keine zugehoerige Frage im Plan" };
  if (frage.status === "veroeffentlicht") return { status: "frei", frage, grund: "Frage ist veroeffentlicht" };
  if (frage.fehler || frage.status === "uebersprungen") {
    return { status: "verfallen", frage, grund: `Frage ${frage.slot} erscheint heute nicht` };
  }
  return { status: "warten", frage, grund: `Frage ${frage.slot} ist noch nicht veroeffentlicht` };
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

  /* 2c. Fallnamen, die nur die Caption kennt. */
  const ohneSachverhalt = fallnamenOhneSachverhalt(beitrag);
  if (ohneSachverhalt.length) fehler.push(`${ohneSachverhalt.join(" und ")} handel${ohneSachverhalt.length > 1 ? "n" : "t"} auf den Folien, ohne vorgestellt zu sein: Entweder eine Folie „Sachverhalt“ direkt nach der Titelfolie (Fall in 2–4 Sätzen, mit allen Namen und Zahlen, die die Lösung benutzt) – oder den Beitrag abstrakt formulieren, ganz ohne Namen. Die Caption genügt nicht, sie ist zugeklappt.`);

  /* 3. Quellenbezüge */
  if (QUELLENBEZUG.test(gesamt)) fehler.push(`Bezug auf Kursquelle/Seiten/Fallnummern entfernen: ${gesamt.match(QUELLENBEZUG)[0]}`);

  /* 3b. Vorstellungen vom Prüfungsablauf, die es im Staatsexamen nicht gibt. */
  for (const [muster, grund] of EXAMENSABLAUF) {
    const treffer = gesamt.match(muster);
    if (treffer) fehler.push(`„${treffer[0]}“: ${grund}`);
  }

  /* 3c. Normfallen: feste Gesetzeszahlen, die nicht verhandelbar sind.
        Deterministisch und vor jedem Modellaufruf - hier kostet ein Fund
        nichts, im Feed kostet er den Beitrag. */
  fehler.push(...normfallen(gesamt));

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
