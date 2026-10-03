"""Folge 100 · Rücktritt vom Versuch § 24 StGB: Das Schema Schritt für Schritt (Mo · Der Fall · Strafrecht/StGB AT,
Format Schema). Fiktiver Fall nach dem Plan-Hook („Ein Einbrecher setzt schon den Hebel am Fenster an, bekommt
Gewissensbisse und geht nach Hause“): Heiner will in die Erdgeschosswohnung von Annegret einbrechen und stehlen, setzt
einen Hebel am Küchenfenster an, der Rahmen bekommt eine Delle; aus Gewissensbissen bricht er ab und geht nach Hause.
Kern: Wortlautkarte § 24 Abs. 1 S. 1 und 2 StGB; Versuch (§§ 242, 244 Abs. 1 Nr. 3, Abs. 4, 22, 23 Abs. 1) nur in zwei
Sätzen mit Verweis auf Folge 097 (Versuchsbeginn: BGH 5 StR 15/20 = BGHSt 65, 15, Rn. 7 f.); Rücktrittsschema IV.:
1. kein fehlgeschlagener Versuch (BGH 4 StR 408/21 Rn. 5), 2. unbeendet/beendet nach dem Rücktrittshorizont (ebd. Rn. 5,
Korrektur Rn. 6; BGHSt 39, 221), 3. Rücktrittshandlung (§ 24 Abs. 1 S. 1 Alt. 1/2, S. 2), 4. Freiwilligkeit
(BGH 2 StR 284/19 Rn. 8 f.; 5 StR 75/20 Rn. 8); § 24 Abs. 2 ein Satz; Klausurtipp: persönlicher Strafaufhebungsgrund
(BGH 4 StR 223/21 Rn. 21), vollendete Delikte bleiben strafbar (BGHSt 42, 43 = 3 StR 445/95 Rn. 7): Sachbeschädigung
§ 303 Abs. 1. Belege je Aussage: ../RECHTSSTAND.md.
Figuren: Heiner (marc, Mann mittel), Annegret (sabrina, Frau mittel); Erzählerin/Lexi Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter, keine Abkürzungen (StGB, BGH) im Sprechtext.
Namen nie im Genitiv mit -s."""

P, PS = 0.3, 0.5

