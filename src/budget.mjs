/* ==========================================================================
   Drei Töpfe, harte Zuordnung, Admission vor jedem bezahlten Aufruf.

   Warum das nötig wurde: Der alte Deckel prüfte einmal vor dem ersten Call
   und danach nicht mehr. Ein Schema-Fehler, ein Retry, eine Zweitmeinung -
   jeder dieser Wege löste einen zweiten bezahlten Aufruf aus, von dem der
   Deckel nichts wusste. Am 18.09. kostete Herr Jurist 0,742 $ bei einem
   Tagesziel von 0,32 $, und niemand konnte vorher sagen, wann er reißen
   würde. Ein Deckel, der erst nach dem Aufruf merkt, dass er überschritten
   ist, ist kein Deckel.

   Drei Regeln tragen dieses Modul:

   1. Jeder bezahlte Aufruf gehört zu genau einem Topf. Die Zuordnung steht
      hier und nirgends sonst. Ein unbekannter Zweck wird abgelehnt - nicht
      still nach Core gebucht.

   2. Vor jedem Aufruf wird sein WORST CASE reserviert, nicht sein erhoffter
      Preis. Passt der Worst Case nicht mehr, startet der Aufruf nicht. Nach
      dem Aufruf wird der tatsächliche Preis gebucht und der Rest freigegeben.

   3. Kein Topf leiht dem anderen. Was Engagement nicht braucht, hilft Core
      nicht, und umgekehrt. Kein Übertrag in den Folgetag.
   ========================================================================== */

/* --- Die Töpfe ---------------------------------------------------------- */
export const TOEPFE = ["core", "engagement", "research"];

/**
 * Zweck → Topf. Die einzige Stelle, an der diese Entscheidung fällt.
 *
 * Core ist das Tagesprodukt: was geschrieben, geprüft, bebildert und gebaut
 * wird, damit die geplanten Beiträge und Stories erscheinen.
 *
 * Engagement sind Antworten an Menschen - Kommentare und Nachrichten. Sie
 * hängen nicht am Tagesprodukt und dürfen es nicht verdrängen.
 *
 * Research ist das FINDEN eines Themas: Websuche, Auswahl, Bewertung. Sobald
 * aus dem gefundenen Thema ein Instagram-Inhalt geschrieben wird, ist das
 * wieder Core - sonst wäre die Grenze beliebig verschiebbar.
 */
export const ZWECK_TOPF = Object.freeze({
  /* Core - Tagesprodukt */
  autor: "core",
  reel: "core",
  stories: "core",
  faktencheck: "core",
  "reel-faktencheck": "core",
  "story-faktencheck": "core",
  bildregie: "core",
  bild: "core",
  erklaerbild: "core",
  loesungsskizze: "core",
  loesung: "core",
  /* Engagement - Antworten an Menschen */
  kommentare: "engagement",
  nachrichten: "engagement",
  /* Research - ein Thema finden, nicht es ausformulieren */
  recherche: "research",
  "recherche-loesung": "research",
});

/** Ein Zweck ohne Topf ist ein Programmierfehler, kein Sonderfall. */
export class UnbekannterZweck extends Error {
  constructor(zweck) {
    super(`Kostenpflichtiger Zweck „${zweck}“ ist keinem Budgettopf zugeordnet. `
      + `Zulässig: ${Object.keys(ZWECK_TOPF).join(", ")}. `
      + `Ein neuer Zweck muss in ZWECK_TOPF eingetragen werden - ein stiller Default wäre ein Leck.`);
    this.name = "UnbekannterZweck";
    this.zweck = zweck;
  }
}

/** Der Topf eines Zwecks. Wirft, wenn es keinen gibt (fail closed). */
export function topfFuer(zweck) {
  const topf = ZWECK_TOPF[zweck];
  if (!topf) throw new UnbekannterZweck(zweck);
  return topf;
}

/** Abgelehnte Admission: Der Aufruf hat nie stattgefunden. */
export class AdmissionAbgelehnt extends Error {
  constructor(zweck, topf, verlangt, frei, deckel) {
    super(`${zweck}: ${verlangt.toFixed(4)} $ im Topf „${topf}“ nicht mehr zulässig `
      + `(frei ${frei.toFixed(4)} $ von ${deckel.toFixed(4)} $) - der Aufruf startet nicht.`);
    this.name = "AdmissionAbgelehnt";
    this.zweck = zweck; this.topf = topf; this.verlangt = verlangt; this.frei = frei; this.deckel = deckel;
  }
}

const runden = (x) => Math.round(x * 1e6) / 1e6;

/**
 * Baut den Budgetzustand eines Laufs.
 *
 * @param {object}   o
 * @param {object}   o.deckel     {core, engagement, research} in USD
 * @param {object}   o.bisher     schon heute verbraucht, je Topf
 * @param {boolean}  o.breakGlass ausdrücklich manuell erhöhter Lauf
 * @param {Function} o.protokoll  (eintrag) => void, für die Telemetrie
 */
