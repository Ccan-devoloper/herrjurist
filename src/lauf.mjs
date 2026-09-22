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
import { manuellFinalisiert, tagesinhaltManuellFinalisiert } from "./finalisierung.mjs";
import { istKostenKontrollFehler, budgetStoppGrund } from "./kostenfehler.mjs";
import { mindsetThema } from "./kalender.mjs";
import { stickerFarbe } from "./stile.mjs";
import { zeitStatistik } from "./zeiten.mjs";
import { themenpool, FAECHER, KLAUSUREN, FEED_KATEGORIEN, feedKategorie, feedFolgeErlaubt } from "./inhalte.mjs";
import { tagesplan, auffuellplan, ledgerLaden, ledgerSpeichern, vermerken, uebertragen, FORMAT_QUELLEN } from "./planer.mjs";
import { pruefeBeitrag, benutzteFirmen, namenSperren, quizBefunde, quizPaarFreigabe, storyFreigabe, quizNachschlag, alleBefunde, persistierteStoryBeanstandungen } from "./pruefung.mjs";
import { beitragSchreiben, storiesSchreiben, storiesPruefen, teaserAusBeitrag, bildregieSicher, aktuellRecherchieren, loesungsRecherchieren, reelSchreiben, entwurfsspeicher, entwuerfeAufraeumen } from "./autor.mjs";
import { reelBauen, layoutFuer } from "./reel.mjs";
import { motiveVerteilen } from "./erklaervideo.mjs";
import { beitragRendern, storyRendern, storyRendernInteraktiv, browserBeenden } from "./render.mjs";
import { interaktivGeplant, interaktivPosten, umfrageBauen, sperreAktiv } from "./interaktiv.mjs";
import { Instagram } from "./instagram.mjs";
import { Hosting } from "./hosting.mjs";
import { kommentareBeantworten } from "./interaktion.mjs";
import { nachrichtenBeantworten } from "./postfach.mjs";
import { lernschleife, storyInsightsAktualisieren, medienSnapshotsAktualisieren, kontoSnapshotAktualisieren } from "./insights.mjs";
import { verteilen } from "./verteilen.mjs";
import { varianteErmitteln } from "./wechsel.mjs";
import { kartenVerschicken } from "./nachrichten.mjs";
import { berichtErstellen, berichtSenden } from "./bericht.mjs";
import { abschluss as kostenAbschluss, budgetSetzen, erwartet, vortagsSchaetzung, tagesStand, tagesLimit, antwortStand, antwortLimit, runden, postenBeginnen, postenBeenden, postenAktiv, PostenFehler, BudgetFehler } from "./kosten.mjs";
import { zustandsSicherung } from "./zustand.mjs";
import { budgetStarten, ZWECK_TOPF, AdmissionAbgelehnt, TopfGesperrt } from "./budget.mjs";
import { telemetrieStarten } from "./telemetrie.mjs";
import { journalStarten } from "./journal.mjs";
import { gemeinschaftsBudget } from "./gemeinschaftsbudget.mjs";
import { bestandLaden, bestandInhalt, reserveAufraeumen, reserveEntnehmen, reserveAuffuellen, ersatzZulaessig, BESTAND_DATEI } from "./reservelauf.mjs";
import { themaTauglich, ZIEL_BESTAND, RESERVE_FORMATE, DUBLETTEN_TAGE } from "./reserve.mjs";
import { kontextSetzen, tagesplanAdmissionBedarf } from "./anbieter.mjs";
import { effektiveKonfiguration, richtlinieGate, REGEL_DECKEL } from "./richtlinie.mjs";
import { veroeffentlichungEintragen, veroeffentlichtBestaetigt, planBereinigen, planNurAusTrockenlauf, echteMedienId } from "./veroeffentlichung.mjs";
import { stimmeStandVerbinden, stimmeStand, stimmeIstGesperrt } from "./stimme.mjs";
import { kandidatenSuchen, stimmeUebernehmen, stimmeWaehlen, gewinner, stimmenStatistik } from "./stimmen.mjs";
import { titelbild } from "./bilder.mjs";
import { wochentag } from "./zeit.mjs";
import { heuteIso, lokaleMinuten, minutenVon } from "./zeit.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const args = new Map(process.argv.slice(2).map((a) => { const [k, v] = a.replace(/^--/, "").split("="); return [k, v ?? true]; }));
const datum = args.get("datum") || heuteIso();
const vorplanen = args.has("vorplanen");
const nurPlanen = args.has("nur-planen") || vorplanen;
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
   dort einmal gesetzt und am Ende des Prozesses in jedem Fall aufgerufen. Was
   sie genau einmal tut (Kosten) und was sie wiederholen darf (Commit, Push),
   steht in src/zustand.mjs - ein gescheiterter Push wird dort erneut
   versucht, ohne die Wochenkosten ein zweites Mal zu addieren. */
/* Die zugesagte Tagesmenge dieses Kanals. Sie steht hier und nicht in einer
   Umgebungsvariablen, damit eine stille Aenderung auffaellt: Das Gate vor dem
   ersten bezahlten Aufruf vergleicht die effektive Konfiguration dagegen. */
const KANAL = "herrjurist";
const PRODUKT = { reelZusaetzlich: true, beitraegeWerktag: 2, storiesProTag: 9 };

let zustandSichern = async () => {};

/* Was ein Lauf gesendet haette, aber nicht gesendet hat. Steht bewusst nur
   hier im Speicher und landet am Ende in out/<datum>/trockenlauf.json - nicht
   im Tagesplan, den der naechste Livelauf liest. */
const probelaeufe = [];

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
    if (treffer) {
      ziel.bild = treffer.bild; ziel.bildQuelle = treffer.quelle; ziel.bildFrei = treffer.frei !== false;
      ziel.bildBreite = treffer.breite || null; ziel.bildHoehe = treffer.hoehe || null;
      ziel.bildTyp = treffer.typ || null; ziel.bildCharaktere = treffer.charaktere || null;
      ziel.coverHinweisPlan = treffer.coverHinweisPlan || null;
    }
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
  if (!titelfolie) return false;
  /* Alte gespeicherte Cover ohne Herkunftsmarker können aus der früheren
     Flat-Illustrationsphase stammen. Nur explizit fotografische Cover oder
     echte Pexels-Fotos werden unverändert übernommen; alles andere wird
     einmal sauber neu beschafft. */
  if (titelfolie.bild && (titelfolie.bildTyp === "ai-cover" || titelfolie.bildTyp === "charakter" || titelfolie.bildTyp === "foto" || /Pexels/i.test(titelfolie.bildQuelle || ""))) return true;
  if (titelfolie.bild) {
    for (const k of ["bild","bildQuelle","bildFrei","bildBreite","bildHoehe","bildTyp"]) delete titelfolie[k];
  }
  try {
    const treffer = await titelbild(beitrag, null, { randFarbe: stickerFarbe(beitrag.klausur, CONFIG.marke.stil), archivDir: motivArchivDir, datum, aiFirstCover: true });
    if (!treffer) return false;
    titelfolie.bild = treffer.bild;
    titelfolie.bildQuelle = treffer.quelle;
    titelfolie.bildFrei = treffer.frei !== false;
    titelfolie.bildBreite = treffer.breite || null;
    titelfolie.bildHoehe = treffer.hoehe || null;
    titelfolie.bildTyp = treffer.typ || "foto";
    titelfolie.bildCharaktere = treffer.charaktere || null;
    titelfolie.coverHinweisPlan = treffer.coverHinweisPlan || null;
    titelfolie.coverQa = treffer.coverQa || null;
    titelfolie.coverQaAttempts = treffer.coverQaAttempts || [];
    titelfolie.bildPrompt = treffer.prompt || null;
    titelfolie.bildKostenUsd = treffer.kostenUsd ?? null;
    return true;
  } catch (e) {
    console.warn(`  ! Titelbild: ${e.message}`);
    return false;
  }
}

