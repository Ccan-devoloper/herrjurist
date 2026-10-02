"""Folge 080 · § 929 S. 1 BGB: Einigung und Übergabe – Übereignung Schema (Mi · Examenswissen · Zivilrecht/Sachenrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Du verkaufst dein Fahrrad, der Käufer holt es erst morgen ab – wem gehört
es heute Nacht?“): Annika verkauft Herrn Brunner am Abend ihr Fahrrad für 300 €, er zahlt bar, holt das Rad aber erst morgen
ab; es bleibt über Nacht im Hof von Annika.
Schema der Übereignung nach § 929 S. 1 BGB: (1) Einigung – dinglicher Vertrag, §§ 145 ff., Bestimmtheit, Abstraktion (Verweis
auf Folge 005), (2) Übergabe – Besitzerwerb des Erwerbers (§ 854 I), vollständiger Besitzverlust des Veräußerers, auf seine
Veranlassung (h. M.); Geheißperson ein Satz, (3) Einigsein im Zeitpunkt der Übergabe, Widerruflichkeit bis zur Übergabe als
h. M. offengelegt, (4) Berechtigung (Eigentum oder Verfügungsbefugnis, § 185; gutgläubiger Erwerb nur Verweis auf Folge 076).
Lösung: ohne Übergabe bleibt Annika heute Nacht Eigentümerin; am Geld ist sie schon Eigentümerin; § 930 nur als ausdrücklich
vereinbarte Variante; § 446 ein Satz (Kaufrecht); morgen Übergabe mit Einigung; Abwandlung § 449 ein Satz.
Wortlautkarten § 929 S. 1 und § 854 Abs. 1 BGB; Klausurtipp und Merksatz mit Lexi.
Figuren: Annika (lucy), Herr Brunner (stephan); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Annika": "lucy", "Brunner": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Verkauf am Abend ----------------------------------------------------------------------------------
    ("[fall]Annika verkauft ihr Fahrrad. [kommt]Am Abend kommt Herr Brunner vorbei und schaut es sich im Hof an.", 0.3),
    ("[br1]Ich nehme es. Hier sind dreihundert Euro.", 0.25, "Brunner"),
    ("[zahlt]Er zahlt bar. [fuss]Mitnehmen kann er das Rad aber erst morgen, er ist zu Fuß gekommen.", 0.25),
    ("[an1]Kein Problem. Das Rad bleibt bis morgen hier im Hof.", 0.3, "Annika"),
    # --- A2 Fall: die Nacht -----------------------------------------------------------------------------------------------
    ("[nacht]Herr Brunner geht nach Hause, das Rad steht über Nacht im Hof. [frage]Wer ist heute Nacht Eigentümer des "
     "Fahrrads? [frage2]Annika oder schon Herr Brunner?", 0.5),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Kaufvertrag und Übereignung --------------------------------------------------------------------------------------
    ("[kv]Zuerst der Kaufvertrag. Er verpflichtet Annika nur, Herrn Brunner das Rad zu übergeben und ihm das Eigentum zu "
     "verschaffen, Paragraf vierhundertdreiunddreißig. [eigen]Eigentum überträgt er selbst nicht. Dafür braucht es eine "
     "eigene Übereignung.", P),
    # --- D § 929 Satz 1 (Wortlaut) ------------------------------------------------------------------------------------------
    ("[p929]Für bewegliche Sachen gilt Paragraf neunhundertneunundzwanzig Satz eins: [w929]Zur Übertragung des Eigentums "
     "an einer beweglichen Sache ist erforderlich, dass der Eigentümer die Sache dem Erwerber übergibt und beide darüber "
     "einig sind, dass das Eigentum übergehen soll. [vier]Daraus folgen vier Prüfungspunkte: [v1]Einigung, [v2]Übergabe, "
     "[v3]Einigsein bei der Übergabe [v4]und Berechtigung.", PS),
    # --- E I. Einigung ------------------------------------------------------------------------------------------------------
    ("[einig]Erstens die Einigung. Sie ist ein dinglicher Vertrag: Beide erklären, dass das Eigentum übergehen soll. "
     "[p145]Für Angebot und Annahme gelten die allgemeinen Regeln, Paragrafen hundertfünfundvierzig folgende. "
     "[best]Und die Einigung muss eine bestimmte Sache betreffen, hier genau dieses Fahrrad.", P),
    ("[abstr]Vom Kaufvertrag ist sie getrennt und abstrakt. Mehr dazu im Video zum Abstraktionsprinzip. "
     "[offen]Ob Annika und Herr Brunner sich heute schon über den Eigentumsübergang geeinigt haben, kann offenbleiben.", PS),
    # --- F II. Übergabe, § 854 Abs. 1 (Wortlaut) -----------------------------------------------------------------------------
    ("[ueberg]Denn zweitens braucht es die Übergabe. Zuerst muss der Erwerber Besitz erlangen. [p854]Paragraf "
     "achthundertvierundfünfzig Absatz eins: [w854]Der Besitz einer Sache wird durch die Erlangung der tatsächlichen Gewalt "
     "über die Sache erworben.", P),
    ("[hm]Nach herrschender Meinung gehören noch zwei Punkte dazu: [verlust]Der Veräußerer gibt seinen Besitz vollständig "
     "auf, [veranl]und der Besitzwechsel geschieht auf seine Veranlassung. [geheiss]Empfangen kann auch ein Dritter "
     "für den Erwerber, etwa als Geheißperson.", P),
    ("[hof]Heute Nacht steht das Rad aber im Hof von Annika. [gewalt]Sie hat die tatsächliche Gewalt darüber, Herr Brunner "
     "nicht. [fehlt]Die Übergabe fehlt.", PS),
    # --- G III. Einigsein ------------------------------------------------------------------------------------------------------
    ("[einigsein]Drittens müssen beide im Zeitpunkt der Übergabe noch einig sein. [widerruf]Nach herrschender Meinung kann "
     "die Einigung bis zur Übergabe widerrufen werden. [reue]Hätten sich beide heute schon geeinigt, könnte "
     "Annika die Einigung also bis morgen noch widerrufen. Dann ginge kein Eigentum über. [bindet]Aus dem Kaufvertrag "
     "bliebe sie aber verpflichtet.", PS),
    # --- H IV. Berechtigung ------------------------------------------------------------------------------------------------------
    ("[berecht]Viertens die Berechtigung. Übereignen kann der Eigentümer [p185]oder wer mit dessen Einwilligung verfügt, "
     "Paragraf hundertfünfundachtzig. [annika]Annika ist Eigentümerin ihres Fahrrads. [gutgl]Gehört die Sache einem anderen, "
     "hilft sonst nur der gutgläubige Erwerb. Den erklärt das Video zum Sachenrecht im Überblick.", PS),
    # --- I Lösung heute Nacht -------------------------------------------------------------------------------------------------
    ("[loes]Also: Heute Nacht fehlt die Übergabe. Annika bleibt Eigentümerin. [anspr]Herr Brunner hat nur einen Anspruch "
     "aus dem Kaufvertrag. [geld]Anders beim Geld: Die Scheine hat er ihr übergeben, und beide waren sich einig. Am Geld ist "
     "Annika schon Eigentümerin.", P),
    ("[p930]Anders wäre es etwa, wenn beide ausdrücklich vereinbart hätten, dass Herr Brunner sofort Eigentümer wird und "
     "Annika das Rad bis morgen für ihn verwahrt. [p930b]Dann ersetzt dieses Besitzmittlungsverhältnis die Übergabe, "
     "Paragraf neunhundertdreißig. [p446]Übrigens geht auch die Gefahr des zufälligen Untergangs nach Paragraf "
     "vierhundertsechsundvierzig erst mit der Übergabe auf den Käufer über. Das ist aber Kaufrecht, nicht Sachenrecht.", PS),
    # --- J Fall: der nächste Morgen ----------------------------------------------------------------------------------------------
    ("[morgen]Am nächsten Morgen kommt Herr Brunner wieder.", 0.25),
    ("[br2]Guten Morgen! Ich hole das Fahrrad ab.", 0.25, "Brunner"),
    ("[an2]Bitte schön. Jetzt gehört es Ihnen.", 0.3, "Annika"),
    ("[gibt]Annika gibt ihm das Rad, und beide sind sich einig. [faehrt]Mit der Übergabe wird Herr Brunner Eigentümer.", PS),
    # --- K Abwandlung: Eigentumsvorbehalt ----------------------------------------------------------------------------------------
    ("[abw]Abwandlung: Herr Brunner nimmt das Rad sofort mit, zahlt aber in Raten, und Annika behält sich das Eigentum bis "
     "zur Zahlung vor. [p449]Dann ist die Einigung nach Paragraf vierhundertneunundvierzig im Zweifel aufschiebend "
     "bedingt. [raten]Eigentümer wird er erst mit vollständiger Zahlung.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Einigung und Übergabe getrennt, auch wenn beides im selben Moment passiert. [tipp2]Und "
     "schreibe nie, der Käufer sei durch den Kaufvertrag Eigentümer geworden.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für Paragraf neunhundertneunundzwanzig Satz eins: [k1]Römisch eins: Einigung, also ein "
     "dinglicher Vertrag über eine bestimmte Sache. [k2]Römisch zwei: Übergabe, [k2b]also Besitzerwerb des Erwerbers, "
     "vollständiger Besitzverlust des Veräußerers, auf dessen Veranlassung. [k3]Römisch drei: Einigsein im Zeitpunkt der "
     "Übergabe. [k4]Römisch vier: Berechtigung des Veräußerers, [k4b]sonst gutgläubiger Erwerb.", PS),
    # --- N Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Kaufvertrag verpflichtet nur. [m2]Eigentum geht erst mit Einigung und Übergabe über.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
