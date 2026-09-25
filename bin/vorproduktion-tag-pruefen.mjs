#!/usr/bin/env node
/**
 * Prüft redaktionell geschriebene Vorproduktionstage (vorproduktion/<datum>.json)
 * gegen die Veröffentlichungsregeln, ohne etwas zu rendern oder aufzurufen.
 * Aufruf: node bin/vorproduktion-tag-pruefen.mjs vorproduktion/2026-10-11.json …
 * Exportiert tagPruefen() für die Übernahme.
 */
import fs from "node:fs";
import { quizPruefen } from "./vorproduktion-quiz-regel.mjs";

const ICON_KEYS = new Set("waage rechner kalender gebaeude diagramm dokument warnung uhr muenzen haus lkw vertrag lupe kreislauf blitz buch fabrik person personen globus paragraf haken kreuz zielscheibe trophaee polizei richter detektiv arzt buero landwirt mechaniker bauarbeiter senior baby achselzucken familie hochzeit handschlag gericht krankenhaus schule hotel laden bank baustelle haeuser ruine tuer wahlurne polizeiauto auto taxi motorrad fahrrad bus zug sattelzug traktor schiff flugzeug krankenwagen tanken anker rakete verbot stopp schild feuer messer dolch sarg geldbeutel banknote kreditkarte quittung hauptbuch geld-weg einkaufswagen paket handtasche edelstein kurve-hoch kurve-runter medaille abschluss stoppuhr ordner aktenschrank aktentasche klemmbrett schriftrolle umschlag fueller zeitung etikett link bueroklammer schere kamera handy laptop fernseher mikrofon megafon telefon drucker glocke schluessel schloss ring hammer werkzeug weinglas bier tablette hund baum setzling schneeflocke streitstand merke fehler frage norm formel begriff tipp zahl countdown lesezeichen teilen folgen".split(" "));
const FORMATE = new Set(["pruefungsfrage", "schema", "streitstand", "minifall", "spickzettel", "vergleich", "klausurtechnik", "wochenrueckblick", "anlass", "reel"]);
const FOLIEN = new Set(["titel", "text", "schritte", "vergleich", "merke", "cta"]);
const HOOKS = new Set(["fehler", "zahl", "frage", "aussage"]);
const BRUCH = /(?:§|§§|Art\.|Abs\.|Satz|S\.|Nr\.|Alt\.|lit\.)$/;
const VERBOTEN = /link in (der )?bio|www\.|https?:\/\/|@herrjurist|instagram\.com/i;
const leer = (x) => !String(x ?? "").trim();
/* Fehler-Hooks ja, das Etikett „Fehler/falsch“ aber sparsam: Der Irrtum soll im
   Kopf des Lesers entstehen. Höchstens ein Cover je Tag trägt das Etikett. */
export const ETIKETT = /fehler|falsch|irrtum|sagt nein|\s=\s|^=|=\s*\S+\?/i;
export function coverTitel(c) {
  return [c?.folien?.[0]?.titel, ...(c?.folien?.[0]?.titelZeilen || []), c?.szenen?.[0]?.titel, ...(c?.titelZeilen || [])].filter(Boolean).join(" ");
}

