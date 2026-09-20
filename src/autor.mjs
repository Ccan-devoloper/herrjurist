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
import { istKostenKontrollFehler } from "./kostenfehler.mjs";
import { FAECHER, KLAUSUREN } from "./inhalte.mjs";
import { belegstelle } from "./wissen.mjs";
import { ICONS } from "./stile.mjs";
import { folieLeer, pruefeBeitrag, korpus, normenOhneGesetz, quizBefunde, fachpruefungAbschliessen } from "./pruefung.mjs";
import { createHash } from "node:crypto";
import { datumLesbar, tageBis, heuteIso } from "./zeit.mjs";
import { erfassen, budgetFrei, BudgetFehler } from "./kosten.mjs";
import { claudeAufruf } from "./anbieter.mjs";
import { rechercheAuftrag, ResearchGrenze } from "./research.mjs";
import { pruefeFakten, korrekturenAnwenden } from "./faktencheck.mjs";
import { hookWaehlen as hookMusterWaehlen, hookAnleitung, pruefeHook, hookTypErkennen } from "./hooks.mjs";
import { dauerWaehlen } from "./insights.mjs";
import { normKurz, normGesprochen, felderKuerzen, NORM_REGEL, NORM_REGEL_STIMME } from "./normen.mjs";
import { hookTyp } from "./insights.mjs";
import { phase } from "./kalender.mjs";

const hier = path.dirname(fileURLToPath(import.meta.url));
const beispiele = JSON.parse(fs.readFileSync(path.resolve(hier, "../beispiele/inhalte.json"), "utf8"));
const beispielReel = JSON.parse(fs.readFileSync(path.resolve(hier, "../beispiele/reel.json"), "utf8"));


/* Beitragsformate – was der Autor je Format bauen soll. */
export const FORMATE = {
  pruefungsfrage: {
    label: "Prüfungsfrage",
    anleitung: "Folie 1: eine echte Prüfungsfrage als Aufhänger (so, wie sie in der Klausur oder mündlichen Prüfung fallen könnte). Dann entscheide dich für einen von zwei Wegen und halte ihn durch: ENTWEDER du antwortest abstrakt – dann kommen auf keiner Folie erfundene Personen, Namen oder Beträge vor – ODER du legst einen Fall zugrunde; dann gehört Folie 2 dem Sachverhalt (art text, Titel „Sachverhalt“): der Fall in 2–4 Sätzen, mit allen Namen, Beträgen und Daten, die die Lösung danach benutzt. Wer auf Folie 3 „Finn“ liest, muss auf Folie 2 erfahren haben, wer Finn ist. Die Caption zählt dafür nicht – sie ist zugeklappt, und die meisten lesen nur die Folien. Danach: die Antwort in klaren Schritten oder Punkten mit den tragenden Normen. Vorletzte Folie: Merksatz. Letzte Folie: CTA.",
    folien: ["titel", "text (Sachverhalt, nur wenn der Beitrag einen Fall erzählt)", "text|schritte", "text|vergleich", "merke", "cta"],
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
    anleitung: "Folie 1: „Hast du diese Woche alles mitgenommen?“. Folie 2 gehört ausschließlich zum Zivilrecht, Folie 3 ausschließlich zum Strafrecht, Folie 4 ausschließlich zum Öffentlichen Recht. Ordne alle Wochenthemen nach dem mitgelieferten Rechtsgebiet ein; Unterfächer sind keine eigenen Rechtsgebiete. Insbesondere gehört BGB AT immer zum Zivilrecht. Überschriften dürfen Rechtsgebiete nie bündeln (also nicht „Zivil- und Strafrecht“ oder „Öffentliches Recht und BGB AT“). Folie 5: Klausurtechnik/Lernplan-Tipp fürs Wochenende; Themen aus Klausur- und Lernmethodik dürfen hier kurz aufgegriffen werden. Letzte Folie: CTA.",
    folien: ["titel", "text", "text", "text", "text", "cta"],
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
- Das Material im Themen-Skelett und in der Wissensbasis ist fachlich maßgeblich. Wo es eine Systematik vorgibt – einen Aufbau, eine Prüfungsreihenfolge, eine Einteilung in Ebenen –, folgst du ihr, auch wenn du eine andere Darstellung kennst. Lehrbücher schneiden denselben Stoff oft unterschiedlich; beide Schnitte können vertretbar sein, und der Kanal spricht mit einer Stimme. Zwei Grenzen: Der Wortlaut ist immer deiner. Und wenn eine Aussage fachlich nicht vertretbar ist – sie widerspricht dem Gesetz, der gefestigten Rechtsprechung oder der ganz herrschenden Meinung –, übernimmst du sie nicht, sondern schreibst das Richtige.
- Du bekommst ein Themen-Skelett (Frage, Normen, Stichpunkte). Formuliere ALLES neu, in eigenen Worten und eigener Struktur. Übernimm keine Sätze, keine Aufzählungsreihenfolgen, keine Beispielzahlen.
- Fälle, Beispiele, Namen und Zahlen erfindest du selbst – und jedes Mal neu: andere Branche, anderer Ort, anderer Name als in früheren Texten. Nie ein Name, der im Ausgangsmaterial vorkommt, nie ein Name aus der Sperrliste, und nie zweimal derselbe Firmen- oder Personenname in verschiedenen Beiträgen.
- Keine Bezüge auf Kurse, Skripte, Seiten, Folien, Fallnummern, Dozenten oder Lernplattformen.

## Marke und Aufforderung (CTA)
- Markenkern: „Examenswissen, sortiert nach Rechtsgebiet“. Jeder Beitrag gehört zu genau einem Gebiet (Zivilrecht, Strafrecht, Öffentliches Recht) und trägt dessen Farbe. Zielgruppe sind Kandidatinnen und Kandidaten im ersten und zweiten juristischen Staatsexamen – schreibe auf diesem Niveau: Streitstände benennen, herrschende Meinung und Gegenansicht sauber trennen, den Streitentscheid nicht auslassen.
- Normen sind das Rückgrat: Jede Aussage, die eine Norm hat, nennt sie. Bei Streitständen die Fundstelle der Argumentation (Wortlaut, Systematik, Sinn und Zweck, Historie) statt bloßer Behauptung.
- Kein Halbwissen und keine Vereinfachung, die in der Klausur Punkte kostet: Lieber eine Frage weniger beantworten als eine falsch.
- Landesrecht kennzeichnen: Polizei- und Ordnungsrecht, Kommunalrecht, Bauordnungsrecht und Verwaltungsvollstreckung sind je Bundesland anders geregelt. Bei solchen Themen gehört ein Hinweis auf die Folie oder in die Caption („je nach Land unterschiedlich – prüf dein Landesrecht“), und es wird kein Landesparagraf als bundesweit gültig ausgegeben.
- Methodik-Beiträge (Fach „Klausur- und Lernmethodik“) erklären die Methode an EINEM konkreten Beispiel aus einem Rechtsgebiet. Ein abstrakter Ratschlag ohne Beispiel ist wertlos – den kann jeder geben.
- Der wichtigste Wachstumsmotor sind Lerngruppen (WhatsApp, Telegram): Jeder Beitrag ist so gebaut, dass man ihn weiterleitet. Haupt-CTA daher immer „Schick das deiner Lerngruppe“ (oder gleichwertig), zweitens „Speichern“, drittens „Folgen“. Nie nur „Speicher dir das“.
- Die Weiterleitungs-CTA nennt möglichst einen konkreten Anlass oder Empfänger aus dem Thema („Schick das der Person in deiner Lerngruppe, die X und Y verwechselt“ / „Schickt euch das vor Tag 2 noch einmal“), statt nur abstrakt „Teilen“ zu sagen. Kein künstlicher Druck.
- Nähe statt Konzern: Fragen in den Kommentaren werden beantwortet, DM ist erlaubt („Schreib mir, wenn etwas unklar ist“). Keine Verkaufsbotschaft, kein Kurs, kein Produkt – jetzt zählen Reichweite, Saves und Weiterleitungen.

## Innere Logik (sehr wichtig)
- Der Beitrag muss aus sich heraus verständlich sein: Jede Zahl, jeder Name, jeder Fall, auf den Titel, Rechnung oder Lösung Bezug nehmen, wird vorher auf einer eigenen Folie eingeführt (z. B. Folie „Sachverhalt“). Nie auf etwas verweisen, das nicht auf den Folien steht.
- Jede Folie außer der CTA hat einen Titel UND Inhalt (Text, Punkte, Schritte, Rechnung). Nie eine leere Folie, nie nur eine Überschrift.
- Genau eine CTA-Folie, und zwar als letzte. Folie 1 ist die einzige Titelfolie.

## Form
- Folienarten: titel (Frage/Aufhänger), text (Titel + Text oder Punkte), schritte (nummeriert, je Schritt titel + text), vergleich (links/rechts mit titel + punkte), rechnung (formel, zeilen, ergebnis), karte (dichter Spickzettel: schritte mit kurzem titel + norm im text), merke (ein Satz, der hängen bleibt), cta (Abschluss mit Folgen-Aufforderung).
- hooks: drei alternative Titel für Folie 1 mit unterschiedlichem Einstieg: (1) konkrete Prüfungsfrage/Entscheidung, (2) echte Abgrenzung oder belegbare Falle, (3) klarer Ablauf/Nutzen oder kurzer Falltrigger. Der Titel nennt das juristische Thema selbst – kein austauschbares „Kennst du das?“ und kein künstliches Geheimnis. Keine erfundenen Häufigkeiten, Punktzahlen, Korrektorenvorlieben oder Superlative.
- Die erste Zeile der Caption ist gleichzeitig Suchtext: Sie nennt das Thema mit den Wörtern, die jemand bei Instagram oder Google eintippen würde (z. B. „Annahmeverzug Voraussetzungen Rechtsfolgen“), natürlich eingebettet in den Hook.
- Folie-1-Titel: 5–10 gut lesbare Wörter, ideal 35–70 Zeichen, maximal 80.
- Folie 2 löst den Swipe ein: keine zweite Teaser-Kachel und kein Fülltext. Sie gibt sofort die entscheidende Abgrenzung, den Sachverhalt oder den ersten echten Prüfungsschritt, damit der Nutzen nach dem Wischen sichtbar wird. Er muss ohne Caption und ohne Ton verständlich machen, welche Rechtsfrage/Abgrenzung folgt. Andere Titel maximal 60 Zeichen.
- Je Folie maximal 5 Punkte / 5 Schritte, insgesamt maximal 380 Zeichen Text je Folie; bei „vergleich“ je Spalte maximal 3 Punkte à 60 Zeichen.
- Kernaussagen und Merksätze aus dem Skelett NIE übernehmen, auch nicht leicht umgestellt – schreibe einen eigenen Merksatz mit anderem Satzbau und anderen Wörtern.
- Hervorhebungen mit *Sternchen* um das Wort – sparsam, ein bis zwei je Folie.
- icon: genau einer aus: ${Object.keys(ICONS).join(", ")}. Nimm das konkreteste Zeichen zum Thema – das, was in der Geschichte des Falls vorkommt: Tötungsdelikt → messer oder polizei, Kaufvertrag → handschlag oder einkaufswagen, Mietrecht → haus oder schluessel, Erbrecht → schriftrolle, Verkehrsunfall → auto, Kündigung → umschlag, Insolvenz → geld-weg. Die allgemeinen Zeichen (waage, paragraf, buch, dokument) sind nur Rückfall, wenn wirklich nichts Konkretes passt.
- Caption: 4–8 Zeilen. Zeile 1 ist der Hook (die Frage oder die Pointe), dann die Kernantwort in 2–4 Sätzen, dann die Aufforderung, den Beitrag an die Lerngruppe weiterzuleiten und zu speichern, plus eine echte Frage an die Leser:innen, die eine Antwort im Kommentar provoziert. ${CONFIG.marke.website ? `Am Ende darf ein Hinweis „Mehr auf ${CONFIG.marke.website} (Link in Bio)“ stehen.` : "Keine Website, keine Plattform, kein Produkt erwähnen – auch nicht „Link in Bio“."} Keine Hashtags in der Caption; die kommen separat.
- Hashtags: 8–14 Stück, deutsch, kleingeschrieben, spezifisch zum Thema plus diese Kernhashtags: ${CONFIG.hashtags.kern.join(" ")}.
- kurztitel: 3–6 Wörter für die Story-Ankündigung und das Reel-Cover. Er muss grammatisch aufgehen: entweder eine Nominalphrase ohne Verb („Mord und Totschlag: das Verhältnis“) oder ein vollständiger Satz/eine vollständige Frage („Sitzt alles?“). Falsch wäre „Wochenrückblick: alles sitzen?“ – ein Infinitiv ohne Subjektbezug.
- BILDREGEL FÜR KARUSSELLS: NUR Folie 1 (Cover/Titelfolie) bekommt ein Foto. Alle inneren Karussell-Slides bleiben reine Text-/Strukturfolien: niemals Foto, Bildhintergrund oder dekoratives Motiv; dort sind nur Typografie, Kästen, Linien, Pfeile und kleine Icons erlaubt.
- bildSzene: PFLICHT für jeden Karussell-Beitrag. Eine ENGLISCHE Beschreibung einer konkreten, fotografierbaren Alltagsszene für das Titelbild – 3 bis 6 Wörter, so, wie man sie in einer Fotodatenbank suchen würde. Sie muss die Rechtsfrage bildlich greifbar machen, nicht sie beschriften: für den Annahmeverzug „delivery man waiting at door“, für das Mietrecht „damp stain on apartment wall“, für den Betrug „person signing contract nervously“. Verboten sind juristische Vokabeln („annahmeverzug“, „liability“), abstrakte Begriffe („justice“, „law“) und die Symbolbild-Klassiker: Richterhammer, Waage, Paragrafenzeichen, Gesetzbuch, Gerichtsgebäude, Anzugträger beim Händedruck – die sagen nichts und stehen unter jedem zweiten Jura-Beitrag. Bevorzuge den Gegenstand, um den es juristisch geht (Akte, Bescheid, Vertrag, Schriftstück, Kalender mit Frist), und nimm eine Person nur, wenn die HANDLUNG das Thema trägt; steht keine Person in der Beschreibung, wird auch keine gezeichnet. Beschreibe ein Schriftstück NIE über das, was daraufsteht, sondern über Form und Zustand („folded letter with wax seal“, „stapled document with sections“, „open ring binder“) - und meide Motive, die von Beschriftung leben (Briefumschlag mit Aufdruck, Schild, Etikett, Buchdeckel, Urkunde, Stempel). Das Zeichenmodell schreibt sonst englische Wörter ins Bild, und zwar falsch geschrieben: Am 18.09. stand „GERITIFIEID MAIL“ auf dem Titelbild eines Beitrags zum Öffentlichen Recht. Prüfe mit der Gegenfrage: „Könnte dieses Bild genauso gut zu einem ganz anderen juristischen Thema gehören?“ Wenn ja, ist es zu allgemein. Das Foto wird freigestellt (Hintergrund weg) und als Motiv auf die Kachel gesetzt – wähle deshalb Szenen mit EINEM klaren Motiv im Vordergrund (ein Gegenstand mit Rand ringsum oder eine Person vom Kopf bis zur Hüfte), keine Gruppen, keine Nahaufnahmen, keine Bewegungsunschärfe, nichts, das am Bildrand abgeschnitten wäre. Das Covermotiv wird fotorealistisch erzeugt/gesucht und zusammen mit dem thematischen Icon auf Folie 1 gesetzt. Gib niemals null zurück; wenn das Thema keine offensichtliche Szene hat, wähle eine ruhige, fachnahe Dokument-/Lernsituation.
- bildSzeneAlt: ebenfalls PFLICHT: eine zweite, deutlich andere fotografierbare Szene zum selben Thema nach denselben Regeln, damit das System automatisch ausweichen kann.

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
          art: { type: "string", enum: ["frage", "antwort", "norm", "streitstand", "merksatz", "formel", "begriff", "fehler", "tipp", "zahl"] },
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

/* ==========================================================================
   Entwurfsspeicher: Was einmal bezahlt ist, wird nicht zweimal bezahlt.

   Am 15.09. schrieb der Morgenlauf beide Texte, bezahlte 0,241 $ - und warf
   sie weg, weil eine Zeile hinter dem Faktencheck einen ReferenceError warf.
   Der Lauf endete ordentlich, der Zustand wurde gepusht, nur der Inhalt war
   nirgends: Gespeichert wird erst, was die Prüfung überstanden hat. Damit war
   das Tagesbudget verbraucht, ohne dass ein einziger Beitrag existierte.

   Deshalb liegt die Antwort des Modells jetzt auf Platte, sobald sie da ist -
   vor jeder Prüfung. Ein zweiter Lauf mit derselben Vorlage bekommt sie
   geschenkt. Der Schlüssel ist die Vorlage selbst (Modell, Systemtext,
   Auftrag, Schema): Ändert sich daran etwas - und sei es nur die
   Beanstandung, die in den zweiten Versuch wandert -, ist es ein anderer
   Auftrag und wird neu gerechnet.

   Der Speicher ist kein Ersatz für die Prüfung: Abgelegt wird der rohe
   Entwurf, geprüft wird er bei jedem Lauf aufs Neue. Ein Entwurf, der gestern
   durchgefallen ist, fällt heute wieder durch - nur eben umsonst. */
let entwurfDir = null;
export function entwurfsspeicher(dir) { entwurfDir = dir; }
const entwurfSchluessel = (o) => createHash("sha256").update(JSON.stringify(o)).digest("hex").slice(0, 16);

function entwurfLesen(schluessel) {
  if (!entwurfDir) return null;
  try {
    const p = path.join(entwurfDir, `${schluessel}.json`);
    return fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, "utf8")) : null;
  } catch { return null; }
}

