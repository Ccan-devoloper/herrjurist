/**
 * Motive zeichnen lassen statt suchen.
 *
 * Die Stockfoto-Suche hatte zwei Fehler, die sich nicht wegkonfigurieren
 * lassen: Das gefundene Foto passte oft nicht zum Thema (Atemmasken bei
 * Betrugsstrafbarkeit), und das nachträgliche Freistellen misslang häufig -
 * am 13.09. stand auf beiden Kanälen ein halbdurchsichtiger Schleier auf der
 * Kachel. Ein erzeugtes Motiv umgeht beides: Es entsteht zum Thema und kommt
 * bereits freigestellt, mit durchsichtigem Grund. Und es braucht keinen
 * Bildnachweis auf der Kachel.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { ffmpegPfad } from "./stimme.mjs";
import { CONFIG } from "./config.mjs";
import { bildAufruf } from "./anbieter.mjs";
import { alphaProfil, FESTIGKEIT_MIN, zuschneiden, bestickern, masse, randkontakt, randVerdacht, freistellen } from "./freistellen.mjs";

export const bildKiAktiv = () => Boolean(CONFIG.bilder.ki.aktiv && CONFIG.bilder.ki.key);

/* Nennt die Szene ueberhaupt einen Menschen? Bis zum 14.09. wurde diese Frage
   nie gestellt - der Auftrag sprach immer von Armen, Haenden, Gliedmassen und
   Anatomie. Damit wurde aus "scale balancing two stacks" zuverlaessig ein
   Mensch, der neben einer Waage steht, und aus einem Reel ueber das steuerliche
   Einlagekonto eine Bilderfolge mit einem Mann und einem Einmachglas. */
const MENSCH = /\b(persons?|people|m[ae]n|wom[ae]n|someone|somebody|child(ren)?|students?|clerks?|customers?|workers?|employees?|judges?|lawyers?|defendants?|witnesses?|teachers?|vendors?|applicants?|officers?|hands?)\b/i;
/* "official" ist die Stolperfalle: als Hauptwort ein Beamter, als Beiwort nur
   amtlich. "official notice with embossed seal" ist ein Schriftstueck, "stopped
   by official" ein Mensch. Unterschieden wird an der Stellung - steht danach
   noch ein Hauptwort, ist es ein Beiwort. */
const AMTSPERSON = /\bofficials?\b(?!\s+[a-z])|\bofficials?\s+\w+ing\b/i;

export function menschInSzene(text) {
  return MENSCH.test(text) || AMTSPERSON.test(text);
}

/* Der Hausstil. Zwei Dinge sind nicht verhandelbar: kein Text im Bild (Modelle
   malen Buchstaben, die wie Recht aussehen und keines sind - auf einem
   Examenskanal ein Eigentor) und genau ein Gegenstand, damit das Motiv auf der
   Kachel noch zu erkennen ist. */
