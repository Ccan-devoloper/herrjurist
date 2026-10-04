"""Folge 158 · § 823 II BGB: Schutzgesetzverletzung – das Prüfungsschema (Mi · Examenswissen · Deliktsrecht, Format Schema).
Beispielfall nach dem Plan-Hook („Der Nachbar fährt ohne Führerschein und beschädigt beim Rangieren dein Auto“): Hiltrud
hat ihr Auto ordnungsgemäß am Straßenrand einer öffentlichen Wohnstraße vor dem Haus geparkt. Ihr Nachbar Burkhard hat
keine Fahrerlaubnis (nie eine Prüfung gemacht), ist aber Halter seines eigenen Autos. Er setzt rückwärts aus seiner
Einfahrt auf die Straße, verschätzt sich beim Rangieren und streift das Auto von Hiltrud (langer Kratzer am hinteren
Kotflügel, kein Aufprall). Reparatur 900 €.
ABWEICHUNG vom Plan-Hook (offengelegt in ../RECHTSSTAND.md): Der Kratzer entsteht auf der öffentlichen Straße, nicht in der
Einfahrt. Eine Fahrerlaubnis braucht nach § 2 Abs. 1 S. 1 StVG nur, wer „auf öffentlichen Straßen“ ein Kraftfahrzeug führt;
in einer privaten Einfahrt allein wäre § 21 StVG regelmäßig nicht verwirklicht (im Klausurtipp ein Satz).
Prüfung: § 823 Abs. 2 S. 1, 2 BGB (Wortlautkarte, wörtlich) → Aufbau in sechs Schritten → I. Schutzgesetz: Art. 2 EGBGB
(Wortlautkarte, jede Rechtsnorm), BGH-Formel (VI ZR 307/18 Rn. 12; VI ZR 110/21 Rn. 9), kein bloßer Reflex, Klassiker
§ 223 StGB (IX ZR 41/10 Rn. 13) und § 263 StGB (VI ZR 4/11 Rn. 9, 13); Parallele Schutznormtheorie (Folge 110) ein Satz;
§ 21 Abs. 1 Nr. 1 StVG (Wortlautkarte), § 2 Abs. 1, Abs. 2 S. 1 Nr. 5 StVG, Subsumtion (Folgerung, kein BGH-Volltext zu
§ 21 StVG als Schutzgesetz gefunden) → II. Schutzbereich persönlich/sachlich (VI ZR 307/18 Rn. 14), offen formulierte
Schutzzweckfrage → III. Verstoß → IV. Rechtswidrigkeit (indiziert) → V. Verschulden: subjektiver Tatbestand des
Schutzgesetzes maßgebend (VIa ZR 335/21 Rn. 38), Satz 2 (Rn. 37) → VI. Schaden, Kausalität, §§ 249 ff. BGB → Vorteil:
reiner Vermögensschaden, § 263 StGB (VI ZR 4/11 Rn. 9) → Lösung, daneben § 823 Abs. 1 und § 7 StVG (Verweis Folge 149, ein
Satz) → Klausurtipp (Lexi) → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Hiltrud, Burkhard
(nie im Genitiv). Stimmen: Hiltrud laura_ruhig, Burkhard william. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; StVG und EGBGB ausgeschrieben (synth_el kennt die Abkürzungen nicht)."""

P, PS = 0.3, 0.5

