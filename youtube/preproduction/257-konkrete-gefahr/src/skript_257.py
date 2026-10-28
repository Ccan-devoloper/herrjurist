"""Folge 257 · Konkrete Gefahr: Wie wahrscheinlich muss der Schaden sein? (Mi · Examenswissen · Polizei- und Ordnungsrecht ·
Schema). Beispielfall nach dem entschärften Plan-Hook (Mehrfamilienhaus statt Flüchtlingsunterkunft; kein Feuer, keine
Explosion, Mann nicht stereotyp): Samstagnachmittag vor einem Mehrfamilienhaus in Nordrhein-Westfalen. Herr Fichtner steht
mit einem offenen Benzinkanister am Hauseingang und raucht; es riecht nach Benzin. Nachbar Sebastian ruft die Polizei.
Polizistin Eilers fordert ihn auf, die Zigarette auszumachen und den Kanister zu schließen. Fichtner: Er wolle nur den
Rasenmäher auftanken.
Aufbau (Schema): Generalklausel (Beispiel NRW, Wortlaut § 8 Abs. 1 PolG NRW; Schutzgüter nur Verweis Folge 213) →
Legaldefinition (Wortlautkarte § 2 Nr. 1 NPOG; BVerfGE 141, 220 Rn. 111) → 1. Sachlage im Einzelfall, 2. Schaden für ein
Schutzgut, 3. absehbare Zeit → 4. hinreichende Wahrscheinlichkeit: Je-desto-Formel (BVerwG 3 C 16.11 Rn. 32), Grenze
(BVerfGE 115, 320 Rn. 136) → 5. Prognose ex ante auf Tatsachen (BVerfGE 115, 320 Rn. 145; OVG NRW 7 A 1717/01; VG Köln
20 K 6403/14 Rn. 45; Anscheinsgefahr nur Verweis Folge 052) → Ergebnis (§§ 4 Abs. 1, 2 Abs. 1 PolG NRW) → Abgrenzung
gegenwärtige, erhebliche, dringende, abstrakte Gefahr (§ 2 Nr. 2, 3, 4, 6 NPOG) → Gegenfall und abstrakte Gefahr
(BVerwG 6 C 44.16 Rn. 23) → Länder-Overlay (NRW, Brandenburg, Niedersachsen, Sachsen) → Klausurtipp → Schema → Merksatz.
Belege: ../RECHTSSTAND.md. Namen (eindeutig deutsche Aussprache, nicht vergeben, eingetragen als „257: Fichtner, Eilers,
Sebastian“): Herr Fichtner (helmut, Mann, älter), Polizistin Eilers (julia, Frau, jung), Nachbar Sebastian (niklas, Mann,
jung); ela_froh nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Fichtner": "helmut", "Eilers": "julia", "Sebastian": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: vor dem Mehrfamilienhaus -------------------------------------------------------------------------------
    ("[fall]Samstagnachmittag vor einem Mehrfamilienhaus. [kanister]Herr Fichtner steht mit einem Benzinkanister am "
     "Hauseingang. [offen]Der Deckel ist offen, [rauch]und Herr Fichtner raucht. [nachbar]Sein Nachbar Sebastian greift "
     "zum Handy.", 0.3),
    ("[se1]Polizei? Vor unserem Haus raucht ein Mann neben einem offenen Benzinkanister. Bitte kommen Sie!", 0.3, "Sebastian"),
    ("[polizei]Kurz darauf ist Polizistin Eilers da. [geruch]Es riecht nach Benzin.", 0.3),
    ("[ei1]Machen Sie bitte sofort die Zigarette aus und schließen Sie den Kanister.", 0.3, "Eilers"),
    ("[fi1]Ich will doch nur den Rasenmäher auftanken. Da passiert schon nichts.", 0.4, "Fichtner"),
    ("[frage]Durfte Polizistin Eilers das verlangen? [frage2]Liegt eine konkrete Gefahr vor, und wie wahrscheinlich muss "
     "der Schaden dafür sein?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Generalklausel (Wortlautkarte § 8 Abs. 1 PolG NRW) ----------------------------------------------------------
    ("[egl]Für die Aufforderung, die Zigarette auszumachen, gibt es keine Standardmaßnahme. Grundlage ist die "
     "Generalklausel. [land]Polizeirecht ist Landesrecht, die Dogmatik ist aber bundesweit gleich. [wl8]Beispiel "
     "Nordrhein-Westfalen, Paragraf acht Absatz eins: Die Polizei kann die notwendigen Maßnahmen treffen, um eine im "
     "einzelnen Falle bestehende, konkrete Gefahr für die öffentliche Sicherheit oder Ordnung abzuwehren. [schutz]Welche "
     "Schutzgüter dazugehören, zeigt unsere Folge zweihundertdreizehn. [kern]Hier geht es um die konkrete Gefahr.", PS),
    # --- D Legaldefinition (Wortlautkarte § 2 Nr. 1 NPOG) ---------------------------------------------------------------
    ("[def]Niedersachsen hat sie ins Gesetz geschrieben, Paragraf zwei Nummer eins: [defa]eine Sachlage, bei der im "
     "einzelnen Fall die hinreichende Wahrscheinlichkeit besteht, [defb]dass in absehbarer Zeit [defc]ein Schaden für die "
     "öffentliche Sicherheit oder Ordnung eintreten wird. [bverfg]Das Bundesverfassungsgericht beschreibt es genauso: Bei "
     "ungehindertem Ablauf des Geschehens droht die Verletzung eines Schutzguts.", PS),
    # --- E 1.–3. Merkmale am Fall ----------------------------------------------------------------------------------------
    ("[e1]Erstens, eine Sachlage im Einzelfall: dieser Kanister, diese Zigarette, dieses Haus. [e2]Zweitens, der drohende "
     "Schaden: Ein Brand würde Leben und Gesundheit der Bewohner treffen und das Haus. [e3]Drittens, in absehbarer Zeit: "
     "Das kann jeden Moment geschehen.", PS),
    # --- F 4. Hinreichende Wahrscheinlichkeit: Je-desto-Formel -------------------------------------------------------------
    ("[jd]Viertens, die Kernfrage: Wie wahrscheinlich muss der Schaden sein? [jdf]Hier gilt die Je-desto-Formel. Das "
     "Bundesverwaltungsgericht formuliert: An die Wahrscheinlichkeit des Schadenseintritts sind umso geringere Anforderungen "
     "zu stellen, je größer und folgenschwerer der möglicherweise eintretende Schaden ist. [jdk]Umgekehrt: Droht nur ein "
     "kleiner Schaden, muss er umso wahrscheinlicher sein.", P),
    ("[jdfall]Bei Herrn Fichtner droht ein Brand in einem bewohnten Haus, also ein sehr großer Schaden. [jdw]Ein offener "
     "Kanister, Benzingeruch und Glut direkt daneben: Ein Brand ist nicht sicher, aber ernsthaft möglich. Das genügt hier. "
     "[grenze]Aber Vorsicht: Selbst bei höchstem Gewicht der drohenden Beeinträchtigung kann auf eine hinreichende "
     "Wahrscheinlichkeit nicht verzichtet werden, sagt das Bundesverfassungsgericht.", PS),
    # --- G 5. Prognose ex ante -------------------------------------------------------------------------------------------
    ("[exante]Fünftens, die Prognose. Maßgeblich ist der Zeitpunkt des Einschreitens, ex ante, aus Sicht eines "
     "besonnenen und sachkundigen Amtswalters. [tats]Die Prognose muss sich auf Tatsachen stützen; bloße Vermutungen "
     "reichen nicht. [eisieht]Eilers sieht den offenen Kanister, riecht das Benzin und sieht die Glut. Das sind Tatsachen. "
     "[wasser]Wäre im Kanister in Wahrheit nur Wasser gewesen, änderte das nichts, solange alles nach Benzin aussah und "
     "roch. Das wäre eine Anscheinsgefahr; mehr dazu in Folge zweiundfünfzig.", P),
    ("[erg]Ergebnis: Es liegt eine konkrete Gefahr vor. [stoerer]Herr Fichtner verursacht sie selbst, [mild]und die "
     "Aufforderung ist ein mildes Mittel. [darf]Eilers durfte verlangen, die Zigarette auszumachen und den Kanister zu "
     "schließen.", PS),
    # --- H Abgrenzung ------------------------------------------------------------------------------------------------------
    ("[abgr]Grenze die konkrete Gefahr von ihren Verwandten ab; Niedersachsen definiert auch sie. [ab1]Gegenwärtig ist "
     "eine Gefahr, wenn die Einwirkung schon begonnen hat oder unmittelbar oder in allernächster Zeit mit an Sicherheit "
     "grenzender Wahrscheinlichkeit bevorsteht. [ab2]Erheblich ist eine Gefahr für ein bedeutsames Rechtsgut, etwa Leben, "
     "Gesundheit oder Freiheit. [ab3]Dringend ist eine Gefahr, die im Hinblick auf das Ausmaß des Schadens und die "
     "Wahrscheinlichkeit erhöht ist. [ab4]Abstrakt ist eine nach allgemeiner Lebenserfahrung mögliche Sachlage, die im "
     "Fall ihres Eintritts eine Gefahr darstellt.", P),
    ("[abfall]Bei Herrn Fichtner sind Leben und Gesundheit bedroht; die Gefahr ist also auch erheblich. [abgen]Ob sie "
     "sogar gegenwärtig ist, musst du nur prüfen, wenn die Befugnisnorm das verlangt.", PS),
    # --- I Gegenfall und abstrakte Gefahr ----------------------------------------------------------------------------------
    ("[gegen]Anders der Gegenfall: Der Kanister ist fest verschlossen und liegt im Kofferraum. [gegen2]Herr Fichtner raucht "
     "auf der anderen Straßenseite. [gneg]Ein Brand ist dann praktisch ausgeschlossen: keine konkrete Gefahr. "
     "[gabs]Ob Rauchen beim Umgang mit Benzin allgemein gefährlich ist, ist dagegen eine Frage der abstrakten Gefahr. "
     "[gabs2]Sie betrifft gleichgelagerte Fälle und wird mit Verordnungen bekämpft, die auch gelten, wenn im Einzelfall keine konkrete "
     "Gefahr besteht.", PS),
    # --- J Länder-Overlay --------------------------------------------------------------------------------------------------
    ("[tab]Die Normen im Überblick. [tnrw]Nordrhein-Westfalen [tbb]und Brandenburg schreiben die konkrete Gefahr direkt in "
     "die Generalklausel, Paragraf acht und Paragraf zehn. [tni]Niedersachsen [tsn]und Sachsen sprechen dort nur von einer "
     "Gefahr und definieren sie in einem eigenen Paragrafen. [tdein]In deinem Land kann die Nummer anders sein; die Prüfung "
     "bleibt gleich.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schreib nicht nur, es bestehe eine Gefahr. [tipp1]Gib die Definition an und subsumiere jedes "
     "Merkmal am Sachverhalt. [tipp2]Bei der Wahrscheinlichkeit gehört die Je-desto-Formel in die Begründung, mit dem "
     "konkret drohenden Schaden. [tipp3]Und beurteile alles ex ante, nicht mit dem Wissen von hinterher.", PS),
    # --- L Schema ------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die konkrete Gefahr. [s1]Erstens: Sachlage im Einzelfall. [s2]Zweitens: drohender Schaden für "
     "ein Schutzgut. [s3]Drittens: in absehbarer Zeit. [s4]Viertens: hinreichende Wahrscheinlichkeit, nach der "
     "Je-desto-Formel. [s5]Fünftens: Prognose ex ante, auf Tatsachen gestützt. [s6]Danach: Verlangt die Norm eine "
     "besondere Gefahr, etwa eine gegenwärtige oder erhebliche?", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Je größer der drohende Schaden, desto geringer die nötige Wahrscheinlichkeit. [m2]Ganz verzichten "
     "darf man auf sie aber nie, und geurteilt wird ex ante, auf der Grundlage von Tatsachen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
