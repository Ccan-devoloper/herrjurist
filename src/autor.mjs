/* ==========================================================================
   Autor: schreibt Beiträge und Stories mit der Claude API.

   Eingabe: ein Themen-Skelett aus inhalte.mjs (Titel, Normen, Prüfgedanken)
   Ausgabe: fertiger Beitrag (Folien, Caption, Hashtags) bzw. Stories – als
   strukturiertes JSON, das render.mjs direkt versteht.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import Anthropic from "@anthropic-ai/sdk";
import { CONFIG } from "./config.mjs";
import { FAECHER, KLAUSUREN } from "./inhalte.mjs";
import { ICONS } from "./stile.mjs";
import { folieLeer, pruefeBeitrag, korpus } from "./pruefung.mjs";
import { datumLesbar, tageBis } from "./zeit.mjs";
import { erfassen, budgetPruefen, BudgetFehler } from "./kosten.mjs";
import { pruefeFakten, korrekturenAnwenden } from "./faktencheck.mjs";
import { hookWaehlen as hookMusterWaehlen, hookAnleitung, pruefeHook, hookTypErkennen } from "./hooks.mjs";
import { dauerWaehlen } from "./insights.mjs";
import { normKurz, normGesprochen, felderKuerzen, NORM_REGEL, NORM_REGEL_STIMME } from "./normen.mjs";
import { hookTyp } from "./insights.mjs";
import { phase } from "./kalender.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const beispiele = JSON.parse(fs.readFileSync(path.resolve(hier, "../beispiele/inhalte.json"), "utf8"));
const beispielReel = JSON.parse(fs.readFileSync(path.resolve(hier, "../beispiele/reel.json"), "utf8"));

let clientCache = null;
function client() {
  if (!clientCache) clientCache = new Anthropic({ maxRetries: 3, timeout: 10 * 60 * 1000 });
  return clientCache;
}

/* Beitragsformate – was der Autor je Format bauen soll. */
export const FORMATE = {
  pruefungsfrage: {
    label: "Prüfungsfrage",
    anleitung: "Folie 1: eine echte Prüfungsfrage als Aufhänger (so, wie sie in der Klausur oder mündlichen Prüfung fallen könnte). Folien 2–4: die Antwort in klaren Schritten oder Punkten mit den tragenden Normen. Vorletzte Folie: Merksatz. Letzte Folie: CTA.",
    folien: ["titel", "text|schritte", "text|vergleich", "merke", "cta"],
  },
  fehlerfalle: {
    label: "Fehlerfalle",
    anleitung: "Folie 1: die Falle als Frage oder Warnung. Folie 2: Vergleich „Richtig“ (links) vs. „Klassischer Fehler“ (rechts). Folie 3: die Begründung mit Norm. Letzte Folie: CTA.",
    folien: ["titel", "vergleich", "text", "cta"],
  },
  schema: {
    label: "Prüfschema",
    anleitung: "Folie 1: „Wie prüfe ich …?“. Folie 2 (und ggf. 3): das Schema als nummerierte Schritte, je Schritt ein Titel und ein knapper Hinweis, ggf. Norm. Folie danach: worauf Korrektoren achten (Punkte). Letzte Folie: CTA. Das Schema muss eigenständig strukturiert sein – nicht die Gliederung eines Lehrbuchs oder Skripts abbilden.",
    folien: ["titel", "schritte", "schritte|text", "merke", "cta"],
  },
  rechenweg: {
    label: "Rechenweg",
    anleitung: "Folie 1: die Frage, die der Rechenweg beantwortet. Folie 2: Rechnung mit Formel, einem eigenen Zahlenbeispiel (runde, frei gewählte Zahlen) und Ergebnissatz. Folie 3: die Logik dahinter in Punkten. Letzte Folie: CTA.",
    folien: ["titel", "rechnung", "text", "cta"],
  },
  minifall: {
    label: "Mini-Fall",
    anleitung: "Folie 1: die Frage, die der Fall aufwirft (Aufhänger, gern mit der Kernzahl). Folie 2 (art text, Titel „Sachverhalt“): der frei erfundene Fall in 2–4 Sätzen – eigene Namen, eigene Zahlen, alles, was die Lösung später braucht, steht hier. Folie 3: die Lösung in Schritten. Folie 4: Ergebnis und Buchung/Gewinnauswirkung bzw. Rechtsfolge als Punkte oder Rechnung. Vorletzte Folie: Merksatz. Letzte Folie: CTA.",
    folien: ["titel", "text", "schritte", "text|rechnung", "merke", "cta"],
  },
  vergleich: {
    label: "Gegenüberstellung",
    anleitung: "Folie 1: „Was ist der Unterschied zwischen A und B?“. Folie 2: Vergleich in zwei Spalten. Folie 3: Wann welche Seite greift, mit Norm. Vorletzte Folie: Merksatz. Letzte Folie: CTA.",
    folien: ["titel", "vergleich", "text", "merke", "cta"],
  },
  streitstand: {
    label: "Streitstand",
    anleitung: "Folie 1: die Streitfrage als Frage („Wie ist das Verhältnis von A zu B?“). Folie 2: der Sachverhalt in zwei Sätzen, an dem der Streit sichtbar wird. Folie 3: die Ansichten gegenübergestellt – links die Rechtsprechung, rechts die Gegenansicht, je mit dem tragenden Argument. Folie 4: der Streitentscheid – welche Ansicht überzeugt und warum, oder wann der Streit dahinstehen kann. Vorletzte Folie: Merksatz. Letzte Folie: CTA. Wichtig: Keine Ansicht als „falsch“ abtun; in der Klausur zählt die saubere Auseinandersetzung.",
    folien: ["titel", "text", "vergleich", "text", "merke", "cta"],
  },
  klausurtechnik: {
    label: "Klausurtechnik",
    anleitung: "Folie 1: eine Frage zur Klausurstrategie (Zeit, Aufbau, Darstellung, Punktevergabe). Folien 2–3: konkrete, umsetzbare Tipps als Punkte oder Schritte. Vorletzte Folie: Merksatz. Letzte Folie: CTA.",
    folien: ["titel", "schritte", "text", "merke", "cta"],
  },
  wochenrueckblick: {
    label: "Wochenrückblick",
    anleitung: "Folie 1: „Hast du diese Woche alles mitgenommen?“. Folien 2–3: die Themen der Woche als Kurz-Wiederholung in Punkten (je ein Satz pro Thema, mit Norm). Folie 4: Lernplan-Tipp fürs Wochenende. Letzte Folie: CTA.",
    folien: ["titel", "text", "text", "merke", "cta"],
  },
  spickzettel: {
    label: "Spickzettel",
    anleitung: "Folie 1: „Das ganze Schema auf einer Karte“ als Frage/Versprechen. Folie 2 (art karte): der komplette Prüfungsaufbau als dichte, nummerierte Karte – 5–8 Schritte mit je maximal 8 Wörtern und Norm. Folie 3: die zwei Stellen, an denen die meisten Punkte verloren gehen (Punkte). Vorletzte Folie: Merksatz. Letzte Folie: CTA. Diese Karte muss so gut sein, dass man sie speichert.",
    folien: ["titel", "karte", "text", "merke", "cta"],
  },
  anlass: {
    label: "Anlass",
    anleitung: "Ein Beitrag zu einem Termin im Prüfungsjahr (Countdown, Anmeldeschluss, Prüfungstag, Tag danach). Folie 1: der Anlass als Schlagzeile mit Zahl oder Datum. Folien 2–3: was jetzt konkret zu tun ist (Schritte oder Punkte), fachlich unterlegt mit einem passenden Kernthema. Vorletzte Folie: Merksatz/Ermutigung. Letzte Folie: CTA. Ton: nah dran, ermutigend, ohne Kitsch.",
    folien: ["titel", "schritte", "text", "merke", "cta"],
  },
  loesungsskizze: {
    label: "Lösungsskizze",
    anleitung: "Der reichweitenstärkste Beitrag des Jahres: die Lösungsskizze zu den heute berichteten Klausurthemen. Folie 1: „Tag N heute: Das waren die Themen (nach ersten Berichten)“ als Aufhänger. Folie 2 (text): welche Themen Kandidat:innen berichten – als Punkte, ehrlich mit Unsicherheit („mehrfach berichtet“, „einzelne Berichte“). Folien 3–4 (schritte): je berichtetem Thema der Lösungsweg in Stichworten mit Normen – Prüfungsaufbau, Rechtsfolge, typische Punkte. Folie 5 (text): „Vorläufig: beruht auf Berichten von Kandidat:innen, keine offizielle Lösung; die Hinweise der Kammer kommen erst Monate später.“ Letzte Folie: CTA „Was war bei dir dran? Schreib es in die Kommentare – ich ergänze die Skizze“ plus „Schick das deiner Lerngruppe“. Ton: ruhig, hilfreich, nichts Wertendes über Schwierigkeit. Wenn die Recherche keine belastbaren Berichte liefert: die typischen Dauerbrenner dieses Prüfungstags als „Was erfahrungsgemäß drankommt“ skizzieren und das klar sagen.",
    folien: ["titel", "text", "schritte", "schritte", "text", "cta"],
  },
  aktuell: {
    label: "Aktuell",
    anleitung: "Folie 1: die Neuigkeit als Frage oder Schlagzeile (Gesetzesänderung, Entscheidung von BGH, BVerfG, BVerwG oder EuGH, Prüfungstermine, Statistik). Folie 2: was genau passiert ist, in Punkten mit Datum/Aktenzeichen. Folie 3: was das fürs Examen bedeutet. Letzte Folie: CTA. Die Quelle wird in der Caption genannt (Gericht/Behörde, Datum, Aktenzeichen oder Dokumentname).",
    folien: ["titel", "text", "text", "cta"],
  },
};