export function bildAuftrag(szene, { stil = "", look = "flach" } = {}) {
  const text = String(szene).trim();
  const mitMensch = menschInSzene(text);
  const foto = look === "foto";
  return [
    /* Die Ansage steht vorn und am Ende, und sie lautet "ohne Hintergrund" -
       so, wie der Betreiber sie am 18.09. selbst erfolgreich erprobt hat. Das
       Wort "transparent" kommt im Auftrag nicht mehr vor: Es ist ein Wort aus
       der Dateiwelt, nicht aus der Bildwelt, und das Modell hat darauf mit
       gemalten Studiohintergruenden geantwortet. */
    "Cut-out image WITHOUT ANY BACKGROUND.",
    foto ? `Photorealistic photograph: ${text}.` : `Flat vector illustration: ${text}.`,
    "Exactly one clear subject, centred, seen from the front or in three-quarter view.",
    /* "nothing cropped" allein hat nicht gereicht: Am 14.09. kam eine Figur
       zurueck, deren Kopf oben glatt am Bildrand endete. Das Modell braucht
       die Ansage als Platzvorgabe, nicht als Verbot. */
    "Frame the subject with clear empty margin on all four sides: the whole subject must be inside the image with visible empty space above the head, below the feet and to the left and right. Never let any part touch or run past an edge. Rather draw the subject smaller than risk cutting it off.",
    ...(mitMensch
      /* Haende und kleine Requisiten sind die Stelle, an der billige Bilder
         auseinanderfallen: verbogene Finger, ein Stift ohne Spitze, eine Lampe,
         die keine mehr ist. Also gar nichts greifen lassen. */
      ? ["Keep the pose calm and simple: arms relaxed at the sides or lightly folded, hands open and empty.",
        "Do not let the subject hold, grip or carry anything - if the scene mentions an object, place that object on the ground or on a surface next to the subject, clearly separate from the hands.",
        "No small fiddly props, no thin stems, no objects near the face, no crossed or overlapping limbs.",
        "Correct anatomy and natural proportions."]
      /* Kein Mensch in der Szene: dann auch keinen dazuerfinden. Das Modell
         moebliert eine Szene sonst von sich aus mit einer Figur, und die Figur
         zieht dann alle Aufmerksamkeit auf sich - der Gegenstand, um den es
         geht, wird zur Requisite in ihrer Hand. */
      : [`${foto ? "Photograph" : "Draw"} the object itself. Absolutely no people, no faces, no hands, no arms, no body parts, no silhouettes of persons.`,
        "Show the object complete and instantly recognisable, at a slight angle so its shape reads clearly - large within the margin, but never beyond it."]),
    foto
      /* "Echt" heisst: Materialien, Licht und Proportionen wie in einer
         Fotografie. Ohne diese Ansage liefert das Modell auf "photograph"
         gern ein glattes 3D-Rendering mit Cartoon-Gesicht. */
      ? "Real materials and textures, soft natural daylight, gentle shallow depth of field, true-to-life colours, the look of a 50 mm lens. It must read as a genuine photograph - not an illustration, not a 3D render, not a painting, no cartoon proportions, no exaggerated features."
      : "Bold simple shapes, even line weight, flat colours with soft shading, clean readable silhouette.",
    stil,
    "Absolutely no text, no letters, no words, no numbers, no signage, no logos, no watermark, no signature.",
    /* Urkunden, Formulare und Schilder sind die Stelle, an der das Verbot
       kippt: Das Modell "beschriftet" sie wie von selbst. Am 17.09. stand
       "FARMHOUSE DEED" gross im Reel. Also Leerseiten und Platzhalterlinien. */
    "If the subject is a document, certificate, form, letter, book cover or sign, draw it with blank pages or abstract wavy placeholder lines only - never legible or pseudo-legible writing, never a title line, never a stamp with words.",
    "Deliver it WITHOUT A BACKGROUND: nothing behind the subject, no backdrop, no room, no surface, no ground shadow, no frame - the subject cut out and standing alone.",
  ].filter(Boolean).join(" ");
}

/**
 * Zeichnet ein Motiv und gibt es freigestellt zurück.
 * @returns {Promise<{pfad:string, breite:number, hoehe:number}|null>} null = nicht brauchbar
 */
