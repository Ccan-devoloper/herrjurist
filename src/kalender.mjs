/* ==========================================================================
   Saisonkalender des juristischen Staatsexamens.

   Liefert für ein Datum die anstehenden Anlässe (Prüfungstage, Fristen,
   Countdown-Meilensteine). Der Planer ersetzt an Anlasstagen den ersten
   Beitrag durch das Format „anlass“ und gibt dem Autor den Kontext mit.
   Termine: schriftliche Prüfung bundeseinheitlich Anfang Oktober (Konfig),
   Anmeldeschluss 30. April, Ergebnisse meist Januar/Februar, mündliche
   Prüfungen Januar bis April.
   ========================================================================== */

import { CONFIG } from "./config.mjs";
import { tageBis } from "./zeit.mjs";

function iso(jahr, monat, tag) { return `${jahr}-${String(monat).padStart(2, "0")}-${String(tag).padStart(2, "0")}`; }

/* Anlässe, die ohne festen Prüfungstermin gelten: der Rhythmus des Jahres.
   Für Jura sind das die Klausurenkampagnen im Frühjahr und Herbst, der Beginn
   des Referendariats und der Semesterwechsel. */
function jahresAnlaesse(jahr) {
  const d = (m, t) => `${jahr}-${String(m).padStart(2, "0")}-${String(t).padStart(2, "0")}`;
  return [
    { datum: d(1, 8), art: "auftakt", titel: "Neues Jahr, neuer Lernplan", kontext: "Zum Jahresbeginn stellen viele ihren Examensplan auf: Stoffverteilung, Klausurenkurs, Wiederholungsrhythmus." },
    { datum: d(3, 1), art: "kampagne", titel: "Frühjahrskampagne", kontext: "In vielen Ländern beginnt jetzt die Klausurenkampagne der ersten juristischen Prüfung. Ton: ruhig, Klausurtechnik, keine neuen Themen." },
    { datum: d(5, 1), art: "referendariat", titel: "Start ins Referendariat", kontext: "Zum Mai beginnt in vielen Ländern ein neuer Referendarjahrgang – Aktenvortrag, Relationstechnik und die Umstellung vom Gutachten- auf den Urteilsstil." },
    { datum: d(8, 15), art: "kampagne", titel: "Herbstkampagne", kontext: "Die zweite Klausurenkampagne des Jahres steht an. Jetzt zählen Dauerbrenner, Klausuren unter Zeit und Nerven." },
    { datum: d(10, 1), art: "semesterstart", titel: "Semesterstart", kontext: "Das Wintersemester beginnt; Erstsemester steigen ein, Examenskandidaten gehen in die Vorbereitung." },
    { datum: d(12, 31), art: "jahreswechsel", titel: "Jahreswechsel", kontext: "Zum Jahreswechsel treten Gesetzesänderungen in Kraft; für das Examen zählt der Rechtsstand, den die Prüfung vorgibt." },
  ];
}