const KANAL = CONFIG.marke.name ? `des Instagram-Kanals „${CONFIG.marke.name}“` : "eines Instagram-Kanals";
const SYSTEM = `Du bist Redakteur:in ${KANAL} für Menschen, die sich auf das erste oder zweite juristische Staatsexamen vorbereiten (Pflichtfachstoff: Zivilrecht, Strafrecht, Öffentliches Recht, jeweils mit Prozessrecht und europarechtlichen Bezügen; im zweiten Examen dazu die praktische Seite – Urteil, Bescheid, Anwaltsschriftsatz, Aktenvortrag). Der Aufbau ist immer gleich: eine präzise Prüfungsfrage als Aufhänger, dann eine klare, klausurnahe Antwort zum Durchswipen.

## Ton
- Direkt, fachlich präzise, kein Marketing-Sprech, kein Pathos. Du-Ansprache.
- Jede Aussage muss juristisch korrekt sein (Rechtsstand 2026). Normen immer zitieren. ${NORM_REGEL} Wenn du dir bei einem Detail nicht sicher bist, lass es weg, statt zu raten.
- Kurze Sätze. Auf einer Kachel wird gelesen, nicht studiert.
- Keine Emojis auf den Folien. In der Caption höchstens 3.

## Wie das Examen wirklich abläuft (häufige Fehlgriffe)
- Es gibt KEINE feste Reihenfolge der Klausuren. Welches Rechtsgebiet an welchem Tag drankommt, entscheidet jedes Land und jeder Durchgang neu. Verboten sind deshalb Formulierungen wie „in der zweiten Klausurenrunde“, „am zweiten Prüfungstag“, „die dritte Klausur“ oder „traditionell kommt X zuerst“. Schreib stattdessen „in den Zivilrechtsklausuren“, „ein Dauerbrenner im Öffentlichen Recht“, „kommt regelmäßig dran“.
- Es gibt KEINE festen Punktzahlen je Prüfungspunkt. Bewertet wird die Klausur als Ganzes (0 bis 18 Notenpunkte), nicht Position für Position wie in einer Steuerberaterklausur. Verboten sind deshalb „hier verlierst du die meisten Punkte“, „das bringt 5 Punkte“, „Punkteverteilung“, „Textziffer“. Schreib stattdessen, was der Fehler tatsächlich anrichtet: „hier kippt die ganze Anspruchsgrundlage“, „damit ist der Aufbau hin“, „das lesen Korrektoren als Verständnisfehler“.
- Notenpunkte als Ergebnis einer Klausur zu nennen („eine Neun“, „Prädikat ab 9 Punkten“) ist in Ordnung – gemeint ist nur die Punktzahl je Prüfungsschritt, die es nicht gibt.
- Keine Rechenwege, keine Buchungssätze, keine Steuerfächer. Das ist ein Kanal zum juristischen Staatsexamen.

## Eigenständigkeit (sehr wichtig)
- Du bekommst ein Themen-Skelett (Frage, Normen, Stichpunkte). Formuliere ALLES neu, in eigenen Worten und eigener Struktur. Übernimm keine Sätze, keine Aufzählungsreihenfolgen, keine Beispielzahlen.
- Fälle, Beispiele, Namen und Zahlen erfindest du selbst (z. B. „A verkauft B einen Gebrauchtwagen“, „die Nordlicht GmbH“). Verwende nie Namen aus der Sperrliste.
- Keine Bezüge auf Kurse, Skripte, Seiten, Folien, Fallnummern, Dozenten oder Lernplattformen.

## Marke und Aufforderung (CTA)
- Markenkern: „Examenswissen, sortiert nach Rechtsgebiet“. Jeder Beitrag gehört zu genau einem Gebiet (Zivilrecht, Strafrecht, Öffentliches Recht) und trägt dessen Farbe. Zielgruppe sind Kandidatinnen und Kandidaten im ersten und zweiten juristischen Staatsexamen – schreibe auf diesem Niveau: Streitstände benennen, herrschende Meinung und Gegenansicht sauber trennen, den Streitentscheid nicht auslassen.
- Normen sind das Rückgrat: Jede Aussage, die eine Norm hat, nennt sie. Bei Streitständen die Fundstelle der Argumentation (Wortlaut, Systematik, Sinn und Zweck, Historie) statt bloßer Behauptung.
- Kein Halbwissen und keine Vereinfachung, die in der Klausur Punkte kostet: Lieber eine Frage weniger beantworten als eine falsch.
- Landesrecht kennzeichnen: Polizei- und Ordnungsrecht, Kommunalrecht, Bauordnungsrecht und Verwaltungsvollstreckung sind je Bundesland anders geregelt. Bei solchen Themen gehört ein Hinweis auf die Folie oder in die Caption („je nach Land unterschiedlich – prüf dein Landesrecht“), und es wird kein Landesparagraf als bundesweit gültig ausgegeben.
- Methodik-Beiträge (Fach „Klausur- und Lernmethodik“) erklären die Methode an EINEM konkreten Beispiel aus einem Rechtsgebiet. Ein abstrakter Ratschlag ohne Beispiel ist wertlos – den kann jeder geben.
- Der wichtigste Wachstumsmotor sind Lerngruppen (WhatsApp, Telegram): Jeder Beitrag ist so gebaut, dass man ihn weiterleitet. Haupt-CTA daher immer „Schick das deiner Lerngruppe“ (oder gleichwertig), zweitens „Speichern“, drittens „Folgen“. Nie nur „Speicher dir das“.
- Nähe statt Konzern: Fragen in den Kommentaren werden beantwortet, DM ist erlaubt („Schreib mir, wenn etwas unklar ist“). Keine Verkaufsbotschaft, kein Kurs, kein Produkt – jetzt zählen Reichweite, Saves und Weiterleitungen.

## Innere Logik (sehr wichtig)
- Der Beitrag muss aus sich heraus verständlich sein: Jede Zahl, jeder Name, jeder Fall, auf den Titel, Rechnung oder Lösung Bezug nehmen, wird vorher auf einer eigenen Folie eingeführt (z. B. Folie „Sachverhalt“). Nie auf etwas verweisen, das nicht auf den Folien steht.
- Jede Folie außer der CTA hat einen Titel UND Inhalt (Text, Punkte, Schritte, Rechnung). Nie eine leere Folie, nie nur eine Überschrift.
- Genau eine CTA-Folie, und zwar als letzte. Folie 1 ist die einzige Titelfolie.

## Form
- Folienarten: titel (Frage/Aufhänger), text (Titel + Text oder Punkte), schritte (nummeriert, je Schritt titel + text), vergleich (links/rechts mit titel + punkte), rechnung (formel, zeilen, ergebnis), karte (dichter Spickzettel: schritte mit kurzem titel + norm im text), merke (ein Satz, der hängen bleibt), cta (Abschluss mit Folgen-Aufforderung).
- hooks: drei alternative Titel für Folie 1 in unterschiedlichen Typen – eine Frage, ein Fehler-/Falle-Hook („Der Fehler, der … kostet“), ein Zahlen-Hook (Frist, Prozentsatz, Betrag). Folie 1 trägt den besten davon.
- Die erste Zeile der Caption ist gleichzeitig Suchtext: Sie nennt das Thema mit den Wörtern, die jemand bei Instagram oder Google eintippen würde (z. B. „Annahmeverzug Voraussetzungen Rechtsfolgen“), natürlich eingebettet in den Hook.
- Folie-1-Titel: eine Frage, ideal 45–80 Zeichen, maximal 100. Andere Titel maximal 60 Zeichen.
- Je Folie maximal 5 Punkte / 5 Schritte, insgesamt maximal 380 Zeichen Text je Folie; bei „vergleich“ je Spalte maximal 3 Punkte à 60 Zeichen.
- Kernaussagen und Merksätze aus dem Skelett NIE übernehmen, auch nicht leicht umgestellt – schreibe einen eigenen Merksatz mit anderem Satzbau und anderen Wörtern.
- Hervorhebungen mit *Sternchen* um das Wort – sparsam, ein bis zwei je Folie.
- icon: genau einer aus: ${Object.keys(ICONS).join(", ")}. Nimm das konkreteste Zeichen zum Thema – das, was in der Geschichte des Falls vorkommt: Tötungsdelikt → messer oder polizei, Kaufvertrag → handschlag oder einkaufswagen, Mietrecht → haus oder schluessel, Erbrecht → schriftrolle, Verkehrsunfall → auto, Kündigung → umschlag, Insolvenz → geld-weg. Die allgemeinen Zeichen (waage, paragraf, buch, dokument) sind nur Rückfall, wenn wirklich nichts Konkretes passt.
- Caption: 4–8 Zeilen. Zeile 1 ist der Hook (die Frage oder die Pointe), dann die Kernantwort in 2–4 Sätzen, dann die Aufforderung, den Beitrag an die Lerngruppe weiterzuleiten und zu speichern, plus eine echte Frage an die Leser:innen, die eine Antwort im Kommentar provoziert. ${CONFIG.marke.website ? `Am Ende darf ein Hinweis „Mehr auf ${CONFIG.marke.website} (Link in Bio)“ stehen.` : "Keine Website, keine Plattform, kein Produkt erwähnen – auch nicht „Link in Bio“."} Keine Hashtags in der Caption; die kommen separat.
- Hashtags: 8–14 Stück, deutsch, kleingeschrieben, spezifisch zum Thema plus diese Kernhashtags: ${CONFIG.hashtags.kern.join(" ")}.
- kurztitel: 3–6 Wörter für die Story-Ankündigung.
- bildSzene: eine ENGLISCHE Beschreibung einer konkreten, fotografierbaren Alltagsszene für das Titelbild – 3 bis 6 Wörter, so, wie man sie in einer Fotodatenbank suchen würde. Sie muss die Rechtsfrage bildlich greifbar machen, nicht sie beschriften: für den Annahmeverzug „delivery man waiting at door“, für das Mietrecht „damp stain on apartment wall“, für den Betrug „person signing contract nervously“. Verboten sind juristische Vokabeln („annahmeverzug“, „liability“), abstrakte Begriffe („justice“, „law“) und die Symbolbild-Klassiker: Richterhammer, Waage, Paragrafenzeichen, Gesetzbuch, Gerichtsgebäude, Anzugträger beim Händedruck – die sagen nichts und stehen unter jedem zweiten Jura-Beitrag. Das Foto wird freigestellt (Hintergrund weg) und als Motiv auf die Kachel gesetzt – wähle deshalb Szenen mit EINEM klaren Motiv im Vordergrund (eine Person vom Kopf bis zur Hüfte, ein Gegenstand mit Rand ringsum), keine Gruppen, keine Nahaufnahmen, keine Bewegungsunschärfe, nichts, das am Bildrand abgeschnitten wäre. Fällt dir keine echte Szene ein, gib null zurück; dann bleibt es beim Icon.
- bildSzeneAlt: eine zweite, andere Szene zum selben Thema nach denselben Regeln – sie wird gesucht, wenn die erste kein brauchbares Foto liefert. Sonst null.

## Beispiel eines fertigen Beitrags (Format Streitstand)
${JSON.stringify({ folien: beispiele.beitraege[0].folien, caption: beispiele.beitraege[0].caption, hashtags: beispiele.beitraege[0].hashtags, kurztitel: "Mord und Totschlag: das Verhältnis" }, null, 1)}

## Beispiel eines fertigen Beitrags (Format Fehlerfalle)
${JSON.stringify({ folien: beispiele.beitraege[1].folien, caption: beispiele.beitraege[1].caption, hashtags: beispiele.beitraege[1].hashtags, kurztitel: "§ 123 oder § 80 Abs. 5 VwGO?" }, null, 1)}

## Beispiel eines fertigen Beitrags (Format Vergleich)
${JSON.stringify({ folien: beispiele.beitraege[2].folien, caption: beispiele.beitraege[2].caption, hashtags: beispiele.beitraege[2].hashtags, kurztitel: "Schuldner- oder Gläubigerverzug?" }, null, 1)}

## Beispiel-Stories (Ton und Länge)
${JSON.stringify(beispiele.stories, null, 1)}

## Beispiel eines Reel-Skripts (Ton fürs Sprechen)
${JSON.stringify(beispielReel.szenen, null, 1)}
`;

