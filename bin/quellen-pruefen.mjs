#!/usr/bin/env node
/**
 * Prüft, welche Recherche-Quellen tatsächlich erreichbar sind und was sie
 * liefern. Kostet nichts: kein einziger Modellaufruf, nur HTTP-Abrufe.
 *
 * Hintergrund: Am 16.09. kostete ein einziger Recherche-Aufruf 0,25 $ und
 * lieferte keinen Beitrag. Bevor daran etwas geändert wird, muss feststehen,
 * welche Seiten es überhaupt gibt und welche davon eine kurze, datierte
 * Liste liefern - denn genau das macht eine Recherche billig: Das Modell
 * sucht nicht ins Blaue, sondern liest eine Übersicht.
 *
 * Aufruf: node bin/quellen-pruefen.mjs   (oder Workflow-Modus „quellen")
 */

const ZEITLIMIT = 20000;

/* Kandidaten. „rss" ist eine maschinenlesbare Liste, „liste" eine
   Übersichtsseite mit Datum, „nachschlag" eine Seite zum gezielten
   Nachschlagen einer schon bekannten Fundstelle. Kostenpflichtige
   Datenbanken (beck-online, juris, Wolters Kluwer) stehen bewusst nicht
   hier - deren Inhalte dürfen nicht weitergegeben werden. */
const QUELLEN = [
  { name: "BGH · Pressemitteilungen (RSS)", art: "rss", url: "https://www.bundesgerichtshof.de/SiteGlobals/Functions/RSSFeed/DE/Pressemitteilungen/RSSNewsfeed_Pressemitteilungen.xml" },
  { name: "BGH · Pressemitteilungen 2026", art: "liste", url: "https://www.bundesgerichtshof.de/DE/Presse/Pressemitteilungen/2026/pressemitteilungen2026_node.html" },
  { name: "BVerfG · Pressemitteilungen", art: "liste", url: "https://www.bundesverfassungsgericht.de/DE/Aktuelles/Pressemitteilungen/pressemitteilungen_node.html" },
  { name: "BVerfG · Entscheidungen (RSS)", art: "rss", url: "https://www.bundesverfassungsgericht.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed/RSSNewsfeed.xml" },
  { name: "BVerwG · Pressemitteilungen", art: "liste", url: "https://www.bundesverwaltungsgericht.de/pressemitteilungen" },
  { name: "BAG · RSS-Übersicht", art: "liste", url: "https://www.bundesarbeitsgericht.de/rss-feeds/" },
  { name: "BAG · Pressemitteilungen (RSS)", art: "rss", url: "https://www.bundesarbeitsgericht.de/rss/pressemitteilungen.xml" },
  { name: "EuGH · Pressemitteilungen", art: "liste", url: "https://curia.europa.eu/jcms/jcms/Jo2_16799/de/" },
  { name: "Rechtsprechung im Internet", art: "nachschlag", url: "https://www.rechtsprechung-im-internet.de/" },
  { name: "Gesetze im Internet", art: "nachschlag", url: "https://www.gesetze-im-internet.de/" },
  { name: "Bundesgesetzblatt (recht.bund.de)", art: "liste", url: "https://www.recht.bund.de/bgbl" },
  { name: "dejure.org", art: "nachschlag", url: "https://dejure.org/" },
  { name: "openJur", art: "nachschlag", url: "https://openjur.de/" },
];

const kurz = (s, n = 70) => String(s).replace(/\s+/g, " ").trim().slice(0, n);

/* Aus einem RSS-Feed die neuesten Einträge ziehen - ohne Bibliothek, der
   Feed ist flach genug dafür. */
function rssEintraege(text, wieviele = 3) {
  const items = [...text.matchAll(/<item[\s>][\s\S]*?<\/item>/gi)].slice(0, wieviele);
  return items.map((m) => {
    const block = m[0];
    const titel = block.match(/<title>(?:<!\[CDATA\[)?([\s\S]*?)(?:\]\]>)?<\/title>/i)?.[1] || "?";
    const datum = block.match(/<pubDate>([\s\S]*?)<\/pubDate>/i)?.[1] || "";
    return `${datum ? `${kurz(datum, 25)} · ` : ""}${kurz(titel, 80)}`;
  });
}

/* Wie viele datierte Einträge trägt eine HTML-Übersicht? Je mehr, desto eher
   ist es eine brauchbare Liste und keine Landingpage. */
function datumsTreffer(text) {
  const a = text.match(/\b\d{1,2}\.\s?(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s?\d{4}\b/g) || [];
  const b = text.match(/\b\d{1,2}\.\d{1,2}\.\d{4}\b/g) || [];
  return a.length + b.length;
}

async function pruefen(q) {
  const start = Date.now();
  try {
    const antwort = await fetch(q.url, {
      redirect: "follow",
      signal: AbortSignal.timeout(ZEITLIMIT),
      headers: { "user-agent": "instagram-bot Quellenpruefung (+https://github.com/Ccan-devoloper/herrjurist)" },
    });
    const text = await antwort.text();
    const dauer = Date.now() - start;
    const typ = (antwort.headers.get("content-type") || "").split(";")[0];
    const befund = { ...q, status: antwort.status, typ, kb: Math.round(text.length / 102.4) / 10, dauer };
    if (!antwort.ok) return { ...befund, urteil: "nicht erreichbar" };
    if (/xml|rss/.test(typ) || /<rss|<feed/i.test(text.slice(0, 500))) {
      const eintraege = rssEintraege(text);
      return { ...befund, eintraege, urteil: eintraege.length ? `Feed mit ${eintraege.length}+ Einträgen` : "Feed ohne Einträge" };
    }
    const daten = datumsTreffer(text);
    return { ...befund, daten, urteil: daten >= 5 ? `Übersicht mit ${daten} Datumsangaben` : daten ? `nur ${daten} Datumsangaben` : "keine datierte Liste" };
  } catch (e) {
    return { ...q, status: 0, urteil: `Fehler: ${kurz(e.message, 60)}` };
  }
}

const befunde = [];
for (const q of QUELLEN) befunde.push(await pruefen(q));

console.log("Quellenprüfung – kostet nichts, ruft kein Modell auf.\n");
for (const b of befunde) {
  const kopf = b.status === 200 ? "✓" : b.status ? `✗ ${b.status}` : "✗";
  console.log(`${kopf} ${b.name}`);
  console.log(`   ${b.url}`);
  console.log(`   ${b.urteil}${b.kb ? ` · ${b.kb} kB · ${b.dauer} ms · ${b.typ}` : ""}`);
  for (const e of b.eintraege || []) console.log(`     – ${e}`);
  console.log();
}

const gut = befunde.filter((b) => b.status === 200 && /Feed mit|Übersicht mit/.test(b.urteil));
console.log(`Ergebnis: ${gut.length} von ${befunde.length} Quellen liefern eine kurze, datierte Liste.`);
if (gut.length) console.log(gut.map((b) => `  · ${b.name}`).join("\n"));
const schlecht = befunde.filter((b) => b.status !== 200);
if (schlecht.length) {
  console.log(`\nNicht erreichbar (gehören nicht in den Prompt):`);
  console.log(schlecht.map((b) => `  · ${b.name} – ${b.urteil}`).join("\n"));
}