/* Alle Anlässe eines Jahres rund um einen Prüfungstermin. */
export function anlaesse(datum = new Date().toISOString().slice(0, 10)) {
  const jahr = Number(datum.slice(0, 4));
  /* Ohne festen Prüfungstermin (Jura: je Land und Durchgang verschieden) gibt
     es keine Countdown- und Prüfungstags-Anlässe – nur den Jahresrhythmus. */
  if (!CONFIG.examen.schriftlich) return jahresAnlaesse(jahr);
  const [pj, pm, pt] = CONFIG.examen.schriftlich.split("-").map(Number);
  const [, , et] = CONFIG.examen.ende.split("-").map(Number);
  const pruefung = { jahr: pj, tag1: iso(pj, pm, pt), tag2: iso(pj, pm, pt + 1), tag3: iso(pj, pm, et) };
  const liste = [
    { datum: iso(jahr, 4, 30), art: "frist", titel: "Anmeldeschluss zur Prüfung", kontext: "Heute endet in vielen Ländern die Meldefrist für den nächsten Durchgang. Wer sich meldet, braucht ab jetzt einen festen Plan." },
    { datum: iso(jahr, 5, 1), art: "auftakt", titel: "Fünf Monate bis zum Examen", kontext: "Nach dem Anmeldeschluss beginnt die heiße Phase: fünf Monate, drei Klausuren, ein Lernplan." },
    { datum: iso(jahr, 1, 15), art: "muendlich", titel: "Vorbereitung auf die mündliche Prüfung", kontext: "Die Ergebnisse der schriftlichen Prüfung kommen in diesen Wochen; wer bestanden hat, bereitet sich jetzt auf die mündliche Prüfung vor: Vortrag, Prüfungsgespräch, Aktualitäten." },
    { datum: iso(jahr, 12, 31), art: "jahreswechsel", titel: "Jahreswechsel: neuer Rechtsstand", kontext: "Zum Jahreswechsel treten Gesetzesänderungen in Kraft; für das Examen zählt der Rechtsstand, den die Prüfung vorgibt." },
  ];
  /* Countdown-Meilensteine vor der schriftlichen Prüfung. */
  for (const n of [100, 60, 30, 14, 7, 3, 1]) {
    const d = new Date(`${pruefung.tag1}T12:00:00Z`); d.setUTCDate(d.getUTCDate() - n);
    liste.push({ datum: d.toISOString().slice(0, 10), art: "countdown", titel: `${n} Tag${n === 1 ? "" : "e"} bis zum Examen`, kontext: `In ${n} Tag${n === 1 ? "" : "en"} beginnt die schriftliche Prüfung (${pruefung.tag1} bis ${pruefung.tag3}). ${n >= 60 ? "Jetzt zählt der Lernplan: Dauerbrenner zuerst, Klausuren unter Zeit." : n >= 7 ? "Jetzt nur noch wiederholen, was sitzt – keine neuen Themen mehr." : "Schlaf, Ruhe, Prüfschemata durchgehen – nichts Neues mehr anfangen."}` });
  }
  liste.push(
    { datum: pruefung.tag1, art: "pruefungstag", titel: "Tag 1: Verfahrensrecht, Umsatzsteuer, Erbschaftsteuer", kontext: "Heute ist der erste Prüfungstag (AO, USt, ErbSt/BewG). Ton: ruhig, ermutigend, ein letzter Klausurtipp – keine neuen Inhalte." },
    { datum: pruefung.tag2, art: "pruefungstag", titel: "Tag 2: Ertragsteuern", kontext: "Heute ist der zweite Prüfungstag (ESt, KSt, GewSt, IStR). Ton: ermutigend, ein Klausurtipp zur Zeiteinteilung." },
    { datum: pruefung.tag3, art: "pruefungstag", titel: "Klausurtag Öffentliches Recht", kontext: "Heute war ein Klausurtag im Öffentlichen Recht. Ton: ermutigend, Hinweis auf Technikpunkte (Klageart, Zulässigkeitsaufbau, Verhältnismäßigkeit)." },
  );
  const nach = new Date(`${pruefung.tag3}T12:00:00Z`); nach.setUTCDate(nach.getUTCDate() + 1);
  const nachIso = nach.toISOString().slice(0, 10);
  liste.push({ datum: nachIso, art: "danach", titel: "Geschafft: Der Tag nach der Prüfung", kontext: "Die schriftliche Prüfung ist vorbei. Ton: Anerkennung, Durchatmen, Ausblick auf Ergebnisse und mündliche Prüfung." });
  /* Lösungsskizzen am Abend der Prüfungstage: der reichweitenstärkste Content
     des Jahres – tausende Kandidat:innen suchen abends nach Lösungsansätzen,
     die offiziellen Hinweise kommen erst Monate später. */
  const tage = [
    [pruefung.tag1, 1, "Verfahrensrecht (AO), Umsatzsteuer, Erbschaftsteuer/Bewertung"],
    [pruefung.tag2, 2, "Strafrecht"],
    [pruefung.tag3, 3, "Öffentliches Recht"],
  ];
  for (const [d, nr, faecher] of tage) {
    liste.push({ datum: d, zeit: "18:30", art: "loesungsskizze", klausur: nr, titel: `Lösungsskizze Tag ${nr}: die berichteten Themen`, kontext: `Heute war Klausurtag ${nr} der schriftlichen Prüfung (${faecher}). Kandidat:innen berichten in Foren und sozialen Netzwerken, welche Sachverhalte drankamen. Aufgabe: die berichteten Themen sammeln und je Thema den Lösungsweg skizzieren – ausdrücklich vorläufig, auf Berichten beruhend, keine offizielle Lösung. Einladung: „Was war bei dir dran? Schreib es in die Kommentare, ich ergänze.“` });
  }
  liste.push({ datum: nachIso, zeit: "12:30", art: "loesungsskizze", klausur: 3, titel: "Alle drei Tage im Überblick: Themen und Lösungswege", kontext: `Die schriftliche Prüfung ${pruefung.jahr} ist vorbei (${pruefung.tag1} bis ${pruefung.tag3}). Aufgabe: die berichteten Themen aller drei Tage bündeln, je Klausur die zwei wichtigsten Lösungswege skizzieren, vorläufig und ohne Anspruch auf Vollständigkeit. Einladung, eigene Erinnerungen an die Aufgaben zu kommentieren.` });
  /* Okt–Dez: Rund die Hälfte fällt durch – wer neu anfängt, braucht jetzt einen
     anderen Plan. Montags ein Beitrag „Zweiter Anlauf“. */
  const neustart = [
    ["Zweiter Anlauf: Warum du beim nächsten Mal anders lernen solltest", "Rund die Hälfte besteht nicht. Wer neu ansetzt, sollte nicht mehr lernen, sondern anders: Fehleranalyse statt Stoffwiederholung, Klausuren unter Zeit von Anfang an, Schemata vor Details."],
    ["Fehleranalyse nach dem Examen: Woran es wirklich lag", "Die häufigsten Gründe fürs Nichtbestehen sind Zeit, Aufbau und unsaubere Subsumtion – nicht fehlendes Wissen. Ehrliche Bestandsaufnahme mit drei Fragen."],
    ["Der Lernplan für den zweiten Anlauf: 12 Monate in vier Phasen", "Von November bis zum nächsten Oktober: Grundlagen, Aufbau, Klausurtraining, Endspurt – mit festen Wochenzielen je Klausurtag."],
    ["Mündliche Prüfung oder zweiter Anlauf: So gehst du mit der Wartezeit um", "Bis zu den Ergebnissen dauert es Monate. Was in dieser Zeit sinnvoll ist – für beide Ausgänge."],
    ["Klausuren unter Zeit: die eine Gewohnheit, die den zweiten Anlauf entscheidet", "Wer im zweiten Anlauf jede Woche eine Klausur unter Echtzeit schreibt, löst das Zeitproblem, an dem die meisten scheitern."],
  ];
  const start = new Date(`${nachIso}T12:00:00Z`); start.setUTCDate(start.getUTCDate() + 4);
  let i = 0;
  for (let d = new Date(start); d.getUTCMonth() <= 11 && d.getUTCFullYear() === pj; d.setUTCDate(d.getUTCDate() + 1)) {
    if (d.getUTCDay() !== 1) continue;
    const [titel, kontext] = neustart[i++ % neustart.length];
    liste.push({ datum: d.toISOString().slice(0, 10), art: "neustart", titel, kontext });
  }
  /* Jan–30. April: Entscheidungs- und Anmeldefenster. Jeden zweiten Montag ein
     Beitrag zu Entscheidung, Lernplan und Motivation – keine Verkaufsbotschaft. */
  const fenster = [
    ["Antreten oder warten? Die ehrliche Entscheidung vor der Anmeldung", "Bis 30. April muss die Anmeldung stehen. Kriterien: Stundenbudget, Klausurstand, Vorwissen je Klausurtag – und was passiert, wenn man ein Jahr wartet."],
    ["Sechs Monate Lernplan: So teilst du die Zeit auf die drei Klausurtage auf", "Nach der Entscheidung kommt der Plan: Wochenstunden je Klausurtag, feste Klausurtermine, Wiederholungsschleifen."],
    ["Was Bestehende anders gemacht haben: fünf Muster", "Aus Erfahrungsberichten lassen sich Muster ableiten: früh Klausuren schreiben, Schemata auswendig, Lerngruppe, Pausen, ein fester Prüfungstag-Ablauf."],
    ["Meldung zum Examen: Fristen, Unterlagen, Stolpersteine", "Antrag, Nachweise, Freischuss-Voraussetzungen – was oft vergessen wird. Je nach Land unterschiedlich."],
  ];
  let j = 0, zaehler = 0;
  for (let d = new Date(Date.UTC(jahr, 0, 1)); d.getUTCMonth() <= 3; d.setUTCDate(d.getUTCDate() + 1)) {
    if (d.getUTCDay() !== 1) continue;
    if (zaehler++ % 2) continue;
    const [titel, kontext] = fenster[j++ % fenster.length];
    liste.push({ datum: d.toISOString().slice(0, 10), art: "anmeldefenster", titel, kontext });
  }
  return liste;
}