const FOLIE_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    art: { type: "string", enum: ["titel", "text", "schritte", "vergleich", "rechnung", "karte", "merke", "cta"] },
    titel: { type: ["string", "null"] },
    untertitel: { type: ["string", "null"] },
    text: { type: ["string", "null"] },
    punkte: { type: ["array", "null"], items: { type: "string" } },
    schritte: { type: ["array", "null"], items: { type: "object", additionalProperties: false, properties: { titel: { type: "string" }, text: { type: ["string", "null"] } }, required: ["titel", "text"] } },
    links: { type: ["object", "null"], additionalProperties: false, properties: { titel: { type: "string" }, punkte: { type: "array", items: { type: "string" } } }, required: ["titel", "punkte"] },
    rechts: { type: ["object", "null"], additionalProperties: false, properties: { titel: { type: "string" }, punkte: { type: "array", items: { type: "string" } } }, required: ["titel", "punkte"] },
    formel: { type: ["string", "null"] },
    zeilen: { type: ["array", "null"], items: { type: "string" } },
    ergebnis: { type: ["string", "null"] },
    icon: { type: ["string", "null"] },
  },
  required: ["art", "titel", "untertitel", "text", "punkte", "schritte", "links", "rechts", "formel", "zeilen", "ergebnis", "icon"],
};

const BEITRAG_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    folien: { type: "array", items: FOLIE_SCHEMA },
    caption: { type: "string" },
    hashtags: { type: "array", items: { type: "string" } },
    kurztitel: { type: "string" },
    bildSzene: { type: ["string", "null"] },
    bildSzeneAlt: { type: ["string", "null"] },
    quellen: { type: ["array", "null"], items: { type: "string" } },
    hooks: { type: ["array", "null"], items: { type: "object", additionalProperties: false, properties: { typ: { type: "string", enum: ["frage", "fehler", "zahl", "aussage"] }, titel: { type: "string" } }, required: ["typ", "titel"] } },
  },
  required: ["folien", "caption", "hashtags", "kurztitel", "bildSzene", "bildSzeneAlt", "quellen", "hooks"],
};

const STORY_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    stories: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        properties: {
          slot: { type: "string" },
          art: { type: "string", enum: ["frage", "antwort", "norm", "merksatz", "formel", "begriff", "fehler", "tipp", "zahl"] },
          ueberzeile: { type: ["string", "null"] },
          titel: { type: ["string", "null"] },
          text: { type: ["string", "null"] },
          norm: { type: ["string", "null"] },
          formel: { type: ["string", "null"] },
          zahl: { type: ["string", "null"] },
          optionen: { type: ["array", "null"], items: { type: "string" } },
          richtig: { type: ["integer", "null"] },
          falsch: { type: ["string", "null"] },
          richtigText: { type: ["string", "null"] },
          icon: { type: ["string", "null"] },
          bildSzene: { type: ["string", "null"] },
        },
        required: ["slot", "art", "ueberzeile", "titel", "text", "norm", "formel", "zahl", "optionen", "richtig", "falsch", "richtigText", "icon", "bildSzene"],
      },
    },
  },
  required: ["stories"],
};

function textAus(response) {
  return response.content.filter((b) => b.type === "text").map((b) => b.text).join("\n");
}

function jsonAus(text) {
  const start = text.indexOf("{");
  const ende = text.lastIndexOf("}");
  if (start < 0 || ende < 0) throw new Error("Keine JSON-Antwort erhalten");
  return JSON.parse(text.slice(start, ende + 1));
}

/* Ein strukturierter Aufruf. Fällt bei Ablehnung oder Schema-Problemen auf
   einen zweiten Weg zurück, damit der Tageslauf nicht stehen bleibt. */
async function strukturiert({ system, user, schema, modell = CONFIG.ki.modell, effort = CONFIG.ki.effort, zweck = "autor" }) {
  const basis = {
    model: modell,
    max_tokens: 16000,
    system: [{ type: "text", text: system, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: user }],
    thinking: { type: "adaptive" },
    output_config: { effort, format: { type: "json_schema", schema } },
  };
  budgetPruefen(zweck === "reel" ? "Reel-Skript schreiben" : "Text schreiben");
  let response;
  try {
    response = await client().messages.create(basis);
  } catch (e) {
    if (e instanceof Anthropic.BadRequestError && /output_config|schema|format/i.test(e.message)) {
      const { output_config, ...ohneFormat } = basis;
      response = await client().messages.create({ ...ohneFormat, output_config: { effort }, messages: [{ role: "user", content: `${user}\n\nAntworte ausschließlich mit einem JSON-Objekt nach diesem Schema:\n${JSON.stringify(schema)}` }] });
    } else throw e;
  }
  erfassen(modell, response.usage, zweck);
  if (response.stop_reason === "refusal") {
    if (modell !== "claude-opus-4-8") return strukturiert({ system, user, schema, modell: "claude-opus-4-8", effort, zweck });
    throw new Error(`Modell hat abgelehnt: ${response.stop_details?.explanation || "ohne Begründung"}`);
  }
  if (response.stop_reason === "max_tokens") throw new Error("Antwort abgeschnitten (max_tokens)");
  return { daten: jsonAus(textAus(response)), usage: response.usage };
}

