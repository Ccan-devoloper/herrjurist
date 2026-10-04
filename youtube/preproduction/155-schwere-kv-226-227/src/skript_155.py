"""Folge 155 · Schwere Körperverletzung § 226 & Todesfolge § 227 StGB (Mi · Examenswissen · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Faustschlag, ein Sturz, ein verlorenes Auge – oder sogar der Tod: Was ändert die
schwere Folge?“): Freitagabend vor einer Bar. Roswitha und Ludger wollen in dasselbe Taxi; Roswitha schlägt Ludger mit der
Faust ins Gesicht (Verletzungsvorsatz), Ludger stürzt rückwärts auf das Pflaster. Variante A: Ludger verliert durch den Schlag
dauerhaft das Sehvermögen auf dem linken Auge. Variante B: Beim Sturz schlägt sein Kopf auf das Pflaster, er stirbt an dieser
Kopfverletzung. Mit beidem hat Roswitha nicht gerechnet.
Prüfung: Grunddelikt § 223 (nur verwiesen, Folge 038) → Erfolgsqualifikation, Wortlautkarte § 18 → Wortlautkarte § 226
Abs. 1 (Nr. 1–3 vollständig) → Variante A unter Nr. 1 (Verlust: BGH 4 StR 327/00 Rn. 16), Nr. 2/3 (−), Fahrlässigkeit
(Vorhersehbarkeit nach 5 StR 42/02 Rn. 42), Abs. 2 (ein Satz) → Wortlautkarte § 227 Abs. 1 → Kausalität genügt nicht →
spezifischer Gefahrzusammenhang (5 StR 42/02 Rn. 37; 5 StR 435/07 Rn. 8; Formel aus BGHSt 31, 96, 98) → Letalitätstheorie
(Lehre, Rn. 37 f.) gegen BGH (Handlung genügt, Rn. 37 f.; Wortlautargument Rn. 38) → Gubener Hetzjagd (versuchte KV mit
Todesfolge, Flucht deliktstypisch, Rn. 39 f.) → älteres Urteil 3 StR 119/70 „zu restriktiv“ (5 StR 435/07 Rn. 10) → Lösung B,
Vorhersehbarkeit (Rn. 42) → Abgrenzung §§ 212, 222 (ein Satz, Verweis Folge 035) → § 227 Abs. 2 (Halbsatz) → Klausurtipp →
Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Roswitha (Täterin), Ludger (Opfer).
Stimmen nur aus dem Pool: Roswitha sabrina (Frau, mittel), Ludger marc (Mann, mittel). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ludger": "marc", "Roswitha": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: vor der Bar ---------------------------------------------------------------------------------------------------
    ("[fall]Ein Freitagabend vor einer Bar in der Altstadt. [taxi]Roswitha und Ludger wollen beide in dasselbe Taxi "
     "steigen.", 0.3),
    ("[l1]Das Taxi habe ich bestellt!", 0.3, "Ludger"),
    ("[r1]Ich war aber zuerst hier.", 0.3, "Roswitha"),
    ("[schlag]Roswitha schlägt Ludger mit der Faust ins Gesicht. Sie will ihn verletzen, mehr nicht. [sturz]Ludger stürzt "
     "rückwärts auf das Pflaster. [va]Variante A: Durch den Schlag verliert Ludger dauerhaft das Sehvermögen auf dem linken "
     "Auge. [vb]Variante B: Beim Sturz schlägt sein Kopf auf das Pflaster, und Ludger stirbt an dieser Kopfverletzung. "
     "[nicht]Mit beidem hat Roswitha nicht gerechnet.", 0.4),
    ("[frage]Ein Faustschlag, ein Sturz, ein verlorenes Auge, oder sogar der Tod. [frage2]Was ändert die schwere Folge?", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Erfolgsqualifikation, § 18 ------------------------------------------------------------------------------------------
    ("[grund]Zuerst das Grunddelikt: Mit dem Faustschlag hat Roswitha Ludger vorsätzlich körperlich misshandelt, Paragraf "
     "zweihundertdreiundzwanzig, mehr dazu im Video zur Körperverletzung. [eq]Darauf bauen die Paragrafen "
     "zweihundertsechsundzwanzig und zweihundertsiebenundzwanzig auf, als erfolgsqualifizierte Delikte: [formel]Grunddelikt plus schwere Folge. [p18]Für die Folge gilt Paragraf achtzehn: Knüpft das Gesetz an eine besondere "
     "Folge der Tat eine schwerere Strafe, so trifft sie den Täter oder den Teilnehmer nur, wenn ihm hinsichtlich dieser Folge "
     "wenigstens Fahrlässigkeit zur Last fällt. [vf]Also Vorsatz für das Grunddelikt und wenigstens Fahrlässigkeit für die "
     "Folge.", PS),
    # --- D Wortlautkarte § 226 Abs. 1, Abs. 2 ----------------------------------------------------------------------------------
    ("[p226]Paragraf zweihundertsechsundzwanzig Absatz eins nennt drei Gruppen schwerer Folgen. [nr1]Nummer eins: der "
     "Verlust des Sehvermögens auf einem oder beiden Augen, des Gehörs, des Sprechvermögens oder der Fortpflanzungsfähigkeit. "
     "[nr2]Nummer zwei: ein wichtiges Glied geht verloren oder ist dauernd unbrauchbar. [nr3]Nummer drei: eine erhebliche "
     "dauernde Entstellung, Siechtum, Lähmung, geistige Krankheit oder Behinderung. [rahmen1]Die Strafe: ein Jahr bis zehn "
     "Jahre.", PS),
    # --- E Variante A ----------------------------------------------------------------------------------------------------------
    ("[sub_a]In Variante A hat Ludger das Sehvermögen auf dem linken Auge verloren. [verlust]Verlust heißt: Die Sehkraft ist "
     "faktisch weg, eine bloße Minderung reicht nicht. Bei Ludger ist das so, Nummer eins liegt vor. [nr23]Nummer "
     "zwei und drei dagegen nicht: Kein Glied ist betroffen, und äußerlich ist Ludger nicht entstellt. [fahrl_a]Und die "
     "Fahrlässigkeit? Dass ein Faustschlag ins Gesicht ein Auge dauerhaft schädigt, liegt nicht außerhalb aller "
     "Lebenserfahrung. Die Folge war vorhersehbar. [erg_a]Roswitha ist in Variante A strafbar nach Paragraf "
     "zweihundertsechsundzwanzig Absatz eins Nummer eins. [abs2]Hätte sie das Auge absichtlich oder wissentlich zerstört, "
     "griffe Absatz zwei: Freiheitsstrafe nicht unter drei Jahren.", PS),
    # --- F Wortlautkarte § 227 Abs. 1 ------------------------------------------------------------------------------------------
    ("[p227]Für Variante B gilt Paragraf zweihundertsiebenundzwanzig Absatz eins: Verursacht der Täter durch die "
     "Körperverletzung den Tod der verletzten Person, so ist die Strafe Freiheitsstrafe nicht unter drei Jahren. [kaus]Der "
     "Faustschlag war ursächlich für den Sturz und damit für den Tod. [nurk]Doch bloße Kausalität reicht nicht.", PS),
    # --- G Kernproblem: spezifischer Gefahrzusammenhang ------------------------------------------------------------------------
    ("[spez]Der Bundesgerichtshof verlangt einen spezifischen Gefahrzusammenhang: Der Körperverletzung muss die "
     "Gefahr anhaften, zum Tod des Opfers zu führen, [nieder]und gerade diese Gefahr muss sich im Tod niedergeschlagen haben. "
     "[woran]Doch woran knüpft diese Gefahr an? [leta]Nach der Letalitätstheorie, einer Ansicht in der Lehre, muss der "
     "Verletzungserfolg selbst tödlich sein. [leta_b]Bei Ludger war aber nicht die Verletzung im Gesicht tödlich, "
     "sondern der Aufprall. [bgh]Der Bundesgerichtshof lässt auch die Gefahr genügen, die schon von der Körperverletzungshandlung "
     "ausgeht. [arg]Dafür spricht der Verweis: Paragraf zweihundertsiebenundzwanzig verweist auf die Paragrafen "
     "zweihundertdreiundzwanzig bis zweihundertsechsundzwanzig a, und dort ist auch der Versuch erfasst.", PS),
    ("[guben]Deshalb ist sogar eine versuchte Körperverletzung mit Todesfolge möglich. So entschied der Bundesgerichtshof "
     "zweitausendzwei im Fall der Gubener Hetzjagd: [floh]Ein Mann floh in Todesangst vor einer Gruppe von Angreifern und zog "
     "sich dabei tödliche Verletzungen zu. [typisch]Eine solche Flucht ist eine naheliegende Reaktion und geradezu "
     "deliktstypisch, sie unterbricht den Zusammenhang nicht. [aelter]Ein älteres Urteil, das bei Selbstgefährdung des "
     "Opfers die Zurechnung verneinte, nannte der Bundesgerichtshof zweitausendacht zu restriktiv.", PS),
    # --- H Lösung Variante B, Abgrenzung ---------------------------------------------------------------------------------------
    ("[sub_b]Zurück zu Ludger. Ein wuchtiger Faustschlag ins Gesicht birgt typischerweise die Gefahr, dass das Opfer stürzt "
     "und mit dem Kopf aufschlägt. [gef_ok]Genau diese Gefahr hat sich im Tod verwirklicht, der Gefahrzusammenhang liegt vor. "
     "[vorh]Und der Tod war vorhersehbar: Er liegt nicht außerhalb aller Lebenserfahrung, die Einzelheiten des Ablaufs muss "
     "Roswitha nicht vorhersehen. [erg_b]Roswitha ist in Variante B strafbar nach Paragraf zweihundertsiebenundzwanzig Absatz "
     "eins. [msf]In minder schweren Fällen sieht Absatz zwei ein Jahr bis zehn Jahre vor.", PS),
    ("[abgr]Hätte Roswitha den Tod vorsätzlich herbeigeführt, wäre es ein Totschlag; [p222]fehlt schon der "
     "Körperverletzungsvorsatz, bleibt die fahrlässige Tötung nach Paragraf zweihundertzweiundzwanzig. [v035]Mehr dazu im Video "
     "zu den Tötungsdelikten.", PS),
    # --- I Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Hake den Paragrafen zweihundertsiebenundzwanzig nicht mit der Kausalität ab. [tipp2]Der "
     "Gefahrzusammenhang ist der Schwerpunkt. Kommt es auf den Streit an, wie bei Ludger, entscheide ihn. [tipp3]Und prüfe die Fahrlässigkeit für die Folge gesondert, nach Paragraf achtzehn.", PS),
    # --- J Prüfungsschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema für die Körperverletzung mit Todesfolge. [s1]Römisch eins, Tatbestand. [s1a]Eins: das "
     "Grunddelikt, eine vorsätzliche Körperverletzung. [s1b]Zwei: die schwere Folge, hier der Tod. [s1c]Drei: Kausalität und "
     "objektive Zurechnung. [s1d]Vier: der spezifische Gefahrzusammenhang. [s1e]Fünf: wenigstens Fahrlässigkeit bezüglich der "
     "Folge, Paragraf achtzehn. [s2]Römisch zwei, Rechtswidrigkeit. [s3]Römisch drei, Schuld. [s226]Bei Paragraf "
     "zweihundertsechsundzwanzig steht an zweiter Stelle eine der schweren Dauerfolgen.", PS),
    # --- K Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Grunddelikt plus schwere Folge, und für die Folge wenigstens Fahrlässigkeit. [m2]Beim Tod muss sich "
     "die spezifische Gefahr der Körperverletzung verwirklichen, und die kann schon von der Handlung ausgehen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
