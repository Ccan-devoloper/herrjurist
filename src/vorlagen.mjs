/* ==========================================================================
   HTML-Vorlagen für Beitragsfolien (1080×1440, 3:4) und Stories (1080×1920).
   Eine Vorlage je Folienart; das Aussehen kommt aus stile.mjs.
   ========================================================================== */

import path from "node:path";
import { fileURLToPath } from "node:url";
import { iconSvg, ICONS, lernPalette } from "./stile.mjs";
import { farbIcon, ZUORDNUNG } from "./icons.mjs";
import { normKurz } from "./normen.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
export const FONT_DIR = path.resolve(hier, "../fonts");

export const MASSE = {
  beitrag: { breite: 1080, hoehe: 1350 },
  story: { breite: 1080, hoehe: 1920 },
};

export const KLAUSUR_FARBE = { 0: "k0", 1: "k1", 2: "k2", 3: "k3", 4: "k4" };

export function esc(s) {
  return String(s ?? "")
    .replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]))
    .replace(/i\.\s?V\.\s?m\./g, "i.\u00a0V.\u00a0m.")
    .replace(/(§§?|Abs\.|Nr\.|S\.|Art\.|R|H)\s(?=\d)/g, "$1\u00a0");
}

/* Überschriften: nur Hervorhebungen, keine Mono-Normen (die wirken in Großschrift fremd). */
/* Die Schreibweise der Normen ist Sache des Renderers, nicht der Quelle.
   Der Autor kuerzt zwar schon, aber gerendert wird auch gespeicherter Text,
   Handbuch-Material und Beispielinhalt - und dort stand schon "Paragraf 48
   VwVfG" auf einer Reel-Folie. normKurz ist idempotent, doppelt schadet also
   nicht. */