STIMMEN = {"Hiltrud": "laura_ruhig", "Burkhard": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Wohnstraße ----------------------------------------------------------------------------------------
    ("[fall]Samstagmittag in einer ruhigen Wohnstraße. [park]Hiltrud hat ihr Auto am Straßenrand vor dem Haus geparkt. "
     "[burk]Ihr Nachbar Burkhard will seinen eigenen Wagen umparken. [ohne]Eine Fahrerlaubnis hat er nicht, die Prüfung hat "
     "er nie gemacht. [rang]Er setzt rückwärts aus seiner Einfahrt auf die Straße, verschätzt sich beim Rangieren [kratz]und "
     "streift das Auto von Hiltrud. [schaden]Am hinteren Kotflügel bleibt ein langer Kratzer.", P),
    ("[h1]Burkhard, du hast doch gar keinen Führerschein!", P, "Hiltrud"),
    ("[b1]Ich wollte doch nur kurz umparken.", P, "Burkhard"),
    # --- A2 Fall: die Frage ----------------------------------------------------------------------------------------------
    ("[fe]Rechtlich geht es um die Fahrerlaubnis; der Führerschein ist nur die Bescheinigung darüber. [rep]Die Reparatur "
     "kostet neunhundert Euro. [frage]Hilft es Hiltrud, dass Burkhard ohne Fahrerlaubnis gefahren ist?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Die Norm: § 823 Abs. 2 BGB ------------------------------------------------------------------------------------
    ("[norm]Die Antwort gibt Paragraf achthundertdreiundzwanzig Absatz zwei BGB: Die gleiche Verpflichtung trifft "
     "denjenigen, welcher gegen ein den Schutz eines anderen bezweckendes Gesetz verstößt. [s2]Satz zwei: Ist nach dem Inhalt "
     "des Gesetzes ein Verstoß gegen dieses auch ohne Verschulden möglich, so tritt die Ersatzpflicht nur im Falle des "
     "Verschuldens ein. [gleich]Gemeint ist Schadensersatz wie in Absatz eins; dessen Schema zeigt das Video zum "
     "Deliktsrecht.", P),
    ("[aufbau]Wir prüfen in sechs Schritten: [a1]Schutzgesetz, [a2]Schutzbereich, [a3]Verstoß, [a4]Rechtswidrigkeit, "
     "[a5]Verschulden [a6]und Schaden.", PS),
    # --- D I. Schutzgesetz -----------------------------------------------------------------------------------------------
    ("[sg]Erstens: das Schutzgesetz. [eg]Gesetz ist nach Artikel zwei des Einführungsgesetzes zum BGB jede Rechtsnorm, also "
     "zum Beispiel auch eine Verordnung. [formel]Ein Schutzgesetz ist sie nach dem Bundesgerichtshof, wenn sie zumindest auch "
     "dazu dienen soll, den Einzelnen oder einzelne Personenkreise gegen die Verletzung eines bestimmten Rechtsguts zu "
     "schützen. [allg]Dabei schadet es nicht, wenn die Norm in erster Linie die Allgemeinheit im Blick hat. [reflex]Ein bloßer Reflex "
     "reicht aber nicht: Schützt eine Vorschrift nur die Allgemeinheit oder die Ordnung, ist sie kein "
     "Schutzgesetz.", P),
    ("[klass]Klassiker sind Strafgesetze wie die Körperverletzung und der Betrug. [snt]Ähnlich fragt die Schutznormtheorie im "
     "Öffentlichen Recht; dort geht es aber um Rechte gegen den Staat, nicht um Schadensersatz.", PS),
    # --- E § 21 StVG als Schutzgesetz -------------------------------------------------------------------------------------
    ("[p21]Im Fall kommt Paragraf einundzwanzig Straßenverkehrsgesetz in Betracht. [p21a]Bestraft wird, wer ein "
     "Kraftfahrzeug führt, obwohl er die dazu erforderliche Fahrerlaubnis nicht hat. [p2]Die braucht nach Paragraf zwei, wer "
     "auf öffentlichen Straßen ein Kraftfahrzeug führt, [p2b]und erteilt wird sie nur dem, der seine Befähigung in einer "
     "Prüfung nachgewiesen hat. [zweck]Die Pflicht schützt die Allgemeinheit, zumindest aber auch jeden anderen im "
     "Straßenverkehr vor Fahrern, deren Können niemand geprüft hat. [sgja]Paragraf einundzwanzig ist damit ein "
     "Schutzgesetz.", PS),
    # --- F II. Schutzbereich ---------------------------------------------------------------------------------------------
    ("[sb]Zweitens: der Schutzbereich. [pers]Persönlich muss der Geschädigte zu dem Kreis gehören, den die Norm schützen "
     "will. [pers2]Das sind die anderen im Straßenverkehr, also auch Hiltrud mit ihrem Auto auf der Straße. [sach]Sachlich "
     "muss sich im Schaden gerade die Gefahr verwirklicht haben, vor der die Norm schützen soll. [sach2]Burkhard hat sich "
     "beim Rangieren verschätzt. Genau davor soll die Prüfung schützen: vor Fahrern, die ihr Auto nicht sicher "
     "beherrschen. [offen]Ob gerade das fehlende Können den Schaden verursacht haben muss, ist eine Frage dieses "
     "Schutzzwecks; hier kommt es darauf nicht an.", PS),
    # --- G III. Verstoß, IV. Rechtswidrigkeit ----------------------------------------------------------------------------
    ("[verst]Drittens: der Verstoß. [verst2]Burkhard hat auf der öffentlichen Straße ein Auto geführt, ohne die "
     "erforderliche Fahrerlaubnis zu haben. [rw]Viertens: Die Rechtswidrigkeit ist durch den Verstoß indiziert, "
     "Rechtfertigungsgründe gibt es nicht.", PS),
    # --- H V. Verschulden ------------------------------------------------------------------------------------------------
    ("[vs]Fünftens: das Verschulden. [vs1]Bezugspunkt ist der Verstoß gegen das Schutzgesetz. [vs2]Bei einem Strafgesetz "
     "gilt dessen subjektiver Tatbestand; verlangt es Vorsatz, dann im Sinne des Strafrechts. [vs3]Burkhard wusste, dass er keine "
     "Fahrerlaubnis hat: Er handelte vorsätzlich. [vs4]Den Kratzer muss er dafür nicht vorhergesehen haben, denn Paragraf "
     "einundzwanzig verlangt keinen Schaden. [vs5]Und nach Satz zwei gilt: Kann man ein Schutzgesetz auch ohne Verschulden "
     "verletzen, haftet trotzdem nur, wer schuldhaft handelt.", PS),
    # --- I VI. Schaden, Kausalität, Rechtsfolge; Vorteil ------------------------------------------------------------------
    ("[sd]Sechstens: Schaden und Kausalität. [kaus]Ohne die verbotene Fahrt hätte das Auto von Hiltrud keinen Kratzer. "
     "[rf]Rechtsfolge nach den Paragrafen zweihundertneunundvierzig folgende: Hiltrud kann den für die "
     "Reparatur erforderlichen Geldbetrag verlangen.", P),
    ("[vort]Warum lohnt Absatz zwei? [vt1]Absatz eins schützt bestimmte Rechtsgüter wie das Eigentum, nicht das Vermögen "
     "als solches. [vt2]Über Absatz zwei ist auch ein reiner Vermögensschaden ersatzfähig, wenn das Schutzgesetz ihn "
     "erfasst, etwa beim Betrug nach Paragraf zweihundertdreiundsechzig Strafgesetzbuch.", PS),
    # --- J Lösung --------------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Hiltrud. [l1]Burkhard muss ihr aus Paragraf achthundertdreiundzwanzig Absatz zwei in Verbindung mit "
     "Paragraf einundzwanzig Straßenverkehrsgesetz die neunhundert Euro ersetzen. [l2]Daneben greift Absatz eins, denn er hat "
     "ihr Eigentum fahrlässig verletzt. [l3]Und weil Burkhard Halter ist, haftet er auch nach Paragraf sieben "
     "Straßenverkehrsgesetz, sogar ohne Verschulden, siehe das Video zur Halterhaftung.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Zitiere immer das konkrete Schutzgesetz, [tp1]also Paragraf achthundertdreiundzwanzig Absatz zwei "
     "in Verbindung mit Paragraf einundzwanzig. [tp2]Dann prüfst du das Schutzgesetz inzident, mit objektivem und "
     "subjektivem Tatbestand. [tp3]Und achte auf den Ort: Wer nur in seiner privaten Einfahrt rangiert, fährt in der Regel "
     "nicht auf einer öffentlichen Straße und braucht dafür keine Fahrerlaubnis.", PS),
    # --- L Prüfschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [c1]Römisch eins: Schutzgesetz, eine Rechtsnorm, die zumindest auch den Einzelnen schützt. "
     "[c2]Römisch zwei: Schutzbereich, persönlich und sachlich. [c3]Römisch drei: Verstoß. [c4]Römisch vier: "
     "Rechtswidrigkeit. [c5]Römisch fünf: Verschulden, bezogen auf den Verstoß. [c6]Römisch sechs: Schaden und "
     "Kausalität.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf achthundertdreiundzwanzig Absatz zwei macht aus einem Gesetz, das den Einzelnen schützt, "
     "einen Anspruch auf Schadensersatz. [m2]Das Verschulden prüfst du am Verstoß gegen dieses Gesetz.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
