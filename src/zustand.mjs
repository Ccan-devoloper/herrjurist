/* ==========================================================================
   Zustandssicherung eines Laufs: Kosten festschreiben, Plan und Fehlerliste
   ablegen, committen, pushen.

   Warum das ein eigenes Modul ist: Am 18.09. gingen zwei Laeufe verloren, weil
   die Sicherung an einem Rueckgabepfad vorbeilief. Die Reparatur war ein
   `finally` am Prozessende - mit einem einzigen Schalter, der zu frueh gesetzt
   wurde. Scheiterte der Push, galt der Zustand trotzdem als gesichert, und der
   zweite Anlauf im `finally` konnte nichts mehr retten.

   Deshalb drei getrennte Zustaende statt einem:

     kostenFest    Die Wochenkosten sind fortgeschrieben. Genau einmal, sonst
                   zaehlt ein Wiederholungsversuch denselben Betrag zweimal.
     vorbereitet   Dateien geschrieben und Commit erzeugt. Scheitert der
                   Commit wirklich (nicht: "nichts zu committen"), bleibt der
                   Schalter aus und der Fehler faellt sichtbar durch.
     durable       Push bestaetigt. Erst danach ist der Zustand ausser
                   Reichweite des Containers, der gleich verschwindet.

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
export function zustandsSicherung({ hosting, plan, datum, kostenAbschluss, wochenKennung, planSpeichern }) {
  let kostenFest = false;
  let vorbereitet = false;
  let durable = false;

  const sichern = async (nachricht = `Zustand ${datum}`) => {
    if (!vorbereitet) {
      /* Kosten genau einmal - auch dann, wenn der Commit darunter scheitert
         und dieser Block ein zweites Mal durchlaufen wird. */
      if (!kostenFest) {
        kostenFest = true;
        const kosten = kostenAbschluss();
        if (kosten.aufrufe) {
          const k = hosting.jsonLesen("kosten.json", { wochen: {} });
          if (!k.wochen) k.wochen = {};
          const kw = wochenKennung(datum);
          const w = k.wochen[kw] || { usd: 0, aufrufe: 0, cacheSumme: 0 };
          w.usd += kosten.usd;
          w.aufrufe += kosten.aufrufe;
          w.cacheSumme += kosten.cacheAnteil * kosten.aufrufe;
          w.cacheAnteil = w.cacheSumme / w.aufrufe;
          k.wochen[kw] = w;
          hosting.jsonSchreiben("kosten.json", k);
        }
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
      await hosting.push();
      durable = true;
    }
    return { kostenFest, vorbereitet, durable };
  };

  sichern.stand = () => ({ kostenFest, vorbereitet, durable });
  return sichern;
}