export function markierenTitel(s) {
  return esc(normKurz(s)).replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

/* Hervorhebungen: *wichtig* → <em>, Normen in Mono. */
export function markieren(s) {
  let t = esc(normKurz(s));
  t = t.replace(/\*([^*]+)\*/g, "<em>$1</em>");
  /* Die Gesetze der drei Rechtsgebiete. Auch Aufzaehlungen ("§§ 61, 62 VwGO")
     und Artikel ("Art. 20 Abs. 3 GG") gehoeren dazu - beides zitiert man im
     Examen staendig. Die Laenge ist begrenzt, damit die Regel nicht ueber
     halbe Saetze hinweg bis zum naechsten Kuerzel greift. */
  t = t.replace(/((?:§§?|Art\.)\s?[\dA-Za-z.,\s]{0,40}?(?:BGB|ZPO|StGB|StPO|GVG|VwGO|VwVfG|BauGB|BauNVO|GewO|POG|PolG|GG|HGB|GmbHG|AktG|InsO|ArbGG|BetrVG|KSchG|TzBfG|SGB|FamFG|WEG|ProdHaftG|StVG|StVO|OWiG|JGG|BeurkG|GBO|ErbbauRG|UWG|MarkenG|UrhG|PatG|AO|EStG|UStG|EGBGB|AEUV|EUV|GRCh|EMRK|BDSG|DSGVO))/g, '<code>$1</code>');
  return t;
}

function fontFace(name, datei, gewicht = "400 700") {
  return `@font-face{font-family:"${name}";src:url("file://${FONT_DIR}/${datei}") format("truetype");font-weight:${gewicht};font-display:block}`;
}

export function css(stil, art = "beitrag") {
  const f = stil.farben;
  const s = stil.schrift;
  const m = MASSE[art];
  return `
${fontFace("Anton", "Anton.ttf", "400")}
${fontFace("Oswald", "Oswald.ttf", "200 700")}
${fontFace("Inter", "Inter.ttf", "100 900")}
${fontFace("Space Grotesk", "SpaceGrotesk.ttf", "300 700")}
${fontFace("Caveat", "Caveat.ttf", "400 700")}
${fontFace("IBM Plex Sans", "IBMPlexSans.ttf", "100 700")}
${fontFace("IBM Plex Serif", "IBMPlexSerif-Bold.ttf", "700")}
${fontFace("IBM Plex Serif", "IBMPlexSerif-SemiBold.ttf", "600")}
${fontFace("IBM Plex Mono", "IBMPlexMono-Medium.ttf", "400 500")}
:root{
  --grund:${f.grund};--flaeche:${f.flaeche};--text:${f.text};--text-weich:${f.textWeich};--linie:${f.linie};
  --akzent:${f.akzent};--pille:${f.pille};--pille-text:${f.pilleText};
  --k1:${f.k1};--k2:${f.k2};--k3:${f.k3};--ok:${f.ok};--warn:${f.warn};--rot:${f.rot};
  --ecken:${stil.ecken};
  --titel:"${s.titel}";--sans:"${s.text}";--mono:"${s.mono}";
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:${m.breite}px;height:${m.hoehe}px;overflow:hidden;background:var(--grund);color:var(--text);font-family:var(--sans),system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.folie{position:relative;width:${m.breite}px;height:${m.hoehe}px;padding:72px 76px 64px;display:flex;flex-direction:column;background:var(--grund)}
.stil-campus .folie{background:radial-gradient(1200px 900px at 20% 0%,#243070 0%,#141a3a 55%,#0e1230 100%)}
.stil-klausurbogen .folie{background:
  repeating-linear-gradient(0deg,transparent 0 63px,rgba(18,35,63,.08) 63px 64px),
  var(--grund)}
.stil-klausurbogen .folie::before{content:"";position:absolute;left:150px;top:0;bottom:0;width:2px;background:rgba(200,16,46,.35)}
.kopf{display:flex;justify-content:space-between;align-items:center;font-size:26px;letter-spacing:.06em;text-transform:uppercase;color:var(--text-weich);font-weight:600}
.etikett{display:inline-flex;align-items:center;gap:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:24px}
.etikett .punkt{width:18px;height:18px;border-radius:50%;background:currentColor}
.etikett.k1{color:var(--k1)}.etikett.k2{color:var(--k2)}.etikett.k3{color:var(--k3)}
.familie-kanzlei .etikett{font-family:"Oswald";font-size:28px;letter-spacing:.02em;line-height:.95;text-transform:none;font-weight:500;flex-direction:column;align-items:flex-start;gap:0}
.familie-kanzlei .etikett .punkt{display:none}
.zaehler{font-family:var(--mono);font-size:24px;color:var(--text-weich)}
h1{font-family:var(--titel);font-weight:${s.titelGewicht};font-size:112px;line-height:${s.titelZeilenhoehe};letter-spacing:${s.titelSpacing};text-transform:${s.titelTransform};margin-top:54px;text-wrap:balance;overflow-wrap:normal}
h2,.merke,.zahl-unter,.karte .t,.spalte h3,ol.schritte b,.norm{overflow-wrap:normal}
.text,ul.punkte,.spalte ul,.story .text,.untertitel .zeile{overflow-wrap:anywhere}
h1.klein{font-size:88px}
h1.winzig{font-size:72px}
h2{font-family:var(--titel);font-weight:${s.titelGewicht};font-size:74px;line-height:1.08;letter-spacing:${s.titelSpacing};margin-top:44px;text-wrap:balance}
.familie-kanzlei h2{font-size:80px}
.unter{margin-top:26px;font-size:36px;line-height:1.35;color:var(--text-weich);max-width:880px}
.text{margin-top:40px;font-size:40px;line-height:1.42;max-width:930px}
.text p+p{margin-top:22px}
ul.punkte{margin-top:40px;list-style:none;display:flex;flex-direction:column;gap:24px;font-size:40px;line-height:1.36}
ul.punkte li{display:flex;gap:24px;align-items:flex-start}
ul.punkte li::before{content:"";flex:none;width:16px;height:16px;border-radius:50%;background:var(--akzent);margin-top:22px}
.stil-klausurbogen ul.punkte li::before{background:var(--rot)}
ol.schritte{margin-top:40px;list-style:none;display:flex;flex-direction:column;gap:26px;counter-reset:s}
ol.schritte li{display:grid;grid-template-columns:96px 1fr;gap:20px;align-items:start;counter-increment:s}
ol.schritte li::before{content:counter(s);font-family:var(--titel);font-size:64px;line-height:1;color:var(--akzent);font-weight:${s.titelGewicht}}
ol.schritte b{display:block;font-size:40px;line-height:1.2;font-weight:700}
ol.schritte span{display:block;font-size:32px;line-height:1.35;color:var(--text-weich);margin-top:6px}
ol.schritte.karte{gap:14px;margin-top:28px;padding:30px 34px;background:var(--flaeche);border:2px solid var(--linie);border-radius:var(--ecken)}
ol.schritte.karte li{grid-template-columns:70px 1fr;gap:14px}
ol.schritte.karte li::before{font-size:46px}
ol.schritte.karte b{font-size:34px}
ol.schritte.karte span{font-size:27px;margin-top:2px}
.vergleich{margin-top:44px;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}
.spalte{background:var(--flaeche);border:2px solid var(--linie);border-radius:var(--ecken);padding:34px}
.spalte h3{font-family:var(--titel);font-size:44px;line-height:1.1;margin-bottom:22px;font-weight:${s.titelGewicht}}
.spalte.links h3{color:var(--ok)}.spalte.rechts h3{color:var(--warn)}
.spalte ul{list-style:none;display:flex;flex-direction:column;gap:16px;font-size:31px;line-height:1.35}
.spalte ul li{padding-left:28px;position:relative}
.spalte ul li::before{content:"–";position:absolute;left:0;color:var(--text-weich)}
.rechnung{margin-top:44px;background:var(--flaeche);border:2px solid var(--linie);border-radius:var(--ecken);padding:40px 44px;font-family:var(--mono)}
.rechnung .formel{font-size:44px;line-height:1.3;color:var(--akzent);font-weight:500;text-wrap:balance}
.stil-klausurbogen .rechnung .formel{color:var(--rot)}
.rechnung .zeilen{margin-top:26px;display:flex;flex-direction:column;gap:14px;font-size:32px;line-height:1.35;color:var(--text)}
.rechnung .ergebnis{margin-top:26px;padding-top:22px;border-top:2px solid var(--linie);font-size:38px;font-weight:600}
.merke{margin-top:auto;margin-bottom:auto;font-family:var(--titel);font-size:78px;line-height:1.12;font-weight:${s.titelGewicht};text-wrap:balance}
.merke::before{content:"„";color:var(--akzent)}
.merke::after{content:"“";color:var(--akzent)}
.stil-klausurbogen .merke::before,.stil-klausurbogen .merke::after{color:var(--rot)}
em{font-style:normal;color:var(--akzent);font-weight:700}
.stil-klausurbogen em{color:var(--rot)}
code{font-family:var(--mono);font-size:.92em;white-space:nowrap}
.pille{display:inline-block;margin-top:40px;padding:14px 34px;border-radius:999px;background:var(--pille);color:var(--pille-text);font-weight:700;font-size:30px;letter-spacing:.02em}
.stil-klausurbogen .pille{border-radius:2px}
.fuss{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:28px;color:var(--text-weich)}
.fuss .handle{font-weight:600;color:var(--text)}
.fuss .klausur{font-family:var(--mono);font-size:24px;letter-spacing:.04em}
.illu{position:absolute;right:56px;bottom:90px;width:420px;height:420px;display:flex;align-items:center;justify-content:center;color:var(--akzent);opacity:.95}
.illu .icon{width:300px;height:300px}
.illu::before{content:"";position:absolute;inset:0;border-radius:50%;border:3px solid var(--linie)}
.stil-campus .illu::before{background:rgba(255,255,255,.04);border-color:rgba(214,255,74,.35)}
.stil-klausurbogen .illu{color:var(--akzent)}
.stil-klausurbogen .illu::before{border-color:rgba(18,35,63,.25)}
.geist{position:absolute;right:-30px;top:120px;font-family:var(--titel);font-size:900px;line-height:1;color:var(--text);opacity:.045;pointer-events:none;user-select:none}
.stil-campus .geist{color:var(--akzent);opacity:.06}
.cta{margin-top:auto;margin-bottom:auto;text-align:left}
.cta h2{font-size:92px;margin-top:0}
.cta .liste{margin-top:40px;display:flex;flex-direction:column;gap:22px;font-size:40px;line-height:1.35}
.cta .liste div{display:flex;gap:22px;align-items:center}
.cta .liste .icon{width:56px;height:56px;color:var(--akzent);flex:none}
.cta .web{margin-top:44px;display:inline-block;font-family:var(--mono);font-size:34px;padding:18px 30px;border:2px solid var(--linie);border-radius:var(--ecken)}
.prio{display:inline-flex;align-items:center;gap:12px;margin-top:36px;font-size:26px;color:var(--text-weich);letter-spacing:.04em;text-transform:uppercase;font-weight:600}
.prio i{width:22px;height:22px;border-radius:50%;background:var(--rot);display:inline-block}
.prio.mittel i{background:var(--warn)}.prio.selten i{background:var(--ok)}

/* Stories */
.story{position:relative;width:1080px;height:1920px;padding:150px 84px 130px;display:flex;flex-direction:column;background:var(--grund)}
.stil-campus .story{background:radial-gradient(1300px 1100px at 30% 10%,#243070 0%,#141a3a 55%,#0e1230 100%)}
.stil-klausurbogen .story{background:repeating-linear-gradient(0deg,transparent 0 63px,rgba(18,35,63,.08) 63px 64px),var(--grund)}
.story .kopf{font-size:30px}
.story .ueberzeile{display:flex;align-items:center;gap:20px}
.story .ueberzeile .uz-icon{display:inline-flex;width:64px;height:64px;border-radius:18px;background:rgba(255,255,255,.85);align-items:center;justify-content:center;flex:none}
.story .ueberzeile .uz-icon .icon{width:44px;height:44px}
.story .ueberzeile{margin-top:70px;font-size:34px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-weich);font-weight:700}
.story .etikett{font-size:30px}
.story h1{font-size:120px;margin-top:34px}
/* Normale Story-Titel duerfen nicht mit text-wrap:balance + fit-content
   intrinsisch zusammenschrumpfen. Das erzeugte bei kurzen Titeln wie
   "Nichtig oder schwebend unwirksam?" drei Zeilen, obwohl zwei passen.
   Cover haben ihre eigene explizite Zeilenlogik weiter unten. */
.story:not(.cover) h1{text-wrap:wrap;width:max-content;max-width:100%}
.story h1.klein{font-size:96px}
.story .text{font-size:48px;line-height:1.4;margin-top:44px}
.story .norm{margin-top:60px;font-family:var(--mono);font-size:64px;line-height:1.2;color:var(--akzent);text-wrap:balance}
.story .norm.norm-liste{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 16px;text-wrap:initial}
.story .norm .norm-einheit{display:inline-block;white-space:nowrap}
.story .norm .norm-einheit:not(:last-child)::after{content:" ·"}
.stil-klausurbogen .story .norm{color:var(--rot)}
.story .optionen{margin-top:60px;display:flex;flex-direction:column;gap:24px}
.story .optionen div{padding:30px 36px;border:3px solid var(--linie);border-radius:var(--ecken);font-size:42px;line-height:1.3;background:var(--flaeche);display:flex;gap:24px}
.story .optionen div b{font-family:var(--titel);color:var(--akzent);flex:none;width:52px}
.story .optionen div.richtig{border-color:var(--ok);box-shadow:inset 0 0 0 3px var(--ok)}
.story .zahl{margin-top:40px;font-family:var(--titel);font-size:420px;line-height:.95;color:var(--akzent);letter-spacing:-.02em}
.stil-klausurbogen .story .zahl{color:var(--rot)}
.story .zahl-unter{font-size:56px;line-height:1.2;margin-top:10px;font-family:var(--titel);text-wrap:balance}
.story .merke{font-size:96px}
/* Motiv in Story und Reel-Cover: unten rechts, laeuft aus der Kachel; der
   Text darueber bleibt frei, die Fusszeile liegt ueber dem Motiv. */
.story .frei{width:720px;height:820px;right:40px;bottom:44px}
.story .foto{left:84px;right:84px;bottom:150px;height:600px}
/* Story-Teaser zeigen das echte Feed-Cover als Ganzes. Kein Crop, keine
   erneute Typografie: Der Nutzer soll genau den Beitrag wiedererkennen, den
   er im Feed oeffnet. */
.story .teaser-cover{position:absolute;left:150px;right:150px;bottom:250px;height:880px;display:flex;align-items:center;justify-content:center;z-index:2}
.story .teaser-cover img{display:block;max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;border-radius:32px;box-shadow:0 30px 70px rgba(0,0,0,.24)}
.story:has(.teaser-cover) .fuss{z-index:3}
.story:has(.frei) .fuss,.story:has(.foto) .fuss{z-index:3}
.story .bildquelle{position:absolute;left:84px;bottom:96px;font-size:22px;color:var(--text-weich);opacity:.85;z-index:3}
/* Steht ein Motiv auf der Story, ruecken ALLE Inhaltsbloecke auf dieselbe
   Breite. Vorher galt das nur fuer Text und Hinweis - die Normzeile lief
   weiter ueber die volle Kachel, und die Kachel sah verrutscht aus.
   820 statt frueher 640: Das Motiv sitzt unten rechts (720 breit, 820 hoch)
   und beginnt erst bei y 1100 - die Bloecke darueber stossen gar nicht an es
   an. Mit 640 blieb rechts ein Drittel der Kachel leer, und ein langes
   deutsches Wort wie „Vollstreckungsklausel" passte selbst in der kleinsten
   Schrift nicht mehr hinein. Dass der Text nicht ins Motiv laeuft, regelt
   einpassen() ueber die Hoehe, nicht ueber die Breite. */
.story:has(.frei) .hinweis,.story:has(.frei) .text,.story:has(.frei) .norm,.story:has(.frei) .karte,.story:has(.frei) .optionen,.story:has(.frei) h1,.story:has(.frei) .zahl-unter{max-width:820px}
.story.cover:has(.frei) .buehne{display:none}
.story .pille{font-size:36px;padding:20px 40px;margin-top:56px}
.story .fuss{font-size:32px}
.story .hinweis{margin-top:60px;font-size:34px;color:var(--text-weich);line-height:1.4}
.story .karte{margin-top:56px;background:var(--flaeche);border:3px solid var(--linie);border-radius:var(--ecken);padding:44px 48px}
.story .karte .t{font-family:var(--titel);font-size:60px;line-height:1.1}
.story .karte .u{margin-top:22px;font-size:38px;line-height:1.4;color:var(--text-weich)}
.story .illu{right:70px;bottom:220px;width:380px;height:380px}
.story .illu .icon{width:260px;height:260px}
.story .geist{font-size:1200px;top:520px}
.story .balken{margin-top:110px;margin-bottom:auto;height:16px;border-radius:999px;background:var(--linie);overflow:hidden}
.story .balken i{display:block;height:100%;background:var(--akzent)}
/* Streitstand: zwei Ansichten untereinander, darunter der Entscheid - er
   traegt die Akzentfarbe, weil er in der Klausur die Punkte bringt. */
.story .norm.klein{margin-top:30px;font-size:44px}
.story .ansichten{margin-top:40px;display:flex;flex-direction:column;gap:20px}
.story .ansichten div{background:var(--flaeche);border:3px solid var(--linie);border-radius:var(--ecken);padding:28px 34px}
.story .ansichten div b{display:block;font-family:var(--titel);font-size:34px;color:var(--akzent);margin-bottom:8px}
.story .ansichten div span{display:block;font-size:38px;line-height:1.35}
.story .karte.entscheid{margin-top:28px;border-color:var(--ok)}
.story .karte.entscheid .t{font-size:34px;letter-spacing:.06em;text-transform:uppercase;color:var(--ok)}
.story .pfeil{margin-top:auto;text-align:center;font-size:34px;color:var(--text-weich);letter-spacing:.12em;text-transform:uppercase}
.story .umfrageplatz{margin-top:auto;height:300px;flex:none}
/* Reel-Cover bleibt eine echte 9:16-Komposition. Die 4:5-Feed-Safe-Area
   schützt nur kritischen Text; Fachband, Reelmarke und Motiv duerfen die
   echten Aussenkanten des Covers nutzen. Das entspricht der funktionierenden
   Urkunde-ohne-Papier-Referenz. */
.story.cover{padding-top:150px;padding-bottom:130px}
.story.cover .reelmarke{position:absolute;right:84px;top:40px;font-family:var(--text);font-weight:700;font-size:28px;letter-spacing:.16em;text-transform:uppercase;background:var(--pille);color:var(--pille-text);padding:12px 26px;border-radius:40px}
.story.cover .dauer{margin-top:30px;font-size:36px;color:var(--text-weich)}
.story.cover .buehne{margin:auto auto 0;width:460px;height:460px;display:flex;align-items:center;justify-content:center;position:relative}
.story.cover .buehne::before{content:"";position:absolute;inset:0;border-radius:50%;background:var(--flaeche);opacity:.6}
.story.cover .buehne .icon{position:relative;width:250px;height:250px;color:var(--akzent)}
`;
}

/* Feste Farbe je Klausurtag: Akzentfarbe, Balken oben, Pille und Fußzeile
   tragen die Farbe des Prüfungstags (k1 Blau, k2 Orange, k3 Grün). */
export function klausurCss(ctx) {
  if (!ctx?.farbeJeKlausur || (ctx.stil?.familie || ctx.stil?.id) === "bunt") return "";
  const k = KLAUSUR_FARBE[ctx.klausur] || "k3";
  return `
.folie,.story,.reel{--akzent:var(--${k});--pille:var(--${k});--pille-text:#0b0b0d}
.folie::before,.story::before,.reel::before{content:"";position:absolute;left:0;top:0;right:0;height:16px;background:var(--${k});z-index:2}
.fuss .klausur{color:var(--${k});font-weight:700}
.familie-kanzlei .untertitel .w.jetzt{color:var(--${k})}`;
}

/* Stil „bunt“: Vollfläche in der Tagesfarbe; alle Bausteine werden zu Pillen,
   Karten und Badges – ohne die Vorlagen selbst zu ändern. */
const PFEIL = encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 110" fill="none" stroke="#111" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 14 C 30 70, 70 92, 128 86"/><path d="M108 66 L 130 86 L 106 100"/></svg>`);
export function buntCss(ctx) {
  const stil = ctx?.stil;
  if (!stil || (stil.familie || stil.id) !== "bunt") return "";
  const p = lernPalette(ctx.fach, stil.tagFarben?.[ctx.klausur] || stil.tagFarben?.[3]);
  const pfeil = `url("data:image/svg+xml,${PFEIL.replace("%23111", encodeURIComponent(p.dunkel))}")`;
  return `
:root{--grund:${p.grund};--text:${p.dunkel};--text-weich:${p.weich || p.dunkel};--akzent:${p.dunkel};--pille:${p.dunkel};--pille-text:#fff;--flaeche:rgba(255,255,255,.92);--linie:rgba(255,255,255,.45);--hell:${p.hell};--lila:${p.lila};--akzent2:${p.akzent2}}
.folie,.story,.reel{background:${p.grund};color:${p.dunkel}}
/* Cover v2 nutzt die Breite wie die Golden References aggressiver als die Inhaltsfolien. */
.art-titel{padding-left:52px;padding-right:52px}
/* Auf weißen Flächen bleibt Nebentext dunkel - die helle Weichfarbe gilt
   nur direkt auf der Grundfarbe. */
.text,ul.punkte li,ol.schritte li,.spalte,.rechnung,.cta .liste div,.story .karte,.story .optionen div,.story .norm,.merke,.reel .merkeblock .norm{--text-weich:${p.dunkel}}
/* Ecke oben links: dunkles Band mit dem Fach; oben rechts der Zähler im weißen Kreis */
.kopf{position:absolute;left:0;top:0;right:0;height:120px;padding:0}
/* Fachband auf Titelfolien buendig an die obere linke Bildkante ziehen. */
.art-titel>.kopf{left:-52px;top:0;right:-52px}
.kopf .etikett{position:absolute;left:0;top:0;font-family:"Inter";font-weight:700;font-size:28px;letter-spacing:.02em;text-transform:none;background:${p.dunkel};color:#fff;padding:16px 46px 16px 40px;clip-path:polygon(0 0,100% 0,calc(100% - 26px) 100%,0 100%);flex-direction:row;line-height:1.1;white-space:nowrap;box-sizing:border-box}
.art-titel>.kopf .etikett{padding-left:92px;padding-right:52px}
.kopf .etikett .punkt{display:none}
.kopf .zaehler{position:absolute;right:38px;top:30px;width:68px;height:68px;border-radius:50%;background:${p.dunkel};color:#fff;font-family:"Inter";font-weight:700;font-size:25px;display:flex;align-items:center;justify-content:center}
.kopf .zaehler:empty{display:none}
/* Titel als Pillen, Zeile für Zeile. Die erste Folie wird im Feed als
   Vorschaubild von 300 px Breite gesehen – dort entscheidet die Schriftgröße,
   ob jemand den Beitrag überhaupt liest. Deshalb so groß wie möglich; zu
   lange Titel fängt einpassen() ab. */
h1{margin-top:68px;font-size:96px;line-height:1.16}
h1.klein{font-size:82px}h1.winzig{font-size:70px}
h1 .z{background:${p.dunkel};color:#fff;padding:.12em .42em;border-radius:34px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
/* Titelfolie: echte Einzelpillen pro Sinneinheit. Weniger Innenabstand und
   nur 8 px Abstand zwischen den Zeilen erzeugen einen kompakten, auf dem
   Handy schnell scanbaren Titelblock. */
.art-titel h1.titel-stack{display:flex;flex-direction:column;align-items:flex-start;gap:5px;width:fit-content;max-width:100%;margin-top:10px;font-size:104px;line-height:.99;letter-spacing:-.025em;text-wrap:initial}
.art-titel h1.titel-stack.klein{font-size:94px}
.art-titel h1.titel-stack.winzig{font-size:84px}
.art-titel h1.titel-stack .titel-zeile{display:block;width:fit-content;max-width:976px;background:${p.dunkel};color:#fff;padding:12px 27px 14px;border-radius:30px;white-space:nowrap}
.art-titel h1.titel-stack .titel-zeile em{color:${p.akzent2}}
h1 em{color:${p.akzent2}}
.cover-badge{margin-top:15px;margin-left:10px;width:fit-content;background:#fff0d6;color:${p.dunkel};padding:10px 26px 11px;border-radius:999px;font-family:"Inter";font-weight:700;font-size:30px;line-height:1.05;position:relative;z-index:4}
.unter{margin-top:22px;display:inline-block;width:fit-content;background:${p.hell};color:${p.dunkel};padding:12px 30px;border-radius:40px;font-weight:700;font-size:36px;line-height:1.25;margin-left:24px}
.prio{margin-top:20px;margin-left:24px;width:fit-content;background:${p.lila};color:${p.dunkel};padding:10px 26px;border-radius:40px;text-transform:none;letter-spacing:0;font-size:28px}
.prio i{display:none}
/* Handschrift-Hinweis mit Pfeil statt Pille */
.art-titel .pille{background:none;color:${p.dunkel};font-family:"Caveat";font-size:58px;font-weight:700;padding:0 0 0 170px;margin-top:40px;margin-left:420px;position:relative;transform:rotate(-4deg);letter-spacing:0}
.art-titel .pille::before{content:"";position:absolute;left:0;top:-30px;width:150px;height:110px;background:${pfeil} no-repeat center/contain}
/* Bühne: Blase, großes Icon, §-Badge, Karte, Sterne */
.art-titel::after{content:"";position:absolute;left:210px;bottom:-140px;width:660px;height:660px;border-radius:50%;background:rgba(255,255,255,.16);pointer-events:none}
/* Fotokarte: unteres Drittel, gleiche Rundung wie die uebrigen Karten. Ist ein
   Foto da, entfaellt die Icon-Buehne samt Kreis und Sternen. */
/* Inhaltsfolien: der Inhalt steht mittig, die Fusszeile klebt unten.
   Vorher holten sich Inhalt und Fusszeile den freien Platz beide ueber
   margin-top:auto. Bei Folien, die selbst schon auto-Raender mitbringen
   (Merksatz, CTA), waren das drei Ansprueche auf denselben Platz - der
   Inhalt landete im oberen Drittel und die untere Haelfte blieb leer.
   Die Titelfolie bleibt oben, dort fuellt das Motiv die untere Haelfte. */
.folie:not(.art-titel){justify-content:center}
.folie:not(.art-titel) > .fuss{position:absolute;left:76px;right:76px;bottom:64px;margin-top:0}
/* Merksatz und CTA zentrieren sich sonst selbst und loesen sich damit von
   ihrer Ueberschrift - das Zentrieren macht jetzt die Folie fuer alle. */
.folie:not(.art-titel) > .merke{margin-top:36px;margin-bottom:0}
.merke-icon{width:96px;height:96px;border-radius:26px;background:rgba(255,255,255,.85);margin-bottom:24px;display:flex;align-items:center;justify-content:center}
.folie:not(.art-titel) > .merke-icon + h2{margin-top:0}
.folie:not(.art-titel) > .cta{margin-top:0;margin-bottom:0}
.art-titel:has(.foto)::after,.art-titel:has(.frei)::after,.art-titel.cover-ohne-bild::after{display:none}
/* Freigestelltes Motiv: unten rechts, laeuft ueber den Rand hinaus. Der
   Schatten setzt es von der Flaeche ab, ohne einen Rahmen zu zeichnen. */
/* Die Buehne endet unterhalb des Kopfblocks: Seit die Motive zugeschnitten
   werden, fuellen sie den Kasten wirklich aus und wuerden sonst in den Pfeil
   und das "So geht's!" hineinlaufen.
   Buendig am rechten Rand statt darueber hinaus: Solange die Motive als
   Briefmarke in der Ecke sassen, schnitt der Ueberstand nur Luft ab - jetzt
   wuerde er das Motiv selbst anschneiden. */
.frei{position:absolute;right:28px;bottom:28px;width:760px;height:700px;z-index:1;pointer-events:none}
/* Links neben dem Motiv, unterhalb der Pfeilzeile: Der Kasten des Motivs
   beginnt bei x = 440 px, die Pfeilzeile endet auch bei vier Titelzeilen
   oberhalb von y = 860 px - dazwischen ist die Flaeche frei. */
.frei-zeichen{position:absolute;left:90px;bottom:210px;width:250px;height:250px;transform:rotate(-9deg);z-index:2;filter:drop-shadow(0 16px 26px rgba(0,0,0,.18))}
.frei-zeichen .icon{width:100%;height:100%}
/* In der Story sitzt das Zeichen unten links neben dem Motiv, unterhalb von
   Pille und Hinweistext - auf Hoehe der Pille verdeckte es die Schrift. */
.story .frei-zeichen{left:84px;bottom:330px;width:240px;height:240px}
/* Der Pexels-Hinweis steht ueber der Zone, die Instagram mit Antwortfeld und
   Reaktionen ueberlagert (unterste ~250 px). */
/* Bildnachweis: Ton in Ton mit der Flaeche - er soll die Kachel nicht
   stoeren, aber lesbar bleiben. Pexels verlangt fuer die API-Nutzung einen
   sichtbaren Hinweis; ganz in der Grundfarbe waere er unsichtbar und der
   Nachweis damit keiner mehr. */
.story .bildquelle{bottom:290px;max-width:320px;line-height:1.3;color:${p.dunkel};opacity:.38;font-size:20px}
/* Der Sticker-Rand steckt schon in der PNG (freistellen.mjs, bestickern):
   zwoelf verkettete drop-shadows brachten Chromium zum Stehen. Hier nur
   noch der weiche Schatten, der den Sticker von der Flaeche hebt. */
.frei img{width:100%;height:100%;object-fit:contain;object-position:right bottom;display:block;filter:drop-shadow(0 26px 40px rgba(0,0,0,.28))}
.frei.charakter{right:-12px;bottom:-6px;width:1050px;height:980px}
.frei.charakter img{object-position:center bottom;filter:drop-shadow(0 18px 28px rgba(0,0,0,.20))}
/* Problematische Action-Freisteller werden mit leichtem Bleed von links nach
   rechts aufgespannt. Die exakte Breite kommt inline aus dem Renderprofil;
   overflow bleibt bewusst sichtbar, damit keine "Sticker"-Innenkante entsteht. */
.frei.charakter.edge-to-edge{max-width:none;overflow:hidden}
.frei.charakter.edge-to-edge img{object-fit:var(--edge-fit,cover);object-position:var(--edge-x,50%) var(--edge-y,50%)}
/* Reel-Freisteller brauchen keinen Crop, sondern eine echte vollbreite Bühne:
   Das zugeschnittene Motiv wird auf Canvasbreite skaliert und unten verankert.
   So berührt die Komposition links/rechts die Coverkante, ohne Figuren durch
   object-fit:cover abzuschneiden. */
.frei.charakter.edge-to-edge.fit-width{overflow:visible}
.frei.charakter.edge-to-edge.fit-width img{position:absolute;left:0;bottom:0;width:100%;height:auto;object-fit:contain;object-position:center bottom}
.art-titel h1,.art-titel .prio{position:relative;z-index:3}
.art-titel .kopf{z-index:3}
/* Fusszeile traegt das Rechtsgebiet - sie bleibt ueber dem Motiv lesbar. */
/* Steht ein Motiv auf der Kachel, rueckt der Pfeil samt "So geht's!" nach
   links: der Kasten des Motivs reicht rechts bis in diese Hoehe hinauf. */
.art-titel:has(.frei) .fuss{position:absolute;left:52px;right:28px;bottom:24px;margin-top:0;z-index:3}
.art-titel.cover-ohne-bild .fuss{position:absolute;left:52px;right:28px;bottom:24px;margin-top:0;z-index:3}
.art-titel:has(.frei) .fuss .klausur{background:var(--hell);color:${p.dunkel};padding:7px 20px;border-radius:30px}
.art-titel.cover-ohne-bild .fuss .klausur{background:var(--hell);color:${p.dunkel};padding:7px 20px;border-radius:30px}
.foto{position:absolute;left:60px;right:60px;bottom:118px;height:520px;border-radius:44px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.22);z-index:1;background:rgba(255,255,255,.14);padding:18px;box-sizing:border-box}
.foto img{width:100%;height:100%;object-fit:contain;object-position:center;display:block;border-radius:28px}
.illu{right:auto;left:330px;bottom:70px;width:420px;height:420px;color:${p.dunkel};opacity:1;z-index:1}
.illu::before{display:none}
.illu .icon{width:380px;height:380px}
.geist{left:140px;right:auto;top:auto;bottom:210px;width:150px;height:150px;border-radius:50%;background:${p.dunkel};color:#fff;font-family:"Space Grotesk";font-size:96px;font-weight:700;display:flex;align-items:center;justify-content:center;opacity:1;box-shadow:0 18px 40px rgba(0,0,0,.2);z-index:1}
.folie:not(.art-titel) .geist{display:none}
.karte2{position:absolute;right:120px;bottom:260px;width:190px;height:190px;background:#fff;border-radius:26px;display:flex;align-items:center;justify-content:center;color:${p.dunkel};box-shadow:0 18px 40px rgba(0,0,0,.18);transform:rotate(9deg);z-index:1}
.stern{position:absolute;color:${p.hell};font-size:54px;z-index:1}
/* Innenfolien: Überschrift als Pille, Inhalte als weiße Karten */
h2{margin-top:120px;font-size:56px;width:fit-content;background:${p.dunkel};color:#fff;padding:14px 34px;border-radius:44px;line-height:1.15}
.cta h2{font-size:66px;margin-top:0;line-height:1.7;background:none;padding:0;color:${p.dunkel}}
.text{margin-top:34px;background:var(--flaeche);border-radius:30px;padding:30px 36px;font-size:36px;line-height:1.4;color:#1c1c22}
ul.punkte{margin-top:34px;gap:18px}
ul.punkte li{background:var(--flaeche);border-radius:30px;padding:24px 30px;font-size:35px;line-height:1.35;color:#1c1c22;align-items:center}
ul.punkte li::before{width:22px;height:22px;background:${p.dunkel};margin-top:0}
ol.schritte{margin-top:34px;gap:20px}
ol.schritte li{background:var(--flaeche);border-radius:30px;padding:24px 30px;grid-template-columns:76px 1fr;gap:22px;align-items:center}
ol.schritte li::before{width:76px;height:76px;border-radius:50%;background:${p.dunkel};color:#fff;font-size:38px;display:flex;align-items:center;justify-content:center;font-family:"Space Grotesk"}
ol.schritte b{font-size:36px;color:${p.dunkel}}
ol.schritte span{font-size:29px;color:#2b2b33}
ol.schritte.karte{background:var(--flaeche);border:0;padding:24px 28px;gap:12px}
ol.schritte.karte li{background:none;padding:6px 0;grid-template-columns:60px 1fr}
ol.schritte.karte li::before{width:56px;height:56px;font-size:30px}
.vergleich{margin-top:34px}
.spalte{background:var(--flaeche);border:0;border-radius:30px;color:#1c1c22}
.spalte.links h3{color:${p.dunkel}}.spalte.rechts h3{color:#b3261e}
.rechnung{margin-top:34px;background:var(--flaeche);border:0;border-radius:30px;color:#1c1c22}
.rechnung .formel{color:${p.dunkel}}
.rechnung .ergebnis{border-top-color:rgba(0,0,0,.15)}
.merke{font-size:66px;line-height:1.7}
.merke::before,.merke::after{color:${p.zitat || p.akzent2}}
em{color:${p.akzent2}}
.text em,ul.punkte em,ol.schritte em,.spalte em{color:${p.dunkel};text-decoration:underline;text-decoration-color:${p.akzent2};text-decoration-thickness:4px;text-underline-offset:6px}
.cta{margin-top:auto;margin-bottom:auto}
.cta .liste{margin-top:30px;gap:20px}
.cta .liste div{background:var(--flaeche);border-radius:30px;padding:24px 30px;font-weight:700;font-size:36px;color:${p.dunkel}}
.cta .liste .icon{width:72px;height:72px;padding:14px;border-radius:22px;background:${p.lila};color:${p.dunkel}}
.fuss{color:${p.dunkel};font-family:"Inter";font-weight:700;font-size:26px}
.fuss .klausur{font-family:"Inter";letter-spacing:0;font-size:26px;color:${p.dunkel}}
.pille{background:${p.dunkel};color:#fff}
/* Stories */
.story .kopf{height:120px}
.story h1{font-size:84px;line-height:1.2;margin-top:120px;width:fit-content;background:${p.dunkel};color:#fff;padding:.25em .5em;border-radius:48px}
.story h1.klein{font-size:74px}
.story .ueberzeile{margin-top:150px;background:${p.lila};color:${p.dunkel};width:fit-content;padding:10px 26px;border-radius:40px;text-transform:none;letter-spacing:0;font-size:32px}
.story .ueberzeile+h1{margin-top:26px}
.story .text{font-size:42px}
.story .norm{background:var(--flaeche);border-radius:30px;padding:30px 36px;color:${p.dunkel};font-size:54px}
.story .optionen div{border:0;border-radius:30px;color:#1c1c22;font-size:40px}
.story .ansichten div{border:0;border-radius:30px;color:#1c1c22}
.story .ansichten div b{color:${p.dunkel}}
.story .karte.entscheid{border:0;box-shadow:inset 0 0 0 5px ${p.dunkel}}
.story .karte.entscheid .t{color:${p.dunkel}}
.story .optionen div b{color:${p.dunkel}}
.story .optionen div.richtig{box-shadow:inset 0 0 0 5px ${p.dunkel}}
.story .zahl{color:#fff;text-shadow:0 12px 40px rgba(0,0,0,.18)}
.story .zahl-unter{color:${p.dunkel}}
.story .zahl-punkte{margin-top:34px;display:flex;flex-direction:column;gap:16px}
.story .zahl-punkte .zp{display:grid;grid-template-columns:54px 1fr;gap:18px;align-items:start;background:var(--flaeche);border-radius:26px;padding:20px 26px;color:${p.dunkel};font-size:34px;line-height:1.28}
.story .zahl-punkte .zp b{font-family:var(--titel);font-size:36px;line-height:1.15}

.story .merke{font-size:78px}
.story .karte{background:var(--flaeche);border:0;border-radius:30px;color:#1c1c22}
.story .karte .t{color:${p.dunkel}}
.story .balken{background:rgba(255,255,255,.4)}
.story .balken i{background:${p.dunkel}}
.story .pfeil{color:${p.dunkel};font-family:"Caveat";font-size:48px;text-transform:none;letter-spacing:0}
.story .hinweis{color:${p.dunkel};opacity:.85}
.story .illu{color:${p.dunkel};opacity:1;left:auto;right:70px;bottom:220px}
.story .geist{display:none}
.story .pille{margin-top:56px}
/* Das Reel-Cover traegt dieselbe Ueberschrift wie die Titelfolie eines
   Karussells: eine Pille je Zeile, nicht ein Kasten um den ganzen Titel. Bis
   zum 13.09. war das Cover der einzige Ort mit dem Kasten - im Profilraster
   standen beide Formate nebeneinander und sahen aus wie zwei Kanaele.
   Die Story-Regel (ein Grund um das ganze h1) wird dafuer zurueckgenommen. */
/* Im sichtbaren 4:5-Ausschnitt hat das Reel-Cover dieselbe Pixelgeometrie
   wie eine Karussell-Titelfolie (1080×1350). Deshalb werden Titel und Pillen
   hier NICHT auf 1920px hochskaliert; genau diese frühere 4/3-Skalierung
   schob die erste Zeile aus der Feed-Safe-Area. */
.story.cover .kopf{top:0}
.story.cover h1{background:none;padding:0;width:auto;font-size:112px;line-height:1.2;margin-top:70px}
.story.cover h1.klein{font-size:96px}
.story.cover h1.winzig{font-size:84px}
.story.cover h1 .z{background:${p.dunkel};color:#fff;padding:.12em .42em;border-radius:34px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.story.cover h1.titel-stack{display:flex;flex-direction:column;align-items:flex-start;gap:5px;width:fit-content;max-width:100%;font-size:104px;line-height:.99;letter-spacing:-.025em}
.story.cover h1.titel-stack.klein{font-size:94px}
.story.cover h1.titel-stack.winzig{font-size:84px}
.story.cover h1.titel-stack .titel-zeile{display:block;width:fit-content;max-width:912px;box-sizing:border-box;background:${p.dunkel};color:#fff;padding:12px 27px 14px;border-radius:30px;white-space:nowrap}
.story.cover .unter{margin-top:22px;margin-left:24px;font-size:34px}
/* Das Motiv darf bis an die echte Unterkante des 9:16-Covers laufen.
   Geschuetzt wird nur der Textblock; die Illustration ist selbst Teil der
   Komposition und soll nicht 285 px ueber dem unteren Rand schweben. */
.story.cover .frei.charakter{bottom:0;right:36px}
.story.cover h1,.story.cover .unter{position:relative;z-index:3}
.story.cover .kopf{z-index:3}
.story.cover .cover-badge{margin-top:12px}
/* Cover-v2 no-arrow: keine automatisch erzeugte Dauer-Handschrift. */
.story.cover .dauer{display:none}
.story.cover .dauer::before{display:none}
.story.cover .buehne::before{background:rgba(255,255,255,.75);opacity:1}
.story.cover .buehne .icon{color:${p.dunkel}}
/* Auf Charakter-Reel-Covern ist das Rechtsgebiet bereits oben links genannt.
   Die zweite Fusszeile lag bisher mit z-index 3 direkt auf Figuren/Portal. */
.story.cover:has(.frei.charakter) .fuss{display:none}
/* Reels */
.reel .fortschritt{background:rgba(255,255,255,.4)}
.reel .fortschritt i{background:${p.dunkel}}
.reel .trenner{background:rgba(255,255,255,.5)}
.reel .kopf{position:absolute;left:84px;right:84px;height:auto}
.reel .kopf .etikett{position:static;clip-path:none;border-radius:40px;padding:10px 26px}
.reel .kopf .zaehler{position:static;width:auto;height:auto;background:none;color:${p.dunkel};font-size:28px}
.reel .hook h1{font-size:68px;line-height:1.15;margin-top:0;width:fit-content;background:${p.dunkel};color:#fff;padding:.22em .5em;border-radius:48px}
/* Die Unterzeile des Aufhaengers sitzt auf der hellen Pille und muss die
   dunkle Farbe tragen. Ohne diese Zeile erbte sie „--text-weich", das im
   bunten Stil ein sehr helles Blau ist - hell auf hell, und die Zeile war
   im Video praktisch unsichtbar (Campus-Reel vom 13.09.). */
.reel .hook .unter{margin-left:0;color:${p.dunkel}}
.reel .schritt .nummer{color:#fff}
.reel .schritt h2{margin-top:0;font-size:60px}
.reel .schritt .text,.reel .ctablock .text{color:${p.dunkel};background:none;padding:0;margin-top:14px}
.reel .merkeblock .ueber{color:${p.dunkel}}
.reel .merke-titel{background:none;padding:0;color:${p.dunkel};font-size:64px;margin-top:16px;width:auto}
.reel .merkeblock .norm{background:var(--flaeche);border-radius:26px;padding:16px 26px;color:${p.dunkel};width:fit-content}
.reel .ctablock h2{background:none;padding:0;color:${p.dunkel};margin-top:0}
.reel .untertitel .block{color:#fff;text-shadow:0 8px 30px rgba(0,0,0,.25)}
.reel .untertitel .w{color:#fff}
.reel .untertitel .w.jetzt,.familie-bunt .untertitel .w.jetzt{color:${p.dunkel}}
.reel .fuss{position:absolute;left:84px;right:84px;bottom:70px;margin:0}
`;
}

function kopf(ctx, zaehler) {
  const kl = KLAUSUR_FARBE[ctx.klausur] || "k3";
  const etikett = (ctx.stil.familie || ctx.stil.id) === "kanzlei"
    ? `<span class="etikett ${kl}">${esc(ctx.fachLabel.split(" / ")[0])}</span>`
    : `<span class="etikett ${kl}"><i class="punkt"></i>${esc(ctx.fachLabel)}</span>`;
  return `<div class="kopf">${etikett}<span class="zaehler">${zaehler ? esc(zaehler) : ""}</span></div>`;
}

/* Fußzeile: nur das Handle, und nur wenn eines konfiguriert ist. Keine Website,
   kein Markenname – das kommt später. */
function fuss(ctx) {
  /* Methodik gehoert zu keinem Rechtsgebiet - dann steht dort das Fach. */
  const rechts = fussRechts(ctx);
  return `<div class="fuss"><span class="handle">${esc(ctx.handle || "")}</span><span class="klausur">${esc(rechts)}</span></div>`;
}
/* Die Marke sortiert nach Rechtsgebiet - das steht in der Fusszeile, so wie
   beim Steuerkanal der Klausurtag. */
export const KLAUSUR_KURZ = { 1: "Zivilrecht", 2: "Strafrecht", 3: "Öffentliches Recht", 4: "Wochenrückblick" };

/* Dasselbe Etikett, das die Fusszeile der Kachel traegt - das Reel nutzt es mit. */
export function fussRechts(ctx) {
  if (ctx?.fach === "mindset") return "Kopfsache";
  if (ctx?.fach === "methodik") return "Klausurtechnik";
  return KLAUSUR_KURZ[ctx?.klausur] || "";
}

/* Foto statt Icon-Buehne: Das Bild liegt als abgerundete Karte im unteren
   Drittel, die Farbe der Kachel bleibt sichtbar. Ganzflaechig waere es ein
   anderer Kanal - so bleibt die Marke erkennbar und das Bild traegt trotzdem. */
/**
 * Bühne für ein freigestelltes Motiv. Feste Box plus „contain" ließ breite
 * Motive (zwei Hände über einem Blatt) zur Briefmarke schrumpfen, während
 * hochkante die Kachel füllten. Gerechnet wird deshalb auf gleiche FLÄCHE:
 * Jedes Motiv bekommt dieselbe optische Wucht, die Form bestimmt nur, ob es
 * breit und flach oder schmal und hoch dasteht.
 * @param {number} breite natürliche Maße des Freistellers
 * @param {{flaeche:number,maxB:number,maxH:number}} ziel
 */
export function motivBuehne(breite, hoehe, ziel) {
  if (!breite || !hoehe) return null;
  const v = breite / hoehe;
  let h = Math.sqrt(ziel.flaeche / v), b = v * h;
  /* Nicht breiter und nicht höher als die Kachel verträgt; die Form bleibt. */
  if (b > ziel.maxB) { b = ziel.maxB; h = b / v; }
  if (h > ziel.maxH) { h = ziel.maxH; b = v * h; }
  return { breite: Math.round(b), hoehe: Math.round(h) };
}

/* Normale Freisteller bleiben kompakt. Charakter-Szenen bekommen dagegen
   fast die ganze untere Haelfte: Sie sollen eine kleine Handlung tragen,
   nicht wie ein Sticker in der Ecke stehen. */
export const BUEHNE_BEITRAG = { flaeche: 640 * 620 * 0.62, maxB: 820, maxH: 640 };
export const BUEHNE_CHARAKTER = { flaeche: 1080 * 960 * 0.98, maxB: 1100, maxH: 1000 };
export const BUEHNE_STORY = { flaeche: 720 * 820 * 0.62, maxB: 920, maxH: 850 };

function fotoBuehne(folie, ziel = BUEHNE_BEITRAG) {
  /* Freigestellt: Das Motiv laeuft unten rechts aus der Kachel, ohne Rahmen.
     Nicht freigestellt (Notfall): als abgerundete Karte. */
  const istCharakter = folie.bildTyp === "charakter";
  const edgeToEdge = istCharakter && folie.coverBildEdgeToEdge === true;
  /* Number(null) === 0 war hier ein versteckter Layoutfehler: fehlende
     Profilwerte wurden dadurch als scale=.65 und x=.05 interpretiert. Genau
     deshalb klebten neue Reel-Motive klein und links angeschnitten am Rand.
     Nur wirklich gesetzte Werte dürfen als Profil gelten. */
  const zahlOderNull = (wert) => {
    if (wert === null || wert === undefined || wert === "") return null;
    const n = Number(wert);
    return Number.isFinite(n) ? n : null;
  };
  const scaleRaw = zahlOderNull(folie.coverBildScale);
  const breiteRaw = zahlOderNull(folie.coverBildBreite);
  const xRaw = zahlOderNull(folie.coverBildX);
  const yRaw = zahlOderNull(folie.coverBildY);
  const topRaw = zahlOderNull(folie.coverBildTop);
  const bottomRaw = zahlOderNull(folie.coverBildBottom);
  const bleedRaw = zahlOderNull(folie.coverBildBleed);
  const fitRaw = String(folie.coverBildFit || "").toLowerCase();
  const fit = fitRaw === "contain" ? "contain" : fitRaw === "width" ? "width" : "cover";
  const hatProfil = edgeToEdge
    || [scaleRaw, breiteRaw, xRaw, yRaw, topRaw, bottomRaw, bleedRaw].some((x) => x !== null)
    || ["contain", "cover", "width"].includes(fitRaw);
  /* Ohne manuelles Profil entscheidet bei Karussells die Browser-QA nach dem
     finalen Titelumbruch über Größe und Position des Motivs. */
  const autoLayout = istCharakter && !hatProfil;
  const klasse = folie.bildFrei === false
    ? "foto"
    : `frei${istCharakter ? " charakter" : ""}${edgeToEdge ? " edge-to-edge" : ""}${edgeToEdge && fit === "width" ? " fit-width" : ""}${autoLayout ? " auto-layout" : ""}`;
  /* Charakter-Szenen sind selbst das Markenzeichen. Neben zwei handelnden
     Figuren noch ein grosses Themen-Icon zu setzen wuerde die Cover wieder
     ueberladen; Stock-/Fallbackmotive behalten das Icon wie bisher. */
  const icon = ICONS[folie.icon] ? folie.icon : "paragraf";
  const zeichen = istCharakter ? "" : farbIcon(icon, klasse.startsWith("frei") ? 240 : 180);
  const charakterZiel = istCharakter ? BUEHNE_CHARAKTER : ziel;
  const box = folie.bildFrei !== false ? motivBuehne(folie.bildBreite, folie.bildHoehe, charakterZiel) : null;
  const scale = istCharakter && scaleRaw !== null ? Math.max(0.65, Math.min(1.35, scaleRaw)) : 1;
  const festeBreite = istCharakter && breiteRaw !== null ? Math.max(720, Math.min(1500, breiteRaw)) : null;
  const x = istCharakter && xRaw !== null ? Math.max(0.05, Math.min(0.95, xRaw)) : null;
  const y = istCharakter && yRaw !== null ? Math.max(0.05, Math.min(0.95, yRaw)) : 0.5;
  const style = [];

  if (edgeToEdge) {
    /* Eine echte Buehne: links/rechts leicht ueber den Rand, oben/unten fest
       definiert. Das Bild selbst fuellt diese Flaeche per object-fit:cover.
       Damit gibt es keine Sticker-Luft mehr und trotzdem keinen Wildwuchs
       ueber den Titelblock. */
    const bleed = bleedRaw !== null ? Math.max(0, Math.min(80, bleedRaw)) : 0;
    style.push(`left:-${Math.round(bleed)}px`);
    style.push(`right:-${Math.round(bleed)}px`);
    style.push(topRaw !== null ? `top:${Math.round(topRaw)}px` : "top:auto");
    style.push(bottomRaw !== null ? `bottom:${Math.round(bottomRaw)}px` : "bottom:0");
    style.push("width:auto");
    style.push("height:auto");
    style.push("transform:none");
    style.push(`--edge-x:${Math.round((x ?? 0.5) * 10000) / 100}%`);
    style.push(`--edge-y:${Math.round(y * 10000) / 100}%`);
    style.push(`--edge-fit:${fit}`);
  } else {
    if (festeBreite && folie.bildBreite && folie.bildHoehe) {
      const ratio = folie.bildHoehe / folie.bildBreite;
      style.push(`width:${Math.round(festeBreite)}px`);
      style.push(`height:${Math.round(festeBreite * ratio)}px`);
    } else if (box) {
      style.push(`width:${Math.round(box.breite * scale)}px`);
      style.push(`height:${Math.round(box.hoehe * scale)}px`);
    }
    if (x != null) {
      style.push(`left:${Math.round(x * 10000) / 100}%`);
      style.push("right:auto");
      style.push("transform:translateX(-50%)");
    }
  }
  const stil = style.length ? ` style="${style.join(";")}"` : "";
  return `<div class="${klasse}"${stil}><img src="${esc(folie.bild)}" alt=""></div>${zeichen ? `<div class="frei-zeichen">${zeichen}</div>` : ""}`;
}

function bildOderIllu(ctx, folie) {
  /* Story mit Motiv (Teaser übernimmt das Bild des Beitrags, Begriff und Tipp
     bekommen ein eigenes): freigestellt unten rechts, wie auf der Titelfolie.
     Pexels verlangt einen sichtbaren Hinweis; Stories haben keine Caption,
     also steht er klein auf der Kachel. */
  if (folie.bild) return `${fotoBuehne(folie, BUEHNE_STORY)}${folie.bildQuelle ? `<div class="bildquelle">${esc(folie.bildQuelle)}</div>` : ""}`;
  if (folie.icon) return `<div class="geist">§</div><div class="illu">${iconSvg(folie.icon)}</div>`;
  return `<div class="geist">§</div>`;
}

/* Zweites Icon für die Karte auf der Bühne – passend, aber nicht identisch. */
function zweitIcon(icon) {
  /* Zweitikon je Hauptikon. Ein Taschenrechner passt in kein Jura-Bild. */
  const paare = { muenzen: "vertrag", rechner: "diagramm", waage: "paragraf", kalender: "uhr", gebaeude: "waage", diagramm: "lupe", dokument: "lupe", warnung: "paragraf", uhr: "kalender", haus: "vertrag", lkw: "vertrag", vertrag: "paragraf", lupe: "dokument", kreislauf: "vertrag", blitz: "warnung", buch: "paragraf", fabrik: "vertrag", person: "vertrag", personen: "buch", globus: "buch", paragraf: "buch", haken: "zielscheibe", kreuz: "warnung", zielscheibe: "haken", trophaee: "zielscheibe" };
  return paare[icon] || "dokument";
}

function sichtbareLaenge(s) {
  return String(s || "").replace(/\*/g, "").replace(/\s+/g, " ").trim().length;
}

function zeilenGreedy(text, max = 17) {
  const woerter = String(text || "").trim().split(/\s+/).filter(Boolean);
  const out = [];
  let aktuell = "";
  for (const wort of woerter) {
    const kandidat = aktuell ? `${aktuell} ${wort}` : wort;
    if (!aktuell || sichtbareLaenge(kandidat) <= max) aktuell = kandidat;
    else {
      out.push(aktuell);
      aktuell = wort;
    }
  }
  if (aktuell) out.push(aktuell);
  return out;
}

const NORM_ZITAT = /(?:§{1,2}|Art\.)\s*\d+[a-z]*(?:\s+(?:(?:Abs\.|Satz|S\.|Nr\.|Alt\.|lit\.)\s*)?[0-9IVXLCa-z]+\)?)*\s+(?:BGB|ZPO|StGB|StPO|GVG|VwGO|VwVfG|BauGB|BauNVO|GewO|POG|PolG|GG|HGB|GmbHG|AktG|InsO|ArbGG|BetrVG|KSchG|TzBfG|SGB|FamFG|WEG|ProdHaftG|StVG|StVO|OWiG|JGG|BeurkG|GBO|ErbbauRG|UWG|MarkenG|UrhG|PatG|AO|EStG|UStG|EGBGB|AEUV|EUV|GRCh|EMRK)[?!:]?/i;

