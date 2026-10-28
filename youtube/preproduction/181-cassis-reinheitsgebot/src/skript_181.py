"""Folge 181 · Cassis de Dijon: Warum fremdes Bier trotz Reinheitsgebot rein darf (Mo · Der Fall · Klassiker-Fall;
Öffentliches Recht/Europarecht; Art. 34, 36 AEUV). Voraussetzung: Folge 176 (Prüfschema Art. 34 AEUV mit Dassonville) –
das Schema wird nicht wiederholt, nur verwiesen; vertieft werden Cassis de Dijon und das Reinheitsgebot-Urteil.
Echte Fälle sachlich nacherzählt: EuGH, Urt. v. 20.2.1979 – Rs. 120/78 (Rewe-Zentral, „Cassis de Dijon“), Rn. 2, 3, 8,
10–14; EuGH, Urt. v. 12.3.1987 – Rs. 178/84 (Kommission/Deutschland, Reinheitsgebot), Rn. 1, 5–7, 12, 24, 26, 28, 29,
32–37, 40, 42, 44, 47, 49, 53, 54, Tenor 1. Dazu EuGH, Urt. v. 17.6.1981 – Rs. 113/80 (Kommission/Irland) Rn. 7, 10, 11
(zwingende Erfordernisse nur bei unterschiedslos geltenden Regelungen), VO (EU) 2019/515 Erwägungsgrund 4 (Begriff
„gegenseitige Anerkennung“), § 1 Abs. 1, 2 BierV (heutige Rechtslage). Belege je Cue: ../RECHTSSTAND.md.
Einstieg (fiktiv, nach dem Plan-Hook): Herr Brodersen (Getränkehandel, Stimme christian) will ein in Belgien aus Gerstenmalz,
Reis und Mais gebrautes Bier verkaufen; Frau Timmermann (Lebensmittelüberwachung, Stimme lucy) meint, nach dem
Reinheitsgebot sei das kein Bier. Rewe-Zentral nur sachlich als Unternehmen, keine Figur, kein Logo.
DARSTELLUNG: Bier und Likör nur als neutrale Flaschen-/Fass-Icons ohne Marke, kein Trinken, kein Glas, keine Flaggen.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Brodersen,
Timmermann (nie im Genitiv). Lexi = Erzählerstimme (Carla).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Normen im Sprechtext als Wörter; „AEUV“ und „EuGH“ werden nicht als Abkürzung gesprochen."""

P, PS = 0.3, 0.5

