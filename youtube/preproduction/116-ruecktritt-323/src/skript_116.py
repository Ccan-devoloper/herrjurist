"""Folge 116 · Rücktritt § 323 BGB: Das Prüfungsschema mit Fristsetzung (Mi · Examenswissen · Zivilrecht/Schuldrecht AT,
Format Schema). Beispielfall nach dem Plan-Hook („Der Online-Shop liefert die bezahlte Spielkonsole einfach nicht.“):
Leni (privat, Verbraucherin) bestellt am 1.7.2026 im Online-Shop von Ottmar (Unternehmer) eine Spielkonsole für 499 €,
zahlt per Vorkasse sofort; Lieferung versprochen bis 8.7.2026. Keine Lieferung. Am 15.7. Frist per E-Mail „bis morgen“.
Ottmar antwortet: Lieferant im Stich gelassen, Konsole kommt bald, bitte Geduld. Am 30.7. (nichts geliefert) erklärt
Leni per E-Mail den Rücktritt und verlangt die 499 € zurück.
Kern als Schema: I. Rücktrittsrecht § 323 Abs. 1 (Wortlautkarte) – 1. gegenseitiger Vertrag; 2. fällige, durchsetzbare
Leistung nicht erbracht (§ 271, § 475 Abs. 1; V ZR 11/18 Rn. 38; Verweis 103); 3. angemessene Frist erfolglos abgelaufen
(zu kurze Frist: VIII ZR 318/19 Rn. 28, VIII ZR 351/19 Rn. 28, 43; Zeitstrahl); 4. Entbehrlichkeit § 323 Abs. 2 Nr. 1–3
(VIII ZR 226/14 Rn. 33; BT-Drucks. 17/12637 S. 59); 5. kein Ausschluss § 323 Abs. 5, 6; kein Vertretenmüssen, kein Verzug
(BT-Drucks. 14/6040 S. 93, 184; Abgrenzung § 281); II. Rücktrittserklärung § 349 (Wortlautkarte); III. § 346 Abs. 1;
Abgrenzung § 326 Abs. 5 und § 437 Nr. 2; Ergebnis; Klausurtipp; Schema; Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Leni (laura_ruhig), Ottmar (william); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Leni": "laura_ruhig", "Ottmar": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Leni bestellt online, 1. Juli 2026 ------------------------------------------------------------------
    ("[fall]Leni bestellt am ersten Juli zweitausendsechsundzwanzig in einem Online-Shop eine Spielkonsole für "
     "vierhundertneunundneunzig Euro. [vork]Sie zahlt per Vorkasse, sofort. [ltermin]Versprochen ist die Lieferung bis "
     "zum achten Juli.", 0.3),
    ("[le1]Bezahlt. In einer Woche ist sie da.", 0.3, "Leni"),
    # --- A2 Fall: Warten, Fristsetzung -----------------------------------------------------------------------------------
    ("[warten]Doch der achte Juli vergeht, und kein Paket kommt. [mail]Am fünfzehnten Juli schreibt Leni dem Shop "
     "eine E-Mail.", 0.3),
    ("[le2]Liefern Sie die Konsole bitte bis morgen.", 0.3, "Leni"),
    # --- A3 Fall: im Lager von Ottmar ------------------------------------------------------------------------------------
    ("[ott]Der Shop gehört Ottmar. [lager]Sein Regal ist leer.", 0.3),
    ("[ot1]Mein Lieferant hat mich im Stich gelassen. Die Konsole kommt bald, bitte haben Sie noch etwas Geduld.", 0.3,
     "Ottmar"),
    # --- A4 Fall: Rücktritt ----------------------------------------------------------------------------------------------
    ("[still]Zwei Wochen später ist immer noch nichts da. [ruecktr]Am dreißigsten Juli schreibt Leni erneut.", 0.3),
    ("[le3]Ich trete vom Kaufvertrag zurück. Bitte überweisen Sie mir die vierhundertneunundneunzig Euro zurück.", 0.3,
     "Leni"),
    ("[frage]Kann Leni wirksam zurücktreten? [frage2]Und war ihre Frist bis morgen nicht viel zu kurz?", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau --------------------------------------------------------------------------------------------------------
    ("[plan]Der Rücktritt hat drei Ebenen: [p1]Römisch eins, ein Rücktrittsrecht, hier aus Paragraf "
     "dreihundertdreiundzwanzig. [p2]Römisch zwei, die Rücktrittserklärung. [p3]Und römisch drei, die Rechtsfolge.", PS),
    # --- D § 323 Abs. 1 (Wortlaut) ---------------------------------------------------------------------------------------
    ("[w1]Paragraf dreihundertdreiundzwanzig Absatz eins: Erbringt bei einem gegenseitigen Vertrag der Schuldner eine "
     "fällige Leistung nicht oder nicht vertragsgemäß, so kann der Gläubiger, wenn er dem Schuldner erfolglos eine "
     "angemessene Frist zur Leistung oder Nacherfüllung bestimmt hat, vom Vertrag zurücktreten.", P),
    # --- E I. 1. Gegenseitiger Vertrag -----------------------------------------------------------------------------------
    ("[g1]Erstens: ein gegenseitiger Vertrag. [g2]Der Kaufvertrag ist einer: Ottmar schuldet die Konsole, Leni den "
     "Kaufpreis, Paragraf vierhundertdreiunddreißig.", P),
    # --- F I. 2. Fällige, durchsetzbare Leistung nicht erbracht -----------------------------------------------------------
    ("[f1]Zweitens: Der Schuldner erbringt eine fällige Leistung nicht. [f2]Vereinbart war die Lieferung bis zum achten "
     "Juli. Spätestens dann ist sie fällig, und sie bleibt aus. [f3]Ohne Termin wäre sie nach Paragraf "
     "zweihunderteinundsiebzig sofort fällig; beim Verbrauchsgüterkauf kann der Käufer sie nach Paragraf "
     "vierhundertfünfundsiebzig nur unverzüglich verlangen. [f4]Die Leistung muss auch durchsetzbar sein: Leni hat "
     "schon bezahlt, Ottmar hat keine Einrede. [f103]Mehr dazu im Video zu Einwendung und Einrede.", P),
    # --- G I. 3. Angemessene Frist, erfolglos abgelaufen (Zeitstrahl) -----------------------------------------------------
    ("[fr1]Drittens: eine angemessene Frist zur Leistung, erfolglos abgelaufen. [fr2]Leni setzt am fünfzehnten Juli "
     "eine Frist bis morgen. [fr3]Für eine Lieferung ist das zu kurz. [fr4]Unwirksam ist die Fristsetzung deshalb aber "
     "nicht: Nach dem Bundesgerichtshof setzt eine zu kurze Frist eine angemessene in Gang, [fr5]es sei denn, der "
     "Gläubiger macht deutlich, dass es ihm gerade auf die Kürze ankommt. [fr6]Leni wartet zwei Wochen. Das genügt "
     "jedenfalls, um eine Konsole zu verschicken. [fr7]Die Frist ist erfolglos abgelaufen.", PS),
    # --- H I. 4. Entbehrlichkeit, § 323 Abs. 2 ----------------------------------------------------------------------------
    ("[e1]Viertens: Manchmal ist die Fristsetzung entbehrlich, Paragraf dreihundertdreiundzwanzig Absatz zwei. "
     "[e2]Nummer eins: Der Schuldner verweigert die Leistung ernsthaft und endgültig. Dafür gelten strenge "
     "Anforderungen. [e2f]Ottmar bittet nur um Geduld, er will ja liefern. [e3]Nummer zwei, das Termingeschäft: Der "
     "Termin muss für den Gläubiger wesentlich sein, etwa weil er das vor Vertragsschluss mitgeteilt hat. [e3f]Ein "
     "bloßer Liefertermin genügt nicht. [e4]Nummer drei, besondere Umstände, gilt nur bei einer nicht vertragsgemäßen "
     "Leistung, nicht, wenn die Lieferung ausbleibt. [e5]Hier war die Frist also nötig, und Leni hat sie gesetzt.", PS),
    # --- I I. 5. Kein Ausschluss, § 323 Abs. 5, 6 -------------------------------------------------------------------------
    ("[a1]Fünftens: kein Ausschluss. [a2]Nach Absatz fünf kann der Gläubiger nach einer Teilleistung vom ganzen Vertrag "
     "nur zurücktreten, wenn er an ihr kein Interesse hat, [a2b]und bei einer Schlechtleistung schließt eine unerhebliche "
     "Pflichtverletzung den Rücktritt aus. [a3]Absatz sechs schließt ihn aus, wenn der Gläubiger allein oder weit "
     "überwiegend verantwortlich ist. [a4]Ottmar hat gar nichts geliefert, und Leni trifft keine Verantwortung.", P),
    # --- J Klausurfehler: kein Vertretenmüssen ----------------------------------------------------------------------------
    ("[vm1]Achtung, typischer Klausurfehler: Vertretenmüssen prüfen. [vm2]Paragraf dreihundertdreiundzwanzig verlangt "
     "es nicht. [vm3]Das Vertretenmüssen gehört zum Schadensersatz statt der Leistung, Paragraf zweihunderteinundachtzig "
     "mit Paragraf zweihundertachtzig Absatz eins. [vm4]Auch Verzug ist keine Voraussetzung des Rücktritts; den erklärt das Video zum Schuldnerverzug. [vm5]Wer an "
     "der Verzögerung schuld ist, spielt hier also keine Rolle.", PS),
    # --- K II. Rücktrittserklärung, § 349 (Wortlaut) ----------------------------------------------------------------------
    ("[r1]Römisch zwei: die Rücktrittserklärung. Paragraf dreihundertneunundvierzig: Der Rücktritt erfolgt durch "
     "Erklärung gegenüber dem anderen Teil. [r2]Die E-Mail von Leni an Ottmar vom dreißigsten Juli genügt.", P),
    # --- L III. Rechtsfolge, § 346 Abs. 1 ---------------------------------------------------------------------------------
    ("[rf1]Römisch drei: die Rechtsfolge. Nach Paragraf dreihundertsechsundvierzig Absatz eins sind die empfangenen "
     "Leistungen zurückzugewähren. [rf2]Ottmar muss die vierhundertneunundneunzig Euro zurückzahlen; [rf3]Leni hat nichts "
     "erhalten und muss nichts zurückgeben.", PS),
    # --- M Abgrenzung: § 326 Abs. 5, § 437 Nr. 2 --------------------------------------------------------------------------
    ("[ab1]Zur Abgrenzung: Ist die Leistung unmöglich, etwa weil eine bestimmte gebrauchte Konsole verbrannt ist, gilt "
     "Paragraf dreihundertsechsundzwanzig Absatz fünf: [ab1b]Rücktritt nach Paragraf dreihundertdreiundzwanzig, aber ohne "
     "Fristsetzung. [ab2]Und bei einer mangelhaften Konsole führt Paragraf vierhundertsiebenunddreißig Nummer zwei zu "
     "Paragraf dreihundertdreiundzwanzig, mit einer Frist zur Nacherfüllung.", PS),
    # --- N Ergebnis -------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Leni ist wirksam zurückgetreten. [erg2]Ottmar muss ihr die vierhundertneunundneunzig Euro "
     "zurückzahlen.", PS),
    # --- O Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Frist in drei Schritten: gesetzt, angemessen, erfolglos abgelaufen. [tipp2]Ist sie zu "
     "kurz, rechne mit der angemessenen Frist weiter, statt den Rücktritt abzulehnen.", PS),
    # --- P Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k1]Römisch eins: Rücktrittsrecht nach Paragraf dreihundertdreiundzwanzig Absatz eins. "
     "[k11]Eins: gegenseitiger Vertrag. [k12]Zwei: fällige, durchsetzbare Leistung nicht erbracht. [k13]Drei: "
     "angemessene Frist erfolglos abgelaufen, [k14]vier: oder Frist entbehrlich. [k15]Fünf: kein Ausschluss. "
     "[k2]Römisch zwei: Rücktrittserklärung. [k3]Römisch drei: Rückgewähr.", PS),
    # --- Q Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Rücktritt fragt nicht, wer schuld ist. [mk2]Er braucht eine fällige Leistung, die ausbleibt, "
     "[mk3]und eine Frist, die erfolglos abläuft, oder einen Grund, warum sie entbehrlich ist.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
