"""Folge 014 · Angebot und Annahme §§ 145 ff. BGB: Wann ist der Vertrag geschlossen? (Examenswissen, Format Schema).
Beispielfall frei erfunden: Gerd bietet Lotte per E-Mail seinen Kombi für 4.000 Euro an, „gilt bis Freitag“ (§ 148).
Am Mittwoch bietet Malte mehr, Gerd widerruft per Mail (zu spät, §§ 145, 130 I 2). Lotte nimmt am Donnerstag an:
Vertrag mit Zugang der Annahme geschlossen. Gegenfälle: Annahme am Samstag (§§ 146, 150 I; Schweigen), ohne Frist
(§ 147 II), Telefon (§ 147 I 2). Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla
(auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Gerd": "johann", "Lotte": "lucy", "Malte": "timo"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A/B Fall: Probefahrt, E-Mail, Widerruf, Annahme -------------------------------------------------------------
    ("[fall]Gerd will seinen alten Kombi verkaufen. [probe]Am Samstag macht Lotte eine Probefahrt. "
     "[mail]Am Sonntagabend schreibt Gerd ihr eine E-Mail.", 0.3),
    ("[g1]Liebe Lotte, du kannst den Kombi für viertausend Euro haben. Mein Angebot gilt bis Freitag.", 0.4, "Gerd"),
    ("[liest]Lotte liest die Mail noch am Sonntag. [anruf]Am Mittwoch ruft Malte bei Gerd an.", 0.3),
    ("[m1]Ich zahle Ihnen viertausendfünfhundert Euro für den Wagen.", 0.4, "Malte"),
    ("[zurueck]Gerd schreibt Lotte sofort: Ich ziehe mein Angebot zurück. "
     "[donn]Am Donnerstagmittag antwortet Lotte trotzdem. Gerd liest die Mail gleich.", 0.3),
    ("[l1]Ich nehme den Kombi für viertausend Euro!", 0.4, "Lotte"),
    ("[g2]Aber ich habe mein Angebot doch zurückgezogen!", 0.5, "Gerd"),
    ("[frage]Ist der Kombi jetzt an Lotte verkauft? Und wann genau kam der Vertrag zustande?", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Anspruch und Vertrag --------------------------------------------------------------------------------------
    ("[ansp]Lotte verlangt den Kombi nach Paragraf vierhundertdreiunddreißig Absatz eins. [vertrag]Dafür braucht es "
     "einen Kaufvertrag, also zwei passende Willenserklärungen: Angebot und Annahme, Paragrafen hundertfünfundvierzig "
     "folgende.", PS),
    # --- E I. Angebot ------------------------------------------------------------------------------------------------
    ("[ang]Römisch eins: das Angebot. [ess]Es muss die wesentlichen Punkte enthalten, beim Kauf also Ware, Preis und "
     "Vertragspartner. [ja]Lotte muss nur noch Ja sagen können. [rbw]Außerdem muss Gerd sich erkennbar binden wollen. "
     "Mein Angebot gilt bis Freitag: deutlicher geht es kaum. [inv]Ein bloßes Werbeschreiben wäre dagegen nur eine "
     "Einladung, selbst ein Angebot zu machen.", P),
    ("[zug]Die E-Mail ist eine Erklärung unter Abwesenden. Sie wird mit Zugang wirksam, Paragraf hundertdreißig. "
     "Lotte hat sie am Sonntag gelesen. [ang_ok]Das Angebot ist wirksam.", PS),
    # --- F II. Bindung und Widerruf ----------------------------------------------------------------------------------
    ("[bind]Römisch zwei: Durfte Gerd am Mittwoch zurückziehen? [p145]Nach Paragraf hundertfünfundvierzig ist er an "
     "sein Angebot gebunden, außer er hat die Bindung ausgeschlossen. [p130]Ein Widerruf wirkt nur, wenn er vorher "
     "oder gleichzeitig mit dem Angebot zugeht, Paragraf hundertdreißig Absatz eins Satz zwei. [spaet]Gerds zweite "
     "Mail kam drei Tage zu spät. Das Angebot steht.", PS),
    # --- G III. Annahme ----------------------------------------------------------------------------------------------
    ("[ann]Römisch drei: die Annahme. [deck]Lotte sagt Ja zu genau diesem Kombi und diesem Preis. [aend]Hätte sie dreitausendfünfhundert Euro geboten, wäre das "
     "nach Paragraf hundertfünfzig Absatz zwei eine Ablehnung mit neuem Angebot. [frist]Sie muss "
     "aber rechtzeitig kommen. Gerd hat eine Frist gesetzt, bis Freitag, Paragraf hundertachtundvierzig. [do]Lottes "
     "Antwort ist am Donnerstag bei ihm.", P),
    ("[erg]Der Kaufvertrag ist geschlossen, und zwar am Donnerstagmittag, als ihre Antwort ankam. [pflicht]Gerd muss "
     "den Kombi an Lotte übergeben und übereignen.", PS),
    # --- H Gegenfall: Annahme am Samstag -----------------------------------------------------------------------------
    ("[sams]Und wenn Lotte erst am Samstag antwortet? [p146]Dann ist das Angebot erloschen, Paragraf "
     "hundertsechsundvierzig. [p150]Ihre verspätete Annahme gilt als neues Angebot, Paragraf hundertfünfzig Absatz "
     "eins. [jetzt]Jetzt liegt es an Gerd, ob er annimmt. [schweig]Schweigt er, ist das grundsätzlich keine Annahme.", PS),
    # --- I Gegenfall: ohne Frist -------------------------------------------------------------------------------------
    ("[ohne]Und ohne Frist? Dann gilt Paragraf hundertsiebenundvierzig Absatz zwei. [regel]Lotte kann annehmen, "
     "solange Gerd unter regelmäßigen Umständen mit ihrer Antwort rechnen darf. [drei]Nach dem Bundesgerichtshof "
     "zählen dazu die Zeit für den Hinweg, eine Überlegungszeit und der Rückweg.", PS),
    # --- J Gegenfall: Telefon ----------------------------------------------------------------------------------------
    ("[tel]Ganz anders am Telefon. [anw]Ein Anruf ist ein Gespräch von Person zu Person, also wie unter Anwesenden. "
     "Bietet Gerd den Kombi am Telefon an, kann Lotte nach Paragraf hundertsiebenundvierzig Absatz eins nur sofort "
     "annehmen.", 0.3),
    ("[deal]Deal! Abgemacht.", 0.4, "Lotte"),
    ("[sofort]Damit ist der Vertrag geschlossen. [spaeter]Wer erst später zusagt, macht nur ein neues Angebot.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Mal dir eine Zeitleiste. [tipp2]Trag jede Erklärung mit dem Tag ein, an dem sie zugeht. "
     "[tipp3]Dann siehst du sofort, ob ein Widerruf zu spät kam und ob die Annahme in der Frist lag.", PS),
    # --- L Klausurschema ---------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Lotte gegen Gerd aus Paragraf vierhundertdreiunddreißig Absatz eins. [k1]Römisch eins: "
     "Angebot, [k1a]mit den wesentlichen Punkten und Rechtsbindungswillen, [k1b]wirksam mit Zugang. [k2]Römisch zwei: "
     "Bindung, kein wirksamer Widerruf.", P),
    ("[k3]Römisch drei: Annahme, [k3a]deckungsgleich [k3b]und rechtzeitig nach den Paragrafen hundertsiebenundvierzig "
     "und hundertachtundvierzig. [k4]Römisch vier: Ergebnis, Vertrag geschlossen, Anspruch entstanden.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein zugegangenes Angebot bindet. [m2]Der Vertrag steht in der Regel, sobald die passende Annahme "
     "rechtzeitig zugeht.", 1.4),
]
