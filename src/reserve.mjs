/* ==========================================================================
   Der Reservebestand: fertige Beiträge, die an einem Blockadetag erscheinen
   können - ohne einen einzigen bezahlten Anbieteraufruf.

   Warum es ihn gibt: Die Kostenkontrolle hält, die Verfügbarkeit nicht. Der
   Admissionbedarf des Pflichtprodukts liegt über der Betriebsgrenze
   (dailyPlanNotAdmissibleAtCap). Ein Slot, der an der Admission scheitert,
   fällt heute sichtbar aus. Der Vorrat ist die Antwort darauf - und er ist
   nur dann eine Antwort, wenn seine Entnahme NICHTS kostet.

   Daraus folgt alles Weitere:

   KEIN NACHCHECK. Ein Vorratsbeitrag wird nie am Blockadetag nachgeprüft -
   dort ist kein Geld. Er wird auch nicht verlängert. Was nicht mehr gilt,
   wird verworfen und später an einem günstigen Tag neu produziert.

   Und weil es keinen Nachcheck gibt, darf nur hinein, was von sich aus nicht
   altert. Das ist die eigentliche Schutzregel; die Haltbarkeit darunter ist
   ein zusätzlicher Sicherheitsgurt, kein Ersatz für sie.

   ZWEI TORE, beide müssen offen sein - und beide schließen im Zweifel:

     Tor 1  Das THEMA muss alterungsarm sein: Schemata und
            Begriffsabgrenzungen. Dauerhafte Systematik, formale
            Prüfungsschritte. Nicht dabei sind Module, Karteikarten,
            Formeln und Quizfragen - Module und Karteikarten tragen
            regelmäßig Jahreswerte, Formeln tragen Sätze und Grenzen, und
            Quiz gehört nicht in diese Phase.

     Tor 2  Der geschriebene INHALT darf keine Zeitabhängigkeit tragen:
            keine Jahreszahlen, keine Beträge, keine Sätze, keine
            Verwaltungsanweisungen, keine Entscheidungen, keine Recherche.
            Ein Thema kann alterungsarm sein und der Beitrag dazu trotzdem
            einen Freibetrag nennen - dann ist er draußen.

   Beide Tore sind bewusst streng. Von 429 Campus-Themen bleiben 29 übrig, von
   906 bei Herr Jurist 237. Für einen Zielbestand von vier ist das reichlich,
   und ein zu enges Tor kostet nur Auswahl - ein zu weites kostet einen
   Beitrag mit veraltetem Rechtsstand.

   WAS DIESES MODUL NICHT TUT: Es füllt nichts auf und entnimmt nichts von
   selbst. Es ist die Regel, nach der das später entschieden wird. Die
   Verdrahtung in den Tageslauf kommt als eigener Schritt - erst die Policy,
   dann die Mechanik.
   ========================================================================== */

/** Zielbestand: drei decken einen vollständigen Blockadetag, einer ist Puffer
    für Verfall, Dublette oder thematisch Unpassendes. */
export const ZIEL_BESTAND = 4;

/** Harte Haltbarkeit. Sicherheitsgurt, nicht Hauptschutz. */
export const TTL_TAGE = 21;

/** Tor 1: Themenarten, die von sich aus nicht altern. */
export const RESERVE_TYPEN = Object.freeze(["schema", "begriff"]);

/** Version der Regel - steht in jedem Eintrag, damit eine Regeländerung den
    Altbestand nicht stillschweigend mitgelten lässt. */
export const REGEL_VERSION = 1;

/* --- Tor 2: Zeitabhängigkeit im geschriebenen Text --------------------- */

/**
 * Textfelder, die Inhalt tragen. Bewusst eine Liste statt „alles im Objekt":
 * Ein Slug wie `2026-09-19-b1` enthält eine Jahreszahl, und eine Bild-URL
 * enthält alles Mögliche. Wer über das ganze Objekt sucht, sperrt am Ende
 * jeden Beitrag aus.
 */
const TEXTFELDER = new Set(["titel", "text", "punkte", "zeilen", "caption", "seo", "frage", "antwort", "merksatz"]);

export const ZEITMARKEN = Object.freeze([
  { muster: /\b(19|20)\d{2}\b/, was: "Jahreszahl" },
  { muster: /\d[\d.,]*\s*(€|EUR\b|Euro\b)/i, was: "Geldbetrag" },
  { muster: /\d[\d.,]*\s*(%|Prozent\b)/i, was: "Prozentsatz" },
  { muster: /\bBMF\b|\bBFH\b|\bEuGH\b|\bBVerfG\b|\bBGH\b/, was: "Verwaltungsanweisung oder Entscheidung" },
  { muster: /\bAz\.|\bUrteil vom\b|\bBeschluss vom\b|\bSchreiben vom\b/i, was: "Fundstelle mit Datum" },
  { muster: /\bFreibetrag|\bFreigrenze|\bPauschbetrag|\bPauschale\b|\bHöchstbetrag|\bGrenzbetrag/i, was: "Betragsgrenze" },
  { muster: /\bgilt seit\b|\bab dem\b|\bseit dem\b|\bRechtsstand\b|\bneu geregelt\b|\bReform\b/i, was: "Zeitbezug" },
  { muster: /gesetz\s+20\d{2}|\bJahressteuergesetz\b|\bWachstumschancengesetz\b/i, was: "datiertes Änderungsgesetz" },
]);