function haengenderNormbruch(zeilen) {
  return zeilen.slice(0, -1).some((z) =>
    /(?:§{1,2}|Art\.|Abs\.|Satz|S\.|Nr\.|Alt\.|lit\.)\s*$/i.test(String(z || "").trim())
  );
}

function normZitatBrechen(zitat, max = 19) {
  const sauber = String(zitat || "").replace(/\s+/g, " ").trim();
  if (sichtbareLaenge(sauber) <= max + 2) return [sauber];
  const kandidaten = [" Satz ", " S. ", " Nr. ", " Alt. ", " lit. "]
    .map((marker) => {
      const i = sauber.indexOf(marker);
      if (i <= 0) return null;
      const links = sauber.slice(0, i).trim();
      const rechts = sauber.slice(i + 1).trim();
      return { links, rechts, score: Math.max(sichtbareLaenge(links), sichtbareLaenge(rechts)) };
    })
    .filter(Boolean)
    .sort((a, b) => a.score - b.score);
  return kandidaten.length ? [kandidaten[0].links, kandidaten[0].rechts] : [sauber];
}

function zeilenMitNormZitat(teil, max = 19) {
  const text = String(teil || "");
  const m = NORM_ZITAT.exec(text);
  if (!m) return null;
  const davor = text.slice(0, m.index).trim();
  const norm = m[0].trim();
  const danach = text.slice(m.index + m[0].length).trim();
  return [
    ...zeilenGreedy(davor, max),
    ...normZitatBrechen(norm, max),
    ...zeilenGreedy(danach, max),
  ].filter(Boolean);
}

