// Gemeinsame Brevo-Anbindung für /api/anmelden und /api/nachtragen (kein eigener Pfad: liegt außerhalb von api/).
// Aufbau wie bei Examenscampus (Repo steuerberater): erst Cloudflare-KV, dann Brevo, Störungen holt der
// stündliche Lauf nach. Liste und Willkommensvorlage kommen aus den Pages-Einstellungen, nicht aus dem Code:
//   BREVO_LISTE        Listen-ID „Herrjurist – Wochenbrief“ (Pflicht)
//   BREVO_VORLAGE_WILLKOMMEN  Transaktionsvorlage für die Begrüßungsmail (optional; fehlt sie, geht keine Mail raus)

async function brevo(env, methode, url, daten, timeoutMs) {
  if (!env.BREVO_API_KEY) return "BREVO_API_KEY fehlt";
  try {
    const res = await fetch(url, {
      method: methode,
      headers: { "api-key": env.BREVO_API_KEY, "content-type": "application/json", accept: "application/json" },
      body: JSON.stringify(daten),
      signal: AbortSignal.timeout(timeoutMs),
    });
    return res.ok ? null : `Brevo ${res.status}: ${(await res.text()).slice(0, 300)}`;
  } catch (e) {
    return `Brevo nicht erreichbar: ${e.name}`;
  }
}

const api = (pfad) => `https://api.brevo.com/v3/${pfad}`;

// Kontakt in die Liste eintragen (201 = neu, 204 = vorhandener Kontakt aktualisiert). null = ok, sonst Fehlertext
export function kontaktEintragen(env, email, vorname, timeoutMs = 3000) {
  const liste = Number(env.BREVO_LISTE);
  if (!liste) return Promise.resolve("BREVO_LISTE fehlt");
  return brevo(env, "POST", api("contacts"),
    { email, attributes: vorname ? { FIRSTNAME: vorname } : {}, listIds: [liste], updateEnabled: true }, timeoutMs);
}

// Begrüßungsmail – höchstens einmal je Kontakt. Der KV-Speicher ist nur „irgendwann konsistent“, deshalb steht
// der Vermerk zusätzlich am Kontakt in Brevo (Attribut WILLKOMMEN_GESENDET) und wird vor dem Senden geprüft.
export async function willkommenSenden(env, email, vorname, timeoutMs = 3000) {
  const vorlage = Number(env.BREVO_VORLAGE_WILLKOMMEN);
  if (!vorlage) return null;                                   // keine Vorlage hinterlegt: nichts zu tun
  if (!env.BREVO_API_KEY) return "BREVO_API_KEY fehlt";
  const kontaktUrl = api(`contacts/${encodeURIComponent(email)}?identifierType=email_id`);
  try {
    const res = await fetch(kontaktUrl, {
      headers: { "api-key": env.BREVO_API_KEY, accept: "application/json" }, signal: AbortSignal.timeout(timeoutMs),
    });
    if (res.ok && (await res.json())?.attributes?.WILLKOMMEN_GESENDET) return null;
  } catch (e) {
    return `Brevo nicht erreichbar: ${e.name}`;
  }
  // Vermerk vor dem Senden setzen: lieber im Ausnahmefall keine Mail als zwei
  const jetzt = new Date().toISOString().slice(0, 10);
  await brevo(env, "POST", api("contacts/attributes/normal/WILLKOMMEN_GESENDET"), { type: "date" }, timeoutMs);   // legt das Attribut beim ersten Mal an
  let f = await brevo(env, "PUT", kontaktUrl, { attributes: { WILLKOMMEN_GESENDET: jetzt } }, timeoutMs);
  if (f) return f;
  f = await brevo(env, "POST", api("smtp/email"),
    { templateId: vorlage, to: [vorname ? { email, name: vorname } : { email }], params: { VORNAME: vorname || "" } }, timeoutMs);
  if (f) await brevo(env, "PUT", kontaktUrl, { attributes: { WILLKOMMEN_GESENDET: "" } }, timeoutMs);   // Versand fehlgeschlagen: Vermerk zurücknehmen
  return f;
}

// Fehlende Schritte für einen Eintrag nachholen. Gibt den aktualisierten Eintrag und ggf. den Fehler zurück.
export async function abarbeiten(env, eintrag, timeoutMs = 3000) {
  const e = { ...eintrag };
  if (!e.kontakt) {
    const f = await kontaktEintragen(env, e.email, e.vorname, timeoutMs);
    if (f) return { eintrag: { ...e, fehler: f }, fehler: f };
    e.kontakt = true;
  }
  if (!e.willkommen) {
    const f = await willkommenSenden(env, e.email, e.vorname, timeoutMs);
    if (f) return { eintrag: { ...e, fehler: f }, fehler: f };
    if (Number(env.BREVO_VORLAGE_WILLKOMMEN)) e.willkommen = new Date().toISOString();
  }
  delete e.fehler;
  return { eintrag: e, fehler: null };
}

const gestoert = (f) => f.startsWith("Brevo nicht erreichbar") || /^Brevo 5\d\d/.test(f);

// Offene Anmeldungen erneut abarbeiten. Fertige wandern von „offen:“ nach „brevo:“.
// Wird die Willkommensvorlage erst später hinterlegt, bekommen ältere „brevo:“-Einträge die Mail nachgeliefert.
export async function nachtragen(env, max = 20) {
  const kv = env.ANMELDUNGEN;
  const ergebnis = { offen: 0, uebertragen: 0, willkommenNachgeliefert: 0, fehlgeschlagen: 0 };
  if (!kv) return ergebnis;

  const { keys } = await kv.list({ prefix: "offen:", limit: max });
  ergebnis.offen = keys.length;
  for (const { name } of keys) {
    const alt = await kv.get(name, "json");
    if (!alt?.email) continue;
    const { eintrag, fehler } = await abarbeiten(env, alt, 8000);
    if (!fehler) {
      await kv.put("brevo:" + name.slice("offen:".length), JSON.stringify({ ...eintrag, nachgetragen: new Date().toISOString() }));
      await kv.delete(name);
      ergebnis.uebertragen++;
    } else {
      await kv.put(name, JSON.stringify({ ...eintrag, versuche: (alt.versuche || 0) + 1 }));
      ergebnis.fehlgeschlagen++;
      if (gestoert(fehler)) return ergebnis;   // Brevo noch gestört: nicht alles weitere anlaufen lassen
    }
  }

  if (!Number(env.BREVO_VORLAGE_WILLKOMMEN)) return ergebnis;
  const fertig = await kv.list({ prefix: "brevo:", limit: 200 });
  for (const { name } of fertig.keys) {
    const alt = await kv.get(name, "json");
    if (!alt?.email || alt.willkommen) continue;
    const { eintrag, fehler } = await abarbeiten(env, { ...alt, kontakt: true }, 8000);
    await kv.put(name, JSON.stringify(eintrag));
    if (fehler) { ergebnis.fehlgeschlagen++; if (gestoert(fehler)) return ergebnis; }
    else ergebnis.willkommenNachgeliefert++;
  }
  return ergebnis;
}
