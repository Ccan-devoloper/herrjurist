/* ==========================================================================
   Tageslauf – wird stündlich von GitHub Actions gestartet.

   1. Asset-Zweig holen (Bilder, Ledger, Tagesplan, Token-Tresor)
   2. Tagesplan laden oder für heute erzeugen
   3. Alle fälligen, noch nicht veröffentlichten Einträge abarbeiten:
      schreiben → prüfen → rendern → hochladen → veröffentlichen → vermerken
   4. Zustand committen und pushen

   Optionen:  --nur-planen   Plan anzeigen, nichts erzeugen
              --nur-rendern  Inhalte erzeugen und rendern, nichts veröffentlichen (wie IG_DRY_RUN=true)
              --datum=YYYY-MM-DD  Plan eines anderen Tages (für Tests)
              --alles        alle Einträge des Tages sofort (ohne Uhrzeit-Prüfung)
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { CONFIG } from "./config.mjs";
import { zeitStatistik } from "./zeiten.mjs";
import { themenpool } from "./inhalte.mjs";
import { tagesplan, auffuellplan, ledgerLaden, ledgerSpeichern, vermerken } from "./planer.mjs";
import { pruefeBeitrag } from "./pruefung.mjs";
import { beitragSchreiben, storiesSchreiben, teaserAusBeitrag, aktuellRecherchieren, loesungsRecherchieren, reelSchreiben } from "./autor.mjs";
import { reelBauen } from "./reel.mjs";
import { beitragRendern, storyRendern, browserBeenden } from "./render.mjs";
import { Instagram } from "./instagram.mjs";
import { Hosting } from "./hosting.mjs";
import { kommentareBeantworten } from "./interaktion.mjs";
import { lernschleife } from "./insights.mjs";
import { verteilen } from "./verteilen.mjs";
import { varianteErmitteln } from "./wechsel.mjs";
import { kartenVerschicken } from "./nachrichten.mjs";
import { berichtErstellen, berichtSenden } from "./bericht.mjs";
import { abschluss as kostenAbschluss, budgetSetzen, reservieren, reservierungAufheben, tagesStand, tagesLimit, BudgetFehler } from "./kosten.mjs";
import { stimmeStandVerbinden, stimmeStand, stimmeIstGesperrt } from "./stimme.mjs";
import { kandidatenSuchen, stimmeUebernehmen, stimmeWaehlen, gewinner, stimmenStatistik } from "./stimmen.mjs";
import { wochentag } from "./zeit.mjs";
import { heuteIso, lokaleMinuten, minutenVon } from "./zeit.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const args = new Map(process.argv.slice(2).map((a) => { const [k, v] = a.replace(/^--/, "").split("="); return [k, v ?? true]; }));
const datum = args.get("datum") || heuteIso();
const nurPlanen = args.has("nur-planen");
const trocken = args.has("nur-rendern") || CONFIG.instagram.trockenlauf;
const alles = args.has("alles");
const auffuellen = Number(args.get("auffuellen") || 0);
const AUSGABE = path.resolve(hier, "../out", datum);

function log(...t) { console.log(new Date().toISOString().slice(11, 19), ...t); }

/* Schwarz/Weiß-Wechsel: Beiträge alternieren fortlaufend über alle Tage
   (Schachbrett im Profil), Stories alternieren innerhalb des Tages. */
const tagIndex = Math.floor(new Date(`${datum}T12:00:00Z`).getTime() / 86400000);
const varianteStory = (slot) => (CONFIG.marke.farbeJeKlausur ? 0 : (Number(slot.slice(1)) - 1) % 2);

/* Plan serialisierbar machen: Themen nur als ID + Titel, Inhalte separat. */
function planSpeichern(hosting, plan) {
  hosting.jsonSchreiben(`plaene/${plan.datum}.json`, plan);
}