/** Sammelt den Inhaltstext eines Beitrags - und nur ihn. */
export function inhaltsText(beitrag) {
  const teile = [];
  const gehen = (wert, schluessel = null) => {
    if (wert == null) return;
    if (typeof wert === "string") { if (schluessel && TEXTFELDER.has(schluessel)) teile.push(wert); return; }
    if (Array.isArray(wert)) { for (const x of wert) gehen(x, schluessel); return; }
    if (typeof wert === "object") { for (const [k, v] of Object.entries(wert)) gehen(v, k); }
  };
  gehen(beitrag?.folien, "folien");
  gehen({ caption: beitrag?.caption, seo: beitrag?.seo });
  return teile.join("\n");
}

/* --- Die einzelnen Prüfungen ------------------------------------------- */

/** Tor 1. */
export function themaTauglich(thema) {
  const gruende = [];
  if (!thema) gruende.push("kein Thema angegeben");
  else if (!RESERVE_TYPEN.includes(thema.typ)) {
    gruende.push(`Themenart ${thema.typ || "unbekannt"} ist nicht alterungsarm (zulaessig: ${RESERVE_TYPEN.join(", ")})`);
  }
  return { ok: gruende.length === 0, gruende };
}

/** Tor 2. */
export function inhaltTauglich(beitrag) {
  const gruende = [];
  if (!beitrag) return { ok: false, gruende: ["kein Beitrag angegeben"] };

  /* Ein Beitrag, dessen Richtigkeit an einer Recherche hängt, altert mit der
     Quelle - unabhängig davon, was im Text steht. */
  if (beitrag.format === "aktuell") gruende.push("Format aktuell beruht auf tagesaktueller Recherche");
  if (Array.isArray(beitrag.quellen) && beitrag.quellen.length) gruende.push("Beitrag stützt sich auf recherchierte Quellen");
  if (beitrag.recherche) gruende.push("Beitrag wurde mit Recherche erstellt");

  const text = inhaltsText(beitrag);
  for (const marke of ZEITMARKEN) {
    const treffer = text.match(marke.muster);
    if (treffer) gruende.push(`${marke.was}: ${String(treffer[0]).slice(0, 40)}`);
  }
  return { ok: gruende.length === 0, gruende };
}

/**
 * Vollständigkeit: Ein Vorratsbeitrag muss am Blockadetag OHNE bezahlten
 * Aufruf erscheinen können. Alles, was dafür nötig ist, muss schon da sein -
 * Text, Faktenfreigabe und die gerenderten Bilder.
 */
export function vollstaendig(eintrag) {
  const fehlend = [];
  if (!eintrag?.beitrag?.folien?.length) fehlend.push("Beitragstext");
  if (!eintrag?.caption) fehlend.push("Caption");
  if (!Array.isArray(eintrag?.bildUrls) || !eintrag.bildUrls.length) fehlend.push("gerenderte Bilder");
  if (!eintrag?.faktenFreigabe?.ok) fehlend.push("Faktenfreigabe");
  if (!eintrag?.faktenFreigabe?.geprueftAm) fehlend.push("Zeitpunkt der Faktenfreigabe");
  return { ok: fehlend.length === 0, fehlend };
}

/** Die Gesamtregel für die Aufnahme in den Vorrat. */
export function reserveTauglich({ thema, beitrag } = {}) {
  const t = themaTauglich(thema);
  const i = inhaltTauglich(beitrag);
  return { ok: t.ok && i.ok, gruende: [...t.gruende, ...i.gruende] };
}

/* --- Haltbarkeit -------------------------------------------------------- */

const TAG_MS = 24 * 60 * 60 * 1000;
const alsTag = (iso) => String(iso || "").slice(0, 10);

export function verfallsdatum(erstelltAm, ttlTage = TTL_TAGE) {
  const d = new Date(`${alsTag(erstelltAm)}T00:00:00Z`);
  if (Number.isNaN(d.getTime())) return null;
  return new Date(d.getTime() + ttlTage * TAG_MS).toISOString().slice(0, 10);
}

export function abgelaufen(eintrag, heute) {
  const bis = eintrag?.verfaelltAm || verfallsdatum(eintrag?.erstelltAm);
  if (!bis) return true;                 // ohne Datum: im Zweifel weg
  return alsTag(heute) > bis;
}

