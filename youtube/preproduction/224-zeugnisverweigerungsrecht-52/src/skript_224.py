"""Folge 224 · Zeugnisverweigerungsrecht § 52 StPO: Aussage gegen den Partner? (Mi · Examenswissen · StPO · Format Schema).
Hook nach dem Themenplan: Eine Frau soll als Zeugin gegen ihren Verlobten aussagen – später auch gegen ihren Mitbewohner.
Fall: Frau Wehner ist mit Herrn Störmer verlobt (Hochzeit geplant). Gegen ihn wird wegen Betrugs ermittelt (Konzertkarten
im Internet verkauft, die es nie gab). Sie sagt bei der Polizei und vor dem Ermittlungsrichter jeweils nach Belehrung aus,
verweigert in der Hauptverhandlung das Zeugnis. Später soll sie gegen ihren Mitbewohner Herrn Ladewig aussagen (Diebstahl
eines Laptops aus seiner Firma).
Aufbau: Fall → Sachverhalt → Zeugenpflicht § 48 Abs. 1 S. 2 → § 52 Abs. 1 (Wortlautkarte), Zweck (BGH 6 StR 326/20 Rn. 22)
→ Verlöbnis (BGHSt 48, 294; BGHSt 55, 65 Rn. 13), nicht erfasste Personen → Belehrung § 52 Abs. 3 S. 1 (Wortlautkarte),
Folge (6 StR 326/20 Rn. 22), Umentscheidung (§ 52 Abs. 3 S. 2; BGHSt 48, 294) → § 252 (Wortlautkarte), GSSt 1/16 Rn. 32
und Leitsatz, Verweis 221 → § 53 (Abs. 1 S. 1 Nr. 1–3, Abs. 2 S. 1) → § 55 (Wortlautkarte; StB 39/24 Rn. 8, 10) → Lösung
(Mitbeschuldigte: 6 StR 326/20 Rn. 18) → Klausurtipp (Lexi) → Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen (eindeutig deutsch, in keiner früheren Folge, reserviert): Wehner, Störmer, Ladewig; Polizist, Ermittlungsrichter und
Richterin bleiben Funktionsrollen.
Aussprache: In Segment 8 steht „Ladewich“ als lautliche Schreibung (Erstvertonung: „Ladewig“ mit hartem Auslaut, von
whisper small und medium so gehört, Segment 20 weich); Tafeln, Untertitel und Cue-Timeline schreiben „Ladewig“.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.35, 0.7

STIMMEN = {"Polizist": "christian", "Richterin": "hilde", "Wehner": "lucy", "Ladewig": "stephan"}  # Lexi = Carla

SEGMENTE = [
    # --- A Wohnung: Verlobung und Vorwurf -------------------------------------------------------------------------------
    ("[fall]Frau Wehner ist seit dem Frühjahr mit Herrn Störmer verlobt. [hochzeit]Im Sommer wollen die beiden heiraten. "
     "[vorwurf]Doch gegen ihn wird ermittelt: Er soll im Internet Konzertkarten verkauft haben, die es nie gab. "
     "[gesehen]Frau Wehner hat gesehen, wie er die Anzeigen schrieb.", 0.5),
    # --- B Polizei ------------------------------------------------------------------------------------------------------
    ("[pol]Die Polizei vernimmt sie als Zeugin und belehrt sie.", 0.2),
    ("[p1]Gegen Ihren Verlobten müssen Sie nicht aussagen.", 0.35, "Polizist"),
    ("[aus1]Sie sagt trotzdem aus. [er]Kurz darauf wiederholt sie alles vor dem Ermittlungsrichter, wieder nach "
     "Belehrung.", 0.5),
    # --- C Hauptverhandlung -----------------------------------------------------------------------------------------------
    ("[hv]Monate später, in der Hauptverhandlung gegen Herrn Störmer.", 0.2),
    ("[r1]Frau Wehner, als Verlobte des Angeklagten dürfen Sie das Zeugnis verweigern.", 0.3, "Richterin"),
    ("[w1]Dann sage ich nichts gegen meinen Verlobten.", 0.5, "Wehner"),
    # --- D Wohngemeinschaft -----------------------------------------------------------------------------------------------
    ("[wg]Später wird gegen ihren Mitbewohner ermittelt, Herrn Ladewich. [lap]Er soll in seiner Firma einen Laptop "
     "gestohlen haben. Frau Wehner hat gesehen, wie er ihn nach Hause brachte. [ladung]Sie wird als Zeugin geladen.", 0.2),
    ("[w2]Muss ich jetzt gegen meinen Mitbewohner aussagen?", 0.5, "Wehner"),
    # --- E Fragen --------------------------------------------------------------------------------------------------------
    ("[fragen]Darf sie gegen ihren Verlobten schweigen? [frage2]Was wird aus ihren früheren Aussagen? [frage3]Und wie "
     "ist es beim Mitbewohner?", 0.6),
    # --- F Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- G Grundsatz: Zeugenpflicht ---------------------------------------------------------------------------------------
    ("[pflicht]Zuerst der Grundsatz: Zeugen müssen aussagen. [p48]Paragraf achtundvierzig: Sie haben die Pflicht "
     "auszusagen, wenn keine im Gesetz zugelassene Ausnahme vorliegt. [ausn]Die wichtigste Ausnahme für die Familie steht "
     "in Paragraf zweiundfünfzig.", P),
    # --- H § 52 Abs. 1 ----------------------------------------------------------------------------------------------------
    ("[a52]Zur Verweigerung des Zeugnisses berechtigt sind: [n1]erstens der Verlobte des Beschuldigten. [n2]Zweitens der "
     "Ehegatte, auch wenn die Ehe nicht mehr besteht. [n2a]Ebenso der Lebenspartner. [n3]Drittens bestimmte Verwandte und "
     "Verschwägerte, etwa Eltern, Kinder und Geschwister. [zweck]Der Grund: Der Zeuge soll nicht zwischen Wahrheitspflicht "
     "und enger persönlicher Bindung zerrieben werden.", P),
    # --- I Verlöbnis und nicht erfasste Personen ----------------------------------------------------------------------------
    ("[verl]Eine Verlobung braucht keine Form. [heir]Entscheidend ist, dass beide wirklich heiraten wollen. Ob das so ist, "
     "beurteilt das Gericht. [zusatz]Anders als bei Ehegatten fehlt der Zusatz, dass das Recht auch danach fortbesteht: "
     "Es gilt nur, solange die Verlobung besteht. [nicht]Nicht in der Liste stehen Freunde, Mitbewohner und Paare, die "
     "ohne Verlobung zusammenleben. [nicht2]Für sie bleibt es bei der Aussagepflicht.", P),
    # --- J Belehrung § 52 Abs. 3 ----------------------------------------------------------------------------------------------
    ("[bel]Damit der Zeuge sein Recht kennt, schreibt Paragraf zweiundfünfzig Absatz drei vor: [bel2]Die Berechtigten "
     "sind vor jeder Vernehmung über ihr Recht zu belehren. [bel3]Das gilt auch bei Polizei und Staatsanwaltschaft. "
     "[fehlt]Fehlt die Belehrung, ist die Aussage grundsätzlich unverwertbar. [wider]Und wer schon ausgesagt hat, darf "
     "sich später noch umentscheiden.", P),
    # --- K § 252 -------------------------------------------------------------------------------------------------------------
    ("[a252]Genau dafür gibt es Paragraf zweihundertzweiundfünfzig: [a252b]Verweigert ein Zeuge erst in der "
     "Hauptverhandlung das Zeugnis, darf seine frühere Aussage nicht verlesen werden. [rspr]Nach der Rechtsprechung darf "
     "sie grundsätzlich auch sonst nicht verwertet werden, etwa durch den Polizisten, der den Zeugen vernommen hat. "
     "[richter]Ausnahme: Ein Richter hat den Zeugen vorher über sein Recht belehrt. Dann darf der Richter als Zeuge "
     "gehört werden. [einf]Eine weitergehende Belehrung ist dafür nicht nötig. [verw221]Mehr dazu in unserer Folge zu "
     "den Beweisverwertungsverboten.", PS),
    # --- L § 53 ---------------------------------------------------------------------------------------------------------------
    ("[a53]Davon zu trennen ist Paragraf dreiundfünfzig. [a53b]Er schützt nicht die Familie, sondern Berufsgeheimnisse: "
     "etwa von Geistlichen, Verteidigern und Ärzten, für das, was ihnen in dieser Eigenschaft anvertraut oder bekannt wurde. "
     "[a53c]Wird ein Arzt von der Schweigepflicht entbunden, muss er aussagen.", P),
    # --- M § 55 ---------------------------------------------------------------------------------------------------------------
    ("[a55]Und Paragraf fünfundfünfzig: [a55b]Jeder Zeuge darf die Auskunft auf Fragen verweigern, deren Antwort ihn "
     "selbst oder einen Angehörigen in Gefahr bringen würde, wegen einer Straftat oder Ordnungswidrigkeit verfolgt zu "
     "werden. [a55c]Das ist kein Recht, ganz zu schweigen, sondern grundsätzlich nur zu einzelnen Fragen. [a55d]Auch "
     "darüber ist der Zeuge zu belehren.", PS),
    # --- N Lösung: Verlobter -------------------------------------------------------------------------------------------------
    ("[l1]Zurück zu Frau Wehner. [l1a]Sie und Herr Störmer wollen im Sommer heiraten, sie sind verlobt. [l1b]Sie darf "
     "das Zeugnis verweigern, auch wenn sie früher ausgesagt hat. [l1c]Ihre Aussage bei der Polizei darf nicht verlesen "
     "werden, und der Polizist darf nicht darüber aussagen. [l1d]Der Ermittlungsrichter hat sie dagegen belehrt: Er darf "
     "als Zeuge über ihre Aussage gehört werden.", P),
    # --- O Lösung: Mitbewohner -----------------------------------------------------------------------------------------------
    ("[l2]Gegen Herrn Ladewig hat sie kein Zeugnisverweigerungsrecht, denn ein Mitbewohner ist kein Angehöriger. "
     "[l2a]Sie muss aussagen. [l2b]Nur wenn einzelne Antworten sie selbst belasten könnten, etwa weil sie ihm den Laptop "
     "billig abgekauft hätte, darf sie diese Fragen verweigern. [l2c]Anders wäre es, wenn ihr Verlobter in diesem Verfahren "
     "wegen derselben Tat mitbeschuldigt wäre.", PS),
    # --- P Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüf den Zeugen in drei Schritten. [s1]Erstens: Gehört er zum Kreis des Paragrafen "
     "zweiundfünfzig? [s2]Zweitens: Wurde er vor jeder Vernehmung belehrt? [s3]Drittens: Schweigt er erst in der "
     "Hauptverhandlung, prüf Paragraf zweihundertzweiundfünfzig und die Ausnahme für den Richter. [s4]Gehört er nicht "
     "dazu, prüf Paragraf dreiundfünfzig und das Auskunftsverweigerungsrecht für einzelne Fragen.", PS),
    # --- Q Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf zweiundfünfzig schützt nur die Angehörigen, die das Gesetz nennt. [mz]Wer erst in der "
     "Hauptverhandlung schweigt, sperrt grundsätzlich auch seine früheren Aussagen. Nur was er nach Belehrung vor "
     "einem Richter gesagt hat, bleibt nutzbar.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = "".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