/* Schlägt das Ablegen fehl, ist das kein Grund, den Beitrag zu verlieren -
   dann wird eben morgen noch einmal bezahlt. */
function entwurfAblegen(schluessel, zweck, daten) {
  if (!entwurfDir) return;
  try {
    fs.mkdirSync(entwurfDir, { recursive: true });
    fs.writeFileSync(path.join(entwurfDir, `${schluessel}.json`), JSON.stringify({ datum: heuteIso(), zweck, daten }, null, 2));
  } catch (e) { console.warn(`  ! Entwurf nicht ablegbar (${e.message})`); }
}

/* Eine Berichtigung gehört in den Speicher, nicht nur in den laufenden
   Prozess. Am 18.09. fand der Faktencheck an b2 eine Stelle, sie wurde
   ersetzt - und die Nachprüfung scheiterte an der Obergrenze des Beitrags.
   Der Speicher hielt aber den UNBERICHTIGTEN Entwurf: Der nächste Lauf hätte
   dieselbe Prüfung für 0,06 $ wiederholt, dieselbe Stelle gefunden und wäre
   an derselben Grenze gescheitert - jede Stunde, bis der Tag leer ist.
   Deshalb wird jede Ersetzung auch auf den abgelegten Entwurf angewandt. */
export function entwurfBerichtigen(schluessel, korrekturen = []) {
  if (!entwurfDir || !schluessel || !korrekturen.length) return 0;
  const gelegt = entwurfLesen(schluessel);
  if (!gelegt?.daten) return 0;
  const n = korrekturenAnwenden(gelegt.daten, korrekturen);
  if (n > 0) entwurfAblegen(schluessel, gelegt.zweck, gelegt.daten);
  return n;
}

/* Aufräumen, sonst wächst der Zweig mit jedem Tag. Drei Tage reichen: Sie
   decken den Ausfall und den Nachlauf, alles Ältere ist längst erschienen. */
export function entwuerfeAufraeumen(tage = 3, heute = heuteIso()) {
  if (!entwurfDir || !fs.existsSync(entwurfDir)) return 0;
  const grenze = new Date(new Date(`${heute}T12:00:00Z`).getTime() - tage * 86400000).toISOString().slice(0, 10);
  let weg = 0;
  for (const name of fs.readdirSync(entwurfDir)) {
    if (!name.endsWith(".json")) continue;
    const p = path.join(entwurfDir, name);
    try {
      if ((JSON.parse(fs.readFileSync(p, "utf8")).datum || "9999") >= grenze) continue;
    } catch { /* unlesbar ist so gut wie alt */ }
    fs.rmSync(p, { force: true });
    weg++;
  }
  return weg;
}

/* Ausgabedeckel je Pflichtaufgabe. 16.000 Token fuer jeden strukturierten
   Aufruf blockierten am 19.09. die Admission nach nur einem realen Aufruf,
   obwohl die fertigen Reels nur rund 2.000 Ausgabe-Token brauchten. Die Werte
   hier sind harte Provider-Ceilings, keine Zielgroessen; Telemetrie bleibt
   die Grundlage fuer spaetere Anpassungen. */
