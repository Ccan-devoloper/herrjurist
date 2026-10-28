"""Folge 259 · Taschengeldparagraph: Darf ein 16-Jähriger auf Raten kaufen? (Mo · Der Fall · BGB AT · Alltagsfall;
§§ 107, 108, 110 BGB; zusätzlich §§ 106, 184, 362 Abs. 1, 433 Abs. 2, 812 BGB).
Fall nach dem Plan-Hook („Anzahlung vom Taschengeld, der Rest in sechs Monatsraten – ohne die Eltern zu fragen“) und der
Gesamtwissen-Fundstelle (2.8 Taschengeldparagraph; Fall „Der Minderjährige mit dem E-Bike“, UNCERTIFIED): Fridolin (16)
kauft im (fiktiven) Radladen von Herrn Heinemann ein gebrauchtes E-Bike für 900 €, zahlt 300 € aus gespartem Taschengeld
an (zur freien Verfügung), den Rest von 600 € in sechs Monatsraten zu je 100 € aus künftigem Taschengeld; die Eltern fragt
er nicht. Herr Heinemann gibt ihm das E-Bike gleich mit. Am nächsten Tag lehnt die Mutter, auch für den Vater, gegenüber
Herrn Heinemann die Genehmigung ab. Voraussetzung (Folge 021, nur verwiesen): Grundschema §§ 104 ff.
Belege je Cue in ../RECHTSSTAND.md: Normwortlaut gesetze-im-internet.de (Abruf 08.10.2026). Leitentscheidung: keine
verifizierte Primärrechtsprechung abrufbar → „Ratenkauf erst mit der letzten Rate“ und „keine Kreditgeschäfte“ im Video
ausdrücklich als herrschende Lehre gekennzeichnet (Wortlaut „bewirkt“, § 362 Abs. 1).
Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Heinemann (william, Mann, älter), Mutter (laura_ruhig, Frau,
mittel). Fridolin spricht nicht (keine junge Männerstimme im Pool). sabrina und marc nicht besetzt (beide in 256).
Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH).
Kein Genitiv eines Namens (Namensprüfung)."""

P, PS = 0.3, 0.5

