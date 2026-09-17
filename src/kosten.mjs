/* Verbrauch der Claude API mitschreiben (für den Wochenbericht). */
const PREISE = {
  "claude-opus-5": { ein: 5, aus: 25, cacheLesen: 0.5, cacheSchreiben: 6.25 },
  "claude-sonnet-5": { ein: 2, aus: 10, cacheLesen: 0.2, cacheSchreiben: 2.5 },
  "claude-opus-4-8": { ein: 5, aus: 25, cacheLesen: 0.5, cacheSchreiben: 6.25 },
  "claude-haiku-4-5": { ein: 1, aus: 5, cacheLesen: 0.1, cacheSchreiben: 1.25 },
  "claude-haiku-4-5-20251001": { ein: 1, aus: 5, cacheLesen: 0.1, cacheSchreiben: 1.25 },
};

const posten = [];

/* --- Tagesdeckel -------------------------------------------------------
   Vor jedem Claude-Aufruf wird geprüft, ob der Tagesverbrauch (bisherige
   Läufe des Tages + dieser Lauf) unter der Grenze liegt. Ist sie erreicht,
   wirft budgetPruefen() einen BudgetFehler – der Rest wartet bis morgen. */
let limitUsd = Infinity, vorbelastung = 0, speichern = null;
/* Zweiter Topf: Antworten auf Kommentare und Nachrichten. Sie zählen nicht
   gegen den Inhaltsdeckel und der Inhalt nicht gegen sie. Beide Töpfe haben
   ihren eigenen Stand und ihre eigene Grenze; nur die Posten-Liste ist
   gemeinsam, getrennt wird nach Zweck. */
let antwortLimitUsd = Infinity, antwortVorbelastung = 0;
const ANTWORT_ZWECKE = ["kommentare", "nachrichten"];
/* Für das Reel des Tages zurückgelegter Betrag. Alle anderen Aufrufe hören
   entsprechend früher auf, damit das Reel am Abend noch geschrieben werden
   kann – es soll täglich erscheinen. */
/* Mehrere Toepfe, nicht einer. Ein einziger Topf mit Freigabeliste kann nicht
   ausdruecken, dass Beitraege und Stories sich gegenseitig NICHT bedienen
   duerfen: Wer auf der Liste steht, kommt an alles. Am 17.09. hat genau das
   den Tag gekostet - das Schreiben eines Beitrags durfte das Geld der neun
   Stories mitverbrauchen, weil die Stories gar keinen eigenen Topf hatten.

   Jeder Topf nennt die Zwecke, die IHN leeren duerfen. Fuer jeden anderen
   Zweck ist er gesperrt. */
const reserven = new Map();
/* Zwecke, die auf die Rücklage zugreifen dürfen – als Liste, denn die Rücklage
   gilt inzwischen allen noch zu schreibenden Beiträgen des Tages, nicht nur
   dem Reel. Verglichen wird der Zweck-Schlüssel, nicht der Wortlaut: Der
   „Story-Faktencheck“ enthält zwar „faktencheck“, bleibt aber außen vor. */
const zweckListe = (f) => (Array.isArray(f) ? f : [f]).map((x) => String(x).toLowerCase()).filter(Boolean);

export class BudgetFehler extends Error {}

