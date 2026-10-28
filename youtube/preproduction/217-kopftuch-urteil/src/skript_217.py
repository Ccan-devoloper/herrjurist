"""Folge 217 · Kopftuch-Urteil: Darf eine Lehrerin mit Kopftuch unterrichten? (Mo · Der Fall · Grundrechte · Klassiker-Fall).
Leitentscheidungen (Volltexte bundesverfassungsgericht.de, Abruf 06.10.2026, zitiert mit Rn.):
BVerfGE 108, 282 – 2 BvR 1436/02, Urt. v. 24.9.2003 (Kopftuch I, Zweiter Senat, 5 : 3);
BVerfGE 138, 296 – 1 BvR 471/10, 1 BvR 1181/10, Beschl. v. 27.1.2015 (Kopftuch II, Erster Senat, 6 : 2);
BVerfGE 153, 1 – 2 BvR 1333/17, Beschl. v. 14.1.2020 (Rechtsreferendarin, Zweiter Senat, 7 : 1).
Fiktiver Fall nach dem Muster von Kopftuch II (pauschales landesweites Verbot mit Ausnahme für christlich-abendländische
Werte wie § 57 Abs. 4 S. 3 SchulG NW a. F.); Land, Schule und alle Figuren erfunden, keine realen Beschwerdeführerinnen.
DARSTELLUNG: Frau Sander als sympathische, kompetente Lehrerin (Open-Peeps-Kopf „Hijab“); Schulleitung und Land neutral;
der Vater bringt ein legitimes Anliegen vor; keine religiösen Symbole anderer Religionen im Bild.
Figuren: Frau Sander (Lehrerin, lucy), Herr Steffens (Schulleiter, stephan), Herr Röder (Vater, christian; nie mit
Steffens in einer Szene), Vorsitzende Richterin (Funktionsrolle, hilde), Rechtsreferendarin (Funktionsrolle, spricht nicht).
Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter; „Grundgesetz“, „Beamtenstatusgesetz“ ausgeschrieben. Belege: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Sander": "lucy", "Steffens": "stephan", "Roeder": "christian", "Richterin": "hilde"}

SEGMENTE = [
    # --- A Fall: Klassenzimmer, Büro des Schulleiters ----------------------------------------------------------------
    ("[fall]Ein Gymnasium, Montagmorgen, erste Stunde. [mathe]Frau Sander unterrichtet Mathematik in der Klasse acht b, "
     "siebenundzwanzig Kinder. [tuch]Sie trägt ein Kopftuch, denn sie versteht es als Gebot ihres Glaubens. [nie]Streit darüber gab "
     "es nie.", P),
    ("[pause]In der Pause bittet Schulleiter Steffens sie in sein Büro. [neu]Das Land hat ein neues Schulgesetz "
     "beschlossen.", 0.2),
    ("[st1]Lehrkräfte dürfen im Dienst keine religiösen Zeichen mehr tragen, an allen Schulen des Landes. Ab dem "
     "ersten August gilt das auch für Sie.", P, "Steffens"),
    ("[sa1]Ich unterrichte Mathe, nicht Religion. Und mein Glaube verlangt das Kopftuch.", P, "Sander"),
    ("[ausn]Ausgenommen ist nur die Darstellung christlicher und abendländischer Bildungs- und "
     "Kulturwerte.", P),
    ("[frage]Darf das Land Frau Sander das Kopftuch so pauschal verbieten? [frage2]Und gilt vor Gericht dasselbe? "
     "[echt]Drei Entscheidungen des Bundesverfassungsgerichts geben die Antwort.", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Schutzbereich und Eingriff, Art. 4 Abs. 1, 2 GG (108, 282 Rn. 36 f., 40; 138, 296 Rn. 85 f., 89 f., 95 f.) -----
    ("[art4]Maßstab ist Artikel vier Grundgesetz. [wl4]Die Freiheit des Glaubens, des Gewissens und die Freiheit des "
     "religiösen und weltanschaulichen Bekenntnisses sind unverletzlich. Die ungestörte Religionsausübung wird "
     "gewährleistet.", P),
    ("[einh]Beide Absätze bilden ein einheitliches Grundrecht; [leben]es schützt auch ein Leben "
     "nach den Geboten des eigenen Glaubens. [streit]Ob der Islam das Kopftuch zwingend verlangt, ist umstritten. [plaus]Darauf "
     "kommt es nicht an: Es genügt, dass Frau Sander plausibel darlegt, dass sie es als verpflichtendes Gebot versteht. "
     "[wahl]Das Verbot stellt sie vor die Wahl: Beruf oder Glaubensgebot. [schwer]Ein schwerer Eingriff.", PS),
    # --- D Schranken: kollidierendes Verfassungsrecht (108, 282 Rn. 38, 41, 45 f.; 138, 296 Rn. 98) -------------------
    ("[vorb]Artikel vier steht unter keinem Gesetzesvorbehalt. [kvr]Grenzen setzt nur kollidierendes Verfassungsrecht, "
     "[best]und auch das nur auf Grundlage eines hinreichend bestimmten Gesetzes. [drei]Drei Gegenpositionen kommen in "
     "Betracht.", P),
    ("[neg]Erstens die negative Glaubensfreiheit der Schüler. [a6]Zweitens das Erziehungsrecht der "
     "Eltern aus Artikel sechs Absatz zwei. [a7]Drittens der staatliche Erziehungsauftrag aus Artikel sieben Absatz eins: "
     "Das gesamte Schulwesen steht unter der Aufsicht des Staates. [neutral]Diesen Auftrag muss der Staat religiös "
     "neutral erfüllen.", P),
    ("[roeder]Darauf beruft sich Herr Röder, der Vater eines Schülers.", 0.2),
    ("[rd1]Mein Sohn soll in der Schule nicht religiös beeinflusst werden. Das entscheiden wir als Eltern.", P, "Roeder"),
    # --- E Kopftuch I (BVerfGE 108, 282 LS 1, Rn. 30, 57–62, 66–71) --------------------------------------------------
    ("[k1]Zweitausenddrei, Kopftuch eins. [bw]Baden-Württemberg hatte eine Bewerberin abgelehnt, weil sie im Unterricht "
     "Kopftuch tragen wollte; ein ausdrückliches Gesetz dazu fehlte. [k1erg]Das Bundesverfassungsgericht: Ein Verbot "
     "braucht eine hinreichend bestimmte gesetzliche Grundlage. [parl]Den Ausgleich muss das Landesparlament selbst "
     "treffen. [folge]Mehrere Länder, etwa Nordrhein-Westfalen, erließen daraufhin Verbote.", PS),
    # --- F Kopftuch II (BVerfGE 138, 296 LS 2–4, Rn. 101, 104 f., 107, 112–116, 123–138) -----------------------------
    ("[k2]Zweitausendfünfzehn, Kopftuch zwei, zum Schulgesetz Nordrhein-Westfalens. [abstr]Ein landesweites Verbot schon "
     "wegen einer bloß abstrakten Gefahr ist unverhältnismäßig, wenn die Lehrerin einem als verpflichtend verstandenen "
     "Gebot folgt. [konkr]Das Gesetz ist deshalb eng auszulegen: Nötig ist eine hinreichend konkrete Gefahr für den "
     "Schulfrieden oder die staatliche Neutralität.", P),
    ("[zurech]Denn das Kopftuch einer Lehrerin macht sich der Staat nicht zu eigen, anders als ein Symbol, "
     "das die Schule selbst aufhängt. [wirbt]Solange die Lehrerin nicht für ihren Glauben wirbt, ist die negative "
     "Glaubensfreiheit der Schüler grundsätzlich nicht beeinträchtigt. [antw]Und die Eltern haben keinen Anspruch, ihre "
     "Kinder von solchen Lehrkräften fernzuhalten. [stoer]Anders, wenn an einer Schule heftig über religiöses Verhalten "
     "gestritten wird und das den Schulbetrieb ernsthaft stört; [bezirk]dann ist ein Verbot auch für bestimmte Schulen "
     "oder Bezirke möglich.", PS),
    ("[priv]Bleibt die Ausnahme für christliche und abendländische Werte. [a33]Artikel dreiunddreißig Absatz drei: "
     "Niemandem darf aus seiner Zugehörigkeit oder Nichtzugehörigkeit zu einem Bekenntnisse oder einer Weltanschauung "
     "ein Nachteil erwachsen. [nichtig]Die Ausnahme benachteiligt andere Religionen, auch "
     "entgegen Artikel drei Absatz drei, und ist nichtig. [alle]Ein Verbot muss für alle Glaubensrichtungen "
     "grundsätzlich unterschiedslos gelten.", P),
    ("[erg]Im Fall gab es nie Streit, eine konkrete Gefahr ist nicht erkennbar. [darf]Frau Sander darf mit Kopftuch "
     "unterrichten.", 0.2),
    ("[st2]Dann bleibt es dabei, Frau Sander: Sie unterrichten die acht b weiter.", P, "Steffens"),
    # --- G Rechtsreferendarin (BVerfGE 153, 1 LS 5, Rn. 5, 9, 90, 95, 102, 104 f.) -----------------------------------
    ("[ref]Strenger ist es in der Justiz. [hessen]Zweitausendzwanzig ging es um eine Rechtsreferendarin in Hessen. [taet]Nach "
     "einem Erlass des Landes durfte sie mit Kopftuch keine Aufgaben übernehmen, bei denen sie als Vertreterin der Justiz auftritt, etwa auf der "
     "Richterbank sitzen oder die Staatsanwaltschaft in der Sitzung vertreten.", 0.2),
    ("[ri1]Heute bitte nicht auf die Richterbank. Sie verfolgen die Verhandlung aus dem Zuschauerraum.", P,
     "Richterin"),
    ("[ref2]Das Bundesverfassungsgericht hielt dieses Verbot für verfassungsgemäß. [hoheit]In der Justiz tritt der Staat "
     "dem Bürger klassisch hoheitlich gegenüber; [robe]mit Robe und festem Ritual prägt er das Bild der Verhandlung selbst. "
     "[spiegel]Die Schule dagegen soll die religiös vielfältige Gesellschaft spiegeln. [muss]Aber: Das Land darf hier verbieten, es muss nicht.", PS),
    # --- H Heute: § 34 Abs. 2 BeamtStG (Fassung 2021); § 61 Abs. 2 BBG nur als Fundstelle --------------------------
    ("[heute]Heute gilt für Landesbeamte Paragraf vierunddreißig Absatz zwei Beamtenstatusgesetz, gefasst "
     "zweitausendeinundzwanzig: [wl34]Religiös oder weltanschaulich konnotierte Merkmale des Erscheinungsbilds können nur "
     "eingeschränkt oder untersagt werden, wenn sie objektiv geeignet sind, das Vertrauen in die neutrale Amtsführung zu beeinträchtigen. "
     "[laender]Die Einzelheiten kann jedes Land selbst regeln.", PS),
    # --- I Klausurtipp mit Prüfungsaufbau (Lexi) ------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Artikel vier im Dreischritt. [t1]Schutzbereich: Ein plausibel dargelegtes Glaubensgebot "
     "genügt. [t2]Eingriff: Wie schwer wiegt er? [t3]Rechtfertigung: Gibt es ein bestimmtes Gesetz, und welches "
     "Verfassungsgut kollidiert? [t3b]Der Kern: Reicht eine abstrakte Gefahr, oder braucht es eine konkrete? [t4]Trenne "
     "Schule und Justiz, und prüfe Ausnahmen für einzelne Religionen an Artikel dreiunddreißig Absatz drei.", PS),
    # --- J Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: In der Schule reicht die bloß abstrakte Gefahr für ein Kopftuchverbot nicht, es braucht eine konkrete. "
     "[m2]Vor Gericht darf der Staat strenger sein. [m3]Und jedes Verbot muss für alle Religionen gleich gelten.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
