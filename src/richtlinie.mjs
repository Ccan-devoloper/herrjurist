/* ==========================================================================
   Was tatsächlich gilt - und wer es ändern darf.

   Zwischen der gewünschten Konfiguration und der, unter der ein Lauf wirklich
   arbeitet, liegen Umgebungsvariablen, Ausnahmedateien und Eingaben aus dem
   Workflow. Bisher konnte ein geplanter Lauf so seinen eigenen Deckel
   anheben: `budget-ausnahmen.json` trug ein Datum, und am 18.09. lief der
   Bot mit 0,80 $ statt 0,32 $ - ohne dass jemand an diesem Tag etwas
   entschieden hätte. Eine Ausnahme, die ein automatischer Lauf selbst zieht,
   ist kein Break Glass, sondern ein zweiter Deckel.

   Deshalb zwei Trennungen:

     gewuenscht → effektiv   Erst nach Defaults, Umgebung, Ausnahmen und
                             Break-Glass-Eingaben steht fest, was gilt.

     schedule vs. manuell    Ein Lauf aus dem Zeitplan bekommt NIE mehr als
                             den Regeldeckel. Eine Anhebung ist eine
                             manuelle Handlung mit Begründung.

   Und ein Gate davor: Stimmt an der effektiven Konfiguration etwas nicht,
   startet der Lauf nicht - bevor der erste bezahlte Aufruf läuft, nicht
   danach.
   ========================================================================== */

export const REGEL_DECKEL = Object.freeze({ core: 0.32, engagement: 0.25, research: 0.12 });

/**
 * Der Abstand zwischen dem Policy-Deckel und der Grenze, bis zu der Aufrufe
 * überhaupt zugelassen werden.
 *
 * Er ist da, weil die Vorabrechnung nicht exakt sein KANN: Anthropic injiziert
 * bei Structured Outputs einen zusätzlichen, berechneten Systemprompt, und der
 * Zählendpunkt ist laut Anbieter eine Schätzung ohne zugesicherte
 * Maximalabweichung (Belege in eingabe.mjs). Was nicht exakt vorhersagbar ist,
 * bekommt Abstand statt einer Behauptung.
 *
 * Das ist eine konservative BETRIEBSGRENZE, kein Beweis. Sie macht ein
 * Überschreiten unwahrscheinlich, nicht unmöglich; unmöglich würde erst ein
 * anbieterseitiger KOSTEN-HARDCAP je Anfrage machen - ein Dollarbetrag, ab
 * dem der Anbieter die Anfrage selbst abbricht. Den gibt es nicht.
 *
 * Ausdrücklich nicht gemeint ist `max_tokens` / `max_output_tokens`: Das
 * begrenzt die Ausgabe-TOKEN und tut das auch zuverlässig - nur eben in
 * Token, nicht in Dollar, und nur auf der Ausgabeseite. „Ausgabedeckel"
 * stand hier für beides und trug damit zwei Bedeutungen.
 *
 * Über IG_PROVIDER_GUARD_USD lässt sich der Abstand VERGRÖSSERN, damit er an
 * gemessenen Abweichungen wachsen kann, statt geraten zu bleiben. Verkleinern
 * lässt er sich damit nicht (siehe POLICY_PROVIDER_GUARD_USD).
 */
export const PROVIDER_GUARD_USD = 0.02;

/**
 * Der normative Mindestabstand - für JEDEN Produktionslauf, auch den von Hand
 * gestarteten.
 *
 * RC5 hat hier eine Ausnahme für `workflow_dispatch` gelassen und sie „wie
 * Break Glass" genannt. Das war aus zwei Gründen falsch:
 *
 *   Erstens war sie gar nicht verdrahtet. Es gibt keinen Workflow-Input für
 *   den Guard und keine Übergabe von IG_PROVIDER_GUARD_USD an den Tageslauf.
 *   Die Ausnahme beschrieb einen Weg, den es nicht gibt.
 *
 *   Zweitens wäre sie kein Break Glass gewesen. Break Glass verlangt einen
 *   ausdrücklichen Betrag UND eine Begründung, beides als Workflow-Eingabe,
 *   beides im Lauf protokolliert. Für die Guard-Absenkung hätte allein
 *   `workflow_dispatch` genügt - ein Häkchen ohne Aussage. Und dieser Satz
 *   stand direkt neben der Ausnahme: „Eine Absenkung gehört versioniert in
 *   diese Zeile, nicht in eine Umgebung."
 *
 * Also eine Policy statt zweier: Nach oben ist offen, ein größerer Abstand
 * ist konservativer und jederzeit erlaubt. Nach unten führt genau ein Weg -
 * diese Zeile zu ändern, versioniert und im Diff sichtbar.
 *
 * Break Glass bleibt zuständig für die bewusste Anhebung des Core-Deckels.
 * Es hebt den Deckel; den Abstand darunter lässt es unberührt.
 */