export function budgetSetzen(opt = {}) {
  /* Beginn eines Laufs: Die Posten der bisherigen Läufe des Tages stecken in
     `bisher`, nicht in dieser Liste. Ohne das Leeren zählte ein zweiter Aufruf
     von budgetSetzen im selben Prozess die alten Posten doppelt. */
  posten.length = 0;
  for (const k of Object.keys(GEMESSEN)) delete GEMESSEN[k];
  /* Die Messungen der früheren Läufe des Tages: Ein Lauf um 21:30 soll nicht
     wieder mit der Tabelle rechnen, wenn der Lauf um 19:43 schon weiß, was
     ein Reel heute tatsächlich kostet. */
  Object.assign(GEMESSEN, opt.gemessen || {});
  limitUsd = opt.limitUsd ?? Infinity;
  vorbelastung = opt.bisher ?? 0;
  antwortLimitUsd = opt.antwortLimitUsd ?? Infinity;
  antwortVorbelastung = opt.bisherAntworten ?? 0;
  speichern = opt.speichern ?? null;
  reserven.clear();
  if (opt.reserviert) reserven.set("beitraege", { betrag: opt.reserviert, fuer: zweckListe(opt.reserviertFuer ?? "reel"), label: opt.reserviertLabel ?? "das Reel" });
  postenBeenden();
}

/* Hebt die Rücklage auf, sobald das Reel steht (oder feststeht, dass heute
   keines mehr kommt). Danach darf der Rest des Tages sie ausschöpfen. */
export function reservieren(betrag, fuer = "reel", label = "das Reel", topf = "beitraege") {
  const b = Math.max(0, Number(betrag) || 0);
  if (b > 0) reserven.set(topf, { betrag: b, fuer: zweckListe(fuer), label });
  else reserven.delete(topf);
}
export function reservierungAufheben(topf = "beitraege") { if (topf == null) reserven.clear(); else reserven.delete(topf); }
/** Summe aller Toepfe (fuer Anzeige und Tests). */
export const reservierung = () => runden([...reserven.values()].reduce((a, r) => a + r.betrag, 0));
/** Was diesem Zweck VERSPERRT ist: alle Toepfe, die ihn nicht freigeben. */
export function fremdeReserve(zweck) {
  const k = schluessel(zweck) || String(zweck).toLowerCase();
  return runden([...reserven.values()].filter((r) => !r.fuer.includes(k)).reduce((a, r) => a + r.betrag, 0));
}
const fremdeLabel = (zweck) => {
  const k = schluessel(zweck) || String(zweck).toLowerCase();
  return [...reserven.values()].filter((r) => !r.fuer.includes(k)).map((r) => r.label).join(" und ");
};
/** Teuerster Aufruf je Zweck – wandert in state/kosten.json, damit der nächste
    Lauf des Tages damit weiterrechnet statt mit der Schätzung. */
export const messungen = () => ({ ...GEMESSEN });

/* Wie viel vom Tagesbudget für das Reel zurückgelegt wird.
   Die Zahl aus der Konfiguration war eine Schätzung aus der Anfangszeit und
   blieb es: 0,11 $ standen jeden Tag fest, obwohl ein Reel gemessen die
   Hälfte kostet. Am 13.09. kippte das den Tag – ein beanstandeter Entwurf
   hatte Geld gekostet, und vom Rest war so viel gebunden, dass kein Beitrag
   mehr geschrieben werden durfte, während das Reel auf Geld saß, das es nie
   brauchen würde. Jetzt zählt der mittlere Reel-Tag der letzten Woche plus ein
   Viertel Zuschlag; die Konfiguration ist nur noch die Obergrenze, solange
   nichts gemessen wurde. */
export function reelReserve(tage = {}, deckel = 0.11, fenster = 7) {
  const werte = Object.keys(tage).sort().slice(-fenster)
    .map((d) => (tage[d]?.zwecke?.reel || 0) + (tage[d]?.zwecke?.["reel-faktencheck"] || 0))
    .filter((v) => v > 0);
  if (!werte.length) return deckel;
  /* Der Mittelwert der Tage, nicht der teuerste: Ein Tag mit Neuversuch darf
     nicht jeden folgenden Tag Geld binden. Der Zuschlag deckt die Schwankung. */
  const sortiert = werte.sort((a, b) => a - b);
  const mitte = sortiert.length % 2 ? sortiert[(sortiert.length - 1) / 2] : (sortiert[sortiert.length / 2 - 1] + sortiert[sortiert.length / 2]) / 2;
  return Math.min(deckel, Math.max(0.05, Math.round(mitte * 1.25 * 1000) / 1000));
}

