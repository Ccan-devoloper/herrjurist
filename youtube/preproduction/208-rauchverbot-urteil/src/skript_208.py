"""Folge 208 · Rauchverbot-Urteil: Gleichheit trifft Berufsfreiheit (Art. 12, 3 GG) (Mo · Der Fall · Klassiker-Fall).
Leitentscheidung: BVerfG, Urt. v. 30.7.2008 – 1 BvR 3262/07, 1 BvR 402/08, 1 BvR 906/08, BVerfGE 121, 317 (Rauchverbot in
Gaststätten; Volltext bundesverfassungsgericht.de, zitiert mit Rn.; Tenor Nr. 1–3).
DARSTELLUNG: keine Tabakmarken, Rauchen nicht verherrlichen (Zigarette nur als durchgestrichenes Symbol), Wirt sympathisch.
Fiktiver Rahmen, der dem echten Fall folgt (Rn. 37–59): Alfons (Wirt einer Einraumkneipe in Baden-Württemberg; Stimme marc),
Herr Stadler (Stammgast; william), Frau Kaltenbach (Betreiberin einer Großraumdiskothek ab 18; sabrina). Die realen
Beschwerdeführer werden nicht benannt. Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Artikel im Sprechtext als Wörter; keine Abkürzungen. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Alfons": "marc", "Stadler": "william", "Kaltenbach": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Einraumkneipe (fiktiv, folgt Rn. 37–39, 46 f.) ---------------------------------------------------
    ("[fall]Alfons führt seit über zwanzig Jahren eine kleine Kneipe in Baden-Württemberg. [raum]Ein einziger Gastraum, "
     "dreiundsechzig Quadratmeter, [gaeste]überwiegend Stammgäste, nach seinen Angaben rund siebzig Prozent davon Raucher.", P),
    ("[verbot]Seit August zweitausendsieben gilt in Gaststätten ein Rauchverbot. [nebenraum]Größere Lokale dürfen aber "
     "einen abgetrennten Raucherraum einrichten. [kein]Bei Alfons geht das nicht: Der Raum lässt sich nicht teilen.", P),
    ("[st1]Tut mir leid, Alfons. Ich gehe jetzt ins große Lokal am Markt, da gibt es einen Raucherraum.", P, "Stadler"),
    ("[umsatz]Nach seinen Angaben sinkt sein Umsatz zunächst um dreißig bis vierzig Prozent.", P),
    ("[a1]Meine Kneipe muss rauchfrei sein, das große Lokal nicht. Ist das gerecht?", P, "Alfons"),
    # --- A2 Die Diskothek (Rn. 54–59) ------------------------------------------------------------------------------------
    ("[disko]Ähnlich geht es Frau Kaltenbach: Ihre Großraumdiskothek lässt nur Erwachsene hinein. [disko2]Trotzdem darf "
     "sie keinen Raucherraum einrichten, denn das Gesetz nimmt Diskotheken davon aus.", P),
    ("[ka1]Jede Gaststätte darf einen Raucherraum haben, nur wir nicht?", P, "Kaltenbach"),
    ("[frage]Verletzt das Berufsfreiheit und Gleichheit? [grund]Unser Fall folgt dem Rauchverbot-Urteil des "
     "Bundesverfassungsgerichts vom dreißigsten Juli zweitausendacht; [berlin]geklagt hatte dort auch eine Berliner Wirtin.", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Art. 12 Abs. 1 GG: Schutzbereich und Eingriff (Rn. 91–94, 114) ---------------------------------------------
    ("[a12]Prüfen wir zuerst die Berufsfreiheit. Artikel zwölf Absatz eins: Alle Deutschen haben das Recht, Beruf, "
     "Arbeitsplatz und Ausbildungsstätte frei zu wählen. Die Berufsausübung kann durch Gesetz oder auf Grund eines Gesetzes "
     "geregelt werden.", P),
    ("[schutz]Geschützt ist auch, welche Leistungen ein Wirt anbietet und welche Gäste er ansprechen will. [gast]Das "
     "Rauchverbot richtet sich zwar an die Gäste. [pflicht]Doch der Wirt darf das Rauchen nicht mehr erlauben und muss "
     "Verstöße unterbinden. [eingriff]Das ist ein unmittelbarer Eingriff in seine Berufsausübung, kein bloßer Reflex, "
     "[stufe1]also auf der ersten Stufe des Apotheken-Urteils eine Berufsausübungsregelung. [eigentum]Artikel vierzehn "
     "tritt zurück: Der Schwerpunkt liegt bei der Erwerbstätigkeit.", P),
    # --- D Rechtfertigung (Rn. 95–115, 121–125) ---------------------------------------------------------------------------
    ("[recht]Der Eingriff braucht ausreichende Gründe des Gemeinwohls und muss verhältnismäßig sein. [grundl]Grundlage "
     "sind die Landesgesetze; die Länder sind zuständig. [ziel]Ihr Ziel ist der Schutz vor den Gefahren des Passivrauchens, "
     "und der Schutz der Bevölkerung vor Gesundheitsgefahren zählt zu den überragend wichtigen Gemeinschaftsgütern. "
     "[geeig]Das Verbot ist geeignet [erford]und erforderlich; die freie Wahl zwischen Raucher- und Nichtraucherlokal durften "
     "die Gesetzgeber für weniger wirksam halten.", P),
    ("[strikt]Mehr noch: Der Gesetzgeber dürfte sogar ein striktes Rauchverbot ohne Ausnahmen verhängen, [eck]auch für "
     "Eckkneipen.", PS),
    # --- E Folgerichtigkeit (Rn. 116, 128–147) ----------------------------------------------------------------------------
    ("[aber]Baden-Württemberg und Berlin wählten aber ein anderes Konzept: [ausn]Raucherräume sind erlaubt, in "
     "Baden-Württemberg sind sogar Bier-, Wein- und Festzelte ausgenommen. [vermind]Der Gesundheitsschutz wird also mit "
     "verminderter Intensität verfolgt.", P),
    ("[folge]Dann gilt: Wer ein Regelungskonzept wählt, muss diese Entscheidung auch folgerichtig weiterverfolgen. "
     "[gewicht]Die Belastung der kleinen Kneipen wiegt jetzt stärker. [wander]Große Lokale halten ihre Raucher im "
     "Raucherraum, die Einraumkneipe verliert ihre Stammgäste an sie; [schaerfer]die Ausnahme verschärft ihre Lage noch. "
     "[wenig]Und dem Nichtraucherschutz bringt das Verbot dort wenig, denn Nichtraucher sind auf diese Kneipen "
     "typischerweise nicht angewiesen.", P),
    ("[unzu]Ergebnis: Für kleine Einraumkneipen mit getränkegeprägtem Angebot ist das Verbot unzumutbar, also nicht "
     "verhältnismäßig im engeren Sinne.", PS),
    # --- F Art. 3 Abs. 1 GG (Tenor Nr. 1 und 2; Rn. 90, 148–160) ---------------------------------------------------------
    ("[a3]Und die Gleichheit? Artikel drei Absatz eins: Alle Menschen sind vor dem Gesetz gleich. [nur12]Für die Kneipen "
     "stützt das Gericht sein Ergebnis allein auf Artikel zwölf. [disko3]Anders bei der Diskothek: Ihr wird eine Ausnahme "
     "vorenthalten, die anderen Gaststätten offensteht, [begue]ein gleichheitswidriger Begünstigungsausschluss. [streng]Weil "
     "das die Berufsfreiheit trifft, gilt ein strenger Maßstab.", P),
    ("[jugend]Der Jugendschutz trägt den Ausschluss nicht: Es genügt, Raucherräume nur dort zu verbieten, wo Minderjährige "
     "Zutritt haben. [tanz]Gegen Nachahmeffekte genügt ein milderes Mittel, etwa ein Raucherraum ohne Tanzfläche. [a123]Also ist der Ausschluss "
     "unvereinbar mit Artikel zwölf Absatz eins in Verbindung mit Artikel drei Absatz eins.", PS),
    # --- G Tenor und Übergangsregelung (Tenor; Rn. 161–169) -------------------------------------------------------------
    ("[tenor]Die Vorschriften sind mit dem Grundgesetz unvereinbar, aber nicht nichtig. [frist]Bis Ende zweitausendneun "
     "mussten die Länder neu regeln: [weg1]entweder ein striktes Verbot ohne Ausnahmen [weg2]oder Ausnahmen, die "
     "folgerichtig auch die kleinen Kneipen erfassen.", P),
    ("[zwischen]Bis dahin blieb das Verbot anwendbar, mit einer Übergangsregelung des Gerichts: [ue1]Einraumkneipen unter "
     "fünfundsiebzig Quadratmetern Gastfläche ohne zubereitete Speisen durften das Rauchen erlauben, [ue2]wenn sie "
     "Minderjährige nicht einließen und als Rauchergaststätte gekennzeichnet waren. [ue3]Diskotheken nur für Erwachsene "
     "durften einen Raucherraum ohne Tanzfläche einrichten.", P),
    # --- H Zurück zu Alfons; heute -----------------------------------------------------------------------------------------
    ("[alfons]Und Alfons? [alf2]In der Übergangszeit darf er selbst wählen, ob seine Kneipe eine Raucherkneipe ist, "
     "wenn er keine zubereiteten Speisen anbietet, Minderjährige nicht einlässt und das an der Tür kennzeichnet. [heute]Heute regelt jedes Land den Nichtraucherschutz in Gaststätten selbst, und jede Ausnahme muss diesem "
     "Maßstab genügen.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Folgerichtigkeit in der Angemessenheit, wie das Gericht. [tipp2]Frag: Wie streng "
     "verfolgt der Gesetzgeber sein Ziel selbst? Lässt er Ausnahmen zu, wiegen die Lasten derer schwerer, die von ihnen "
     "nichts haben. [tipp3]Den Gleichheitssatz prüfst du gesondert, wenn einer Gruppe eine Ausnahme vorenthalten wird.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Schutzbereich der Berufsfreiheit. [k2]Römisch zwei: Eingriff, hier eine "
     "Berufsausübungsregelung. [k3]Römisch drei: Rechtfertigung, mit gesetzlicher Grundlage, [k4]legitimem Ziel, Eignung "
     "und Erforderlichkeit [k5]und Angemessenheit, samt Folgerichtigkeit. [k6]Römisch vier: Gleichheitssatz, wenn eine "
     "Ausnahme vorenthalten wird.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein striktes Rauchverbot darf der Gesetzgeber wählen. [m2]Lässt er Ausnahmen zu, muss er sie "
     "folgerichtig gestalten, sonst trifft die Last unzumutbar die kleinen Betriebe, die von der Ausnahme nichts haben.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
