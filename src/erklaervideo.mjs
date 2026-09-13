/* ==========================================================================
   Zweites Reel-Layout: das Erklaervideo.

   Entstanden aus der Bild-fuer-Bild-Vermessung zweier Vorbilder (Studyflix).
   Was diese Videos ausmacht und was hier uebernommen ist:

     · Eine einzige Buehne je Kapitel, 10 bis 20 Sekunden lang. Alle drei bis
       fuenf Sekunden kommt ein Element dazu, dazwischen steht das Bild
       vollkommen still. Gemessen: 13,4 s Ueberschrift, 16,2 s Figur, 17,9 s
       erste Plakette, 20,7 s zweite, 28 s Medaillon. Kein Dauerzappeln.
     · Die Figur nimmt 82 bis 83 Prozent der Bildhoehe ein und ist unten
       angeschnitten - sie steht nicht auf der Flaeche, sie ragt aus dem Rand.
       Sie faehrt senkrecht von unten herein und bewegt sich danach nicht mehr.
     · Aussagen stehen auf halbdurchsichtigen schwarzen Plaketten (gemessen 24
       bis 52 Prozent Deckung ueber der Buehnenfarbe), linksbuendig, kleiner
       Eckenradius. Sie fahren seitlich herein und laufen ueber den Bildrand
       hinaus. Darauf stehen Stichworte, keine Saetze - was dazwischen liegt,
       sagt die Stimme.
     · Ein Schluesselwort je Plakette ist farbig abgesetzt.
     · Ein zweites Bild sitzt in einer getoenten Kreisscheibe neben der Figur.
     · Ein rotes Kreuz markiert, was gerade nicht gilt.
     · Keine Musik: In beiden Vorbildern ist das Grundrauschen in den
       Sprechpausen exakt null.

   Die Buehnenfarbe bleibt die Farbe des Klausurtags - sie ist der Markenkern
   und wird hier nicht durch eine fremde Palette ersetzt. Je Kapitel wechselt
   nur der Ton zwischen Grundfarbe und einer dunkleren Mischung, damit ein
   Kapitelwechsel sichtbar ist.
   ========================================================================== */

import fs from "node:fs";
import { CONFIG } from "./config.mjs";
import { normKurz } from "./normen.mjs";

const B = 1080, H = 1920;

const schuetzen = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const esc = (s) => schuetzen(normKurz(s));

/* Ein Wort je Plakette wird farbig. Der Autor markiert es mit *Sternchen*;
   fehlt die Markierung, bleibt die Plakette einfarbig - lieber schlicht als
   das falsche Wort betont.
   Wichtig: Die Kurzform wird auf den ganzen Text angewandt, nicht auf die
   Stuecke. normKurz() schneidet Leerzeichen an den Raendern ab - stueckweise
   angewandt klebte daraus „Rueckstellung:vierFragen". */
function plakettenText(text) {
  return String(normKurz(text) ?? "")
    .split(/(\*[^*]+\*)/)
    .map((t) => (/^\*[^*]+\*$/.test(t) ? `<b>${schuetzen(t.slice(1, -1))}</b>` : schuetzen(t)))
    .join("");
}

/**
 * Stichworte einer Szene. Der Autor liefert sie in `marken`; ohne das Feld
 * wird der Bildschirmtext zerlegt: der erste Teilsatz ist fast immer die
 * Aussage, der Rest die Begruendung, die ohnehin die Stimme traegt.
 */
export function markenFuer(szene, hoechstens = 2) {
  const roh = Array.isArray(szene.marken) ? szene.marken.filter((m) => typeof m === "string" && m.trim()) : [];
  if (roh.length) return roh.slice(0, hoechstens).map((t) => t.trim());
  const quelle = String(szene.text || szene.unter || "").trim();
  if (!quelle) return [];
  return quelle
    .split(/(?<=[.;:])\s+|\s+–\s+/)
    .map((t) => t.replace(/[.;:]\s*$/, "").trim())
    .filter(Boolean)
    .slice(0, hoechstens)
    /* Auf den Plaketten steht nie mehr als ein Atemzug. Was laenger ist, wird
       am letzten Komma vor der Grenze gekappt statt mitten im Wort. */
    .map((t) => (t.length <= 46 ? t : (t.slice(0, 46).replace(/[,\s][^,\s]*$/, "") || t.slice(0, 46)) + " …"));
}