export async function motivZeichnen(szene, { randFarbe = null, stil = "", zweck = "bild", look = null } = {}) {
  /* Titelbilder im eingestellten Look, Erklärfiguren immer flach. */
  const aussehen = look || (zweck === "erklaerbild" ? "flach" : CONFIG.bilder.ki.look || "flach");
  if (!bildKiAktiv() || !szene) return null;
  /* Der Zweck entscheidet, welcher Topf gilt. Bis zum 17.09. stand hier für
     JEDES Bild „Bild zeichnen" - auch für die Figuren des Erklärvideos, die
     unter dem Zweck „erklaerbild" laufen und dafür eine eigene Rücklage
     haben. Geprüft wurde dann unter dem Schlüssel „bild": mit dem
     Sicherheitsabstand für Schmuckbilder UND mit der eigenen Rücklage als
     FREMDER Rücklage. Das Bild blockierte sich damit selbst, sobald der Tag
     eng wurde - und das Reel fiel auf das klassische Layout zurück, obwohl
     das Geld dafür ausdrücklich zurückgelegt war. Der Schlüssel muss im
     Zwecktext stehen, weil kosten.mjs ihn daraus liest. */
  const ki = CONFIG.bilder.ki;
  let daten;
  try {
    /* Ein gezeichnetes Motiv ist fast immer optionale Qualitaet: Ohne es
       bleibt die Icon-Buehne. Es geht deshalb durch dieselbe Tuer wie jeder
       bezahlte Aufruf - und hinter alle Pflichtruecklagen.

       Der durchsichtige Hintergrund wird immer verlangt - im Auftragstext und
       hier im Aufruf. Kommt er so zurueck, ist das Motiv ohne weiteren
       Schritt verwendbar, und genau das ist der Regelfall beim flachen Look. */
    daten = await bildAufruf({
      zweck, modell: ki.modell, optional: true, preisUsd: ki.preisUsd, zeitlimitMs: ki.zeitlimitMs, slot: szene,
      auftrag: {
        key: ki.key,
        koerper: { model: ki.modell, prompt: bildAuftrag(szene, { stil, look: aussehen }), n: 1, size: ki.groesse, quality: ki.guete, background: "transparent", output_format: "png" },
      },
    });
  } catch (e) {
    console.warn(`  ! Motiv zeichnen fehlgeschlagen (${e.name === "AbortError" ? "Zeitlimit" : e.message.slice(0, 120)}) - Titelfolie bleibt beim Icon.`);
    return null;
  }
  const b64 = daten?.data?.[0]?.b64_json;
  /* Bezahlt wird, sobald das Bild da ist - auch wenn es gleich verworfen wird.
     Ein Posten, der nicht gebucht wird, fehlt dem Tagesdeckel. */
  if (!b64) { console.warn("  ! Motiv zeichnen: keine Bilddaten zurückgekommen."); return null; }
  const roh = path.join(os.tmpdir(), `ki-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  fs.writeFileSync(roh, Buffer.from(b64, "base64"));
  /* Beim Foto-Look haelt sich das Modell oft nicht an den Transparenzwunsch:
     Die Probe vom 18.09. zeichnete dasselbe Motiv dreimal, und alle drei kamen
     MIT Studiohintergrund zurueck, obwohl Transparenz bestellt war. Wer eine
     Fotografie verlangt, bekommt einen Hintergrund dazugemalt.

     Bisher wurde so ein Bild verworfen. Uebrig blieb damit gerade das, was wie
     ein Aufkleber aussieht - die flache Illustration -, und der Foto-Look kam
     nie auf die Kachel. Jetzt wird nachgeholt, was das Modell schuldig blieb:
     freistellen mit rembg, dem Werkzeug, das die gefundenen Fotos seit jeher
     ausschneidet. Es kostet nichts und prueft Deckung, Festigkeit, Anschnitt
     und Seitenverhaeltnis gleich mit.

     Beim flachen Look bleibt es beim Verwerfen: Dort liefert das Modell die
     Transparenz zuverlaessig, und ein Bild ohne sie ist dort ein Fehlschlag. */
  const vorabProfil = alphaProfil(roh);
  const alphaTaugt = vorabProfil && vorabProfil.festigkeit >= FESTIGKEIT_MIN && vorabProfil.belegt >= 0.02;
  if (aussehen === "foto" && !alphaTaugt) {
    const frei = freistellen(roh, { randFarbe: null, schaerfePruefen: false });
    fs.rmSync(roh, { force: true });
    if (!frei?.pfad) { console.warn("  ! Gezeichnetes Foto kam mit Hintergrund und liess sich nicht freistellen - Titelfolie bleibt beim Icon."); return null; }
    const ohneRandFoto = frei.pfad.replace(/\.png$/, "-roh.png");
    fs.copyFileSync(frei.pfad, ohneRandFoto);
    const fertigFoto = randFarbe ? bestickern(frei.pfad, randFarbe) : frei.pfad;
    const mFoto = masse(fertigFoto) || {};
    console.log(`  → Motiv fotografiert: „${szene}" (kam mit Hintergrund, freigestellt, Deckung ${(frei.deckung * 100).toFixed(0)} %)`);
    return { pfad: fertigFoto, ohneRand: ohneRandFoto, breite: mFoto.breite || null, hoehe: mFoto.hoehe || null };
  }
  /* Dieselbe Härteprüfung wie beim Freisteller: Ein weicher Schleier ist auch
     dann ein Schleier, wenn ihn niemand ausgeschnitten hat. */
  const prof = alphaProfil(roh);
  if (!prof || prof.festigkeit < FESTIGKEIT_MIN || prof.belegt < 0.02) {
    console.warn(`  ! Gezeichnetes Motiv unbrauchbar (${prof ? `${(prof.festigkeit * 100).toFixed(0)} % deckend, ${(prof.belegt * 100).toFixed(0)} % belegt` : "kein Alphakanal"}) - Titelfolie bleibt beim Icon.`);
    fs.rmSync(roh, { force: true });
    return null;
  }
  /* Angeschnitten? Diese Prüfung gab es bisher nur für gesuchte Fotos, nicht
     für gezeichnete Motive - und genau dort fehlte sie. Am 14.09. stand auf
     der Kachel zum Erbrecht eine Frau, deren Kopf oben glatt abgeschnitten
     war: 46 % der obersten Bildzeile waren deckend, der Stickerrand lief quer
     über den Scheitel. Das Modell hatte die Figur über den Rand hinaus
     gezeichnet, und niemand hat hingesehen. */
  const rand = randkontakt(roh);
  const verdacht = randVerdacht(rand);
  if (verdacht) {
    console.warn(`  ! Gezeichnetes Motiv angeschnitten (${verdacht} deckend am Bildrand) – verworfen, Motiv kommt aus dem Archiv oder es bleibt beim Icon.`);
    fs.rmSync(roh, { force: true });
    return null;
  }
  const geschnitten = zuschneiden(roh);
  /* Eine randlose Kopie fuers Archiv: Der farbige Rand haengt am Rechtsgebiet
     und wird bei jeder Verwendung neu gezogen. */
  const ohneRand = geschnitten.replace(/\.png$/, "-roh.png");
  fs.copyFileSync(geschnitten, ohneRand);
  const fertig = randFarbe ? bestickern(geschnitten, randFarbe) : geschnitten;
  const m = masse(fertig) || {};
  console.log(`  → Motiv gezeichnet: „${szene}" (${(prof.festigkeit * 100).toFixed(0)} % deckend)`);
  return { pfad: fertig, ohneRand, breite: m.breite || null, hoehe: m.hoehe || null };
}

/**
 * Holt ein archiviertes Motiv hervor und zieht den Rand in der heutigen Farbe.
 * @returns {{pfad:string, breite:number, hoehe:number}|null}
 */
export function motivHervorholen(quelle, { randFarbe = null } = {}) {
  if (!fs.existsSync(quelle)) return null;
  const kopie = path.join(os.tmpdir(), `archiv-${Date.now()}-${Math.random().toString(36).slice(2, 8)}.png`);
  /* Der Rand wird auf einem PNG gezogen; ein archiviertes WebP muss dafuer
     zurueckverwandelt werden. */
  if (/\.webp$/i.test(quelle)) {
    const s = spawnSync(ffmpegPfad(), ["-y", "-loglevel", "error", "-i", quelle, "-frames:v", "1", "-update", "1", kopie], { encoding: "utf8", timeout: 60000 });
    if (s.status !== 0 || !fs.existsSync(kopie)) { console.warn("  ! Archiviertes Motiv nicht lesbar."); return null; }
  } else fs.copyFileSync(quelle, kopie);
  const fertig = randFarbe ? bestickern(kopie, randFarbe) : kopie;
  const m = masse(fertig) || {};
  return { pfad: fertig, breite: m.breite || null, hoehe: m.hoehe || null };
}
