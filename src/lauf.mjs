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
import { mindsetThema } from "./kalender.mjs";
import { stickerFarbe } from "./stile.mjs";
import { zeitStatistik } from "./zeiten.mjs";
import { themenpool, KLAUSUREN } from "./inhalte.mjs";
import { tagesplan, auffuellplan, ledgerLaden, ledgerSpeichern, vermerken, uebertragen, FORMAT_QUELLEN } from "./planer.mjs";
import { pruefeBeitrag, benutzteFirmen, namenSperren, quizBefunde, quizReihenfolge, storyFreigabe } from "./pruefung.mjs";
import { beitragSchreiben, storiesSchreiben, storiesPruefen, teaserAusBeitrag, bildregieSicher, aktuellRecherchieren, loesungsRecherchieren, reelSchreiben, entwurfsspeicher, entwuerfeAufraeumen } from "./autor.mjs";
import { reelBauen, layoutFuer } from "./reel.mjs";
import { motiveVerteilen } from "./erklaervideo.mjs";
import { beitragRendern, storyRendern, storyRendernInteraktiv, browserBeenden } from "./render.mjs";
import { interaktivGeplant, interaktivPosten, umfrageBauen, sperreAktiv } from "./interaktiv.mjs";
import { Instagram } from "./instagram.mjs";
import { Hosting } from "./hosting.mjs";
import { kommentareBeantworten } from "./interaktion.mjs";
import { nachrichtenBeantworten } from "./postfach.mjs";
import { lernschleife } from "./insights.mjs";
import { verteilen } from "./verteilen.mjs";
import { varianteErmitteln } from "./wechsel.mjs";
import { kartenVerschicken } from "./nachrichten.mjs";
import { berichtErstellen, berichtSenden } from "./bericht.mjs";
import { abschluss as kostenAbschluss, budgetSetzen, reservieren, reelReserve, erwartet, vortagsSchaetzung, reservierungAufheben, tagesStand, tagesLimit, antwortStand, antwortLimit, bezahlbareSumme, runden, postenBeginnen, postenBeenden, postenAktiv, PostenFehler, BudgetFehler } from "./kosten.mjs";
import { stimmeStandVerbinden, stimmeStand, stimmeIstGesperrt } from "./stimme.mjs";
import { kandidatenSuchen, stimmeUebernehmen, stimmeWaehlen, gewinner, stimmenStatistik } from "./stimmen.mjs";
import { titelbild } from "./bilder.mjs";
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
/* Was ein Lauf bezahlt hat, muss er auch sichern - selbst dann, wenn er nichts
   veroeffentlicht und selbst dann, wenn er mit einem Fehler endet.

   Am 18.09. fehlte genau das. Die Zeile "Nichts faellig" stand VOR dem Block,
   der den Zustand festschreibt, und kehrte mit `return` zurueck. Zwei Laeufe
   schrieben denselben Beitrag fuer zusammen 0,166 $; weil sie nichts
   veroeffentlichten, landeten weder der bezahlte Entwurf noch die Kosten im
   Asset-Zweig. Der naechste Lauf fand keinen Entwurf, schrieb ihn noch einmal
   und bezahlte noch einmal - und der Tagesdeckel rechnete die ganze Zeit mit
   einem Stand, der 0,17 $ zu niedrig war.

   Die Funktion haengt deshalb nicht mehr im Ablauf von main(), sondern wird
   dort einmal gesetzt und am Ende des Prozesses in jedem Fall aufgerufen. Sie
   sichert genau einmal; ein zweiter Aufruf tut nichts, damit die Wochenkosten
   nicht doppelt gezaehlt werden. */
let zustandSichern = async () => {};
let zustandGesichert = false;

function planSpeichern(hosting, plan) {
  hosting.jsonSchreiben(`plaene/${plan.datum}.json`, plan);
}

/* Bildnachweis fuer die Caption. Pexels verlangt einen sichtbaren Hinweis auf
   die Quelle; auf der Kachel stoert er, in der Caption nicht. */
function bildnachweis(beitrag) {
  const q = beitrag?.folien?.find((f) => f.art === "titel")?.bildQuelle;
  return q ? `\n\n${q}` : "";
}

/* Motiv für Reel-Cover oder Story: dieselbe Suche wie für die Titelfolie
   (bildSzene → Pexels → freistellen), abgelegt am Objekt selbst. */
/* Verzeichnis der archivierten Motive. Steht erst fest, wenn der Asset-Zweig
   ausgecheckt ist - bis dahin null, dann wird nichts archiviert. */
let motivArchivDir = null;

/* Welches Rechtsgebiet fehlt dem Tag noch? Zwei der drei Beitraege bekommen
   ihr Gebiet fest zugeteilt (planer.mjs); „aktuell" hat keines, weil es der
   Nachrichtenlage folgt. Das uebrige Gebiet geht als Wunsch in die Recherche -
   so zeigt auch der Mittwoch moeglichst alle drei Farben. */
function fehlendesGebiet(plan) {
  const belegt = new Set((plan?.beitraege || []).map((b) => b.thema?.klausur).filter(Boolean));
  const offen = [1, 2, 3].filter((g) => !belegt.has(g));
  return offen.length === 1 ? KLAUSUREN[offen[0]]?.label || null : null;
}

async function motivBesorgen(ziel, was = "Motiv", opt = {}) {
  if (!ziel || ziel.bild || !ziel.bildSzene) return;
  try {
    const treffer = await titelbild(ziel, null, { randFarbe: stickerFarbe(ziel.klausur, CONFIG.marke.stil), archivDir: motivArchivDir, datum, ...opt });
    if (treffer) { ziel.bild = treffer.bild; ziel.bildQuelle = treffer.quelle; ziel.bildFrei = treffer.frei !== false; ziel.bildBreite = treffer.breite || null; ziel.bildHoehe = treffer.hoehe || null; }
  } catch (e) { console.warn(`  ! ${was}: ${e.message}`); }
}

/**
 * Motive fuer das Erklaervideo: je Szene eine Figur. Anders als beim Cover
 * bekommen sie keinen Stickerrand - sie stehen gross und angeschnitten auf
 * der Buehne, ein weisser Saum saehe dort aus wie ein Ausschneidefehler.
 *
 * Der Deckel je Reel ist der eigentliche Punkt: Vier Motive kosten vier Cent,
 * acht waeren die Haelfte des Tagesbudgets. Was darueber hinausgeht, nimmt
 * eine Figur aus einer frueheren Szene desselben Reels - im Vorbild taucht
 * dieselbe Figur ohnehin mehrfach auf. Motive aus dem Archiv kosten nichts
 * und zaehlen deshalb nicht gegen den Deckel.
 */
