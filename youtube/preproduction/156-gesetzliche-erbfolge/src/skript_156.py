"""Folge 156 · Gesetzliche Erbfolge §§ 1924 ff. BGB: Wer erbt ohne Testament? (Fr · Klausurpraxis · Erbrecht, Format Schema).
Beispielfall nach dem Plan-Hook („Der Vater stirbt ohne Testament – zurück bleiben Ehefrau, eine Tochter und ein Enkel vom
verstorbenen Sohn“): Kurt stirbt mit 78 Jahren ohne Testament. Er lebte mit Christa im gesetzlichen Güterstand der
Zugewinngemeinschaft. Kinder: Verena (lebt; ihre Tochter Mathilda) und Andreas (drei Jahre vor Kurt gestorben; sein einziges
Kind Severin). Kurts Eltern sind lange verstorben, sein Bruder Egbert lebt.
Prüfung: Stammbaum → § 1922 Abs. 1 (Wortlautkarte) → Ordnungen: § 1924 Abs. 1 (Wortlautkarte), §§ 1925, 1926 als Stufen,
§ 1930 (Wortlautkarte) → innerhalb der Ordnung: § 1924 Abs. 2 (Repräsentation), Abs. 3 (Eintritt), Abs. 4 (gleiche Teile,
Stämme) → Ehegatte: § 1931 Abs. 1 S. 1 (Wortlautkarte), Abs. 3 i. V. m. § 1371 Abs. 1 (Wortlautkarte) → Ergebnis 1/2, 1/4,
1/4 mit Gegenprobe; Variante Gütertrennung § 1931 Abs. 4 (je 1/3) → Klausurtipp (Lexi; § 2032) → Schema → Merksatz.
Takt: Der Todesfall nur als Text; Kurt und Andreas erscheinen nicht als Figuren, nur als Namen im Stammbaum (grauer Rahmen).
Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Kurt, Christa,
Verena, Mathilda, Andreas, Severin, Egbert (nie im Genitiv mit -s). Stimmen: Severin niklas, Egbert helmut. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Severin": "niklas", "Egbert": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Familie ---------------------------------------------------------------------------------------------
    ("[fall]Kurt ist mit achtundsiebzig Jahren gestorben. [test]Ein Testament hat er nicht hinterlassen. [fam]Die Familie "
     "kommt zusammen: [chr]Christa, seine Ehefrau, [ver]die Tochter Verena mit ihrer kleinen Tochter Mathilda [sev]und "
     "Severin, der Enkel. [andr]Sein Vater Andreas, der Sohn von Kurt, ist schon vor drei Jahren gestorben. [egb]Auch Egbert "
     "ist da, der Bruder von Kurt.", P),
    ("[rs]Mein Vater lebt nicht mehr. Bekomme ich dann überhaupt etwas?", P, "Severin"),
    ("[re]Und ich? Ich bin immerhin sein Bruder.", P, "Egbert"),
    ("[frage]Wer erbt, wenn es kein Testament gibt? [frage2]Und wie viel bekommt jeder?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Stammbaum -------------------------------------------------------------------------------------------------------
    ("[baum]Zeichnen wir den Stammbaum. [bk]Oben steht Kurt, der Erblasser. [bc]Neben ihm Christa. Die beiden lebten im "
     "gesetzlichen Güterstand, der Zugewinngemeinschaft. [bkin]Darunter die Kinder: Verena [band]und Andreas, der vor Kurt "
     "gestorben ist. [benk]Darunter die Enkel: Mathilda und Severin. [beg]Und daneben Egbert, der Bruder von Kurt; ihre "
     "Eltern sind schon lange verstorben.", PS),
    # --- D § 1922 Abs. 1 BGB -----------------------------------------------------------------------------------------------
    ("[p1922]Paragraf neunzehnhundertzweiundzwanzig Absatz eins: Mit dem Tode einer Person geht deren Vermögen als Ganzes "
     "auf eine oder mehrere andere Personen über. [univ]Das ist die Gesamtrechtsnachfolge, auch Universalsukzession genannt. "
     "[ges]Weil Kurt kein Testament gemacht hat, gilt die gesetzliche Erbfolge. [v040]Mit einem Testament wäre das anders; "
     "das zeigt das Video zum Berliner Testament.", PS),
    # --- E Ordnungen: § 1924 Abs. 1, §§ 1925, 1926 BGB ---------------------------------------------------------------------
    ("[ord]Das Gesetz teilt die Verwandten in Ordnungen ein. [p1924]Paragraf neunzehnhundertvierundzwanzig Absatz eins: "
     "Gesetzliche Erben der ersten Ordnung sind die Abkömmlinge des Erblassers. [abk]Abkömmlinge sind Kinder, Enkel und "
     "Urenkel. [o2]Zur zweiten Ordnung gehören nach Paragraf neunzehnhundertfünfundzwanzig die Eltern und deren "
     "Abkömmlinge, also auch Egbert. [o3]Zur dritten Ordnung gehören nach Paragraf neunzehnhundertsechsundzwanzig die "
     "Großeltern und deren Abkömmlinge.", P),
    # --- F § 1930 BGB ------------------------------------------------------------------------------------------------------
    ("[p1930]Und Paragraf neunzehnhundertdreißig: Ein Verwandter ist nicht zur Erbfolge berufen, solange ein Verwandter "
     "einer vorhergehenden Ordnung vorhanden ist. [egb2]Kurt hat Abkömmlinge. [egb3]Egbert erbt deshalb nichts, obwohl er "
     "der Bruder ist.", PS),
    # --- G1 § 1924 Abs. 2 BGB: Repräsentation ------------------------------------------------------------------------------
    ("[inn]Und wer erbt innerhalb der ersten Ordnung? [p2]Absatz zwei: Ein zur Zeit des Erbfalls lebender Abkömmling "
     "schließt die durch ihn mit dem Erblasser verwandten Abkömmlinge von der Erbfolge aus. [repr]Das ist das "
     "Repräsentationsprinzip. [repr2]Verena lebt, also erbt Mathilda nicht.", P),
    # --- G2 § 1924 Abs. 3, 4 BGB: Eintritt, Stämme -------------------------------------------------------------------------
    ("[p3]Absatz drei: An die Stelle eines zur Zeit des Erbfalls nicht mehr lebenden Abkömmlings treten die durch ihn mit "
     "dem Erblasser verwandten Abkömmlinge. [eintr]Das ist das Eintrittsrecht: Severin tritt an die Stelle von Andreas. "
     "[p4]Und nach Absatz vier erben Kinder zu gleichen Teilen. [staemme]Das Gesetz nennt das Erbfolge nach Stämmen: ein "
     "Stamm Verena, ein Stamm Andreas. [gleich]Verena und Severin bekommen gleich viel.", PS),
    # --- H1 § 1931 Abs. 1 S. 1 BGB -----------------------------------------------------------------------------------------
    ("[ehe]Und Christa? [p1931]Paragraf neunzehnhunderteinunddreißig Absatz eins Satz eins: Der überlebende Ehegatte des "
     "Erblassers ist neben Verwandten der ersten Ordnung zu einem Viertel, neben Verwandten der zweiten Ordnung oder neben "
     "Großeltern zur Hälfte der Erbschaft als gesetzlicher Erbe berufen. [viertel]Neben Verena und Severin bekommt Christa "
     "also zunächst ein Viertel.", P),
    # --- H2 § 1931 Abs. 3, § 1371 Abs. 1 BGB -------------------------------------------------------------------------------
    ("[abs3]Doch Absatz drei lässt Paragraf dreizehnhunderteinundsiebzig unberührt. [p1371]Endet die Zugewinngemeinschaft "
     "durch den Tod, erhöht sich nach dessen Absatz eins der gesetzliche Erbteil des überlebenden Ehegatten um ein Viertel "
     "der Erbschaft, [pausch]egal, ob überhaupt ein Zugewinn erzielt wurde. [halb]Ein Viertel plus ein Viertel: Christa "
     "erbt die Hälfte.", PS),
    # --- I Ergebnis, Gegenprobe, Variante ----------------------------------------------------------------------------------
    ("[erg]Das Ergebnis. [e_chr]Christa erbt die Hälfte. [e_rest]Die andere Hälfte teilen sich die beiden Stämme: "
     "[e_ver]Verena erbt ein Viertel [e_sev]und Severin ein Viertel. [probe]Gegenprobe: Eine Hälfte und zwei Viertel ergeben "
     "zusammen eins, also den ganzen Nachlass. [e_nicht]Mathilda und Egbert erben nichts.", P),
    ("[guet]Variante: Bei Gütertrennung erben nach Paragraf neunzehnhunderteinunddreißig Absatz vier der Ehegatte und ein "
     "oder zwei Kinder zu gleichen Teilen, [drittel]mit Severin an der Stelle von Andreas also je ein Drittel.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme zuerst die Quote des Ehegatten. [t1]Dafür musst du nur wissen, welche Ordnung zum Zug "
     "kommt, [t2]und welcher Güterstand galt. [t3]Erst dann verteilst du den Rest nach Stämmen. [t4]Und mehrere Erben bilden eine "
     "Erbengemeinschaft nach Paragraf zweitausend zweiunddreißig.", PS),
    # --- L Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Römisch eins: Erbfall ohne Verfügung von Todes wegen. [s2]Römisch zwei: die vorrangige "
     "Ordnung, Paragrafen neunzehnhundertvierundzwanzig bis neunzehnhundertdreißig. [s3]Römisch drei: der Erbteil des "
     "Ehegatten, [s3a]Paragraf neunzehnhunderteinunddreißig, [s3b]bei Zugewinngemeinschaft plus ein Viertel nach Paragraf "
     "dreizehnhunderteinundsiebzig. [s4]Römisch vier: der Rest nach Stämmen, [s4a]mit Repräsentation und Eintrittsrecht. "
     "[s5]Römisch fünf: die Gegenprobe, die Summe ist eins.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst die Quote des Ehegatten, dann der Rest nach Ordnungen und Stämmen. [m2]Wer lebt, schließt seine "
     "Abkömmlinge aus; an die Stelle eines Verstorbenen treten seine Abkömmlinge.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