export function tagPruefen(tag, datei = tag?.datum || "?") {
  const f = [];
  const fehler = (m) => f.push(`${datei}: ${m}`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(tag?.datum || "")) fehler("datum fehlt");
  const b = tag?.plan?.beitraege || [], s = tag?.plan?.stories || [];
  if (b.length !== 3) fehler("erwartet 3 Feed-Beiträge");
  if (s.length !== 9 || s.filter((x) => x.beitragSlot).length !== 3) fehler("erwartet 9 Stories, davon 3 Teaser");
  if (VERBOTEN.test(JSON.stringify(tag?.inhalte || {}))) fehler("Link/Website/Handle im Inhalt");

  for (const p of b) {
    const c = tag.inhalte?.[p.slot];
    const w = (m) => fehler(`${p.slot}: ${m}`);
    if (!c) { w("Inhalt fehlt"); continue; }
    if (c.format !== p.format) w(`Format ${c.format} ≠ Plan ${p.format}`);
    if (!FORMATE.has(c.format)) w(`unbekanntes Format ${c.format}`);
    if (c.manuellGeprueft !== true) w("manuellGeprueft fehlt");
    if (!HOOKS.has(c.hookTyp)) w(`hookTyp ${c.hookTyp} ungültig`);
    if (leer(c.caption) || c.caption.length < 120) w("caption fehlt/zu kurz");
    if (!Array.isArray(c.hashtags) || c.hashtags.length < 5 || c.hashtags.length > 12 || c.hashtags.some((h) => !/^#[\p{L}\d]+$/u.test(h))) w("hashtags ungültig (5–12, #wort)");
    if (leer(c.kurztitel) || c.kurztitel.length > 52) w("kurztitel fehlt/zu lang (≤52)");
    if (leer(c.coverText) || c.coverText.length > 40) w("coverText fehlt/zu lang (≤40)");
    if (leer(c.coverBadge)) w("coverBadge fehlt");
    const zeilen = c.folien ? c.folien[0]?.titelZeilen : c.titelZeilen;
    if (!Array.isArray(zeilen) || zeilen.length < 2 || zeilen.length > 4) w("titelZeilen: 2–4 Zeilen");
    for (const z of zeilen || []) {
      if (z.length > 22) w(`Titelzeile zu lang (${z.length}): ${z}`);
      if (BRUCH.test(z.trim())) w(`Titelzeile endet mit Normteil: ${z}`);
    }
    if (!c.coverRegie?.kernidee) w("coverRegie.kernidee fehlt");
    if (Array.isArray(c.folien)) {
      if (c.folien[0]?.art !== "titel") w("erste Folie muss titel sein");
      if (c.folien.length < 5 || c.folien.length > 9) w(`Folienzahl ${c.folien.length} (5–9)`);
      for (const [i, fo] of c.folien.entries()) {
        if (!FOLIEN.has(fo.art)) w(`Folie ${i + 1}: Art ${fo.art} unbekannt`);
        if (fo.art === "text" && leer(fo.text) && !(fo.punkte?.length)) w(`Folie ${i + 1}: text/punkte fehlen`);
        if (fo.art === "schritte" && !(fo.schritte?.length >= 2 && fo.schritte.every((x) => !leer(x.titel) && !leer(x.text)))) w(`Folie ${i + 1}: schritte unvollständig`);
        if (fo.art === "vergleich" && !(fo.links?.punkte?.length && fo.rechts?.punkte?.length && fo.links.titel && fo.rechts.titel)) w(`Folie ${i + 1}: vergleich unvollständig`);
        if (fo.art === "vergleich") {
          /* Schmale Spalten: der Renderer bricht überlange Wörter mitten im Wort um. */
          const lang = [fo.links?.titel, fo.rechts?.titel, ...(fo.links?.punkte || []), ...(fo.rechts?.punkte || [])]
            .join(" ").split(/[\s/]+/).filter((x) => x.replace(/[^\p{L}]/gu, "").length > 22 && !x.includes("-"));
          if (lang.length) w(`Folie ${i + 1}: überlange Wörter in Vergleichsspalte (${lang.join(", ")}) – trennen („Interessen-abwägung“) oder umformulieren`);
        }
        if (fo.art === "merke" && leer(fo.text)) w(`Folie ${i + 1}: merke ohne text`);
        if (fo.art === "cta") {
          if (!(fo.punkte?.length >= 2 && fo.punkte.length <= 4)) w("cta: 2–4 punkte");
          if (!Array.isArray(fo.icons) || fo.icons.length !== fo.punkte?.length || fo.icons.some((x) => !ICON_KEYS.has(x))) w("cta: icons ungültig");
        }
        if (fo.icon && !ICON_KEYS.has(fo.icon)) w(`Folie ${i + 1}: icon ${fo.icon} ungültig`);
      }
      if (c.folien.at(-1)?.art !== "cta") w("letzte Folie muss cta sein");
    } else if (Array.isArray(c.szenen)) {
      const sz = c.szenen;
      if (sz[0]?.art !== "hook" || sz.at(-1)?.art !== "cta") w("Reel: erste Szene hook, letzte cta");
      if (sz.length < 6 || sz.length > 9) w(`Reel: ${sz.length} Szenen (6–9)`);
      const woerter = sz.map((x) => String(x.sprecher || "").split(/\s+/).filter(Boolean).length).reduce((a, x) => a + x, 0);
      if (woerter < 140 || woerter > 240) w(`Reel: ${woerter} Sprecherwörter (140–240)`);
      const erster = String(sz[0]?.sprecher || "").split(/(?<=[.?!])\s/)[0].split(/\s+/).length;
      if (erster > 14) w(`Reel: erster Sprechersatz zu lang (${erster} Wörter, ≤14)`);
      for (const [i, x] of sz.entries()) {
        if (leer(x.titel) || leer(x.sprecher)) w(`Reel Szene ${i + 1}: titel/sprecher fehlt`);
        if (x.icon && !ICON_KEYS.has(x.icon)) w(`Reel Szene ${i + 1}: icon ${x.icon} ungültig`);
        if (!Array.isArray(x.marken) || !x.marken.length) w(`Reel Szene ${i + 1}: marken fehlen`);
      }
    } else w("weder folien noch szenen");
  }

  const etikettiert = b.filter((p) => ETIKETT.test(coverTitel(tag.inhalte?.[p.slot])));
  if (etikettiert.length > 1) fehler(`Fehler-Etikett („Fehler/falsch/=…?“) auf ${etikettiert.length} Covern (${etikettiert.map((p) => p.slot).join(", ")}) – höchstens 1 je Tag, Irrtum ohne Etikett formulieren`);

  for (const p of s.filter((x) => !x.beitragSlot)) {
    const x = tag.inhalte?.[p.slot];
    const w = (m) => fehler(`${p.slot} (${p.art}): ${m}`);
    if (!x) { w("Inhalt fehlt"); continue; }
    if (x.art !== p.art) w(`art ${x.art} ≠ Plan ${p.art}`);
    if (x.manuellGeprueft !== true) w("manuellGeprueft fehlt");
    if (leer(x.titel) || leer(x.ueberzeile) || leer(x.fachLabel)) w("titel/ueberzeile/fachLabel fehlt");
    if (x.titel?.length > 110) w("titel zu lang (≤110)");
    const t = String(x.text || "");
    if (t.length > 420) w(`text zu lang (${t.length}, ≤420)`);
    if (["antwort", "norm", "merksatz", "begriff", "tipp"].includes(p.art) && leer(t)) w("text fehlt");
    if (p.art === "norm" && leer(x.norm)) w("norm fehlt");
    if (p.art === "fehler" && (leer(x.falsch) || leer(x.richtigText))) w("falsch/richtigText fehlt");
    if (p.art === "streitstand" && (!Array.isArray(x.optionen) || x.optionen.length !== 2 || leer(t))) w("streitstand: 2 optionen + text");
    if (p.art === "zahl" && (!Array.isArray(x.punkte) || String(x.punkte.length) !== String(x.zahl))) w("zahl: punkte-Anzahl = zahl");
  }
  try { quizPruefen(tag, datei); } catch (e) { fehler(e.message); }
  return f;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  let alle = [];
  for (const p of process.argv.slice(2)) {
    try { alle = alle.concat(tagPruefen(JSON.parse(fs.readFileSync(p, "utf8")), p)); } catch (e) { alle.push(`${p}: ${e.message}`); }
  }
  for (const x of alle) console.log("✗ " + x);
  console.log(alle.length ? `${alle.length} Befund(e)` : `✓ ${process.argv.length - 2} Datei(en) regelkonform`);
  process.exit(alle.length ? 1 : 0);
}