/* Explizite KI-Zeilen sind redaktionell wertvoll, aber keine Zeile darf
   technisch aus ihrer Pille laufen. Wir teilen deshalb nur wirklich zu lange
   Mehrwort-Zeilen weiter auf. Einzelne lange Fachwoerter bleiben ungeteilt und
   nutzen die vorhandenen festen Schriftstufen. */
function expliziteTitelZeilenAnpassen(zeilen, max = 21) {
  let out = [...zeilen];
  let guard = 0;
  while (out.length < 4 && guard++ < 8) {
    let index = -1;
    let laenge = max;
    for (let i = 0; i < out.length; i++) {
      const z = String(out[i] || "").trim();
      if (!/\s/.test(z)) continue;
      const l = sichtbareLaenge(z);
      if (l > laenge) { laenge = l; index = i; }
    }
    if (index < 0) break;

    const original = out[index];
    const mitNorm = zeilenMitNormZitat(original, Math.min(max, 19));
    let split = mitNorm && mitNorm.length > 1 ? mitNorm : zeilenGreedy(original, max);
    if (split.length <= 1 || out.length - 1 + split.length > 4) break;
    out.splice(index, 1, ...split);
  }
  return out;
}

/* Semantische Zeilen statt Browser-Zufallsumbruch. Jede dunkle Pille ist eine
   Sinneinheit: Norm, Gegensatz, Reihenfolge oder Ergebnis. Neue Beiträge
   liefern die Zeilen aus der Hook-Regie; Altbestand bekommt einen
   deterministischen Fallback. */
