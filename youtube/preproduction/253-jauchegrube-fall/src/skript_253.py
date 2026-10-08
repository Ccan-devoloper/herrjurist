"""Folge 253 · Jauchegrube-Fall: dolus generalis oder Versuch plus Fahrlässigkeit? (Mo · Der Fall · StGB AT · Klassiker-Fall).
Übungsfall (Personen fiktiv), dem echten Fall nachgebildet: Brunhilde greift im Streit am Gartenzaun ihre Nachbarin an und nimmt
deren Tod in Kauf; die Nachbarin bleibt regungslos liegen, Brunhilde hält sie für tot, beschließt erst jetzt, die vermeintliche
Leiche verschwinden zu lassen, und versenkt sie im Teich; erst dort stirbt die bewusstlose Nachbarin.
Der echte Fall nur abstrakt: BGH, Urt. v. 26.4.1960 – 5 StR 77/60, BGHSt 14, 193 (Angeklagte, Frau B, bedingter Tötungsvorsatz,
Jauchegrube; Gründe nach der Wiedergabe ra-kotz.de, gegengeprüft juraexamen.info). Neuere Rspr. mit Rn.: BGH, Urt. v. 3.12.2015
– 4 StR 223/15 (HRRS 2016 Nr. 77 = NStZ 2016, 721), Rn. 10 (Ursächlichkeit trotz eigenen späteren Handelns, zitiert BGHSt 14, 193,
194), Rn. 12 (Formel; Verdeckungshandlung ohne Tötungsvorsatz: keine wesentliche Abweichung, zitiert 5 StR 77/60), Rn. 13.
Aufbau: Fall → Frage → Sachverhalt → echter Fall (abstrakt) → zweiaktiges Geschehen → objektiv (Kausalität) → § 16 Abs. 1 S. 1
(Wortlautkarte), Vorsatz bei der Tathandlung, Kausalverlauf (Verweis Folge 068) → 1. dolus generalis (historisch, vom BGH
abgelehnt) → 2. BGH: unwesentliche Abweichung, bedingter Vorsatz ändert nichts; Formel 4 StR 223/15 Rn. 12 → 3. Versuchslösung
(Teil der Lehre: Versuch + § 222) → 4. vermittelnd: Tatplan → Ergebnis im Fall nach BGH (+ Gegenansichten) → Klausurtipp, Schema,
Merksatz (Lexi).
DARSTELLUNG: keine Gewaltszene, kein Würgen, keine Leiche, kein Ertrinken im Bild; das Opfer ist keine Figur; nur Symbole
(leerer Garten, Wasseroberfläche, Uhr, Pillen); keine Tatdetails.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Brunhilde sabrina. Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Brunhilde": "sabrina"}

SEGMENTE = [
    # --- A Fall: Streit am Gartenzaun, der Teich ---------------------------------------------------------------------------
    ("[fall]Brunhilde und ihre Nachbarin streiten seit Jahren über den Weg zum Teich. [streit]Eines Nachmittags eskaliert der "
     "Streit am Gartenzaun. [angriff]Brunhilde greift die Nachbarin an. Dass sie dabei sterben kann, nimmt Brunhilde in Kauf. "
     "[still]Die Nachbarin bleibt regungslos liegen.", 0.3),
    ("[br1]Sie atmet nicht mehr. Sie ist tot.", P, "Brunhilde"),
    ("[verst]Erst jetzt beschließt Brunhilde, die vermeintliche Leiche verschwinden zu lassen. [teich]Sie versenkt die Nachbarin "
     "im Teich. [lebte]Doch die Nachbarin war nur bewusstlos. [stirbt]Erst im Wasser stirbt sie.", 0.4),
    ("[frage]Brunhilde wollte die Nachbarin töten. Doch als sie sie versenkte, hielt sie sie schon für tot. [frage2]Ist "
     "Brunhilde wegen vollendeten Totschlags strafbar? Oder nur wegen Versuchs und fahrlässiger Tötung?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall (nur abstrakt) -----------------------------------------------------------------------------------
    ("[echt]Der Fall folgt einem Klassiker: dem Jauchegrube-Fall, entschieden vom Bundesgerichtshof neunzehnhundertsechzig. "
     "[echt2]Dort griff die Angeklagte eine Frau mit bedingtem Tötungsvorsatz an. Sie hielt die Bewusstlose für tot und warf sie "
     "in eine Jauchegrube. [echt3]Erst dort starb die Frau.", P),
    # --- D Das Problem: zweiaktiges Geschehen; objektiv; § 16 (Wortlautkarte) ---------------------------------------------
    ("[zwei]Das Problem ist ein zweiaktiges Geschehen. [akt1]Beim ersten Akt, dem Angriff, hatte Brunhilde Tötungsvorsatz. Doch "
     "dieser Akt tötete nicht unmittelbar. [akt2]Beim zweiten Akt, dem Versenken, starb die Nachbarin. Da glaubte Brunhilde "
     "aber, der Erfolg sei längst eingetreten.", P),
    ("[obj]Zuerst die objektive Seite. [kaus]Der Angriff war ursächlich für den Tod. Ohne ihn hätte Brunhilde die Nachbarin "
     "nicht für tot gehalten und nicht versenkt. [kaus2]Dass ihr eigenes späteres Handeln mitwirkte, ändert daran nichts. "
     "[zurech]Die Lehre fragt hier zusätzlich nach der objektiven Zurechnung. Sie lässt sich bejahen, weil ein solcher Verlauf "
     "nicht fernliegt.", P),
    ("[p16]Schwierig ist der Vorsatz. Paragraf sechzehn Absatz eins Satz eins: Wer bei Begehung der Tat einen Umstand nicht "
     "kennt, der zum gesetzlichen Tatbestand gehört, handelt nicht vorsätzlich. [zeit]Der Vorsatz muss also bei der "
     "Tathandlung vorliegen. [kv]Er muss sich auch auf den Kausalverlauf erstrecken, aber nur in seinen wesentlichen Zügen. "
     "[f68]Den Irrtum über den Kausalverlauf erklärt Folge achtundsechzig.", P),
    # --- E1 dolus generalis (historisch) -----------------------------------------------------------------------------------
    ("[dg]Erste Lösung, historisch: die Lehre vom dolus generalis. [dg2]Sie sah beide Akte als ein Geschehen, getragen von einem "
     "Gesamtvorsatz. Danach wäre Brunhilde wegen vollendeten Totschlags strafbar. [dg3]Der Bundesgerichtshof hat das im "
     "Jauchegrube-Fall abgelehnt. Der Generalvorsatz sei unklar und rechtsgeschichtlich überholt. Mit ihm dürfe man den "
     "Tötungsvorsatz nicht auf spätere Handlungen ausdehnen, bei denen er nicht mehr bestand. [dg4]Heute wird diese Lehre "
     "nicht mehr vertreten.", P),
    # --- E2 BGH: unwesentliche Abweichung ----------------------------------------------------------------------------------
    ("[bgh]Trotzdem bestätigte der Bundesgerichtshof die Verurteilung wegen vollendeten Totschlags. [bgh2]Er knüpfte an den "
     "ersten Akt an. Mit ihm hatte die Angeklagte den Tod verursacht, und zwar mit bedingtem Vorsatz. [bgh3]Der Tod trat zwar "
     "anders ein als vorgestellt. Diese Abweichung sei aber nur gering und rechtlich ohne Bedeutung. [bedingt]Dass sie nur mit "
     "bedingtem und nicht mit direktem Vorsatz handelte, ändere daran nichts.", P),
    ("[formel]Heute sagt der Bundesgerichtshof: Eine Abweichung vom vorgestellten Kausalverlauf ist unwesentlich, wenn sie sich "
     "innerhalb der Grenzen des nach allgemeiner Lebenserfahrung Vorhersehbaren hält und keine andere Bewertung der Tat "
     "rechtfertigt. [verdeck]Stirbt das Opfer erst durch eine Verdeckungshandlung, die nicht mehr vom Tötungsvorsatz getragen "
     "ist, verneint die Rechtsprechung eine wesentliche Abweichung.", P),
    # --- E3 Versuchslösung (Teil der Lehre) --------------------------------------------------------------------------------
    ("[vers]Ein Teil der Lehre trennt die beiden Akte. [vers2]Der erste Akt ist dann ein versuchter Totschlag, der zweite eine "
     "fahrlässige Tötung nach Paragraf zweihundertzweiundzwanzig. [vers3]Denn bei dem Akt, der den Tod herbeiführte, fehlte der "
     "Vorsatz. [vers4]Die Kritik: Diese Lösung reißt ein zusammengehöriges Geschehen auseinander.", P),
    # --- E4 vermittelnd: Tatplan -------------------------------------------------------------------------------------------
    ("[plan]Vermittelnde Stimmen fragen nach dem Tatplan. [plan2]Vollendung soll danach nur vorliegen, wenn der Täter das "
     "Beseitigen schon beim ersten Akt eingeplant hatte.", P),
    # --- F Ergebnis im Fall nach dem BGH -----------------------------------------------------------------------------------
    ("[erg]Zurück zu Brunhilde. [e1]Sie griff die Nachbarin mit Tötungsvorsatz an, und der Angriff war ursächlich für den Tod. "
     "[e2]Dass ein Täter die vermeintliche Leiche beseitigt und das Opfer erst dabei stirbt, liegt nicht außerhalb der "
     "Lebenserfahrung. [e3]Es rechtfertigt auch keine andere Bewertung. Brunhilde wollte töten, und der Tod geht auf ihren "
     "Angriff zurück. [e4]Nach dem Bundesgerichtshof ist Brunhilde wegen vollendeten Totschlags strafbar. Mordmerkmale lassen "
     "wir offen. [e5]Nach der Versuchslösung bliebe es bei versuchtem Totschlag und fahrlässiger Tötung. [e6]Ebenso nach dem "
     "Tatplan, denn das Versenken war nicht eingeplant.", PS),
    # --- G Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Der Streit gehört in den subjektiven Tatbestand, zum Vorsatz bezüglich des Kausalverlaufs. [k1]Stelle "
     "kurz fest, dass beim Versenken kein Tötungsvorsatz mehr bestand. Prüfe dann den Angriff. [k2]Den dolus generalis "
     "erwähnst du höchstens kurz. Den Streit entscheidest du, denn die Ansichten führen zu verschiedenen Ergebnissen.", P),
    # --- H Klausurschema (Lexi), progressiv --------------------------------------------------------------------------------
    ("[sch]So baust du die Prüfung auf: Totschlag durch den Angriff, Paragraf zweihundertzwölf. [s1]Objektiver Tatbestand: Tod, "
     "Kausalität und objektive Zurechnung, trotz des zweiten Akts. [s2]Subjektiver Tatbestand: Vorsatz bezüglich des Todes. "
     "[s3]Dann der Vorsatz bezüglich des Kausalverlaufs. Hier stellst du den Streit dar. Nach dem Bundesgerichtshof ist die "
     "Abweichung unwesentlich. [s4]Danach Rechtswidrigkeit und Schuld.", PS),
    # --- I Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Den Generalvorsatz lehnt der Bundesgerichtshof ab. [m2]Stirbt das Opfer erst durch den zweiten Akt, ist das nach dem "
     "Bundesgerichtshof in der Regel nur eine unwesentliche Abweichung vom vorgestellten Kausalverlauf. [m3]Der Täter ist dann "
     "wegen vollendeter Tat strafbar.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
