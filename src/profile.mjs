/* ==========================================================================
   Wovon ein Token-Ceiling eine Aussage ist - und wovon nicht.

   Ein Ceiling (`max_tokens`) beantwortet eine einzige Frage: Wie gross darf
   die Antwort EINES Aufrufs werden, bevor sie abgeschnitten wird? Das ist
   etwas anderes als der Tagesdeckel, der sagt, wie viel Geld ein Topf
   insgesamt ausgeben darf. Die beiden werden hier bewusst getrennt gehalten;
   eine Groesse, die beides gleichzeitig bedeutet, laesst sich nicht
   vernuenftig kalibrieren.

   Zwei Ebenen, weil Hashes keine Naehe kennen:

     Exaktes Profil     Alles, was die Laenge einer Antwort strukturell
                        beeinflusst: Aufgabe, Anbieter, Modell, Aufwand,
                        Denkmodus, System-Prompt, Schema, Werkzeuge,
                        Projektionsversion, Ceiling. NICHT der konkrete
                        Beitragstext - sonst waere jeder Beitrag ein neues
                        Profil und nichts je kalibriert.

     Kalibrierfamilie   Ein lesbarer Name wie „reel-autor / sonnet-5 / low /
                        reel-schema-v3“. Er gruppiert Profile, die derselben
                        Aufgabe dienen, und dient als Evidenz fuer ein neues
                        Profil - nicht als Ersatz fuer dessen eigene Messung.

   Was hier ausdruecklich NICHT passiert: aus einem Hash den „aehnlichsten“
   suchen. Hashes haben keine semantische Naehe; wer so etwas baut, baut einen
   Zufallsgenerator mit Fachvokabular.
   ========================================================================== */

import crypto from "node:crypto";

const kurzHash = (text) => crypto.createHash("sha256").update(String(text)).digest("hex").slice(0, 12);

/** Deterministischer Hash eines Textbausteins (System-Prompt, Schema, Werkzeuge). */
export function bausteinHash(wert) {
  if (wert == null) return "leer";
  return kurzHash(typeof wert === "string" ? wert : JSON.stringify(wert));
}

/**
 * Das exakte Profil eines Aufruftyps. Zwei Aufrufe mit derselben Kennung
 * sind statistisch vergleichbar; ihre Antwortlaengen duerfen in dieselbe
 * Messreihe.
 */
export function exaktesProfil({
  zweck, provider, modell, effort = null, denkmodus = null,
  systemHash = "leer", schemaHash = "leer", werkzeugHash = "leer",
  promptVersion = "1", maxTokens = null,
}) {
  const teile = [zweck, provider, modell, effort ?? "-", denkmodus ?? "-", systemHash, schemaHash, werkzeugHash, promptVersion, String(maxTokens ?? "-")];
  return { id: `${zweck}:${kurzHash(teile.join("|"))}`, teile };
}

/**
 * Die Kalibrierfamilie: lesbar, grob, nuetzlich als Ausgangspunkt. Sie sagt
 * „solche Aufgaben sehen ungefaehr so aus“ - nicht „dieses Profil ist
 * kalibriert“.
 */
export function kalibrierFamilie({ zweck, modell, effort = null, schemaVersion = null }) {
  return [zweck, modell, effort ?? "-", schemaVersion ?? "-"].join(" / ");
}

/* --- Rollendes Fenster ---------------------------------------------------
   Perzentile werden ANGEZEIGT, nicht gespeichert. Wer nur p95 und n
   aufhebt, kann daraus spaeter keinen neuen p95 rechnen; die Rohwerte sind
   bei diesen Datenmengen ohnehin klein genug. */
export const FENSTER_GROESSE = 100;

export function leeresFenster(profilId, familie) {
  return {
    profilId, familie,
    letzteAusgabeTokens: [],
    aufrufeGesamt: 0,
    erfolgreicheAufrufe: 0,
    abschnitte: 0,          // stop_reason === "max_tokens"
    schemaFehler: 0,
    anbieterFehler: 0,
    sonstigeFehler: 0,
    aktuellesCeiling: null,
    ceilingGesetztAm: null,
    unkalibriert: true,
    zuletzt: null,
  };
}

/**
 * Traegt einen Aufruf in das Fenster ein.
 *
 * Bewusst werden AUCH die gescheiterten gezaehlt. Wer nur erfolgreiche
 * Aufrufe speichert, misst am Ende, wie lang die Antworten waren, die nicht
 * abgeschnitten wurden - und haelt das fuer die Verteilung der Antworten.
 * Das ist Survivorship Bias mit Nachkommastellen.
 */
