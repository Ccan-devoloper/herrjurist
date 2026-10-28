"""Folge 004 · Neutralitätspflicht: Darf eine Ministerin gegen eine Partei posten? (frei nach BVerfGE 148, 11 – 2 BvE 1/16;
Gegenfall nach BVerfGE 154, 320 – 2 BvE 1/19; Linie BVerfGE 162, 207 – 2 BvE 4/20, 5/20). Personen und Partei erfunden.
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad. „Partei Iks“ wird so geschrieben, damit die Stimme den Buchstaben X sicher als „Iks“ spricht;
im Bild steht „Partei X“."""

P, PS = 0.4, 0.9

STIMMEN = {"Brandt": "laura_klar", "Krueger": "christian", "Mia": "julia", "Hahn": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Ministerium ------------------------------------------------------------------------------
    ("[buero]Montagmorgen in einem Bundesministerium. [kundg]Die Partei Iks hat für Samstag eine Kundgebung gegen die "
     "Politik der Bundesregierung angekündigt. [brandt]Ministerin Brandt ist verärgert.", 0.3),
    ("[b1]Das poste ich sofort: Rote Karte für Partei Iks!", 0.3, "Brandt"),
    ("[k1]Über den offiziellen Kanal des Ministeriums?", 0.3, "Krueger"),
    ("[b2]Natürlich. Dort lesen es die meisten.", 0.4, "Brandt"),
    ("[post]Kurz darauf steht der Beitrag online, mit dem Wappen des Ministeriums. [post2]Rote Karte für Partei Iks! "
     "Ihre Redner treiben die Radikalisierung voran. [post3]Wer am Samstag mitläuft, stärkt sie.", 0.5),
    # --- B Fall: die Folgen ----------------------------------------------------------------------------------
    ("[mia]Die Studentin Mia wollte sich die Kundgebung eigentlich ansehen.", 0.2),
    ("[m1]Wenn sogar die Ministerin das sagt, bleibe ich lieber weg.", 0.4, "Mia"),
    ("[hahn]Der Vorsitzende von Partei Iks ist empört.", 0.2),
    ("[h1]Das ist Missbrauch des Amtes! Wir gehen nach Karlsruhe.", 0.4, "Hahn"),
    ("[frage]Durfte die Ministerin so posten? Und was wäre, wenn sie denselben Satz auf einem Parteitag gesagt hätte?", 0.6),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Zulässigkeit: Organstreit --------------------------------------------------------------------------
    ("[zul]Partei Iks kann ein Organstreitverfahren einleiten, nach Artikel vierundneunzig Absatz eins Nummer eins "
     "Grundgesetz.", P),
    ("[bet]Beteiligtenfähig ist die Partei, soweit sie ihren besonderen Status aus Artikel einundzwanzig geltend macht. "
     "[bet2]Die Ministerin ebenso: Artikel fünfundsechzig Satz zwei gibt jedem Bundesminister eigene Rechte.", P),
    ("[gegenst]Der Beitrag ist eine Maßnahme, und eine Verletzung der Chancengleichheit ist möglich. "
     "[befugt]Also ist die Partei antragsbefugt. [rsb]Selbst wenn der Beitrag gelöscht wird, bleibt das "
     "Rechtsschutzbedürfnis, weil sich so etwas wiederholen kann. [frist]Die Frist beträgt sechs Monate.", PS),
    # --- E Begründetheit: Maßstab ----------------------------------------------------------------------------
    ("[mass]Zur Begründetheit. [art20]Alle Staatsgewalt geht vom Volke aus, Artikel zwanzig Absatz zwei. Die Willensbildung "
     "muss vom Volk zu den Staatsorganen laufen, nicht umgekehrt.", P),
    ("[art21]Deshalb garantiert Artikel einundzwanzig Absatz eins den Parteien gleiche Chancen, und Staatsorgane müssen "
     "neutral bleiben. [immer]Nicht nur im Wahlkampf, sondern auch dazwischen.", P),
    ("[info]Zugleich darf die Regierung ihre Politik erklären und Kritik zurückweisen, allerdings nur sachlich.", PS),
    # --- F Schritt 1: amtlich? ---------------------------------------------------------------------------------
    ("[amt]Erster Schritt: Hat Brandt als Ministerin gehandelt oder als Parteipolitikerin? [pp]Auch eine Ministerin darf "
     "Parteipolitik machen, nur nicht mit den Mitteln ihres Amtes.", P),
    ("[mittel]Amtlich ist eine Äußerung, wenn sie Autorität oder Ressourcen des Amtes nutzt: Pressemitteilungen, die "
     "Internetseite des Ministeriums, Staatssymbole. [konto]Für offizielle Konten in sozialen Medien dürfte nach dem "
     "Bundesverfassungsgericht dasselbe gelten.", P),
    ("[sub_amt]Brandt postet über den Dienstkanal mit Wappen. Sie handelt also als Ministerin.", PS),
    # --- G Schritt 2: Eingriff -------------------------------------------------------------------------------
    ("[eingriff]Zweiter Schritt: der Eingriff. [rk]Die Rote Karte bewertet Partei Iks einseitig negativ. [abschreck]Und der "
     "Beitrag soll erkennbar Menschen von der Kundgebung fernhalten. [mia2]Schon eine solche abschreckende Wirkung greift in "
     "die Chancengleichheit ein.", PS),
    # --- H Schritt 3: Rechtfertigung, Ergebnis ------------------------------------------------------------------
    ("[recht]Dritter Schritt: Ist das gerechtfertigt? Brandt beruft sich darauf, Kritik an der Regierung zurückzuweisen. "
     "[sach]Doch ihr Beitrag erklärt keine Politik und widerlegt keinen Vorwurf. Er wertet nur ab. "
     "[gegenschlag]Ein Recht auf Gegenschlag gibt es nicht.", P),
    ("[erg]Ergebnis: Der Beitrag verletzt Partei Iks in ihrem Recht auf Chancengleichheit aus Artikel einundzwanzig Absatz "
     "eins. [wanka]So entschied das Bundesverfassungsgericht zweitausendachtzehn über eine Rote Karte auf der Internetseite "
     "eines Ministeriums.", PS),
    # --- I Gegenfall: Parteitag --------------------------------------------------------------------------------
    ("[parteitag]Und auf dem Parteitag? Dort spricht Brandt als Parteipolitikerin, ohne Mittel des Amtes. [pt2]Dann darf "
     "sie Partei Iks scharf kritisieren. Das Neutralitätsgebot greift dort nicht.", P),
    ("[titel]Auch der Ministertitel allein macht eine Rede nicht amtlich. [repost]Aber Vorsicht: Teilt das Ministerium das "
     "Video auf seinem Kanal, setzt es wieder Mittel des Amtes ein. [urt20]So entschied Karlsruhe zweitausendzwanzig: Das "
     "Interview eines Ministers war zulässig, seine Veröffentlichung auf der Ministeriumsseite nicht.", P),
    ("[kanzler]Zweitausendzweiundzwanzig galt das auch für die Kanzlerin: Ihre Äußerung auf einer Pressekonferenz im "
     "Ausland war amtlich und verletzte die Chancengleichheit. [kanzler3]Stabilität der Regierung oder Ansehen im Ausland können zwar rechtfertigen, aber nur, wenn "
     "sie wirklich gefährdet sind.", PS),
    # --- J Klausurtipp (Lexi) ---------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe immer zuerst, ob amtlich gehandelt wurde. [tipp1]Erst dann kommen Neutralität und "
     "Sachlichkeit. [tipp2]Und zitiere den Organstreit heute nach Artikel vierundneunzig. Ältere Urteile nennen noch "
     "Artikel dreiundneunzig.", PS),
    # --- K Klausurschema ------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]A, Zulässigkeit des Organstreits: "
     "[s1b]Beteiligte, Maßnahme, Antragsbefugnis, Rechtsschutzbedürfnis, Frist.", P),
    ("[s2]B, Begründetheit. [s2a]Römisch eins: Chancengleichheit aus Artikel einundzwanzig. [s2b]Römisch zwei: amtliches "
     "Handeln. [s2c]Römisch drei: Eingriff durch einseitige Parteinahme. [s2d]Römisch vier: Rechtfertigung, vor allem "
     "Sachlichkeit.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------
    ("[merke]Merke: Als Parteipolitikerin darf die Ministerin austeilen. [m2]Wer aber das Amt und seine Kanäle nutzt, "
     "muss neutral und sachlich bleiben.", 1.4),
]
