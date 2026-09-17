#!/usr/bin/env node
/* ==========================================================================
   Einmalige Anmeldung für den interaktiven Story-Weg – auf dem EIGENEN Rechner.

   Der Grund steht im Protokoll des 17.09.: Die Erstanmeldung vom
   GitHub-Actions-Runner hat Instagram mit „Please wait a few minutes before
   you try again" abgewiesen. Runner stehen in Rechenzentren, und eine
   Erstanmeldung von einer Rechenzentrums-IP ist für Instagram das
   auffälligste Muster überhaupt. Das wiederholte Versuchen hilft dagegen
   nicht – es macht es schlimmer.

   Deshalb dieser Weg: einmal von einem normalen Anschluss anmelden, die
   Sitzung verschlüsselt als Secret hinterlegen. Die CI meldet sich danach nie
   mehr an, sie benutzt nur noch diese Sitzung.

   Voraussetzungen auf dem eigenen Rechner:
     pip install instagrapi
     IG_PRIVAT_USER, IG_PRIVAT_PASS, IG_PRIVAT_KEY in der Umgebung

   Aufruf:
     IG_PRIVAT_USER=... IG_PRIVAT_PASS=... IG_PRIVAT_KEY=... \
       node bin/interaktiv-anmelden.mjs
   ========================================================================== */

import { CONFIG } from "../src/config.mjs";
import { anmeldenNur } from "../src/interaktiv.mjs";

const { nutzer, passwort } = CONFIG.interaktiv;
if (!nutzer || !passwort) { console.error("✗ IG_PRIVAT_USER und IG_PRIVAT_PASS fehlen."); process.exit(2); }
if (!CONFIG.interaktiv.schluessel) { console.error("✗ IG_PRIVAT_KEY fehlt – ohne ihn lässt sich die Sitzung nicht verschlüsseln."); process.exit(2); }

console.log(`Melde @${nutzer} an – von diesem Anschluss, nicht aus der CI.`);
try {
  const { tresor } = await anmeldenNur();
  console.log("\n✓ Angemeldet. Diesen Wert als GitHub-Secret IG_PRIVAT_SITZUNG eintragen:\n");
  console.log(tresor);
  console.log("\nEr ist verschlüsselt (IG_PRIVAT_KEY) und ohne den Schlüssel wertlos –");
  console.log("trotzdem gehört er nur in das Secret-Feld, sonst nirgendwohin.");
} catch (e) {
  console.error(`\n✗ Anmeldung fehlgeschlagen (${e.art || "fehler"}): ${e.message}`);
  if (e.art === "challenge") console.error("  Erst in der Instagram-App anmelden und bestätigen, dann hier noch einmal.");
  if (e.art === "aufbau") console.error("  Fehlt instagrapi? →  pip install instagrapi");
  process.exit(1);
}