export const POLICY_PROVIDER_GUARD_USD = 0.02;

/**
 * Liest den Guard aus der Umgebung - und unterscheidet dabei „nicht gesetzt"
 * von „falsch gesetzt".
 *
 * Variante A, ausdrücklich gewählt: Ein GESETZTER, aber unbrauchbarer Wert
 * ist ein Konfigurationsfehler und wird abgelehnt, nicht still durch den
 * Standard ersetzt. Ein stiller Fallback auf einen Tippfehler ist genau die
 * Fehlerklasse, die dieses Projekt den ganzen Abend ausgebaut hat: Er sieht
 * aus wie Sicherheit und ist eine verschluckte Meldung. Wer den Abstand
 * ändern will, soll merken, ob es geklappt hat.
 *
 * Nicht gesetzt ist dagegen kein Fehler - dann gilt der Standard.
 *
 * @returns {{usd:number, quelle:"standard"|"umgebung"|"ungueltig", gueltig:boolean, roh:string|null}}
 */
export function providerGuardLesen(roh = process.env.IG_PROVIDER_GUARD_USD) {
  const text = roh === undefined || roh === null ? "" : String(roh).trim();
  if (text === "") return { usd: PROVIDER_GUARD_USD, quelle: "standard", gueltig: true, roh: null };
  const n = Number(text);
  if (!Number.isFinite(n) || n < 0) {
    /* Der Rückfallwert ist trotzdem der sichere - falls jemand das Ergebnis
       benutzt, ohne das Gate zu fragen. Das Gate fragt. */
    return { usd: PROVIDER_GUARD_USD, quelle: "ungueltig", gueltig: false, roh: text };
  }
  return { usd: n, quelle: "umgebung", gueltig: true, roh: text };
}

/** Nur der Betrag - für Aufrufer, die die Herkunft nicht brauchen. */
export function providerGuard(roh = process.env.IG_PROVIDER_GUARD_USD) {
  return providerGuardLesen(roh).usd;
}

export class RichtlinieVerletzt extends Error {
  constructor(befunde) {
    super(`Effektive Konfiguration unzulässig:\n${befunde.map((b) => `  - ${b}`).join("\n")}`);
    this.name = "RichtlinieVerletzt";
    this.befunde = befunde;
  }
}

/**
 * Leitet die effektive Konfiguration eines Laufs ab.
 *
 * @param {object} o
 * @param {string} o.ausloeser   "schedule" | "workflow_dispatch" | "lokal"
 * @param {object} o.deckel      gewünschte Regeldeckel (aus CONFIG)
 * @param {object} o.ausnahmen   Inhalt von budget-ausnahmen.json
 * @param {string} o.datum       ISO-Tag
 * @param {object} o.breakGlass  {aktiv, betragUsd, grund} aus der Workflow-Eingabe
 * @param {boolean} o.researchGetrennt  ob der eigene Research-Topf aktiv ist
 */