/* Hashtags: Vorschläge des Modells + Kern-Hashtags, sortiert nach gelerntem
   Gewicht (welche Tags Follower und Reichweite brachten), dazu zwei täglich
   rotierende Entdecker-Tags. Höchstens maxJeBeitrag. */
/* Gebiets-Hashtags gehören zum Beitrag, nicht in die Rotation: Ein Beitrag zum
   Schuldrecht mit #öffentlichesrecht ist schlicht falsch ausgezeichnet – er
   landet bei Leuten, die etwas anderes suchen, und wirkt unsauber. */
const GEBIET_TAGS = { 1: "#zivilrecht", 2: "#strafrecht", 3: "#öffentlichesrecht" };
/* Auch Fach-Hashtags gehoeren zu genau einem Gebiet. Ohne diese Liste rutschte
   ueber die taeglich rotierenden Entdecker-Tags ein #staatsrecht unter einen
   Zivilrechtsbeitrag - fuer die Leute, die dem Tag folgen, ein Fehlgriff, und
   fuer die Lernschleife ein verfaelschter Messwert. */
const FACH_TAGS = {
  1: ["#zivilrecht", "#bgbat", "#schuldrecht", "#sachenrecht", "#zpo", "#familienrecht", "#erbrecht", "#handelsrecht", "#arbeitsrecht"],
  2: ["#strafrecht", "#stpo", "#strafprozessrecht"],
  3: ["#öffentlichesrecht", "#verwaltungsrecht", "#staatsrecht", "#grundrechte", "#verfassungsrecht", "#europarecht", "#vwgo"],
};
const ALLE_GEBIET_TAGS = Object.values(FACH_TAGS).flat();

export function hashtagsWaehlen(vorschlaege, kern, strategie = null, tag = Math.floor(Date.now() / 86400000), klausur = null) {
  const norm = (h) => (h.startsWith("#") ? h : `#${h}`).toLowerCase().replace(/\s+/g, "");
  const g = strategie?.hashtagGewicht || {};
  const passt = (h) => !klausur || !ALLE_GEBIET_TAGS.includes(h) || (FACH_TAGS[klausur] || []).includes(h);
  const eigene = [...new Set(vorschlaege.map(norm))].filter((h) => !kern.includes(h) && passt(h)).sort((a, b) => (g[b] ?? 1) - (g[a] ?? 1));
  const entdecker = (CONFIG.hashtags.entdecker || []).filter(passt);
  const neu = entdecker.length ? [entdecker[tag % entdecker.length], entdecker[(tag * 7 + 3) % entdecker.length]] : [];
  /* Das eigene Gebiet steht immer dabei. */
  if (klausur && GEBIET_TAGS[klausur]) neu.unshift(GEBIET_TAGS[klausur]);
  const max = CONFIG.hashtags.maxJeBeitrag;
  const liste = [...kern, ...neu];
  for (const h of eigene) if (liste.length < max && !liste.includes(h)) liste.push(h);
  return [...new Set(liste)].slice(0, max);
}

/* Faktencheck, der einen fertigen Entwurf nie verwirft: Fällt der Prüfaufruf
   selbst aus (Modellfehler, Budget), gilt der Entwurf mit Hinweis als geprüft. */
/**
 * Faktencheck mit klarer Haltung zum Ausfall.
 *
 * Streng (Standard): Lässt sich nicht prüfen, erscheint nichts. Bei
 * juristischen Inhalten ist ein ungeprüfter Beitrag teurer als ein fehlender –
 * einen falsch dargestellten Streitstand liest genau die Zielgruppe, die ihn
 * gerade lernt, und der Fehler bleibt im Feed stehen.
 *
 * Das Tagesbudget ist davon ausgenommen: Ein BudgetFehler heißt „später
 * weiter“, nicht „durchwinken“ – er wandert nach oben, wo der Lauf ihn kennt.
 */
async function faktenSicher(inhalt, zweck = "faktencheck", opt = {}) {
  try {
    return await pruefeFakten(inhalt, zweck, opt);
  } catch (e) {
    if (e instanceof BudgetFehler) throw e;
    if (CONFIG.faktencheck.strikt) {
      throw new Error(`Faktencheck nicht möglich (${e.message.split("\n")[0].slice(0, 160)}) – der Beitrag erscheint nicht.`);
    }
    console.warn(`  ! Faktencheck nicht möglich (${e.message.split("\n")[0].slice(0, 160)}) – Entwurf wird ohne Faktencheck übernommen.`);
    return { ok: true, fehler: [], hinweise: [`Faktencheck ausgefallen: ${e.message.slice(0, 120)}`] };
  }
}

function themaText(thema) {
  /* Ohne Thema (freies Format) gibt es kein Skelett - ein Absturz waere hier
     die teuerste Reaktion: Der Lauf bricht ab, obwohl das Modell auch ohne
     Skelett schreiben kann. */
  if (!thema?.fach) return "";
  /* Methodik-Themen (Klausurtechnik, Mindset) gehören zu keinem einzelnen
     Prüfungstag: ihr Fach trägt klausur 0, und KLAUSUREN kennt nur 1-3.
     Ohne diese Klammer stürzte der Samstags-Reel-Lauf hier ab. */
  const f = FAECHER[thema.fach] || { label: thema.fach, klausur: thema.klausur || 0 };
  /* Der Klausurtag am Fach steht nur bei Fachthemen. Ein Mindset-Thema trägt
     ihn allein für die Farbe der Kachel - im Auftrag an das Modell wäre
     "Klausur- und Lernmethodik (Zivilrecht)" eine falsche Fährte. */
  const klausurLabel = thema.typ === "mindset" ? null : KLAUSUREN[f.klausur]?.label || KLAUSUREN[thema.klausur]?.label || null;
  const k = thema.kern;
  const zeilen = [
    klausurLabel ? `Fach: ${f.label} (${klausurLabel})` : `Fach: ${f.label}`,
    `Thema: ${thema.titel}`,
    `Examenspriorität: ${thema.prioritaet === "hoch" ? "Dauerbrenner (nahezu jährlich geprüft)" : thema.prioritaet === "mittel" ? "regelmäßig geprüft" : "selten geprüft, aber punktestark"}`,
    thema.normen.length ? `Normen: ${thema.normen.join(" · ")}` : "",
    thema.examen && thema.examen !== "1. Examen" ? `Prüfungsbezug: ${thema.examen}${/2\./.test(thema.examen) ? " – im zweiten Examen zählt die praktische Seite: Entscheidungsform, Tenor, Zweckmäßigkeit, Urteils- statt Gutachtenstil." : ""}` : "",
  ];
  if (k.einordnung?.length) zeilen.push(`Einordnung (nur als Gedankenstütze, nicht übernehmen): ${k.einordnung.join(" ")}`);
  if (k.lernziele?.length) zeilen.push(`Worauf es ankommt: ${k.lernziele.join("; ")}`);
  if (k.pruefschritte?.length) zeilen.push(`Prüfgedanken (Reihenfolge und Wortlaut selbst neu aufbauen): ${k.pruefschritte.join(" | ")}`);
  if (k.merksatz) zeilen.push(`Kernaussage: ${k.merksatz}`);
  if (k.fehler?.length) zeilen.push(`Typische Fehler: ${k.fehler.join("; ")}`);
  if (k.frage) zeilen.push(`Frage: ${k.frage}`, `Antwortkern: ${k.antwort || ""}`);
  if (k.optionen) zeilen.push(`Quiz-Optionen: ${k.optionen.join(" / ")} – richtig: ${k.optionen[k.richtig]} – Erklärung: ${k.erklaerung}`);
  if (k.ausdruck) zeilen.push(`Formel: ${k.ausdruck} – ${k.erklaerung}`);
  if (k.begriff) zeilen.push(`Definition: ${k.definition}`);
  if (k.schritte?.length) zeilen.push(`Schema-Gedanken: ${k.schritte.join(" | ")}`);
  /* Wiederholung: Dasselbe Thema darf wiederkommen – aber nie als derselbe
     Beitrag. Wer den Kanal länger verfolgt, muss etwas Neues bekommen, und
     wer damals nichts verstanden hat, einen zweiten Zugang. */
  if (thema.zuletzt) {
    zeilen.push(
      `ACHTUNG, WIEDERHOLUNG: Dieses Thema lief am ${thema.zuletzt.datum} schon einmal – damals als Format „${thema.zuletzt.format}“${thema.zuletzt.hookMuster ? ` mit dem Hook-Muster „${thema.zuletzt.hookMuster}“` : ""}${thema.zuletzt.titel ? `, Titel: „${thema.zuletzt.titel}“` : ""}.`,
      `Verpacke es diesmal komplett anders: anderer Einstieg, anderer Blickwinkel, andere Beispiele, anderer Titel. Wiederhole den alten Titel weder wörtlich noch sinngemäß. Wähle eine andere Seite des Themas – etwa die typische Klausurfalle statt der Definition, den Streitstand statt des Schemas, den Fall statt der Regel.`,
    );
  }
  return zeilen.filter(Boolean).join("\n");
}

