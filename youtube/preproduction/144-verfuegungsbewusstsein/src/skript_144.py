"""Folge 144 · Verfügungsbewusstsein: Versteckte Ware – Diebstahl oder Betrug? (Fr · Klausurpraxis · StGB BT, Format Abgrenzung).
Fall nach dem Plan-Hook: Fabian versteckt im Supermarkt Kopfhörer (120 €) in einer Waschmittelpackung, verschließt sie und legt
an der Kasse nur die Packung aufs Band; Kassiererin Carina scannt das Waschmittel (8 €), Fabian zahlt und verlässt den Laden.
Prüfung: Abgrenzung (Fremd-/Selbstschädigung, Exklusivität; BGHSt 41, 198, 201 nach BGHSt 17, 205; BGH 1 StR 402/16 Rn. 11)
→ Wortlautkarten § 242 Abs. 1, § 263 Abs. 1 (Verfügung nur Verweis auf Folge 065) → Kernfrage Verfügungsbewusstsein
(BGHSt 41, 198, 202 f.: Konkretisierung durch Eintippen, genereller Verfügungswille „bloße Fiktion“; Gegenansicht OLG Düsseldorf
NJW 1993, 1407 nur nach der Wiedergabe im BGH-Beschluss; Nachfrage an der Kasse S. 203; § 252-Argument S. 203 f.)
→ Subsumtion § 242 (Vollendung nur Verweis auf Folge 055) → Gegenvariante Etikettentausch: Betrug → Klausurtipp → Schema
→ Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Fabian, Carina (nie im Genitiv).
Stimmen (Pool niklas, helmut, ela_froh, julia): Fabian niklas (Mann, jung), Carina ela_froh (Frau, jung; nur ein freundlicher
Kassensatz, keine ernste Rolle). Lexi = Erzählerin Carla. Segmente: (text, pause) = Erzählerin Carla (auch Lexi),
(text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter;
„Bundesgerichtshof“ und „Oberlandesgericht“ ausgeschrieben. „Wegnahme“ spricht synth_el als „Weck-nahme“ (AUSSPRACHE)."""

P, PS = 0.3, 0.5

