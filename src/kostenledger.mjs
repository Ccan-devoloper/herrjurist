/* ==========================================================================
   Dauerhafte Einzelkosten-Historie.

   state/kosten.json hatte bisher Summen je Tag/Zweck. Das reicht fuer Budget
   und Wochenbericht, beantwortet aber nicht die Betriebsfrage: Welcher konkrete
   Aufruf hat wie viel gekostet, womit und warum?

   Quelle ist bewusst das Budget-Journal, nicht eine zweite Kostenschaetzung.
   Das Journal wird vor jedem bezahlten Provideraufruf durable und kennt nach
   der Antwort den tatsaechlichen Betrag. Einzelkosten werden nach
   reservationId zusammengefuehrt; wiederholtes Synchronisieren ist deshalb
   idempotent.

   Alte Summen bleiben unangetastet. Die Detailhistorie beginnt mit der
   Einfuehrung dieses Moduls; fruehere Preview-/Hilfskosten koennen darin
   fehlen und werden nicht nachtraeglich erfunden.
   ========================================================================== */

const runden = (n) => Math.round((Number(n) || 0) * 1e6) / 1e6;

const WARUM = Object.freeze({
  autor: "Entwurf eines Feedbeitrags",
  reel: "Entwurf bzw. Textarbeit fuer ein Reel",
  stories: "Erzeugung von Story-Texten",
  faktencheck: "Juristischer Faktencheck eines Feedbeitrags",
  "reel-faktencheck": "Juristischer Faktencheck eines Reels",
  "story-faktencheck": "Juristischer Faktencheck von Stories",
  bildregie: "Bildregie bzw. Motivplanung",
  bild: "Erzeugung eines Cover-/Beitragsbildes",
  "bild-qa": "Visuelle Qualitaetspruefung eines Bildes",
  erklaerbild: "Erzeugung eines Motivs fuer ein Erklaer-Reel",
  loesungsskizze: "Erzeugung einer Loesungsskizze",
  loesung: "Erzeugung einer Loesung",
  kommentare: "Antworten auf Instagram-Kommentare",
  nachrichten: "Antworten auf Instagram-Nachrichten",
  recherche: "Recherche zur Themenfindung",
  "recherche-loesung": "Recherche fuer eine Loesung",
});

export function kostenGrund(zweck, slot = null) {
  const basis = WARUM[zweck] || `Kostenpflichtiger Provideraufruf fuer „${zweck || "unbekannt"}“`;
  return slot ? `${basis} (Slot ${slot})` : basis;
}

function normalisieren(e, kanal) {
  const state = e.state || "unknown";
  const bekannt = state === "settled" && Number.isFinite(Number(e.actualUsd));
  const ungeklaert = state === "sent" || state === "unresolved";
  return {
    reservationId: e.reservationId,
    datum: e.date || null,
    kanal: e.channel || kanal || null,
    topf: e.bucket || null,
    zweck: e.purpose || null,
    warum: e.reason || kostenGrund(e.purpose, e.slot),
    slot: e.slot || null,
    versuch: e.attempt ?? null,
    provider: e.provider || null,
    modell: e.model || null,
    promptVersion: e.promptVersion || null,
    status: state,
    reserviertUsd: runden(e.reservedUsd),
    kostenUsd: bekannt ? runden(e.actualUsd) : null,
    konservativGebundenUsd: ungeklaert ? runden(e.reservedUsd) : 0,
    kostenBekannt: bekannt,
    outcome: e.outcome || null,
    fehler: e.errorType || e.grund || null,
    usage: e.usage || null,
    erstelltAm: e.createdAt || null,
    aktualisiertAm: e.updatedAt || null,
  };
}

/**
 * Fuehrt einen Journal-Snapshot in die dauerhafte Kostenhistorie zusammen.
 * Mutation des Eingabeobjekts wird vermieden, damit Tests und Aufrufer den
 * Vorher-/Nachher-Zustand sauber vergleichen koennen.
 */
export function einzelkostenSynchronisieren(kosten = {}, journal = {}) {
  const neu = structuredClone(kosten || {});
  const datum = journal?.datum;
  if (!datum || !Array.isArray(journal?.eintraege)) return neu;

  neu.einzelkosten ||= {};
  neu.einzelkostenSummen ||= {};
  neu.einzelkostenMeta ||= {
    version: 1,
    seit: new Date().toISOString(),
    hinweis: "Detailhistorie ist ab Einfuehrung vollstaendig; aeltere Preview-/Hilfskosten koennen fehlen.",
  };

  const alt = Array.isArray(neu.einzelkosten[datum]) ? neu.einzelkosten[datum] : [];
  const nachId = new Map(alt.filter((x) => x?.reservationId).map((x) => [x.reservationId, x]));

  for (const roh of journal.eintraege) {
    if (!roh?.reservationId) continue;
    const jetzt = normalisieren(roh, journal.kanal);
    const vorher = nachId.get(roh.reservationId) || {};
    nachId.set(roh.reservationId, { ...vorher, ...jetzt });
  }

  const liste = [...nachId.values()].sort((a, b) =>
    String(a.erstelltAm || a.reservationId).localeCompare(String(b.erstelltAm || b.reservationId)));
  neu.einzelkosten[datum] = liste;

  const bekannte = liste.filter((e) => e.kostenBekannt);
  const ungeklaerte = liste.filter((e) => e.status === "sent" || e.status === "unresolved");
  neu.einzelkostenSummen[datum] = {
    bekannteKostenUsd: runden(bekannte.reduce((s, e) => s + Number(e.kostenUsd || 0), 0)),
    bekannteKostenposten: bekannte.length,
    ungeklaerteMaxBelastungUsd: runden(ungeklaerte.reduce((s, e) => s + Number(e.reserviertUsd || 0), 0)),
    ungeklaertePosten: ungeklaerte.length,
    eintraegeGesamt: liste.length,
    stand: new Date().toISOString(),
  };

  return neu;
}