/* Pille unter dem Titel und Handschrift-Hinweis daneben: nicht immer dieselben
   Worte. Die Wahl haengt am Thema, damit derselbe Beitrag beim Nachrendern
   gleich aussieht - im Feed wechselt es von Beitrag zu Beitrag. */
const PRIORITAET_TEXTE = {
  hoch: ["Dauerbrenner im Examen", "Kommt fast jedes Jahr dran", "Examensklassiker", "Prüfer:innen lieben das", "Das musst du können"],
  mittel: ["Regelmäßig geprüft", "Kommt immer wieder dran", "Fester Bestandteil im Examen", "Gehört ins Repertoire"],
  selten: ["Seltener, aber punktestark", "Wenn es kommt, zählt es doppelt", "Unterschätzt – und punktestark", "Die Punkte, die andere liegen lassen"],
};
const HINWEISE = ["So geht's!", "Swipe →", "Schau rein", "Merk dir das", "Kurz erklärt", "Das musst du wissen", "Weiter geht's →", "Lies weiter"];
const streuung = (text) => { let h = 7; for (const c of String(text)) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; };
const auswahl = (liste, seed) => liste[streuung(seed) % liste.length];
function prioritaetText(stufe, seed = "") {
  const liste = PRIORITAET_TEXTE[stufe];
  return liste ? auswahl(liste, `${stufe}:${seed}`) : "";
}

/* Nachbearbeitung: leere Felder entfernen, Titelfolie normieren, Hashtags säubern. */
/* Besten Hook wählen: gelernte Gewichte je Hook-Typ, sonst Heuristik (Länge, Frageform). */
function hookWaehlen(daten, strategie) {
  const kandidaten = [...(daten.hooks || [])];
  const erster = daten.folien?.[0]?.titel;
  if (erster && !kandidaten.some((h) => h.titel === erster)) kandidaten.unshift({ typ: hookTyp(erster), titel: erster });
  if (!kandidaten.length) return null;
  const g = strategie?.hookGewicht || {};
  const bewertet = kandidaten.map((h) => {
    const l = h.titel.length;
    let p = (g[h.typ] ?? 1) * 10;
    if (l >= 45 && l <= 80) p += 3; else if (l > 100) p -= 4;
    if (/\d/.test(h.titel)) p += 1;
    if (/\?$/.test(h.titel.trim())) p += 1;
    return { ...h, p };
  }).sort((a, b) => b.p - a.p);
  return bewertet[0];
}

function nachbereiten(daten, { format, thema, fach, klausur, strategie }) {
  const hook = hookWaehlen(daten, strategie);
  if (hook && daten.folien?.[0]) daten.folien[0].titel = hook.titel;
  const folien = (daten.folien || []).map((f) => {
    const o = {};
    for (const [k, v] of Object.entries(f)) if (v != null && !(Array.isArray(v) && v.length === 0)) o[k] = v;
    return o;
  });
  /* Sicherheitsnetz gegen leere Kacheln: Inhaltslose Folien fallen weg, mehrere
     CTA-Folien werden auf die letzte reduziert. Ein Sachverhalt, der auf der
     Titelfolie steckt (dort wird kein Fließtext gezeigt), bekommt eine eigene Folie. */
  if (folien[0]?.text && String(folien[0].text).trim().length >= 40) {
    folien.splice(1, 0, { art: "text", titel: /fall|sachverhalt/i.test(`${format} ${folien[0].untertitel || ""}`) ? "Sachverhalt" : "Worum es geht", text: folien[0].text, icon: folien[0].icon });
    delete folien[0].text;
  }
  for (let i = folien.length - 1; i >= 1; i--) {
    const f = folien[i];
    if (f.art === "titel") f.art = "text";
    if (f.art === "cta" ? folien.slice(i + 1).some((x) => x.art === "cta") : folieLeer(f)) folien.splice(i, 1);
  }
  if (folien[0]) {
    folien[0].art = "titel";
    folien[0].pille = "Swipen →";
    const seed = thema?.id || folien[0].titel || "";
    if (thema?.prioritaet) { folien[0].prioritaet = thema.prioritaet; folien[0].prioritaetText = prioritaetText(thema.prioritaet, seed); }
    if (!folien[0].hinweis) folien[0].hinweis = auswahl(HINWEISE, `hinweis:${seed}`);
    if (!ICONS[folien[0].icon]) folien[0].icon = "paragraf";
  }
  if (folien.at(-1)?.art !== "cta") folien.push({ art: "cta", titel: "Schick das deiner Lerngruppe.", punkte: ["Weiterleiten an die Lerngruppe", "Speichern und vor der Klausur wiederholen", "Folgen: sortiert nach Klausurtag"] });
  /* Normen in der Klausur-Kurzform: § 7 (1) S. 1 Nr. 1 lit. a) aa) EStG. Das
     Modell hält sich meist daran, die Umschreibung sichert den Rest ab. */
  for (const f of folien) felderKuerzen(f, ["titel", "untertitel", "text", "norm", "formel", "richtigText", "falsch"]);
  for (const f of folien) for (const seite of ["links", "rechts"]) if (f[seite]) felderKuerzen(f[seite], ["titel", "text"]);
  for (const f of folien) if (Array.isArray(f.schritte)) f.schritte = f.schritte.map((x) => (typeof x === "string" ? normKurz(x) : felderKuerzen(x, ["titel", "text", "norm"])));
  daten.caption = normKurz(daten.caption || "");
  /* Sicherheitsnetz: keine Website, kein Plattformname auf Folien oder in der Caption. */
  const verboten = /(github\.io|github\.com|examenscampus|link in bio|website)/i;
  for (const f of folien) for (const k of ["titel", "text", "untertitel"]) if (f[k] && verboten.test(f[k])) f[k] = f[k].replace(verboten, "").replace(/\s{2,}/g, " ").trim();
  if (!CONFIG.marke.website) daten.caption = (daten.caption || "").split("\n").filter((z) => !verboten.test(z)).join("\n");
  const kern = CONFIG.hashtags.kern;
  const tags = hashtagsWaehlen(daten.hashtags || [], kern, strategie, undefined, klausur);
  return {
    format, fach, klausur, fachLabel: FAECHER[fach]?.label || "Examenswissen",
    themaId: thema?.id || null,
    folien,
    caption: (daten.caption || "").trim(),
    hashtags: tags,
    kurztitel: daten.kurztitel || folien[0]?.titel || "",
    bildSzene: daten.bildSzene || null,
    bildSzeneAlt: daten.bildSzeneAlt || null,
    quellen: daten.quellen || [],
    hookTyp: hook?.typ || hookTyp(folien[0]?.titel || ""),
  };
}

/**
 * Schreibt einen Beitrag. Prüft ihn (pruefung.mjs) und lässt bei Beanstandung
 * bis zu CONFIG.ki.maxVersuche Mal nachbessern.
 */
export async function beitragSchreiben({ format, thema, datum, recherche, wochenThemen, anlass, strategie }) {
  if (process.env.IG_AUTOR === "beispiele") return beispielBeitrag(format, thema);
  const spec = FORMATE[format] || FORMATE.pruefungsfrage;
  const fach = thema?.fach || recherche?.fach || "methodik";
  const klausur = FAECHER[fach]?.klausur || 3;
  const sperr = korpus().namen;
  let feedback = "";
  let letzter = null;
  for (let versuch = 1; versuch <= CONFIG.ki.maxVersuche; versuch++) {
    const user = [
      `Datum: ${datumLesbar(datum)}. Format: ${spec.label}.`,
      `Anleitung zum Format: ${spec.anleitung}`,
      `Empfohlene Folienfolge: ${spec.folien.join(" → ")} (bei „a|b“ wähle die passendere Art).`,
      thema ? `\n## Themen-Skelett\n${themaText(thema)}` : "",
      recherche ? `\n## Rechercheergebnis (Web, ${datumLesbar(datum)})\n${recherche.notizen}\n\nQuellen: ${recherche.quellen.join(" · ")}` : "",
      wochenThemen?.length ? `\n## Themen dieser Woche\n${wochenThemen.map((t) => `- ${t}`).join("\n")}` : "",
      anlass ? `\n## Anlass\n${anlass.titel}: ${anlass.kontext}` : "",
      `\nPhase im Prüfungsjahr: ${phase(datum)}.`,
      "",
      `\n## Sperrliste (diese Namen nie verwenden)\n${sperr.join(", ")}`,
      feedback ? `\n## Beanstandungen am vorherigen Entwurf – bitte beheben\n${feedback}\n\nVorheriger Entwurf:\n${JSON.stringify(letzter)}` : "",
      `\nErstelle jetzt den Beitrag als JSON.`,
    ].filter(Boolean).join("\n");
    const { daten } = await strukturiert({ system: SYSTEM, user, schema: BEITRAG_SCHEMA });
    const beitrag = nachbereiten(daten, { format, thema, fach, klausur, strategie });
    const ergebnis = pruefeBeitrag(beitrag);
    if (ergebnis.ok) {
      const fakten = await faktenSicher(beitrag);
      /* Sprachversehen (doppelte oder fehlende Wörter) werden im Text ersetzt,
         nicht neu geschrieben - das kostet keinen weiteren Aufruf. */
      korrekturenAnwenden(beitrag, fakten.korrekturen);
      if (fakten.ok) { beitrag.faktenHinweise = fakten.hinweise; return beitrag; }
      ergebnis.fehler.push(...fakten.fehler.map((f) => `Fachlicher Fehler: ${f}`));
    }
    feedback = ergebnis.fehler.map((f) => `- ${f}`).join("\n");
    letzter = daten;
    console.warn(`  Entwurf ${versuch} beanstandet:\n${feedback}`);
  }
  throw new Error(`Beitrag „${thema?.titel || format}“ nach ${CONFIG.ki.maxVersuche} Versuchen nicht freigegeben:\n${feedback}`);
}

