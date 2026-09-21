/* global FormData, Blob */
/**
 * Wiederkehrende Herr-Jurist-Charaktere als thematische Cover- und Reel-Szenen.
 *
 * Anders als die fruehere Stockfoto-/Einzelmotiv-Pipeline entstehen hier keine
 * austauschbaren Gegenstaende. Je nach Inhalt werden eine, zwei oder mehrere
 * feste Figuren aus ihren Referenzbildern in eine neue, zum juristischen Thema
 * passende Handlung gesetzt. Requisiten sind kein Muss: Entscheidend ist, dass
 * die Szene den juristischen Gedanken sofort sichtbar macht.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execFileSync } from "node:child_process";
import { CONFIG } from "./config.mjs";
import { ffmpegPfad } from "./stimme.mjs";
import { bildAufruf, openaiAufruf, openaiBildEditSenden } from "./anbieter.mjs";
import { alphaProfil, FESTIGKEIT_MIN, zuschneiden, bestickern, masse, randkontakt, randVerdacht, freistellen } from "./freistellen.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const basis = path.resolve(hier, "../assets/charaktere");

export const CHARAKTERE = Object.freeze({
  rex: {
    id: "rex", name: "Rex Rohrbruch", datei: "rex-rohrbruch.jpg.b64",
    kurz: "lanky light-skinned anxious male portal mechanic with messy brown hair, patched blue-grey work suit, brown boots, tool backpack and traces of green portal fluid",
  },
  zylla: {
    id: "zylla", name: "Zylla Glitch", datei: "zylla-glitch.jpg.b64",
    kurz: "slim green-skinned alien woman with magenta swept hair, two antennae, oversized lavender iridescent jacket, black top, black skinny trousers and pink-white sneakers",
  },
  form7: {
    id: "form7", name: "FORM-7", datei: "form-7.jpg.b64",
    kurz: "floating pale-blue round-headed bureaucratic drone with sleepy half-lidded eyes, dark side panels, a small gold antenna-crown, white-gold uniform torso, clipboard and tiny side pods",
  },
  brakk: {
    id: "brakk", name: "Brakk Quarzfaust", datei: "brakk-quarzfaust.jpg.b64",
    kurz: "very muscular tan miner with a square jaw, purple-blue crystal growths on shoulders and head, miner headlamp, brown bib overalls, heavy grey boots and gloves",
  },
  flux: {
    id: "flux", name: "Prof. Wurmfried Flux", datei: "prof-wurmfried-flux.jpg.b64",
    kurz: "tall pink segmented worm-like professor with large round glasses, sparse hair, cheerful face, white-gold academic tunic, pointer and round hover base",
  },
  mara: {
    id: "mara", name: "Mara Sternpfad", datei: "mara-sternpfad.jpg.b64",
    kurz: "older light-skinned woman with grey hair in a messy bun, yellow cap, cigarette, orange vest over black top, olive cargo trousers and a large green expedition backpack with antenna dish and many pouches",
  },
});

export function charakterBildAktiv() {
  return Boolean(CONFIG.bilder?.charaktere?.aktiv && CONFIG.bilder?.ki?.key);
}

function zielText(ziel = {}) {
  const titel = ziel?.folien?.find?.((f) => f.art === "titel")?.titel || "";
  return [
    ziel.kurztitel, ziel.fachLabel, ziel.fach, ziel.format, titel,
    ziel.titel, ziel.unter, ziel.text, ziel.sprecher, ziel.norm,
    ziel.bildSzene, ziel.bildSzeneAlt, ziel.coverText,
    ...(Array.isArray(ziel.coverCharaktere) ? ziel.coverCharaktere : []),
  ].filter(Boolean).join(" · ");
}

const REGELN = [
  /* Die Reihenfolge ist Regie: konkrete Rechtsbilder vor generischen
     Methodik-Woertern. Sie reproduziert bewusst die starken Paarungen der
     freigegebenen Referenzcover und sorgt zugleich dafuer, dass alle sechs
     Figuren echte Rollen im Feed haben. */
  { re: /wochenrueckblick|wochenrückblick|themen der woche|wiederholung der woche/i, ids: ["zylla", "form7"] },
  { re: /142|unfall|unfallort|verkehrsunfall|unerlaub.*entfern|flucht/i, ids: ["rex", "mara"] },
  { re: /versuch|unmittelbar|letzten handgriff|§\s*22\s*stgb/i, ids: ["rex", "mara"] },
  { re: /besitz|eigentum|§\s*985|sachenrecht|gutglaub|übereign|uebereign/i, ids: ["brakk", "form7"] },
  { re: /anfecht|irrtum|kausal|§\s*119/i, ids: ["form7", "rex"] },
  { re: /angebot|annahme|schaufenster|invitatio|vertragsschluss/i, ids: ["zylla", "form7"] },
  { re: /kuendig|kündig|arbeitsrecht|zugang.*frist|fristbeginn/i, ids: ["zylla", "flux"] },
  { re: /zpo|zivilprozess|zwangsvoll|vollstreckungsklausel|zulässigkeit.*begründet|zulaessigkeit.*begruendet/i, ids: ["form7", "flux"] },
  { re: /vollzieh|aufschieb|80\s*(abs|ii|2|5)|verwaltungsprozess|vwgo|bescheid/i, ids: ["mara", "form7"] },
  { re: /280|pflichtverletz|leistungsstör|leistungsstoer|schadensersatz|schuldrecht/i, ids: ["rex", "flux"] },
  { re: /mittaeter|mittäter|mehrpersonen|dreiperson|vertretung/i, ids: ["brakk", "zylla", "form7"] },
  { re: /definition|begriff|dogmatik/i, ids: ["flux"] },
  { re: /mindset|blackout|zeitdruck|perfektion|nervos/i, ids: ["mara"] },
  { re: /streitstand|ansichten|ergebnis vergleichen|methodik|anspruchsgrundlage|aufbau/i, ids: ["form7", "flux"] },
  { re: /strafrecht bt|diebstahl|raub|betrug|körperverletz|koerperverletz|gewalt/i, ids: ["brakk", "rex"] },
  { re: /erbe|testament|famil|nachlass|erbrecht/i, ids: ["mara", "flux"] },
  { re: /mangel|werk|repar|bau|kauf|liefer/i, ids: ["rex", "brakk"] },
];