export function effektiveKonfiguration({
  ausloeser, deckel = REGEL_DECKEL, ausnahmen = {}, datum,
  breakGlass = null, researchGetrennt = true,
}) {
  const hinweise = [];
  const effektiv = { core: Number(deckel.core), engagement: Number(deckel.engagement), research: Number(deckel.research) };

  /* Historische Datums-Ausnahmen bleiben als Beleg stehen - sie erklären, was
     an einem vergangenen Tag passiert ist. Wirkung auf einen geplanten Lauf
     haben sie nicht mehr. Insbesondere der Eintrag für den 23.09. (0,45 $)
     stammt aus der Zeit, als die Recherche aus dem Core-Topf bezahlt wurde;
     mit eigenem Research-Topf ist er gegenstandslos. */
  const ausnahme = Number(ausnahmen?.[datum]);
  if (ausnahme > 0) {
    hinweise.push(researchGetrennt
      ? `Datums-Ausnahme ${datum}: ${ausnahme.toFixed(2)} $ steht in der Historie, wirkt aber nicht mehr - Research hat einen eigenen Topf.`
      : `Datums-Ausnahme ${datum}: ${ausnahme.toFixed(2)} $ ignoriert - Ausnahmen heben den Core-Deckel nicht mehr an.`);
  }

  /* Break Glass: nur manuell, nur mit Begründung, nur für Core. */
  const bg = { aktiv: false, betragUsd: 0, grund: null, ausloeser };
  if (breakGlass?.aktiv) {
    if (ausloeser === "schedule") {
      hinweise.push("Break Glass aus einem geplanten Lauf verlangt - abgelehnt. Eine Anhebung ist eine manuelle Handlung.");
    } else if (!String(breakGlass.grund || "").trim()) {
      hinweise.push("Break Glass ohne Begründung verlangt - abgelehnt.");
    } else if (!(Number(breakGlass.betragUsd) > effektiv.core)) {
      hinweise.push(`Break Glass ohne sinnvollen Betrag (${breakGlass.betragUsd}) - abgelehnt.`);
    } else {
      bg.aktiv = true;
      bg.betragUsd = Number(breakGlass.betragUsd);
      bg.grund = String(breakGlass.grund).trim();
      effektiv.core = bg.betragUsd;
      hinweise.push(`Break Glass: Core heute ${bg.betragUsd.toFixed(2)} $ statt ${Number(deckel.core).toFixed(2)} $ - „${bg.grund}“.`);
    }
  }

  /* Policy-Deckel und Betriebsgrenze sind zwei Zahlen, nicht eine. Zugelassen
     wird bis zur Betriebsgrenze; der Policy-Deckel ist die Zusage. */
  const guardStand = providerGuardLesen();
  const guard = guardStand.usd;
  const betrieb = Object.fromEntries(Object.entries(effektiv)
    .map(([t, v]) => [t, Math.round(Math.max(0, v - guard) * 1e6) / 1e6]));
  if (!guardStand.gueltig) {
    hinweise.push(`IG_PROVIDER_GUARD_USD=„${guardStand.roh}" ist kein gültiger Betrag - der Lauf startet nicht. `
      + `Ein gesetzter, unbrauchbarer Wert wird nicht still durch den Standard ersetzt.`);
  } else if (guard > 0) {
    hinweise.push(`Provider-Guard ${guard.toFixed(4)} $ je Topf (${guardStand.quelle}): zugelassen wird bis Core ${betrieb.core.toFixed(4)} $, `
      + `Policy cap ist ${effektiv.core.toFixed(2)} $.`);
  }

  return {
    deckel: effektiv, betriebsDeckel: betrieb,
    providerGuardUsd: guard, providerGuard: guardStand,
    breakGlass: bg, ausloeser, hinweise, regel: { ...deckel },
  };
}

/**
 * Das Gate vor dem ersten bezahlten Aufruf. Es prüft, was ein geplanter Lauf
 * mitbringen MUSS - und lässt ihn sonst gar nicht erst anfangen.
 *
 * @param {object} o.konfiguration  Ergebnis von effektiveKonfiguration()
 * @param {object} o.produkt        {reelZusaetzlich, feedBeitraege}
 * @param {object} o.erwartet       Sollwerte des Kanals
 * @param {object} o.ceilings       {profil: maxTokens}
 * @param {object} o.ceilingPolicy  erlaubte Spanne je Profil
 * @param {number} o.researchSuchen globales Suchlimit
 */
