/* ==========================================================================
   Drei Stilrichtungen. Der aktive Stil steht in config.mjs (marke.stil) bzw.
   in der Umgebungsvariablen IG_STIL. Jeder Stil liefert CSS-Variablen; die
   Vorlagen (vorlagen.mjs) sind für alle Stile gleich.
   ========================================================================== */

export const STILE = {
  /* A · Kanzlei – schwarz/weiß, große Condensed-Schrift, farbiges Fach-Etikett.
     Nächster Verwandter von herrjurist. */
  kanzlei: {
    name: "Kanzlei",
    beschreibung: "Schwarz, große weiße Schlagzeile, farbiges Fach-Etikett – der herrjurist-Look für Steuerrecht.",
    modus: "dunkel",
    schrift: { titel: "Anton", text: "Inter", mono: "IBM Plex Mono", titelGewicht: 400, titelTransform: "none", titelSpacing: "0.005em", titelZeilenhoehe: 1.02 },
    farben: {
      grund: "#0b0b0d", flaeche: "#161619", text: "#ffffff", textWeich: "#b9b9c2", linie: "#2a2a30",
      akzent: "#ffffff", pille: "#ffffff", pilleText: "#0b0b0d",
      k1: "#5b8cff", k2: "#ff6a3d", k3: "#3ddc84",
      ok: "#3ddc84", warn: "#ffb020", rot: "#ff4d4d",
    },
    ecken: "6px",
  },

  /* A′ · Kanzlei hell – dieselbe Typografie auf Weiß. Im Wechsel mit der
     dunklen Variante ergibt sich im Profil ein Schachbrett. */
  "kanzlei-hell": {
    name: "Kanzlei (hell)",
    beschreibung: "Weiße Variante des Kanzlei-Stils – gleiche Schrift, umgekehrte Farben.",
    modus: "hell",
    familie: "kanzlei",
    schrift: { titel: "Anton", text: "Inter", mono: "IBM Plex Mono", titelGewicht: 400, titelTransform: "none", titelSpacing: "0.005em", titelZeilenhoehe: 1.02 },
    farben: {
      grund: "#ffffff", flaeche: "#f3f3f5", text: "#0b0b0d", textWeich: "#55555e", linie: "#d9d9de",
      akzent: "#0b0b0d", pille: "#0b0b0d", pilleText: "#ffffff",
      k1: "#2f63e0", k2: "#e0501f", k3: "#1f9c5a",
      ok: "#1f9c5a", warn: "#c97a00", rot: "#d92d2d",
    },
    ecken: "6px",
  },

  /* D · Bunt – ganze Kachel in der Farbe des Klausurtags (Tag 1 Blau, Tag 2
     Orange, Tag 3 Grün), Titel in Pillen, handschriftlicher Hinweis, Bühne mit
     großem Icon, §-Badge und Karte. Vorbild: bunte Studygram-Profile. */
  bunt: {
    name: "Bunt",
    beschreibung: "Vollflächig in der Tagesfarbe, Pillen-Titel, Handschrift-Hinweis, Icon-Bühne – auffällig und freundlich.",
    modus: "bunt",
    familie: "bunt",
    schrift: { titel: "Space Grotesk", text: "Inter", mono: "IBM Plex Mono", titelGewicht: 700, titelTransform: "none", titelSpacing: "-0.01em", titelZeilenhoehe: 1.05 },
    farben: {
      grund: "#23d98b", flaeche: "rgba(255,255,255,.92)", text: "#0b4a33", textWeich: "#1d5c44", linie: "rgba(255,255,255,.45)",
      akzent: "#0b4a33", pille: "#0b4a33", pilleText: "#ffffff",
      k1: "#2d5be3", k2: "#ff7a45", k3: "#23d98b",
      ok: "#0b4a33", warn: "#7a3a10", rot: "#b3261e",
    },
    /* Palette je Klausurtag: Grund, dunkle Kontrastfarbe, helle und lila Pille, Zweitakzent. */
    tagFarben: {
      1: { grund: "#2d5be3", dunkel: "#0c1b4d", hell: "#e3ebff", lila: "#cdbcff", akzent2: "#ffd166" },
      2: { grund: "#ff7a45", dunkel: "#3a1708", hell: "#fff0e6", lila: "#ffd9c2", akzent2: "#2d5be3" },
      3: { grund: "#23d98b", dunkel: "#0b4a33", hell: "#e9fff4", lila: "#d9c8ff", akzent2: "#ff7a45" },
    },
    ecken: "30px",
  },

  /* B · Klausurbogen – Papier, Tintenblau, Serifen. Entspricht dem Design der
     Webseite (IBM Plex, Korrekturfarben, Randziffern). */
  klausurbogen: {
    name: "Klausurbogen",
    beschreibung: "Papier & Tinte wie die Webseite: IBM Plex Serif, Normen in Mono, Korrekturfarben Rot/Orange/Grün.",
    modus: "papier",
    schrift: { titel: "IBM Plex Serif", text: "IBM Plex Sans", mono: "IBM Plex Mono", titelGewicht: 700, titelTransform: "none", titelSpacing: "-0.01em", titelZeilenhoehe: 1.08 },
    farben: {
      grund: "#f6f2e9", flaeche: "#fffdf8", text: "#12233f", textWeich: "#5b6478", linie: "#cfc6b4",
      akzent: "#12233f", pille: "#12233f", pilleText: "#f6f2e9",
      k1: "#1f5fbf", k2: "#c8102e", k3: "#1b8a4c",
      ok: "#1b8a4c", warn: "#d97a00", rot: "#c8102e",
    },
    ecken: "2px",
  },

  /* C · Campus – tiefes Indigo mit Limette, Space Grotesk, weiche Karten.
     Moderner „Studygram“-Look. */
  campus: {
    name: "Campus",
    beschreibung: "Indigo-Verlauf, Limetten-Akzent, Space Grotesk, runde Karten – modern und jung.",
    modus: "dunkel",
    schrift: { titel: "Space Grotesk", text: "Inter", mono: "IBM Plex Mono", titelGewicht: 700, titelTransform: "none", titelSpacing: "-0.02em", titelZeilenhoehe: 1.05 },
    farben: {
      grund: "#141a3a", flaeche: "#1d2550", text: "#f7f8ff", textWeich: "#aab2d9", linie: "#2e3870",
      akzent: "#d6ff4a", pille: "#d6ff4a", pilleText: "#141a3a",
      k1: "#6ea8ff", k2: "#ff8a5b", k3: "#5cf0a8",
      ok: "#5cf0a8", warn: "#ffc860", rot: "#ff6b6b",
    },
    ecken: "22px",
  },
};

