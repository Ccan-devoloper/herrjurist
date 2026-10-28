"""Folge 203 · Einverständliche Fremdgefährdung: Beifahrer beim Straßenrennen (Mi · Examenswissen · StGB AT, Format Abgrenzung).
Fall nach dem Plan-Hook („Ein Beifahrer feuert seinen Fahrer bei einem nächtlichen Rennen an und stirbt, als dieser die
Kontrolle verliert.“): Hilmar (Anfang 50) fährt in der Nacht zum Samstag, 1:10 Uhr, mit seinem getunten Wagen gegen einen
zweiten Wagen ein Rennen auf einer Landstraße; Beifahrer ist sein junger Kollege Eike (um 25). Beide kennen die Gefahr.
Eike feuert Hilmar an. Erlaubt sind 100 km/h, Hilmar fährt fast 190 km/h; in einer Kurve verliert er die Kontrolle, der Wagen
kommt von der Straße ab, Eike stirbt noch an der Unfallstelle, Hilmar überlebt verletzt.
Darstellung zurückhaltend: kein Aufprall, kein Blut, keine Verletzten im Bild, keine echten Automarken, keine
Raser-Verherrlichung – nur Wagen-Icons, Kurvenschild, Warndreieck und Blaulicht.
Echter Fall: BGH, Urt. v. 20.11.2008 – 4 StR 328/08, BGHSt 53, 55 (Rn. nach der amtlichen Fassung auf
bundesgerichtshof.de). Aufbau (Abgrenzung): Fall → Sachverhalt → echter Fall → § 222 (Wortlaut), unproblematisch →
Selbstgefährdung (Verweis Folge 058) oder einverständliche Fremdgefährdung, Kriterium Tatherrschaft (Rn. 21–23) →
hier Fremdgefährdung (Rn. 24) → Gegenansicht in einem Satz (Rn. 25) → Einwilligung, § 228 (Wortlaut), konkrete
Todesgefahr (Rn. 27–30; Verweis Folge 157), Ergebnis → § 315d (Wortlaut Auszug) in einem Satz → Klausurtipp
(Lexi, Prüfungsreihenfolge Schritt für Schritt) → Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Auftragsliste und Volltextsuche 06.10.2026): Hilmar, Eike.
Nie im Genitiv mit -s. Stimmen (Pool niklas, helmut, ela_froh, julia): Hilmar helmut (Mann, älter), Eike niklas
(Mann, jung); ela_froh und julia nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gerichtsnamen im Sprechtext als Wörter (keine Abkürzungen wie StGB/BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Hilmar": "helmut", "Eike": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Parkplatz in der Nacht ----------------------------------------------------------------------------
    ("[fall]Samstag, ein Uhr zehn in der Nacht. Ein leerer Parkplatz am Stadtrand. [hilmar]Hilmar, Anfang fünfzig, hat "
     "seinen Wagen auf Tempo getrimmt. [eike]Sein junger Kollege Eike fährt als Beifahrer mit. [gegner]Auf der Landstraße "
     "wollen sie gegen einen zweiten Wagen ein Rennen fahren. [wissen]Beide sind nüchtern und wissen, wie gefährlich das ist.", P),
    ("[e1]Los, Hilmar, gib Gas! Den hängen wir ab!", P, "Eike"),
    ("[h1]Halt dich fest!", P, "Hilmar"),
    # --- A2 Fall: das Rennen auf der Landstraße -------------------------------------------------------------------------
    ("[start]Die beiden Wagen starten nebeneinander. [tempo]Erlaubt sind hundert, Hilmar fährt fast hundertneunzig. "
     "[anfeuern]Eike feuert ihn weiter an. [kurve]In einer Kurve verliert Hilmar die Kontrolle, [ab]der Wagen kommt von der "
     "Straße ab. [stirbt]Eike stirbt noch an der Unfallstelle, Hilmar überlebt verletzt. [frage]Hat Hilmar ihn fahrlässig "
     "getötet? [frage2]Oder hat Eike sich selbst gefährdet?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall ------------------------------------------------------------------------------------------------
    ("[bgh]Vorbild ist ein Urteil des Bundesgerichtshofs vom zwanzigsten November zweitausendacht. "
     "[bgh2]Dort fuhren zwei Wagen auf einer Bundesstraße sogenannte Beschleunigungstests. Der spätere Tote saß als "
     "Beifahrer daneben, gab Startzeichen und filmte. [bgh3]Beim gleichzeitigen Überholen eines dritten Autos kam der Wagen "
     "von der Fahrbahn ab. [bgh4]Das Landgericht verurteilte die Fahrer nur wegen Gefährdung des Straßenverkehrs. Der "
     "Bundesgerichtshof sprach sie zusätzlich der fahrlässigen Tötung schuldig.", PS),
    # --- D § 222 StGB ----------------------------------------------------------------------------------------------------
    ("[p222]Prüfen wir also fahrlässige Tötung, Paragraf zweihundertzweiundzwanzig: Wer durch Fahrlässigkeit den Tod eines "
     "Menschen verursacht. [erfolg]Eike ist tot, und ohne das Rennen wäre er nicht gestorben. [pflicht]Hilmar fuhr viel zu "
     "schnell und verletzte so seine Sorgfaltspflicht. [vorh]Ein tödlicher Unfall war auch vorhersehbar. [unpro]Bis hierhin "
     "ist der Fall unproblematisch.", PS),
    # --- E Abgrenzung: Selbstgefährdung oder einverständliche Fremdgefährdung? -------------------------------------------
    ("[problem]Das Problem steckt in der Zurechnung. [selbst]Wer eine eigenverantwortliche Selbstgefährdung nur veranlasst, "
     "ermöglicht oder fördert, ist grundsätzlich nicht strafbar. [v058]Das kennst du aus unserer Folge zum "
     "Heroinspritzen-Fall. [fremd]Anders bei der einverständlichen Fremdgefährdung: Hier gefährdet ein anderer das Opfer, "
     "und das Opfer ist damit einverstanden.", P),
    ("[krit]Wie grenzt man ab? Der Bundesgerichtshof stellt auf die Tatherrschaft über die gefährdende Handlung ab, wie bei "
     "Täterschaft und Teilnahme. [auch]Das gilt auch beim Fahrlässigkeitsdelikt. [unmittel]Besonders wichtig ist, wer das "
     "Geschehen beherrscht, das unmittelbar zum Erfolg führt.", PS),
    # --- F Hier: Fremdgefährdung -----------------------------------------------------------------------------------------
    ("[hier]Im Fall saß Hilmar am Steuer. [lenk]Allein er bestimmte Geschwindigkeit und Lenkung. [ausgesetzt]Eike konnte "
     "die Gefahr nicht durch eigenes Handeln abwenden, er war dem Fahrverhalten nur ausgesetzt. [anf]Sein Anfeuern hat nur "
     "untergeordnete Bedeutung, wie Startzeichen und Filmen im echten Fall. [fg]Also: einverständliche Fremdgefährdung. "
     "Der Tod ist Hilmar zuzurechnen.", P),
    ("[roxin]Ein Teil der Lehre, etwa Roxin, will manche Fremdgefährdungen der Selbstgefährdung gleichstellen; der "
     "Bundesgerichtshof lehnte das hier ab, denn es zählt die tatsächliche Situation beim Unfall, nicht, wer zufällig am "
     "Steuer saß.", PS),
    # --- G Einwilligung, § 228 StGB --------------------------------------------------------------------------------------
    ("[einw]Bleibt die Rechtswidrigkeit. Eike war mit dem Risiko einverstanden. Rechtfertigt das? [p228]Den Maßstab liefert "
     "Paragraf zweihundertachtundzwanzig: Wer eine Körperverletzung mit Einwilligung der verletzten Person vornimmt, handelt "
     "nur dann rechtswidrig, wenn die Tat trotz der Einwilligung gegen die guten Sitten verstößt.", P),
    ("[indiv]Der Bundesgerichtshof sagt: Paragraf zweihundertzweiundzwanzig schützt allein Rechtsgüter des Einzelnen. Die "
     "Einwilligung in das Risiko kann deshalb rechtfertigen. [grenze]Aber nur bis zur Grenze der Sittenwidrigkeit. "
     "Sittenwidrig ist die Tat jedenfalls, wenn sie den Einwilligenden in konkrete Todesgefahr bringt, beurteilt aus der "
     "Sicht vor der Tat. [v157]Mehr zu diesem Maßstab in unserer Folge zur verabredeten Schlägerei. [allg]Anders bei "
     "Paragraf dreihundertfünfzehn c, der Gefährdung des Straßenverkehrs: Er schützt auch die Sicherheit des Verkehrs im "
     "Allgemeinen. Dort hilft die Einwilligung grundsätzlich nicht.", PS),
    ("[erg]Im Fall: Mit fast hundertneunzig in eine Kurve auf der Landstraße, da war Eike in konkreter Todesgefahr. "
     "[erg2]Seine Einwilligung rechtfertigt nicht. Hilmar konnte die Gefahr auch selbst erkennen, er handelte schuldhaft. "
     "[erg3]Hilmar ist strafbar wegen fahrlässiger Tötung.", PS),
    # --- H § 315d StGB ----------------------------------------------------------------------------------------------------
    ("[p315d]Heute kommt Paragraf dreihundertfünfzehn d hinzu, das verbotene Kraftfahrzeugrennen, in Kraft seit dem "
     "dreizehnten Oktober zweitausendsiebzehn und im echten Fall noch nicht anwendbar: [abs5]Verursacht der Fahrer bei "
     "einer vorsätzlichen konkreten Gefährdung den Tod eines anderen Menschen, drohen nach Absatz fünf ein bis zehn Jahre "
     "Freiheitsstrafe.", PS),
    # --- I Klausurtipp mit Prüfungsreihenfolge (Lexi) -------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte die Prüfungsreihenfolge ein. [k1]Erstens der Tatbestand: Erfolg, Kausalität, "
     "Sorgfaltspflichtverletzung und Vorhersehbarkeit. [k2]Dann die Zurechnung: Selbst- oder Fremdgefährdung? Frag, wer die "
     "gefährdende Handlung beherrscht. [k3]Zweitens die Rechtswidrigkeit: Einwilligung, aber keine konkrete Todesgefahr. "
     "[k4]Drittens die Schuld. [k5]Und beim Rennen denk an Paragraf dreihundertfünfzehn d.", PS),
    # --- J Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Beherrscht der andere die gefährdende Handlung, ist es Fremdgefährdung, keine Selbstgefährdung. [mk2]Dann hilft nur noch die "
     "Einwilligung, und die endet bei konkreter Todesgefahr.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
