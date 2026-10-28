"""Folge 223 · Mittellose Ehefrau bürgt: Ist die Angehörigenbürgschaft sittenwidrig? (Mo · Der Fall · Weitere
Vertragstypen · Klassiker-Fall). Fiktiver Fall nach dem Plan-Hook: Tischlermeister Gero braucht für seine Werkstatt einen
Firmenkredit über 200.000 € (Zinsen 1.000 € im Monat); Herr Wittkamp von der Bank verlangt die Bürgschaft seiner Frau
Anneke, die kein eigenes Einkommen und kein Vermögen hat. Drei Jahre später sind 180.000 € offen.
Aufbau: Anspruch aus § 765 Abs. 1 (Wortlautkarte), Form § 766 S. 1 gewahrt; Bürgschaftsbeschluss BVerfGE 89, 214
(Art. 2 Abs. 1 GG als Wortlautkarte; S. 231, 232, 234); § 138 Abs. 1 (Wortlautkarte) mit den BGH-Kriterien
(XI ZR 82/11 Rn. 9; XI ZR 32/16 Rn. 20); Subsumtion (XI ZR 32/16 Rn. 29 f.); Ergebnis nichtig; Gegenfall eigenes Interesse
(XI ZR 32/16 Rn. 29; BVerfGE 89, 214, 235 f.); Klausurtipp und Merksatz mit Lexi.
Figuren: Anneke (julia), Gero (niklas), Herr Wittkamp (helmut); Erzählerin und Lexi: Carla ohne Rolle.
DARSTELLUNG: keine echte Bank, kein Logo; Anneke sachlich und selbstbestimmt, Gero ohne Klischee, die Bank sachlich.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen, Artikel und Paragrafen im Sprechtext als Wörter; „BVerfG“/„GG“ ausgeschrieben (synth_el buchstabiert Abkürzungen).
Kein Genitiv der Namen. Belege: ../RECHTSSTAND.md.
Nach der ersten Vertonung Segment 2 umformuliert („… wenn Ihre Frau dafür bürgt.“ → „… eine Bürgschaft übernimmt.“), weil
whisper small und medium „bürgt“ übereinstimmend als „birgt“ hörten; einmalig nachvertont."""

P, PS = 0.3, 0.5

STIMMEN = {"Anneke": "julia", "Gero": "niklas", "Wittkamp": "helmut"}

