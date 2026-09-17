/* ==========================================================================
   Faktencheck: ein zweiter, unabhängiger Aufruf prüft jeden Beitrag und
   jedes Reel-Skript auf fachliche Fehler – Normzitate, Prüfungsaufbau,
   Streitstände, Definitionen, Fristen, Zuständigkeiten, Rechtsstand 2026.
   Nur klare Fehler führen zur Nachbesserung; Stilfragen nicht, und auch
   nicht, dass eine vertretbare Ansicht vertreten wird.
   ========================================================================== */

import Anthropic from "@anthropic-ai/sdk";
import { CONFIG } from "./config.mjs";
import { erfassen, budgetPruefen, BudgetFehler } from "./kosten.mjs";

let clientCache = null;
const client = () => (clientCache ||= new Anthropic({ maxRetries: 3, timeout: 5 * 60 * 1000 }));

const SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    befunde: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        properties: {
          schwere: { type: "string", enum: ["fehler", "unsicher", "hinweis", "sprache"] },
          stelle: { type: "string" },
          problem: { type: "string" },
          korrektur: { type: "string" },
          /* Nur bei „sprache“: die fehlerhafte Wortfolge genau so, wie sie im
             Text steht, und die berichtigte Fassung. Damit lässt sich der
             Fehler ohne Neufassung im Text ersetzen. */
          original: { type: "string" },
          ersatz: { type: "string" },
        },
        required: ["schwere", "stelle", "problem", "korrektur", "original", "ersatz"],
      },
    },
  },
  required: ["befunde"],
};

