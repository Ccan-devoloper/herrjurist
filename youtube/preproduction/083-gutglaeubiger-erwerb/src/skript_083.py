"""Folge 083 · Gutgläubiger Erwerb §§ 932 ff. BGB: Eigentum vom Nichteigentümer? (Mi · Examenswissen · Zivilrecht/
Sachenrecht, Format Schema). Beispielfall nach dem Plan-Hook („Dein Freund verkauft dein geliehenes Rad an jemanden, der fest
glaubt, es gehöre ihm“): Erika leiht ihrem Freund Benno ihr Fahrrad für eine Woche. Benno verkauft es als seines an Selma für
200 €, sie zahlt, er übergibt es. Am Sonntag sieht Erika ihr Rad bei Selma.
Schema § 929 S. 1 i. V. m. § 932 BGB: (1) Rechtsgeschäft als Verkehrsgeschäft, (2) Einigung und Übergabe (Verweis auf Folge 080),
(3) Nichtberechtigung, (4) Rechtsschein des Besitzes/Besitzverschaffungsmacht, (5) guter Glaube § 932 II (Beweislast aus dem
Satzbau „es sei denn“, BGH V ZR 148/21 Rn. 14), (6) kein Abhandenkommen § 935 I (Leihe = freiwillig); Abwandlung gestohlenes
Rad; § 935 II ein Satz; §§ 933, 934 je ein Satz; § 936 ein Satz; § 816 I 1 ein Satz (Verweis auf Folge 073).
Wortlautkarten § 932 Abs. 1 S. 1, Abs. 2 und § 935 Abs. 1 S. 1 BGB; Klausurtipp und Merksatz mit Lexi.
Figuren: Erika (hilde), Benno (christian), Selma (lucy); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Erika": "hilde", "Benno": "christian", "Selma": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Leihe -------------------------------------------------------------------------------------------
    ("[fall]Erika verleiht ihr Fahrrad für eine Woche an ihren Freund Benno.", 0.25),
    ("[er1]Hier, bis Sonntag. Pass gut darauf auf!", 0.25, "Erika"),
    ("[be1]Danke! Am Sonntag hast du es zurück.", 0.3, "Benno"),
    # --- A2 Fall: der Verkauf -----------------------------------------------------------------------------------------
    ("[knapp]Doch Benno ist knapp bei Kasse. [selma]Er bietet das Rad Selma an und gibt es als seines aus.", 0.25),
    ("[be2]Das ist mein Rad. Für zweihundert Euro gehört es dir.", 0.25, "Benno"),
    ("[zahlt]Selma hat keinen Grund zu zweifeln. Sie zahlt, [gibt]Benno gibt ihr das Rad, und beide sind sich einig, "
     "dass es jetzt ihr gehört.", 0.3),
    # --- A3 Fall: der Sonntag -----------------------------------------------------------------------------------------
    ("[sonntag]Am Sonntag sieht Erika ihr Rad wieder, mit Selma darauf.", 0.25),
    ("[er2]Das ist mein Fahrrad! Gib es mir zurück.", 0.25, "Erika"),
    ("[se1]Nein, ich habe es gekauft. Es gehört mir.", 0.3, "Selma"),
    ("[frage]Wer ist jetzt Eigentümerin, Erika oder Selma? [frage2]Kann man Eigentum vom Nichteigentümer erwerben?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Ausgangspunkt und § 932 Abs. 1 Satz 1 (Wortlaut) ----------------------------------------------------------------
    ("[p985]Erika könnte das Rad nach Paragraf neunhundertfünfundachtzig herausverlangen, wenn sie noch Eigentümerin ist. "
     "[nb0]Benno durfte es nicht übereignen. [p932]Doch Paragraf neunhundertzweiunddreißig Absatz eins Satz eins sagt: "
     "[w932]Durch eine nach Paragraf neunhundertneunundzwanzig erfolgte Veräußerung wird der Erwerber auch dann "
     "Eigentümer, wenn die Sache nicht dem Veräußerer gehört, es sei denn, dass er zu der Zeit, zu der er nach diesen "
     "Vorschriften das Eigentum erwerben würde, nicht in gutem Glauben ist.", PS),
    ("[sechs]Geprüft werden sechs Punkte: [v1]ein Rechtsgeschäft, [v2]Einigung und Übergabe, [v3]Nichtberechtigung, "
     "[v4]Rechtsschein, [v5]guter Glaube [v6]und kein Abhandenkommen.", PS),
    # --- D 1. Verkehrsgeschäft ----------------------------------------------------------------------------------------------
    ("[rg]Erstens: ein Rechtsgeschäft, und zwar ein Verkehrsgeschäft. Veräußerer und Erwerber dürfen weder rechtlich noch "
     "wirtschaftlich identisch sein. [rg2]Benno und Selma sind zwei verschiedene Personen.", P),
    # --- E 2. Einigung und Übergabe -----------------------------------------------------------------------------------------
    ("[eu]Zweitens: Einigung und Übergabe nach Paragraf neunhundertneunundzwanzig Satz eins. Wie das funktioniert, erklärt "
     "das Video zur Übereignung. [eu2]Benno und Selma sind sich einig, und er gibt ihr das Rad in die Hand.", P),
    # --- F 3. Nichtberechtigung -----------------------------------------------------------------------------------------------
    ("[nb]Drittens: Benno ist nicht berechtigt. Das Rad gehört Erika, und sie hat ihm den Verkauf nicht erlaubt. "
     "[luecke]Genau diese Lücke kann der gute Glaube schließen, nur diese.", P),
    # --- G 4. Rechtsschein -------------------------------------------------------------------------------------------------------
    ("[rs]Viertens: der Rechtsschein. Grundlage des gutgläubigen Erwerbs ist der Besitz. [bvm]Der Veräußerer muss dem "
     "Erwerber den Besitz verschaffen können, man spricht von Besitzverschaffungsmacht. [rs2]Benno hatte das Rad und hat es "
     "Selma übergeben.", PS),
    # --- H 5. guter Glaube, § 932 Abs. 2 (Wortlaut) ------------------------------------------------------------------------------
    ("[gg]Fünftens: der gute Glaube. [w932b]Nach Absatz zwei ist der Erwerber nicht in gutem Glauben, wenn ihm bekannt oder "
     "infolge grober Fahrlässigkeit unbekannt ist, dass die Sache nicht dem Veräußerer gehört. [grob]Grob fahrlässig ist, "
     "wer die erforderliche Sorgfalt in ungewöhnlich großem Maße verletzt "
     "und übersieht, was jedem hätte einleuchten müssen. [nachf]Eine allgemeine Nachforschungspflicht hat "
     "der Erwerber aber nicht. [zeit]Maßgeblich ist der Moment des Erwerbs, hier die Übergabe.", P),
    ("[bew]Und achte auf den Satzbau: es sei denn. [bew2]Deshalb muss nicht Selma ihren guten Glauben beweisen. Wer den "
     "Erwerb bestreitet, hier Erika, muss beweisen, dass Selma bösgläubig war. So sieht es auch der Bundesgerichtshof. "
     "[selma2]Selma hatte keinen Grund zu zweifeln. Sie ist in gutem Glauben.", PS),
    # --- I 6. kein Abhandenkommen, § 935 Abs. 1 Satz 1 (Wortlaut) -----------------------------------------------------------------
    ("[ab]Sechstens: Die Sache darf nicht abhandengekommen sein. [w935]Paragraf neunhundertfünfunddreißig Absatz eins "
     "Satz eins: Der Erwerb des Eigentums auf Grund der Paragrafen neunhundertzweiunddreißig bis neunhundertvierunddreißig "
     "tritt nicht ein, wenn die Sache dem Eigentümer gestohlen worden, verloren gegangen oder sonst abhanden gekommen war. "
     "[unfr]Abhanden kommt eine Sache, wenn der Eigentümer den Besitz unfreiwillig verliert.", P),
    ("[leihe]Erika hat Benno das Rad aber freiwillig geliehen, und Benno hat es freiwillig weggegeben. Kein Abhandenkommen. "
     "[erg]Ergebnis: Selma ist Eigentümerin geworden, nach Paragraf neunhundertneunundzwanzig Satz eins in Verbindung mit "
     "Paragraf neunhundertzweiunddreißig. [erg2]Erika kann das Rad von Selma nicht herausverlangen.", PS),
    # --- J Abwandlung: gestohlenes Rad --------------------------------------------------------------------------------------------
    ("[abw]Abwandlung: Ein Dieb stiehlt das Rad aus der Garage von Erika und verkauft es an Selma. [abw2]Dann ist es Erika "
     "abhandengekommen. Selma wird nicht Eigentümerin, auch wenn sie gutgläubig ist. [p935b]Ausnahmen nennt Absatz zwei, "
     "etwa für Geld und für Sachen aus einer öffentlichen Versteigerung.", PS),
    # --- K §§ 933, 934, 936 ----------------------------------------------------------------------------------------------------------
    ("[p933]Wird die Übergabe ersetzt, gelten Sonderregeln. Beim Besitzkonstitut wird der Erwerber nach Paragraf "
     "neunhundertdreiunddreißig erst Eigentümer, wenn ihm der Veräußerer die Sache übergibt. [p934]Bei der Abtretung des "
     "Herausgabeanspruchs genügt nach Paragraf neunhundertvierunddreißig die Abtretung, wenn der Veräußerer mittelbarer "
     "Besitzer ist, sonst erst der Besitzerwerb vom Dritten. [p936]Und nach Paragraf neunhundertsechsunddreißig erlöschen "
     "Rechte Dritter an der Sache, etwa ein Pfandrecht, wenn der Erwerber auch insoweit gutgläubig ist.", PS),
    # --- L Folgeanspruch: § 816 Abs. 1 Satz 1 --------------------------------------------------------------------------------------
    ("[p816]Und Erika geht nicht leer aus. Nach Paragraf achthundertsechzehn Absatz eins Satz eins muss Benno ihr "
     "herausgeben, was er durch die Verfügung erlangt hat, also den Erlös von zweihundert Euro. Mehr dazu im Video zum "
     "Bereicherungsrecht.", PS),
    # --- M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe das Abhandenkommen immer, auch wenn der Erwerber gutgläubig ist. [tipp2]Und frage dort nicht "
     "nach dem Erwerber, sondern ob der Eigentümer oder sein Besitzmittler den Besitz freiwillig aus der Hand gegeben hat.", PS),
    # --- N Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den gutgläubigen Erwerb nach Paragraf neunhundertneunundzwanzig Satz eins in Verbindung "
     "mit Paragraf neunhundertzweiunddreißig: [k1]Römisch eins: Rechtsgeschäft, also ein Verkehrsgeschäft. [k2]Römisch "
     "zwei: Einigung und Übergabe. [k3]Römisch drei: Nichtberechtigung des Veräußerers. [k4]Römisch vier: Rechtsschein des "
     "Besitzes. [k5]Römisch fünf: guter Glaube, also weder Kenntnis noch grob fahrlässige Unkenntnis. [k6]Römisch sechs: "
     "kein Abhandenkommen nach Paragraf neunhundertfünfunddreißig.", PS),
    # --- O Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der gute Glaube ersetzt nur die fehlende Berechtigung. [m2]Und bei abhandengekommenen Sachen hilft er "
     "grundsätzlich nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