export const AUSGABE_CEILINGS = Object.freeze({ autor: 6000, reel: 4000, stories: 4500 });

/* Ein strukturierter Aufruf. Fällt bei Ablehnung oder Schema-Problemen auf
   einen zweiten Weg zurück, damit der Tageslauf nicht stehen bleibt. */
async function strukturiert({ system, user, schema, modell = CONFIG.ki.modell, effort = CONFIG.ki.effort, zweck = "autor" }) {
  const basis = {
    model: modell,
    max_tokens: AUSGABE_CEILINGS[zweck] || 6000,
    system: [{ type: "text", text: system, cache_control: { type: "ephemeral" } }],
    messages: [{ role: "user", content: user }],
    thinking: { type: "adaptive" },
    output_config: { effort, format: { type: "json_schema", schema } },
  };
  const schluessel = entwurfSchluessel({ modell, system, user, schema });
  const gelegt = entwurfLesen(schluessel);
  if (gelegt) {
    console.log(`  ↻ Entwurf aus dem Speicher vom ${gelegt.datum} (${zweck}, 0,0000 $)`);
    return { daten: gelegt.daten, usage: null, schluessel };
  }
  /* Jeder Versuch ist ein eigener bezahlter Aufruf und braucht seine eigene
     Zulassung. Der Schema-Fallback lief frueher auf der Pruefung des
     Erstaufrufs mit - ein einziger BadRequest verdoppelte damit den Preis,
     ohne dass der Deckel davon wusste. */
  let response;
  try {
    response = await claudeAufruf({ zweck, params: basis, modell, attempt: 1, slot: zweck });
  } catch (e) {
    if (e instanceof Anthropic.BadRequestError && /output_config|schema|format/i.test(e.message)) {
      const { output_config, ...ohneFormat } = basis;
      response = await claudeAufruf({
        zweck, modell, attempt: 2, slot: zweck,
        params: { ...ohneFormat, output_config: { effort }, messages: [{ role: "user", content: `${user}\n\nAntworte ausschließlich mit einem JSON-Objekt nach diesem Schema:\n${JSON.stringify(schema)}` }] },
      });
    } else throw e;
  }
  if (response.stop_reason === "refusal") {
    if (modell !== "claude-opus-4-8") return strukturiert({ system, user, schema, modell: "claude-opus-4-8", effort, zweck });
    throw new Error(`Modell hat abgelehnt: ${response.stop_details?.explanation || "ohne Begründung"}`);
  }
  if (response.stop_reason === "max_tokens") throw new Error("Antwort abgeschnitten (max_tokens)");
  const daten = jsonAus(textAus(response));
  /* Erst ablegen, dann zurückgeben: Was zwischen hier und der Prüfung schiefgeht,
     darf das Geld nicht mitnehmen. */
  entwurfAblegen(schluessel, zweck, daten);
  return { daten, usage: response.usage, schluessel };
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
  1: ["#zivilrecht", "#bgbat", "#schuldrecht", "#sachenrecht", "#zpo", "#zwangsvollstreckung", "#familienrecht", "#erbrecht", "#handelsrecht", "#arbeitsrecht"],
  2: ["#strafrecht", "#stpo", "#strafprozessrecht", "#anklageschrift", "#revisionsklausur"],
  3: ["#öffentlichesrecht", "#verwaltungsrecht", "#staatsrecht", "#grundrechte", "#verfassungsrecht", "#europarecht", "#vwgo", "#assessorklausur"],
};
const ALLE_GEBIET_TAGS = Object.values(FACH_TAGS).flat();

/* Die Faecherliste fuer das Modell wird aus der Tabelle gebaut, nicht von Hand
   gepflegt. Sonst kennt der Recherche-Auftrag ein neu angelegtes Fach nicht,
   und das Modell muss den Assessorstoff in "zpo" zwaengen - genau so ist der
   ganze Stoff des zweiten Examens urspruenglich unter dem Etikett "ZPO",
   "VwGO" und "StPO" gelandet. */
const FACH_LISTE = Object.keys(FAECHER).filter((id) => FAECHER[id].klausur !== 0).join(", ");

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
/* Letzter Ausweg vor der Neufassung: Hat der Faktencheck zu JEDEM Fehler eine
   austauschbare Wortfolge geliefert, wird sie ersetzt und der Text noch einmal
   geprüft. Ein Faktencheck kostet ein Zehntel einer Neufassung; misslingt die
   Berichtigung, geht es den bisherigen Weg. */
async function nachbessern(inhalt, fakten, pruefen, zweck = "faktencheck", schluessel = null) {
  if (!fakten.behebbar?.length || fakten.behebbar.length < fakten.fehler.length) return null;
  const n = korrekturenAnwenden(inhalt, fakten.behebbar);
  if (!n) return null;
  entwurfBerichtigen(schluessel, fakten.behebbar);
  console.warn(`  ${n} Stelle(n) berichtigt statt neu geschrieben – wird erneut geprüft.`);
  if (pruefen && !pruefen(inhalt).ok) return null;
  /* Alle harten Befunde hatten eine eindeutige Original→Ersatz-Fundstelle
     und wurden exakt angewandt. Dafür noch einmal denselben Provider zu
     bezahlen war am 19.09. ein Kostenmultiplikator: Prüfen → Korrigieren →
     Nachprüfen, obwohl die Korrektur bereits vom Prüfer stammt. Die lokale
     Strukturprüfung oben bleibt; eine weitere Provider-Runde ist keine
     Voraussetzung für die Freigabe. */
  return {
    ok: true, fehler: [],
    hinweise: [...(fakten.hinweise || []), "Alle harten Prüfbefunde wurden per exakter Fundstelle korrigiert; keine zweite Providerprüfung."],
    korrekturen: [], behebbar: [],
  };
}

/* Dieselbe Belegstelle, die der Autor beim Schreiben hatte, bekommt auch der
   Faktencheck. Sonst prüft er den Text gegen sein Gedächtnis, während der
   Autor gegen das Handbuch geschrieben hat – und beanstandet dann Fristen und
   Reihenfolgen, die genau so im Handbuch stehen. Das kostete jedes Mal eine
   Neufassung. */
export function pruefHinweis(thema) {
  const quelle = belegstelle(thema);
  if (!quelle) return "";
  return `${quelle}\n\nDer Text oben wurde auf dieser Grundlage geschrieben. Was mit der Belegstelle übereinstimmt, beanstande nicht. Was sie nicht abdeckt, prüfst du mit voller Strenge gegen Gesetz und Rechtsprechung – die Belegstelle ist eine Stütze für das, was sie sagt, kein Freibrief für das, was sie nicht sagt.`;
}

async function faktenSicher(inhalt, zweck = "faktencheck", opt = {}) {
  try {
    return await pruefeFakten(inhalt, zweck, opt);
  } catch (e) {
    /* ZUERST die Kostenkontrolle, und zwar die ganze - nicht nur die Fälle vor
       dem Senden. Ein Budgetstopp, eine gebrochene Kostenzusage
       (InvarianteVerletzt), ein Zweck ohne Topf, ein bezahlter Pfad ohne
       Laufkontext: keiner davon ist ein Ausfall des Prüfers, und keiner darf
       unten in den Degrade-Pfad geraten. Der gibt bei strikt=false
       { ok: true } zurück - „kein Geld für die Prüfung" würde dann „gilt als
       geprüft" heißen. Ein ungeprüfter Rechtsbeitrag ist teurer als ein
       fehlender. */
    if (istKostenKontrollFehler(e)) throw e;
    if (CONFIG.faktencheck.strikt) {
      throw new Error(`Faktencheck nicht möglich (${e.message.split("\n")[0].slice(0, 160)}) – der Beitrag erscheint nicht.`);
    }
    console.warn(`  ! Faktencheck nicht möglich (${e.message.split("\n")[0].slice(0, 160)}) – Entwurf wird ohne Faktencheck übernommen.`);
    /* `ausgefallen` haelt den Unterschied fest, den `ok: true` hier
       verschluckt: geprueft und bestanden gegen nicht geprueft. Der Tagesbetrieb
       darf mit dem Entwurf weiterarbeiten - der Vorrat nicht. Er wird 21 Tage
       nicht mehr angefasst, und am Blockadetag gibt es kein Geld fuer eine
       nachgeholte Pruefung. */
    return { ok: true, ausgefallen: true, fehler: [], hinweise: [`Faktencheck ausgefallen: ${e.message.slice(0, 120)}`] };
  }
}

/**
 * Haelt am Beitrag fest, WIE er freigegeben wurde - nicht nur, DASS er
 * zurueckkam. Der Tagesbetrieb liest das nicht; der Vorrat schon: Was er
 * aufnimmt, liegt bis zu 21 Tage ungeprueft, also muss die Pruefung vorher
 * wirklich gelaufen sein.
 */
function freigabeStempeln(beitrag, fakten) {
  beitrag.faktenFreigabe = {
    ok: true,
    geprueftAm: new Date().toISOString(),
    ausgefallen: !!fakten?.ausgefallen,
    hinweise: fakten?.hinweise || [],
  };
  return beitrag;
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
  if (k.einordnung?.length) zeilen.push(`Einordnung (fachlich maßgeblich, in eigenen Worten wiedergeben): ${k.einordnung.join(" ")}`);
  if (k.lernziele?.length) zeilen.push(`Worauf es ankommt: ${k.lernziele.join("; ")}`);
  if (k.pruefschritte?.length) zeilen.push(`Prüfgedanken (Systematik und Reihenfolge übernehmen, Wortlaut selbst formulieren): ${k.pruefschritte.join(" | ")}`);
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
  /* Zuletzt, damit der lange Block nicht zwischen den Stichworten steht: die
     Belegstelle aus der Wissensbasis. Sie ist der Unterschied zwischen "das
     Modell erinnert sich an die Frist" und "die Frist steht da". Fehlt der
     Schlüssel oder passt kein Kapitel, bleibt die Zeile leer und der Beitrag
     entsteht wie vor dieser Änderung. */
  zeilen.push(belegstelle(thema));
  return zeilen.filter(Boolean).join("\n");
}

/* Pille unter dem Titel und Handschrift-Hinweis daneben: nicht immer dieselben
   Worte. Die Wahl haengt am Thema, damit derselbe Beitrag beim Nachrendern
   gleich aussieht - im Feed wechselt es von Beitrag zu Beitrag. */
