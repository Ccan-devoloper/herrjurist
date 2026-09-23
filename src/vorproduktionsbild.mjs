import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const PROMPT_VERSION = "herrjurist-charakter-cover-v1";

const sha256 = (puffer) => crypto.createHash("sha256").update(puffer).digest("hex");

function sortieren(wert) {
  if (Array.isArray(wert)) return wert.map(sortieren);
  if (!wert || typeof wert !== "object") return wert;
  return Object.fromEntries(Object.keys(wert).sort().map((k) => [k, sortieren(wert[k])]));
}

function visuellerKern(inhalt = {}) {
  const titel = inhalt?.folien?.find?.((f) => f.art === "titel") || inhalt?.folien?.[0] || {};
  const szene = inhalt?.szenen?.[0] || {};
  const felder = [
    "slug", "themaId", "kurztitel", "fachLabel", "fach", "klausur", "format",
    "titel", "unter", "text", "sprecher", "norm", "bildSzene", "bildSzeneAlt",
    "coverText", "coverRegie", "coverRegieManuell",
    "coverCharaktere", "coverCharaktereManuell", "coverCharaktereQuelle",
  ];
  const pick = (obj) => Object.fromEntries(
    felder.filter((k) => obj?.[k] != null).map((k) => [k, obj[k]]),
  );
  return { beitrag: pick(inhalt), titel: pick(titel), ersteSzene: pick(szene) };
}

export function vorproduktionsBildInputHash(inhalt, { modell = "", guete = "" } = {}) {
  return sha256(Buffer.from(JSON.stringify(sortieren({
    promptVersion: PROMPT_VERSION, modell, guete, visuell: visuellerKern(inhalt),
  })), "utf8"));
}

function metaPfad(basisDir, datum, slot) {
  return path.join(basisDir, "vorproduktion", datum, "rohbilder", `${slot}.json`);
}

export function pngPufferAusTreffer(treffer) {
  const m = String(treffer?.bild || "").match(/^data:image\/png;base64,([A-Za-z0-9+/=]+)$/);
  if (!m) throw new Error("Persistierbares Charakterbild ist keine PNG-data-URI.");
  const puffer = Buffer.from(m[1], "base64");
  if (puffer.subarray(0, 8).toString("hex") !== "89504e470d0a1a0a") {
    throw new Error("Persistierbares Charakterbild hat keine gueltige PNG-Signatur.");
  }
  return puffer;
}

export function rohbildLaden({ basisDir, datum, slot, inhalt, modell = "", guete = "" }) {
  const mp = metaPfad(basisDir, datum, slot);
  if (!fs.existsSync(mp)) return null;
  const meta = JSON.parse(fs.readFileSync(mp, "utf8"));
  const erwartet = vorproduktionsBildInputHash(inhalt, { modell, guete });
  if (meta.inputHash !== erwartet || meta.modell !== modell || meta.guete !== guete) return null;

  const rel = String(meta.gitPfad || "");
  const bildPfad = path.join(basisDir, ...rel.split("/"));
  if (!rel || !fs.existsSync(bildPfad)) {
    throw new Error(`Persistiertes Rohbild ${datum} ${slot} fehlt. Keine automatische Neugenerierung.`);
  }
  const puffer = fs.readFileSync(bildPfad);
  if (sha256(puffer) !== meta.sha256) {
    throw new Error(`Persistiertes Rohbild ${datum} ${slot} hat falschen SHA-256. Keine automatische Neugenerierung.`);
  }
  return {
    bild: `data:image/png;base64,${puffer.toString("base64")}`,
    quelle: null, seite: null, frei: true,
    breite: meta.breite || null, hoehe: meta.hoehe || null,
    typ: "charakter", charaktere: meta.charaktere || [],
    prompt: meta.prompt || null, coverHinweisPlan: meta.coverHinweisPlan || null,
    kostenUsd: 0, urspruenglicheKostenUsd: Number(meta.kostenUsd || 0),
    wiederverwendet: true, rohbild: meta,
  };
}

export function rohbildSpeichern({
  basisDir, basisUrl, datum, slot, inhalt, treffer, modell = "", guete = "",
}) {
  const puffer = pngPufferAusTreffer(treffer);
  const bildSha = sha256(puffer);
  const gitPfad = path.posix.join(
    "vorproduktion", datum, "rohbilder", `${slot}-${bildSha.slice(0, 16)}.png`,
  );
  const bildPfad = path.join(basisDir, ...gitPfad.split("/"));
  fs.mkdirSync(path.dirname(bildPfad), { recursive: true });
  if (fs.existsSync(bildPfad) && sha256(fs.readFileSync(bildPfad)) !== bildSha) {
    throw new Error(`Rohbild-Ziel ${gitPfad} existiert mit anderem Inhalt.`);
  }
  if (!fs.existsSync(bildPfad)) fs.writeFileSync(bildPfad, puffer);

  const rawUrl = basisUrl
    ? `${String(basisUrl).replace(/\/$/, "")}/${gitPfad.split("/").map(encodeURIComponent).join("/")}`
    : null;
  const meta = {
    version: 1, datum, slot,
    inputHash: vorproduktionsBildInputHash(inhalt, { modell, guete }),
    sha256: bildSha, gitPfad, rawUrl, modell, guete,
    charaktere: treffer?.charaktere || [],
    breite: treffer?.breite || null, hoehe: treffer?.hoehe || null,
    prompt: treffer?.prompt || null,
    coverHinweisPlan: treffer?.coverHinweisPlan || null,
    kostenUsd: Number(treffer?.kostenUsd || 0),
    erzeugtAm: new Date().toISOString(),
  };
  const mp = metaPfad(basisDir, datum, slot);
  fs.mkdirSync(path.dirname(mp), { recursive: true });
  fs.writeFileSync(mp, JSON.stringify(meta, null, 2) + "\n");
  return { meta, bildPfad, metaPfad: mp };
}
