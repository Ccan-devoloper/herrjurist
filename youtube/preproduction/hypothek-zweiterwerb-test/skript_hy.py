"""Gutgläubiger Zweiterwerb der forderungsentkleideten Hypothek. [marke] = Bildelement ab diesem Wort."""

P, PS = 0.4, 0.9

SEGMENTE = [
    # --- Fall -----------------------------------------------------------------------------------------------
    ("[fall]Emma besitzt ein Grundstück. [bruno]Bruno verspricht ihr ein Darlehen über hunderttausend Euro. "
     "[hyp]Zur Sicherheit bestellt Emma ihm eine Briefhypothek. [brief]Sie wird ins Grundbuch eingetragen, und Bruno bekommt den Brief.", P),
    ("[nie]Doch Bruno zahlt das Darlehen nie aus.", PS),
    ("[clara]Trotzdem tritt Bruno die angebliche Forderung samt Hypothek schriftlich an Clara ab und übergibt ihr den Brief. "
     "[ahnungslos]Clara ahnt nichts.", P),
    ("[david]Später tritt Clara alles an David ab. [weiss]David weiß allerdings, dass Bruno nie ausgezahlt hat.", P),
    ("[frage]Hat David die Hypothek erworben?", 0.6),
    # --- Sachverhalt zum Nachlesen ------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- I. Ausgangslage -------------------------------------------------------------------------------------------
    ("[schema]Wir gehen der Reihe nach vor. Zuerst: Wem stand die Hypothek am Anfang zu?", P),
    ("[akz]Die Hypothek ist akzessorisch. Sie setzt eine Forderung voraus, Paragraf elfhundertdreizehn. "
     "[keine]Bruno hat nie ausgezahlt, also ist kein Rückzahlungsanspruch entstanden.", P),
    ("[egs]Deshalb steht das Recht Emma selbst zu, als Eigentümergrundschuld. "
     "Paragrafen elfhundertdreiundsechzig und elfhundertsiebenundsiebzig.", PS),
    # --- II. Ersterwerb Clara ----------------------------------------------------------------------------------------
    ("[s_clara]Dann der Erwerb durch Clara. [abtr]Die Hypothek geht mit der Forderung über. Nötig sind eine schriftliche "
     "Abtretung und die Übergabe des Briefs, Paragrafen elfhundertdreiundfünfzig und elfhundertvierundfünfzig.", P),
    ("[nb]Aber Bruno hatte weder Forderung noch Hypothek. Und eine Forderung kann man grundsätzlich nicht gutgläubig erwerben.", P),
    ("[1138]Hier hilft Paragraf elfhundertachtunddreißig. Für die Hypothek gilt der öffentliche Glaube des Grundbuchs "
     "auch in Ansehung der Forderung. [gg]Bruno war als Gläubiger eingetragen, und Clara war gutgläubig, Paragraf achthundertzweiundneunzig.", P),
    ("[entkl]Clara erwirbt also die Hypothek, aber nicht die Forderung. Man spricht von einer forderungsentkleideten Hypothek. "
     "[folge]Clara kann in das Grundstück vollstrecken, Paragraf elfhundertsiebenundvierzig. "
     "[folge2]Zahlung von Emma persönlich kann sie nicht verlangen.", PS),
    # --- III. Zweiterwerb David ----------------------------------------------------------------------------------------
    ("[s_david]Jetzt das eigentliche Problem: der Zweiterwerb durch David. [boes]David ist bösgläubig. "
     "Und eine Forderung gibt es immer noch nicht.", P),
    ("[aa]Eine Mindermeinung sagt: Paragraf elfhundertachtunddreißig schützt nur Gutgläubige. [aa2]David erwirbt deshalb nichts.", P),
    ("[hm]Die herrschende Meinung sieht das anders. [hm1]Clara ist Berechtigte. David erwirbt also vom Berechtigten, "
     "auf seinen guten Glauben kommt es nicht an. [hm2]Übertragen wird wie gewohnt, durch Abtretung und Briefübergabe.", P),
    ("[arg]Das überzeugt. Sonst könnte Clara ihr Recht praktisch nicht weiterveräußern, und ihr Schutz liefe leer.", PS),
    # --- Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: David hat die Hypothek erworben, ohne Forderung. [emma]Emma muss die Zwangsvollstreckung in ihr Grundstück dulden. "
     "[ausgl]Ausgleich sucht sie bei Bruno, etwa nach Paragraf achthundertsechzehn Absatz eins Satz eins.", P),
    ("[tipp]Klausurtipp: Den guten Glauben prüfst du nur beim Ersterwerb. [tipp2]Ist das Recht einmal gutgläubig erworben, "
     "geht es danach ganz normal weiter. [tipp3]Besonders umstritten ist nur der Fall, dass Bruno selbst das Recht zurückerwirbt.", PS),
    # --- Schema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Erstens: Entstehung. Ohne Forderung liegt eine Eigentümergrundschuld vor. "
     "[k2]Zweitens: Ersterwerb, gutgläubig über Paragraf elfhundertachtunddreißig, forderungsentkleidet.", P),
    ("[k3]Drittens: Zweiterwerb. Erwerb vom Berechtigten, Streit darstellen, der herrschenden Meinung folgen.", PS),
    # --- Merksatz --------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer eine forderungsentkleidete Hypothek gutgläubig erworben hat, kann sie weiter übertragen. "
     "[m2]Der Zweiterwerber erwirbt vom Berechtigten, auch wenn er bösgläubig ist.", 1.4),
]