STIMMEN = {"Fabian": "niklas", "Carina": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Supermarkt, Kasse ------------------------------------------------------------------------------------------
    ("[fall]Samstagnachmittag im Supermarkt. [regal]Fabian nimmt Kopfhörer für hundertzwanzig Euro aus dem Regal. "
     "[pack]Dann öffnet er eine Waschmittelpackung und schiebt die Kopfhörer hinein. [zu]Er verschließt die Packung wieder; "
     "von außen sieht man nichts. [kasse]An der Kasse legt er nur die Packung aufs Band. [scan]Kassiererin Carina scannt sie: "
     "Waschmittel, acht Euro.", P),
    ("[c1]Acht Euro, bitte.", P, "Carina"),
    ("[f1]Hier, bitte. Schönen Tag noch.", P, "Fabian"),
    ("[raus]Fabian zahlt und verlässt mit der Packung den Laden. [frage]Diebstahl oder Betrug? [frage2]Carina hat ihm die "
     "Packung ja selbst gegeben. Hat sie damit auch über die Kopfhörer verfügt?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Abgrenzung: Fremdschädigung / Selbstschädigung ---------------------------------------------------------------------
    ("[abgr]Für dieselbe Sache schließen sich Diebstahl und Betrug aus. [fremd]Beim Diebstahl führt der Täter den Schaden "
     "selbst herbei: Er nimmt die Sache eigenmächtig weg. [selbst]Beim Betrug schädigt sich das Opfer selbst: Getäuscht gibt "
     "es die Sache heraus. [bgh1]Der Bundesgerichtshof sagt: Betrug liegt vor, wenn der Getäuschte aufgrund freier, nur durch "
     "Irrtum beeinflusster Entschließung Gewahrsam übertragen will und überträgt. [wille]Es kommt also auf den Willen von "
     "Carina an.", PS),
    # --- D Wortlaut § 242, § 263 ------------------------------------------------------------------------------------------------
    ("[p242]Paragraf zweihundertzweiundvierzig Absatz eins: Wer eine fremde bewegliche Sache einem anderen in der Absicht "
     "wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft. [p263]Paragraf "
     "zweihundertdreiundsechzig verlangt eine Täuschung, einen Irrtum und einen Vermögensschaden. [vf]Dazwischen steht die "
     "ungeschriebene Vermögensverfügung; das ganze Schema zeigt unsere Folge zum Betrug.", PS),
    # --- E Kernfrage: Verfügungsbewusstsein -----------------------------------------------------------------------------------
    ("[kern]Jetzt die Kernfrage. [vbw]Beim Sachbetrug muss das Opfer wissen, worüber es verfügt. Man nennt das "
     "Verfügungsbewusstsein. [nichts]Carina weiß nichts von den Kopfhörern. [nurw]Sie scannt das Waschmittel und will nur "
     "das Waschmittel herausgeben. [tippt]Nach dem Bundesgerichtshof konkretisiert der Kassierer seinen Verfügungswillen, "
     "indem er die Preise der vorgelegten Waren eintippt. [wahr]Über Ware, die er nicht wahrnimmt, verfügt er nicht bewusst. "
     "[hm]Das ist die herrschende Meinung: Über die Kopfhörer hat Carina nicht verfügt.", PS),
    # --- F Gegenansicht und Argumente -------------------------------------------------------------------------------------------
    ("[gegen]Die Gegenansicht lässt ein generelles Verfügungsbewusstsein genügen: Carina wolle alles herausgeben, was Fabian "
     "an der Kasse mitnimmt, hier also die Packung samt Inhalt. [olg]So sah es das Oberlandesgericht Düsseldorf "
     "neunzehnhundertzweiundneunzig für Ware, die im Einkaufswagen versteckt war. [fikt]Der Bundesgerichtshof widersprach "
     "neunzehnhundertfünfundneunzig: Ein genereller Verfügungswille über den ganzen Inhalt sei eine bloße Fiktion. "
     "[frag]Selbst wenn Carina fragt, ob das alles ist, und Fabian lügt, neigt der Bundesgerichtshof zum Diebstahl: "
     "[gelegen]Die Täuschung verschafft ihm nur die Gelegenheit zur Wegnahme. [raeub]Dazu ein Wertungsargument: Der "
     "räuberische Diebstahl knüpft nur an einen Diebstahl an. Wer die Ware danach mit Gewalt verteidigt, würde sonst je "
     "nach Versteck ganz verschieden bestraft.", PS),
    # --- G Subsumtion § 242 -------------------------------------------------------------------------------------------------------
    ("[wegn]Also zurück zum Diebstahl. Die Kopfhörer sind für Fabian fremde bewegliche Sachen. [gew]Gewahrsam daran hat "
     "der Supermarkt. [bruch]Carina ist mit dem Gewahrsamswechsel an den Kopfhörern nicht einverstanden; sie kennt sie ja "
     "nicht. Das ist ein Gewahrsamsbruch. [neu]Spätestens mit dem Verlassen des Ladens hat Fabian neuen Gewahrsam "
     "begründet; die Wegnahme ist vollendet. [enkl]Wann genau, hängt von den Umständen des Einzelfalls ab; dazu unsere Folge "
     "zur Gewahrsamsenklave. [subj]Fabian handelt vorsätzlich und will die Kopfhörer behalten, ohne zu zahlen. Er hat "
     "Zueignungsabsicht und handelt rechtswidrig und schuldhaft. [erg]Ergebnis: Diebstahl nach Paragraf zweihundertzweiundvierzig. "
     "[kein263]Betrug scheidet aus, weil es an einer Vermögensverfügung über die Kopfhörer fehlt.", PS),
    # --- H Gegenvariante: Etikettentausch ---------------------------------------------------------------------------------------
    ("[gv]Jetzt die Gegenvariante. [etik]Fabian klebt das Preisetikett des Waschmittels auf die Kopfhörer und legt sie offen "
     "aufs Band. [gv2]Carina scannt: acht Euro. [gv3]Diesmal sieht sie die Kopfhörer und gibt sie bewusst heraus, nur zum "
     "falschen Preis. [gv4]Fabian täuscht über den Preis, Carina irrt und verfügt über die Kopfhörer. [gv5]Der Supermarkt "
     "gibt Kopfhörer für hundertzwanzig Euro gegen acht Euro her: ein Vermögensschaden. [gv6]Das ist Sachbetrug nach "
     "Paragraf zweihundertdreiundsechzig.", PS),
    # --- I Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Fang mit dem Delikt an, das näher liegt, bei versteckter Ware also mit dem Diebstahl. "
     "[tipp2]Das Verfügungsbewusstsein prüfst du dort bei der Wegnahme: Gab die Kassiererin den Gewahrsam bewusst heraus, "
     "fehlt der Gewahrsamsbruch. [tipp3]Bejahst du den Diebstahl, lehnst du den Betrug danach kurz ab: keine Verfügung über "
     "die versteckte Sache.", PS),
    # --- J Prüfschema -------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Kasse. [s1]Römisch eins, Diebstahl: fremde bewegliche Sache, [s1b]Wegnahme als Bruch "
     "fremden Gewahrsams, [s1c]und dort die Frage: Kannte die Kassiererin die Sache und gab sie sie bewusst heraus? "
     "[s1d]Dann Vorsatz, Zueignungsabsicht, Rechtswidrigkeit und Schuld. [s2]Römisch zwei, Betrug: Täuschung, Irrtum, "
     "Vermögensverfügung mit Verfügungsbewusstsein, Schaden. [s3]Für dieselbe Sache ist nur eines von beiden erfüllt.", PS),
    # --- K Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer von der Sache nichts weiß, verfügt nicht über sie. [m2]Versteckte Ware an der Kasse ist deshalb in "
     "der Regel Diebstahl, [m3]offen vorgelegte Ware zum falschen Preis Betrug.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
