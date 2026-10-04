"""Folge 196 · Flugreise-Fall: Der Minderjährige, der ohne Ticket mitflog (§ 812 BGB) (Mo · Der Fall · Bereicherungsrecht,
Klassiker-Fall). Leitentscheidung: BGH, Urt. v. 7.1.1971 – VII ZR 9/70, BGHZ 55, 128 (= NJW 1971, 609). Volltext amtlich
nicht frei abrufbar (gelesen in einer nicht amtlichen Wiedergabe, juraLIB): keine wörtlichen Zitate, keine Randnummern daraus.
Kerngehalt amtlich gesichert über BGH GSSt 2/20 Rn. 23, 5 ARs 20/19 Rn. 13 (§ 819 BGB beim Minderjährigen, § 828 Abs. 3 BGB
analog, BGHZ 55, 128, 136 f.), VIa ZR 8/21 Rn. 88, 95 (BGHZ 55, 128, 132–135), IX ZR 160/14 Rn. 17, 21 (Luxusausgaben,
BGHZ 55, 128, 132, 134), III ZR 231/12 Rn. 27 und VIII ZR 38/14 Rn. 19 (echte Vermögensvermehrung, BGHZ 55, 128, 131),
III ZA 19/14 Rn. 6 (Geschäftsführung ohne Auftrag, NJW 1971, 609, 612). Leistungsbegriff: VIII ZR 39/17 Rn. 17.
Normen: § 812 Abs. 1 Satz 1, § 818 Abs. 2, 3, 4, § 819 Abs. 1, § 828 Abs. 3 BGB (Wortlautkarten), §§ 107, 108 BGB (Verweis
Folge 021), § 265a StGB, §§ 677, 683, 670 BGB (ein Satz). Belege: ../RECHTSSTAND.md. Überblick § 812 nur verwiesen (Folge 073).
Historischer Sachverhalt (1968) mit erfundenen Namen; Fluggesellschaft ohne Namen und Logo, keine Flughäfen genannt (nur das
Reiseziel New York); Einreiseverweigerung nur als Text. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht
vergeben (Liste des Auftrags, Volltextsuche 04.10.2026): Till, Ruprecht – nie im Genitiv. Stimmen: Till niklas (17 Jahre),
Ruprecht helmut (Stationsleiter, älter). Die Mutter spricht nicht. Lexi = Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Till": "niklas", "Ruprecht": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: an Bord -------------------------------------------------------------------------------------------------
    ("[fall]Neunzehnhundertachtundsechzig. [till]Till ist siebzehn und fliegt mit gültigem Ticket bis zu einer "
     "Zwischenlandung. [transit]Dort steigt er mit den Transitpassagieren einfach wieder ein [ny]und fliegt ohne Ticket "
     "weiter nach New York.", P),
    ("[t1]Einmal New York sehen! Ein Ticket dafür hätte ich mir nie leisten können.", P, "Till"),
    # --- A2 Fall: Ankunft in New York -------------------------------------------------------------------------------------
    ("[visum]Doch in New York verweigern ihm die Behörden die Einreise: Er hat kein Visum. [rup]Stationsleiter Ruprecht "
     "von der Fluggesellschaft kümmert sich um ihn.", P),
    ("[r1]Ohne Visum geht es nicht weiter. Wir fliegen Sie noch heute zurück.", P, "Ruprecht"),
    # --- A3 Fall: die Rechnung --------------------------------------------------------------------------------------------
    ("[forder]Zurück in Deutschland verlangt die Fluggesellschaft den Preis für den Hinflug: tausendeinhundertachtundachtzig "
     "Mark. [mutter]Seine Mutter genehmigt nichts.", P),
    ("[t2]Ich habe doch nichts gespart! Ohne den Gratisflug wäre ich nie geflogen.", P, "Till"),
    ("[frage]Muss Till den Flug bezahlen? [klass]Das ist der Flugreise-Fall des Bundesgerichtshofs, "
     "[klass2]entschieden am siebten Januar neunzehnhunderteinundsiebzig.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Kein Vertrag, kein Schaden --------------------------------------------------------------------------------------
    ("[vertrag]Zuerst: Gibt es einen Vertrag? [minder]Till ist minderjährig, und ein Beförderungsvertrag bringt ihm nicht "
     "lediglich einen rechtlichen Vorteil. [genehm]Ohne Einwilligung hängt er von der Genehmigung der Mutter ab, und die "
     "verweigert sie; mehr dazu im Video zur Geschäftsfähigkeit. [sozial]Einen Vertrag schon durch bloßes Einsteigen lehnte "
     "der BGH ab: Im Flugverkehr wird jeder Fluggast namentlich erfasst. [delikt]Auch Schadensersatz scheidet aus: Die "
     "Maschine war nicht ausgebucht; einen Schaden konnte die Fluggesellschaft nicht darlegen. [bleibt]Bleibt das Bereicherungsrecht.", PS),
    # --- D § 812 Abs. 1 Satz 1 BGB -----------------------------------------------------------------------------------------
    ("[norm]Anspruchsgrundlage ist Paragraf achthundertzwölf Absatz eins Satz eins BGB: [w1]Wer durch die Leistung eines "
     "anderen oder in sonstiger Weise auf dessen Kosten etwas ohne rechtlichen Grund erlangt, ist ihm zur Herausgabe "
     "verpflichtet. [leist]Eine Leistung ist die bewusste und zweckgerichtete Vermehrung fremden Vermögens. [nleist]Die "
     "Fluggesellschaft wollte Till aber gar nicht nach New York bringen. [sonst]Er hat sich die Beförderung in sonstiger "
     "Weise auf ihre Kosten verschafft: die Eingriffskondiktion. [offen]Der BGH selbst hat sich auf die Art der Kondiktion "
     "nicht festgelegt. [ogrund]Einen rechtlichen Grund hatte Till jedenfalls nicht.", PS),
    # --- E Was ist erlangt? (Meinungsstand) --------------------------------------------------------------------------------
    ("[erl]Was hat Till erlangt? [ma]Eine Ansicht sieht das Erlangte in der Beförderung selbst. [mb]Die andere stellt nur "
     "auf ersparte Aufwendungen ab, und erspart hat Till nichts. [bg1]Der "
     "Bundesgerichtshof verlangt zwar grundsätzlich eine echte Vermögensvermehrung. [bg2]Im Ergebnis zählt für ihn aber die "
     "erlangte Beförderung; ob Till etwas erspart hat, prüft er wie den Wegfall der Bereicherung, also bei Paragraf "
     "achthundertachtzehn Absatz drei.", PS),
    # --- F § 818 Abs. 2 und 3 BGB ------------------------------------------------------------------------------------------
    ("[w2]Herausgeben kann Till den Flug nicht. Nach Paragraf achthundertachtzehn Absatz zwei hat er dann den Wert zu "
     "ersetzen, [wert]also die übliche Vergütung für den Flug. [w3]Aber Absatz drei: Die Verpflichtung ist ausgeschlossen, "
     "soweit der Empfänger nicht mehr bereichert ist. [lux]Ein Luxus, den man sich sonst nie geleistet hätte, kann "
     "tatsächlich zur Entreicherung führen, [lux2]jedenfalls beim gutgläubigen Empfänger.", PS),
    # --- G § 819 Abs. 1 BGB ------------------------------------------------------------------------------------------------
    ("[w819]Doch Paragraf achthundertneunzehn Absatz eins: Kennt der Empfänger den Mangel des rechtlichen Grundes bei dem "
     "Empfang, haftet er so, wie wenn der Anspruch auf Herausgabe rechtshängig geworden wäre. [r4]Damit gilt Paragraf "
     "achthundertachtzehn Absatz vier: Er haftet nach den allgemeinen Vorschriften; die Entreicherung hilft ihm nicht. [als]Der BGH behandelt ihn so, "
     "als hätte er sich etwas erspart. [kennt]Till wusste, dass er kein Ticket hatte. [aber]Aber er war siebzehn. Wessen "
     "Kenntnis zählt?", PS),
    # --- H Wessen Kenntnis? (Meinungsstand und BGH) ------------------------------------------------------------------------
    ("[mst]Das wird unterschiedlich beurteilt. [s1]Eine Ansicht stellt immer auf die Eltern ab. [s2]Eine andere wendet die "
     "Deliktsregeln entsprechend an, also die Einsicht des Minderjährigen. [s3]Eine dritte unterscheidet: bei der "
     "Leistungskondiktion die Eltern, bei der Eingriffskondiktion die Deliktsregeln. [b1]Der BGH: Soweit es der "
     "Minderjährigenschutz verlangt, vor allem bei der Rückabwicklung von Verträgen des Minderjährigen, zählt die Kenntnis "
     "der Eltern. [b2]Hat sich der Minderjährige das Erlangte aber durch eine vorsätzliche unerlaubte Handlung verschafft, "
     "zählt seine eigene Kenntnis. [b3]Hier sah der BGH zumindest ein Erschleichen der Beförderung nach Paragraf "
     "zweihundertfünfundsechzig a StGB.", PS),
    # --- I § 828 Abs. 3 BGB analog -----------------------------------------------------------------------------------------
    ("[w828]Maßstab ist dann Paragraf achthundertachtundzwanzig Absatz drei, entsprechend angewandt: [w828b]Wer das "
     "achtzehnte Lebensjahr noch nicht vollendet hat, ist nicht verantwortlich, wenn er nicht die zur Erkenntnis der "
     "Verantwortlichkeit erforderliche Einsicht hat. [damals]Damals stand diese Regel noch in Absatz zwei. [ein]Till war "
     "fast achtzehn und war gerade erst mit Ticket geflogen. [ein2]Dass er ohne Ticket nicht weiterfliegen durfte, konnte er "
     "einsehen.", PS),
    # --- J Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Till haftet verschärft. [erg2]Er muss den Wert des Fluges ersetzen, also den üblichen Flugpreis, "
     "[erg3]und auf die Entreicherung kann er sich nicht berufen. [rueck]Den Rückflug sprach der BGH der Fluggesellschaft "
     "über die Geschäftsführung ohne Auftrag zu.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Beim Minderjährigen im Bereicherungsrecht stoßen zwei Wertungen aufeinander. [tp2]Sein Schutz "
     "spricht für die Kenntnis der Eltern, [tp3]sein deliktsähnliches Verhalten für seine eigene Einsicht. [tp4]Entscheide "
     "das bei Paragraf achthundertneunzehn, und begründe, warum.", PS),
    # --- L Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [c1]Römisch eins: Anspruch aus Paragraf achthundertzwölf Absatz eins Satz eins Alternative zwei. "
     "[c2]Erstens: etwas erlangt, die Beförderung. [c3]Zweitens: in sonstiger Weise auf Kosten der Fluggesellschaft. "
     "[c4]Drittens: ohne rechtlichen Grund, kein Vertrag. [c5]Römisch zwei: Umfang. [c6]Erstens: Wertersatz "
     "nach Paragraf achthundertachtzehn Absatz zwei. [c7]Zweitens: Entreicherung nach Absatz drei? [c8]Drittens: verschärfte "
     "Haftung nach Paragraf achthundertneunzehn Absatz eins: Wessen Kenntnis zählt?", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Hat sich ein Minderjähriger das Erlangte durch eine vorsätzliche unerlaubte Handlung verschafft, zählt bei Paragraf "
     "achthundertneunzehn seine eigene Kenntnis, wenn er die nötige Einsicht hat. [mk2]Dann hilft ihm die Entreicherung "
     "nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