const SYSTEM = `Du bist Prüfer:in für juristische Fachtexte (erstes und zweites juristisches Staatsexamen, deutsches Recht, Rechtsstand 2026). Du bekommst Texte eines Instagram-Kanals und prüfst ausschließlich die fachliche Richtigkeit:
- Normzitate: richtiges Gesetz, Paragraf, Absatz, Satz, Nummer, Buchstabe. Ein falscher Absatz ist ein Fehler, auch wenn die Aussage stimmt.
- Ob die genannte Norm die Aussage überhaupt trägt: Wird § 823 Abs. 1 BGB für etwas zitiert, das aus § 823 Abs. 2 BGB folgt, ist das ein Fehler.
- Prüfungsaufbau und Reihenfolge: Tatbestand vor Rechtswidrigkeit vor Schuld; Zulässigkeit vor Begründetheit; Anspruch entstanden, nicht erloschen, durchsetzbar.
- Streitstände: Wird eine Ansicht der Rechtsprechung oder der Literatur zugeschrieben, muss die Zuordnung stimmen. Wird ein Streit als entschieden dargestellt, der offen ist (oder umgekehrt), ist das ein Fehler. Fehlt bei einem Streit der Streitentscheid, ist das ein Hinweis.
- Definitionen: Die gängige Definition muss vollständig sein – fehlt ein Merkmal, kostet das in der Klausur Punkte.
- Fristen, Zahlen, Schwellenwerte und Zuständigkeiten (Instanzenzug, Gerichtsbarkeit, sachliche und örtliche Zuständigkeit).
- Rechtsstand: aufgehobene oder geänderte Normen sind Fehler (z. B. die GbR nach dem MoPeG, das Schuldrecht nach der Warenkaufrichtlinie).
- Landesrecht: Polizei-, Kommunal- und Bauordnungsrecht unterscheiden sich je Bundesland. Wird ein Landesparagraf als bundesweit gültig ausgegeben, ist das ein Fehler; fehlt der Hinweis auf die Landesabhängigkeit, ist es ein Hinweis.
- Innere Logik: Der Text muss aus sich heraus verständlich sein. Wird auf einen Fall, eine Person oder eine Zahl Bezug genommen, die nirgends eingeführt wird, ist das ein „fehler“ – mit dem Hinweis, welche Angaben fehlen.
- Personenbezug: Jede Voraussetzung, die an eine bestimmte Person geknüpft ist – Kenntnis, Kennenmüssen, Zustimmung, Erklärung, Verschulden, Zurechnung –, prüfst du ausdrücklich darauf, WELCHE Person Gesetz oder Rechtsprechung meinen. Wird sie der falschen Person zugeschrieben (dem anderen Ehegatten statt dem Vertragspartner bei § 1365 BGB, dem Gläubiger statt dem Schuldner, dem Täter statt dem Opfer), ist das ein „fehler“, auch wenn der Satz sonst stimmt. Sag dir bei jeder solchen Stelle: „Wer genau muss hier was?“ – und entscheide erst dann.
- Fallgruppen bei Zahlen: Staffelt die Rechtsprechung einen Wert nach Fallgruppen (kleines gegen großes Vermögen, Verbraucher gegen Unternehmer), ist ein Wert für die falsche Fallgruppe ein „fehler“ und eine Spanne, die beide vermischt („85 bis 90 Prozent“), ein „hinweis“ mit der gestaffelten Fassung als Korrektur.
- Vollständigkeit einer Rechtsfolge: Wird eine Rechtsfolge an eine Voraussetzung geknüpft, das Gesetz verlangt aber eine weitere tragende Voraussetzung (die Ersetzung der Zustimmung nach § 1365 Abs. 2 BGB nur bei ordnungsmäßiger Verwaltung), ist das ein „hinweis“; macht das Fehlen die Aussage falsch, ein „fehler“.
- Behauptungen über Häufigkeit oder Typik („der häufigste Fehler“, „die meisten übersehen“) sind ohne Beleg ein „hinweis“ mit einer neutralen Fassung als Korrektur („ein typischer Aufbaufehler“).

Du prüfst gegen Gesetz und Rechtsprechung, nicht gegen den Autor: Der Text stammt von einem Modell derselben Familie wie du. Was dir plausibel klingt, ist dadurch nicht richtig – ein Fehler, der dir beim Schreiben unterliefe, unterläuft dir auch beim Lesen, wenn du nicht bewusst dagegenhältst. Prüfe jede Zuschreibung (wer, was, wann, wie viel) gegen ihr Gegenteil, bevor du sie durchwinkst. Ein kurzer Text ist kein Grund für eine kurze Prüfung: Ein Reel-Skript mit 140 Wörtern trägt so viele Behauptungen wie ein Beitrag, und es wird von mehr Menschen gehört.

Zusätzlich – und nur das – prüfst du die Sprache auf offensichtliche Versehen: doppelte Wörter („U hat U selbst“), fehlende Wörter, verdrehte Buchstaben, ein falscher Kasus, eine abgebrochene Klammer. Dazu gehören auch Überschriften, die grammatisch nicht aufgehen: „Wochenrückblick: alles sitzen?“ ist falsch (richtig: „sitzt alles?“), ebenso ein Bezugsfehler zwischen Subjekt und Verb. Eine knappe Nominalphrase ohne Verb ist dagegen als Überschrift in Ordnung („Mord und Totschlag: das Verhältnis“). Melde solche Versehen als „sprache“ und gib in „original“ die fehlerhafte Wortfolge exakt so an, wie sie im Text steht (mindestens drei Wörter, damit die Stelle eindeutig ist), in „ersatz“ die berichtigte Fassung mit denselben Wörtern drumherum. Stilfragen, Umformulierungen und Kürzungen sind keine Sprachversehen – nur, was ein Korrektor mit dem Rotstift anstreichen würde. Auch bei einem fachlichen „fehler“ gibst du „original“ und „ersatz“ an, WENN er sich durch Austausch einer Wortfolge beheben lässt (falscher Absatz, falsche Zahl, falsch benanntes Merkmal, falsch zugeordnete Ansicht): „original“ die falsche Stelle exakt wie im Text, „ersatz“ dieselbe Stelle richtig, ohne den Satz umzubauen. Braucht die Berichtigung mehr als das – fehlt ein Sachverhalt, stimmt der Aufbau nicht, ist die Aussage im Kern falsch –, bleiben beide Felder leer. Bei allen übrigen Befunden ebenfalls.

Zahlen rechnest du nach, statt sie zu überfliegen. Für jede Zahl im Text – Bruchteil, Quote, Frist, Betrag, Schwellenwert – prüfst du einzeln:
1. Trägt die zitierte Norm genau diese Zahl? Mach dir die Tatbestandsvariante klar, aus der sie folgt. Eine Zahl, die du nicht aus der genannten Norm herleiten kannst, ist ein Fehler.
2. Hängt die Zahl an einer Voraussetzung, die im Sachverhalt stehen muss – Güterstand, Ordnung der Verwandten, Fristbeginn, Rechtsform? Fehlt diese Angabe im Text, ist das ein Fehler: Die Zahl steht dann auf einer Annahme.
3. Geht die Rechnung auf? Teilquoten müssen zusammen das Ganze ergeben.
Eine Rechnung, die am Ende aufgeht, kann trotzdem auf einer falschen Ausgangszahl beruhen – prüfe deshalb jede Zahl für sich, nicht nur die Summe. Hat eine Norm je nach Fallgruppe verschiedene Werte (etwa der Ehegattenerbteil neben Verwandten erster gegenüber zweiter Ordnung), sag dir ausdrücklich, welche Fallgruppe hier vorliegt, und prüfe erst dann, ob der Text den passenden Wert genommen hat.

Die Systematik des Materials ist nicht dein Maßstab, sondern dein Ausgangspunkt. Derselbe Stoff wird in der Literatur oft unterschiedlich geschnitten – wo ein Aufbau, eine Prüfungsreihenfolge oder eine Einteilung in Ebenen von der dir geläufigen Darstellung abweicht, aber in sich stimmig und vertretbar ist, ist das KEIN Fehler, sondern höchstens ein „hinweis“. Ein „fehler“ ist die Abweichung erst, wenn sie nicht mehr vertretbar ist: wenn sie dem Gesetzeswortlaut, der gefestigten Rechtsprechung oder der ganz herrschenden Meinung widerspricht. Ein Widerspruch INNERHALB eines Beitrags – dieselbe Sache einmal so und einmal anders eingeordnet – ist dagegen immer ein Fehler.

Melde als „fehler“ nur, was eindeutig falsch ist und in der Klausur Punkte kosten würde. Als „unsicher“ alles, was du nicht sicher beurteilen kannst – gerade bei Streitständen und Landesrecht lieber „unsicher“ als eine falsche Korrektur. Als „hinweis“ Unschärfen, die vertretbar sind. Keine Stil- oder Formatkritik, und keine Kritik daran, dass eine vertretbare Ansicht vertreten wird. Wenn alles korrekt ist, gib eine leere Liste zurück.`;

