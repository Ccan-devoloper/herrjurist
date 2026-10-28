"""Folge 232 · Kündigung wegen 1,30 Euro? Der Fall Emmely (§ 626 BGB) (Mo · Der Fall · Arbeitsrecht, Klassiker-Fall).
Fiktiver Rahmen, der dem echten Fall folgt (BAG, Urt. v. 10.6.2010 – 2 AZR 541/09): Kassiererin Doris (fiktiv) arbeitet
seit fast 31 Jahren beanstandungsfrei in einem Supermarkt (fiktiv, keine echte Handelskette). Kollegin Merle findet zwei
Pfandbons (0,48 € und 0,82 €), Filialleiter Bartels gibt sie Doris zur Aufbewahrung im Kassenbüro, falls sich der Kunde
meldet. Zehn Tage später löst Doris bei einem privaten Einkauf zwei nicht abgezeichnete Pfandbons ein (1,30 €), Herr Bartels
steht daneben. Fristlose, hilfsweise ordentliche Kündigung.
Prüfung: § 626 Abs. 1 BGB (Wortlautkarte) → zwei Stufen (Rn. 16) → Stufe 1: an sich geeignet, auch geringwertig, keine
Wertgrenze, Prognoseprinzip (Rn. 25–28), Feststellung LAG, Anordnung missachtet, Kernbereich (Rn. 20 f., 31, 42) → Stufe 2:
Abwägungskriterien, mildere Mittel (Rn. 34), Abmahnung aus Verhältnismäßigkeit, § 314 Abs. 2 BGB als Bestätigung
(Wortlautkarte; Rn. 35, 37), Ausnahmen, auch im Vermögensbereich (Rn. 37 f.), Fall: offen statt heimlich (Rn. 45),
fast 31 Jahre, „Vorrat an Vertrauen“, objektiver Maßstab (Rn. 47–50), geringer Nachteil (Rn. 50), Prozessverhalten
(Rn. 52, 56) → Ergebnis (Rn. 14, 32) → § 626 Abs. 2 (Wortlautkarte), hilfsweise ordentliche Kündigung § 1 Abs. 2 S. 1 KSchG
(Wortlautkarte kurz; Rn. 58), Verweis Folge 152 → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi).
Belege: ../RECHTSSTAND.md. Die reale Klägerin wird weder dargestellt noch benannt; „Emmely“ nur als Fallbezeichnung auf
der Tafel, nicht im Sprechtext.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Liste und namen_reserviert.txt, 07.10.2026): Doris, Merle,
Bartels (nie im Genitiv). Stimmen: Merle ela_froh (fröhlicher, harmloser Satz), Herr Bartels helmut; Doris spricht nicht
(keine Frauenstimme passenden Alters im Pool). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; KSchG ausgeschrieben."""

P, PS = 0.3, 0.5

