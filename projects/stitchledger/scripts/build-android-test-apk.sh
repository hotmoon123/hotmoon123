#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
: "${EXPO_PUBLIC_API_URL:?Set EXPO_PUBLIC_API_URL to your actual reachable HTTPS backend before building.}"
case "$EXPO_PUBLIC_API_URL" in https://*) ;; *) echo 'A release-mode mobile build requires an HTTPS backend URL.'; exit 1;; esac
command -v java >/dev/null || { echo 'Install a compatible JDK (17 or newer).'; exit 1; }
command -v node >/dev/null || { echo 'Install the supported Node.js version described in the runbook.'; exit 1; }
SDK="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-}}"
[[ -n "$SDK" && -d "$SDK" ]] || { echo 'Install the Android SDK and set ANDROID_HOME first. Review and accept its licenses yourself.'; exit 1; }
export ANDROID_HOME="$SDK"
cd "$ROOT/mobile"
npm ci
npm run typecheck
cd android
chmod +x gradlew
./gradlew :app:assembleRelease
APK="$ROOT/mobile/android/app/build/outputs/apk/release/app-release.apk"
[[ -f "$APK" ]] || { echo 'Expected APK was not produced. Read the Gradle output.'; exit 1; }
printf '\nStandalone Android TEST APK: %s\n' "$APK"
printf 'Signed with the generated public development key. Not for store publication or real customer data.\n'
printf 'To install on your own authorized USB-debugging-enabled Android device: adb install -r "%s"\n' "$APK"