export function textAus(beitrag) {
  const teile = [];
  for (const f of beitrag.folien || []) teile.push(`[Folie ${f.art}] ${[f.titel, f.untertitel, f.text, ...(f.punkte || []), ...(f.schritte || []).map((s) => (typeof s === "string" ? s : `${s.titel}: ${s.text || ""}`)), f.formel, ...(f.zeilen || []), f.ergebnis, f.links?.titel, ...(f.links?.punkte || []), f.rechts?.titel, ...(f.rechts?.punkte || [])].filter(Boolean).join(" · ")}`);
  for (const s of beitrag.szenen || []) teile.push(`[Szene ${s.art}] ${[s.titel, s.text, s.norm, s.sprecher].filter(Boolean).join(" · ")}`);
  /* Stories tragen den Slot im Kopf, damit ein Befund einer einzelnen Kachel
     zugeordnet werden kann - neun Stories in einem Aufruf zu pruefen ist
     bezahlbar, neun einzelne Aufrufe waeren es nicht. */
  for (const s of beitrag.stories || []) teile.push(`[Story ${s.slot} ${s.art}] ${[s.ueberzeile, s.titel, s.norm, s.formel, s.zahl, s.text, ...(s.optionen || []), s.richtigText, s.falsch].filter(Boolean).join(" · ")}`);
  if (beitrag.caption) teile.push(`[Caption] ${beitrag.caption}`);
  /* Der Kurztitel stand bisher in keiner Pruefung - dabei ist er die
     Ueberschrift der Teaser-Story und des Reel-Covers, also das, was die
     meisten zuerst lesen. Am 13.09. ging so „Wochenrueckblick: alles sitzen?"
     durch, ein Satz ohne Praedikat. */
  if (beitrag.kurztitel) teile.push(`[Kurztitel] ${beitrag.kurztitel}`);
  return teile.join("\n");
}

