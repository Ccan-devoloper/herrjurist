"""Folge 185 · Unterlassene Hilfeleistung § 323c: Muss ich jedem helfen? (Mi · Examenswissen · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook („Mehrere Kunden steigen im Foyer einer Bankfiliale über einen bewusstlosen älteren Mann
hinweg, um Geld abzuheben“), vollständig fiktiv: kein Ort, keine echten Personen, keine Bank-Logos, der reale Fall wird
nicht erwähnt. Ein älterer Mann bricht im Vorraum einer Bankfiliale vor den Geldautomaten zusammen und bleibt bewusstlos
liegen (ruhige Peeps-Figur, keine Verletzung, kein Blut). In 20 Minuten steigen 4 Kunden über ihn hinweg: Herr Brauer
(„Ich hab gleich einen Termin.“), Frau Hauser („Da kommen doch gleich andere.“), Herr Kessel („Der schläft doch nur.“),
Frau Weigel (kann keine Erste Hilfe, geht). Dann wählt Frau Bühler 112 und bringt ihn in die stabile Seitenlage
(positives Vorbild); der Rettungsdienst bringt ihn ins Krankenhaus, er erholt sich.
Aufbau: Fall → Frage → Sachverhalt → Wortlautkarte § 323c Abs. 1 (vollständig, vorgelesen) → echtes Unterlassungsdelikt
→ 1. Unglücksfall (plötzliches Ereignis, erhebliche Gefahr; objektivierte ex-ante-Sicht) → 2. Nichthilfeleisten
→ 3. Erforderlichkeit (andere könnten helfen: egal; entfällt bei ausreichender Hilfe oder sicherem Tod) → 4. Zumutbarkeit
(Wortlaut; im Tatbestand) → 5. Vorsatz (Irrtum § 16) → Strafrahmen → Abgrenzung § 13 (ein Satz, Verweis 071/115) → Abs. 2
(Wortlautkarte, ein Satz) → Lösung je Kunde → Klausurtipp (Lexi) → Prüfschema → Merksatz mit 112.
Belege (BGH 1 StR 373/19 Rn. 11 f.; 4 StR 71/11 Rn. 21; 2 StR 115/15 Rn. 10, 12; 2 StR 109/20 Rn. 18; 5 StR 363/15
Rn. 5 f.; 5 StR 132/18 Rn. 46; 2 StR 563/18 Rn. 14, 17; 1 StR 21/93 Rn. 4 f.; 4 StR 71/11 Rn. 20): ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Herr Brauer, Frau Hauser, Herr Kessel,
Frau Weigel, Frau Bühler (nie im Genitiv). Der ältere Mann bleibt ohne Namen (Funktionsrolle) und spricht nicht.
Stimmen (nur aus dem Pool): Herr Brauer marc (Mann, mittel), Frau Hauser sabrina (Frau, mittel), Herr Kessel william
(Mann, älter), Frau Bühler laura_ruhig (Frau, mittel); Frau Weigel spricht nicht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter.
Nachvertonung v2 (nur Segment 15): „plötzlich eintretendes Ereignis“ hörten whisper small und medium als „einträgendes“;
umformuliert zu „ein Ereignis, das plötzlich eintritt, …“ (Paraphrase der BGH-Definition)."""

P, PS = 0.3, 0.5

