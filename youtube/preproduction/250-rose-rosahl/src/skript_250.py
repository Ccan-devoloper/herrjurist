"""Folge 250 · Rose-Rosahl-Fall: Error in persona des Täters – und der Anstifter? (Mo · Der Fall · StGB AT · Klassiker-Fall).
Übungsfall nach dem Plan-Hook (Personen fiktiv): Die Bauunternehmerin Edeltraud bittet ihren Bekannten Vinzenz, ihren Konkurrenten
zu töten, und gibt ihm ein Foto; Vinzenz wartet abends am dunklen Kanalweg und tötet einen Spaziergänger, den er für den
Konkurrenten hält.
Prüfung: A. Vinzenz, § 212: objektiver Tatbestand, Vorsatz, § 16 Abs. 1 Satz 1 (Wortlautkarte), error in persona bei
Gleichwertigkeit unbeachtlich (BGHSt 37, 214, 216 mit BGHSt 11, 268, 270; Verweis Folge 068). B. Edeltraud, §§ 212, 26 (§ 26 als
Wortlautkarte): Haupttat, Bestimmen, doppelter Vorsatz; Problem error in persona des Täters für den Anstifter:
1. Unbeachtlichkeitslehre (PrObTr, GA 7 (1859), 322 – Rose-Rosahl; historischer Fall, Original nicht online verfügbar),
2. Aberratio-Lösung (Teile der Lehre: versuchte Anstiftung § 30 Abs. 1, ggf. § 222),
3. BGH, Urt. v. 25.10.1990 – 4 StR 371/90, BGHSt 37, 214 (Hoferben): Abweichung, unbeachtlich in den Grenzen des nach
allgemeiner Lebenserfahrung Vorhersehbaren (S. 218 f.); aberratio-Regeln nicht anwendbar (S. 219); vermittelnd
Individualisierung. Ergebnis nach BGH, Blutbad-Argument (ein Satz) und Antwort des BGH; Klausurtipp, Schema, Merksatz (Lexi).
DARSTELLUNG: keine Waffe, kein Schuss, keine Leiche im Bild; nur Dunkelheit, Weg, Silhouetten-Andeutung, Pillen; das Opfer wird
nicht gezeigt; reale historische Personen (Rose, Rosahl) nicht als Figuren.
Stimmen (Pool stephan, hilde, christian, lucy): Edeltraud hilde, Vinzenz stephan. Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Edeltraud": "hilde", "Vinzenz": "stephan"}

SEGMENTE = [
    # --- A Fall: der Auftrag, der Abend am Kanal ---------------------------------------------------------------------------
    ("[fall]Edeltraud führt eine Baufirma. [konk]Ihr Konkurrent nimmt ihr einen Auftrag nach dem anderen weg. [auftrag]Sie bittet "
     "ihren Bekannten Vinzenz, ihn zu töten. [foto]Sie gibt ihm ein Foto.", 0.2),
    ("[ed1]Er geht jeden Abend allein am Kanal spazieren. Dort erwischst du ihn.", P, "Edeltraud"),
    ("[vi1]Gut. Morgen Abend warte ich dort auf ihn.", P, "Vinzenz"),
    ("[nacht]Am nächsten Abend steht Vinzenz im Dunkeln am Kanalweg. [schritte]Schritte. Ein Mann kommt näher, Statur und "
     "Mantel passen zum Foto.", 0.2),
    ("[vi2]Da ist er.", P, "Vinzenz"),
    ("[tat]Vinzenz tötet den Mann. [irrtum]Doch es ist nicht der Konkurrent, sondern ein Spaziergänger, der ihm nur ähnlich "
     "sieht.", 0.4),
    ("[frage]Vinzenz hat den Falschen getötet. [frage2]Ist Edeltraud trotzdem Anstifterin zum Totschlag, obwohl sie diesen Mann "
     "nie treffen wollte?", PS),
    # --- Sachverhalt ---------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- B Täter: Vinzenz, § 212, § 16 (Wortlautkarte), error in persona -----------------------------------------------------
    ("[aufbau]Zuerst der Täter. [t_obj]Vinzenz hat einen Menschen getötet, objektiv ein Totschlag nach Paragraf "
     "zweihundertzwölf. [p16]Aber handelte er vorsätzlich? Nach Paragraf sechzehn fehlt der Vorsatz, wenn der Täter einen "
     "Umstand nicht kennt, der zum gesetzlichen Tatbestand gehört. [umstand]Zum Tatbestand "
     "gehört nur: einen Menschen. Wer dieser Mensch ist, gehört nicht dazu. [eip]Vinzenz wollte genau den Mann töten, den er vor "
     "sich sah, und irrte nur über dessen Identität: ein error in persona. [gleich]Bei gleichwertigen Objekten ist er "
     "unbeachtlich. [t_erg]Vinzenz ist wegen Totschlags strafbar. Ob Mordmerkmale vorliegen, lassen wir "
     "hier offen. [f68]Mehr dazu in Folge achtundsechzig.", P),
    # --- C Anstifterin: Edeltraud, § 26 (Wortlautkarte), das Problem ----------------------------------------------------------
    ("[p26]Jetzt Edeltraud. Paragraf sechsundzwanzig: Als Anstifter wird gleich einem Täter bestraft, wer vorsätzlich einen "
     "anderen zu dessen vorsätzlich begangener rechtswidriger Tat bestimmt hat. [haupt]Die Haupttat liegt vor: der "
     "vorsätzliche, rechtswidrige Totschlag von Vinzenz. [bestimmt]Und Edeltraud hat ihn dazu bestimmt. Sie hat seinen "
     "Tatentschluss hervorgerufen. [doppel]Dazu braucht sie doppelten Vorsatz: auf die Haupttat und auf das Bestimmen. "
     "[problem]Ihr Vorsatz galt aber dem Konkurrenten. Ist der Irrtum von Vinzenz auch für sie unbeachtlich, "
     "[problem2]oder für sie ein Fehlgehen der Tat, eine aberratio ictus?", P),
    # --- D1 Unbeachtlichkeitslehre: Rose-Rosahl (PrObTr 1859) -----------------------------------------------------------------
    ("[rose]Die Frage ist alt. [rose2]Im Rose-Rosahl-Fall, entschieden achtzehnhundertneunundfünfzig, stiftet der Holzhändler "
     "Rosahl seinen Arbeiter Rose an, einen Mann zu töten. Rose tötet in der Dämmerung einen Schüler. [probtr]Das "
     "Preußische Obertribunal entschied: Der Irrtum ist auch für den Anstifter unbeachtlich. [unbeacht]Diese "
     "Unbeachtlichkeitslehre sagt: Der Anstifter hat zur Tötung eines Menschen bestimmt. Das Risiko einer Verwechslung trägt er "
     "wie der Täter.", P),
    # --- D2 Aberratio-Lösung (Lehre) ------------------------------------------------------------------------------------------
    ("[aberr]Weite Teile der Lehre sehen das anders. Für den Anstifter sei der Täter wie ein Tatmittel, das sein Ziel verfehlt: "
     "eine aberratio ictus. [ab_folge]Meist folgt daraus: versuchte Anstiftung zum Totschlag am Konkurrenten nach Paragraf "
     "dreißig Absatz eins, und gegebenenfalls fahrlässige Tötung des Spaziergängers.", P),
    # --- D3 BGHSt 37, 214 (Hoferben-Fall) -------------------------------------------------------------------------------------
    ("[bgh]Mehr als hundertdreißig Jahre später entschied der Bundesgerichtshof den Hoferben-Fall. [hof]Ein Vater will seinen "
     "Sohn, den Hoferben, töten lassen und zeigt dem Täter ein Foto. Im dunklen Pferdestall tötet der Täter einen Nachbarn, der "
     "dem Sohn ähnelt. [lg]Er bejahte eine vollendete Anstiftung zum Mord. [abw]Die Verwechslung sei für den Anstifter zwar eine Abweichung vom geplanten Geschehen. [lebens]Sie "
     "sei aber unbeachtlich, weil sie sich in den Grenzen des nach allgemeiner Lebenserfahrung Vorhersehbaren hielt. [hand]Der "
     "Vater hatte das Geschehen bewusst aus der Hand gegeben. [aberr_nein]Die Regeln der aberratio ictus passen nach dem Senat "
     "nicht. Sie sind für Fälle entwickelt, in denen der Täter das Angriffsobjekt vor sich sieht, aber ein anderes trifft. [indiv]Ähnlich fragt ein "
     "Teil der Lehre, ob der Anstifter es dem Täter überlassen hat, das Opfer zu erkennen.", P),
    # --- E Ergebnis im Fall nach dem BGH; Blutbad-Argument ------------------------------------------------------------------
    ("[erg]Zurück zu Edeltraud. [s_hand]Auch sie hat die Tat aus der Hand gegeben: Vinzenz sollte den Mann allein, im Dunkeln "
     "und nach einem Foto erkennen. [s_vorh]Am Kanal gehen abends auch andere spazieren. Eine Verwechslung lag nicht außerhalb "
     "jeder Lebenserfahrung. [s_unerw]Dass sie ihr unerwünscht war, ändert nichts. [s_erg]Nach dem Bundesgerichtshof ist "
     "Edeltraud strafbar wegen Anstiftung zum Totschlag. "
     "[s_lehre]Nach der aberratio-Lösung bliebe es bei versuchter Anstiftung. [blut]Die Lehre hält das "
     "Blutbad-Argument dagegen: Tötet der Täter weiter, bis er den Richtigen trifft, müsste der Anstifter für jedes Opfer "
     "haften. [blut2]Der Bundesgerichtshof begrenzt die Haftung über die Vorhersehbarkeit: Was außerhalb der Lebenserfahrung "
     "liegt, wird dem Anstifter nicht zugerechnet.", PS),
    # --- F Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Täter vor dem Teilnehmer, denn die Anstiftung braucht eine vorsätzliche, rechtswidrige "
     "Haupttat. [k1]Prüfe den Irrtum für jeden Beteiligten getrennt. Was beim Täter unbeachtlich ist, wird beim Anstifter erst "
     "zum Problem. [k2]Den Streit erörterst du im Vorsatz des Anstifters und entscheidest ihn, denn "
     "die Ansichten führen hier zu verschiedenen Ergebnissen.", P),
    # --- G Klausurschema (Lexi), progressiv ----------------------------------------------------------------------------------
    ("[sch]So baust du die Lösung auf: [s1]Zuerst Vinzenz, Totschlag nach Paragraf zweihundertzwölf. Objektiver Tatbestand "
     "gegeben. Vorsatz gegeben, der error in persona ist unbeachtlich. Rechtswidrig und schuldhaft. [s2]Dann Edeltraud, "
     "Anstiftung zum Totschlag nach den Paragrafen zweihundertzwölf und sechsundzwanzig. Objektiv: vorsätzliche, rechtswidrige "
     "Haupttat und Bestimmen. [s3]Subjektiv: Vorsatz bezüglich der Haupttat, hier der Streit. Nach dem Bundesgerichtshof "
     "gegeben, weil die Verwechslung vorhersehbar war. Dazu Vorsatz bezüglich des Bestimmens. [s4]Danach Rechtswidrigkeit und "
     "Schuld.", PS),
    # --- H Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der error in persona ist für den Täter unbeachtlich. [m2]Für den Anstifter ist er eine Abweichung vom "
     "Tatplan. Nach dem Bundesgerichtshof bleibt sie unbeachtlich, solange sie nach allgemeiner Lebenserfahrung vorhersehbar "
     "war. [m3]Wer die Tat aus der Hand gibt, trägt in der Regel das Risiko der Verwechslung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