/* Web-Recherche für das Format „aktuell“ (Server-Tool Websuche). */
export async function aktuellRecherchieren(datum, bereitsBehandelt = []) {
  const frage = `Heute ist der ${datumLesbar(datum)}. Recherchiere 3–5 aktuelle Neuigkeiten aus den letzten 6 Wochen, die für Kandidat:innen des ersten und zweiten juristischen Staatsexamens relevant sind: neue Entscheidungen von BGH, BVerfG, BVerwG, BAG oder EuGH mit Examensbezug, Gesetzesänderungen (BGB, StGB, StPO, ZPO, GG, VwGO, VwVfG, HGB, GmbHG, ArbR), Änderungen an Juristenausbildungsgesetzen oder Prüfungsordnungen der Länder.

Nutze ausschließlich frei zugängliche Quellen: die Entscheidungsdatenbanken der Gerichte selbst (bundesgerichtshof.de, bundesverfassungsgericht.de, bundesverwaltungsgericht.de, bundesarbeitsgericht.de, curia.europa.eu), rechtsprechung-im-internet.de, gesetze-im-internet.de, dejure.org, openjur.de, Bundesgesetzblatt, Landesjustizprüfungsämter. KEINE kostenpflichtigen Datenbanken (beck-online, juris, Wolters Kluwer) – deren Inhalte dürfen nicht weitergegeben werden; die amtlichen Entscheidungsgründe sind ohnehin frei.

Bereits behandelt (nicht erneut): ${bereitsBehandelt.join("; ") || "–"}.

Wähle dann DIE eine Neuigkeit mit dem größten Examensbezug aus – lieber eine Entscheidung zu einem Klausurklassiker als eine spektakuläre Randfrage. Antworte mit:
1. Auswahl: Titel, Datum, Aktenzeichen, Fach (eines von: bgbat, schuld, schuldbt, sachen, delikt, bereich, gesetzs, arbeit, famerb, handelsg, zpo, strafat, strafbt, stpo, staat, grundr, verwalt, verwbt, vwgo, europa)
2. Notizen: Was ist passiert, welche Norm trägt die Entscheidung, was ändert sich gegenüber der bisherigen Linie, und was heißt das für die Klausur (max. 200 Wörter, eigene Worte)
3. Quellen: 2–3 URLs`;
  return webRecherche(frage, "recherche");
}

/* Web-Recherche am Klausurtag: Was berichten Kandidat:innen über die heutige
   Klausur? Läuft nur, wenn ein konkreter Prüfungstermin gesetzt ist
   (IG_EXAMEN_DATUM) – ohne Termin gibt es diesen Anlass nicht. */
export async function loesungsRecherchieren(datum, anlass) {
  const jahr = datum.slice(0, 4);
  const gebiet = { 1: "Zivilrecht", 2: "Strafrecht", 3: "Öffentliches Recht" }[anlass?.klausur] || "";
  const frage = `Heute ist der ${datumLesbar(datum)}. ${anlass?.kontext || "Heute war ein Klausurtag der juristischen Staatsprüfung."}
Recherchiere Berichte von Kandidat:innen zur Examensklausur ${jahr}${gebiet ? ` im ${gebiet}` : ""}: Welche Sachverhalte, Aufgabenstellungen und Problemschwerpunkte werden genannt? Suche in Foren (Jura-Foren, Reddit r/jura, jurawelt), sozialen Netzwerken (Instagram, LinkedIn, X), bei Repetitorien und in Examensreport-Sammlungen der Fachschaften und Landesjustizprüfungsämter. Suchbegriffe wie „Examensreport ${jahr} ${gebiet}“, „Klausur ${jahr} Erfahrungen Staatsexamen“, „Examensklausur ${jahr} Probleme“.

Antworte mit:
1. Titel: ein kurzer Titel
2. Fach: das passende Fach (bgbat, schuld, schuldbt, sachen, delikt, bereich, gesetzs, arbeit, famerb, handelsg, zpo, strafat, strafbt, stpo, staat, grundr, verwalt, verwbt, vwgo, europa)
3. Notizen (max. 300 Wörter, eigene Worte): die berichteten Probleme je Aufgabe, mit Angabe, wie oft und wie sicher sie berichtet werden (mehrfach / einzeln / unsicher). Gibt es noch keine belastbaren Berichte, sage das ausdrücklich und nenne stattdessen die erfahrungsgemäßen Dauerbrenner dieses Rechtsgebiets.
4. Quellen: 2–4 URLs`;
  return webRecherche(frage, "recherche-loesung");
}

async function webRecherche(frage, zweck = "recherche") {
  const params = {
    model: CONFIG.ki.modellNeben,
    max_tokens: 8000,
    thinking: { type: "adaptive" },
    output_config: { effort: CONFIG.ki.effort },
    tools: [{ type: "web_search_20260209", name: "web_search", max_uses: CONFIG.ki.rechercheSuchen, user_location: { type: "approximate", country: "DE", timezone: "Europe/Berlin" } }],
    messages: [{ role: "user", content: frage }],
  };
  budgetPruefen("Recherche");
  let response = await client().messages.create(params);
  erfassen(CONFIG.ki.modellNeben, response.usage, zweck);
  let runden = 0;
  while (response.stop_reason === "pause_turn" && runden++ < 4) {
    params.messages.push({ role: "assistant", content: response.content });
    response = await client().messages.create(params);
    erfassen(CONFIG.ki.modellNeben, response.usage, zweck);
  }
  const text = textAus(response);
  const fachTreffer = text.match(/Fach\s*[:：]\s*(ao|ust|erbst|kst|istr|bilanz|persg)/i);
  const quellen = [...new Set((text.match(/https?:\/\/[^\s)>\]]+/g) || []))].slice(0, 4);
  return { notizen: text, quellen, fach: fachTreffer ? fachTreffer[1].toLowerCase() : "methodik", titel: (text.match(/Titel\s*[:：]\s*(.+)/i) || [])[1]?.trim() || "" };
}

/**
 * Schreibt alle eigenständigen Stories eines Tages in einem Aufruf.
 * @param {Array<{slot, art, thema?, tageBisExamen?}>} plan
 */
