/* ==========================================================================
   Tagesplaner.

   Erstellt für ein Datum den Plan: welche Themen, welche Formate, welche
   Uhrzeiten – für Beiträge und Stories. Deterministisch (Seed = Datum), damit
   mehrere Läufe am selben Tag denselben Plan sehen. Ein Ledger (state/ledger.json)
   sorgt dafür, dass Themen nicht zu früh wiederkommen und alle Fächer rotieren.
   ========================================================================== */

import fs from "node:fs";
import path from "node:path";
import { CONFIG } from "./config.mjs";
import { themenpool, FAECHER, KLAUSUREN, FEED_KATEGORIEN, feedKategorie } from "./inhalte.mjs";
import { heuteIso, wochentag, minutenVon, hhmm, tageBis } from "./zeit.mjs";
import { anlaesseFuer, mindsetThema } from "./kalender.mjs";
import { zeitenWaehlen } from "./zeiten.mjs";

/* Mulberry32 – kleiner, reproduzierbarer Zufallsgenerator. */
function rng(seedText) {
  let h = 1779033703 ^ seedText.length;
  for (let i = 0; i < seedText.length; i++) { h = Math.imul(h ^ seedText.charCodeAt(i), 3432918353); h = (h << 13) | (h >>> 19); }
  let a = h >>> 0;
  return () => { a |= 0; a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}

export function ledgerLaden(pfad) {
  if (pfad && fs.existsSync(pfad)) return JSON.parse(fs.readFileSync(pfad, "utf8"));
  return { veroeffentlicht: [], fachZaehler: {} };
}

export function ledgerSpeichern(pfad, ledger) {
  fs.mkdirSync(path.dirname(pfad), { recursive: true });
  fs.writeFileSync(pfad, JSON.stringify(ledger, null, 2));
}

/* Welche Themen-Typen ein Format sinnvoll speisen. */
/* Welches Beitragsformat darf sich aus welchen Themen-Typen bedienen?
   Der Typ beschreibt das Material (Schema, Frage-Antwort-Karte, Begriffspaar,
   Rechnung), das Format den Aufbau des Beitrags. Ein Thema vom Typ „quiz“ –
   eine Frage mit zwei vertretbaren Wegen – trägt nicht nur die Prüfungsfrage,
   sondern ebenso den Mini-Fall, die Fehlerfalle und das Reel. */
export const FORMAT_QUELLEN = {
  pruefungsfrage: ["modul", "karteikarte", "quiz", "schema"],
  fehlerfalle:    ["modul", "karteikarte", "quiz"],
  schema:         ["modul", "schema"],
  rechenweg:      ["formel", "modul"],
  spickzettel:    ["modul", "schema"],
  anlass:         ["modul", "karteikarte"],
  reel:           ["modul", "schema", "karteikarte", "quiz"],
  loesungsskizze: [],
  minifall:       ["modul", "karteikarte", "quiz"],
  vergleich:      ["modul", "karteikarte", "begriff"],
  streitstand:    ["modul", "begriff", "karteikarte"],
  klausurtechnik: ["modul", "formel", "schema"],
  wochenrueckblick: [],
  aktuell:        [],
};

/* Ein Rechtsgebiet je Beitrag - und taeglich rotierend.

   Bis zum 16.09. entschied eine gewichtete Zufallswahl mit Rueckstands-Bonus,
   welches Gebiet drankommt. Im Mittel war das ausgeglichen, an einem einzelnen
   Tag aber beliebig: Zwei Beitraege konnten dasselbe Gebiet tragen, ein
   drittes fehlte ganz. Dabei gibt es bei drei Beitraegen taeglich genau drei
   Gebiete - Zivilrecht, Strafrecht, Oeffentliches Recht. Jedes bekommt seinen
   Beitrag, und welches Gebiet welchen Platz im Tag besetzt, wandert Tag fuer
   Tag weiter: mal ist das Reel zivilrechtlich, mal strafrechtlich, mal
   oeffentlich-rechtlich.

   Beitraege ohne Thema aus dem Pool zaehlen nicht mit - „aktuell" folgt der
   Nachrichtenlage, das Samstags-Reel traegt ein Mindset-Thema. Sie wuerden
   sonst ein Gebiet verbrauchen, das sie gar nicht zeigen. */
export function gebieteDesTages(datum, plaetze) {
  const tage = Math.floor(Date.UTC(+datum.slice(0, 4), +datum.slice(5, 7) - 1, +datum.slice(8, 10)) / 86400000);
  const start = ((tage % 3) + 3) % 3;
  return Array.from({ length: Math.max(0, plaetze) }, (_, i) => ((start + i) % 3) + 1);
}

/* Wachstumsmodus: erst die Dauerbrenner. Eine Stufe zählt nur, wenn sie
   genug Auswahl lässt (vier Kandidaten, wie im Endspurt) – sonst rückt die
   nächste nach. So „gehen die 🔴-Themen aus“ (in die Wiederholsperre),
   bevor 🟠 drankommt, und 🟢 bleibt der Nachschub für lange Tage. Greift
   nach allen anderen Filtern, damit die Stufe im tatsächlichen Slot
   (Format, Gebiet, Sperre) gebildet wird und nicht am ganzen Pool. */
export function prioritaetsKaskade(kandidaten, mindestens = 4) {
  if (!CONFIG.plan.viralVorrang) return kandidaten;
  const hoch = kandidaten.filter((t) => t.prioritaet === "hoch");
  if (hoch.length >= mindestens) return hoch;
  const wichtig = kandidaten.filter((t) => t.prioritaet !== "selten");
  return wichtig.length >= mindestens ? wichtig : kandidaten;
}

function gewichteteWahl(kandidaten, zufall, ledger, strategie = null) {
  const g = CONFIG.plan.prioritaetGewicht;
  const zaehler = ledger.fachZaehler || {};
  const minFach = Math.min(...Object.keys(FAECHER).map((f) => zaehler[f] || 0));
  const fachGewicht = (CONFIG.plan.lernen && strategie?.fachGewicht) || {};
  const gewichte = kandidaten.map((t) => {
    let w = (g[t.prioritaet] || 10) * (fachGewicht[t.fach] ?? 1);
    /* Fächer, die zuletzt seltener dran waren, bekommen einen Bonus –
       so bleibt das Profil für alle drei Klausuren interessant. */
    const rueckstand = (zaehler[t.fach] || 0) - minFach;
    w *= rueckstand === 0 ? 1.6 : rueckstand === 1 ? 1.2 : 1;
    /* Streitstände sind die Beiträge, die gespeichert und weitergeleitet
       werden – leichter Schub, die Stufenwahl darüber bleibt maßgeblich. */
    if (t.streit) w *= 1.25;
    return w;
  });
  const summe = gewichte.reduce((a, b) => a + b, 0);
  let r = zufall() * summe;
  for (let i = 0; i < kandidaten.length; i++) { r -= gewichte[i]; if (r <= 0) return kandidaten[i]; }
  return kandidaten[kandidaten.length - 1];
}

/* Was wurde zu einem Thema zuletzt veröffentlicht? Der jüngste Eintrag zählt –
   daraus wird die Sperre berechnet und, bei einer Wiederholung, die Auflage an
   den Autor, das Thema anders zu verpacken. */
/** Wann ein Thema zuletzt lief - getrennt nach Beitrag und Story. */
function letzteNutzung(ledger, art) {
  const m = new Map();
  for (const e of ledger.veroeffentlicht || []) {
    if (!e.thema || e.art !== art) continue;
    const alt = m.get(e.thema);
    if (!alt || (e.datum || "") > (alt.datum || "")) m.set(e.thema, e);
  }
  return m;
}

/**
 * Themen, die für diese Art gerade frei sind.
 *
 * Beiträge und Stories haben getrennte Sperren: Eine Story darf ein Thema
 * aufgreifen, das als Beitrag lief (und umgekehrt) - das ist Wiederholung,
 * kein Doppel. Zwei Stories zum selben Thema kurz hintereinander sind es
 * schon: Am 12. und 13.09. stand zweimal „Dienst- oder Werkvertrag?" als
 * Norm des Tages, weil die Sperre Stories gar nicht ansah.
 */
function verfuegbar(pool, ledger, datum, benutzt, art = "beitrag") {
  const sperre = art === "story" ? CONFIG.plan.storySperreTage : CONFIG.plan.themenSperreTage;
  const zuletzt = letzteNutzung(ledger, art);
  return pool.filter((t) => {
    if (benutzt.has(t.id)) return false;
    const e = zuletzt.get(t.id);
    return !e || tageBis(datum, new Date(`${e.datum}T12:00:00Z`)) >= sperre;
  });
}

/**
 * Notfall, wenn der Vorrat einer Story-Art erschöpft ist: das am längsten
 * zurückliegende Thema zuerst. Betrifft vor allem Rechenwege - bei Herr
 * Jurist gibt es dafür nur eine Handvoll Themen.
 */
function aeltesteZuerst(pool, ledger, benutzt, art = "story") {
  const zuletzt = letzteNutzung(ledger, art);
  const wann = (t) => zuletzt.get(t.id)?.datum || "0000-00-00";
  return pool.filter((t) => !benutzt.has(t.id)).sort((a, b) => wann(a).localeCompare(wann(b))).slice(0, 5);
}

function storyZeiten(anzahl, zufall) {
  const [von, bis] = CONFIG.plan.storyFenster.map(minutenVon);
  const schritt = (bis - von) / Math.max(1, anzahl);
  return Array.from({ length: anzahl }, (_, i) => hhmm(Math.round(von + i * schritt + zufall() * Math.min(25, schritt / 2))));
}

/**
 * Baut den Tagesplan.
 * @returns {{datum, beitraege:[{slot, zeit, format, thema}], stories:[{slot, zeit, art, thema?, beitragSlot?}]}}
 */
export function tagesplan(datum = heuteIso(), ledger = ledgerLaden(), pool = themenpool(), strategie = null) {
  const zufall = rng(`plan:${datum}`);
  const wt = wochentag(new Date(`${datum}T12:00:00Z`));
  const wochenende = wt === 0 || wt === 6;
  const anzahl = wochenende ? CONFIG.plan.beitraegeWochenende : CONFIG.plan.beitraegeWerktag;
  const tageVor = CONFIG.examen.schriftlich ? tageBis(CONFIG.examen.schriftlich, new Date(`${datum}T12:00:00Z`)) : -1;
  /* Endspurt: in den letzten Wochen vor der Prüfung Klausurtechnik und Dauerbrenner. */
  const endspurt = tageVor >= 0 && tageVor <= CONFIG.plan.endspurtTage;
  const tabelle = endspurt ? CONFIG.plan.formateEndspurt : CONFIG.plan.formateJeWochentag;
  const formate = (tabelle[wt] || ["pruefungsfrage", "fehlerfalle", "schema"]).slice(0, anzahl);
  /* Reel-Tage (Standard: täglich). Je nach CONFIG.reel.zusaetzlich kommt das
     Reel zu den Beiträgen dazu (drei Feed-Veröffentlichungen) oder ersetzt den
     letzten (zwei). Steht vor der Lernschleife, damit diese nur Plätze tauscht,
     die auch bleiben. */
  if (CONFIG.reel.aktiv && CONFIG.reel.tage.includes(wt) && formate.length) {
    if (CONFIG.reel.zusaetzlich) formate.push("reel");
    else formate[formate.length - 1] = "reel";
  }
  /* Lernschleife: ein Format, das deutlich schlechter läuft als der Schnitt, wird an
     diesem Tag durch das beste Format ersetzt (nie „aktuell“/„wochenrueckblick“/Reel). */
  const fg = (CONFIG.plan.lernen && strategie?.formatGewicht) || {};
  const bestes = Object.entries(fg).filter(([k]) => !["aktuell", "wochenrueckblick", "reel", "anlass"].includes(k)).sort((a, b) => b[1] - a[1])[0];
  if (bestes && bestes[1] >= 1.2) {
    const schwach = formate.findIndex((f) => (fg[f] ?? 1) <= 0.75 && !["aktuell", "wochenrueckblick", "reel"].includes(f));
    if (schwach >= 0 && !formate.includes(bestes[0])) formate[schwach] = bestes[0];
  }
  /* Anlasstage (Countdown, Prüfungstag …): der erste Beitrag wird zum Anlass. */
  const anlaesseHeute = anlaesseFuer(datum);
  const anlass = anlaesseHeute.find((a) => !a.zeit) || null;
  const abendAnlass = anlaesseHeute.find((a) => a.zeit) || null;
  if (anlass && formate.length) formate[0] = "anlass";
  /* Abend-Anlass (Lösungsskizze am Prüfungstag): ersetzt den letzten Beitrag des Tages. */
  if (abendAnlass && formate.length) formate[formate.length - 1] = "loesungsskizze";
  /* Uhrzeiten: gelernt aus dem, was gemessen wurde (zeiten.mjs) – je
     Beitragsart und Wochentag, mit Erkundung solange die Daten dünn sind. */
  const zeiten = zeitenWaehlen({ formate, datum, ledger, strategie, zufall });
  const benutzt = new Set();
  const ledgerKopie = { ...ledger, fachZaehler: { ...(ledger.fachZaehler || {}) } };

  const beitraegeBisher = [];
  const vorher = letzteNutzung(ledger, "beitrag");

  /* Das Reel sucht sich sein Thema ZUERST aus.

     Bis zum 14.09. lief es umgekehrt: Das Reel steht im Tagesplan an letzter
     Stelle, und der Farbwechsel-Filter unten verbietet jedem Beitrag die
     Rechtsgebiete, die am selben Tag schon dran waren. An einem Tag mit drei
     Beiträgen bekam das Reel damit nicht die beste Wahl, sondern den Rest -
     und weil die beiden Kachelbeiträge fast immer Zivil- und Strafrecht
     nehmen (Zivilrecht stellt knapp die Hälfte des Pools), blieb für das Reel
     zwangsläufig das Öffentliche Recht übrig.

     Das Ergebnis war im Raster zu sehen: Die ersten fünf Reels des Kanals
     waren alle grün. Ein tägliches Format, das nur ein Drittel des Stoffs
     zeigt, verschenkt genau die Reichweite, für die es da ist.

     Also erst das Reel, dann der Rest. Die Reihenfolge im Plan (Slot und
     Uhrzeit) bleibt unverändert - nur die Wahl des Themas wird vorgezogen. */
  const reihenfolge = formate.map((_, i) => i).sort((a, b) => (formate[b] === "reel" ? 1 : 0) - (formate[a] === "reel" ? 1 : 0));

  /* Welcher Slot traegt heute welches Rechtsgebiet? Zugeteilt wird nur an
     Slots, die sich aus dem Themenpool bedienen. Das loest zugleich das alte
     Reel-Problem: Die ersten fuenf Reels des Kanals waren allesamt gruen,
     weil die Kachelbeitraege sich zuerst Zivil- und Strafrecht nahmen und
     fuer das Reel das Oeffentliche Recht uebrig blieb. Jetzt steht das Gebiet
     jedes Slots vorher fest und wandert taeglich weiter. */
  const ausPool = (f) => (FORMAT_QUELLEN[f] || []).length > 0;
  const poolSlots = formate.map((f, i) => i).filter((i) => ausPool(formate[i]) && !(formate[i] === "reel" && wt === 6));
  /* Zugeteilt wird nach PLATZ im Tag, nicht nach Reihenfolge der Pool-Slots.
     Der Unterschied ist nicht akademisch: Zaehlte man die Pool-Slots durch,
     rueckte mittwochs b2 auf das Gebiet von b1 nach, weil „aktuell" kein
     Thema aus dem Pool zieht - und b1 spraenge von Tag zu Tag, statt sauber
     Strafrecht → Oeffentliches Recht → Zivilrecht zu wandern. Ein Slot ohne
     Pool-Thema laesst sein Gebiet lieber liegen; es geht als Wunsch in die
     Recherche (siehe fehlendesGebiet() in lauf.mjs). */
  const rotation = gebieteDesTages(datum, formate.length);
  /* Samstag gehört der erste Karussell-Slot bewusst der violetten
     Klausurmethodik. Das Reel ist ebenfalls violett (Mindset), dazwischen
     liegt ein Fachbeitrag. So können beide Sonderformate am selben Tag
     erscheinen, ohne im Feed direkt aufeinanderzufolgen. */
  const gebietFuer = new Map(poolSlots.map((slot) => [
    slot,
    wt === 6 && formate[slot] === "klausurtechnik" ? 0 : rotation[slot],
  ]));
  const beitraege = new Array(formate.length);
  for (const i of reihenfolge) {
    const format = formate[i];
    const typen = FORMAT_QUELLEN[format] || [];
    let thema = null;
    if (typen.length) {
      let kandidaten = verfuegbar(pool, ledgerKopie, datum, benutzt).filter((t) => typen.includes(t.typ));
      /* Endspurt: Dauerbrenner zuerst – keine seltenen Themen mehr. */
      if (endspurt) { const hoch = kandidaten.filter((t) => t.prioritaet === "hoch"); if (hoch.length >= 4) kandidaten = hoch; }
      /* Wiederholungen anders verpacken: Ein Thema, das schon einmal in diesem
         Format lief, wird für dieses Format zurückgestellt. Kommt es doch
         wieder dran, bekommt der Autor die Auflage, einen anderen Zugang zu
         wählen (siehe unten, thema.zuletzt). */
      const frisch = kandidaten.filter((t) => vorher.get(t.id)?.format !== format);
      if (frisch.length >= 3) kandidaten = frisch;
      /* Die sichtbare Kategorie dieses Slots steht fest - hart, nicht als
         Wunsch. Ist innerhalb der Wiederholsperre nichts frei, wird lieber das
         älteste Farbfeld wiederverwendet als in eine andere Farbe zu springen. */
      const ziel = gebietFuer.get(i);
      if (ziel != null) {
        const imGebiet = kandidaten.filter((t) => t.klausur === ziel);
        if (imGebiet.length) kandidaten = imGebiet;
        else {
          const farbReserve = pool.filter((t) => typen.includes(t.typ) && t.klausur === ziel && !benutzt.has(t.id));
          if (farbReserve.length) {
            kandidaten = aeltesteZuerst(farbReserve, ledgerKopie, benutzt, "beitrag");
            console.warn(`  ! ${FEED_KATEGORIEN[ziel] || KLAUSUREN[ziel]?.kurz || ziel}: Wiederholsperre erschöpft für „${format}“ – ältestes Thema derselben Farbe wird genommen.`);
          }
        }
      }
      const notfall = ziel != null
        ? pool.filter((t) => typen.includes(t.typ) && t.klausur === ziel)
        : pool.filter((t) => typen.includes(t.typ));
      thema = gewichteteWahl(prioritaetsKaskade(kandidaten.length ? kandidaten : notfall), zufall, ledgerKopie, strategie);
      /* War das Thema schon einmal dran, reist die Vorgeschichte mit: Format,
         Hook und Titel von damals. Der Autor darf sich davon nicht wiederholen. */
      const alt = vorher.get(thema.id);
      if (alt) thema = { ...thema, zuletzt: { datum: alt.datum, format: alt.format, hookMuster: alt.hookMuster || alt.hookTyp || null, titel: alt.titel || null } };
      benutzt.add(thema.id);
      ledgerKopie.fachZaehler[thema.fach] = (ledgerKopie.fachZaehler[thema.fach] || 0) + 1;
    }
    /* Samstags-Reel: Mindset statt Fachthema – holt Menschen ab, die Fachposts nie sehen. */
    if (format === "reel" && wt === 6) thema = mindsetThema(datum);
    const zeit = format === "loesungsskizze" ? abendAnlass.zeit : (zeiten[i] || zeiten.at(-1));
    /* Sichtbare Kategorie wird am Plan festgehalten. Das ist besonders für
       freie Formate wichtig: „aktuell“ hat noch kein Thema, der
       Wochenrückblick nie eines. */
    const klausur = format === "wochenrueckblick"
      ? 4
      : (format === "reel" && wt === 6)
        ? 0
        : (thema?.klausur ?? rotation[i] ?? null);
    const eintrag = { slot: `b${i + 1}`, zeit, format, thema, klausur, anlass: format === "anlass" ? anlass : format === "loesungsskizze" ? abendAnlass : undefined, lang: format === "reel" ? CONFIG.reel.langeTage.includes(wt) : undefined };
    beitraegeBisher.push(eintrag);
    beitraege[i] = eintrag;
  }

  /* Stories: höchstens wenige, gezielte Feed-Teaser statt einer Kopie jedes
     Beitrags. Eigene Daten 19.–25.09.: Teaser lagen bei ca. 93 Reach im Schnitt
     und erzeugten praktisch keine direkte Interaktion. Wenn wir einen Teaser
     nutzen, bekommt ihn deshalb der laut Lernschleife stärkste Tagesbeitrag. */
  const stories = [];
  const teaserAnzahl = Math.min(CONFIG.plan.teaserProTag ?? 1, beitraege.length);
  const formatGewicht = (CONFIG.plan.lernen && strategie?.formatGewicht) || {};
  const teaserKandidaten = beitraege
    .map((b, index) => ({ b, index, gewicht: Number(formatGewicht[b.format] ?? 1) }))
    .sort((a, b) => (b.gewicht - a.gewicht) || (a.index - b.index))
    .slice(0, teaserAnzahl)
    .sort((a, b) => a.index - b.index);
  for (const { b } of teaserKandidaten) stories.push({ art: "teaser", beitragSlot: b.slot, zeit: b.zeit });
  /* Zwei Arten stehen jeden Tag: Die Quizfrage ist das stärkste Format für
     Antworten, die Norm des Tages der Markenkern. Der Rest rotiert, damit
     über die Woche alle Arten drankommen - vorher lief die Liste jeden Tag
     von vorn und "fehler", "tipp" und "zahl" kamen nie an die Reihe, weil das
     Tageskontingent vorher voll war. */
  const FEST = ["frage", "norm"];
  const WECHSELND = ["streitstand", "merksatz", "begriff", "fehler", "tipp", "zahl", "formel"];
  /* Arten mit dünnem Vorrat laufen im Takt statt täglich: Für Rechenwege gibt
     es in Jura nur eine Handvoll Themen - täglich hiesse alle fünf Tage
     dasselbe. Der Takt zählt Tage seit 1970, ist also für jeden Kalendertag
     derselbe, egal wann der Plan entsteht. */
  const tagesZahl = Math.floor(Date.UTC(+datum.slice(0, 4), +datum.slice(5, 7) - 1, +datum.slice(8, 10)) / 86400000);
  const takt = CONFIG.plan.storyArtTakt || {};
  const versatz = tagesZahl % WECHSELND.length;
  const eigenstaendig = [...FEST, "countdown", ...WECHSELND.slice(versatz), ...WECHSELND.slice(0, versatz)];
  const tageBisExamen = CONFIG.examen.schriftlich ? tageBis(CONFIG.examen.schriftlich, new Date(`${datum}T12:00:00Z`)) : -1;
  let k = 0;
  /* Prüfungstage: nur Teaser-Stories – das Budget gehört der Lösungsskizze am Abend. */
  const pruefungstag = anlass?.art === "pruefungstag";
  while (!pruefungstag && stories.length < CONFIG.plan.storiesProTag && k < 40) {
    const art = eigenstaendig[k % eigenstaendig.length];
    k++;
    if (art === "countdown" && (tageBisExamen < 0 || tageBisExamen > 200)) continue;
    if (takt[art] && tagesZahl % takt[art] !== 0) continue;
    let thema = null;
    const typen = { frage: ["quiz", "karteikarte"], norm: ["modul", "begriff"], streitstand: ["schema", "modul"], merksatz: ["modul"], formel: ["formel"], begriff: ["begriff", "karteikarte"], fehler: ["modul"], tipp: ["modul"], zahl: ["formel", "modul"] }[art];
    if (typen) {
      const passend = pool.filter((t) => typen.includes(t.typ));
      let kandidaten = verfuegbar(passend, ledgerKopie, datum, benutzt, "story");
      /* Vorrat dieser Art erschöpft? Erst eine andere Art versuchen - erst
         wenn die Runde fast durch ist, das älteste Thema wiederholen. So
         erscheinen Rechenwege bei dünner Auswahl seltener statt doppelt. */
      if (!kandidaten.length) {
        if (k < 25) continue;
        kandidaten = aeltesteZuerst(passend, ledgerKopie, benutzt);
      }
      if (!kandidaten.length) continue;
      thema = gewichteteWahl(kandidaten, zufall, ledgerKopie, strategie);
      benutzt.add(thema.id);
    }
    /* Frage und Antwort sind zwei Stories. */
    if (art === "frage") {
      stories.push({ art: "frage", thema });
      stories.push({ art: "antwort", thema });
    } else {
      stories.push({ art, thema, tageBisExamen: art === "countdown" ? tageBisExamen : undefined });
    }
  }
  /* Zeiten nur für die Stories berechnen, die noch keine haben. Die Teaser
     erscheinen mit ihrem Beitrag und bringen ihre Zeit mit; wurden sie
     mitgezählt, blieben die ersten beiden Slots des Fensters ungenutzt - und
     damit der ganze Morgen leer, obwohl das Fenster um 7 Uhr beginnt. */
  const ohneZeit = stories.filter((s) => !s.zeit);
  const storyZeitenListe = storyZeiten(ohneZeit.length, zufall);
  ohneZeit.forEach((s, i) => { s.zeit = storyZeitenListe[i]; });
  /* Eine Quizfrage braucht Zeit zum Abstimmen. Die Auflösung kommt standardmäßig
     vier Stunden später (konfigurierbar), höchstens am Ende des Story-Fensters.
     Damit wird aus „lesen → sofort Lösung sehen“ ein echter Rückkehr-/Vote-Anlass. */
  const storyBis = minutenVon(CONFIG.plan.storyFenster[1]);
  const quizAbstand = Math.max(60, Number(CONFIG.plan.quizAufloesungStunden || 4) * 60);
  for (let i = 0; i < stories.length; i++) {
    if (stories[i].art !== "antwort") continue;
    const frage = stories.slice(0, i).reverse().find((s) => s.art === "frage" && s.thema?.id === stories[i].thema?.id);
    if (!frage?.zeit) continue;
    stories[i].zeit = hhmm(Math.min(storyBis, minutenVon(frage.zeit) + quizAbstand));
  }
  stories.sort((a, b) => minutenVon(a.zeit) - minutenVon(b.zeit));
  /* Slots folgen der tatsächlichen Chronologie. Das hält Frage/Auflösung und
     die späteren Insight-Auswertungen nachvollziehbar. */
  stories.forEach((s, i) => { s.slot = `s${i + 1}`; });

  return { datum, wochentag: wt, beitraege, stories, anlass, abendAnlass };
}

/* Auffüllplan: n Beiträge (keine Reels, keine Tagesformate) mit Themen aus dem
   Pool, Fächer und Formate rotierend. */
export function auffuellplan(anzahl, ledger = ledgerLaden(), pool = themenpool(), seed = "auffuellen") {
  const zufall = rng(`auffuellen:${seed}`);
  const formate = ["pruefungsfrage", "fehlerfalle", "schema", "streitstand", "minifall", "vergleich", "spickzettel", "klausurtechnik"];
  const benutzt = new Set();
  const ledgerKopie = { ...ledger, fachZaehler: { ...(ledger.fachZaehler || {}) } };
  const heute = heuteIso();
  const liste = [];
  for (let i = 0; i < anzahl; i++) {
    const format = formate[i % formate.length];
    const typen = FORMAT_QUELLEN[format] || ["modul"];
    const kandidaten = verfuegbar(pool, ledgerKopie, heute, benutzt).filter((t) => typen.includes(t.typ));
    const thema = gewichteteWahl(prioritaetsKaskade(kandidaten.length ? kandidaten : pool.filter((t) => typen.includes(t.typ))), zufall, ledgerKopie);
    benutzt.add(thema.id);
    ledgerKopie.fachZaehler[thema.fach] = (ledgerKopie.fachZaehler[thema.fach] || 0) + 1;
    liste.push({ slot: `f${i + 1}`, format, thema });
  }
  return liste;
}

/* Schwarz/Weiß-Wechsel: immer das Gegenteil des zuletzt veröffentlichten
   Beitrags – unabhängig von Fehlschlägen, Slots oder Tagen. So bleibt das
   Schachbrett im Profil lückenlos. */
/* Übertrag: Was gestern nicht erschienen ist, kommt heute zuerst – an Stelle
   eines neu gezogenen Themas gleicher Art (Reel für Reel, Beitrag für
   Beitrag), damit der Tag nicht teurer wird. Das verdrängte Thema war noch
   nicht vermerkt und bleibt im Pool. Höchstens einmal, damit ein Thema, das
   zweimal scheitert, nicht ewig kreist. Formate, die an ihrem Tag hängen
   (Lösungsskizze zum Klausurtag, Aktuelles, Anlass), bleiben zurück. */
export function uebertragen(plan, planGestern, gestern) {
  const fest = new Set(["loesungsskizze", "aktuell", "anlass"]);
  const offen = (planGestern?.beitraege || []).filter((b) => b.status !== "veroeffentlicht" && !(b.uebertragen >= 1) && !fest.has(b.format) && (b.themaId || b.format === "wochenrueckblick"));
  const uebernommen = [];
  for (const alt of offen) {
    const istReel = alt.format === "reel";
    const kategorie = feedKategorie(alt);
    /* Übertrag darf die Farbfolge nicht verändern. Ein alter Beitrag ersetzt
       nur einen heutigen Platz derselben sichtbaren Kategorie und derselben
       Medienart. Gibt es so einen Platz nicht, bleibt er zurück. Dadurch
       wandert z. B. ein Sonntags-Wochenrückblick nicht in den Montag. */
    const ziel = plan.beitraege.find((b) =>
      (b.format === "reel") === istReel &&
      !b.uebertragenVon &&
      kategorie != null &&
      feedKategorie(b) === kategorie
    );
    if (!ziel) continue;
    const mitnahme = {
      format: alt.format,
      themaId: alt.themaId || null,
      themaTitel: alt.themaTitel || null,
      fach: alt.fach || null,
      klausur: kategorie,
      lang: alt.lang,
      uebertragenVon: `${gestern}-${alt.slot}`,
      uebertragen: (alt.uebertragen || 0) + 1,
    };
    Object.assign(ziel, mitnahme);
    uebernommen.push({ alt, ziel });
  }
  return uebernommen;
}

export function naechsteVariante(ledger) {
  const letzter = [...(ledger.veroeffentlicht || [])].reverse().find((e) => e.art === "beitrag" && e.medienId && e.medienId !== "trocken" && e.variante != null);
  return letzter ? 1 - letzter.variante : 0;
}

/* Nach einer Veröffentlichung im Ledger vermerken. */
export function vermerken(ledger, eintrag) {
  ledger.veroeffentlicht = ledger.veroeffentlicht || [];
  ledger.veroeffentlicht.push(eintrag);
  if (eintrag.thema && eintrag.art === "beitrag") {
    const fach = eintrag.fach;
    ledger.fachZaehler = ledger.fachZaehler || {};
    ledger.fachZaehler[fach] = (ledger.fachZaehler[fach] || 0) + 1;
  }
  /* Ledger schlank halten: 400 Tage reichen für die Sperre. */
  const grenze = new Date(Date.now() - 400 * 86400000).toISOString().slice(0, 10);
  ledger.veroeffentlicht = ledger.veroeffentlicht.filter((e) => e.datum >= grenze);
  return ledger;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const datum = process.argv[2] || heuteIso();
  const plan = tagesplan(datum);
  console.log(`Plan für ${datum} (Wochentag ${plan.wochentag})`);
  for (const b of plan.beitraege) console.log(`  ${b.zeit}  Beitrag ${b.slot} ${b.format.padEnd(15)} ${b.thema ? `${b.thema.fach.padEnd(6)} ${b.thema.prioritaet.padEnd(6)} ${b.thema.titel}` : "(ohne Thema – Web/Rückblick)"}`);
  for (const s of plan.stories) console.log(`  ${s.zeit}  Story   ${s.slot.padEnd(3)} ${s.art.padEnd(10)} ${s.thema ? `${s.thema.fach.padEnd(6)} ${s.thema.titel}` : s.beitragSlot ? `→ Beitrag ${s.beitragSlot}` : ""}`);
}