const PRIORITAET_TEXTE = {
  /* Die Prioritaetsstufe kommt aus dem Themeninventar. Die Pille darf diese
     Einstufung benennen, aber keine erfundene Jahreshaeufigkeit,
     Korrektorenvorliebe oder Punktwirkung daraus machen. */
  hoch: ["Hohe Examenspriorität", "Klausurrelevant", "Examensklassiker", "Sicher beherrschen", "Grundbaustein fürs Examen"],
  mittel: ["Mittlere Examenspriorität", "Gehört ins Repertoire", "Wichtig für den Aufbau", "Prüfungssicher einordnen", "Solides Examenswissen"],
  selten: ["Vertiefungsstoff", "Seltenerer Prüfungsstoff", "Gut zur Abgrenzung", "Detail mit Systembezug", "Sauber einordnen"],
};
const HINWEISE = ["So geht's!", "Swipe →", "Schau rein", "Merk dir das", "Kurz erklärt", "Das musst du wissen", "Weiter geht's →", "Lies weiter"];
const streuung = (text) => { let h = 7; for (const c of String(text)) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; };
const auswahl = (liste, seed) => liste[streuung(seed) % liste.length];
function prioritaetText(stufe, seed = "") {
  const liste = PRIORITAET_TEXTE[stufe];
  return liste ? auswahl(liste, `${stufe}:${seed}`) : "";
}

/* Nachbearbeitung: leere Felder entfernen, Titelfolie normieren, Hashtags säubern. */
const HOOK_UNBELEGT = /fast alle|die meisten|kaum jemand|niemand|jeder macht|in jeder.{0,24}klausur|kommt (?:fast )?jedes jahr|immer dran|verrät|häufigste|teuerste|volle punkte|halbe (?:klausur|punkte)|prüfer(?::innen|innen)? (?:lieben|erwarten)|garantiert|punktegeschenk/i;
const HOOK_GENERISCH = /^(kenn(?:st|en) du|das stimmt so nicht|schluss mit|so nicht,? sondern so|ein halbsatz entscheidet|die reihenfolge ist alles)[!? .]*$/i;
const HOOK_STOP = new Set(["der","die","das","den","dem","des","ein","eine","einer","eines","und","oder","mit","ohne","für","von","bei","was","wie","wann","warum","welche","welcher","welches","prüfen","prüfung"]);
const hookWoerter = (s) => String(s || "").toLocaleLowerCase("de-DE").match(/[\p{L}\p{N}§]+/gu) || [];

/* Besten Carousel-Hook wählen. Das gelernte Muster bleibt wichtig, bekommt
   aber zwei harte Leitplanken: Thema auf der ersten Kachel erkennbar und kein
   unbelegtes Clickbait-Versprechen. */
function hookWaehlen(daten, strategie, thema = null) {
  const kandidaten = [...(daten.hooks || [])];
  const erster = daten.folien?.[0]?.titel;
  if (erster && !kandidaten.some((h) => h.titel === erster)) kandidaten.unshift({ typ: hookTyp(erster), titel: erster });
  if (!kandidaten.length) return null;
  const g = strategie?.hookGewicht || {};
  const themaText = [thema?.titel, ...(thema?.normen || [])].filter(Boolean).join(" ");
  const themaWoerter = new Set(hookWoerter(themaText).filter((w) => w.length >= 4 && !HOOK_STOP.has(w)));
  const bewertet = kandidaten.map((h) => {
    const titel = String(h.titel || "").trim();
    const woerter = hookWoerter(titel);
    let p = (g[h.typ] ?? 1) * 10;
    if (woerter.length >= 5 && woerter.length <= 10) p += 3;
    else if (woerter.length > 12 || titel.length > 80) p -= 5;
    if (/\?$/.test(titel)) p += 1;
    if (themaWoerter.size && woerter.some((w) => themaWoerter.has(w))) p += 4;
    if (HOOK_UNBELEGT.test(titel)) p -= 30;
    if (HOOK_GENERISCH.test(titel)) p -= 12;
    return { ...h, p };
  }).sort((a, b) => b.p - a.p);
  return bewertet[0];
}

function nachbereiten(daten, { format, thema, fach, klausur, strategie }) {
  const hook = hookWaehlen(daten, strategie, thema);
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

export function wochenThemenPrompt(wochenThemen = []) {
  const gruppen = new Map([[1, []], [2, []], [3, []], [0, []]]);
  for (const roh of wochenThemen || []) {
    const t = typeof roh === "string" ? { titel: roh } : (roh || {});
    const titel = String(t.titel || "").trim();
    if (!titel) continue;
    const fach = t.fach || null;
    const gebiet = Number.isInteger(t.gebiet) ? t.gebiet : (FAECHER[fach]?.klausur ?? 0);
    const ziel = [1, 2, 3].includes(gebiet) ? gebiet : 0;
    const fachLabel = t.fachLabel || FAECHER[fach]?.kurz || "";
    gruppen.get(ziel).push(`${fachLabel ? `[${fachLabel}] ` : ""}${titel}`);
  }

  const abschnitt = (gebiet, label) => {
    const eintraege = gruppen.get(gebiet);
    return `### ${label}\n${eintraege.length ? eintraege.map((t) => `- ${t}`).join("\n") : "- (keine veröffentlichten Themen in diesem Gebiet)"}`;
  };
  return [
    abschnitt(1, KLAUSUREN[1].label),
    abschnitt(2, KLAUSUREN[2].label),
    abschnitt(3, KLAUSUREN[3].label),
    abschnitt(0, "Klausur- und Lernmethodik / sonstige Themen"),
  ].join("\n\n");
}

/**
 * Schreibt einen Beitrag. Prüft ihn (pruefung.mjs) und lässt bei Beanstandung
 * bis zu CONFIG.ki.maxVersuche Mal nachbessern.
 */
export async function beitragSchreiben({ format, thema, datum, recherche, wochenThemen, anlass, strategie }) {
  if (process.env.IG_AUTOR === "beispiele") return beispielBeitrag(format, thema);
  const spec = FORMATE[format] || FORMATE.pruefungsfrage;
  const fach = thema?.fach || recherche?.fach || "methodik";
  const klausur = FAECHER[fach]?.klausur ?? 3;
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
      wochenThemen?.length ? `\n## Themen dieser Woche – verbindlich nach Rechtsgebiet\n${wochenThemenPrompt(wochenThemen)}` : "",
      anlass ? `\n## Anlass\n${anlass.titel}: ${anlass.kontext}` : "",
      `\nPhase im Prüfungsjahr: ${phase(datum)}.`,
      "",
      `\n## Sperrliste (diese Namen nie verwenden)\n${sperr.join(", ")}`,
      feedback ? `\n## Beanstandungen am vorherigen Entwurf – bitte beheben\n${feedback}\n\nVorheriger Entwurf:\n${JSON.stringify(letzter)}` : "",
      `\nErstelle jetzt den Beitrag als JSON.`,
    ].filter(Boolean).join("\n");
    const { daten, schluessel } = await strukturiert({ system: SYSTEM, user, schema: BEITRAG_SCHEMA, effort: CONFIG.ki.effortBeitrag });
    const beitrag = nachbereiten(daten, { format, thema, fach, klausur, strategie });
    const ergebnis = pruefeBeitrag(beitrag);
    if (ergebnis.ok) {
      const fakten = await faktenSicher(beitrag, "faktencheck", { hinweis: pruefHinweis(thema) });
      /* Sprachversehen (doppelte oder fehlende Wörter) werden im Text ersetzt,
         nicht neu geschrieben - das kostet keinen weiteren Aufruf. */
      korrekturenAnwenden(beitrag, fakten.korrekturen);
      entwurfBerichtigen(schluessel, fakten.korrekturen);
      if (fakten.ok) { beitrag.faktenHinweise = fakten.hinweise; return freigabeStempeln(beitrag, fakten); }
      const berichtigt = await nachbessern(beitrag, fakten, pruefeBeitrag, "faktencheck", schluessel);
      if (berichtigt) { beitrag.faktenHinweise = berichtigt.hinweise; return freigabeStempeln(beitrag, berichtigt); }
      ergebnis.fehler.push(...fakten.fehler.map((f) => `Fachlicher Fehler: ${f}`));
    }
    feedback = ergebnis.fehler.map((f) => `- ${f}`).join("\n");
    letzter = daten;
    console.warn(`  Entwurf ${versuch} beanstandet:\n${feedback}`);
  }
  throw new Error(`Beitrag „${thema?.titel || format}“ nach ${CONFIG.ki.maxVersuche} Versuchen nicht freigegeben:\n${feedback}`);
}

/* Web-Recherche für das Format „aktuell“ (Server-Tool Websuche). */
/* Die Quellen sind nicht geraten, sondern geprüft: bin/quellen-pruefen.mjs
   ruft jede einzeln ab und sagt, ob sie antwortet und eine datierte Liste
   trägt. Der erste Lauf am 16.09. zeigte, wie nötig das war - von dreizehn
   Kandidaten waren zehn tot (das BVerwG benutzt .php-Pfade, der BGH hat
   keinen RSS-Feed, das BVerfG liegt unter /DE/Presse/). Eine Recherche, die
   auf tote Seiten zeigt, sucht frei weiter - und genau das kostete an
   diesem Tag 0,25 $ ohne ein einziges Ergebnis. */
const QUELLEN_JURA = `Auswahlhilfe (dort steht, WARUM eine Entscheidung examensrelevant ist - damit fängst du an):
- Aktuelle Rechtsprechung, Lehrstuhl Weiler, Uni Bielefeld: https://www.uni-bielefeld.de/fakultaeten/rechtswissenschaft/ls/weiler/aktuelle_rechtsprechung/
- FamoS, Fälle des Monats, Uni Würzburg: https://famos.jura.uni-wuerzburg.de/faelle/

Amtliche Quellen (dort holst du Aktenzeichen, Datum und die tragenden Gründe):
- BGH, Pressemitteilungen 2026: https://www.bundesgerichtshof.de/DE/Presse/Pressemitteilungen/2026/pressemitteilungen2026_node.html
- BGH, Entscheidungen: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/list.py?Gericht=bgh&Sort=3&Art=pm
- BVerfG, Pressemitteilungen: https://www.bundesverfassungsgericht.de/DE/Presse/Pressemitteilungen/pressemitteilungen_node.html
- BVerwG, Pressemitteilungen: https://www.bundesverwaltungsgericht.de/presse/pressemitteilungen/pressemitteilungen.php
- BAG: https://www.bundesarbeitsgericht.de/pressestelle/ und https://www.bundesarbeitsgericht.de/entscheidungen/
- EuGH, Pressemitteilungen: https://curia.europa.eu/jcms/jcms/Jo2_7052/de/
- dejure.org: https://dejure.org/
- Bundesgesetzblatt: https://www.recht.bund.de/bgbl`;

