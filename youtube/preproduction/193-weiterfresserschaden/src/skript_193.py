"""Folge 193 · Weiterfresserschaden: Ein 40-Euro-Teil zerstört den ganzen Motor (Mo · Der Fall · Deliktsrecht, Klassiker-Fall).
Fall nach dem Plan-Hook („Ein fehlerhaftes Kleinteil im Wert von 40 Euro zerstört nach einigen Wochen den ganzen Motor“),
Personen und Firmen fiktiv, keine Automarke, kein Unfall mit Personen: Hinnerk kauft im Autohaus einen fabrikneuen Kleinwagen
für 26.000 €. Der Hersteller hat eine Spannrolle am Zahnriemen fehlerhaft gefertigt (Kleinteil, 40 €). Nach 6 Wochen bricht
sie, der Zahnriemen springt über, der Motor ist zerstört; Hinnerk rollt sicher an den Straßenrand. Werkstattmeister Ottokar:
neuer Motor 7.800 €; rechtzeitig getauscht, wäre der Motor heil geblieben.
Leitentscheidungen laut Plan: BGH, Urt. v. 24.11.1976 – VIII ZR 137/75, BGHZ 67, 359 (Schwimmerschalter) und BGH, Urt. v.
18.1.1983 – VI ZR 310/79, BGHZ 86, 256 (Gaszug); Datum, Az. und Fundstellen gesichert über BGH VI ZR 21/20 Rn. 10, 11
(Volltexte der Altentscheidungen amtlich nicht frei abrufbar, kein Zitat daraus). Kerngehalt über BGH, Urt. v. 23.2.2021 –
VI ZR 21/20, Rn. 10 (Anspruchskonkurrenz), 11 (Äquivalenz-/Integritätsinteresse, stoffgleich), 13 (mangelhaftes Teil selbst
keine Eigentumsverletzung), 16 (Kriterien der Stoffgleichheit), 21 (Rechtsgutsverletzung erst mit dem Schaden);
Kritik/Gesetzgeber: BT-Drucks. 14/6040 S. 229 („Wertungswiderspruch“), BGH V ZR 33/19 Rn. 51. Normen: § 823 Abs. 1 BGB
(Wortlautkarte, wörtlich), § 437 BGB (ein Satz, Verweis Folge 059), § 438 Abs. 1 Nr. 3, Abs. 2, §§ 195, 199 Abs. 1 BGB,
§ 1 Abs. 1 Satz 2 ProdHaftG (Wortlautkarte). Belege: ../RECHTSSTAND.md. Schema zu § 823 I nur verwiesen (Folge 067),
reiner Vermögensschaden (Folge 187) nicht wiederholt.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Liste des Auftrags, Volltextsuche 04.10.2026):
Hinnerk, Ottokar – nie im Genitiv. Stimmen: Hinnerk niklas (Mann, jung), Ottokar helmut (Mann, älter). Lexi = Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ottokar": "helmut", "Hinnerk": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Autohaus, sechs Wochen später am Straßenrand -----------------------------------------------------------
    ("[fall]Ein Autohaus am Stadtrand. [hinnerk]Hinnerk kauft hier einen fabrikneuen Kleinwagen für sechsundzwanzigtausend "
     "Euro. [teil]Was niemand weiß: Der Hersteller hat eine Spannrolle am Zahnriemen fehlerhaft gefertigt, ein Kleinteil im "
     "Wert von vierzig Euro. [fahrt]Sechs Wochen fährt der Wagen problemlos. [bruch]Dann bricht die Spannrolle, der Zahnriemen "
     "springt über, [motor]und der Motor ist zerstört. [rand]Hinnerk rollt sicher an den Straßenrand.", P),
    # --- A2 Fall: in der Werkstatt -----------------------------------------------------------------------------------------
    ("[werk]In der Werkstatt schaut Meister Ottokar nach.", P),
    ("[o1]Die Spannrolle ist gebrochen. Ein Teil für vierzig Euro, und der Motor ist hin. [o2]Ein neuer kostet "
     "siebentausendachthundert Euro.", P, "Ottokar"),
    ("[h1]Der Wagen ist sechs Wochen alt! Dann soll der Hersteller den Motor bezahlen.", P, "Hinnerk"),
    ("[frage]Kann Hinnerk vom Hersteller Ersatz für den Motor verlangen? [klass]Das ist der Weiterfresserschaden, ein "
     "Klassiker mit zwei Leitentscheidungen: [klass2]dem Schwimmerschalter-Fall von neunzehnhundertsechsundsiebzig und dem "
     "Gaszug-Fall von neunzehnhundertdreiundachtzig.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Warum Deliktsrecht? ---------------------------------------------------------------------------------------------
    ("[warum]Warum überhaupt Deliktsrecht? [vk]Gegen das Autohaus hat Hinnerk die Mängelrechte aus Paragraf "
     "vierhundertsiebenunddreißig; den Mangelbegriff erklärt das Video zum Sachmangel. [hst]Mit dem Hersteller aber hat er "
     "keinen Vertrag; ihn erreicht er nur über das Deliktsrecht oder das Produkthaftungsgesetz. [fr1]Dazu kommen die Fristen: Mängelansprüche verjähren beim "
     "Autokauf grundsätzlich in zwei Jahren ab Ablieferung. [fr2]Für das Delikt gilt die regelmäßige Frist von drei Jahren. "
     "[fr3]Sie beginnt erst mit dem Schluss des Jahres, in dem der Anspruch entsteht und Hinnerk die Umstände und den "
     "Schuldner kennt oder ohne grobe Fahrlässigkeit kennen müsste. [fr4]Entstanden ist der Anspruch erst mit der Zerstörung "
     "des Motors. Das zählt, wenn ein Teil erst nach Jahren bricht.", PS),
    # --- D Die Norm: § 823 Abs. 1 BGB ---------------------------------------------------------------------------------------
    ("[norm]Anspruchsgrundlage gegen den Hersteller ist Paragraf achthundertdreiundzwanzig Absatz eins BGB: [w1]Wer "
     "vorsätzlich oder fahrlässig das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein sonstiges Recht "
     "eines anderen widerrechtlich verletzt, ist dem anderen zum Ersatz des daraus entstehenden Schadens verpflichtet. "
     "[schema]Die übrigen Merkmale prüfst du nach dem Schema aus dem Video zum Deliktsrecht. [prob]Hier geht es um das "
     "Eigentum, und da liegt das Problem: [prob2]Hinnerk hat das Auto schon mit der fehlerhaften Spannrolle erworben. "
     "[prob3]Kann man eine Sache verletzen, die von Anfang an mangelhaft war?", PS),
    # --- E Zwei Interessen, Stoffgleichheit --------------------------------------------------------------------------------
    ("[int]Der Bundesgerichtshof unterscheidet zwei Interessen. [aeq]Das Vertragsrecht schützt das Äquivalenzinteresse: die "
     "Erwartung, für den Kaufpreis eine mangelfreie Sache zu bekommen. [integ]Das Deliktsrecht schützt das "
     "Integritätsinteresse: durch die Sache nicht am Eigentum verletzt zu werden. [unwert]Der Mangelunwert steckt von "
     "Anfang an in der Sache; er gehört zum enttäuschten Kauf. [deckt]Deckt sich der Schaden mit diesem Mangelunwert, ist er "
     "stoffgleich, und für das Delikt ist kein Raum. [mehr]Geht der Schaden darüber hinaus, kann das "
     "Integritätsinteresse verletzt sein.", PS),
    # --- F Kriterien der Stoffgleichheit -----------------------------------------------------------------------------------
    ("[krit]Wann ist der Schaden stoffgleich? [k1]Nach dem Bundesgerichtshof dann, wenn der Fehler von Anfang an die ganze "
     "Sache erfasst, [k2]etwa weil sie von vornherein nicht oder kaum brauchbar ist, [k3]oder wenn sich der Mangel technisch "
     "nicht oder nicht mit wirtschaftlich vertretbarem Aufwand beheben lässt. [k4]Ist der Mangel dagegen zunächst auf ein Teil "
     "beschränkt und behebbar, [k5]und zerstört er erst später den Rest, dann hat dieser Rest einen eigenen Wert: "
     "[k6]Der Schaden ist nicht stoffgleich.", PS),
    # --- G Anwendung auf den Fall ------------------------------------------------------------------------------------------
    ("[anw]Im Fall: [a1]Der Fehler steckte nur in der Spannrolle, einem Teil für vierzig Euro. [a2]Rechtzeitig getauscht, "
     "wäre der Motor heil geblieben; der Mangel war also mit geringem Aufwand behebbar. [a3]Der Motor selbst war mangelfrei "
     "und hatte einen eigenen Wert. [a4]Sein Schaden ist nicht stoffgleich: Das ist eine Eigentumsverletzung am Motor. "
     "[a5]Die Spannrolle selbst dagegen war von Anfang an fehlerhaft. Für sie bleibt es beim Kaufrecht.", PS),
    # --- H Gegenbeispiel: ganzer Motor von Anfang an unbrauchbar -----------------------------------------------------------
    ("[gegen]Anders liegt es, wenn der Fehler von Anfang an das ganze Gerät erfasst. [g1]Ist etwa der ganze Motor falsch "
     "konstruiert und lässt sich das nicht mit vertretbarem Aufwand beheben, war er von Anfang an kaum zu gebrauchen. "
     "[g2]Geht er später kaputt, ist der Schaden stoffgleich; es bleibt allein beim Kaufrecht.", PS),
    # --- I Kritik und Produkthaftungsgesetz --------------------------------------------------------------------------------
    ("[lehre]Ein Teil der Lehre kritisiert die Figur: Sie umgehe die kürzere Verjährung des Kaufrechts. [bt]Der Gesetzgeber "
     "meinte bei der Schuldrechtsreform, dieser Wertungswiderspruch werde weitgehend vermieden, weil die regelmäßige "
     "Verjährung nun kürzer ist. "
     "[phg]Enger ist das Produkthaftungsgesetz: [phg1]Bei Sachschäden haftet der Hersteller danach nur, wenn eine andere Sache "
     "als das fehlerhafte Produkt beschädigt wird. [phg2]Der Motor ist aber Teil des fehlerhaften Autos. Gegen den Hersteller "
     "hilft für ihn also nur Paragraf achthundertdreiundzwanzig.", PS),
    # --- J Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Die Zerstörung des Motors verletzt das Eigentum von Hinnerk. [erg2]Liegen auch die übrigen "
     "Voraussetzungen vor, muss der Hersteller den Motor ersetzen. [erg3]Für die Spannrolle selbst bleibt es bei den "
     "Mängelrechten gegen das Autohaus.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Stoffgleichheit prüfst du bei der Eigentumsverletzung, nicht erst beim Schaden. [tp2]Trenne "
     "sauber: Was war von Anfang an mangelhaft, und was war vorher heil? [tp3]Und vergiss die Ansprüche gegen den Verkäufer "
     "nicht; sie stehen daneben.", PS),
    # --- L Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für den Weiterfresserschaden. [c1]Römisch eins: Eigentumsverletzung. [c2]Erstens: Welcher Teil war "
     "beim Erwerb mangelhaft? [c3]Zweitens: Stoffgleichheit, also Mangel auf ein Teil beschränkt und behebbar, Schaden erst "
     "später am übrigen Teil? [c4]Römisch zwei: die übrigen Merkmale von Paragraf "
     "achthundertdreiundzwanzig. [c5]Römisch drei: Konkurrenzen, also Kaufrecht gegen den Verkäufer und Produkthaftung nur "
     "für andere Sachen.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Steckt ein Mangel zunächst nur in einem behebbaren Teil und zerstört er später die übrige Sache, ist das "
     "Eigentum an der übrigen Sache verletzt. [m2]Was von Anfang an mangelhaft war, bleibt beim Kaufrecht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