/**
 * Wendet Sprachkorrekturen direkt auf die Texte an: jede Zeichenkette im
 * Objekt, in der „original“ wörtlich vorkommt, bekommt „ersatz“. Kein neuer
 * Aufruf, keine Neufassung – ein doppeltes Wort kostet so nichts.
 * @returns {number} Zahl der ersetzten Stellen
 */
export function korrekturenAnwenden(obj, korrekturen = []) {
  let n = 0;
  const gehe = (o) => {
    if (Array.isArray(o)) { o.forEach((v, i) => { if (typeof v === "string") { const w = ersetze(v); if (w !== v) { o[i] = w; } } else gehe(v); }); return; }
    if (o && typeof o === "object") for (const k of Object.keys(o)) { const v = o[k]; if (typeof v === "string") { const w = ersetze(v); if (w !== v) o[k] = w; } else gehe(v); }
  };
  const ersetze = (text) => {
    let t = text;
    for (const k of korrekturen) { if (k.original && t.includes(k.original)) { t = t.split(k.original).join(k.ersatz); n++; } }
    return t;
  };
  gehe(obj);
  return n;
}

/**
 * @returns {{ok:boolean, fehler:string[], hinweise:string[], korrekturen:{original:string, ersatz:string}[], behebbar:{original:string, ersatz:string}[]}}
 */
/* Befunde des Prüfers sortieren - als reine Funktion, damit ein Test sie
   greift. Weiche Beanstandungen („irreführend“, „präzisieren“,
   „missverständlich“) sind keine Fehler, die eine teure Neufassung
   rechtfertigen – sie werden zu Hinweisen. AUSSER der Prüfer liefert eine
   konkrete Ersetzung (original → ersatz) mit: Dann ist es ein Fehler mit
   Fundstelle, egal wie freundlich er formuliert ist, und die Berichtigung
   kostet nur eine Nachprüfung. Sonst wäre ein falscher Absatz mit dem Wort
   „ungenau" in der Begründung als Hinweis durchgerutscht. */
const WEICH = /irreführend|präzisier|missverständlich|ungenau|unscharf|unschärfe|ausdrucksweise|formulierung|konzeptionell|didaktisch|sollte (?:ergänzt|erwähnt|klargestellt)|könnte|empfehl|verkürzt|vereinfacht|mathematisch (?:richtig|korrekt)|ist (?:zwar |dann )?(?:sachlich )?korrekt|suggeriert|wird dem aufbau nicht gerecht|deutlicher|gestaffelt|darstellung/i;
export function befundeSortieren(befunde = []) {
  const brauchbar = (b) => Boolean(b?.original && b?.ersatz && b.original !== b.ersatz && String(b.original).trim().split(/\s+/).length >= 2);
  const sprache = (b) => b?.schwere === "sprache";
  const ist = (b) => b?.schwere === "fehler" && (brauchbar(b) || !WEICH.test(`${b.problem} ${b.korrektur}`));
  return {
    fehler: befunde.filter(ist),
    /* Sprachversehen mit brauchbarer Fundstelle werden ersetzt, nicht neu
       geschrieben. Ohne verwertbares Original bleibt es ein Hinweis. */
    korrekturen: befunde.filter((b) => sprache(b) && brauchbar(b)).map((b) => ({ original: b.original, ersatz: b.ersatz })),
    weich: befunde.filter((b) => !ist(b) && !sprache(b)),
    brauchbar,
  };
}

/* Wird in diesem Beitrag gerechnet? Dann prüft nicht das billigste Modell.

   Am 14.09. ging eine Erbquote raus, die Ehefrau und Kinder vertauscht hatte.
   Geprüft hatte Haiku, geschrieben Sonnet - das schwächere Modell sollte den
   Fehler des stärkeren finden. Bei allem anderen ist das vertretbar, bei
   Zahlen nicht: Eine falsche Zahl ist eindeutig falsch, sie steht groß auf
   der Kachel, und wer sie abschreibt, schreibt sie in die Klausur.

   Der Filter ist absichtlich weit - lieber ein paar Beiträge zu viel streng
   geprüft als der eine zu wenig. Teuer wird das nicht: In fünf Tagen traf es
   1 von 13 Beiträgen. */