STIMMEN = {"Heinemann": "william", "Mutter": "laura_ruhig"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: im Radladen ---------------------------------------------------------------------------------------
    ("[fall]Stell dir vor, du bist sechzehn und willst unbedingt ein E-Bike. [fridolin]So geht es Fridolin. "
     "[laden]Im Radladen von Herrn Heinemann steht ein gebrauchtes E-Bike für neunhundert Euro. [angebot]Herr Heinemann "
     "macht ihm einen Vorschlag.", P),
    ("[h1]Dreihundert Euro jetzt, den Rest in sechs Monatsraten zu je hundert Euro.", P, "Heinemann"),
    # --- A2 Anzahlung, Raten, Eltern nicht gefragt ------------------------------------------------------------------
    ("[anz]Fridolin zahlt die dreihundert Euro aus seinem gesparten Taschengeld an. [raten]Die übrigen sechshundert Euro "
     "will er in sechs Raten aus seinem künftigen Taschengeld zahlen. [frei]Das Taschengeld geben ihm die Eltern zur "
     "freien Verfügung. [nicht]Gefragt hat er sie aber nicht. [mit]Herr Heinemann gibt ihm das E-Bike gleich mit.", P),
    # --- A3 Abends zu Hause, am nächsten Tag der Anruf ---------------------------------------------------------------
    ("[abend]Am Abend steht das E-Bike im Flur.", P),
    ("[m1]Ein E-Bike auf Raten? Das hättest du mit uns besprechen müssen.", P, "Mutter"),
    ("[anruf]Am nächsten Tag ruft die Mutter, auch für den Vater, bei Herrn Heinemann an.", P),
    ("[m2]Diesen Ratenkauf genehmigen wir nicht.", P, "Mutter"),
    ("[frage]Muss Fridolin die restlichen sechshundert Euro zahlen? [frage2]Oder rettet ihn der Taschengeldparagraf?", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruch, Einigung, beschränkte Geschäftsfähigkeit -------------------------------------------------------
    ("[ansp]Herr Heinemann könnte die sechshundert Euro nach Paragraf vierhundertdreiunddreißig Absatz zwei verlangen. "
     "[einig]Einig sind sich die beiden. [wirk]Fraglich ist, ob der Vertrag wirksam ist. Fridolin ist sechzehn, also "
     "nach Paragraf hundertsechs beschränkt geschäftsfähig. [v021]Das Grundschema zeigt unsere Folge zu Minderjährigen im "
     "Vertragsrecht. Hier geht es um den Ratenkauf.", P),
    # --- D § 107 (Wortlautkarte) ------------------------------------------------------------------------------------
    ("[p107]Paragraf hundertsieben sagt: Der Minderjährige bedarf zu einer Willenserklärung, durch die er nicht lediglich "
     "einen rechtlichen Vorteil erlangt, der Einwilligung seines gesetzlichen Vertreters. [pflicht]Der Ratenkauf verpflichtet "
     "Fridolin, neunhundert Euro zu zahlen. Das ist ein rechtlicher Nachteil. [keine]Eingewilligt haben die Eltern nicht.", P),
    # --- E § 108 Abs. 1 (Wortlautkarte) -----------------------------------------------------------------------------
    ("[p108]Dann gilt Paragraf hundertacht Absatz eins: Schließt der Minderjährige einen Vertrag ohne die erforderliche "
     "Einwilligung des gesetzlichen Vertreters, so hängt die Wirksamkeit des Vertrags von der Genehmigung des Vertreters "
     "ab. [schwebe]Bis dahin ist der Vertrag schwebend unwirksam.", PS),
    # --- F § 110 (Wortlautkarte) ------------------------------------------------------------------------------------
    ("[p110]Vielleicht braucht es aber gar keine Genehmigung. [p110w]Nach Paragraf hundertzehn gilt der Vertrag als von "
     "Anfang an wirksam, wenn der Minderjährige die vertragsmäßige Leistung mit Mitteln bewirkt, die ihm zu diesem Zweck "
     "oder zu freier Verfügung überlassen worden sind. [mittel]Das Taschengeld hat Fridolin zur freien Verfügung. Das "
     "passt.", P),
    # --- G „bewirkt“ = vollständig erfüllt --------------------------------------------------------------------------
    ("[bewirkt]Entscheidend ist das Wort bewirkt. [erfuell]Bewirkt ist eine Leistung erst, wenn sie vollständig erbracht "
     "ist, so wie bei der Erfüllung nach Paragraf dreihundertzweiundsechzig. [anz2]Fridolin hat bisher nur dreihundert "
     "von neunhundert Euro gezahlt. [teil]Und die Anzahlung macht den Kauf auch nicht teilweise wirksam.", P),
    # --- H Ratenkauf und Kreditgeschäfte (herrschende Lehre) --------------------------------------------------------
    ("[rate]Für den Ratenkauf heißt das nach herrschender Lehre: [letzte]Der Vertrag wird erst wirksam, wenn die letzte "
     "Rate aus dem Taschengeld bezahlt ist. [kredit]Eine Pflicht, später zu zahlen, deckt der Taschengeldparagraf also "
     "nicht. Kreditgeschäfte bleiben ohne die Eltern in der Schwebe.", PS),
    # --- I Eltern: Genehmigung, Verweigerung, Aufforderung ----------------------------------------------------------
    ("[eltern]Es kommt also auf die Eltern an. [gen]Genehmigen sie, ist der Vertrag von Anfang an wirksam. [verw]Verweigern "
     "sie die Genehmigung, ist er endgültig unwirksam. [auff]Hätte Herr Heinemann die Eltern zur Erklärung aufgefordert, "
     "könnten sie nur noch ihm gegenüber erklären und nur binnen zwei Wochen nach Empfang genehmigen. Schweigen sie, gilt "
     "die Genehmigung als verweigert.", P),
    # --- K Ergebnis und Rückabwicklung ------------------------------------------------------------------------------
    ("[erg]Hier hat die Mutter für beide Eltern abgelehnt, gegenüber Herrn Heinemann. [erg2]Der Vertrag ist endgültig "
     "unwirksam. Fridolin muss die sechshundert Euro nicht zahlen. [rueck]Das E-Bike und die Anzahlung werden grundsätzlich "
     "nach Paragraf achthundertzwölf zurückabgewickelt. Mehr dazu in unserer Folge zur Leistungskondiktion.", PS),
    # --- L Klausurtipp (Lexi) ---------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bejahe den Taschengeldparagrafen nicht schon wegen der Anzahlung. [tipp2]Frage genau: Ist die "
     "ganze vertragsmäßige Leistung bewirkt, und zwar mit überlassenen Mitteln? [tipp3]Solange eine Rate offen ist, lautet "
     "die Antwort nein. Dann prüfst du die Genehmigung nach Paragraf hundertacht.", PS),
    # --- M Prüfungsschema -------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Herr Heinemann gegen Fridolin auf die restlichen sechshundert Euro. [s1]Römisch eins: "
     "Einigung. [s2]Römisch zwei: Wirksamkeit. [s2a]Erstens: beschränkt geschäftsfähig, Paragraf hundertsechs. "
     "[s2b]Zweitens: nicht lediglich rechtlich vorteilhaft, keine Einwilligung, Paragraf hundertsieben. [s2c]Drittens: "
     "Taschengeldparagraf, Leistung vollständig bewirkt? Hier nein. [s2d]Viertens: Genehmigung nach Paragraf hundertacht, "
     "hier verweigert. [s3]Römisch drei: Ergebnis, kein Anspruch.", PS),
    # --- N Merksatz (Lexi) ------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Taschengeldparagraf hilft erst, wenn alles aus dem Taschengeld bezahlt ist. [merk2]Beim Ratenkauf also erst mit der "
     "letzten Rate. Bis dahin entscheiden die Eltern.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    assert not re.search(r"Fridolins|Heinemanns", text), "Genitiv eines Namens"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