/* Zeitpunkte der Eintritte einer Szene. Gemessen am Vorbild: Die Figur kommt
   kurz nach Kapitelbeginn, die Plaketten verteilen sich ueber die gesprochene
   Strecke, das Medaillon sitzt im letzten Drittel. */
export function eintritte(szene, marken) {
  const von = szene.start, dauer = Math.max(1, szene.dauer);
  const sprichVon = von + Math.min(0.7, dauer * 0.06);
  const sprichDauer = Math.max(0.8, dauer - (sprichVon - von) - Math.min(0.8, dauer * 0.08));
  const n = Math.max(1, marken.length);
  return {
    figur: von + 0.5,
    plaketten: marken.map((_, k) => sprichVon + sprichDauer * (0.2 + (k * 0.62) / n)),
    medaillon: sprichVon + sprichDauer * 0.72,
  };
}

/* Eine dunklere Mischung der Buehnenfarbe fuer jedes zweite Kapitel. */
const dunklerTon = (grund, dunkel) => `color-mix(in srgb, ${grund} 74%, ${dunkel})`;

const KREUZ = '<svg viewBox="0 0 100 100" width="132" height="132"><path d="M14 16 L86 84 M86 16 L14 84" stroke="#ff3b30" stroke-width="13" stroke-linecap="round" fill="none"/></svg>';

/* Motive kommen aus bilder.mjs bereits als Daten-URL; ein Dateipfad geht
   genauso, damit sich das Layout auch einzeln bauen laesst. */
const bildDaten = (q) => {
  if (!q) return null;
  if (/^data:/.test(q)) return q;
  if (!fs.existsSync(q)) return null;
  const art = /\.jpe?g$/i.test(q) ? "jpeg" : "png";
  return `data:image/${art};base64,${fs.readFileSync(q).toString("base64")}`;
};

/**
 * Baut die Seite. `plan.szenen` traegt Startzeit und Dauer je Szene,
 * `reel.szenen` den Inhalt; die Figur steht als Dateipfad in `bild`.
 */
