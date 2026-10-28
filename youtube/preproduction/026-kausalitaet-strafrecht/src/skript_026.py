"""Folge 026 · Kausalität im Strafrecht: Conditio-sine-qua-non einfach erklärt (Examenswissen, Format Schema).
Fiktiver Fall (Personen erfunden, Hook des Themenplans): Kioskbesitzer Egon verkauft Bodo ein Feuerzeug, mit dem Bodo nachts
die Scheune der Landwirtin Maren anzündet. Verletzt wird niemand. Erfolgsdelikte (§§ 212, 222, 306 StGB), Bedingungstheorie
(BGH: BGHSt 39, 195; 49, 1; 4 StR 138/22), Reserveursache, Dazwischentreten eines Dritten (keine Unterbrechung, BGH 3 StR 394/20,
4 StR 223/15), Kausalität ist nur die erste Hürde (objektive Zurechnung: Lehre, eigene Folge). Abwandlungen: überholende
Kausalität (Blitz überholt die Kerze -> nur Versuch), alternative Kausalität (zwei unabhängige Feuer, BGHSt 39, 195 zwei Schüsse),
kumulative Kausalität; Ausblick Unterlassen (Quasi-Kausalität, BGH 4 StR 200/21). Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Egon": "helmut", "Bodo": "stephan", "Maren": "ela_warm"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: am Dorfkiosk ------------------------------------------------------------------------------------------
    ("[fall]Freitagabend am Dorfkiosk. [egon]Egon, Mitte sechzig, steht hinter seiner Theke. [bodo]Da kommt Bodo herein.", 0.3),
    ("[b1]Ein Feuerzeug, bitte.", 0.3, "Bodo"),
    ("[e1]Macht zwei Euro.", 0.4, "Egon"),
    ("[ahnt]Egon ahnt nichts. [nacht]In der Nacht geht Bodo zur Scheune der Landwirtin Maren. [zuend]Mit dem Feuerzeug zündet "
     "er das Stroh an. [brand]Die Scheune brennt nieder, verletzt wird niemand.", 0.3),
    ("[m1]Meine Scheune!", 0.4, "Maren"),
    ("[frage]Ist der Verkauf des Feuerzeugs kausal für den Brand? [frage2]Und reicht das schon, um Egon zu bestrafen?", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Erfolgsdelikte ----------------------------------------------------------------------------------------------
    ("[erfolg]Kausalität prüfst du bei jedem Erfolgsdelikt. Dort gehört ein Erfolg zum Tatbestand, etwa der Tod beim "
     "Totschlag, Paragraf zweihundertzwölf. [p222]Bei der fahrlässigen Tötung steht es sogar im Gesetz: Wer durch Fahrlässigkeit "
     "den Tod eines Menschen verursacht. [p306]In unserem Fall ist der Erfolg der Brand der Scheune, Brandstiftung nach "
     "Paragraf dreihundertsechs.", PS),
    # --- D Bedingungstheorie -------------------------------------------------------------------------------------------
    ("[csqn]Wann ist eine Handlung ursächlich? Der Bundesgerichtshof wendet die Bedingungstheorie an. [formel]Ursächlich ist "
     "jede Bedingung, die nicht hinweggedacht werden kann, ohne dass der Erfolg in seiner konkreten Gestalt entfiele. "
     "Das ist die Conditio-sine-qua-non-Formel. [aequi]Die Lehre spricht von der Äquivalenztheorie, denn alle Bedingungen sind gleichwertig.", P),
    # --- E Subsumtion Bodo, Egon ---------------------------------------------------------------------------------------
    ("[bodo_k]Zuerst Bodo: Denk das Anzünden weg, dann brennt die Scheune nicht. Kausal. [egon_k]Jetzt Egon: Denk den Verkauf "
     "weg, dann hat Bodo in dieser Nacht kein Feuerzeug, und die Scheune brennt nicht so, wie sie gebrannt hat. Auch der "
     "Verkauf ist kausal. [weit]Nach dieser Formel wäre sogar der Hersteller des Feuerzeugs kausal. Die Formel allein "
     "reicht also sehr weit.", P),
    # --- F Reserveursache ----------------------------------------------------------------------------------------------
    ("[reserve]Bodo wendet ein:", 0.2),
    ("[b2]Ohne Egon hätte ich eben Streichhölzer geholt.", 0.4, "Bodo"),
    ("[res2]Das hilft nicht. Kausal bleibt eine Bedingung auch dann, wenn sonst ein anderer gehandelt und denselben Erfolg "
     "herbeigeführt hätte. [res3]Solche Ersatzursachen bleiben außer Betracht. Es zählt der tatsächliche Ablauf.", P),
    # --- G Unterbrechung? ----------------------------------------------------------------------------------------------
    ("[dritt]Unterbricht wenigstens Bodos eigene Tat den Zusammenhang? [neu]Nein. Unterbrochen ist er nur, wenn ein späteres "
     "Ereignis die Fortwirkung der ersten Bedingung beseitigt und allein eine neue Ursachenreihe eröffnet. [knuepft]Bodo "
     "knüpft aber an das Feuerzeug an. Dass ein Dritter vorsätzlich mitwirkt, ändert an der Kausalität nichts.", P),
    # --- H Nur die erste Hürde -----------------------------------------------------------------------------------------
    ("[huerde]Ist Egon damit schon strafbar? So schnell geht es nicht. Kausalität ist nur die erste Hürde. [zurech]Ob ihm der "
     "Brand zuzurechnen ist, prüft die Lehre im nächsten Schritt, der objektiven Zurechnung. Dazu gibt es eine eigene Folge. "
     "[vors]Und Vorsatz hatte Egon ohnehin nicht, denn er wusste nichts von Bodos Plan.", PS),
    # --- I Abwandlung 1: überholende Kausalität ------------------------------------------------------------------------
    ("[var1]Abwandlung eins: Bodo stellt eine brennende Kerze ins Stroh. Sie soll in einer Stunde das Stroh entzünden. "
     "[blitz]Doch vorher schlägt ein Blitz ein, und die Scheune brennt ab, ehe die Kerze heruntergebrannt ist. "
     "[ueberh]Der Blitz hat eine neue Ursachenreihe eröffnet und die Kerze überholt. Die Lehre nennt das überholende "
     "Kausalität. [versuch]Bodos Kerze ist für den Brand nicht kausal. Ihm bleibt nur versuchte Brandstiftung, Paragrafen "
     "dreihundertsechs, zweiundzwanzig und dreiundzwanzig.", PS),
    # --- J Abwandlung 2: alternative Kausalität ------------------------------------------------------------------------
    ("[var2]Abwandlung zwei: In derselben Nacht legt auch Silke Feuer, unabhängig von Bodo, am anderen Ende der Scheune. "
     "[jedes]Beide Feuer wachsen zusammen, und jedes hätte die Scheune auch allein zerstört. [streng]Streng nach der Formel könnte man Bodos Feuer wegdenken, "
     "und die Scheune brennt trotzdem. Bei Silke genauso. Dann wäre keiner kausal.", P),
    ("[alt]Das kann nicht stimmen. Der Bundesgerichtshof hat bei zwei Schüssen, von denen jeder allein tödlich war, beide "
     "als ursächlich angesehen. [altlehre]Die Lehre spricht von alternativer Kausalität und passt die Formel an: Von mehreren "
     "Bedingungen, die zwar alternativ, aber nicht kumulativ hinweggedacht werden können, ist jede ursächlich.", PS),
    # --- K Abwandlung 3: kumulative Kausalität -------------------------------------------------------------------------
    ("[var3]Abwandlung drei: Bodo und Silke legen wieder Feuer, doch jedes wäre im feuchten Stroh allein erloschen. Erst zusammen greift der Brand auf die "
     "Scheune über. [kum]Das nennt die Lehre kumulative Kausalität. Denkt man einen Beitrag weg, entfällt der Erfolg. Also "
     "sind beide kausal. [kum2]Ob ihnen der Brand auch zuzurechnen ist, klärt wieder erst der nächste Prüfungsschritt.", PS),
    # --- L Ausblick Unterlassen ----------------------------------------------------------------------------------------
    ("[unterl]Ein Ausblick zum Unterlassen: Dort fehlt eine Handlung, die man wegdenken kann. [quasi]Man denkt deshalb die "
     "gebotene Handlung hinzu. Quasi-kausal ist das Unterlassen, wenn der Erfolg dann mit an Sicherheit grenzender "
     "Wahrscheinlichkeit ausgeblieben wäre.", PS),
    # --- M Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ist die Kausalität offensichtlich, genügt ein Satz. [tipp2]Ausführlich wird es nur in Sonderfällen: "
     "bei Ersatzursachen und bei alternativer, kumulativer oder überholender Kausalität. [tipp3]Und schränke nicht schon bei "
     "der Kausalität ein. Wertungen gehören erst in die nächsten Prüfungsschritte.", PS),
    # --- N Klausurschema -----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den objektiven Tatbestand eines Erfolgsdelikts. [k1]Erstens die Handlung, [k2]zweitens der "
     "Erfolg. [k3]Drittens die Kausalität nach der Formel. [k3a]Ersatzursachen bleiben außer Betracht. [k3b]Bei alternativer "
     "Kausalität gilt die angepasste Formel, [k3c]bei kumulativer Kausalität sind alle Beiträge kausal, [k3d]und eine "
     "überholte Bedingung ist nicht kausal. [k4]Viertens nach der Lehre die objektive Zurechnung.", PS),
    # --- O Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Kausal ist jede Bedingung, die man nicht wegdenken kann, ohne dass der konkrete Erfolg entfiele. "
     "[m2]Ersatzursachen, die nicht gewirkt haben, zählen nicht. [m3]Und kausal heißt noch nicht strafbar.", 1.4),
]
