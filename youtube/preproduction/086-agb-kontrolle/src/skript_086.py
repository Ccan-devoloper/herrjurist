"""Folge 086 · AGB-Kontrolle Schema §§ 305 ff. BGB: So prüfst du in 7 Schritten (Mi · Examenswissen · Zivilrecht/
Schuldrecht AT, Format Schema). Beispielfall nach dem Plan-Hook („Im Kleingedruckten des Fitnessstudios steht eine
Mindestlaufzeit von drei Jahren“): Mira (Verbraucherin) bucht im Januar online im Fitnessstudio von Rolf (Unternehmer) ein
Kurs-Abo (jede Woche 2 Kurse mit Trainer, 30 € im Monat); Hinweis auf die AGB mit Link, Haken gesetzt. In den AGB unter
„Laufzeit“: Mindestlaufzeit 36 Monate. Anfang Juli will Mira zum Monatsende kündigen, Rolf verweist auf die drei Jahre.
Schema in 7 Schritten: (1) Anwendungsbereich § 310, (2) AGB-Begriff § 305 I (Wortlautkarte § 305 I 1), (3) Einbeziehung
§ 305 II, III, Vorrang der Individualabrede § 305b (ein Satz), (4) keine überraschende Klausel § 305c I, (5) Auslegung,
Unklarheitenregel § 305c II, (6) Inhaltskontrolle § 307 III, Reihenfolge § 309 → § 308 → § 307, § 309 Nr. 9 a)
(Wortlautkarte; reiner Gerätevertrag = Miete, BGH XII ZR 42/10), Nr. 9 b), c) seit 1.3.2022, § 312k (ein Satz),
(7) Rechtsfolge § 306 (Wortlautkarte Abs. 1, 2; Verbot der geltungserhaltenden Reduktion, BGH VIII ZR 262/09 Rn. 24).
Klausurtipp und Merksatz mit Lexi. Figuren: Mira (lucy), Rolf (stephan); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter; „A.G.B.“ mit Punkten wie
die Gesetzesabkürzungen in synth_el.sprechtext()."""

P, PS = 0.3, 0.5