const istAntwort = (zweck) => ANTWORT_ZWECKE.includes(schluessel(zweck));
export const tagesStand = () => vorbelastung + summeInhalt();
export const tagesLimit = () => limitUsd;
export const antwortStand = () => antwortVorbelastung + summeAntworten();
export const antwortLimit = () => antwortLimitUsd;

/* --- Was ein Aufruf kostet, bevor er läuft ------------------------------
   Geprüft wird vor dem Aufruf, gezählt danach. Eine pauschale Reserve von
   0,02 $ reichte deshalb nicht: Ein Reel-Aufruf kostet das Dreifache, und
   einzelne Tage lagen bis zu 16 % über dem Limit.

   Der Deckel wird jetzt vorab mit dem belastet, was ein Aufruf dieses Zwecks
   erfahrungsgemäß kostet. Die Werte stammen aus den Läufen der letzten Woche;
   wird ein Aufruf teurer als gedacht, rechnet der Rest des Laufs mit dem
   höheren Wert weiter. */
const ERWARTET = {
  "story-faktencheck": 0.01,
  "reel-faktencheck": 0.01,
  faktencheck: 0.01,
  /* 0,05 war geraten. Gemessen am 16.09.: 0,25 $ - ohne Cache wurde bei
     jedem pause_turn der ganze Verlauf neu bezahlt. Mit der Cache-Marke in
     autor.mjs liegt der Aufruf deutlich darunter; bis der erste Lauf eines
     Tages das gemessen hat, rechnet der Deckel mit 0,12 $ statt mit einer
     Zahl, die den Tag sprengen kann. */
  recherche: 0.12,
  stories: 0.05,
  beitrag: 0.05,
  autor: 0.05,
  reel: 0.06,
  bild: 0.01,
  /* Die Figuren des Erklaervideos tragen einen eigenen Zweck, damit die
     Ruecklage sie schuetzen kann, ohne jedes andere Bild mitzuschuetzen.
     Ohne sie faellt das Reel auf das klassische Layout zurueck. */
  erklaerbild: 0.01,
  /* Ein Aufruf je Reel, guenstiges Modell, wenige Szenen: Cent-Betrag. */
  bildregie: 0.01,
  /* Kommentare und Nachrichten laufen ueber das guenstige Modell und fassen
     alle offenen Faelle in EINEN Aufruf. Ohne eigenen Eintrag griff der
     Standardwert von 0,05 $ - das Zehnfache des Wirklichen. An einem vollen
     Tag reichte das, um die Antworten stumm ausfallen zu lassen: Der Deckel
     rechnete mit Geld, das nie ausgegeben worden waere. */
  kommentare: 0.01,
  nachrichten: 0.01,
};
/* Seit dem 15.09. schreibt das starke Modell die Antworten (siehe
   CONFIG.antworten); die 0,01 $ oben stammen aus der Haiku-Zeit. Der Wert
   hier gilt, bis der erste Aufruf des Tages gemessen ist. */
ERWARTET.kommentare = 0.05;
ERWARTET.nachrichten = 0.05;
const STANDARD = 0.05;
/* Längste Übereinstimmung gewinnt: „reel-faktencheck“ enthält „reel“. */
const schluessel = (zweck) => Object.keys(ERWARTET).sort((a, b) => b.length - a.length).find((n) => String(zweck).toLowerCase().includes(n)) || null;

/* Was ein Zweck in diesem Lauf tatsächlich gekostet hat (teuerster Aufruf).
   Die Tabelle oben ist nur der Startwert für den ersten Aufruf; sobald
   gemessen wurde, zählt die Messung – in beide Richtungen.

   Warum das wichtig ist: Am 11.09. wurde ein Reel-Entwurf vom Faktencheck zu
   Recht beanstandet („Paragraf 9“ statt „Art. 9 Abs. 3 GG“). Der zweite
   Versuch scheiterte dann nicht am Geld, sondern an der Schätzung – der
   Entwurf hatte 0,047 $ gekostet, vorab belastet wurden aber 0,06 $, und
   damit lag der Deckel rechnerisch 0,005 $ zu tief. Das Reel fiel aus,
   obwohl es bezahlbar gewesen wäre. */
