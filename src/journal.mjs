/* ==========================================================================
   Das Budget-Journal: Reservierungen, die einen Runner-Absturz überleben.

   Die Admission aus budget.mjs lebt im Prozess. Solange der Prozess lebt,
   hält sie - aber ein GitHub-Runner stirbt auch mal hart: Timeout, OOM,
   Abbruch, der Job wird abgeschossen. Dann läuft folgender Ablauf ins Leere:

     reservieren → gesendet → der Anbieter berechnet Geld → Runner stirbt
     → kein finally, kein Tagesabschluss, keine Zeile in kosten.json
     → der nächste Stundenlauf weiß von diesem Geld nichts
     → und darf denselben Betrag ein zweites Mal ausgeben.

   Über sechzehn Läufe am Tag ist das kein theoretischer Fall. Es ist
   dieselbe Fehlerklasse wie der verlorene Kosten- und Publish-Zustand vom
   18.09., nur eine Ebene tiefer - und sie macht aus dem Tagesdeckel eine
   Zusage, die nur innerhalb eines Prozesses gilt.

   Deshalb wird JEDE Reservierung durable, bevor der Anbieter etwas zu sehen
   bekommt. Zwei Schreibvorgänge je Aufruf, beide vor dem Absenden:

     1. `reserved`  Das Geld ist zugesagt. Gesendet wurde noch nichts.
     2. `sent`      Unmittelbar vor dem Absenden. Ab hier ist offen, ob der
                    Anbieter berechnet hat.

   Warum zwei und nicht einer: Ohne den zweiten Schreibvorgang lässt sich
   hinterher nicht unterscheiden, ob der Absturz VOR oder NACH dem Absenden
   kam. Man müsste jede Reservierung als möglicherweise ausgegeben behandeln
   und verschenkte jedes Mal Geld, das nie ausgegeben wurde. Mit dem zweiten
   Schreibvorgang gilt:

     Eintrag steht auf `reserved`  → Schritt 2 wurde nie erreicht → es wurde
                                     BEWEISBAR nicht gesendet → freigeben.
     Eintrag steht auf `sent`      → könnte berechnet worden sein → der
                                     Betrag bleibt blockiert.

   Was NICHT durable geschrieben wird, sondern beim nächsten Schreibvorgang
   mitfährt: die Abrechnung (`settled`) und der ungeklärte Fall
   (`unresolved`). Beides darf verlorengehen, ohne dass die Zusage bricht -
   wer eine Abrechnung verliert, behält den reservierten Betrag als
   verbraucht, und der ist immer größer oder gleich dem tatsächlichen.

   Die Richtung des Fehlers ist der ganze Punkt: Wir verlieren im Zweifel
   Spielraum, nie Kontrolle.

   Zwei Dinge, die beim Gegenlesen aufgefallen sind und hier ausdrücklich
   gelöst werden:

   TRANSAKTIONALITÄT. Ein Schreibvorgang darf den maßgeblichen Zustand erst
   ändern, wenn er bestätigt ist. Die erste Fassung setzte den Eintrag lokal
   auf `sent`, schrieb, und warf bei fehlgeschlagenem Push. Der Anbieter wurde
   korrekt nicht gerufen - aber die lokale Datei trug bereits `sent`, und ein
   späterer Push (etwa der Tagesabschluss) hätte diesen Zustand doch noch
   hinausgetragen. Der nächste Lauf hätte Geld blockiert, das nie ausgegeben
   wurde: kein Overspend, aber ein Phantomverbrauch, der Pflichtinhalte
   verdrängt. Jetzt wird auf einer Kopie gearbeitet; erst die bestätigte
   Durability übernimmt sie. Scheitert sie, wird der alte Stand
   zurückgeschrieben, damit auch ein späterer Push nichts Falsches trägt.

   CUTOVER. Das Journal kennt nur, was seit seiner Einführung durch es
   hindurchgegangen ist. Was der Tag davor schon gekostet hat, steht in
   kosten.json. Ein `max(kosten.json, journal)` wäre bequem und falsch: Sind
   die beiden Mengen disjunkt - 0,10 $ aus der Zeit davor, 0,08 $ ungeklärt
   danach -, ist der wahre Stand 0,18 $ und nicht 0,10 $. Deshalb wird der
   Altbestand EINMAL beim Anlegen des Tagesjournals als `legacyBaseline`
   eingefroren; danach ist das Journal für diesen Tag maßgeblich und der
   Stand ist Baseline + Beiträge des Journals. Dieselben abgerechneten
   Aufrufe stehen zwar auch in kosten.json, werden aber nicht ein zweites Mal
   addiert, weil die Baseline nicht mitwächst.
   ========================================================================== */

import { BudgetStopp } from "./budgetstopp.mjs";