STIMMEN = {"Mira": "lucy", "Rolf": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Anmeldung online ------------------------------------------------------------------------------
    ("[fall]Mira will fit werden. Im Januar bucht sie online ein Kurs-Abo im Fitnessstudio von Rolf: [abo]jede Woche "
     "zwei Kurse mit Trainer, dreißig Euro im Monat. [hinw]Vor dem Klick steht der Hinweis auf die A.G.B., mit Link. "
     "[haken]Mira setzt den Haken und bucht.", 0.3),
    # --- A2 Fall: die Kündigung im Studio -------------------------------------------------------------------------------
    ("[juli]Anfang Juli hat Mira keine Zeit mehr für die Kurse. Sie geht zu Rolf ins Studio.", 0.25),
    ("[mi1]Ich möchte kündigen, zum Ende des Monats.", 0.25, "Mira"),
    ("[ro1]Das geht nicht. Lies das Kleingedruckte: Mindestlaufzeit drei Jahre.", 0.3, "Rolf"),
    ("[klein]Tatsächlich steht in den A.G.B. unter der Überschrift Laufzeit: [mind]Die Mindestlaufzeit beträgt "
     "sechsunddreißig Monate.", 0.3),
    ("[frage]Ist Mira wirklich drei Jahre gebunden? [frage2]Prüfen wir die Klausel in sieben Schritten.", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C sieben Schritte -----------------------------------------------------------------------------------------------
    ("[sieben]Die A.G.B.-Kontrolle hat sieben Schritte: [s1]Anwendungsbereich, [s2]A.G.B.-Begriff, [s3]Einbeziehung, "
     "[s4]keine überraschende Klausel, [s5]Auslegung, [s6]Inhaltskontrolle [s7]und Rechtsfolge.", PS),
    # --- D 1. Anwendungsbereich, § 310 ----------------------------------------------------------------------------------
    ("[anw]Erstens: der Anwendungsbereich, Paragraf dreihundertzehn. [anw4]Im Erb-, Familien- und Gesellschaftsrecht "
     "gelten die Regeln nicht. [anw1]Gegenüber Unternehmern gelten sie nur eingeschränkt, etwa ohne Paragraf "
     "dreihundertneun. [anw3]Mira ist Verbraucherin, Rolf ist Unternehmer. Bei diesem Verbrauchervertrag gilt alles.", P),
    # --- E 2. AGB-Begriff, § 305 Abs. 1 Satz 1 (Wortlaut) ----------------------------------------------------------------
    ("[begr]Zweitens: Liegen A.G.B. vor? [w305]Paragraf dreihundertfünf Absatz eins Satz eins: Allgemeine "
     "Geschäftsbedingungen sind alle für eine Vielzahl von Verträgen vorformulierten Vertragsbedingungen, die eine "
     "Vertragspartei, der Verwender, der anderen Vertragspartei bei Abschluss eines Vertrags stellt. [viel]Eine Vielzahl "
     "liegt schon vor, wenn der Verwender die Bedingungen dreimal verwenden will. [begr2]Rolf nutzt dieselben Bedingungen "
     "für alle Mitglieder, und ausgehandelt wurde nichts.", P),
    # --- F 3. Einbeziehung, § 305 Abs. 2, 3; § 305b ----------------------------------------------------------------------
    ("[einb]Drittens: die Einbeziehung nach Paragraf dreihundertfünf Absatz zwei. [e1]Der Verwender muss bei "
     "Vertragsschluss ausdrücklich auf die A.G.B. hinweisen, [e2]der anderen Seite zumutbar ermöglichen, sie zu lesen, "
     "[e3]und sie muss einverstanden sein. [esub]Online heißt das: Hinweis vor dem Klick, Link zum Lesen, Haken gesetzt. "
     "[abs3]Für künftige Geschäfte erlaubt Absatz drei eine Vereinbarung im Voraus. "
     "[indiv]Und hätten Mira und Rolf individuell etwas anderes vereinbart, ginge diese Individualabrede nach Paragraf "
     "dreihundertfünf b den A.G.B. vor.", P),
    # --- G 4. keine überraschende Klausel, § 305c Abs. 1 ----------------------------------------------------------------
    ("[ueber]Viertens: keine überraschende Klausel, Paragraf dreihundertfünf c Absatz eins. Was so ungewöhnlich ist, dass "
     "der Kunde nicht damit rechnen muss, wird nicht Vertragsbestandteil. [usub]Laufzeiten sind bei solchen Verträgen aber üblich, "
     "und die Klausel steht offen unter der Überschrift Laufzeit. [ulang]Ob drei Jahre zu lang sind, ist eine Frage der "
     "Inhaltskontrolle.", P),
    # --- H 5. Auslegung, § 305c Abs. 2 -------------------------------------------------------------------------------------
    ("[ausl]Fünftens: die Auslegung. A.G.B. werden einheitlich so ausgelegt, wie verständige und redliche "
     "Vertragspartner sie verstehen. [unkl]Bleiben Zweifel, gehen sie nach Paragraf dreihundertfünf c Absatz zwei zu "
     "Lasten des Verwenders. [asub]Hier gibt es keine Zweifel: sechsunddreißig Monate sind eindeutig.", P),
    # --- I 6. Inhaltskontrolle: Kontrollfähigkeit und Reihenfolge ---------------------------------------------------------
    ("[ink]Sechstens: die Inhaltskontrolle. [kf]Kontrolliert werden nach Paragraf dreihundertsieben Absatz drei Klauseln, "
     "die vom Gesetz abweichen oder es ergänzen. Eine feste Mindestlaufzeit tut das. [reihe]Geprüft wird vom Speziellen "
     "zum Allgemeinen: [r309]zuerst Paragraf dreihundertneun, die Verbote ohne Wertungsmöglichkeit, [r308]dann Paragraf "
     "dreihundertacht mit Wertungsmöglichkeit, [r307]zuletzt die Generalklausel des Paragrafen dreihundertsieben.", P),
    # --- J § 309 Nr. 9 a) (Wortlaut) ----------------------------------------------------------------------------------------
    ("[w309]Paragraf dreihundertneun Nummer neun erklärt für unwirksam: bei einem Vertragsverhältnis, das die regelmäßige "
     "Lieferung von Waren oder die regelmäßige Erbringung von Dienst- oder Werkleistungen durch den Verwender zum "
     "Gegenstand hat, Buchstabe a: eine den anderen Vertragsteil länger als zwei Jahre bindende Laufzeit des Vertrags. "
     "[miete]Achtung: Überlässt ein Studio nur Geräte und Räume, sieht der Bundesgerichtshof darin einen Mietvertrag, und "
     "Nummer neun passt nicht. Dann bleibt Paragraf dreihundertsieben. [kurse]Rolf schuldet aber jede Woche Kurse mit "
     "Trainer, also regelmäßige Dienstleistungen. [drei]Drei Jahre sind länger als zwei. Die Klausel ist unwirksam.", PS),
    ("[bc]Seit März zweitausendzweiundzwanzig gilt außerdem: Verlängert sich ein solcher Vertrag stillschweigend, dann nur "
     "auf unbestimmte Zeit und mit höchstens einem Monat Kündigungsfrist. [button]Und weil Mira online gebucht hat, muss Rolf nach "
     "Paragraf dreihundertzwölf k auch einen Kündigungsbutton anbieten.", PS),
    # --- K 7. Rechtsfolge, § 306 Abs. 1, 2 (Wortlaut) ------------------------------------------------------------------------
    ("[rf]Siebtens: die Rechtsfolge, Paragraf dreihundertsechs. [w306]Sind Allgemeine Geschäftsbedingungen ganz oder "
     "teilweise nicht Vertragsbestandteil geworden oder unwirksam, so bleibt der Vertrag im Übrigen wirksam. "
     "[w306b]Soweit die Bestimmungen nicht Vertragsbestandteil geworden oder unwirksam sind, richtet sich der Inhalt des "
     "Vertrags nach den gesetzlichen Vorschriften. [red]Die Klausel wird also nicht auf zwei Jahre gekürzt, sie fällt ganz "
     "weg. Das ist das Verbot der geltungserhaltenden Reduktion, so auch der Bundesgerichtshof. [abs3h]Nur bei "
     "unzumutbarer Härte ist nach Absatz drei der ganze Vertrag unwirksam.", PS),
    # --- L Ergebnis -------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Das Kurs-Abo bleibt wirksam, aber ohne Mindestlaufzeit. [erg2]Es läuft auf unbestimmte Zeit, und "
     "Mira kann nach dem Gesetz kündigen: Beim Monatsbeitrag spätestens am Fünfzehnten zum Monatsende. [erg3]Kündigt sie "
     "Anfang Juli, endet das Abo Ende Juli.", PS),
    # --- M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte in der Inhaltskontrolle die Reihenfolge ein, erst Paragraf dreihundertneun, dann "
     "dreihundertacht, dann dreihundertsieben. [tipp2]Und prüfe vorher die Kontrollfähigkeit: Den Preis der Hauptleistung "
     "selbst misst du nur am Transparenzgebot.", PS),
    # --- N Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für die A.G.B.-Kontrolle: [k1]Römisch eins: Anwendungsbereich. "
     "[k2]Römisch zwei: A.G.B.-Begriff. [k3]Römisch drei: Einbeziehung nach "
     "Absatz zwei und drei, Vorrang der Individualabrede. [k4]Römisch vier: keine überraschende Klausel. [k5]Römisch "
     "fünf: Auslegung, Zweifel zu Lasten des Verwenders. [k6]Römisch sechs: Inhaltskontrolle, dreihundertneun vor "
     "dreihundertacht vor dreihundertsieben. [k7]Römisch sieben: Rechtsfolge.", PS),
    # --- O Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine unwirksame Klausel fällt ganz weg. [m2]Der Vertrag bleibt, und in die Lücke tritt das Gesetz.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