/* Alle Anlässe eines Datums (Morgen-Anlass ohne Uhrzeit, Abend-Anlass mit Uhrzeit). */
export function anlaesseFuer(datum) {
  return anlaesse(datum).filter((a) => a.datum === datum);
}

/* Mindset-Themen für die Samstags-Reels (Ersatz für den „Talking Head“):
   holen Menschen ab, die Fachposts nie sehen würden. */
export const MINDSET_THEMEN = [
  { id: "mindset-1", typ: "mindset", fach: "ao", klausur: 1, prioritaet: "hoch", titel: "Prüfungsangst: Was am Abend vor Tag 1 wirklich hilft", normen: [], kern: { einordnung: ["Angst ist normal und sogar nützlich – solange sie nicht das Denken blockiert."], lernziele: ["ein konkretes Abendritual", "Schlaf vor Wiederholung", "Materialien am Vorabend packen"], merksatz: "Nichts Neues mehr lernen, nur noch Ruhe organisieren." } },
  { id: "mindset-2", typ: "mindset", fach: "ao", klausur: 1, prioritaet: "hoch", titel: "Blackout in der Klausur: das 3-Schritte-Protokoll", normen: [], kern: { einordnung: ["Ein Blackout dauert Minuten, wenn man ein Protokoll hat – und die ganze Klausur, wenn nicht."], lernziele: ["Aufgabe wechseln statt starren", "Sachverhalt laut im Kopf gliedern", "mit dem Schema beginnen, nicht mit der Lösung"], merksatz: "Wechseln, gliedern, Schema – dann kommt der Rest." } },
  { id: "mindset-3", typ: "mindset", fach: "kst", klausur: 2, prioritaet: "hoch", titel: "Zeitdruck: Warum Punkte am Ende verloren gehen, nicht am Anfang", normen: [], kern: { einordnung: ["Fast alle verlieren Punkte, weil sie die erste Aufgabe zu schön machen."], lernziele: ["Minutenplan je Aufgabe", "Ergebnissatz auch ohne letzte Rechenzeile", "Abbruchkriterium am Rand notieren"], merksatz: "Die Uhr entscheidet über die Note, nicht das Wissen." } },
  { id: "mindset-4", typ: "mindset", fach: "bilanz", klausur: 3, prioritaet: "hoch", titel: "Perfektionismus: Der Bearbeitungsstil, der durchfallen lässt", normen: [], kern: { einordnung: ["Perfekte Teillösungen bringen weniger als vollständige, knappe Lösungen."], lernziele: ["alle Textziffern anfassen", "Buchungssatz und Gewinnauswirkung immer", "erst Punkte sammeln, dann glätten"], merksatz: "Vollständig schlägt perfekt." } },
  { id: "mindset-5", typ: "mindset", fach: "ust", klausur: 1, prioritaet: "hoch", titel: "Lerngruppe: Warum du nicht allein lernen solltest", normen: [], kern: { einordnung: ["Wer erklärt, versteht. Wer sich vergleicht, erkennt Lücken."], lernziele: ["wöchentlicher Klausurtausch", "gegenseitiges Korrigieren mit Punkteschema", "ein fester Termin"], merksatz: "Erklären ist die härteste Prüfung – und die beste Vorbereitung." } },
  { id: "mindset-6", typ: "mindset", fach: "kst", klausur: 2, prioritaet: "hoch", titel: "Der Prüfungstag: Ablauf von 5 Uhr bis zur Abgabe", normen: [], kern: { einordnung: ["Ein fester Ablauf nimmt Entscheidungen ab, die am Prüfungstag Energie kosten."], lernziele: ["Frühstück, Anreise, Materialien", "erste 10 Minuten: Sachverhalt lesen, nicht schreiben", "Pausen bewusst nehmen"], merksatz: "Routine ist am Prüfungstag mehr wert als jede Wiederholung." } },
  { id: "mindset-7", typ: "mindset", fach: "bilanz", klausur: 3, prioritaet: "hoch", titel: "Nach einer schlechten Klausur: Wie du Tag 2 trotzdem rettest", normen: [], kern: { einordnung: ["Ein Tag entscheidet nicht – der Durchschnitt zählt, und Tag 2 und 3 sind noch offen."], lernziele: ["nicht nachrechnen, nicht diskutieren", "Abend ohne Fachgespräch", "Schemata für den nächsten Tag durchgehen"], merksatz: "Was geschrieben ist, ist geschrieben. Der nächste Tag ist eine neue Klausur." } },
  { id: "mindset-8", typ: "mindset", fach: "ao", klausur: 1, prioritaet: "hoch", titel: "Wie du mit Nichtwissen in der Klausur umgehst", normen: [], kern: { einordnung: ["Niemand weiß alles – Punkte gibt es für sauberen Aufbau auch bei unsicherem Ergebnis."], lernziele: ["Obersatz, Definition, Subsumtion trotzdem", "mit vertretbarer Annahme weiterrechnen", "keine leeren Aufgaben"], merksatz: "Ein sauberer Weg zum falschen Ergebnis bringt mehr als kein Weg." } },
];

