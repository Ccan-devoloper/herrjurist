"""Folge 122 · Widerrufsrecht Fernabsatz §§ 312g, 355 BGB: 14 Tage und Ausnahmen (Mi · Examenswissen · Zivilrecht/
Schuldrecht AT, Format Schema). Beispielfall nach dem Plan-Hook („Du bestellst Sneaker online, trägst sie einmal draußen
und schickst sie zurück.“): Ilka (privat, Verbraucherin) bestellt am 4.9.2026 im Onlineshop von Herrn Riemann
(Unternehmer) ein Paar Sneaker (Serienware, keine Marke) für 120 €, zahlt sofort; Versand und Rückversand kostenlos;
ordnungsgemäße Belehrung. Erhalt am 8.9.2026. Am 12.9. trägt sie die Sneaker einen Nachmittag draußen im Park (Sohlen
verschmutzt). Am 15.9. E-Mail „Ich widerrufe den Kauf …“ und Rücksendung. Herr Riemann: „Getragene Schuhe nehme ich
nicht zurück.“ Mit den Spuren sind die Sneaker nur noch 80 € wert.
Kern als Schema: I. Widerrufsrecht – 1. Verbrauchervertrag § 310 Abs. 3 (Verweis 106); 2. Fernabsatzvertrag § 312c
Abs. 1 (Wortlautkarte); 3. Widerrufsrecht § 312g Abs. 1 (Wortlautkarte), Ausnahmen § 312g Abs. 2 Nr. 1, 2, 3 (Wortlaut-
Auswahl; EuGH C-681/17 Rn. 40, 41); II. Ausübung – 1. Erklärung § 355 Abs. 1 S. 2–4 (BT-Drs. 17/12637 S. 60; § 356a);
2. Frist § 355 Abs. 2 S. 1, § 356 Abs. 2 Nr. 1 Buchst. a, Abs. 3 S. 1, Höchstfrist § 356 Abs. 4 S. 1 (geltende
Nummerierung!), Absendung § 355 Abs. 1 S. 5, Zeitstrahl; Verweis 117 (Fristrechnung); III. Rechtsfolgen – Rückgewähr
§§ 355 Abs. 3 S. 1, 357 Abs. 1; Wertersatz § 357a Abs. 1 (Wortlautkarte; ErwG 47 RL 2011/83/EU, BT-Drs. 17/12637 S. 63,
BGH VIII ZR 55/15 Rn. 20, 22; EuGH C-681/17 Rn. 47); Ergebnis (Aufrechnung §§ 387, 389); Klausurtipp; Schema; Merksatz.
Belege: ../RECHTSSTAND.md.
Figuren: Ilka (sabrina), Herr Riemann (william); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ilka": "sabrina", "Riemann": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Bestellung ------------------------------------------------------------------------------------------
    ("[fall]Ilka bestellt am vierten September im Onlineshop von Herrn Riemann ein Paar Sneaker für hundertzwanzig Euro. "
     "[liefer]Am achten September kommt das Paket.", 0.3),
    ("[il1]Die passen perfekt.", 0.3, "Ilka"),
    # --- A2 Fall: draußen getragen ---------------------------------------------------------------------------------------
    ("[park]Am zwölften September trägt sie die Sneaker einen ganzen Nachmittag draußen im Park. [sohle]Danach sind die Sohlen "
     "verschmutzt. [gef]Und so richtig gefallen sie ihr doch nicht.", 0.3),
    # --- A3 Fall: Widerruf und Rücksendung -------------------------------------------------------------------------------
    ("[zurueck]Am fünfzehnten September schickt sie die Sneaker zurück und schreibt Herrn Riemann eine E-Mail.", 0.3),
    ("[il2]Ich widerrufe den Kauf. Bitte erstatten Sie mir die hundertzwanzig Euro.", 0.3, "Ilka"),
    # --- A4 Fall: Retourenannahme bei Herrn Riemann ----------------------------------------------------------------------
    ("[ri]Herr Riemann packt das Paket aus [spur]und sieht die Spuren an den Sohlen.", 0.3),
    ("[ri1]Die sind ja getragen! Getragene Schuhe nehme ich nicht zurück.", 0.3, "Riemann"),
    ("[wert]Mit den Spuren sind die Sneaker nur noch achtzig Euro wert. [frage]Kann Ilka trotzdem widerrufen? "
     "[frage2]Und muss sie für das Tragen bezahlen?", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau --------------------------------------------------------------------------------------------------------
    ("[plan]Den Widerruf prüfst du in drei Schritten: [p1]Römisch eins, besteht ein Widerrufsrecht? [p2]Römisch zwei, "
     "wurde es wirksam ausgeübt? [p3]Und römisch drei, die Rechtsfolgen.", PS),
    # --- D I. 1. Verbrauchervertrag ---------------------------------------------------------------------------------------
    ("[v1]Römisch eins, erstens: ein Verbrauchervertrag, also ein Vertrag zwischen einem Unternehmer und einem "
     "Verbraucher, Paragraf dreihundertzehn Absatz drei. [v2]Ilka kauft privat, Herr Riemann betreibt den Shop gewerblich. "
     "[v106]Mehr dazu im Video zum Verbraucherbegriff.", P),
    # --- E I. 2. Fernabsatzvertrag, § 312c Abs. 1 (Wortlaut) --------------------------------------------------------------
    ("[fa1]Zweitens: ein Fernabsatzvertrag, Paragraf dreihundertzwölf c Absatz eins. [fa2]Beide Seiten verwenden für "
     "Verhandlung und Vertragsschluss ausschließlich Fernkommunikationsmittel, [fa3]es sei denn, der Vertrag kommt nicht im "
     "Rahmen eines für den Fernabsatz organisierten Vertriebssystems zustande. [fa4]Ein Onlineshop ist ein solches System, "
     "und Ilka hat nur über die Website bestellt.", P),
    # --- F I. 3. Widerrufsrecht, § 312g Abs. 1 (Wortlaut) ----------------------------------------------------------------
    ("[wr1]Drittens: das Widerrufsrecht selbst. Paragraf dreihundertzwölf g Absatz eins: Dem Verbraucher steht bei "
     "außerhalb von Geschäftsräumen geschlossenen Verträgen und bei Fernabsatzverträgen ein Widerrufsrecht gemäß Paragraf "
     "dreihundertfünfundfünfzig zu.", P),
    # --- G Ausnahmen, § 312g Abs. 2 ---------------------------------------------------------------------------------------
    ("[au1]Absatz zwei nennt Ausnahmen, drei sind beim Onlinekauf wichtig. [au2]Nummer eins: Waren, die nicht "
     "vorgefertigt sind und nach den Vorgaben des Verbrauchers hergestellt werden, etwa Schuhe nach Maß. [au3]Nummer zwei: "
     "Waren, die schnell verderben können, etwa frischer Fisch. [au4]Nummer drei: versiegelte Waren, die aus Gründen der "
     "Hygiene nicht zur Rückgabe geeignet sind, wenn die Versiegelung nach der Lieferung entfernt wurde. [eugh]Der Europäische Gerichtshof "
     "legt das eng aus: Selbst eine Matratze ohne Schutzfolie fällt nicht darunter. [au5]Die Sneaker sind Serienware, "
     "sie verderben nicht und waren nicht versiegelt. [au6]Keine Ausnahme greift. Ilka hat ein Widerrufsrecht.", PS),
    # --- H II. 1. Erklärung, § 355 Abs. 1 ---------------------------------------------------------------------------------
    ("[e1]Römisch zwei: die Ausübung. Erstens, die Erklärung gegenüber dem Unternehmer, Paragraf dreihundertfünfundfünfzig "
     "Absatz eins. [e2]Aus ihr muss der Entschluss zum Widerruf eindeutig hervorgehen. [e3]Eine Begründung braucht sie "
     "nicht. [e4]Kommentarlos zurückschicken reicht nach der Gesetzesbegründung nicht, "
     "[e5]ein Zettel mit eindeutiger Erklärung im Paket schon. [e6]Onlineshops müssen dafür außerdem eine "
     "Widerrufsfunktion anbieten, Paragraf dreihundertsechsundfünfzig a. [e7]Die E-Mail von Ilka ist "
     "eindeutig.", P),
    # --- I II. 2. Frist (Zeitstrahl) --------------------------------------------------------------------------------------
    ("[fr1]Zweitens: die Frist. Sie beträgt vierzehn Tage, Paragraf dreihundertfünfundfünfzig Absatz zwei. [fr2]Beim "
     "Verbrauchsgüterkauf beginnt sie erst, wenn der Verbraucher die Ware erhalten hat, Paragraf dreihundertsechsundfünfzig "
     "Absatz zwei Nummer eins a, [fr3]und nicht, bevor er ordnungsgemäß belehrt wurde, Absatz drei. [fr4]Ilka erhält die "
     "Sneaker am achten September. Die Frist endet am zweiundzwanzigsten September. [fr5]Ihre E-Mail vom fünfzehnten September ist rechtzeitig, die "
     "Absendung genügt. [fr117]Die genaue Fristrechnung zeigt das Video zu den Klausurfehlern. "
     "[fr6]Fehlt die Belehrung, erlischt das Widerrufsrecht spätestens zwölf Monate und vierzehn Tage nach dem Erhalt, "
     "Paragraf dreihundertsechsundfünfzig Absatz vier. [fr7]Hier wäre das der zweiundzwanzigste September zweitausendsiebenundzwanzig.", PS),
    # --- J III. Rechtsfolgen: Rückgewähr ----------------------------------------------------------------------------------
    ("[rf1]Römisch drei: die Rechtsfolgen. Die empfangenen Leistungen sind zurückzugewähren, spätestens nach vierzehn "
     "Tagen, Paragrafen dreihundertfünfundfünfzig Absatz drei und dreihundertsiebenundfünfzig. [rf2]Herr Riemann muss die "
     "hundertzwanzig Euro erstatten.", P),
    # --- K Wertersatz, § 357a Abs. 1 (Wortlaut) ---------------------------------------------------------------------------
    ("[we1]Aber für das Tragen kann Ilka Wertersatz schulden, Paragraf dreihundertsiebenundfünfzig a Absatz eins. "
     "[we2]Erstens: Der Wertverlust geht auf einen Umgang mit der Ware zurück, der zur Prüfung von Beschaffenheit, "
     "Eigenschaften und Funktionsweise nicht notwendig war. [we3]Prüfen darf der Verbraucher so, wie er es in einem "
     "Geschäft dürfte. [we4]Nach der Richtlinie heißt das: ein Kleidungsstück anprobieren, aber nicht "
     "tragen. [we5]Anprobieren in der Wohnung wäre also erlaubt. Ein Nachmittag draußen im Park ist mehr als Prüfen. "
     "[we6]Zweitens: Der Händler hat ordnungsgemäß über das Widerrufsrecht belehrt. Das ist hier der Fall. [we7]Das "
     "Widerrufsrecht verliert Ilka dadurch nicht. Sie haftet nur für den Wertverlust.", PS),
    # --- L Ergebnis -------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Ilka hat wirksam widerrufen. [erg2]Herr Riemann muss die hundertzwanzig Euro zurückzahlen. "
     "[erg3]Ilka schuldet ihm Wertersatz für den Wertverlust, hier vierzig Euro. [erg4]Rechnet er auf, zahlt er ihr "
     "achtzig Euro zurück.", PS),
    # --- M Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Getragene Ware ist kein Ausschlussgrund. [tipp2]Den Gebrauch prüfst du nicht beim "
     "Widerrufsrecht, sondern erst bei den Rechtsfolgen, beim Wertersatz.", PS),
    # --- N Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k1]Römisch eins: Widerrufsrecht. [k11]Erstens: Verbrauchervertrag. [k12]Zweitens: "
     "Fernabsatzvertrag. [k13]Drittens: Widerrufsrecht nach Paragraf dreihundertzwölf g Absatz eins, [k14]keine Ausnahme "
     "nach Absatz zwei. [k2]Römisch zwei: Ausübung. [k21]Erstens: eindeutige Erklärung. [k22]Zweitens: innerhalb der Frist. "
     "[k3]Römisch drei: Rechtsfolgen. [k31]Erstens: Rückgewähr. [k32]Zweitens: gegebenenfalls Wertersatz.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Getragen heißt nicht ausgeschlossen. [mk2]Widerrufen kannst du auch nach dem Tragen. [mk3]Was über "
     "das Prüfen hinausgeht, zahlst du als Wertersatz.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
