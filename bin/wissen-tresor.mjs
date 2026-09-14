#!/usr/bin/env node
/* ==========================================================================
   Wissensbasis ein- und auspacken.

   node bin/wissen-tresor.mjs packen <quellordner>   – *.txt -> daten/wissen/*.txt.enc
   node bin/wissen-tresor.mjs pruefen               – zeigt, was im Tresor liegt
   node bin/wissen-tresor.mjs auspacken <zielordner> – zurück in Klartext

   Der Schlüssel kommt aus IG_WISSEN_KEY. Er steht nirgends im Repo und wird
   auch hier nicht ausgegeben – gezeigt wird nur ein Fingerabdruck, damit man
   prüfen kann, ob lokal und in den GitHub-Secrets derselbe Schlüssel liegt,
   ohne ihn dafür nebeneinanderzulegen.

   Warum überhaupt ein Tresor: Das Repo ist öffentlich, das Handbuch nicht.
   Verschlüsselt kann der Volltext im selben Repo liegen wie der Code, ohne
   dass ihn jemand lesen kann, der die Seite im Browser öffnet.

   Neuen Schlüssel erzeugen (32 Byte, base64):
   node -e 'console.log(require("crypto").randomBytes(32).toString("base64"))'
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { WISSEN_ORDNER, wissenVerschluesseln, wissenEntschluesseln, wissenIndex, wissenLeeren } from "../src/wissen.mjs";
import { CONFIG } from "../src/config.mjs";

const [, , befehl, ordner] = process.argv;
const geheim = CONFIG.wissen.schluessel;

/* Fingerabdruck statt Schlüssel: sagt "derselbe" oder "ein anderer", ohne
   den Schlüssel selbst irgendwo hinzuschreiben. */
const abdruck = (s) => (s ? crypto.createHash("sha256").update(String(s)).digest("hex").slice(0, 12) : "–");

if (!geheim && befehl !== "pruefen") {
  console.error("IG_WISSEN_KEY fehlt. Ohne Schlüssel lässt sich der Tresor weder füllen noch öffnen.");
  process.exit(1);
}

function packen(quelle) {
  if (!quelle || !fs.existsSync(quelle)) { console.error(`Quellordner fehlt: ${quelle}`); process.exit(1); }
  fs.mkdirSync(WISSEN_ORDNER, { recursive: true });
  const dateien = fs.readdirSync(quelle).filter((d) => d.endsWith(".txt")).sort();
  if (!dateien.length) { console.error(`Keine .txt in ${quelle}`); process.exit(1); }
  let roh = 0, ver = 0;
  for (const datei of dateien) {
    const text = fs.readFileSync(path.join(quelle, datei), "utf8");
    const tresor = wissenVerschluesseln(text, geheim);
    fs.writeFileSync(path.join(WISSEN_ORDNER, `${datei}.enc`), tresor);
    roh += text.length; ver += tresor.length;
    console.log(`  ${datei} → ${datei}.enc  (${text.length} → ${tresor.length} Byte)`);
  }
  console.log(`\n${dateien.length} Bände im Tresor, ${(ver / 1024 / 1024).toFixed(2)} MB. Schlüssel-Fingerabdruck ${abdruck(geheim)}`);
  console.log(`Klartext gesamt: ${(roh / 1024 / 1024).toFixed(2)} MB – der liegt NICHT im Repo.`);
}

function pruefen() {
  console.log(`Schlüssel-Fingerabdruck: ${abdruck(geheim)}`);
  if (!fs.existsSync(WISSEN_ORDNER)) { console.log("Kein Tresor vorhanden."); return; }
  const dateien = fs.readdirSync(WISSEN_ORDNER).filter((d) => /\.txt(\.enc)?$/.test(d));
  console.log(`${dateien.length} Datei(en) in daten/wissen.`);
  if (!geheim) { console.log("Ohne IG_WISSEN_KEY bleibt der Inhalt zu."); return; }
  wissenLeeren();
  const index = wissenIndex({ geheim });
  console.log(`${index.length} Kapitel lesbar:`);
  for (const b of [...new Set(index.map((k) => k.band))].sort((a, c) => a - c)) {
    const k = index.filter((x) => x.band === b);
    console.log(`  Band ${b}: ${String(k.length).padStart(3)} Kapitel, ${String(k.reduce((a, x) => a + x.text.length, 0)).padStart(7)} Zeichen – ${k[0]?.bandTitel || ""}`);
  }
}

function auspacken(ziel) {
  if (!ziel) { console.error("Zielordner fehlt."); process.exit(1); }
  fs.mkdirSync(ziel, { recursive: true });
  for (const datei of fs.readdirSync(WISSEN_ORDNER).filter((d) => d.endsWith(".enc"))) {
    const text = wissenEntschluesseln(fs.readFileSync(path.join(WISSEN_ORDNER, datei)), geheim);
    const name = datei.replace(/\.enc$/, "");
    fs.writeFileSync(path.join(ziel, name), text);
    console.log(`  ${datei} → ${path.join(ziel, name)} (${text.length} Zeichen)`);
  }
}

if (befehl === "packen") packen(ordner);
else if (befehl === "pruefen") pruefen();
else if (befehl === "auspacken") auspacken(ordner);
else {
  console.log("Aufruf: node bin/wissen-tresor.mjs packen|pruefen|auspacken [ordner]");
  process.exit(1);
}
