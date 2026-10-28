"""Folge 068 · Tatbestandsirrtum § 16 StGB: Jäger, Pilzsammler & Fahrlässigkeit (Mi · Examenswissen · StGB AT, Format Schema).
Beispielfall nach dem Plan-Hook, sehr zurückhaltend dargestellt (keine Waffe im Bild, kein Schuss, kein Blut, keine Verletzung;
nur Hochsitz, Dämmerung/Mond, Busch, Wildschwein als Gedankenbild, Rettungswagen-Symbol): Jägerin Jutta sitzt in der
Abenddämmerung auf ihrem Hochsitz und wartet auf Wildschweine; im Unterholz sucht der Rentner Ludwig nach Pilzen. Im
Dämmerlicht sieht Jutta nur einen dunklen Umriss, hält ihn für ein Wildschwein und schießt, ohne genauer hinzusehen. Ludwig
wird am Bein getroffen und überlebt (§ 229); § 222 nur als Abwandlung in einem Satz.
Prüfung: §§ 223, 224 I Nr. 2 objektiv (+) → Vorsatz = Wissen und Wollen (Verweis Folge 029) → § 16 I 1 (Wortlautkarte;
BGHSt 63, 88 Rn. 14): „andere Person“ (§ 223) bzw. „Mensch“ (§ 212) unbekannt → Vorsatz (−), versuchter Totschlag (−)
→ kein error in persona (BGH 4 StR 281/25 Rn. 7 f.: nur gleichwertige Objekte) → § 16 I 2, § 15 → § 229 (Wortlautkarte):
Erfolg/Kausalität, objektive Sorgfaltspflichtverletzung (BGHSt 66, 119 Rn. 14; UVV Jagd VSG 4.4 § 3 Abs. 4), objektive
Vorhersehbarkeit (Rn. 11, 18), Pflichtwidrigkeitszusammenhang, Rechtswidrigkeit, Schuld → Ergebnis → Abwandlung § 222 →
Abgrenzung § 17 (ein Satz) → Klausurtipp (Strafantrag § 230 I) → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Jutta, Ludwig. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Jutta": "julia", "Ludwig": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: am Waldrand in der Abenddämmerung ---------------------------------------------------------------------------
    ("[fall]Ein Abend im Oktober, kurz nach Sonnenuntergang, am Rand eines Waldes. [jutta]Jutta, eine erfahrene Jägerin, sitzt "
     "auf ihrem Hochsitz. Sie darf hier jagen und wartet auf Wildschweine. [ludwig]Im Unterholz gegenüber sucht Ludwig, ein "
     "Rentner, noch nach Pilzen.", 0.3),
    ("[l1]Noch ein paar Steinpilze, dann gehe ich heim.", 0.3, "Ludwig"),
    ("[bueckt]Ludwig bückt sich, das Gebüsch raschelt. [umriss]Im Dämmerlicht sieht Jutta nur einen dunklen Umriss.", 0.3),
    ("[j1]Da im Gebüsch, ein Wildschwein.", 0.3, "Jutta"),
    ("[schuss]Ohne genauer hinzusehen, schießt sie. [treffer]Getroffen wird Ludwig, am Bein. [rtw]Ein Rettungswagen bringt "
     "ihn ins Krankenhaus. Er überlebt.", 0.3),
    ("[j2]Ich war mir sicher, das ist ein Wildschwein.", 0.4, "Jutta"),
    ("[frage]Hat Jutta den Pilzsammler vorsätzlich verletzt? [frage2]Und wenn nicht: Bleibt dann gar nichts?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Vorsatzdelikt: §§ 223, 224 --------------------------------------------------------------------------------------------
    ("[p223]Wir beginnen mit dem Vorsatzdelikt: Körperverletzung nach Paragraf zweihundertdreiundzwanzig, wegen des Gewehrs "
     "zusammen mit Paragraf zweihundertvierundzwanzig. [obj]Objektiv ist alles erfüllt. Ludwig ist eine andere Person, er ist "
     "an der Gesundheit geschädigt, und das Gewehr ist eine Waffe. [subj]Fraglich ist der Vorsatz. [ww]Vorsatz heißt Wissen und "
     "Wollen aller Tatumstände, das kennst du aus unserer Folge zu den Vorsatzformen. [wollte]Jutta wollte ein Wildschwein "
     "treffen. Dass dort ein Mensch stand, wusste sie nicht.", PS),
    # --- D § 16 Abs. 1 Satz 1 ----------------------------------------------------------------------------------------------------
    ("[p16]Genau das regelt Paragraf sechzehn Absatz eins Satz eins: Wer bei Begehung der Tat einen Umstand nicht kennt, der "
     "zum gesetzlichen Tatbestand gehört, handelt nicht vorsätzlich. [umstand]Ein solcher Umstand ist bei der Körperverletzung "
     "die andere Person, beim Totschlag der Mensch. [kennt]Jutta kennt ihn nicht, sie hält den Umriss für ein Tier. "
     "[vorsneg]Der Vorsatz entfällt, die gefährliche Körperverletzung scheidet aus. [versuch]Auch ein versuchter Totschlag "
     "scheitert, denn dafür hätte sie einen Menschen töten wollen müssen.", PS),
    # --- E Abgrenzung: error in persona ------------------------------------------------------------------------------------------
    ("[eip]Das ist auch kein bloßer error in persona. Dort verwechselt der Täter etwa einen Menschen mit einem anderen Menschen. "
     "[gleich]Weil beide Objekte gleichwertig sind, bleibt der Vorsatz bestehen. [tier]Hier aber steht ein Mensch statt eines "
     "Tieres im Gebüsch. Das ist nicht gleichwertig, deshalb greift Paragraf sechzehn.", PS),
    # --- F § 16 Abs. 1 Satz 2, § 15, § 229 ---------------------------------------------------------------------------------------
    ("[satz2]Aber Paragraf sechzehn nimmt nur den Vorsatz. Satz zwei: Die Strafbarkeit wegen fahrlässiger Begehung bleibt "
     "unberührt. [p15]Fahrlässiges Handeln ist nach Paragraf fünfzehn nur strafbar, wenn das Gesetz es ausdrücklich mit Strafe "
     "bedroht. [p229]Bei der Körperverletzung tut es das, in Paragraf zweihundertneunundzwanzig: Wer durch Fahrlässigkeit die "
     "Körperverletzung einer anderen Person verursacht, wird bestraft.", PS),
    # --- G § 229: objektive Sorgfaltspflichtverletzung ---------------------------------------------------------------------------
    ("[erfolg]Prüfen wir. Ludwig ist verletzt, und der Schuss hat das verursacht. [pflicht]Entscheidend ist die objektive "
     "Sorgfaltspflichtverletzung. [mass]Maßstab ist nach dem Bundesgerichtshof ein besonnener und gewissenhafter Mensch in der "
     "konkreten Lage und sozialen Rolle des Handelnden, hier also eine sorgfältige Jägerin. [uvv]Die Unfallverhütungsvorschrift "
     "Jagd sagt dazu: Ein Schuss darf erst abgegeben werden, wenn sich der Schütze vergewissert hat, dass niemand gefährdet "
     "wird. [ansp]Jäger nennen das: das Ziel sicher ansprechen. [verstoss]Jutta schießt in der Dämmerung auf einen Umriss, den "
     "sie nicht sicher erkannt hat. Das ist pflichtwidrig.", P),
    # --- H § 229: Vorhersehbarkeit, Zusammenhang, Rechtswidrigkeit, Schuld, Ergebnis ---------------------------------------------
    ("[vorh]Auch die objektive Vorhersehbarkeit liegt vor. Dass am Waldrand abends noch Menschen unterwegs sind und ein Schuss "
     "auf ein nicht erkanntes Ziel einen von ihnen treffen kann, ist vorhersehbar. [zus]Und hätte Jutta genau hingesehen, "
     "hätte sie Ludwig erkannt und nicht geschossen. [rw]Rechtfertigungsgründe gibt es nicht. [schuld]In der Schuld fragst du, "
     "ob sie die Gefahr auch persönlich erkennen und vermeiden konnte. Als erfahrene Jägerin konnte sie das. [erg]Ergebnis: "
     "Jutta ist strafbar wegen fahrlässiger Körperverletzung.", PS),
    # --- I Abwandlung § 222 ------------------------------------------------------------------------------------------------------
    ("[ab]Abwandlung: Stirbt Ludwig, gilt dasselbe. Kein Totschlag, aber fahrlässige Tötung nach Paragraf "
     "zweihundertzweiundzwanzig.", PS),
    # --- J Abgrenzung § 17 -------------------------------------------------------------------------------------------------------
    ("[p17]Nicht verwechseln mit dem Verbotsirrtum nach Paragraf siebzehn. Dort kennt der Täter alle Tatumstände, hält sein Tun "
     "aber für erlaubt. Dazu kommt eine eigene Folge.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst das Vorsatzdelikt und lass es im subjektiven Tatbestand an Paragraf sechzehn scheitern. "
     "[tipp2]Dann beginnst du mit einem neuen Obersatz das Fahrlässigkeitsdelikt. [tipp3]Und denk bei der fahrlässigen "
     "Körperverletzung an den Strafantrag nach Paragraf zweihundertdreißig, es sei denn, die Strafverfolgungsbehörde bejaht "
     "das besondere öffentliche Interesse.", PS),
    # --- L Prüfschema ------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]Punkt A: gefährliche Körperverletzung. [s1a]Der objektive Tatbestand ist erfüllt, [s1b]im "
     "subjektiven Tatbestand fehlt der Vorsatz nach Paragraf sechzehn Absatz eins Satz eins. [s2]Punkt B: fahrlässige "
     "Körperverletzung. [s2a]Römisch eins, Tatbestand: Erfolg, Handlung und Kausalität, [s2b]objektive "
     "Sorgfaltspflichtverletzung, [s2c]objektive Vorhersehbarkeit [s2d]und der Zusammenhang zwischen Pflichtverletzung und "
     "Erfolg. [s2e]Römisch zwei, Rechtswidrigkeit. [s2f]Römisch drei, Schuld: Konnte sie persönlich erkennen und vermeiden? "
     "[s2g]Römisch vier, der Strafantrag.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer einen Tatumstand nicht kennt, handelt nicht vorsätzlich. [m2]Paragraf sechzehn nimmt aber nur den "
     "Vorsatz. [m3]War der Irrtum bei gehöriger Sorgfalt vermeidbar, bleibt die Strafbarkeit wegen Fahrlässigkeit, soweit das "
     "Gesetz sie vorsieht.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
