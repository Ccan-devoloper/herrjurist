/* ==========================================================================
   Hooks für Reels: die ersten zwei Sekunden.

   Instagram entscheidet über die Verteilung eines Reels vor allem danach, wie
   viele Zuschauer über die Drei-Sekunden-Marke hinaus dabeibleiben. Wer dort
   abspringt, kostet Reichweite; ein Reel mit starkem Halt wird um ein
   Vielfaches weiter ausgespielt. Deshalb hat jedes Reel hier einen Hook nach
   festem Muster – und der Bildschirmtext trägt ihn allein, weil viele ohne Ton
   schauen.

   Die Muster stammen aus der Praxis kurzer Videos – Neugier und Wissenslücke,
   Alltagsbezug, Problem und Abhilfe, Widerspruch, direkte Frage, steile
   Behauptung, Preisschild, Szene – und sind hier auf das Steuerberaterexamen
   übersetzt. Welches Muster ein Tag bekommt, entscheidet die Rotation; was
   messbar besser lief, wird bevorzugt (insights.mjs liefert hookGewicht).

   Gesprochen wird der Hook anders als der Rest: langsamer, etwas lauter, mit
   einer Pause danach (stimme.mjs, reel.mjs).
   ========================================================================== */

/**
 * Die Muster. `regel` geht wörtlich in den Auftrag an das Modell,
 * `beispiele` zeigen den Ton an fachlichen Themen.
 */