async function erklaerMotive(reel) {
  const deckel = Math.max(0, CONFIG.reel.erklaerBilder);
  let gezeichnet = 0;
  for (const szene of reel.szenen) {
    if (szene.bild || !szene.bildSzene) continue;
    const vorher = tagesStand();
    /* Ist der Deckel erreicht, wird weiter im Archiv gesucht, aber nicht mehr
       gezeichnet. Ein passendes altes Motiv kostet nichts und trifft das
       Thema - die wiederholte Figur der Nachbarszene tut das nicht. */
    await motivBesorgen(szene, "Erklärbild", { randFarbe: null, nurArchiv: gezeichnet >= deckel, zweck: "erklaerbild" });
    if (szene.bild && tagesStand() > vorher) gezeichnet++;
  }
  return motiveVerteilen(reel.szenen);
}

/* Setzt das Foto auf die Titelfolie, sofern eines gefunden wird. */
async function titelfolieBebildern(beitrag) {
  const titelfolie = beitrag?.folien?.find((f) => f.art === "titel");
  if (!titelfolie || titelfolie.bild) return;
  try {
    const treffer = await titelbild(beitrag, null, { randFarbe: stickerFarbe(beitrag.klausur, CONFIG.marke.stil), archivDir: motivArchivDir, datum });
    if (treffer) { titelfolie.bild = treffer.bild; titelfolie.bildQuelle = treffer.quelle; titelfolie.bildFrei = treffer.frei !== false; titelfolie.bildBreite = treffer.breite || null; titelfolie.bildHoehe = treffer.hoehe || null; }
  } catch (e) { console.warn(`  ! Titelbild: ${e.message}`); }
}