export function titelZeilen(titel, vorgegeben = null) {
  const sauber = String(titel || "").replace(/\s+/g, " ").trim();
  const explizit = Array.isArray(vorgegeben)
    ? vorgegeben.map((x) => String(x || "").replace(/\s+/g, " ").trim()).filter(Boolean).slice(0, 4)
    : [];
  if (explizit.length >= 2 && !haengenderNormbruch(explizit)) {
    const angepasst = expliziteTitelZeilenAnpassen(explizit, 21);
    const technischPlausibel = angepasst.every((z) => sichtbareLaenge(z) <= 21 || !/\s/.test(z));
    if (technischPlausibel && angepasst.length <= 4 && !haengenderNormbruch(angepasst)) return angepasst;
  }

  const relation = sauber.match(/^(.+?)\s+(kommt vor|ist nicht automatisch)\s+(.+)$/i);
  if (relation) return [relation[1], relation[2], relation[3]];

  const teile = [];
  const trenner = sauber.match(/^(.+?[?:])\s+(.+)$/);
  if (trenner) {
    teile.push(trenner[1]);
    teile.push(trenner[2]);
  } else {
    teile.push(sauber);
  }

  /* Normzitate sind eine semantische Einheit. Ein Zeilenumbruch zwischen
     "§ 80 Abs. 5" und "VwGO" ist fachlich und optisch schlechter als eine
     etwas längere Pille; deshalb bleiben bekannte Gesetzeszitate zusammen. */
  const istNormEinheit = (teil) => /^(?:§§?|Art\.)\s/i.test(teil)
    && /\b(?:BGB|ZPO|StGB|StPO|GVG|VwGO|VwVfG|BauGB|BauNVO|GewO|POG|PolG|GG|HGB|GmbHG|AktG|InsO|ArbGG|BetrVG|KSchG|TzBfG|SGB|FamFG|WEG|ProdHaftG|StVG|StVO|OWiG|JGG|BeurkG|GBO|ErbbauRG|UWG|MarkenG|UrhG|PatG|AO|EStG|UStG|EGBGB|AEUV|EUV|GRCh|EMRK)[?!:]?$/i.test(teil);
  const bauen = (max) => teile.flatMap((teil) => {
    if (istNormEinheit(teil)) return normZitatBrechen(teil, max);
    return zeilenMitNormZitat(teil, max) || zeilenGreedy(teil, max);
  });
  let zeilen = bauen(16);
  if (zeilen.length > 4) zeilen = bauen(19);
  if (zeilen.length > 4) zeilen = bauen(22);
  while (zeilen.length > 4) {
    const letzte = zeilen.pop();
    zeilen[zeilen.length - 1] = `${zeilen.at(-1)} ${letzte}`;
  }
  return zeilen.filter(Boolean);
}