const GEMESSEN = {};
const erwartetFuer = (zweck) => { const k = schluessel(zweck); if (!k) return STANDARD; return GEMESSEN[k] ?? ERWARTET[k]; };
/* Für die Rücklage im Lauf: was ein Aufruf dieses Zwecks heute voraussichtlich kostet. */
export const erwartet = (zweck) => erwartetFuer(zweck);


/* Zwecke, die einen Beitrag schmücken, aber nicht tragen. Sie brauchen den
   doppelten Spielraum ihrer Schätzung, bevor sie starten dürfen.

   Der Grund steht im Log vom 16.09.: Die Schätzung für eine Recherche lag bei
   0,05 $, der Aufruf kostete 0,252 $ - und weil vor dem Aufruf nur mit der
   Schätzung gerechnet wird, lief er trotzdem los. Gegen eine Schätzung, die
   um das Fünffache danebenliegt, hilft kein Nachrechnen hinterher; es hilft
   nur, solchen Aufrufen von vornherein mehr Luft abzuverlangen, als sie
   voraussichtlich brauchen. Was den Tag trägt - Beiträge, Stories,
   Faktenchecks - bleibt davon unberührt und rechnet weiter genau. */
const KUER = ["recherche", "recherche-loesung"];
const kuerFaktor = (zweck) => (KUER.includes(schluessel(zweck) || String(zweck).toLowerCase()) ? 2 : 1);

/* Wenn es eng wird, weicht das Bild - nie die Prüfung.

   Beides läuft über denselben Deckel, und bisher verlor schlicht, wer zuletzt
   dran war. Damit konnte ein gezeichnetes Motiv den Faktencheck des
   Abendbeitrags auffressen. Die Rangfolge ist aber eindeutig: Ein Beitrag
   ohne eigenes Motiv trägt ein Icon und sieht nüchterner aus. Ein Beitrag
   ohne Faktencheck kann falsch sein.

   Deshalb hört das Zeichnen früher auf als der harte Deckel: Der Abstand
   reicht für die Prüfungen, die am selben Tag noch kommen. */
/* Obergrenze je Beitrag.

   In der Nacht zum 17.09. verbrauchte EIN Beitrag 0.19 $ von 0.32 $: drei
   Faktencheck-Runden und ein Neuschreiben, weil der Entwurf die
   Regelbeispiele des § 243 StGB zweimal in Abs. 2 statt Abs. 1 S. 2
   verortete. Die Pruefung hatte fachlich recht - aber danach war b2
   unbezahlbar und alle neun Stories fielen aus.

   Ein Beitrag, der seine Grenze reisst, wird deshalb ZURUECKGESTELLT, nicht
   ungeprueft veroeffentlicht: Sein Entwurf bleibt gespeichert und wartet auf
   den naechsten Tag. Der Rest des Tages behaelt sein Geld. */
let postenGrenze = Infinity, postenStart = 0, postenLabel = "";
export function postenBeginnen(label, grenze) {
  postenLabel = label; postenStart = tagesStand();
  postenGrenze = Number.isFinite(grenze) && grenze > 0 ? grenze : Infinity;
}
export function postenBeenden() { postenGrenze = Infinity; postenStart = 0; postenLabel = ""; }
/** Läuft gerade ein Posten? Ein verschachtelter Aufruf soll ihn fortführen, nicht neu beginnen. */
export const postenAktiv = () => Number.isFinite(postenGrenze);
/** Was der laufende Posten bisher gekostet hat. */
export const postenStand = () => runden(Math.max(0, tagesStand() - postenStart));
/** Eigener Fehlertyp: Nur DIESER Posten ist am Ende, nicht der Tag. */
export class PostenFehler extends BudgetFehler {}

