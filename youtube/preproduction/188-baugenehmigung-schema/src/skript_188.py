"""Folge 188 · Baugenehmigung Schema: Bauplanungs- und Bauordnungsrecht (Mi · Examenswissen · Baurecht, Format Schema).
Beispielfall nach dem Plan-Hook („Deine Garage erfüllt jeden Brandschutz – steht aber mitten im Außenbereich.“):
Herr Hasenkamp (um 55) will auf seiner Wiese weit draußen vor dem Dorf, ringsum nur Felder, eine Betongarage mit 40 m² für
seine zwei Oldtimer bauen und stellt einen Bauantrag. Kein Bebauungsplan, kein Bebauungszusammenhang; der
Flächennutzungsplan stellt Fläche für die Landwirtschaft dar. Frau Ortmann (um 35) von der Bauaufsichtsbehörde lehnt ab.
Aufbau (Schema): Fall → Sachverhalt → Anspruch (Wortlautkarte Art. 68 Abs. 1 S. 1 BayBO, § 74 Abs. 1 S. 1 BauO NRW 2018) →
Länder-Overlay (Tabelle BY/NRW) → Kompetenz (Art. 74 Abs. 1 Nr. 18, Art. 70 Abs. 1 GG) → I. Genehmigungsbedürftigkeit
(Art. 55 Abs. 1 BayBO / § 60 Abs. 1 BauO NRW 2018; verfahrensfrei/Freistellung) → II. Bauantrag (unterstellt) →
III. 1. Verfahrensart, Prüfprogramm (Art. 59 BayBO / § 64 BauO NRW 2018; Brandschutz) → 2. Bauplanungsrecht (Wortlautkarte
§ 29 Abs. 1 BauGB; Weiche §§ 30, 34, 35; § 35 nur Ergebnis, Verweis 085) → 3. Bauordnungsrecht → Ergebnis → Schema →
Klausurtipp (Lexi; Verpflichtungsklage, Verweis 081) → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Hasenkamp, Ortmann (nie im Genitiv).
Stimmen (Pool stephan, hilde, christian, lucy): Herr Hasenkamp christian (Mann, mittel), Frau Ortmann lucy (Frau, jung).
stephan und hilde nicht verwendet (keine Stephan/Christian-Paarung). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter (keine Abkürzungen wie BauGB/BayBO)."""

P, PS = 0.3, 0.5