/* Stil für die n-te Kachel: Beim Kanzlei-Stil mit Wechsel wird zwischen
   dunkel und hell alterniert, sonst bleibt der Stil fest. */
export function stilFuer(name, index = 0, wechsel = true) {
  if (name === "kanzlei" && wechsel) return index % 2 === 0 ? "kanzlei" : "kanzlei-hell";
  return name;
}

export function stil(name) {
  const s = STILE[name];
  if (!s) throw new Error(`Unbekannter Stil „${name}“. Möglich: ${Object.keys(STILE).join(", ")}`);
  return { id: name, ...s };
}

/* Icons als Strich-Grafiken (24×24 viewBox). Der Autor wählt einen Schlüssel. */
export const ICONS = {
  waage: '<path d="M12 3v18M5 21h14M12 6l-6 8h12l-6-8zM6 14a3 3 0 0 0 6 0M12 14a3 3 0 0 0 6 0" transform="translate(0 0)"/><path d="M4 7h16"/>',
  rechner: '<rect x="5" y="2" width="14" height="20" rx="2"/><rect x="8" y="5" width="8" height="4"/><path d="M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01"/>',
  kalender: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
  gebaeude: '<path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-5h6v5M9 10h.01M15 10h.01M9 14h.01M15 14h.01"/>',
  diagramm: '<path d="M3 21h18M6 17V10M11 17V5M16 17v-7M21 17v-3"/>',
  dokument: '<path d="M6 2h8l5 5v15H6zM14 2v5h5M9 13h6M9 17h6"/>',
  warnung: '<path d="M12 3 2 21h20zM12 10v5M12 18h.01"/>',
  uhr: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
  muenzen: '<ellipse cx="9" cy="7" rx="6" ry="3"/><path d="M3 7v5c0 1.7 2.7 3 6 3s6-1.3 6-3V7M3 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5M15 10c3 .2 6 1.4 6 3v5c0 1.7-2.7 3-6 3"/>',
  haus: '<path d="M3 11 12 3l9 8M5 10v11h14V10M10 21v-6h4v6"/>',
  lkw: '<path d="M1 7h13v10H1zM14 10h4l4 4v3h-8z"/><circle cx="5" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
  vertrag: '<path d="M4 4h12l4 4v12H4zM16 4v4h4M8 13l2 2 4-4"/>',
  lupe: '<circle cx="10" cy="10" r="6"/><path d="M15 15l6 6"/>',
  kreislauf: '<path d="M20 12a8 8 0 1 1-2.3-5.7M20 4v5h-5"/>',
  blitz: '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
  buch: '<path d="M4 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8z"/>',
  fabrik: '<path d="M3 21V9l5 3V9l5 3V9l5 3V4h3v17zM7 17h2M12 17h2M17 17h2"/>',
  person: '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
  personen: '<circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M2 20a7 7 0 0 1 14 0M15 20a5 5 0 0 1 7 0"/>',
  globus: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
  paragraf: '<path d="M14 5.5c-1-1.2-2.4-1.5-3.6-1.5C8.2 4 7 5.3 7 6.8c0 3.6 7 2.6 7 6.4 0 1.7-1.4 2.8-3.4 2.8-1.6 0-2.9-.6-3.8-1.6M10 18.5c1 1.2 2.4 1.5 3.6 1.5 2.2 0 3.4-1.3 3.4-2.8 0-3.6-7-2.6-7-6.4"/>',
  haken: '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
  kreuz: '<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
  zielscheibe: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
  trophaee: '<path d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H4v2a3 3 0 0 0 3 3M16 6h4v2a3 3 0 0 1-3 3M12 13v4M8 21h8M9 17h6v4H9z"/>',
};

export function iconSvg(name, groesse = 96) {
  const pfad = ICONS[name] || ICONS.paragraf;
  return `<svg class="icon" width="${groesse}" height="${groesse}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">${pfad}</svg>`;
}