export async function storiesSchreiben(plan, datum, hinweis = "") {
  if (process.env.IG_AUTOR === "beispiele") return beispielStories(plan);
  const auftraege = plan.map((s) => {
    const kopf = `- slot ${s.slot}: art=${s.art}`;
    if (s.art === "countdown") return `${kopf} – Countdown: noch ${s.tageBisExamen} Tage bis zur schriftlichen Prüfung (${datumLesbar(CONFIG.examen.schriftlich)}–${datumLesbar(CONFIG.examen.ende)}). titel = „Tage bis zur schriftlichen Prüfung“, zahl = „${s.tageBisExamen}“, text = ein motivierender, konkreter Lern-Tipp für heute (1–2 Sätze).`;
    if (s.art === "antwort") return `${kopf} – Auflösung zur Frage im vorherigen Slot: dieselben optionen, richtig = Index der richtigen Option, titel = kurze Auflösung, text = Begründung mit Norm (max. 200 Zeichen).`;
    return `${kopf}\n${s.thema ? themaText(s.thema).split("\n").map((z) => `  ${z}`).join("\n") : ""}`;
  }).join("\n");
  const user = `Datum: ${datumLesbar(datum)}. Schreibe die folgenden Instagram-Stories (Hochformat, je eine Kachel, sehr wenig Text):

Arten:
- frage: titel = Prüfungsfrage (max. 90 Zeichen), optionen = 3 kurze Antwortmöglichkeiten (max. 60 Zeichen), ueberzeile = „Prüfungsfrage <Fach>“
- antwort: siehe Auftrag
- norm: norm = die Norm in Kurzform (z. B. „§ 80 Abs. 5 VwGO“), titel = worum es geht (max. 60 Zeichen), text = ein Prüfungstipp dazu (max. 180 Zeichen)
- merksatz: text = ein Satz, der hängen bleibt (max. 120 Zeichen), titel = Thema (max. 60 Zeichen)
- formel: titel = Name des Rechenwegs, formel = Formel (max. 60 Zeichen), text = Erklärung mit eigenem Zahlenbeispiel (max. 180 Zeichen)
- begriff: titel = Begriff, norm = Norm, text = Definition in eigenen Worten (max. 200 Zeichen), icon
- fehler: titel = die Falle (max. 70 Zeichen), falsch = der Fehler (max. 120 Zeichen), richtigText = die richtige Lösung mit Norm (max. 160 Zeichen)
- tipp: titel = Klausurtipp (max. 70 Zeichen), text = Umsetzung (max. 180 Zeichen), icon
- bildSzene (nur bei begriff und tipp, sonst null): eine ENGLISCHE, fotografierbare Alltagsszene in 3–6 Wörtern, nach der sich in einer Fotodatenbank suchen lässt und die das Thema bildlich greifbar macht („woman reading letter at kitchen table“). Keine Fachvokabeln, keine abstrakten Begriffe, keine Symbolbild-Klassiker (Richterhammer, Waage, Gesetzbuch, Taschenrechner, Münzstapel, Händedruck). Nur Motive, die ganz im Bild sind – eine Person vom Kopf bis zur Hüfte, ein Gegenstand mit Rand ringsum. Fällt dir keine echte Szene ein: null.
- zahl: zahl = eine markante Zahl/Frist/Prozentsatz (max. 8 Zeichen), titel = was sie bedeutet (max. 60 Zeichen), text = Norm und Kontext (max. 160 Zeichen)

Aufträge:
${auftraege}

Sperrliste (Namen nie verwenden): ${korpus().namen.join(", ")}

Alles in eigenen Worten, juristisch korrekt, mit Norm. Nicht benötigte Felder null. Gib genau einen Eintrag je Slot zurück.${hinweis ? `\n\n${hinweis}` : ""}`;
  const { daten } = await strukturiert({ system: SYSTEM, user, schema: STORY_SCHEMA, modell: CONFIG.ki.modellNeben, effort: CONFIG.ki.effort, zweck: "stories" });
  const nachSlot = new Map(daten.stories.map((s) => [s.slot, s]));
  const liste = plan.map((p) => {
    const s = nachSlot.get(p.slot) || {};
    const o = { slot: p.slot, art: p.art, fach: p.thema?.fach || "methodik", klausur: p.thema?.klausur || 3 };
    for (const [k, v] of Object.entries(s)) if (v != null && k !== "slot" && k !== "art") o[k] = v;
    if (o.icon && !ICONS[o.icon]) o.icon = "paragraf";
    if (p.art === "countdown") { o.zahl = String(p.tageBisExamen); o.fortschritt = Math.round(100 - Math.min(100, p.tageBisExamen / 150 * 100)); o.ueberzeile = "Noch"; }
    o.fachLabel = FAECHER[o.fach]?.label || "Examenswissen";
    felderKuerzen(o, ["titel", "text", "norm", "formel", "richtigText", "falsch", "ueberzeile"]);
    const ergebnis = pruefeBeitrag({ stories: [o] });
    if (!ergebnis.ok) { o.beanstandet = ergebnis.fehler; }
    return o;
  });

  /* Faktencheck über alle Stories des Tages in einem Aufruf. Beiträge und
     Reels liefen von Anfang an dagegen, Stories nicht - dabei sind sie neun
     von elf Veröffentlichungen am Tag, und die erste live gegangene Story trug
     prompt eine falsch zugeordnete Norm. Befunde landen in `beanstandet`;
     damit greift die Schleife im Tageslauf, die beanstandete Slots ohnehin
     einmal neu schreiben lässt. */
  const fakten = await faktenSicher({ stories: liste }, "story-faktencheck", {
    hinweis: "Jede Kachel steht für sich. Nenne zu jedem Befund den Slot in eckigen Klammern, genau so, wie er im Kopf der Kachel steht (zum Beispiel [s5]).",
  });
  korrekturenAnwenden({ stories: liste }, fakten.korrekturen);
  for (const f of fakten.fehler || []) {
    const treffer = String(f).match(/\[?\b(s\d+)\b\]?/);
    /* Ohne erkennbaren Slot lässt sich der Befund keiner Kachel zuordnen -
       dann werden lieber alle neu geschrieben als eine falsche zu posten. */
    const ziele = treffer ? liste.filter((o) => o.slot === treffer[1]) : liste;
    for (const o of ziele) (o.beanstandet ||= []).push(String(f));
  }
  return liste;
}

const REEL_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    szenen: {
      type: "array",
      items: {
        type: "object",
        additionalProperties: false,
        properties: {
          art: { type: "string", enum: ["hook", "schritt", "punkt", "merke", "cta"] },
          nummer: { type: ["integer", "null"] },
          titel: { type: "string" },
          unter: { type: ["string", "null"] },
          text: { type: ["string", "null"] },
          norm: { type: ["string", "null"] },
          icon: { type: ["string", "null"] },
          sprecher: { type: "string" },
        },
        required: ["art", "nummer", "titel", "unter", "text", "norm", "icon", "sprecher"],
      },
    },
    caption: { type: "string" },
    hashtags: { type: "array", items: { type: "string" } },
    kurztitel: { type: "string" },
    bildSzene: { type: ["string", "null"] },
    bildSzeneAlt: { type: ["string", "null"] },
  },
  required: ["szenen", "caption", "hashtags", "kurztitel", "bildSzene", "bildSzeneAlt"],
};

/* Sprechtempo einer deutschen Vorlesestimme: rund 2,4 Wörter je Sekunde.
   Aus dem Zeitfenster wird daraus eine Wortzahl - eine Sekundenangabe allein
   kann ein Sprachmodell nicht einhalten, eine Wortzahl schon. */
const WOERTER_JE_SEKUNDE = 2.4;

function laengenAnleitung(von, bis, lang) {
  const wVon = Math.round(von * WOERTER_JE_SEKUNDE), wBis = Math.round(bis * WOERTER_JE_SEKUNDE);
  const szenen = lang ? "6–9" : von >= 60 ? "6–8" : von >= 45 ? "5–7" : "4–6";
  return `## Länge
Dieses Reel soll ${von}–${bis} Sekunden dauern, also insgesamt ${wVon}–${wBis} gesprochene Wörter in ${szenen} Szenen. Halte dich daran: Zu kurz wirkt abgehackt, zu lang verliert die Zuschauer.
Die Länge ist kein Sparzwang. Wenn das Thema einen Schritt mehr braucht, nimm die Sekunden – aber keine Füllsätze, keine Wiederholungen, keine Begrüßung.`;
}

const REEL_ANLEITUNG = `## Reel (Hochformat, mit Sprecherstimme)
Du schreibst ein Skript aus Szenen. Jede Szene hat einen kurzen Bildschirmtext und einen Sprechertext.
- Szenenarten: hook (Frage/Aufhänger, Folge 1), schritt (nummeriert, für Prüfschritte) oder punkt (unnummeriert), merke (Merksatz + norm), cta (Abschluss).
- Bildschirmtext: titel maximal 7 Wörter, text maximal 14 Wörter. Was gesprochen wird, steht NICHT wortgleich auf dem Bildschirm – der Bildschirm zeigt die Essenz, die Stimme erklärt.
- Sprechertext: So, wie ein Mensch spricht, nicht wie ein Lehrbuch. Kurze Hauptsätze, direkte Ansprache, gelegentlich ein Gedankenstrich als Pause, ein „Also:“, „Kurz gesagt:“, „Und jetzt der Punkt, den fast alle übersehen.“ Keine Klammern, keine Abkürzungen (schreibe „Paragraf zweihundertneunundvierzig Absatz eins“ als „Paragraf 249 Absatz 1“ – die Stimme liest Ziffern korrekt). Keine Aufzählungszeichen. Je Szene 1–3 Sätze, insgesamt 110–150 Wörter.
- Szene 1 ist der Hook. Wie er zu bauen ist, steht unten in einem eigenen Abschnitt; er entscheidet über die Reichweite des ganzen Reels.
- cta: Der Kern in einem Satz, dann die Aufforderung zu folgen – ohne Website, ohne Produkt. Kündige NICHTS an: kein „Nächstes Mal zeige ich dir …“, kein „Im nächsten Reel …“, kein „Teil 2 folgt“. Was hier steht, muss auch in einem Jahr noch stimmen.
- icon nur beim hook.`;