function titelKlasse(t, zeilen = null) {
  const z = titelZeilen(t, zeilen);
  const max = Math.max(0, ...z.map(sichtbareLaenge));
  if (max > 22) return "winzig";
  if (max > 19 || (z.length === 4 && max > 16)) return "klein";
  return "";
}

/* Handschriftliche Cover-Zusätze sind deaktiviert. Cover und Reel-Cover
   tragen nur die feste Marken-Hierarchie aus Fachband, Titel, Badge und Motiv. */
function coverHinweisHtml() {
  return "";
}

function titelBlock(titel, zeilen, ctx) {
  const klasse = titelKlasse(titel, zeilen);
  if ((ctx?.stil?.familie || ctx?.stil?.id) === "bunt") {
    return `<h1 class="${klasse} titel-stack">${titelZeilen(titel, zeilen).map((z) => `<span class="titel-zeile">${markierenTitel(z)}</span>`).join("")}</h1>`;
  }
  return `<h1 class="${klasse}"><span class="z">${markierenTitel(titel)}</span></h1>`;
}

function ctaIconAusText(text) {
  const t = String(text || "").toLowerCase();
  if (/zustell|brief|post|mitteil|bescheid/.test(t)) return "umschlag";
  if (/vollstreck|gericht|entscheidung|urteil|tenor/.test(t)) return "hammer";
  if (/titel|anspruch|norm|gesetz|paragraph|schema|obersatz|dokument|antrag|akte|sachverhalt|fall/.test(t)) return "dokument";
  if (/klausel|ausnahme|prüf|kontroll|subsum|merkmal|abgrenz|voraussetz|aufbau|schritt|reihenfolg/.test(t)) return "lupe";
  if (/abwäg|verhältnis|angemessen|interessen|gewicht|würdig|vergleich|unterscheid/.test(t)) return "waage";
  if (/speicher|wiederhol|lern|merk|festig/.test(t)) return "buch";
  if (/lerngruppe|teilen|schick|person|beteilig|partei/.test(t)) return "personen";
  if (/frage|kommentar|unklar|erklär/.test(t)) return "frage";
  if (/frist|zeitpunkt|dauer|uhr/.test(t)) return "uhr";
  if (/fehler|falsch|warn|vermeid/.test(t)) return "warnung";
  if (/ergebnis|rechtsfolge|fertig|abschließ/.test(t)) return "haken";
  return null;
}

