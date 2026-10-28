"""Willenserklärung – Fall nach der „Trierer Weinversteigerung“ (Lehrbuchfall). [marke] = Bildelement ab diesem Wort."""

P, PS = 0.4, 0.9

SEGMENTE = [
    # --- Fall ---------------------------------------------------------------------------------------
    ("[fall]Trier, eine Weinversteigerung. [a]Anton ist zum ersten Mal dabei. [wein]Gerade wird ein Posten Riesling aufgerufen.", P),
    ("Da [freund]entdeckt Anton hinten im Saal einen alten Freund. [winkt]Er hebt die Hand und winkt ihm zu.", P),
    ("[regel]Nach den Versteigerungsbedingungen bedeutet eine erhobene Hand: Ich biete hundert Euro mehr.", P),
    ("[zuschlag]Der Auktionator ruft: Zum Dritten, zugeschlagen! [schreck]Anton ist entsetzt.", P),
    ("[frage]Muss Anton den Wein bezahlen?", PS),
    # --- Anspruch und Vertragsschluss ---------------------------------------------------------------------
    ("[schema]Der Versteigerer könnte einen Anspruch auf Zahlung des Kaufpreises haben, [a433]aus Paragraf vierhundertdreiunddreißig Absatz zwei BGB.", P),
    ("[vertrag]Dafür braucht es einen Kaufvertrag, also zwei übereinstimmende Willenserklärungen. "
     "[gebot]Bei einer Versteigerung ist das Gebot das Angebot, [zsl]der Zuschlag die Annahme. [156]So regelt es Paragraf hundertsechsundfünfzig.", P),
    ("[kern]Die entscheidende Frage lautet also: Ist das Handheben von Anton überhaupt eine Willenserklärung?", PS),
    # --- Definition -------------------------------------------------------------------------------------
    ("[def]Eine Willenserklärung ist die Äußerung eines Willens, der unmittelbar auf eine Rechtsfolge gerichtet ist. "
     "[zwei]Sie hat einen objektiven und einen subjektiven Tatbestand.", PS),
    # --- Objektiver Tatbestand ----------------------------------------------------------------------------
    ("[obj]Objektiv fragst du: Wie durfte ein vernünftiger Empfänger das Verhalten verstehen? "
     "[133]Maßstab sind die Paragrafen hundertdreiunddreißig und hundertsiebenundfünfzig.", P),
    ("[objfall]Im Versteigerungssaal bedeutet eine erhobene Hand ein Gebot. [objok]Der objektive Tatbestand liegt vor.", PS),
    # --- Subjektiver Tatbestand -----------------------------------------------------------------------------
    ("[subj]Subjektiv unterscheidet man drei Elemente.", P),
    ("[hw]Erstens den Handlungswillen: Der Erklärende handelt bewusst. [hwbsp]Er fehlt etwa bei einem bloßen Reflex. "
     "[hwfolge]Ohne Handlungswillen gibt es keine Willenserklärung.", P),
    ("[eb]Zweitens das Erklärungsbewusstsein: Der Erklärende weiß, dass er überhaupt etwas rechtlich Erhebliches erklärt.", P),
    ("[gw]Drittens den Geschäftswillen: Er will eine ganz bestimmte Rechtsfolge. "
     "[gwfolge]Fehlt nur der Geschäftswille, ist die Erklärung wirksam, aber nach Paragraf hundertneunzehn anfechtbar.", PS),
    # --- Anwendung auf Anton ------------------------------------------------------------------------------
    ("[anton]Und bei Anton? [antonhw]Er hebt die Hand bewusst, der Handlungswille ist da. "
     "[antoneb]Aber er will nur grüßen. Er weiß nicht, dass er rechtlich etwas erklärt. Ihm fehlt das Erklärungsbewusstsein.", PS),
    # --- Streit ------------------------------------------------------------------------------------------------
    ("[streit]Ist eine Erklärung ohne Erklärungsbewusstsein eine Willenserklärung? Das ist umstritten.", P),
    ("[wt]Nach der Willenstheorie nicht, denn es fehlt ein echter Wille. "
     "[wtfolge]Anton wäre nicht gebunden, müsste aber analog Paragraf hundertzweiundzwanzig den Vertrauensschaden ersetzen.", P),
    ("[hm]Die herrschende Meinung und der Bundesgerichtshof stellen auf Zurechnung ab. "
     "[hm1]Eine Willenserklärung liegt vor, wenn der Erklärende bei der im Verkehr erforderlichen Sorgfalt hätte erkennen "
     "und vermeiden können, dass sein Verhalten als Willenserklärung verstanden wird, [hm2]und wenn der Empfänger sie auch so verstanden hat.", P),
    ("[hmgrund]Dafür spricht der Schutz des Rechtsverkehrs. Wer so einen Anschein setzt, muss ihn sich zurechnen lassen. "
     "[hmanf]Gefangen ist der Erklärende trotzdem nicht: Er kann analog Paragraf hundertneunzehn Absatz eins anfechten.", P),
    ("[hmfall]Anton hätte erkennen können, dass Handheben bei einer Versteigerung als Gebot gilt. "
     "[hmfall2]Und der Auktionator hat es so verstanden. "
     "[hmerg]Also liegt eine Willenserklärung vor. Mit dem Zuschlag ist der Kaufvertrag zustande gekommen.", PS),
    # --- Anfechtung ---------------------------------------------------------------------------------------------
    ("[anf]Anton kann aber anfechten. [121]Er muss das unverzüglich tun, Paragraf hunderteinundzwanzig. "
     "[142]Dann ist der Vertrag von Anfang an nichtig, Paragraf hundertzweiundvierzig Absatz eins.", P),
    ("[122]Den Vertrauensschaden muss er trotzdem ersetzen, Paragraf hundertzweiundzwanzig, [122bsp]etwa die Kosten einer erneuten Versteigerung.", PS),
    # --- Schema ---------------------------------------------------------------------------------------------------
    ("[sch]So baust du die Klausur auf. [s1]Erstens: Ist der Anspruch entstanden? Kaufvertrag durch Gebot und Zuschlag.", P),
    ("[s2]Beim Gebot prüfst du den objektiven und den subjektiven Tatbestand. "
     "[s3]Fehlt das Erklärungsbewusstsein, entscheidest du den Streit und prüfst die Zurechnung.", P),
    ("[s4]Zweitens: Ist der Anspruch durch Anfechtung untergegangen? [s5]Ergebnis: kein Kaufpreis, aber Ersatz des Vertrauensschadens.", PS),
    # --- Merksatz --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ohne Handlungswillen keine Willenserklärung. "
     "[m2]Ohne Erklärungsbewusstsein nach herrschender Meinung schon, wenn sie zurechenbar ist. [m3]Dann hilft nur die Anfechtung.", 1.4),
]
