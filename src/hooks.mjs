/* ==========================================================================
   Hooks für Reels: Thema sofort erkennbar, Nutzen sofort klar.

   Fuer die Verteilung zaehlen vor allem Aufmerksamkeit und Weiterleitungen.
   Daraus folgt fuer einen Examenskanal NICHT mehr Clickbait, sondern mehr
   Praezision: Wer den Kanal noch nicht kennt, muss in der ersten Kachel bzw.
   im ersten Satz erkennen, welche Rechtsfrage geloest wird und warum der
   Inhalt fuer die Klausur nuetzlich ist.

   Keine erfundenen Haeufigkeiten, Punktwerte, Korrektorenvorlieben oder
   Superlative. Ein guter Hook verspricht nur, was das Reel danach einloest.
   ========================================================================== */

export const HOOKS = {
  frage: {
    name: "Prüfungsfrage",
    regel: "Stelle die konkrete Rechtsfrage, die das Reel beantwortet. Der Fachbegriff oder die Norm gehört in den Bildschirmtext.",
    beispiele: [
      { titel: "§ 123 oder § 80 V?", sprecher: "Wann brauchst du Paragraf 123 VwGO – und wann Paragraf 80 Absatz 5?" },
      { titel: "Heimtücke trotz offenen Angriffs?", sprecher: "Kann Heimtücke vorliegen, obwohl der Täter dem Opfer offen gegenübertritt?" },
    ],
  },
  abgrenzung: {
    name: "Abgrenzung",
    regel: "Stelle zwei klausurrelevante Alternativen gegeneinander. Beide Begriffe müssen auf dem Bildschirm stehen.",
    beispiele: [
      { titel: "Anfechtung oder Rücktritt?", sprecher: "Ein Irrtum und ein Mangel treffen zusammen – welcher Weg gehört zuerst in die Prüfung?" },
      { titel: "Raub oder räuberische Erpressung?", sprecher: "Woran trennst du Raub und räuberische Erpressung im Aufbau sauber?" },
    ],
  },
  fehler: {
    name: "Konkrete Falle",
    regel: "Benenne einen sachlich belegbaren Aufbau- oder Zuordnungsfehler. Behaupte nicht, wie viele ihn machen oder wie viele Punkte er kostet.",
    beispiele: [
      { titel: "Annahmeverzug: hier kippt der Anspruch", sprecher: "Wenn du Annahmeverzug und Unmöglichkeit vertauschst, prüfst du ab hier die falsche Rechtsfolge." },
      { titel: "Falscher Antrag, falscher Aufbau", sprecher: "Bei Paragraf 80 Absatz 5 entscheidet schon der Antrag, welchen Prüfungsmaßstab du brauchst." },
    ],
  },
  reihenfolge: {
    name: "Reihenfolge",
    regel: "Zeige die Stelle, an der eine Prüfungsreihenfolge entscheidet. Formuliere als konkrete 'was zuerst?'-Frage.",
    beispiele: [
      { titel: "Konkurrenzen: was prüfst du zuerst?", sprecher: "Bei Konkurrenzen entscheidet die Reihenfolge, ob dein weiterer Aufbau überhaupt passt." },
      { titel: "Erst Anspruch, dann Einrede?", sprecher: "Wo gehört die Verjährung hin, damit Anspruch und Einrede sauber getrennt bleiben?" },
    ],
  },
  fall: {
    name: "Mini-Fall",
    regel: "Beginne mit einem sehr kurzen Sachverhaltsmoment und nenne die Rechtsfrage noch in derselben Hook-Szene.",
    beispiele: [
      { titel: "Ware weg – wer trägt?", sprecher: "Der Käufer nimmt nicht ab, danach geht die Ware unter: Wer trägt jetzt die Gegenleistungsgefahr?" },
      { titel: "Bescheid da, Tatsache neu", sprecher: "Nach dem Steuerbescheid taucht eine neue Tatsache auf – hier entscheidet die Korrekturvorschrift." },
    ],
  },
  norm: {
    name: "Norm-Anker",
    regel: "Nutze eine konkrete Norm als Wiedererkennungsanker und sage, welche Entscheidung an ihr hängt.",
    beispiele: [
      { titel: "§ 254 BGB: wo genau?", sprecher: "Paragraf 254 BGB ist schnell genannt – entscheidend ist, an welcher Stelle du ihn einbaust." },
      { titel: "§ 28 StGB: welche Ebene?", sprecher: "Paragraf 28 StGB löst nicht jedes Beteiligungsproblem gleich – zuerst brauchst du die richtige Ebene." },
    ],
  },
  widerspruch: {
    name: "Irrtum korrigieren",
    regel: "Korrigiere nur eine tatsächlich falsche Aussage, die du im Reel fachlich begründen kannst. Kein Strohmann, kein 'alle lernen das falsch'.",
    beispiele: [
      { titel: "Widerspruch stoppt Vollziehung?", sprecher: "Nein – Widerspruch und aufschiebende Wirkung musst du sauber auseinanderhalten." },
      { titel: "Verbotsirrtum bei ETBI?", sprecher: "Den Erlaubnistatbestandsirrtum ordnest du nicht einfach wie einen normalen Verbotsirrtum ein." },
    ],
  },
  loesung: {
    name: "Konkreter Ablauf",
    regel: "Versprich einen kleinen, klaren Ablauf, den das Reel vollständig liefert. Zahlen nur, wenn genau so viele Schritte folgen.",
    beispiele: [
      { titel: "Drei Schritte zur Klageart", sprecher: "Mit drei Fragen kommst du von Begehren und Maßnahme zur passenden Klageart." },
      { titel: "So ordnest du Konkurrenzen", sprecher: "Erst Gesetzeseinheit, dann Tateinheit oder Tatmehrheit – genau diese Reihenfolge bauen wir auf." },
    ],
  },
};

