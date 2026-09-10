/* ==========================================================================
   HTML-Vorlagen für Beitragsfolien (1080×1350) und Stories (1080×1920).
   Eine Vorlage je Folienart; das Aussehen kommt aus stile.mjs.
   ========================================================================== */

import path from "node:path";
import { fileURLToPath } from "node:url";
import { iconSvg, ICONS } from "./stile.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
export const FONT_DIR = path.resolve(hier, "../fonts");

export const MASSE = {
  beitrag: { breite: 1080, hoehe: 1350 },
  story: { breite: 1080, hoehe: 1920 },
};

export const KLAUSUR_FARBE = { 1: "k1", 2: "k2", 3: "k3" };

export function esc(s) {
  return String(s ?? "")
    .replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]))
    .replace(/i\.\s?V\.\s?m\./g, "i.\u00a0V.\u00a0m.")
    .replace(/(§§?|Abs\.|Nr\.|S\.|Art\.|R|H)\s(?=\d)/g, "$1\u00a0");
}

/* Überschriften: nur Hervorhebungen, keine Mono-Normen (die wirken in Großschrift fremd). */
export function markierenTitel(s) {
  return esc(s).replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

/* Hervorhebungen: *wichtig* → <em>, Normen in Mono. */
export function markieren(s) {
  let t = esc(s);
  t = t.replace(/\*([^*]+)\*/g, "<em>$1</em>");
  t = t.replace(/(§§?\s?[\dA-Za-z.\s]+?(?:HGB|EStG|AO|UStG|KStG|GewStG|ErbStG|BewG|UmwStG|AStG|EStDV|EStR|KStR|UStAE|BGB|GrEStG|FGO|DBA))/g, '<code>$1</code>');
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
.story .ueberzeile{margin-top:70px;font-size:34px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-weich);font-weight:700}
.story .etikett{font-size:30px}
.story h1{font-size:120px;margin-top:34px}
.story h1.klein{font-size:96px}
.story .text{font-size:48px;line-height:1.4;margin-top:44px}
.story .norm{margin-top:60px;font-family:var(--mono);font-size:64px;line-height:1.2;color:var(--akzent);text-wrap:balance}
.stil-klausurbogen .story .norm{color:var(--rot)}
.story .optionen{margin-top:60px;display:flex;flex-direction:column;gap:24px}
.story .optionen div{padding:30px 36px;border:3px solid var(--linie);border-radius:var(--ecken);font-size:42px;line-height:1.3;background:var(--flaeche);display:flex;gap:24px}
.story .optionen div b{font-family:var(--titel);color:var(--akzent);flex:none;width:52px}
.story .optionen div.richtig{border-color:var(--ok);box-shadow:inset 0 0 0 3px var(--ok)}
.story .zahl{margin-top:40px;font-family:var(--titel);font-size:420px;line-height:.95;color:var(--akzent);letter-spacing:-.02em}
.stil-klausurbogen .story .zahl{color:var(--rot)}
.story .zahl-unter{font-size:56px;line-height:1.2;margin-top:10px;font-family:var(--titel);text-wrap:balance}
.story .merke{font-size:96px}
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
.story .pfeil{margin-top:auto;text-align:center;font-size:34px;color:var(--text-weich);letter-spacing:.12em;text-transform:uppercase}
/* Reel-Cover: das Standbild, das im Feed und im Profilraster für das Reel steht.
   Alles Wichtige liegt im mittleren 4:5-Bereich (y 285–1635), den Instagram
   dort zeigt. */
.story.cover .reelmarke{position:absolute;right:84px;top:40px;font-family:var(--text);font-weight:700;font-size:28px;letter-spacing:.16em;text-transform:uppercase;background:var(--pille);color:var(--pille-text);padding:12px 26px;border-radius:40px}
.story.cover .dauer{margin-top:30px;font-size:36px;color:var(--text-weich)}
.story.cover .buehne{margin:auto auto 150px;width:460px;height:460px;display:flex;align-items:center;justify-content:center;position:relative}
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
  const p = stil.tagFarben?.[ctx.klausur] || stil.tagFarben?.[3];
  const pfeil = `url("data:image/svg+xml,${PFEIL.replace("%23111", encodeURIComponent(p.dunkel))}")`;
  return `
:root{--grund:${p.grund};--text:${p.dunkel};--text-weich:${p.dunkel};--akzent:${p.dunkel};--pille:${p.dunkel};--pille-text:#fff;--flaeche:rgba(255,255,255,.92);--linie:rgba(255,255,255,.45);--hell:${p.hell};--lila:${p.lila};--akzent2:${p.akzent2}}
.folie,.story,.reel{background:${p.grund};color:${p.dunkel}}
/* Ecke oben links: dunkles Band mit dem Fach; oben rechts der Zähler im weißen Kreis */
.kopf{position:absolute;left:0;top:0;right:0;height:120px;padding:0}
.kopf .etikett{position:absolute;left:0;top:0;font-family:"Inter";font-weight:700;font-size:28px;letter-spacing:.02em;text-transform:none;background:${p.dunkel};color:#fff;padding:16px 46px 16px 40px;clip-path:polygon(0 0,100% 0,calc(100% - 26px) 100%,0 100%);flex-direction:row;line-height:1.1}
.kopf .etikett .punkt{display:none}
.kopf .zaehler{position:absolute;right:46px;top:40px;width:78px;height:78px;border-radius:50%;background:rgba(255,255,255,.9);color:${p.dunkel};font-family:"Inter";font-weight:700;font-size:26px;display:flex;align-items:center;justify-content:center}
.kopf .zaehler:empty{display:none}
/* Titel als Pillen, Zeile für Zeile. Die erste Folie wird im Feed als
   Vorschaubild von 300 px Breite gesehen – dort entscheidet die Schriftgröße,
   ob jemand den Beitrag überhaupt liest. Deshalb so groß wie möglich; zu
   lange Titel fängt einpassen() ab. */
h1{margin-top:72px;font-size:100px;line-height:1.5}
h1.klein{font-size:86px}h1.winzig{font-size:74px}
h1 .z{background:${p.dunkel};color:#fff;padding:.14em .5em;border-radius:48px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
h1 em{color:${p.akzent2}}
.unter{margin-top:22px;display:inline-block;width:fit-content;background:${p.hell};color:${p.dunkel};padding:12px 30px;border-radius:40px;font-weight:700;font-size:36px;line-height:1.25;margin-left:24px}
.prio{margin-top:20px;margin-left:24px;width:fit-content;background:${p.lila};color:${p.dunkel};padding:10px 26px;border-radius:40px;text-transform:none;letter-spacing:0;font-size:28px}
.prio i{display:none}
/* Handschrift-Hinweis mit Pfeil statt Pille */
.art-titel .pille{background:none;color:${p.dunkel};font-family:"Caveat";font-size:58px;font-weight:700;padding:0 0 0 170px;margin-top:40px;margin-left:420px;position:relative;transform:rotate(-4deg);letter-spacing:0}
.art-titel .pille::before{content:"";position:absolute;left:0;top:-30px;width:150px;height:110px;background:${pfeil} no-repeat center/contain}
/* Bühne: Blase, großes Icon, §-Badge, Karte, Sterne */
.art-titel::after{content:"";position:absolute;left:210px;bottom:-140px;width:660px;height:660px;border-radius:50%;background:rgba(255,255,255,.16);pointer-events:none}
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
.merke::before,.merke::after{color:${p.akzent2}}
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
.story .optionen div b{color:${p.dunkel}}
.story .optionen div.richtig{box-shadow:inset 0 0 0 5px ${p.dunkel}}
.story .zahl{color:#fff;text-shadow:0 12px 40px rgba(0,0,0,.18)}
.story .zahl-unter{color:${p.dunkel}}
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
.story.cover .dauer{font-family:"Caveat";font-size:52px;color:${p.dunkel};opacity:1;margin-top:24px}
.story.cover .buehne::before{background:rgba(255,255,255,.75);opacity:1}
.story.cover .buehne .icon{color:${p.dunkel}}
/* Reels */
.reel .fortschritt{background:rgba(255,255,255,.4)}
.reel .fortschritt i{background:${p.dunkel}}
.reel .trenner{background:rgba(255,255,255,.5)}
.reel .kopf{position:absolute;left:84px;right:84px;height:auto}
.reel .kopf .etikett{position:static;clip-path:none;border-radius:40px;padding:10px 26px}
.reel .kopf .zaehler{position:static;width:auto;height:auto;background:none;color:${p.dunkel};font-size:28px}
.reel .hook h1{font-size:68px;line-height:1.15;margin-top:0;width:fit-content;background:${p.dunkel};color:#fff;padding:.22em .5em;border-radius:48px}
.reel .hook .unter{margin-left:0}
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
  return `<div class="fuss"><span class="handle">${esc(ctx.handle || "")}</span><span class="klausur">${esc(KLAUSUR_KURZ[ctx.klausur] || "")}</span></div>`;
}
/* Die Marke sortiert nach Rechtsgebiet - das steht in der Fusszeile, so wie
   beim Steuerkanal der Klausurtag. */
const KLAUSUR_KURZ = { 1: "Zivilrecht", 2: "Strafrecht", 3: "Öffentliches Recht" };

function bildOderIllu(ctx, folie) {
  if (folie.icon) return `<div class="geist">§</div><div class="illu">${iconSvg(folie.icon)}</div>`;
  return `<div class="geist">§</div>`;
}

/* Zweites Icon für die Karte auf der Bühne – passend, aber nicht identisch. */
function zweitIcon(icon) {
  /* Zweitikon je Hauptikon. Ein Taschenrechner passt in kein Jura-Bild. */
  const paare = { muenzen: "vertrag", rechner: "diagramm", waage: "paragraf", kalender: "uhr", gebaeude: "waage", diagramm: "lupe", dokument: "lupe", warnung: "paragraf", uhr: "kalender", haus: "vertrag", lkw: "vertrag", vertrag: "paragraf", lupe: "dokument", kreislauf: "vertrag", blitz: "warnung", buch: "paragraf", fabrik: "vertrag", person: "vertrag", personen: "buch", globus: "buch", paragraf: "buch", haken: "zielscheibe", kreuz: "warnung", zielscheibe: "haken", trophaee: "zielscheibe" };
  return paare[icon] || "dokument";
}

function titelKlasse(t) {
  const l = (t || "").length;
  return l > 92 ? "winzig" : l > 62 ? "klein" : "";
}

const FOLIEN = {
  titel: (f, ctx, i, n) => `
    ${kopf(ctx, "")}
    <h1 class="${titelKlasse(f.titel)}"><span class="z">${markierenTitel(f.titel)}</span></h1>
    ${f.untertitel ? `<p class="unter">${markieren(f.untertitel)}</p>` : ""}
    ${f.prioritaet ? `<div class="prio ${f.prioritaet}"><i></i>${esc(f.prioritaetText || "")}</div>` : ""}
    <div><span class="pille">${esc((ctx.stil.familie || ctx.stil.id) === "bunt" ? (f.hinweis || "So geht's!") : (f.pille || "Swipen →"))}</span></div>
    ${bildOderIllu(ctx, f)}
    ${(ctx.stil.familie || ctx.stil.id) === "bunt" ? `<div class="karte2">${iconSvg(zweitIcon(f.icon), 120)}</div><span class="stern" style="left:150px;top:790px">✦</span><span class="stern" style="left:900px;top:750px;font-size:40px">✦</span><span class="stern" style="left:860px;top:1040px">✦</span>` : ""}
    ${fuss(ctx)}`,
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
    ${f.titel ? `<h2>${markierenTitel(f.titel)}</h2>` : ""}
    <p class="merke">${markieren(f.text)}</p>
    ${fuss(ctx)}`,
  cta: (f, ctx, i, n) => `
    ${kopf(ctx, `${i}/${n}`)}
    <div class="cta">
      <h2>${markieren(f.titel || "Folgen für mehr.")}</h2>
      <div class="liste">
        ${(f.punkte || ["Folgen für tägliche Prüfungsfragen", "Speichern für die Wiederholung", "Fragen? Ab in die Kommentare"]).map((p, k) => `<div>${iconSvg(["haken", "buch", "personen"][k % 3], 56)}<span>${markieren(p)}</span></div>`).join("")}
      </div>
    </div>
    ${fuss(ctx)}`,
};

