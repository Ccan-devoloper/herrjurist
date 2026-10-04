"""Folge 143 · Fraport-Urteil: Gilt das Grundgesetz für eine Flughafen-AG? (Mi · Examenswissen · Klassiker-Fall; Art. 1 III,
5 I, 8 I GG). Echter Fall sachlich nacherzählt: BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06 (BVerfGE 128, 226), Volltext
bundesverfassungsgericht.de, Randnummern dort; Mittelbare Drittwirkung: BVerfG, Beschl. v. 11.4.2018 – 1 BvR 3080/09.
Reale Beteiligte (Beschwerdeführerin, Aktivisten, Mitarbeiter, Richter) treten nicht als Figuren auf und werden nicht
benannt. Fiktive Figuren im realen Schauplatz (wie 028): Dorothea (Reisende, bekommt ein Flugblatt; Stimme sabrina) und
Herr Sievers (Mitarbeiter der Flughafengesellschaft, Dramatisierung der Position der Betreiberin, BVerfG Rn. 1, 5 f., 10;
Stimme marc). Beide Namen werden im Sprechtext nicht genannt (nur Namensschild/Sachverhalt).
NEUTRALITÄT: Inhalt der Flugblätter nur sachlich („zu einer bevorstehenden Abschiebung“, Rn. 9), keine Bewertung;
neutrales Terminal-Icon, kein Logo.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Dorothea": "sabrina", "Sievers": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Der Fall im Terminal (Rn. 9, 10) ----------------------------------------------------------------------------
    ("[fall]Frankfurter Flughafen, elfter März zweitausenddrei, Terminal eins. [akt]Eine Aktivistin kommt mit fünf weiteren "
     "Aktivisten einer Initiative gegen Abschiebungen. [flug]Sie verteilt Flugblätter zu einer bevorstehenden Abschiebung. [ende]Mitarbeiter der "
     "Flughafengesellschaft und der Bundesgrenzschutz beenden die Aktion.", P),
    ("[b1]Ohne unsere Erlaubnis keine Flugblätter und keine Demonstrationen im Terminal.", P, "Sievers"),
    ("[verbot]Am nächsten Tag erteilt die Betreiberin, die Fraport Aktiengesellschaft, der Aktivistin ein "
     "Flughafenverbot. [straf]Wird sie wieder unberechtigt angetroffen, droht ein Strafantrag wegen Hausfriedensbruchs.", P),
    # --- A2 Eigentümer, Instanzen, Frage (Rn. 2, 11–18, 44) ------------------------------------------------------------
    ("[aktien]Die Aktien der Fraport gehören damals zu rund siebzig Prozent dem Land Hessen, der Stadt Frankfurt und dem "
     "Bund; [privat]der Rest ist in privater Hand.", P),
    ("[d1]Darf eine Aktiengesellschaft so etwas einfach verbieten?", P, "Dorothea"),
    ("[klage]Die Aktivistin klagt. [aglg]Amtsgericht und Landgericht weisen ab: Die Fraport habe ein Hausrecht und sei "
     "nicht unmittelbar an die Grundrechte gebunden. [bgh]Der Bundesgerichtshof lässt die Bindung offen; das Verbot sei "
     "jedenfalls verhältnismäßig. [vb]Es folgt die Verfassungsbeschwerde.", P),
    ("[frage]Gilt das Grundgesetz für eine Flughafen-Aktiengesellschaft? [frage2]Und ist ein Terminal ein Ort für "
     "Demonstrationen und Flugblätter?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Grundrechtsbindung, Art. 1 Abs. 3 GG (Rn. 45–60) -------------------------------------------------------------
    ("[bind]Am zweiundzwanzigsten Februar zweitausendelf entscheidet das Bundesverfassungsgericht. Erster Schritt: die "
     "Grundrechtsbindung. [a13]Artikel eins Absatz drei: Die nachfolgenden Grundrechte binden Gesetzgebung, vollziehende "
     "Gewalt und Rechtsprechung als unmittelbar geltendes Recht.", P),
    ("[s1b]Wir sind doch eine Aktiengesellschaft wie jede andere.", P, "Sievers"),
    ("[flucht]Der Staat bleibt gebunden, auch wenn er in privatrechtlicher Form handelt; [verstellt]eine "
     "Flucht ins Privatrecht ist ihm verstellt. [frei]Der Bürger ist prinzipiell frei, der Staat prinzipiell gebunden.", P),
    ("[gemischt]Das gilt auch für gemischtwirtschaftliche Unternehmen, an denen Staat und Private beteiligt sind, "
     "[beherr]wenn die öffentliche Hand sie beherrscht. [haelfte]In der Regel heißt das: Mehr als die Hälfte der Anteile "
     "liegt in öffentlicher Hand. [quote]Eine Grundrechtsbindung nach Quoten gibt es nicht.", P),
    ("[fraport]Die Fraport ist also unmittelbar an die Grundrechte gebunden. [eigen]Auf eigene Grundrechte, etwa ihr "
     "Eigentum, kann sie sich gegenüber der Aktivistin nicht berufen. [aktion]Und die privaten Aktionäre? Sie haben sich "
     "freiwillig beteiligt; ihre Rechte erfahren dadurch keine ungerechtfertigte Einbuße.", PS),
    # --- D Versammlungsfreiheit, Art. 8 Abs. 1 GG (Rn. 63–73) -----------------------------------------------------------
    ("[a8]Zweiter Schritt: die Versammlungsfreiheit. Artikel acht Absatz eins: Alle Deutschen haben das Recht, sich ohne "
     "Anmeldung oder Erlaubnis friedlich und ohne Waffen zu versammeln. [ort]Geschützt ist auch die Wahl des Ortes.", P),
    ("[kein]Aber Artikel acht gibt kein Zutrittsrecht zu beliebigen Orten. [nicht]Nicht geschützt sind etwa "
     "Versammlungen in Verwaltungsgebäuden, Schwimmbädern oder Krankenhäusern, [schleuse]und auch nicht hinter der "
     "Sicherheitskontrolle, wo nur Fluggäste hindürfen. [gepaeck]Ebenso wenig in Bereichen, die nur einer Funktion "
     "dienen, wie der Gepäckausgabe.", P),
    ("[forum]Geschützt ist die Versammlung dort, wo ein allgemeiner öffentlicher Verkehr eröffnet ist. [leitbild]Leitbild "
     "ist das öffentliche Forum: ein Ort mit Läden, Cafés und Flächen zum Flanieren, offen für viele verschiedene "
     "Tätigkeiten. [ffm]So ist der Frankfurter Flughafen in wesentlichen Bereichen gestaltet. [eingriff]Das unbefristete "
     "Verbot für den ganzen Flughafen ist deshalb ein Eingriff.", P),
    # --- E Meinungsfreiheit, Art. 5 Abs. 1 Satz 1 GG (Rn. 97–100) ----------------------------------------------------------
    ("[a5]Dazu kommt die Meinungsfreiheit aus Artikel fünf Absatz eins. [blatt]Flugblätter zu verteilen ist eine "
     "geschützte Form, eine Meinung zu verbreiten. [raum]Anders als die Versammlung braucht sie keinen besonderen Raum: "
     "Sie gilt überall, wo man tatsächlich Zugang hat.", PS),
    # --- F Rechtfertigung (Rn. 76–79, 86–107) ------------------------------------------------------------------------------
    ("[schranke]Dritter Schritt: die Rechtfertigung. [himmel]Eine Versammlung im Terminal gilt als Versammlung unter "
     "freiem Himmel, obwohl sie überdacht ist, denn sie trifft mitten im Terminal auf das allgemeine Publikum. "
     "[hausr]Deshalb darf sie nach Artikel acht Absatz zwei beschränkt werden, auch auf Grund des Hausrechts aus den "
     "Paragrafen neunhundertdrei und tausendvier BGB. [allg]Für die Meinungsfreiheit ist das Hausrecht ein allgemeines "
     "Gesetz.", P),
    ("[zweck]Aber die Fraport darf ihr Hausrecht nicht nach Belieben nutzen, sondern nur für legitime Zwecke des "
     "Gemeinwohls. [sicher]Das sind vor allem die Sicherheit und die Funktionsfähigkeit des Flughafens. [wohl]Kein "
     "legitimer Zweck ist eine Wohlfühlatmosphäre ohne politische Diskussionen.", P),
    ("[s2b]Und wenn eine Demonstration den Betrieb im Terminal stört?", P, "Sievers"),
    ("[mehr]Dann darf der Betreiber mehr beschränken als auf der Straße: [gross]etwa Großdemonstrationen untersagen, "
     "Trommeln oder Megafone verbieten, [luft]oder Flugblätter hinter der Sicherheitskontrolle von einer Erlaubnis "
     "abhängig machen. [pauschal]Ein pauschales Verbot aber, ohne konkrete Gefahr, unbefristet und für den "
     "ganzen Flughafen, ist unverhältnismäßig; [erlaub]ebenso eine allgemeine Erlaubnispflicht für Versammlungen und "
     "Flugblätter.", P),
    # --- G Ergebnis und Bedeutung (Tenor, Rn. 44, 59; 1 BvR 3080/09 Rn. 32, 41) -----------------------------------------------
    ("[erg]Ergebnis: Die Verfassungsbeschwerde hat Erfolg. Die Urteile verletzen die Aktivistin in ihrer "
     "Versammlungsfreiheit und ihrer Meinungsfreiheit. [zurueck]Sie werden aufgehoben.", P),
    ("[privu]Und ein rein privates Unternehmen? Es ist in der Regel nur mittelbar gebunden: Die Grundrechte wirken über das "
     "Zivilrecht. [stadion]So beim Stadionverbot: Ein Verein darf Fans nicht ohne sachlichen Grund von einem Spiel "
     "ausschließen, das er einem großen Publikum geöffnet hat.", PS),
    # --- H Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei einem Unternehmen in Privatrechtsform prüfst du zuerst die Grundrechtsbindung. Frag: Wem "
     "gehört mehr als die Hälfte der Anteile? [tipp2]Und denk an Artikel acht Absatz zwei: "
     "Im Terminal gilt die Versammlung als eine unter freiem Himmel.", PS),
    # --- I Prüfschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k0]Vorab: Grundrechtsbindung nach Artikel eins Absatz drei, bei gemischten Unternehmen durch "
     "Beherrschung. [k1]Römisch eins: Schutzbereich, eine Versammlung an einem Ort allgemeinen kommunikativen Verkehrs. "
     "[k2]Römisch zwei: Eingriff. [k3]Römisch drei: Rechtfertigung, Schranke aus Artikel acht Absatz zwei, Hausrecht, "
     "legitimer Zweck und Verhältnismäßigkeit. [k4]Danach die Meinungsfreiheit entsprechend.", PS),
    # --- J Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Staat bleibt an die Grundrechte gebunden, auch als Aktiengesellschaft. [m2]Und wo er ein "
     "öffentliches Forum eröffnet, darf er Versammlungen und Flugblätter nicht pauschal verbieten.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
