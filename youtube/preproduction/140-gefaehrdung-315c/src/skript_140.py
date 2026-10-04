"""Folge 140 · Gefährdung des Straßenverkehrs § 315c: Die 7 Todsünden & Schema (Mi · Examenswissen · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Fahrer überholt vor einer Kuppe und zwingt einen Entgegenkommenden zur Vollbremsung“):
Reinhold fährt auf einer Landstraße bergauf hinter einem langsamen Lastwagen, ist spät dran für einen Termin und überholt vor
einer Kuppe, obwohl er nicht sehen kann, ob Gegenverkehr kommt („Da kommt schon keiner“). Hinter der Kuppe kommt ihm Gertrud
entgegen; sie verhindert mit einer Vollbremsung den Zusammenstoß, Reinhold zieht knapp vor dem Lastwagen nach rechts.
Niemand wird verletzt, kein Zusammenstoß (im Bild nur Bremsspur-Strich und Warnsymbol). Reinhold ist nüchtern.
Prüfung: Überblick und Wortlautkarte § 315c Abs. 1 (Auszug) → I. 1. Führen eines Fahrzeugs im Straßenverkehr → 2. Tathandlung:
Nr. 1 (Verweis auf Folge 130) / Nr. 2 a–g als Tabelle, Wortlautkarte Nr. 2 b, § 5 Abs. 2 S. 1 StVO → 3. grob verkehrswidrig
(OLG Koblenz 4 ORs 4 Ss 16/23; BGH 4 StR 225/20 Rn. 14) und rücksichtslos (BGH 4 StR 354/23 Rn. 29 nach BGHSt 5, 392, 395)
→ 4. konkrete Gefahr (BGH 4 StR 73/24 Rn. 6, 4 StR 391/24 Rn. 4; Wertgrenze 750 € zweistufig: 4 StR 86/19 Rn. 7,
4 StR 245/10 Rn. 4; Tatfahrzeug und tatbeteiligte Mitfahrer: 4 StR 86/19 Rn. 8, 4 StR 73/24 Rn. 7, 4 StR 435/12 Rn. 5 f.;
„und dadurch“: 4 StR 73/24 Rn. 9) → 5. Vorsatz-Fahrlässigkeits-Kombinationen Abs. 1 / Abs. 3 Nr. 1 / Abs. 3 Nr. 2
(Wortlautkarte Abs. 3; Gefährdungsvorsatz 4 StR 493/23 Rn. 14) → II./III. → Konkurrenzen (§ 316 Abs. 1 a. E.) → Ergebnis
(§ 69 Abs. 2 Nr. 1) → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Reinhold, Gertrud (nie im Genitiv).
Stimmen (nur aus dem Pool stephan, hilde, christian, lucy): Reinhold stephan (Mann, mittel), Gertrud hilde (Frau, älter).
Lexi = Erzählerin Carla. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue; jede Marke genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; „Straßenverkehrsordnung“ und
„Bundesgerichtshof“ ausgeschrieben."""

P, PS = 0.3, 0.5