STIMMEN = {"Heiner": "marc", "Annegret": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Seitenstraße -------------------------------------------------------------------------------------
    ("[fall]Dienstagnachmittag in einer ruhigen Seitenstraße. [heiner]Heiner, Mitte vierzig, braucht dringend Geld. "
     "[wohnung]Er weiß: In der Erdgeschosswohnung von [annegret]Annegret ist jetzt niemand, sie arbeitet in der "
     "Spätschicht. [gehweg]Das Küchenfenster liegt direkt am Gehweg. [hebel]Heiner will einbrechen und stehlen. Er setzt "
     "einen Hebel am Fensterrahmen an und drückt. [delle]Das Holz gibt schon nach, im Rahmen bleibt eine tiefe Delle.", 0.3),
    ("[h1]Was mache ich hier eigentlich? Das ist nicht richtig.", 0.3, "Heiner"),
    ("[reue]Heiner hat Gewissensbisse. [niemand]Niemand hat ihn bemerkt, das Fenster hätte er gleich offen gehabt. "
     "[heim]Trotzdem steckt er den Hebel ein und geht nach Hause. [abends]Am Abend kommt Annegret heim.", 0.3),
    ("[a1]Was ist denn mit meinem Fensterrahmen passiert?", 0.4, "Annegret"),
    ("[frage]Ist Heiner strafbar? [frage2]Wir prüfen den Rücktritt vom Versuch Schritt für Schritt.", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 24 Abs. 1 ---------------------------------------------------------------------------------------
    ("[p24]Paragraf vierundzwanzig, Absatz eins: [p24w]Wegen Versuchs wird nicht bestraft, wer freiwillig die weitere "
     "Ausführung der Tat aufgibt oder deren Vollendung verhindert. [p24s2]Und Satz zwei: Wird die Tat ohne Zutun des "
     "Zurücktretenden nicht vollendet, so wird er straflos, wenn er sich freiwillig und ernsthaft bemüht, die Vollendung "
     "zu verhindern.", PS),
    # --- D Versuch (I. bis III.) in zwei Sätzen -----------------------------------------------------------------------
    ("[vers]Den Versuch prüfst du wie in Folge siebenundneunzig: [vers1]Heiner will in eine bewohnte Wohnung einbrechen "
     "und stehlen, und nach dem Bundesgerichtshof setzt unmittelbar an, wer das Einbruchswerkzeug schon angesetzt hat. "
     "[vers2]Rechtswidrig und schuldhaft handelt er auch, also liegt ein versuchter Wohnungseinbruchdiebstahl in eine "
     "dauerhaft genutzte Privatwohnung vor, Paragraf zweihundertvierundvierzig, Absatz vier.", PS),
    # --- E IV. 1. Kein fehlgeschlagener Versuch ------------------------------------------------------------------------
    ("[rt]Römisch vier: der Rücktritt. [rt1]Erstens darf der Versuch nicht fehlgeschlagen sein. [rt1b]Fehlgeschlagen ist "
     "er, wenn der Täter die Tat mit den eingesetzten oder anderen naheliegenden Mitteln nicht mehr vollenden kann und "
     "das erkennt, oder wenn er die Vollendung nicht mehr für möglich hält. [rt1c]Anders als in Folge siebenundneunzig, "
     "wo die einzige Patrone verschossen war, ist das hier nicht so: Heiner hätte das Fenster gleich aufgehebelt.", PS),
    # --- F IV. 2. Unbeendet oder beendet -----------------------------------------------------------------------------
    ("[rt2]Zweitens: Ist der Versuch unbeendet oder beendet? [hor]Maßgeblich ist die Vorstellung des Täters nach der "
     "letzten Ausführungshandlung, der Rücktrittshorizont. [unb]Unbeendet ist der Versuch, wenn der Täter noch nicht alles "
     "getan hat, was nach seiner Vorstellung für die Vollendung nötig ist. [bee]Beendet ist er, wenn er den Erfolg schon "
     "für möglich hält oder sich darüber keine Gedanken macht. [korr]In engen zeitlichen Grenzen kann der Täter diese Vorstellung noch korrigieren. "
     "[unb2]Heiner weiß: Das Fenster ist noch zu, gestohlen hat er nichts. Der Versuch ist unbeendet.", PS),
    # --- G IV. 3. Rücktrittshandlung --------------------------------------------------------------------------------
    ("[rh]Drittens die Rücktrittshandlung. [rh1]Beim unbeendeten Versuch genügt es, die weitere Ausführung aufzugeben, "
     "Satz eins, erste Alternative. [rh2]Beim beendeten Versuch muss der Täter die Vollendung verhindern, die zweite "
     "Alternative. [rh3]Wird die Tat ohne sein Zutun nicht vollendet, reicht nach Satz zwei sein freiwilliges und "
     "ernsthaftes Bemühen. [rh4]Heiner steckt den Hebel ein und geht nach Hause. Er gibt die Tat auf.", PS),
    # --- H IV. 4. Freiwilligkeit ---------------------------------------------------------------------------------------
    ("[fw]Viertens die Freiwilligkeit. [fw1]Freiwillig handelt nach dem Bundesgerichtshof, wer Herr seiner Entschlüsse "
     "bleibt und die Tat noch für ausführbar hält. [fw2]In der Klausur unterscheidest du autonome Motive, die aus dem "
     "Täter selbst kommen, [fw3]von heteronomen, etwa Hindernissen von außen, die der Vollendung zwingend entgegenstehen. "
     "[fw4]Ein sittlich billigenswertes Motiv verlangt der Bundesgerichtshof nicht. [fw5]Heiner hat Gewissensbisse, und "
     "niemand stört ihn. Er bleibt Herr seiner Entschlüsse und tritt freiwillig zurück.", PS),
    # --- I Mehrere Beteiligte, Ergebnis --------------------------------------------------------------------------------
    ("[zwei]Wären mehrere beteiligt, müsste der Zurücktretende nach Absatz zwei die Vollendung verhindern. [erg]Ergebnis: "
     "Wegen des versuchten Wohnungseinbruchdiebstahls bleibt Heiner straflos. [erg2]Strafbar bleibt er aber wegen der Delle im "
     "Fensterrahmen.", PS),
    # --- J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Der Rücktritt ist ein persönlicher Strafaufhebungsgrund, und er erfasst nur den Versuch. "
     "[tipp2]Schon vollendete Delikte bleiben strafbar. [tipp3]Die Delle ist eine vollendete Sachbeschädigung nach "
     "Paragraf dreihundertdrei. Prüfe sie gesondert.", PS),
    # --- K Klausurschema ----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s0]Vorprüfung, Tatbestand, Rechtswidrigkeit und Schuld wie beim Versuch. [s4]Dann "
     "Römisch vier: Rücktritt nach Paragraf vierundzwanzig, Absatz eins. [s41]Erstens kein fehlgeschlagener Versuch. "
     "[s42]Zweitens unbeendet oder beendet, nach dem Rücktrittshorizont. [s43]Drittens die Rücktrittshandlung: "
     "[s43a]Aufgeben beim unbeendeten, [s43b]Verhindern oder ernsthaftes Bemühen beim beendeten Versuch. "
     "[s44]Viertens die Freiwilligkeit.", PS),
    # --- L Merksatz (Lexi) --------------------------------------------------------------------------------------------
    ("[merke]Merke: Zurücktreten kann nur, wessen Versuch nicht fehlgeschlagen ist. [m2]Beim unbeendeten Versuch genügt "
     "freiwilliges Aufgeben, beim beendeten muss der Täter die Vollendung verhindern. [m3]Und was schon vollendet ist, "
     "bleibt strafbar.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