export function budgetStarten({ deckel, bisher = {}, breakGlass = false, protokoll = () => {} }) {
  for (const t of TOEPFE) {
    if (!(t in deckel)) throw new Error(`Budgettopf „${t}“ hat keinen Deckel - Scheduled Production darf so nicht starten.`);
  }
  const verbraucht = Object.fromEntries(TOEPFE.map((t) => [t, Number(bisher[t] || 0)]));
  const reserviert = Object.fromEntries(TOEPFE.map((t) => [t, 0]));
  /* Rücklagen für Pflichtinhalte: Optionale Aufrufe müssen an ihnen
     vorbeikommen, Pflichtaufrufe dürfen sie verbrauchen. */
  const pflicht = new Map();

  const pflichtSumme = (topf, ohne = null) => {
    let s = 0;
    for (const [name, r] of pflicht) if (r.topf === topf && name !== ohne) s += r.usd;
    return s;
  };
  const frei = (topf, { optional = false, ohnePflicht = null } = {}) => {
    const belegt = verbraucht[topf] + reserviert[topf] + (optional ? pflichtSumme(topf, ohnePflicht) : 0);
    return runden(deckel[topf] - belegt);
  };

  /**
   * Lässt einen bezahlten Aufruf zu - oder eben nicht.
   *
   * `worstCase` ist der teuerste Ausgang dieses Aufrufs, nicht sein
   * erwarteter Preis. Nur so kann ein voll ausgeschöpfter Aufruf den Topf
   * nicht über den Deckel treiben.
   *
   * `optional` markiert Aufrufe, die die Qualität verbessern, aber nicht zum
   * Pflichtprodukt gehören - zusätzliche Erklärbilder etwa. Sie kommen nur
   * durch, wenn danach noch alle Pflichtrücklagen bezahlbar sind.
   */
  const zulassen = (zweck, worstCase, opt = {}) => {
    const topf = topfFuer(zweck);
    const verlangt = runden(Math.max(0, Number(worstCase) || 0));
    const verfuegbar = frei(topf, { optional: opt.optional, ohnePflicht: opt.pflichtName || null });
    if (verlangt > verfuegbar) {
      const fehler = new AdmissionAbgelehnt(zweck, topf, verlangt, verfuegbar, deckel[topf]);
      protokoll({ art: "admission", ergebnis: "abgelehnt", zweck, topf, verlangt, frei: verfuegbar, optional: !!opt.optional, breakGlass });
      throw fehler;
    }
    reserviert[topf] = runden(reserviert[topf] + verlangt);
    protokoll({ art: "admission", ergebnis: "zugelassen", zweck, topf, verlangt, frei: verfuegbar, optional: !!opt.optional, breakGlass });

    let abgeschlossen = false;
    return {
      zweck, topf, reserviert: verlangt, breakGlass,
      /* Der Aufruf ist gelaufen und hat `usd` gekostet. Die Differenz zur
         Reservierung geht zurück in den Topf. */
      buchen(usd) {
        if (abgeschlossen) throw new Error(`Admission für „${zweck}“ ist bereits abgeschlossen.`);
        abgeschlossen = true;
        const tatsaechlich = runden(Math.max(0, Number(usd) || 0));
        reserviert[topf] = runden(Math.max(0, reserviert[topf] - verlangt));
        verbraucht[topf] = runden(verbraucht[topf] + tatsaechlich);
        protokoll({ art: "buchung", zweck, topf, reserviert: verlangt, tatsaechlich, freigegeben: runden(verlangt - tatsaechlich), breakGlass });
        return tatsaechlich;
      },
      /* Der Aufruf hat nicht stattgefunden (Fehler vor dem Senden, Abbruch).
         Die Reservierung verfällt vollständig. */
      freigeben() {
        if (abgeschlossen) return 0;
        abgeschlossen = true;
        reserviert[topf] = runden(Math.max(0, reserviert[topf] - verlangt));
        protokoll({ art: "freigabe", zweck, topf, freigegeben: verlangt, breakGlass });
        return verlangt;
      },
    };
  };

  /** Bequemer Weg: zulassen, aufrufen, buchen - auch im Fehlerfall sauber. */
  const mitAdmission = async (zweck, worstCase, arbeit, opt = {}) => {
    const zulassung = zulassen(zweck, worstCase, opt);
    try {
      const { ergebnis, usd } = await arbeit(zulassung);
      zulassung.buchen(usd ?? 0);
      return ergebnis;
    } catch (e) {
      zulassung.freigeben();
      throw e;
    }
  };

  /**
   * Legt Geld für einen Pflichtinhalt zurück. Optionale Aufrufe kommen an
   * dieser Rücklage nicht vorbei; Pflichtaufrufe schon.
   */
  const pflichtRuecklage = (name, zweck, usd) => {
    const topf = topfFuer(zweck);
    if (usd > 0) pflicht.set(name, { topf, usd: runden(usd), zweck });
    else pflicht.delete(name);
  };
  const pflichtAufloesen = (name) => pflicht.delete(name);

  return {
    zulassen, mitAdmission, pflichtRuecklage, pflichtAufloesen,
    frei, breakGlass,
    stand: () => ({
      deckel: { ...deckel },
      verbraucht: { ...verbraucht },
      reserviert: { ...reserviert },
      pflicht: Object.fromEntries([...pflicht].map(([n, r]) => [n, { ...r }])),
      breakGlass,
    }),
  };
}