STIMMEN = {"Brodersen": "christian", "Timmermann": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Getränkehandel ------------------------------------------------------------------------------------------
    ("[fall]Herr Brodersen betreibt einen Getränkehandel. [bel]Neu im Sortiment: ein Bier aus Belgien, [reis]gebraut aus "
     "Gerstenmalz, Reis und Mais. [timm]Frau Timmermann von der "
     "Lebensmittelüberwachung sieht sich die Flaschen an.", P),
    ("[t1]Mit Reis und Mais gebraut? Nach dem Reinheitsgebot ist das kein Bier. So dürfen Sie es nicht verkaufen.", P,
     "Timmermann"),
    ("[b1]In Belgien ist das ganz normales Bier. Warum soll es hier anders heißen?", P, "Brodersen"),
    ("[frage]Darf ein Staat den Namen Bier für Getränke reservieren, die nach seinen eigenen Regeln gebraut sind?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Einordnung: Verweis auf Folge 176 -------------------------------------------------------------------------------
    ("[verweis]Das Prüfschema für Artikel vierunddreißig kennst du aus dem Video zu Dassonville. [recht]Heute geht es um "
     "die Rechtfertigung, an zwei Klassikern: [zwei]Cassis de Dijon und dem Reinheitsgebot.", PS),
    # --- D Cassis de Dijon (Rs. 120/78) ----------------------------------------------------------------------------------
    ("[c79]Neunzehnhundertneunundsiebzig: [rewe]Das Handelsunternehmen Rewe-Zentral will einen Fruchtsaftlikör aus "
     "Frankreich einführen, den Cassis de Dijon. [monop]Die Bundesmonopolverwaltung für Branntwein winkt ab: in Deutschland "
     "nicht verkehrsfähig. [mind]Fruchtsaftliköre brauchen hier mindestens fünfundzwanzig Prozent Weingeist, [cgehalt]der "
     "Cassis hat nur fünfzehn bis zwanzig.", P),
    ("[unter]Die Regel gilt für alle Fruchtsaftliköre, ob aus Deutschland oder aus dem Ausland: eine unterschiedslos "
     "anwendbare Maßnahme. [behind]Trotzdem hält sie eingeführte Liköre vom deutschen Markt fern: eine Maßnahme gleicher "
     "Wirkung.", PS),
    ("[formel]Der Gerichtshof: Hemmnisse für den Binnenhandel der Gemeinschaft, die sich aus den Unterschieden "
     "der nationalen Regelungen über die Vermarktung dieser Erzeugnisse ergeben, müssen hingenommen werden, soweit diese "
     "Bestimmungen notwendig sind, um zwingenden Erfordernissen gerecht zu werden, [vier]insbesondere den Erfordernissen "
     "einer wirksamen steuerlichen Kontrolle, des Schutzes der öffentlichen Gesundheit, der Lauterkeit des Handelsverkehrs "
     "und des Verbraucherschutzes. [neben]Sie treten neben die Gründe aus Artikel sechsunddreißig.", PS),
    ("[gesund]Deutschland beruft sich auf die Gesundheit. [stich]Nicht stichhaltig: Es gibt ohnehin "
     "sehr viele Getränke mit geringem oder mittlerem Alkoholgehalt. [lauter]Dann auf den Schutz vor unlauterem Wettbewerb. "
     "[etik1]Auch das trägt nicht: Es genügt, die Angabe von Herkunft und Alkoholgehalt auf der Verpackung vorzuschreiben. "
     "[milder]Das Etikett ist das mildere Mittel.", PS),
    ("[anerk]Deshalb gibt es keinen stichhaltigen Grund dafür, zu verhindern, dass in einem Mitgliedstaat rechtmäßig hergestellte "
     "und in den Verkehr gebrachte alkoholische Getränke in die anderen Mitgliedstaaten eingeführt werden. [grundsatz]Diesen "
     "Gedanken nennt man heute den Grundsatz der gegenseitigen Anerkennung.", PS),
    # --- E Reinheitsgebot (Rs. 178/84) ----------------------------------------------------------------------------------
    ("[r87]Acht Jahre später geht es um das Bier. [klage]Die Kommission hat Deutschland wegen Vertragsverletzung verklagt. "
     "[par10]Nach Paragraf zehn des damaligen Biersteuergesetzes durfte nur ein Getränk Bier heißen, das dem Reinheitsgebot "
     "entspricht: [zutat]Für untergäriges Bier waren nur Gerstenmalz, Hopfen, Hefe und Wasser erlaubt, [kein]Reis und Mais "
     "galten nicht als Getreide. [zusatz]Dazu kam ein absolutes Verbot von Zusatzstoffen. [nurde]Die Brauvorschrift "
     "selbst galt nur für Brauereien in Deutschland, also keine Maßnahme gleicher Wirkung.", PS),
    ("[name]Zuerst der Name. [hemm]Das Bezeichnungsverbot kann die Einfuhr von Bier mit Reis oder Mais behindern. "
     "[vschutz]Deutschland beruft sich auf den Verbraucherschutz. [wandel]Der Gerichtshof: Die Vorstellungen der Verbraucher können sich fortentwickeln, [zement]und das Recht "
     "eines Mitgliedstaats darf nicht dazu dienen, die gegebenen Verbrauchsgewohnheiten zu zementieren. [gattung]In den "
     "anderen Mitgliedstaaten ist das Wort für Bier eine Gattungsbezeichnung, auch wenn neben Gerstenmalz Reis oder Mais "
     "verwendet wird.", P),
    ("[etik2]Das mildere Mittel ist wieder das Etikett: Mit der Angabe der verwendeten Grundstoffe kann der Verbraucher "
     "seine Wahl in Kenntnis aller Umstände treffen. [negativ]Nur darf diese Kennzeichnung kein negatives Bild von anders gebrautem Bier erzeugen. [v1]Das "
     "Bezeichnungsverbot verstößt also gegen die Warenverkehrsfreiheit.", PS),
    ("[zus]Dann die Zusatzstoffe. [a36]Hier zählt der Gesundheitsschutz nach Artikel sechsunddreißig. "
     "[zulass]Die Staaten dürfen Zusatzstoffe grundsätzlich von einer Zulassung abhängig machen, [erf]aber nur so weit, wie "
     "es für den Gesundheitsschutz tatsächlich erforderlich ist. [muss]Einen Zusatzstoff, der in einem anderen Mitgliedstaat "
     "zugelassen ist, muss der Einfuhrstaat zulassen, wenn er die Gesundheit nicht gefährdet und einem echten Bedürfnis "
     "entspricht. [pausch]Das deutsche Verbot schloss "
     "aber alle Zusatzstoffe pauschal aus, [verf]ohne ein Verfahren für die Zulassung. [v2]Das Verbot ist unverhältnismäßig und durch Artikel "
     "sechsunddreißig nicht gedeckt.", PS),
    ("[tenor]Ergebnis: Deutschland hat gegen den freien Warenverkehr verstoßen. [bierv]Heute regelt das "
     "die Bierverordnung: Im Ausland hergestellte Getränke dürfen als Bier verkauft werden, wenn sie im Herstellungsland so "
     "verkehrsfähig sind. [inl]Für in Deutschland hergestellte Getränke bleibt es dagegen grundsätzlich beim Reinheitsgebot. "
     "[ilnd]Man spricht von Inländerdiskriminierung.", PS),
    # --- F Lösung --------------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Herrn Brodersen. [l1]Ein Verbot, sein Getränk Bier zu nennen, gilt unterschiedslos, behindert aber die "
     "Einfuhr. [l2]Verbraucherschutz ist ein zwingendes Erfordernis, [l3]doch ein Etikett mit Gerstenmalz, Reis und Mais "
     "informiert genauso gut. [l4]Das Verbot wäre unverhältnismäßig: [l5]Herr Brodersen darf sein belgisches Bier als Bier "
     "verkaufen.", P),
    ("[t2]Gut, dann darf es auch hier Bier heißen.", PS, "Timmermann"),
    # --- G Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Zwingende Erfordernisse greifen nach der klassischen Rechtsprechung nur bei unterschiedslos "
     "anwendbaren Maßnahmen. [disk]Trifft eine Regel nur eingeführte Waren, bleibt allein Artikel sechsunddreißig, [eng]und "
     "dessen Gründe sind abschließend und eng auszulegen.", PS),
    # --- H Schema der Rechtfertigung --------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Rechtfertigung. [s1]Römisch eins: Rechtfertigungsgrund, [s1a]Artikel sechsunddreißig "
     "[s1b]oder ein zwingendes Erfordernis, nur bei unterschiedslosen Maßnahmen. [s2]Römisch zwei: Verhältnismäßigkeit. "
     "[s2a]Das Mittel muss geeignet sein, [s2b]und von mehreren geeigneten Mitteln wählt der Staat das, das den Handel am "
     "wenigsten behindert, etwa ein Etikett statt eines Verbots.", PS),
    # --- I Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Unterschiedslos anwendbare Regeln können durch zwingende Erfordernisse gerechtfertigt sein, aber nur, "
     "soweit sie notwendig sind. [m2]Reicht ein Etikett, darf, was in einem Mitgliedstaat rechtmäßig hergestellt und "
     "verkauft wird, auch in den anderen verkauft werden.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