STIMMEN = {"Hasenkamp": "christian", "Ortmann": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Wiese vor dem Dorf -----------------------------------------------------------------------------------
    ("[fall]Herr Hasenkamp besitzt eine Wiese weit draußen vor dem Dorf, ringsum nur Felder. [plan]Dort will er eine Garage "
     "für seine zwei Oldtimer bauen, vierzig Quadratmeter, aus Beton. [antrag]Er stellt einen Bauantrag.", P),
    ("[ha1]Die Garage erfüllt jeden Brandschutz und hält alle Abstände ein. Was soll da schiefgehen?", P, "Hasenkamp"),
    # --- A2 Fall: bei der Bauaufsichtsbehörde ------------------------------------------------------------------------------
    ("[amt]Frau Ortmann von der Bauaufsichtsbehörde prüft den Antrag. [kbpl]Für die Wiese gilt kein Bebauungsplan, "
     "[fnp]und der Flächennutzungsplan stellt sie als Fläche für die Landwirtschaft dar.", P),
    ("[or1]Ihre Garage mag sicher sein. Aber sie steht im Außenbereich. Ich lehne den Antrag ab.", P, "Ortmann"),
    ("[frage]Hat Herr Hasenkamp einen Anspruch auf die Baugenehmigung? [frage2]Die Antwort liegt auf zwei Ebenen: "
     "Bauplanungsrecht und Bauordnungsrecht.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruchsgrundlage: Art. 68 Abs. 1 S. 1 BayBO, § 74 Abs. 1 S. 1 BauO NRW 2018 -------------------------------------
    ("[anspr]Die Anspruchsgrundlage steht in der Landesbauordnung, hier am Beispiel Bayern und Nordrhein-Westfalen. "
     "[by68]Artikel achtundsechzig Absatz eins Satz eins der Bayerischen Bauordnung: Die Baugenehmigung ist zu erteilen, "
     "wenn dem Bauvorhaben keine öffentlich-rechtlichen Vorschriften entgegenstehen, die im bauaufsichtlichen "
     "Genehmigungsverfahren zu prüfen sind. [nrw74]Paragraf vierundsiebzig Absatz eins der Landesbauordnung "
     "Nordrhein-Westfalen sagt es ohne diesen Zusatz. [gebunden]„Ist zu erteilen“ heißt: eine gebundene Entscheidung. "
     "[anspr2]Steht nichts entgegen, hat Herr Hasenkamp einen Anspruch.", P),
    # --- D Länder-Overlay -------------------------------------------------------------------------------------------------
    ("[tab]Die Nummern unterscheiden sich, das Prinzip nicht. [tab1]Die Genehmigungspflicht steht in Bayern "
     "in Artikel fünfundfünfzig, in Nordrhein-Westfalen in Paragraf sechzig, [tab2]das vereinfachte Verfahren in Artikel "
     "neunundfünfzig und Paragraf vierundsechzig, [tab3]der Anspruch in Artikel achtundsechzig und Paragraf vierundsiebzig. "
     "[eigen]Andere Länder regeln es ähnlich; schlag die Nummern in deiner Landesbauordnung nach.", PS),
    # --- E Kompetenz: Art. 74 Abs. 1 Nr. 18, Art. 70 Abs. 1 GG -----------------------------------------------------------
    ("[komp]Warum zwei Ebenen? Wegen der Gesetzgebungskompetenz. [gg74]Artikel vierundsiebzig Absatz eins Nummer achtzehn "
     "Grundgesetz: Die konkurrierende Gesetzgebung erstreckt sich auf das Bodenrecht. [bodenr]Dazu gehört das "
     "Bauplanungsrecht im Baugesetzbuch: Darf an diesem Ort so gebaut werden? [gg70]Für das Bauordnungsrecht hat der Bund "
     "keine Kompetenz; es bleibt nach Artikel siebzig bei den Ländern. [ordn]Die Landesbauordnungen regeln vor allem die "
     "Gefahrenabwehr am Bau und das Genehmigungsverfahren.", PS),
    # --- F I. Genehmigungsbedürftigkeit, II. Bauantrag ----------------------------------------------------------------------
    ("[gb]Römisch eins: Braucht die Garage überhaupt eine Genehmigung? [by55]Nach Artikel fünfundfünfzig Absatz eins "
     "bedürfen die Errichtung, Änderung und Nutzungsänderung von Anlagen der Baugenehmigung, soweit keine Ausnahme greift. "
     "[nrw60]Paragraf sechzig in Nordrhein-Westfalen nennt auch die Beseitigung. [frei]Verfahrensfrei "
     "sind kleine Garagen bis fünfzig Quadratmeter, mit weiteren Maßgaben je Land, [ausser]aber nicht im Außenbereich. "
     "[freist]Die Genehmigungsfreistellung setzt einen qualifizierten oder vorhabenbezogenen Bebauungsplan voraus; den gibt "
     "es hier nicht. [pflicht]Die Garage ist genehmigungspflichtig. [ba]Römisch zwei: Den Bauantrag hat Herr Hasenkamp "
     "ordnungsgemäß gestellt; das unterstellen wir.", PS),
    # --- G III. 1. Verfahrensart und Prüfprogramm --------------------------------------------------------------------------
    ("[gf]Römisch drei: Genehmigungsfähigkeit. [verf]Erstens: Welches Verfahren gilt? [sonder]Die Garage ist kein "
     "Sonderbau, [verein]also gilt das vereinfachte Baugenehmigungsverfahren. [prog]Es legt fest, was die Behörde prüft: "
     "[p1]das Bauplanungsrecht, Paragrafen neunundzwanzig bis achtunddreißig Baugesetzbuch, [p2]die Abstandsflächen und "
     "örtliche Bauvorschriften, [p3]beantragte Abweichungen [p4]und bestimmte andere öffentlich-rechtliche Vorschriften. "
     "[brand]Den Brandschutz prüft die Behörde hier grundsätzlich nicht mit. [trotz]Einhalten muss Herr Hasenkamp ihn "
     "trotzdem.", PS),
    # --- H III. 2. Bauplanungsrecht ----------------------------------------------------------------------------------------
    ("[bpl]Zweitens, das Herzstück: das Bauplanungsrecht. [p29]Paragraf neunundzwanzig Absatz eins Baugesetzbuch: Für "
     "Vorhaben, die die Errichtung, Änderung oder Nutzungsänderung von baulichen Anlagen zum Inhalt haben, gelten die "
     "Paragrafen dreißig bis siebenunddreißig. [vorh]Die Garage ist eine bauliche Anlage, ihr Bau ein Vorhaben. "
     "[weiche]Jetzt kommt die Weiche. [w30]Gilt ein Bebauungsplan, Paragraf dreißig? Nein. [w34]Liegt die Wiese in einem "
     "im Zusammenhang bebauten Ortsteil, Paragraf vierunddreißig? Nein, ringsum sind nur Felder. [w35]Also Außenbereich, "
     "Paragraf fünfunddreißig.", P),
    ("[l35]Die Garage dient keinem landwirtschaftlichen Betrieb und ist auch sonst nicht privilegiert: [sonst]ein sonstiges "
     "Vorhaben nach Absatz zwei. [belang]Sie widerspricht dem Flächennutzungsplan und beeinträchtigt die natürliche "
     "Eigenart der Landschaft, Absatz drei Nummer eins und fünf. [verw85]Die Einzelheiten zeigt das Video zum "
     "Außenbereich. [unzul]Ergebnis: bauplanungsrechtlich unzulässig.", PS),
    # --- I III. 3. Bauordnungsrecht, Ergebnis ------------------------------------------------------------------------------
    ("[bo]Drittens: Bauordnungsrecht. [abst]Die Abstandsflächen hält die Garage ein. [hilft]Das hilft ihr aber nicht. "
     "[steht]Dem Vorhaben steht Paragraf fünfunddreißig entgegen, eine Vorschrift, die die Behörde prüfen muss. "
     "[erg]Herr Hasenkamp hat keinen Anspruch; die Ablehnung war rechtmäßig.", P),
    ("[ha2]Dann hilft mir der beste Brandschutz nichts, wenn der Ort nicht passt.", PS, "Hasenkamp"),
    # --- J Schema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Anspruch auf Baugenehmigung. [s0]Anspruchsgrundlage: die Landesbauordnung. [s1]Römisch eins: Genehmigungsbedürftigkeit, also keine "
     "Verfahrensfreiheit und keine Freistellung. [s2]Römisch zwei: ordnungsgemäßer Bauantrag. [s3]Römisch drei: "
     "Genehmigungsfähigkeit. [s3a]Erstens: Verfahrensart und Prüfprogramm. [s3b]Zweitens: Bauplanungsrecht, Paragrafen "
     "neunundzwanzig bis achtunddreißig. [s3c]Drittens: Bauordnungsrecht, soweit es geprüft wird. [s3d]Viertens: andere "
     "öffentlich-rechtliche Vorschriften im Prüfprogramm. [s4]Römisch vier: Ergebnis.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme zuerst die Verfahrensart. [k1]Daraus folgt das Prüfprogramm, also was die Behörde "
     "überhaupt prüfen muss. [k2]Das Bauplanungsrecht gehört in jedem Baugenehmigungsverfahren dazu. [k3]Seinen Anspruch "
     "verfolgt Herr Hasenkamp mit der Verpflichtungsklage; den Aufbau zeigt das Video zu Zulässigkeit und Begründetheit.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Das Bauplanungsrecht fragt, ob an diesem Ort gebaut werden darf, [m2]das Bauordnungsrecht vor allem, "
     "wie sicher gebaut wird. [m3]Die Baugenehmigung gibt es nur, wenn keine zu prüfende Vorschrift entgegensteht. "
     "[m4]Der falsche Ort genügt schon für die Ablehnung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
