"""Folge 173 · GbR nach MoPeG: Rechtsfähig, eingetragen, haftend (§§ 705 ff. BGB) (Mi · Examenswissen · Zivilrecht/
Gesellschaftsrecht, Format Schema). Beispielfall nach dem Plan-Hook („Drei Freunde gründen eine Band und kaufen gemeinsam eine
Musikanlage auf Rechnung“): Bente (Gitarre), Gerrit (Schlagzeug) und Ingo (Bass) gründen per Handschlag eine Band, jeder zahlt
50 € im Monat in die Bandkasse. Zu dritt kaufen und unterschreiben sie im Musikgeschäft von Frau Bornemann für die Band eine
Anlage für 3.600 €, zahlbar in 14 Tagen; sie wird geliefert. Die Bandkasse reicht nicht; Frau Bornemann verlangt alles von Ingo.
Prüfung: Aufbau → § 705 Abs. 1 (Wortlautkarte, vorgelesen; formfrei, Zweck, Förderung) → § 705 Abs. 2 (Wortlautkarte),
nicht rechtsfähige Gesellschaft, § 705 Abs. 3 (Wortlautkarte, Vermutung), § 719 Abs. 1 → § 707 Abs. 1 (Wortlautkarte),
freiwillig, § 707a Abs. 2 (eGbR), § 47 Abs. 2 GBO → § 713 (Wortlautkarte), ARGE Weißes Roß (BGH II ZR 331/00), Gesamthand
aufgegeben → § 720 Abs. 1 (Wortlautkarte), Abs. 2, Vollmacht, § 715 → § 721 (Wortlautkarte), Verweis Folge 120, § 721a,
§ 721b → Lösung → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Bente, Gerrit, Ingo,
Bornemann (nie im Genitiv). Stimmen: Bente lucy, Gerrit stephan, Ingo christian (stephan und christian nie Dialogpartner in
derselben Szene: Ingo spricht nur in der Szene „Zwei Wochen später“, in der Gerrit nicht spricht), Frau Bornemann hilde.
Lexi = Erzählerin Carla.
Sprechtext: „G.b.R.“ und „e.G.b.R.“ mit Punkten, damit die Buchstaben einzeln gesprochen werden (synth_el kennt die Abkürzung
nicht; dieselbe Technik wie dort für BGB); „Mopeg“ als Wort (Tafeln: „MoPeG“), „Arge“ als Wort (Tafeln: „ARGE“). Untertitel
führen die Schreibung zurück (meta_173.py).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Bente": "lucy", "Gerrit": "stephan", "Ingo": "christian", "Bornemann": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Proberaum -------------------------------------------------------------------------------------------
    ("[fall]Bente, Gerrit und Ingo machen seit der Schulzeit zusammen Musik: [proben]Gitarre, Schlagzeug und Bass.", P),
    ("[b1]Ab heute sind wir eine echte Band. Abgemacht?", P, "Bente"),
    ("[g1]Abgemacht! Jeder zahlt fünfzig Euro im Monat in die Bandkasse.", P, "Gerrit"),
    # --- A2 Fall: im Musikgeschäft ----------------------------------------------------------------------------------------
    ("[laden]Zu dritt gehen sie in ein Musikgeschäft. [bor]Die Inhaberin, Frau Bornemann, zeigt ihnen eine Anlage für "
     "dreitausendsechshundert Euro.", P),
    ("[fb1]Auf wen schreibe ich die Rechnung?", P, "Bornemann"),
    ("[b2]Auf unsere Band. Wir kaufen sie zusammen.", P, "Bente"),
    ("[unter]Alle drei unterschreiben den Kaufvertrag für die Band. [liefer]Die Anlage wird geliefert, die Rechnung ist in "
     "vierzehn Tagen fällig.", P),
    # --- A3 Fall: zwei Wochen später --------------------------------------------------------------------------------------
    ("[spaet]Doch die Bandkasse reicht nicht. [ingo]Frau Bornemann wendet sich an Ingo.", P),
    ("[fb2]Bitte zahlen Sie die dreitausendsechshundert Euro.", P, "Bornemann"),
    ("[i1]Ich allein? Die Anlage hat doch die Band gekauft!", P, "Ingo"),
    ("[frage]Wer ist hier Vertragspartner? [frage2]Und muss Ingo wirklich die ganze Summe zahlen?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau ------------------------------------------------------------------------------------------------------------
    ("[aufbau]Seit dem ersten Januar zweitausendvierundzwanzig regelt das Mopeg die Gesellschaft bürgerlichen Rechts, kurz "
     "G.b.R., neu. [a1]Wir prüfen in drei Schritten: [a2]Ist die Band eine rechtsfähige G.b.R.? [a3]Wurde sie wirksam "
     "vertreten? [a4]Und haften die Bandmitglieder persönlich?", PS),
    # --- D § 705 Abs. 1: Entstehung --------------------------------------------------------------------------------------
    ("[p1]Zuerst die Entstehung. Nach Paragraf siebenhundertfünf Absatz eins braucht es einen Gesellschaftsvertrag, in "
     "dem sich die Gesellschafter verpflichten, einen gemeinsamen Zweck zu fördern. [form]Eine besondere Form ist "
     "grundsätzlich nicht nötig; ein Handschlag genügt. [zweck]Der gemeinsame Zweck: zusammen Musik machen. [foerd]Gefördert wird er durch Proben und die "
     "fünfzig Euro im Monat. [p1fall]Die drei haben also eine G.b.R. gegründet.", P),
    # --- E § 705 Abs. 2, 3; § 719: rechtsfähig? ---------------------------------------------------------------------------
    ("[p2]Aber ist sie auch rechtsfähig? [p2a]Nach Absatz zwei kann die Gesellschaft selbst Rechte erwerben und "
     "Verbindlichkeiten eingehen, wenn sie nach dem gemeinsamen Willen der Gesellschafter am Rechtsverkehr teilnehmen soll. "
     "[innen]Sonst ist sie nicht rechtsfähig und regelt nur das Verhältnis der Gesellschafter untereinander. [p3]Absatz drei "
     "vermutet diesen Willen, wenn die Gesellschaft ein Unternehmen unter gemeinsamem Namen betreibt. [p2fall]Darauf kommt "
     "es hier nicht an: Alle drei wollen ausdrücklich als Band einkaufen. "
     "[p719]Nach Paragraf siebenhundertneunzehn entsteht sie gegenüber Dritten, sobald sie mit Zustimmung aller am "
     "Rechtsverkehr teilnimmt, hier mit dem Kauf.", P),
    # --- F § 707 Abs. 1: Eintragung, eGbR, § 47 Abs. 2 GBO ----------------------------------------------------------------
    ("[eintr]Muss die Band dafür ins Register? [p707]Nach Paragraf siebenhundertsieben Absatz eins können die Gesellschafter "
     "sie beim Gericht zur Eintragung in das Gesellschaftsregister anmelden. [kann]Sie können, müssen aber nicht; die Rechtsfähigkeit hängt nicht an der Eintragung. [egbr]Eingetragen "
     "führt sie den Zusatz e.G.b.R. [gbo]Fürs Grundbuch "
     "ist die Eintragung aber Voraussetzung: Nach Paragraf siebenundvierzig Absatz zwei Grundbuchordnung soll ein Recht für eine "
     "G.b.R. nur eingetragen werden, wenn sie im Gesellschaftsregister steht. [haus]Für ein eigenes Grundstück müsste sich die "
     "Band also erst eintragen lassen.", P),
    # --- G § 713: Gesellschaftsvermögen ---------------------------------------------------------------------------------
    ("[verm]Wem gehört nun die Anlage? [p713]Nach Paragraf siebenhundertdreizehn sind die Beiträge, die für die "
     "Gesellschaft erworbenen Rechte und die gegen sie begründeten Verbindlichkeiten Vermögen der Gesellschaft. [anl2]Die Anlage gehört also der G.b.R. selbst, ebenso das Geld in der Bandkasse. [schuld]Auch die "
     "Kaufpreisschuld ist eine Verbindlichkeit der Gesellschaft. [arge]Den Weg hatte der Bundesgerichtshof "
     "zweitausendeins geebnet, im Fall Arge Weißes Ross: Die Außengesellschaft ist rechtsfähig, soweit sie am Rechtsverkehr "
     "teilnimmt. [mopeg]Das Mopeg hat die alte Gesamthand aufgegeben.", P),
    # --- H § 720 Abs. 1: Vertretung, § 715 ------------------------------------------------------------------------------
    ("[vertr]Wer handelt für die Band? [p720]Paragraf siebenhundertzwanzig Absatz eins: Zur Vertretung der Gesellschaft sind "
     "alle Gesellschafter gemeinsam befugt, es sei denn, der Gesellschaftsvertrag bestimmt etwas anderes. [vfall]Alle drei "
     "haben gemeinsam für die Band unterschrieben: Sie ist wirksam vertreten. [allein]Hätte Bente allein "
     "bestellt, bräuchte sie Einzelvertretungsmacht oder eine Vollmacht. "
     "[gf]Davon zu trennen ist die Geschäftsführung nach Paragraf siebenhundertfünfzehn, also wer intern entscheiden darf.", P),
    # --- I § 721: Haftung, § 721a, § 721b --------------------------------------------------------------------------------
    ("[haft]Und Ingo? [p721]Paragraf siebenhunderteinundzwanzig: Die Gesellschafter haften für die Verbindlichkeiten der "
     "Gesellschaft den Gläubigern als Gesamtschuldner persönlich. Eine entgegenstehende Vereinbarung ist Dritten gegenüber "
     "unwirksam. [pers]Persönlich heißt: auch mit dem Privatvermögen. [gesamt]Als Gesamtschuldner schuldet jeder die ganze "
     "Summe, die Gläubigerin bekommt sie aber nur einmal. [v120]Mehr dazu im Video zur Gesamtschuld. "
     "[p721a]Wer später eintritt, haftet nach Paragraf siebenhunderteinundzwanzig a auch für Altschulden. "
     "[p721b]Und nach Paragraf siebenhunderteinundzwanzig b kann Ingo einwenden, was auch die Gesellschaft einwenden könnte, "
     "etwa dass schon bezahlt ist.", P),
    # --- J Lösung ------------------------------------------------------------------------------------------------------------
    ("[loes]Zur Lösung. [l1]Die Band ist eine rechtsfähige G.b.R. [l2]Durch die gemeinsame Unterschrift ist sie selbst "
     "Käuferin geworden [l3]und schuldet Frau Bornemann nach Paragraf vierhundertdreiunddreißig Absatz zwei "
     "dreitausendsechshundert Euro. [l4]Daneben haften alle drei persönlich, auch Ingo. "
     "[l5]Frau Bornemann kann also von der Band und von jedem der drei alles verlangen, insgesamt aber nur einmal. [l6]Zahlt "
     "Ingo, kann er bei der Gesellschaft Rückgriff nehmen.", PS),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Anspruch gegen einen Gesellschafter in drei Schritten. [t1]Gibt es eine rechtsfähige "
     "G.b.R.? [t2]Hat sie, wirksam vertreten, eine Verbindlichkeit begründet? [t3]Und haftet der Gesellschafter nach "
     "Paragraf siebenhunderteinundzwanzig? [t4]Anspruchsgrundlage ist dann Paragraf vierhundertdreiunddreißig "
     "Absatz zwei in Verbindung mit Paragraf siebenhunderteinundzwanzig.", PS),
    # --- L Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Römisch eins: Schuld der Gesellschaft. [s1a]Erstens: rechtsfähige G.b.R., also "
     "Vertrag und gewollte Teilnahme am Rechtsverkehr. [s1b]Zweitens: Vertrag, wirksam vertreten nach Paragraf "
     "siebenhundertzwanzig. [s2]Römisch zwei: Haftung des Gesellschafters nach Paragraf siebenhunderteinundzwanzig. "
     "[s2a]Erstens: Gesellschafterstellung. [s2b]Zweitens: keine Einwendungen nach Paragraf siebenhunderteinundzwanzig b.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die rechtsfähige G.b.R. kauft und schuldet selbst. [m2]Für ihre Schulden haftet jeder Gesellschafter "
     "persönlich auf das Ganze.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