async function main() {
  log(`Instagram-Bot · ${datum} · Stil ${CONFIG.marke.stil} · ${trocken ? "TROCKENLAUF" : "live"}`);

  /* IG_NO_PUSH=true: nichts in den Assets-Zweig pushen – für Trockenläufe
     gegen eine Kopie des Zustands. Ein Trockenlauf am 13.09. hatte sonst
     Beispieltexte für den Folgetag in den echten Zweig geschoben. */
  const hosting = new Hosting({ pushen: !nurPlanen && process.env.IG_NO_PUSH !== "true" }).vorbereiten();
  motivArchivDir = path.join(hosting.stateDir, "motive");
  /* Bezahlte Entwürfe überleben den Lauf, in dem sie entstanden sind - siehe
     autor.mjs. Aufgeräumt wird gleich zu Beginn, damit der Zweig nicht wächst. */
  entwurfsspeicher(path.join(hosting.stateDir, "entwuerfe"));
  entwuerfeAufraeumen();
  const ledgerPfad = path.join(hosting.stateDir, "ledger.json");

  /* Erfundene Firmennamen früherer Beiträge sperren: Der Autor bekommt sie
     als Sperrliste, die Prüfung weist Wiederholungen ab. So gibt es keine
     Haus-Firma, die in jedem zweiten Beitrag auftaucht. */
  const alteFirmen = benutzteFirmen(path.join(hosting.stateDir, "inhalte"), datum);
  if (alteFirmen.length) namenSperren(alteFirmen);

  /* Tagesdeckel: bisheriger Verbrauch des Tages aus state/kosten.json, jeder
     weitere Aufruf wird sofort dort festgehalten. */
  const kostenStart = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} });
  /* Ausnahmen vom Tagesdeckel, je Datum, im Zustand des Kanals
     (state/budget-ausnahmen.json, etwa { "2026-09-13": 0.40 }). Für genau
     einen Tag, danach gilt wieder der Deckel aus der Konfiguration. */
  const ausnahmen = hosting.jsonLesen("budget-ausnahmen.json", {});
  const tagesLimitUsd = Number(ausnahmen?.[datum]) > 0 ? Number(ausnahmen[datum]) : CONFIG.ki.tagesBudgetUsd;
  if (tagesLimitUsd !== CONFIG.ki.tagesBudgetUsd) log(`  Tagesdeckel heute ausnahmsweise ${tagesLimitUsd.toFixed(2)} $ (statt ${CONFIG.ki.tagesBudgetUsd.toFixed(2)} $)`);
  /* Der Antworttopf (Kommentare, Nachrichten) wird getrennt geführt. Ein
     Tageseintrag von vor dieser Trennung hat noch kein Feld `antworten`;
     dann steckt der Betrag im Gesamtwert und wird einmalig herausgerechnet. */
  const heute = kostenStart.tage?.[datum] || {};
  const antwortenBisher = heute.antworten ?? Number(((heute.zwecke?.kommentare || 0) + (heute.zwecke?.nachrichten || 0)).toFixed(4));
  const inhaltBisher = heute.antworten != null ? (heute.usd || 0) : Math.max(0, (heute.usd || 0) - antwortenBisher);
  budgetSetzen({
    limitUsd: tagesLimitUsd,
    antwortLimitUsd: CONFIG.antworten.tagesBudgetUsd,
    bisher: inhaltBisher,
    bisherAntworten: antwortenBisher,
    gemessen: kostenStart.tage?.[datum]?.messungen || {},
    /* Was die Vortage gemessen haben, bis der heutige Lauf eigene Zahlen hat. */
    vortag: vortagsSchaetzung(kostenStart.tage || {}, datum),
    speichern: (usd, aufrufe, zwecke, gemessen, antworten) => {
      const k = hosting.jsonLesen("kosten.json", { wochen: {}, tage: {} }); k.tage = k.tage || {};
      const alt = kostenStart.tage?.[datum] || {};
      const gesamtZwecke = { ...(alt.zwecke || {}) };
      for (const [z, betrag] of Object.entries(zwecke || {})) gesamtZwecke[z] = Number(((alt.zwecke?.[z] || 0) + betrag).toFixed(4));
      const hoechste = { ...(alt.messungen || {}) };
      for (const [z, betrag] of Object.entries(gemessen || {})) hoechste[z] = Number(Math.max(hoechste[z] || 0, betrag).toFixed(4));
      k.tage[datum] = { usd: Number(usd.toFixed(4)), antworten: Number((antworten || 0).toFixed(4)), aufrufe: (alt.aufrufe || 0) + aufrufe, zwecke: gesamtZwecke, messungen: hoechste, stand: new Date().toISOString() };
      hosting.jsonSchreiben("kosten.json", k);
    },
  });
  log(`Tagesbudget: ${tagesStand().toFixed(3)} $ von ${tagesLimit().toFixed(2)} $ verbraucht · Antworten: ${antwortStand().toFixed(3)} $ von ${antwortLimit().toFixed(2)} $`);

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
  /* Gespeicherte Kandidaten aus der Zeit vor der Deutsch-Regel werfen wir
     hier raus. Danach ist die Liste leer und die Suche laeuft neu - sonst
     spraeche weiter eine englische Stimme, weil die Liste ja „voll" ist. */
  if (CONFIG.reel.nurDeutscheStimme && stimmenListe?.kandidaten?.some((k) => !k.deutsch)) {
    const behalten = stimmenListe.kandidaten.filter((k) => k.deutsch);
    log(`Stimmen: ${stimmenListe.kandidaten.length - behalten.length} nicht deutschsprachige entfernt.`);
    stimmenListe = { ...stimmenListe, kandidaten: behalten, fest: behalten.some((k) => k.id === stimmenListe.fest?.id) ? stimmenListe.fest : null };
    hosting.jsonSchreiben("stimmen.json", stimmenListe);
  }
  /* Findet die Suche nichts, wird sie nicht jeden Tag wiederholt: Ein
     kostenloses Abo bekommt auch morgen keine deutsche Bibliotheksstimme.
     Einmal die Woche nachsehen genuegt - falls der Tarif wechselt. */
  const sucheFaellig = !stimmenListe?.gesucht || (Date.now() - Date.parse(stimmenListe.gesucht)) > 7 * 86400000;
  if (CONFIG.reel.elevenlabsKey && CONFIG.reel.stimmeLernen && !stimmenListe?.kandidaten?.length && sucheFaellig && !stimmeStand().erschoepft) {
    try {
      const roh = await kandidatenSuchen({ anzahl: CONFIG.reel.stimmeAnzahl, abo: stimmeStand().abo });
      const bezahlt = String(stimmeStand().abo || "") !== "free";
      const kandidaten = [];
      for (const k of roh) kandidaten.push(await stimmeUebernehmen(k, { bezahlt }));
      stimmenListe = { gesucht: new Date().toISOString(), kandidaten, fest: null };
      hosting.jsonSchreiben("stimmen.json", stimmenListe);
      if (kandidaten.length) log(`Stimmen gefunden: ${kandidaten.map((k) => `${k.name} (${k.geschlecht || "?"}, ${k.beschreibung || k.einsatz || "–"})`).join(" · ")}`);
      else log("Stimmen: keine deutschsprachige bei ElevenLabs verfügbar – es spricht Piper (de_DE-thorsten-high).");
    } catch (e) { console.warn(`  ! Stimmensuche fehlgeschlagen: ${e.message}`); }
  }
  const ledger = ledgerLaden(ledgerPfad);
  const pool = themenpool();
  const poolIndex = new Map(pool.map((t) => [t.id, t]));
  /* Themen auflösen: Die Mindset-Themen des Samstags-Reels stehen im Kalender,
     nicht im Themenpool - der Plan hält nur ihre Kennung. Ohne diesen Umweg
     kam beim Veröffentlichen `undefined` statt eines Themas an, und das Reel
     fiel aus (12.09., erster Samstag mit dieser Regel). */
  const themaFuer = (id) => (id ? poolIndex.get(id) || (String(id).startsWith("mindset") ? mindsetThema(datum) : null) : null);

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
    /* Übertrag von gestern: nicht erschienene Beiträge zuerst. Ein schon
       geschriebener Text zieht mit um und kostet nichts mehr. */
    const gestern = new Date(new Date(`${datum}T12:00:00Z`).getTime() - 86400000).toISOString().slice(0, 10);
    const planGestern = hosting.jsonLesen(`plaene/${gestern}.json`, null);
    for (const { alt, ziel } of uebertragen(plan, planGestern?.trocken ? null : planGestern, gestern)) {
      const text = alt.textFehler ? null : hosting.jsonLesen(`inhalte/${gestern}-${alt.slot}.json`, null);
      if (text) { text.slug = `${datum}-${ziel.slot}`; hosting.jsonSchreiben(`inhalte/${datum}-${ziel.slot}.json`, text); }
      log(`  Übertrag von gestern: ${alt.format} „${alt.themaTitel || alt.slot}“ → ${ziel.slot} ${ziel.zeit}${text ? " (Text vorhanden)" : ""}`);
    }
    planSpeichern(hosting, plan);
    log(`Tagesplan erzeugt: ${plan.beitraege.length} Beiträge, ${plan.stories.length} Stories`);
    if (CONFIG.plan.zeitLernen) {
      const zs = zeitStatistik(ledger);
      log(`  Uhrzeiten: ${zs.gesamt ? `aus ${zs.gesamt} gemessenen Beiträgen gelernt` : "noch ohne Messungen"}${zs.gesamt < 20 ? ", weitere Stunden werden ausprobiert" : ""}`);
    }
  }
  zustandSichern = async (nachricht = `Zustand ${datum}`) => {
    if (zustandGesichert) return;
    zustandGesichert = true;
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
    hosting.commit(nachricht);
    await hosting.push();
  };

  if (nurPlanen) {
    for (const b of plan.beitraege) log(`  ${b.zeit} Beitrag ${b.slot} ${b.format} ${b.themaTitel || ""} [${b.status}]`);
    for (const s of plan.stories) log(`  ${s.zeit} Story ${s.slot} ${s.art} ${s.beitragSlot ? "→ " + s.beitragSlot : themaFuer(s.themaId)?.titel || ""} [${s.status}]`);
    return;
  }

  if (auffuellen > 0) { await auffuellenLauf(auffuellen, { hosting, ledger, ledgerPfad, pool, poolIndex, strategie }); return; }

    /* Rücklage für alles, was heute noch zu schreiben ist: Solange ein Beitrag
     oder das Reel keinen Text hat, bleibt sein erwarteter Preis zurückgelegt,
     damit Stories, Interaktion oder Auffüllen ihn nicht aufbrauchen. Am
     13.09. war nur das Reel geschützt – und zwei Beiträge fielen aus. Die
     Rücklage schrumpft mit jedem geschriebenen Text. */
  const textDatei = (b) => `inhalte/${datum}-${b.slot}.json`;
  const textFehlt = (b) => b.status !== "veroeffentlicht" && !b.fehler && !b.textFehler && !hosting.jsonLesen(textDatei(b), null);
  const ruecklageAktualisieren = () => {
    const offen = trocken ? [] : plan.beitraege.filter(textFehlt);
    /* Zurückgelegt wird nur, was vom Rest des Tages auch WIRKLICH bezahlbar
       ist. Am 17.09. lagen 0.13 $ für einen Beitrag und die Erklärfiguren
       zurück, während nur noch 0.045 $ frei waren: Der Beitrag war davon nie
       zu bezahlen, seine Rücklage hat aber die neun Stories blockiert, die
       zusammen weniger gekostet hätten. Geld für etwas Unbezahlbares
       zurückzulegen heißt, es zweimal zu verlieren.

       Deshalb: der Reihe nach aufsummieren und beim ersten Posten abbrechen,
       der nicht mehr hineinpasst. Was passt, behält seinen Vorrang - was
       nicht passt, gibt den Rest für das Billigere frei. */
    const freiJetzt = Math.max(0, tagesLimit() - tagesStand());
    const preisFuer = (b) => (b.format === "reel"
      ? reelReserve(kostenStart.tage, CONFIG.ki.reelReserveUsd)
      : erwartet("autor") + erwartet("faktencheck"));
    let summe = bezahlbareSumme(offen.map(preisFuer), freiJetzt);
    /* Die Rücklage gehört den Beiträgen, die heute noch geschrieben werden
       müssen - und nur ihnen. „recherche" stand hier bis zum 16.09. mit in
       der Liste; an dem Tag hat ein einziger Recherche-Aufruf die Rücklage
       aufgebraucht und danach fielen auf beiden Kanälen ALLE Beiträge und
       Stories aus. Eine Recherche schmückt einen Beitrag; ein Beitrag ohne
       Recherche erscheint trotzdem. Deshalb darf sie nur von dem leben, was
       über der Rücklage frei ist. */
    /* Das Erklaervideo lebt von seinen Figuren: Fehlt das Geld fuer die
       Motive, baut reelBauen() still das klassische Layout - am 16.09. genau
       so passiert. Solange das Reel des Tages aussteht und das Erklaer-Layout
       gilt, bleibt sein Bildbudget zurueckgelegt. */
    const erklaerOffen = !trocken && layoutFuer(datum) === "erklaer"
      && plan.beitraege.some((b) => b.format === "reel" && b.status !== "veroeffentlicht" && !b.fehler);
    const erklaerPreis = CONFIG.reel.erklaerBilder * erwartet("erklaerbild");
    if (erklaerOffen && summe + erklaerPreis <= freiJetzt) summe = runden(summe + erklaerPreis);
    if (summe > 0) reservieren(summe, ["autor", "faktencheck", "reel", "reel-faktencheck", "erklaerbild", "bildregie"], `${offen.length} noch zu schreibende Beiträge${erklaerOffen && summe >= erklaerPreis ? " und die Figuren des Erklärvideos" : ""}`, "beitraege");
    else reservierungAufheben("beitraege");

    /* Eigener Topf für die Stories - und das ist der Kern der Reparatur vom
       17.09. Bisher hatten nur die Beiträge eine Rücklage; die Stories lebten
       von dem, was übrig blieb. Ein Beitrag, der sich verteuert, hat sie
       damit einfach mitgegessen: An dem Tag kosteten drei Faktencheck-Runden
       für EINEN Beitrag 0.19 $, und alle neun Stories fielen aus.
       Ein Topf, den die Beiträge nicht öffnen können, verhindert das. */
    const storyStand = trocken ? [] : (plan.stories || [])
      .filter((st) => st.art !== "teaser" && st.status !== "veroeffentlicht")
      .map((st) => hosting.jsonLesen(`inhalte/${datum}-${st.slot}.json`, null));
    const ungeschrieben = storyStand.filter((v) => !v).length;
    /* Geschrieben, aber noch nicht geprüft - und das ist der Fall, den die
       erste Fassung dieses Topfes übersehen hat. Am 17.09. um 07:46 waren
       sechs Story-Texte bezahlt und fertig, der Topf war damit aufgehoben,
       und der Faktencheck hatte nichts mehr, wovon er leben konnte. Ein Text
       ohne Prüfung wird nie veröffentlicht: Das Geld für das Schreiben wäre
       verbrannt gewesen. Der Topf hält deshalb bis zur PRÜFUNG, nicht bis
       zum Text. */
    const ungeprueft = storyStand.filter((v) => v && v.faktencheckOffen).length;
    const storyWunsch = ungeschrieben
      ? erwartet("stories") + erwartet("story-faktencheck")
      : ungeprueft ? erwartet("story-faktencheck") : 0;
    /* Auch dieser Topf darf nie mehr halten, als überhaupt noch da ist -
       sonst ist es wieder der Fehler, den bezahlbareSumme behebt. */
    const storyPreis = bezahlbareSumme([storyWunsch], Math.max(0, freiJetzt - summe));
    const storyLabel = ungeschrieben
      ? `${ungeschrieben} noch zu schreibende Stories`
      : `${ungeprueft} Story-Texte, deren Prüfung aussteht`;
    if (storyPreis > 0) reservieren(storyPreis, ["stories", "story-faktencheck"], storyLabel, "stories");
    else reservierungAufheben("stories");
    return summe;
  };
  const ruecklage = ruecklageAktualisieren();
  if (ruecklage > 0) log(`  ${ruecklage.toFixed(3)} $ für ${plan.beitraege.filter(textFehlt).length} noch zu schreibende Beiträge zurückgelegt`);

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
    /* Postfach: Direktnachrichten beantworten – ebenfalls bei jedem Lauf.
       Instagram nimmt eine Antwort nur binnen 24 Stunden an, stündlich reicht
       dafür bequem. Fehlt die Berechtigung am Token, kommt der Endpunkt leer
       zurück; das wird gemeldet und der Lauf geht weiter. */
    if (CONFIG.postfach.aktiv) {
      try {
        const r = await nachrichtenBeantworten(ig, ledger, { log, stateDir: hosting.stateDir });
        if (r.beantwortet) { ledgerSpeichern(ledgerPfad, ledger); hosting.commit(`Nachrichten beantwortet ${datum}`); await hosting.push(); }
        log(`Postfach: ${r.beantwortet} Antworten (${r.unterhaltungen} Unterhaltungen, ${r.offen} offen)`);
      } catch (e) {
        if (e instanceof BudgetFehler) log(`  ⏸ ${e.message}`); else console.error(`  ✗ Postfach: ${e.message}`);
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
  /* --- Texte des Tages vorab ---------------------------------------------
     Reel und Beiträge bekommen ihren Text im ersten Lauf des Tages, solange
     das Budget voll ist – nicht erst zur Sendezeit. Was morgens nicht
     bezahlbar ist, weiß man morgens; abends ist es zu spät. Reihenfolge:
     erst das Reel (größte Reichweite), dann die Beiträge nach Uhrzeit.
     Ausnahme: die Lösungsskizze am Klausurtag braucht die Berichte des
     Nachmittags. Geschriebene Texte liegen unter inhalte/ und kosten später
     nichts mehr. */
  /* Themen, die heute schon vergeben sind - damit ein Ausweichbeitrag nicht
     dasselbe Thema nimmt wie ein anderer Slot. */
  const belegteThemen = new Set([...plan.beitraege, ...plan.stories].map((e) => e.themaId).filter(Boolean));
  /* Ein Slot, dessen Recherche nichts hergibt, faellt nicht aus: Er nimmt ein
     Thema aus dem Pool. „aktuell" und „loesungsskizze" leben von der
     Recherche und haben kein eigenes Thema - ohne diesen Ausweg fehlte der
     Beitrag ganz. Am 16.09. war genau das der Fall.

     Zwei Wege fuehren hierher: kein Geld fuer die Recherche (BudgetFehler)
     oder eine Recherche, die sauber nichts gefunden hat. Der zweite Weg ist
     kein Fehler: Lieber ein guter Beitrag aus dem Pool als einer ueber eine
     Neuigkeit ohne Pruefungsbezug. */
  const aufThemenpoolAusweichen = (eintrag) => {
    const frei = pool.filter((t) => !belegteThemen.has(t.id) && (FORMAT_QUELLEN.pruefungsfrage || []).includes(t.typ));
    const ausweich = frei.find(Boolean) || pool.find((t) => !belegteThemen.has(t.id));
    if (!ausweich) return null;
    belegteThemen.add(ausweich.id);
    eintrag.format = "pruefungsfrage";
    eintrag.themaId = ausweich.id;
    log(`  → „pruefungsfrage" statt Recherche: „${ausweich.titel}" - ein Beitrag ohne Recherche ist besser als keiner.`);
    return textBesorgen(eintrag);
  };

  const textBesorgen = async (eintrag) => {
    const vorhanden = hosting.jsonLesen(textDatei(eintrag), null);
    if (vorhanden) return vorhanden;
    /* Die Obergrenze je Beitrag gilt HIER, nicht nur in der Vorab-Schleife:
       textBesorgen läuft auch zur Sendezeit (Lösungsskizze, oder wenn das
       Vorschreiben vorübergehend scheiterte). Ein Ausweichbeitrag ruft
       textBesorgen aus textBesorgen heraus - dann läuft der Posten weiter,
       statt neu zu beginnen, sonst zählte die Recherche davor nicht mit. */
    const eigenerPosten = !postenAktiv();
    /* Das Reel hat eine eigene Obergrenze: laengeres Skript, teurerer
       Pruefer. Ein Deckel, der es planmaessig zurueckstellt, waere keiner. */
    if (eigenerPosten) postenBeginnen(`${eintrag.format === "reel" ? "Reel" : "Beitrag"} ${eintrag.slot}`, eintrag.format === "reel" ? CONFIG.ki.maxJeReelUsd : CONFIG.ki.maxJeBeitragUsd);
    try {
      return await textSchreiben(eintrag);
    } finally {
      if (eigenerPosten) postenBeenden();
    }
  };
  const textSchreiben = async (eintrag) => {
    const thema = themaFuer(eintrag.themaId);
    let text;
    if (eintrag.format === "reel") {
      text = await reelSchreiben({ thema, datum, lang: Boolean(eintrag.lang), anlass: plan.anlass, strategie });
    } else {
      let recherche = null, wochenThemen = null;
      if (eintrag.format === "aktuell" || eintrag.format === "loesungsskizze") {
        const bisher = (ledger.veroeffentlicht || []).filter((e) => e.format === "aktuell").slice(-12).map((e) => e.titel);
        try {
          recherche = eintrag.format === "loesungsskizze"
            ? await loesungsRecherchieren(datum, eintrag.anlass || plan.abendAnlass)
            : await aktuellRecherchieren(datum, bisher, fehlendesGebiet(plan));
          /* „KEINE_NEUIGKEIT" ist die verabredete Antwort fuer: nichts
             gefunden, was den Massstab haelt. Ebenso zaehlt ein Ergebnis
             ohne jede Quelle - daraus laesst sich kein belegter Beitrag
             bauen. Beides fuehrt sofort auf den Themenpool, statt einen
             duennen Beitrag zu erzwingen. */
          const leer = /KEINE_NEUIGKEIT/i.test(recherche.notizen || "") || !recherche.quellen.length;
          if (leer) {
            log(`  Recherche ohne verwertbares Ergebnis${/KEINE_NEUIGKEIT/i.test(recherche.notizen || "") ? " (nichts mit Prüfungsbezug gefunden)" : " (keine Quellen)"}.`);
            const ersatz = aufThemenpoolAusweichen(eintrag);
            if (ersatz) return ersatz;
          } else log(`  Recherche: ${recherche.titel || "(ohne Titel)"} · ${recherche.quellen.length} Quellen`);
        } catch (e) {
          if (!(e instanceof BudgetFehler)) throw e;
          /* Kein Geld für die Recherche - aber ein Beitrag ohne Recherche ist
             besser als kein Beitrag. „aktuell" und „loesungsskizze" leben von
             ihr und haben kein eigenes Thema; also weicht der Slot auf ein
             Format aus, das sich aus dem Themenpool bedient.

             Am 16.09. fehlte genau das: Die Recherche verbrauchte den Tag,
             danach warf sie einen BudgetFehler, der durch textBesorgen nach
             oben durchschlug - und der Beitrag fiel ersatzlos aus. */
          log(`  ⏸ ${e.message}`);
          const ersatz = aufThemenpoolAusweichen(eintrag);
          if (!ersatz) throw e;
          return ersatz;
        }
      }
      if (eintrag.format === "wochenrueckblick") {
        const grenze = new Date(new Date(`${datum}T12:00:00Z`).getTime() - 7 * 86400000).toISOString().slice(0, 10);
        wochenThemen = (ledger.veroeffentlicht || []).filter((e) => e.art === "beitrag" && e.datum >= grenze).map((e) => e.titel);
        if (!wochenThemen.length) wochenThemen = pool.filter((t) => t.prioritaet === "hoch").slice(0, 5).map((t) => t.titel);
      }
      text = await beitragSchreiben({ format: eintrag.format, thema, datum, recherche, wochenThemen, anlass: eintrag.format === "anlass" ? plan.anlass : eintrag.format === "loesungsskizze" ? plan.abendAnlass : null, strategie });
    }
    text.slug = `${datum}-${eintrag.slot}`;
    hosting.jsonSchreiben(textDatei(eintrag), text);
    ruecklageAktualisieren();
    return text;
  };
  const vorab = plan.beitraege.filter((b) => textFehlt(b) && b.format !== "loesungsskizze").sort((a, b) => (a.format === "reel" ? -1 : 0) - (b.format === "reel" ? -1 : 0));
  let vorabGeschrieben = 0, vorabGescheitert = 0;
  for (const eintrag of vorab) {
    try {
      log(`Text vorab: ${eintrag.format === "reel" ? "Reel" : "Beitrag"} ${eintrag.slot} ${eintrag.themaTitel || ""}`);
      await textBesorgen(eintrag);
      vorabGeschrieben++;
    } catch (e) {
      /* Nur DIESER Beitrag ist am Ende, nicht der Tag: weitermachen mit dem
         nächsten. Ein `break` hier hätte am 17.09. nach dem ersten teuren
         Beitrag alles Übrige mitgerissen. */
      if (e instanceof PostenFehler) { log(`  ⏸ ${e.message}`); continue; }
      if (e instanceof BudgetFehler) { log(`  ⏸ ${e.message}`); break; }
      /* Nach allen Versuchen nicht freigegeben: heute nicht noch einmal
         bezahlen – morgen mit frischem Entwurf, der Plan trägt ihn über.
         Alles andere (Netz, API) ist vorübergehend: der nächste Lauf
         versucht es wieder, ohne dass etwas verloren ist. */
      if (/nicht freigegeben/.test(e.message)) {
        eintrag.textFehler = `${new Date().toISOString()} ${e.message}`;
        eintrag.fehler = eintrag.textFehler;
        vorabGescheitert++;
      }
      console.error(`  ✗ Text ${eintrag.slot}: ${e.message.split("\n")[0]}`);
    }
  }
  if (vorabGeschrieben || vorabGescheitert) {
    planSpeichern(hosting, plan);
    hosting.commit(`Texte ${datum} vorab (${vorabGeschrieben})`); await hosting.push();
  }

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
        const auftrag = (liste) => liste.map((s) => ({ slot: s.slot, art: s.art, thema: themaFuer(s.themaId), tageBisExamen: s.tageBisExamen }));
        const neu = await storiesSchreiben(auftrag(offen), datum);
        for (const s of neu) { hosting.jsonSchreiben(`inhalte/${datum}-${s.slot}.json`, s); geschrieben.set(s.slot, s); }
        log(`  Story-Texte für ${neu.length} Slots geschrieben`);
        /* Beanstandete Slots einmal neu schreiben statt sie zu verlieren: ein
           Nachschlag für zwei, drei Slots kostet nur wenige Cent. */
        hosting.commit(`Story-Texte ${datum}`);
        const alleBefunde = (s) => [...(s.beanstandet || []), ...(s.beanstandetFachlich || [])];
        const strittig = neu.filter((s) => alleBefunde(s).length);
        if (strittig.length) try {
          const hinweis = `Die folgenden Entwürfe wurden abgelehnt – formuliere sie vollständig neu:\n${strittig.map((s) => `- Slot ${s.slot}: ${alleBefunde(s).join("; ")}`).join("\n")}`;
          log(`  ${strittig.length} Story-Entwürfe beanstandet – zweiter Versuch`);
          const zweite = await storiesSchreiben(auftrag(offen.filter((o) => strittig.some((s) => s.slot === o.slot))), datum, hinweis);
          for (const s of zweite) {
            const vorher = geschrieben.get(s.slot);
            if (alleBefunde(s).length && vorher && !alleBefunde(vorher).length) continue;
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
    /* Texte, die geschrieben und bezahlt sind, deren Faktencheck aber am
       Budget scheiterte, liegen unter inhalte/ und tragen `faktencheckOffen`.
       Sie werden hier nachgeprüft - das kostet nur die Prüfung, nicht das
       Schreiben. Klappt es wieder nicht, warten sie auf den nächsten Lauf. */
    const ungeprueft = [...geschrieben.values()].filter((s) => s.faktencheckOffen);
    if (ungeprueft.length) {
      /* Erst neu rechnen, dann prüfen. Die Rücklage stammt sonst aus der Zeit
         VOR dem Schreiben der Texte und hält Geld für Dinge zurück, die
         inzwischen unbezahlbar geworden sind - am 17.09. lagen so 0.04 $ für
         die Erklärfiguren fest, während nur 0.035 $ frei waren, und der
         Faktencheck der sechs fertigen Stories kam nicht mehr durch. */
      ruecklageAktualisieren();
      log(`  ${ungeprueft.length} Story-Texte warten auf ihren Faktencheck – wird nachgeholt`);
      try {
        await storiesPruefen(ungeprueft);
        for (const s of ungeprueft) hosting.jsonSchreiben(`inhalte/${datum}-${s.slot}.json`, s);
        hosting.commit(`Story-Faktencheck nachgeholt ${datum}`);
      } catch (e) {
        if (e instanceof BudgetFehler) log(`  ⏸ ${e.message}`);
        else { fehler++; console.error(`  ✗ Story-Faktencheck nachholen: ${e.message}`); }
      }
    }
  }

  /* Dann die Beiträge (wichtiger), zuletzt die Stories veröffentlichen. */
  for (const eintrag of beitraegeFaellig) {
    if (frei() <= 0) { log("Tageskontingent erschöpft – Beitrag verschoben."); break; }
    if (eintrag.textFehler && !hosting.jsonLesen(textDatei(eintrag), null)) continue;
    try {
      log(`Beitrag ${eintrag.slot} (${eintrag.format}) ${eintrag.themaTitel || ""}`);
      if (eintrag.format === "reel") {
        const reel = await textBesorgen(eintrag);
        const varianteReel = (CONFIG.marke.farbeJeKlausur ? 0 : await varianteErmitteln({ ig, ledger, trocken, log }));
        const gewaehlteStimme = stimmeWaehlen({ kandidaten: stimmenListe?.kandidaten || [], ledger, datum, fest: stimmenListe?.fest || null });
        await motivBesorgen(reel, "Reel-Cover");
        /* Das Erklaervideo lebt von den Figuren - ohne sie faellt reelBauen()
           auf das klassische Layout zurueck. Deshalb erst die Motive, dann
           bauen. */
        const layout = layoutFuer(datum);
        if (layout === "erklaer") {
          /* Ein Text, der vor der Bildregie geschrieben wurde (Nachtlauf vor
             dem 17.09.), bekommt sie hier nachgeholt - einmal, dann steht es
             im gespeicherten Text. */
          if (await bildregieSicher(reel)) hosting.jsonSchreiben(textDatei(eintrag), reel);
          const m = await erklaerMotive(reel);
          /* „eigene" zaehlt die verschiedenen Bilder: Je weiter die Zahl unter
             der Szenenzahl liegt, desto oefter musste eine Szene die Figur der
             vorherigen uebernehmen - das faellt beim Zusehen auf. */
          log(`  Erklärvideo: ${m.eigene} verschiedene Motive auf ${m.mit} von ${reel.szenen.length} Szenen.`);
        }
        const r = await reelBauen(reel, path.join(AUSGABE, "reels", eintrag.slot), { variante: varianteReel, datum, layout, hintergrundDir: path.join(hosting.stateDir, "hintergrund"), stimmeId: gewaehlteStimme?.id || null, stimmeName: gewaehlteStimme?.name || null });
        log(`  Reel gebaut: ${r.dauer.toFixed(1)} s · Layout ${r.layout} · Stimme ${r.anbieter}${r.stimmeName ? ` „${r.stimmeName}“` : ""} · Animation ${r.animation}`);
        /* Stimme vom Tarif gesperrt: aus der Liste werfen, beim nächsten Lauf
           wird neu gesucht – sonst bliebe ElevenLabs dauerhaft ungenutzt. */
        if (gewaehlteStimme && stimmeIstGesperrt(gewaehlteStimme.id) && stimmenListe?.kandidaten) {
          stimmenListe = { ...stimmenListe, kandidaten: stimmenListe.kandidaten.filter((k) => k.id !== gewaehlteStimme.id) };
          hosting.jsonSchreiben("stimmen.json", stimmenListe);
          log(`  Stimme „${gewaehlteStimme.name}“ entfernt (Tarif erlaubt sie nicht).`);
        }
        const [videoUrl, coverUrl] = await hosting.veroeffentlichen([r.video, r.cover], datum, `Reel ${datum} ${eintrag.slot}`);
        const caption = `${reel.caption}${reel.bildQuelle ? `\n\n${reel.bildQuelle}` : ""}\n\n${reel.hashtags.join(" ")}`;
        const medienId = await ig.reelPosten({ videoUrl, coverUrl, caption });
        kontingent.genutzt += 1;
        eintrag.status = "veroeffentlicht"; eintrag.medienId = medienId; eintrag.veroeffentlicht = new Date().toISOString();
        vermerken(ledger, { datum, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, stunde: Math.floor(lokaleMinuten() / 60), format: "reel", thema: reel.themaId, fach: reel.fach, titel: reel.szenen[0]?.titel || reel.kurztitel, hookTyp: reel.hookTyp, hookMuster: reel.hookMuster, medienId, variante: varianteReel, hashtags: reel.hashtags, stimmeId: r.stimmeId || null, stimmeName: r.stimmeName || null, layout: r.layout || null, dauer: Math.round(r.dauer * 10) / 10, veroeffentlicht: new Date().toISOString() });
        eintrag.kanaele = await verteilen({ art: "reel", videoUrl, videoPfad: r.video, bildUrls: [coverUrl], titel: reel.kurztitel || reel.szenen[0]?.titel, text: caption, hashtags: reel.hashtags }, { log, trockenlauf: trocken, stateDir: hosting.stateDir });
        fertigeBeitraege.set(eintrag.slot, { ...reel, folien: [{ art: "titel", titel: reel.szenen[0]?.titel, icon: reel.szenen[0]?.icon }], kurztitel: reel.kurztitel });
        ledgerSpeichern(ledgerPfad, ledger); planSpeichern(hosting, plan);
        ruecklageAktualisieren();
        hosting.commit(`Veröffentlicht: Reel ${datum} ${eintrag.slot}`); await hosting.push();
        log(`  ✓ Reel ${medienId} (${r.dauer.toFixed(0)} s, Stimme: ${r.anbieter})`);
        continue;
      }
      const beitrag = await textBesorgen(eintrag);
      const variante = (CONFIG.marke.farbeJeKlausur ? 0 : await varianteErmitteln({ ig, ledger, trocken, log }));
      /* Titelbild: Der Autor hat eine Szene beschrieben, bilder.mjs sucht sie.
         Ohne Treffer bleibt es bei der Icon-Bühne - ein beliebiges Symbolfoto
         waere schlechter als keines. */
      await titelfolieBebildern(beitrag);
      const bilder = await beitragRendern(beitrag, path.join(AUSGABE, "beitraege"), { variante });
      const urls = await hosting.veroeffentlichen(bilder, datum, `Beitrag ${datum} ${eintrag.slot}`);
      const caption = `${beitrag.caption}${bildnachweis(beitrag)}\n\n${beitrag.hashtags.join(" ")}`;
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
      eintrag.kanaele = await verteilen({ art: "beitrag", bildUrls: urls, bildPfade: bilder, titel: beitrag.folien[0].titel, text: caption, hashtags: beitrag.hashtags }, { log, trockenlauf: trocken, stateDir: hosting.stateDir });
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
        /* Eine Stelle entscheidet, ob diese Story erscheinen darf: ungeprüft
           nicht, fachlich beanstandet nicht, und ein Befund ohne Herkunft aus
           dem Altbestand auch nicht. Eine frühere FORMbeanstandung darf nur
           eine erneute Formprüfung aufheben - nie einen fachlichen Befund
           (Safety 0c, Review-Auftrag Abschnitte 13 bis 15). */
        const freigabe = storyFreigabe(story);
        if (!freigabe.frei) {
          log(`Story ${eintrag.slot}: ${freigabe.grund}${freigabe.warten ? " – später." : " – übersprungen."}`);
          if (!freigabe.warten) eintrag.status = "uebersprungen";
          continue;
        }
        if (freigabe.bereinigt) {
          delete story.beanstandet;
          hosting.jsonSchreiben(`inhalte/${datum}-${eintrag.slot}.json`, story);
        }
      }
      /* Safety 0a: Eine Antwort erscheint nie vor ihrer Frage, und nur mit
         ihr zusammen. Geplante Uhrzeiten sind keine Abhaengigkeit - am 16.09.
         stand die Antwort beim Schwesterkanal Minuten VOR der endgueltigen
         Frage im Kanal. Faellt die Frage endgueltig aus, faellt die Antwort
         mit ihr; eine Antwort ohne Frage ist fuer die Lesenden nichts wert.

         Direkt davor noch einmal die Paarpruefung auf dem, was wirklich
         veroeffentlicht wird: Zwischen Schreiben und Senden kann ein
         einzelner Slot neu geschrieben worden sein. */
      if (eintrag.art === "antwort") {
        const ordnung = quizReihenfolge(eintrag, plan.stories);
        if (ordnung.status === "warten") { log(`Story ${eintrag.slot}: ${ordnung.grund} - spaeter.`); continue; }
        if (ordnung.status === "verfallen") {
          log(`Story ${eintrag.slot}: ${ordnung.grund} - die Antwort entfaellt mit ihr.`);
          eintrag.status = "uebersprungen"; continue;
        }
        if (ordnung.frage) {
          const frageText = hosting.jsonLesen(`inhalte/${datum}-${ordnung.frage.slot}.json`, null);
          const paarBefunde = quizBefunde([frageText, story].filter(Boolean));
          if (paarBefunde.length) {
            log(`Story ${eintrag.slot} passt nicht mehr zur Frage ${ordnung.frage.slot}: ${paarBefunde.join(" · ")} - uebersprungen.`);
            eintrag.status = "uebersprungen"; continue;
          }
        }
      } else if (eintrag.art === "frage") {
        const eigene = quizBefunde([story]);
        if (eigene.length) {
          log(`Story ${eintrag.slot} beanstandet: ${eigene.join(" · ")} - uebersprungen.`);
          eintrag.status = "uebersprungen"; continue;
        }
      }

      /* Bild in der Story: nur, wo der Autor eine Szene genannt hat (Begriff,
         Tipp); der Teaser bringt das Bild des Beitrags schon mit. */
      await motivBesorgen(story, "Story-Motiv", { ki: false });
      const zielBild = path.join(AUSGABE, "stories", `${datum}-${eintrag.slot}-${story.art}.jpg`);
      const stilOpt = { variante: varianteStory(eintrag.slot) };

      /* Interaktive Story (native Umfrage) über die private Schnittstelle.
         Sie bekommt ein eigenes Bild, das unten Platz für den Sticker lässt.
         Geht der Weg nicht - Challenge, Bremse, geänderter Endpunkt -, wird
         ganz normal gerendert und über die Graph API veröffentlicht: Eine
         Story fällt nie aus, nur weil der Zusatzweg klemmt. */
      let medienId = null;
      if (!trocken && interaktivGeplant(story) && !sperreAktiv(ledger)) {
        try {
          const { pfad, platz } = await storyRendernInteraktiv(story, zielBild, stilOpt);
          medienId = await interaktivPosten({ bildPfad: pfad, umfrage: umfrageBauen(story, platz), stateDir: hosting.stateDir, ledger, log });
          eintrag.interaktiv = true;
          /* Das Bild geht trotzdem in den Asset-Zweig - instagrapi lädt die
             lokale Datei hoch, aber das Archiv soll lückenlos bleiben. */
          await hosting.veroeffentlichen([pfad], datum, `Story ${datum} ${eintrag.slot} (interaktiv)`);
        } catch (e) {
          console.warn(`  ! Umfrage für Story ${eintrag.slot} nicht gesetzt (${e.art || "fehler"}: ${e.message}) – normale Story folgt.`);
        }
      }

      if (!medienId) {
        const bild = await storyRendern(story, zielBild, stilOpt);
        const [url] = await hosting.veroeffentlichen([bild], datum, `Story ${datum} ${eintrag.slot}`);
        medienId = await ig.storyPosten({ bildUrl: url });
        /* Nur der offizielle Weg zählt auf das Tageskontingent der Graph-API. */
        kontingent.genutzt += 1;
      }
      eintrag.status = "veroeffentlicht";
      eintrag.medienId = medienId;
      eintrag.veroeffentlicht = new Date().toISOString();
      vermerken(ledger, { datum, art: "story", slot: eintrag.slot, storyArt: story.art, thema: story.themaId || eintrag.themaId || null, fach: story.fach, titel: story.titel || story.text || "", medienId, veroeffentlicht: new Date().toISOString() });
      ledgerSpeichern(ledgerPfad, ledger);
      planSpeichern(hosting, plan);
      hosting.commit(`Veröffentlicht: Story ${datum} ${eintrag.slot}`);
      await hosting.push();
      log(`  ✓ Story ${eintrag.slot} ${story.art}${eintrag.interaktiv ? " mit Umfrage" : ""} → ${medienId}`);
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

  await zustandSichern(`Zustand ${datum}`);
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
        postenBeginnen(`Auffüllen ${eintrag.slot}`, CONFIG.ki.maxJeBeitragUsd);
        try { beitrag = await beitragSchreiben({ format: eintrag.format, thema: eintrag.thema, datum, strategie }); }
        finally { postenBeenden(); }
        beitrag.slug = slot;
        hosting.jsonSchreiben(`inhalte/${slot}.json`, beitrag);
      }
      await titelfolieBebildern(beitrag);
      const bilder = await beitragRendern(beitrag, path.join(AUSGABE, "auffuellen"), { variante });
      const urls = await hosting.veroeffentlichen(bilder, datum, `Auffüllen ${slot}`);
      const caption = `${beitrag.caption}${bildnachweis(beitrag)}\n\n${beitrag.hashtags.join(" ")}`;
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
      await verteilen({ art: "beitrag", bildUrls: urls, bildPfade: bilder, titel: beitrag.folien[0].titel, text: caption, hashtags: beitrag.hashtags }, { log, trockenlauf: trocken, stateDir: hosting.stateDir });
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
  /* Letzte Instanz: Auch ein abgebrochener oder fruehzeitig zurueckgekehrter
     Lauf schreibt fest, was er bezahlt hat. Schlaegt das Sichern selbst fehl,
     darf es den urspruenglichen Fehler nicht verdecken. */
  .finally(async () => {
    try { await zustandSichern(); }
    catch (e) { console.error(`  ! Zustand nicht gesichert: ${e.message}`); process.exitCode = 1; }
    browserBeenden();
  });
