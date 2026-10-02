"""Folge 042 · Gefährliche Körperverletzung Schema: § 224 StGB mit allen 5 Varianten (Fr · Klausurpraxis, Format Schema).
Fall auf einem Dorffest: Tobias stößt beim Tanzen Reinhards Bierglas um; Reinhard stößt ihn zu Boden und tritt ihm mit dem
schweren Arbeitsstiefel gegen den Kopf. Wortlaut § 224 I, II; Aufbau Grundtatbestand § 223 → Qualifikation § 224 → Vorsatz;
Nr. 2 (BGH 1 StR 171/18 Rn. 6; Schuh: BGH 6 StR 298/22 Rn. 4), Nr. 1 (BGHSt 51, 18 = 4 StR 536/05 Rn. 17),
Nr. 3 (BGH 3 StR 386/20 Rn. 4; 3 StR 146/12 Rn. 3), Nr. 4 (BGHSt 47, 383 = 5 StR 210/02 Rn. 10 f.),
Nr. 5 (BGH 1 StR 344/16 Rn. 12; 2 StR 206/21 Rn. 4), Vorsatz (BGH 3 StR 386/20 Rn. 12; 4 StR 551/12 Rn. 24),
Versuch § 224 II, kein Strafantrag (§ 230); Klausurtipp, Schema, Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.7

STIMMEN = {"Reinhard": "helmut", "Tobias": "timo", "Anja": "ela_warm"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Dorffest ------------------------------------------------------------------------------------------------
    ("[fall]Samstagnachmittag auf dem Dorffest. [tobias]Tobias tanzt vor dem Festzelt [glas]und stößt dabei aus Versehen "
     "das Bierglas von Reinhard um. [reinhard]Reinhard, Mitte fünfzig, ist außer sich.", 0.3),
    ("[r1]Das wirst du bereuen!", 0.3, "Reinhard"),
    ("[stoss]Er stößt Tobias zu Boden [tritt]und tritt ihm mit seinem schweren Arbeitsstiefel gegen den Kopf. [beule]Tobias "
     "bekommt eine dicke Beule.", 0.3),
    ("[t1]Mit dem Stiefel? Das ist doch gefährlich!", 0.3, "Tobias"),
    ("[frage]Gefährlich auch im Sinne des Gesetzes? [frage2]Wann wird aus der Körperverletzung eine gefährliche, und wie "
     "prüfst du das?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall mit allen Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 224 ------------------------------------------------------------------------------------------------
    ("[p224]Maßstab ist Paragraf zweihundertvierundzwanzig, die gefährliche Körperverletzung. [p224w]Sie verlangt eine "
     "Körperverletzung, begangen auf eine von fünf Arten: [n1]durch Beibringung von Gift oder anderen gesundheitsschädlichen "
     "Stoffen, [n2]mittels einer Waffe oder eines anderen gefährlichen Werkzeugs, [n3]mittels eines hinterlistigen "
     "Überfalls, [n4]mit einem anderen Beteiligten gemeinschaftlich [n5]oder mittels einer das Leben gefährdenden "
     "Behandlung. [straf]Die Strafe: sechs Monate bis zehn Jahre. [abs2]Und nach Absatz zwei ist der Versuch strafbar.", PS),
    # --- D Aufbau ----------------------------------------------------------------------------------------------------------
    ("[aufbau]Paragraf zweihundertvierundzwanzig ist eine Qualifikation. [grund]Erst prüfst du den Grundtatbestand, "
     "Paragraf zweihundertdreiundzwanzig, [dann]dann mindestens eine der fünf Nummern.", PS),
    # --- E Grundfall: § 223 und Nr. 2 -------------------------------------------------------------------------------------
    ("[gf]Zum Grundfall. [gf223]Der Tritt ist eine körperliche Misshandlung, die Beule eine "
     "Gesundheitsschädigung: [gf_ok]Paragraf zweihundertdreiundzwanzig liegt vor. [nr2]In Betracht kommt Nummer zwei, das "
     "gefährliche Werkzeug. [wdef]Nach dem Bundesgerichtshof ist das jeder bewegliche Gegenstand, der nach seiner objektiven "
     "Beschaffenheit [wart]und der Art seiner Benutzung im konkreten Einzelfall [werh]geeignet ist, erhebliche "
     "Körperverletzungen herbeizuführen.", PS),
    ("[schuh]Und der Schuh am Fuß? [schuh2]Es kommt auf den Einzelfall an: auf die Beschaffenheit des Schuhs, [heftig]die "
     "Heftigkeit des Tritts [teil]und den getroffenen Körperteil. [kopf]Ein Straßenschuh von üblicher Beschaffenheit ist "
     "regelmäßig ein gefährliches Werkzeug, wenn damit gegen den Kopf getreten wird. [stiefel]Reinhard trägt sogar einen "
     "schweren Arbeitsstiefel. [nr2_ok]Nummer zwei ist erfüllt. [nr5gf]Ob der Tritt auch das Leben gefährdet, prüfst "
     "du bei Nummer fünf.", PS),
    # --- F Nr. 1: Gift oder gesundheitsschädliche Stoffe -----------------------------------------------------------------
    ("[nr1]Variante eins: Reinhard mischt Tobias heimlich eine hohe Dosis eines starken Schlafmittels ins Glas. "
     "[zus]Tobias bricht zusammen und muss im Krankenhaus behandelt werden. [stoff]Nach dem Bundesgerichtshof genügt jeder "
     "Stoff, der nach seiner Art und dem konkreten Einsatz zur erheblichen Gesundheitsschädigung geeignet ist. [alltag]Das "
     "kann sogar ein Stoff des täglichen Bedarfs sein, etwa Kochsalz in großer Menge. [nr1_ok]Die hohe Dosis Schlafmittel "
     "ist dazu geeignet: Nummer eins.", PS),
    # --- G Nr. 3: hinterlistiger Überfall --------------------------------------------------------------------------------
    ("[nr3]Variante zwei: Reinhard geht lächelnd auf Tobias zu und reicht ihm die Hand.", 0.3),
    ("[r2]Komm, vertragen wir uns wieder.", 0.3, "Reinhard"),
    ("[schlag]Dann schlägt er unvermittelt zu. [hdef]Hinterlistig ist ein Überfall nach dem Bundesgerichtshof, wenn der "
     "Täter planmäßig in einer auf Verdeckung der wahren Absicht berechneten Weise vorgeht, [hzweck]um dem Opfer die Abwehr "
     "zu erschweren. [fried]Typisch ist vorgetäuschte Friedfertigkeit, [nr3_ok]genau wie bei Reinhard: Nummer drei. "
     "[hinten]Greift er Tobias dagegen nur überraschend von hinten an, [hinten_no]genügt das bloße Ausnutzen des "
     "Überraschungsmoments nicht.", PS),
    # --- H Nr. 4: gemeinschaftlich ---------------------------------------------------------------------------------------
    ("[nr4]Variante drei: Reinhards Tochter Anja stellt sich Tobias in den Weg.", 0.3),
    ("[a1]Hier kommst du nicht vorbei!", 0.3, "Anja"),
    ("[zuschl]Während Reinhard zuschlägt, kann Tobias nicht ausweichen. [selbst]Anja selbst schlägt nicht. [geh]Nach dem "
     "Bundesgerichtshof genügt auch ein Gehilfe als anderer Beteiligter. [vstk]Gemeinschaftlich ist die Tat jedenfalls, "
     "wenn der anwesende Gehilfe den Angriff bewusst so verstärkt, dass sich die Lage des Opfers "
     "verschlechtert, [flucht]etwa weil es schlechter ausweichen oder fliehen kann. [nr4_ok]So ist es hier: Nummer vier.", PS),
    # --- I Nr. 5: das Leben gefährdende Behandlung -----------------------------------------------------------------------
    ("[nr5]Variante vier: Reinhard drückt Tobias kräftig und lange den Hals zu. [keine]In Lebensgefahr gerät "
     "Tobias nicht. "
     "[ldef]Das muss er nach dem Bundesgerichtshof auch nicht. [abstr]Es genügt, dass die Behandlung abstrakt geeignet ist, "
     "das Leben zu gefährden. [dauer]Beim Würgen kommt es auf Dauer und Stärke an, [griff]nicht jeder Griff an den Hals "
     "reicht. [nr5_ok]Reinhards kräftiges und langes Würgen ist dazu geeignet: Nummer fünf.", PS),
    # --- J Vorsatz -------------------------------------------------------------------------------------------------------
    ("[vz]Dann der subjektive Tatbestand. [vz1]Reinhard braucht Vorsatz bezüglich der Körperverletzung [vz2]und der "
     "Qualifikation. [umst]Dafür genügt, dass er die Umstände kennt, aus denen sich die Gefährlichkeit ergibt, [stief]im "
     "Grundfall also: schwerer Stiefel, Tritt gegen den Kopf. [bezw]Die Gefährlichkeit bezwecken muss er nicht.", PS),
    # --- K Versuch -------------------------------------------------------------------------------------------------------
    ("[vers]Variante fünf: Reinhard holt mit dem Stiefel zum Tritt gegen den Kopf aus, [weg]doch Tobias rollt sich weg. "
     "[tatent]Reinhard wollte so treten [ansetz]und hat nach seiner Vorstellung unmittelbar angesetzt. [vers_ok]Die "
     "versuchte gefährliche Körperverletzung ist nach Absatz zwei strafbar.", PS),
    # --- L Ergebnis ------------------------------------------------------------------------------------------------------
    ("[erg]Zurück zum Grundfall: [rw]Rechtfertigungs- und Entschuldigungsgründe fehlen. [erg2]Reinhard hat "
     "sich wegen gefährlicher Körperverletzung strafbar gemacht. [antrag]Einen Strafantrag braucht es dafür nicht: Paragraf "
     "zweihundertdreißig nennt nur die einfache und die fahrlässige Körperverletzung.", PS),
    # --- M Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Paragrafen zweihundertdreiundzwanzig und zweihundertvierundzwanzig zusammen, erst den "
     "Grundtatbestand, dann die Nummern. [tipp2]Sprich jede Nummer an, die der Sachverhalt nahelegt; oft sind es mehrere. "
     "[tipp3]Und beim Schuh begründest du konkret: welcher Schuh, wie heftig, welcher Körperteil.", PS),
    # --- N Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k_i]Römisch eins: Tatbestand. [k1]Objektiv: [k1a]die Körperverletzung, [k1b]dann die Qualifikation: [kq1]Gift, [kq2]gefährliches Werkzeug, [kq3]hinterlistiger "
     "Überfall, [kq4]gemeinschaftliche Begehung [kq5]oder lebensgefährdende Behandlung. [k2]Subjektiv: Vorsatz, auch "
     "bezüglich der Qualifikation. [k_ii]Römisch zwei: Rechtswidrigkeit. [k_iii]Römisch drei: Schuld. [k_v]Scheitert die "
     "Vollendung, prüfst du den Versuch nach Absatz zwei.", PS),
    # --- O Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf zweihundertvierundzwanzig baut auf der Körperverletzung auf. [m2]Jede der fünf Nummern "
     "beschreibt eine Begehungsweise, die die Tat abstrakt gefährlicher macht. [m3]Und der Vorsatz muss diese gefährlichen Umstände "
     "umfassen.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
