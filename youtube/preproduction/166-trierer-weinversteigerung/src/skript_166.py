"""Folge 166 · Trierer Weinversteigerung: Erklärungsbewusstsein beim Winken? (Mo · Der Fall · Klassiker-Fall;
§§ 119 I analog, 121, 122, 133, 142, 156, 157 BGB). Die Trierer Weinversteigerung ist ein Lehrbuchfall (Hermann Isay,
Die Willenserklärung im Thatbestande des Rechtsgeschäfts, 1899, S. 25 – Scan gelesen), kein Gerichtsfall.
Leitentscheidung: BGH, Urt. v. 7.6.1984 – IX ZR 66/83, BGHZ 91, 324 (Sparkassen-Bürgschaft), Volltext DFR
(servat.unibe.ch/dfr/bz091324.html) mit Seiten der amtlichen Sammlung; bestätigt u. a. BGH XI ZR 537/21 Rn. 29.
Fiktiver Hook: Ekkehard (Stimme christian) winkt bei einer Weinversteigerung seiner Freundin Reinhild (spricht nicht) zu,
Auktionatorin Frau Haller (Stimme hilde) erteilt den Zuschlag. Wein nur als Fass-Icon, kein Alkoholkonsum.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Haller": "hilde", "Ekkehard": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Weinversteigerung (fiktiv) ------------------------------------------------------------------------
    ("[fall]Eine Weinversteigerung. [regel]Im Saal gilt: Wer die Hand hebt, bietet. [haller]Auktionatorin Frau Haller "
     "versteigert Fässer aus ihrem eigenen Weinkeller.", P),
    ("[h1]Ein Fass Riesling. Achthundertfünfzig Euro sind geboten. Wer bietet neunhundert?", P, "Haller"),
    ("[ekke]Ekkehard ist nur mitgekommen, um zuzusehen. [rein]Da entdeckt er an der Tür seine Freundin Reinhild "
     "[wink]und hebt die Hand, um ihr zuzuwinken.", P),
    ("[h2]Neunhundert Euro vom Herrn in der Mitte! Zum Ersten, zum Zweiten, und zugeschlagen!", P, "Haller"),
    ("[e1]Moment! Ich habe nicht geboten. Ich habe nur meiner Freundin zugewinkt!", P, "Ekkehard"),
    ("[p156]Paragraf hundertsechsundfünfzig BGB: Bei einer Versteigerung kommt der Vertrag erst durch den Zuschlag "
     "zustande. [frage]Aber war Ekkehards Winken überhaupt ein Gebot, obwohl er gar nicht daran dachte, etwas zu "
     "erklären?", PS),
    # --- A3 Der Klassiker: Lehrbuchfall und BGHZ 91, 324 ---------------------------------------------------------------
    ("[klassiker]Das ist die Trierer Weinversteigerung: ein klassischer Lehrbuchfall aus dem Jahr "
     "achtzehnhundertneunundneunzig, kein Gerichtsfall. [bgh]Entschieden hat der Bundesgerichtshof die Frage "
     "neunzehnhundertvierundachtzig in einem anderen Fall. [spk]Eine Sparkasse schrieb einer Firma, sie habe für deren "
     "Kundin eine Bürgschaft übernommen. [mitt]Dabei wollte sie nur etwas mitteilen, nicht bürgen.", P),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand der Willenserklärung: objektiv -------------------------------------------------------------------
    ("[tb]Frau Haller verlangt neunhundert Euro. Das setzt einen Kaufvertrag voraus, also ein Gebot von Ekkehard. "
     "[ot]Eine Willenserklärung hat einen objektiven und einen subjektiven Tatbestand. [ausl]Objektiv kommt es darauf an, "
     "wie der Empfänger das Verhalten verstehen durfte. [p133]Nach den Paragrafen hundertdreiunddreißig und "
     "hundertsiebenundfünfzig ist der wirkliche Wille zu erforschen, [p157]aber nach Treu und Glauben mit Rücksicht auf "
     "die Verkehrssitte.", P),
    ("[saal]Im Versteigerungssaal heißt die erhobene Hand: Ich biete mehr. [objok]Objektiv liegt also ein Gebot vor.", P),
    # --- C2 subjektiv ---------------------------------------------------------------------------------------------------
    ("[st]Subjektiv unterscheidet man drei Elemente. [hw]Der Handlungswille: Ekkehard hebt die Hand bewusst, kein "
     "Reflex. [eb]Das Erklärungsbewusstsein: das Bewusstsein, überhaupt etwas rechtlich Erhebliches zu erklären. "
     "[ebn]Das fehlt ihm, er wollte nur winken. [gw]Und der Geschäftswille, ein bestimmtes Geschäft zu schließen. "
     "Den hat er erst recht nicht.", P),
    ("[frage2]Gibt es eine Willenserklärung ohne Erklärungsbewusstsein?", PS),
    # --- D Streit ------------------------------------------------------------------------------------------------------
    ("[wt]Die Willenstheorie sagt nein: Das Erklärungsbewusstsein sei unverzichtbar. [w118]Sie stützt sich auf "
     "Paragraf hundertachtzehn: Eine nicht ernstlich gemeinte Erklärung ist nichtig. [w122]Der Erklärende schulde "
     "allenfalls analog Paragraf hundertzweiundzwanzig den Vertrauensschaden.", P),
    ("[et]Die Gegenansicht schützt das Vertrauen des Empfängers und den Verkehr: [et2]Die Erklärung ist zunächst "
     "wirksam, kann aber angefochten werden.", P),
    ("[bghz]Dem folgt der Bundesgerichtshof, mit einer Einschränkung. [formel]Trotz fehlenden Erklärungsbewusstseins "
     "liegt eine Willenserklärung vor, wenn der Erklärende bei Anwendung der im Verkehr erforderlichen Sorgfalt hätte "
     "erkennen und vermeiden können, dass seine Äußerung als Willenserklärung aufgefasst werden durfte, [verst]und wenn "
     "der Empfänger sie auch tatsächlich so verstanden hat. [pot]Man spricht von potentiellem Erklärungsbewusstsein.", P),
    ("[wahl]Der Grund: Der Erklärende behält die Wahl. [wa]Er kann anfechten und muss dann den Vertrauensschaden "
     "ersetzen. [wb]Oder er bleibt bei seiner Erklärung und erhält die Gegenleistung. [p118]Paragraf hundertachtzehn "
     "passt nicht: Er meint den, der bewusst keine Bindung will.", P),
    ("[sub]Für Ekkehard heißt das: Wer im Versteigerungssaal die Hand hebt, hätte erkennen können, dass das als Gebot "
     "gilt. [hver]Und Frau Haller hat es auch so verstanden. [weok]Die Willenserklärung liegt vor; [kv]mit dem Zuschlag "
     "ist der Kaufvertrag geschlossen.", PS),
    # --- E Anfechtung ---------------------------------------------------------------------------------------------------
    ("[anf]Ekkehard kann sich aber lösen. [p119]Nach Paragraf hundertneunzehn Absatz eins kann anfechten, wer eine "
     "Erklärung dieses Inhalts überhaupt nicht abgeben wollte. [bgh119]Das trifft nach dem Bundesgerichtshof auch den, "
     "der gar keine rechtsgeschäftliche Erklärung abgeben wollte. [analog]Meist spricht man von einer Anfechtung analog "
     "Paragraf hundertneunzehn.", P),
    ("[p121]Die Anfechtung muss unverzüglich erfolgen, also ohne schuldhaftes Zögern, nachdem er den Anfechtungsgrund "
     "kennt. [mangel]Und sie muss erkennen lassen, dass er das Geschäft gerade wegen des Willensmangels nicht gelten "
     "lassen will. [spk2]Daran scheiterte die Sparkasse: Ihr erster Brief bestritt nur die Bürgschaft, "
     "[tage]die Anfechtung kam fünfzehn Tage später, zu spät.", P),
    ("[eok]Ekkehard dagegen widerspricht sofort und nennt den Grund: Er hat nur gewinkt. [p142]Damit ist der Kaufvertrag "
     "nach Paragraf hundertzweiundvierzig von Anfang an nichtig.", P),
    ("[p122]Aber Paragraf hundertzweiundzwanzig: Ekkehard muss Frau Haller den Schaden ersetzen, den sie erleidet, weil "
     "sie auf die Gültigkeit vertraut hat. [kost]Etwa die Kosten, das Fass noch einmal anzubieten. [deckel]Höchstens aber "
     "so viel, wie ihr der Vertrag gebracht hätte.", PS),
    # --- F Lösung des Hooks ---------------------------------------------------------------------------------------------
    ("[loes]Ergebnis: Ekkehards Winken war eine Willenserklärung, der Vertrag kam zustande. [loes2]Er hat ihn wirksam "
     "angefochten und muss die neunhundert Euro nicht zahlen. [loes3]Frau Haller erhält nur ihren Vertrauensschaden.", PS),
    # --- G Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Das Erklärungsbewusstsein prüfst du im subjektiven Tatbestand der Willenserklärung. "
     "[tipp2]Erst wenn die Erklärung steht, kommt die Anfechtung. Schreib also nicht vorschnell: kein Vertrag.", PS),
    # --- H Prüfschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Kaufvertrag durch Gebot und Zuschlag. [k2]Objektiver Tatbestand: "
     "Erklärungswert aus Sicht des Empfängers. [k3]Subjektiver Tatbestand: Handlungswille und Erklärungsbewusstsein, "
     "[k4]fehlt es, genügt das potentielle Erklärungsbewusstsein. [k5]Römisch zwei: Nichtigkeit durch Anfechtung "
     "analog Paragraf hundertneunzehn, unverzüglich nach Paragraf hunderteinundzwanzig. [k6]Römisch drei: "
     "Vertrauensschaden nach Paragraf hundertzweiundzwanzig.", PS),
    # --- I Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer erkennen konnte, dass sein Verhalten als Willenserklärung verstanden wird, muss es sich "
     "zurechnen lassen. [m2]Er kann anfechten, zahlt dann aber den Vertrauensschaden.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
