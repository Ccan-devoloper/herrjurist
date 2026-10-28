"""Folge 248 · Gesellschafterhaftung GbR § 721 BGB: Haften die Mitglieder privat? (Mi · Examenswissen ·
Gesellschaftsrecht · Schema; §§ 721–721b, 722, 728b BGB). Beispielfall nach dem Plan-Hook („Die GbR zahlt die Rechnung
nicht – der Gläubiger greift auf dein Privatkonto zu“): Philipp und Mathilde betreiben ein Architekturbüro als
(nicht eingetragene) rechtsfähige GbR. Im Februar kauft das Büro beim Tischler Herrn Altmann Arbeitstische und Regale für
18.000 €, zahlbar Ende Juni. Im März tritt Alma ein (interne Abrede: keine Haftung für Altschulden), Ende April scheidet
Mathilde aus (Herr Altmann erfährt es per Rundschreiben). Reihenfolge bewusst: erst Eintritt, dann Ausscheiden – sonst
bliebe ein Gesellschafter allein und die GbR erlösche (§ 712a Abs. 1 BGB). Das Büro hat gegen Herrn Altmann ein fälliges
Honorar von 3.000 € (Pläne für seine Werkstatt) → § 721b Abs. 2 BGB (Aufrechnungsrecht der Gesellschaft).
Belege je Cue in ../RECHTSSTAND.md. Grundlagen der rechtsfähigen GbR nur verwiesen (Folge 173), Gesamtschuld (Folge 120).
Stimmen (Pool niklas, helmut, ela_froh, julia): Philipp (niklas, Mann, jung), Herr Altmann (helmut, Mann, älter),
Alma (ela_froh, Frau, jung – nur ein heiterer Satz beim Eintritt); julia nicht besetzt; Mathilde spricht nicht.
Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, HGB);
keine Genitivformen der Namen („von Philipp“ statt „Philipps“)."""

P, PS = 0.3, 0.5