export function mindsetThema(datum) {
  const tage = Math.floor(Date.UTC(+datum.slice(0, 4), +datum.slice(5, 7) - 1, +datum.slice(8, 10)) / 86400000);
  return MINDSET_THEMEN[Math.floor(tage / 7) % MINDSET_THEMEN.length];
}

/* Anlass für genau dieses Datum (oder null). */
export function anlassFuer(datum) {
  return anlaesse(datum).find((a) => a.datum === datum) || null;
}

/* Ohne festen Termin richtet sich die Phase nach dem Kalenderjahr: Kampagnen
   im Frühjahr und Herbst, dazwischen Vorbereitung. */
function jahresPhase(datum) {
  const monat = Number(datum.slice(5, 7));
  if (monat === 3 || monat === 4) return "Frühjahrskampagne – viele schreiben gerade ihre Examensklausuren: Klausurtechnik, Dauerbrenner, Nerven; nichts Neues aufmachen";
  if (monat === 8 || monat === 9) return "Herbstkampagne – zweite Klausurenrunde des Jahres: Wiederholung, Zeitmanagement, ruhiger Ton";
  if (monat === 5 || monat === 10) return "Neustart – neuer Referendarjahrgang bzw. Semesterbeginn: Grundlagen, Aufbauwissen, Lernorganisation";
  if (monat === 1 || monat === 2) return "Vorbereitungsphase – Lernplan, Stoffverteilung, Klausurenkurs; jetzt ist Zeit für Tiefe";
  return "reguläre Vorbereitungszeit – Examenswissen systematisch, Streitstände und Schemata";
}

