"""Folge 249 · Gefahr im Verzug: Durchsuchung ohne Richter? (Art. 13 II GG) (Fr · Klausurpraxis · Grundrechte · Klassiker-Fall).
Fall nach dem Plan-Hook („Polizisten klingeln am Sonntagabend und wollen sofort deine Wohnung durchsuchen – ein Richter sei
nicht erreichbar“): Sonntag, 19 Uhr. Kommissar Bader und Kommissarin Ebner (Ermittlungspersonen der Staatsanwaltschaft)
klingeln bei Ines, Grafikerin mit Atelier neben der Wohnung. Um 15 Uhr hatte ein Konzertbesucher angezeigt, dass seine online
gekauften Eintrittskarten gefälscht sind; bezahlt hatte er auf ein Konto von Ines. Beim Bereitschaftsdienst des Amtsgerichts
hat niemand angerufen, obwohl die Bereitschaftsrichterin erreichbar war; nichts deutet darauf hin, dass Ines von der Anzeige
weiß. Ines widerspricht; die beiden durchsuchen trotzdem Wohnung und Atelier und finden einen Stapel Konzertkarten.
Prüfung als Grundrechtsfall: 1. Schutzbereich (Wortlautkarte Art. 13 Abs. 1 GG; Wohnung = räumliche Sphäre des Privatlebens,
weit, auch Geschäftsräume: BVerfG 2 BvR 460/25 Rn. 28, BVerfGE 109, 279 Rn. 142) und Eingriff (Durchsuchungsbegriff
2 BvR 460/25 Rn. 36; schwerwiegend BVerfGE 103, 142 Rn. 26) → 2. Rechtfertigung, Wortlautkarte Art. 13 Abs. 2 GG
(Regel/Ausnahme Rn. 31, vorbeugende neutrale Kontrolle Rn. 27, eng Rn. 32) → 3. Anforderungen (Rn. 34, 38, 39, 40, 54)
und Bereitschaftsdienst (Rn. 40; BVerfGE 151, 67 Rn. 56, 58) → 4. § 105 Abs. 1 S. 1 StPO (Wortlautkarte), § 102 StPO,
Verweis Folge 151 → 5. Lösung (BVerfGE 139, 245 Rn. 71: mündliche Entscheidung in einfachen Fällen), Gegenfall, Verwertung
nur ein Satz (2 BvR 2225/08 Rn. 16 f.; Verweis Folge 221) → Klausurtipp (Rn. 44 f.; Abgrenzung Betreten, 2 BvR 460/25
Rn. 34 ff.) → Schema → Merksatz.
Belege: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Liste des
Koordinators, namen_reserviert.txt, grep über youtube/): Ines, Bader, Ebner (nie im Genitiv). Stimmen nur aus dem Pool:
Ines lucy (Frau, jung), Bader stephan (Mann, mittel); Ebner und die Bereitschaftsrichterin sprechen nicht; christian und
hilde nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ines": "lucy", "Bader": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Sonntag, 19 Uhr, an der Wohnungstür ------------------------------------------------------------------
    ("[fall]Sonntag, neunzehn Uhr. [klingel]Bei Ines klingelt es. [tuer]Vor der Tür stehen Kommissar Bader und "
     "Kommissarin Ebner.", 0.3),
    ("[b1]Wir müssen sofort Ihre Wohnung und Ihr Atelier durchsuchen. Ein Richter ist am Sonntagabend nicht zu "
     "erreichen.", 0.3, "Bader"),
    ("[i1]Ohne Beschluss? Dann rufen Sie doch den Bereitschaftsdienst an!", 0.3, "Ines"),
    ("[b2]Das dauert zu lange. Bis dahin haben Sie alles verschwinden lassen.", 0.4, "Bader"),
    # --- A2 Fall: was vorher geschah ----------------------------------------------------------------------------------
    ("[vorher]Was vorher geschah: [anz]Um fünfzehn Uhr hatte ein Konzertbesucher angezeigt, dass seine Eintrittskarten "
     "gefälscht sind. [konto]Gekauft hatte er sie online, bezahlt auf ein Konto von Ines. [atelier]Ines ist Grafikerin und "
     "arbeitet in einem Atelier gleich neben ihrer Wohnung. [ruf]Niemand hat versucht, den Bereitschaftsdienst des "
     "Amtsgerichts zu erreichen, [richterin]obwohl die Richterin an diesem Abend erreichbar war. [ahnt]Und nichts deutet darauf hin, dass "
     "Ines von der Anzeige weiß.", 0.3),
    # --- A3 Fall: die Durchsuchung --------------------------------------------------------------------------------------
    ("[wider]Ines widerspricht. Trotzdem durchsuchen die beiden Wohnung und Atelier [fund]und finden einen Stapel "
     "Konzertkarten.", 0.3),
    ("[frage]Verletzt die Durchsuchung Ines in ihrem Grundrecht aus Artikel dreizehn Grundgesetz?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Schutzbereich und Eingriff (Wortlautkarte Art. 13 Abs. 1 GG) ---------------------------------------------
    ("[art13]Erstens, der Schutzbereich. Artikel dreizehn Absatz eins: Die Wohnung ist unverletzlich. [raum]Geschützt ist "
     "die räumliche Sphäre, in der sich das Privatleben entfaltet. [weit]Der Begriff ist weit: [gesch]Auch Arbeits- und "
     "Geschäftsräume wie das Atelier von Ines gehören dazu. [eingr]Zweitens, der Eingriff. Eine Durchsuchung ist das gezielte Suchen des "
     "Staates nach etwas, das die Inhaberin nicht von sich aus offenlegen oder herausgeben will. [schwer]Sie greift schwer in das Grundrecht ein.", PS),
    # --- D 2. Rechtfertigung: Art. 13 Abs. 2 GG (Wortlautkarte) -------------------------------------------------------
    ("[abs2]Drittens, die Rechtfertigung. Hier gilt Absatz zwei: [richter]Durchsuchungen dürfen nur durch den Richter, "
     "[giv]bei Gefahr im Verzuge auch durch die in den Gesetzen vorgesehenen anderen Organe angeordnet werden. "
     "[regel]Das Bundesverfassungsgericht stellte zweitausendeins klar: Die richterliche Anordnung ist die Regel, die "
     "nichtrichterliche die Ausnahme. [neutral]Denn der Richter kontrolliert vorher, unabhängig und neutral. [eng]Deshalb "
     "ist Gefahr im Verzug eng auszulegen.", PS),
    # --- E 3. Anforderungen an Gefahr im Verzug (BVerfGE 103, 142) ----------------------------------------------------
    ("[def]Gefahr im Verzug liegt nur vor, wenn schon die vorherige Einholung der richterlichen Anordnung den Erfolg der "
     "Durchsuchung gefährden würde. [tats]Das muss mit Tatsachen des Einzelfalls begründet werden; Spekulationen oder "
     "fallunabhängige Vermutungen aus kriminalistischer Alltagserfahrung reichen nicht. [versuch]Regelmäßig muss die Polizei zuerst "
     "versuchen, einen Richter zu erreichen. [selbst]Die Eile darf sie nicht selbst herbeiführen, [doku]und ihre Gründe "
     "muss sie in den Akten dokumentieren, auch ob sie einen Richter zu erreichen versucht hat.", P),
    ("[bereit]Dafür müssen die Gerichte einen Ermittlungsrichter erreichbar halten, auch durch einen Bereitschaftsdienst. "
     "[tag]Zweitausendneunzehn präzisierte das Gericht: Bei Tage, ganzjährig von sechs bis einundzwanzig Uhr, muss ein "
     "Ermittlungsrichter uneingeschränkt erreichbar sein, auch außerhalb der Dienststunden. [nacht]Nachts verlangt die "
     "Verfassung einen Bereitschaftsdienst nur, wenn der Bedarf über den Ausnahmefall hinausgeht. [abstr]Der bloße Hinweis, zu dieser Zeit sei gewöhnlich kein Richter zu "
     "erreichen, begründet keine Gefahr im Verzug.", PS),
    # --- F 4. Einfaches Recht: § 105 Abs. 1 S. 1 StPO (Wortlautkarte) --------------------------------------------------
    ("[p105]Im einfachen Recht setzt das Paragraf hundertfünf Absatz eins der Strafprozessordnung um: "
     "[p105a]Durchsuchungen dürfen nur durch den Richter, [p105b]bei Gefahr im Verzug auch durch die Staatsanwaltschaft und "
     "ihre Ermittlungspersonen angeordnet werden. [kompet]Bader und Ebner sind Ermittlungspersonen; ohne Richter durften "
     "sie also nur bei Gefahr im Verzug durchsuchen. [p102]Die Befugnis, beim Verdächtigen zu durchsuchen, steht in "
     "Paragraf hundertzwei. [f151]Die Durchsuchung nach der Strafprozessordnung im Ganzen zeigt unsere Folge "
     "hunderteinundfünfzig.", PS),
    # --- G 5. Lösung ----------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Ines. [sonntag]Sonntag, neunzehn Uhr, ist Tageszeit. Ein Ermittlungsrichter musste erreichbar sein, "
     "und die Richterin war es auch. [anruf]Bader hätte also zumindest versuchen müssen, über die "
     "Staatsanwaltschaft den Bereitschaftsrichter zu erreichen; seit fünfzehn Uhr war dafür Zeit. [muendl]In einfachen Fällen darf der Richter sogar allein nach mündlicher Schilderung "
     "entscheiden. [spek]Dass Ines alles verschwinden lässt, ist eine bloße Vermutung, denn sie weiß von der Anzeige "
     "nichts. [neg]Gefahr im Verzug liegt nicht vor. [erg]Die Durchsuchung verletzt Ines in ihrem Grundrecht aus "
     "Artikel dreizehn.", PS),
    ("[gegen]Anders wäre es, wenn die Polizei konkret wüsste, dass Ines die Karten noch an diesem Abend wegschaffen will. "
     "[gegen2]Das wäre eine Tatsache des Einzelfalls, [gegen3]und dann könnte schon der Versuch, einen "
     "Richter zu erreichen, zu spät kommen.", P),
    ("[verw]Ob die Karten als Beweis verwertbar bleiben, ist eine eigene Frage der Abwägung; mehr dazu in Folge "
     "zweihunderteinundzwanzig.", PS),
    # --- H Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Gefahr im Verzug prüfst du in der Rechtfertigung, bei Artikel dreizehn Absatz zwei. "
     "[tipp1]Es ist ein Begriff der Verfassung, [tipp2]und die Gerichte kontrollieren ihn in vollem Umfang, ohne "
     "Beurteilungsspielraum der Ermittlungsbehörden. [tipp3]Grenze außerdem die Durchsuchung vom bloßen Betreten ab: Nur für die "
     "Durchsuchung gilt der Richtervorbehalt aus Absatz zwei.", PS),
    # --- I Schema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [s1]Erstens: Schutzbereich, die Wohnung, auch Geschäftsräume. [s2]Zweitens: Eingriff durch die "
     "Durchsuchung. [s3]Drittens: Rechtfertigung nach Absatz zwei. [s3a]Grundlage ist Paragraf hundertzwei. "
     "[s3b]Anordnen muss nach Paragraf hundertfünf der Richter, [s3c]ohne ihn nur bei Gefahr im Verzug: auf Tatsachen "
     "gestützt, Richter zuvor versucht, nicht selbst herbeigeführt, dokumentiert. [s3d]Dann die Verhältnismäßigkeit. "
     "[s4]Viertens: das Ergebnis.", PS),
    # --- J Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Durchsuchung ordnet grundsätzlich der Richter an. [m2]Gefahr im Verzug ist die enge Ausnahme: "
     "Tatsachen statt Vermutungen, und zuerst der Versuch, einen Richter zu erreichen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