export function folieHtml(folie, ctx, index, anzahl) {
  const render = FOLIEN[folie.art] || FOLIEN.text;
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>${css(ctx.stil, "beitrag")}${klausurCss(ctx)}${buntCss(ctx)}</style></head>
<body class="stil-${ctx.stil.id} familie-${ctx.stil.familie || ctx.stil.id}"><div class="folie art-${esc(folie.art || "text")}">${render(folie, ctx, index, anzahl)}</div></body></html>`;
}

const sk = (ctx) => kopf(ctx, "");

const STORIES = {
  teaser: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Neuer Beitrag")}</div>
    <h1 class="${titelKlasse(s.titel)}">${markierenTitel(s.titel)}</h1>
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    <div><span class="pille">${esc(s.pille || "Jetzt im Feed")}</span></div>
    <div class="hinweis">Oben auf den Namen tippen – der Beitrag ist der neueste im Profil.</div>
    ${bildOderIllu(ctx, s)}
    ${fuss(ctx)}`,
  frage: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Prüfungsfrage")}</div>
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.optionen?.length ? `<div class="optionen">${s.optionen.map((o, k) => `<div><b>${"ABCD"[k]}</b><span>${markieren(o)}</span></div>`).join("")}</div>` : ""}
    <div class="pfeil">Antwort in der nächsten Story →</div>
    ${fuss(ctx)}`,
  antwort: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Richtig ist")}</div>
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.optionen?.length ? `<div class="optionen">${s.optionen.map((o, k) => `<div class="${k === s.richtig ? "richtig" : ""}"><b>${"ABCD"[k]}</b><span>${markieren(o)}</span></div>`).join("")}</div>` : ""}
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    ${fuss(ctx)}`,
  norm: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Norm des Tages")}</div>
    <div class="norm">${esc(s.norm)}</div>
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    <div class="geist">§</div>
    ${fuss(ctx)}`,
  merksatz: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Merksatz")}</div>
    <p class="merke">${markieren(s.text)}</p>
    ${s.titel ? `<div class="hinweis">${markieren(s.titel)}</div>` : ""}
    ${fuss(ctx)}`,
  countdown: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Noch")}</div>
    <div class="zahl">${esc(s.zahl)}</div>
    <div class="zahl-unter">${markierenTitel(s.titel)}</div>
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    <div class="balken"><i style="width:${Math.max(2, Math.min(100, Number(s.fortschritt || 0)))}%"></i></div>
    ${fuss(ctx)}`,
  formel: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Rechenweg")}</div>
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    <div class="karte"><div class="t" style="font-family:var(--mono)">${esc(s.formel)}</div>${s.text ? `<div class="u">${markieren(s.text)}</div>` : ""}</div>
    ${fuss(ctx)}`,
  begriff: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Begriff des Tages")}</div>
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    ${s.norm ? `<div class="norm" style="font-size:44px;margin-top:30px">${esc(s.norm)}</div>` : ""}
    <div class="text">${markieren(s.text)}</div>
    ${bildOderIllu(ctx, s)}
    ${fuss(ctx)}`,
  zahl: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Zahl des Tages")}</div>
    <div class="zahl" style="font-size:300px">${esc(s.zahl)}</div>
    <div class="zahl-unter">${markierenTitel(s.titel)}</div>
    ${s.text ? `<div class="text">${markieren(s.text)}</div>` : ""}
    ${fuss(ctx)}`,
  tipp: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Klausurtipp")}</div>
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    <div class="text">${markieren(s.text)}</div>
    ${bildOderIllu(ctx, s)}
    ${fuss(ctx)}`,
  fehler: (s, ctx) => `
    ${sk(ctx)}
    <div class="ueberzeile">${esc(s.ueberzeile || "Typischer Fehler")}</div>
    <h1 class="klein">${markierenTitel(s.titel)}</h1>
    <div class="karte"><div class="t" style="color:var(--rot)">Falsch</div><div class="u">${markieren(s.falsch)}</div></div>
    <div class="karte"><div class="t" style="color:var(--ok)">Richtig</div><div class="u">${markieren(s.richtigText || s.text)}</div></div>
    ${fuss(ctx)}`,
};

export function storyHtml(story, ctx) {
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
  const inhalt = `
    ${kopf(ctx, "")}
    <span class="reelmarke">Reel</span>
    <div class="ueberzeile">${esc(daten.ueberzeile || "Reel")}</div>
    <h1 class="${titelKlasse(daten.titel)}">${markierenTitel(daten.titel)}</h1>
    ${daten.dauerText ? `<div class="dauer">${esc(daten.dauerText)}</div>` : ""}
    <div class="buehne">${iconSvg(ICONS[daten.icon] ? daten.icon : "paragraf")}</div>
    ${fuss(ctx)}`;
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>${css(ctx.stil, "story")}${klausurCss(ctx)}${buntCss(ctx)}</style></head>
<body class="stil-${ctx.stil.id} familie-${ctx.stil.familie || ctx.stil.id}"><div class="story cover">${inhalt}</div></body></html>`;
}

export const FOLIEN_ARTEN = Object.keys(FOLIEN);
export const STORY_ARTEN = Object.keys(STORIES);
