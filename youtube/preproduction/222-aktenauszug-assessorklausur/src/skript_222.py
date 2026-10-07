"""Folge 222 · Aktenauszug Assessorklausur: Die ersten 20 Minuten mit der Akte (Fr · 2. Examen · Klausurtechnik, Format Schema).
Beispielfall: Zweites Examen, Zivilrechtsklausur, fünf Stunden. Die Referendarin Hermine liest zuerst den Bearbeitervermerk
(Entscheidung des Gerichts; Rubrum, Streitwertfestsetzung und Rechtsbehelfsbelehrung erlassen; Entscheidung am 30.9.2026).
In der Akte verlangt Herr Rehberg von seiner früheren Vermieterin Frau Pohlmann die Mietkaution von 1.500 € nebst Zinsen
seit Rechtshängigkeit zurück; Frau Pohlmann behält sie wegen Kratzern im Parkett (Kostenvoranschlag 1.650 €).
Schritte mit Zeitachse (Minuten = Empfehlung aus Erfahrung): 1. Bearbeitervermerk (0–5), 2. erster Durchgang (5–15) mit
Blick nach Klausurtyp (§ 313 Abs. 2 ZPO, § 117 Abs. 2 VwGO, § 200 Abs. 1 StPO), 3. Arbeitsblatt (15–20); Fallen; Klausurtipp;
Schema; Merksatz. Verweise: Folge 18 (Relationstechnik), 39 (Anklageklausur), 45 (Zeitplan).
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache: Hermine, Rehberg, Pohlmann (kein Genitiv);
die Aufsicht bleibt ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.8   # PS 0.8 statt 0.9: Hauptfilm unter 7:00 (Erstvertonung 7:03,6 mit Schlussszene 9:20 Uhr, siehe ABNAHME.md)

STIMMEN = {"Hermine": "sabrina", "Aufsicht": "william", "Rehberg": "marc", "Pohlmann": "laura_ruhig"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: Klausurraum, neun Uhr ----------------------------------------------------------------------------------
    ("[fall]Neun Uhr, zweites Examen, Klausur im Zivilrecht. [akte]Vor Hermine liegt eine Akte mit dreißig Seiten.", 0.3),
    ("[auf1]Bitte beginnen Sie. Sie haben fünf Stunden.", 0.4, "Aufsicht"),
    ("[hinten]Hermine blättert zuerst ganz nach hinten. [vermerk]Dort steht der Bearbeitervermerk: "
     "[entw]Die Entscheidung des Gerichts ist zu entwerfen. "
     "[erl]Rubrum, Streitwertfestsetzung und Rechtsbehelfsbelehrung sind erlassen.", 0.4),
    ("[h1]Drei Teile erlassen. Was genau muss ich also schreiben?", 0.5, "Hermine"),
    # --- A2 Fall: was in der Akte steht ----------------------------------------------------------------------------------
    ("[vorn]Erst dann liest sie vorn. [streit]Herr Rehberg verlangt von seiner früheren Vermieterin, Frau Pohlmann, "
     "die Mietkaution zurück.", 0.3),
    ("[r1]Ich will meine Kaution zurück, eintausendfünfhundert Euro.", 0.4, "Rehberg"),
    ("[p1]Das Parkett ist zerkratzt. Die Kaution behalte ich.", 0.5, "Pohlmann"),
    ("[frage]Was tust du in den ersten zwanzig Minuten mit der Akte, [frage2]bevor du eine Zeile schreibst?", 0.6),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Überblick: Aktenauszug und Zeitachse ---------------------------------------------------------------------------
    ("[auszug]Im zweiten Examen bekommst du in der Regel keinen fertigen Sachverhalt, sondern einen Aktenauszug: "
     "Schriftsätze, Anlagen, Protokolle. [ordnen]Den Streitstoff musst du erst selbst ordnen. "
     "[empf]Für die ersten zwanzig Minuten gilt: Die Minuten sind eine Empfehlung aus Erfahrung, "
     "keine Vorgabe. [z1]Etwa fünf Minuten für den Bearbeitervermerk, [z2]zehn Minuten für einen ersten Durchgang durch "
     "die Akte [z3]und fünf Minuten für dein Arbeitsblatt.", PS),
    # --- D Schritt 1: Bearbeitervermerk (Minute 0 bis 5) -------------------------------------------------------------------
    ("[s1]Erstens, Minute null bis fünf: der Bearbeitervermerk. Lies ihn zuerst, auch wenn er ganz hinten steht. "
     "[auftrag]Er ist dein Arbeitsauftrag. [rolle]Wer bist du: Gericht, Anwalt oder Staatsanwaltschaft? "
     "[produkt]Danach richtet sich, was du entwirfst: ein Urteil, einen Schriftsatz oder eine Anklage. "
     "[her1]Hermine entscheidet als Gericht.", P),
    ("[erlassen]Dann: Was ist erlassen? Erlassen heißt, diesen Teil musst du nicht schreiben. "
     "[rest]Alles andere gehört grundsätzlich in den Entwurf. [rest2]Bei Hermine also Tenor, Tatbestand und "
     "Entscheidungsgründe. [datum]Nennt der Vermerk ein Datum, ist das dein "
     "Stichtag. Hier ergeht die Entscheidung am dreißigsten September. [stich]Von diesem Tag aus beurteilst du, welche "
     "Fristen schon abgelaufen sind.", PS),
    # --- E Schritt 2: erster Durchgang (Minute 5 bis 15) --------------------------------------------------------------------
    ("[s2]Zweitens, Minute fünf bis fünfzehn: ein erster Durchgang durch die Akte, mit Stift, aber noch ohne zu prüfen. "
     "[bet]Markiere die Beteiligten: [kl]Kläger ist Herr Rehberg, [bk]Beklagte ist Frau Pohlmann. [antr]Dann die Anträge. "
     "[ak]Herr Rehberg beantragt, Frau Pohlmann zur Zahlung von eintausendfünfhundert Euro nebst Zinsen seit "
     "Rechtshängigkeit zu verurteilen. [ab]Frau Pohlmann beantragt, die Klage abzuweisen.", P),
    ("[chron]Und dann die Chronologie mit allen Daten. [d1]Mietbeginn am ersten April zweitausendeinundzwanzig, "
     "die Kaution ist gezahlt. [d2]Auszug am einunddreißigsten Mai zweitausendfünfundzwanzig. [d3]Die Klage geht am "
     "zwölften Januar zweitausendsechsundzwanzig ein [d4]und wird am zwanzigsten Januar zugestellt.", PS),
    # --- F Blick nach Klausurtyp ------------------------------------------------------------------------------------------
    ("[typ]Worauf du beim Lesen besonders achtest, hängt vom Entwurf ab. [zpo]Für das Zivilurteil gilt Paragraf "
     "dreihundertdreizehn Absatz zwei ZPO: [w313]Im Tatbestand stehen Ansprüche, Angriffs- und "
     "Verteidigungsmittel und Anträge, knapp dargestellt. [trenn]Deshalb trennst du schon "
     "jetzt: Was ist unstreitig, was behauptet der Kläger, was die Beklagte? [unstr]Bei Hermine sind Mietvertrag, Kaution "
     "und Auszug unstreitig. [str]Streitig sind die Kratzer im Parkett. Herr Rehberg bestreitet sie. "
     "[rel]Wie du daraus die Relation baust, zeigt Folge achtzehn.", P),
    ("[vwgo]Für das Verwaltungsurteil zählt Paragraf hundertsiebzehn Absatz zwei VwGO die Teile auf, [teile]von den "
     "Beteiligten bis zur Rechtsmittelbelehrung. [abgl]Gleiche diese Liste mit dem Vermerk ab. [frist]Und markiere "
     "Bescheid, Widerspruch und Zustellungen, wegen der Monatsfrist für die Anfechtungsklage, Paragraf vierundsiebzig.", P),
    ("[stpo]Für die Anklage nennt Paragraf zweihundert Absatz eins StPO den Angeschuldigten, die Tat mit Zeit und Ort, "
     "die gesetzlichen Merkmale und die Strafvorschriften. [jetat]Notiere also schon beim Lesen für jede Tat: wer, wann, wo. "
     "[ankl]Den Aufbau der Anklageklausur zeigt Folge neununddreißig.", PS),
    # --- G Schritt 3: Arbeitsblatt (Minute 15 bis 20) -----------------------------------------------------------------------
    ("[s3]Drittens, Minute fünfzehn bis zwanzig: dein Arbeitsblatt. [blatt]Ein Muster: [b1]Oben steht der Auftrag aus dem "
     "Vermerk, mit den erlassenen Teilen und dem Stichtag. [b2]Darunter Beteiligte und Anträge. [b3]Dann der Zeitstrahl. "
     "[b4]Und drei Spalten: unstreitig, Kläger behauptet, Beklagte behauptet. [fuell]Beim genauen Lesen danach füllst du "
     "das Blatt weiter. [zeitpl]Zum Schluss verteilst du die übrigen vier Stunden und vierzig Minuten. "
     "[f45]Wie, zeigt Folge fünfundvierzig.", PS),
    # --- H Fallen ----------------------------------------------------------------------------------------------------------
    ("[fallen]Drei typische Fallen. [f1]Falle eins: Hinweise im Vermerk. Steht dort etwa, die Zustellungen seien "
     "ordnungsgemäß, unterstellst du das und prüfst es nicht neu. [f1b]Und erlassen ist nur das Schreiben, nicht das "
     "Denken. Den Streitstoff musst du trotzdem vollständig erfassen.", P),
    ("[f2]Falle zwei: die Anlagen. Mietvertrag, Kostenvoranschlag und Schreiben gehören zur Akte. [f2b]Lies sie mit. "
     "[f2c]Bei Hermine steht der Betrag der Reparatur nur im Kostenvoranschlag: eintausendsechshundertfünfzig Euro.", P),
    ("[f3]Falle drei: die Daten. Eingang und Zustellung sind nicht dasselbe. [rh]Rechtshängig wird die Klage erst mit der "
     "Zustellung. [zins]Von da an laufen Prozesszinsen. [her3]Für die Zinsen kommt es also auf den zwanzigsten Januar "
     "an, nicht auf den zwölften. [p167]Für die Verjährung kann dagegen schon der Eingang genügen, wenn demnächst "
     "zugestellt wird, Paragraf hundertsiebenundsechzig ZPO.", PS),
    # --- J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lies den Bearbeitervermerk nach den zwanzig Minuten noch einmal. [tipp2]Erst mit der Akte im Kopf "
     "merkst du, ob du die Aufgabe richtig verstanden hast.", PS),
    # --- K Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die ersten zwanzig Minuten. [k1]Römisch eins, Minute null bis fünf: der Bearbeitervermerk, "
     "[k1a]mit Rolle, Entwurf, erlassenen Teilen und Stichtag. [k2]Römisch zwei, Minute fünf bis fünfzehn: der erste "
     "Durchgang, [k2a]mit Beteiligten, Anträgen, Chronologie und Daten, [k2b]je nach Entwurf mit Blick auf Tatbestand, "
     "Urteilsteile oder Anklagesatz. [k3]Römisch drei, Minute fünfzehn bis zwanzig: das Arbeitsblatt, [k3a]mit Zeitstrahl, "
     "Streitstand und Zeitplan.", PS),
    # --- L Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Bearbeitervermerk bestimmt, was du schreibst. [m2]Was er nicht erlässt, gehört in deinen Entwurf.", 1.4),
]