STIMMEN = {"Philipp": "niklas", "Altmann": "helmut", "Alma": "ela_froh"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: das Architekturbüro – Kauf, Eintritt Alma, Ausscheiden Mathilde ------------------------------------------
    ("[fall]Philipp und Mathilde betreiben zusammen ein Architekturbüro, als Gesellschaft bürgerlichen Rechts. [moebel]Im "
     "Februar kauft das Büro beim Tischler Herrn Altmann neue Arbeitstische und Regale für achtzehntausend Euro, zahlbar "
     "Ende Juni. [alma]Im März tritt Alma als dritte Gesellschafterin ein.", P),
    ("[a1]Ab heute bin ich dabei! Für alte Rechnungen hafte ich aber nicht, das haben wir so vereinbart.", P, "Alma"),
    ("[mathilde]Ende April scheidet Mathilde aus und geht in den Ruhestand; [rund]Herr Altmann erfährt davon durch ein "
     "Rundschreiben.", P),
    # --- A2 Juli: Herr Altmann im Büro --------------------------------------------------------------------------------------
    ("[juli]Im Juli ist die Rechnung noch offen, und das Konto des Büros ist leer.", P),
    ("[h1]Die achtzehntausend Euro sind seit Wochen fällig. Dann zahlen Sie eben von Ihrem Privatkonto!", P, "Altmann"),
    ("[p1]Die Möbel hat doch das Büro gekauft, nicht ich! Und Sie schulden uns noch dreitausend Euro für die Pläne Ihrer "
     "Werkstatt.", P, "Philipp"),
    ("[frage]Muss Philipp mit seinem Privatvermögen zahlen? [frage2]Und haften auch Alma und Mathilde?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Schuldnerin ist die GbR (§ 705 Abs. 2, § 433 Abs. 2; Verweis Folge 173) ---------------------------------------
    ("[gbr]Zuerst: Wer schuldet überhaupt? [rf]Das Büro soll am Rechtsverkehr teilnehmen, ist also eine rechtsfähige "
     "Gesellschaft nach Paragraf siebenhundertfünf Absatz zwei. [v173]Wie sie entsteht, zeigt unser Video zur Gesellschaft "
     "bürgerlichen Rechts nach der Reform. [schuld]Käuferin ist die Gesellschaft selbst; sie schuldet die achtzehntausend "
     "Euro nach Paragraf vierhundertdreiunddreißig Absatz zwei.", P),
    # --- D § 721 BGB (Wortlautkarte), Rechtsstand MoPeG ---------------------------------------------------------------
    ("[p721]Und die Gesellschafter? [w721]Paragraf siebenhunderteinundzwanzig: Die Gesellschafter haften für die "
     "Verbindlichkeiten der Gesellschaft den Gläubigern als Gesamtschuldner persönlich. [satz2]Eine entgegenstehende "
     "Vereinbarung ist Dritten gegenüber unwirksam. [frueher]Früher galt das nur entsprechend dem Recht der offenen "
     "Handelsgesellschaft; seit dem ersten Januar zweitausendvierundzwanzig steht es ausdrücklich im Gesetz.", PS),
    # --- E Merkmale der Haftung (BT-Drs. 19/27635, S. 165 f.; BGH II ZR 331/00) -----------------------------------------
    ("[merk]Was heißt das? [pers]Persönlich: Philipp haftet mit seinem Privatvermögen. [unbe]Unbeschränkt: ohne "
     "Höchstbetrag. [prim]Unmittelbar und primär: Herr Altmann darf sich direkt an Philipp wenden und muss nicht zuerst "
     "die Gesellschaft verklagen. [gesamt]Als Gesamtschuldner schuldet jeder Gesellschafter die ganze Summe; Herr Altmann "
     "bekommt sie aber nur einmal, [v120]mehr dazu im Video zur Gesamtschuld. [akz]Und akzessorisch: Die Haftung richtet "
     "sich nach Bestand und Inhalt der Schuld der Gesellschaft.", PS),
    # --- F § 721a BGB (Wortlautkarte): Alma ---------------------------------------------------------------------------
    ("[eintr]Nun zu Alma. [w721a]Nach Paragraf siebenhunderteinundzwanzig a haftet, wer in eine bestehende Gesellschaft "
     "eintritt, gleich den anderen Gesellschaftern für die vor seinem Eintritt begründeten Verbindlichkeiten. [alt]Der Kauf "
     "war im Februar, Alma kam im März: eine Altschuld. [abr]Ihre interne Abrede ist nach Satz zwei Dritten gegenüber "
     "unwirksam. [afall]Alma haftet also mit.", PS),
    # --- G § 721b BGB (Wortlautkarte): Einwendungen, Aufrechnungsrecht der Gesellschaft ----------------------------------
    ("[einw]Kann Philipp sich wehren? [w721b]Nach Paragraf siebenhunderteinundzwanzig b Absatz eins kann er Einwendungen "
     "und Einreden der Gesellschaft geltend machen, etwa Erfüllung oder Verjährung. [abs2]Und nach Absatz zwei darf er die "
     "Befriedigung des Gläubigers verweigern, solange der Gesellschaft das Recht zur Anfechtung oder Aufrechnung zusteht. "
     "[aufr]Hier könnte die Gesellschaft mit ihrem fälligen Honorar von dreitausend Euro aufrechnen. [verw]In dieser Höhe "
     "darf Philipp die Zahlung verweigern; [rest]offen bleiben fünfzehntausend Euro.", PS),
    # --- H § 728b BGB (Wortlautkarte): Mathilde -----------------------------------------------------------------------
    ("[aus]Und Mathilde? Sie ist ausgeschieden. [w728b]Nach Paragraf siebenhundertachtundzwanzig b haftet sie für die bis "
     "dahin begründeten Verbindlichkeiten, wenn sie vor Ablauf von fünf Jahren nach ihrem Ausscheiden fällig sind [fest]und "
     "der Anspruch gegen sie festgestellt ist, etwa durch Urteil, oder eine Vollstreckungshandlung beantragt wird. "
     "[frist]Bei einer nicht eingetragenen Gesellschaft beginnt die Frist, sobald der Gläubiger vom Ausscheiden erfährt, "
     "hier mit dem Rundschreiben. [mfall]Die Schuld aus dem Kauf ist vor dem Ausscheiden von Mathilde begründet und Ende "
     "Juni fällig geworden. [mfall2]Klagt Herr Altmann rechtzeitig, haftet also auch Mathilde.", PS),
    # --- I § 722 Abs. 2 BGB (Wortlautkarte): Vollstreckung --------------------------------------------------------------
    ("[vollstr]Und wie kommt Herr Altmann an das Geld? [w722]Paragraf siebenhundertzweiundzwanzig Absatz zwei: Aus einem "
     "gegen die Gesellschaft gerichteten Vollstreckungstitel findet die Zwangsvollstreckung gegen die Gesellschafter nicht "
     "statt. [titel]Für das Privatkonto von Philipp braucht er also einen Titel gegen Philipp selbst. [beide]Deshalb "
     "verklagt man am besten die Gesellschaft und die Gesellschafter zusammen.", PS),
    # --- J Innenausgleich (§ 716 Abs. 1; § 426; BGH II ZR 310/12 Rn. 34 f.) --------------------------------------------
    ("[innen]Und wenn Philipp zahlt? [p716]Dann kann er von der Gesellschaft Ersatz verlangen, nach Paragraf "
     "siebenhundertsechzehn Absatz eins. [p426]Von den Mitgesellschaftern kann er Ausgleich nur verlangen, wenn von "
     "der Gesellschaft nichts zu bekommen ist. [abr2]Und erst dort, im Innenverhältnis, zählt die Abrede mit Alma.", PS),
    # --- K Ergebnis (zurück im Büro) -------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Herr Altmann kann von Philipp persönlich fünfzehntausend Euro verlangen; [erg2]die übrigen dreitausend "
     "darf Philipp verweigern, solange die Gesellschaft aufrechnen kann. [erg3]Ebenso haften Alma und, bei rechtzeitiger "
     "Klage, auch Mathilde.", PS),
    # --- L Klausurtipp (Lexi; BGH II ZR 197/10 Rn. 14) -------------------------------------------------------------------
    ("[tipp]Klausurtipp: Zeichne für jeden Gesellschafter eine Zeitleiste. [tipp2]Entscheidend ist, wann die "
     "Verbindlichkeit begründet wurde, also wann ihre Rechtsgrundlage gelegt war, auch wenn sie erst später fällig wird. "
     "[tipp3]Liegt das vor dem Eintritt, greift Paragraf siebenhunderteinundzwanzig a; liegt es vor dem Ausscheiden, "
     "Paragraf siebenhundertachtundzwanzig b.", PS),
    # --- M Prüfungsschema ------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema für die Haftung eines Gesellschafters. [s1]Eins: eine Verbindlichkeit der rechtsfähigen "
     "Gesellschaft, hier aus Paragraf vierhundertdreiunddreißig Absatz zwei. [s2]Zwei: die Gesellschafterstellung, beim "
     "Eintritt Paragraf siebenhunderteinundzwanzig a, nach dem Ausscheiden die Grenzen von Paragraf "
     "siebenhundertachtundzwanzig b. [s3]Drei: die Rechtsfolge nach Paragraf siebenhunderteinundzwanzig, also persönliche "
     "und unbeschränkte Haftung als Gesamtschuldner. [s4]Vier: Einwendungen und Einreden nach Paragraf "
     "siebenhunderteinundzwanzig b. [s5]Und für die Vollstreckung: ein Titel gegen den Gesellschafter selbst.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Für die Schulden der Gesellschaft haftet jeder Gesellschafter persönlich und unbeschränkt. [merk2]Wer "
     "eintritt, haftet auch für Altschulden; wer ausscheidet, nur noch in den Grenzen der Fünfjahresfrist.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\bHGB\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    assert not re.search(r"Philipps|Almas|Mathildes|Altmanns", text), "Genitiv eines Namens"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
