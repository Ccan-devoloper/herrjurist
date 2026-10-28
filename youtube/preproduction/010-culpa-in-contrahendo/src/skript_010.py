"""Folge 010 · Haftung ohne Vertrag? Culpa in contrahendo und der Linoleumrollen-Fall (Mo · Der Fall · Schuldrecht AT).
Fiktiver Fall (Einrichtungshaus, umkippende Teppichrollen) nach dem Vorbild von RG, Urt. v. 7.12.1911 – VI 240/11 = RGZ 78, 239
(Linoleumrollen-Fall); Namen erfunden, keine realen Beteiligten. Heutige Rechtslage: §§ 280 I, 311 II Nr. 2, 241 II, 278,
253 II BGB; Gegenüberstellung Delikt (§§ 823 I, 831 I 2 BGB, Entlastungsbeweis). Dritte im Näheverhältnis und Fallgruppen
nach der Gesetzesbegründung (BT-Drs. 14/6040, S. 162 f.) und BGH, Urt. v. 13.10.2017 – V ZR 11/17, Rn. 5.
Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Hartmann": "laura_ruhig", "Jannik": "timo", "Kessler": "stephan"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Einrichtungshaus -------------------------------------------------------------------------
    ("[laden]Ein Einrichtungshaus, Abteilung Bodenbeläge. [kundin]Frau Hartmann möchte einen Teppichboden kaufen. "
     "[muster]Verkäufer Jannik zeigt ihr Muster.", 0.3),
    ("[h1]Den hier nehme ich. Können Sie mir die Rolle zeigen?", 0.3, "Hartmann"),
    ("[rollen]Jannik stellt zwei schwere Rollen beiseite, ohne sie zu sichern. "
     "[kippen]Die Rollen kippen um und reißen Frau Hartmann zu Boden.", 0.3),
    ("[j1]Oh nein! Haben Sie sich verletzt?", 0.3, "Jannik"),
    ("[arm]Ihr Handgelenk ist gebrochen. [nichts]Gekauft hat sie nichts. "
     "[fordert]Vom Inhaber, Herrn Kessler, verlangt sie Ersatz der Heilungskosten und Schmerzensgeld.", 0.3),
    ("[k1]Einen Vertrag hatten wir nie. Und Jannik habe ich sorgfältig ausgewählt und angeleitet.", 0.4, "Kessler"),
    ("[frage]Haftet Kessler, obwohl nie ein Vertrag zustande kam?", 0.6),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Delikt genügt nicht ----------------------------------------------------------------------------------
    ("[delikt]Naheliegend ist das Deliktsrecht. [p823]Jannik selbst haftet nach Paragraf achthundertdreiundzwanzig, "
     "er hat fahrlässig ihren Körper verletzt. [p831]Kessler haftet nach Paragraf achthunderteinunddreißig "
     "für seinen Verrichtungsgehilfen.", P),
    ("[exkul]Aber er kann sich entlasten, wenn er Jannik sorgfältig ausgewählt und angeleitet hat. "
     "[luecke]Dann bliebe Frau Hartmann nur der Angestellte.", PS),
    # --- D Der Linoleumrollen-Fall ---------------------------------------------------------------------------------
    ("[rg]Neunzehnhundertelf, der Linoleumrollen-Fall. In einem Warenhaus fallen zwei Linoleumrollen auf eine "
     "Kundin und ihr Kind. [rg2]Zum Kauf kommt es nicht.", P),
    ("[rg3]Das Reichsgericht sagt: Die Bitte, Ware vorzulegen, und das Vorlegen bereiten einen Kauf vor. "
     "[rg4]Es entsteht ein vertragsähnliches Rechtsverhältnis [rg5]mit der Pflicht, auf Gesundheit und Eigentum "
     "des anderen zu achten.", P),
    ("[rg6]Für diese Pflicht setzt der Inhaber seinen Angestellten ein. Also haftet er nach Paragraf "
     "zweihundertachtundsiebzig für dessen Verschulden. [mittellos]Sonst würde der Verletzte an den meist mittellosen "
     "Angestellten verwiesen. [cic]Der Fall wurde zum Klassiker der culpa in contrahendo. "
     "[kodif]Seit zweitausendzwei steht sie im Gesetz, in Paragraf dreihundertelf Absatz zwei.", PS),
    # --- E Prüfung: Schuldverhältnis -----------------------------------------------------------------------------
    ("[a]Wir prüfen also: Frau Hartmann gegen Kessler auf Schadensersatz aus culpa in contrahendo. [sch1]Erstens braucht es ein Schuldverhältnis. "
     "Ein Kaufvertrag fehlt. [nr]Aber nach Paragraf dreihundertelf Absatz zwei genügen schon Vertragsverhandlungen, "
     "die Anbahnung eines Vertrags oder ähnliche geschäftliche Kontakte.", P),
    ("[anb]Hier liegt eine Anbahnung vor, Nummer zwei: Frau Hartmann kommt, um zu kaufen, und gibt dem Geschäft so "
     "die Möglichkeit, auf ihre Gesundheit einzuwirken. [begr]Die Gesetzesbegründung nennt hier ausdrücklich "
     "den Linoleumrollen-Fall.", PS),
    # --- F Pflichtverletzung, Vertretenmüssen ----------------------------------------------------------------------
    ("[pfl]Zweitens: eine Pflichtverletzung. Paragraf zweihunderteinundvierzig Absatz zwei verlangt Rücksicht auf die "
     "Rechtsgüter des anderen Teils. [pfl2]Wer schwere Rollen ungesichert abstellt, verletzt diese Pflicht. "
     "[pfl3]Die Pflicht trifft Kessler, Jannik hat sie für ihn verletzt.", PS),
    ("[vm]Drittens: Vertretenmüssen. Es wird nach Paragraf zweihundertachtzig Absatz eins Satz zwei vermutet. "
     "[p278]Janniks Verschulden wird Kessler nach Paragraf zweihundertachtundsiebzig zugerechnet, denn Jannik ist sein "
     "Erfüllungsgehilfe. [fahrl]Und Jannik war fahrlässig: Er hätte die Rollen abstützen oder schräg an die Wand "
     "lehnen müssen. [keine]Eine Entlastung wie bei Paragraf achthunderteinunddreißig gibt es hier nicht.", PS),
    # --- G Schaden, Ergebnis ---------------------------------------------------------------------------------------
    ("[schaden]Viertens: der Schaden. Zu ersetzen sind etwa die Heilungskosten. [smg]Und weil ihr Körper verletzt ist, "
     "gibt es nach Paragraf zweihundertdreiundfünfzig Absatz zwei auch Schmerzensgeld. "
     "[erg]Ergebnis: Kessler haftet, obwohl es nie einen Vertrag gab.", PS),
    # --- H Gegenfall: die Tochter ----------------------------------------------------------------------------------
    ("[kind]Und wäre Frau Hartmanns Tochter mitgekommen und auch getroffen worden? "
     "[kind2]Dritte, die einer Partei nahestehen, können nach den Grundsätzen des Vertrags mit Schutzwirkung zugunsten "
     "Dritter geschützt sein, [kind3]laut Gesetzesbegründung schon vor dem Vertragsschluss.", PS),
    # --- I Fallgruppen ----------------------------------------------------------------------------------------------
    ("[gruppen]Die kippende Rolle steht für eine Fallgruppe: verletzte Schutzpflichten. "
     "[g2]Daneben gibt es verletzte Aufklärungspflichten, die zu einem nachteiligen Vertrag führen, "
     "[g3]den Abbruch von Verhandlungen ohne triftigen Grund, wenn der Vertrag schon als sicher galt, "
     "[g4]und die Haftung Dritter nach Absatz drei, wenn sie besonderes Vertrauen in Anspruch nehmen.", PS),
    # --- J Klausurtipp (Lexi) --------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die culpa in contrahendo vor dem Delikt, als vertragsähnlichen Anspruch. "
     "[tipp1]Und zeig, warum sie zählt: Für den Erfüllungsgehilfen gibt es keine Entlastung, "
     "für den Verrichtungsgehilfen schon.", PS),
    # --- K Klausurschema -------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Anspruch aus culpa in contrahendo, Paragrafen zweihundertachtzig, dreihundertelf, "
     "zweihunderteinundvierzig. [s2]Römisch eins: vorvertragliches Schuldverhältnis. [s3]Römisch zwei: Pflichtverletzung. "
     "[s4]Römisch drei: Vertretenmüssen, mit Paragraf zweihundertachtundsiebzig. [s5]Römisch vier: Schaden, auch "
     "Schmerzensgeld.", P),
    ("[s6]Danach das Delikt: Paragraf achthunderteinunddreißig mit Entlastung [s7]und Paragraf "
     "achthundertdreiundzwanzig gegen den Angestellten.", PS),
    # --- L Merksatz (Lexi) -----------------------------------------------------------------------------------------
    ("[merke]Merke: Wer einen Vertrag anbahnt, schuldet schon Rücksicht. "
     "[m2]Für seine Gehilfen haftet er dann wie für sich selbst, ohne Entlastung.", 1.4),
]