/**
 * Trennt den Bestand. Abgelaufenes wird verworfen, nicht verlängert und nicht
 * nachgeprüft - Ersatz entsteht später an einem günstigen Tag.
 */
export function bestandPruefen(bestand = [], heute) {
  const gueltig = [];
  const verfallen = [];
  for (const e of bestand) {
    if (abgelaufen(e, heute)) verfallen.push({ ...e, grund: "TTL abgelaufen" });
    else if (Number(e?.regelVersion) !== REGEL_VERSION) verfallen.push({ ...e, grund: `nach Regelversion ${e?.regelVersion ?? "?"} aufgenommen, es gilt ${REGEL_VERSION}` });
    else if (!vollstaendig(e).ok) verfallen.push({ ...e, grund: `unvollständig: ${vollstaendig(e).fehlend.join(", ")}` });
    else gueltig.push(e);
  }
  return { gueltig, verfallen };
}

/**
 * Wie viele Beiträge fehlen zum Zielbestand.
 *
 * Es gibt keinen Mindestverbrauch: Ist der Bestand voll, ist der Bedarf null,
 * und an einem Tag ohne Restbudget wird nichts erzeugt. Der Bedarf sagt, was
 * fehlt - nicht, dass es heute entstehen muss.
 */
export function bedarf(bestand = [], heute, ziel = ZIEL_BESTAND) {
  return Math.max(0, ziel - bestandPruefen(bestand, heute).gueltig.length);
}

/* --- Entnahme ----------------------------------------------------------- */

/**
 * Nimmt einen Beitrag aus dem Vorrat - oder keinen.
 *
 * Hier wird NICHTS bezahlt und nichts nachgeprüft. Die Auswahl arbeitet nur
 * mit dem, was schon dasteht: Haltbarkeit, Vollständigkeit, und ob das Thema
 * kürzlich schon erschienen ist.
 *
 * Genommen wird das ÄLTESTE taugliche Stück: Was zuerst verfällt, wird zuerst
 * gebraucht.
 */
export function entnehmen(bestand = [], { heute, ledger = null, dublettenTage = 60 } = {}) {
  const { gueltig, verfallen } = bestandPruefen(bestand, heute);
  const jung = new Set();
  if (ledger?.beitraege?.length) {
    const grenze = new Date(new Date(`${alsTag(heute)}T00:00:00Z`).getTime() - dublettenTage * TAG_MS).toISOString().slice(0, 10);
    for (const b of ledger.beitraege) if (alsTag(b.datum) >= grenze && b.thema) jung.add(b.thema);
  }
  const frei = gueltig.filter((e) => !jung.has(e.themaId));
  if (!frei.length) {
    return {
      eintrag: null,
      rest: gueltig,
      verfallen,
      grund: gueltig.length
        ? `alle ${gueltig.length} Vorratsbeiträge behandeln ein Thema, das in den letzten ${dublettenTage} Tagen erschienen ist`
        : "kein gültiger Vorratsbeitrag vorhanden",
    };
  }
  const gewaehlt = [...frei].sort((a, b) => String(a.erstelltAm).localeCompare(String(b.erstelltAm)))[0];
  return {
    eintrag: gewaehlt,
    rest: gueltig.filter((e) => e.id !== gewaehlt.id),
    verfallen,
    grund: null,
  };
}

/* --- Aufnahme ----------------------------------------------------------- */

/**
 * Baut einen Vorratseintrag - und nimmt ihn nur an, wenn beide Tore offen
 * sind und alles Nötige dabei ist. Ein halber Eintrag ist schlimmer als
 * keiner: Er belegt einen Platz und fällt am Blockadetag durch.
 */
export function eintragBauen({ id, kanal, thema, beitrag, bildUrls, caption, hashtags = [], faktenFreigabe, erstelltAm }) {
  const regel = reserveTauglich({ thema, beitrag });
  const entwurf = {
    id, kanal,
    erstelltAm: alsTag(erstelltAm),
    verfaelltAm: verfallsdatum(erstelltAm),
    themaId: thema?.id ?? beitrag?.themaId ?? null,
    fach: thema?.fach ?? beitrag?.fach ?? null,
    typ: thema?.typ ?? null,
    format: beitrag?.format || "karussell",
    beitrag, bildUrls, caption, hashtags,
    faktenFreigabe,
    regelVersion: REGEL_VERSION,
    tauglichkeit: { ok: regel.ok, gruende: regel.gruende, geprueftAm: new Date().toISOString() },
  };
  const voll = vollstaendig(entwurf);
  if (!regel.ok || !voll.ok) {
    return { ok: false, eintrag: null, gruende: [...regel.gruende, ...voll.fehlend.map((f) => `fehlt: ${f}`)] };
  }
  return { ok: true, eintrag: entwurf, gruende: [] };
}
