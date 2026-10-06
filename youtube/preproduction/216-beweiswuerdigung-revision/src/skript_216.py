"""Folge 216 · Beweiswürdigung Revision: Lücken, Widersprüche, in dubio pro reo (Fr · 2. Examen · StPO-Praxis, Sonderlage).
Beispielfall nach dem Plan-Hook („In einem Aussage-gegen-Aussage-Fall übergeht das Urteil, dass die Belastungszeugin ihre
Schilderung dreimal geändert hat“): Das Amtsgericht verurteilt Herrn Kerber wegen Körperverletzung (§ 223 StGB) zu 60
Tagessätzen. Er soll seine Kollegin Frau Bremer in der Spätschicht eines Paketlagers gegen ein Regal gestoßen haben; Zeugen
gibt es keine, Herr Kerber bestreitet. Laut den Urteilsgründen schilderte Frau Bremer den Vorfall dreimal verschieden
(Schichtleiterin: Stoß gegen das Regal; Polizei: Faustschlag auf den Arm; Hauptverhandlung: am Arm gepackt und zur Seite
gerissen). Das Urteil nennt die Aussage „konstant“, erörtert die Abweichungen nicht und schreibt, das Gericht habe keine
Zweifel. Rechtsanwalt Wegmann hat Sprungrevision (§ 335 StPO) eingelegt und die allgemeine Sachrüge erhoben.
Prüfung: § 261 StPO (Wortlautkarte; Sache des Tatgerichts, nur Rechtsfehler: BGH 6 StR 543/24 Rn. 16) → Sachrüge (Verweis
Folge 204) → Aussage gegen Aussage (BGH 2 StR 194/17 Rn. 10; 6 StR 260/25 Rn. 5; 6 StR 105/25 Rn. 6) → Fall: Lücke und
Widerspruch (6 StR 105/25 Rn. 9, 12), Beruhen (2 StR 205/24 Rn. 21), §§ 353, 354 Abs. 2 → in dubio pro reo als
Entscheidungsregel (BGH 2 StR 128/25 Rn. 31), Art. 6 Abs. 2 EMRK (Wortlautkarte) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben, in namen_reserviert.txt eingetragen: Kerber,
Bremer, Wegmann (die Richterin bleibt namenlos). Stimmen nur aus dem Pool: Herr Kerber marc, Frau Bremer sabrina,
Rechtsanwalt Wegmann william, Richterin laura_ruhig; Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Kerber": "marc", "Bremer": "sabrina", "Wegmann": "william", "Richterin": "laura_ruhig"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: in der Kanzlei --------------------------------------------------------------------------------------------
    ("[fall]Eine Anwaltskanzlei. Rechtsanwalt Wegmann hat das Urteil des Amtsgerichts vor sich. [urteil]Sein Mandant, Herr "
     "Kerber, ist wegen Körperverletzung zu sechzig Tagessätzen verurteilt worden. [lager]Er soll seine Kollegin, Frau Bremer, "
     "in der Spätschicht eines Paketlagers gegen ein Regal gestoßen haben. [aga]Zeugen gab es keine. Aussage steht gegen Aussage.", P),
    ("[k1]Ich habe sie nicht angefasst.", P, "Kerber"),
    # --- A2 Fall: die drei Schilderungen (Rückblick) ------------------------------------------------------------------------
    ("[drei]Laut den Urteilsgründen hat Frau Bremer den Vorfall dreimal geschildert. [v1]Noch am selben Abend der Schichtleiterin:", P),
    ("[b1]Er hat mich gegen das Regal gestoßen.", P, "Bremer"),
    ("[v2]Zwei Wochen später bei der Polizei:", P),
    ("[b2]Er hat mir mit der Faust auf den Arm geschlagen.", P, "Bremer"),
    ("[v3]Und in der Hauptverhandlung:", P),
    ("[b3]Er hat mich am Arm gepackt und zur Seite gerissen.", P, "Bremer"),
    ("[attest]Ein Attest belegt einen Bluterguss am Oberarm.", P),
    # --- A3 Fall: Rückblick, die Urteilsverkündung --------------------------------------------------------------------------
    ("[saal]Die Richterin folgt der Zeugin.", P),
    ("[r1]Die Zeugin hat den Vorfall konstant und glaubhaft geschildert. Zweifel hat das Gericht nicht.", P, "Richterin"),
    # --- A4 Fall: zurück in der Kanzlei -------------------------------------------------------------------------------------
    ("[w1]Dreimal anders geschildert, und das soll konstant sein? Dazu steht im Urteil kein Wort.", P, "Wegmann"),
    ("[k2]Dann gilt doch: Im Zweifel für den Angeklagten!", P, "Kerber"),
    ("[frage]Kann Rechtsanwalt Wegmann diese Beweiswürdigung mit der Revision angreifen? [frage2]Und hilft Herrn Kerber der "
     "Satz in dubio pro reo?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 261 StPO: freie Überzeugung, nur Rechtsfehler ------------------------------------------------------------------
    ("[p261]Paragraf zweihunderteinundsechzig: Über das Ergebnis der Beweisaufnahme entscheidet das Gericht nach seiner "
     "freien, aus dem Inbegriff der Verhandlung geschöpften Überzeugung. [sache]Die Beweiswürdigung ist also Sache des "
     "Tatgerichts. [nurrf]Das Revisionsgericht prüft nur, ob ihm Rechtsfehler unterlaufen sind: [l1]ob die Würdigung "
     "lückenhaft, [l2]widersprüchlich [l3]oder unklar ist, [l4]gegen Denkgesetze oder Erfahrungssätze verstößt [l5]oder "
     "überspannte Anforderungen an die zur Verurteilung nötige Gewissheit stellt.", P),
    ("[sachr]Solche Fehler deckt schon die allgemeine Sachrüge auf, denn sie ergeben sich aus dem Urteil selbst. Wie die Sachrüge "
     "funktioniert, zeigt eine eigene Folge.", PS),
    # --- D Aussage gegen Aussage ---------------------------------------------------------------------------------------------
    ("[aga2]Steht Aussage gegen Aussage, darf das Gericht auch auf eine einzige Belastungszeugin hin verurteilen, wenn es "
     "von ihrer Aussage überzeugt ist. [sorgf]Es muss sie aber besonders sorgfältig würdigen. [gesamt]Die Urteilsgründe "
     "müssen erkennen lassen, dass es alle Umstände für und gegen den Angeklagten erkannt und in einer Gesamtschau gewürdigt "
     "hat. [krit]Dazu gehören die Entstehung der Aussage, [motiv]mögliche Motive, [konst]ihre Konstanz, [det]Detailreichtum "
     "und Plausibilität.", P),
    ("[frueh]Deshalb muss das Urteil auch frühere Angaben der Zeugin mitteilen. [abw]Nur so kann das Revisionsgericht "
     "prüfen, ob das Gericht Abweichungen gesehen und richtig gewichtet hat. [nicht]Abweichungen machen eine Aussage nicht "
     "automatisch unglaubhaft. [erkl]Das Gericht muss sie aber erkennen und erklären.", PS),
    # --- E Der Fall: Lücke und Widerspruch -----------------------------------------------------------------------------------
    ("[fall2]Zurück zu Herrn Kerber. [drei2]Das Urteil teilt alle drei Schilderungen mit: [s1]Stoß gegen das Regal, "
     "[s2]Faustschlag, [s3]am Arm gepackt. [konst2]Trotzdem nennt es die Aussage konstant [kwort]und erörtert die "
     "Abweichungen mit keinem Wort. [luecke]Das ist lückenhaft. [wid]Und es ist widersprüchlich: Das Urteil nennt konstant, "
     "was es selbst als dreimal verschieden beschreibt.", P),
    ("[beruh]Auf diesem Fehler beruht das Urteil. Es ist nicht auszuschließen, dass die Richterin bei rechtsfehlerfreier "
     "Würdigung anders entschieden hätte. [aufh]Das Revisionsgericht hebt das Urteil mit den Feststellungen auf [zur]und "
     "verweist die Sache an eine andere Abteilung des Amtsgerichts zurück. [frei]Selbst freisprechen kann es nicht, denn die "
     "Aussage neu zu würdigen, ist Sache des Tatgerichts.", PS),
    # --- F In dubio pro reo und Art. 6 Abs. 2 EMRK ---------------------------------------------------------------------------
    ("[idpr]Und in dubio pro reo? Darauf beruft sich Herr Kerber zu früh. [regel]Der Satz ist keine Beweisregel, sondern "
     "eine Entscheidungsregel. [erst]Er greift erst, wenn das Gericht nach abgeschlossener Beweiswürdigung nicht voll "
     "überzeugt ist. [verl]Verletzt ist er deshalb nur, wenn das Urteil erkennen lässt, dass das Gericht Zweifel hatte und "
     "trotzdem verurteilte. [hier]Hier schreibt die Richterin ausdrücklich, das Gericht habe keine Zweifel. [muss]Ob sie "
     "hätte zweifeln müssen, ist eine Frage der Beweiswürdigung, und dort liegt der Fehler.", P),
    ("[emrk]Eng verwandt ist die Unschuldsvermutung aus Artikel sechs Absatz zwei der Europäischen "
     "Menschenrechtskonvention: Jede Person, die einer Straftat angeklagt ist, gilt bis zum gesetzlichen Beweis ihrer "
     "Schuld als unschuldig.", PS),
    # --- G Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp für deine Revisionsbegründung. [t1]Erhebe die allgemeine Sachrüge und führe aus, dass die "
     "Beweiswürdigung lückenhaft und widersprüchlich ist. [t2]Formuliere eng am Urteil: Das Urteil teilt drei "
     "unterschiedliche Schilderungen der Zeugin mit, nennt ihre Aussage aber konstant, ohne die Abweichungen zu erörtern. "
     "[t3]Und rüge in dubio pro reo nur, wenn das Urteil selbst Zweifel erkennen lässt.", PS),
    # --- H Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [sc1]Römisch eins: der Maßstab, Paragraf zweihunderteinundsechzig, nur Rechtsfehler. "
     "[sc2]Römisch zwei: bei Aussage gegen Aussage die Gesamtschau, mit Entstehung, Konstanz und früheren Angaben. "
     "[sc3]Römisch drei: der Zweifelssatz, nur bei Zweifeln des Gerichts. [sc4]Römisch vier: das Beruhen, dann Aufhebung "
     "und Zurückverweisung.", PS),
    # --- I Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Das Revisionsgericht würdigt die Beweise nicht neu. [m2]Es prüft, ob das Urteil Widersprüche gesehen "
     "und erklärt hat. Und in dubio pro reo greift erst, wenn das Gericht selbst zweifelt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
