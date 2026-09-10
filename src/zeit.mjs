/* Zeit-Helfer: alles in Europe/Berlin, unabhängig von der Zeitzone des Runners. */
import { CONFIG } from "./config.mjs";

const ZONE = CONFIG.marke.zeitzone;

function teile(date) {
  const f = new Intl.DateTimeFormat("de-DE", {
    timeZone: ZONE, hour12: false,
    year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", weekday: "short",
  });
  const p = Object.fromEntries(f.formatToParts(date).map((x) => [x.type, x.value]));
  const wochentagIndex = { So: 0, Mo: 1, Di: 2, Mi: 3, Do: 4, Fr: 5, Sa: 6 }[p.weekday.replace(".", "")];
  return { jahr: p.year, monat: p.month, tag: p.day, stunde: Number(p.hour === "24" ? 0 : p.hour), minute: Number(p.minute), wochentag: wochentagIndex };
}

export function heuteIso(date = new Date()) {
  const t = teile(date);
  return `${t.jahr}-${t.monat}-${t.tag}`;
}

export function lokaleMinuten(date = new Date()) {
  const t = teile(date);
  return t.stunde * 60 + t.minute;
}

export function wochentag(date = new Date()) {
  return teile(date).wochentag;
}

export function minutenVon(hhmm) {
  const [h, m] = hhmm.split(":").map(Number);
  return h * 60 + m;
}

export function hhmm(minuten) {
  return `${String(Math.floor(minuten / 60)).padStart(2, "0")}:${String(minuten % 60).padStart(2, "0")}`;
}

export function tageBis(isoDatum, date = new Date()) {
  const a = new Date(`${heuteIso(date)}T00:00:00Z`);
  const b = new Date(`${isoDatum}T00:00:00Z`);
  return Math.round((b - a) / 86400000);
}

export function datumLesbar(iso) {
  const [j, m, t] = iso.split("-");
  return `${t}.${m}.${j}`;
}
