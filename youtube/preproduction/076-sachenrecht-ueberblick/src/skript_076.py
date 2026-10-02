"""Folge 076 · Sachenrecht Überblick: Eigentum an Sachen und Grundstücken (Mo · Der Fall · Zivilrecht/Sachenrecht,
Format Schema). Ein durchgehender Beispielfall nach dem Plan-Hook („Handy, Auto, Haus – wie Eigentum übergeht, wann
guter Glaube hilft und was die Grundbucheintragung bewirkt“) mit drei Stationen:
1. Handy: Arne verkauft Nina ein Handy, das seiner Schwester gehört und ihm nur geliehen ist (§§ 929 S. 1, 932, 1006;
   kein Abhandenkommen, § 935 I; Ausnahme Geld § 935 II ein Satz). Übergabesurrogate §§ 929 S. 2, 930, 931 im Überblick.
2. Auto: Herr Kuhnert verkauft Nina den Gebrauchtwagen seines Schwagers, ohne die Zulassungsbescheinigung Teil II
   vorzulegen (§ 932 II grob fahrlässig; BGH V ZR 8/19 Rn. 29, V ZR 92/12 Rn. 11, 13, 14); Herausgabe § 985.
3. Haus: Frau Lohse ist im Grundbuch eingetragen, aber nicht Eigentümerin (§§ 873 I, 925, 311b I, 94; § 892 I 1,
   Widerspruch ein Satz, Vormerkung § 883 ein Satz).
Grundsätze Publizität, Spezialität, Abstraktion je ein Satz; Vergleichstabelle bewegliche Sache/Grundstück progressiv;
Wortlautkarten § 929 S. 1, § 932 I 1 und II, § 873 I BGB; Klausurtipp und Merksatz mit Lexi.
Figuren: Nina (julia), Arne (niklas), Herr Kuhnert (helmut), Frau Lohse (ela_froh); Lexi/Erzählerin Carla.
Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.25, 0.45

STIMMEN = {"Nina": "julia", "Arne": "niklas", "Kuhnert": "helmut", "Lohse": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: das Handy -------------------------------------------------------------------------------------------
    ("[fall]Nina kauft in einem Jahr drei Dinge: ein Handy, ein Auto und ein Haus. [handy]Zuerst das Handy. Ihr "
     "Bekannter Arne bietet es ihr an.", 0.25),
    ("[ar1]Mein altes Handy. Für hundertfünfzig Euro gehört es dir.", 0.25, "Arne"),
    ("[zahlt]Nina zahlt, und Arne gibt ihr das Handy. [schwester]Was Nina nicht weiß: Das Handy gehört der Schwester "
     "von Arne. Sie hat es ihm nur geliehen.", 0.3),
    # --- A2 Fall: das Auto --------------------------------------------------------------------------------------------
    ("[auto]Dann das Auto. Auf einem Parkplatz verkauft Herr Kuhnert ihr einen Gebrauchtwagen für sechstausend Euro.", 0.25),
    ("[ni1]Und wo ist die Zulassungsbescheinigung?", 0.25, "Nina"),
    ("[ku1]Die schicke ich Ihnen nächste Woche. Hier ist der Schlüssel.", 0.25, "Kuhnert"),
    ("[faehrt]Nina zahlt und fährt los. [schwager]Das Auto gehört aber dem Schwager von Herrn Kuhnert. Er hat es ihm "
     "nur geliehen.", 0.3),
    # --- A3 Fall: das Haus --------------------------------------------------------------------------------------------
    ("[haus]Zuletzt das Haus. Frau Lohse verkauft Nina ein kleines Haus. [notar]Beim Notar schließen beide den "
     "Kaufvertrag und erklären die Auflassung.", 0.25),
    ("[lo1]Ich stehe im Grundbuch. Das Haus gehört mir.", 0.25, "Lohse"),
    ("[falsch]Doch das Grundbuch ist falsch: Die Übertragung an Frau Lohse war unwirksam, das Haus gehört noch ihrem "
     "Bruder. Nina weiß davon nichts. [frage]Wird Nina trotzdem Eigentümerin? [frage2]Am Handy, am Auto und am Haus?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Grundsätze -------------------------------------------------------------------------------------------------
    ("[grund]Zuerst drei Grundsätze des Sachenrechts. [publ]Publizität: Wem eine Sache gehört, soll man erkennen können, "
     "bei beweglichen Sachen am Besitz, bei Grundstücken am Grundbuch. [spez]Spezialität: Übertragen wird stets eine "
     "bestimmte Sache. [abstr]Und Abstraktion: Die Übereignung ist ein eigenes Geschäft, grundsätzlich "
     "unabhängig vom Kaufvertrag. [mehr]Mehr dazu in eigenen Videos.", PS),
    # --- D § 929 Satz 1 (Wortlaut) ------------------------------------------------------------------------------------
    ("[p929]Für bewegliche Sachen gilt Paragraf neunhundertneunundzwanzig Satz eins: [w929]Zur Übertragung des Eigentums "
     "an einer beweglichen Sache ist erforderlich, dass der Eigentümer die Sache dem Erwerber übergibt und beide darüber "
     "einig sind, dass das Eigentum übergehen soll.", P),
    ("[einig]Nina und Arne sind sich einig, [ueberg]und Arne übergibt ihr das Handy. [berecht]Aber übergeben muss der "
     "Eigentümer. Arne ist nicht berechtigt.", P),
    ("[surr]Übrigens kann die Übergabe ersetzt werden: [s2]Hat der Erwerber die Sache schon, genügt nach Satz zwei die "
     "Einigung. [p930]Behält der Veräußerer sie, genügt nach Paragraf neunhundertdreißig ein Besitzmittlungsverhältnis. "
     "[p931]Und hat sie ein Dritter, genügt die Abtretung des Herausgabeanspruchs, Paragraf neunhunderteinunddreißig.", PS),
    # --- E § 932 (Wortlaut) -------------------------------------------------------------------------------------------
    ("[p932]Hilft Nina der gute Glaube? Paragraf neunhundertzweiunddreißig Absatz eins: [w932]Der Erwerber wird auch "
     "dann Eigentümer, wenn die Sache nicht dem Veräußerer gehört, es sei denn, dass er nicht in gutem Glauben ist. "
     "[w932b]Nach Absatz zwei schaden ihm Kenntnis und grobe Fahrlässigkeit.", P),
    ("[schein]Grundlage ist der Rechtsschein des Besitzes: Für den Besitzer wird vermutet, dass er Eigentümer ist, "
     "Paragraf tausendsechs. [nina1]Arne hatte das Handy, und Nina hatte keinen Grund zu zweifeln. [nina2]Sie ist in "
     "gutem Glauben.", P),
    # --- F § 935 ------------------------------------------------------------------------------------------------------
    ("[p935]Anders wäre es, wenn das Handy der Schwester gestohlen worden wäre. Nach Paragraf neunhundertfünfunddreißig "
     "Absatz eins gibt es keinen gutgläubigen Erwerb, wenn die Sache dem Eigentümer abhandengekommen ist. [geld]Eine "
     "Ausnahme gilt nach Absatz zwei etwa für Geld. [freiw]Abhandengekommen heißt: Der Besitz ging unfreiwillig verloren. "
     "Die Schwester hat das Handy aber freiwillig verliehen. [nina4]Nina wird also Eigentümerin.", PS),
    # --- G Auto -------------------------------------------------------------------------------------------------------
    ("[auto2]Beim Auto liegen [auto3]Einigung und Übergabe vor, aber Herr Kuhnert ist nicht Eigentümer. "
     "[nabh]Abhandengekommen ist das Auto nicht, der Schwager hat es freiwillig verliehen. Es kommt auf den guten "
     "Glauben an.", P),
    ("[zb2]Beim Gebrauchtwagen reicht nach dem Bundesgerichtshof der Besitz allein als Rechtsschein nicht. [zb3]Der Käufer muss sich "
     "regelmäßig mindestens die Zulassungsbescheinigung Teil zwei zeigen lassen, um die Berechtigung des Verkäufers zu "
     "prüfen. [grob]Nina hat darauf verzichtet. Das ist grob fahrlässig. [auto4]Sie wird nicht Eigentümerin.", PS),
    # --- H Haus: §§ 873, 925 ------------------------------------------------------------------------------------------
    ("[p873]Und das Haus, also das Grundstück? [w873]Paragraf achthundertdreiundsiebzig Absatz eins verlangt die "
     "Einigung des Berechtigten mit dem Erwerber und die Eintragung in das Grundbuch.", P),
    ("[p925]Diese Einigung heißt Auflassung. Nach Paragraf neunhundertfünfundzwanzig müssen beide sie bei gleichzeitiger "
     "Anwesenheit vor einer zuständigen Stelle erklären, etwa vor einem Notar. [eintr]Eigentümerin wird Nina aber erst mit der Eintragung.", P),
    # --- I Haus: § 892 ------------------------------------------------------------------------------------------------
    ("[p892]Und dass Frau Lohse nicht berechtigt ist? Hier hilft der öffentliche Glaube des Grundbuchs, Paragraf "
     "achthundertzweiundneunzig: [w892]Für den Erwerber gilt der Inhalt des Grundbuchs als richtig, es sei denn, ein "
     "Widerspruch ist eingetragen oder ihm ist die Unrichtigkeit bekannt. [kennt]Schaden kann also nur Kenntnis, nicht "
     "grobe Fahrlässigkeit. [nina3]Nina weiß nichts, und ein Widerspruch fehlt. Mit der Eintragung wird sie Eigentümerin.", P),
    ("[wid]Hätte der Bruder vorher einen Widerspruch eintragen lassen, wäre der Erwerb gescheitert. [vorm]Bis zur "
     "Eintragung kann eine Vormerkung den Anspruch eines Käufers gegen spätere Verfügungen schützen, Paragraf "
     "achthundertdreiundachtzig.", PS),
    # --- J Vergleich und Ergebnis -------------------------------------------------------------------------------------
    ("[vgl]Im Vergleich: [v1]Bewegliche Sachen gehen durch Einigung und Übergabe über, Grundstücke durch Auflassung und "
     "Eintragung. [v2]Den Rechtsschein trägt einmal der Besitz, einmal das Grundbuch. [v3]Bei beweglichen Sachen schaden "
     "Kenntnis und grobe Fahrlässigkeit, beim Grundstück nur Kenntnis. [v4]Und die Sperre für abhandengekommene Sachen "
     "gibt es nur bei beweglichen Sachen.", P),
    ("[erg]Ergebnis: [e1]Das Handy gehört Nina. [e2]Das Auto bleibt beim Schwager. [e3]Und am Haus wird sie mit der "
     "Eintragung Eigentümerin.", PS),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe beim Erwerb vom Nichtberechtigten in dieser Reihenfolge: Paragraf "
     "neunhundertneunundzwanzig, dann neunhundertzweiunddreißig, dann neunhundertfünfunddreißig. "
     "[tipp2]Und schreibe beim Grundstück nicht grob fahrlässig. Bei Paragraf achthundertzweiundneunzig zählt nur die "
     "Kenntnis.", PS),
    # --- L Klausurschema ----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für bewegliche Sachen: [k1]Römisch eins: Einigung. [k2]Römisch zwei: Übergabe oder ein "
     "Übergabeersatz. [k3]Römisch drei: "
     "Berechtigung des Veräußerers. [k4]Fehlt sie, römisch vier: gutgläubiger Erwerb nach den Paragrafen "
     "neunhundertzweiunddreißig folgende, [k4b]ohne Abhandenkommen nach Paragraf neunhundertfünfunddreißig. [k5]Beim Grundstück: Auflassung, Eintragung und Berechtigung oder der öffentliche "
     "Glaube des Grundbuchs.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei beweglichen Sachen trägt der Besitz den guten Glauben, bei Grundstücken das Grundbuch. [m2]Und "
     "beim Grundbuch schadet nur Kenntnis oder ein Widerspruch.", 1.2),
]
