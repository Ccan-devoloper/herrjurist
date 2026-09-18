/* ==========================================================================
   Drei Töpfe, harte Zuordnung, Admission vor jedem bezahlten Aufruf.

   Warum das nötig wurde: Der alte Deckel prüfte einmal vor dem ersten Call
   und danach nicht mehr. Ein Schema-Fehler, ein Retry, eine Zweitmeinung -
   jeder dieser Wege löste einen zweiten bezahlten Aufruf aus, von dem der
   Deckel nichts wusste. Am 18.09. kostete Herr Jurist 0,742 $ bei einem
   Tagesziel von 0,32 $, und niemand konnte vorher sagen, wann er reißen
   würde. Ein Deckel, der erst nach dem Aufruf merkt, dass er überschritten
   ist, ist kein Deckel.

   Vier Regeln tragen dieses Modul:

   1. Jeder bezahlte Aufruf gehört zu genau einem Topf. Die Zuordnung steht
      hier und nirgends sonst. Ein unbekannter Zweck wird abgelehnt - nicht
      still nach Core gebucht.

   2. Vor jedem Aufruf wird sein WORST CASE reserviert, nicht sein erhoffter
      Preis. Passt der Worst Case nicht mehr, startet der Aufruf nicht.

   3. Was der Anbieter berechnet haben KÖNNTE, wird nicht wieder freigegeben.
      Ein Fehler nach dem Senden ist kein „hat nicht stattgefunden“: Tokens
      sind verbraucht, auch wenn die Antwort im Parser zerbricht. Nur ein
      Fehler VOR dem Senden gibt die Reservierung zurück.

   4. Kein Topf leiht dem anderen. Was Engagement nicht braucht, hilft Core
      nicht, und umgekehrt. Kein Übertrag in den Folgetag.
   ========================================================================== */

import { BudgetStopp } from "./budgetstopp.mjs";

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

/**
 * Töpfe mit harter Vorab-Zusage. Für sie gilt: tatsächliche Kosten <=
 * reservierte Kosten. Research steht bewusst NICHT darin - dort erzeugen
 * serverseitige Suchen Eingabe-Token, deren Dollarwert vor dem Start nicht
 * exakt bekannt ist. Diese Grenze ist eine Zusage über die Zahl der Aufrufe
 * und Suchen, nicht über den Cent - und das wird hier nicht anders behauptet.
 */
const HARTE_TOEPFE = new Set(["core", "engagement"]);

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

/** Abgelehnte Admission: Der Aufruf hat nie stattgefunden. */
export class AdmissionAbgelehnt extends BudgetStopp {
  constructor(zweck, topf, verlangt, frei, deckel, grund = null) {
    super(`${zweck}: ${verlangt.toFixed(4)} $ im Topf „${topf}“ nicht mehr zulässig `
      + `(frei ${frei.toFixed(4)} $ von ${deckel.toFixed(4)} $) - der Aufruf startet nicht.`
      + (grund ? ` ${grund}` : ""));
    this.name = "AdmissionAbgelehnt";
    this.zweck = zweck; this.topf = topf; this.verlangt = verlangt; this.frei = frei; this.deckel = deckel;
    this.grund = grund;
  }
}

/**
 * Ein Aufruf hat mehr gekostet als zugesagt. Das Geld ist ausgegeben und
 * nicht zurückzuholen - aber der Topf hat seine Zusage verloren und wird
 * gesperrt, damit kein weiterer Aufruf den Schaden vergrößert.
 */
export class InvarianteVerletzt extends Error {
  constructor(zweck, topf, reserviert, tatsaechlich) {
    super(`${zweck}: tatsächlich ${tatsaechlich.toFixed(4)} $ gegen zugesagte ${reserviert.toFixed(4)} $ `
      + `im Topf „${topf}“. Der Betrag ist verbucht; der Topf ist für weitere Aufrufe gesperrt.`);
    this.name = "InvarianteVerletzt";
    this.zweck = zweck; this.topf = topf; this.reserviert = reserviert; this.tatsaechlich = tatsaechlich;
  }
}

/** Es ist mehr für Pflichtinhalte zurückgelegt, als der Topf noch hergibt. */
export class PflichtUeberreserviert extends BudgetStopp {
  constructor(topf, verlangt, frei) {
    super(`Pflichtrücklagen im Topf „${topf}“ verlangen ${verlangt.toFixed(4)} $, frei sind ${frei.toFixed(4)} $. `
      + `Das Pflichtprodukt ist so nicht vollständig finanzierbar - die Entscheidung gehört nach oben, nicht in eine stille Kürzung.`);
    this.name = "PflichtUeberreserviert";
    this.topf = topf; this.verlangt = verlangt; this.frei = frei;
  }
}