export const HOOKS = {
  fehler: {
    name: "Fehler-Hook",
    regel: "Benenne den Fehler, den fast alle machen, bevor du die Lösung zeigst. Kein Vorwurf, sondern Wiedererkennung.",
    beispiele: [
      { titel: "Der teuerste Denkfehler", sprecher: "Fast alle prüfen hier die Frist zuerst. Genau das kostet die Punkte." },
      { titel: "Falsches Amt, Frist weg?", sprecher: "Der Einspruch landet beim falschen Finanzamt – und viele schreiben sofort: unzulässig." },
    ],
  },
  frage: {
    name: "Direkte Frage",
    regel: "Stelle eine Frage, die man im Examen beantworten können muss und bei der man kurz zögert. Die Antwort kommt erst später im Reel.",
    beispiele: [
      { titel: "Wer schuldet die Steuer?", sprecher: "Die Rechnung weist Umsatzsteuer aus, die Leistung gab es nie. Wer schuldet sie?" },
      { titel: "Neue Tatsache oder nicht?", sprecher: "Das Finanzamt erfährt es nach dem Bescheid. Reicht das für eine Änderung?" },
    ],
  },
  luecke: {
    name: "Wissenslücke",
    regel: "Zeige, dass es eine bestimmte Stelle gibt, die alles entscheidet, ohne sie sofort zu verraten.",
    beispiele: [
      { titel: "Ein Halbsatz entscheidet", sprecher: "In Paragraf 173 steckt ein Halbsatz, der über die ganze Änderung entscheidet." },
      { titel: "Die Reihenfolge ist alles", sprecher: "Zwei Prüfungsschritte, eine Reihenfolge – und nur eine davon führt zur richtigen Lösung." },
    ],
  },
  behauptung: {
    name: "Steile Behauptung",
    regel: "Stelle eine These auf, die zunächst widerspricht, und löse sie im Reel fachlich sauber auf. Keine Übertreibung, die du nicht belegst.",
    beispiele: [
      { titel: "Fristen sind Punktegeschenke", sprecher: "Die Fristberechnung ist der einfachste Punktelieferant in Klausur 1. Ernsthaft." },
      { titel: "Auswendig lernen bringt nichts", sprecher: "Das Schema auswendig zu können reicht hier nicht. Es kommt auf die Zuordnung an." },
    ],
  },
  kosten: {
    name: "Preisschild",
    regel: "Sage konkret, was der Fehler oder das Wissen im Examen wert ist. Zahlen nur, wenn sie aus dem Themen-Skelett stammen – niemals erfundene Statistiken.",
    beispiele: [
      { titel: "Das kostet dich Punkte", sprecher: "Wer hier die falsche Bewertung ansetzt, verliert die halbe Textziffer." },
      { titel: "Drei Sätze, volle Punkte", sprecher: "Für diesen Prüfungspunkt brauchst du drei Sätze. Mehr will der Korrektor nicht." },
    ],
  },
  szene: {
    name: "Szene aus der Klausur",
    regel: "Setze die Zuschauer mitten in die Prüfungssituation, in der zweiten Person, im Präsens.",
    beispiele: [
      { titel: "Minute 90, Blatt 4", sprecher: "Du liest den Sachverhalt zum dritten Mal und weißt nicht, wo du anfangen sollst." },
      { titel: "Der Satz im Sachverhalt", sprecher: "Ein Nebensatz im Sachverhalt – und plötzlich läuft die ganze Prüfung anders." },
    ],
  },
  alltag: {
    name: "Alltag beim Lernen",
    regel: "Sprich ein Gefühl aus, das jede und jeder beim Lernen kennt, und knüpfe daran das Fachthema. Wiedererkennung vor Fachbegriff.",
    beispiele: [
      { titel: "Kennst du diesen Moment?", sprecher: "Du hast das Schema dreimal gelernt und in der Klausur ist es weg." },
      { titel: "Immer dieselbe Stelle", sprecher: "Jedes Mal, wenn die Bewertung dran ist, fängst du wieder von vorne an." },
    ],
  },
  widerspruch: {
    name: "Widerspruch",
    regel: "Stelle eine verbreitete Annahme in Frage, die tatsächlich falsch ist, und löse sie fachlich auf. Nur echte Irrtümer, keine Strohmänner.",
    beispiele: [
      { titel: "Das stimmt so nicht", sprecher: "Der Einspruch hemmt die Vollziehung? Genau umgekehrt." },
      { titel: "Fast alle lernen das falsch", sprecher: "Grobes Verschulden trifft den Steuerpflichtigen? Nicht in dieser Fallgruppe." },
    ],
  },
  loesung: {
    name: "Problem und Abhilfe",
    regel: "Nenne den Schmerzpunkt und verspreche im selben Atemzug die Abhilfe, die das Reel liefert. Das Versprechen muss das Reel auch einlösen.",
    beispiele: [
      { titel: "Schluss mit Raten", sprecher: "Du weißt nie, wo die Prüfung anfängt? Dafür gibt es genau eine Reihenfolge." },
      { titel: "Nie wieder Fristchaos", sprecher: "Fristen kosten dich Zeit? Mit drei Fragen bist du in zwanzig Sekunden durch." },
    ],
  },
  kontrast: {
    name: "Vorher und nachher",
    regel: "Stelle zwei Wege gegenüber: den, den die meisten gehen, und den, der zur Lösung führt.",
    beispiele: [
      { titel: "So nicht, sondern so", sprecher: "Die meisten fangen bei der Bewertung an. Der Korrektor erwartet die Zurechnung." },
      { titel: "Zwei Zeilen Unterschied", sprecher: "Dieselbe Rechnung, zwei Sätze mehr – und aus vier Punkten werden sieben." },
    ],
  },
};

export const HOOK_TYPEN = Object.keys(HOOKS);

/* Öffner, die die ersten Sekunden verschenken. Wer so anfängt, verliert die
   Hälfte der Zuschauer, bevor der Inhalt beginnt. */
const SCHWACHE_OEFFNER = /^\s*(hallo|hi\b|hey|guten (morgen|tag|abend)|willkommen|schön,? dass|heute (geht|zeige|sprechen|schauen|lernen)|in diesem (video|reel|beitrag)|wir (schauen|sprechen|klären)|lass uns|kurz (erklärt|gesagt)[:,]?\s*$|ich (zeige|erkläre) (dir|euch) (heute|jetzt))/i;

/** Höchstlängen: Der Bildschirmtext muss ohne Ton wirken, gesprochen bleibt er ein Satz. */
export const HOOK_GRENZEN = { titelWoerter: 6, sprecherWoerter: 18 };

/**
 * Welches Muster bekommt dieser Tag? Grundlage ist eine Rotation, damit sich
 * die Hooks nicht wiederholen. Sobald die Lernschleife Gewichte liefert,
 * fallen deutlich schwächere Muster aus der Rotation heraus.
 */
export function hookWaehlen(datum, strategie = null) {
  const gewicht = strategie?.hookGewicht || {};
  const stark = HOOK_TYPEN.filter((t) => (gewicht[t] ?? 1) >= 0.75);
  const auswahl = stark.length ? stark : HOOK_TYPEN;
  const tag = Math.floor(Date.parse(`${datum}T12:00:00Z`) / 86400000);
  return auswahl[((tag % auswahl.length) + auswahl.length) % auswahl.length];
}