const BRUCH_ZU_NORM = /\d+\s*\/\s*\d+\s*\(\s*§/;
const ZAHLWORT = /\b(Quote|Quoten|Erbteil|Bruchteil|Prozent|Frist von|Schwellenwert|Betrag|Hälfte|Drittel|Viertel|Achtel)\b/i;

export function zahlenLastig(beitrag) {
  for (const f of beitrag?.folien || []) {
    if (f.art === "rechnung" || f.formel) return true;
  }
  const text = JSON.stringify(beitrag || {});
  return BRUCH_ZU_NORM.test(text) || ZAHLWORT.test(text);
}

export async function pruefeFakten(beitrag, zweck = "faktencheck", { hinweis = "", streng = null } = {}) {
  if (!CONFIG.faktencheck.aktiv) return { ok: true, fehler: [], hinweise: [], korrekturen: [], behebbar: [] };
  budgetPruefen({ "reel-faktencheck": "Reel-Faktencheck", "story-faktencheck": "Story-Faktencheck" }[zweck] || "Faktencheck");
  /* Beiträge und Reels gehen immer an den strengen Prüfer.

     Die Auswertung der letzten fünf Tage war eindeutig: Der günstige Prüfer
     arbeitet - er fand auf 6 von 13 Beiträgen echte Feinheiten (§ 729 ZPO
     statt § 726, die Einordnung des § 28 StGB, einen unscharfen
     Prognosemaßstab). Beim Beitrag vom 14.09. gab er aber genau einen
     Hinweis, und zwar zur Folie DANEBEN, während die vertauschte Erbquote
     unbeanstandet blieb. Er hat hingeschaut und es nicht gesehen.

     Fehler sind eben nicht nur Zahlen: ein falscher Absatz, eine falsch
     zugeordnete Ansicht, ein Aufbau in der falschen Reihenfolge - all das
     kostet in der Klausur Punkte, und all das hängt an der Stärke des
     prüfenden Modells. Ein Beitrag steht dauerhaft im Feed.

     Stories bleiben beim günstigen Prüfer: Sie verschwinden nach 24 Stunden,
     und alle neun werden in EINEM Aufruf geprüft - eine Aufwertung schlüge
     dort am stärksten aufs Budget und am wenigsten auf die Haltbarkeit
     durch. Wird in einer Story gerechnet, greift die Eskalation trotzdem. */
  const stories = zweck === "story-faktencheck";
  const scharf = streng ?? (!stories || zahlenLastig(beitrag));
  const modell = (scharf && CONFIG.ki.modellPruefungStreng) || CONFIG.ki.modellPruefung || CONFIG.ki.modellNeben;
  if (scharf) console.log(`  Faktencheck streng (${modell})${stories ? " – in einer Story wird gerechnet." : ""}`);
  const haiku = /haiku/i.test(modell);
  const user = `Prüfe diesen Text:\n\n${textAus(beitrag)}${hinweis ? `\n\n${hinweis}` : ""}`;
  const basis = {
    model: modell,
    max_tokens: 6000,
    system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: user }],
    /* Haiku kennt kein adaptives Denken – dort ohne. */
    ...(haiku ? {} : { thinking: { type: "adaptive" } }),
    /* Das Reel bekommt die gründlichere Prüfung. Am 16.09. prüfte Sonnet das
       Herr-Jurist-Reel in sechs Sekunden mit 400 Ausgabe-Token - und ließ
       „Kenntnis des anderen Ehegatten“ statt des Vertragspartners durch. Ein
       Reel läuft einmal am Tag, wird am häufigsten gesehen und steht dauerhaft;
       die paar Cent mehr für tieferes Nachdenken sind dort am besten angelegt. */
    output_config: { ...(haiku ? {} : { effort: zweck === "reel-faktencheck" ? "high" : "medium" }), format: { type: "json_schema", schema: SCHEMA } },
  };
  /* Zwei Anläufe, bevor ein Fehler entsteht: erst mit Schema und Denken,
     dann - wenn die Antwort nicht lesbar ist oder das Modell ablehnt - ohne
     beides, JSON per Anweisung. Ein unlesbares Ergebnis war bis zum 17.09.
     ein stilles Bestehen; ein einzelner Fehlversuch soll aber auch keinen
     Beitrag um eine Stunde verschieben. Der zweite Anlauf kostet im seltenen
     Fall etwa so viel wie der erste. */
  const ohneSchema = () => { const { thinking, output_config, ...rest } = basis; return { ...rest, messages: [{ role: "user", content: `${user}\n\nAntworte ausschließlich mit einem JSON-Objekt nach diesem Schema:\n${JSON.stringify(SCHEMA)}` }] }; };
  const auswerten = (response) => {
    if (response.stop_reason === "refusal") throw new Error(`Modell hat die Prüfung abgelehnt (${response.stop_details?.explanation || "ohne Begründung"})`);
    const text = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
    let d;
    try { d = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1)); }
    catch (e) { throw new Error(`keine lesbare JSON-Antwort (${e.message.slice(0, 80)})`); }
    if (!Array.isArray(d?.befunde)) throw new Error("Antwort ohne Befundliste");
    return d;
  };
  let daten, ersterFehler = null;
  for (const [nr, anfrage] of [[1, () => basis], [2, ohneSchema]]) {
    let response;
    try {
      response = await client().messages.create(anfrage());
    } catch (e) {
      if (!(e instanceof Anthropic.BadRequestError) || nr === 2) throw e;
      /* Schema oder Denken nicht erlaubt: direkt zum zweiten Weg. */
      continue;
    }
    erfassen(modell, response.usage, zweck);
    try { daten = auswerten(response); break; }
    catch (e) {
      ersterFehler ||= e;
      if (nr === 2) throw new Error(`Faktencheck nicht auswertbar: ${ersterFehler.message}; zweiter Anlauf: ${e.message}`);
      console.warn(`  ! Faktencheck-Ergebnis nicht auswertbar (${e.message.slice(0, 80)}) – zweiter Anlauf ohne Schema.`);
    }
  }
  const { fehler: gefunden, korrekturen, weich, brauchbar } = befundeSortieren(daten.befunde);
  let bestaetigt = gefunden;
  let verworfen = [];
  if (bestaetigt.length && CONFIG.faktencheck.zweitmeinung) {
    try {
      const urteile = await zweitmeinung(textAus(beitrag), bestaetigt, zweck);
      ({ bestaetigt, verworfen } = urteileAnwenden(bestaetigt, urteile));
      if (verworfen.length) console.log(`  Zweitmeinung: ${verworfen.length} von ${verworfen.length + bestaetigt.length} Einwänden nicht bestätigt – ${verworfen.map((b) => `„${b.stelle}“`).join(", ")}`);
    } catch (e) {
      /* Die Zweitmeinung ist eine Zusatzrunde, kein Pflichtteil. Reicht das
         Budget dafür nicht, gelten die Einwände - der Aufruf darf daran
         nicht sterben. Am 16.09. riss genau dieses `throw` neun bereits
         geschriebene und bezahlte Story-Texte mit sich: Der Prüfer war
         fertig, nur die Zweitmeinung war zu teuer, und weil der Fehler
         nach oben durchschlug, kam aus `storiesSchreiben` nichts zurück. */
      if (e instanceof BudgetFehler) console.warn(`  ! ${e.message.split("\n")[0]} – Einwände gelten ohne Zweitmeinung.`);
      else console.warn(`  ! Zweitmeinung nicht möglich (${e.message.split("\n")[0].slice(0, 120)}) – Einwände gelten.`);
    }
  }
  const behebbar = bestaetigt.filter(brauchbar).map((b) => ({ original: b.original, ersatz: b.ersatz }));
  const fehler = bestaetigt.map((b) => `${b.stelle}: ${b.problem} → ${b.korrektur}`);
  const hinweise = [...weich.map((b) => `${b.stelle}: ${b.problem}`), ...verworfen.map((b) => `${b.stelle}: ${b.problem} (Zweitmeinung: kein Fehler)`)];
  if (korrekturen.length) console.log(`  Sprachkorrekturen: ${korrekturen.map((k) => `„${k.original}“ → „${k.ersatz}“`).join(" · ")}`);
  return { ok: fehler.length === 0, fehler, hinweise, korrekturen, behebbar };
}

