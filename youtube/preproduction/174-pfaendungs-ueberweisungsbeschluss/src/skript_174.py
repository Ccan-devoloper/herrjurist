"""Folge 174 · Pfändungs- und Überweisungsbeschluss: Konto- und Lohnpfändung (Fr · 2. Examen · ZV, Format Schema).
Übungsfall nach dem Hook des Themenplans: Der Tischler Herr Dorfmann hat gegen Frau Kästner ein vollstreckbares Urteil über
3.600 Euro (Einbauküche) mit Klausel, zugestellt. Frau Kästner arbeitet bei einem großen Arbeitgeber (fiktives Autowerk, kein
echter Name, keine Marke); ihr Gehalt geht auf ihr Girokonto bei einer Bank (fiktiv).
Aufbau: 1. Antrag und Zuständigkeit (Wortlautkarte § 828 I, II ZPO; § 13 ZPO; § 20 Abs. 1 Nr. 17 RPflG) →
2. Pfändung (Wortlautkarte § 829 I 1, 2: Arrestatorium, Inhibitorium; § 829 I 3 einheitlicher Beschluss; § 834 ZPO, Verweis 153)
→ Wirksamkeit (§ 829 II 1, 2, Wortlautkarte § 829 III; § 192 ZPO) → 3. Überweisung (Wortlautkarte § 835 I; § 835 II; § 829a I;
Wortlautkarte § 836 I) → 4. Drittschuldnererklärung (Wortlautkarte § 840 I, Haftung § 840 II 2) → 5. Lohnpfändung (§§ 850, 850a,
850c ZPO; Pfändungsfreigrenzenbekanntmachung 2026, BGBl. 2026 I Nr. 80; § 832 ZPO) → 6. Konto (Wortlautkarte § 850k I 1;
§ 850k II; § 899 I 1 ZPO) → Ergebnis → Klausurtipp (Lexi) → Prüfschema (Merktabelle der Schritte) → Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Fiktive Figuren: Herr Dorfmann (christian), Frau Kästner (lucy), die Personalleiterin (hilde). Der Bankberater spricht nicht.
stephan nicht eingesetzt (stephan und christian nie Dialogpartner in derselben Szene).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.6

STIMMEN = {"Dorfmann": "christian", "Kästner": "lucy", "Personalleiterin": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Küche ----------------------------------------------------------------------------------------------
    ("[fall]Herr Dorfmann ist Tischler. [kueche]Er baut Frau Kästner eine Einbauküche ein, für dreitausendsechshundert "
     "Euro. [zahlt]Sie zahlt nicht. [urteil]Herr Dorfmann erstreitet ein Urteil, mit Vollstreckungsklausel, und es wird ihr "
     "zugestellt. [job]Frau Kästner arbeitet bei einem großen Arbeitgeber, einem Autowerk. [konto]Ihr Gehalt geht auf ihr "
     "Girokonto.", 0.3),
    ("[d1]Dann hole ich mir mein Geld von Ihrem Gehalt und von Ihrem Konto.", 0.25, "Dorfmann"),
    ("[k1]Mein Gehalt? Davon lebe ich doch!", 0.3, "Kästner"),
    ("[frage]Wie kommt Herr Dorfmann an Lohn und Guthaben? [frage2]Wann wirkt die Pfändung, und was müssen Arbeitgeber und "
     "Bank tun?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Antrag und Zuständigkeit (Wortlaut § 828) -------------------------------------------------------------------
    ("[antrag]Erstens: der Antrag beim zuständigen Gericht. [wl828]Nach Paragraf achthundertachtundzwanzig erfolgen die "
     "gerichtlichen Handlungen bei der Vollstreckung in Forderungen durch das Vollstreckungsgericht. [p828b]Das ist das "
     "Amtsgericht, bei dem die Schuldnerin ihren allgemeinen Gerichtsstand hat, also an ihrem Wohnsitz. [rpfl]Dort "
     "entscheidet der Rechtspfleger, Paragraf zwanzig Absatz eins Nummer siebzehn Rechtspflegergesetz. [voraus]Er prüft die allgemeinen "
     "Vollstreckungsvoraussetzungen: Titel, Klausel und Zustellung, wie in unserem Video zum Grundschema.", P),
    # --- D 2. Pfändung (Wortlaut § 829 I) ---------------------------------------------------------------------------------
    ("[pfaend]Zweitens: die Pfändung. [wl829]Nach Paragraf achthundertneunundzwanzig Absatz eins verbietet das Gericht dem "
     "Drittschuldner, an die Schuldnerin zu zahlen. [arrest]Das ist das Arrestatorium. [inhib]Zugleich gebietet es der "
     "Schuldnerin, sich jeder Verfügung über die Forderung zu enthalten: das Inhibitorium. [dritt]Drittschuldner sind hier "
     "zwei: der Arbeitgeber für den Lohn und die Bank für das Guthaben. [einh]Beide Forderungen kann das Gericht auf "
     "Antrag in einem einheitlichen Beschluss pfänden. [p834]Frau Kästner wird vorher nicht angehört, Paragraf "
     "achthundertvierunddreißig. [verw153]Wie sie sich danach wehrt, zeigen unsere Videos zur Vollstreckungserinnerung und zu den "
     "Rechtsbehelfen.", P),
    # --- E Wirksamkeit: Zustellung an den Drittschuldner (Wortlaut § 829 III) -----------------------------------------------
    ("[zust]Wirksam wird die Pfändung erst mit der Zustellung. [p829_2]Herr Dorfmann lässt den Beschluss den "
     "Drittschuldnern zustellen, durch den Gerichtsvollzieher. [wl829_3]Absatz drei: Mit der Zustellung des Beschlusses an "
     "den Drittschuldner ist die Pfändung als bewirkt anzusehen. [schuldn]Danach stellt der Gerichtsvollzieher den "
     "Beschluss sofort auch Frau Kästner zu.", 0.3),
    ("[p1]Ein Pfändungsbeschluss gegen Frau Kästner. Den pfändbaren Teil ihres Lohns zahlen wir nicht mehr an sie aus.", 0.3,
     "Personalleiterin"),
    # --- F 3. Überweisung (Wortlaut § 835 I, § 836 I) ----------------------------------------------------------------------
    ("[ueber]Drittens: die Überweisung. Der Gläubiger kann sie zusammen mit der Pfändung beantragen. Daher der Name "
     "Pfändungs- und Überweisungsbeschluss. [wl835]Nach Paragraf achthundertfünfunddreißig Absatz eins ist die gepfändete "
     "Geldforderung dem Gläubiger nach seiner Wahl zur Einziehung oder an Zahlungs statt zu überweisen. [unter]Der "
     "Unterschied: An Zahlungs statt geht die Forderung auf ihn über, und er gilt, soweit sie besteht, als befriedigt; zur Einziehung "
     "darf er sie nur einziehen. [wl836]Paragraf achthundertsechsunddreißig Absatz eins: Die Überweisung ersetzt die "
     "förmlichen Erklärungen der Schuldnerin, von denen die Berechtigung zur Einziehung abhängt. [hier835]Herr Dorfmann "
     "wählt die Einziehung. Er darf nun selbst von Arbeitgeber und Bank Zahlung verlangen.", P),
    # --- G 4. Drittschuldnererklärung (Wortlaut § 840 I) -------------------------------------------------------------------
    ("[erkl]Viertens: die Drittschuldnererklärung. [wl840]Nach Paragraf achthundertvierzig Absatz eins muss der "
     "Drittschuldner auf Verlangen des Gläubigers binnen zwei Wochen ab Zustellung erklären, [e1]ob er die Forderung "
     "anerkennt und zahlen will, [e2]ob andere Personen Ansprüche erheben [e3]und ob schon andere Gläubiger gepfändet haben. "
     "[e4]Die Bank erklärt zudem, ob es ein Pfändungsschutzkonto ist.", 0.3),
    ("[p2]Wir erkennen die Lohnforderung an. Andere Pfändungen liegen nicht vor.", 0.3, "Personalleiterin"),
    ("[haft]Erfüllt der Drittschuldner diese Pflicht nicht, haftet er dem Gläubiger für den daraus entstehenden Schaden, "
     "Absatz zwei.", PS),
    # --- H 5. Lohnpfändung: Pfändungsschutz -----------------------------------------------------------------------------------
    ("[lohn]Fünftens: der Pfändungsschutz beim Lohn. [p850]Nach Paragraf achthundertfünfzig ist Arbeitseinkommen "
     "nur nach den Paragrafen achthundertfünfzig a bis i pfändbar. [p850a]Manches ist ganz oder teilweise unpfändbar, etwa die Hälfte der Vergütung "
     "für Mehrarbeit. [p850c]Vor allem bleibt ein Grundbetrag frei, Paragraf achthundertfünfzig c: seit dem ersten Juli "
     "zweitausendsechsundzwanzig eintausendfünfhundertsiebenundachtzig Euro und vierzig Cent im Monat, mehr bei "
     "Unterhaltspflichten. [drei]Vom Betrag darüber bleiben grundsätzlich drei Zehntel frei. [tabelle]Der Beschluss verweist nur auf die "
     "Tabelle der amtlichen Bekanntmachung; daraus liest der Arbeitgeber den pfändbaren Betrag ab. [juli]Die Beträge werden jedes Jahr zum ersten Juli "
     "angepasst. [p832]Und die Pfändung erfasst auch die künftigen Gehälter, Paragraf achthundertzweiunddreißig.", PS),
    # --- I 6. Kontopfändung: Pfändungsschutzkonto --------------------------------------------------------------------------
    ("[konto2]Sechstens: das Konto.", 0.25),
    ("[k2]Bitte führen Sie mein Girokonto als Pfändungsschutzkonto.", 0.3, "Kästner"),
    ("[wl850k]Das kann sie jederzeit verlangen, Paragraf achthundertfünfzig k. Ist schon gepfändet, muss die Bank das ab dem "
     "vierten Geschäftstag nach ihrem Verlangen tun. [moni]An den Gläubiger zahlt sie Guthaben ohnehin erst einen Monat nach "
     "Zustellung des Überweisungsbeschlusses aus, Paragraf achthundertfünfunddreißig Absatz drei. [frei]Und Frau Kästner bleibt jeden Monat ein Freibetrag: der Grundbetrag, aufgerundet auf "
     "volle zehn Euro, derzeit eintausendfünfhundertneunzig Euro, Paragraf achthundertneunundneunzig.", PS),
    # --- J Ergebnis ---------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Herr Dorfmann kommt an Lohn und Guthaben, [erg2]aber nur an den pfändbaren Teil, Monat für Monat.", PS),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Achte auf den Zeitpunkt. Die Pfändung wirkt erst mit der Zustellung an den Drittschuldner, nicht "
     "schon mit dem Erlass des Beschlusses. [tipp2]Und prüfe, wie überwiesen wurde: Nur bei der Überweisung an Zahlungs statt gilt der "
     "Gläubiger als befriedigt.", PS),
    # --- L Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema in fünf Schritten. [s1]Erstens der Antrag beim Vollstreckungsgericht. [s2]Zweitens der Pfändungs- "
     "und Überweisungsbeschluss mit Arrestatorium und Inhibitorium. [s3]Drittens die Zustellung an den Drittschuldner: Jetzt "
     "ist gepfändet. [s4]Viertens die Drittschuldnererklärung binnen zwei Wochen. [s5]Fünftens die Einziehung, begrenzt "
     "durch den Pfändungsschutz.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gepfändet ist erst, wenn der Beschluss dem Drittschuldner zugestellt ist. [m2]Was der Gläubiger bekommt, "
     "begrenzt der Pfändungsschutz: beim Lohn die Tabelle, beim Konto das Pfändungsschutzkonto.", 1.4),
]