export const JZUSTAND = Object.freeze({
  RESERVIERT: "reserved",
  GESENDET: "sent",
  ABGERECHNET: "settled",
  UNGEKLAERT: "unresolved",
  VERFALLEN: "expired",
});

const TOEPFE = ["core", "engagement", "research"];
const runden = (n) => Math.round((Number(n) || 0) * 1e6) / 1e6;

/** Die durable Sicherung hat nicht bestätigt - der Aufruf findet nicht statt. */
export class JournalNichtDurable extends BudgetStopp {
  constructor(zweck, phase) {
    super(`Budget-Journal für „${zweck}“ (${phase}) ist nicht durable geworden. `
      + `Der Aufruf wird nicht gesendet: Eine Reservierung, die den nächsten Lauf nicht erreicht, `
      + `ist keine Reservierung.`);
    this.name = "JournalNichtDurable";
    this.zweck = zweck; this.phase = phase;
  }
}

/**
 * Öffnet das Journal eines Tages.
 *
 * @param {object}   o
 * @param {Function} o.lesen       () => {datum, eintraege} | null
 * @param {Function} o.schreiben   async (inhalt) => boolean (durable bestätigt)
 * @param {string}   o.datum       ISO-Tag
 * @param {string}   o.kanal
 * @param {boolean}  o.remoteNoetig  ob eine Bestätigung verlangt wird
 */