export function richtlinieGate({
  konfiguration, produkt = {}, erwartet = {}, ceilings = {}, ceilingPolicy = {},
  researchSuchen = 2, zwecke = [], zweckTopf = {},
}) {
  const befunde = [];
  const { deckel, breakGlass, ausloeser, regel } = konfiguration;
  const geplant = ausloeser === "schedule";

  /* Geprüft wird gegen REGEL_DECKEL - die normative Konstante in diesem
     Modul -, NICHT gegen `konfiguration.regel`.

     Der Unterschied ist der ganze Sinn des Gates: `konfiguration.regel` ist
     eine Kopie dessen, was CONFIG mitgebracht hat. Verstellt jemand dort
     versehentlich core auf 0,40 $, wandern effektiver Deckel UND „Regel“
     gemeinsam auf 0,40 - und ein Vergleich der beiden fällt zufrieden aus.
     Ein Gate, das seinen Maßstab vom Geprüften bezieht, prüft nichts.

     Break Glass bleibt die einzige Ausnahme für Core, und die gibt es nur
     manuell. Engagement und Research kennen gar keine. */
  const norm = REGEL_DECKEL;
  for (const topf of ["core", "engagement", "research"]) {
    if (Number(regel[topf]) !== norm[topf]) {
      befunde.push(`Regeldeckel ${topf} = ${regel[topf]} weicht von der Richtlinie ${norm[topf]} ab `
        + `(CONFIG darf die Policy nicht verschieben)`);
    }
  }
  if (Number(deckel.engagement) !== norm.engagement) befunde.push(`Engagement-Deckel ${deckel.engagement} statt ${norm.engagement}`);
  if (Number(deckel.research) !== norm.research) befunde.push(`Research-Deckel ${deckel.research} statt ${norm.research}`);
  if (breakGlass.aktiv) {
    if (geplant) befunde.push("Break Glass in einem geplanten Lauf aktiv");
    else if (Number(deckel.core) !== Number(breakGlass.betragUsd)) {
      befunde.push(`Core-Deckel ${deckel.core} passt nicht zum Break-Glass-Betrag ${breakGlass.betragUsd}`);
    }
  } else if (Number(deckel.core) !== norm.core) {
    befunde.push(`Core-Deckel ${deckel.core} statt ${norm.core} ohne Break Glass`);
  }

  /* Produktmenge: Sie ist das Versprechen an die Leser und keine Stellschraube
     für Kostenprobleme. */
  for (const [feld, soll] of Object.entries(erwartet)) {
    if (produkt[feld] !== soll) befunde.push(`Produktmenge ${feld}: ${produkt[feld]} statt ${soll}`);
  }

  /* Der Provider-Guard ist Teil der Policy, nicht der Umgebung - und zwar in
     JEDEM Produktionslauf. Ein zu kleiner Abstand startet nicht, egal wer den
     Lauf ausgelöst hat. */
  const guard = Number(konfiguration.providerGuardUsd);
  const guardStand = konfiguration.providerGuard || null;
  if (guardStand && guardStand.gueltig === false) {
    /* Variante A: gesetzt und unbrauchbar ist ein Konfigurationsfehler - in
       jedem Lauf, nicht nur im geplanten. */
    befunde.push(`IG_PROVIDER_GUARD_USD=„${guardStand.roh}" ist kein gültiger Betrag`);
  } else if (!Number.isFinite(guard) || guard < 0) {
    befunde.push(`Provider-Guard ${konfiguration.providerGuardUsd} ist kein gültiger Betrag`);
  } else if (guard < POLICY_PROVIDER_GUARD_USD) {
    befunde.push(`Provider-Guard ${guard.toFixed(4)} $ unter dem Policy-Mindestwert ${POLICY_PROVIDER_GUARD_USD.toFixed(4)} $ `
      + `- eine Absenkung ist eine versionierte Policy-Änderung, keine Umgebungsvariable. `
      + `Break Glass hebt den Core-Deckel, nicht den Abstand darunter.`);
  }

  if (researchSuchen > 2) befunde.push(`Research-Suchlimit ${researchSuchen} über dem erlaubten Höchstwert 2`);

  for (const [profil, wert] of Object.entries(ceilings)) {
    const spanne = ceilingPolicy[profil];
    if (!spanne) { befunde.push(`Ceiling für „${profil}“ ohne Richtlinie`); continue; }
    if (wert < spanne.min || wert > spanne.max) befunde.push(`Ceiling ${profil} = ${wert} außerhalb ${spanne.min}–${spanne.max}`);
  }

  for (const z of zwecke) if (!zweckTopf[z]) befunde.push(`Zweck „${z}“ ohne Budgettopf`);

  if (befunde.length) throw new RichtlinieVerletzt(befunde);
  return { ok: true, deckel, breakGlass };
}