function ctaIconSchluessel(folie, text, index) {
  const key = folie.icons?.[index] || ctaIconAusText(text);
  if (!key) throw new Error(`CTA-Punkt braucht einen semantischen Icon-Key: ${String(text || "").trim()}`);
  if (!(key in ICONS) && !(key in ZUORDNUNG)) throw new Error(`Unbekannter CTA-Icon-Key: ${key}`);
  return key;
}

const FOLIEN = {
  titel: (f, ctx, i, n) => {
    const bunt = (ctx.stil.familie || ctx.stil.id) === "bunt";
    const badge = String(f.coverBadge || f.prioritaetText || "").trim();
    return `
    ${kopf(ctx, "")}
    ${titelBlock(f.titel, f.titelZeilen, ctx)}
    ${f.untertitel ? `<p class="unter">${markieren(f.untertitel)}</p>` : ""}
    ${badge ? `<div class="cover-badge">${esc(badge)}</div>` : ""}
    ${!bunt && f.pille ? `<div><span class="pille">${esc(f.pille)}</span></div>` : ""}
    ${f.coverBildAuslassen ? "" : (f.bild ? fotoBuehne(f) : bildOderIllu(ctx, f))}
    ${bunt && (f.bild || f.coverBildAuslassen) ? coverHinweisHtml(f) : ""}
    ${!f.coverBildAuslassen && !f.bild && bunt ? `<div class="karte2">${iconSvg(zweitIcon(f.icon), 120)}</div><span class="stern" style="left:150px;top:790px">✦</span><span class="stern" style="left:900px;top:750px;font-size:40px">✦</span><span class="stern" style="left:860px;top:1040px">✦</span>` : ""}
    ${fuss(ctx)}`;
  },
  text: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    <h2>${markierenTitel(f.titel)}</h2>
    ${f.text ? `<div class="text">${String(f.text).split(/\n+/).map((p) => `<p>${markieren(p)}</p>`).join("")}</div>` : ""}
    ${f.punkte?.length ? `<ul class="punkte">${f.punkte.map((p) => `<li><span>${markieren(p)}</span></li>`).join("")}</ul>` : ""}
    ${fuss(ctx)}`,
  schritte: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    <h2>${markierenTitel(f.titel)}</h2>
    <ol class="schritte">${(f.schritte || []).map((s) => (typeof s === "string" ? `<li><b>${markieren(s)}</b></li>` : `<li><div><b>${markieren(s.titel)}</b>${s.text ? `<span>${markieren(s.text)}</span>` : ""}</div></li>`)).join("")}</ol>
    ${fuss(ctx)}`,
  vergleich: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    <h2>${markierenTitel(f.titel)}</h2>
    <div class="vergleich">
      <div class="spalte links"><h3>${markieren(f.links?.titel)}</h3><ul>${(f.links?.punkte || []).map((p) => `<li>${markieren(p)}</li>`).join("")}</ul></div>
      <div class="spalte rechts"><h3>${markieren(f.rechts?.titel)}</h3><ul>${(f.rechts?.punkte || []).map((p) => `<li>${markieren(p)}</li>`).join("")}</ul></div>
    </div>
    ${fuss(ctx)}`,
  rechnung: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    <h2>${markierenTitel(f.titel)}</h2>
    <div class="rechnung">
      <div class="formel">${esc(f.formel)}</div>
      ${f.zeilen?.length ? `<div class="zeilen">${f.zeilen.map((z) => `<div>${esc(z)}</div>`).join("")}</div>` : ""}
      ${f.ergebnis ? `<div class="ergebnis">${esc(f.ergebnis)}</div>` : ""}
    </div>
    ${f.text ? `<div class="text"><p>${markieren(f.text)}</p></div>` : ""}
    ${fuss(ctx)}`,
  karte: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    <h2>${markierenTitel(f.titel || "Auf einen Blick")}</h2>
    <ol class="schritte karte">${(f.schritte || []).map((s) => (typeof s === "string" ? `<li><b>${markieren(s)}</b></li>` : `<li><div><b>${markieren(s.titel)}</b>${s.text ? `<span>${markieren(s.text)}</span>` : ""}</div></li>`)).join("")}</ol>
    ${fuss(ctx)}`,
  merke: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    ${farbIcon("merke", 64) ? `<div class="merke-icon">${farbIcon("merke", 64)}</div>` : ""}
    ${f.titel ? `<h2>${markierenTitel(f.titel)}</h2>` : ""}
    <p class="merke">${markieren(f.text)}</p>
    ${fuss(ctx)}`,
  cta: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    <div class="cta">
      <h2>${markieren(f.titel || "Folgen für mehr.")}</h2>
      <div class="liste">
        ${(f.punkte || ["Folgen für tägliche Prüfungsfragen", "Speichern für die Wiederholung", "Fragen? Ab in die Kommentare"]).map((p, k) => `<div>${iconSvg(ctaIconSchluessel(f, p, k), 56)}<span>${markieren(p)}</span></div>`).join("")}
      </div>
    </div>
    ${fuss(ctx)}`,
};

export function folieHtml(folie, ctx, index, anzahl) {
  const render = FOLIEN[folie.art] || FOLIEN.text;
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>${css(ctx.stil, "beitrag")}${klausurCss(ctx)}${buntCss(ctx)}</style></head>
<body class="stil-${ctx.stil.id} familie-${ctx.stil.familie || ctx.stil.id}"><div class="folie art-${esc(folie.art || "text")}${folie.art === "titel" && folie.coverBildAuslassen ? " cover-ohne-bild" : ""}">${render(folie, ctx, index, anzahl)}</div></body></html>`;
}

const sk = (ctx) => kopf(ctx, "");

/* Überzeile einer Story mit dem farbigen Zeichen ihrer Art (Merksatz → Glühbirne,
   Fehler → Warnkreis). Ohne Iconify-Satz steht die Zeile ohne Zeichen. */
function ueberzeile(art, text) {
  const zeichen = farbIcon(art, 52);
  return `<div class="ueberzeile">${zeichen ? `<span class="uz-icon">${zeichen}</span>` : ""}<span>${esc(text)}</span></div>`;
}

