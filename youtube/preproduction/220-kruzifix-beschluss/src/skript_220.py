"""Folge 220 · Kruzifix-Beschluss: Muss das Kreuz aus dem Klassenzimmer? (Mo · Der Fall · Grundrechte · Klassiker-Fall).
Leitentscheidung (Volltext bundesverfassungsgericht.de, Abruf 07.10.2026, zitiert mit Rn.):
BVerfGE 93, 1 – 1 BvR 1087/91, Beschl. v. 16.5.1995 (Kruzifix, Erster Senat; abw. Meinung Seidl, Söllner, Haas).
Folgefälle: Art. 7 Abs. 3 BayEUG i. d. F. v. 23.12.1995 (Wortlaut nach BayVerfGH, Vf. 6-VII-96 u. a., amtliches PDF;
heute Art. 7 Abs. 4 BayEUG, am amtlichen Portal nicht geprüft); BVerwG, Urt. v. 21.4.1999 – 6 C 18.98 (BVerwGE 109, 40);
BVerwG, Urt. v. 19.12.2023 – 10 C 5.22 (Kreuzerlass, § 28 AGO).
Fiktiver Fall nach dem Muster des Kruzifix-Beschlusses: Familie Rohde, ihr Sohn und Schulleiter Kampe sind erfunden; die
realen Beschwerdeführer werden weder dargestellt noch benannt. DARSTELLUNG: respektvoll gegenüber allen Bekenntnissen;
das Kreuz als schlichtes Symbol (Tabler „cross“, ohne Korpus); keine Karikatur von Gläubigen oder Nichtgläubigen.
Figuren: Herr Rohde (Vater, niklas), Herr Kampe (Schulleiter, helmut); Frau Rohde und der Sohn sprechen nicht.
Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Artikel im Sprechtext als Wörter. Belege: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Rohde": "niklas", "Kampe": "helmut"}

SEGMENTE = [
    # --- A Fall: Klassenzimmer, Elterngespräch (fiktiv, Muster BVerfGE 93, 1 Rn. 2–5) ----------------------------------
    ("[fall]Bayern, Anfang der neunziger Jahre, eine staatliche Grundschule. [kreuz]Über der Tafel hängt ein Kreuz; "
     "die Volksschulordnung schreibt vor: In jedem Klassenzimmer ist ein Kreuz anzubringen. [eltern]Herr und Frau Rohde "
     "gehören keiner Kirche an und erziehen ihren Sohn ohne religiöses Bekenntnis. [gespr]Sie bitten Schulleiter Kampe "
     "um ein Gespräch.", 0.2),
    ("[ro1]Unser Sohn soll nicht jeden Tag unter dem Kreuz lernen müssen. Bitte hängen Sie es ab.", P, "Rohde"),
    ("[ka1]Das Kreuz schreibt die Schulordnung vor. Und es steht doch für unsere abendländische Kultur.", P, "Kampe"),
    ("[frage]Muss das Kreuz aus dem Klassenzimmer? [echt]Genau darüber entschied das Bundesverfassungsgericht "
     "neunzehnhundertfünfundneunzig im Kruzifix-Beschluss.", PS),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Schutzbereich: Art. 4 Abs. 1 GG (Rn. 34–36) --------------------------------------------------------------
    ("[art4]Maßstab ist Artikel vier Absatz eins Grundgesetz: [wl4]Die Freiheit des Glaubens, des Gewissens und die "
     "Freiheit des religiösen und weltanschaulichen Bekenntnisses sind unverletzlich.", P),
    ("[pos]Geschützt ist die Freiheit, einen Glauben zu haben und nach ihm zu leben. [neg]Ebenso geschützt ist die "
     "negative Seite: Man darf kultischen Handlungen und Symbolen eines Glaubens fernbleiben, den man nicht teilt. "
     "[alltag]Vor fremden Glaubenssymbolen im Alltag bewahrt das Grundrecht nicht. [lage]Wohl aber vor einer Lage, die "
     "der Staat schafft und in der man einem Symbol ohne Ausweichmöglichkeit ausgesetzt ist. [a6]Die Eltern schützt "
     "Artikel vier zusammen mit Artikel sechs Absatz zwei: Sie dürfen ihr Kind von Glaubensüberzeugungen fernhalten, "
     "die ihnen falsch erscheinen.", PS),
    # --- D Eingriff (Rn. 37–47) -------------------------------------------------------------------------------------
    ("[eingr]Ist das angeordnete Kreuz ein Eingriff? [pflicht]Ja. Wegen der Schulpflicht sind die Kinder dem Kreuz "
     "von Staats wegen und ohne Ausweichmöglichkeit ausgesetzt; [unter]sie müssen unter dem Kreuz lernen. [strasse]Das "
     "ist etwas anderes als ein Kreuz im Straßenbild: Diese Begegnung ist flüchtig, und sie geht nicht vom Staat aus. "
     "[korpus]Das gilt für Kreuze mit und ohne Korpus.", P),
    ("[kultur]Und ist das Kreuz nicht bloß ein Zeichen abendländischer Kultur? [symbol]Nein, sagt das Gericht: Es ist "
     "das Glaubenssymbol des Christentums schlechthin. [appell]Im Klassenzimmer hat es appellativen Charakter, und das "
     "gegenüber Kindern, die besonders leicht zu beeinflussen sind.", PS),
    # --- E Rechtfertigung (Rn. 48–57) -------------------------------------------------------------------------------
    ("[vorb]Artikel vier ist vorbehaltlos gewährleistet. Grenzen müssen sich aus der Verfassung selbst ergeben. "
     "[a7]In Betracht kommt Artikel sieben Absatz eins: Das gesamte Schulwesen steht unter der Aufsicht des Staates. "
     "[auftrag]Daraus folgt ein eigener staatlicher Erziehungsauftrag.", P),
    ("[konk]Der Konflikt ist nach praktischer Konkordanz zu lösen: Keine Position setzt sich maximal durch, alle "
     "erfahren einen möglichst schonenden Ausgleich. [bezug]Religiöse Bezüge muss die Schule deshalb nicht völlig "
     "meiden. [minimum]Sie darf aber nur das unerlässliche Minimum an Zwang enthalten und christliche "
     "Glaubensinhalte nicht verbindlich machen. [grenze]Das Kreuz in jedem Klassenzimmer überschreitet diese Grenze.", P),
    ("[posit]Und die positive Glaubensfreiheit der christlichen Eltern und Kinder? [allen]Sie steht allen zu, nicht nur "
     "Christen. [mehr]Und der Konflikt lässt sich nicht nach dem Mehrheitsprinzip lösen, denn die Glaubensfreiheit "
     "schützt gerade Minderheiten. [frei]Religionsunterricht und Schulgebet müssen freiwillig bleiben und zumutbare "
     "Ausweichmöglichkeiten lassen. [wand]Dem Kreuz an der Wand kann niemand ausweichen.", PS),
    # --- F Ergebnis (Leitsätze, Tenor, Rn. 56, 58 f.; abw. Meinung Rn. 60, 73 f., 84, 87 f.) ---------------------------
    ("[erg]Ergebnis: Ein Kreuz in den Unterrichtsräumen einer staatlichen Pflichtschule, die keine Bekenntnisschule "
     "ist, verstößt gegen Artikel vier Absatz eins. [nichtig]Die Vorschrift der Volksschulordnung erklärte das Gericht für nichtig. "
     "[abw]Drei der acht Richter widersprachen: Das Kreuz stehe für die Werte der christlichen Gemeinschaftsschule, "
     "und das Toleranzgebot verlange, es hinzunehmen.", 0.2),
    ("[ka2]Dann nehmen wir das Kreuz in der Klasse Ihres Sohnes ab, Herr Rohde.", P, "Kampe"),
    # --- G Folgen in Bayern (Art. 7 Abs. 3 BayEUG 1995; BVerwG 6 C 18.98; BVerwG 10 C 5.22) ---------------------------
    ("[bayern]Bayern reagierte noch neunzehnhundertfünfundneunzig mit einer Widerspruchslösung im Schulgesetz: "
     "[haengt]Das Kreuz hängt weiter. [wid]Widersprechen Eltern aus ernsthaften und einsehbaren Gründen des Glaubens "
     "oder der Weltanschauung, sucht der Schulleiter eine gütliche Einigung. [bverwg]Neunzehnhundertneunundneunzig "
     "stellte das Bundesverwaltungsgericht klar: Gelingt keine Einigung und gibt es keine zumutbare Alternative, muss "
     "sich der Widersprechende durchsetzen. [erlass]Die Kreuze, die Bayern seit zweitausendachtzehn im Eingangsbereich "
     "seiner Behörden aufhängt, muss es dagegen nicht entfernen. [flucht]Geklagt hatten Weltanschauungsgemeinschaften, "
     "und dort ist die Begegnung nur flüchtig.", PS),
    # --- H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe in drei Schritten. [t1]Schutzbereich: die negative Glaubensfreiheit, für die Eltern "
     "zusammen mit Artikel sechs Absatz zwei. [t2]Eingriff: Die Schulpflicht macht das Kreuz unausweichlich, und es ist "
     "ein religiöses Symbol. [t3]Rechtfertigung: Artikel sieben Absatz eins und die positive Glaubensfreiheit der "
     "anderen, abgewogen in praktischer Konkordanz. [t4]Grenze ab: Das Kopftuch einer Lehrerin ist ihr eigenes "
     "Bekenntnis, das Kreuz an der Wand hängt der Staat auf. [fehler]Und argumentiere nie mit der Mehrheit in der "
     "Klasse.", PS),
    # --- I Merksatz (Lexi) -----------------------------------------------------------------------------------------
    ("[merke]Merke: Der Staat darf Kinder nicht zwingen, unter dem Kreuz zu lernen. [m2]Wo die Schulpflicht kein "
     "Ausweichen lässt, entscheidet nicht die Mehrheit.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