/** Der Abschnitt, der im Auftrag an das Modell steht. */
export function hookAnleitung(typ) {
  const h = HOOKS[typ] || HOOKS.frage;
  const beispiele = h.beispiele.map((b) => `  · Bildschirm: „${b.titel}“ – gesprochen: „${b.sprecher}“`).join("\n");
  return `## Hook (Szene 1) – Muster „${h.name}“
${h.regel}
Der Bildschirmtext trägt den Hook allein: höchstens ${HOOK_GRENZEN.titelWoerter} Wörter, groß und lesbar, denn viele schauen ohne Ton.
Gesprochen ist der Hook EIN Satz mit höchstens ${HOOK_GRENZEN.sprecherWoerter} Wörtern und steht ganz am Anfang – keine Begrüßung, keine Ankündigung, kein „In diesem Reel“.
Er nennt noch nicht die Lösung; die kommt in den folgenden Szenen.
So klingt das Muster (andere Themen):
${beispiele}`;
}

/**
 * Prüft die erste Szene: Trägt sie wirklich einen Hook?
 * @returns {string[]} Beanstandungen (leer = in Ordnung)
 */
export function pruefeHook(szene) {
  const fehler = [];
  if (!szene) return ["Erste Szene fehlt – ohne Hook kein Reel"];
  const titel = String(szene.titel || "").trim();
  const sprecher = String(szene.sprecher || "").trim();
  if (!titel) fehler.push("Hook: Der Bildschirmtext der ersten Szene fehlt");
  const titelWoerter = titel.split(/\s+/).filter(Boolean).length;
  if (titelWoerter > HOOK_GRENZEN.titelWoerter) fehler.push(`Hook: Bildschirmtext hat ${titelWoerter} Wörter (höchstens ${HOOK_GRENZEN.titelWoerter})`);
  if (SCHWACHE_OEFFNER.test(sprecher)) fehler.push(`Hook: schwacher Einstieg („${sprecher.split(/[.!?]/)[0].slice(0, 40)}…“) – die ersten Sekunden gehören dem Aufhänger, nicht der Begrüßung`);
  const ersterSatz = sprecher.split(/(?<=[.!?])\s/)[0] || "";
  const satzWoerter = ersterSatz.split(/\s+/).filter(Boolean).length;
  if (satzWoerter > HOOK_GRENZEN.sprecherWoerter) fehler.push(`Hook: gesprochener Aufhänger hat ${satzWoerter} Wörter (höchstens ${HOOK_GRENZEN.sprecherWoerter})`);
  return fehler;
}

/**
 * Ordnet einen fertigen Hook einem Muster zu – Grundlage für die Lernschleife,
 * die misst, welches Muster Follower und Reichweite bringt.
 */
export function hookTypErkennen(titel = "", sprecher = "") {
  const t = `${titel} ${sprecher}`;
  if (/stimmt so nicht|genau umgekehrt|lernen das falsch|angeblich|stimmt nicht/i.test(t)) return "widerspruch";
  if (/schluss mit|nie wieder|dafür gibt es|so gehts|so geht's/i.test(t)) return "loesung";
  if (/kennst du|jedes mal|immer dieselbe|jeder kennt|geht dir auch/i.test(t)) return "alltag";
  if (/\?/.test(titel)) return "frage";
  if (/fehler|falle|falsch|übersehen|vergessen|die meisten|fast alle/i.test(t)) return "fehler";
  if (/punkt(e|en)?|kostet|wert|note|bringt dir/i.test(t)) return "kosten";
  if (/\bdu\b|\bdir\b|minute|blatt|sitzt|liest/i.test(t)) return "szene";
  if (/statt|sondern|anstatt|vorher|nachher|zwei wege/i.test(t)) return "kontrast";
  if (/entscheidet|steckt|geheim|kaum jemand|übersieht/i.test(t)) return "luecke";
  if (/^(nie|immer|vergiss|kein|niemand|jeder)/i.test(titel.trim()) || /ernsthaft|wirklich wahr|glaub/i.test(t)) return "behauptung";
  return "aussage";
}