export async function aktuellRecherchieren(datum, bereitsBehandelt = [], gebiet = null) {
  /* Das Rechtsgebiet des Tages als Wunsch, nicht als Auftrag: Die
     Nachrichtenlage laesst sich nicht einteilen, und eine erzwungene
     Randentscheidung aus dem richtigen Gebiet waere schlechter als eine
     starke aus dem falschen. */
  const wunsch = gebiet ? `\n- Wenn die Auswahl es hergibt, nimm bevorzugt etwas aus dem ${gebiet}; heute fehlt dieses Gebiet sonst im Kanal. Zwingend ist das nicht.` : "";
  const frage = `Heute ist der ${datumLesbar(datum)}. Finde EINE aktuelle Neuigkeit der letzten 6 Wochen, die für Kandidat:innen des ersten oder zweiten juristischen Staatsexamens wirklich zählt: eine Entscheidung von BGH, BVerfG, BVerwG, BAG oder EuGH zu einem Klausurthema, eine Gesetzesänderung (BGB, StGB, StPO, ZPO, GG, VwGO, VwVfG, HGB, GmbHG, ArbR) oder eine Änderung an Juristenausbildungsgesetzen oder Prüfungsordnungen.

${QUELLEN_JURA}

So arbeitest du:
- Fang bei der Auswahlhilfe an. Diese Seiten sind kurz und datiert und sagen dir, was examensrelevant ist. Findest du dort etwas Passendes, ist die Suche beendet - such nicht weiter nach etwas noch Besserem.
- HÖCHSTENS ZWEI Suchvorgänge. Danach schreibst du mit dem, was du hast.
- Von den Besprechungen übernimmst du KEINEN Satz und KEINE Gliederung. Sie sagen dir nur, worauf es ankommt; der Beitrag entsteht aus der Entscheidung selbst, in eigenen Worten. Als Quelle nennst du die Entscheidung, nicht die Besprechung.
- KEINE kostenpflichtigen Datenbanken (beck-online, juris-Volltexte, Wolters Kluwer). Die amtlichen Gründe sind frei zugänglich.
- Lieber eine Entscheidung zu einem Klausurklassiker als eine spektakuläre Randfrage.${wunsch}

Bereits behandelt (nicht erneut): ${bereitsBehandelt.join("; ") || "–"}.

Antworte mit:
1. Titel: kurzer Titel
2. Datum und Aktenzeichen
3. Fach: eines von ${FACH_LISTE}
4. Notizen: Was ist passiert, welche Norm trägt es, was ändert sich gegenüber der bisherigen Linie, was heißt das für die Klausur (max. 200 Wörter, eigene Worte)
5. Quellen: 2–3 URLs

Findest du nach zwei Suchen nichts, was diese Maßstäbe erfüllt, antworte NUR mit dem Wort KEINE_NEUIGKEIT und sonst nichts. Das ist kein Fehler, sondern ein sauberes Ergebnis - der Beitrag entsteht dann aus dem Themenpool.`;
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
2. Fach: das passende Fach (${FACH_LISTE})
3. Notizen (max. 300 Wörter, eigene Worte): die berichteten Probleme je Aufgabe, mit Angabe, wie oft und wie sicher sie berichtet werden (mehrfach / einzeln / unsicher). Gibt es noch keine belastbaren Berichte, sage das ausdrücklich und nenne stattdessen die erfahrungsgemäßen Dauerbrenner dieses Rechtsgebiets.
4. Quellen: 2–4 URLs`;
  return webRecherche(frage, "recherche-loesung");
}

/* Web-Recherche.

   Am 16.09. hat dieser eine Aufruf beide Kanäle lahmgelegt:

     $ 0.2520 recherche · 116.2k ein / 2.0k aus / 0 Cache
       Recherche: (ohne Titel) · 0 Quellen
       ⏸ Tagesbudget erreicht (0.375 $ von 0.32 $)

   116.000 Eingabe-Token für null Quellen, geschätzt waren 0,05 $. Danach
   fielen auf beiden Kanälen alle Beiträge und Stories des Tages aus.

   Zwei Fehler steckten darin, beide hier behoben:

   1. KEIN CACHE. Ein `pause_turn` heißt: dieselbe Unterhaltung noch einmal
      schicken, damit die Suche weiterläuft. Die Suchergebnisse wachsen dabei
      mit jeder Runde - und ohne Cache-Marke wurde jede Runde der komplette
      bisherige Verlauf erneut voll bezahlt. Fünf Runden ergeben so das
      Vielfache dessen, was die Suche selbst kostet. Die Marke am Ende der
      Nachrichtenliste lässt jede Folgerunde zum Zehntel lesen.

   2. KEINE BREMSE IM LAUF. Geprüft wurde einmal vorher, mit einer Schätzung.
      Lag die daneben, lief der Aufruf trotzdem bis zum Ende. Jetzt wird vor
      jeder weiteren Runde erneut geprüft; ist der Deckel erreicht, bricht die
      Recherche mit dem ab, was sie bis dahin hat. Ein halbes Ergebnis ist
      besser als ein verlorener Tag. */
/* Runden, die eine Recherche weiterlaufen darf. Am 16.09. standen hier vier
   und die Suche war danach IMMER NOCH nicht fertig: Der letzte Durchgang
   endete mit stop_reason „pause_turn", also mitten in der Recherche, und
   lieferte deshalb keinen Text - 0,25 $ für nichts. Weniger Suchen (siehe
   rechercheAnfrage) führen schneller zu einem Ergebnis als mehr Runden. */
const RECHERCHE_RUNDEN = 3;

export function rechercheAnfrage(frage) {
  return {
    model: CONFIG.ki.modellNeben,
    max_tokens: 8000,
    thinking: { type: "adaptive" },
    output_config: { effort: CONFIG.ki.effort },
    /* Cacht den letzten cachefähigen Block der Anfrage - bei jeder weiteren
       Runde also den gesamten Verlauf samt Suchergebnissen. */
    cache_control: { type: "ephemeral" },
    tools: [{ type: "web_search_20260209", name: "web_search", max_uses: Math.min(CONFIG.ki.rechercheSuchen, 2), user_location: { type: "approximate", country: "DE", timezone: "Europe/Berlin" } }],
    messages: [{ role: "user", content: frage }],
  };
}

async function webRecherche(frage, zweck = "recherche") {
  const params = rechercheAnfrage(frage);
  /* Das Suchkontingent gilt fuer den GANZEN Auftrag. `max_uses` gilt je
     Anfrage - bei pause_turn bekam das Modell bisher wieder zwei Suchen, nach
     vier Runden also acht. Der Auftrag fuehrt jetzt den Zaehler, und jede
     Fortsetzung ist ein eigener bezahlter Aufruf mit eigener Zulassung. */
  const auftrag = rechercheAuftrag({ maxAnfragen: RECHERCHE_RUNDEN + 1 });
  const suchenSetzen = (anzahl) => {
    for (const t of params.tools || []) if (t.name === "web_search") t.max_uses = anzahl;
  };
  const erste = auftrag.anfrageBeginnen();
  suchenSetzen(erste.maxUses);
  let response = await claudeAufruf({ zweck, params, modell: CONFIG.ki.modellNeben, attempt: erste.nummer, slot: zweck });
  auftrag.antwortVerbuchen(response.usage);
  let runden = 0;
  while (response.stop_reason === "pause_turn" && runden++ < RECHERCHE_RUNDEN) {
    const darf = auftrag.darfAnfragen({ brauchtSuche: true });
    if (!darf.ok) { console.warn(`  ! Recherche nach ${runden} Runde(n) beendet: ${darf.grund}.`); break; }
    let weiter;
    try { weiter = auftrag.anfrageBeginnen(); }
    catch (e) { if (e instanceof ResearchGrenze) { console.warn(`  ! Recherche beendet: ${e.message}`); break; } throw e; }
    suchenSetzen(weiter.maxUses);
    params.messages.push({ role: "assistant", content: response.content });
    try {
      response = await claudeAufruf({ zweck, params, modell: CONFIG.ki.modellNeben, attempt: weiter.nummer, slot: zweck });
    } catch (e) {
      /* Auch hier die weite Klasse: Der Ausweg ist der Themenpool, also ein
         KOSTENLOSER Pfad - keine fachliche Freigabe. Ein gesperrter Topf oder
         eine gebrochene Zusage darf ebenso dorthin führen wie ein
         Budgetstopp; was nicht geht, ist weiterzuzahlen. */
      if (istKostenKontrollFehler(e)) {
        console.warn(`  ! Recherche nach ${runden} Runde(n) abgebrochen – die Kostenkontrolle lässt keine weitere Anfrage zu.`);
        break;
      }
      throw e;
    }
    auftrag.antwortVerbuchen(response.usage);
  }
  console.log(`  Recherche: ${auftrag.stand().anfragen} Anfrage(n), ${auftrag.stand().suchenVerbraucht} von ${auftrag.stand().maxSuchen} Suchen.`);
  const text = textAus(response);
  const fachTreffer = text.match(/Fach\s*[:：]\s*(ao|ust|erbst|kst|istr|bilanz|persg)/i);
  const quellen = [...new Set((text.match(/https?:\/\/[^\s)>\]]+/g) || []))].slice(0, 4);
  /* Eine Recherche ohne Quellen ist kein Ergebnis, sondern ein bezahlter
     Fehlschlag. Sie muss im Log auffallen, sonst sucht man die Ursache beim
     nächsten Mal wieder von vorn. */
  if (response.stop_reason === "pause_turn") console.warn(`  ! Recherche (${zweck}) war nach ${RECHERCHE_RUNDEN} Runden immer noch am Suchen – abgebrochen, der Beitrag entsteht ohne sie.`);
  else if (!quellen.length) console.warn(`  ! Recherche (${zweck}) ohne Quellen und ohne verwertbaren Text – der Aufruf ist bezahlt, das Ergebnis leer.`);
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
- streitstand: der Meinungsstreit, wie ihn die Klausur verlangt. titel = die Streitfrage als Frage (max. 80 Zeichen), norm = die Norm, um die gestritten wird, optionen = GENAU ZWEI Ansichten, jede in der Form „Label: Aussage" – das Label ist die Zuordnung („Rechtsprechung", „h.M.", „Literatur", „a.A.", „Eingeschränkte Schuldtheorie"), die Aussage sagt in einem Satz, was diese Ansicht annimmt (je max. 110 Zeichen). text = der STREITENTSCHEID: welcher Ansicht du folgst und mit welchem Argument, plus – wenn beide zum selben Ergebnis kommen – der Satz, dass der Streit hier dahinstehen kann (max. 190 Zeichen). Nimm nur Streitstände, die es wirklich gibt, und ordne die Ansichten korrekt zu; erfinde keine Meinungen.
- merksatz: text = ein Satz, der hängen bleibt (max. 120 Zeichen), titel = Thema (max. 60 Zeichen)
- formel: titel = Name des Rechenwegs, formel = Formel (max. 60 Zeichen), text = Erklärung mit eigenem Zahlenbeispiel (max. 180 Zeichen)
- begriff: titel = Begriff, norm = Norm, text = Definition in eigenen Worten (max. 200 Zeichen), icon
- fehler: titel = die Falle (max. 70 Zeichen), falsch = der Fehler (max. 120 Zeichen), richtigText = die richtige Lösung mit Norm (max. 160 Zeichen)
- tipp: titel = Klausurtipp (max. 70 Zeichen), text = Umsetzung (max. 180 Zeichen), icon
- bildSzene (nur bei begriff und tipp, sonst null): eine ENGLISCHE, fotografierbare Alltagsszene in 3–6 Wörtern, nach der sich in einer Fotodatenbank suchen lässt und die das Thema bildlich greifbar macht („woman reading letter at kitchen table“). Keine Fachvokabeln, keine abstrakten Begriffe, keine Symbolbild-Klassiker (Richterhammer, Waage, Gesetzbuch, Taschenrechner, Münzstapel, Händedruck). Nur Motive, die ganz im Bild sind – eine Person vom Kopf bis zur Hüfte, ein Gegenstand mit Rand ringsum. Beschreibe ein Schriftstück NIE über das, was daraufsteht, sondern über Form und Zustand („folded letter with wax seal“, „stapled document with sections“, „open ring binder“) - und meide Motive, die von Beschriftung leben (Briefumschlag mit Aufdruck, Schild, Etikett, Buchdeckel, Urkunde, Stempel). Das Zeichenmodell schreibt sonst englische Wörter ins Bild, und zwar falsch geschrieben: Am 18.09. stand „GERITIFIEID MAIL“ auf dem Titelbild eines Beitrags zum Öffentlichen Recht. Fällt dir keine echte Szene ein: null.
- zahl: zahl = eine markante Zahl/Frist/Prozentsatz (max. 8 Zeichen), titel = was sie bedeutet (max. 60 Zeichen), text = Norm und Kontext (max. 160 Zeichen)

Aufträge:
${auftraege}

Sperrliste (Namen nie verwenden): ${korpus().namen.join(", ")}

Alles in eigenen Worten, juristisch korrekt, mit Norm. Nicht benötigte Felder null. Gib genau einen Eintrag je Slot zurück.${hinweis ? `\n\n${hinweis}` : ""}`;
  const { daten } = await strukturiert({ system: SYSTEM, user, schema: STORY_SCHEMA, modell: CONFIG.ki.modellNeben, effort: CONFIG.ki.effort, zweck: "stories" });
  const nachSlot = new Map(daten.stories.map((s) => [s.slot, s]));
  const liste = plan.map((p) => {
    const s = nachSlot.get(p.slot) || {};
    const o = { slot: p.slot, art: p.art, fach: p.thema?.fach || "methodik", klausur: p.thema?.klausur ?? 3 };
    /* Frage und Antwort gehoeren zusammen und muessen das auch nach einem
       einzelnen Neuversuch noch wissen. Bis es ein eigenes Quiz-Objekt gibt,
       traegt das Thema die Klammer. */
    if (p.thema?.id) o.pairId = p.thema.id;
    for (const [k, v] of Object.entries(s)) if (v != null && k !== "slot" && k !== "art") o[k] = v;
    if (o.icon && !ICONS[o.icon]) o.icon = "paragraf";
    if (p.art === "countdown") { o.zahl = String(p.tageBisExamen); o.fortschritt = Math.round(100 - Math.min(100, p.tageBisExamen / 150 * 100)); o.ueberzeile = "Noch"; }
    o.fachLabel = FAECHER[o.fach]?.label || "Examenswissen";
    felderKuerzen(o, ["titel", "text", "norm", "formel", "richtigText", "falsch", "ueberzeile"]);
    /* Auch in den Ansichten eines Streitstands steht die Kurzform auf der
       Kachel - dort stecken die meisten Normzitate der Story. */
    if (Array.isArray(o.optionen)) o.optionen = o.optionen.map((x) => normKurz(String(x)));
    const ergebnis = pruefeBeitrag({ stories: [o] });
    if (!ergebnis.ok) { o.beanstandet = ergebnis.fehler; }
    /* Die Marke sagt spaeteren Laeufen, dass die Befunde dieser Story nach
       Herkunft getrennt sind. Ohne sie gilt ein Befund als ungeklaert. */
    o.befundeTypisiert = true;
    return o;
  });
  /* Quiz-Invarianten ueber die ganze Lieferung: Einzelbefunde und die
     Paarpruefung zwischen Frage und Antwort. Deterministisch, kostenlos, und
     genau der Fall vom 16.09. */
  for (const f of quizBefunde(liste)) {
    const treffer = String(f).match(/\[(s\d+)\]/);
    const ziele = treffer ? liste.filter((o) => o.slot === treffer[1]) : liste;
    for (const o of ziele) (o.beanstandet ||= []).push(String(f));
  }

  return storiesPruefen(liste);
}