SEGMENTE = [
    # --- A1 Fall: die Werkstatt -------------------------------------------------------------------------------------
    ("[fall]Gero ist Tischlermeister und hat eine eigene Werkstatt. [kredit]Für neue Maschinen braucht er von der Bank "
     "einen Firmenkredit über zweihunderttausend Euro, [zins]die Zinsen betragen tausend Euro im Monat. [bank]Herr "
     "Wittkamp von der Bank sagt:", 0.3),
    ("[wi1]Den Kredit gibt es nur, wenn Ihre Frau eine Bürgschaft übernimmt.", P, "Wittkamp"),
    ("[anneke]Anneke ist seit acht Jahren mit Gero verheiratet. [mittel]Sie hat kein eigenes Einkommen und kein "
     "Vermögen, und das wird absehbar so bleiben.", 0.25),
    ("[ge1]Anneke, ohne deine Bürgschaft bekomme ich den Kredit nicht.", 0.25, "Gero"),
    ("[an1]Wenn es für die Werkstatt sein muss, unterschreibe ich.", P, "Anneke"),
    ("[urk]Sie unterschreibt eigenhändig die Urkunde: Ich bürge für den Firmenkredit von Gero über zweihunderttausend "
     "Euro. [nimmt]Herr Wittkamp nimmt die Erklärung an.", P),
    # --- A2 Fall: drei Jahre später, die Frage --------------------------------------------------------------------------
    ("[spaet]Drei Jahre später bleiben die Aufträge aus, Gero kann die Raten nicht mehr zahlen. [kuend]Die Bank kündigt "
     "den Kredit, hundertachtzigtausend Euro sind offen. [brief]Herr Wittkamp wendet sich an Anneke.", 0.25),
    ("[wi2]Sie haben gebürgt. Bitte zahlen Sie die hundertachtzigtausend Euro.", 0.25, "Wittkamp"),
    ("[an2]Davon kann ich nicht einmal die Zinsen bezahlen.", P, "Anneke"),
    ("[frage]Muss Anneke zahlen? [frage2]Oder ist ihre Bürgschaft sittenwidrig und nichtig?", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Anspruch aus § 765 Abs. 1 (Wortlaut), Einigung, Form § 766 S. 1, Hauptschuld --------------------------------
    ("[agl]Die Bank könnte gegen Anneke einen Anspruch aus Paragraf siebenhundertfünfundsechzig Absatz eins haben. "
     "[w765]Danach verpflichtet sich die bürgende Person gegenüber dem Gläubiger eines Dritten, für dessen "
     "Verbindlichkeit einzustehen. [einig]Anneke und die Bank haben sich geeinigt. [form]Auch die Form nach Paragraf "
     "siebenhundertsechsundsechzig Satz eins ist gewahrt: Anneke hat die Erklärung schriftlich erteilt und eigenhändig "
     "unterschrieben. [haupt]Die Hauptschuld von Gero besteht ebenfalls. [problem]Das Problem liegt woanders: Ist die "
     "Bürgschaft nach Paragraf hundertachtunddreißig Absatz eins nichtig?", PS),
    # --- D Bürgschaftsbeschluss: BVerfGE 89, 214 (Art. 2 Abs. 1 GG als Wortlautkarte) ---------------------------------
    ("[bverfg]Den Weg hat das Bundesverfassungsgericht neunzehnhundertdreiundneunzig im Bürgschaftsbeschluss gewiesen. "
     "[tochter]Dort hatte eine einundzwanzigjährige Tochter ohne Berufsausbildung für die Geschäftskredite ihres Vaters "
     "gebürgt, bis zu hunderttausend Mark. [art2]Artikel zwei Absatz eins Grundgesetz schützt die freie Entfaltung der "
     "Persönlichkeit [privat]und damit die Privatautonomie, also die Selbstbestimmung im Rechtsleben. [fremd]Hat aber "
     "eine Seite ein so starkes Übergewicht, dass sie den Vertragsinhalt faktisch allein bestimmt, ist die andere Seite "
     "fremdbestimmt.", P),
    ("[korr]Ist ein Vertrag für eine Seite ungewöhnlich belastend und die Folge strukturell ungleicher "
     "Verhandlungsstärke, müssen die Zivilgerichte korrigierend eingreifen, [gk]und zwar über die Generalklauseln der "
     "Paragrafen hundertachtunddreißig und zweihundertzweiundvierzig. [vvv]Der Satz: Vertrag ist Vertrag, reicht dann "
     "nicht.", PS),
    # --- E § 138 Abs. 1 (Wortlaut) und die Kriterien des BGH ---------------------------------------------------------
    ("[w138]Paragraf hundertachtunddreißig Absatz eins lautet: Ein Rechtsgeschäft, das gegen die guten Sitten verstößt, "
     "ist nichtig. [bgh]Für Bürgschaften naher Angehöriger hat der Bundesgerichtshof daraus feste Kriterien entwickelt. "
     "[krass]Erstens: krasse finanzielle Überforderung. Sie liegt grundsätzlich vor, wenn die bürgende Person "
     "voraussichtlich nicht einmal die laufenden Zinsen aus dem pfändbaren Teil ihres Einkommens und Vermögens dauerhaft "
     "tragen kann. [nahe]Zweitens: Sie steht dem Hauptschuldner persönlich besonders nahe, etwa als Ehegatte.", P),
    ("[verm]Dann wird vermutet, dass sie allein aus emotionaler Verbundenheit gebürgt und die Bank das in sittlich "
     "anstößiger Weise ausgenutzt hat. [widerl]Diese Vermutung kann die Bank widerlegen, sie muss dazu aber selbst "
     "vortragen und beweisen.", PS),
    # --- F Subsumtion ---------------------------------------------------------------------------------------------
    ("[sub]Jetzt zum Fall. [kein]Anneke hat weder Einkommen noch Vermögen, pfändbar ist nichts. [zins2]Schon die Zinsen "
     "von tausend Euro im Monat kann sie nicht tragen. Sie ist also krass überfordert. [ehe]Als Ehefrau steht sie Gero "
     "persönlich besonders nahe. [eigen]Ein eigenes Interesse am Kredit hat sie nicht, die Werkstatt gehört Gero allein. "
     "[mittelb]Dass es der Familie besser geht, wenn die Werkstatt läuft, ist nur ein mittelbarer Vorteil. [nichts]Und "
     "Umstände, die die Vermutung widerlegen, sind nicht ersichtlich.", PS),
    # --- G Ergebnis -------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Die Bürgschaft ist sittenwidrig und nach Paragraf hundertachtunddreißig Absatz eins nichtig. "
     "[erg2]Anneke muss der Bank nichts zahlen.", PS),
    # --- H Gegenfall: eigenes Interesse ------------------------------------------------------------------------------
    ("[gegen]Anders liegt es, wenn die bürgende Person ein eigenes Interesse am Kredit hat, etwa weil ihr das "
     "finanzierte Objekt zur Hälfte gehört. Dann ist die Vermutung widerlegt. [bf2]Auch im Bürgschaftsbeschluss "
     "scheiterte eine Ehefrau ohne Einkommen mit ihrer Verfassungsbeschwerde: Sie hatte für einen Konsumkredit ihres "
     "Mannes in üblicher Höhe gebürgt, und man durfte annehmen, dass sie selbst an diesem Kredit interessiert war.", PS),
    # --- I Klausurtipp (Lexi) --------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Sittenwidrigkeit beim Bürgschaftsvertrag, also beim Entstehen des Anspruchs. "
     "[tipp2]Maßgeblich ist die Prognose bei Abgabe der Bürgschaftserklärung, nicht erst die spätere Pleite. "
     "[tipp3]Und trenne sauber: Die Überforderung rechnest du am Sachverhalt nach, die Ausnutzung wird vermutet.", PS),
    # --- J Klausurschema --------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: [k1]Römisch eins: Anspruch entstanden, [k1a]mit Bürgschaftsvertrag und Form, "
     "[k1b]aber keine Nichtigkeit nach Paragraf hundertachtunddreißig Absatz eins: [k1c]krasse finanzielle "
     "Überforderung, [k1d]besondere persönliche Nähe [k1e]und Vermutung nicht widerlegt. [k1f]Dazu die Hauptschuld. "
     "[k2]Römisch zwei: nicht erloschen. [k3]Römisch drei: durchsetzbar.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Kann eine nahestehende Person nicht einmal die Zinsen tragen, [m2]ist ihre Bürgschaft in der Regel "
     "sittenwidrig, [m3]es sei denn, die Bank widerlegt die Vermutung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
