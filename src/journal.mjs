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
   ========================================================================== */

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
export class JournalNichtDurable extends Error {
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
export function journalStarten({ lesen, schreiben, datum, kanal = null, remoteNoetig = true }) {
  const bestand = lesen?.() || null;
  /* Ein Journal des Vortags ist erledigt - Töpfe gelten je Tag. */
  const eintraege = bestand?.datum === datum && Array.isArray(bestand.eintraege) ? bestand.eintraege.map((e) => ({ ...e })) : [];
  let laufendeNummer = eintraege.length;
  let schreibFehler = null;

  const inhalt = () => ({ datum, kanal, eintraege, stand: new Date().toISOString() });

  const sichern = async (zweck, phase) => {
    let ok = false;
    try { ok = await schreiben(inhalt()); }
    catch (e) { schreibFehler = e; ok = false; }
    if (!ok && remoteNoetig) throw new JournalNichtDurable(zweck, phase);
    return ok;
  };

  /**
   * Was aus früheren Läufen dieses Tages übrig ist - und was davon Geld
   * blockiert. Wird einmal zu Laufbeginn aufgerufen.
   */
  const uebernahme = () => {
    const vorbelastung = Object.fromEntries(TOEPFE.map((t) => [t, 0]));
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
    const reservationId = `${datum}-${String(++laufendeNummer).padStart(4, "0")}-${purpose}`;
    eintraege.push({
      reservationId, date: datum, bucket, purpose, attempt, slot,
      reservedUsd: runden(reservedUsd), actualUsd: null,
      state: JZUSTAND.RESERVIERT, createdAt: jetzt, updatedAt: jetzt,
    });
    await sichern(purpose, "reservierung");
    return reservationId;
  };

  /** Schritt 2: durable, unmittelbar vor dem Absenden. */
  const senden = async (id) => {
    const e = finden(id);
    if (!e) return false;
    e.state = JZUSTAND.GESENDET;
    e.updatedAt = new Date().toISOString();
    await sichern(e.purpose, "sendevermerk");
    return true;
  };

  /* Ab hier nur noch im Speicher: Diese Übergänge dürfen verlorengehen, ohne
     dass die Zusage bricht - der nächste Lauf rechnet dann konservativer. */
  const abrechnen = (id, actualUsd) => {
    const e = finden(id); if (!e) return false;
    e.state = JZUSTAND.ABGERECHNET; e.actualUsd = runden(actualUsd); e.updatedAt = new Date().toISOString();
    return true;
  };
  const ungeklaert = (id, grund = "Kosten nach dem Senden unbekannt") => {
    const e = finden(id); if (!e) return false;
    e.state = JZUSTAND.UNGEKLAERT; e.grund = grund; e.updatedAt = new Date().toISOString();
    return true;
  };
  const verfallen = (id, grund = "vor dem Senden abgebrochen") => {
    const e = finden(id); if (!e) return false;
    if (e.state === JZUSTAND.RESERVIERT) { e.state = JZUSTAND.VERFALLEN; e.grund = grund; e.updatedAt = new Date().toISOString(); }
    return true;
  };

  /** Am Ende des Laufs: die offenen Übergänge festschreiben. */
  const abschluss = async () => {
    try { return await schreiben(inhalt()); } catch { return false; }
  };

  return {
    uebernahme, reservieren, senden, abrechnen, ungeklaert, verfallen, abschluss,
    eintraege: () => eintraege.map((e) => ({ ...e })),
    letzterFehler: () => schreibFehler,
    stand: () => ({
      datum, anzahl: eintraege.length,
      jeZustand: eintraege.reduce((a, e) => ({ ...a, [e.state]: (a[e.state] || 0) + 1 }), {}),
    }),
  };
}
