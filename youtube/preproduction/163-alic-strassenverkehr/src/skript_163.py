"""Folge 163 · Betrunken Auto fahren: a.l.i.c. im Straßenverkehr – BGHSt 42, 235 (Mo · Der Fall · Klassiker-Fall;
§§ 20, 315c, 316, 323a, 69 StGB; Art. 103 Abs. 2 GG). Leitentscheidung: BGH, Urt. v. 22.8.1996 – 4 StR 217/96, BGHSt 42, 235,
Volltext HRRS mit Randnummern (hrr-strafrecht.de/hrr/4/96/4-217-96.php). Belege je Cue: ../RECHTSSTAND.md.
Hook (fiktiv, nach dem Plan): Leopold sitzt freitags in der Kneipe; schon beim ersten Bier weiß er, dass er nachher selbst
heimfährt. Nach Mitternacht fährt er ruhig durch die Nacht; an einer Polizeikontrolle (ohne Unfall) fällt er auf. Ein
Sachverständiger: bei Fahrtantritt schuldunfähig (Fallannahme, kein Promillewert). Variante nur als Text: Ein anderer Fahrer
muss scharf bremsen (konkrete Gefahr, § 315c).
Prüfung: § 20 (Wortlautkarte, Koinzidenzprinzip) → a.l.i.c. knapp (Ausnahmemodell, Tatbestandsmodell) → echter Fall
(Rn. 1, 6, 14 f.) → Kern: Tatbestandsmodell scheitert am „Führen“ (Rn. 17–19), Ausnahmemodell an § 20 und Art. 103 Abs. 2 GG
(Wortlautkarte; Rn. 22) → offen gelassen (Rn. 16, 18), § 222 ohne a.l.i.c. (Rn. 8 f.) → § 323a (Wortlautkarte; Rn. 23, 25)
→ Lösung des Hooks, § 69 Abs. 1, 2 Nr. 4 → Klausurtipp → Prüfschema → Merksatz.
DARSTELLUNG: kein Unfall im Bild, kein Aufprall, keine Verletzten; Alkohol nur als neutrale Glas-Icons; Fahrt als ruhige
Nachtfahrt. Der echte Unfall des BGH-Falls wird nur in einem sachlichen Satz genannt (Tenor: fahrlässige Tötung), nicht gezeigt.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Leopold (nie im Genitiv); die Polizistin ist
Funktionsrolle ohne Namen. Stimmen (nur aus dem Pool william, sabrina, marc, laura_ruhig): Leopold william (Mann, älter),
Polizistin laura_ruhig (Frau, mittel). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; „Bundesgerichtshof“ ausgeschrieben."""

P, PS = 0.3, 0.5

