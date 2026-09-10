/* ==========================================================================
   Themenpool für den Instagram-Bot (erstes und zweites juristisches
   Staatsexamen).

   Anders als beim Steuerkanal gibt es keine Webseitendaten als Quelle: Der
   Stoff steht in daten/themen.mjs, abgeleitet aus dem Zuschnitt der
   bestehenden Beiträge des Kanals – Frage zuerst, dann Abgrenzung,
   Definition oder Streitstand.

   Die Einträge sind bewusst schlank. Der Autor (autor.mjs) formuliert alles
   neu, der Faktencheck prüft nach. Was hier steht, ist Gerüst, nicht Text.
   ========================================================================== */

import { THEMEN } from "../daten/themen.mjs";
import { GEBIETE, FAECHER as FACH_TABELLE } from "../daten/gebiete.mjs";

/* Der Renderer und der Autor erwarten „klausur“ als Markenachse – hier ist
   das das Rechtsgebiet. Zivilrecht 1, Strafrecht 2, Öffentliches Recht 3. */
export const FAECHER = Object.fromEntries(
  Object.entries(FACH_TABELLE).map(([id, f]) => [id, { ...f, klausur: f.gebiet }]),
);

export const KLAUSUREN = {
  1: { label: "Zivilrecht", kurz: "Zivilrecht" },
  2: { label: "Strafrecht", kurz: "Strafrecht" },
  3: { label: "Öffentliches Recht", kurz: "Öffentliches Recht" },
};

export { GEBIETE };

/* Welche Sorte Thema ist das? Der Planer wählt danach aus, welches Format zu
   welchem Thema passt: Ein Schema trägt einen Schema-Beitrag, eine Abgrenzung
   trägt einen Vergleich. Erkennbar ist das an der Frage selbst. */
function typVon(titel) {
  if (/^Wie prüft man|^Wie wird .* geprüft|Voraussetzungen|^Wie funktioniert|Aufbau/i.test(titel)) return "schema";
  if (/Unterschied|unterscheide|Abgrenzung|grenzt man|Verhältnis zwischen/i.test(titel)) return "begriff";
  if (/berechne|Berechnung|Grenzwert/i.test(titel)) return "formel";
  if (/^Welche|^Was sind die|^Wann liegt|^Wann ist|^Wann tritt/i.test(titel)) return "karteikarte";
  return "modul";
}

/* Streitstände erkennt man daran, dass zwei Ansichten gegeneinander stehen –
   sie tragen das Format „streitstand“ besonders gut. */
const istStreit = (t) => Boolean(t.kern?.lernziele?.some((z) => /Rechtsprechung|Literatur|herrschend|h\.M\.|a\.A\.|Theorie|gegen/i.test(z)));

export function themenpool() {
  return THEMEN.map((t, i) => {
    const fach = FAECHER[t.fach];
    if (!fach) throw new Error(`Thema ${i} nennt ein unbekanntes Fach: ${t.fach}`);
    const typ = t.typ || typVon(t.titel);
    return {
      id: t.id || `${t.fach}-${String(i + 1).padStart(3, "0")}`,
      fach: t.fach,
      klausur: fach.klausur,
      typ,
      streit: istStreit(t),
      titel: t.titel,
      normen: t.normen || [],
      kern: {
        /* Die Frage ist der Titel – der Kanal fragt zuerst und antwortet dann. */
        frage: t.titel,
        lernziele: t.kern?.lernziele || [],
        pruefschritte: t.kern?.pruefschritte || [],
        merksatz: t.kern?.merksatz || "",
        fehler: t.kern?.fehler || [],
      },
      prioritaet: t.prioritaet || "mittel",
      /* Erstes oder zweites Examen? Steht nur bei Themen aus dem Handbuch;
         der Autor erwähnt es, wo es den Zuschnitt ändert (Gutachtenstil im
         ersten, Urteils-/Aktenvortragsstil im zweiten Examen). */
      examen: t.examen || null,
    };
  });
}

export function poolStatistik(pool = themenpool()) {
  const je = (key) => pool.reduce((acc, t) => { acc[t[key]] = (acc[t[key]] || 0) + 1; return acc; }, {});
  return { gesamt: pool.length, jeFach: je("fach"), jeTyp: je("typ"), jePrioritaet: je("prioritaet"), jeKlausur: je("klausur"), streit: pool.filter((t) => t.streit).length };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(JSON.stringify(poolStatistik(), null, 2));
}