/* Kurzer Kontext für den Autor: Wo stehen wir im Prüfungsjahr? Der Jahreszyklus
   ist der Redaktionsplan. */
export function phase(datum) {
  if (!CONFIG.examen.schriftlich) return jahresPhase(datum);
  const tage = tageBis(CONFIG.examen.schriftlich, new Date(`${datum}T12:00:00Z`));
  const monat = Number(datum.slice(5, 7));
  if (tage >= 0 && tage <= 2) return "Prüfungstage – morgens Ruhe und ein letzter Klausurtipp, abends die Lösungsskizze zu den berichteten Themen";
  if (tage > 2 && tage <= 14) return "Endspurt vor der schriftlichen Prüfung – nur wiederholen, nichts Neues; Klausurtechnik, Zeitmanagement, Dauerbrenner; Ziel: Reichweite und Weiterleitungen in Lerngruppen, nichts verkaufen";
  if (tage > 14 && tage <= CONFIG.plan.endspurtTage) return "letzte Wochen vor der Prüfung – Klausurtechnik, Zeitmanagement, Dauerbrenner-Wiederholung; die Zielgruppe ist jetzt am aufmerksamsten; Ziel: Reichweite und Weiterleitungen, nichts verkaufen";
  if (tage > CONFIG.plan.endspurtTage && tage <= 60) return "heiße Phase – Klausuren unter Zeit, Dauerbrenner sichern";
  if (tage < 0 && tage >= -3) return "direkt nach der Prüfung – Lösungsskizzen zu den berichteten Klausurthemen, Anerkennung, Durchatmen";
  if (monat >= 10) return "nach der Prüfung (Okt–Dez) – rund die Hälfte besteht nicht: Wer neu ansetzt, braucht einen anderen Plan (Fehleranalyse, Klausuren unter Zeit, Schemata); daneben mündliche Prüfung für die anderen";
  if (monat <= 4) return "Entscheidungs- und Anmeldefenster (Anmeldeschluss 30. April) – der neue Jahrgang entscheidet, ob und wie er lernt: Lernplanung, Entscheidungshilfen, Motivation, Community; keine Verkaufsbotschaft";
  return "Hauptlernphase (Mai–September) – höchstes Engagement: Systematik, Schemata, Dauerbrenner, Klausurtraining";
}