/* Welche Einwände nach der Zweitmeinung bestehen bleiben. Fehlt ein Urteil
   zu einem Einwand, bleibt er bestehen – im Zweifel gilt der Einwand. */
export function urteileAnwenden(befunde, urteile = []) {
  const bestaetigt = [], verworfen = [];
  befunde.forEach((b, i) => {
    const u = (urteile || []).find((x) => Number(x.nr) === i + 1);
    if (u && u.zutreffend === false) verworfen.push(b); else bestaetigt.push(b);
  });
  return { bestaetigt, verworfen };
}

const SCHIEDS_SCHEMA = {
  type: "object",
  properties: {
    urteile: {
      type: "array",
      items: {
        type: "object",
        properties: { nr: { type: "integer" }, zutreffend: { type: "boolean" }, begruendung: { type: "string" } },
        required: ["nr", "zutreffend", "begruendung"],
      },
    },
  },
  required: ["urteile"],
};

const SCHIEDS_SYSTEM = `Du bist Schiedsrichter:in zwischen einem juristischen Fachtext und den Einwänden eines Prüfers (deutsches Recht, Rechtsstand 2026). Du bekommst den Text und nummerierte Einwände. Beurteile JEDEN Einwand einzeln und unabhängig:
- zutreffend = true: Der Text ist an dieser Stelle wirklich falsch – falsche Norm, falscher Absatz, falsche Rechtsfolge, falsche Zuordnung, aufgehobenes Recht. In der Klausur gäbe es dafür Abzug.
- zutreffend = false: Der Text ist korrekt oder vertretbar, und der Einwand irrt – etwa weil der Prüfer eine Norm falsch versteht, eine vertretbare Ansicht als Fehler wertet, eine Vereinfachung rügt, die für das Format zulässig ist, oder Stil und Didaktik kritisiert.
Prüfe die Norm selbst nach, bevor du urteilst; wiederhole nicht den Einwand. Bist du unsicher, ob der Text falsch ist, ist der Einwand NICHT zutreffend – nur ein klar belegter Fehler zählt. Begründung in höchstens zwei Sätzen.`;

