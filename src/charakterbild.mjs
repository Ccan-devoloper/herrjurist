/**
 * Wiederkehrende Herr-Jurist-Charaktere als thematische Cover- und Reel-Szenen.
 *
 * Anders als die fruehere Stockfoto-/Einzelmotiv-Pipeline entstehen hier keine
 * austauschbaren Gegenstaende. Ein oder zwei feste Figuren werden aus ihren
 * Referenzbildern in eine neue, zum juristischen Thema passende Handlung
 * gesetzt. Die Referenzbilder bleiben gleich; Szene, Pose und Requisite sind
 * fuer jeden Beitrag neu.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { CONFIG } from "./config.mjs";
import { bildAufruf } from "./anbieter.mjs";
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
    ziel.bildSzene, ziel.bildSzeneAlt,
  ].filter(Boolean).join(" · ");
}

const REGELN = [
  { re: /kuendig|kündig|vertrag|angebot|annahme|willenserklaer|willenserklär|zugang|anfecht|irrtum|widerruf|ruecktritt|rücktritt/i, ids: ["zylla", "flux"] },
  { re: /schema|pruef|prüf|aufbau|streit|ansicht|vergleich|klausur|zulaess|zuläss|begruendet|begründet|frist|tenor|rechtsbehelf|verfahren/i, ids: ["form7", "flux"] },
  { re: /verwalt|vwgo|grundrecht|versammlung|polizei|behoerd|behörd|bescheid|vollzieh|oeffentlich|öffentlich/i, ids: ["mara", "form7"] },
  { re: /straf|tatbestand|versuch|diebstahl|raub|koerper|körper|gewalt|unfall|142|flucht|taeter|täter|mittaeter|mittäter/i, ids: ["brakk", "form7"] },
  { re: /besitz|eigentum|sache|mangel|schaden|werk|repar|bau|kauf|liefer/i, ids: ["rex", "brakk"] },
  { re: /erbe|testament|famil|nachlass|erbrecht/i, ids: ["mara", "flux"] },
  { re: /mindset|blackout|keine ahnung|lernen|wiederhol|zeitdruck|perfektion/i, ids: ["mara", "flux"] },
];

export function charaktereFuer(ziel = {}) {
  const text = zielText(ziel);
  for (const regel of REGELN) if (regel.re.test(text)) return regel.ids.map((id) => CHARAKTERE[id]);
  return [CHARAKTERE.form7, CHARAKTERE.flux];
}

function handlungFuer(ziel, chars) {
  const text = zielText(ziel);
  const a = chars[0]?.name || "the first character";
  const b = chars[1]?.name || "the second character";
  if (/kuendig|kündig/i.test(text)) return `${a} hands ${b} a blank termination letter; ${b} reacts surprised while ${a} clearly ends the relationship.`;
  if (/142|unfall|unfallort|24 stunden/i.test(text)) return `${a} turns away from a lightly damaged small car as if leaving the accident scene, while ${b} stops them and points back to the car.`;
  if (/streit|ansicht|ergebnis|vergleich/i.test(text)) return `${a} carefully compares two different blank solution sheets side by side while ${b} waits before starting an argument.`;
  if (/anfecht|irrtum/i.test(text)) return `${a} points out an obvious mistake on a blank contract while ${b} suddenly realizes the error.`;
  if (/angebot|annahme|vertragsschluss|schaufenster/i.test(text)) return `${a} presents a blank offer sheet while ${b} deliberately decides whether to accept it.`;
  if (/besitz|eigentum/i.test(text)) return `${a} holds a house key while ${b} points to a separate blank ownership document, making clear that possession and ownership are different.`;
  if (/versuch|letzten handgriff|unmittelbar/i.test(text)) return `${a} is just about to complete a decisive action while ${b} stops and examines the moment immediately before completion.`;
  if (/zulaess|zuläss|begruendet|begründet/i.test(text)) return `${a} checks a first procedural gate on a blank checklist before allowing ${b} to move to a clearly separate second stage.`;
  if (/vollzieh|aufschieb/i.test(text)) return `${a} checks whether a process is already running before ${b} reaches for a large pause switch.`;
  if (/frist|kalender|zugang/i.test(text)) return `${a} points at a blank calendar while ${b} holds a sealed blank envelope, both concentrating on the correct timing.`;
  if (/dieb|raub|straf|tatbestand/i.test(text)) return `${a} reenacts the concrete act with one simple prop while ${b} inspects the sequence step by step.`;
  const cue = String(ziel?.bildSzene || ziel?.titel || ziel?.kurztitel || "a legal exam problem").trim();
  return `${a} and ${b} act out this concrete exam situation: ${cue}. One character performs the action, the other visibly checks or reacts to it.`;
}

export function charakterPrompt(ziel = {}, chars = charaktereFuer(ziel)) {
  const referenzen = chars.map((c, i) =>
    `Reference image ${i + 1} is ${c.name}: ${c.kurz}. Preserve this exact character identity, face, body proportions, outfit, colours and distinctive features.`
  ).join(" ");
  const kontext = zielText(ziel).slice(0, 900);
  const handlung = handlungFuer(ziel, chars);
  return [
    "Create a NEW flat 2D sci-fi comedy cartoon scene using the supplied character reference image(s).",
    referenzen,
    "Do not copy the reference pose; redraw the same character(s) in a new pose and interaction.",
    `Scene action: ${handlung}`,
    `Legal-topic context, only to understand the visual meaning: ${kontext}`,
    "Use one coherent scene, not separate portraits. Show one or two characters only, plus at most one large simple prop that is essential to the action.",
    "Keep silhouettes readable at Instagram thumbnail size. Exaggerate gesture and facial reaction enough to communicate the action instantly.",
    "Absolutely no text, no letters, no words, no numbers, no paragraph symbols, no logos, no watermark. Documents and screens must be blank or use abstract non-letter lines only.",
    "No background and no scenery: transparent background, nothing behind the characters, no room, no floor, no landscape, no frame. A small prop may touch the characters if the action requires it.",
    "Leave clear transparent margin around the complete scene on all four sides. Do not crop heads, feet, hands, hair, crystals or props.",
    "Bold clean outlines, flat colours, subtle simple shading, consistent with the supplied original character artwork.",
  ].join(" ");
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

async function editAufruf({ chars, prompt, quality, size, key, modell, zeitlimitMs }) {
  const form = new FormData();
  form.append("model", modell);
  for (const c of chars) {
    const datei = path.join(basis, c.datei);
    const b64 = fs.readFileSync(datei, "utf8").trim();
    const bytes = Buffer.from(b64, "base64");
    form.append("image[]", new Blob([bytes], { type: "image/jpeg" }), c.datei.replace(/\.b64$/, ""));
  }
  form.append("prompt", prompt);
  form.append("quality", quality);
  form.append("size", size);
  form.append("background", "transparent");
  form.append("output_format", "png");
  const steuerung = new AbortController();
  const wecker = setTimeout(() => steuerung.abort(), zeitlimitMs);
  try {
    const r = await fetch("https://api.openai.com/v1/images/edits", {
      method: "POST",
      headers: { Authorization: `Bearer ${key}` },
      body: form,
      signal: steuerung.signal,
    });
    if (!r.ok) throw new Error(`OpenAI image edit ${r.status}: ${(await r.text().catch(() => "")).slice(0, 220)}`);
    return await r.json();
  } finally { clearTimeout(wecker); }
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
  const chars = charaktereFuer(ziel).slice(0, 2);
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
      const fertig = qa(roh, randFarbe);
      if (!fertig) {
        console.warn(`  ! Charakterbild QA fehlgeschlagen (${chars.map((c) => c.name).join(" + ")}, Versuch ${i + 1})`);
        continue;
      }
      const kosten = bildKostenUsd(daten);
      console.log(`  → Charakterbild: ${chars.map((c) => c.name).join(" + ")} · ${v.quality}${kosten != null ? ` · ${kosten.toFixed(4)} $` : ""}`);
      return { ...fertig, charaktere: chars.map((c) => c.name), prompt, kostenUsd: kosten };
    } catch (e) {
      console.warn(`  ! Charakterbild Versuch ${i + 1} fehlgeschlagen: ${e.message.slice(0, 180)}`);
    }
  }
  return null;
}