async function main() {
  log(`Instagram-Bot · ${datum} · Stil ${CONFIG.marke.stil} · ${trocken ? "TROCKENLAUF" : "live"}`);

  const hosting = new Hosting({ pushen: !nurPlanen }).vorbereiten();
  const ledgerPfad = path.join(hosting.stateDir, "ledger.json");

  /* Tagesdeckel: bisheriger Verbrauch des Tages aus state/kosten.json, jeder
     weitere Aufruf wird sofort dort festgehalten. */
  const kostenStart = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} });
  budgetSetzen({
    limitUsd: CONFIG.ki.tagesBudgetUsd,
    bisher: kostenStart.tage?.[datum]?.usd || 0,
    speichern: (usd, aufrufe, zwecke) => {
      const k = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} }); k.tage = k.tage || {};
      const alt = kostenStart.tage?.[datum] || {};
      const gesamtZwecke = { ...(alt.zwecke || {}) };
      for (const [z, betrag] of Object.entries(zwecke || {})) gesamtZwecke[z] = Number(((alt.zwecke?.[z] || 0) + betrag).toFixed(4));
      k.tage[datum] = { usd: Number(usd.toFixed(4)), aufrufe: (alt.aufrufe || 0) + aufrufe, zwecke: gesamtZwecke, stand: new Date().toISOString() };
      hosting.jsonSchreiben("kosten.json", k);
    },
  });
  log(`Tagesbudget: ${tagesStand().toFixed(3)} $ von ${tagesLimit().toFixed(2)} $ verbraucht`);

  /* Stimmen-Kontingent: ElevenLabs, solange das Monatsguthaben des Abos reicht,
     danach automatisch Piper. Der Stand überdauert den Lauf im Assets-Zweig. */
  stimmeStandVerbinden({
    lesen: () => hosting.jsonLesen("stimme.json", null),
    schreiben: (stand) => hosting.jsonSchreiben("stimme.json", stand),
  });
  if (CONFIG.reel.elevenlabsKey) {
    const st = stimmeStand();
    log(`Stimme: ElevenLabs${st.abo ? ` (${st.abo})` : ""}${st.erschoepft ? " – Guthaben aufgebraucht, es spricht Piper" : st.rest != null ? ` · ${st.rest} Zeichen frei` : ""}`);
  }

  /* Stimmenauswahl: einmalig deutsche Kandidaten aus der Bibliothek suchen,
     danach steht die Liste in state/stimmen.json. Welche davon spricht, sagt
     stimmeWaehlen() je Reel – bis eine gewonnen hat. */
  let stimmenListe = hosting.jsonLesen("stimmen.json", null);
  if (CONFIG.reel.elevenlabsKey && CONFIG.reel.stimmeLernen && !stimmenListe?.kandidaten?.length && !stimmeStand().erschoepft) {
    try {
      const roh = await kandidatenSuchen({ anzahl: CONFIG.reel.stimmeAnzahl, abo: stimmeStand().abo });
      const bezahlt = String(stimmeStand().abo || "") !== "free";
      const kandidaten = [];
      for (const k of roh) kandidaten.push(await stimmeUebernehmen(k, { bezahlt }));
      if (kandidaten.length) {
        stimmenListe = { gesucht: new Date().toISOString(), kandidaten, fest: null };
        hosting.jsonSchreiben("stimmen.json", stimmenListe);
        log(`Stimmen gefunden: ${kandidaten.map((k) => `${k.name} (${k.geschlecht || "?"}, ${k.beschreibung || k.einsatz || "–"})`).join(" · ")}`);
      }
    } catch (e) { console.warn(`  ! Stimmensuche fehlgeschlagen: ${e.message}`); }
  }
  const ledger = ledgerLaden(ledgerPfad);
  const pool = themenpool();
  const poolIndex = new Map(pool.map((t) => [t.id, t]));

  /* Gelernte Strategie (Formate, Fächer, Uhrzeiten) aus der Lernschleife. */
  const strategie = hosting.jsonLesen("strategie.json", null);

  /* Plan des Tages – nur einmal erzeugen, danach fortschreiben. */
  let plan = hosting.jsonLesen(`plaene/${datum}.json`, null);
  /* Ein Plan aus einem Trockenlauf (Einträge mit medienId „trocken“) gilt live
     nicht – er wird verworfen und neu erzeugt, sonst hält der Bot alles für
     bereits veröffentlicht. */
  if (plan && !trocken && (plan.trocken || [...(plan.beitraege || []), ...(plan.stories || [])].some((e) => e.medienId === "trocken"))) {
    log("Tagesplan stammt aus einem Trockenlauf – wird neu erzeugt.");
    plan = null;
  }
  if (!plan) {
    const p = tagesplan(datum, ledger, pool, strategie);
    plan = {
      datum: p.datum, erzeugt: new Date().toISOString(), anlass: p.anlass || null, abendAnlass: p.abendAnlass || null, trocken,
      beitraege: p.beitraege.map((b) => ({ slot: b.slot, zeit: b.zeit, format: b.format, themaId: b.thema?.id || null, themaTitel: b.thema?.titel || null, fach: b.thema?.fach || null, lang: b.lang, status: "geplant" })),
      stories: p.stories.map((s) => ({ slot: s.slot, zeit: s.zeit, art: s.art, themaId: s.thema?.id || null, beitragSlot: s.beitragSlot || null, tageBisExamen: s.tageBisExamen, status: "geplant" })),
    };
    planSpeichern(hosting, plan);
    log(`Tagesplan erzeugt: ${plan.beitraege.length} Beiträge, ${plan.stories.length} Stories`);
    if (CONFIG.plan.zeitLernen) {
      const zs = zeitStatistik(ledger);
      log(`  Uhrzeiten: ${zs.gesamt ? `aus ${zs.gesamt} gemessenen Beiträgen gelernt` : "noch ohne Messungen"}${zs.gesamt < 20 ? ", weitere Stunden werden ausprobiert" : ""}`);
    }
  }
  if (nurPlanen) {
    for (const b of plan.beitraege) log(`  ${b.zeit} Beitrag ${b.slot} ${b.format} ${b.themaTitel || ""} [${b.status}]`);
    for (const s of plan.stories) log(`  ${s.zeit} Story ${s.slot} ${s.art} ${s.beitragSlot ? "→ " + s.beitragSlot : poolIndex.get(s.themaId)?.titel || ""} [${s.status}]`);
    return;
  }

  if (auffuellen > 0) { await auffuellenLauf(auffuellen, { hosting, ledger, ledgerPfad, pool, poolIndex, strategie }); return; }

  /* Das Reel des Tages ist gesetzt: Solange es aussteht, bleibt ein Teil des
     Tagesbudgets dafür zurückgelegt, damit es nicht an Beiträgen, Recherche
     oder Auffüllen scheitert. */
  const reelOffen = plan.beitraege.some((b) => b.format === "reel" && b.status !== "veroeffentlicht" && !b.fehler);
  if (reelOffen && !trocken) { reservieren(CONFIG.ki.reelReserveUsd); log(`  ${CONFIG.ki.reelReserveUsd.toFixed(2)} $ für das Reel zurückgelegt`); }
  else reservierungAufheben();

  const jetzt = lokaleMinuten();
  const faellig = (e) => e.status !== "veroeffentlicht" && (alles || minutenVon(e.zeit) <= jetzt);
  const beitraegeFaellig = plan.beitraege.filter(faellig);
  const storiesFaellig = plan.stories.filter(faellig);

  /* Instagram-Verbindung und Kontingent. */
  const ig = new Instagram({ trockenlauf: trocken, tresorDatei: path.join(hosting.stateDir, "token.enc") });
  let kontingent = { genutzt: 0, maximum: 100 };
  if (!trocken) {
    ig.tresorLaden();
    const { konto, limit } = await ig.pruefen();
    kontingent = limit;
    log(`Verbunden mit @${konto.username} · Kontingent ${limit.genutzt}/${limit.maximum}`);
    if (await ig.tokenAuffrischen()) log("Zugriffstoken verlängert und im Tresor gespeichert.");

    /* Interaktion: neue Kommentare beantworten – bei jedem Lauf, unabhängig vom Plan. */
    if (CONFIG.interaktion.aktiv) {
      try {
        const r = await kommentareBeantworten(ig, ledger, { log });
        if (r.beantwortet) { ledgerSpeichern(ledgerPfad, ledger); hosting.commit(`Kommentare beantwortet ${datum}`); await hosting.push(); }
        log(`Interaktion: ${r.beantwortet} Antworten (${r.geprueft} Beiträge, ${r.kommentare ?? 0} Kommentare geprüft)`);
      } catch (e) {
        if (e instanceof BudgetFehler) log(`  ⏸ ${e.message}`); else console.error(`  ✗ Interaktion: ${e.message}`);
      }
    }
    /* Schlüsselwort-Nachrichten: Spickzettel-Karten an Kommentierende. */
    try {
      const karten = new Map((ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.karteUrl && e.medienId).map((e) => [e.medienId, { bildUrl: e.karteUrl, titel: e.titel }]));
      const r = await kartenVerschicken(ig, ledger, karten, { log });
      if (r.gesendet) { ledgerSpeichern(ledgerPfad, ledger); hosting.commit(`Karten verschickt ${datum}`); await hosting.push(); }
    } catch (e) {
      console.error(`  ✗ Nachrichten: ${e.message}`);
    }
    /* Lernschleife: einmal am Tag beim ersten Lauf (Insights, Strategie, Follower). */
    const wochenStand = hosting.jsonLesen("lernschleife.json", { datum: null });
    if (wochenStand.datum !== datum) {
      try {
        await lernschleife(ig, ledger, hosting, { log });
        hosting.jsonSchreiben("lernschleife.json", { datum });
        /* Stimmen: Hat eine der Kandidatinnen genug Messungen und liegt sie
           deutlich vorn, wird sie festgeschrieben – ab dann klingt der Kanal
           immer gleich. */
        if (stimmenListe?.kandidaten?.length && !stimmenListe.fest) {
          const stat = stimmenStatistik(ledger);
          const sieger = gewinner(stat, stimmenListe.kandidaten);
          if (sieger) {
            stimmenListe = { ...stimmenListe, fest: { id: sieger.id, name: sieger.name }, entschieden: new Date().toISOString(), stand: stat.je };
            hosting.jsonSchreiben("stimmen.json", stimmenListe);
            log(`Stimme steht fest: „${sieger.name}“ (${sieger.mittel.toFixed(2)}× Schnitt aus ${sieger.n} Reels) – ab jetzt spricht nur noch sie.`);
          }
        }
        ledgerSpeichern(ledgerPfad, ledger);
        hosting.commit(`Lernschleife ${datum}`); await hosting.push();
      } catch (e) { console.error(`  ✗ Lernschleife: ${e.message}`); }
    }
    /* Wochenbericht: montags beim ersten Lauf. */
    const berichtStand = hosting.jsonLesen("bericht.json", { woche: null });
    const kw = wochenKennung(datum);
    if (wochentag(new Date(`${datum}T12:00:00Z`)) === CONFIG.bericht.wochentag && berichtStand.woche !== kw) {
      try {
        const kostenWoche = hosting.jsonLesen("kosten.json", { wochen: {} });
        const text = berichtErstellen({ ledger, strategie: hosting.jsonLesen("strategie.json", null), follower: hosting.jsonLesen("follower.json", []), kosten: { ...(kostenWoche.wochen?.[wochenKennung(vorwoche(datum))] || kostenWoche.wochen?.[kw] || {}), tage: kostenWoche.tage || {}, limit: CONFIG.ki.tagesBudgetUsd }, datum, fehler: hosting.jsonLesen("fehler.json", []).slice(-10), hinweise: berichtHinweise(hosting.jsonLesen("strategie.json", null)), stimme: hosting.jsonLesen("stimme.json", null), stimmen: hosting.jsonLesen("stimmen.json", null) });
        hosting.jsonSchreiben(`berichte/${kw}.txt`, { text });
        const r = await berichtSenden(text, `Instagram-Bot · Wochenbericht ${kw}`);
        hosting.jsonSchreiben("bericht.json", { woche: kw, gesendet: r.gesendet, grund: r.grund || null });
        log(`Wochenbericht ${kw}: ${r.gesendet ? "per E-Mail gesendet" : `nur abgelegt (${r.grund})`}`);
      } catch (e) { console.error(`  ✗ Wochenbericht: ${e.message}`); }
    }
  }
  /* Auffüllen läuft erst, wenn die regulären Beiträge des Tages durch sind –
     sonst frisst es morgens das Tagesbudget, und Reel und Stories fallen aus. */
  const tagesplanFertig = plan.beitraege.every((b) => b.status === "veroeffentlicht" || b.fehler);
  const auffuellOffen = !trocken && !nurPlanen && tagesplanFertig && (() => { const a = hosting.jsonLesen("auffuellen.json", null); return a && a.fertig < a.ziel; })();
  if (!beitraegeFaellig.length && !storiesFaellig.length && !auffuellOffen) { log("Nichts fällig."); return; }
  const frei = () => kontingent.maximum - kontingent.genutzt - CONFIG.instagram.sicherheitsabstandLimit;

  const fertigeBeitraege = new Map();   // slot → Beitrag (für Teaser)
  let fehler = 0;

  /* Story-Texte des ganzen Tages zuerst, in einem einzigen günstigen KI-Aufruf:
     Sie kosten nur wenige Cent, würden aber ausfallen, wenn erst die teuren
     Beiträge das Tagesbudget aufbrauchen (so am 09.09.: fünf Abend-Stories
     blieben liegen). Einmal geschrieben, liegen sie unter inhalte/ und werden
     in späteren Läufen des Tages nur noch gerendert. */
  const geschrieben = new Map();
  /* Auch früher übersprungene Slots gehören dazu: Ihr Text liegt bereits unter
     inhalte/ und wird vor dem Veröffentlichen erneut geprüft. Ohne sie fehlte
     der Text später im Veröffentlichungslauf und die Story fiele ganz aus. */
  const eigenstaendig = plan.stories.filter((s) => s.art !== "teaser" && s.status !== "veroeffentlicht");
  if (eigenstaendig.length && (storiesFaellig.length || beitraegeFaellig.length)) {
    const vorhanden = eigenstaendig.map((s) => [s.slot, hosting.jsonLesen(`inhalte/${datum}-${s.slot}.json`, null)]);
    const offen = vorhanden.filter(([, v]) => !v).map(([slot]) => eigenstaendig.find((s) => s.slot === slot));
    for (const [slot, v] of vorhanden) if (v) geschrieben.set(slot, v);
    if (offen.length) {
      try {
        const auftrag = (liste) => liste.map((s) => ({ slot: s.slot, art: s.art, thema: s.themaId ? poolIndex.get(s.themaId) : null, tageBisExamen: s.tageBisExamen }));
        const neu = await storiesSchreiben(auftrag(offen), datum);
        for (const s of neu) { hosting.jsonSchreiben(`inhalte/${datum}-${s.slot}.json`, s); geschrieben.set(s.slot, s); }
        log(`  Story-Texte für ${neu.length} Slots geschrieben`);
        /* Beanstandete Slots einmal neu schreiben statt sie zu verlieren: ein
           Nachschlag für zwei, drei Slots kostet nur wenige Cent. */
        hosting.commit(`Story-Texte ${datum}`);
        const strittig = neu.filter((s) => s.beanstandet);
        if (strittig.length) try {
          const hinweis = `Die folgenden Entwürfe wurden abgelehnt – formuliere sie vollständig neu:\n${strittig.map((s) => `- Slot ${s.slot}: ${s.beanstandet.join("; ")}`).join("\n")}`;
          log(`  ${strittig.length} Story-Entwürfe beanstandet – zweiter Versuch`);
          const zweite = await storiesSchreiben(auftrag(offen.filter((o) => strittig.some((s) => s.slot === o.slot))), datum, hinweis);
          for (const s of zweite) {
            const vorher = geschrieben.get(s.slot);
            if (s.beanstandet && vorher && !vorher.beanstandet) continue;
            hosting.jsonSchreiben(`inhalte/${datum}-${s.slot}.json`, s); geschrieben.set(s.slot, s);
          }
          hosting.commit(`Story-Texte ${datum} (zweiter Versuch)`);
        } catch (e) {
          if (e instanceof BudgetFehler) log(`  ⏸ ${e.message}`);
          else console.error(`  ✗ Stories nachschreiben: ${e.message}`);
        }
      } catch (e) {
        if (e instanceof BudgetFehler) log(`  ⏸ ${e.message}`);
        else { fehler++; console.error(`  ✗ Stories schreiben: ${e.message}`); }
      }
    }
  }

  /* Dann die Beiträge (wichtiger), zuletzt die Stories veröffentlichen. */
  for (const eintrag of beitraegeFaellig) {
    if (frei() <= 0) { log("Tageskontingent erschöpft – Beitrag verschoben."); break; }
    try {
      log(`Beitrag ${eintrag.slot} (${eintrag.format}) ${eintrag.themaTitel || ""}`);
      if (eintrag.format === "reel") {
        let reel = hosting.jsonLesen(`inhalte/${datum}-${eintrag.slot}.json`, null);
        if (!reel) {
          reel = await reelSchreiben({ thema: eintrag.themaId ? poolIndex.get(eintrag.themaId) : null, datum, lang: Boolean(eintrag.lang), anlass: plan.anlass, strategie });
          reel.slug = `${datum}-${eintrag.slot}`;
          hosting.jsonSchreiben(`inhalte/${datum}-${eintrag.slot}.json`, reel);
        }
        const varianteReel = (CONFIG.marke.farbeJeKlausur ? 0 : await varianteErmitteln({ ig, ledger, trocken, log }));
        const gewaehlteStimme = stimmeWaehlen({ kandidaten: stimmenListe?.kandidaten || [], ledger, datum, fest: stimmenListe?.fest || null });
        const r = await reelBauen(reel, path.join(AUSGABE, "reels", eintrag.slot), { variante: varianteReel, datum, hintergrundDir: path.join(hosting.stateDir, "hintergrund"), stimmeId: gewaehlteStimme?.id || null, stimmeName: gewaehlteStimme?.name || null });
        log(`  Reel gebaut: ${r.dauer.toFixed(1)} s · Stimme ${r.anbieter}${r.stimmeName ? ` „${r.stimmeName}“` : ""} · Animation ${r.animation}`);
        /* Stimme vom Tarif gesperrt: aus der Liste werfen, beim nächsten Lauf
           wird neu gesucht – sonst bliebe ElevenLabs dauerhaft ungenutzt. */
        if (gewaehlteStimme && stimmeIstGesperrt(gewaehlteStimme.id) && stimmenListe?.kandidaten) {
          stimmenListe = { ...stimmenListe, kandidaten: stimmenListe.kandidaten.filter((k) => k.id !== gewaehlteStimme.id) };
          hosting.jsonSchreiben("stimmen.json", stimmenListe);
          log(`  Stimme „${gewaehlteStimme.name}“ entfernt (Tarif erlaubt sie nicht).`);
        }
        const [videoUrl, coverUrl] = await hosting.veroeffentlichen([r.video, r.cover], datum, `Reel ${datum} ${eintrag.slot}`);
        const caption = `${reel.caption}\n\n${reel.hashtags.join(" ")}`;
        const medienId = await ig.reelPosten({ videoUrl, coverUrl, caption });
        kontingent.genutzt += 1;
        eintrag.status = "veroeffentlicht"; eintrag.medienId = medienId; eintrag.veroeffentlicht = new Date().toISOString();
        vermerken(ledger, { datum, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, stunde: Math.floor(lokaleMinuten() / 60), format: "reel", thema: reel.themaId, fach: reel.fach, titel: reel.szenen[0]?.titel || reel.kurztitel, hookTyp: reel.hookTyp, hookMuster: reel.hookMuster, medienId, variante: varianteReel, hashtags: reel.hashtags, stimmeId: r.stimmeId || null, stimmeName: r.stimmeName || null, veroeffentlicht: new Date().toISOString() });
        eintrag.kanaele = await verteilen({ art: "reel", videoUrl, videoPfad: r.video, bildUrls: [coverUrl], titel: reel.kurztitel || reel.szenen[0]?.titel, text: caption, hashtags: reel.hashtags }, { log, trockenlauf: trocken });
        fertigeBeitraege.set(eintrag.slot, { ...reel, folien: [{ art: "titel", titel: reel.szenen[0]?.titel, icon: reel.szenen[0]?.icon }], kurztitel: reel.kurztitel });
        ledgerSpeichern(ledgerPfad, ledger); planSpeichern(hosting, plan);
        reservierungAufheben();   // Reel steht, der Rest des Tages darf die Rücklage nutzen
        hosting.commit(`Veröffentlicht: Reel ${datum} ${eintrag.slot}`); await hosting.push();
        log(`  ✓ Reel ${medienId} (${r.dauer.toFixed(0)} s, Stimme: ${r.anbieter})`);
        continue;
      }
      let beitrag = hosting.jsonLesen(`inhalte/${datum}-${eintrag.slot}.json`, null);
      if (!beitrag) {
        const thema = eintrag.themaId ? poolIndex.get(eintrag.themaId) : null;
        let recherche = null, wochenThemen = null;
        if (eintrag.format === "aktuell" || eintrag.format === "loesungsskizze") {
          const bisher = (ledger.veroeffentlicht || []).filter((e) => e.format === "aktuell").slice(-12).map((e) => e.titel);
          recherche = eintrag.format === "loesungsskizze" ? await loesungsRecherchieren(datum, eintrag.anlass || plan.abendAnlass) : await aktuellRecherchieren(datum, bisher);
          log(`  Recherche: ${recherche.titel || "(ohne Titel)"} · ${recherche.quellen.length} Quellen`);
        }
        if (eintrag.format === "wochenrueckblick") {
          const grenze = new Date(new Date(`${datum}T12:00:00Z`).getTime() - 7 * 86400000).toISOString().slice(0, 10);
          wochenThemen = (ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.datum >= grenze).map((e) => e.titel);
          if (!wochenThemen.length) wochenThemen = pool.filter((t) => t.prioritaet === "hoch").slice(0, 5).map((t) => t.titel);
        }
        beitrag = await beitragSchreiben({ format: eintrag.format, thema, datum, recherche, wochenThemen, anlass: eintrag.format === "anlass" ? plan.anlass : eintrag.format === "loesungsskizze" ? plan.abendAnlass : null, strategie });
        beitrag.slug = `${datum}-${eintrag.slot}`;
        hosting.jsonSchreiben(`inhalte/${datum}-${eintrag.slot}.json`, beitrag);
      }
      const variante = (CONFIG.marke.farbeJeKlausur ? 0 : await varianteErmitteln({ ig, ledger, trocken, log }));
      const bilder = await beitragRendern(beitrag, path.join(AUSGABE, "beitraege"), { variante });
      const urls = await hosting.veroeffentlichen(bilder, datum, `Beitrag ${datum} ${eintrag.slot}`);
      const caption = `${beitrag.caption}\n\n${beitrag.hashtags.join(" ")}`;
      const schonDa = await ig.bereitsVeroeffentlicht(caption);
      if (schonDa) log(`  Beitrag steht bereits auf Instagram (${schonDa}) – wird nur vermerkt.`);
      const medienId = schonDa || await ig.beitragPosten({ bildUrls: urls, caption });
      kontingent.genutzt += 1;
      eintrag.status = "veroeffentlicht";
      eintrag.medienId = medienId;
      eintrag.veroeffentlicht = new Date().toISOString();
      const karteIndex = beitrag.folien.findIndex((f) => f.art === "karte");
      vermerken(ledger, { datum, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, stunde: Math.floor(lokaleMinuten() / 60), format: eintrag.format, thema: beitrag.themaId, fach: beitrag.fach, titel: beitrag.folien[0].titel, hookTyp: beitrag.hookTyp, medienId, variante, hashtags: beitrag.hashtags, veroeffentlicht: new Date().toISOString(), karteUrl: karteIndex >= 0 ? urls[karteIndex] : null });
      fertigeBeitraege.set(eintrag.slot, beitrag);
      /* Auf weitere Kanäle verteilen (Threads, Facebook, LinkedIn …). */
      eintrag.kanaele = await verteilen({ art: "beitrag", bildUrls: urls, bildPfade: bilder, titel: beitrag.folien[0].titel, text: caption, hashtags: beitrag.hashtags }, { log, trockenlauf: trocken });
      ledgerSpeichern(ledgerPfad, ledger);
      planSpeichern(hosting, plan);
      hosting.commit(`Veröffentlicht: Beitrag ${datum} ${eintrag.slot}`);
      await hosting.push();
      log(`  ✓ ${medienId} (${urls.length} Folien)`);
    } catch (e) {
      if (e instanceof BudgetFehler) { log(`  ⏸ ${e.message}`); continue; }
      fehler++;
      eintrag.fehler = `${new Date().toISOString()} ${e.message}`;
      planSpeichern(hosting, plan);
      console.error(`  ✗ Beitrag ${eintrag.slot}: ${e.message}`);
    }
  }

  for (const eintrag of storiesFaellig) {
    if (frei() <= 0) { log("Tageskontingent erschöpft – Story verschoben."); break; }
    try {
      let story;
      if (eintrag.art === "teaser") {
        let beitrag = fertigeBeitraege.get(eintrag.beitragSlot) || hosting.jsonLesen(`inhalte/${datum}-${eintrag.beitragSlot}.json`, null);
        const b = plan.beitraege.find((x) => x.slot === eintrag.beitragSlot);
        if (!beitrag || b?.status !== "veroeffentlicht") { log(`Story ${eintrag.slot}: Beitrag ${eintrag.beitragSlot} noch nicht veröffentlicht – später.`); continue; }
        story = teaserAusBeitrag(beitrag, eintrag.slot);
      } else {
        story = geschrieben.get(eintrag.slot);
        if (!story) continue;
        /* Frühere Beanstandungen mit den heutigen Regeln nachprüfen: Wurde die
           Prüfung seither entschärft (etwa Fachsprache statt Abschreiben), darf
           die Story doch erscheinen, statt dauerhaft zu fehlen. */
        if (story.beanstandet) {
          const erneut = pruefeBeitrag({ stories: [story] });
          if (erneut.ok) { delete story.beanstandet; hosting.jsonSchreiben(`inhalte/${datum}-${eintrag.slot}.json`, story); }
          else { log(`Story ${eintrag.slot} beanstandet: ${erneut.fehler.join("; ")} – übersprungen.`); eintrag.status = "uebersprungen"; continue; }
        }
      }
      const bild = await storyRendern(story, path.join(AUSGABE, "stories", `${datum}-${eintrag.slot}-${story.art}.jpg`), { variante: varianteStory(eintrag.slot) });
      const [url] = await hosting.veroeffentlichen([bild], datum, `Story ${datum} ${eintrag.slot}`);
      const medienId = await ig.storyPosten({ bildUrl: url });
      kontingent.genutzt += 1;
      eintrag.status = "veroeffentlicht";
      eintrag.medienId = medienId;
      eintrag.veroeffentlicht = new Date().toISOString();
      vermerken(ledger, { datum, art: "story", slot: eintrag.slot, storyArt: story.art, thema: story.themaId || eintrag.themaId || null, fach: story.fach, titel: story.titel || story.text || "", medienId });
      ledgerSpeichern(ledgerPfad, ledger);
      planSpeichern(hosting, plan);
      hosting.commit(`Veröffentlicht: Story ${datum} ${eintrag.slot}`);
      await hosting.push();
      log(`  ✓ Story ${eintrag.slot} ${story.art} → ${medienId}`);
    } catch (e) {
      if (e instanceof BudgetFehler) { log(`  ⏸ ${e.message}`); continue; }
      fehler++;
      eintrag.fehler = `${new Date().toISOString()} ${e.message}`;
      planSpeichern(hosting, plan);
      console.error(`  ✗ Story ${eintrag.slot}: ${e.message}`);
    }
  }

  /* Ein angefangenes Auffüllen (state/auffuellen.json) läuft von selbst weiter –
     in kleinen Portionen, damit der Stundenlauf nicht blockiert. */
  const auffuellStand = hosting.jsonLesen("auffuellen.json", null);
  /* Erst wenn Beiträge UND Stories des Tages durch sind (auch übersprungene),
     bekommt das Auffüllen den Rest des Budgets – nie vor den Stories. */
  const planJetztFertig = plan.beitraege.every((b) => b.status === "veroeffentlicht" || b.fehler) && plan.stories.every((s) => s.status !== "geplant");
  if (!trocken && !nurPlanen && planJetztFertig && auffuellStand && auffuellStand.fertig < auffuellStand.ziel) {
    log(`Auffüllen fortsetzen: ${auffuellStand.fertig}/${auffuellStand.ziel}`);
    try { await auffuellenLauf(auffuellStand.ziel, { hosting, ledger, ledgerPfad, pool, poolIndex, strategie, maxJeLauf: 4 }); }
    catch (e) { fehler++; console.error(`  ✗ Auffüllen: ${e.message}`); }
  }

  /* Kosten der Woche und Fehler für den Bericht festhalten. */
  const kosten = kostenAbschluss();
  if (kosten.aufrufe) {
    const k = hosting.jsonLesen("kosten.json", { wochen: {} });
    const kw = wochenKennung(datum);
    const w = k.wochen[kw] || { usd: 0, aufrufe: 0, cacheSumme: 0 };
    w.usd += kosten.usd; w.aufrufe += kosten.aufrufe; w.cacheSumme += kosten.cacheAnteil * kosten.aufrufe; w.cacheAnteil = w.cacheSumme / w.aufrufe;
    k.wochen[kw] = w;
    hosting.jsonSchreiben("kosten.json", k);
  }
  const fehlerListe = hosting.jsonLesen("fehler.json", []);
  for (const e of [...plan.beitraege, ...plan.stories]) if (e.fehler && !fehlerListe.includes(e.fehler)) fehlerListe.push(e.fehler);
  hosting.jsonSchreiben("fehler.json", fehlerListe.slice(-50));

  const geloescht = hosting.aufraeumen();
  if (geloescht) hosting.commit(`Alte Bilder entfernt (${geloescht} Tage)`);
  planSpeichern(hosting, plan);
  hosting.commit(`Zustand ${datum}`);
  await hosting.push();
  if (trocken && ig.protokoll.length) fs.writeFileSync(path.join(AUSGABE, "trockenlauf.json"), JSON.stringify(ig.protokoll, null, 2));
  log(`Fertig · ${plan.beitraege.filter((b) => b.status === "veroeffentlicht").length}/${plan.beitraege.length} Beiträge, ${plan.stories.filter((s) => s.status === "veroeffentlicht").length}/${plan.stories.length} Stories · Fehler: ${fehler}`);
  if (fehler) process.exitCode = 1;
}

