"""Folge 110 · Schutznormtheorie: Klagen gegen die Genehmigung eines anderen (Mi · Examenswissen · Schema).
Übungsfall nach dem Hook des Themenplans („Neben deinem Haus soll eine Shisha-Bar mit Außenbereich öffnen – du willst die
Erlaubnis angreifen“), Beispielland Nordrhein-Westfalen (Gaststättengesetz des Bundes gilt dort nach Art. 125a I GG fort):
Frau Hoppe eröffnet im Nachbarhaus eine Shisha-Bar, die auch Bier und Cocktails ausschenkt; die Stadt erteilt ihr die
Gaststättenerlaubnis für Gasträume und eine Terrasse mit 40 Plätzen, Betrieb bis 24 Uhr. Die Terrasse liegt unter dem
Schlafzimmerfenster von Frau Brüning, die Anfechtungsklage erhebt. Abgrenzung zu 088/090 (Baugenehmigung, Rücksichtnahme):
hier eine gaststättenrechtliche Erlaubnis, Schwerpunkt Methode.
Schema: 1. Ausgangspunkt § 42 II VwGO (Wortlautkarte, Verweis 105): Dritte ist nicht Adressatin; 2. Schutznormtheorie
(BVerwG 3 C 5.23 Rn. 40; 6 C 2.23 Rn. 24) in drei Fragen: a) welche Norm – § 4 I 1 Nr. 3 GastG (Wortlautkarte), b) schützt sie
auch Einzelne – Wortlaut (§ 3 I BImSchG „Nachbarschaft“), Systematik (§ 5 I Nr. 3 GastG), Zweck; BVerwG 8 C 3.19 Rn. 39,
OVG NRW 4 B 652/15 Rn. 27; c) gehört die Klägerin zum geschützten Kreis (Einwirkungsbereich; vgl. 3 C 5.23 Rn. 43), Möglichkeit
(6 C 2.23 Rn. 13); 3. typische Normen ja/nein (Lärmschutz GastG; § 5 I Nr. 1 BImSchG; Abstandsflächen – 4 B 52.15 Rn. 9;
Gebietserhaltung – 4 C 6.20 Rn. 8; nein: Vorsorge § 5 I Nr. 2 BImSchG – 7 B 2.08 Rn. 15; Maß nur nach Plangeberwillen –
4 C 7.17 Rn. 14); 4. Grundrechte nur hilfsweise (4 C 3.08 Rn. 15). Ergebnis: klagebefugt, Begründetheit offen.
Fiktive Figuren: Frau Brüning (hilde), Frau Hoppe (lucy), der Richter (stephan). Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Brüning": "hilde", "Hoppe": "lucy", "Richter": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Wohnstraße, Shisha-Bar mit Terrasse, Gaststättenerlaubnis ------------------------------------------------
    ("[fall]Frau Brüning wohnt seit dreißig Jahren in einer ruhigen Wohnstraße. [bar]Im Nachbarhaus eröffnet Frau Hoppe "
     "eine Shisha-Bar, mit einer Terrasse direkt unter dem Schlafzimmerfenster von Frau Brüning. [erl]Die Stadt erteilt ihr die "
     "Gaststättenerlaubnis, auch für die Terrasse, bis Mitternacht.", 0.2),
    ("[ho1]Bei uns sitzt man draußen bis Mitternacht. Die Erlaubnis habe ich!", 0.3, "Hoppe"),
    ("[br1]Bis Mitternacht unter meinem Fenster? Dann kann ich nicht mehr schlafen. Ich klage gegen diese Erlaubnis.", 0.3,
     "Brüning"),
    ("[frage]Aber die Erlaubnis richtet sich gar nicht an Frau Brüning. [frage2]Darf sie die Genehmigung einer anderen "
     "anfechten?", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Ausgangspunkt § 42 II -----------------------------------------------------------------------------------------
    ("[p42]Erstens, der Ausgangspunkt: Paragraf zweiundvierzig Absatz zwei. Klagebefugt ist nur, wer geltend macht, in "
     "seinen Rechten verletzt zu sein. [adr]Die Adressatentheorie hilft Frau Brüning nicht: Adressatin ist Frau Hoppe, "
     "und die Erlaubnis begünstigt sie. [v105]Die Grundlagen zeigt unser Video zur Klagebefugnis.", P),
    # --- D 2. Schutznormtheorie ---------------------------------------------------------------------------------------------
    ("[snt]Zweitens, die Schutznormtheorie. Ein Dritter braucht eine Norm, die zumindest auch ihn schützt. [kreis]Das "
     "Bundesverwaltungsgericht verlangt: Die Norm muss das geschützte private Interesse, die Art seiner Verletzung und den Kreis der geschützten "
     "Personen hinreichend deutlich abgrenzen. [allg]Es genügt ein Personenkreis, der sich hinreichend von der "
     "Allgemeinheit unterscheidet. [reflex]Wer nur reflexartig mitbetroffen ist, hat kein eigenes Recht.", P),
    # --- E Frage a: Welche Norm? Wortlautkarte § 4 I 1 Nr. 3 GastG ----------------------------------------------------------
    ("[fa]Das prüfst du in drei Fragen. Erstens: Welche Norm kommt in Betracht? [nrw]Wir spielen den Fall in "
     "Nordrhein-Westfalen. Dort gilt das Gaststättengesetz des Bundes fort, andere Länder haben eigene Gesetze. [wl4]Nach "
     "Paragraf vier Absatz eins Satz eins Nummer drei ist die Erlaubnis zu versagen, wenn der Betrieb im Hinblick auf "
     "seine örtliche Lage schädliche Umwelteinwirkungen im Sinne des Bundes-Immissionsschutzgesetzes befürchten lässt.", P),
    # --- F Frage b: Schützt sie auch Einzelne? Wortlaut, Systematik, Zweck ---------------------------------------------------
    ("[fb]Zweitens: Schützt diese Norm auch Einzelne? Das klärst du durch Auslegung. [wort]Zum Wortlaut: Schädliche "
     "Umwelteinwirkungen sind nach dem Bundes-Immissionsschutzgesetz Einwirkungen wie Geräusche, die erhebliche Belästigungen für die "
     "Allgemeinheit oder die Nachbarschaft herbeiführen können. [sys]Zur Systematik: Paragraf fünf des Gaststättengesetzes erlaubt Auflagen zum "
     "Schutz der Bewohner der Nachbargrundstücke. [zweck]Zum Zweck: Die Norm soll den Konflikt zwischen Gaststätte und "
     "Wohnen lösen. [ja]Insoweit ist sie drittschützend, so sieht es auch das Bundesverwaltungsgericht.", P),
    # --- G Frage c: Gehört die Klägerin zum geschützten Kreis? ----------------------------------------------------------------
    ("[fc]Drittens: Gehört Frau Brüning zum geschützten Kreis? [nachb]Zur Nachbarschaft gehört, wer im Einwirkungsbereich "
     "des Betriebs wohnt. Frau Brüning wohnt direkt über der Terrasse. [moegl]Dass laute Gespräche bis Mitternacht sie "
     "erheblich belästigen, ist jedenfalls nicht offensichtlich ausgeschlossen. [gegen]Anders wäre es bei jemandem, der drei "
     "Straßen weiter wohnt, vom Lärm nichts hört und Shisha-Bars einfach nicht mag.", P),
    # --- H 3. Typische Normen: drittschützend ja/nein -------------------------------------------------------------------------
    ("[tab]Drittens, typische Normen im Überblick. [t1]Drittschützend ist der Schutz vor schädlichen Umwelteinwirkungen im "
     "Gaststättenrecht [t2]und ebenso die Schutzpflicht für genehmigungsbedürftige Anlagen nach Paragraf fünf Absatz eins "
     "Nummer eins des Bundes-Immissionsschutzgesetzes. [t3]Im Baurecht schützen die Abstandsflächen der Landesbauordnung den "
     "Nachbarn, [t4]ebenso die Art der baulichen Nutzung über den Gebietserhaltungsanspruch. [bau]Mehr dazu in unseren Videos "
     "zum Rücksichtnahmegebot und zur Drittanfechtung. [t5]Nicht drittschützend ist grundsätzlich die Vorsorgepflicht nach Nummer zwei: Sie "
     "dient der Allgemeinheit. [t6]Und Festsetzungen zum Maß der baulichen Nutzung schützen den Nachbarn nur, wenn die "
     "Gemeinde als Plangeber das will.", P),
    # --- I 4. Grundrechte nur hilfsweise ------------------------------------------------------------------------------------
    ("[grund]Viertens, die Grundrechte. Als Schutznorm helfen sie nur hilfsweise: Zuerst entscheidet das einfache Gesetz, "
     "wen es schützt.", P),
    # --- J Ergebnis ---------------------------------------------------------------------------------------------------------
    ("[erg]Frau Brüning kann sich auf den Lärmschutz im Gaststättengesetz berufen. Sie ist klagebefugt. [ri]Das "
     "Verwaltungsgericht sagt:", 0.2),
    ("[ri1]Sie sind klagebefugt, Frau Brüning. Ob die Terrasse wirklich zu laut ist, prüfen wir in der Begründetheit.", 0.6,
     "Richter"),
    # --- K Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei der Drittanfechtung nennst du schon in der Klagebefugnis die konkrete Schutznorm und begründest "
     "kurz, warum sie auch den Kläger schützt. [tipp2]In der Begründetheit zählen dann nur Verstöße gegen drittschützende "
     "Normen. Ein Fehler, der allein die Allgemeinheit betrifft, hilft dem Nachbarn nicht.", PS),
    # --- L Schema -------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema zur Klagebefugnis Dritter. [s1]Eins, der Ausgangspunkt: Paragraf zweiundvierzig Absatz zwei, der "
     "Dritte ist nicht Adressat. [s2]Zwei, die Schutznorm: [s2a]Welche Norm? [s2b]Schützt sie auch Einzelne, nach "
     "Wortlaut, Systematik und Zweck? [s2c]Gehört der Kläger zum geschützten Kreis, und ist eine Verletzung möglich? "
     "[s3]Drei, typische Schutznormen: Lärmschutz, Abstandsflächen, Gebietserhaltung, nicht die Vorsorge. [s4]Vier, "
     "Grundrechte nur hilfsweise.", PS),
    # --- M Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Genehmigung eines anderen greifst du nur mit einer Norm an, die auch dich schützt. [m2]Die Nachbarin "
     "findet sie im Lärmschutz. Wer nur dagegen ist, findet keine.", 1.4),
]
