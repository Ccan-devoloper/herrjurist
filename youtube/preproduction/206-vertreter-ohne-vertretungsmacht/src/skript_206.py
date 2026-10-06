"""Folge 206 · § 179 BGB: Vertreter ohne Vertretungsmacht – haftet er persönlich? (Mi · Examenswissen · BGB AT, Format Schema).
Fall nach dem Plan-Hook („Ein Bekannter verkauft ‚in deinem Namen' dein Motorrad – du willst davon nichts wissen.“):
Das Motorrad von Enno steht über den Winter in der Garage seines Bekannten Kuno. Kuno verkauft es ausdrücklich im Namen von Enno
für 4.500 € an Silja und behauptet, Enno wolle verkaufen; er weiß, dass Enno nie zugestimmt hat. Silja hat keinen Anlass zu
zweifeln. Übergabe und Zahlung sollen am Samstag stattfinden. Am Samstag verweigert Enno gegenüber Silja die Genehmigung.
Silja kauft ein gleichwertiges Motorrad beim Händler für 5.300 € und verlangt von Kuno 800 € Mehrkosten.
Schema: Ausgangslage (Verweis Folge 043, Voraussetzungen der Stellvertretung; Rechtsscheinsvollmacht scheidet aus) →
§ 177 I (Wortlautkarte, schwebend unwirksam, § 184 I) → § 177 II (Wortlautkarte: Aufforderung, zwei Wochen, Schweigen)
→ § 178 (Wortlautkarte: Widerruf, nur positive Kenntnis) → § 179 I (Wortlautkarte: Wahl Erfüllung/Schadensersatz,
Beweislast Vertretungsmacht, Erfüllungsinteresse; BGH III ZR 266/11 Rn. 34, 39; VII ZR 122/14 Rn. 24) → § 179 II
(Wortlautkarte: Vertrauensschaden, gedeckelt) → § 179 III (Wortlautkarte: Kenntnis/Kennenmüssen, beschränkt
Geschäftsfähiger) → Falllösung (800 €) → § 180 in einem Satz (BGH VIII ZR 4/23 Rn. 37) → Klausurtipp → Prüfschema →
Merksatz. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Liste des Auftrags, Volltextsuche
06.10.2026, Reservierungsliste der parallelen Folgen): Enno (Eigentümer, Stimme niklas), Kuno (Bekannter, helmut),
Silja (Käuferin, ela_froh) – nie im Genitiv. Lexi = Carla (Erzählerstimme).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Enno": "niklas", "Kuno": "helmut", "Silja": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Garage ------------------------------------------------------------------------------------------------
    ("[fall]Ein Bekannter verkauft „in deinem Namen“ dein Motorrad – und du willst davon nichts wissen. [enno]So geht es "
     "Enno. [garage]Sein Motorrad steht über den Winter in der Garage seines Bekannten Kuno. [silja]Eines Tages schaut "
     "Silja vorbei und fragt, ob das Motorrad zu verkaufen ist.", P),
    ("[k1]Enno will es loswerden. Ich verkaufe es dir in seinem Namen, für viertausendfünfhundert Euro.", P, "Kuno"),
    ("[s1]Abgemacht! Ich hole es am Samstag ab.", P, "Silja"),
    ("[vertrag]Beide unterschreiben einen Kaufvertrag. [weiss]Dabei weiß Kuno genau: Enno hat nie zugestimmt. "
     "[zweifel]Silja hat keinen Anlass, daran zu zweifeln.", P),
    # --- A2 Fall: Samstag ---------------------------------------------------------------------------------------------------
    ("[samstag]Am Samstag kommt Enno in die Garage und trifft Silja.", P),
    ("[e1]Davon will ich nichts wissen. Das genehmige ich nicht!", P, "Enno"),
    ("[haendler]Silja kauft ein gleichwertiges Motorrad beim Händler, für fünftausenddreihundert Euro.", P),
    ("[s2]Kuno, die achthundert Euro Mehrkosten zahlst du mir!", P, "Silja"),
    ("[frage]Haftet Kuno persönlich? [frage2]Wir prüfen das Schritt für Schritt.", PS),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Ausgangslage -----------------------------------------------------------------------------------------------------
    ("[vor]Zuerst die Ausgangslage. [drei]Wirksam vertreten kann nur, wer eine eigene Willenserklärung im fremden Namen "
     "und mit Vertretungsmacht abgibt. Das kennst du aus der Folge zur Stellvertretung. [hier]Kuno erklärt selbst und "
     "ausdrücklich im Namen von Enno. [ohne]Aber eine Vollmacht hat Enno ihm nie erteilt. [schein]Auch eine Duldungs- oder "
     "Anscheinsvollmacht scheidet aus: Kuno tritt zum ersten Mal für Enno auf. [falsus]Kuno ist also Vertreter ohne "
     "Vertretungsmacht, lateinisch falsus procurator.", PS),
    # --- D Schwebend unwirksam, § 177 Abs. 1 --------------------------------------------------------------------------------
    ("[p177]Paragraf hundertsiebenundsiebzig Absatz eins: Schließt jemand ohne Vertretungsmacht im Namen eines anderen einen "
     "Vertrag, so hängt die Wirksamkeit des Vertrags für und gegen den Vertretenen von dessen Genehmigung ab. "
     "[schweb]Der Kaufvertrag ist also schwebend unwirksam. [genehm]Genehmigt Enno, wird er rückwirkend Vertragspartner, "
     "Paragraf hundertvierundachtzig. [verw]Verweigert er die Genehmigung, bleibt der Vertrag für ihn unwirksam.", PS),
    # --- E Aufforderung, § 177 Abs. 2 ---------------------------------------------------------------------------------------
    ("[auff]Silja muss nicht ewig warten. [p1772]Nach Absatz zwei kann sie Enno zur Erklärung über die Genehmigung "
     "auffordern. [ihr]Dann kann er nur noch ihr gegenüber genehmigen oder verweigern. [vorher]Was er vorher nur zu Kuno "
     "gesagt hat, wird unwirksam. [frist]Und die Genehmigung ist nur bis zum Ablauf von zwei Wochen nach dem Empfang der "
     "Aufforderung möglich. [schweigt]Schweigt Enno, gilt sie als verweigert.", PS),
    # --- F Widerruf, § 178 --------------------------------------------------------------------------------------------------
    ("[p178]Umgekehrt darf Silja bis zur Genehmigung aussteigen. Nach Paragraf hundertachtundsiebzig kann sie widerrufen, "
     "[kennt]es sei denn, sie hat den Mangel der Vertretungsmacht beim Abschluss gekannt. [nurk]Hier zählt nur echte "
     "Kenntnis. [adr]Den Widerruf kann sie auch gegenüber Kuno erklären.", PS),
    # --- G Haftung, § 179 Abs. 1 --------------------------------------------------------------------------------------------
    ("[jetzt]Enno hat die Genehmigung aber verweigert. [p179]Jetzt greift Paragraf "
     "hundertneunundsiebzig Absatz eins: Wer als Vertreter einen Vertrag geschlossen hat, ist, sofern er nicht seine "
     "Vertretungsmacht nachweist, dem anderen Teil nach dessen Wahl zur Erfüllung oder zum Schadensersatz verpflichtet, "
     "wenn der Vertretene die Genehmigung des Vertrags verweigert. [beweis]Die Vertretungsmacht muss also Kuno beweisen, "
     "nicht Silja.", PS),
    ("[wahl]Silja hat die Wahl. [erf]Erfüllung hilft ihr wenig: Das Motorrad gehört Enno, nicht Kuno. [se]Also verlangt "
     "sie Schadensersatz, und zwar das Erfüllungsinteresse: [stellt]Sie wird so gestellt, als hätte der Vertrag gegolten "
     "und wäre erfüllt worden.", PS),
    # --- H § 179 Abs. 2 -----------------------------------------------------------------------------------------------------
    ("[p1792]Milder haftet der Vertreter nach Absatz zwei, wenn er den Mangel der Vertretungsmacht nicht gekannt hat. "
     "[vertr]Dann schuldet er nur den Vertrauensschaden: was Silja verliert, "
     "weil sie auf die Vertretungsmacht vertraut hat, [anh]zum Beispiel neunzig Euro Miete für einen Anhänger zum Abholen. "
     "[deckel]Und höchstens so viel, wie ihr Interesse an der Wirksamkeit des Vertrags beträgt.", PS),
    # --- I § 179 Abs. 3 -----------------------------------------------------------------------------------------------------
    ("[p1793]Ganz ausgeschlossen ist die Haftung nach Absatz drei, wenn der andere Teil den Mangel der Vertretungsmacht "
     "kannte oder kennen musste, also aus Fahrlässigkeit nicht kannte. [minder]Und ein beschränkt geschäftsfähiger "
     "Vertreter haftet nur, wenn er mit Zustimmung seines gesetzlichen Vertreters gehandelt hat. [nichts]Hier greift nichts "
     "davon: Silja hatte keinen Anlass zu Zweifeln, und Kuno ist volljährig.", PS),
    # --- J Falllösung -------------------------------------------------------------------------------------------------------
    ("[loes]Zur Lösung. [geg]Von Enno kann Silja nichts verlangen: Ohne Vertretungsmacht und ohne Genehmigung ist er nicht "
     "Vertragspartner. [gegk]Gegen Kuno hat sie den Anspruch aus Paragraf hundertneunundsiebzig Absatz eins, [voll]und weil "
     "er den Mangel kannte, haftet er voll. [rechn]Für ein gleichwertiges Motorrad zahlt Silja fünftausenddreihundert statt "
     "viertausendfünfhundert Euro. [erg]Kuno muss ihr also achthundert Euro ersetzen.", P),
    ("[k2]Und ich dachte, Enno freut sich über das Geld.", P, "Kuno"),
    # --- K § 180 in einem Satz ----------------------------------------------------------------------------------------------
    ("[p180]Zuletzt einseitige Rechtsgeschäfte wie eine Kündigung: Hier ist Vertretung ohne Vertretungsmacht "
     "nach Paragraf hundertachtzig unzulässig, die Erklärung also nichtig, [ausn]es sei denn, der Empfänger hat die "
     "behauptete Vertretungsmacht nicht beanstandet oder war einverstanden.", PS),
    # --- L Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst den Anspruch gegen den Vertretenen. [tp1]Erst wenn er an der fehlenden "
     "Vertretungsmacht und der verweigerten Genehmigung scheitert, [tp2]kommt der Anspruch gegen den Vertreter. "
     "[tp3]Paragraf hundertneunundsiebzig ist dabei selbst die Anspruchsgrundlage, anders als Paragraf "
     "hundertvierundsechzig. [tp4]Und dass der andere den Mangel kannte oder kennen musste, muss der Vertreter beweisen.", PS),
    # --- M Prüfschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [c1]Römisch eins: Silja gegen Enno aus Paragraf vierhundertdreiunddreißig Absatz eins. "
     "[c2]Kein Vertrag: Kuno handelt ohne Vertretungsmacht, und Enno verweigert die Genehmigung. [c3]Römisch zwei: Silja "
     "gegen Kuno aus Paragraf hundertneunundsiebzig Absatz eins. [c4]Erstens: Vertrag als Vertreter im fremden Namen. "
     "[c5]Zweitens: ohne Vertretungsmacht. [c6]Drittens: Genehmigung verweigert. [c7]Viertens: kein Ausschluss nach Absatz drei. [c8]Fünftens: Rechtsfolge. Wahl zwischen Erfüllung und "
     "Schadensersatz, bei Unkenntnis des Vertreters nur der Vertrauensschaden.", PS),
    # --- N Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer ohne Vertretungsmacht im fremden Namen einen Vertrag schließt, haftet selbst, wenn der Vertretene "
     "die Genehmigung verweigert. [mk2]Kannte er den Mangel, haftet er auf das volle Erfüllungsinteresse.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
    assert not re.search(r"\b(Ennos|Kunos|Siljas)\b", text), "Genitiv eines Namens"
