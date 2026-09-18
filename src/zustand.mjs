/* ==========================================================================
   Zustandssicherung eines Laufs: Kosten festschreiben, Plan und Fehlerliste
   ablegen, committen, pushen.

   Warum das ein eigenes Modul ist: Am 18.09. gingen zwei Laeufe verloren, weil
   die Sicherung an einem Rueckgabepfad vorbeilief. Die Reparatur war ein
   `finally` am Prozessende - mit einem einzigen Schalter, der zu frueh gesetzt
   wurde. Scheiterte der Push, galt der Zustand trotzdem als gesichert, und der
   zweite Anlauf im `finally` konnte nichts mehr retten.

   Deshalb vier getrennte Zustaende statt einem:

     kostenSnapshot    Die Abrechnung des Laufs, genau einmal erhoben. Ein
                       zweiter Aufruf von kostenAbschluss() koennte inzwischen
                       gewachsene Posten mitzaehlen.
     kostenAngewendet  Der Snapshot steht in kosten.json. Erst danach gilt er
                       als verbucht. Scheitert das Schreiben - oder etwas
                       zwischen Erheben und Schreiben -, bleibt der Schalter
                       aus, und der naechste Versuch verbucht denselben
                       Snapshot: kein Verlust, keine Doppelzaehlung.
     vorbereitet       Dateien geschrieben und Commit erzeugt. Scheitert der
                       Commit wirklich (nicht: "nichts zu committen"), bleibt
                       der Schalter aus und der Fehler faellt sichtbar durch.
     durable           Push BESTAETIGT. Nicht: Push versucht. Gibt push()
                       false zurueck, ohne dass ein Modus ohne Remote-
                       Durability gewaehlt ist, bleibt der Zustand nicht
                       durable - und der naechste Versuch holt es nach.

   So ist jeder Schritt einzeln wiederholbar: Ein misslungener Push wird im
   `finally` noch einmal versucht, ohne dass die Kosten erneut addiert werden.
   ========================================================================== */

/**
 * Baut die Sicherungsfunktion eines Laufs.
 *
 * Bewusst ohne Import von hosting/kosten: Die Abhaengigkeiten werden
 * hereingereicht, damit sich das Verhalten testen laesst, ohne Git, Netz und
 * Instagram zu brauchen.
 *
 * @param {object}   o
 * @param {object}   o.hosting         Asset-Zweig (jsonLesen/jsonSchreiben/aufraeumen/commit/push)
 * @param {object}   o.plan            Tagesplan (wird mitgespeichert)
 * @param {string}   o.datum           ISO-Datum des Laufs
 * @param {Function} o.kostenAbschluss () => {usd, aufrufe, cacheAnteil}
 * @param {Function} o.wochenKennung   (iso) => "2026-W38"
 * @param {Function} o.planSpeichern   (hosting, plan) => void
 * @returns {Function} async (nachricht) => {kostenFest, vorbereitet, durable}
 */
export function zustandsSicherung({ hosting, plan, datum, kostenAbschluss, wochenKennung, planSpeichern, remoteNoetig }) {
  let kostenSnapshot = null;
  let kostenAngewendet = false;
  let vorbereitet = false;
  let durable = false;
  let ohneRemote = false;
  /* Ohne ausdrueckliche Angabe entscheidet das Hosting: Wer nicht pusht,
     verlangt auch keine Remote-Durability. */
  const brauchtRemote = remoteNoetig ?? (hosting.pushen !== false);

  const sichern = async (nachricht = `Zustand ${datum}`) => {
    if (!vorbereitet) {
      /* Erheben und Verbuchen sind zwei Schritte. Frueher stand der Schalter
         schon vor dem Schreiben auf true: Ging danach etwas schief, war der
         Betrag weder in kosten.json noch wiederholbar - er fehlte einfach. */
      if (!kostenAngewendet) {
        if (!kostenSnapshot) kostenSnapshot = kostenAbschluss();
        if (kostenSnapshot.aufrufe) {
          const k = hosting.jsonLesen("kosten.json", { wochen: {} });
          if (!k.wochen) k.wochen = {};
          const kw = wochenKennung(datum);
          const w = k.wochen[kw] || { usd: 0, aufrufe: 0, cacheSumme: 0 };
          w.usd += kostenSnapshot.usd;
          w.aufrufe += kostenSnapshot.aufrufe;
          w.cacheSumme += kostenSnapshot.cacheAnteil * kostenSnapshot.aufrufe;
          w.cacheAnteil = w.cacheSumme / w.aufrufe;
          k.wochen[kw] = w;
          hosting.jsonSchreiben("kosten.json", k);
        }
        /* Erst hier: Der Betrag steht in der Datei. */
        kostenAngewendet = true;
      }

      /* Die folgenden Schreibvorgaenge sind wiederholbar: Sie setzen den
         Dateiinhalt, sie haengen nichts an. */
      const fehlerListe = hosting.jsonLesen("fehler.json", []);
      for (const e of [...(plan?.beitraege || []), ...(plan?.stories || [])]) {
        if (e.fehler && !fehlerListe.includes(e.fehler)) fehlerListe.push(e.fehler);
      }
      hosting.jsonSchreiben("fehler.json", fehlerListe.slice(-50));

      const geloescht = hosting.aufraeumen();
      if (geloescht) hosting.commit(`Alte Bilder entfernt (${geloescht} Tage)`);
      planSpeichern(hosting, plan);
      /* commit() wirft bei echten Git-Fehlern und liefert false, wenn es
         schlicht nichts zu committen gibt. Beides ist in Ordnung - nur ein
         geworfener Fehler darf `vorbereitet` nicht setzen. */
      hosting.commit(nachricht);
      vorbereitet = true;
    }

    if (!durable) {
      /* Der Rueckgabewert entscheidet, nicht der blosse Aufruf. push() liefert
         false, wenn gar nicht gepusht wird (IG_NO_PUSH) - dann ist der Zustand
         lokal durable und mehr wird nicht verlangt. Verlangt der Lauf aber
         Remote-Durability und der Push bestaetigt sie nicht, bleibt der
         Schalter aus: Der naechste Versuch holt denselben Commit nach. */
      const gepusht = await hosting.push();
      if (gepusht) durable = true;
      else if (!brauchtRemote) { durable = true; ohneRemote = true; }
      else throw new Error("Push nicht bestaetigt - der Zustand ist nicht durable.");
    }
    return { kostenSnapshot, kostenAngewendet, vorbereitet, durable, ohneRemote };
  };

  sichern.stand = () => ({
    kostenErhoben: !!kostenSnapshot, kostenAngewendet, vorbereitet, durable, ohneRemote,
  });
  return sichern;
}
