"""Folge 150 · Elfes-Urteil: Allgemeine Handlungsfreiheit nach Art. 2 I GG (Fr · Klausurpraxis · Klassiker-Fall;
Art. 2 I, 11 GG; § 7 PassG). Echter Fall sachlich nacherzählt: BVerfG, Urt. v. 16.1.1957 – 1 BvR 253/56,
BVerfGE 6, 32 (Elfes), Volltext DFR (servat.unibe.ch/dfr/bv006032.html), Seiten der amtlichen Sammlung <…>.
Ausblick: BVerfG, Beschl. v. 6.6.1989 – 1 BvR 921/85, BVerfGE 80, 137 (Reiten im Walde) <152 f.> (Volltext DFR).
NEUTRAL: Wilhelm Elfes wird nur sachlich benannt, nicht dargestellt; der Grund der Passverweigerung nur so, wie ihn der
Volltext beschreibt (<33>), ohne Bewertung. Keine Parteinamen, keine Logos, kein Porträt.
Moderner Einstieg mit fiktiven Figuren: Torben (Antragsteller, Stimme niklas) und Herr Haupt (Sachbearbeiter der
Passbehörde, Stimme helmut); der Hook folgt dem Wortlaut von § 7 Abs. 1 Nr. 1 PassG.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Torben": "niklas", "Haupt": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Moderner Einstieg (fiktiv, § 7 Abs. 1 Nr. 1 PassG) ----------------------------------------------------------
    ("[fall]Torben will zu einer Konferenz ins Ausland. [antrag]Bei der Passbehörde beantragt er einen neuen Reisepass.", P),
    ("[h1]Den Pass müssen wir versagen. Bestimmte Tatsachen begründen die Annahme, "
     "dass Sie erhebliche Belange der Bundesrepublik gefährden.", P, "Haupt"),
    ("[o1]Ich will doch nur reisen. Welches Grundrecht schützt das?", P, "Torben"),
    ("[frage0]Schützt das Grundgesetz die Ausreise, und woran wird die Versagung gemessen? "
     "[klassiker]Die Antwort gibt das Elfes-Urteil des Bundesverfassungsgerichts.", PS),
    # --- B Der echte Fall (BVerfGE 6, 32 <33 f.>) -----------------------------------------------------------------------
    ("[elfes]Wilhelm Elfes war nach dem Krieg Oberbürgermeister von Mönchengladbach, später dort Oberstadtdirektor. "
     "[kritik]Er kritisierte öffentlich, auch im Ausland, die Politik der Bundesregierung, vor allem zur Wehrpolitik "
     "und zur Frage der Wiedervereinigung. [pass]Neunzehnhundertdreiundfünfzig wollte er seinen Reisepass verlängern "
     "lassen. [versagt]Die Passbehörde lehnte ab, ohne nähere Begründung, gestützt auf Paragraf sieben des Passgesetzes.", P),
    ("[norm]Danach war der Pass zu versagen, wenn Tatsachen die Annahme rechtfertigten, der Antragsteller gefährde "
     "die innere oder äußere Sicherheit oder sonstige erhebliche Belange der Bundesrepublik. [wien]Das "
     "Bundesverwaltungsgericht stützte die Versagung auf seine Teilnahme an einem Friedenskongress in Wien und eine "
     "Erklärung, die er dort verlas. [vb]Elfes blieb in allen Instanzen erfolglos und erhob Verfassungsbeschwerde.", P),
    ("[frage]Verletzt die Passversagung ein Grundrecht?", PS),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D I. Art. 11 GG (<34–36>) --------------------------------------------------------------------------------------
    ("[urteil]Am sechzehnten Januar neunzehnhundertsiebenundfünfzig entscheidet das Bundesverfassungsgericht. "
     "[a11]Erste Frage: Artikel elf Absatz eins. Alle Deutschen genießen Freizügigkeit im ganzen Bundesgebiet. "
     "[wortl]Schon dieser Wortlaut spricht nach dem Gericht nicht für ein Recht auf Ausreise. [schr]Auch die Schranken "
     "in Absatz zwei zielen auf das Inland; die seit langem bekannte Passversagung aus Gründen der Staatssicherheit "
     "fehlt dort. [nein11]Artikel elf erfasst die Ausreise also nicht.", P),
    # --- E II. Art. 2 Abs. 1 GG (<36 f.>) ---------------------------------------------------------------------------------
    ("[a2]Geschützt ist sie trotzdem, durch Artikel zwei Absatz eins: Jeder hat das Recht auf die freie Entfaltung "
     "seiner Persönlichkeit, soweit er nicht die Rechte anderer verletzt und nicht gegen die verfassungsmäßige Ordnung "
     "oder das Sittengesetz verstößt.", P),
    ("[kern]Eine Gegenansicht wollte nur einen Kernbereich der Persönlichkeit schützen. [warum]Das Gericht fragt: "
     "Wie sollte eine Entfaltung nur in diesem Kern gegen die Rechte anderer oder die verfassungsmäßige Ordnung "
     "verstoßen? [umf]Gemeint ist deshalb die Handlungsfreiheit im umfassenden Sinn. [tun]Die ursprüngliche Fassung "
     "lautete schlicht: Jeder kann tun und lassen, was er will. [ausfl]Die Ausreisefreiheit ist ein Ausfluss dieser "
     "allgemeinen Handlungsfreiheit.", P),
    ("[auff]Für bestimmte Lebensbereiche gibt es besondere Grundrechte. Nur soweit keines davon greift, beruft man "
     "sich auf Artikel zwei Absatz eins. [auff2]Man nennt es deshalb das Auffanggrundrecht.", PS),
    # --- F III. Schranke: verfassungsmäßige Ordnung (<37–43>) -------------------------------------------------------------
    ("[schranke]Die Schranke ist die verfassungsmäßige Ordnung. [ordn]Gemeint ist die verfassungsmäßige "
     "Rechtsordnung: [jede]jede Rechtsnorm, die formell und materiell der Verfassung gemäß ist. [leer]Läuft das "
     "Grundrecht damit leer? Nein. Das Gesetz muss selbst verfassungsmäßig sein, vor allem rechtsstaatlich. [kernber]Und "
     "ein letzter, unantastbarer Bereich privater Lebensgestaltung bleibt jedem Zugriff entzogen.", P),
    ("[passg]Gehört das Passgesetz dazu? [anspr]Es gibt einen Anspruch auf den Pass und erlaubt die Versagung nur unter "
     "bestimmten Voraussetzungen; so wahrt es die Freiheitsvermutung. [vage]Bedenken weckte nur die Klausel sonstige "
     "erhebliche Belange: Der Gesetzgeber darf die Grenzen der Freiheit nicht mit einer vagen Generalklausel dem Ermessen "
     "der Verwaltung überlassen. [voll]Doch die Gerichte prüfen den Begriff voll nach, [eng]und er ist eng zu "
     "verstehen: Die Belange müssen an Gewicht der inneren und äußeren Sicherheit nahekommen.", P),
    # --- G Ergebnis (<32 Tenor, 43–45>) -----------------------------------------------------------------------------------
    ("[erg]Ergebnis: So verstanden ist die Vorschrift verfassungsgemäß, [anw]und auch ihre Anwendung durch das "
     "Bundesverwaltungsgericht hält stand. [zur]Elfes ist nicht in seinen Grundrechten verletzt, die Verfassungsbeschwerde wird zurückgewiesen. [begr]Nicht gebilligt "
     "hat das Gericht nur die Versagung ohne Begründung: Wer betroffen ist, hat Anspruch darauf, die Gründe zu erfahren.", PS),
    # --- H Bedeutung (Leitsatz 4 <32>, <41>; BVerfGE 80, 137 <152 f.>) -------------------------------------------------
    ("[tor]Die Bedeutung reicht weit über den Pass hinaus: Jeder kann mit der Verfassungsbeschwerde geltend machen, eine "
     "Norm, die seine Handlungsfreiheit beschränkt, gehöre nicht zur verfassungsmäßigen Ordnung. [messbar]So wird jede "
     "solche Norm am ganzen Grundgesetz messbar. [reiten]Neunzehnhundertneunundachtzig bestätigt das Gericht im "
     "Beschluss Reiten im Walde: Geschützt ist jede Form menschlichen Handelns, [verh]und den materiellen Maßstab "
     "für Eingriffe bietet der Grundsatz der Verhältnismäßigkeit.", PS),
    # --- I Zurück zum Einstieg -----------------------------------------------------------------------------------------
    ("[o2]Und was heißt das für meinen Pass?", P, "Torben"),
    ("[heute]Heute steht die Regel in Paragraf sieben Absatz eins Nummer eins des Passgesetzes, fast wortgleich. "
     "[tb1]Torben ist in seiner allgemeinen Handlungsfreiheit betroffen, nicht in der Freizügigkeit. [tb2]Die Behörde "
     "braucht bestimmte Tatsachen, und nach dem Elfes-Urteil müssen die Belange der Sicherheit des Staates an Gewicht nahekommen. "
     "[abs2]Nach Absatz zwei ist von der Versagung abzusehen, wenn sie unverhältnismäßig ist, etwa wenn ein "
     "beschränkter Pass genügt.", PS),
    # --- J Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Artikel zwei Absatz eins immer zuletzt. Erst die speziellen Grundrechte, hier "
     "Artikel elf. [tipp2]Nur wenn keines greift, kommt die allgemeine Handlungsfreiheit als Auffanggrundrecht zum Zug.", PS),
    # --- K Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Schutzbereich. Zuerst die speziellen Grundrechte; Artikel elf erfasst die "
     "Ausreise nicht. [k2]Dann Artikel zwei Absatz eins: jedes Verhalten, auch die Ausreise. [k3]Römisch zwei: Eingriff, "
     "hier die Passversagung. [k4]Römisch drei: Rechtfertigung. Schranke ist die verfassungsmäßige Ordnung. [k5]Prüfe "
     "also das Gesetz formell und materiell, besonders Bestimmtheit und Verhältnismäßigkeit, [k6]und dann seine "
     "Anwendung im Einzelfall.", PS),
    # --- L Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Artikel zwei Absatz eins schützt jedes Verhalten, auch die Ausreise. [m2]Beschränken darf diese "
     "Freiheit nur eine Norm, die formell und materiell verfassungsmäßig ist.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