/* Faktencheck über alle Stories des Tages in einem Aufruf. Beiträge und
   Reels liefen von Anfang an dagegen, Stories nicht - dabei sind sie neun
   von elf Veröffentlichungen am Tag, und die erste live gegangene Story trug
   prompt eine falsch zugeordnete Norm. Befunde landen in `beanstandet`;
   damit greift die Schleife im Tageslauf, die beanstandete Slots ohnehin
   einmal neu schreiben lässt.

   Reicht das Budget für die Prüfung nicht, fliegt der Aufruf nicht mehr
   heraus: Die Texte sind geschrieben und bezahlt, sie tragen dann
   `faktencheckOffen` und warten gespeichert auf ihre Prüfung. Ein späterer
   Lauf holt sie nach, ohne sie noch einmal schreiben zu lassen. Ungeprüft
   erscheint keine von ihnen. Am 16.09. gingen an dieser Stelle auf dem
   Schwesterkanal neun bezahlte Story-Texte verloren, weil der Fehler den
   ganzen Aufruf mitnahm. */
export async function storiesPruefen(liste) {
  if (!liste.length) return liste;
  try {
    const fakten = await faktenSicher({ stories: liste }, "story-faktencheck", {
      hinweis: "Jede Kachel steht für sich - mit einer Ausnahme: Was unter [QuizPair] steht, ist EIN Gegenstand. Frage und Antwort gehören dort zusammen, und du beanstandest ausdrücklich, wenn die als richtig markierte Option fachlich nicht die richtige ist oder wenn Frage und Antwort einander widersprechen. Nenne zu jedem Befund den Slot in eckigen Klammern, genau so, wie er im Kopf der Kachel steht (zum Beispiel [s5]).",
    });
    korrekturenAnwenden({ stories: liste }, fakten.korrekturen);
    /* Das Ergebnis dieser Pruefung wird erst gesammelt und dann als Ganzes
       gesetzt: Eine fachliche Vollpruefung ersetzt die fachlichen Befunde der
       geprueften Fassung, sie haengt sie nicht an. Findet sie nichts, ist der
       alte fachliche Befund erledigt - sonst haette eine einmal beanstandete
       Kachel keinen Weg zurueck, auch wenn der Text laengst korrigiert ist.
       Befunde anderer Herkunft (Form, Quiz) bleiben unberuehrt. */
    const neueBefunde = liste.map(() => []);
    for (const f of fakten.fehler || []) {
      const treffer = String(f).match(/\[?\b(s\d+)\b\]?/);
      /* Ohne erkennbaren Slot lässt sich der Befund keiner Kachel zuordnen -
         dann werden lieber alle neu geschrieben als eine falsche zu posten. */
      liste.forEach((o, i) => { if (!treffer || o.slot === treffer[1]) neueBefunde[i].push(String(f)); });
    }
    /* Fachliche Befunde in ihr eigenes Feld, mit Stempel der geprueften
       Fassung: Ein spaeterer Formcheck darf sie nicht schliessen (Safety 0c),
       eine spaetere Vollpruefung derselben Fassung schon. */
    liste.forEach((o, i) => fachpruefungAbschliessen(o, neueBefunde[i]));
  } catch (e) {
    /* Nicht nur beim Budget: Auch ein technischer Ausfall der Prüfung
       (API-Störung, unlesbares Ergebnis) darf die bezahlten Texte nicht
       mitreißen. Sie bleiben gespeichert, tragen `faktencheckOffen` und
       werden im nächsten Lauf geprüft. Ungeprüft erscheint keine. */
    if (istKostenKontrollFehler(e)) console.warn(`  ⏸ ${e.message.split("\n")[0]} – die Story-Texte bleiben gespeichert und werden im nächsten Lauf geprüft.`);
    else console.warn(`  ! Story-Faktencheck ausgefallen (${e.message.split("\n")[0].slice(0, 120)}) – die Texte bleiben gespeichert und werden im nächsten Lauf geprüft.`);
    for (const o of liste) o.faktencheckOffen = true;
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
          marken: { type: "array", items: { type: "string" } },
          bildSzene: { type: ["string", "null"] },
          kreuz: { type: "boolean" },
        },
        required: ["art", "nummer", "titel", "unter", "text", "norm", "icon", "sprecher", "marken", "bildSzene", "kreuz"],
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
- icon nur beim hook.
- Genauigkeit im Sprechertext: Jede Voraussetzung, die an einer Person hängt, nennt diese Person mit ihrer Rolle – „der Vertragspartner muss wissen“, „der Erwerber schuldet“ –, nie „der andere“, „man“ oder „eine beteiligte Person“. Staffelt das Gesetz oder die Rechtsprechung einen Wert nach Fallgruppen, nennst du die Staffelung („über 85 Prozent bei kleinem, über 90 Prozent bei großem Vermögen“), nicht eine verschmolzene Spanne. Hängt eine Rechtsfolge an mehr als einer Voraussetzung, nennst du die tragende mit – fünf Wörter mehr sind billiger als ein Fehler, der dauerhaft im Feed steht.
- Keine Behauptungen über Häufigkeit, die du nicht belegen kannst: nicht „der häufigste Fehler“, nicht „die meisten übersehen“ – sondern „ein typischer Aufbaufehler“.
- Der Bildschirmtext der Hook-Szene trägt die Frage oder Entscheidung selbst – das Wort, um das es geht („Vertrag wirksam?“, „Wer haftet?“, „Strafbar?“), nicht nur den Sachverhalt. Wer ohne Ton schaut, muss in der ersten Sekunde sehen, was auf dem Spiel steht.
- kurztitel verspricht genau das, was das Reel liefert: Fünf Vorfragen heißen „5 Vorfragen“, nicht „Lösungsaufbau“; ein Ausschnitt heißt nicht „das komplette Schema“.
- Die Weiterleitungs-Aufforderung in der cta-Szene nennt den Empfänger konkret und aus dem Inhalt heraus („Schick das der Person in deiner Lerngruppe, die 85 und 90 immer verwechselt“), nicht allgemein „Schick das deiner Lerngruppe“.

### Felder für die Bühnen-Darstellung
Das Reel wird abwechselnd in zwei Layouts gebaut. Die folgenden drei Felder braucht das zweite – fülle sie IMMER aus, auch wenn du nicht weißt, welches gerade dran ist.
- marken: ein bis zwei sehr kurze Stichwortzeilen je Szene, die den Kern der Szene tragen. 2 bis 6 Wörter, KEIN ganzer Satz, kein Punkt am Ende. Sie stehen groß auf der Bühne, während die Stimme erklärt – sie wiederholen den Sprechertext also nicht, sie verdichten ihn. Genau EIN Wort je Zeile setzt du in *Sternchen*; das wird farbig hervorgehoben, und es muss das Wort sein, auf das es ankommt. Jede Norm auf der Bühne trägt ihr Gesetz – „§ 20 BGB", nie „§ 20"; bei zwei Normen desselben Gesetzes genügt es einmal am Ende („§ 9 + § 11 BGB"). Ein Paragraf ohne Gesetz wird abgelehnt. Beispiele: „Schuldner *bietet an*“, „§ 294 BGB: *tatsächliches* Angebot“, „Frist *entbehrlich*“. Bei der cta-Szene genügt eine Zeile.
- bildSzene je Szene: eine ENGLISCHE Beschreibung dessen, was zu DIESER Szene gezeigt wird – 3 bis 6 Wörter. Sie wird freigestellt groß neben den Text gestellt.
  ZUERST der Gegenstand, nicht der Mensch. Zeige das Ding, um das es juristisch geht: die Akte, den Bescheid, das Urteil, den Vertrag, die Anklageschrift, das Grundbuch, die Tatwaffe, das Schriftstück, die Frist im Kalender. Nur wenn die Szene wirklich von einer HANDLUNG einer Person lebt („der Gläubiger nimmt nicht an“), darf eine Person vorkommen. Steht keine Person in der Beschreibung, wird auch keine gezeichnet – das ist so gewollt.
  Entscheidend ist der Fachbezug, nicht die Pantomime. Falsch wäre für das steuerliche Einlagekonto „person adding coins to jar“: Münzen in einem Glas könnten zu jedem Thema der Welt gehören. Richtig wären Dinge, die in genau diesem Thema wirklich vorkommen – für die Anklageschrift „stapled court document with sections“, für die Zwangsvollstreckung „sealed enforcement order with stamp“. Prüfe jede Beschreibung mit der Gegenfrage: „Könnte dieses Bild genauso gut zu einem ganz anderen juristischen Thema gehören?“ Wenn ja, ist es zu allgemein – such etwas Spezifischeres.
  Jede Szene bekommt ihr eigenes Bild; gib nicht zweimal dieselbe oder eine fast gleiche Beschreibung an. Keine Fachvokabeln im Bildauftrag („anwartschaftsrecht“, „revision“ – das Modell malt sonst Buchstaben), keine Symbolbild-Klassiker (Waage vor Bücherwand, Richterhammer, Handschlag im Anzug, Paragrafenzeichen), keine Gruppen.
  Schriftstücke ohne lesbare Beschriftung: kein Schild, kein Etikett, keine Urkunde mit Titelzeile, kein Formular mit Feldnamen – das Modell schreibt sonst englische Wörter ins Bild („FARMHOUSE DEED“), und die stehen dann groß im Reel. Beschreibe ein Schriftstück über Form und Zustand („folded letter with wax seal“, „stapled document with sections“), nie über das, was daraufsteht.
  Fällt dir für eine Szene nichts ein, das wirklich zu ihrer Aussage passt: null. Dann übernimmt sie das Motiv der vorherigen Szene, und das ist besser als ein Bild, das danebenliegt.
- kreuz: true genau dann, wenn die letzte marken-Zeile etwas benennt, das gerade NICHT gilt oder NICHT nötig ist („Verschulden nötig?“, „Fristsetzung erforderlich?“). Dann wird ein rotes Kreuz danebengesetzt. Sonst false. Höchstens eine Szene je Reel bekommt true.`;

/* Reel-Skript schreiben (Szenen mit Bildschirm- und Sprechertext). */
export async function reelSchreiben({ thema, datum, lang = false, anlass = null, strategie = null }) {
  const fach = thema?.fach || "methodik";
  const klausur = FAECHER[fach]?.klausur ?? 3;
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
      "\n## Cover-Motiv\nbildSzene: eine ENGLISCHE, fotografierbare Alltagsszene in 3–6 Wörtern für das Standbild des Reels, nach der sich in einer Fotodatenbank suchen lässt und die das Thema bildlich greifbar macht („woman reading letter at kitchen table“). Keine Fachvokabeln, keine abstrakten Begriffe, keine Symbolbild-Klassiker (Richterhammer, Waage, Gesetzbuch, Taschenrechner, Münzstapel, Händedruck). Nur Motive, die ganz im Bild sind – eine Person vom Kopf bis zur Hüfte, ein Gegenstand mit Rand ringsum; keine Gruppen, keine Nahaufnahmen, keine Bewegungsunschärfe. Beschreibe ein Schriftstück NIE über das, was daraufsteht, sondern über Form und Zustand („folded letter with wax seal“, „stapled document with sections“, „open ring binder“) - und meide Motive, die von Beschriftung leben (Briefumschlag mit Aufdruck, Schild, Etikett, Buchdeckel, Urkunde, Stempel). Das Zeichenmodell schreibt sonst englische Wörter ins Bild, und zwar falsch geschrieben: Am 18.09. stand „GERITIFIEID MAIL“ auf dem Titelbild eines Beitrags zum Öffentlichen Recht. Fällt dir keine echte Szene ein: null.\nbildSzeneAlt: eine zweite, andere Szene nach denselben Regeln als Ersatz, sonst null.",
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
    const { daten, schluessel } = await strukturiert({ system: SYSTEM, user, schema: REEL_SCHEMA, zweck: "reel", effort: CONFIG.ki.effortReel });
    const szenen = daten.szenen.map((s) => {
      const o = {};
      for (const [k, v] of Object.entries(s)) if (v != null) o[k] = v;
      if (o.icon && !ICONS[o.icon]) o.icon = "paragraf";
      /* Auf dem Bildschirm die Kurzform, in der Stimme die ausgeschriebene
         Fassung – „(1)“ würde sonst als „Klammer auf eins“ vorgelesen. */
      felderKuerzen(o, ["titel", "unter", "text", "norm"]);
      /* Die Stichwortzeilen der Buehne sind Bildschirmtext: Kurzform, und die
         Sternchen-Markierung bleibt stehen. */
      if (Array.isArray(o.marken)) o.marken = o.marken.map((m) => normKurz(String(m))).filter(Boolean).slice(0, 2);
      if (o.sprecher) o.sprecher = normGesprochen(o.sprecher);
      return o;
    });
    const reel = { format: "reel", fach, klausur, fachLabel: FAECHER[fach]?.label, themaId: thema?.id || null, szenen, caption: normKurz((daten.caption || "").trim()), hashtags: [...new Set([...(daten.hashtags || []).map((h) => (h.startsWith("#") ? h : `#${h}`).toLowerCase()), ...CONFIG.hashtags.kern])].slice(0, CONFIG.hashtags.maxJeBeitrag), kurztitel: daten.kurztitel || szenen[0]?.titel || "", bildSzene: daten.bildSzene || null, bildSzeneAlt: daten.bildSzeneAlt || null };
    /* Prüfung über die Folien-Logik: Szenen als Folien, Sprechertext als Text. */
    const ergebnis = pruefeBeitrag({ folien: [{ art: "titel", titel: szenen[0]?.titel || "" }, ...szenen.slice(1).map((s) => ({ art: "text", titel: s.titel, text: `${s.text || ""} ${s.sprecher}` })), { art: "cta" }], caption: reel.caption, hashtags: reel.hashtags });
    ergebnis.fehler.push(...pruefeHook(szenen[0]));
    /* Bühnentext: Jede Norm auf einer Stichwortzeile braucht ihr Gesetz. */
    for (const s of szenen) {
      for (const m of s.marken || []) {
        const nackt = normenOhneGesetz(m);
        if (nackt.length) ergebnis.fehler.push(`Stichwortzeile „${m}“ nennt ${nackt.join(", ")} ohne Gesetz – auf der Bühne immer mit Gesetz („§ 20 BGB“)`);
      }
      if (s.norm && normenOhneGesetz(s.norm).length) ergebnis.fehler.push(`Norm „${s.norm}“ ohne Gesetz`);
    }
    /* Auch die Stimme nennt das Gesetz. Geprüft wird der ganze Sprechtext am
       Stück: Wird das Gesetz irgendwo danach genannt, reicht das der Hörerin;
       wird es NIE genannt (Campus-Reel vom 17.09.: „Paragraf 3 oder Paragraf 7
       Absatz 1 Nummer 1“, kein ErbStG), ist das ein Fehler. */
    const nacktGesprochen = normenOhneGesetz(szenen.map((s) => s.sprecher || "").join(" "));
    if (nacktGesprochen.length) ergebnis.fehler.push(`Sprechertext nennt ${[...new Set(nacktGesprochen)].join(", ")} ohne Gesetz – auch gesprochen gehört das Gesetz dazu („Paragraf 1365 BGB“)`);
    /* Die Annahmegrenze folgt dem gewählten Zeitfenster. Stand sie fest, wurde
       jedes längere Reel abgelehnt, obwohl die Anleitung genau diese Länge
       verlangt hatte - ein Nachschlag pro Reel, und nach drei Versuchen gar
       kein Reel. Die Toleranz ist großzügig: Ein paar Wörter mehr verschieben
       die Dauer um Sekunden, nicht um ein Fenster. */
    const woerter = szenen.reduce((n, s) => n + s.sprecher.split(/\s+/).length, 0);
    const zielVon = Math.round(von * WOERTER_JE_SEKUNDE), zielBis = Math.round(bis * WOERTER_JE_SEKUNDE);
    const min = Math.round(zielVon * 0.75), max = Math.round(zielBis * 1.25);
    /* Das gelernte Zeitfenster ist ein Optimierungsziel, kein Grund fuer eine
       bezahlte Neufassung. Neu geschrieben wird nur, wenn die absolute
       technische Reel-Grenze gerissen wuerde. */
    const absolutMax = Math.round(CONFIG.reel.maxSekunden * WOERTER_JE_SEKUNDE);
    if (woerter > absolutMax) ergebnis.fehler.push(`Sprechertext hat ${woerter} Wörter (absolute Grenze ${absolutMax})`);
    else if (woerter < min || woerter > max) console.warn(`  ! Reel-Laenge ${woerter} Wörter außerhalb Ziel ${zielVon}–${zielBis}; wird ohne bezahlte Neufassung verwendet.`);
    if (!ergebnis.fehler.length) {
      /* Mindset-Reels enthalten bewusst keinen Rechtsstoff. Ein bezahlter
         juristischer Faktencheck hat hier am 19.09. Budget gebunden, ohne
         Rechtsaussagen zu pruefen. Form, Laenge und Sprechertext sind bereits
         deterministisch geprueft; fachliche Reels behalten den Providercheck. */
      const fakten = thema?.typ === "mindset"
        ? { ok: true, fehler: [], hinweise: ["Mindset-Reel: kein bezahlter Rechts-Faktencheck nötig."], korrekturen: [], behebbar: [] }
        : await faktenSicher(reel, "reel-faktencheck", { hinweis: pruefHinweis(thema) });
      korrekturenAnwenden(reel, fakten.korrekturen);
      entwurfBerichtigen(schluessel, fakten.korrekturen);
      if (fakten.ok) { reel.hookTyp = hookTypErkennen(szenen[0]?.titel || "", szenen[0]?.sprecher || ""); reel.hookMuster = hookMuster; await bildregieSicher(reel); return reel; }
      const berichtigtesReel = await nachbessern(reel, fakten, null, "reel-faktencheck", schluessel);
      if (berichtigtesReel) { reel.hookTyp = hookTypErkennen(szenen[0]?.titel || "", szenen[0]?.sprecher || ""); reel.hookMuster = hookMuster; await bildregieSicher(reel); return reel; }
      ergebnis.fehler.push(...fakten.fehler.map((f) => `Fachlicher Fehler: ${f}`));
    }
    feedback = ergebnis.fehler.map((f) => `- ${f}`).join("\n");
    letzter = daten;
    console.warn(`  Reel-Entwurf ${versuch} beanstandet:\n${feedback}`);
  }
  throw new Error(`Reel „${thema?.titel}“ nach ${CONFIG.ki.maxVersuche} Versuchen nicht freigegeben:\n${feedback}`);
}

