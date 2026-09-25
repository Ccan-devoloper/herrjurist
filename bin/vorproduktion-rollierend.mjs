#!/usr/bin/env node
/**
 * Rollierende Vorproduktion: Aus den redaktionell fertigen Tagen im Repository
 * (vorproduktion/<datum>.json) werden nur die nächsten HORIZONT Tage in den
 * Asset-Zweig übernommen und gerendert. So bleibt der Asset-Zweig schlank,
 * obwohl ein ganzes Jahr vorgeschrieben ist.
 *
 * Gibt die fälligen Daten als Zeile `tage=<d1> <d2> …` aus (für $GITHUB_OUTPUT).
 * Ein Tag ist fällig, wenn er im Asset-Zweig fehlt, noch nicht gerendert ist
 * oder sich die Repo-Fassung seit der Übernahme geändert hat. Tage, auf die
 * schon Charakter-Cover angewandt wurden, werden nie automatisch überschrieben.
 */
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { Hosting } from "../src/hosting.mjs";

const HORIZONT = Number(process.env.IG_VORPRODUKTION_HORIZONT || 14);
const MAX_JE_LAUF = Number(process.env.IG_VORPRODUKTION_MAX_JE_LAUF || 4);
const heute = process.env.IG_HEUTE || new Date().toISOString().slice(0, 10);
const plus = (d, n) => { const x = new Date(`${d}T12:00:00Z`); x.setUTCDate(x.getUTCDate() + n); return x.toISOString().slice(0, 10); };

const host = new Hosting({ pushen: false }).vorbereiten();
const repoDir = new URL("../vorproduktion/", import.meta.url);
const faellig = [];
for (let i = 1; i <= HORIZONT && faellig.length < MAX_JE_LAUF; i++) {
  const d = plus(heute, i);
  const quelle = new URL(`${d}.json`, repoDir);
  if (!fs.existsSync(quelle)) continue;
  const sha = crypto.createHash("sha256").update(fs.readFileSync(quelle)).digest("hex");
  const assetPfad = path.join(host.dir, "vorproduktion", `${d}.json`);
  if (!fs.existsSync(assetPfad)) { faellig.push(d); continue; }
  const asset = JSON.parse(fs.readFileSync(assetPfad, "utf8"));
  const gerendert = asset.renderVorschau?.status === "fertig" && fs.existsSync(path.join(host.dir, "vorproduktion", d, "fertig"));
  const gleich = asset.repoQuelle?.sha256 === sha;
  if (gerendert && (gleich || !asset.repoQuelle)) continue;
  if (asset.renderVorschau?.coverbilderAngewandt) {
    console.error(`${d}: Repo-Fassung geändert, aber Charakter-Cover sind schon angewandt – bitte gezielt nachziehen, kein automatisches Überschreiben.`);
    continue;
  }
  faellig.push(d);
}
console.error(`Heute ${heute}, Horizont ${HORIZONT} Tage: fällig ${faellig.join(", ") || "–"}`);
console.log(`tage=${faellig.join(" ")}`);