/* Zahl-des-Tages bleibt absichtlich riesig, wird aber nach Zeichenlaenge
   abgestuft. Die fachliche Validierung begrenzt das Feld zusaetzlich auf acht
   Zeichen und verlangt mindestens eine Ziffer. So kann selbst ein manuell
   finalisierter Wert nicht mehr rechts aus der Story laufen. */
function storyZahlGroesse(wert) {
  const laenge = String(wert ?? "").trim().length;
  if (laenge <= 3) return 300;
  if (laenge <= 5) return 230;
  return 180;
}

function normListeHtml(wert, extraKlasse = "") {
  const teile = String(wert || "").split(/\s*·\s*/).map((x) => x.trim()).filter(Boolean);
  const klasse = `norm${extraKlasse ? ` ${extraKlasse}` : ""}`;
  if (teile.length <= 1) return `<div class="${klasse}">${esc(wert)}</div>`;
  return `<div class="${klasse} norm-liste">${teile.map((teil) => `<span class="norm-einheit">${esc(teil)}</span>`).join("")}</div>`;
}

function storySemantikPruefen(story = {}) {
  if (story.art === "fehler") {
    if (!String(story.falsch || story.titel || "").trim()) {
      throw new Error("Fehler-Story braucht eine falsche Aussage in falsch oder titel.");
    }
    if (!String(story.richtigText || story.text || "").trim()) {
      throw new Error("Fehler-Story braucht eine richtige Aufloesung in richtigText oder text.");
    }
  }
  if (story.art === "norm" && !String(story.norm || "").trim()) {
    throw new Error("Norm-Story braucht mindestens eine Norm.");
  }
  if (story.art === "zahl") {
    const n = Number.parseInt(String(story.zahl || ""), 10);
    if (Number.isInteger(n) && n >= 2 && n <= 6) {
      if (!Array.isArray(story.punkte) || story.punkte.length !== n) {
        throw new Error(`Zahl-Story mit ${n} braucht genau ${n} sichtbar getrennte punkte.`);
      }
    }
  }
}

const STORIES = {
  teaser: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("teilen", s.ueberzeile || "Neuer Beitrag")}
    <h1 class="${titelKlasse(s.titel)}">${markierenTitel(s.titel)}</h1>
    ${s.coverBild ? "" : (s.text ? `<div class="text">${markieren(s.text)}</div>` : "")}
    <div><span class="pille">${esc(s.pille || "Jetzt im Feed")}</span></div>
    ${s.coverBild
      ? `<div class="teaser-cover"><img src="${esc(s.coverBild)}" alt=""></div>`
      : `<div class="hinweis">Oben auf den Namen tippen – der Beitrag ist der neueste im Profil.</div>${bildOderIllu(ctx, s)}`}
    ${fuss(ctx)}`,
  frage: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("frage", s.ueberzeile || "Prüfungsfrage")}
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.optionen?.length ? `<div class="optionen">${s.optionen.map((o, k) => `<div><b>${"ABCD"[k]}</b><span>${markieren(o)}</span></div>`).join("")}</div>` : ""}
    ${s.interaktiv
      /* Interaktive Fassung: Statt des Hinweises bleibt ein freier Streifen,
         auf den der native Umfrage-Sticker gelegt wird. Der Platz wird nach
         dem Rendern gemessen (render.mjs) - geschätzte Koordinaten lägen bei
         einem längeren Titel irgendwann auf dem Text. Die Antworten stehen
         schon oben; der Sticker fragt nur A/B/C ab. */
      ? `<div class="umfrageplatz"></div>`
      : `<div class="pfeil">Antwort in der nächsten Story →</div>`}
    ${fuss(ctx)}`,
  antwort: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("haken", s.ueberzeile || "Richtig ist")}
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.optionen?.length ? `<div class="optionen">${s.optionen.map((o, k) => `<div class="${k === s.richtig ? "richtig" : ""}"><b>${"ABCD"[k]}</b><span>${markieren(o)}</span></div>`).join("")}</div>` : ""}
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    ${fuss(ctx)}`,
  norm: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("norm", s.ueberzeile || "Norm des Tages")}
    ${normListeHtml(s.norm)}
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    <div class="geist">§</div>
    ${fuss(ctx)}`,
  /* Der Meinungsstreit - das, was eine Jura-Klausur von jedem anderen Fach
     unterscheidet. Zwei Ansichten nebeneinander, darunter der Streitentscheid:
     genau die Reihenfolge, in der er in der Klausur geschrieben wird. */
  streitstand: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("streitstand", s.ueberzeile || "Streitstand")}
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.norm ? `<div class="norm klein">${esc(s.norm)}</div>` : ""}
    <div class="ansichten">${(s.optionen || []).slice(0, 2).map((o) => {
      const [kopf, ...rest] = String(o).split(":");
      const text = rest.join(":").trim();
      return `<div><b>${markieren(text ? kopf : "Ansicht")}</b><span>${markieren(text || kopf)}</span></div>`;
    }).join("")}</div>
    ${s.text ? `<div class="karte entscheid"><div class="t">Streitentscheid</div><div class="u">${markieren(s.text)}</div></div>` : ""}
    ${fuss(ctx)}`,
  merksatz: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("merke", s.ueberzeile || "Merksatz")}
    <p class="merke">${markieren(s.text)}</p>
    ${s.titel ? `<div class="hinweis">${markieren(s.titel)}</div>` : ""}
    ${fuss(ctx)}`,
  countdown: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("countdown", s.ueberzeile || "Noch")}
    <div class="zahl">${esc(s.zahl)}</div>
    <div class="zahl-unter">${markierenTitel(s.titel)}</div>
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    <div class="balken"><i style="width:${Math.max(2, Math.min(100, Number(s.fortschritt || 0)))}%"></i></div>
    ${fuss(ctx)}`,
  formel: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("formel", s.ueberzeile || "Rechenweg")}
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    <div class="karte"><div class="t" style="font-family:var(--mono)">${esc(s.formel)}</div>${s.text ? `<div class="u">${markieren(s.text)}</div>` : ""}</div>
    ${fuss(ctx)}`,
  begriff: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("begriff", s.ueberzeile || "Begriff des Tages")}
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.norm ? `<div class="norm" style="font-size:44px;margin-top:30px">${esc(s.norm)}</div>` : ""}
    <div class="text">${markieren(s.text)}</div>
    ${bildOderIllu(ctx, s)}
    ${fuss(ctx)}`,
  zahl: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("zahl", s.ueberzeile || "Zahl des Tages")}
    <div class="zahl" style="font-size:${storyZahlGroesse(s.zahl)}px;white-space:nowrap;max-width:100%">${esc(s.zahl)}</div>
    <div class="zahl-unter">${markierenTitel(s.titel)}</div>
    ${s.punkte?.length ? `<div class="zahl-punkte">${s.punkte.map((p, i) => `<div class="zp"><b>${i + 1}</b><span>${markieren(p)}</span></div>`).join("")}</div>` : (s.text ? `<div class="text">${markieren(s.text)}</div>` : "")}
    ${fuss(ctx)}`,
  tipp: (s, ctx) => `
    ${sk(ctx)}
    ${ueberzeile("tipp", s.ueberzeile || "Klausurtipp")}
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    <div class="text">${markieren(s.text)}</div>
    ${bildOderIllu(ctx, s)}
    ${fuss(ctx)}`,
  fehler: (s, ctx) => {
    const falsch = String(s.falsch || s.titel || "").trim();
    const richtig = String(s.richtigText || s.text || "").trim();
    return `
    ${sk(ctx)}
    ${ueberzeile("fehler", s.ueberzeile || "Typischer Fehler")}
    ${s.falsch && s.titel ? `<h1 class="klein">${markierenTitel(s.titel)}</h1>` : ""}
    <div class="karte"><div class="t" style="color:var(--rot)">Falsch</div><div class="u">${markieren(falsch)}</div></div>
    <div class="karte"><div class="t" style="color:var(--ok)">Richtig</div><div class="u">${markieren(richtig)}</div></div>
    ${fuss(ctx)}`;
  },
};

export function storyHtml(story, ctx) {
  storySemantikPruefen(story);
  const render = STORIES[story.art] || STORIES.tipp;
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>${css(ctx.stil, "story")}${klausurCss(ctx)}${buntCss(ctx)}</style></head>
<body class="stil-${ctx.stil.id} familie-${ctx.stil.familie || ctx.stil.id}"><div class="story">${render(story, ctx)}</div></body></html>`;
}

/**
 * Cover eines Reels: Thema, Fach und Dauer als ruhiges Standbild, damit im Feed
 * und im Profilraster sofort zu sehen ist, worum es geht. Ein Standbild aus dem
 * Video zeigt sonst nur den Hintergrundclip.
 * @param {{titel, ueberzeile?, dauerText?, icon?}} daten
 */
export function coverHtml(daten, ctx) {
  const bunt = (ctx.stil.familie || ctx.stil.id) === "bunt";
  const badgeRaw = String(daten.coverBadge || "").trim();
  /* "Reel" steht bereits als feste Marke oben rechts. Ein zweites "Reel"
     unter dem Titel wirkt wie ein verrutschtes Label und wird deshalb nicht
     noch einmal als Cover-Badge gesetzt. Inhaltliche Badges bleiben erhalten. */
  const badge = /^reel$/i.test(badgeRaw) ? "" : badgeRaw;
  const inhalt = `
    ${kopf(ctx, "")}
    <span class="reelmarke">Reel</span>
    ${titelBlock(daten.titel, daten.titelZeilen, ctx)}
    ${badge ? `<div class="cover-badge">${esc(badge)}</div>` : ""}
    ${daten.coverBildAuslassen ? "" : (daten.bild ? fotoBuehne(daten, BUEHNE_STORY) : `<div class="buehne">${iconSvg(ICONS[daten.icon] ? daten.icon : "paragraf")}</div>`)}
    ${bunt && (daten.bild || daten.coverBildAuslassen) ? coverHinweisHtml(daten) : ""}
    ${fuss(ctx)}`;
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>${css(ctx.stil, "story")}${klausurCss(ctx)}${buntCss(ctx)}</style></head>
<body class="stil-${ctx.stil.id} familie-${ctx.stil.familie || ctx.stil.id}"><div class="story cover">${inhalt}</div></body></html>`;
}

export const FOLIEN_ARTEN = Object.keys(FOLIEN);
export const STORY_ARTEN = Object.keys(STORIES);