const PRUEF_ABSTAND = Number(process.env.IG_PRUEF_ABSTAND_USD || 0.03);
const abstandFuer = (zweck) => (schluessel(zweck) === "bild" ? PRUEF_ABSTAND : 0);

/* Reicht die Obergrenze des laufenden Postens noch? Antwortzwecke haben einen
   eigenen Topf und kennen keine Posten. */
const postenFrei = (zweck) => istAntwort(zweck)
  || postenStand() + erwartetFuer(zweck) * kuerFaktor(zweck) <= postenGrenze;

export const budgetFrei = (zweck = "") => istAntwort(zweck)
  ? antwortStand() + erwartetFuer(zweck) < antwortLimitUsd
  : postenFrei(zweck)
    && tagesStand() + erwartetFuer(zweck) * kuerFaktor(zweck) + abstandFuer(zweck) + fremdeReserve(zweck) < limitUsd;

export function budgetPruefen(zweck = "Claude-Aufruf") {
  if (budgetFrei(zweck)) return;
  if (istAntwort(zweck)) throw new BudgetFehler(`Antwortbudget erreicht (${antwortStand().toFixed(3)} $ von ${antwortLimitUsd.toFixed(2)} $) – ${zweck} wartet bis morgen.`);
  /* Zuerst der Posten: Ist NUR er am Ende, geht der Tag weiter. Die
     Unterscheidung traegt der Fehlertyp, nicht der Wortlaut. */
  if (!postenFrei(zweck)) {
    throw new PostenFehler(`Obergrenze für ${postenLabel || "diesen Beitrag"} erreicht (${postenStand().toFixed(3)} $ von ${postenGrenze.toFixed(2)} $) – zurückgestellt, der Entwurf wartet auf morgen. Der Rest des Tages behält sein Geld.`);
  }
  const fremd = fremdeReserve(zweck);
  const rest = fremd ? ` (davon ${fremd.toFixed(2)} $ für ${fremdeLabel(zweck)} zurückgelegt)` : "";
  throw new BudgetFehler(`Tagesbudget erreicht (${tagesStand().toFixed(3)} $ von ${limitUsd.toFixed(2)} $)${rest} – ${zweck} wartet bis morgen.`);
}

export function erfassen(modell, usage, zweck = "") {
  if (!usage) return 0;
  const p = PREISE[modell] || PREISE["claude-opus-5"];
  const usd = ((usage.input_tokens || 0) * p.ein + (usage.output_tokens || 0) * p.aus + (usage.cache_read_input_tokens || 0) * p.cacheLesen + (usage.cache_creation_input_tokens || 0) * p.cacheSchreiben) / 1e6;
  posten.push({ modell, zweck, usd, ein: usage.input_tokens || 0, aus: usage.output_tokens || 0, cache: usage.cache_read_input_tokens || 0 });
  /* Der Rest des Laufs rechnet ab jetzt mit dem gemessenen Wert (dem teuersten
     Aufruf dieses Zwecks), nicht mehr mit der Schätzung. */
  const zweckSchluessel = schluessel(zweck);
  if (zweckSchluessel) GEMESSEN[zweckSchluessel] = Math.max(GEMESSEN[zweckSchluessel] ?? 0, usd);
  const k = (n) => (n >= 1000 ? `${(n / 1000).toFixed(1)}k` : String(n));
  console.log(`  $ ${usd.toFixed(4)} ${zweck || modell} · ${k(usage.input_tokens || 0)} ein / ${k(usage.output_tokens || 0)} aus / ${k(usage.cache_read_input_tokens || 0)} Cache`);
  if (speichern) { try { speichern(tagesStand(), posten.length, jeZweck(), messungen(), antwortStand()); } catch (e) { console.warn(`  ! Kosten nicht gespeichert: ${e.message}`); } }
  return usd;
}

