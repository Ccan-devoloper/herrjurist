"""Folge 161 · Abhandenkommen § 935 BGB: Gestohlen oder verliehen? (Mi · Examenswissen · Sachenrecht, Format Abgrenzung).
Zwei Parallelfälle nach dem Plan-Hook („Die verliehene Kamera kann wirksam weiterverkauft werden – die gestohlene nicht“):
Fall A: Hella leiht ihre Kamera ihrem Freund Knut bis Montag; Knut gibt sie auf dem Flohmarkt als seine aus und verkauft sie
für 300 € an die gutgläubige Berta. Fall B: Hella legt die Kamera im Park neben sich auf eine Bank; ein Dieb nimmt sie weg und
verkauft sie auf demselben Flohmarkt für 300 € an die gutgläubige Berta.
Prüfung: §§ 929 S. 1, 932 (Verweis Folge 083) → § 935 Abs. 1 S. 1 (Wortlautkarte, vorgelesen) → 1. Begriff: unfreiwilliger
Verlust des unmittelbaren Besitzes (BGH V ZR 8/19 Rn. 9; V ZR 92/25 Rn. 11), Täuschung macht nicht unfreiwillig (V ZR 8/19
Rn. 9) → 2. mittelbarer Besitz: § 935 Abs. 1 S. 2 (Wortlautkarte, vorgelesen), es kommt auf den Besitzmittler an, Verlust des
mittelbaren Besitzes genügt nicht (V ZR 58/13 Rn. 16, 19) → 3. Besitzdiener § 855 (Wortlautkarte), eigenmächtige Weggabe
(V ZR 58/13 Rn. 9; V ZR 8/19 Rn. 16: Einzelheiten streitig), Probefahrer kein Besitzdiener (V ZR 8/19 Leitsätze, Rn. 21)
→ 4. § 935 Abs. 2 (Wortlautkarte, mit § 979 Abs. 1a) → 5. Wertung (V ZR 92/25 Rn. 15; „Veranlassungsprinzip“ als
Lehrbegriff gekennzeichnet), Sperre dauerhaft (V ZR 92/25 Rn. 13, Leitsatz) → 6. Lösung beider Fälle, § 985 (Verweis Folge
092) → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Hella, Knut, Berta
(nie im Genitiv). Stimmen: Hella sabrina, Knut marc; Berta und der Dieb sprechen nicht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Hella": "sabrina", "Knut": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall A: verliehen -----------------------------------------------------------------------------------------
    ("[fall]Fall A. [hella]Hella besitzt eine Kamera. [leih]Ihr Freund Knut will am Wochenende fotografieren, und Hella "
     "leiht sie ihm bis Montag.", P),
    ("[h1]Hier, bring sie mir am Montag zurück.", P, "Hella"),
    ("[knapp]Doch Knut braucht Geld. [flohm]Auf dem Flohmarkt gibt er die Kamera als seine eigene aus.", P),
    ("[k1]Die Kamera gehört mir. Für dreihundert Euro ist sie deine.", P, "Knut"),
    ("[berta]Berta zahlt, Knut übergibt ihr die Kamera, [glaub]und Berta hat keinen Grund zu zweifeln.", PS),
    # --- B Fall B: gestohlen ------------------------------------------------------------------------------------------
    ("[fallb]Fall B. [bank]Hella legt die Kamera im Park neben sich auf eine Bank. [dieb]Ein Dieb nimmt sie unbemerkt weg "
     "[verk]und verkauft sie auf demselben Flohmarkt an Berta, wieder für dreihundert Euro. [glaub2]Auch diesmal hat Berta "
     "keinen Grund zu zweifeln.", P),
    ("[frage]Zweimal derselbe gutgläubige Kauf. [frage2]Wird Berta jedes Mal Eigentümerin?", PS),
    # --- C Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier sind beide Fälle zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Einordnung, § 935 Abs. 1 S. 1 --------------------------------------------------------------------------------
    ("[nb]In beiden Fällen verkauft jemand, dem die Kamera nicht gehört. [p932]Berta kann deshalb nur gutgläubig erwerben, "
     "nach Paragraf neunhundertneunundzwanzig Satz eins und Paragraf neunhundertzweiunddreißig; das Schema zeigt das Video "
     "zum gutgläubigen Erwerb. [gg]Gutgläubig ist Berta in beiden Fällen. [w1]Die Weiche stellt Paragraf "
     "neunhundertfünfunddreißig Absatz eins Satz eins: Der Erwerb des Eigentums auf Grund der Paragrafen "
     "neunhundertzweiunddreißig bis neunhundertvierunddreißig tritt nicht ein, [w1b]wenn die Sache dem Eigentümer "
     "gestohlen worden, verloren gegangen oder sonst abhanden gekommen war.", PS),
    # --- E 1. Begriff ---------------------------------------------------------------------------------------------------
    ("[begr]Gestohlen und verloren sind nur Beispiele, der Oberbegriff ist das Abhandenkommen. [def]Nach dem "
     "Bundesgerichtshof kommt eine Sache abhanden, wenn der Eigentümer den unmittelbaren Besitz ohne seinen Willen "
     "verliert. [grund]Denn ein unfreiwilliger Besitzverlust entwertet den Besitz als Grundlage des gutgläubigen Erwerbs. "
     "[fb]Im Fall B nimmt der Dieb die Kamera weg, ohne dass Hella es will: abhandengekommen.", P),
    ("[taeu]Aber Vorsicht bei Täuschung: [taeu2]Wer sich eine Sache mit einer Lüge erschwindelt, hat sie trotzdem "
     "freiwillig bekommen.", PS),
    # --- F 2. mittelbarer Besitz ----------------------------------------------------------------------------------------
    ("[mb]Und Fall A? [mb2]Als Verleiherin war Hella nur noch mittelbare Besitzerin, Knut als Entleiher unmittelbarer "
     "Besitzer. [w2]Dafür gilt Satz zwei: Das Gleiche gilt, falls der Eigentümer nur mittelbarer Besitzer war, dann, wenn "
     "die Sache dem Besitzer abhanden gekommen war. [knut]Es kommt also auf Knut an. [knut2]Und Knut hat die Kamera "
     "freiwillig an Berta übergeben. [mbv]Dass Hella damit ihren mittelbaren Besitz verliert, reicht nicht. [umg]Anders "
     "wäre es, wenn man Knut die Kamera gestohlen hätte: Dann wäre sie nach Satz zwei abhandengekommen.", PS),
    # --- G 3. Besitzdiener ----------------------------------------------------------------------------------------------
    ("[bd]Eine Falle bleibt: der Besitzdiener, bekannt aus dem Video zu Besitz und Eigentum. [w3]Nach Paragraf achthundertfünfundfünfzig ist nur der andere Besitzer, "
     "wenn jemand die tatsächliche Gewalt für ihn in seinem Haushalt oder Erwerbsgeschäft ausübt und seinen Weisungen "
     "folgen muss. [studio]Angenommen, Knut arbeitet als Angestellter im Fotoladen von Hella und verkauft eine Kamera aus "
     "dem Laden eigenmächtig. [bd2]Dann bleibt Hella unmittelbare Besitzerin, Knut ist nur ihr Besitzdiener. [bd3]Gibt er "
     "die Kamera ohne ihren Willen weg, kann sie nach der Rechtsprechung abhandengekommen sein; [streit]die Einzelheiten "
     "sind streitig.", P),
    ("[probe]Kein Besitzdiener ist dagegen der Kaufinteressent auf einer unbegleiteten Probefahrt. [probe2]Der "
     "Bundesgerichtshof hat entschieden: Wer sich mit gefälschten Papieren ein Auto für eine Stunde Probefahrt geben "
     "lässt und nie zurückkommt, hat es freiwillig bekommen. [probe3]Kein Abhandenkommen.", PS),
    # --- H 4. Ausnahmen Abs. 2 ------------------------------------------------------------------------------------------
    ("[abs2]Absatz zwei kennt Ausnahmen: [geld]Geld, Inhaberpapiere [verst]und Sachen aus einer öffentlichen "
     "Versteigerung oder einer Fundsachen-Versteigerung im Internet nach Paragraf neunhundertneunundsiebzig. [abs2b]Eine "
     "Kamera ist kein Geld, und der Flohmarkt ist keine öffentliche Versteigerung.", PS),
    # --- I 5. Wertung ---------------------------------------------------------------------------------------------------
    ("[wert]Warum dieser Unterschied? [wert2]Der Bundesgerichtshof sagt: Wer eine Sache freiwillig aus der Hand gibt, "
     "trägt auch die Gefahr einer unrechtmäßigen Verfügung. [wert3]Wem sie ohne seinen Willen entzogen wird, der bleibt "
     "schutzbedürftig. [veran]In der Lehre spricht man vom Veranlassungsprinzip: Hella hat Knut selbst ausgesucht, den "
     "Dieb nicht. [dauer]Deshalb bleibt eine abhandengekommene Sache grundsätzlich auch für jeden weiteren Käufer "
     "gesperrt, bis die Eigentümerin wieder Besitz erlangt.", PS),
    # --- J 6. Lösung ----------------------------------------------------------------------------------------------------
    ("[loes]Die Lösung. [la]Fall A: kein Abhandenkommen. Berta wird Eigentümerin. [la2]Hella kann die Kamera nicht nach "
     "Paragraf neunhundertfünfundachtzig herausverlangen und muss sich an Knut halten. [lb]Fall B: Die Kamera ist "
     "abhandengekommen. Berta wird trotz guten Glaubens nicht Eigentümerin. [lb2]Hella bleibt Eigentümerin und kann die "
     "Kamera nach Paragraf neunhundertfünfundachtzig von Berta herausverlangen; mehr dazu im Video zum Herausgabeanspruch.", PS),
    # --- K Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Paragraf neunhundertfünfunddreißig immer erst nach den Paragrafen "
     "neunhundertzweiunddreißig bis neunhundertvierunddreißig, als letzte Hürde. [tp2]Frag dann: Wer hatte den "
     "unmittelbaren Besitz, und hat er ihn freiwillig aufgegeben? [tp3]Und bei einer Täuschung denk an die "
     "Freiwilligkeit: Betrug ist kein Diebstahl.", PS),
    # --- L Prüfschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zu Paragraf neunhundertfünfunddreißig. [c1]Römisch eins: Wer hatte den unmittelbaren Besitz? "
     "Der Eigentümer, auch durch einen Besitzdiener, oder sein Besitzmittler. [c2]Römisch zwei: Hat er ihn unfreiwillig "
     "verloren? Eine Täuschung reicht nicht. [c3]Römisch drei: Greift eine Ausnahme nach Absatz zwei?", PS),
    # --- M Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Verliehen ist nicht abhandengekommen. [m2]Abhanden kommt eine Sache nur, wenn der unmittelbare Besitz "
     "unfreiwillig verloren geht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