export const HOOK_TYPEN = Object.keys(HOOKS);

const SCHWACHE_OEFFNER = /^\s*(hallo|hi\b|hey|guten (morgen|tag|abend)|willkommen|schön,? dass|heute (geht|zeige|sprechen|schauen|lernen)|in diesem (video|reel|beitrag)|wir (schauen|sprechen|klären)|lass uns|ich (zeige|erkläre) (dir|euch) (heute|jetzt))/i;
const UNBELEGTE_CLAIMS = /fast alle|die meisten|kaum jemand|niemand|jeder macht|in jeder.{0,24}klausur|kommt (?:fast )?jedes jahr|immer dran|verrät|häufigste|teuerste|volle punkte|halbe (?:klausur|punkte)|prüfer(?::innen|innen)? (?:lieben|erwarten)|garantiert|punktegeschenk/i;
const GENERISCHER_TITEL = /^(kenn(?:st|en) du (?:das|diesen moment)|das stimmt so nicht|schluss mit raten|so nicht,? sondern so|ein halbsatz entscheidet|die reihenfolge ist alles|was prüfst du zuerst\??|hier kippt (?:der|die|das) [^!?]+)[!? .]*$/i;

export const HOOK_GRENZEN = { titelWoerter: 7, sprecherWoerter: 20 };

export function hookWaehlen(datum, strategie = null) {
  const gewicht = strategie?.hookGewicht || {};
  const stark = HOOK_TYPEN.filter((t) => (gewicht[t] ?? 1) >= 0.75);
  const auswahl = stark.length ? stark : HOOK_TYPEN;
  const tag = Math.floor(Date.parse(`${datum}T12:00:00Z`) / 86400000);
  return auswahl[((tag % auswahl.length) + auswahl.length) % auswahl.length];
}

export function hookAnleitung(typ) {
  const h = HOOKS[typ] || HOOKS.frage;
  const beispiele = h.beispiele.map((b) => `  · Bildschirm: „${b.titel}“ – gesprochen: „${b.sprecher}“`).join("\n");
  return `## Hook (Szene 1) – Muster „${h.name}“
${h.regel}
Der Bildschirmtext muss OHNE Ton und OHNE Caption verständlich sein: höchstens ${HOOK_GRENZEN.titelWoerter} Wörter, groß lesbar, mit Rechtsfrage, Norm oder Abgrenzungsbegriffen statt einer austauschbaren Neugierformel.
Gesprochen ist der Hook EIN Satz mit höchstens ${HOOK_GRENZEN.sprecherWoerter} Wörtern und steht ganz am Anfang – keine Begrüßung und keine Ankündigung.
Kein erfundener Konsens („fast alle“), keine erfundene Punktwirkung, kein Korrektoren-Mindreading. Das Versprechen der Hook-Szene muss das Reel vollständig einlösen.
So klingt das Muster (andere Themen):
${beispiele}`;
}

export function pruefeHook(szene) {
  const fehler = [];
  if (!szene) return ["Erste Szene fehlt – ohne Hook kein Reel"];
  const titel = String(szene.titel || "").trim();
  const sprecher = String(szene.sprecher || "").trim();
  if (!titel) fehler.push("Hook: Der Bildschirmtext der ersten Szene fehlt");
  const titelWoerter = titel.split(/\s+/).filter(Boolean).length;
  if (titelWoerter > HOOK_GRENZEN.titelWoerter) fehler.push(`Hook: Bildschirmtext hat ${titelWoerter} Wörter (höchstens ${HOOK_GRENZEN.titelWoerter})`);
  if (SCHWACHE_OEFFNER.test(sprecher)) fehler.push("Hook: Die ersten Sekunden beginnen mit Ankündigung/Begrüßung statt mit der Sache");
  if (UNBELEGTE_CLAIMS.test(`${titel} ${sprecher}`)) fehler.push("Hook: unbelegte Häufigkeits-, Punkte- oder Korrektorenbehauptung");
  if (GENERISCHER_TITEL.test(titel)) fehler.push("Hook: Bildschirmtext ist ohne Ton zu generisch – Rechtsfrage/Begriff muss auf die erste Szene");
  const ersterSatz = sprecher.split(/(?<=[.!?])\s/)[0] || "";
  const satzWoerter = ersterSatz.split(/\s+/).filter(Boolean).length;
  if (satzWoerter > HOOK_GRENZEN.sprecherWoerter) fehler.push(`Hook: gesprochener Aufhänger hat ${satzWoerter} Wörter (höchstens ${HOOK_GRENZEN.sprecherWoerter})`);
  return fehler;
}

export function hookTypErkennen(titel = "", sprecher = "") {
  const t = `${titel} ${sprecher}`;
  if (/\boder\b|vs\.?|unterschied|abgrenz/i.test(titel)) return "abgrenzung";
  if (/was prüfst du zuerst|erst .* dann|reihenfolge/i.test(t)) return "reihenfolge";
  if (/^§|paragraf|§\s*\d/i.test(titel)) return "norm";
  if (/drei schritte|vier schritte|so ordnest|so prüfst/i.test(t)) return "loesung";
  if (/stimmt (?:so )?nicht|nein\b|nicht einfach|genau umgekehrt/i.test(t)) return "widerspruch";
  if (/fehler|falle|falsch|vertausch|kippt/i.test(t)) return "fehler";
  if (/\?/.test(titel)) return "frage";
  if (/\bdu\b|\bdir\b|bescheid|ware|vertrag|opfer|täter|käufer|kläger/i.test(t)) return "fall";
  return "frage";
}