/** Der Topf ist nach einer Invariantenverletzung gesperrt. */
export class TopfGesperrt extends BudgetStopp {
  constructor(topf, grund) {
    super(`Topf „${topf}“ ist gesperrt: ${grund}`);
    this.name = "TopfGesperrt";
    this.topf = topf;
  }
}

/** Der Topf eines Zwecks. Wirft, wenn es keinen gibt (fail closed). */
export function topfFuer(zweck) {
  const topf = ZWECK_TOPF[zweck];
  if (!topf) throw new UnbekannterZweck(zweck);
  return topf;
}

const runden = (x) => Math.round(x * 1e6) / 1e6;

/* Lebenslauf eines Aufrufs. Der Unterschied zwischen „nicht gesendet“ und
   „gesendet“ ist der ganze Punkt: Nur im ersten Fall darf Geld zurück. */
export const ZUSTAND = Object.freeze({
  RESERVIERT: "reserviert",   // zugelassen, noch nichts gesendet
  GESENDET: "gesendet",       // der Anbieter hat die Anfrage
  ABGERECHNET: "abgerechnet", // tatsächliche Kosten bekannt und gebucht
  UNGEKLAERT: "ungeklaert",   // gesendet, Kosten unbekannt - Reserve bleibt verbraucht
  VERFALLEN: "verfallen",     // nie gesendet, Reserve zurückgegeben
});

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
  const gesperrt = Object.fromEntries(TOEPFE.map((t) => [t, null]));
  const verletzungen = [];
  const ungeklaert = [];
  /* Rücklagen für Pflichtinhalte, je Name ein Betrag. */
  const pflicht = new Map();
  /* Solange bezahlte Pflichtarbeit aussteht, ist das sichere Budget für
     bezahlte KÜREN null.

     Warum so grob und nicht fein über Rücklagen: Eine Rücklage müsste den
     harten Worst Case der ausstehenden Pflichtaufrufe zurücklegen, und der
     liegt über dem ganzen Topf (siehe tagesplanWorstCase). Eine KLEINERE
     Rücklage - etwa der gemessene Durchschnitt - sähe ordentlich aus und wäre
     eine erfundene Zahl: Sie würde eine Verfügbarkeit zusagen, die niemand
     nachrechnen kann. Lieber eine harte, ehrliche Regel, die manchmal ein
     schönes Bild kostet, als eine weiche, die manchmal einen Pflichtbeitrag
     kostet. Kostenlose Ausweichwege (Archivbild, Icon, reines Layout) laufen
     ohnehin nicht über diesen Weg und bleiben erlaubt. */
  let optionalSperre = null;

  const pflichtSumme = (topf, ohne = null) => {
    let s = 0;
    for (const [name, r] of pflicht) if (r.topf === topf && name !== ohne) s += r.usd;
    return runden(s);
  };

  /**
   * Was steht diesem Aufruf zur Verfügung?
   *
   * Semantik der Pflichtrücklagen, ausdrücklich:
   *   - JEDER Aufruf respektiert ALLE Pflichtrücklagen …
   *   - … außer seiner eigenen, die er unter ihrem Namen anmeldet.
   * Damit kann weder ein optionales Bild noch ein anderer Pflichtaufruf das
   * Geld verbrauchen, das für ein noch ausstehendes Pflichtstück zurückliegt.
   */
  const frei = (topf, { ohnePflicht = null } = {}) =>
    runden(deckel[topf] - verbraucht[topf] - reserviert[topf] - pflichtSumme(topf, ohnePflicht));

  const sperren = (topf, grund) => { if (!gesperrt[topf]) gesperrt[topf] = grund; };

  /**
   * Lässt einen bezahlten Aufruf zu - oder eben nicht.
   *
   * `worstCase` ist der teuerste Ausgang dieses Aufrufs, nicht sein
   * erwarteter Preis. Nur so kann ein voll ausgeschöpfter Aufruf den Topf
   * nicht über den Deckel treiben.
   *
   * `opt.pflichtName` meldet den Aufruf als Einlösung genau dieser Rücklage.
   * `opt.optional` ist Kennzeichnung für die Telemetrie; optionale Aufrufe
   * melden keine Rücklage an und stehen damit hinter allen Pflichtstücken.
   */
  const zulassen = (zweck, worstCase, opt = {}) => {
    const topf = topfFuer(zweck);
    if (gesperrt[topf]) throw new TopfGesperrt(topf, gesperrt[topf]);
    const verlangt = runden(Math.max(0, Number(worstCase) || 0));
    const eigene = opt.optional ? null : (opt.pflichtName || null);
    const verfuegbar = frei(topf, { ohnePflicht: eigene });
    if (opt.optional && optionalSperre) {
      protokoll({ art: "admission", ergebnis: "abgelehnt", zweck, topf, reservedUsd: verlangt, frei: verfuegbar, optional: true, breakGlass });
      throw new AdmissionAbgelehnt(zweck, topf, verlangt, verfuegbar, deckel[topf], optionalSperre);
    }
    if (verlangt > verfuegbar) {
      protokoll({ art: "admission", ergebnis: "abgelehnt", zweck, topf, reservedUsd: verlangt, frei: verfuegbar, optional: !!opt.optional, breakGlass });
      throw new AdmissionAbgelehnt(zweck, topf, verlangt, verfuegbar, deckel[topf]);
    }
    reserviert[topf] = runden(reserviert[topf] + verlangt);
    protokoll({ art: "admission", ergebnis: "zugelassen", zweck, topf, reservedUsd: verlangt, frei: verfuegbar, optional: !!opt.optional, breakGlass });

    let zustand = ZUSTAND.RESERVIERT;
    let gemeldeteKosten = null;
    const reserveAufloesen = () => { reserviert[topf] = runden(Math.max(0, reserviert[topf] - verlangt)); };

    const griff = {
      zweck, topf, reservedUsd: verlangt, breakGlass, optional: !!opt.optional,
      get zustand() { return zustand; },
      istGesendet: () => zustand !== ZUSTAND.RESERVIERT,

      /** Unmittelbar vor dem Absenden aufrufen. Ab hier gibt es kein Geld zurück. */
      gesendet() {
        if (zustand === ZUSTAND.RESERVIERT) zustand = ZUSTAND.GESENDET;
        return griff;
      },

      /** Usage melden, sobald sie bekannt ist - auch wenn danach noch etwas schiefgeht. */
      kosten(usd) {
        gemeldeteKosten = runden(Math.max(0, Number(usd) || 0));
        return griff;
      },

      /** Der Aufruf ist abgerechnet. */
      buchen(usd) {
        if (zustand === ZUSTAND.ABGERECHNET || zustand === ZUSTAND.UNGEKLAERT || zustand === ZUSTAND.VERFALLEN) {
          throw new Error(`Admission für „${zweck}“ ist bereits abgeschlossen (${zustand}).`);
        }
        const tatsaechlich = runden(Math.max(0, Number(usd ?? gemeldeteKosten) || 0));
        zustand = ZUSTAND.ABGERECHNET;
        reserveAufloesen();
        verbraucht[topf] = runden(verbraucht[topf] + tatsaechlich);
        const zuviel = runden(tatsaechlich - verlangt);
        protokoll({
          art: "buchung", zweck, topf, reservedUsd: verlangt, actualUsd: tatsaechlich,
          releasedUsd: Math.max(0, runden(verlangt - tatsaechlich)), sent: true, breakGlass,
          invariantViolation: zuviel > 0 || undefined,
        });
        /* Mehr ausgegeben als zugesagt: Das Geld ist weg, aber der Topf hat
           seine Zusage verloren. Kein weiterer Aufruf darf den Schaden
           vergrößern. Für Research gilt die weichere Zusage - dort wird keine
           Cent-Garantie behauptet, also auch keine gebrochen. */
        if (zuviel > 0 && HARTE_TOEPFE.has(topf)) {
          const fehler = new InvarianteVerletzt(zweck, topf, verlangt, tatsaechlich);
          verletzungen.push({ zweck, topf, reservedUsd: verlangt, actualUsd: tatsaechlich });
          sperren(topf, fehler.message);
          console.error(`  ‼ ${fehler.message}`);
          throw fehler;
        }
        return tatsaechlich;
      },

      /**
       * Der Aufruf hat NICHT stattgefunden. Nur vor dem Senden erlaubt;
       * danach ist es eine ungeklärte Ausgabe, kein Rückgeld.
       */
      freigeben() {
        if (zustand === ZUSTAND.ABGERECHNET || zustand === ZUSTAND.UNGEKLAERT || zustand === ZUSTAND.VERFALLEN) return 0;
        if (zustand === ZUSTAND.GESENDET) return griff.ungeklaert("freigeben() nach dem Senden");
        zustand = ZUSTAND.VERFALLEN;
        reserveAufloesen();
        protokoll({ art: "freigabe", zweck, topf, reservedUsd: verlangt, releasedUsd: verlangt, sent: false, breakGlass });
        return verlangt;
      },

      /**
       * Gesendet, Kosten unbekannt. Die Reservierung gilt als verbraucht -
       * konservativ und für den Rest des Tages. Lieber zu früh aufhören als
       * ein zweites Mal dasselbe Geld ausgeben.
       */
      ungeklaert(grund = "Kosten nach dem Senden unbekannt") {
        if (zustand === ZUSTAND.ABGERECHNET || zustand === ZUSTAND.UNGEKLAERT || zustand === ZUSTAND.VERFALLEN) return 0;
        if (gemeldeteKosten != null) return griff.buchen(gemeldeteKosten);
        zustand = ZUSTAND.UNGEKLAERT;
        reserveAufloesen();
        verbraucht[topf] = runden(verbraucht[topf] + verlangt);
        ungeklaert.push({ zweck, topf, reservedUsd: verlangt, grund });
        protokoll({ art: "ungeklaert", zweck, topf, reservedUsd: verlangt, spendUnknown: true, sent: true, releasedUsd: 0, errorType: grund, breakGlass });
        console.warn(`  ! ${zweck}: gesendet, Kosten unbekannt (${grund}) - ${verlangt.toFixed(4)} $ gelten als verbraucht.`);
        return verlangt;
      },
    };
    return griff;
  };

  /**
   * Bequemer Weg: zulassen, aufrufen, abrechnen.
   *
   * `arbeit` bekommt den Griff und MUSS `griff.gesendet()` aufrufen, bevor
   * sie den Anbieter anspricht, und `griff.kosten(usd)`, sobald die Usage
   * bekannt ist. Danach entscheidet der Zustand, was mit der Reservierung
   * passiert - nicht die Frage, ob eine Ausnahme geflogen ist.
   */
  const mitAdmission = async (zweck, worstCase, arbeit, opt = {}) => {
    const griff = zulassen(zweck, worstCase, opt);
    try {
      const ergebnis = await arbeit(griff);
      const usd = ergebnis && typeof ergebnis === "object" && "usd" in ergebnis ? ergebnis.usd : undefined;
      if (griff.zustand === ZUSTAND.RESERVIERT && usd === undefined) griff.freigeben();
      else if (griff.zustand !== ZUSTAND.ABGERECHNET) griff.buchen(usd);
      return ergebnis && typeof ergebnis === "object" && "ergebnis" in ergebnis ? ergebnis.ergebnis : ergebnis;
    } catch (e) {
      if (e instanceof InvarianteVerletzt) throw e;
      if (!griff.istGesendet()) griff.freigeben();
      else griff.ungeklaert(e?.name || e?.message || "Fehler nach dem Senden");
      throw e;
    }
  };

  /**
   * Legt Geld für einen Pflichtinhalt zurück. Eine Rücklage, die der Topf
   * nicht mehr hergibt, wird nicht still angenommen: Dass das Pflichtprodukt
   * nicht mehr vollständig finanzierbar ist, ist eine Nachricht, keine
   * Rundungsfrage.
   */
  const pflichtRuecklage = (name, zweck, usd) => {
    const topf = topfFuer(zweck);
    const betrag = runden(Math.max(0, Number(usd) || 0));
    if (betrag <= 0) { pflicht.delete(name); return 0; }
    const platz = runden(deckel[topf] - verbraucht[topf] - reserviert[topf] - pflichtSumme(topf, name));
    if (betrag > platz) {
      pflicht.delete(name);
      throw new PflichtUeberreserviert(topf, betrag, platz);
    }
    pflicht.set(name, { topf, usd: betrag, zweck });
    return betrag;
  };
  const pflichtAufloesen = (name) => pflicht.delete(name);

  /**
   * Sperrt bezahlte optionale Aufrufe, solange bezahlte Pflichtarbeit
   * aussteht. `grund` steht danach in der Ablehnung und im Protokoll.
   */
  const optionalSperren = (grund) => { optionalSperre = grund || "Bezahlte Pflichtarbeit steht noch aus."; return optionalSperre; };
  const optionalFreigeben = () => { optionalSperre = null; };
  const optionalGesperrt = () => optionalSperre;

  return {
    zulassen, mitAdmission, pflichtRuecklage, pflichtAufloesen, frei, breakGlass,
    optionalSperren, optionalFreigeben, optionalGesperrt,
    gesperrt: (topf) => gesperrt[topf] || null,
    stand: () => ({
      deckel: { ...deckel },
      verbraucht: { ...verbraucht },
      reserviert: { ...reserviert },
      pflicht: Object.fromEntries([...pflicht].map(([n, r]) => [n, { ...r }])),
      gesperrt: { ...gesperrt },
      optionalSperre,
      verletzungen: [...verletzungen],
      ungeklaert: [...ungeklaert],
      breakGlass,
    }),
  };
}
