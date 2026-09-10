/* ==========================================================================
   Bild-Hosting und Zustand im Zweig „instagram-assets“ dieses Repositories.

   Instagram lädt Bilder nur von öffentlichen URLs. Jedes gerenderte JPEG wird
   in den Asset-Zweig committet und über raw.githubusercontent.com ausgeliefert.
   Im selben Zweig liegen Ledger, Tagespläne und der Token-Tresor (state/).
   ========================================================================== */

import { execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { CONFIG } from "./config.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(hier, "../..");
const schlafen = (ms) => new Promise((r) => setTimeout(r, ms));

function git(args, cwd = REPO, opt = {}) {
  return execFileSync("git", args, { cwd, encoding: "utf8", stdio: ["ignore", "pipe", opt.stderr || "pipe"], ...opt }).trim();
}

/* Remote-URL mit Zugangsdaten: Im Workflow trägt der frische Klon des
   Asset-Zweigs nicht die Anmeldung des Haupt-Checkouts; GITHUB_TOKEN reicht. */
function remoteMitToken(url) {
  const token = process.env.GITHUB_TOKEN;
  if (!token) return url;
  const { owner, repo } = remoteInfo();
  return `https://x-access-token:${token}@github.com/${owner}/${repo}.git`;
}

/* owner/repo aus dem Remote ableiten (https oder ssh). */
export function remoteInfo() {
  const url = git(["remote", "get-url", "origin"]);
  const m = url.match(/github\.com[:/]([^/]+)\/([^/.]+)(?:\.git)?/);
  if (!m) throw new Error(`Kein GitHub-Remote erkannt: ${url}`);
  return { owner: m[1], repo: m[2] };
}

export class Hosting {
  constructor(opt = {}) {
    this.zweig = opt.zweig || CONFIG.hosting.zweig;
    this.dir = path.resolve(REPO, opt.verzeichnis || CONFIG.hosting.verzeichnis);
    this.basisUrl = opt.basisUrl || CONFIG.hosting.basisUrl;
    this.pushen = opt.pushen ?? (process.env.IG_NO_PUSH !== "true");
  }

  get stateDir() { return path.join(this.dir, "state"); }

  /* Asset-Zweig auschecken (oder als leeren Orphan-Zweig anlegen). */
  vorbereiten() {
    if (!this.basisUrl) {
      const { owner, repo } = remoteInfo();
      this.basisUrl = `https://raw.githubusercontent.com/${owner}/${repo}/${this.zweig}`;
    }
    if (fs.existsSync(path.join(this.dir, ".git"))) {
      try { git(["remote", "set-url", "origin", remoteMitToken(git(["remote", "get-url", "origin"], this.dir))], this.dir); } catch { /* egal */ }
      try { git(["pull", "--rebase", "--quiet", "origin", this.zweig], this.dir); } catch { /* offline oder neuer Zweig */ }
      return this;
    }
    fs.mkdirSync(path.dirname(this.dir), { recursive: true });
    const remote = remoteMitToken(git(["remote", "get-url", "origin"]));
    let existiert = false;
    try { existiert = git(["ls-remote", "--heads", remote, this.zweig]).length > 0; } catch { existiert = false; }
    if (existiert) {
      git(["clone", "--quiet", "--branch", this.zweig, "--single-branch", "--depth", "50", remote, this.dir]);
    } else {
      fs.mkdirSync(this.dir, { recursive: true });
      git(["init", "--quiet", "-b", this.zweig], this.dir);
      git(["remote", "add", "origin", remote], this.dir);
      fs.writeFileSync(path.join(this.dir, "README.md"), `# Instagram-Assets\n\nAutomatisch erzeugte Bilder und Zustand des Instagram-Bots (siehe social/). Nicht von Hand bearbeiten.\n`);
      git(["add", "."], this.dir);
      this.commit("Asset-Zweig angelegt");
    }
    git(["config", "user.name", process.env.GIT_AUTHOR_NAME || "instagram-bot"], this.dir);
    git(["config", "user.email", process.env.GIT_AUTHOR_EMAIL || "instagram-bot@users.noreply.github.com"], this.dir);
    fs.mkdirSync(this.stateDir, { recursive: true });
    return this;
  }

  commit(nachricht) {
    git(["config", "user.name", process.env.GIT_AUTHOR_NAME || "instagram-bot"], this.dir);
    git(["config", "user.email", process.env.GIT_AUTHOR_EMAIL || "instagram-bot@users.noreply.github.com"], this.dir);
    git(["add", "-A"], this.dir);
    try { git(["commit", "--quiet", "-m", nachricht], this.dir); return true; } catch { return false; }
  }

  async push() {
    if (!this.pushen) return false;
    for (let i = 1; i <= 4; i++) {
      try { git(["push", "--quiet", "-u", "origin", this.zweig], this.dir); return true; }
      catch (e) {
        try { git(["pull", "--rebase", "--quiet", "origin", this.zweig], this.dir); } catch { /* ignorieren */ }
        if (i === 4) throw e;
        await schlafen(1000 * 2 ** i);
      }
    }
    return false;
  }

  /* Datei in den Zweig legen; Rückgabe: öffentliche URL. */
  ablegen(quelle, relativ) {
    const ziel = path.join(this.dir, relativ);
    fs.mkdirSync(path.dirname(ziel), { recursive: true });
    fs.copyFileSync(quelle, ziel);
    return `${this.basisUrl}/${relativ.split(path.sep).map(encodeURIComponent).join("/")}`;
  }

  /* Bilder committen, pushen und warten, bis sie öffentlich abrufbar sind. */
  /* Jede Veröffentlichung bekommt eine eigene Kennung im Dateinamen – so kann
     der CDN-Cache von raw.githubusercontent.com nie ein älteres Bild liefern. */
  async veroeffentlichen(dateien, datum, nachricht) {
    const kennung = Date.now().toString(36);
    const urls = dateien.map((d) => { const { name, ext } = path.parse(d); return this.ablegen(d, path.join("bilder", datum, `${name}-${kennung}${ext}`)); });
    this.commit(nachricht || `Bilder ${datum}`);
    await this.push();
    if (this.pushen) for (const url of urls) await this.erreichbar(url);
    return urls;
  }

  async erreichbar(url, { maxSekunden = 90 } = {}) {
    const start = Date.now();
    let letzter = "";
    while (Date.now() - start < maxSekunden * 1000) {
      try {
        const res = await fetch(url, { method: "HEAD", cache: "no-store" });
        if (res.ok && /(image\/jpeg|video\/mp4|application\/octet-stream)/.test(res.headers.get("content-type") || "")) return true;
        letzter = `${res.status} ${res.headers.get("content-type")}`;
      } catch (e) { letzter = e.message; }
      await schlafen(5000);
    }
    throw new Error(`Bild nicht öffentlich erreichbar: ${url} (${letzter})`);
  }

  /* Bilder älter als N Tage entfernen – der Zweig bleibt klein. */
  aufraeumen(tage = 21) {
    const dir = path.join(this.dir, "bilder");
    if (!fs.existsSync(dir)) return 0;
    const grenze = new Date(Date.now() - tage * 86400000).toISOString().slice(0, 10);
    let n = 0;
    for (const d of fs.readdirSync(dir)) if (/^\d{4}-\d{2}-\d{2}$/.test(d) && d < grenze) { fs.rmSync(path.join(dir, d), { recursive: true, force: true }); n++; }
    return n;
  }

  jsonLesen(name, fallback) {
    const p = path.join(this.stateDir, name);
    return fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, "utf8")) : fallback;
  }

  jsonSchreiben(name, daten) {
    const p = path.join(this.stateDir, name);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, JSON.stringify(daten, null, 2));
  }
}
