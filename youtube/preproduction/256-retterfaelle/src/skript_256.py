"""Folge 256 · Retterfälle: Der Retter stirbt – haftet der Brandstifter? (Mo · Der Fall · StGB AT · Klassiker-Fall).
Fiktiver Fall nach dem Plan-Hook („Ein Mann zündet sein Mehrfamilienhaus an; ein Nachbar stürzt beim Versuch, Kinder zu retten,
durch die brennende Decke.“): Siegbert (Anfang 60) legt am Abend im Keller seines vermieteten Mehrfamilienhauses Feuer und geht;
er hofft, dass niemand zu Schaden kommt. Mieterin Liesbeth kommt vom Einkaufen, ihre beiden Kinder sind noch in der Wohnung im
Obergeschoss. Nachbar Arndt (um 40, Haus nebenan) läuft hinein, bringt die Kinder über das Vordach ins Freie und stürzt beim
Rückweg durch die brennende Decke; er stirbt.
Echter Fall: BGH, Urt. v. 8.9.1993 – 3 StR 341/93, BGHSt 39, 322 (Volltext HRRS, Rn. 1–11; Sohn der Hauseigentümer, Tod im Rauch,
§ 222 bestätigt; § 307 Nr. 1 a. F. nicht anwendbar, Rn. 4). Prüfung: § 222 (Wortlautkarte), Kausalität trotz Freiwilligkeit
(Rn. 6), Vorhersehbarkeit (Rn. 7); Problem Selbstgefährdung (Verweis 058, Rn. 9), Abgrenzung Fremdgefährdung (Verweis 203,
ein Satz); BGH: Einschränkung, einsichtiges Motiv, „zugute kommt / einzustehen“ (Rn. 10, Leitsatz 1), Grenze sinnlos /
offensichtlich unverhältnismäßig (Rn. 10); Berufsretter (BGH 4 StR 19/20, BGHSt 66, 119, Leitsatz 1, Rn. 27); Lehre je ein
Satz (ZJS 2016, 62 ff.; Uni Freiburg KK 709); § 306c (Wortlautkarte), Grunddelikt § 306a Abs. 1 Nr. 1, altes Recht, h. L.,
Leichtfertigkeit (BGHSt 46, 279 Rn. 24); Klausurtipp, Schema und Merksatz mit Lexi. Belege je Cue: ../RECHTSSTAND.md.
DARSTELLUNG: Feuer stilisiert (Flammen-Icons, Rauchwolke), keine brennenden Menschen, kein Sturz im Bild, keine Leiche; die
Kinder nur als Silhouetten in Sicherheit; Arndt respektvoll (entschlossen, hilfsbereit). Personen fiktiv.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Arndt marc (Mann, mittel), Liesbeth sabrina (Frau, mittel); Siegbert spricht
nicht. Erzählerin und Lexi: Carla ohne Rolle. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen, Paragrafen und Gerichtsnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Arndt": "marc", "Liesbeth": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Abend vor dem Mehrfamilienhaus ----------------------------------------------------------------------------
    ("[fall]Ein Mittwochabend in der Stadt. [siegbert]Siegbert, Anfang sechzig, besitzt ein Mehrfamilienhaus. "
     "Darin wohnen mehrere Familien. [feuer]Im Keller legt er Feuer und verlässt das Haus. Er hofft, dass "
     "niemand zu Schaden kommt. [rauch]Doch Flammen und Rauch breiten sich schnell aus. [liesbeth]Da "
     "kommt Liesbeth vom Einkaufen. Ihre beiden Kinder sind noch oben in der Wohnung.", 0.2),
    ("[li1]Meine Kinder sind noch da drin!", P, "Liesbeth"),
    ("[arndt]Arndt, um die vierzig, wohnt im Haus nebenan. Er zögert keinen Moment.", 0.2),
    ("[ar1]Ich hole sie raus!", P, "Arndt"),
    ("[rein]Arndt läuft in das brennende Haus. [kinder]Er findet die Kinder und schickt sie über das Vordach ins Freie. "
     "Sie sind in Sicherheit. [decke]Als er selbst folgen will, stürzt er durch die brennende Decke. Arndt stirbt.", 0.4),
    ("[frage]Arndt ging freiwillig ins Feuer. Muss Siegbert trotzdem für seinen Tod einstehen? "
     "[frage2]Oder unterbricht seine freie Entscheidung die Zurechnung?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall --------------------------------------------------------------------------------------------------
    ("[bgh]Der Fall lehnt sich an ein Urteil des Bundesgerichtshofs vom achten September neunzehnhundertdreiundneunzig an. "
     "[bgh2]Dort hatte der Angeklagte während einer Feier ein Wohnhaus angezündet. Der zweiundzwanzigjährige Sohn der "
     "Eigentümer lief ins brennende Obergeschoss, um Sachen oder Menschen zu retten, etwa seinen kleinen Bruder. "
     "[bgh3]Er brach im Rauch bewusstlos zusammen und starb. Der Bundesgerichtshof bestätigte die Verurteilung "
     "wegen fahrlässiger Tötung.", PS),
    # --- D § 222 StGB (Wortlautkarte) --------------------------------------------------------------------------------------
    ("[p222]Prüfen wir Siegbert zuerst nach Paragraf zweihundertzweiundzwanzig: Wer durch Fahrlässigkeit den Tod eines "
     "Menschen verursacht. [erfolg]Der Erfolg ist eingetreten: Arndt ist tot. [kaus]Ohne das Feuer wäre er nicht ins Haus "
     "gelaufen. Dass er sich selbst entschied, unterbricht den Ursachenzusammenhang nicht. [vorh]Das Anzünden "
     "ist sorgfaltswidrig, und dass jemand zur Rettung ins Feuer läuft, war vorhersehbar.", P),
    # --- E Problem: eigenverantwortliche Selbstgefährdung? -----------------------------------------------------------------
    ("[problem]Das Problem liegt bei der Zurechnung. [heroin]Aus dem Heroinspritzen-Fall in Folge achtundfünfzig kennst du "
     "den Grundsatz: Wer nur eine eigenverantwortliche Selbstgefährdung veranlasst oder fördert, dem wird der Erfolg nicht "
     "zugerechnet. [retter]Arndt kannte die Gefahr und ging trotzdem hinein. Also eine Selbstgefährdung? "
     "[fremd]Eine Fremdgefährdung wie beim Rennen aus Folge zweihundertdrei ist es nicht: Den Schritt ins Feuer "
     "beherrschte Arndt selbst.", P),
    # --- F BGHSt 39, 322: Zurechnung bejaht ---------------------------------------------------------------------------------
    ("[nein]Der Bundesgerichtshof lässt den Brandstifter trotzdem haften. [schema]Die Grundsätze aus dem Heroinfall passen "
     "nicht schematisch, wenn der Täter den anderen durch deliktisches Verhalten zur Selbstgefährdung veranlasst. [motiv]Das gilt insbesondere, wenn der Täter die naheliegende Möglichkeit einer solchen Selbstgefährdung "
     "schafft: Er begründet ohne Mitwirkung des Opfers eine erhebliche Gefahr und damit ein einsichtiges Motiv für gefährliche Rettungsmaßnahmen. "
     "[zugute]Der Gedanke dahinter: Gelingt die Rettung, kommt das dem Täter zugute. Misslingt sie, muss er dafür "
     "einstehen. [leitsatz]Der erste Leitsatz ist allgemein gefasst: Stirbt ein Dritter bei Rettungshandlungen, "
     "kann das dem Brandstifter als fahrlässige Tötung zugerechnet werden.", P),
    # --- G Grenze ------------------------------------------------------------------------------------------------------------
    ("[grenze]Die Grenze: Anders mag es bei einem von vornherein sinnlosen oder mit offensichtlich "
     "unverhältnismäßigen Wagnissen verbundenen Rettungsversuch sein. [unvern]Im echten Fall war die Rettung nicht "
     "offenkundig unvernünftig.", P),
    # --- H Subsumtion -------------------------------------------------------------------------------------------------------
    ("[subs]Und Arndt? Zwei Kinder in Lebensgefahr: Ein einsichtigeres Motiv gibt es kaum. [sinn]Seine Rettung war weder "
     "sinnlos noch unvernünftig, sie ist sogar gelungen. [zu222]Der Tod von Arndt ist Siegbert zuzurechnen. "
     "Fahrlässige Tötung liegt vor.", P),
    # --- I Berufsretter -----------------------------------------------------------------------------------------------------
    ("[beruf]Zweitausendeinundzwanzig hat der Bundesgerichtshof das auf Berufsretter übertragen, etwa auf "
     "Feuerwehrleute. [pflicht]Bei ihnen tritt an die Stelle des einsichtigen Motivs die Rechtspflicht zum Eingreifen.", PS),
    # --- J Lehre ------------------------------------------------------------------------------------------------------------
    ("[lehre]In der Lehre ist das umstritten. [l1]Nach einer Ansicht gefährdet sich der freiwillige Retter eigenverantwortlich, "
     "die Zurechnung entfällt. [l2]Andere rechnen nur zu, wenn der Retter zur Rettung verpflichtet ist oder aus einer "
     "notstandsähnlichen Zwangslage handelt. [l3]Wieder andere rechnen gefährliche Rettungen dem Erstverursacher unabhängig "
     "von einer Rettungspflicht zu, weil sie zu seiner Risikosphäre gehören.", PS),
    # --- K § 306c StGB (Wortlautkarte) --------------------------------------------------------------------------------------
    ("[p306c]Bleibt die Brandstiftung mit Todesfolge, Paragraf dreihundertsechs c: Verursacht der Täter durch eine "
     "Brandstiftung wenigstens leichtfertig den Tod eines anderen Menschen. [grund]Grunddelikt ist die schwere "
     "Brandstiftung nach Paragraf dreihundertsechs a, denn das Haus dient der Wohnung von Menschen, auch wenn es Siegbert "
     "gehört. [alt]Im echten Fall half die Vorgängervorschrift nicht: Das Opfer musste sich zur Zeit der "
     "Tat im Gebäude befinden, der Retter war es nicht. [heute]Der heutige Paragraf verzichtet darauf. "
     "Nach herrschender Lehre erfasst er deshalb grundsätzlich auch den Retter, außer bei unvernünftig großem Risiko. [leicht]Dazu muss Siegbert wenigstens leichtfertig gehandelt haben, also aus "
     "besonderem Leichtsinn oder besonderer Gleichgültigkeit. [leicht2]Wer ein bewohntes Haus anzündet, dem drängt "
     "sich auf, dass Menschen sterben können, auch Retter. Dann greift Paragraf dreihundertsechs c. [p222neben]Fehlt die Leichtfertigkeit, bleibt Paragraf "
     "zweihundertzweiundzwanzig.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Den Retter prüfst du bei der objektiven Zurechnung, bei Paragraf dreihundertsechs c im spezifischen "
     "Gefahrzusammenhang. [k1]Prüfe dort die eigenverantwortliche Selbstgefährdung und stell den Streit kurz dar. [k2]Dann frag: Gab es ein einsichtiges Motiv, und war die Rettung nicht offensichtlich unvernünftig?", P),
    # --- M Klausurschema (Lexi), progressiv --------------------------------------------------------------------------------
    ("[sch]Dein Schema: [s1]Erstens die schwere Brandstiftung nach Paragraf dreihundertsechs a. [s2]Zweitens "
     "Paragraf dreihundertsechs c: der Tod eines anderen Menschen durch die Brandstiftung, [s3]die Zurechnung trotz "
     "Rettungshandlung [s4]und wenigstens Leichtfertigkeit. [s5]Drittens, ohne "
     "Leichtfertigkeit, die fahrlässige Tötung.", PS),
    # --- N Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Nach dem Bundesgerichtshof wird dem Brandstifter auch der Tod des Retters zugerechnet, wenn er "
     "ein einsichtiges Motiv zur Rettung geschaffen hat. [m2]Anders kann es nur bei einem sinnlosen oder offensichtlich unverhältnismäßigen "
     "Rettungsversuch sein.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
