"""Folge 088 · Rücksichtnahmegebot: Der Riesenbau neben deinem Einfamilienhaus (Mo · Der Fall · Öffentliches Recht/Baurecht).
Übungsfall nach dem Hook des Themenplans: Frau Kolbe wohnt in einem eingeschossigen Einfamilienhaus am Stadtrand (kein
Bebauungsplan, ringsum ein- und zweigeschossige Einfamilienhäuser). Herr Reimers erhält die Baugenehmigung für einen
achtgeschossigen Wohnblock (25 m hoch, 50 m lang, 14 m vor ihrem Haus, quer vor dem ganzen Garten); die Abstandsflächen der
Landesbauordnung sind eingehalten. Frau Kolbe klagt.
Kern: Drittanfechtung, Klagebefugnis § 42 II VwGO, Schutznormtheorie, § 113 I 1 VwGO; drittschützende Normen im Überblick
(Abstandsflächen, Gebietserhaltungsanspruch – BVerwG 4 C 6.20 Rn. 8, 4 B 46.19 Rn. 5 –, Maß nicht drittschützend – BVerwG
4 C 7.17 Rn. 21, OVG NRW 10 B 1713/08 Rn. 8); Rücksichtnahmegebot: Herkunft (§ 35 III – BVerwG 4 B 72.06 Rn. 8; § 34 I 1
„einfügt“ – Wortlautkarte, BVerwG 4 B 50.17 Rn. 4; § 15 I 2 BauNVO – Wortlautkarte, BVerwG 4 C 8.11 Rn. 16; § 31 II BauGB,
BVerwG 4 C 7.17 Rn. 12), Maßstab (BVerwGE 52, 122 <126>, wiedergegeben in BVerwG 4 B 52.15 Rn. 12), Verschattung (OVG NRW
7 A 1791/19 Rn. 42), Abstandsflächen als Indiz (BVerwG 4 B 50.17 Rn. 4, 4 B 52.15 Rn. 9), gleiche Höhe (4 B 52.15 Rn. 10),
erdrückende/abriegelnde Wirkung (OVG NRW 7 A 1791/19 Rn. 39; BVerwG 4 B 72.06 Rn. 9); Ergebnis; Eilrechtsschutz nur Verweis
(§ 212a I BauGB, §§ 80a III, 80 V VwGO); Klausurtipp, Schema, Merksatz (Lexi).
Fiktive Figuren: Frau Kolbe (hilde), Herr Reimers (stephan). Belege je Aussage: RECHTSSTAND.md. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Kolbe": "hilde", "Reimers": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Garten, Wohnblock, Baugenehmigung -------------------------------------------------------------------------
    ("[fall]Frau Kolbe wohnt seit vierzig Jahren in ihrem kleinen Einfamilienhaus am Stadtrand. [garten]Ringsum stehen nur "
     "Einfamilienhäuser, einen Bebauungsplan gibt es nicht. Ihr Garten liegt in der Sonne. [reimers]Auf dem Grundstück "
     "südlich davon plant Herr Reimers einen Wohnblock.", 0.2),
    ("[re1]Hier entstehen acht Geschosse mit vierzig Wohnungen. Die Abstandsflächen halte ich ein.", 0.3, "Reimers"),
    ("[genehm]Die Bauaufsichtsbehörde erteilt ihm die Baugenehmigung. [masse]Der Block wird fünfundzwanzig Meter hoch und "
     "fünfzig Meter lang, er steht vierzehn Meter vor ihrem Haus, quer vor dem ganzen Garten. [schatten]Der Garten läge "
     "fortan im Schatten.", 0.2),
    ("[ko1]Der Klotz nimmt mir ja die ganze Sonne! Dagegen klage ich.", 0.3, "Kolbe"),
    ("[frage]Kann Frau Kolbe die Baugenehmigung ihres Nachbarn zu Fall bringen?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C A. Zulässigkeit: Drittanfechtung, Klagebefugnis, Schutznormtheorie --------------------------------------------------
    ("[klage]Frau Kolbe greift eine Genehmigung an, die einem anderen erteilt wurde: Das ist die Anfechtungsklage eines "
     "Dritten. [p42]Klagebefugt ist sie nach Paragraf zweiundvierzig Absatz zwei aber nur, wenn sie geltend macht, in "
     "eigenen Rechten verletzt zu sein. [schutz]Nach der Schutznormtheorie hilft ihr nur eine Norm, die zumindest auch sie "
     "als Nachbarin schützt, also eine drittschützende Norm. [objektiv]Dass die Genehmigung objektiv rechtswidrig ist, "
     "genügt nicht, auch nicht in der Begründetheit: Nach Paragraf hundertdreizehn Absatz eins muss sie gerade dadurch "
     "in ihren Rechten verletzt sein.", P),
    # --- D B. Begründetheit: drittschützende Normen im Überblick ----------------------------------------------------------------
    ("[ueber]Welche drittschützende Norm kommt in Frage? [abst]Die Abstandsflächen der Landesbauordnung schützen auch den "
     "Nachbarn, hier sind sie aber eingehalten. [gebiet]Die Art der baulichen Nutzung gibt jedem Eigentümer im Baugebiet "
     "einen Gebietserhaltungsanspruch, doch ein Wohnblock ist Wohnen wie ihr Haus. [mass]Dass acht Geschosse nicht zu den "
     "kleinen Häusern ringsum passen, hilft ihr allein nicht: Das Maß der baulichen Nutzung schützt den Nachbarn in der "
     "Regel nicht. [bleibt]Es bleibt das Gebot der Rücksichtnahme.", P),
    # --- E Herkunft des Rücksichtnahmegebots -----------------------------------------------------------------------------------
    ("[herkunft]Einen eigenen Paragrafen hat es nicht. [aussen]Im Außenbereich ist es ein unbenannter öffentlicher Belang "
     "nach Paragraf fünfunddreißig Absatz drei. [wl34]Im Innenbereich steckt es in Paragraf vierunddreißig Absatz eins Satz "
     "eins: Das Vorhaben muss sich in die Eigenart der näheren Umgebung einfügen. [einf]Wer auf die Nachbarn keine "
     "Rücksicht nimmt, fügt sich nicht ein.", P),
    ("[wl15]Gilt ein Bebauungsplan, nennt es Paragraf fünfzehn Absatz eins Satz zwei der Baunutzungsverordnung: Anlagen sind "
     "auch unzulässig, wenn von ihnen Belästigungen oder Störungen ausgehen können, die unzumutbar sind. [befr]Und bei einer "
     "Befreiung von seinen Festsetzungen verlangt Paragraf einunddreißig Absatz zwei, dass die Abweichung auch unter "
     "Würdigung nachbarlicher Interessen mit den öffentlichen Belangen vereinbar ist.", P),
    # --- F Maßstab -------------------------------------------------------------------------------------------------------------
    ("[mst]Wann ist ein Vorhaben rücksichtslos? Grundlegend ist ein Urteil des Bundesverwaltungsgerichts von "
     "neunzehnhundertsiebenundsiebzig. [je1]Je empfindlicher und schutzwürdiger die Stellung des Nachbarn ist, desto mehr "
     "Rücksicht kann er verlangen. [je2]Je verständlicher und unabweisbarer die Interessen des Bauherrn sind, desto weniger "
     "Rücksicht muss er nehmen. [zumut]Abzuwägen ist, was beiden nach Lage der Dinge zuzumuten ist.", P),
    # --- G Subsumtion: Verschattung, Indiz, erdrückende Wirkung ------------------------------------------------------------------
    ("[schat]Zuerst der Schatten. In einem bebauten Viertel musst du in der Regel hinnehmen, dass das Nachbargrundstück "
     "bebaut wird und dein Grundstück zeitweise verschattet. [indiz]Auch die eingehaltenen Abstandsflächen sprechen gegen "
     "Frau Kolbe: Für Licht und Sonne sind sie ein starkes Indiz. [regel]Die Regel, dass dann keine Rücksichtslosigkeit "
     "vorliegt, setzt aber voraus, dass sich der Bau auch sonst einfügt. Acht Geschosse zwischen Einfamilienhäusern tun "
     "das nicht.", P),
    ("[erdr]Entscheidend ist die erdrückende Wirkung. Sie liegt vor, wenn ein Bau wegen seiner Ausmaße dem "
     "Nachbargrundstück förmlich die Luft nimmt, wenn ein Gefühl des Eingemauertseins entsteht [riegel]oder wenn er das "
     "Grundstück regelrecht abriegelt. [hoehe]Bei gleicher Höhe kommt das grundsätzlich nicht in Betracht. Hier hat der "
     "Block acht Geschosse, ihr Haus eines. [fall2]Fünfundzwanzig Meter hoch, fünfzig Meter lang, vierzehn Meter vor dem "
     "Haus: Ihr Grundstück wirkt daneben nur noch wie eine Fläche, die der Block beherrscht. [wohn]Neue Wohnungen sind ein "
     "verständliches Interesse, rechtfertigen das aber nicht. [rlos]Das Vorhaben ist rücksichtslos.", P),
    # --- H Ergebnis, Eilrechtsschutz ---------------------------------------------------------------------------------------------
    ("[erg]Die Baugenehmigung verstößt gegen das Rücksichtnahmegebot und verletzt Frau Kolbe in ihren Rechten. Ihre Klage "
     "ist begründet, das Gericht hebt die Genehmigung auf. [eil]Weil die Klage den Bau nach Paragraf zweihundertzwölf a des "
     "Baugesetzbuchs nicht aufhält, braucht sie zusätzlich Eilrechtsschutz nach Paragraf achtzig a und achtzig Absatz "
     "fünf. Dazu gibt es ein eigenes Video.", 0.3),
    ("[ko2]Dann muss Herr Reimers eben rücksichtsvoller planen.", PS, "Kolbe"),
    # --- I Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne sauber. [tipp1]In der Klagebefugnis genügt, dass eine Verletzung des Rücksichtnahmegebots "
     "möglich ist. [tipp2]Erst in der Begründetheit prüfst du, ob die Genehmigung rechtswidrig ist und die Nachbarin gerade "
     "dadurch in ihren Rechten verletzt. [tipp3]Und nenne die Herkunft: im Innenbereich das Einfügen nach Paragraf "
     "vierunddreißig.", PS),
    # --- J Klausurschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]A, Zulässigkeit: [s2]Anfechtungsklage gegen die Baugenehmigung, [s3]Klagebefugnis über "
     "eine drittschützende Norm. [s4]B, Begründetheit: [s5]Verstoß gegen eine drittschützende Norm, [s6]etwa Abstandsflächen "
     "oder Gebietserhaltungsanspruch, [s7]sonst das Rücksichtnahmegebot mit Abwägung der Zumutbarkeit und erdrückender "
     "Wirkung, [s8]und dadurch die Verletzung eigener Rechte.", PS),
    # --- K Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Als Nachbar kannst du nur drittschützende Normen rügen. [m2]Das Rücksichtnahmegebot schützt dich vor "
     "einem Bau, der dir unzumutbar ist, etwa weil er dein Grundstück erdrückt. Schatten allein genügt selten.", 1.4),
]
