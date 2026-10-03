"""Folge 118 · Parteiengleichheit: Stadthalle für eine umstrittene Partei? (Mo · Der Fall · Klassiker-Fall · Kommunalrecht).
Fiktiver Fall nach dem Plan-Hook („Eine vom Verfassungsschutz beobachtete Partei will ihren Landesparteitag in der
Stadthalle abhalten“), Vorbild sachlich: Stadthalle Wetzlar, BVerfG (K), Beschl. v. 24.3.2018 – 1 BvQ 18/18.
Fiktive Partei mit neutralem Namen und Symbol: „Weitblick-Partei“ (Symbol Berg, weiß/grau, keine Farbe realer Parteien).
Beispielland Nordrhein-Westfalen (§ 8 Abs. 2, 4 GO NRW), offen gelegt; Normtabelle nur mit am Wortlaut geprüften Normen
(NRW, Niedersachsen, Sachsen, Brandenburg), übrige Länder ohne Paragrafen mit Prüfhinweis.
Kern: Anspruchsgrundlage GO NRW (Wortlautkarte) + § 5 Abs. 1 PartG (Wortlautkarte) → Widmung und Vergabepraxis,
Widmungsänderung aus konkretem Anlass (VG Minden 2 L 353/23 Rn. 42, 44, 50 f.; Nds. OVG 10 ME 75/22, Leitsatz 1)
→ Parteienprivileg Art. 21 Abs. 4 GG (Wortlautkarte; BVerfGE 40, 287 Rn. 16, 19; BVerfGE 144, 20 Rn. 526;
2 BvB 1/19 Rn. 224), Abs. 3 ein Satz → Grenzen (§ 5 Abs. 3 PartG; OVG NRW 15 B 144/24 Rn. 21, 24) → Ergebnis →
Durchsetzung § 123 VwGO (15 B 144/24 Rn. 29, 32) → Wetzlar (1 BvQ 18/18 Rn. 1, 2, 5, Tenor; PM 16/2018, 26/2018)
→ Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Hartmut (nie im Genitiv mit -s).
Bürgermeisterin und Richterin bleiben ohne Namen (Funktionsrollen); die Stadt bleibt ohne Namen.
Stimmen: Hartmut christian; Bürgermeisterin hilde; Richterin lucy (stephan nicht verwendet: klingt wie christian).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Hartmut": "christian", "Bürgermeisterin": "hilde", "Richterin": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Antrag im Rathaus ----------------------------------------------------------------------------------
    ("[fall]Die Weitblick-Partei will im März ihren Landesparteitag in der Stadthalle abhalten. [sitz]Ihr Landesverband hat "
     "seinen Sitz in der Stadt. [beob]Der Verfassungsschutz des Landes beobachtet sie. [nichtverb]Verboten ist sie "
     "nicht.", 0.3),
    ("[h1]Wir beantragen die Stadthalle für einen Samstag im März, für vierhundert Delegierte.", 0.3, "Hartmut"),
    ("[frei]Der Saal fasst achthundert Menschen, der Termin ist frei. [vorher]Im letzten Jahr haben zwei andere Parteien "
     "hier ihre Parteitage abgehalten.", 0.3),
    ("[b1]Diese Partei wird vom Verfassungsschutz beobachtet. Unsere Halle bekommt sie nicht.", 0.3, "Bürgermeisterin"),
    # --- A2 Fall: Ratsbeschluss und Eilantrag -------------------------------------------------------------------------------
    ("[rat]Eine Woche später beschließt der Stadtrat: [ratb]Die Stadthalle steht künftig nicht mehr für "
     "Parteiveranstaltungen zur Verfügung. [eilan]Die Partei beantragt beim Verwaltungsgericht eine einstweilige Anordnung.",
     0.3),
    ("[frage]Darf die Stadt Nein sagen? [frage2]Es geht um die Gleichbehandlung der Parteien. [vorbild]Vorbild ist ein "
     "echter Fall aus Wetzlar.", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Anspruchsgrundlage: Gemeindeordnung (Beispiel NRW) und Normtabelle ------------------------------------------------
    ("[anspr]Wir prüfen den Anspruch auf Zulassung. [land]Kommunalrecht ist Landesrecht; unser Beispiel ist "
     "Nordrhein-Westfalen, in deinem Land oft unter anderer Nummer. [p8]Nach Paragraf acht Absatz zwei der Gemeindeordnung "
     "sind alle Einwohner im Rahmen des geltenden Rechts berechtigt, die öffentlichen Einrichtungen zu "
     "benutzen. [p8iv]Nach Absatz vier gilt das entsprechend für Personenvereinigungen, also für den Landesverband mit Sitz "
     "in der Stadt. [oe]Die Stadthalle ist eine öffentliche Einrichtung. [rahmen]Im Rahmen des geltenden Rechts heißt: im "
     "Rahmen von Widmung und Kapazität.", PS),
    ("[tabelle]Andere Länder regeln das ähnlich, siehe Beschreibung. [a28]Ob die Stadt ihre Halle für Parteien "
     "öffnet, entscheidet sie in ihrer Selbstverwaltung, Artikel achtundzwanzig Absatz zwei Grundgesetz, aber nicht "
     "beliebig.", PS),
    # --- E § 5 Abs. 1 PartG ----------------------------------------------------------------------------------------------
    ("[p5]Paragraf fünf Absatz eins Parteiengesetz: Wenn ein Träger öffentlicher Gewalt den Parteien Einrichtungen zur "
     "Verfügung stellt, sollen alle Parteien gleichbehandelt werden. [chanc]Dahinter steht die Chancengleichheit der "
     "Parteien, Artikel drei und einundzwanzig Grundgesetz. [ohnesitz]Das hilft auch Parteien ohne Sitz in der Stadt.", PS),
    # --- F Widmung und Vergabepraxis, Widmungsänderung ---------------------------------------------------------------------
    ("[widm]Erster Prüfpunkt: die Widmung. Sie kann sich aus der Vergabepraxis ergeben. [praxis]Die Stadt hat die Halle "
     "schon zwei Parteien für Parteitage überlassen. [imzweck]Ein Landesparteitag liegt also im Widmungszweck. [ratsb]Und "
     "der Ratsbeschluss? [anlass]Er kam erst nach dem Antrag. Die Widmung zu ändern, nur um den Antrag einer bestimmten "
     "Partei abzulehnen, verstößt gegen die Gleichbehandlung der Parteien. [alt]Über den gestellten Antrag wird nach den "
     "alten Regeln entschieden. [zukunft]Für die Zukunft darf die Stadt die Halle für alle Parteien schließen, aber nicht "
     "gezielt für eine.", PS),
    # --- G Parteienprivileg Art. 21 Abs. 4 GG, Verfassungsschutz, Abs. 3 ---------------------------------------------------
    ("[privi]Zweiter Prüfpunkt: der Verfassungsschutz. [p21]Artikel einundzwanzig Absatz vier Grundgesetz: Über die Frage "
     "der Verfassungswidrigkeit entscheidet das Bundesverfassungsgericht. [bisdahin]Bis dahin darf die Verwaltung eine "
     "Partei nicht wegen ihrer Ziele benachteiligen; [bekaempf]sie darf politisch bekämpft, aber nicht behindert werden. "
     "[vs]Auch die Beobachtung ändert daran nichts: Sie ist eine Einschätzung der Behörde, kein Urteil über die "
     "Verfassungswidrigkeit. [keinnach]Rechtliche Nachteile darf die Stadt daran nicht knüpfen. [abs3]Absatz drei, der "
     "Ausschluss von der staatlichen Finanzierung, betrifft anderes; auch darüber entscheidet allein Karlsruhe.", PS),
    # --- H Grenzen und Ergebnis ------------------------------------------------------------------------------------------
    ("[grenz]Grenzenlos ist der Anspruch nicht. [kap]Ist der Termin schon vergeben, zählt meist, wer zuerst angefragt "
     "hat. [aufl]Sachliche Bedingungen wie ein Sicherheitskonzept sind erlaubt, wenn sie für alle Parteien "
     "gelten. [gefahr]Und Gegendemonstrationen? Gefahren abzuwehren ist Sache der Polizei; ablehnen darf die Stadt erst im "
     "polizeilichen Notstand. [hier]Hier ist der Termin frei, und konkrete Gefahren fehlen.", P),
    ("[erg]Ergebnis: Die Weitblick-Partei hat einen Anspruch auf Zulassung zur Stadthalle.", PS),
    # --- I Durchsetzung: § 123 VwGO --------------------------------------------------------------------------------------
    ("[eil]Ein Urteil käme zu spät. Deshalb der Eilantrag nach Paragraf hundertdreiundzwanzig "
     "Verwaltungsgerichtsordnung. [ao]Anordnungsanspruch ist der Zulassungsanspruch, [ag]Anordnungsgrund der nahe Termin, "
     "der hier ausnahmsweise die Vorwegnahme der Hauptsache rechtfertigt.", P),
    ("[r1]Die Stadt wird verpflichtet, der Partei die Stadthalle zu überlassen.", 0.4, "Richterin"),
    # --- J Wetzlar: Bindung an Gerichtsentscheidungen ---------------------------------------------------------------------
    ("[wetz]Und wenn die Stadt nicht folgt? So war es in Wetzlar. [wetz2]Das Verwaltungsgericht verpflichtete die Stadt "
     "vorläufig, einer Partei die Stadthalle für eine Wahlkampfveranstaltung zu überlassen; [vgh]der "
     "Verwaltungsgerichtshof bestätigte das. [verw]Die Stadt verweigerte den Zugang trotzdem, mit der Begründung, Nachweise "
     "zu Versicherung und Sanitätsdienst fehlten. [zwang]Es folgte ein Zwangsgeld. [karls]Am Tag der Veranstaltung gab das "
     "Bundesverfassungsgericht der Stadt auf, der Entscheidung zu folgen. [nicht]Auch das befolgte sie nicht.", P),
    ("[gruende]Karlsruhe stellte fest: Ihre Gründe hatte sie vor Gericht nicht rechtzeitig vorgebracht, oder die Gerichte hielten sie für "
     "unerheblich. [verl]Das verletzt voraussichtlich die Versammlungsfreiheit, zusammen mit der Bindung an Gesetz und Recht "
     "und dem effektiven Rechtsschutz. [fehl]Später sprach das Gericht von Fehlvorstellungen über die "
     "Bindungskraft richterlicher Entscheidungen. [a203]Die Verwaltung ist an Gesetz und Recht gebunden, "
     "Artikel zwanzig Absatz drei; eine vollziehbare Gerichtsentscheidung muss sie befolgen.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: erst die Gemeindeordnung, dann Paragraf fünf Parteiengesetz. [tipp2]Achte auf die "
     "Daten: Kommt der Ratsbeschluss nach dem Antrag, spricht das für eine Widmungsänderung aus konkretem Anlass. "
     "[tipp3]Und ob die Partei verfassungswidrig ist, prüfst du nicht; das entscheidet allein Karlsruhe.", PS),
    # --- L Prüfschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für den Zulassungsanspruch. [s1]Römisch eins: Anspruchsgrundlage, Gemeindeordnung und "
     "Parteiengesetz. [s2]Römisch zwei: öffentliche Einrichtung und Berechtigter. [s3]Römisch drei: "
     "Widmung, Vergabepraxis, Widmungsänderung. [s4]Römisch vier: kein sachlicher Grund dagegen; die Ziele der "
     "Partei zählen nicht. [s5]Römisch fünf: Durchsetzung nach Paragraf "
     "hundertdreiundzwanzig.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Bis das Bundesverfassungsgericht eine Partei verbietet, darf die Stadt sie nicht wegen ihrer "
     "Ziele benachteiligen. [m2]Wer die Halle anderen Parteien überlässt, muss sie auch ihr überlassen. [m3]Und eine "
     "Gerichtsentscheidung wird befolgt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
