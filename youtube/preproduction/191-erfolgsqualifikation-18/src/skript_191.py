"""Folge 191 · Erfolgsqualifiziertes Delikt Schema: Gefahrzusammenhang & § 18 (Mi · Examenswissen · StGB AT, Format Schema).
Neuer Zuschnitt (der Plan-Hook Faustschlag/Bordstein ist in Folge 155 verfilmt, dort nur in einem Satz verwiesen): das
allgemeine AT-Schema der Erfolgsqualifikation an einem neuen Fall, Freiheitsberaubung mit Todesfolge § 239 Abs. 4 StGB.
Fall: Bertram und Hubertus wohnen zusammen in einer Wohnung im 2. Stock. Nach einem Streit schließt Bertram Hubertus in
dessen Zimmer ein und nimmt den Schlüssel mit. Hubertus will hinaus, steigt aus dem Fenster, stürzt ab und stirbt (nur als
Text und Fenster-Icon, kein Sturz im Bild). Bertram wollte ihn nur eine Weile einsperren, mit einer Flucht durchs Fenster hat
er nicht gerechnet.
Aufbau: Fall → Frage → Sachverhalt → Struktur (Grunddelikt + schwere Folge; Verweis 155) → Wortlautkarte § 18 → § 11 Abs. 2
(Wortlautkarte), Teilnahme und Versuch möglich → Schema I.–V. als Tafel → Wortlautkarte § 239 Abs. 1, 4 → I. Grunddelikt
(Einsperren nicht unüberwindlich, 1 StR 590/00 Rn. 1; Verweis 029) → II. Tod, Kausalität → III. Gefahrzusammenhang (BGHSt 62, 49
Rn. 14 f.; Fluchtreaktion; BGHSt 19, 382, 386 f. nach 3 StR 279/20 Rn. 18; Selbstgefährdung ein Satz, BGHSt 62, 49 Rn. 17, 20)
→ IV. Fahrlässigkeit (BGHSt 62, 49 Rn. 22; 3 StR 279/20 Rn. 18; Verweis 182) → V. RW/Schuld → Ergebnis → Versuch (3 StR 415/20
Rn. 9, 12, 15; BGHSt 42, 158 Rn. 8 f., 12, 16 f., 26) → fahrlässig/leichtfertig (§ 251, 5 StR 628/14 Rn. 8) → Klausurtipp →
Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Bertram (Täter), Hubertus (Opfer).
Stimmen nur aus dem Pool: Bertram william (Mann, älter), Hubertus marc (Mann, mittel). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Bertram": "william", "Hubertus": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Wohnung im zweiten Stock -----------------------------------------------------------------------------------
    ("[fall]Eine Wohnung im zweiten Stock. [wg]Bertram und Hubertus wohnen hier zusammen. [streit]Eines Abends "
     "streiten sie.", P),
    ("[h1]Lass mich einfach in Ruhe!", P, "Hubertus"),
    ("[b1]Du bleibst da drin, bis du dich beruhigt hast.", P, "Bertram"),
    ("[schloss]Bertram schließt die Zimmertür von außen ab und nimmt den Schlüssel mit.", P),
    ("[h2]Mach sofort die Tür auf!", P, "Hubertus"),
    ("[fenster]Hubertus will hinaus und steigt aus dem Fenster. [tod]Er stürzt ab und stirbt. [nicht]Bertram wollte ihn nur "
     "eine Weile einsperren. Mit einer Flucht durchs Fenster hat er nicht gerechnet.", 0.4),
    ("[frage]Haftet Bertram für den Tod? [frage2]Und wie prüfst du ein erfolgsqualifiziertes Delikt?", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Struktur, § 18, § 11 Abs. 2 ------------------------------------------------------------------------------------------
    ("[eq]Bertram hat Hubertus vorsätzlich eingesperrt, daraus folgte der Tod. [eq2]Das ist ein erfolgsqualifiziertes "
     "Delikt: vorsätzliches Grunddelikt plus schwere Folge mit höherer Strafe. [v155]Den Faustschlag mit "
     "tödlichem Sturz zeigt das Video zur Körperverletzung mit Todesfolge. Hier geht es um das allgemeine Schema.", PS),
    ("[p18]Die Grundregel steht in Paragraf achtzehn: Knüpft das Gesetz an eine besondere Folge der Tat eine schwerere "
     "Strafe, so trifft sie den Täter oder den Teilnehmer nur, wenn ihm hinsichtlich dieser Folge wenigstens Fahrlässigkeit "
     "zur Last fällt. [vf]Also Vorsatz für das Grunddelikt und wenigstens Fahrlässigkeit für die Folge. [wenig]Wenigstens "
     "heißt: Vorsatz bezüglich der Folge schadet nicht.", PS),
    ("[p112]Und Paragraf elf Absatz zwei bestimmt: Eine solche Vorsatz-Fahrlässigkeits-Kombination gilt als vorsätzliche "
     "Tat. [teiln]Deshalb sind Anstiftung und Beihilfe möglich, denn sie setzen eine vorsätzliche Haupttat voraus. "
     "[teiln2]Für die Folge haftet der Teilnehmer aber nur, wenn ihm selbst wenigstens Fahrlässigkeit zur Last fällt. [versuch]Auch "
     "der Versuch ist möglich.", PS),
    # --- D Schema als Tafel -----------------------------------------------------------------------------------------------------
    ("[sch]Daraus folgt das Schema. [s1]Römisch eins: das Grunddelikt, objektiv und subjektiv. [s2]Römisch zwei: die schwere "
     "Folge und ihre Kausalität. [s3]Römisch drei: der spezifische Gefahrzusammenhang. [s4]Römisch vier: wenigstens "
     "Fahrlässigkeit bezüglich der Folge, manchmal Leichtfertigkeit, etwa beim Raub mit Todesfolge. [s5]Römisch fünf: Rechtswidrigkeit und Schuld, dort auch die subjektive Vorhersehbarkeit.", PS),
    # --- E Wortlautkarte § 239, I. Grunddelikt, II. Folge -----------------------------------------------------------------------
    ("[p239]Im Fall gilt Paragraf zweihundertneununddreißig Absatz vier: [abs4]Verursacht der Täter durch die Tat oder eine während der "
     "Tat begangene Handlung den Tod des Opfers, so ist die Strafe Freiheitsstrafe nicht unter drei Jahren.", PS),
    ("[gd]Römisch eins, das Grunddelikt nach Absatz eins: Bertram hat Hubertus eingesperrt. [fenst]Das Fenster ändert daran nichts. Einsperren muss nicht "
     "unüberwindlich sein; es genügt, dass der gewöhnliche Ausgang versperrt ist. [vors]Und er handelte vorsätzlich, mehr "
     "dazu im Video zu den Vorsatzformen. [folge]Römisch zwei: Hubertus ist tot. [kaus]Ohne das Einsperren wäre er "
     "nicht hinausgeklettert, die Tat war ursächlich. [nurk]Doch bloße Kausalität reicht nicht.", PS),
    # --- F III. Spezifischer Gefahrzusammenhang ---------------------------------------------------------------------------------
    ("[spez]Römisch drei, der Kern: der spezifische Gefahrzusammenhang. [formel]Nach dem Bundesgerichtshof sollen "
     "erfolgsqualifizierte Delikte der Gefahr entgegenwirken, die mit dem jeweiligen Grunddelikt verbunden ist. [nieder]Gerade "
     "diese Gefahr muss sich in der Folge niederschlagen.", PS),
    ("[typ]Wer eingesperrt ist, will hinaus. [typ2]Ein riskanter Fluchtversuch ist deshalb eine typische Gefahr der "
     "Freiheitsberaubung. [bgh64]Schon neunzehnhundertvierundsechzig hat der Bundesgerichtshof auch Folgen eines "
     "Selbstbefreiungsversuchs erfasst. [selbst]Anders kann es liegen, wenn sich das Opfer frei verantwortlich selbst "
     "gefährdet und sein Verhalten nicht von der Tat bestimmt ist. [hier]Hubertus aber stieg aus dem Fenster, um der "
     "Freiheitsberaubung zu entkommen. [gz_ok]Der Gefahrzusammenhang liegt vor.", PS),
    # --- G IV. Fahrlässigkeit, V. RW/Schuld, Ergebnis ---------------------------------------------------------------------------
    ("[fahrl]Römisch vier, die Fahrlässigkeit. Die Pflichtwidrigkeit liegt schon im vorsätzlichen Grunddelikt, [vorh]entscheidend "
     "ist die Vorhersehbarkeit. [bgh21]Zweitausendeinundzwanzig hat der Bundesgerichtshof bei einem Sturz aus dem Fenster "
     "betont: Bei einem Fluchtversuch ist die Folge in der Regel vorhersehbar, weil der Mensch natürlicherweise bestrebt ist, sich der "
     "Freiheitsberaubung zu entziehen. [v182]Mehr im "
     "Video zum Fahrlässigkeitsdelikt.", PS),
    ("[rws]Römisch fünf: Bertram handelte rechtswidrig und schuldhaft, auch er persönlich konnte den tödlichen Ausgang "
     "vorhersehen. [erg]Ergebnis: Freiheitsberaubung mit Todesfolge nach Paragraf "
     "zweihundertneununddreißig Absatz vier.", PS),
    # --- H Versuch und Rücktritt ------------------------------------------------------------------------------------------------
    ("[vers]Jetzt der Versuch. "
     "[zwei]Zwei Fälle musst du trennen. [eqv]Beim erfolgsqualifizierten Versuch bleibt das Grunddelikt im Versuch stecken, "
     "doch die schwere Folge tritt ein. [eqv2]Beispiel: Bei einem versuchten Raub löst sich ein Schuss und tötet einen "
     "Menschen; Beute machen die Täter nicht. [veq]Bei der versuchten Erfolgsqualifikation ist das Grunddelikt verwirklicht, "
     "die in Kauf genommene oder gewollte Folge bleibt aber aus. [veq2]Beispiel: Jemand setzt ein Wohnhaus in "
     "Brand und rechnet mit dem Tod der Bewohner, doch alle überleben.", PS),
    ("[rt]Und der Rücktritt? [rt2]Der Bundesgerichtshof entschied neunzehnhundertsechsundneunzig: Vom Raubversuch "
     "kann der Täter noch zurücktreten, auch wenn der Tod schon eingetreten ist. [rt3]Denn der Rücktritt bezieht sich auf das Grunddelikt. Entfällt dessen Strafbarkeit, fehlt der "
     "Anknüpfungspunkt für die Folge. [rt4]In Betracht kommt dann noch die fahrlässige Tötung.", PS),
    # --- I Fahrlässig oder leichtfertig -----------------------------------------------------------------------------------------
    ("[wf]Zurück zu Römisch vier: Fahrlässigkeit genügt, wo die Norm nichts anderes sagt, wie bei der "
     "Freiheitsberaubung mit Todesfolge. [p251]Paragraf zweihunderteinundfünfzig verlangt dagegen, dass der Täter den Tod "
     "wenigstens leichtfertig verursacht. [lf]Leichtfertig ist eine gesteigerte Fahrlässigkeit: [lf2]Der Täter lässt die "
     "sich aufdrängende Möglichkeit eines tödlichen Verlaufs aus besonderem Leichtsinn oder besonderer Gleichgültigkeit "
     "außer Acht.", PS),
    # --- J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag beim Gefahrzusammenhang, welche typische Gefahr gerade dieses Grunddelikt schafft. Beim "
     "Einsperren ist es die Flucht. [tipp2]Und lies den Wortlaut: Steht dort leichtfertig, reicht einfache "
     "Fahrlässigkeit nicht.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------------
    ("[merke]Merke: vorsätzliches Grunddelikt, schwere Folge, spezifischer Gefahrzusammenhang und wenigstens Fahrlässigkeit. "
     "[m2]Und weil das Ganze als vorsätzliche Tat gilt, sind Versuch und Teilnahme möglich.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