STIMMEN = {"Leopold": "william", "Polizistin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: in der Kneipe ------------------------------------------------------------------------------------------
    ("[fall]Freitagabend in der Kneipe. [leo]Leopold trifft Freunde. [auto]Sein Auto steht vor der Tür. "
     "[erstes]Schon beim ersten Bier ist ihm klar: Nachher fährt er selbst nach Hause.", P),
    ("[l1]Ich fahre nachher selbst heim. Das geht schon.", P, "Leopold"),
    ("[spaet]Es wird spät, und es bleibt nicht bei einem Bier. [mitt]Nach Mitternacht steigt Leopold in sein Auto.", P),
    # --- A2 Fall: ruhige Fahrt durch die Nacht -------------------------------------------------------------------------------
    ("[fahrt]Er fährt durch die Nacht. [kontr]Am Ortseingang steht eine Polizeikontrolle.", P),
    # --- A3 Fall: die Kontrolle ----------------------------------------------------------------------------------------------
    ("[p1]Guten Abend, Verkehrskontrolle. Haben Sie etwas getrunken?", P, "Polizistin"),
    ("[l2]Nur ein paar Bier.", P, "Leopold"),
    ("[blut]Die Blutprobe zeigt: Leopold war stark betrunken. [gut]Ein Sachverständiger stellt fest: Bei "
     "Fahrtantritt war er schuldunfähig. [frage]Kann Leopold trotzdem wegen Trunkenheit im Verkehr bestraft werden? "
     "[frage2]Er wusste doch schon beim ersten Bier, dass er fahren wird. [var]Und was gilt, wenn unterwegs ein anderer "
     "Fahrer scharf bremsen musste?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 20 StGB (Wortlautkarte), Koinzidenzprinzip ------------------------------------------------------------------------
    ("[p20]Nach Paragraf zwanzig handelt ohne Schuld, wer bei Begehung der Tat wegen einer der dort genannten Störungen "
     "unfähig ist, das Unrecht der Tat einzusehen oder nach dieser Einsicht zu handeln. [stfg]Ein schwerer "
     "Rausch kann die Steuerungsfähigkeit aufheben, so wie bei Leopold. [koinz]Entscheidend ist der Zeitpunkt: Die "
     "Schuldfähigkeit muss bei Begehung der Tat vorliegen. Das nennt man Koinzidenzprinzip. [z1]Beim ersten Bier war "
     "Leopold schuldfähig, aber er fuhr noch nicht. [z2]Am Steuer fuhr er, war aber schuldunfähig.", PS),
    # --- D a.l.i.c. knapp: Ausnahmemodell, Tatbestandsmodell ---------------------------------------------------------------
    ("[alic]Hier setzt die actio libera in causa an, die in ihrer Ursache freie Handlung. [idee]Wer sich schuldhaft "
     "berauscht und dabei schon an die spätere Tat denkt, soll sich nicht auf den Rausch berufen können. [ausn]Das "
     "Ausnahmemodell macht dafür eine Ausnahme vom Koinzidenzprinzip: Die Schuld beim Trinken genügt. [tatb]Das "
     "Tatbestandsmodell verlegt dagegen die Tathandlung nach vorn: Schon das Sich-Betrinken ist der Beginn der Tat.", PS),
    # --- E Der echte Fall: BGHSt 42, 235 ------------------------------------------------------------------------------------
    ("[echt]Genau darüber hat der Bundesgerichtshof neunzehnhundertsechsundneunzig entschieden. [lief]Ein "
     "Lieferwagenfahrer ohne Fahrerlaubnis betrank sich in den Niederlanden, [trank]obwohl er noch kein Hotel für die "
     "Nacht hatte. [grenze]Kurz hinter der deutschen Grenze "
     "verunglückte er an einer Kontrollstelle; zwei Beamte des Grenzschutzes kamen ums Leben. "
     "[sfu]Beim Fahren war er schuldunfähig. [lg]Das Landgericht Osnabrück verurteilte ihn trotzdem auch wegen "
     "vorsätzlicher Gefährdung des Straßenverkehrs, mit Hilfe der actio libera in causa.", PS),
    # --- F Kern: Tatbestandsmodell scheitert am „Führen“ ---------------------------------------------------------------------
    ("[kern]Der Bundesgerichtshof sah das anders: Jedenfalls bei der Gefährdung des Straßenverkehrs und beim Fahren ohne "
     "Fahrerlaubnis ist die Vorverlagerung der Schuld unzulässig. [fuehr]Erstens zum Tatbestandsmodell: Diese Delikte verlangen, dass der Täter ein Fahrzeug führt. "
     "[anf]Das Führen beginnt erst mit dem Anfahren; nicht einmal das Anlassen des Motors genügt. [trink]Wer sich "
     "betrinkt, führt also noch kein Fahrzeug. [verh]Die Paragrafen dreihundertfünfzehn c und dreihundertsechzehn "
     "verbieten ein Verhalten, das sich nicht als Herbeiführen eines davon trennbaren Erfolgs "
     "begreifen lässt. [eigen]In der Lehre heißen solche Tatbestände "
     "verhaltensgebundene oder eigenhändige Delikte. [fahrl]Das gilt auch für fahrlässige Verstöße.", PS),
    # --- G Ausnahmemodell: § 20, Art. 103 Abs. 2 GG (Wortlautkarte) -----------------------------------------------------------
    ("[ausn2]Zweitens zum Ausnahmemodell: Es ist mit dem eindeutigen Wortlaut von Paragraf zwanzig nicht vereinbar, der "
     "die Schuldfähigkeit bei Begehung der Tat verlangt. [gew]Auch als Gewohnheitsrecht lässt sich die Ausnahme nicht "
     "halten. [a103]Denn Artikel einhundertdrei Absatz zwei des Grundgesetzes sagt: Eine Tat kann nur "
     "bestraft werden, wenn die Strafbarkeit gesetzlich bestimmt war, bevor die Tat begangen wurde. [verbot]Das verbietet "
     "strafbarkeitsbegründendes Gewohnheitsrecht, [at]auch im Allgemeinen Teil.", PS),
    # --- H Was offen bleibt; fahrlässige Tötung ohne a.l.i.c. ---------------------------------------------------------------
    ("[offen]Ob die Rechtsfigur bei anderen Delikten trägt, ließ der Senat offen. [k222]Bei der fahrlässigen "
     "Tötung braucht man sie gar nicht: Hier knüpft der Vorwurf an das Trinken an, obwohl der Fahrer damit rechnen musste, "
     "danach noch zu fahren. [erg222]Deshalb blieb er wegen fahrlässiger Tötung in zwei Fällen strafbar.", PS),
    # --- I Was bleibt: § 323a StGB (Wortlautkarte) ---------------------------------------------------------------------------
    ("[p323]Was bleibt bei den Verkehrsdelikten? Der Vollrausch, Paragraf dreihundertdreiundzwanzig a. [w1]Bestraft wird, "
     "wer sich vorsätzlich oder fahrlässig in einen Rausch versetzt, [w2]wenn er in diesem Zustand eine rechtswidrige Tat "
     "begeht [w3]und ihretwegen nicht bestraft werden kann, weil er infolge des Rausches schuldunfähig war oder dies nicht "
     "auszuschließen ist. [bed]Die Rauschtat "
     "ist dabei kein Tatbestandsmerkmal, sondern eine Bedingung der Strafbarkeit. [rahmen]Die Strafe reicht bis zu fünf "
     "Jahren, [abs2]darf aber nicht schwerer sein als die für die Rauschtat angedrohte Strafe. [bgh2]Im echten Fall: vorsätzlicher "
     "Vollrausch mit der Verkehrsgefährdung als Rauschtat.", PS),
    # --- J Lösung des Hooks ----------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Leopold. [l316]Aus Paragraf dreihundertsechzehn ist er nicht strafbar: Er war schuldunfähig, und die "
     "actio libera in causa hilft hier nicht. [l323]Er hat sich aber vorsätzlich in einen Rausch versetzt und dann sein "
     "Auto geführt: Vollrausch, mit der Trunkenheitsfahrt als Rauschtat. [l1j]Paragraf dreihundertsechzehn droht höchstens "
     "ein Jahr an; diese Grenze gilt auch hier. [lvar]In der Variante mit der scharfen Bremsung ist die Rauschtat "
     "Paragraf dreihundertfünfzehn c, wenn ein Beinahe-Unfall feststeht. [l69]Die Fahrerlaubnis wird ihm in der Regel "
     "entzogen, auch beim Vollrausch: Paragraf neunundsechzig.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst das Verkehrsdelikt bis zur Schuld. [tipp2]Bei Paragraf zwanzig sprichst du die "
     "actio libera in causa an und lehnst sie mit dem Bundesgerichtshof ab. [tipp3]Erst danach kommt der Vollrausch.", PS),
    # --- L Prüfschema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]A: Paragraf dreihundertsechzehn. Tatbestand und Rechtswidrigkeit liegen vor. "
     "[s2]Schuld: Paragraf zwanzig, schuldunfähig bei Fahrtantritt. [s3]Actio libera in causa? Bei Verkehrsdelikten "
     "abgelehnt. [s4]B: Paragraf dreihundertdreiundzwanzig a. Römisch eins: vorsätzlich oder fahrlässig in einen Rausch "
     "versetzt. [s5]Römisch zwei: Rauschtat als Bedingung der Strafbarkeit. [s6]Römisch drei: Rechtswidrigkeit und "
     "Schuld, Strafrahmen nach Absatz zwei.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer sich betrinkt, führt noch kein Fahrzeug. [m2]Bei Paragraf dreihundertfünfzehn c und "
     "dreihundertsechzehn hilft die actio libera in causa deshalb nicht; [m3]es bleibt der Vollrausch.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
