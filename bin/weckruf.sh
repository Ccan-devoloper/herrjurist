#!/usr/bin/env bash
# Weckkette mit begrenzten API-Retries. Sourcen ist fuer die Regressionstests
# nebenwirkungsfrei; nur der direkte Aufruf startet die Kette.

weck_warnung() { printf '::warning::Weckkette: %s\n' "$*" >&2; }

gh_sicher() {
  local ausgabe versuch
  for versuch in 1 2 3; do
    # Fehler-JSON auf stdout darf NIE als fachlicher Rueckgabewert weiterleben.
    if ausgabe=$(timeout 30s gh "$@"); then
      printf '%s\n' "$ausgabe"
      return 0
    fi
    weck_warnung "GitHub-Aufruf fehlgeschlagen (Versuch $versuch/3)."
    if [ "$versuch" -lt 3 ]; then sleep "$((versuch * 2))"; fi
  done
  return 1
}

laufstart_epoch() {
  local fallback=$1 wert epoch
  if wert=$(gh_sicher api "repos/$GH_REPO/actions/runs/$GITHUB_RUN_ID" --jq .run_started_at) \
    && [[ "$wert" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?Z$ ]] \
    && epoch=$(date -u -d "$wert" +%s 2>/dev/null) \
    && [[ "$epoch" =~ ^[0-9]+$ ]]; then
    printf '%s\n' "$epoch"
  else
    weck_warnung "Kein gueltiger Laufstart; verwende den sicheren Tagesbeginn."
    printf '%s\n' "$fallback"
  fi
}

juengere_kette_aktiv() {
  local n
  # Nur ein API-Aufruf statt fuenf; nur bestaetigte juengere Ketten beenden uns.
  if n=$(gh_sicher api "repos/$GH_REPO/actions/runs?per_page=100" --jq \
    "[.workflow_runs[] | select(.path == \".github/workflows/instagram.yml\" and .id > $GITHUB_RUN_ID and (.status == \"in_progress\" or .status == \"queued\" or .status == \"pending\" or .status == \"waiting\" or .status == \"requested\"))] | length") \
    && [[ "$n" =~ ^[0-9]+$ ]]; then
    [ "$n" -gt 0 ]
  else
    weck_warnung "Kettenstatus unbekannt; die aktuelle Kette bleibt erhalten."
    return 1
  fi
}

wecken() {
  # Auch der Dispatch wird wiederholt. Eventuelle Doppelstarts werden durch
  # die bestehende posten-Concurrency und den gespeicherten Sendestatus abgefangen.
  gh_sicher workflow run instagram.yml --ref main -f modus=live -f wecker=true "$@"
}

weckruf_main() {
  set -euo pipefail
  : "${GH_REPO:?GH_REPO fehlt}" "${GH_TOKEN:?GH_TOKEN fehlt}" "${GITHUB_RUN_ID:?GITHUB_RUN_ID fehlt}"
  [[ "$GITHUB_RUN_ID" =~ ^[0-9]+$ ]] || { weck_warnung "Ungueltige Run-ID."; return 1; }
  cd "$(dirname "${BASH_SOURCE[0]}")/.."
  if juengere_kette_aktiv; then echo "Juengere Kette aktiv – dieser Weckruf endet."; return 0; fi

  local start h tag zielh slot frist nacht=0 vorlauf=480 jetzt termin seit n
  local kette_geprueft zuletzt_gemeldet="" tagesbeginn ende
  start=$(date -u +%s)
  h=$((10#$(date -u +%H)))
  tag=$(date -u +%F)
  zielh=$((h + 1))
  # 04 UTC ist im Sommer 06 Uhr: genug Vorlauf fuer B1 um 06:30 Berlin.
  if [ "$zielh" -lt 4 ]; then zielh=4; fi
  if [ "$zielh" -gt 20 ]; then zielh=4; tag=$(date -u -d "$tag +1 day" +%F); fi
  slot=$(date -u -d "$tag $(printf %02d "$zielh"):00:00" +%s)
  frist=$((slot + 120))
  ende=$((start + 20400))  # Reserve vor dem 350-Minuten-Timeout des Jobs.
  if [ "$((frist - start))" -gt 19800 ]; then frist=$((start + 19800)); nacht=1; fi
  echo "Naechster Stundenstart: $(date -u -d "@$slot" +%FT%TZ)"

  # Bei unlesbarem Laufstart darf kein heute ueberfaelliger Slot verloren gehen.
  # Bestaetigt veroeffentlichte Slots filtert naechster-termin selbst heraus.
  tagesbeginn=$(TZ=Europe/Berlin date -d "$(TZ=Europe/Berlin date +%F) 00:00:00" +%s)
  NAECHSTER_SEIT=$(laufstart_epoch "$((tagesbeginn - 1))")
  export NAECHSTER_SEIT
  kette_geprueft=$start

  while :; do
    jetzt=$(date -u +%s)
    if [ "$jetzt" -ge "$ende" ]; then
      weck_warnung "GitHub dauerhaft nicht erreichbar; unabhaengige Cron-Starts bleiben aktiv."
      return 1
    fi
    if [ "$((jetzt - kette_geprueft))" -ge 600 ]; then
      if juengere_kette_aktiv; then echo "Juengere Kette aktiv – dieser Weckruf endet."; return 0; fi
      kette_geprueft=$jetzt
    fi
    termin=$(timeout 30s node bin/naechster-termin.mjs || true)
    if [[ -n "$termin" && ! "$termin" =~ ^[0-9]{1,12}$ ]]; then
      weck_warnung "Ungueltiger naechster Termin; verwende den Stunden-Fallback."
      termin=""
    fi
    if [ -n "$termin" ] && [ "$termin" != "$zuletzt_gemeldet" ]; then
      echo "Naechster Termin laut Tagesplan: $(date -u -d "@$termin" +%FT%TZ)"
      zuletzt_gemeldet=$termin
    fi
    if [ -n "$termin" ] && [ "$((termin - vorlauf))" -le "$jetzt" ]; then
      if juengere_kette_aktiv; then echo "Juengere Kette aktiv – dieser Weckruf endet."; return 0; fi
      if wecken; then echo "Faelligen Termin geweckt."; return 0; fi
      weck_warnung "Dispatch fehlgeschlagen; die Kette versucht es erneut."
      sleep 60
      continue
    fi
    if [ "$jetzt" -ge "$frist" ]; then
      if juengere_kette_aktiv; then echo "Juengere Kette aktiv – dieser Weckruf endet."; return 0; fi
      if [ "$nacht" = 1 ]; then
        if wecken -f nur_wecken=true; then return 0; fi
      else
        seit=$(date -u -d "@$slot" +%FT%TZ)
        if n=$(gh_sicher api "repos/$GH_REPO/actions/runs?created=>=$seit&per_page=100" --jq \
          '[.workflow_runs[] | select(.path == ".github/workflows/instagram.yml")] | length') \
          && [[ "$n" =~ ^[0-9]+$ ]] && [ "$n" -gt 0 ]; then
          echo "Stundenlauf hat ausgeloest – dieser uebernimmt die Kette."
          return 0
        fi
        if wecken; then echo "Stunden-Fallback geweckt."; return 0; fi
      fi
      weck_warnung "Wecken noch nicht bestaetigt; erneuter Versuch in der Kette."
      frist=$((jetzt + 60))
    fi
    sleep 60
  done
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then weckruf_main "$@"; fi