STIMMEN = {"Brauer": "marc", "Hauser": "sabrina", "Kessel": "william", "Buehler": "laura_ruhig"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: der Vorraum der Bank ---------------------------------------------------------------------------------------
    ("[fall]Ein Montagmorgen im Vorraum einer Bankfiliale. [mann]Ein älterer Mann bricht vor den Geldautomaten zusammen. "
     "[liegt]Er bleibt bewusstlos am Boden liegen. [vier]In den nächsten zwanzig Minuten kommen vier Kunden. "
     "[brauer]Herr Brauer steigt über den Mann hinweg und hebt Geld ab.", P),
    ("[br1]Ich hab gleich einen Termin.", P, "Brauer"),
    ("[hauser]Frau Hauser sieht den Mann, zögert kurz und geht auch zum Automaten.", P),
    ("[ha1]Da kommen doch gleich andere.", P, "Hauser"),
    # --- A2 Fall: Herr Kessel, Frau Weigel -----------------------------------------------------------------------------------
    ("[kessel]Herr Kessel wirft einen kurzen Blick auf ihn.", P),
    ("[ke1]Der schläft doch nur.", P, "Kessel"),
    ("[weigel]Frau Weigel bleibt kurz stehen. Sie hat nie Erste Hilfe gelernt und geht wieder.", P),
    # --- A3 Fall: Frau Bühler hilft ------------------------------------------------------------------------------------------
    ("[buehler]Erst die fünfte Kundin, Frau Bühler, kniet sich zu ihm, spricht ihn an und wählt den Notruf.", P),
    ("[bu1]Hier liegt ein Mann bewusstlos am Boden. Er atmet.", P, "Buehler"),
    ("[seite]Sie bringt ihn in die stabile Seitenlage und bleibt bei ihm. [rtw]Der Rettungsdienst bringt ihn ins "
     "Krankenhaus, dort erholt er sich.", 0.4),
    ("[frage]Haben sich die vier Kunden strafbar gemacht? [frage2]Muss man wirklich jedem helfen?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 323c Abs. 1 --------------------------------------------------------------------------------------------
    ("[p323]Die Norm ist Paragraf dreihundertdreiundzwanzig c Absatz eins: Wer bei Unglücksfällen oder gemeiner Gefahr oder "
     "Not nicht Hilfe leistet, obwohl dies erforderlich und ihm den Umständen nach zuzumuten, insbesondere ohne erhebliche "
     "eigene Gefahr und ohne Verletzung anderer wichtiger Pflichten möglich ist, [strafe]wird mit Freiheitsstrafe bis zu "
     "einem Jahr oder mit Geldstrafe bestraft.", PS),
    ("[echt]Das ist ein echtes Unterlassungsdelikt: Bestraft wird das Nichthelfen selbst. [jeder]Die Pflicht trifft jeden, "
     "auch ohne Garantenstellung. [kein]Und es kommt nicht darauf an, ob die Hilfe am Ende etwas geändert hätte.", PS),
    # --- D 1. Unglücksfall ---------------------------------------------------------------------------------------------------
    ("[ungl]Erstens der Unglücksfall. [def]Nach dem Bundesgerichtshof ist das ein Ereignis, das plötzlich eintritt, "
     "erheblichen Schaden an Menschen oder Sachen anrichtet und weiteren Schaden zu verursachen droht. [droht]Schon ein "
     "drohender erheblicher Schaden genügt. "
     "[exante]Du beurteilst das ex ante: so, wie ein verständiger Beobachter die Lage im Moment der Hilfe sieht. "
     "[ungl2]Ein Mann bricht zusammen und reagiert nicht mehr. Das ist ein Unglücksfall.", PS),
    # --- E 2. Nichthilfeleisten, 3. Erforderlichkeit -------------------------------------------------------------------------
    ("[nicht]Zweitens: Die Kunden leisten keine Hilfe. [was]Geschuldet ist die Hilfe, die dir möglich ist, oft schon der "
     "Notruf. [erf]Drittens die Erforderlichkeit. [andere]Dass andere helfen könnten, ändert nichts, solange keine sofortige "
     "Hilfe von anderer Seite gesichert ist. [entf]Nicht mehr erforderlich ist sie erst, wenn schon ausreichend geholfen "
     "wird [tot]oder wenn der Verunglückte sicher tot ist. [erf2]Hier hilft zwanzig Minuten lang niemand.", PS),
    # --- F 4. Zumutbarkeit ---------------------------------------------------------------------------------------------------
    ("[zum]Viertens die Zumutbarkeit. [zumw]Das Gesetz nennt zwei Beispiele: Die Hilfe muss ohne erhebliche eigene Gefahr "
     "möglich sein [pfl]und ohne Verletzung anderer wichtiger Pflichten. [termin]Ein Termin bei der Arbeit ist keine solche "
     "Pflicht. [anruf]Und ein Notruf geht auch ohne Kenntnisse in Erster Hilfe, ganz ohne eigene Gefahr. "
     "[tb]Die Zumutbarkeit prüfst du hier im Tatbestand, sie steht ja im Wortlaut.", PS),
    # --- G 5. Vorsatz, Strafrahmen -------------------------------------------------------------------------------------------
    ("[vors]Fünftens der Vorsatz. Der Täter muss den Unglücksfall erkennen und die Umstände, die Hilfe erforderlich und "
     "zumutbar machen. [bed]Bedingter Vorsatz genügt. [irrt]Wer wirklich glaubt, der Mann schlafe nur, irrt über den "
     "Unglücksfall. Dann fehlt der Vorsatz, Paragraf sechzehn. [fahrl]Fahrlässig ist die unterlassene Hilfeleistung nicht "
     "strafbar.", PS),
    # --- H Abgrenzung § 13, Abs. 2 -------------------------------------------------------------------------------------------
    ("[p13]Ist jemand Garant, etwa als Vater, prüfst du zusätzlich das unechte Unterlassen nach Paragraf dreizehn, mehr dazu "
     "in den Videos zum Unterlassungsdelikt und zur Garantenstellung. [abs2]Und nach Absatz zwei wird ebenso bestraft, wer "
     "in diesen Situationen eine Person behindert, die einem Dritten Hilfe leistet oder leisten will.", PS),
    # --- I Lösung je Kunde ---------------------------------------------------------------------------------------------------
    ("[loes]Zur Lösung. [l1]Herr Brauer: Sein Termin macht die Hilfe nicht unzumutbar. Strafbar. [l2]Frau Hauser: Dass andere "
     "kommen könnten, beseitigt die Erforderlichkeit nicht. Strafbar. [l3]Herr Kessel: Glaubt er wirklich an einen "
     "Schlafenden, fehlt der Vorsatz. [l3b]Hält er einen Notfall aber für möglich und nimmt das in Kauf, ist er strafbar. "
     "[l4]Frau Weigel: Den Notruf hätte sie wählen können. Strafbar. [l5]Und Frau Bühler hat genau das Richtige getan.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Fehlt eine Garantenstellung, vergiss Paragraf dreihundertdreiundzwanzig c nicht. Wegen "
     "übersehener unterlassener Hilfeleistung hat der Bundesgerichtshof schon Freisprüche aufgehoben. [tipp2]Und prüfe die Zumutbarkeit im Tatbestand, nicht "
     "erst in der Schuld.", PS),
    # --- K Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Römisch eins, Tatbestand: [s1a]Unglücksfall, gemeine Gefahr oder Not, [s1b]Nichthilfeleisten, "
     "[s1c]Erforderlichkeit, [s1d]Zumutbarkeit, [s1e]Vorsatz. [s2]Römisch zwei, Rechtswidrigkeit. [s3]Römisch drei, Schuld.",
     PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei einem Unglücksfall muss jeder helfen, soweit es erforderlich und zumutbar ist. [m2]Und den Notruf "
     "eins, eins, zwei zu wählen, ist fast immer möglich und zumutbar.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
