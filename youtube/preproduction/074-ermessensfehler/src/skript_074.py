"""Folge 074 · Ermessensfehler: Was darf das Gericht kontrollieren? (§ 114 VwGO) (Mi · Examenswissen · Verwaltungsrecht AT,
Format Schema). Übungsfall nach dem Hook des Themenplans („Das machen wir grundsätzlich nie.“), Beispielland
Nordrhein-Westfalen: Frau Kampmann beantragt für ihr Café in der Altstadt eine Sondernutzungserlaubnis für vier Tische auf
dem breiten Gehweg (§ 18 Abs. 1 StrWG NRW; Ermessen: OVG NRW 11 A 114/20 Rn. 29, 58). Herr Hornung von der Stadt lehnt ab:
„Das machen wir grundsätzlich nie.“ Sie klagt; im Prozess trägt die Stadt erstmals Gründe vor (Platz für Fußgänger).
Kern: gebunden – Ermessen (kann/soll, BVerwG 9 B 79.09 Rn. 2), Rechtsfolgenseite, Entschließungs-/Auswahlermessen,
Beurteilungsspielraum nur ein Satz (BVerwG 3 B 11.16 Rn. 8); Wortlautkarten § 40 VwVfG und § 114 VwGO; Kontrolle nur auf
Rechtsfehler; Ermessensnichtgebrauch (BVerwG 1 C 20.05 Rn. 17–19), Fehlgebrauch/Defizit (straßenbezogene Gründe,
wettbewerbsneutral: OVG NRW 11 A 1081/12 Rn. 9, 11), Überschreitung (§ 18 Abs. 2 StrWG NRW; Verhältnismäßigkeit),
Reduzierung auf null (BVerwG 1 B 16.13 Rn. 4); § 39 Abs. 1 Satz 3 VwVfG ein Satz; § 114 Satz 2: nur Ergänzung
(BVerwG 8 C 25.19 Rn. 13; 1 C 20.05 Rn. 22; 1 C 14.10 Rn. 9); Verpflichtungsklage → Bescheidungsurteil § 113 Abs. 5 Satz 2.
Fiktive Figuren: Frau Kampmann (ela_froh), Herr Hornung (helmut), die Richterin (julia). Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Kampmann": "ela_froh", "Hornung": "helmut", "Richterin": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Café und der Antrag ----------------------------------------------------------------------------------
    ("[fall]Frau Kampmann hat ein kleines Café in der Altstadt. [antrag]Sie beantragt bei der Stadt, im Sommer vier Tische "
     "auf den breiten Gehweg vor ihrem Café stellen zu dürfen. [hornung]Herr Hornung von der Stadt bringt die Antwort.", 0.2),
    ("[ho1]Frau Kampmann, Tische auf dem Gehweg? Das machen wir grundsätzlich nie. Ihr Antrag ist abgelehnt.", 0.3, "Hornung"),
    ("[ka1]Nie? Sie haben sich meinen Gehweg doch gar nicht angesehen!", 0.3, "Kampmann"),
    ("[klage]Frau Kampmann klagt beim Verwaltungsgericht. [frage]Was darf das Gericht hier kontrollieren? [frage2]Und hat "
     "die Klage Erfolg?", 0.6),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Die Norm: Sondernutzung ---------------------------------------------------------------------------------------
    ("[norm]Wer Tische auf den Gehweg stellt, nutzt die Straße über den Gemeingebrauch hinaus: eine Sondernutzung. "
     "[norm2]Sie braucht eine Erlaubnis, in Nordrhein-Westfalen nach Paragraf achtzehn Straßen- und Wegegesetz. "
     "[norm3]Über die Erlaubnis entscheidet die Stadt nach Ermessen. [land]In deinem Land steht das unter einer anderen "
     "Nummer.", P),
    # --- D Gebunden oder Ermessen ----------------------------------------------------------------------------------------
    ("[geb]Die erste Frage lautet immer: Ist die Behörde gebunden, oder hat sie Ermessen? [muss]Heißt es im Gesetz "
     "„muss“ oder „ist zu“, ist die Entscheidung gebunden: Liegt der Tatbestand vor, folgt die Rechtsfolge zwingend. "
     "[kann]Heißt es „kann“, hat die Behörde Ermessen. [soll]„Soll“ bindet im Regelfall, Ermessen bleibt nur im atypischen "
     "Fall.", P),
    ("[rfs]Ermessen sitzt auf der Rechtsfolgenseite: [ent]ob die Behörde handelt, das Entschließungsermessen, [aus]und "
     "wie sie handelt, das Auswahlermessen. [bsr]Unbestimmte Rechtsbegriffe im Tatbestand prüft das Gericht dagegen "
     "grundsätzlich voll. Ein Beurteilungsspielraum ist die seltene Ausnahme.", P),
    # --- E Wortlaut § 40 VwVfG -----------------------------------------------------------------------------------------
    ("[wl40]Wie die Behörde ihr Ermessen ausüben muss, sagt Paragraf vierzig Verwaltungsverfahrensgesetz: Ist die Behörde "
     "ermächtigt, nach ihrem Ermessen zu handeln, hat sie ihr Ermessen entsprechend dem Zweck der Ermächtigung auszuüben "
     "[grenz]und die gesetzlichen Grenzen des Ermessens einzuhalten. [nrw40]Für die Stadt gilt das gleichlautende "
     "Landesgesetz.", P),
    # --- F Wortlaut § 114 Satz 1 VwGO ------------------------------------------------------------------------------------
    ("[wl114]Und was kontrolliert das Gericht? Nach Paragraf hundertvierzehn Satz eins Verwaltungsgerichtsordnung prüft "
     "es, ob die Behörde die gesetzlichen Grenzen des Ermessens überschritten [zweck]oder ihr Ermessen nicht dem Zweck der "
     "Ermächtigung entsprechend gebraucht hat. [nurrf]Das Gericht prüft also nur Rechtsfehler. [nicht]Ob eine andere "
     "Lösung zweckmäßiger wäre, entscheidet es nicht. Es setzt sein Ermessen nicht an die Stelle der Behörde.", P),
    # --- G Die drei Ermessensfehler ----------------------------------------------------------------------------------------
    ("[drei]Daraus folgen drei Ermessensfehler. [f1]Erstens, der Ermessensnichtgebrauch, auch Ermessensausfall: Die "
     "Behörde übt ihr Ermessen gar nicht aus, etwa weil sie sich für gebunden hält. [f1b]Genau das steckt in „Das machen "
     "wir grundsätzlich nie“: Wer pauschal ablehnt, schaut sich den Einzelfall nicht an.", P),
    ("[f2]Zweitens, der Ermessensfehlgebrauch: Die Behörde lässt sich von sachfremden Erwägungen leiten [defizit]oder "
     "lässt wichtige Gesichtspunkte weg, das Ermessensdefizit. [f2b]Bei der Sondernutzung zählen nur Gründe mit Bezug zur "
     "Straße, etwa die Sicherheit und Leichtigkeit des Verkehrs oder das Stadtbild. [f2c]Lehnt die Stadt ab, um den Wirt "
     "nebenan vor Konkurrenz zu schützen, ist das sachfremd.", P),
    ("[f3]Drittens, die Ermessensüberschreitung: Die Behörde wählt eine Rechtsfolge, die das Gesetz nicht vorsieht, "
     "[f3b]etwa eine Erlaubnis für immer, obwohl sie nur auf Zeit oder auf Widerruf erteilt werden darf. [f3c]Dazu zählt "
     "auch ein Verstoß gegen Grundrechte oder die Verhältnismäßigkeit: Genügt eine Auflage, etwa einen Durchgang frei "
     "zu halten, kann eine Ablehnung unverhältnismäßig sein.", P),
    ("[null]Manchmal schrumpft das Ermessen sogar auf null. Dann ist nur noch eine Entscheidung rechtmäßig, [null2]und das "
     "Gericht kann die Behörde direkt dazu verpflichten.", P),
    # --- H Subsumtion im Fall ----------------------------------------------------------------------------------------------
    ("[zurueck]Zurück zu Frau Kampmann. [ausfall]Die Stadt hat nur gesagt: grundsätzlich nie. Mit ihrem Gehweg, den vier "
     "Tischen und dem Platz für Fußgänger hat sie sich nicht befasst. [ausfall2]Das ist ein Ermessensausfall, die "
     "Ablehnung ist rechtswidrig. [begr]Das zeigt auch die Begründung: Nach Paragraf neununddreißig soll sie die "
     "Gesichtspunkte erkennen lassen, von denen die Behörde bei ihrem Ermessen ausgegangen ist.", P),
    # --- I Nachschieben, § 114 Satz 2 ------------------------------------------------------------------------------------
    ("[prozess]Im Prozess trägt die Stadt erstmals vor, Fußgänger bräuchten dort Platz. [wl1142]Hilft ihr Satz zwei? Die "
     "Verwaltungsbehörde kann ihre Ermessenserwägungen hinsichtlich des Verwaltungsaktes auch noch im "
     "verwaltungsgerichtlichen Verfahren ergänzen. [ergaenzen]Ergänzen heißt: vorhandene Erwägungen vervollständigen. "
     "[heilung]Ein Ermessensausfall lässt sich so nach dem Bundesverwaltungsgericht nicht heilen. Hatte die Behörde von "
     "Anfang an Ermessen, kann sie es im Prozess nicht erstmals ausüben.", P),
    # --- J Ergebnis: Bescheidungsurteil ------------------------------------------------------------------------------------
    ("[vk]Frau Kampmann will die Erlaubnis, also erhebt sie eine Verpflichtungsklage. [spruch]Das Ermessen ist aber nicht "
     "auf null geschrumpft, die Sache ist nicht spruchreif. [bu]Deshalb ergeht ein Bescheidungsurteil nach Paragraf "
     "hundertdreizehn Absatz fünf Satz zwei. [verweis]Mehr dazu im Video zu den Klagearten. [urteil]Die Richterin "
     "verkündet:", 0.2),
    ("[ri1]Der Bescheid wird aufgehoben. Die Stadt muss unter Beachtung der Rechtsauffassung des Gerichts neu entscheiden. "
     "Im Übrigen wird die Klage abgewiesen.", 0.4, "Richterin"),
    ("[teil]Ein Teilerfolg: Frau Kampmann bekommt eine neue, fehlerfreie Entscheidung. [neu]Dann darf die Stadt den Platz "
     "für Fußgänger abwägen.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ermessen prüfst du in der Begründetheit, bei der Rechtsfolge, erst wenn der Tatbestand steht. "
     "[tipp1]Benenne dann den Fehler genau: Nichtgebrauch, Fehlgebrauch oder Überschreitung. [tipp2]Und fehlt jede "
     "Ermessenserwägung, hilft kein Nachschieben.", PS),
    # --- L Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Eins: Räumt die Norm Ermessen ein? [s2]Zwei: Liegt ein Ermessensfehler nach Paragraf "
     "hundertvierzehn Satz eins vor? [s3]Nichtgebrauch, [s4]Fehlgebrauch, [s5]Überschreitung. [s6]Drei: Ist das Ermessen "
     "auf null reduziert? [s7]Vier: Wurden Erwägungen zulässig ergänzt? [s8]Fünf: die Folge, Aufhebung, Bescheidung oder "
     "Verpflichtung.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Beim Ermessen prüft das Gericht nur Rechtsfehler, nicht die Zweckmäßigkeit. [m2]Und wer sein Ermessen "
     "nie ausgeübt hat, kann im Prozess nichts ergänzen.", 1.4),
]
