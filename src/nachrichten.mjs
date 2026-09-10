/* ==========================================================================
   Schlüsselwort-Nachrichten: „Kommentiere SCHEMA und du bekommst die Karte
   als Nachricht.“ Kommentare treiben die Reichweite, die Nachricht liefert
   die Spickzettel-Karte direkt ins Postfach.

   Voraussetzung: Berechtigung instagram_business_manage_messages mit
   „Advanced Access“ (einmalige App-Prüfung bei Meta). Ohne sie schlägt der
   Versand fehl – der Bot merkt sich das und probiert es erst am nächsten
   Tag wieder, damit kein Lauf blockiert.
   ========================================================================== */

import { CONFIG } from "./config.mjs";

/* Kommentare mit Schlüsselwort unter Beiträgen, die eine Karte haben. */
export function schluesselwortKommentare(medien, eigenerName, ledger, karten) {
  const wort = CONFIG.nachrichten.schluesselwort.toLowerCase();
  const erledigt = new Set((ledger.nachrichten || []).map((n) => n.kommentarId));
  const out = [];
  for (const m of medien) {
    const karte = karten.get(m.id);
    if (!karte) continue;
    for (const k of m.comments?.data || []) {
      if (!k.text || erledigt.has(k.id)) continue;
      if (k.username && eigenerName && k.username.toLowerCase() === eigenerName.toLowerCase()) continue;
      if (Date.now() - new Date(k.timestamp).getTime() > 6.5 * 86400000) continue;   // private Antworten nur 7 Tage lang möglich
      if (!k.text.toLowerCase().includes(wort)) continue;
      out.push({ kommentarId: k.id, username: k.username, medienId: m.id, karte });
    }
  }
  return out;
}

/**
 * Verschickt die Karten. `karten`: Map medienId → { bildUrl, titel }.
 */
export async function kartenVerschicken(ig, ledger, karten, { log = console.log } = {}) {
  if (!CONFIG.nachrichten.aktiv || !karten.size) return { gesendet: 0 };
  const sperre = ledger.nachrichtenSperreBis;
  if (sperre && new Date(sperre) > new Date()) return { gesendet: 0, gesperrt: true };
  const eigener = await ig.eigenerName();
  const medien = await ig.neuesteMedien(CONFIG.interaktion.beitraegeZurueck);
  const offen = schluesselwortKommentare(medien, eigener, ledger, karten).slice(0, CONFIG.nachrichten.maxJeLauf);
  ledger.nachrichten = ledger.nachrichten || [];
  let n = 0;
  for (const k of offen) {
    try {
      const id = await ig.privateAntwort(k.kommentarId, { bildUrl: k.karte.bildUrl, text: `Hier ist deine Karte „${k.karte.titel}“. Speichern, bevor sie in der Timeline verschwindet – und viel Erfolg im Examen!` });
      ledger.nachrichten.push({ kommentarId: k.kommentarId, medienId: k.medienId, von: k.username, datum: new Date().toISOString().slice(0, 10), id });
      n++;
      log(`  ✉ Karte an @${k.username}`);
    } catch (e) {
      if (/permission|\(#10\)|\(#3\)|not authorized|OAuth/i.test(e.message)) {
        ledger.nachrichtenSperreBis = new Date(Date.now() + 86400000).toISOString();
        console.error(`  ✗ Nachrichten: keine Berechtigung (${e.message.slice(0, 120)}) – bis morgen ausgesetzt. Siehe README „Schlüsselwort-Nachrichten“.`);
        break;
      }
      console.error(`  ✗ Nachricht an @${k.username}: ${e.message}`);
    }
  }
  const grenze = new Date(Date.now() - 30 * 86400000).toISOString().slice(0, 10);
  ledger.nachrichten = ledger.nachrichten.filter((x) => x.datum >= grenze);
  return { gesendet: n };
}