export function fensterAktualisieren(fenster, { ausgabeTokens = null, stopReason = null, fehlerArt = null, ceiling = null, zeit = null }) {
  const f = { ...fenster, letzteAusgabeTokens: [...fenster.letzteAusgabeTokens] };
  f.aufrufeGesamt += 1;
  f.zuletzt = zeit || new Date().toISOString();
  if (ceiling != null && ceiling !== f.aktuellesCeiling) { f.aktuellesCeiling = ceiling; f.ceilingGesetztAm = f.zuletzt; }
  if (stopReason === "max_tokens") f.abschnitte += 1;
  if (fehlerArt === "schema") f.schemaFehler += 1;
  else if (fehlerArt === "anbieter") f.anbieterFehler += 1;
  else if (fehlerArt) f.sonstigeFehler += 1;
  if (!fehlerArt && stopReason !== "max_tokens" && ausgabeTokens != null) {
    f.erfolgreicheAufrufe += 1;
    f.letzteAusgabeTokens.push(ausgabeTokens);
    if (f.letzteAusgabeTokens.length > FENSTER_GROESSE) f.letzteAusgabeTokens = f.letzteAusgabeTokens.slice(-FENSTER_GROESSE);
  }
  if (f.erfolgreicheAufrufe >= 20) f.unkalibriert = false;
  return f;
}

/** p50/p95/p99 zur Anzeige. Nearest-rank, damit kleine Reihen nicht luegen. */
export function perzentile(werte) {
  const w = [...werte].filter((x) => Number.isFinite(x)).sort((a, b) => a - b);
  if (!w.length) return { n: 0, p50: null, p95: null, p99: null, max: null };
  const rang = (p) => w[Math.min(w.length - 1, Math.max(0, Math.ceil((p / 100) * w.length) - 1))];
  return { n: w.length, p50: rang(50), p95: rang(95), p99: rang(99), max: w[w.length - 1] };
}

/**
 * Einseitige 95-%-Obergrenze fuer die Abschneide-Wahrscheinlichkeit.
 *
 * k = 0: die geschlossene Form 1 - 0.05^(1/n). „Bisher nie abgeschnitten“
 *        heisst nicht „schneidet nie ab“ - bei n = 20 liegt die Obergrenze
 *        noch bei 13,9 %.
 * k > 0: exakte Clopper-Pearson-Grenze, hier ueber die Verteilungsfunktion
 *        der Binomialverteilung gesucht.
 *
 * Diese Zahl bewertet AUSSCHLIESSLICH das Risiko, dass eine Antwort am
 * Ceiling abgeschnitten wird. Ueber die fachliche Qualitaet des Inhalts sagt
 * sie nichts.
 */
export function abschneideGrenze(n, k = 0) {
  if (!n || n <= 0) return null;
  if (k <= 0) return 1 - Math.pow(0.05, 1 / n);
  if (k >= n) return 1;
  /* P(X <= k | n, p) = 0.05 nach p aufloesen - monoton fallend in p. */
  const summe = (p) => {
    let s = 0, term = Math.pow(1 - p, n);
    for (let i = 0; i <= k; i++) {
      s += term;
      term = term * ((n - i) / (i + 1)) * (p / (1 - p));
    }
    return s;
  };
  let lo = k / n, hi = 1;
  for (let i = 0; i < 200; i++) {
    const m = (lo + hi) / 2;
    if (summe(m) > 0.05) lo = m; else hi = m;
  }
  return (lo + hi) / 2;
}

/* Feste Auswertungspunkte. Nach jedem einzelnen Aufruf zu rechnen erzeugt
   Rauschen, das wie Erkenntnis aussieht. */
export const CHECKPOINTS = [20, 40, 60, 100];

/**
 * Was die Messung nahelegt - als VORSCHLAG. Phase 1a veraendert kein Ceiling
 * automatisch, weder nach oben noch nach unten. Ein automatisch gesenktes
 * Ceiling erzeugt Abschnitte, Abschnitte erzeugen Neuversuche, und
 * Neuversuche kosten mehr als der gesparte Spielraum je wert war.
 */
export function ceilingVorschlag(fenster, { sicherheitsfaktor = 1.5 } = {}) {
  const p = perzentile(fenster.letzteAusgabeTokens);
  const n = fenster.erfolgreicheAufrufe + fenster.abschnitte;
  const grenze = abschneideGrenze(n, fenster.abschnitte);
  const checkpoint = CHECKPOINTS.includes(n);
  return {
    profilId: fenster.profilId,
    familie: fenster.familie,
    n, abschnitte: fenster.abschnitte,
    ...p,
    abschneideGrenze95: grenze,
    aktuellesCeiling: fenster.aktuellesCeiling,
    vorschlag: p.p95 == null ? null : Math.ceil((p.p95 * sicherheitsfaktor) / 500) * 500,
    checkpoint,
    unkalibriert: fenster.unkalibriert,
    /* Ausdruecklich: Das ist eine Empfehlung an einen Menschen. */
    angewendet: false,
  };
}