function idsAusManuellerRegie(ziel = {}) {
  /* Nur eine AUSDRUECKLICHE menschliche/Chat-Freigabe darf die semantische
     Charakterregie ueberschreiben. Das alte Feld coverCharaktere kam auch aus
     dem Claude-Fallback und hat die guten Themenregeln deshalb ungewollt
     ausgehebelt. Alte automatische Werte werden ab jetzt ignoriert. */
  const titel = ziel?.folien?.find?.((f) => f.art === "titel") || {};
  const quelle = String(ziel.coverCharaktereQuelle || titel.coverCharaktereQuelle || "").toLowerCase();
  const roh = ziel.coverCharaktereManuell || titel.coverCharaktereManuell
    || (["chat", "manuell", "human"].includes(quelle) ? (ziel.coverCharaktere || titel.coverCharaktere) : null);
  if (!Array.isArray(roh)) return [];
  return [...new Set(roh.map((x) => String(x || "").toLowerCase()).filter((id) => CHARAKTERE[id]))].slice(0, 6);
}

function fallbackCharaktere(text) {
  /* Auch im generischen Fallback soll FORM-7 nicht jeden zweiten Beitrag
     uebernehmen. Eine kleine deterministische Streuung ueber den Inhalt sorgt
     fuer Cast-Balance, ohne Zufall und ohne externes Modell. */
  const paare = [
    ["rex", "flux"],
    ["zylla", "mara"],
    ["brakk", "flux"],
    ["zylla", "rex"],
  ];
  let h = 0;
  for (const ch of String(text || "")) h = ((h * 31) + ch.charCodeAt(0)) >>> 0;
  return paare[h % paare.length];
}

export function charaktereFuer(ziel = {}) {
  const manuell = idsAusManuellerRegie(ziel);
  if (manuell.length) return manuell.map((id) => CHARAKTERE[id]);
  const text = zielText(ziel);
  for (const regel of REGELN) if (regel.re.test(text)) return regel.ids.map((id) => CHARAKTERE[id]);
  return fallbackCharaktere(text).map((id) => CHARAKTERE[id]);
}

function themenKontext(ziel = {}) {
  const titel = ziel?.folien?.find?.((f) => f.art === "titel")?.titel || "";
  return [
    ziel.kurztitel, ziel.fachLabel, ziel.fach, ziel.format, titel,
    ziel.titel, ziel.unter, ziel.text, ziel.sprecher, ziel.norm, ziel.coverText,
  ].filter(Boolean).join(" · ").slice(0, 900);
}

