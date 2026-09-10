/* ==========================================================================
   Themenpool für das erste und zweite juristische Staatsexamen.

   Zuschnitt: Der Pool ist aus den bestehenden Beiträgen des Kanals abgeleitet
   – Frage-zuerst, Abgrenzungen, Definitionen, Streitstände, Meinungsstreit.
   Nicht Lehrbuch, sondern das, was in der Klausur den Unterschied macht.

   Ein Eintrag ist bewusst schlank: Titel (die Frage), die tragenden Normen,
   Examenspriorität und ein paar Stichpunkte als Gedankenstütze. Ausformuliert
   wird nichts – das macht der Autor (autor.mjs), und der Faktencheck prüft
   nach. So bleibt der Pool wartbar und der Beitrag klingt nie nach Datenbank.

   prioritaet: hoch = Dauerbrenner, mittel = regelmäßig, selten = Nische mit
   Aufmerksamkeitswert.
   ========================================================================== */

export const THEMEN = [
  /* ---- Zivilrecht: BGB AT ------------------------------------------------ */
  { fach: "bgbat", titel: "Was sind die Voraussetzungen und Rechtsfolgen einer wirksamen Anfechtung?", normen: ["§ 119 BGB", "§ 123 BGB", "§ 142 (1) BGB", "§ 143 BGB"], prioritaet: "hoch",
    kern: { lernziele: ["Anfechtungsgrund, Erklärung, Frist, Anfechtungsgegner", "Rückwirkende Nichtigkeit und § 122 BGB als Kehrseite"], pruefschritte: ["Anfechtbare Willenserklärung", "Anfechtungsgrund", "Anfechtungserklärung gegenüber dem richtigen Gegner", "Frist", "Kein Ausschluss"] } },
  { fach: "bgbat", titel: "Wie erfolgt die Abgrenzung zwischen Vertrag und Gefälligkeit?", normen: ["§ 145 BGB", "§ 241 (1) BGB"], prioritaet: "hoch",
    kern: { lernziele: ["Rechtsbindungswille als objektiver Maßstab", "Gefälligkeitsverhältnis mit rechtlichem Charakter als Zwischenstufe"] } },
  { fach: "bgbat", titel: "Inwieweit werden sich widersprechende AGB Vertragsbestandteil?", normen: ["§ 305 (2) BGB", "§ 306 BGB", "§ 154 BGB"], prioritaet: "hoch",
    kern: { lernziele: ["Theorie des letzten Wortes gegen Restgültigkeitstheorie", "Herrschend: kongruente Klauseln gelten, der Rest fällt weg"] } },
  { fach: "bgbat", titel: "Welche Formvorschriften gibt es und was ist die Folge eines Formverstoßes?", normen: ["§ 125 BGB", "§ 126 BGB", "§ 126a BGB", "§ 126b BGB", "§ 128 BGB"], prioritaet: "mittel" },
  { fach: "bgbat", titel: "Was besagt die Kipp'sche Lehre von der Doppelnichtigkeit?", normen: ["§ 134 BGB", "§ 138 BGB", "§ 142 BGB"], prioritaet: "selten" },
  { fach: "bgbat", titel: "Wie wirkt die Stellvertretung ohne Vertretungsmacht?", normen: ["§ 177 BGB", "§ 179 BGB", "§ 164 BGB"], prioritaet: "hoch" },
  { fach: "bgbat", titel: "Wann liegt ein Insichgeschäft vor und wann ist es zulässig?", normen: ["§ 181 BGB"], prioritaet: "mittel" },
  { fach: "bgbat", titel: "Worin unterscheiden sich Anfechtung und Wegfall der Geschäftsgrundlage?", normen: ["§ 119 (2) BGB", "§ 313 BGB"], prioritaet: "hoch" },

  /* ---- Zivilrecht: Schuldrecht AT ---------------------------------------- */
  { fach: "schuld", titel: "Welche Arten der Leistungsstörung gibt es?", normen: ["§ 275 BGB", "§ 280 BGB", "§ 286 BGB", "§ 323 BGB"], prioritaet: "hoch",
    kern: { lernziele: ["Unmöglichkeit, Verzug, Schlechtleistung, Nebenpflichtverletzung", "Immer zuerst: Welcher Anspruch, welche Pflicht, welche Störung?"] } },
  { fach: "schuld", titel: "Wann liegt Annahmeverzug vor?", normen: ["§ 293 BGB", "§ 294 BGB", "§ 295 BGB", "§ 296 BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Was sind die Rechtsfolgen des Annahmeverzugs?", normen: ["§ 300 BGB", "§ 301 BGB", "§ 302 BGB", "§ 304 BGB", "§ 326 (2) BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Was ist der Unterschied zwischen dem Schuldner- und dem Gläubigerverzug?", normen: ["§ 286 BGB", "§ 293 BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Wann tritt Konkretisierung bei Hol-, Bring- und Schickschulden ein?", normen: ["§ 243 (2) BGB", "§ 269 BGB", "§ 447 BGB"], prioritaet: "hoch",
    kern: { lernziele: ["Konkretisierung setzt das zur Leistung Erforderliche voraus", "Bei der Schickschuld: Übergabe an die Transportperson"] } },
  { fach: "schuld", titel: "Was ist der Unterschied zwischen dem Ersatz des positiven und des negativen Interesses?", normen: ["§ 249 BGB", "§ 122 BGB", "§ 284 BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Was besagt die Lehre vom fehlerhaften Vertrag?", normen: ["§ 142 BGB", "§ 611a BGB"], prioritaet: "mittel" },
  { fach: "schuld", titel: "Wann haftet man für das Verschulden eines Erfüllungsgehilfen?", normen: ["§ 278 BGB", "§ 831 BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Wie prüft man einen Anspruch aus culpa in contrahendo?", normen: ["§ 311 (2) BGB", "§ 241 (2) BGB", "§ 280 (1) BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Was besagt die Saldotheorie?", normen: ["§ 812 BGB", "§ 818 (3) BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Wann ist ein Vertrag zugunsten Dritter echt und wann unecht?", normen: ["§ 328 BGB", "§ 329 BGB"], prioritaet: "mittel" },
  { fach: "schuld", titel: "Was ist ein Vertrag mit Schutzwirkung zugunsten Dritter?", normen: ["§ 311 (3) BGB", "§ 328 BGB"], prioritaet: "hoch" },

  /* ---- Zivilrecht: Schuldrecht BT ---------------------------------------- */
  { fach: "schuldbt", titel: "Welche Kaufarten sind im BGB geregelt?", normen: ["§ 433 BGB", "§ 453 BGB", "§ 474 BGB", "§ 481 BGB"], prioritaet: "mittel" },
  { fach: "schuldbt", titel: "Wie ist der geminderte Kaufpreis nach § 441 (3) BGB zu berechnen?", normen: ["§ 441 (3) BGB", "§ 437 Nr. 2 BGB"], prioritaet: "mittel",
    kern: { lernziele: ["Verhältnisrechnung: Kaufpreis mal Istwert geteilt durch Sollwert", "Nicht der Mangelbeseitigungsaufwand ist der Maßstab"] } },
  { fach: "schuldbt", titel: "Wie werden Dienst- und Werkvertrag voneinander abgegrenzt?", normen: ["§ 611 BGB", "§ 631 BGB"], prioritaet: "hoch" },
  { fach: "schuldbt", titel: "Wann kann der Käufer ohne Fristsetzung zurücktreten?", normen: ["§ 323 (2) BGB", "§ 440 BGB", "§ 326 (5) BGB"], prioritaet: "hoch" },
  { fach: "schuldbt", titel: "Was gilt beim Verbrauchsgüterkauf anders?", normen: ["§ 474 BGB", "§ 475 BGB", "§ 477 BGB"], prioritaet: "hoch" },
  { fach: "schuldbt", titel: "Ist Vertragspartner des Anwalts stets der Mandant?", normen: ["§ 675 BGB", "§ 611 BGB"], prioritaet: "selten" },
  { fach: "schuldbt", titel: "Lohnt sich ein langjähriger Ratenkauf?", normen: ["§ 491 BGB", "§ 355 BGB"], prioritaet: "selten" },

  /* ---- Zivilrecht: Sachenrecht ------------------------------------------- */
  { fach: "sachen", titel: "Welche Vermutungen enthält § 1006 BGB?", normen: ["§ 1006 BGB", "§ 985 BGB"], prioritaet: "mittel" },
  { fach: "sachen", titel: "Welche dinglichen Rechte gibt es?", normen: ["§ 903 BGB", "§ 1018 BGB", "§ 1113 BGB", "§ 1204 BGB"], prioritaet: "mittel" },
  { fach: "sachen", titel: "Welche Ausnahmen gibt es zur Sperrwirkung des EBV im Deliktsrecht?", normen: ["§ 993 (1) BGB", "§ 992 BGB", "§ 823 BGB"], prioritaet: "hoch",
    kern: { lernziele: ["Nicht-so-berechtigter Besitzer, Fremdbesitzerexzess, deliktischer Besitzerwerb"] } },
  { fach: "sachen", titel: "Wann ist ein gutgläubiger Erwerb ausgeschlossen?", normen: ["§ 932 BGB", "§ 935 BGB", "§ 936 BGB"], prioritaet: "hoch" },
  { fach: "sachen", titel: "Wie funktioniert das Anwartschaftsrecht beim Eigentumsvorbehalt?", normen: ["§ 449 BGB", "§ 929 BGB", "§ 158 (1) BGB"], prioritaet: "hoch" },
  { fach: "sachen", titel: "Wie prüft man den Herausgabeanspruch aus § 985 BGB?", normen: ["§ 985 BGB", "§ 986 BGB"], prioritaet: "hoch" },

  /* ---- Zivilrecht: Deliktsrecht ------------------------------------------ */
  { fach: "delikt", titel: "Trifft Fahrradfahrer ein Mitverschulden bei fehlendem Helm?", normen: ["§ 254 BGB", "§ 823 (1) BGB"], prioritaet: "selten" },
  { fach: "delikt", titel: "Wann haftet der Geschäftsherr nach § 831 BGB und wann kann er sich entlasten?", normen: ["§ 831 BGB", "§ 278 BGB"], prioritaet: "hoch" },
  { fach: "delikt", titel: "Was ist das Recht am eingerichteten und ausgeübten Gewerbebetrieb?", normen: ["§ 823 (1) BGB"], prioritaet: "mittel" },
  { fach: "delikt", titel: "Wie prüft man die Verkehrssicherungspflicht?", normen: ["§ 823 (1) BGB"], prioritaet: "hoch" },
  { fach: "delikt", titel: "Wann greift die Produzentenhaftung neben dem ProdHaftG?", normen: ["§ 823 (1) BGB", "§ 1 ProdHaftG"], prioritaet: "mittel" },

  /* ---- Zivilrecht: Arbeitsrecht ------------------------------------------ */
  { fach: "arbeit", titel: "Was sind die wichtigsten Rechtsfolgen einer Schwangerschaft im Arbeitsrecht?", normen: ["§ 17 MuSchG", "§ 3 MuSchG", "§ 15 BEEG"], prioritaet: "mittel" },
  { fach: "arbeit", titel: "Wie prüft man die Wirksamkeit einer ordentlichen Kündigung?", normen: ["§ 1 KSchG", "§ 623 BGB", "§ 102 BetrVG"], prioritaet: "hoch" },
  { fach: "arbeit", titel: "Wann ist eine außerordentliche Kündigung gerechtfertigt?", normen: ["§ 626 BGB"], prioritaet: "hoch" },
  { fach: "arbeit", titel: "Wie grenzt man Arbeitnehmer und freien Mitarbeiter ab?", normen: ["§ 611a BGB"], prioritaet: "hoch" },

  /* ---- Zivilrecht: Familien- und Erbrecht -------------------------------- */
  { fach: "famerb", titel: "Was bedeutet „angemessen“ i.S.d. § 1357 BGB?", normen: ["§ 1357 BGB"], prioritaet: "mittel" },
  { fach: "famerb", titel: "Müssen Kinder im Haushalt helfen?", normen: ["§ 1619 BGB"], prioritaet: "selten" },
  { fach: "famerb", titel: "Wie wird der Pflichtteil berechnet?", normen: ["§ 2303 BGB", "§ 2311 BGB", "§ 2325 BGB"], prioritaet: "mittel" },
  { fach: "famerb", titel: "Worin unterscheiden sich Vor- und Nacherbe von Erbe und Vermächtnisnehmer?", normen: ["§ 2100 BGB", "§ 1939 BGB", "§ 2174 BGB"], prioritaet: "mittel" },

  /* ---- Zivilrecht: Handels- und Gesellschaftsrecht ------------------------ */
  { fach: "handelsg", titel: "Wann liegt ein Handelsgeschäft vor und was folgt daraus?", normen: ["§ 343 HGB", "§ 377 HGB"], prioritaet: "hoch" },
  { fach: "handelsg", titel: "Wie haftet der Gesellschafter einer GbR nach der Reform?", normen: ["§ 721 BGB", "§ 128 HGB"], prioritaet: "hoch" },
  { fach: "handelsg", titel: "Was ist die Rechtsscheinhaftung im Handelsrecht?", normen: ["§ 5 HGB", "§ 15 HGB"], prioritaet: "mittel" },

  /* ---- Zivilrecht: ZPO --------------------------------------------------- */
  { fach: "zpo", titel: "Was bedeuten Anhängigkeit und Rechtshängigkeit?", normen: ["§ 253 (1) ZPO", "§ 261 ZPO", "§ 262 ZPO"], prioritaet: "hoch",
    kern: { lernziele: ["Anhängigkeit ab Einreichung, Rechtshängigkeit ab Zustellung", "Rechtsfolgen: Verjährungshemmung, Verbot doppelter Rechtshängigkeit"] } },
  { fach: "zpo", titel: "Worauf kommt es für den rechtzeitigen Eingang eines per Telefax übermittelten Schriftsatzes bei Gericht an?", normen: ["§ 130 ZPO", "§ 130a ZPO"], prioritaet: "mittel" },
  { fach: "zpo", titel: "Was sind die allgemeinen Voraussetzungen der Zwangsvollstreckung?", normen: ["§ 704 ZPO", "§ 750 ZPO", "§ 794 ZPO"], prioritaet: "hoch",
    kern: { lernziele: ["Titel, Klausel, Zustellung als Dreiklang"] } },
  { fach: "zpo", titel: "Was sind die Voraussetzungen eines Versäumnisurteils gegen den Beklagten?", normen: ["§ 331 ZPO", "§ 335 ZPO"], prioritaet: "hoch" },
  { fach: "zpo", titel: "Wie ist der Instanzenzug im Zivilprozess?", normen: ["§ 511 ZPO", "§ 542 ZPO", "§ 23 GVG", "§ 71 GVG"], prioritaet: "mittel" },
  { fach: "zpo", titel: "Wie unterscheiden sich Leistungs-, Feststellungs- und Gestaltungsklage?", normen: ["§ 253 ZPO", "§ 256 ZPO"], prioritaet: "hoch" },

  /* ---- Strafrecht AT ------------------------------------------------------ */
  { fach: "strafat", titel: "Was ist der Unterschied zwischen Eventualvorsatz und bewusster Fahrlässigkeit?", normen: ["§ 15 StGB", "§ 16 StGB"], prioritaet: "hoch",
    kern: { lernziele: ["Wissens- und Wollenselement", "Billigend in Kauf nehmen gegen pflichtwidriges Vertrauen"] } },
  { fach: "strafat", titel: "Welche Arten der Kausalität gibt es?", normen: ["§ 13 StGB"], prioritaet: "hoch",
    kern: { lernziele: ["Äquivalenz, kumulativ, alternativ, abgebrochen, überholend", "Objektive Zurechnung als Korrektiv"] } },
  { fach: "strafat", titel: "Was ist ein untauglicher Versuch, was ein Wahndelikt?", normen: ["§ 22 StGB", "§ 23 (3) StGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Was ist ein intensiver bzw. extensiver Notwehrexzess?", normen: ["§ 33 StGB", "§ 32 StGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Worin unterscheiden sich Einverständnis und Einwilligung?", normen: ["§ 228 StGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Worin unterscheiden sich Beschützer- und Überwachergarant?", normen: ["§ 13 StGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Wann ist ein Rücktritt vom Versuch strafbefreiend?", normen: ["§ 24 StGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Wie grenzt man Täterschaft und Teilnahme ab?", normen: ["§ 25 StGB", "§ 26 StGB", "§ 27 StGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Was ist der Erlaubnistatbestandsirrtum und wie wird er behandelt?", normen: ["§ 16 StGB", "§ 17 StGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Wie prüft man die actio libera in causa?", normen: ["§ 20 StGB", "§ 323a StGB"], prioritaet: "mittel" },
  { fach: "strafat", titel: "Welche BAK-Grenzwerte muss man kennen?", normen: ["§ 20 StGB", "§ 21 StGB", "§ 316 StGB"], prioritaet: "mittel" },

  /* ---- Strafrecht BT ------------------------------------------------------ */
  { fach: "strafbt", titel: "Wie ist das Verhältnis zwischen § 211 StGB und § 212 StGB?", normen: ["§ 211 StGB", "§ 212 StGB", "§ 28 StGB"], prioritaet: "hoch",
    kern: { lernziele: ["Rechtsprechung: eigenständiger Tatbestand", "Literatur: Qualifikation – Folgen für § 28 StGB"] } },
  { fach: "strafbt", titel: "Wann liegt Heimtücke vor?", normen: ["§ 211 (2) StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Wie grenzt man Diebstahl und Betrug ab?", normen: ["§ 242 StGB", "§ 263 StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Wann liegt eine Zueignungsabsicht vor?", normen: ["§ 242 StGB", "§ 246 StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Wie prüft man den Vermögensschaden beim Betrug?", normen: ["§ 263 StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Wann ist Raub vollendet und wie verhält er sich zur räuberischen Erpressung?", normen: ["§ 249 StGB", "§ 253 StGB", "§ 255 StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Was ist eine gefährliche Körperverletzung nach § 224 StGB?", normen: ["§ 223 StGB", "§ 224 StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Ist die Bezeichnung „Bulle“ gegenüber einem Polizisten strafbar?", normen: ["§ 185 StGB"], prioritaet: "selten" },

  /* ---- Strafprozessrecht -------------------------------------------------- */
  { fach: "stpo", titel: "Welche Beweisverwertungsverbote gibt es und wie prüft man sie?", normen: ["§ 136a StPO", "§ 100a StPO"], prioritaet: "hoch" },
  { fach: "stpo", titel: "Wann darf ohne richterliche Anordnung durchsucht werden?", normen: ["§ 102 StPO", "§ 105 StPO", "Art. 13 GG"], prioritaet: "hoch" },
  { fach: "stpo", titel: "Was sind die Voraussetzungen der Untersuchungshaft?", normen: ["§ 112 StPO", "§ 116 StPO"], prioritaet: "mittel" },

  /* ---- Öffentliches Recht: Staatsrecht ------------------------------------ */
  { fach: "staat", titel: "Was sind die wichtigsten Ausprägungen des Rechtsstaatsprinzips?", normen: ["Art. 20 (3) GG", "Art. 19 (4) GG"], prioritaet: "hoch" },
  { fach: "staat", titel: "Welche Form von Demokratie sieht das Grundgesetz vor?", normen: ["Art. 20 (2) GG", "Art. 38 GG"], prioritaet: "mittel" },
  { fach: "staat", titel: "Wie lauten die Wahlgrundsätze und welche Bedeutung haben sie?", normen: ["Art. 38 (1) GG"], prioritaet: "mittel" },
  { fach: "staat", titel: "Welche Rechte und Pflichten hat der Bundespräsident?", normen: ["Art. 54 GG", "Art. 82 GG", "Art. 60 GG"], prioritaet: "mittel" },
  { fach: "staat", titel: "Worin unterscheiden sich echte und unechte Rückwirkung?", normen: ["Art. 20 (3) GG", "Art. 2 (1) GG"], prioritaet: "hoch" },
  { fach: "staat", titel: "Welche Bedeutung hat die Radbruch'sche Formel?", normen: ["Art. 20 (3) GG"], prioritaet: "selten" },
  { fach: "staat", titel: "Welche Gerichtsbarkeiten gibt es in Deutschland?", normen: ["Art. 95 GG", "Art. 92 GG"], prioritaet: "selten" },
  { fach: "staat", titel: "Wann gelten Vorrang und Vorbehalt des Gesetzes?", normen: ["Art. 20 (3) GG"], prioritaet: "hoch" },
  { fach: "staat", titel: "Wie prüft man die Verfassungsbeschwerde?", normen: ["Art. 93 (1) Nr. 4a GG", "§ 90 BVerfGG"], prioritaet: "hoch" },
  { fach: "staat", titel: "Wann hat der Bund die Gesetzgebungskompetenz?", normen: ["Art. 70 GG", "Art. 72 GG", "Art. 74 GG"], prioritaet: "hoch" },

  /* ---- Öffentliches Recht: Grundrechte ------------------------------------ */
  { fach: "grundr", titel: "Wie prüft man einen Eingriff in Art. 12 GG?", normen: ["Art. 12 (1) GG"], prioritaet: "hoch",
    kern: { lernziele: ["Drei-Stufen-Theorie", "Abgrenzung zu Art. 14 GG: erwerben gegen erworben"] } },
  { fach: "grundr", titel: "Wann ist Art. 2 (1) GG einschlägig und wann ein spezielleres Grundrecht?", normen: ["Art. 2 (1) GG"], prioritaet: "hoch" },
  { fach: "grundr", titel: "Wie wirken Grundrechte zwischen Privaten?", normen: ["Art. 1 (3) GG", "§ 242 BGB"], prioritaet: "hoch" },
  { fach: "grundr", titel: "Wie prüft man die Verhältnismäßigkeit?", normen: ["Art. 20 (3) GG"], prioritaet: "hoch" },
  { fach: "grundr", titel: "Was schützt die allgemeine Handlungsfreiheit nicht mehr?", normen: ["Art. 2 (1) GG", "Art. 2 (2) GG"], prioritaet: "mittel" },

  /* ---- Öffentliches Recht: Verwaltungsrecht ------------------------------- */
  { fach: "verwalt", titel: "Was ist der Unterschied zwischen Entschließungs- und Auswahlermessen?", normen: ["§ 40 VwVfG", "§ 114 VwGO"], prioritaet: "hoch" },
  { fach: "verwalt", titel: "Was ist ein Koordinations- und was ein Subordinationsvertrag i.S.d. §§ 54 ff. VwVfG?", normen: ["§ 54 VwVfG", "§ 55 VwVfG", "§ 56 VwVfG"], prioritaet: "mittel" },
  { fach: "verwalt", titel: "Welche Arten von Verwaltungsvorschriften gibt es?", normen: ["Art. 84 (2) GG", "§ 40 VwVfG"], prioritaet: "mittel" },
  { fach: "verwalt", titel: "Wann ist ein Verwaltungsakt nichtig?", normen: ["§ 44 VwVfG", "§ 43 VwVfG"], prioritaet: "hoch" },
  { fach: "verwalt", titel: "Wann darf ein rechtswidriger begünstigender Verwaltungsakt zurückgenommen werden?", normen: ["§ 48 VwVfG", "§ 49 VwVfG"], prioritaet: "hoch" },
  { fach: "verwalt", titel: "Wie prüft man die Bestimmtheit eines Verwaltungsakts?", normen: ["§ 37 VwVfG", "§ 35 VwVfG"], prioritaet: "mittel" },
  { fach: "verwalt", titel: "Welche Arten von Gemeindehoheiten gibt es?", normen: ["Art. 28 (2) GG"], prioritaet: "mittel" },

  /* ---- Öffentliches Recht: Verwaltungsprozessrecht ------------------------ */
  { fach: "vwgo", titel: "Welche Formen einer einstweiligen Anordnung gibt es nach § 123 (1) VwGO?", normen: ["§ 123 (1) VwGO"], prioritaet: "hoch" },
  { fach: "vwgo", titel: "Wann wendet man § 123 VwGO und wann § 80 (5) VwGO im einstweiligen Rechtsschutz an?", normen: ["§ 123 (5) VwGO", "§ 80 (5) VwGO"], prioritaet: "hoch",
    kern: { lernziele: ["Faustformel: Belastender VA angegriffen → § 80 (5) VwGO", "Alles andere → § 123 VwGO"] } },
  { fach: "vwgo", titel: "Wie prüft man die Zulässigkeit der Anfechtungsklage?", normen: ["§ 42 (1) VwGO", "§ 42 (2) VwGO", "§ 68 VwGO", "§ 74 VwGO"], prioritaet: "hoch" },
  { fach: "vwgo", titel: "Wann ist die Fortsetzungsfeststellungsklage statthaft?", normen: ["§ 113 (1) S. 4 VwGO"], prioritaet: "hoch" },
  { fach: "vwgo", titel: "Wie grenzt man Verpflichtungs- und allgemeine Leistungsklage ab?", normen: ["§ 42 (1) VwGO", "§ 43 VwGO"], prioritaet: "hoch" },

  /* ---- Öffentliches Recht: Europarecht ------------------------------------ */
  { fach: "europa", titel: "Welches sind die vier EU-Grundfreiheiten?", normen: ["Art. 34 AEUV", "Art. 45 AEUV", "Art. 49 AEUV", "Art. 56 AEUV", "Art. 63 AEUV"], prioritaet: "mittel" },
  { fach: "europa", titel: "Welche Organe hat die EU?", normen: ["Art. 13 EUV"], prioritaet: "mittel" },
  { fach: "europa", titel: "Wann wirkt eine Richtlinie unmittelbar?", normen: ["Art. 288 AEUV"], prioritaet: "hoch" },
  { fach: "europa", titel: "Was ist das Vorabentscheidungsverfahren?", normen: ["Art. 267 AEUV"], prioritaet: "hoch" },

  /* ---- Öffentliches Recht: Besonderes Verwaltungsrecht ------------------- */
  { fach: "verwbt", titel: "Wie prüft man die Rechtmäßigkeit einer Baugenehmigung?", normen: ["§ 29 BauGB", "§ 30 BauGB", "§ 34 BauGB", "§ 35 BauGB"], prioritaet: "hoch",
    kern: { lernziele: ["Erst die Zulässigkeit nach Planungsrecht, dann das Bauordnungsrecht des Landes", "Innenbereich, Außenbereich, Bebauungsplan – die drei Weichen"] } },
  { fach: "verwbt", titel: "Wann ist ein Vorhaben im Außenbereich zulässig?", normen: ["§ 35 (1) BauGB", "§ 35 (2) BauGB"], prioritaet: "hoch" },
  { fach: "verwbt", titel: "Was ist das Gebot der Rücksichtnahme?", normen: ["§ 15 BauNVO", "§ 34 (1) BauGB"], prioritaet: "hoch" },
  { fach: "verwbt", titel: "Wer ist Störer im Polizei- und Ordnungsrecht?", normen: ["Polizeigesetze der Länder"], prioritaet: "hoch",
    kern: { lernziele: ["Handlungsstörer, Zustandsstörer, Nichtstörer", "Unmittelbarkeitstheorie gegen Theorie der rechtswidrigen Verursachung"] } },
  { fach: "verwbt", titel: "Wann darf die Polizei einen Nichtstörer in Anspruch nehmen?", normen: ["Polizeigesetze der Länder"], prioritaet: "hoch" },
  { fach: "verwbt", titel: "Was ist der Unterschied zwischen Gefahr, Anscheinsgefahr und Gefahrenverdacht?", normen: ["Polizeigesetze der Länder"], prioritaet: "hoch" },
  { fach: "verwbt", titel: "Wie prüft man die Rechtmäßigkeit einer kommunalen Satzung?", normen: ["Art. 28 (2) GG", "Gemeindeordnungen der Länder"], prioritaet: "mittel" },
  { fach: "verwbt", titel: "Wann hat ein Gemeinderatsmitglied ein Mitwirkungsverbot?", normen: ["Gemeindeordnungen der Länder"], prioritaet: "mittel" },
  { fach: "verwbt", titel: "Was ist eine öffentliche Einrichtung und wer hat Zugang zu ihr?", normen: ["Art. 28 (2) GG", "Gemeindeordnungen der Länder"], prioritaet: "mittel" },
  { fach: "verwbt", titel: "Wie ist der Verwaltungszwang aufgebaut?", normen: ["§ 6 VwVG", "§ 13 VwVG"], prioritaet: "hoch" },

  /* ---- Weitere Dauerbrenner ---------------------------------------------- */
  { fach: "bgbat", titel: "Wann ist ein Schweigen als Willenserklärung zu werten?", normen: ["§ 151 BGB", "§ 362 HGB"], prioritaet: "mittel" },
  { fach: "bgbat", titel: "Was gilt beim Handeln unter fremdem Namen?", normen: ["§ 164 BGB", "§ 177 BGB"], prioritaet: "mittel" },
  { fach: "schuld", titel: "Wie prüft man den Rücktritt nach § 323 BGB?", normen: ["§ 323 BGB", "§ 346 BGB"], prioritaet: "hoch" },
  { fach: "schuld", titel: "Was ist die Drittschadensliquidation und wann greift sie?", normen: ["§ 249 BGB", "§ 447 BGB"], prioritaet: "hoch",
    kern: { lernziele: ["Zufällige Schadensverlagerung als Voraussetzung", "Fallgruppen: mittelbare Stellvertretung, Obhutsfälle, Versendungskauf"] } },
  { fach: "schuldbt", titel: "Wie grenzt man Miete und Leihe ab?", normen: ["§ 535 BGB", "§ 598 BGB"], prioritaet: "mittel" },
  { fach: "schuldbt", titel: "Wann haftet der Bürge und wann kann er die Einrede erheben?", normen: ["§ 765 BGB", "§ 768 BGB", "§ 771 BGB"], prioritaet: "mittel" },
  { fach: "sachen", titel: "Wie prüft man die Sicherungsübereignung?", normen: ["§ 930 BGB", "§ 868 BGB"], prioritaet: "hoch" },
  { fach: "sachen", titel: "Was ist ein Scheinbestandteil und was ein wesentlicher Bestandteil?", normen: ["§ 93 BGB", "§ 94 BGB", "§ 95 BGB"], prioritaet: "mittel" },
  { fach: "delikt", titel: "Wie wird das allgemeine Persönlichkeitsrecht geschützt?", normen: ["§ 823 (1) BGB", "Art. 2 (1) GG", "Art. 1 (1) GG"], prioritaet: "hoch" },
  { fach: "zpo", titel: "Wann ist eine Klageänderung zulässig?", normen: ["§ 263 ZPO", "§ 264 ZPO"], prioritaet: "mittel" },
  { fach: "zpo", titel: "Wie funktioniert die Drittwiderspruchsklage?", normen: ["§ 771 ZPO"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Wie prüft man den rechtfertigenden Notstand?", normen: ["§ 34 StGB", "§ 228 BGB", "§ 904 BGB"], prioritaet: "hoch" },
  { fach: "strafat", titel: "Was ist ein error in persona und wie wirkt die aberratio ictus?", normen: ["§ 16 StGB"], prioritaet: "hoch",
    kern: { lernziele: ["Rechtsprechung: aberratio ictus meist unbeachtlich bei Gleichwertigkeit", "Literatur: Konkretisierung entscheidet – Versuch plus Fahrlässigkeit"] } },
  { fach: "strafat", titel: "Wann ist der Versuch beendet und wann unbeendet?", normen: ["§ 24 (1) StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Wie prüft man die Untreue nach § 266 StGB?", normen: ["§ 266 StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Wann liegt eine Urkundenfälschung vor?", normen: ["§ 267 StGB"], prioritaet: "hoch" },
  { fach: "strafbt", titel: "Was ist der Unterschied zwischen Raub und räuberischem Diebstahl?", normen: ["§ 249 StGB", "§ 252 StGB"], prioritaet: "hoch" },
  { fach: "stpo", titel: "Wie ist der Ablauf einer Hauptverhandlung?", normen: ["§ 243 StPO", "§ 244 StPO", "§ 258 StPO"], prioritaet: "mittel" },
  { fach: "staat", titel: "Wie prüft man das Organstreitverfahren?", normen: ["Art. 93 (1) Nr. 1 GG", "§ 63 BVerfGG"], prioritaet: "hoch" },
  { fach: "grundr", titel: "Wann ist die Meinungsfreiheit eingeschränkt?", normen: ["Art. 5 (1) GG", "Art. 5 (2) GG"], prioritaet: "hoch" },
  { fach: "grundr", titel: "Wie prüft man den allgemeinen Gleichheitssatz?", normen: ["Art. 3 (1) GG"], prioritaet: "hoch" },
  { fach: "verwalt", titel: "Wann liegt ein Verwaltungsakt vor?", normen: ["§ 35 VwVfG"], prioritaet: "hoch" },
  { fach: "verwalt", titel: "Was ist eine Allgemeinverfügung?", normen: ["§ 35 S. 2 VwVfG"], prioritaet: "mittel" },
  { fach: "vwgo", titel: "Wann ist die Feststellungsklage subsidiär?", normen: ["§ 43 (2) VwGO"], prioritaet: "mittel" },
  { fach: "europa", titel: "Wie prüft man einen Verstoß gegen die Warenverkehrsfreiheit?", normen: ["Art. 34 AEUV", "Art. 36 AEUV"], prioritaet: "hoch" },
  { fach: "arbeit", titel: "Wann ist ein Betriebsübergang nach § 613a BGB gegeben?", normen: ["§ 613a BGB"], prioritaet: "hoch" },
  { fach: "handelsg", titel: "Wie haftet der eintretende Gesellschafter für Altschulden?", normen: ["§ 721a BGB", "§ 130 HGB"], prioritaet: "mittel" },
  { fach: "famerb", titel: "Wie funktioniert der Zugewinnausgleich?", normen: ["§ 1373 BGB", "§ 1378 BGB"], prioritaet: "mittel" },
];