STIMMEN = {"Merle": "ela_froh", "Bartels": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: an der Kasse ----------------------------------------------------------------------------------------------
    ("[fall]Ein Supermarkt mitten in der Stadt. [doris]Doris sitzt hier seit fast einunddreißig Jahren an der Kasse, ohne "
     "jede Beanstandung. [fund]Eines Morgens findet ihre Kollegin Merle im Kassenbereich zwei Pfandbons, über "
     "achtundvierzig und zweiundachtzig Cent.", P),
    ("[me1]Die hat wohl jemand liegen lassen!", P, "Merle"),
    ("[chef]Filialleiter Bartels gibt die Bons an Doris weiter.", 0.2),
    ("[ba1]Bewahren Sie die im Kassenbüro auf, falls sich noch jemand meldet.", P, "Bartels"),
    ("[ablage]Doris legt sie auf eine Ablage im Kassenbüro. [zehn]Zehn Tage später kauft sie außerhalb ihrer Arbeitszeit "
     "privat ein. [einl]Bei Merle an der Kasse reicht sie zwei Pfandbons, die nicht abgezeichnet sind. [summe]Ihr Einkauf "
     "wird einen Euro dreißig billiger. [dabei]Herr Bartels steht direkt daneben.", P),
    ("[kuend]Der Arbeitgeber verdächtigt sie, die Bons aus dem Kassenbüro eingelöst zu haben, und kündigt fristlos, "
     "hilfsweise ordentlich.", 0.2),
    ("[ba2]Das Vertrauen ist unwiederbringlich zerstört.", P, "Bartels"),
    ("[frage]Darf man nach fast einunddreißig Jahren wegen Pfandbons über einen Euro dreißig fristlos kündigen? "
     "[echt]Unser Fall folgt einem echten Fall, den das Bundesarbeitsgericht zweitausendzehn entschieden hat.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 626 Abs. 1 BGB, zwei Stufen (Rn. 16) ----------------------------------------------------------------------------
    ("[p626]Die Antwort steht in Paragraf sechshundertsechsundzwanzig Absatz eins BGB. [wg]Ein Dienstverhältnis, also auch "
     "ein Arbeitsverhältnis, kann aus wichtigem Grund ohne Kündigungsfrist gekündigt werden, [umst]wenn dem Kündigenden "
     "unter Berücksichtigung aller Umstände des Einzelfalles und unter Abwägung der Interessen beider Vertragsteile "
     "[zumut]die Fortsetzung bis zum Ablauf der Kündigungsfrist nicht zugemutet werden kann. [stufen]Das "
     "Bundesarbeitsgericht prüft deshalb in zwei Stufen: [stufe1]Ist der Sachverhalt an sich, also typischerweise, als "
     "wichtiger Grund geeignet? [stufe2]Und ist die Fortsetzung nach Abwägung aller Umstände trotzdem zumutbar? "
     "[absolut]Absolute Kündigungsgründe kennt das Gesetz nicht.", PS),
    # --- D Stufe 1: an sich geeignet (Rn. 20 f., 25–28, 31, 42) ---------------------------------------------------------------
    ("[s1]Erste Stufe. [verm]Rechtswidrige und vorsätzliche Handlungen gegen das Vermögen des Arbeitgebers sind an sich "
     "als wichtiger Grund geeignet, [gering]auch wenn es nur um Sachen von geringem Wert geht oder gar kein Schaden "
     "entsteht. [grenze]Eine Wertgrenze lehnt das Gericht ab: [vertr]Das Vertrauen wird erschüttert, egal wie hoch der "
     "Schaden ist. [prog]Und die Kündigung ist keine Strafe. Es gilt das Prognoseprinzip: Ist künftig noch eine "
     "störungsfreie Vertragserfüllung zu erwarten?", P),
    ("[fest]Im Fall hält das Landesarbeitsgericht für erwiesen, dass Doris die Bons aus dem Kassenbüro eingelöst hat. "
     "[bestr]Sie bestreitet ein bewusstes Fehlverhalten; [bind]das Bundesarbeitsgericht ist aber an diese Feststellung "
     "gebunden. [vort]Doris hat sich einen Vorteil verschafft, der ihr nicht zustand, [weis]und die klare Anweisung ihres "
     "Filialleiters missachtet. [kern]Das trifft den Kernbereich ihrer Arbeit als Kassiererin. [ansich]Ein wichtiger Grund "
     "an sich liegt also vor.", PS),
    # --- E Stufe 2: Interessenabwägung (Rn. 34–38) ---------------------------------------------------------------------------
    ("[abw]Zweite Stufe: die Interessenabwägung. [krit]Zu berücksichtigen sind etwa das Gewicht der Pflichtverletzung, der "
     "Grad des Verschuldens, eine Wiederholungsgefahr [dauer]und die Dauer des Arbeitsverhältnisses mit seinem "
     "störungsfreien Verlauf. [mild]Fristlos kündigen darf der Arbeitgeber nur, wenn ihm alle milderen Mittel unzumutbar "
     "sind, [abm]vor allem eine Abmahnung oder eine ordentliche Kündigung.", P),
    ("[verh]Die Abmahnung folgt aus dem Grundsatz der Verhältnismäßigkeit; [p314]Paragraf dreihundertvierzehn Absatz zwei "
     "BGB bestätigt diesen Gedanken. [entb]Entbehrlich ist sie nur, wenn eine Besserung selbst nach einer Abmahnung nicht "
     "zu erwarten ist [schwer]oder die Pflichtverletzung so schwer wiegt, dass eine Hinnahme offensichtlich ausgeschlossen "
     "ist. [vb]Das gilt auch bei Vermögensdelikten gegen den Arbeitgeber.", PS),
    # --- F Abwägung im Fall (Rn. 45–50, 52, 56) ------------------------------------------------------------------------------
    ("[fall2]Und im Fall? [offen]Doris hat die Bons offen eingelöst, vor den Augen ihres Vorgesetzten. [heiml]Das war "
     "nicht auf Heimlichkeit angelegt [unr]und spricht dafür, dass sie sich eines schweren Unrechts nicht bewusst war. "
     "[jahre]Vor allem: fast einunddreißig Jahre ohne vergleichbare Pflichtverletzung. [vorrat]Das Gericht spricht von einem "
     "erarbeiteten Vorrat an Vertrauen. [aufg]Je länger die Zusammenarbeit ungestört war, desto eher wird er durch einen "
     "ersten Vorfall nicht vollständig aufgezehrt. "
     "[obj]Maßgeblich ist ein objektiver Maßstab, nicht das Gefühl des Arbeitgebers. [schad]Dazu kommt der geringe "
     "Nachteil: Nach zehn Tagen war mit einer Nachfrage nach den Bons nicht mehr zu rechnen.", P),
    ("[proz]Und dass Doris ihre Erklärungen im Prozess mehrmals geändert hat? [zug]Das zählt nicht gegen sie. Maßgeblich "
     "ist der Zeitpunkt, in dem die Kündigung zugeht. [rueck]Ihr wechselnder Vortrag lässt keine Rückschlüsse auf ihre "
     "künftige Zuverlässigkeit zu.", PS),
    # --- G Ergebnis (Rn. 14, 32, 50) -----------------------------------------------------------------------------------------
    ("[erg]Das Ergebnis: [unw]Die fristlose Kündigung ist unwirksam. [ausr]Eine Abmahnung hätte ausgereicht.", PS),
    # --- H § 626 Abs. 2 BGB, hilfsweise ordentliche Kündigung (Rn. 58) -------------------------------------------------------
    ("[p2]Noch zwei Punkte. Paragraf sechshundertsechsundzwanzig Absatz zwei: Die Kündigung kann nur "
     "innerhalb von zwei Wochen erfolgen, [kennt]ab Kenntnis der maßgebenden Tatsachen. [ord]Und die hilfsweise ordentliche "
     "Kündigung? [kschg]Sie ist nach Paragraf eins Absatz zwei Kündigungsschutzgesetz sozial ungerechtfertigt, weil auch "
     "hier die Abmahnung genügt hätte. [v152]Wann das Kündigungsschutzgesetz gilt, zeigt das Video zum Kündigungsschutz.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: [t1]Sortiere den Bagatellfall nicht schon auf der ersten Stufe aus. [t2]Der geringe Wert gehört "
     "in die Interessenabwägung. [t3]Und prüfe dort immer, ob eine Abmahnung als milderes Mittel genügt hätte.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die fristlose Kündigung. [k1]Römisch eins: Kündigungserklärung, schriftlich nach Paragraf "
     "sechshundertdreiundzwanzig BGB. [k2]Römisch zwei: Klagefrist von drei Wochen nach Paragraf dreizehn und Paragraf vier "
     "Kündigungsschutzgesetz. [k3]Römisch drei: wichtiger Grund nach Paragraf sechshundertsechsundzwanzig Absatz eins, "
     "[k3a]erstens an sich geeignet, [k3b]zweitens Interessenabwägung mit milderen Mitteln. [k4]Römisch vier: "
     "Zwei-Wochen-Frist nach Absatz zwei.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Auch ein Bagatelldelikt gegen den Arbeitgeber kann an sich ein wichtiger Grund sein. [m2]Doch vor der "
     "Kündigung steht in der Regel die Abmahnung, gerade nach vielen Jahren ohne Beanstandung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