STIMMEN = {"Reinhold": "stephan", "Gertrud": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Überholen vor der Kuppe -----------------------------------------------------------------------------------
    ("[fall]Eine Landstraße am Vormittag. [lkw]Reinhold fährt bergauf hinter einem langsamen Lastwagen. [spaet]Er ist spät "
     "dran für einen Termin. [kuppe]Vor ihm liegt eine Kuppe; was dahinter kommt, kann er nicht sehen. [ueber]Trotzdem schert "
     "er aus und überholt. [gert]Hinter der Kuppe kommt ihm Gertrud entgegen. [brems]Sie macht eine Vollbremsung. "
     "[knapp]Reinhold zieht knapp vor dem Lastwagen nach rechts. [heil]Es kracht nicht, verletzt wird niemand.", 0.3),
    # --- A2 Fall: am Straßenrand ----------------------------------------------------------------------------------------------
    ("[rand]Kurz darauf halten beide am Straßenrand.", 0.3),
    ("[g1]Das war knapp! Ich konnte gerade noch bremsen.", 0.3, "Gertrud"),
    ("[r1]Ich dachte, da kommt schon keiner. Ich musste pünktlich sein.", 0.3, "Reinhold"),
    ("[frage]Hat sich Reinhold wegen Gefährdung des Straßenverkehrs strafbar gemacht? [frage2]Und wenn ja: vorsätzlich "
     "oder fahrlässig?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Überblick § 315c Abs. 1 (Wortlautkarte) ------------------------------------------------------------------------
    ("[p315c]Paragraf dreihundertfünfzehn c Absatz eins hat zwei Wege. [nr1]Nummer eins erfasst den fahruntüchtigen "
     "Fahrer, [nr2]Nummer zwei sieben besonders gefährliche Verkehrsverstöße. [gef]In beiden Fällen muss dadurch Leib oder "
     "Leben eines anderen oder eine fremde Sache von bedeutendem Wert gefährdet sein. [fuehr]Erstens: Reinhold führt sein "
     "Auto im öffentlichen Straßenverkehr. Das ist unproblematisch.", PS),
    # --- D Tathandlung: Nr. 1, Nr. 2 a–g ------------------------------------------------------------------------------------
    ("[th]Zweitens die Tathandlung. [nr1b]Nummer eins scheidet aus, Reinhold ist nüchtern und fahrtüchtig. Zur Fahruntüchtigkeit gibt es "
     "unsere Folge zu Paragraf dreihundertsechzehn. [tods]Bleibt Nummer zwei. Die sieben Fälle heißen in Lehrbüchern die "
     "sieben Todsünden; das Gesetz selbst kennt den Begriff nicht. [ta]Buchstabe a: Vorfahrt nicht beachtet. [tb]b: falsch überholt. "
     "[tc]c: an Fußgängerüberwegen falsch gefahren. [td]d: zu schnell an unübersichtlichen Stellen, Kreuzungen, Einmündungen und Bahnübergängen. "
     "[te]e: an unübersichtlichen Stellen nicht rechts gefahren. [tf]f: auf Autobahnen und Kraftfahrstraßen gewendet, rückwärts oder entgegen der Fahrtrichtung gefahren. "
     "[tg]g: haltende oder liegengebliebene Fahrzeuge nicht kenntlich gemacht. [liste]Andere Verstöße erfasst Nummer zwei nicht.", PS),
    ("[p2b]Hier passt Buchstabe b: wer falsch überholt oder sonst bei Überholvorgängen falsch fährt. [stvo]Überholen darf "
     "nach der Straßenverkehrsordnung nur, wer übersehen kann, dass der Gegenverkehr während des ganzen Überholvorgangs "
     "nicht behindert wird. [sicht]Vor der Kuppe konnte Reinhold das nicht. [falsch]Er hat falsch überholt.", PS),
    # --- E grob verkehrswidrig und rücksichtslos ----------------------------------------------------------------------------
    ("[grob]Drittens: grob verkehrswidrig und rücksichtslos. [grob2]Grob verkehrswidrig ist ein objektiv besonders "
     "gefährlicher Verstoß. [grob3]Reinhold überholte ohne jede Sicht auf den Gegenverkehr; das ist ein solcher Verstoß. [rueck]Rücksichtslos ist "
     "subjektiv: Der Fahrer setzt sich aus eigensüchtigen Gründen bewusst über seine Pflichten hinweg, [gleich]oder er "
     "lässt aus Gleichgültigkeit Bedenken gar nicht erst aufkommen. [vertr]Dass er auf einen guten Ausgang vertraut, hilft "
     "ihm nicht. [rein]Reinhold kannte die fehlende Sicht und überholte trotzdem, nur um pünktlich zu sein. Beides liegt "
     "vor.", PS),
    # --- F konkrete Gefahr --------------------------------------------------------------------------------------------------
    ("[gefahr]Viertens die konkrete Gefahr. [beinahe]Nötig ist ein Beinahe-Unfall: Ob es zum Schaden kommt, hängt nur "
     "noch vom Zufall ab; ein Beobachter würde sagen, das ist gerade noch einmal gut gegangen. [gert2]Nur weil Gertrud sofort voll "
     "bremste, kam es nicht zum Zusammenstoß; die Autos verfehlten sich um wenige Meter. Ihr Leib und Leben waren konkret gefährdet. [dadurch]Und die Gefahr "
     "folgt gerade aus dem falschen Überholen.", PS),
    ("[sache]Bei fremden Sachen verlangt der Bundesgerichtshof einen bedeutenden Wert der Sache und einen drohenden "
     "bedeutenden Schaden, [wert]die Grenze liegt jeweils bei siebenhundertfünfzig Euro. [eigen]Das vom Täter geführte Fahrzeug "
     "zählt nicht, auch wenn es ihm nicht gehört; [mitf]Mitfahrer schützt die Norm nur, wenn sie an der Tat nicht "
     "beteiligt sind.", PS),
    # --- G Vorsatz-Fahrlässigkeits-Kombinationen ----------------------------------------------------------------------------
    ("[kombi]Fünftens der subjektive Tatbestand. Es gibt drei Kombinationen. [kvv]Absatz eins: Vorsatz bei Handlung und "
     "Gefahr. [kvf]Absatz drei Nummer eins: vorsätzliche Handlung, aber die Gefahr fahrlässig verursacht. [kff]Absatz drei "
     "Nummer zwei: beides fahrlässig. [rahmen]Die Höchststrafe sinkt dann von fünf auf zwei Jahre.", PS),
    ("[gvors]Gefährdungsvorsatz hat, wer den Beinahe-Unfall für möglich hält und billigend in Kauf nimmt. [rein2]Reinhold "
     "überholte bewusst ohne Sicht, vertraute aber darauf, dass niemand kommt. [fahrl]Dass Gegenverkehr kommen kann, war "
     "vorhersehbar. Die Gefahr verursachte er also fahrlässig: Absatz drei Nummer eins.", PS),
    # --- H Rechtswidrigkeit, Schuld, Konkurrenzen, Ergebnis -----------------------------------------------------------------
    ("[rws]Rechtswidrigkeit und Schuld sind unproblematisch. [konk]Fährt jemand zugleich betrunken, tritt Paragraf "
     "dreihundertsechzehn hinter Paragraf dreihundertfünfzehn c zurück. [erg]Ergebnis: Reinhold ist strafbar nach "
     "Paragraf dreihundertfünfzehn c Absatz eins Nummer zwei b, Absatz drei Nummer eins. [fe]In der Regel wird ihm auch "
     "die Fahrerlaubnis entzogen.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Grob verkehrswidrig und rücksichtslos sind zwei getrennte Merkmale; [tipp2]die Rücksichtslosigkeit "
     "begründest du mit den Motiven des Fahrers. [tipp3]Und den Beinahe-Unfall belegst du mit Tatsachen wie Abständen und "
     "Geschwindigkeiten; dass jemand stark bremsen musste, genügt allein nicht.", PS),
    # --- J Prüfschema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zu Paragraf dreihundertfünfzehn c. [s1]Römisch eins, Tatbestand: Führen eines Fahrzeugs im "
     "Straßenverkehr; [s1b]Tathandlung nach Nummer eins oder Nummer zwei a bis g, [s1c]bei Nummer zwei grob verkehrswidrig "
     "und rücksichtslos; [s1d]konkrete Gefahr, verursacht durch die Tathandlung; [s1e]Vorsatz oder eine Kombination nach "
     "Absatz drei. [s2]Römisch zwei und drei: Rechtswidrigkeit und Schuld. [s3]Dann die Konkurrenzen.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf dreihundertfünfzehn c Absatz eins Nummer zwei verlangt dreierlei: [m2]eine der sieben Todsünden, grob verkehrswidrig "
     "und rücksichtslos begangen, [m3]und dadurch einen Beinahe-Unfall.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