/* Reel-Skript schreiben (Szenen mit Bildschirm- und Sprechertext). */
export async function reelSchreiben({ thema, datum, lang = false, anlass = null, strategie = null }) {
  const fach = thema?.fach || "methodik";
  const klausur = FAECHER[fach]?.klausur || 3;
  const sperr = korpus().namen;
  /* Muster des Tages – rotiert, bevorzugt aber, was gemessen besser lief. */
  const hookMuster = hookMusterWaehlen(datum, strategie);
  /* Die Ziellänge kommt aus der Lernschleife: Jedes Fenster wird erst ein paar
     Mal ausprobiert, danach gewinnt, was gemessen besser lief. Ein Reel muss
     nicht kurz sein - braucht ein Prüfschema 80 Sekunden, bekommt es sie. */
  const [von, bis] = dauerWaehlen(datum, strategie, { min: lang ? 60 : 0 });
  let feedback = "", letzter = null;
  for (let versuch = 1; versuch <= CONFIG.ki.maxVersuche; versuch++) {
    const user = [
      `Datum: ${datumLesbar(datum)}. Format: ${lang ? `Reel mit einem kompletten Prüfschema, ${von}–${bis} Sekunden` : `Reel, ${von}–${bis} Sekunden`}.`,
      laengenAnleitung(von, bis, lang),
      REEL_ANLEITUNG,
      hookAnleitung(hookMuster),
      "\n## Cover-Motiv\nbildSzene: eine ENGLISCHE, fotografierbare Alltagsszene in 3–6 Wörtern für das Standbild des Reels, nach der sich in einer Fotodatenbank suchen lässt und die das Thema bildlich greifbar macht („woman reading letter at kitchen table“). Keine Fachvokabeln, keine abstrakten Begriffe, keine Symbolbild-Klassiker (Richterhammer, Waage, Gesetzbuch, Taschenrechner, Münzstapel, Händedruck). Nur Motive, die ganz im Bild sind – eine Person vom Kopf bis zur Hüfte, ein Gegenstand mit Rand ringsum; keine Gruppen, keine Nahaufnahmen, keine Bewegungsunschärfe. Fällt dir keine echte Szene ein: null.\nbildSzeneAlt: eine zweite, andere Szene nach denselben Regeln als Ersatz, sonst null.",
      `\n## Normen\n${NORM_REGEL}\n${NORM_REGEL_STIMME}`,
      anlass ? `\n## Anlass\n${anlass.titel}: ${anlass.kontext}` : "",
      `Phase im Prüfungsjahr: ${phase(datum)}.`,
      thema?.typ === "mindset" ? "\n## Mindset-Reel (Ersatz für ein Talking-Head-Video)\nKein Fachschema, sondern ein persönlicher, ruhiger Ton in Du-Form: ein Problem, das fast alle kennen (Angst, Blackout, Zeitdruck, Perfektionismus), dann 3–4 konkrete, sofort umsetzbare Handgriffe, zum Schluss ein Satz, der bleibt. Normen nur, wenn sie wirklich helfen. Bildschirmtitel kurz und menschlich, kein Ratgeber-Kitsch." : "",
      `\n## Themen-Skelett\n${themaText(thema)}`,
      `\n## Sperrliste (diese Namen nie verwenden)\n${sperr.join(", ")}`,
      `\n## Beispiel für Ton und Länge (anderes Thema)\n${JSON.stringify(beispielReel.szenen.slice(0, 3), null, 1)}`,
      feedback ? `\n## Beanstandungen am vorherigen Entwurf – bitte beheben\n${feedback}\n\nVorheriger Entwurf:\n${JSON.stringify(letzter)}` : "",
      `\nErstelle jetzt das Reel-Skript als JSON.`,
    ].filter(Boolean).join("\n");
    const { daten } = await strukturiert({ system: SYSTEM, user, schema: REEL_SCHEMA, zweck: "reel" });
    const szenen = daten.szenen.map((s) => {
      const o = {};
      for (const [k, v] of Object.entries(s)) if (v != null) o[k] = v;
      if (o.icon && !ICONS[o.icon]) o.icon = "paragraf";
      /* Auf dem Bildschirm die Kurzform, in der Stimme die ausgeschriebene
         Fassung – „(1)“ würde sonst als „Klammer auf eins“ vorgelesen. */
      felderKuerzen(o, ["titel", "unter", "text", "norm"]);
      if (o.sprecher) o.sprecher = normGesprochen(o.sprecher);
      return o;
    });
    const reel = { format: "reel", fach, klausur, fachLabel: FAECHER[fach]?.label, themaId: thema?.id || null, szenen, caption: normKurz((daten.caption || "").trim()), hashtags: [...new Set([...(daten.hashtags || []).map((h) => (h.startsWith("#") ? h : `#${h}`).toLowerCase()), ...CONFIG.hashtags.kern])].slice(0, CONFIG.hashtags.maxJeBeitrag), kurztitel: daten.kurztitel || szenen[0]?.titel || "", bildSzene: daten.bildSzene || null, bildSzeneAlt: daten.bildSzeneAlt || null };
    /* Prüfung über die Folien-Logik: Szenen als Folien, Sprechertext als Text. */
    const ergebnis = pruefeBeitrag({ folien: [{ art: "titel", titel: szenen[0]?.titel || "" }, ...szenen.slice(1).map((s) => ({ art: "text", titel: s.titel, text: `${s.text || ""} ${s.sprecher}` })), { art: "cta" }], caption: reel.caption, hashtags: reel.hashtags });
    ergebnis.fehler.push(...pruefeHook(szenen[0]));
    /* Die Annahmegrenze folgt dem gewählten Zeitfenster. Stand sie fest, wurde
       jedes längere Reel abgelehnt, obwohl die Anleitung genau diese Länge
       verlangt hatte - ein Nachschlag pro Reel, und nach drei Versuchen gar
       kein Reel. Die Toleranz ist großzügig: Ein paar Wörter mehr verschieben
       die Dauer um Sekunden, nicht um ein Fenster. */
    const woerter = szenen.reduce((n, s) => n + s.sprecher.split(/\s+/).length, 0);
    const zielVon = Math.round(von * WOERTER_JE_SEKUNDE), zielBis = Math.round(bis * WOERTER_JE_SEKUNDE);
    const min = Math.round(zielVon * 0.75), max = Math.round(zielBis * 1.25);
    if (woerter < min || woerter > max) ergebnis.fehler.push(`Sprechertext hat ${woerter} Wörter (Ziel ${zielVon}–${zielBis})`);
    if (!ergebnis.fehler.length) {
      const fakten = await faktenSicher(reel, "reel-faktencheck");
      korrekturenAnwenden(reel, fakten.korrekturen);
      if (fakten.ok) { reel.hookTyp = hookTypErkennen(szenen[0]?.titel || "", szenen[0]?.sprecher || ""); reel.hookMuster = hookMuster; return reel; }
      ergebnis.fehler.push(...fakten.fehler.map((f) => `Fachlicher Fehler: ${f}`));
    }
    feedback = ergebnis.fehler.map((f) => `- ${f}`).join("\n");
    letzter = daten;
    console.warn(`  Reel-Entwurf ${versuch} beanstandet:\n${feedback}`);
  }
  throw new Error(`Reel „${thema?.titel}“ nach ${CONFIG.ki.maxVersuche} Versuchen nicht freigegeben:\n${feedback}`);
}

/* Teaser-Story aus einem fertigen Beitrag – ohne KI-Aufruf. */
export function teaserAusBeitrag(beitrag, slot) {
  return {
    slot, art: "teaser", fach: beitrag.fach, klausur: beitrag.klausur, fachLabel: beitrag.fachLabel,
    ueberzeile: "Neuer Beitrag",
    titel: beitrag.kurztitel || beitrag.folien[0].titel,
    text: beitrag.folien[0].titel !== beitrag.kurztitel ? beitrag.folien[0].titel : "",
    icon: beitrag.folien[0].icon || "paragraf",
    /* Das Motiv der Titelfolie wandert mit - so kündigt die Story den Beitrag
       mit demselben Bild an. */
    bild: beitrag.folien[0].bild || null, bildFrei: beitrag.folien[0].bildFrei !== false, bildQuelle: beitrag.folien[0].bildQuelle || null,
    pille: "Jetzt im Feed",
  };
}

/* --- Beispielmodus (IG_AUTOR=beispiele): Inhalte aus beispiele/inhalte.json,
   ohne API-Aufruf. Für lokale Tests des Renderns und Hochladens. --- */
function beispielBeitrag(format, thema) {
  const b = beispiele.beitraege.find((x) => x.format === format) || beispiele.beitraege[0];
  const fach = thema?.fach || b.fach;
  return nachbereiten({ ...b, kurztitel: b.folien[0].titel, quellen: [] }, { format, thema, fach, klausur: FAECHER[fach]?.klausur || b.klausur });
}

function beispielStories(plan) {
  return plan.map((p) => {
    const s = beispiele.stories.find((x) => x.art === p.art) || beispiele.stories[0];
    const o = { ...s, slot: p.slot, art: p.art, fach: p.thema?.fach || s.fach, klausur: p.thema?.klausur || s.klausur };
    if (p.art === "countdown") { o.zahl = String(p.tageBisExamen); o.fortschritt = Math.round(100 - Math.min(100, p.tageBisExamen / 150 * 100)); }
    o.fachLabel = FAECHER[o.fach]?.label || "Examenswissen";
    return o;
  });
}