export function journalStarten({ lesen, schreiben, datum, kanal = null, remoteNoetig = true, legacyBaseline = null }) {
  const bestand = lesen?.() || null;
  /* Ein Journal des Vortags ist erledigt - Töpfe gelten je Tag. */
  const heutiges = bestand?.datum === datum ? bestand : null;
  let eintraege = heutiges && Array.isArray(heutiges.eintraege) ? heutiges.eintraege.map((e) => ({ ...e })) : [];

  /* Die Baseline wird genau EINMAL je Tag festgeschrieben - beim Anlegen des
     Journals. Gibt es schon eines, gilt dessen Baseline; ein späterer Lauf
     darf sie nicht aus einer inzwischen gewachsenen kosten.json neu ableiten,
     sonst zählt er die Aufrufe des Journals ein zweites Mal. */
  const basis = Object.fromEntries(TOEPFE.map((t) => [t, 0]));
  const baseline = heutiges?.legacyBaseline
    ? { ...basis, ...heutiges.legacyBaseline }
    : { ...basis, ...(legacyBaseline || {}) };
  const baselineNeu = !heutiges?.legacyBaseline;

  let laufendeNummer = eintraege.length;
  let schreibFehler = null;

  const inhalt = (liste = eintraege) => ({
    datum, kanal, legacyBaseline: baseline, eintraege: liste, stand: new Date().toISOString(),
  });

  /**
   * Schreibt einen Stand durable. `liste` ist der Stand, der gelten SOLL -
   * nicht zwingend der, der gerade im Speicher steht. Erst der bestätigte
   * Schreibvorgang macht ihn maßgeblich.
   */
  const sichern = async (liste, zweck, phase) => {
    let ok = false;
    try { ok = await schreiben(inhalt(liste)); }
    catch (e) { schreibFehler = e; ok = false; }
    if (!ok && remoteNoetig) throw new JournalNichtDurable(zweck, phase);
    return ok;
  };

  /**
   * Was aus früheren Läufen dieses Tages übrig ist - und was davon Geld
   * blockiert. Wird einmal zu Laufbeginn aufgerufen.
   */
  const uebernahme = () => {
    /* Der Stand ist Baseline PLUS die Beiträge des Journals - nicht das
       Maximum von beidem. Die beiden Mengen sind disjunkt. */
    const vorbelastung = Object.fromEntries(TOEPFE.map((t) => [t, runden(baseline[t] || 0)]));
    const freigegeben = [];
    const blockiert = [];
    for (const e of eintraege) {
      if (!TOEPFE.includes(e.bucket)) continue;
      if (e.state === JZUSTAND.ABGERECHNET) {
        vorbelastung[e.bucket] = runden(vorbelastung[e.bucket] + Number(e.actualUsd || 0));
      } else if (e.state === JZUSTAND.GESENDET || e.state === JZUSTAND.UNGEKLAERT) {
        /* Gesendet und nie abgerechnet: Der Anbieter KÖNNTE berechnet haben.
           Konservativ gilt die Reservierung als verbraucht. */
        vorbelastung[e.bucket] = runden(vorbelastung[e.bucket] + Number(e.reservedUsd || 0));
        if (e.state === JZUSTAND.GESENDET) {
          e.state = JZUSTAND.UNGEKLAERT;
          e.grund = e.grund || "Lauf endete nach dem Senden ohne Abrechnung";
          e.updatedAt = new Date().toISOString();
        }
        blockiert.push({ ...e });
      } else if (e.state === JZUSTAND.RESERVIERT) {
        /* Nie bis zum Sendevermerk gekommen: beweisbar nicht gesendet. */
        e.state = JZUSTAND.VERFALLEN;
        e.grund = "Lauf endete vor dem Senden";
        e.updatedAt = new Date().toISOString();
        freigegeben.push({ ...e });
      }
    }
    return { vorbelastung, freigegeben, blockiert };
  };

  const finden = (id) => eintraege.find((e) => e.reservationId === id) || null;

  /** Schritt 1: durable, bevor irgendetwas gesendet wird. */
  const reservieren = async ({ bucket, purpose, attempt = 1, reservedUsd, slot = null }) => {
    const jetzt = new Date().toISOString();
    const reservationId = `${datum}-${String(laufendeNummer + 1).padStart(4, "0")}-${purpose}`;
    const neuerEintrag = {
      reservationId, date: datum, bucket, purpose, attempt, slot,
      reservedUsd: runden(reservedUsd), actualUsd: null,
      state: JZUSTAND.RESERVIERT, createdAt: jetzt, updatedAt: jetzt,
    };
    /* Erst schreiben, dann übernehmen. Scheitert der Schreibvorgang, hat es
       diese Reservierung nie gegeben - und der Aufruf findet nicht statt.
       Trägt ein späterer Push den Eintrag doch noch hinaus, steht er auf
       `reserved`; der nächste Lauf gibt ihn frei, weil der Sendevermerk
       fehlt. Das ist die sichere Richtung. */
    await sichern([...eintraege, neuerEintrag], purpose, "reservierung");
    eintraege = [...eintraege, neuerEintrag];
    laufendeNummer += 1;
    return reservationId;
  };

  /**
   * Schritt 2: durable, unmittelbar vor dem Absenden - und transaktional.
   *
   * Der maßgebliche Zustand wird ERST nach bestätigter Durability auf `sent`
   * gesetzt. Scheitert der Schreibvorgang, wird der alte Stand
   * zurückgeschrieben: Ein späterer Push darf kein `sent` hinaustragen für
   * einen Aufruf, der nie gesendet wurde - das wäre Phantomverbrauch, der
   * echte Pflichtinhalte verdrängt.
   */
  const senden = async (id) => {
    const alt = finden(id);
    if (!alt) return false;
    const naechster = eintraege.map((e) => (e.reservationId === id
      ? { ...e, state: JZUSTAND.GESENDET, updatedAt: new Date().toISOString() }
      : e));
    try {
      await sichern(naechster, alt.purpose, "sendevermerk");
    } catch (fehler) {
      /* Zurückrollen, und zwar auch auf der Platte. Ein Fehlschlag hier ist
         nicht schlimm - der maßgebliche Stand im Speicher ist ohnehin der
         alte, und die nächste Sicherung schreibt ihn erneut. */
      try { await schreiben(inhalt(eintraege)); } catch { /* der Stand im Speicher bleibt maßgeblich */ }
      throw fehler;
    }
    eintraege = naechster;
    return true;
  };

  /* Ab hier nur noch im Speicher: Diese Übergänge dürfen verlorengehen, ohne
     dass die Zusage bricht - der nächste Lauf rechnet dann konservativer. */
  const aendern = (id, felder, nurWenn = null) => {
    const e = finden(id); if (!e) return false;
    if (nurWenn && !nurWenn(e)) return false;
    eintraege = eintraege.map((x) => (x.reservationId === id
      ? { ...x, ...felder, updatedAt: new Date().toISOString() } : x));
    return true;
  };
  const abrechnen = (id, actualUsd) => aendern(id, { state: JZUSTAND.ABGERECHNET, actualUsd: runden(actualUsd) });
  const ungeklaert = (id, grund = "Kosten nach dem Senden unbekannt") => aendern(id, { state: JZUSTAND.UNGEKLAERT, grund });
  const verfallen = (id, grund = "vor dem Senden abgebrochen") =>
    aendern(id, { state: JZUSTAND.VERFALLEN, grund }, (e) => e.state === JZUSTAND.RESERVIERT);

  /** Am Ende des Laufs: die offenen Übergänge festschreiben. */
  const abschluss = async () => {
    try { return await schreiben(inhalt(eintraege)); } catch { return false; }
  };

  return {
    uebernahme, reservieren, senden, abrechnen, ungeklaert, verfallen, abschluss,
    eintraege: () => eintraege.map((e) => ({ ...e })),
    letzterFehler: () => schreibFehler,
    legacyBaseline: () => ({ ...baseline }),
    baselineNeu: () => baselineNeu,
    stand: () => ({
      datum, anzahl: eintraege.length, legacyBaseline: { ...baseline },
      jeZustand: eintraege.reduce((a, e) => ({ ...a, [e.state]: (a[e.state] || 0) + 1 }), {}),
    }),
  };
}