/**
 * Ein Posten, dessen Preis nicht aus Token folgt, sondern pro Stück feststeht -
 * ein erzeugtes Bild etwa. Der Preis kommt aus der Konfiguration, weil die
 * Bild-Schnittstelle ihn nicht zurückmeldet; er ist bewusst etwas höher
 * angesetzt als der Listenpreis, damit der Tagesdeckel nie zu niedrig rechnet.
 */
export function erfassenStueck(usd, zweck = "bild", was = "") {
  const betrag = Math.max(0, Number(usd) || 0);
  posten.push({ modell: zweck, zweck, usd: betrag, ein: 0, aus: 0, cache: 0 });
  const zweckSchluessel = schluessel(zweck);
  if (zweckSchluessel) GEMESSEN[zweckSchluessel] = Math.max(GEMESSEN[zweckSchluessel] ?? 0, betrag);
  console.log(`  $ ${betrag.toFixed(4)} ${zweck}${was ? ` · ${was}` : ""}`);
  if (speichern) { try { speichern(tagesStand(), posten.length, jeZweck(), messungen(), antwortStand()); } catch (e) { console.warn(`  ! Kosten nicht gespeichert: ${e.message}`); } }
  return betrag;
}

/** Kosten dieses Laufs je Zweck (z. B. recherche, beitrag, faktencheck). */
export function jeZweck() {
  const m = {};
  for (const p of posten) m[p.zweck || p.modell] = (m[p.zweck || p.modell] || 0) + p.usd;
  return m;
}

export function summe() {
  return posten.reduce((a, b) => a + b.usd, 0);
}
/* Die beiden Töpfe, getrennt nach Zweck. */
export function summeInhalt() {
  return posten.filter((p) => !istAntwort(p.zweck || "")).reduce((a, b) => a + b.usd, 0);
}
export function summeAntworten() {
  return posten.filter((p) => istAntwort(p.zweck || "")).reduce((a, b) => a + b.usd, 0);
}

export function abschluss() {
  return { usd: summe(), aufrufe: posten.length, cacheAnteil: posten.length ? posten.reduce((a, b) => a + b.cache, 0) / Math.max(1, posten.reduce((a, b) => a + b.ein + b.cache, 0)) : 0, posten: [...posten] };
}

/* Auf drei Nachkommastellen - Cent-Bruchteile sollen sich nicht ueber viele
   Laeufe zu einem Phantombetrag aufaddieren. */
export const runden = (x) => Math.round(x * 1000) / 1000;

/**
 * Wie viel von einer Wunschliste zurueckgelegt werden darf, wenn nur `frei`
 * uebrig ist: der Reihe nach aufsummieren, beim ersten Posten abbrechen, der
 * nicht mehr hineinpasst.
 *
 * Der Grund steht im Protokoll vom 17.09.: 0.13 $ lagen fuer einen Beitrag
 * und die Erklaerfiguren zurueck, frei waren 0.045 $. Der Beitrag war davon
 * nie zu bezahlen - seine Ruecklage hat aber die neun Stories blockiert, die
 * zusammen weniger gekostet haetten. Geld fuer etwas Unbezahlbares
 * zurueckzulegen heisst, es zweimal zu verlieren.
 *
 * Bewusst der Reihe nach und nicht "was am besten passt": Die Reihenfolge ist
 * die Rangfolge. Was passt, behaelt seinen Vorrang; was nicht passt, gibt den
 * Rest fuer das Billigere frei.
 */
export function bezahlbareSumme(preise, frei) {
  const grenze = Math.max(0, Number(frei) || 0);
  let summe = 0;
  for (const p of preise) {
    const preis = Math.max(0, Number(p) || 0);
    if (summe + preis > grenze) break;
    summe += preis;
  }
  return runden(summe);
}