export function erklaerHtml(reel, plan, ctx) {
  const stil = ctx.stil;
  const p = stil.tagFarben?.[ctx.klausur] || stil.tagFarben?.[3] || { grund: stil.farben.grund, dunkel: stil.farben.text, akzent2: stil.farben.akzent };
  const akzent = p.akzent2 || "#ffd166";
  /* Schrift in der dunklen Farbe des Klausurtags - so steht sie auf jeder
     Buehnenfarbe, auch auf dem hellen Gruen des dritten Tages, und passt zu
     den Kacheln des Kanals. Weiss war auf Gruen kaum zu lesen. */
  const kopfFarbe = p.dunkel || "#0b0b0d";

  const daten = [];
  const abschnitte = plan.szenen.map((s, i) => {
    const inhalt = reel.szenen[s.index] || reel.szenen[i] || {};
    const marken = markenFuer(inhalt, CONFIG.reel.erklaerMarken);
    const zeiten = eintritte(s, marken);
    /* Seiten wechseln sich ab: Die Figur steht mal rechts, mal links, die
       Plaketten fahren jeweils von der anderen Seite herein. */
    const seite = i % 2 === 0 ? "rechts" : "links";
    const figur = bildDaten(inhalt.bild);
    const med = bildDaten(inhalt.medaillon);
    daten.push({ von: s.start, bis: s.start + s.dauer, seite, ...zeiten, kreuz: marken.map((_, k) => Boolean(inhalt.kreuz) && k === marken.length - 1) });
    const plaketten = marken.map((m, k) => {
      const mitKreuz = Boolean(inhalt.kreuz) && k === marken.length - 1;
      return `<div class="plakette${mitKreuz ? " mit-kreuz" : ""}">${plakettenText(m)}${mitKreuz ? `<i class="kreuz">${KREUZ}</i>` : ""}</div>`;
    }).join("");
    return `<section class="szene" data-seite="${seite}" style="--buehne:${i % 2 === 0 ? p.grund : dunklerTon(p.grund, p.dunkel)}">
      <h1>${zeilen(inhalt.titel).map((z) => `<span>${esc(z)}</span>`).join("")}</h1>
      <div class="plaketten">${plaketten}</div>
      ${med ? `<div class="medaillon"><img src="${med}" alt=""></div>` : ""}
      ${figur ? `<div class="figur"><img src="${figur}" alt=""></div>` : ""}
    </section>`;
  }).join("");

  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>
${schriftCss()}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:${B}px;height:${H}px;overflow:hidden;background:#000;font-family:"Inter",system-ui,sans-serif}
.reel{position:relative;width:${B}px;height:${H}px;overflow:hidden}
.szene{position:absolute;inset:0;background:var(--buehne);overflow:hidden;display:none}

/* Ueberschrift: weisser Text mit feinem Unterstrich je Zeile. Im Vorbild
   traegt die Ueberschrift nie einen Kasten. */
h1{position:absolute;top:104px;left:60px;right:60px;display:flex;flex-direction:column;align-items:center;gap:16px;text-align:center}
h1 span{display:inline-block;font-size:74px;font-weight:800;color:${kopfFarbe};line-height:1.1;letter-spacing:-0.5px;
        padding-bottom:12px;border-bottom:5px solid ${kopfFarbe}66}

/* Plaketten: halbdurchsichtiges Schwarz, linksbuendig, ueber den Rand hinaus. */
.plaketten{position:absolute;top:640px;display:flex;flex-direction:column;gap:26px}
[data-seite="rechts"] .plaketten{left:-64px;align-items:flex-start}
[data-seite="links"]  .plaketten{right:-64px;align-items:flex-end}
.plakette{position:relative;max-width:900px;background:rgba(0,0,0,.44);color:#fff;font-size:50px;font-weight:600;
          line-height:1.24;border-radius:12px;padding:20px 34px;opacity:0;text-align:left}
[data-seite="rechts"] .plakette{padding-left:88px}
[data-seite="links"]  .plakette{padding-right:88px}
/* Wo ein Kreuz sitzt, bekommt die Plakette an dieser Seite Luft. */
[data-seite="rechts"] .plakette.mit-kreuz{padding-right:170px}
[data-seite="links"]  .plakette.mit-kreuz{padding-left:170px}
.plakette b{font-weight:800;color:${akzent}}
.kreuz{position:absolute;top:50%;right:14px;transform:translateY(-50%) scale(0);display:block;line-height:0}
[data-seite="links"] .kreuz{right:auto;left:14px}

/* Zweitbild: getoente Kreisscheibe in derselben Farbfamilie, ohne Rand. */
.medaillon{position:absolute;top:1120px;width:370px;height:370px;border-radius:50%;background:rgba(0,0,0,.22);
           display:flex;align-items:center;justify-content:center;overflow:hidden;opacity:0;transform:scale(.25)}
[data-seite="rechts"] .medaillon{left:70px}
[data-seite="links"]  .medaillon{right:70px}
.medaillon img{width:84%;height:84%;object-fit:contain}

/* Figur: gross, unten angeschnitten, an einer Seite verankert. */
.figur{position:absolute;bottom:-150px;height:1400px;width:720px;display:flex;align-items:flex-end;justify-content:center;opacity:0}
[data-seite="rechts"] .figur{right:-60px}
[data-seite="links"]  .figur{left:-60px}
.figur img{max-width:100%;max-height:100%;object-fit:contain;object-position:bottom}

.fuss{position:absolute;left:60px;right:60px;bottom:46px;display:flex;justify-content:space-between;
      font-size:30px;font-weight:600;color:${kopfFarbe}b0}
</style></head><body><div class="reel">
${abschnitte}
<div class="fuss"><span>${esc(ctx.handle || "")}</span><span>${esc(ctx.fachLabel || "")}</span></div>
</div>
<script>
const SZENEN = ${JSON.stringify(daten)};
const WISCH = 0.4;
const aus = (x) => (x <= 0 ? 0 : x >= 1 ? 1 : 1 - Math.pow(1 - x, 3));
/* Kurzes Ueberschwingen - im Vorbild rastet das Medaillon mit einem Tick ein. */
const knapp = (x) => (x <= 0 ? 0 : x >= 1 ? 1 : 1 + 1.9 * Math.pow(x - 1, 3) + 1.1 * Math.pow(x - 1, 2));
const teile = [...document.querySelectorAll(".szene")];
window.setzeZeit = function (t) {
  teile.forEach((el, i) => {
    const s = SZENEN[i];
    const sichtbar = t >= s.von - WISCH && t < s.bis;
    el.style.display = sichtbar ? "block" : "none";
    if (!sichtbar) return;
    el.style.zIndex = String(i + 1);
    /* Kapitelwechsel als waagerechter Wisch. */
    const w = i === 0 ? 1 : aus((t - (s.von - WISCH)) / WISCH);
    el.style.clipPath = w >= 1 ? "none" : "inset(0 0 0 " + (100 - w * 100).toFixed(2) + "%)";
    const fig = el.querySelector(".figur");
    if (fig) {
      const q = aus((t - s.figur) / 0.55);
      fig.style.opacity = q > 0 ? "1" : "0";
      fig.style.transform = "translateY(" + ((1 - q) * 1420).toFixed(1) + "px)";
    }
    el.querySelectorAll(".plakette").forEach((pl, k) => {
      const q = aus((t - s.plaketten[k]) / 0.45);
      const weg = s.seite === "rechts" ? -1 : 1;
      pl.style.opacity = q > 0 ? "1" : "0";
      pl.style.transform = "translateX(" + (weg * (1 - q) * (pl.offsetWidth + 90)).toFixed(1) + "px)";
      const kr = pl.querySelector(".kreuz");
      if (kr) {
        const r = knapp((t - (s.plaketten[k] + 0.75)) / 0.32);
        kr.style.transform = "translateY(-50%) scale(" + r.toFixed(3) + ") rotate(" + (-10 * r).toFixed(1) + "deg)";
      }
    });
    const med = el.querySelector(".medaillon");
    if (med) {
      const q = knapp((t - s.medaillon) / 0.45);
      med.style.opacity = q > 0 ? "1" : "0";
      med.style.transform = "scale(" + q.toFixed(3) + ")";
    }
  });
};
/* Ueberschriften, die nicht passen, werden verkleinert - einmal beim Aufbau. */
(function einpassen() {
  for (const el of teile) {
    el.style.display = "block";
    for (const k of el.querySelectorAll("h1 span")) {
      let px = parseFloat(getComputedStyle(k).fontSize);
      for (let i = 0; i < 14 && k.scrollWidth > k.parentElement.clientWidth; i++) { px *= 0.94; k.style.fontSize = px + "px"; }
    }
    for (const k of el.querySelectorAll(".plakette")) {
      let px = parseFloat(getComputedStyle(k).fontSize);
      for (let i = 0; i < 10 && k.scrollHeight > 190; i++) { px *= 0.94; k.style.fontSize = px + "px"; }
    }
    el.style.display = "none";
  }
})();
window.setzeZeit(0);
</script></body></html>`;
}

/* Ueberschrift ausgewogen umbrechen: erst moeglichst wenige Zeilen, dann
   moeglichst gleich lange. Ein einzelnes „vor?" auf der zweiten Zeile sieht
   aus wie ein Versehen. */
export function zeilen(titel, maxZeilen = 3, maxLaenge = 24) {
  const w = String(titel || "").split(/\s+/).filter(Boolean);
  if (!w.length) return [""];
  let beste = null;
  const teilen = (fertig, rest) => {
    if (!rest.length) {
      const wert = fertig.length * 1000 + Math.max(...fertig.map((z) => z.length));
      if (fertig.every((z) => z.length <= maxLaenge) && (!beste || wert < beste.wert)) beste = { zeilen: [...fertig], wert };
      return;
    }
    for (let n = 1; n <= rest.length; n++) {
      const zeile = rest.slice(0, n).join(" ");
      if (zeile.length > maxLaenge && n > 1) break;
      if (fertig.length + 1 > maxZeilen) break;
      teilen([...fertig, zeile], rest.slice(n));
    }
  };
  teilen([], w);
  return beste ? beste.zeilen : [String(titel)];
}

/* Eine Schrift genuegt: Inter traegt alle Gewichte in einer Datei. */
function schriftCss() {
  const datei = new URL("../fonts/Inter.ttf", import.meta.url).pathname;
  return `@font-face{font-family:"Inter";src:url("file://${datei}") format("truetype");font-weight:100 900;font-display:block}`;
}
