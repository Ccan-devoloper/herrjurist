"""Folge 064 · Abschleppfall: Musst du die Kosten zahlen? Polizeirecht erklärt (Mo · Der Fall · Polizei- und
Ordnungsrecht). Übungsfall nach dem Hook des Themenplans, Beispielland Nordrhein-Westfalen (VwVG NRW, VO VwVG NRW, OBG NRW):
Frau Kaiser parkt „nur fünf Minuten“ ohne Parkausweis auf einem Parkplatz für schwerbehinderte Menschen (Zeichen 314 mit
Zusatzzeichen Rollstuhlfahrersinnbild) vor der Apotheke. Herr Meier vom Ordnungsamt findet niemanden am Wagen und bestellt
einen Abschleppwagen. Als Frau Kaiser nach zehn Minuten zurückkommt, hängt das Auto am Haken; Herr Becker vom Abschleppdienst
bringt es auf den Hof. Kostenbescheid über 250 € (Abschleppkosten als Auslagen und Verwaltungsgebühr).
Prüfung: drei Ebenen; § 77 I VwVG NRW i. V. m. § 20 II 2 Nr. 7, § 15 I Nr. 7 VO VwVG NRW; formell; Konnexität (BVerwG 3 C 25.16
Rn. 11); Grundverwaltungsakt Zeichen 314 + Zusatzzeichen (Wortlautkarte Anlage 3 StVO lfd. Nr. 7), § 12 II StVO; Allgemeinverfügung
§ 35 S. 2 VwVfG, Sichtbarkeitsgrundsatz (BVerwG 3 C 10.15 Rn. 16, 19), Wegfahrgebot § 80 II 1 Nr. 2 VwGO analog (BVerwG 3 C 25.16
Rn. 14); Ersatzvornahme § 59 I VwVG NRW (Wortlautkarte), Sofortvollzug § 55 II VwVG NRW (OVG NRW 5 A 2289/18 Rn. 30 f.),
unmittelbare Ausführung in anderen Ländern (BVerwG 3 C 10.15 Rn. 10); Verhältnismäßigkeit (BVerwG 3 C 5.13; OVG NRW 5 A 2339/99;
VG Düsseldorf 14 K 6945/16); Kostenpflicht, Ergebnis; Klausurtipp (Sicherstellung § 24w OBG NRW), Schema, Merksatz.
Fiktive Figuren: Frau Kaiser (ela_froh), Herr Meier (helmut), Herr Becker (niklas). Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Kaiser": "ela_froh", "Meier": "helmut", "Becker": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: vor der Apotheke ---------------------------------------------------------------------------------------
    ("[fall]Ein Vormittag in einer Stadt in Nordrhein-Westfalen. [park]Frau Kaiser stellt ihr Auto auf einen Parkplatz für "
     "schwerbehinderte Menschen, direkt vor der Apotheke. [schild]Das blaue Schild mit dem Rollstuhlsymbol ist gut zu sehen. "
     "[ausweis]Einen Parkausweis hat sie nicht.", 0.2),
    ("[ka1]Nur fünf Minuten, ich bin gleich wieder da.", 0.3, "Kaiser"),
    # --- B Fall: das Ordnungsamt kommt ------------------------------------------------------------------------------------
    ("[meier]Kurz darauf kommt Herr Meier vom Ordnungsamt. [kein]Kein Parkausweis im Auto, niemand am Wagen, kein Zettel. "
     "[ruft]Er bestellt einen Abschleppwagen.", 0.2),
    ("[me1]Der Platz muss frei sein. Das Auto wird abgeschleppt.", 0.3, "Meier"),
    # --- C Fall: am Haken -------------------------------------------------------------------------------------------------
    ("[zurueck]Nach zehn Minuten kommt Frau Kaiser zurück. [haken]Ihr Auto hängt schon am Haken. [becker]Herr Becker vom "
     "Abschleppdienst bringt es auf den Hof.", 0.2),
    ("[ka2]Ich war doch nur fünf Minuten weg!", 0.3, "Kaiser"),
    ("[be1]Den Auftrag hat die Stadt gegeben.", 0.3, "Becker"),
    # --- D Kostenbescheid und Frage -----------------------------------------------------------------------------------------
    ("[bescheid]Eine Woche später kommt ein Kostenbescheid: [betrag]zweihundertfünfzig Euro für Abschleppkosten und "
     "Verwaltungsgebühr. [frage]Muss Frau Kaiser zahlen?", 0.6),
    # --- E Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F Drei Ebenen, Landesrecht ---------------------------------------------------------------------------------------------
    ("[ebenen]Im Abschleppfall trennst du drei Ebenen: [e1]das Verkehrszeichen, [e2]das Abschleppen [e3]und die Kosten. "
     "[land]Das Vollstreckungsrecht ist Landesrecht. Wir nehmen Nordrhein-Westfalen als Beispiel. Die anderen Länder haben "
     "ähnliche Regeln, oft unter anderer Nummer.", P),
    # --- G Ermächtigungsgrundlage, formell, Konnexität -------------------------------------------------------------------------
    ("[egl]Angegriffen wird der Kostenbescheid. Grundlage ist Paragraf siebenundsiebzig Verwaltungsvollstreckungsgesetz mit "
     "der Ausführungsverordnung: [ausl]Die Abschleppkosten verlangt die Stadt als Auslagen, [geb]dazu kommt eine Gebühr. "
     "[formell]Formell gibt es keine Probleme: Die Stadt ist zuständig und hat Frau Kaiser angehört. [konnex]Materiell gilt: "
     "Kosten gibt es nur, wenn das Abschleppen rechtmäßig war.", P),
    # --- H Grundverwaltungsakt: das Schild, Wortlaut Anlage 3 StVO -------------------------------------------------------------
    ("[gva]Was hat die Stadt vollstreckt? Das Schild. [wl314]Zeichen dreihundertvierzehn erlaubt das Parken. Das Zusatzzeichen "
     "mit dem Rollstuhlsymbol beschränkt die Erlaubnis auf schwerbehinderte Menschen mit außergewöhnlicher Gehbehinderung "
     "oder vergleichbaren Einschränkungen und auf blinde Menschen. [gilt]Und sie gilt nur mit gut lesbar ausgelegtem "
     "Parkausweis. [andere]Für alle anderen ist das Parken dort verboten. [fuenf]Nur fünf Minuten hilft nicht: Wer sein "
     "Fahrzeug verlässt, der parkt, Paragraf zwölf Absatz zwei der Straßenverkehrs-Ordnung.", P),
    # --- I Allgemeinverfügung, Sichtbarkeit, Wegfahrgebot ----------------------------------------------------------------------
    ("[va]Das Schild ist ein Verwaltungsakt in Form einer Allgemeinverfügung, Paragraf fünfunddreißig Satz zwei "
     "Verwaltungsverfahrensgesetz. [bekannt]Bekannt gegeben wird es durch das Aufstellen. [sicht]Nach dem "
     "Sichtbarkeitsgrundsatz wirkt es gegenüber jedem, wenn ein durchschnittlicher Kraftfahrer es mit einem raschen und "
     "beiläufigen Blick erfassen kann, ob er es sieht oder nicht. [umschau]Beim Parken gehört dazu eine einfache Umschau nach "
     "dem Aussteigen. [weg]Das Schild enthält zugleich ein Wegfahrgebot. [sofort]Es ist sofort vollziehbar, entsprechend "
     "Paragraf achtzig Absatz zwei Satz eins Nummer zwei Verwaltungsgerichtsordnung, [polizei]der Regel für unaufschiebbare "
     "Anordnungen von Polizeivollzugsbeamten.", P),
    # --- J Ersatzvornahme, Wortlaut § 59 I VwVG NRW ----------------------------------------------------------------------------
    ("[ev]Jetzt das Abschleppen. Wegfahren kann auch ein anderer, es ist eine vertretbare Handlung. [wl59]Dann darf die "
     "Behörde nach Paragraf neunundfünfzig die Handlung auf Kosten des Betroffenen selbst ausführen oder einen anderen "
     "beauftragen. [evname]Das ist die Ersatzvornahme.", P),
    # --- K Gestrecktes Verfahren oder Sofortvollzug -----------------------------------------------------------------------------
    ("[wege]Für das Verfahren gibt es zwei Wege. [gestr]Im gestreckten Verfahren wird ein Verwaltungsakt vollstreckt, hier "
     "das Wegfahrgebot. Dazu gehören Androhung und Festsetzung. [nrw]Die Festsetzung braucht aber einen erreichbaren "
     "Adressaten. Das Oberverwaltungsgericht Nordrhein-Westfalen greift deshalb auf den sofortigen Vollzug zurück, "
     "Paragraf fünfundfünfzig Absatz zwei. [entb]Dann darf die Stadt ohne Androhung handeln, und die Festsetzung fällt weg. [gefahr]Die nötige gegenwärtige "
     "Gefahr liegt vor: Der Verstoß gegen das Schild stört die öffentliche Sicherheit schon jetzt. [ua]In anderen Ländern "
     "läuft das Abschleppen zum Teil als unmittelbare Ausführung, etwa in Berlin.", P),
    # --- L Verhältnismäßigkeit: geeignet, erforderlich, Wartezeit -----------------------------------------------------------------
    ("[vhm]Bleibt die Verhältnismäßigkeit, der Kern des Falls. [geeig]Das Abschleppen macht den Platz frei, es ist geeignet. "
     "[erf]Erforderlich ist es, wenn kein milderes Mittel bleibt. Herr Meier muss die Fahrerin nur suchen, wenn er sie ohne "
     "Schwierigkeiten und ohne Verzögerung erreichen kann. [risiko]Das Risiko, nicht erreichbar zu sein, trägt, wer falsch "
     "parkt. [warten]Eine feste Wartezeit gibt es nicht. Warten kann aber geboten sein, etwa wenn konkret erkennbar ist, dass "
     "der Fahrer gleich zurückkommt und wegfährt. [hier]Hier war niemand zu sehen, und im Auto lag kein Hinweis.", P),
    # --- M Angemessenheit, Gegenfälle ----------------------------------------------------------------------------------------------
    ("[angem]Und angemessen? [funktion]Ein Parkplatz für schwerbehinderte Menschen erfüllt seinen Zweck nur, wenn er "
     "jederzeit frei ist. Die Berechtigten sollen sich darauf verlassen können. [konkret]Deshalb darf die Stadt nach dem "
     "Oberverwaltungsgericht Nordrhein-Westfalen abschleppen, auch wenn gerade niemand konkret am Parken gehindert wird. "
     "[gegen]Anders kann es liegen, wenn ein Auto nur verbotswidrig steht und niemanden behindert, etwa auf dem Gehweg. "
     "Die bloße Vorbildwirkung reicht dann nicht. [sicht2]Und steht die Fahrerin in Sicht- oder Rufweite, ist Ansprechen "
     "das mildere Mittel.", PS),
    # --- N Ergebnis und Kosten ---------------------------------------------------------------------------------------------------
    ("[erg]Das Abschleppen war also rechtmäßig. [pflicht]Frau Kaiser hat die Gefahr verursacht. Sie ist Verhaltensstörerin "
     "und muss die Kosten tragen. [hoehe]Die Abschleppkosten sind Auslagen, die Gebühr liegt im Rahmen von dreißig bis "
     "hundertachtzig Euro. [zahlt]Frau Kaiser muss zahlen. [bussgeld]Ein Bußgeld wäre ein eigenes Verfahren, und mit "
     "Zivil- oder Strafrecht hat der Fall nichts zu tun.", PS),
    # --- O Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte die drei Ebenen auseinander und prüfe das Abschleppen inzident im Kostenbescheid. "
     "[tipp2]Kommt das Auto auf einen Verwahrhof, prüfen manche Gerichte stattdessen eine Sicherstellung, heute im "
     "Ordnungsbehördengesetz geregelt. [tipp3]Oft lassen sie das offen, wenn beide Wege zum selben Ergebnis führen.", PS),
    # --- P Klausurschema --------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q1]Eins, Ermächtigungsgrundlage: Paragraf siebenundsiebzig Verwaltungsvollstreckungsgesetz "
     "mit Ausführungsverordnung. [q2]Zwei, formell: Zuständigkeit und Anhörung. [q3]Drei, materiell: rechtmäßiges "
     "Abschleppen. [q3a]Darin der Grundverwaltungsakt: das Schild, wirksam bekannt gegeben und sofort vollziehbar. "
     "[q3b]Dann die Ersatzvornahme im sofortigen Vollzug [q3c]und die Verhältnismäßigkeit. [q4]Vier, Kostenpflicht und "
     "Höhe.", PS),
    # --- Q Merksatz (Lexi) ----------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Auto auf dem Behindertenparkplatz darf regelmäßig sofort abgeschleppt werden, auch nach fünf "
     "Minuten. [m2]Die Kosten zahlt, wer falsch geparkt hat, aber nur, wenn das Abschleppen rechtmäßig war.", 1.4),
]