/* Teaser-Story aus einem fertigen Beitrag – ohne KI-Aufruf. */

/* ==========================================================================
   Bildregie: ein zweiter Blick auf die Motive des Erklaervideos.

   Am 17.09. trug ein Reel zur Erbschaftsteuer diese Motive: ein Notizblock
   fuer „fuenf Punkte", zwei Briefumschlaege fuer „Schenkung oder Erbfall",
   Pass und Schluessel fuer die Steuerpflicht. Alles Metaphern - nichts,
   woran jemand den Inhalt erkennt. Der Autor hatte eine strenge Anleitung
   und hat sie beim Schreiben trotzdem beiseitegelegt, weil er in dem Moment
   den TEXT baut, nicht das Bild.

   Deshalb fragt ein eigener, billiger Aufruf hinterher je Szene: Zeigt das
   Motiv den Gegenstand, um den es hier fachlich geht? Und wenn nicht: welchen
   dann? Ein Aufruf je Reel, das guenstige Modell, wenige Cent. Faellt er
   aus (Budget, Netz), bleiben die Motive des Autors - lieber so als kein
   Reel.
   ========================================================================== */
const BILDREGIE_SCHEMA = {
  type: "object", additionalProperties: false,
  properties: { szenen: { type: "array", items: { type: "object", additionalProperties: false,
    properties: { nr: { type: "integer" }, passt: { type: "boolean" }, grund: { type: "string" }, besser: { type: ["string", "null"] } },
    required: ["nr", "passt", "grund", "besser"] } } },
  required: ["szenen"],
};
const BILDREGIE_SYSTEM = `Du bist Bildredakteur:in eines Instagram-Kanals für das Recht. Du bekommst die Szenen eines Erklärvideos: Titel, Sprechertext und das vorgeschlagene Motiv (englisch, wird als freigestellte Illustration groß neben den Text gesetzt).

Beurteile jedes Motiv mit EINER Frage: Zeigt es den Gegenstand, um den es in DIESER Szene fachlich geht – so, dass eine Examenskandidat:in es beim Zusehen sofort dem Inhalt zuordnet? Metaphern gelten NICHT: Briefumschläge für „Erbfall oder Schenkung", ein Notizblock für „fünf Prüfungspunkte", ein Pass für „Steuerpflicht", Münzen für „Bewertung", eine Waage für „Abwägung" – das könnte jedes Thema der Welt sein. Auch ein Motiv, das nur zum Oberthema passt, aber nicht zu dieser Szene, passt nicht.

Passt es nicht, nenne ein besseres: englisch, 3 bis 8 Wörter, EIN Gegenstand, keine Schrift im Bild, keine Person (außer die Szene lebt von einer Handlung), kein Symbolbild-Klassiker. Nimm die Dinge, die in diesem Rechtsgebiet wirklich vorkommen: Klageschrift mit Gerichtsstempel, Urteil mit Siegel, Anklageschrift, Bescheid mit Rechtsbehelfsbelehrung, Kaufvertrag mit zwei Unterschriften, Mietvertrag, Grundbuchauszug, Kalenderblatt mit markierter Frist, Mahnbescheid, Vollstreckungstitel, Testament, Führerschein, Tatwaffe (Messer, Brecheisen), Handschellen, Versammlungsplakat, Baugenehmigung. Der Gegenstand muss zur Aussage der Szene passen, nicht nur zum Thema des Reels – zwei Szenen desselben Reels bekommen nie dasselbe Motiv. Fällt dir nichts ein, das wirklich passt: besser = null und passt = false; dann übernimmt die Szene das Motiv der Nachbarszene.`;

