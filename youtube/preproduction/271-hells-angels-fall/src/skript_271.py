"""Folge 271 · Hells-Angels-Fall: Schüsse auf das SEK – Erlaubnistatbestandsirrtum (Mo · Der Fall · StGB AT · Klassiker-Fall).
Fiktiver Rahmen, der dem echten Fall folgt: BGH, Urt. v. 2.11.2011 – 2 StR 375/11 (Randnummern nach der amtlichen Fassung auf
bundesgerichtshof.de; HRRS zählt anders) und Pressemitteilung Nr. 174/2011. Elmar (führendes Mitglied eines Rockerclubs) und
Gabi (seine Verlobte) sind erfundene Figuren; keine echten Namen, keine Clubsymbole. Ablauf: Hook (Rn. 6–9) → Hintergrund
(Rn. 7, 9) → LG/BGH, Frage → Sachverhalt → § 212 (Rn. 9: billigend in Kauf) → § 32 Abs. 2 (Wortlautkarte), Notwehr gegen
Polizei offen (Rn. 19 f.) → vorgestellte Lage (Rn. 9, 22) → Erforderlichkeit aus seiner Sicht, Warnschuss (Rn. 22–24) →
ETI, § 16 Abs. 1 (Wortlautkarte), Vorsatzschuld entfällt (Rn. 21, 24), Verweis 231 → § 222 (Rn. 25 f.) → Kritik (Rotsch,
ZJS 2012, 109) → Klausurtipp, Schema, Merksatz (Lexi). Belege je Cue: ../RECHTSSTAND.md.
DARSTELLUNG: kein Schuss, kein Mündungsfeuer, keine Waffe im Bild, keine Verletzten; der getroffene Beamte wird nur erwähnt.
Stimmen (Pool niklas, helmut, ela_froh, julia): Elmar niklas (Mann, jung), Gabi julia (Frau, jung). Erzählerin und Lexi:
Carla ohne Rolle. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Elmar": "niklas", "Gabi": "julia"}

SEGMENTE = [
    # --- A1 Fall: Schlafzimmer, frühmorgens --------------------------------------------------------------------------------
    ("[fall]Frühmorgens, gegen sechs Uhr, es dämmert. [gabi]Gabi wacht auf: Unten an der Haustür knackt es laut.", 0.2),
    ("[ga1]Elmar, wach auf! Da ist jemand an der Tür!", P, "Gabi"),
    ("[elmar]Elmar ist ein führendes Mitglied eines Rockerclubs. [geruecht]Seit Wochen gibt es Gerüchte, ein verfeindeter "
     "Club wolle einen von ihnen töten. Am Vortag bekam er neue Hinweise. [fenster]Er schaut aus dem Fenster, erkennt aber "
     "niemanden. [ueberfall]Er glaubt: Jetzt kommt der Überfall. [pistole]Er nimmt seine Pistole, für die er eine Erlaubnis "
     "hat. [handy]Gabi schickt er zurück ins Schlafzimmer: Sie soll mit dem Handy die Familie verständigen.", 0.2),
    # --- A2 Fall: Flur, Treppe, Haustür ------------------------------------------------------------------------------------
    ("[licht]Im Flur schaltet er das Licht ein und geht die Treppe hinunter. [knack]Trotzdem wird draußen weiter an der Tür "
     "gearbeitet. [umriss]Durch das Glas sieht er nur Umrisse. [keine]Für ihn steht fest: Das sind keine normalen Einbrecher, "
     "das sind die Rivalen.", 0.2),
    ("[el1]Verschwindet!", P, "Elmar"),
    ("[nichts]Draußen hört ihn niemand. [schuss]Er rechnet damit, gleich durch die Tür beschossen zu werden, und schießt "
     "zweimal auf die geschlossene Tür. [beamter]Der zweite Schuss trifft einen Polizeibeamten tödlich. [polizei]Erst jetzt "
     "ruft ein anderer Beamter: Hier ist die Polizei! [weg]Elmar legt die Waffe sofort weg.", 0.2),
    ("[el2]Warum habt ihr nicht geklingelt?", P, "Elmar"),
    ("[sek]Draußen stand ein Spezialeinsatzkommando. [durchs]Es sollte sein Haus durchsuchen und ihn dafür im Schlaf "
     "überraschen. [verdeckt]Auch als das Licht anging, gaben sich die Beamten nicht zu erkennen.", P),
    # --- A3 Die Frage ------------------------------------------------------------------------------------------------------
    ("[lg]Das Landgericht verurteilte Elmar wegen Totschlags: Selbst in der vorgestellten Lage hätte er zuerst einen "
     "Warnschuss abgeben müssen. [bgh]Der Bundesgerichtshof sprach ihn vom Totschlag frei, im sogenannten Hells-Angels-Fall. "
     "[frage]Durfte er sich eine Notwehrlage vorstellen, und musste er vorher warnen?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand § 212 ------------------------------------------------------------------------------------------------
    ("[tb]Zuerst Totschlag, Paragraf zweihundertzwölf: Elmar hat einen Menschen getötet und dabei billigend in Kauf "
     "genommen, jemanden tödlich zu treffen. [ident]Dass er einen Polizisten traf statt eines Rivalen, ist ein unbeachtlicher "
     "Irrtum über die Person.", P),
    # --- D Rechtswidrigkeit: § 32 Abs. 2 (Wortlautkarte), Notwehr gegen die Polizei offen ---------------------------------
    ("[rw]War er durch Notwehr gerechtfertigt? [p32]Paragraf zweiunddreißig, Absatz zwei: Notwehr ist die Verteidigung, die "
     "erforderlich ist, um einen gegenwärtigen rechtswidrigen Angriff von sich oder einem anderen abzuwenden. "
     "[poli]Gegen die Polizei gibt es Notwehr nur, wenn ihr Einsatz in seiner konkreten Gestalt rechtswidrig war. "
     "[zweifel]Zweifel gab es, denn eine Durchsuchung ist grundsätzlich offen durchzuführen. [offen]Der Bundesgerichtshof "
     "ließ das offen: Jedenfalls lag ein Erlaubnistatbestandsirrtum vor.", P),
    # --- E Vorgestellte Lage -----------------------------------------------------------------------------------------------
    ("[vorst]Denn Elmar stellte sich einen Überfall der Rivalen vor. [akut]Die Tür war fast aufgebrochen, er rechnete mit "
     "mehreren bewaffneten Angreifern. [lage]Das wäre ein gegenwärtiger rechtswidriger Angriff auf sein Leben und das von "
     "Gabi. [spaeter]Ob er den Irrtum hätte vermeiden können, prüfen wir später bei der Fahrlässigkeit.", P),
    # --- F Erforderlichkeit aus seiner Sicht: Warnschuss? -------------------------------------------------------------------
    ("[erf]Aber war der Schuss nach seiner Vorstellung erforderlich? [regel]Der Angegriffene darf das Mittel wählen, das die "
     "Gefahr sicher beendet. In der Regel muss er eine Schusswaffe aber zuerst androhen oder einen Warnschuss abgeben. "
     "[geeignet]Das gilt nur, wenn ein Warnschuss den Angriff auch beenden würde. [hier]Elmar erwartete das Gegenteil: Die "
     "Angreifer würden dann durch die Tür schießen. Zeit zum Abwägen blieb ihm nicht. [kampf]Auf einen Kampf mit "
     "ungewissem Ausgang muss sich niemand einlassen. [ruf]Gerufen hatte er ohnehin, ohne Wirkung. [erfja]Aus seiner Sicht "
     "waren beide Schüsse erforderlich.", P),
    # --- G Folge: ETI, § 16 Abs. 1 (Wortlautkarte) -------------------------------------------------------------------------
    ("[eti]Damit liegt ein Erlaubnistatbestandsirrtum vor. [p16]Paragraf sechzehn, Absatz eins: Wer bei Begehung der Tat "
     "einen Umstand nicht kennt, der zum gesetzlichen Tatbestand gehört, handelt nicht vorsätzlich. Die Strafbarkeit wegen "
     "fahrlässiger Begehung bleibt unberührt. [entspr]Der Bundesgerichtshof wendet das entsprechend an: Die Vorsatzschuld "
     "entfällt, ein Totschlag scheidet aus. [streit]Wie man das genau begründet, ist ein Theorienstreit, den Folge "
     "zweihunderteinunddreißig erklärt.", P),
    # --- H Fahrlässige Tötung § 222 ----------------------------------------------------------------------------------------
    ("[fahr]Bleibt die fahrlässige Tötung, Paragraf zweihundertzweiundzwanzig. Sie läge nur vor, wenn Elmar seinen Irrtum "
     "hätte vermeiden können. [unverm]Das verneinte der Bundesgerichtshof: Elmar ging aus plausiblen Gründen von einem "
     "lebensbedrohlichen Überfall aus. [nicht_erk]Und weil sich die Beamten nicht zu erkennen gaben, konnte er den "
     "Polizeieinsatz nicht rechtzeitig erkennen. [frei]Deshalb: Freispruch.", PS),
    # --- I Kritik (ein Satz, Beleg Rotsch, ZJS 2012, 109) -----------------------------------------------------------------
    ("[kritik]Der Freispruch sorgte bundesweit für Empörung, [lehre]eine Urteilsbesprechung in der Fachliteratur hält ihn "
     "dagegen für richtig und bedauert eher, dass offenblieb, ob der Einsatz rechtmäßig war.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst die echte Notwehr. Bei einem Polizeieinsatz heißt das: War er rechtmäßig? "
     "[k1]Nur wenn keine Notwehrlage besteht, kommt es auf den Irrtum an. [k2]Dann prüfst du alle Notwehrmerkmale auf "
     "Grundlage der Vorstellung des Täters, auch die Erforderlichkeit. [k3]Wäre der Schuss selbst nach seiner Vorstellung "
     "nicht erforderlich gewesen, irrt er über die Grenzen der Notwehr: ein Fall von Paragraf siebzehn. [k4]So sah es das "
     "Landgericht und hielt diesen Irrtum für vermeidbar.", P),
    # --- K Gutachtenaufbau (Lexi), progressiv ------------------------------------------------------------------------------
    ("[sch]Dein Aufbau: [s1]Erstens Totschlag: Der Tatbestand ist erfüllt. [s2]Zweitens Rechtswidrigkeit: Die Notwehr "
     "scheitert, wenn der Einsatz rechtmäßig war. [s3]Drittens Schuld: Erlaubnistatbestandsirrtum, die Vorsatzschuld "
     "entfällt. [s4]Danach die fahrlässige Tötung: Der Irrtum war unvermeidbar, also straflos.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Beim Erlaubnistatbestandsirrtum misst du die Notwehr an der Vorstellung des Täters, auch die "
     "Erforderlichkeit. [m2]Passt alles, entfällt die Vorsatzschuld. Fahrlässig strafbar ist er nur, wenn er den Irrtum "
     "hätte vermeiden können.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
