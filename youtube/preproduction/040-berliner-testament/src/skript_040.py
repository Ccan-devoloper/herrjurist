"""Folge 040 · Berliner Testament: Die Falle nach dem ersten Todesfall (§ 2271 BGB) (Mo · Der Fall · Zivilrecht/Erbrecht).
Übungsfall nach dem Plan-Hook („Nach dem Tod ihres Mannes will die Witwe den Sohn statt der Tochter als Schlusserben
einsetzen“), Muster BGH, Beschl. v. 26.10.2011 – IV ZR 72/11 und OLG Köln, Beschl. v. 12.1.2026 – 2 W 169/25:
Günter und Ingrid (Ehepaar) setzen sich im eigenhändigen gemeinschaftlichen Testament gegenseitig als Alleinerben und ihre
Kinder Petra und Uwe als Schlusserben zu gleichen Teilen ein. Nach Günters Tod (Ingrid hat das Erbe angenommen) will Ingrid
neu testieren: Uwe soll alles bekommen.
Kern: §§ 2265, 2267 (Wirksamkeit), § 2269 I (Einheitslösung), § 2270 I–III (Wechselbezüglichkeit, Vermutung Abs. 2),
§ 2271 I (Widerruf zu Lebzeiten nur nach § 2296), § 2271 II 1 (Erlöschen, Ausschlagung), §§ 1943, 1944 (Annahme, Frist),
Änderungsvorbehalt (OLG Hamm 10 W 40/21), Ausblick § 2287 analog, Pflichtteil § 2303 I.
Wortlautkarten: § 2269 Abs. 1, § 2270 Abs. 1, § 2271 Abs. 2 Satz 1 BGB. Belege je Aussage: ../RECHTSSTAND.md.
Vierstellige Paragrafen werden als „zweitausend zweihundert…“ gesprochen (getrennt geschrieben, leichter für die Stimme).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Guenter": "helmut", "Ingrid": "hilde", "Petra": "lisa"}  # Lexi = Erzählerstimme (Carla); Uwe ohne Text

SEGMENTE = [
    # --- A Fall: das gemeinsame Testament ----------------------------------------------------------------------------
    ("[fall]Günter und Ingrid sind seit über vierzig Jahren verheiratet. "
     "[tisch]Am Küchentisch schreibt Günter ihr gemeinsames Testament mit der Hand.", 0.3),
    ("[g1]Wir setzen uns gegenseitig als Alleinerben ein. Nach dem Tod des Letzten von uns erben Petra und Uwe "
     "zu gleichen Teilen.", 0.3, "Guenter"),
    ("[unter]Beide unterschreiben.", 0.2),
    ("[i1]Dann bleibt alles in der Familie.", 0.4, "Ingrid"),
    # --- B Fall: nach Günters Tod -------------------------------------------------------------------------------------
    ("[tod]Drei Jahre später stirbt Günter. [erbt]Ingrid erbt alles und nimmt das Erbe an. "
     "[streit]Mit ihrer Tochter Petra hat sie sich inzwischen zerstritten, [uwe]ihr Sohn Uwe hilft ihr im Alltag.", 0.3),
    ("[i2]Ich schreibe ein neues Testament. Uwe soll alles bekommen.", 0.3, "Ingrid"),
    ("[p1]Das hast du mit Papa anders ausgemacht!", 0.4, "Petra"),
    ("[frage]Darf Ingrid ihr Testament noch ändern? [frage2]Oder sitzt sie nach dem ersten Todesfall in der Falle?", 0.6),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Wirksamkeit: §§ 2265, 2267 ----------------------------------------------------------------------------------
    ("[gt]Zuerst: Ist das gemeinsame Testament wirksam? [p2265]Ein gemeinschaftliches Testament können nach Paragraf "
     "zweitausend zweihundertfünfundsechzig nur Ehegatten errichten, [lp]eingetragene Lebenspartner nach dem "
     "Lebenspartnerschaftsgesetz ebenso. [nicht]Ein unverheiratetes Paar kann es nicht. "
     "[form]Zur Form genügt nach Paragraf zweitausend zweihundertsiebenundsechzig: Einer schreibt das Testament "
     "eigenhändig und unterschreibt, [form2]der andere unterschreibt mit. "
     "[formok]Günter hat geschrieben, beide haben unterschrieben. Das Testament ist wirksam.", PS),
    # --- E Inhalt: § 2269 Abs. 1 (Wortlautkarte) -----------------------------------------------------------------------
    ("[inhalt]Was haben die beiden verfügt? [p2269]Paragraf zweitausend zweihundertneunundsechzig Absatz eins hilft "
     "mit einer Auslegungsregel: [w2269]Setzen sich Ehegatten gegenseitig ein und soll der beiderseitige Nachlass nach "
     "dem Tod des Überlebenden an einen Dritten fallen, [w2269b]ist der Dritte im Zweifel für den gesamten Nachlass "
     "Erbe des zuletzt versterbenden Ehegatten.", P),
    ("[einheit]Das ist die Einheitslösung: Ingrid wird Vollerbin von Günter. "
     "[schluss]Petra und Uwe sind Schlusserben. Sie erben erst nach Ingrid, dann aber alles. "
     "[trenn]Eine Vor- und Nacherbschaft, die Trennungslösung, gilt nur, wenn sich das aus dem Testament ergibt.", PS),
    # --- F Wechselbezüglichkeit: § 2270 (Wortlautkarte Abs. 1) -----------------------------------------------------------
    ("[p2270]Die Falle steckt in Paragraf zweitausend zweihundertsiebzig Absatz eins. "
     "[w2270]Wechselbezüglich sind Verfügungen, von denen anzunehmen ist, dass die des einen nicht ohne die des "
     "anderen getroffen wäre. [w2270b]Dann reißt die Nichtigkeit oder der Widerruf der einen Verfügung die andere mit.", P),
    ("[ausl]Ob das so ist, klärst du zuerst durch Auslegung. [vermut]Bleibt es offen, greift die Vermutung aus "
     "Absatz zwei: [zuw]Günter wendet Ingrid sein Vermögen zu, [kinder]und Ingrid setzt für den Fall ihres Überlebens "
     "Petra und Uwe ein, die mit Günter verwandt sind. [wb]Also ist Ingrids Schlusserbeneinsetzung wechselbezüglich "
     "zu Günters Einsetzung von Ingrid. [abs3]Das geht nach Absatz drei nur bei Erbeinsetzungen, Vermächtnissen, "
     "Auflagen und der Wahl des anwendbaren Erbrechts.", PS),
    # --- G Bindung: § 2271 ----------------------------------------------------------------------------------------------
    ("[leb]Solange beide leben, gibt es noch einen Ausweg. [wid]Sie kann ihre Verfügung widerrufen, aber nur durch "
     "notariell beurkundete Erklärung gegenüber Günter, nach Paragraf zweitausend zweihunderteinundsiebzig Absatz eins "
     "und Paragraf zweitausend zweihundertsechsundneunzig. [allein]Ein neues Testament allein reicht dafür nicht.", P),
    ("[tod2]Mit Günters Tod ändert sich alles. [w2271]Paragraf zweitausend zweihunderteinundsiebzig Absatz zwei "
     "Satz eins: Das Recht zum Widerruf erlischt mit dem Tode des anderen Ehegatten; [w2271b]der Überlebende kann "
     "jedoch seine Verfügung aufheben, wenn er das ihm Zugewendete ausschlägt. "
     "[gebunden]Ingrid ist jetzt grundsätzlich gebunden, ähnlich wie bei einem Erbvertrag.", P),
    # --- H Ausweg Ausschlagung -------------------------------------------------------------------------------------------
    ("[aus]Der gesetzliche Ausweg ist die Ausschlagung. [preis]Dann verliert Ingrid aber, was Günter ihr zugewendet hat. "
     "[frist]Und eine Erbschaft kann man in der Regel nur binnen sechs Wochen ausschlagen, "
     "[angen]und gar nicht mehr, wenn man sie angenommen hat. [zu]Ingrid hat angenommen. Der Weg ist versperrt. "
     "[sonder]Sonderfälle nach Absatz zwei Satz zwei, etwa schwere Verfehlungen eines Kindes, lassen wir hier beiseite.", PS),
    # --- I Ergebnis ---------------------------------------------------------------------------------------------------
    ("[erg]Das Ergebnis: [e1]Ingrids neues Testament ist unwirksam, soweit es Petra beeinträchtigt. "
     "[e2]Nach Ingrids Tod erben Petra und Uwe je zur Hälfte.", PS),
    # --- J Gestaltungstipp: Änderungsvorbehalt --------------------------------------------------------------------------
    ("[klausel]Hätten Günter und Ingrid das vermeiden können? Ja, mit einer Änderungsklausel. "
     "[kl2]Etwa: Der Überlebende darf die Verteilung unter den Kindern ändern. "
     "[kl3]So ein Vorbehalt schließt die Bindung in seinem Umfang aus. "
     "[kl4]Nach dem Oberlandesgericht Hamm kann er sogar decken, dass ein Kind alles bekommt.", PS),
    # --- K Ausblick: Schenkungen, Pflichtteil -------------------------------------------------------------------------
    ("[schenk]Zu Lebzeiten bleibt Ingrid frei: Als Vollerbin darf sie über ihr Vermögen verfügen. "
     "[p2287]Verschenkt sie das Haus aber an Uwe, um Petra zu beeinträchtigen, und hat sie daran kein eigenes "
     "lebzeitiges Interesse, kann Petra nach Ingrids Tod ihren Anteil herausverlangen. "
     "[bgh]Der Bundesgerichtshof wendet dafür Paragraf zweitausend zweihundertsiebenundachtzig entsprechend an.", P),
    ("[pfl]Und beim ersten Erbfall? Da gingen Petra und Uwe leer aus. [pfl2]Sie können von Ingrid ihren Pflichtteil "
     "verlangen, nach Paragraf zweitausend dreihundertdrei.", PS),
    # --- L Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Wechselbezüglichkeit für jede Verfügung einzeln, und zwar im Verhältnis zur "
     "Verfügung des anderen Ehegatten. [tipp2]Und erst auslegen: Die Vermutung aus Absatz zwei greift nur, wenn die "
     "Auslegung kein Ergebnis bringt. [tipp3]Hat ein Ehegatte zum Beispiel viel mehr Vermögen, kann das gegen die "
     "Wechselbezüglichkeit sprechen.", PS),
    # --- M Klausurschema ------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur Frage, wer Ingrid beerbt. [s1]Römisch eins: Wirksamkeit des gemeinschaftlichen "
     "Testaments. [s2]Römisch zwei: Inhalt durch Auslegung, die Einheitslösung. [s3]Römisch drei: "
     "Wechselbezüglichkeit, [s4]erst Auslegung, dann die Vermutung.", P),
    ("[s5]Römisch vier: Bindung des Überlebenden: [s6]kein Widerruf zu Lebzeiten beider, "
     "[s7]Widerrufsrecht mit dem Tod erloschen, [s8]keine Ausschlagung, kein Änderungsvorbehalt. "
     "[s9]Römisch fünf: Das neue Testament ist unwirksam, soweit es beeinträchtigt.", PS),
    # --- N Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Nach dem ersten Todesfall ist der Überlebende an wechselbezügliche Verfügungen gebunden. "
     "[mk2]Lösen kann er sich grundsätzlich nur durch Ausschlagung, es sei denn, das Testament behält ihm die Änderung vor.", 1.4),
]
