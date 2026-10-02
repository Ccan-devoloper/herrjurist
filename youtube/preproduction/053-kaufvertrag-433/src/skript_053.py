"""Folge 053 · § 433 BGB: Die Pflichten aus dem Kaufvertrag – Prüfungsschema (Mi · Examenswissen · Zivilrecht/Kaufrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Du kaufst ein gebrauchtes Fahrrad – was genau darfst du vom Verkäufer
verlangen?“): Inga kauft am Freitag von Herrn Lüders (privat) dessen gebrauchtes Trekkingrad für 250 Euro, Abholung am
Samstag. Am Samstag will Inga das Rad mitnehmen und erst am Montag überweisen; Herr Lüders verweigert die Herausgabe
(§ 320 I). Inga holt das Geld, beide tauschen (Übergabe und Übereignung, § 929 S. 1; Erfüllung, § 362 I).
Kern: Wortlautkarten § 433 I und II, Pflichten des Verkäufers (Übergabe, Übereignung, Mängelfreiheit §§ 434, 435) und des
Käufers (Kaufpreis, Abnahme), Trennungsprinzip (Verweis Folge 005), Aufbau entstanden – nicht erloschen – durchsetzbar
(Folge 006), § 320/§ 322 (BGH V ZR 11/18 Rn. 38; VIII ZR 211/15 Rn. 29 zur Abnahme), Ausblick Gefahrübergang
§§ 434 I, 446, 437 (BGH VIII ZR 187/20 Rn. 78) und Verbrauchsgüterkauf §§ 474, 475 I.
Figuren: Inga (ela_froh), Herr Lüders (timo); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.7

STIMMEN = {"Inga": "ela_froh", "Lueders": "timo"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Freitag im Vorgarten, Samstag der Streit, der Tausch ---------------------------------------------------
    ("[fall]Inga sucht ein gebrauchtes Fahrrad. [anzeige]Im Internet bietet Herr Lüders sein altes Trekkingrad an, für "
     "zweihundertfünfzig Euro. [besuch]Am Freitag sieht Inga es sich bei ihm im Vorgarten an.", 0.3),
    ("[i1]Das Rad nehme ich, für zweihundertfünfzig Euro.", 0.3, "Inga"),
    ("[l1]Abgemacht! Holen Sie es morgen ab.", 0.4, "Lueders"),
    ("[sams]Am Samstag kommt Inga wieder und will das Rad gleich mitnehmen.", 0.3),
    ("[i2]Das Geld überweise ich Ihnen am Montag.", 0.3, "Inga"),
    ("[l2]Nein. Erst das Geld, dann das Rad.", 0.4, "Lueders"),
    ("[automat]Inga holt das Geld am Automaten an der Ecke. [tausch]Sie zahlt, und Herr Lüders gibt ihr das Rad und den "
     "Schlüssel für das Schloss. [weg]Inga fährt davon.", 0.4),
    ("[frage]Was durfte Inga von Herrn Lüders verlangen? [frage2]Durfte er das Rad zurückhalten? Und was schuldet Inga ihm?", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruch, Wortlaut § 433 I -------------------------------------------------------------------------------------
    ("[ansp]Inga verlangt das Rad. Anspruchsgrundlage ist Paragraf vierhundertdreiunddreißig. [w1]Absatz eins: Durch den "
     "Kaufvertrag wird der Verkäufer einer Sache verpflichtet, dem Käufer die Sache zu übergeben und das Eigentum an der "
     "Sache zu verschaffen. [w1b]Der Verkäufer hat dem Käufer die Sache frei von Sach- und Rechtsmängeln zu verschaffen.", P),
    ("[vk]Der Verkäufer schuldet also dreierlei. [vk1]Übergabe: Inga bekommt den Besitz, die tatsächliche Gewalt über das "
     "Rad. [vk2]Übereignung: Sie wird Eigentümerin. [vk3]Und ein Rad ohne Mängel: [sm]keinen Sachmangel, etwa eine kaputte "
     "Bremse, Paragraf vierhundertvierunddreißig, [rm]und keinen Rechtsmangel, Paragraf vierhundertfünfunddreißig. Kein "
     "Dritter darf Rechte an dem Rad gegen Inga geltend machen können.", PS),
    # --- D Wortlaut § 433 II ----------------------------------------------------------------------------------------------
    ("[w2]Absatz zwei regelt die Gegenseite: Der Käufer ist verpflichtet, dem Verkäufer den vereinbarten Kaufpreis zu "
     "zahlen und die gekaufte Sache abzunehmen. [kp]Inga schuldet also zweihundertfünfzig Euro [ab]und muss das Rad "
     "abnehmen, hier also abholen.", PS),
    # --- E Trennungsprinzip -----------------------------------------------------------------------------------------------
    ("[trenn]Wichtig: Der Kaufvertrag verpflichtet nur. [p929]Eigentümerin wird Inga erst durch eine eigene Übereignung "
     "nach Paragraf neunhundertneunundzwanzig Satz eins: Einigung und Übergabe. [tp]Das ist das Trennungsprinzip. "
     "[f005]Mehr dazu in der Folge zum Abstraktionsprinzip.", PS),
    # --- F Drei Schritte ----------------------------------------------------------------------------------------------------
    ("[drei]Jeden Anspruch prüfst du in drei Schritten: [s1]entstanden, [s2]nicht erloschen, [s3]durchsetzbar.", P),
    # --- G I. entstanden ----------------------------------------------------------------------------------------------------
    ("[ent]Römisch eins: Ist der Anspruch entstanden? [kv]Inga und Herr Lüders haben sich am Freitag über das Rad und den "
     "Preis geeinigt. [kv_ok]Ein wirksamer Kaufvertrag liegt vor, der Anspruch ist entstanden.", P),
    # --- H II. nicht erloschen ----------------------------------------------------------------------------------------------
    ("[erl]Römisch zwei: nicht erloschen. [p362]Nach Paragraf dreihundertzweiundsechzig erlischt das Schuldverhältnis, "
     "wenn die geschuldete Leistung an den Gläubiger bewirkt wird. [sa]Am Samstagmorgen hat Inga das Rad aber noch nicht. "
     "[erl_ok]Der Anspruch besteht.", P),
    # --- I III. durchsetzbar: § 320, § 322 ------------------------------------------------------------------------------------
    ("[dur]Römisch drei: durchsetzbar? Hier liegt der Streit vom Samstag. [p320]Der Kauf ist ein gegenseitiger Vertrag. "
     "Nach Paragraf dreihundertzwanzig kann jede Seite ihre Leistung bis zur Bewirkung der Gegenleistung verweigern, "
     "[vor]es sei denn, sie muss vorleisten. [kein]Eine Zahlung erst am Montag war nicht vereinbart. Herr Lüders durfte "
     "das Rad also zurückhalten.", P),
    ("[zug]Umgekehrt musste auch Inga nicht vorleisten: Beide leisten Zug um Zug. [p322]Klagt Inga und beruft er sich auf "
     "sein Recht, wird er nach Paragraf dreihundertzweiundzwanzig nur zur Leistung Zug um Zug verurteilt. [abn]Die Abnahme "
     "ist dagegen nach dem Bundesgerichtshof im Allgemeinen keine Gegenleistung für die Lieferung.", PS),
    # --- J Erfüllung beim Tausch ------------------------------------------------------------------------------------------------
    ("[erf]Dann der Tausch am Samstag. [ue]Herr Lüders übergibt Rad und Schlüssel, und beide sind sich einig, dass das "
     "Eigentum übergeht. [geld]Genauso übereignet Inga ihm die Geldscheine. [erl2]Damit sind beide Ansprüche erfüllt und "
     "nach Paragraf dreihundertzweiundsechzig erloschen. [abg]Abgenommen hat Inga das Rad auch: Sie fährt damit nach Hause.", PS),
    # --- K Ausblick: Gefahrübergang und Gewährleistung -----------------------------------------------------------------------
    ("[gew]Und ab wann greift das Gewährleistungsrecht? [p434]Ob das Rad mangelfrei ist, entscheidet sich bei "
     "Gefahrübergang, Paragraf vierhundertvierunddreißig Absatz eins. [p446]Die Gefahr geht nach Paragraf "
     "vierhundertsechsundvierzig mit der Übergabe über. [p437]War die Bremse schon am Samstag kaputt, hat Inga "
     "grundsätzlich die Mängelrechte aus Paragraf vierhundertsiebenunddreißig.", PS),
    # --- L Ausblick: Verbrauchsgüterkauf -------------------------------------------------------------------------------------
    ("[vgk]Noch ein Ausblick: Kauft ein Verbraucher von einem Unternehmer, ist das ein Verbrauchsgüterkauf, Paragraf "
     "vierhundertvierundsiebzig. [p475]Dann gelten Sonderregeln. Ist keine Leistungszeit bestimmt, muss der Unternehmer "
     "zum Beispiel spätestens dreißig Tage nach Vertragsschluss übergeben, Paragraf vierhundertfünfundsiebzig. "
     "[priv]Herr Lüders verkauft privat, das gilt hier nicht.", PS),
    # --- M Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Achte darauf, was wohin gehört. [tipp2]Den Kaufvertrag prüfst du bei entstanden, die Übereignung "
     "erst bei erloschen. [tipp3]Und schreib nie: Mit dem Kaufvertrag ist Inga Eigentümerin geworden.", PS),
    # --- N Klausurschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Inga gegen Herrn Lüders aus Paragraf vierhundertdreiunddreißig Absatz eins Satz eins. "
     "[k1]Römisch eins: Anspruch entstanden, [k1a]also ein wirksamer Kaufvertrag. [k2]Römisch zwei: nicht erloschen, "
     "[k2a]vor allem keine Erfüllung nach Paragraf dreihundertzweiundsechzig durch Übergabe und Übereignung.", P),
    ("[k3]Römisch drei: durchsetzbar, [k3a]bei einer Einrede aus Paragraf dreihundertzwanzig nur Zug um Zug. "
     "[k4]Den Kaufpreis aus Absatz zwei prüfst du genauso.", PS),
    # --- O Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Kaufvertrag verpflichtet beide Seiten, im Zweifel Zug um Zug. [m2]Das Eigentum geht erst mit der "
     "Übereignung über, nicht schon mit dem Kaufvertrag.", 1.4),
]
