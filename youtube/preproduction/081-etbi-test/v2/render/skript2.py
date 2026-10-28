"""Folge 081 v2 – Erlaubnistatbestandsirrtum im Papier-/Schema-Stil.

[marke] steht direkt vor dem Wort, bei dem ein Bildelement erscheint. Die Marken werden
über die Phonem-Alignments der Stimme auf die Audiozeit dieses Wortes gelegt.
Zweiter Wert = Pause nach der Einheit in Sekunden.
"""

P, PS = 0.4, 0.9  # normale Pause / Pause vor Folienwechsel

SEGMENTE = [
    # --- Fall -----------------------------------------------------------------------
    ("[fall]Nachts am Bahnhof. [a]A wartet allein auf den letzten Zug.", P),
    ("Plötzlich [b]rennt ein Mann auf ihn zu, B, und [tasche]greift hastig in seine Jackentasche.", P),
    ("A denkt: [messer]Der zieht ein Messer! Um ihm zuvorzukommen, [faust]schlägt A ihm mit der Faust ins Gesicht. "
     "[nase]B geht zu Boden, die Nase ist gebrochen.", P),
    ("Dann die Überraschung: [handy]B wollte A nur sein Handy zurückgeben. A hatte es auf der Bank liegen lassen.", P),
    ("[licht]Unter der Laterne hätte A bei genauem Hinsehen erkennen können, dass B das Handy schon in der Hand hielt.", P),
    ("[frage]Wie hat sich A strafbar gemacht?", PS),
    # --- Schema: Tatbestand, Rechtswidrigkeit --------------------------------------------
    ("[schema]Wir prüfen [a223]Körperverletzung nach Paragraf zweihundertdreiundzwanzig Absatz eins Strafgesetzbuch.", P),
    ("[tb]Der Tatbestand ist schnell erfüllt: Der Faustschlag ist eine [tbok]körperliche Misshandlung, "
     "die gebrochene Nase eine Gesundheitsschädigung. Und A wollte B treffen. Er handelt [vors]vorsätzlich.", P),
    ("Spannend wird es bei der [rw]Rechtswidrigkeit. A könnte durch [nw]Notwehr gerechtfertigt sein.", PS),
    # --- § 32 ----------------------------------------------------------------------------
    ("[norm]Paragraf zweiunddreißig: Wer eine Tat begeht, die durch Notwehr geboten ist, handelt nicht [hl1]rechtswidrig.", P),
    ("[abs2]Notwehr ist die Verteidigung, die erforderlich ist, um einen [hl2]gegenwärtigen rechtswidrigen Angriff "
     "von sich oder einem anderen abzuwenden.", PS),
    # --- Notwehrlage: Vorstellung vs. Wirklichkeit ----------------------------------------
    ("[nwl]Ein Angriff ist jede drohende Verletzung rechtlich geschützter Interessen durch einen Menschen. "
     "Und genau daran fehlt es: [wirkl]B wollte helfen, nicht angreifen. Objektiv liegt keine Notwehrlage vor.", P),
    ("Aber: [vorst]In der Vorstellung von A gab es sehr wohl einen Angriff. Er hielt sich für gerechtfertigt. "
     "Man spricht von [putativ]Putativnotwehr.", PS),
    ("[zurueck]Zurück zum Schema. [nwneg]Notwehr scheidet aus, die Tat ist rechtswidrig. "
     "[frage2]Aber was folgt aus dem Irrtum von A?", PS),
    # --- zwei gesetzliche Irrtümer --------------------------------------------------------
    ("[irrtum]Das Strafgesetzbuch regelt zwei Irrtümer. [tbi]Den Tatbestandsirrtum nach Paragraf sechzehn: "
     "Der Täter irrt über den Sachverhalt. Er weiß nicht, was er tut. [tbifolge]Dann entfällt der Vorsatz.", P),
    ("[vi]Und den Verbotsirrtum nach Paragraf siebzehn: Der Täter kennt den Sachverhalt, bewertet ihn aber rechtlich falsch. "
     "[vifolge]Ohne Schuld handelt er nur, wenn er den Irrtum nicht vermeiden konnte.", PS),
    # --- Matrix ---------------------------------------------------------------------------
    ("[matrix]Wo steht unser Fall? Ordne ihn in diese Tabelle ein. "
     "[m1]Irrt der Täter über Tatsachen des Tatbestands, ist es ein Tatbestandsirrtum. "
     "[m2]Irrt er über die rechtliche Bewertung, ist es ein Verbotsirrtum.", P),
    ("[m3]Auf der Ebene der Rechtfertigung gilt: Hält der Täter einen Rechtfertigungsgrund für gegeben, den es so nicht gibt, "
     "oder überdehnt er dessen Grenzen, ist das ein Erlaubnisirrtum. Auch das ist ein Verbotsirrtum nach Paragraf siebzehn.", P),
    ("[m4]Bleibt das letzte Feld: Der Täter irrt über Tatsachen, die ihn rechtfertigen würden, wenn sie wahr wären. "
     "[etbi]Das ist der Erlaubnistatbestandsirrtum. [luecke]Und für ihn gibt es keine gesetzliche Regelung.", PS),
    # --- liegt ein ETBI vor? ---------------------------------------------------------------
    ("[pruef]In der Klausur prüfst du zuerst, ob ein Erlaubnistatbestandsirrtum wirklich vorliegt. "
     "Die Frage lautet: [wenn]Wäre A gerechtfertigt, wenn seine Vorstellung stimmen würde?", P),
    ("[c1]Ein Messerangriff wäre ein gegenwärtiger, rechtswidriger Angriff. [c2]Der Faustschlag wäre erforderlich, "
     "denn ein milderes, gleich sicheres Mittel gegen ein gezogenes Messer ist nicht ersichtlich. "
     "[c3]Er wäre auch geboten, und [c4]A handelte, um sich zu verteidigen. [c5]Also: Ein Erlaubnistatbestandsirrtum liegt vor.", P),
    ("[tipp]Typischer Klausurfehler: Diese hypothetische Notwehrprüfung wird übersprungen. "
     "Wäre der Schlag selbst bei einem echten Angriff übertrieben gewesen, hilft der Erlaubnistatbestandsirrtum nicht.", PS),
    # --- Streitstand ------------------------------------------------------------------------
    ("[streit]Wie der Erlaubnistatbestandsirrtum zu behandeln ist, ist umstritten. [vier]Vier Ansichten solltest du kennen.", PS),
    ("[lnt]Erstens: die Lehre von den negativen Tatbestandsmerkmalen. [bloecke]Sie kennt keinen dreistufigen Aufbau. "
     "[merge]Tatbestand und Rechtswidrigkeit verschmelzen zu einem Gesamtunrechtstatbestand. "
     "Rechtfertigungsgründe sind danach negative Tatbestandsmerkmale.", P),
    ("[lntfolge]Folge: Paragraf sechzehn Absatz eins gilt direkt, der Vorsatz entfällt. "
     "[lntkritik]Kritik: Wer eine Mücke erschlägt und wer einen Angreifer in Notwehr abwehrt, stünden dann auf einer Stufe. "
     "Das verwischt den Unterschied zwischen tatbestandslosem und gerechtfertigtem Verhalten.", PS),
    ("[sst]Zweitens: die strenge Schuldtheorie. [sst17]Sie behandelt jeden Irrtum auf der Ebene der Rechtfertigung "
     "als Verbotsirrtum nach Paragraf siebzehn. [sstv1]War der Irrtum vermeidbar, bleibt A wegen vorsätzlicher Tat strafbar. "
     "Die Strafe kann nur gemildert werden. [sstv2]War er unvermeidbar, entfällt die Schuld.", P),
    ("[sstkritik]Kritik: A wollte sich rechtstreu verhalten. Er irrt nicht über Recht, sondern über Tatsachen. "
     "Ihn wie jemanden zu bestrafen, der bewusst Unrecht tut, wird dem nicht gerecht.", PS),
    ("[est]Drittens: die eingeschränkte Schuldtheorie. [est16]Sie wendet Paragraf sechzehn Absatz eins analog an, "
     "weil die Lage einem Tatbestandsirrtum gleicht. [estfolge]Das Vorsatzunrecht entfällt.", P),
    ("[estkritik]Kritik: Dann fehlt eine vorsätzliche, rechtswidrige Haupttat. [teiln]Wer die Wahrheit kennt und A "
     "anstiftet oder ihm hilft, bliebe jedenfalls als Teilnehmer straflos. [lueck2]Eine Strafbarkeitslücke.", PS),
    ("[rest]Viertens, die herrschende Meinung: die rechtsfolgenverweisende eingeschränkte Schuldtheorie. "
     "[restvors]Der Vorsatz bleibt bestehen, [restrw]die Tat ist vorsätzlich und rechtswidrig. "
     "[restschuld]Entfallen soll erst die Vorsatzschuld. Nur in der Rechtsfolge wird Paragraf sechzehn Absatz eins analog angewendet.", P),
    ("[restvorteil]Damit bleibt eine teilnahmefähige Haupttat. [bgh]Auch die Rechtsprechung wendet Paragraf sechzehn entsprechend an.", PS),
    # --- Streitentscheid ------------------------------------------------------------------
    ("[tab]Im Ergebnis kommen drei Ansichten zum selben Ziel: [t1]keine Strafbarkeit wegen vorsätzlicher Tat. "
     "[t2]Nur die strenge Schuldtheorie weicht ab, weil der Irrtum von A vermeidbar war. "
     "[entsch]Deshalb musst du den Streit hier entscheiden.", P),
    ("[tipp2]Klausurtipp: War der Irrtum unvermeidbar, sind sich alle Ansichten im Ergebnis einig. "
     "Dann kannst du den Streit offenlassen.", P),
    ("[folge]Wir folgen der herrschenden Meinung. [f1]Die strenge Schuldtheorie wird dem rechtstreuen Täter nicht gerecht, "
     "[f2]und nur die rechtsfolgenverweisende Lösung schließt die Lücke bei der Teilnahme.", PS),
    # --- Endschema ------------------------------------------------------------------------
    ("[end]Damit steht dein Schema. [e1]Tatbestand erfüllt. [e2]Die Tat ist rechtswidrig, Notwehr scheidet aus. "
     "[e3]In der Schuld prüfst du den Erlaubnistatbestandsirrtum [e4]und entscheidest den Streit. "
     "[e5]Die Vorsatzschuld entfällt. [e6]A ist nicht wegen vorsätzlicher Körperverletzung strafbar.", PS),
    ("[b229]Aber Vorsicht: Paragraf sechzehn Absatz eins Satz zwei lässt die Strafbarkeit wegen Fahrlässigkeit unberührt. "
     "[b1]Prüfe deshalb fahrlässige Körperverletzung nach Paragraf zweihundertneunundzwanzig.", P),
    ("[b2]Unter der Laterne hätte A das Handy bei genauem Hinsehen erkennen können. Sein Irrtum war sorgfaltswidrig. "
     "[b3]A ist wegen fahrlässiger Körperverletzung strafbar. [b4]Denk dabei an den Strafantrag nach Paragraf zweihundertdreißig.", PS),
    # --- Merksatz -------------------------------------------------------------------------
    ("[merke]Merke: Irrt der Täter über [hl3]Tatsachen, die ihn rechtfertigen würden, entfällt nach herrschender Meinung "
     "die [hl4]Vorsatzschuld. [merke2]Irrt er über die [hl5]rechtliche Bewertung, hilft ihm nur Paragraf siebzehn.", 1.4),
]