async function main() {
  log(`Instagram-Bot · ${datum} · Stil ${CONFIG.marke.stil} · ${trocken ? "TROCKENLAUF" : "live"}`);

  /* IG_NO_PUSH=true: nichts in den Assets-Zweig pushen – für Trockenläufe
     gegen eine Kopie des Zustands. Ein Trockenlauf am 13.09. hatte sonst
     Beispieltexte für den Folgetag in den echten Zweig geschoben. */
  const hosting = new Hosting({ pushen: (vorplanen || !nurPlanen) && process.env.IG_NO_PUSH !== "true" }).vorbereiten();
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

  /* --- Phase 1a: drei Töpfe, effektive Konfiguration, Admission ---------
     Die Datums-Ausnahmen bleiben als Audit-Historie stehen, heben aber
     keinen geplanten Lauf mehr an. Eine Anhebung ist eine manuelle Handlung
     mit Begründung - am 18.09. lief der Bot mit 0,80 $ statt 0,32 $, ohne
     dass an diesem Tag jemand etwas entschieden hätte. */
  const ausloeser = process.env.GITHUB_EVENT_NAME || (process.env.CI ? "unbekannt" : "lokal");
  const konfiguration = effektiveKonfiguration({
    ausloeser, datum, ausnahmen,
    deckel: { core: CONFIG.ki.tagesBudgetUsd, engagement: CONFIG.antworten.tagesBudgetUsd, research: CONFIG.ki.researchBudgetUsd ?? REGEL_DECKEL.research },
    breakGlass: {
      aktiv: String(process.env.IG_BREAK_GLASS || "") === "true",
      betragUsd: Number(process.env.IG_BREAK_GLASS_USD || 0),
      grund: process.env.IG_BREAK_GLASS_GRUND || "",
    },
  });
  for (const h of konfiguration.hinweise) log(`  ${h}`);
  richtlinieGate({
    konfiguration,
    /* Die Produktmenge ist das Versprechen an die Leser, keine Stellschraube
       fuer Kostenprobleme: Herr Jurist 2 Karussells + 1 Reel, Examens Campus
       1 Karussell + 1 Reel, dazu die Stories. Stimmt sie nicht, startet der
       Lauf nicht. */
    produkt: {
      reelZusaetzlich: !!CONFIG.reel?.zusaetzlich,
      beitraegeWerktag: CONFIG.plan.beitraegeWerktag,
      storiesProTag: CONFIG.plan.storiesProTag,
    },
    erwartet: {
      reelZusaetzlich: PRODUKT.reelZusaetzlich,
      beitraegeWerktag: PRODUKT.beitraegeWerktag,
      storiesProTag: PRODUKT.storiesProTag,
    },
    researchSuchen: Math.min(CONFIG.ki.rechercheSuchen ?? 2, 2),
    zwecke: Object.keys(ZWECK_TOPF), zweckTopf: ZWECK_TOPF,
  });

  const tagesLimitUsd = konfiguration.betriebsDeckel.core;
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

  /* Was heute schon ausgegeben wurde, je Topf - aus den Zwecken des Tages. */
  const bisherJeTopf = { core: 0, engagement: 0, research: 0 };
  for (const [zweck, betrag] of Object.entries(heute.zwecke || {})) {
    const topf = ZWECK_TOPF[zweck];
    if (topf) bisherJeTopf[topf] += Number(betrag) || 0;
    else console.warn(`  ! Zweck „${zweck}“ aus dem Tagesstand hat keinen Topf - er zählt gegen keinen Deckel.`);
  }
  const telemetrie = telemetrieStarten({
    datum, kanal: KANAL, dir: AUSGABE, breakGlass: konfiguration.breakGlass.aktiv,
    providerGuardUsd: konfiguration.providerGuardUsd,
  });

  /* Das Budget-Journal: Reservierungen, die diesen Prozess ueberleben.

     Ohne es gilt der Tagesdeckel nur INNERHALB eines Laufs. Stirbt der Runner
     nach dem Senden hart, weiss der naechste Stundenlauf von diesem Geld
     nichts und darf es ein zweites Mal ausgeben - sechzehnmal am Tag ist das
     kein theoretischer Fall. */
  const journal = journalStarten({
    datum, kanal: KANAL,
    lesen: () => hosting.jsonLesen("budget-journal.json", null),
    schreiben: async (inhalt) => {
      hosting.jsonSchreiben("budget-journal.json", inhalt);
      hosting.commit(`Budget-Journal ${datum}`);
      const gepusht = await hosting.push();
      /* Ohne Remote (IG_NO_PUSH) ist die lokale Datei die Durability, die es
         gibt - dann wird sie auch nicht mehr verlangt. */
      return gepusht || hosting.pushen === false;
    },
    remoteNoetig: hosting.pushen !== false,
    /* Der Altbestand aus kosten.json wird EINMAL je Tag eingefroren. Danach
       ist das Journal massgeblich; die Baseline waechst nicht mit, sonst
       zaehlten die abgerechneten Aufrufe des Journals doppelt - sie stehen ja
       auch in kosten.json. Ein max() ueber beide waere bequem und falsch:
       Sind die Mengen disjunkt (0,10 $ davor, 0,08 $ ungeklaert danach), ist
       der wahre Stand 0,18 $ und nicht 0,10 $. */
    legacyBaseline: bisherJeTopf,
  });
  /* Der Vorrat wird zuerst aufgeraeumt: Was abgelaufen ist, fliegt samt
     Bildern raus, bevor irgendetwas darauf zurueckgreift. Kein Nachcheck,
     keine Verlaengerung - Ersatz entsteht spaeter an einem guenstigen Tag. */
  let reserveBestand = bestandLaden(hosting);
  {
    const vorher = reserveBestand.length;
    const auf = reserveAufraeumen({ hosting, bestand: reserveBestand, heute: datum, log });
    reserveBestand = auf.bestand;
    if (auf.entfernt.length) {
      hosting.jsonSchreiben(BESTAND_DATEI, bestandInhalt(reserveBestand, KANAL));
      log(`  Vorrat: ${auf.entfernt.length} von ${vorher} Einträgen verworfen, ${reserveBestand.length} gültig.`);
    }
  }

  const uebernommen = journal.uebernahme();
  if (journal.baselineNeu()) {
    const b = journal.legacyBaseline();
    log(`  Journal fuer ${datum} angelegt · Altbestand eingefroren: Core ${b.core.toFixed(4)} · Engagement ${b.engagement.toFixed(4)} · Research ${b.research.toFixed(4)} $`);
  }
  if (uebernommen.freigegeben.length || uebernommen.blockiert.length) {
    log(`  Journal: ${uebernommen.freigegeben.length} Reservierung(en) aus einem abgebrochenen Lauf freigegeben `
      + `(beweisbar nicht gesendet), ${uebernommen.blockiert.length} bleiben blockiert (gesendet, nie abgerechnet).`);
    for (const e of uebernommen.blockiert) log(`    ! ${e.purpose}${e.slot ? ` (${e.slot})` : ""}: ${e.reservedUsd.toFixed(4)} $ gelten als verbraucht`);
    await journal.abschluss();
  }
  /* Das Journal ist ab hier die eine Quelle: eingefrorener Altbestand plus
     seine eigenen Eintraege. Kein Maximum, keine zweite Rechnung. */
  for (const t of Object.keys(bisherJeTopf)) bisherJeTopf[t] = uebernommen.vorbelastung[t] || 0;

  /* Zugelassen wird bis zur BETRIEBSGRENZE, nicht bis zum Policy-Deckel. Der
     Abstand dazwischen ist der Provider-Guard: Was der Anbieter bei
     Structured Outputs selbst an Systemprompt hinzufuegt, wird berechnet und
     steht in keiner Anfrage, die wir vorher wiegen koennen; und der
     Zaehlendpunkt ist laut Anbieter eine Schaetzung ohne zugesicherte
     Maximalabweichung. Was nicht exakt vorhersagbar ist, bekommt Abstand. */
  const gemeinschaft = trocken
    ? { fremdFrei: { core: 0, engagement: 0, research: 0 }, grund: "Trockenlauf" }
    : await gemeinschaftsBudget({ kanal: KANAL, datum, deckel: konfiguration.betriebsDeckel });
  const budget = budgetStarten({
    deckel: konfiguration.betriebsDeckel, bisher: bisherJeTopf, fremdFrei: gemeinschaft.fremdFrei,
    breakGlass: konfiguration.breakGlass.aktiv, protokoll: () => {},
  });
  kontextSetzen({ budget, telemetrie, journal, kanal: KANAL, datum });
  const fremdSumme = Object.values(gemeinschaft.fremdFrei || {}).reduce((a, b) => a + Number(b || 0), 0);
  if (fremdSumme > 0) {
    log("  Gemeinschaftsbudget: Schwesterkanal pflichtseitig vorbereitet; Pflichtaufrufe dürfen zusätzlich "
      + `Core ${(gemeinschaft.fremdFrei.core || 0).toFixed(4)} · Engagement ${(gemeinschaft.fremdFrei.engagement || 0).toFixed(4)} · `
      + `Research ${(gemeinschaft.fremdFrei.research || 0).toFixed(4)} $ nutzen.`);
  } else {
    log(`  Gemeinschaftsbudget: kein Schwester-Rest freigegeben (${gemeinschaft.grund}).`);
  }
  log(`  Töpfe (Betriebsgrenze, Policy ${konfiguration.deckel.core.toFixed(2)} $ minus Guard ${konfiguration.providerGuardUsd.toFixed(4)} $): `
    + `Core ${bisherJeTopf.core.toFixed(3)}/${konfiguration.betriebsDeckel.core.toFixed(4)} · `
    + `Engagement ${bisherJeTopf.engagement.toFixed(3)}/${konfiguration.betriebsDeckel.engagement.toFixed(4)} · `
    + `Research ${bisherJeTopf.research.toFixed(3)}/${konfiguration.betriebsDeckel.research.toFixed(4)} $`
    + `${konfiguration.breakGlass.aktiv ? ` · BREAK GLASS: „${konfiguration.breakGlass.grund}“` : ""}`);

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
  /* Altbestand in Ordnung bringen, ohne den Tag wegzuwerfen.

     Früher wurde ein Plan mit Trockenlauf-Spuren komplett verworfen und neu
     erzeugt. Das ist zu grob: Stehen daneben echte Veröffentlichungen, gehen
     deren Zustände verloren, und der Bot schickt sie ein zweites Mal hinaus.
     Jetzt wird genau das zurückgesetzt, was keine echte Medien-ID trägt -
     fail closed, Eintrag für Eintrag. Nur ein Plan, der vollständig aus einem
     Trockenlauf stammt und noch nichts Echtes enthält, wird neu erzeugt;
     dabei geht nichts verloren. */
  if (plan && !trocken && planNurAusTrockenlauf(plan)) {
    log("Tagesplan stammt vollständig aus einem Trockenlauf und enthält nichts Veröffentlichtes – wird neu erzeugt.");
    plan = null;
  } else if (plan && !trocken) {
    const { bereinigt, unklar } = planBereinigen(plan);
    for (const b of bereinigt) log(`  ! Slot ${b.slot}: ${b.grund} – gilt wieder als geplant.`);
    /* Ohne Nachweis wird nichts zurückgesetzt: Der Slot könnte erschienen
       sein, und ein zweiter Post ließe sich nicht zurücknehmen. Er bleibt
       gesperrt und steht im Bericht, bis jemand ihn auflöst. */
    for (const u of unklar) {
      console.warn(`  ! Slot ${u.slot}: ${u.grund} – bleibt gesperrt, wird NICHT erneut veröffentlicht.`);
      const eintrag = [...plan.beitraege, ...plan.stories].find((e) => e.slot === u.slot);
      if (eintrag && !eintrag.fehler) eintrag.fehler = `${new Date().toISOString()} Veröffentlichung unbestätigt: ${u.grund}`;
    }
    if (bereinigt.length || unklar.length) { delete plan.trocken; planSpeichern(hosting, plan); }
  }
  if (!plan) {
    const p = tagesplan(datum, ledger, pool, strategie);
    plan = {
      datum: p.datum, erzeugt: new Date().toISOString(), anlass: p.anlass || null, abendAnlass: p.abendAnlass || null, trocken,
      beitraege: p.beitraege.map((b) => ({ slot: b.slot, zeit: b.zeit, format: b.format, themaId: b.thema?.id || null, themaTitel: b.thema?.titel || null, fach: b.thema?.fach || null, klausur: b.klausur ?? null, lang: b.lang, status: "geplant" })),
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
  zustandSichern = zustandsSicherung({
    hosting, plan, datum, kostenAbschluss, wochenKennung, planSpeichern,
    /* Die rollenden Profilfenster gehoeren zum gesicherten Zustand, nicht in
       einen Nachtrag danach: Sie werden innerhalb der Sicherung geschrieben,
       vor Commit und Push, und ueberstehen damit das Ende des Runners. Die
       Rohzeilen bleiben lokal und gehen als Artefakt. */
    vorSichern: () => {
      /* Das Journal schreibt seine offenen Uebergaenge (abgerechnet,
         ungeklaert) hier mit fest - sie durften bis dahin im Speicher
         stehen, weil ihr Verlust nur konservativer, nie riskanter rechnet.

         Und zwar ueber journal.snapshot(), nicht von Hand nachgebaut: Die
         erste Fassung setzte das Objekt hier selbst zusammen und vergass
         legacyBaseline. Der naechste Runner leitete sie dann wieder aus
         kosten.json ab - inklusive der Aufrufe, die im Journal schon
         standen. Ein von Hand nachgebautes Format ist ein Format, das
         auseinanderlaeuft. */
      hosting.jsonSchreiben("budget-journal.json", journal.snapshot());
      hosting.jsonSchreiben(BESTAND_DATEI, bestandInhalt(reserveBestand, KANAL));
      if (!telemetrie?.anzahl?.()) return;
      const bestand = hosting.jsonLesen("profile.json", {});
      hosting.jsonSchreiben("profile.json", telemetrie.fensterFortschreiben(bestand));
    },
  });

  if (nurPlanen) {
    for (const b of plan.beitraege) log(`  ${b.zeit} Beitrag ${b.slot} ${b.format} ${b.themaTitel || ""} [${b.status}]`);
    for (const s of plan.stories) log(`  ${s.zeit} Story ${s.slot} ${s.art} ${s.beitragSlot ? "→ " + s.beitragSlot : themaFuer(s.themaId)?.titel || ""} [${s.status}]`);
    return;
  }

  /* Hybridbetrieb: Der Tagesplan liegt bereits vor, aber vor 07:00 Uhr
     Ortszeit bekommt die manuelle Chat-Finalisierung Vorrang. Ein früher
     Winter-Lauf (06:35) soll nicht ausgerechnet wenige Minuten vor der
     menschlichen Freigabe kostenpflichtig alle Texte erzeugen. Ab 07:00
     bleibt die bisherige API-Pipeline als Ausfallsicherung vollständig aktiv.
     Die Postingzeiten selbst werden NICHT verändert. */
  if (!trocken && !alles && lokaleMinuten() < 7 * 60) {
    log("Chat-Finalisierungsfenster bis 07:00 – Plan steht, kostenpflichtige Inhaltserzeugung wartet.");
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
  /* Die ehrliche Produktionsregel bis zum Reservebestand.

     Vorher standen hier Rücklagen des alten Deckels aus kosten.mjs. Sie
     rechneten mit erwarteten Preisen, und seit alle bezahlten Aufrufe durch
     die Admission gehen, prüfte sie niemand mehr: zwei Reservierungssysteme
     nebeneinander, von denen nur eines noch etwas entschied. Zwei Systeme,
     die sich widersprechen können, sind schlechter als eines, das hart ist.

     Was bleibt, ist die Frage, die sie beantworten sollten: Darf eine Kür
     Geld ausgeben, das die Pflicht noch braucht? Die Antwort kann heute nur
     nein sein, und zwar ohne Zwischentöne. Der volle Admissionbedarf der
     ausstehenden Pflichtaufrufe übersteigt den ganzen Topf (siehe
     dailyPlanNotAdmissibleAtCap) - eine Rücklage, die kleiner ist als
     dieser Bedarf, wäre eine erfundene Zahl mit einer erfundenen Sicherheit
     daran.

     Also: Solange bezahlte Pflichtarbeit aussteht, ist das sichere Budget für
     bezahlte Küren null. Kostenlose Wege - Archivbild, Icon, reines Layout -
     laufen nicht über die Admission und bleiben offen. Sobald die Pflicht des
     Tages durch ist, ist der Rest des Topfes wieder für Küren da. */
  const storyPflichtOffen = () => {
    const stand = (plan.stories || [])
      .filter((st) => st.art !== "teaser" && st.status !== "veroeffentlicht")
      .map((st) => hosting.jsonLesen(`inhalte/${datum}-${st.slot}.json`, null));
    const ungeschrieben = stand.filter((v) => !v).length;
    /* Ein Text ohne Prüfung wird nie veröffentlicht - das Geld fürs Schreiben
       wäre verbrannt. Die Pflicht endet deshalb mit der Prüfung, nicht mit
       dem Text. */
    const ungeprueft = stand.filter((v) => v && !manuellFinalisiert(v) && v.faktencheckOffen).length;
    return { ungeschrieben, ungeprueft };
  };

  const ruecklageAktualisieren = () => {
    if (trocken) { budget.optionalFreigeben(); return []; }
    const offeneBeitraege = plan.beitraege.filter(textFehlt);
    const { ungeschrieben, ungeprueft } = storyPflichtOffen();
    const offen = [];
    if (offeneBeitraege.length) offen.push(`${offeneBeitraege.length} Beitrag/Reel`);
    if (ungeschrieben) offen.push(`${ungeschrieben} Story-Texte`);
    if (ungeprueft) offen.push(`${ungeprueft} Story-Prüfungen`);
    if (offen.length) budget.optionalSperren(`Bezahlte Pflichtarbeit steht aus: ${offen.join(", ")}. Bezahlte Küren warten.`);
    else budget.optionalFreigeben();
    return offen;
  };
  const pflichtOffen = ruecklageAktualisieren();
  if (pflichtOffen.length) log(`  Bezahlte Küren gesperrt, solange Pflichtarbeit aussteht: ${pflichtOffen.join(", ")}`);

  /* Der unbequeme Befund, einmal je Lauf: Mit den heutigen Ceilings liegt
     der Admissionbedarf des Pflichtprodukts ueber dem Core-Deckel. Das
     heisst nicht, dass der Tag teuer wird - gemessen kostet er einen
     Bruchteil. Es heisst, dass niemand vorher sagen kann, dass jeder
     Pflichtaufruf zugelassen wird, wenn jeder seine Reserve in voller Hoehe
     anmeldet. Die Verfuegbarkeitszusage braucht den Reservebestand.

     Die Eingabezahlen hier sind PLANUNGSWERTE: Zum Zeitpunkt der Planung
     gibt es die Anfragen noch nicht, also auch keine Rechnung ueber ihre
     Bytes. Sie sind an gemessenen Prompts geeicht und bewusst grosszuegig.
     Die Admissiongrenze je Aufruf entsteht erst spaeter, in eingabe.mjs -
     und auch sie ist ein konservativer Wert, kein bewiesener Hoechstpreis. */
  const EIN_LANG = 16000, EIN_PRUEFUNG = 12000;
  const wc = tagesplanAdmissionBedarf({
    deckelCore: konfiguration.deckel.core,
    posten: [
      ...plan.beitraege.filter((b) => b.status !== "veroeffentlicht").flatMap((b) => ([
        { name: `${b.slot} Text`, modell: CONFIG.ki.modell, maxTokens: b.format === "reel" ? 4000 : 6000, eingabeTokens: EIN_LANG },
        { name: `${b.slot} Faktencheck`, modell: b.format === "reel" ? (CONFIG.ki.modellPruefungReel || CONFIG.ki.modell) : CONFIG.ki.modell, maxTokens: 3000, eingabeTokens: EIN_PRUEFUNG },
      ])),
      ...(plan.stories.some((x) => x.status !== "veroeffentlicht" && x.art !== "teaser")
        ? [{ name: "Stories", modell: CONFIG.ki.modell, maxTokens: 4500, eingabeTokens: EIN_LANG },
           { name: "Story-Faktencheck", modell: CONFIG.ki.modellPruefung || CONFIG.ki.modellNeben, maxTokens: 3000, eingabeTokens: EIN_PRUEFUNG }]
        : []),
    ],
  });
  if (wc.dailyPlanNotAdmissibleAtCap) log(`  ! dailyPlanNotAdmissibleAtCap: ${wc.hinweis}`);

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
        if (istKostenKontrollFehler(e)) log(`  ⏸ ${e.message}`); else console.error(`  ✗ Interaktion: ${e.message}`);
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
        if (istKostenKontrollFehler(e)) log(`  ⏸ ${e.message}`); else console.error(`  ✗ Postfach: ${e.message}`);
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
    /* Dashboard-Snapshots: Stories, Feed/Reels und der Followerstand werden
       im Stundenlauf als Zeitreihe gesichert. Der Ledger behaelt weiterhin
       jeweils den neuesten Stand; insight-snapshots.json bewahrt den Verlauf. */
    try {
      const snapshots = hosting.jsonLesen("insight-snapshots.json", { version: 1, stand: null, medien: {}, konto: [] });
      const story = await storyInsightsAktualisieren(ig, ledger, { log, snapshots });
      const medien = await medienSnapshotsAktualisieren(ig, ledger, snapshots, { log });
      const konto = await kontoSnapshotAktualisieren(ig, snapshots, { log });
      if (story.gemessen || medien.gemessen || konto.gemessen) {
        hosting.jsonSchreiben("insight-snapshots.json", snapshots);
        ledgerSpeichern(ledgerPfad, ledger);
        hosting.commit(`Insight-Snapshots ${datum}`);
        await hosting.push();
      }
    } catch (e) {
      console.error(`  ✗ Insight-Snapshots: ${e.message}`);
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
  /* Pflicht-Texte nach Fälligkeit absichern -----------------------------
     Die eigenständigen Stories haben morgens die ersten Slots des Tages und
     entstehen als ein günstiger Batch. Sie müssen deshalb VOR dem
     Vorschreiben späterer Feed-Slots gebaut und geprüft werden. Die alte
     Reihenfolge schrieb zuerst Reel und alle Feed-Texte; am 19.09. war danach
     kein Admission-Spielraum mehr für die schon fälligen Stories. */
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
  if (eigenstaendig.length) {
    const vorhanden = eigenstaendig.map((s) => [s.slot, hosting.jsonLesen(`inhalte/${datum}-${s.slot}.json`, null)]);
    const vorhandenSlots = new Set(vorhanden.filter(([, v]) => Boolean(v)).map(([slot]) => slot));
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
        const strittig = neu.filter((s) => alleBefunde(s).length);
        if (strittig.length) try {
          /* Safety 0d: Ein Quizslot wird nie allein neu geschrieben. Welche
             Slots mitmuessen und welcher Partner unveraenderlich ist, steht in
             quizNachschlag() - dort ist es ohne Netz und Instagram pruefbar. */
          const partnerText = (slot) => geschrieben.get(slot) || hosting.jsonLesen(`inhalte/${datum}-${slot}.json`, null);
          const { slots: mitPartner, paarSlots, festeOptionen, warnungen } = quizNachschlag(strittig, plan.stories, partnerText);
          for (const w of warnungen) console.warn(`  ! ${w}`);
          const hinweis = [
            `Die folgenden Entwürfe wurden abgelehnt – formuliere sie vollständig neu:\n${strittig.map((s) => `- Slot ${s.slot}: ${alleBefunde(s).join("; ")}`).join("\n")}`,
            mitPartner.length > strittig.length ? "Frage und Antwort eines Quiz gehören zusammen: Beide Kacheln werden gemeinsam neu geschrieben und müssen dieselben Optionen in derselben Reihenfolge tragen." : "",
            ...festeOptionen,
          ].filter(Boolean).join("\n\n");
          log(`  ${strittig.length} Story-Entwürfe beanstandet – zweiter Versuch${mitPartner.length > strittig.length ? ` (mit ${mitPartner.length - strittig.length} Partner-Kachel)` : ""}${festeOptionen.length ? `, ${festeOptionen.length} Partner unverändert` : ""}`);
          const zweite = await storiesSchreiben(auftrag(mitPartner), datum, hinweis);
          for (const s of zweite) {
            const vorher = geschrieben.get(s.slot);
            /* Bei Paaren gilt die neue Lieferung als Ganzes: Eine alte
               Haelfte mit einer neuen zu mischen ist genau die Drift, die
               verhindert werden soll. */
            if (!paarSlots.has(s.slot) && alleBefunde(s).length && vorher && !alleBefunde(vorher).length) continue;
            hosting.jsonSchreiben(`inhalte/${datum}-${s.slot}.json`, s); geschrieben.set(s.slot, s);
          }
          hosting.commit(`Story-Texte ${datum} (zweiter Versuch)`);
        } catch (e) {
          if (istKostenKontrollFehler(e)) log(`  ⏸ ${e.message}`);
          else console.error(`  ✗ Stories nachschreiben: ${e.message}`);
        }
      } catch (e) {
        if (istKostenKontrollFehler(e)) log(`  ⏸ ${e.message}`);
        else { fehler++; console.error(`  ✗ Stories schreiben: ${e.message}`); }
      }
    }
    /* Persistierte Beanstandungen sind kein Endzustand. Die bisherige
       Reparaturschleife sah nur Texte, die IN DIESEM Lauf neu entstanden.
       Scheiterte ihr zweiter Versuch am Budget, lag der beanstandete Text
       danach dauerhaft auf Platte und wurde in allen Folgeläufen nur noch
       übersprungen. Vorhandene beanstandete Entwürfe bekommen deshalb in
       jedem späteren Lauf genau einen neuen Reparaturversuch. */
    const erneutStrittig = persistierteStoryBeanstandungen(geschrieben, vorhandenSlots);
    if (erneutStrittig.length) {
      try {
        const auftrag = (liste) => liste.map((s) => ({
          slot: s.slot, art: s.art, thema: themaFuer(s.themaId), tageBisExamen: s.tageBisExamen,
        }));
        const partnerText = (slot) => geschrieben.get(slot) || hosting.jsonLesen(`inhalte/${datum}-${slot}.json`, null);
        const { slots: mitPartner, paarSlots, festeOptionen, warnungen } = quizNachschlag(erneutStrittig, plan.stories, partnerText);
        for (const w of warnungen) console.warn(`  ! ${w}`);
        const hinweis = [
          `Diese gespeicherten Entwürfe wurden in einem früheren Lauf beanstandet. Korrigiere die genannten Fehler vollständig; ein beanstandeter Slot darf nicht einfach ausfallen:\n${erneutStrittig.map((s) => `- Slot ${s.slot}: ${alleBefunde(s).join("; ")}`).join("\n")}`,
          mitPartner.length > erneutStrittig.length ? "Frage und Antwort eines Quiz gehören zusammen: Beide Kacheln werden gemeinsam neu geschrieben und müssen dieselben Optionen in derselben Reihenfolge tragen." : "",
          ...festeOptionen,
        ].filter(Boolean).join("\n\n");
        log(`  ${erneutStrittig.length} gespeicherte Story-Beanstandung(en) – erneuter Reparaturversuch`);
        const repariert = await storiesSchreiben(auftrag(mitPartner), datum, hinweis);
        for (const s of repariert) {
          const vorher = geschrieben.get(s.slot);
          if (!paarSlots.has(s.slot) && alleBefunde(s).length && vorher && !alleBefunde(vorher).length) continue;
          hosting.jsonSchreiben(`inhalte/${datum}-${s.slot}.json`, s);
          geschrieben.set(s.slot, s);
        }
        hosting.commit(`Story-Texte ${datum} (persistierte Beanstandungen repariert)`);
      } catch (e) {
        /* Budgetmangel ist WARTEN, nicht AUSFALL. Die Datei und der Planstatus
           bleiben erhalten; der nächste Stundenlauf versucht es erneut. */
        if (istKostenKontrollFehler(e)) log(`  ⏸ Story-Reparatur wartet auf Budget: ${e.message}`);
        else { fehler++; console.error(`  ✗ Persistierte Stories nachschreiben: ${e.message}`); }
      }
    }

    /* Texte, die geschrieben und bezahlt sind, deren Faktencheck aber am
       Budget scheiterte, liegen unter inhalte/ und tragen `faktencheckOffen`.
       Sie werden hier nachgeprüft - das kostet nur die Prüfung, nicht das
       Schreiben. Klappt es wieder nicht, warten sie auf den nächsten Lauf. */
    const ungeprueft = [...geschrieben.values()].filter((s) => !manuellFinalisiert(s) && s.faktencheckOffen);
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
        if (istKostenKontrollFehler(e)) log(`  ⏸ ${e.message}`);
        else { fehler++; console.error(`  ✗ Story-Faktencheck nachholen: ${e.message}`); }
      }
    }
  }


  /* --- Texte des Tages vorab ---------------------------------------------
     Reel und Beiträge bekommen ihren Text im ersten Lauf des Tages, solange
     das Budget voll ist – nicht erst zur Sendezeit. Was morgens nicht
     bezahlbar ist, weiß man morgens; abends ist es zu spät. Nach dem
     Story-Batch folgen die Feed-Slots in ihrer tatsächlichen Sende-Reihenfolge.
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
    const ziel = Number(eintrag.klausur);
    const farbtreu = [0, 1, 2, 3].includes(ziel);
    const frei = pool.filter((t) =>
      !belegteThemen.has(t.id) &&
      (FORMAT_QUELLEN.pruefungsfrage || []).includes(t.typ) &&
      (!farbtreu || t.klausur === ziel)
    );
    /* Bei einem fest eingeplanten Farbslot wird nicht in ein anderes Gebiet
       ausgewichen. Lieber bleibt der Slot offen, als dass im Feed zwei gleiche
       Kategorien aufeinanderfolgen oder ein Rechtsgebiet doppelt erscheint. */
    const ausweich = frei.find(Boolean) || (!farbtreu ? pool.find((t) => !belegteThemen.has(t.id)) : null);
    if (!ausweich) return null;
    belegteThemen.add(ausweich.id);
    eintrag.format = "pruefungsfrage";
    eintrag.themaId = ausweich.id;
    eintrag.themaTitel = ausweich.titel;
    eintrag.fach = ausweich.fach;
    log(`  → „pruefungsfrage" statt Recherche: „${ausweich.titel}" - Farbslot ${FEED_KATEGORIEN[ziel] || ziel} bleibt erhalten.`);
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
          const zielGebiet = [1, 2, 3].includes(Number(eintrag.klausur)) ? Number(eintrag.klausur) : null;
          recherche = eintrag.format === "loesungsskizze"
            ? await loesungsRecherchieren(datum, eintrag.anlass || plan.abendAnlass)
            : await aktuellRecherchieren(datum, bisher, KLAUSUREN[zielGebiet]?.label || fehlendesGebiet(plan));
          /* „KEINE_NEUIGKEIT" ist die verabredete Antwort fuer: nichts
             gefunden, was den Massstab haelt. Ebenso zaehlt ein Ergebnis
             ohne jede Quelle - daraus laesst sich kein belegter Beitrag
             bauen. Ein Aktuell-Beitrag muss außerdem im fest geplanten
             Rechtsgebiet bleiben; sonst wird auf den Themenpool ausgewichen. */
          const rechercheGebiet = FAECHER[recherche.fach]?.klausur ?? null;
          const falschesGebiet = eintrag.format === "aktuell" && zielGebiet && rechercheGebiet !== zielGebiet;
          const leer = /KEINE_NEUIGKEIT/i.test(recherche.notizen || "") || !recherche.quellen.length || falschesGebiet;
          if (leer) {
            const grund = falschesGebiet
              ? `Recherche landete in ${FEED_KATEGORIEN[rechercheGebiet] || recherche.fach || "unbekannt"} statt ${FEED_KATEGORIEN[zielGebiet]}`
              : (/KEINE_NEUIGKEIT/i.test(recherche.notizen || "") ? "nichts mit Prüfungsbezug gefunden" : "keine Quellen");
            log(`  Recherche ohne verwertbares Ergebnis (${grund}).`);
            const ersatz = aufThemenpoolAusweichen(eintrag);
            if (ersatz) return ersatz;
          } else log(`  Recherche: ${recherche.titel || "(ohne Titel)"} · ${recherche.quellen.length} Quellen`);
        } catch (e) {
          if (!istKostenKontrollFehler(e)) throw e;
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
  const vorab = plan.beitraege.filter((b) => textFehlt(b) && b.format !== "loesungsskizze").sort((a, b) => minutenVon(a.zeit) - minutenVon(b.zeit));
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
      if (e?.name === "PostenFehler") { log(`  ⏸ ${e.message}`); continue; }
      if (istKostenKontrollFehler(e)) { log(`  ⏸ ${e.message}`); break; }
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

  /* Letzte Schutzschicht direkt vor Instagram: Auch wenn ein älterer Plan,
     ein Übertrag oder ein ausgefallener Zwischenslot die Tagesfolge verändert,
     werden zwei gleiche sichtbare Kategorien nie direkt nacheinander gesendet.
     Der blockierte Slot bleibt geplant; ein späterer andersfarbiger Slot kann
     zuerst erscheinen, danach ist er beim nächsten Lauf wieder zulässig. */
  const rotationsfolgeErlaubt = (inhalt, eintrag) => {
    if (trocken) return true;
    const vorher = [...(ledger.veroeffentlicht || [])].reverse().find((e) => e.art === "beitrag" && e.medienId && e.medienId !== "trocken");
    const nachher = { format: eintrag.format, fach: inhalt?.fach || eintrag.fach, klausur: inhalt?.klausur ?? eintrag.klausur };
    if (feedFolgeErlaubt(vorher, nachher)) return true;
    const k = feedKategorie(nachher);
    log(`  ↷ ${eintrag.slot} wartet: ${FEED_KATEGORIEN[k] || k} würde direkt auf dieselbe Feed-Kategorie folgen.`);
    return false;
  };

  /* Story-Texte dräge (wichtiger), zuletzt die Stories veröffentlichen. */
  for (const eintrag of beitraegeFaellig) {
    if (frei() <= 0) { log("Tageskontingent erschöpft – Beitrag verschoben."); break; }
    if (eintrag.textFehler && !hosting.jsonLesen(textDatei(eintrag), null)) continue;
    try {
      log(`Beitrag ${eintrag.slot} (${eintrag.format}) ${eintrag.themaTitel || ""}`);
      if (eintrag.format === "reel") {
        const reel = await textBesorgen(eintrag);
        if (!rotationsfolgeErlaubt(reel, eintrag)) continue;
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
        const echt = veroeffentlichungEintragen(eintrag, medienId);
        if (!echt.bestaetigt) { probelaeufe.push({ slot: eintrag.slot, art: "reel", kennung: echt.kennung, zeit: new Date().toISOString() }); log(`  ○ Probelauf: Reel ${eintrag.slot} ${echt.grund} – der Plan bleibt unverändert.`); }
        if (echt.bestaetigt) vermerken(ledger, { datum, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, stunde: Math.floor(lokaleMinuten() / 60), format: "reel", thema: reel.themaId, fach: reel.fach, klausur: reel.klausur, titel: reel.szenen[0]?.titel || reel.kurztitel, hookTyp: reel.hookTyp, hookMuster: reel.hookMuster, medienId, variante: varianteReel, hashtags: reel.hashtags, stimmeId: r.stimmeId || null, stimmeName: r.stimmeName || null, layout: r.layout || null, dauer: Math.round(r.dauer * 10) / 10, veroeffentlicht: new Date().toISOString() });
        if (echt.bestaetigt) eintrag.kanaele = await verteilen({ art: "reel", videoUrl, videoPfad: r.video, bildUrls: [coverUrl], titel: reel.kurztitel || reel.szenen[0]?.titel, text: caption, hashtags: reel.hashtags }, { log, trockenlauf: trocken, stateDir: hosting.stateDir });
        fertigeBeitraege.set(eintrag.slot, { ...reel, folien: [{ art: "titel", titel: reel.szenen[0]?.titel, icon: reel.szenen[0]?.icon }], kurztitel: reel.kurztitel });
        ledgerSpeichern(ledgerPfad, ledger); planSpeichern(hosting, plan);
        ruecklageAktualisieren();
        hosting.commit(`Veröffentlicht: Reel ${datum} ${eintrag.slot}`); await hosting.push();
        if (echt.bestaetigt) log(`  ✓ Reel ${medienId} (${r.dauer.toFixed(0)} s, Stimme: ${r.anbieter})`);
        else log(`  ○ Reel ${eintrag.slot} gebaut (${r.dauer.toFixed(0)} s), aber nicht gesendet.`);
        continue;
      }
      const beitrag = await textBesorgen(eintrag);
      if (!rotationsfolgeErlaubt(beitrag, eintrag)) continue;
      const variante = (CONFIG.marke.farbeJeKlausur ? 0 : await varianteErmitteln({ ig, ledger, trocken, log }));
      /* Produktregel: Karussell = bevorzugt fotorealistisches Cover + Icon;
         innere Slides bleiben bildfrei. Archiv/Pexels/Bild-KI bilden die
         automatische Rettungskette. Scheitern alle Bildquellen, gewinnt
         Availability: das bestehende Icon-Cover wird trotzdem veröffentlicht. */
      if (!(await titelfolieBebildern(beitrag))) {
        console.warn(`  ! Beitrag ${eintrag.slot}: kein Charakter-Cover verfügbar – Veröffentlichung mit Icon-Cover.`);
      }
      const bilder = await beitragRendern(beitrag, path.join(AUSGABE, "beitraege"), { variante });
      const urls = await hosting.veroeffentlichen(bilder, datum, `Beitrag ${datum} ${eintrag.slot}`);
      const caption = `${beitrag.caption}${bildnachweis(beitrag)}\n\n${beitrag.hashtags.join(" ")}`;
      const schonDa = await ig.bereitsVeroeffentlicht(caption);
      if (schonDa) log(`  Beitrag steht bereits auf Instagram (${schonDa}) – wird nur vermerkt.`);
      const medienId = schonDa || await ig.beitragPosten({ bildUrls: urls, caption });
      kontingent.genutzt += 1;
      const echt = veroeffentlichungEintragen(eintrag, medienId);
      if (!echt.bestaetigt) { probelaeufe.push({ slot: eintrag.slot, art: "beitrag", kennung: echt.kennung, zeit: new Date().toISOString() }); log(`  ○ Probelauf: Beitrag ${eintrag.slot} ${echt.grund} – der Plan bleibt unverändert.`); }
      const karteIndex = beitrag.folien.findIndex((f) => f.art === "karte");
      if (echt.bestaetigt) vermerken(ledger, { datum, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, stunde: Math.floor(lokaleMinuten() / 60), format: eintrag.format, thema: beitrag.themaId, fach: beitrag.fach, klausur: beitrag.klausur, titel: beitrag.folien[0].titel, hookTyp: beitrag.hookTyp, medienId, variante, hashtags: beitrag.hashtags, veroeffentlicht: new Date().toISOString(), karteUrl: karteIndex >= 0 ? urls[karteIndex] : null });
      fertigeBeitraege.set(eintrag.slot, beitrag);
      /* Auf weitere Kanäle verteilen (Threads, Facebook, LinkedIn …). */
      if (echt.bestaetigt) eintrag.kanaele = await verteilen({ art: "beitrag", bildUrls: urls, bildPfade: bilder, titel: beitrag.folien[0].titel, text: caption, hashtags: beitrag.hashtags }, { log, trockenlauf: trocken, stateDir: hosting.stateDir });
      ledgerSpeichern(ledgerPfad, ledger);
      planSpeichern(hosting, plan);
      hosting.commit(`Veröffentlicht: Beitrag ${datum} ${eintrag.slot}`);
      await hosting.push();
      if (echt.bestaetigt) log(`  ✓ ${medienId} (${urls.length} Folien)`);
      else log(`  ○ Beitrag ${eintrag.slot} gerendert (${urls.length} Folien), aber nicht gesendet.`);
    } catch (e) {
      /* Ein Slot, der am Budget scheitert, faellt nicht still aus: Er wird
         gemeldet, im Plan vermerkt und landet im Bericht. Fail closed heisst
         nicht schweigen. */
      /* Jeder Budgetstopp - Admission, gesperrter Topf, nicht durable
         gewordenes Journal, alter Deckel - bedeutet dasselbe: Der Slot bleibt
         geplant und erscheint heute nicht. Unterschieden wird nur, wie
         ausführlich vermerkt wird. */
      if (istKostenKontrollFehler(e)) {
        eintrag.budgetBlockiert = { seit: new Date().toISOString(), grund: budgetStoppGrund(e), topf: e.topf || null, art: e.name };
        log(`  ⛔ ${eintrag.slot} budget-blockiert: ${budgetStoppGrund(e)}`);

        /* Der Vorrat greift genau hier und nur hier: ein Feed-Beitrag, der an
           der Kostenkontrolle scheitert. Kein allgemeiner Fehler-Fallback -
           ein technischer Ausfall oder ein fachlich beanstandeter Inhalt sind
           andere Probleme, und ein Ersatzbeitrag wuerde sie verdecken. */
        const zulaessig = ersatzZulaessig({ eintrag, fehler: e });
        if (!trocken && zulaessig.ok) {
          try {
            const r = await reserveEntnehmen({
              hosting, bestand: reserveBestand, heute: datum, ledger, ig,
              eintrag, slot: eintrag.slot,
              echteMedienId, veroeffentlichungEintragen, vermerken,
              inhaltSpeichern: (slot, beitrag) => hosting.jsonSchreiben(`inhalte/${datum}-${slot}.json`, beitrag),
              log,
            });
            if (r.medienId) {
              reserveBestand = r.bestand;
              /* Ohne fachliche Arbeit dazwischen: Slot, Inhalt und Ledger
                 stehen, jetzt wird derselbe Zustand durable gemacht. Erst
                 danach duerfen die Vorratsbilder weg - scheitert der Push,
                 steigt der naechste Lauf ueber bereitsVeroeffentlicht() wieder
                 ein und braucht sie womoeglich noch. */
              ledgerSpeichern(ledgerPfad, ledger);
              await zustandSichern(`Reserve ${eintrag.slot} ${datum}`);
              r.nachDurable();
              log(`  ✓ ${r.medienId} aus dem Vorrat${r.wiedergefunden ? " (bereits veröffentlicht, nur vermerkt)" : ""}`);
              continue;
            }
          } catch (rf) {
            /* Ein Fehler beim Ersatz darf den Lauf nicht kosten - der Slot
               bleibt dann blockiert wie ohne Vorrat. */
            console.error(`  ✗ Vorrat für ${eintrag.slot}: ${rf.message}`);
          }
        } else if (!zulaessig.ok) {
          log(`  Vorrat: kein Ersatz für ${eintrag.slot} - ${zulaessig.grund}`);
        }
        continue;
      }
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
        /* Der Teaser kündigt einen Beitrag an, den es ohne bestätigte
           Medien-ID nicht gibt. Der Planstatus allein reicht nicht: Am 18.09.
           stand er auf „veröffentlicht“, während die ID „trocken“ lautete. */
        if (!beitrag || !veroeffentlichtBestaetigt(b)) { log(`Story ${eintrag.slot}: Beitrag ${eintrag.beitragSlot} noch nicht veröffentlicht – später.`); continue; }
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
      /* Safety 0: Das Quiz ist EIN Gegenstand. Weder Frage noch Antwort
         erscheinen allein - erst wenn beide Kacheln gespeichert, freigegeben
         und zueinander passend sind, geht die erste von beiden raus. Geprueft
         wird hier auf dem, was wirklich gespeichert ist, nicht auf dem, was
         der Plan behauptet: Zwischen Schreiben und Senden kann ein einzelner
         Slot neu geschrieben worden sein, und genau das ist am 16.09.
         passiert. */
      if (eintrag.art === "frage" || eintrag.art === "antwort") {
        const paar = quizPaarFreigabe(eintrag, plan.stories, (slot) => hosting.jsonLesen(`inhalte/${datum}-${slot}.json`, null));
        if (paar.status !== "frei") {
          const nachsatz = paar.status === "warten" ? "spaeter." : "uebersprungen.";
          log(`Story ${eintrag.slot}: ${paar.grund} - ${nachsatz}`);
          if (paar.status !== "warten") eintrag.status = "uebersprungen";
          /* Ein widerspruechlicher Zustand ist kein normaler Ablauf: Er wird
             am Eintrag vermerkt, damit er im Bericht auftaucht, statt still
             jeden Lauf zu wiederholen. */
          if (paar.status === "inkonsistent") {
            eintrag.fehler = `${new Date().toISOString()} Quiz-Paar inkonsistent: ${paar.grund}`;
            console.warn(`  ! Quiz-Paar ${eintrag.slot}: ${paar.grund}`);
          }
          continue;
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
      const echt = veroeffentlichungEintragen(eintrag, medienId);
      if (!echt.bestaetigt) { probelaeufe.push({ slot: eintrag.slot, art: "story", kennung: echt.kennung, zeit: new Date().toISOString() }); log(`  ○ Probelauf: Story ${eintrag.slot} ${echt.grund} – der Plan bleibt unverändert.`); }
      if (echt.bestaetigt) vermerken(ledger, { datum, art: "story", slot: eintrag.slot, storyArt: story.art, thema: story.themaId || eintrag.themaId || null, fach: story.fach, titel: story.titel || story.text || "", medienId, veroeffentlicht: new Date().toISOString() });
      ledgerSpeichern(ledgerPfad, ledger);
      planSpeichern(hosting, plan);
      hosting.commit(`Veröffentlicht: Story ${datum} ${eintrag.slot}`);
      await hosting.push();
      if (echt.bestaetigt) log(`  ✓ Story ${eintrag.slot} ${story.art}${eintrag.interaktiv ? " mit Umfrage" : ""} → ${medienId}`);
      else log(`  ○ Story ${eintrag.slot} ${story.art} gerendert, aber nicht gesendet.`);
    } catch (e) {
      if (istKostenKontrollFehler(e)) { log(`  ⏸ ${e.message}`); continue; }
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

  /* Ein Thema fuer den Vorrat: Tor 1 der Policy, und dann nur solche, die
     weder heute geplant sind, noch schon im Bestand liegen, noch in der
     Dublettenfrist erschienen sind. Was hier schon aussortiert wird, kostet
     spaeter kein Geld - Tor 2 prueft erst den fertigen, bezahlten Text. */
  const reserveThemaWaehlen = () => {
    const imBestand = new Set(reserveBestand.map((e) => e.themaId).filter(Boolean));
    const grenze = new Date(new Date(`${datum}T00:00:00Z`).getTime() - DUBLETTEN_TAGE * 86400000).toISOString().slice(0, 10);
    const jung = new Set((ledger.veroeffentlicht || []).filter((e) => String(e.datum || "") >= grenze && e.thema).map((e) => e.thema));
    const frei = pool.filter((t) => themaTauglich(t).ok && !belegteThemen.has(t.id) && !imBestand.has(t.id) && !jung.has(t.id));
    if (!frei.length) return null;
    /* Kein Zufall: das Thema, dessen Fach im Bestand am duennsten vertreten
       ist. Ein Vorrat aus vier Beitraegen desselben Klausurtags waere am
       Blockadetag eine schlechte Auswahl. */
    const jeFach = new Map();
    for (const e of reserveBestand) jeFach.set(e.fach, (jeFach.get(e.fach) || 0) + 1);
    return [...frei].sort((a, b) => (jeFach.get(a.fach) || 0) - (jeFach.get(b.fach) || 0) || String(a.id).localeCompare(String(b.id)))[0];
  };

  /* Die teure Haelfte des Nachschubs: schreiben, pruefen, rendern, ablegen.
     Sie laeuft unter derselben Beitragsgrenze wie ein Pflichtbeitrag und
     legt ihre Bilder unter bilder/reserve/<id>/ ab - ausserhalb der
     Datumsrotation, die sonst genau am 21. Tag zuschlagen wuerde. */
  const reserveBeitragErzeugen = async ({ id, pfad }) => {
    const thema = reserveThemaWaehlen();
    if (!thema) return null;
    log(`  Vorrat: ${id} wird erzeugt · ${thema.typ} · ${thema.titel}`);
    /* Das Thema gilt ab jetzt als belegt, auch wenn der Beitrag gleich an
       Tor 2 scheitert: Ein zweiter Versuch am selben Thema im selben Lauf
       koennte nur dasselbe Ergebnis kaufen. */
    belegteThemen.add(thema.id);
    let beitrag;
    /* Dieselbe Obergrenze wie fuer einen Pflichtbeitrag - und dasselbe
       Verschachtelungsverbot wie in textBesorgen: Ein laufender Posten wird
       fortgefuehrt, nicht ueberschrieben. */
    const eigenerPosten = !postenAktiv();
    if (eigenerPosten) postenBeginnen(`Vorrat ${id}`, CONFIG.ki.maxJeBeitragUsd);
    try { beitrag = await beitragSchreiben({ format: RESERVE_FORMATE[thema.typ], thema, datum, strategie }); }
    finally { if (eigenerPosten) postenBeenden(); }
    if (!(await titelfolieBebildern(beitrag))) {
      console.warn(`  ! Vorrat ${id}: kein Charakter-Cover – Reserve wird mit Icon-Cover gerendert.`);
    }
    const variante = (CONFIG.marke.farbeJeKlausur ? 0 : await varianteErmitteln({ ig, ledger, trocken, log }));
    const bilder = await beitragRendern(beitrag, path.join(AUSGABE, "reserve", id), { variante });
    const bildUrls = await hosting.veroeffentlichen(bilder, pfad, `Vorrat ${id}`);
    /* Die Publikationscaption entsteht HIER, in genau derselben Form wie im
       Tageslauf - und wird so gespeichert. Am Blockadetag wird nichts mehr
       zusammengesetzt; bereitsVeroeffentlicht() vergleicht diesen Text. */
    const caption = `${beitrag.caption}${bildnachweis(beitrag)}\n\n${beitrag.hashtags.join(" ")}`;
    return { thema, beitrag, bildUrls, caption, hashtags: beitrag.hashtags || [], faktenFreigabe: beitrag.faktenFreigabe };
  };

  /* ---- Vorrat auffüllen: ganz am Ende, aus echtem Restbudget ------------
     Die Reihenfolge des Tages ist bewusst so und nicht anders:
       Pflichtbeiträge → kostenlose Entnahme auf einem kostenblockierten Slot
       → Stories → und erst hier, wenn KEINE bezahlte Pflichtarbeit mehr offen
       ist, höchstens EIN Nachschub.
     Der Vorrat ist die Versicherung, nicht das Produkt. Er darf dem heutigen
     Pflichtprodukt nie einen Cent wegnehmen. Die Sperre dafür ist dieselbe,
     die schon für jede andere bezahlte Kür gilt (budget.optionalGesperrt),
     hier nur noch einmal frisch nachgezogen. */
  const chatTagFinalisiert = tagesinhaltManuellFinalisiert(
    plan,
    (slot) => hosting.jsonLesen(`inhalte/${datum}-${slot}.json`, null),
  );
  if (chatTagFinalisiert) {
    log("  Vorrat: kein bezahlter Nachschub – Tagesinhalt wurde im Chat vollständig finalisiert.");
  } else if (!trocken && !nurPlanen) {
    ruecklageAktualisieren();
    try {
      const vorher = reserveBestand.length;
      const auf = await reserveAuffuellen({
        bestand: reserveBestand, heute: datum, kanal: KANAL, budget,
        beitragsGrenzeUsd: CONFIG.ki.reserveNachschubMinUsd,
        erzeugen: reserveBeitragErzeugen,
        speichern: (neuerBestand) => { reserveBestand = neuerBestand; hosting.jsonSchreiben(BESTAND_DATEI, bestandInhalt(neuerBestand, KANAL)); },
        log,
      });
      reserveBestand = auf.bestand;
      if (auf.erzeugt) log(`  Vorrat: ${auf.erzeugt} Beitrag/Beiträge erzeugt (${vorher} → ${reserveBestand.length}/${ZIEL_BESTAND}).`);
      else if (auf.grund) log(`  Vorrat: kein Nachschub - ${auf.grund}.`);
    } catch (e) {
      /* Der Nachschub ist eine Kür. Scheitert er, hat der Tag trotzdem
         stattgefunden - er wird gemeldet, nicht als Tagesfehler gezählt. */
      if (istKostenKontrollFehler(e)) log(`  ⏸ Vorrat: ${e.message}`);
      else console.error(`  ✗ Vorrat: ${e.message}`);
    }
  }

  await zustandSichern(`Zustand ${datum}`);
  /* Die rollenden Fenster hat die Sicherung selbst geschrieben (vorSichern);
     hier steht nur noch, was im Protokoll erscheinen soll. */
  if (telemetrie.anzahl()) {
    const u = telemetrie.uebersicht();
    for (const [topf, z] of Object.entries(u.jeTopf)) {
      log(`  Telemetrie ${topf}: ${z.aufrufe} Aufrufe, ${z.usd.toFixed(4)} $`
        + `${z.ungeklaert ? `, ${z.ungeklaert} ungeklärt` : ""}${z.abschnitte ? `, ${z.abschnitte} abgeschnitten` : ""}`);
    }
  }
  const budgetStand = budget.stand();
  log(`  Töpfe am Ende: Core ${budgetStand.verbraucht.core.toFixed(4)}/${budgetStand.deckel.core.toFixed(2)} · `
    + `Engagement ${budgetStand.verbraucht.engagement.toFixed(4)}/${budgetStand.deckel.engagement.toFixed(2)} · `
    + `Research ${budgetStand.verbraucht.research.toFixed(4)}/${budgetStand.deckel.research.toFixed(2)} $`);
  const blockiert = [...plan.beitraege, ...plan.stories].filter((e) => e.budgetBlockiert);
  if (blockiert.length) log(`  ⛔ ${blockiert.length} Slot(s) budget-blockiert: ${blockiert.map((e) => e.slot).join(", ")} - sie erscheinen heute nicht.`);

  /* Das Protokoll des Trockenlaufs: nur lokal, nie im Asset-Zweig. Es sagt,
     was hinausgegangen WÄRE - und lässt den Tagesplan in Ruhe. */
  if (ig.protokoll.length || probelaeufe.length) {
    fs.mkdirSync(AUSGABE, { recursive: true });
    fs.writeFileSync(path.join(AUSGABE, "trockenlauf.json"),
      JSON.stringify({ datum, trocken, gesendet: ig.protokoll, nichtVeroeffentlicht: probelaeufe }, null, 2));
  }
  if (probelaeufe.length) log(`Probelauf: ${probelaeufe.length} Posten wurden erzeugt, aber nicht veröffentlicht (out/${datum}/trockenlauf.json).`);
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
      if (!(await titelfolieBebildern(beitrag))) {
        console.warn(`  ! Auffüllen ${eintrag.slot}: kein Charakter-Cover – Veröffentlichung mit Icon-Cover.`);
      }
      const bilder = await beitragRendern(beitrag, path.join(AUSGABE, "auffuellen"), { variante });
      const urls = await hosting.veroeffentlichen(bilder, datum, `Auffüllen ${slot}`);
      const caption = `${beitrag.caption}${bildnachweis(beitrag)}\n\n${beitrag.hashtags.join(" ")}`;
      const schonDa = await ig.bereitsVeroeffentlicht(caption);
      if (schonDa) log(`  Beitrag steht bereits auf Instagram (${schonDa}) – wird nur vermerkt.`);
      const medienId = schonDa || await ig.beitragPosten({ bildUrls: urls, caption });
      const karteIndex = beitrag.folien.findIndex((f) => f.art === "karte");
      /* Bei einem bereits vorhandenen Beitrag ist die gemessene Variante die des Vorgängers – nicht eintragen. */
      if (!echteMedienId(medienId)) { probelaeufe.push({ slot: eintrag.slot, art: "auffuellen", kennung: String(medienId ?? ""), zeit: new Date().toISOString() }); log(`  ○ Probelauf: ${eintrag.slot} ohne Medien-ID – nicht vermerkt.`); }
      if (echteMedienId(medienId)) vermerken(ledger, { datum, art: "beitrag", slot: eintrag.slot, zeit: eintrag.zeit, stunde: Math.floor(lokaleMinuten() / 60), format: eintrag.format, thema: beitrag.themaId, fach: beitrag.fach, titel: beitrag.folien[0].titel, hookTyp: beitrag.hookTyp, medienId, variante: schonDa ? null : variante, hashtags: beitrag.hashtags, veroeffentlicht: new Date().toISOString(), karteUrl: karteIndex >= 0 ? urls[karteIndex] : null });
      /* Der Fortschritt zaehlt nur, was wirklich erschienen ist - sonst
         glaubt der naechste Lauf, ein Trockenlauf haette den Feed gefuellt. */
      if (echteMedienId(medienId)) stand.fertig = i + 1;
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
      if (istKostenKontrollFehler(e)) { log(`  ⏸ ${e.message} Auffüllen wird morgen fortgesetzt.`); budgetStopp = true; break; }
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