/* Auffüllen: n Beiträge am Stück veröffentlichen (Feed füllen). Fortschritt in
   state/auffuellen.json – ein Abbruch (z. B. leeres Guthaben) wird beim nächsten
   Aufruf mit derselben Zahl fortgesetzt. Keine Reels, keine Stories. */
async function auffuellenLauf(ziel, { hosting, ledger, ledgerPfad, pool, poolIndex, strategie, maxJeLauf = Infinity }) {
  const stand = hosting.jsonLesen("auffuellen.json", { ziel: 0, fertig: 0, seed: datum });
  if (stand.ziel !== ziel) { stand.ziel = ziel; stand.fertig = Math.min(stand.fertig, ziel); stand.seed = stand.seed || datum; }
  if (stand.fertig >= ziel) { log(`Auffüllen: ${ziel} Beiträge sind bereits veröffentlicht.`); return; }
  const ig = new Instagram({ trockenlauf: trocken, tresorDatei: path.join(hosting.stateDir, "token.enc") });
  if (!trocken) { ig.tresorLaden(); const { konto, limit } = await ig.pruefen(); log(`Auffüllen ${stand.fertig}/${ziel} · @${konto.username} · Kontingent ${limit.genutzt}/${limit.maximum}`); if (limit.maximum - limit.genutzt < 3) { log("Tageskontingent erschöpft – später weiter."); return; } }
  const plan = auffuellplan(ziel, ledger, pool, stand.seed);
  let fehler = 0, versuche = 0, limitPausen = 0, budgetStopp = false;
  const grenze = Math.min(ziel, stand.fertig + maxJeLauf);
  for (let i = stand.fertig; i < grenze; i++) {
    const eintrag = plan[i];
    const slot = `${datum}-${eintrag.slot}`;
    try {
      const variante = (CONFIG.marke.farbeJeKlausur ? 0 : await varianteErmitteln({ ig, ledger, trocken, log }));
      log(`Auffüllen ${i + 1}/${ziel}: ${eintrag.format} · ${eintrag.thema.titel}`);
      let beitrag = hosting.jsonLesen(`inhalte/${slot}.json`, null);
      if (!beitrag) {
        beitrag = await beitragSchreiben({ format: eintrag.format, thema: eintrag.thema, datum, strategie });
        beitrag.slug = slot;
        hosting.jsonSchreiben(`inhalte/${slot}.json`, beitrag);
      }
      const bilder = await beitragRendern(beitrag, path.join(AUSGABE, "auffuellen"), { variante });
      const urls = await hosting.veroeffentlichen(bilder, datum, `Auffüllen ${slot}`);
      const caption = `${beitrag.caption}\n\n${beitrag.hashtags.join(" ")}`;
      const schonDa = await ig.bereitsVeroeffentlicht(caption);
      if (schonDa) log(`  Beitrag steht bereits auf Instagram (${schonDa}) – wird nur vermerkt.`);
      const medienId = schonDa || await ig.beitragPosten({ bildUrls: urls, caption });
      const karteIndex = beitrag.folien.findIndex((f) => f.art === "karte");
      /* Bei einem bereits vorhandenen Beitrag ist die gemessene Variante die des Vorgängers – nicht eintragen. */
      vermerken(ledger, { datum, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, stunde: Math.floor(lokaleMinuten() / 60), format: eintrag.format, thema: beitrag.themaId, fach: beitrag.fach, titel: beitrag.folien[0].titel, hookTyp: beitrag.hookTyp, medienId, variante: schonDa ? null : variante, hashtags: beitrag.hashtags, veroeffentlicht: new Date().toISOString(), karteUrl: karteIndex >= 0 ? urls[karteIndex] : null });
      stand.fertig = i + 1;
      versuche = 0;
      hosting.jsonSchreiben("auffuellen.json", stand);
      ledgerSpeichern(ledgerPfad, ledger);
      hosting.commit(`Auffüllen ${i + 1}/${ziel}`); await hosting.push();
      log(`  ✓ ${medienId}`);
      await verteilen({ art: "beitrag", bildUrls: urls, bildPfade: bilder, titel: beitrag.folien[0].titel, text: caption, hashtags: beitrag.hashtags }, { log, trockenlauf: trocken });
      /* Abstand zwischen den Beiträgen: schont das Stundenlimit der App
         (jede Container-Abfrage zählt) und wirkt weniger wie ein Massenupload. */
      if (i + 1 < grenze && !trocken) await new Promise((r) => setTimeout(r, CONFIG.instagram.auffuellPauseSekunden * 1000));
    } catch (e) {
      console.error(`  ✗ Auffüllen ${i + 1}: ${e.message}`);
      if (e instanceof BudgetFehler) { log(`  ⏸ ${e.message} Auffüllen wird morgen fortgesetzt.`); budgetStopp = true; break; }
      if (/credit|billing|insufficient|402|quota/i.test(e.message)) { console.error("Guthaben oder Kontingent erschöpft – Auffüllen wird beim nächsten Aufruf fortgesetzt."); break; }
      const ratenlimit = /request limit|code (4|17|32|613)\b/i.test(e.message);
      if (ratenlimit) {
        /* Stundenlimit der App: nicht als Fehler zählen, zehn Minuten warten und
           denselben Beitrag (mit gespeichertem Entwurf) noch einmal versuchen. */
        if (limitPausen++ >= 6) { console.error("Ratenlimit hält an – Auffüllen wird beim nächsten Aufruf fortgesetzt."); break; }
        console.error("  Ratenlimit – zehn Minuten Pause, dann weiter."); await new Promise((r) => setTimeout(r, 600000)); i--; continue;
      }
      fehler++;
      if (fehler >= 4) { console.error("Vier Fehler – Auffüllen abgebrochen, Fortsetzung beim nächsten Aufruf."); break; }
      /* Inhaltlich nicht freigegeben: das Thema nicht sofort noch einmal schreiben
         (kostet zwei weitere Entwürfe), sondern zum nächsten übergehen. */
      if (/nicht freigegeben/.test(e.message)) { console.error("  Thema wird übersprungen, kommt später wieder in den Pool."); fs.rmSync(path.join(hosting.stateDir, `inhalte/${slot}.json`), { force: true }); continue; }
      /* Denselben Beitrag noch einmal versuchen, damit kein Platz übersprungen
         wird. Ein gespeicherter Entwurf wird nur verworfen, wenn der Fehler
         nicht von Instagram kam (sonst kostet die Neufassung nur Geld). */
      if (versuche++ < 2) { if (!/^Instagram|Container/.test(e.message)) fs.rmSync(path.join(hosting.stateDir, `inhalte/${slot}.json`), { force: true }); i--; }
    }
  }
  hosting.commit(`Auffüllen Stand ${stand.fertig}/${ziel}`); await hosting.push();
  log(`Auffüllen: ${stand.fertig}/${ziel} veröffentlicht · Fehler: ${fehler}`);
  if (stand.fertig < grenze && !budgetStopp) process.exitCode = 1;
}