function handlungFuer(ziel, chars) {
  const text = zielText(ziel);
  const namen = chars.map((x) => x.name);
  const a = namen[0];
  const b = namen[1];
  const c = namen[2];

  /* Jede Regie nennt ausschliesslich Figuren, die auch wirklich als Referenz
     mitgeschickt werden. Kein "another character", kein Polizist, Clerk,
     Detective oder sonstige Platzhalterrolle: Genau diese Woerter haben die
     Fremdcharaktere in den ersten Trockenlaeufen erzeugt. */
  const solo = (satz) => satz.replaceAll("{A}", a);
  const duo = (satz, fallback) => b
    ? satz.replaceAll("{A}", a).replaceAll("{B}", b)
    : solo(fallback);
  const trio = (satz, fallback) => c
    ? satz.replaceAll("{A}", a).replaceAll("{B}", b).replaceAll("{C}", c)
    : duo(fallback, fallback);

  if (/kuendig|kündig|arbeitsrecht|zugang.*frist|fristbeginn/i.test(text)) {
    return duo(
      "{A} calmly hands {B} one sealed blank envelope while a simple blank calendar beside them marks the timing; {B} reacts to receiving it.",
      "{A} holds one sealed blank envelope beside a simple blank calendar and clearly points to the moment of receipt."
    );
  }
  if (/142|unfall|unfallort|unerlaub.*entfern|verkehrsunfall/i.test(text)) {
    return duo(
      "{A} stands beside a lightly damaged small red car and starts to step away; {B} firmly blocks the path and points back to the accident scene.",
      "{A} stands beside a lightly damaged small red car, pauses mid-step and points back to the accident scene."
    );
  }
  if (/versuch|unmittelbar|letzten handgriff|§\s*22\s*stgb/i.test(text)) {
    return duo(
      "{A} reaches toward a large glowing green machine button just before pressing it; {B} sharply stops {A}'s hand at the decisive last moment.",
      "{A} freezes with one hand a few centimetres above a large glowing green machine button, visibly at the decisive last moment."
    );
  }
  if (/besitz|eigentum|985|sachenrecht/i.test(text)) {
    return duo(
      "{A} carries a heavy wooden crate and a house key while {B} points to a separate blank ownership document with a seal, visibly separating possession from ownership.",
      "{A} holds a house key in one hand and a separate blank ownership document with a seal in the other, clearly comparing the two."
    );
  }
  if (/anfecht|irrtum|kausal|119/i.test(text)) {
    return duo(
      "{A} presents a clean two-step clipboard with only abstract check marks while {B} compares two visibly different glowing devices and notices the mistake.",
      "{A} compares two visibly different objects, notices the mistake, and points from the first object to the resulting decision."
    );
  }
  if (/angebot|annahme|schaufenster|invitatio|vertragsschluss/i.test(text)) {
    return duo(
      "{A} gestures toward one displayed product behind a small glass showcase while {B} holds a blank clipboard and deliberately points out that no contract has been concluded yet.",
      "{A} studies one displayed product behind a small glass showcase while holding a blank contract folder closed."
    );
  }
  if (/zpo|zivilprozess|zwangsvoll|vollstreckungsklausel|zuläss|zulaess|begründet|begruendet/i.test(text)) {
    return duo(
      "{A} sorts two clearly separate blank case-file stacks in the correct order while {B} points first to the left stack and only then to the right stack.",
      "{A} sorts two clearly separate blank case-file stacks in a strict first-then-second order."
    );
  }
  if (/vollzieh|aufschieb|80\s*(abs|ii|2|5)|vwgo|bescheid/i.test(text)) {
    return duo(
      "{A} points at a barrier that is already moving while {B} studies one blank warning notice and reaches toward a separate pause control, checking the exception first.",
      "{A} studies one blank warning notice beside a moving barrier and clearly checks whether the process is already running before touching a pause control."
    );
  }
  if (/280|pflichtverletz|leistungsstör|leistungsstoer|schadensersatz|schuldrecht/i.test(text)) {
    return duo(
      "{A} inspects a broken device and traces the defect back through a short chain of three abstract checkpoints while {B} explains the order with a pointer.",
      "{A} inspects a broken device and traces the defect through three abstract checkpoints in a clear order."
    );
  }
  if (/streit|ansicht|ergebnis|vergleich|methodik/i.test(text)) {
    return duo(
      "{A} compares two blank solution sheets side by side and first checks whether their result symbols match; {B} waits with a pointer until that comparison is finished.",
      "{A} compares two blank solution sheets side by side before deciding whether an argument is needed."
    );
  }
  if (/frist|kalender|zugang/i.test(text)) {
    return duo(
      "{A} points at a simple blank calendar while {B} holds one sealed blank envelope, both focused on the exact moment of receipt.",
      "{A} holds one sealed blank envelope beside a simple blank calendar and points at the moment of receipt."
    );
  }
  if (/mittaeter|mittäter|mehrpersonen|dreiperson|vertretung/i.test(text)) {
    return trio(
      "{A}, {B} and {C} form one connected action around a single legal object: one acts, one observes the allocation of roles, and one checks a blank decision board.",
      "{A} and {B} act on opposite sides of one shared legal object while clearly showing two different roles."
    );
  }
  if (/definition|begriff|dogmatik/i.test(text)) {
    return solo("{A} teaches one precise concept with a pointer and a clean abstract diagram made only of shapes, arrows and check marks.");
  }
  if (/mindset|blackout|zeitdruck|perfektion|nervos/i.test(text)) {
    return solo("{A} calmly checks a compact blank exam checklist under visible time pressure, focused and unimpressed.");
  }

  if (chars.length >= 3) {
    return trio(
      "{A}, {B} and {C} form one coherent interaction around a single topic-relevant legal prop; every selected character has a clear role and nobody else is present.",
      "{A} and {B} interact around one topic-relevant legal prop and make the legal distinction visually obvious."
    );
  }
  if (chars.length === 2) {
    return duo(
      "{A} and {B} interact around one topic-relevant legal prop and make the legal distinction visually obvious through gesture and reaction.",
      "{A} demonstrates the legal distinction with one topic-relevant prop in a single readable pose."
    );
  }
  return solo("{A} demonstrates the legal idea with one topic-relevant prop in a single immediately readable pose.");
}