async function zweitmeinung(text, befunde, zweck = "faktencheck") {
  budgetPruefen({ "reel-faktencheck": "Reel-Faktencheck (Zweitmeinung)", "story-faktencheck": "Story-Faktencheck (Zweitmeinung)" }[zweck] || "Faktencheck (Zweitmeinung)");
  const modell = CONFIG.faktencheck.zweitmeinungModell || CONFIG.ki.modell;
  const user = `Text:\n\n${text}\n\nEinwände des Prüfers:\n${befunde.map((b, i) => `${i + 1}. [${b.stelle}] ${b.problem} → ${b.korrektur}`).join("\n")}\n\nBeurteile jeden Einwand.`;
  const basis = {
    model: modell,
    max_tokens: 4000,
    system: [{ type: "text", text: SCHIEDS_SYSTEM, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: user }],
    thinking: { type: "adaptive" },
    output_config: { effort: "high", format: { type: "json_schema", schema: SCHIEDS_SCHEMA } },
  };
  let response;
  try {
    response = await client().messages.create(basis);
  } catch (e) {
    if (!(e instanceof Anthropic.BadRequestError)) throw e;
    const { thinking, output_config, ...rest } = basis;
    response = await client().messages.create({ ...rest, messages: [{ role: "user", content: `${user}\n\nAntworte ausschließlich mit einem JSON-Objekt nach diesem Schema:\n${JSON.stringify(SCHIEDS_SCHEMA)}` }] });
  }
  erfassen(modell, response.usage, zweck);
  const antwort = response.content.filter((b) => b.type === "text").map((b) => b.text).join("");
  const daten = JSON.parse(antwort.slice(antwort.indexOf("{"), antwort.lastIndexOf("}") + 1));
  for (const u of daten.urteile || []) if (u.zutreffend === false) console.log(`    Einwand ${u.nr} verworfen: ${String(u.begruendung || "").slice(0, 160)}`);
  return daten.urteile || [];
}
