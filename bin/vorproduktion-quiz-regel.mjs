/* Frage- und Antwort-Stories erscheinen immer als Quiz: drei Optionen, eine
   richtig, in beiden Stories identisch. Fehlen die Felder, zeichnet der
   Renderer nur die nackte Frage – das ist seit dem 29.09.2026 unbemerkt
   passiert und wird deshalb vor jeder Übernahme geprüft. */
export function quizPruefen(tag, datum) {
  const paar = (tag.plan?.stories || []).filter((s) => s.art === "frage" || s.art === "antwort");
  for (const s of paar) {
    const x = tag.inhalte?.[s.slot];
    const ok = Array.isArray(x?.optionen) && x.optionen.length === 3
      && x.optionen.every((o) => typeof o === "string" && o.trim())
      && Number.isInteger(x.richtig) && x.richtig >= 0 && x.richtig < 3;
    if (!ok) throw new Error(`${datum} ${s.slot}: ${s.art}-Story braucht 3 Optionen und „richtig“ (Quiz-System)`);
  }
  const [a, b] = paar.map((s) => tag.inhalte[s.slot]);
  if (a && b && (JSON.stringify(a.optionen) !== JSON.stringify(b.optionen) || a.richtig !== b.richtig)) {
    throw new Error(`${datum}: Frage und Antwort haben unterschiedliche Quiz-Optionen`);
  }
}