export function charakterPrompt(ziel = {}, chars = charaktereFuer(ziel), korrektur = "") {
  const referenzen = chars.map((ch, i) =>
    \`Reference image \${i + 1} is the ONLY canonical identity for \${ch.name}: \${ch.kurz}. Match that exact face/head shape, body proportions, skin/fur/material colours, outfit, accessories and silhouette.\`
  ).join(" ");
  const handlung = handlungFuer(ziel, chars);
  const kontext = themenKontext(ziel);
  const korrekturText = korrektur
    ? \`Quality-review correction for this redraw: \${String(korrektur).slice(0, 700)}\`
    : "";

  return [
    "Create a NEW premium 2D editorial sci-fi comedy illustration for the lower half of a 3:4 Instagram cover.",
    referenzen,
    \`Use EXACTLY \${chars.length} recurring character identity/identities: \${chars.map((x) => x.name).join(", ")}. No other human, humanoid, robot, creature, face, body, silhouette or duplicate of a selected character may appear.\`,
    "The supplied references define identity, not pose. Redraw those same identities in a new topic-specific action.",
    \`Scene direction: \${handlung}\`,
    \`Legal context for meaning only, NOT a request to add people or text: \${kontext}\`,
    korrekturText,
    "Composition: one coherent editorial-cartoon vignette, preferably wider than tall for two or more characters. Keep the visual centre low so the Herrjurist renderer can place a large title above it. Use the lower roughly 60 percent of the imagined 3:4 cover; do not build a background.",
    "Characters must interact rather than pose independently. Every selected character needs a clear job in the scene. Use only props that make the legal point instantly understandable; omit props that do not help.",
    "Show complete readable anatomy: full heads and faces, all essential hands/fingers, feet or hover bases, and every important prop. No fused hands, spare limbs, duplicated body parts, cropped heads or accidental amputations.",
    "Polished premium cartoon finish matching the references: confident clean ink outlines, controlled cel shading, subtle material highlights and texture, expressive faces, precise accessories, clean edges and consistent proportions. Do NOT simplify into flat clip-art and do NOT switch to 3D, photorealism, watercolor or sketch style.",
    "Absolutely no explanatory prose, letters, numbers, law citations, labels, logos, signatures or gibberish inside the generated illustration. Papers, screens, folders and signs must be blank or contain only simple abstract shapes/check marks. Herrjurist adds all readable text later.",
    "Transparent background only. No room, landscape, wall, decorative frame or colored sticker outline. A soft ground shadow directly under the selected characters or main prop is allowed.",
    "Fill the transparent image confidently: the complete vignette should occupy about 88 to 94 percent of the usable width or height while retaining a small clean safety margin around every body part and prop.",
  ].filter(Boolean).join(" ");
}

export function bildKostenUsd(antwort) {
  const u = antwort?.usage;
  if (!u) return null;
  const d = u.input_tokens_details || {};
  const od = u.output_tokens_details || {};
  const bildEin = Number(d.image_tokens || 0);
  const textEin = Number(d.text_tokens || Math.max(0, Number(u.input_tokens || 0) - bildEin));
  const bildAus = Number(od.image_tokens || u.output_tokens || 0);
  const textAus = Number(od.text_tokens || 0);
  const usd = bildEin * 8 / 1e6 + textEin * 5 / 1e6 + bildAus * 30 / 1e6 + textAus * 10 / 1e6;
  return Number(usd.toFixed(6));
}

function referenzNormalisieren(char) {
  const quelle = path.join(basis, char.datei);
  const b64 = fs.readFileSync(quelle, "utf8").trim();
  const roh = path.join(os.tmpdir(), `hj-ref-${char.id}-${process.pid}-${Date.now()}.jpg`);
  const norm = path.join(os.tmpdir(), `hj-ref-${char.id}-${process.pid}-${Date.now()}-384.jpg`);
  fs.writeFileSync(roh, Buffer.from(b64, "base64"));
  try {
    /* Die ersten Testreferenzen waren extrem kleine Thumbnails. GPT Image
       lehnt solche Dateien als ungueltige Bildeingabe ab. Vor jedem Upload
       werden sie daher in ein echtes 384x384-JPEG mit weissem Rand
       normalisiert; der Charakter selbst wird dabei nicht veraendert. */
    execFileSync(ffmpegPfad(), [
      "-y", "-loglevel", "error", "-i", roh,
      "-vf", "scale=336:336:force_original_aspect_ratio=decrease,pad=384:384:(ow-iw)/2:(oh-ih)/2:color=white",
      "-frames:v", "1", "-q:v", "3", norm,
    ]);
    return norm;
  } finally {
    fs.rmSync(roh, { force: true });
  }
}

const schlafen = (ms) => new Promise((r) => setTimeout(r, ms));
let letzterBildStart = 0;

async function ratenfensterWarten(ms = 13000) {
  const warten = Math.max(0, letzterBildStart + ms - Date.now());
  if (warten > 0) await schlafen(warten);
  letzterBildStart = Date.now();
}

async function editAufruf({ chars, prompt, quality, size, key, modell, zeitlimitMs }) {
  const refs = chars.map(referenzNormalisieren);
  try {
    for (let rateVersuch = 0; rateVersuch < 3; rateVersuch++) {
      const form = new FormData();
      form.append("model", modell);
      refs.forEach((datei, i) => {
        const bytes = fs.readFileSync(datei);
        form.append("image[]", new Blob([bytes], { type: "image/jpeg" }), `${chars[i].id}.jpg`);
      });
      form.append("prompt", prompt);
      form.append("quality", quality);
      form.append("size", size);
      form.append("background", "transparent");
      form.append("output_format", "png");
      try {
        /* Tier 1 erlaubt fuer GPT Image derzeit nur wenige Bilder pro Minute.
           Auch ein erfolgreicher Aufruf zaehlt; deshalb nicht erst nach 429
           bremsen, sondern jeden Bildstart bewusst auseinanderziehen. */
        await ratenfensterWarten(Number(CONFIG.bilder?.charaktere?.minAbstandMs || 13000));
        return await openaiBildEditSenden({ form, key, zeitlimitMs });
      } catch (fehler) {
        if (Number(fehler?.status) !== 429 || rateVersuch === 2) throw fehler;
        const retry = Number(fehler?.retryAfter || 0);
        const warten = Math.max(13000, Number.isFinite(retry) ? retry * 1000 : 0);
        console.warn(`  ! GPT-Image-Ratenlimit; ${Math.ceil(warten / 1000)} s Pause, dann gleicher Versuch erneut.`);
        await schlafen(warten);
      }
    }
    throw new Error("GPT-Image-Ratenlimit nach drei Versuchen");
  } finally {
    for (const p of refs) fs.rmSync(p, { force: true });
  }
}

function dateiAusAntwort(daten) {
  const b64 = daten?.data?.[0]?.b64_json;
  if (!b64) return null;
  const roh = path.join(os.tmpdir(), `charakter-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  fs.writeFileSync(roh, Buffer.from(b64, "base64"));
  return roh;
}

function qa(roh, randFarbe = null) {
  let arbeitsPfad = roh;
  let prof = alphaProfil(arbeitsPfad);
  const alphaTaugt = prof && prof.festigkeit >= FESTIGKEIT_MIN && prof.belegt >= 0.02;
  if (!alphaTaugt) {
    const frei = freistellen(arbeitsPfad, { randFarbe: null, schaerfePruefen: false });
    fs.rmSync(arbeitsPfad, { force: true });
    if (!frei?.pfad) return null;
    arbeitsPfad = frei.pfad;
    prof = alphaProfil(arbeitsPfad);
  }
  if (!prof || prof.festigkeit < FESTIGKEIT_MIN || prof.belegt < 0.02) {
    fs.rmSync(arbeitsPfad, { force: true });
    return null;
  }
  const randFehler = randVerdacht(randkontakt(arbeitsPfad));
  if (randFehler) {
    fs.rmSync(arbeitsPfad, { force: true });
    return null;
  }
  const geschnitten = zuschneiden(arbeitsPfad);
  if (geschnitten !== arbeitsPfad) fs.rmSync(arbeitsPfad, { force: true });
  const ohneRand = geschnitten.replace(/\.png$/, "-roh.png");
  fs.copyFileSync(geschnitten, ohneRand);
  const fertig = randFarbe ? bestickern(geschnitten, randFarbe) : geschnitten;
  const m = masse(fertig) || {};
  return { pfad: fertig, ohneRand, breite: m.breite || null, hoehe: m.hoehe || null };
}

/**
 * Erzeugt eine neue thematische Szene mit den festen Herr-Jurist-Charakteren.
 * Ein QA-Fehler bekommt genau einen zweiten Versuch in hoeherer Qualitaet.
 */
export async function charakterMotivZeichnen(ziel, { randFarbe = null, zweck = "bild", slot = null } = {}) {
  if (!charakterBildAktiv() || !ziel) return null;
  const cfg = CONFIG.bilder.charaktere;
  const chars = charaktereFuer(ziel).slice(0, 6);
  if (!chars.length || chars.some((c) => !fs.existsSync(path.join(basis, c.datei)))) return null;
  const prompt = charakterPrompt(ziel, chars);
  const versuche = [
    { quality: cfg.guete, reserve: cfg.reserveUsd },
    { quality: cfg.retryGuete, reserve: cfg.retryReserveUsd },
  ];
  for (let i = 0; i < versuche.length; i++) {
    const v = versuche[i];
    try {
      const daten = await bildAufruf({
        zweck,
        modell: cfg.modell,
        optional: true,
        preisUsd: v.reserve,
        zeitlimitMs: cfg.zeitlimitMs,
        slot: slot || ziel?.slug || ziel?.themaId || ziel?.titel || "charakter",
        senden: () => editAufruf({
          chars, prompt, quality: v.quality, size: cfg.groesse,
          key: CONFIG.bilder.ki.key, modell: cfg.modell, zeitlimitMs: cfg.zeitlimitMs,
        }),
        kostenAusAntwort: bildKostenUsd,
      });
      const roh = dateiAusAntwort(daten);
      if (!roh) continue;
      const fertig = qa(roh, cfg.randAktiv ? randFarbe : null);
      if (!fertig) {
        console.warn(`  ! Charakterbild QA fehlgeschlagen (${chars.map((c) => c.name).join(" + ")}, Versuch ${i + 1})`);
        continue;
      }
      const kosten = bildKostenUsd(daten);
      console.log(`  → Charakterbild: ${chars.map((c) => c.name).join(" + ")} · ${v.quality}${kosten != null ? ` · ${kosten.toFixed(4)} $` : ""}`);
      return { ...fertig, charaktere: chars.map((c) => c.name), prompt, kostenUsd: kosten };
    } catch (e) {
      console.warn(`  ! Charakterbild Versuch ${i + 1} fehlgeschlagen: ${e.message.slice(0, 180)}`);
      /* Ein 4xx-Eingabefehler wird durch hoehere Qualitaet nicht besser.
         Nur ein inhaltlich/visuell misslungenes, aber technisch erzeugtes Bild
         bekommt den teureren High-Retry. */
      if (Number(e?.status) >= 400 && Number(e?.status) < 500 && Number(e?.status) !== 429) break;
    }
  }
  return null;
}
