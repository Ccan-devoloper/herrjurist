"""Folge 230 · Gleichheitssatz Art. 3 I GG: Willkürformel und Neue Formel (Mi · Examenswissen · Schema).
Belege: Art. 1 Abs. 3, Art. 3 Abs. 1 GG (gesetze-im-internet.de); BVerfGE 1, 14 <52> (Willkürformel); BVerfGE 55, 72 <88>
(Neue Formel, Beschl. v. 7.10.1980 – 1 BvL 50/79 u. a.); BVerfGE 88, 87 <96>; BVerfGE 138, 136 Rn. 121 f. (stufenloser
Maßstab); BVerfGE 134, 1 Rn. 58, 61 (Vergleichbarkeit, derselbe Träger); BVerfG (K), Beschl. v. 19.7.2016 – 2 BvR 470/08
(Einheimischentarif im Freizeitbad), Rn. 2–4, 8, 24–43, Tenor.
Fiktiver Fall, der dem echten Fall folgt: Freizeitbad einer Gemeinde, betrieben von einer Gesellschaft, die ganz der Gemeinde
gehört; Einheimische zahlen 6 €, alle anderen 9 € (Rabatt rund ein Drittel wie Rn. 2). Figuren: Herr Kühnel (Kasse; stephan),
Frau Dittmer (Einheimische, um 70; hilde), Martha (wohnt im Nachbarort, um 28; lucy). Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Artikel im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Kühnel": "stephan", "Dittmer": "hilde", "Martha": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: an der Kasse des Freizeitbads (fiktiv, folgt 2 BvR 470/08 Rn. 2, 42 f.) --------------------------------
    ("[fall]Samstagmorgen im Freizeitbad einer kleinen Gemeinde. [gmbh]Betrieben wird es von einer Gesellschaft, die ganz "
     "der Gemeinde gehört. [werb]Das Bad wirbt um Urlauber aus der ganzen Region und soll Gewinn bringen.", P),
    ("[kas1]Wer hier im Ort wohnt, zahlt sechs Euro. Alle anderen zahlen neun.", P, "Kühnel"),
    ("[dit]Frau Dittmer wohnt im Ort und zeigt ihren Ausweis.", P),
    ("[di1]Einmal ermäßigt, bitte. Ich wohne gleich um die Ecke.", P, "Dittmer"),
    ("[mar]Martha wohnt im Nachbarort. Für dasselbe Becken soll sie neun Euro zahlen.", P),
    ("[ma1]Gleiches Becken, gleiches Wasser, und ich zahle drei Euro mehr. Ist das gerecht?", P, "Martha"),
    ("[frage]Darf das Bad der Gemeinde Einheimische beim Eintritt bevorzugen? [echt]Unser Fall folgt einem Beschluss des "
     "Bundesverfassungsgerichts vom neunzehnten Juli zweitausendsechzehn: [drittel]Ein Freizeitbad gab den Einwohnern "
     "bestimmter Gemeinden rund ein Drittel Rabatt.", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Norm und Bindung (Art. 3 Abs. 1, Art. 1 Abs. 3 GG; 2 BvR 470/08 Rn. 25 f., 34) ----------------------------
    ("[a3]Maßstab ist Artikel drei Absatz eins: Alle Menschen sind vor dem Gesetz gleich. [a13]Nach Artikel eins Absatz "
     "drei binden die Grundrechte Gesetzgebung, vollziehende Gewalt und Rechtsprechung als unmittelbar geltendes Recht. "
     "[gbind]Das gilt auch für die Betreibergesellschaft: Ein Unternehmen, das ganz der öffentlichen Hand gehört, ist "
     "unmittelbar an die Grundrechte gebunden, auch wenn es privatrechtlich auftritt.", P),
    # --- D Zweistufige Prüfung: Ungleichbehandlung (BVerfGE 134, 1 Rn. 55, 58, 61) -----------------------------------
    ("[zwei]Geprüft wird in zwei Schritten: [s1]erst die Ungleichbehandlung von wesentlich Gleichem, [s2]dann ihre "
     "Rechtfertigung.", P),
    ("[vgl]Zuerst bildest du die Vergleichsgruppen: einheimische und auswärtige Badegäste. [ober]Der gemeinsame "
     "Oberbegriff: Gäste desselben Bads, die dieselbe Leistung kaufen. [selbe]Beide Gruppen behandelt derselbe Träger, das "
     "Bad der Gemeinde. [ungl]Die einen zahlen sechs Euro, die anderen neun: eine Ungleichbehandlung.", P),
    # --- E Maßstab: Willkürformel, Neue Formel, stufenlos (BVerfGE 1, 14; 55, 72; 88, 87; 138, 136) -----------------
    ("[mass]Doch wie streng prüft man die Rechtfertigung? [willk]Anfangs fragte das Bundesverfassungsgericht vor allem nach "
     "Willkür: Der Gleichheitssatz ist verletzt, wenn sich ein vernünftiger, sich aus der Natur der Sache ergebender oder "
     "sonstwie sachlich einleuchtender Grund für die gesetzliche Differenzierung oder Gleichbehandlung nicht finden lässt.", P),
    ("[neu]Neunzehnhundertachtzig folgte die Neue Formel: [nf2]Verletzt ist der Gleichheitssatz, wenn eine Gruppe von "
     "Normadressaten im Vergleich zu anderen Normadressaten anders behandelt wird, obwohl zwischen beiden Gruppen keine "
     "Unterschiede von solcher Art und solchem Gewicht bestehen, dass sie die ungleiche Behandlung rechtfertigen könnten.", P),
    ("[heute]Heute gilt ein stufenloser Maßstab, [band]vom bloßen Willkürverbot bis zu einer strengen Bindung an "
     "Verhältnismäßigkeitserfordernisse. [str1]Strenger wird es, je mehr eine Regel an Merkmale der Person anknüpft, die man "
     "kaum beeinflussen kann, [str2]je näher diese Merkmale denen aus Absatz drei kommen [str3]und je stärker die "
     "Ungleichbehandlung Freiheitsrechte trifft.", PS),
    # --- F Der Wohnort (2 BvR 470/08 Rn. 38–40) ----------------------------------------------------------------------
    ("[wohn]Und der Wohnort? [nicht]Einer Gemeinde ist es nicht von vornherein verwehrt, ihre Einwohner zu bevorzugen; "
     "[sachg]sie braucht aber Sachgründe. [allein]Der Wohnsitz allein ist kein solcher Grund. [untr]Tragen kann nur ein "
     "Grund, der mit dem Wohnort untrennbar zusammenhängt: [ziele]etwa knappe Mittel für die eigenen Aufgaben, ein Ausgleich "
     "für besondere Lasten der Einwohner, höherer Aufwand durch Auswärtige oder die Stärkung der örtlichen Gemeinschaft.", P),
    # --- G Der echte Fall (2 BvR 470/08 Rn. 2–4, 8, 35–37, 41–43, Tenor) -------------------------------------------
    ("[real]Im echten Fall verlangte ein Besucher aus Österreich die Differenz zurück; Amtsgericht und Oberlandesgericht "
     "gaben ihm nicht recht. [verk]Sie hatten verkannt, dass die Betreibergesellschaft unmittelbar an die Grundrechte "
     "gebunden ist. [touri]Und ein Sachgrund fehlte: Das Bad sollte gerade Auswärtige anziehen und Gewinn erzielen, nicht "
     "die örtliche Gemeinschaft fördern. [last]Ein Ausgleich für Lasten war nicht erkennbar, zumal die meisten Einwohner des "
     "Landkreises gar keinen Rabatt bekamen. [haush]Festgestellt war auch nicht, dass das Bad mit Haushaltsmitteln gebaut "
     "oder betrieben wurde.", P),
    ("[erg]Nach den bisherigen Feststellungen sah das Bundesverfassungsgericht Artikel drei Absatz eins verletzt, [aufh]hob "
     "die Urteile auf und verwies die Sache zurück. [martha]Für Martha heißt das: Ihr Mehrpreis ist nicht gerechtfertigt. "
     "[anders]Anders kann es liegen, wenn die Gemeinde mit dem Rabatt tatsächlich einen solchen Sachgrund verfolgt.", PS),
    # --- H Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bilde zuerst das Vergleichspaar und nenne den gemeinsamen Oberbegriff. [tipp2]Wer sofort mit der "
     "Rechtfertigung beginnt, weiß nicht, welche Ungleichbehandlung er eigentlich rechtfertigen muss. [tipp3]Lege danach "
     "den Maßstab fest, bevor du die Gründe abwägst.", PS),
    # --- I Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Ungleichbehandlung von wesentlich Gleichem, [k2]mit Vergleichsgruppen, "
     "gemeinsamem Oberbegriff und demselben Träger. [k3]Römisch zwei: Rechtfertigung, [k4]zuerst der Maßstab, vom "
     "Willkürverbot bis zur Verhältnismäßigkeit, [k5]dann der Sachgrund, bei strenger Prüfung mit Eignung, Erforderlichkeit "
     "und Angemessenheit. [k6]Römisch drei: Ergebnis.", PS),
    # --- J Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst vergleichen, dann rechtfertigen. [m2]Je mehr das Merkmal an die Person anknüpft und je stärker "
     "Freiheit betroffen ist, desto strenger die Prüfung. [m3]Der Wohnort allein rechtfertigt keinen Rabatt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