function wochenKennung(iso) {
  const d = new Date(`${iso}T12:00:00Z`);
  const tag = (d.getUTCDay() + 6) % 7;
  d.setUTCDate(d.getUTCDate() - tag + 3);
  const erster = new Date(Date.UTC(d.getUTCFullYear(), 0, 4));
  const kw = 1 + Math.round(((d - erster) / 86400000 - 3 + ((erster.getUTCDay() + 6) % 7)) / 7);
  return `${d.getUTCFullYear()}-W${String(kw).padStart(2, "0")}`;
}
function vorwoche(iso) { return new Date(new Date(`${iso}T12:00:00Z`).getTime() - 7 * 86400000).toISOString().slice(0, 10); }
function berichtHinweise(strategie = null) {
  const h = [];
  /* Wachstum: was die API nicht kann, muss von Hand passieren – der Bericht sagt, was fehlt. */
  const profil = strategie?.profil;
  if (profil && !profil.bio) h.push("Profil ohne Bio – Vorschlag: „Examensvorbereitung, sortiert nach Klausurtag · täglich Prüfungsfragen, Schemata, Reels“.");
  if (profil && !profil.bild) h.push("Kein Profilbild gesetzt – ohne Bild folgt fast niemand.");
  if (!CONFIG.verteilen.threads.token) h.push("Threads nicht verbunden – kostenlose Zweitreichweite mit demselben Meta-Login (README, Abschnitt Weiterverteilen).");
  if (!CONFIG.verteilen.tiktok?.refreshToken && !CONFIG.verteilen.youtube?.refreshToken) h.push("Reels laufen nur auf Instagram – TikTok/YouTube Shorts verdoppeln die Chance auf neue Follower (README).");
  if ((strategie?.follower ?? 0) < 50) h.push("Unter 50 Followern greift der Algorithmus kaum: 10 Minuten am Tag von Hand unter #steuerberaterexamen kommentieren, Beiträge in 3–5 Lerngruppen (WhatsApp/Telegram) teilen, 20 Kolleg:innen persönlich einladen.");
  if (CONFIG.verteilen.linkedin.token) h.push("LinkedIn-Token läuft nach 60 Tagen ab – bei Fehlern im Bericht erneuern.");
  if (!CONFIG.reel.elevenlabsKey) h.push("Reels sprechen mit der kostenlosen Piper-Stimme; ElevenLabs-Schlüssel schaltet die natürlichere Stimme frei.");
  return h;
}

main()
  .catch((e) => {
    console.error(e);
    if (/access blocked|code 200\b/i.test(e.message || "")) console.error("\nMeta hat den API-Zugriff der App gesperrt („API access blocked“). Das lässt sich nur im Meta-App-Dashboard klären (Benachrichtigungen/„Alerts“, App-Review → Einschränkungen, ggf. Einspruch) bzw. in der Instagram-App unter Kontostatus. Der Bot versucht es stündlich weiter und läuft von selbst wieder an, sobald die Sperre aufgehoben ist.");
    process.exitCode = 1;
  })
  .finally(() => browserBeenden());