export async function bildregie(reel) {
  const szenen = reel?.szenen || [];
  if (!szenen.some((s) => s.bildSzene)) return { geprueft: 0, ersetzt: 0 };
  const user = `Reel-Thema: ${reel.kurztitel || szenen[0]?.titel || ""}\n\n${szenen.map((s, i) => `Szene ${i + 1} [${s.art}]\n  Titel: ${s.titel || ""}\n  Sprecher: ${s.sprecher || ""}\n  Motiv: ${s.bildSzene || "(keins)"}`).join("\n\n")}\n\nBeurteile jede Szene.`;

  let response;
  try {
    response = await claudeAufruf({
      zweck: "bildregie", modell: CONFIG.ki.modellNeben, slot: reel?.slug || "reel", optional: true,
      params: {
        model: CONFIG.ki.modellNeben, max_tokens: 3000,
        system: [{ type: "text", text: BILDREGIE_SYSTEM, cache_control: { type: "ephemeral" } }],
        messages: [{ role: "user", content: user }],
        thinking: { type: "adaptive" },
        output_config: { effort: "low", format: { type: "json_schema", schema: BILDREGIE_SCHEMA } },
      },
    });
  } catch (e) {
    if (istKostenKontrollFehler(e)) throw e;
    console.warn(`  ! Bildregie nicht möglich (${e.message.split("\n")[0].slice(0, 100)}) – Motive des Autors bleiben.`);
    return { geprueft: 0, ersetzt: 0 };
  }

  let daten;
  try { const t = textAus(response); daten = JSON.parse(t.slice(t.indexOf("{"), t.lastIndexOf("}") + 1)); }
  catch { console.warn("  ! Bildregie: Antwort nicht lesbar – Motive des Autors bleiben."); return { geprueft: 0, ersetzt: 0 }; }
  let ersetzt = 0;
  for (const u of daten?.szenen || []) {
    const s = szenen[Number(u.nr) - 1];
    if (!s || u.passt) continue;
    const besser = typeof u.besser === "string" && u.besser.trim().split(/\s+/).length >= 2 ? u.besser.trim() : null;
    console.log(`  Bildregie Szene ${u.nr}: „${s.bildSzene}“ passt nicht (${String(u.grund || "").slice(0, 90)})${besser ? ` → „${besser}“` : " → Motiv der Nachbarszene"}`);
    s.bildSzene = besser;
    ersetzt++;
  }
  return { geprueft: (daten?.szenen || []).length, ersetzt };
}


/* Die Regie darf das Reel nie kosten: Budget- und Netzfehler werden gemeldet,
   das Reel geht mit den Motiven des Autors weiter. */
export async function bildregieSicher(reel) {
  if (!reel || reel.bildregie) return false;
  try { const r = await bildregie(reel); if (r.geprueft) console.log(`  Bildregie: ${r.ersetzt} von ${r.geprueft} Motiven ersetzt.`); reel.bildregie = true; return true; }
  catch (e) { console.warn(`  ! Bildregie übersprungen (${e.message.split("\n")[0].slice(0, 100)}) – Motive des Autors bleiben.`); return false; }
}

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
    bildBreite: beitrag.folien[0].bildBreite || null, bildHoehe: beitrag.folien[0].bildHoehe || null,
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
