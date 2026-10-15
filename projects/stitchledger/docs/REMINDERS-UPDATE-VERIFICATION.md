# v0.2.1 workflow-reminder verification record

**Date:** 9 October 2026  
**Scope:** opt-in local workflow/due-date reminder increment; no backend schema or money-rule change.

## Checks performed in the development workspace

| Check | Result | What it proves | What it does not prove |
|---|---:|---|---|
| `npm run typecheck` | Passed | TypeScript source, including `reminders.ts`, is type-consistent | Native runtime/OS delivery behaviour |
| `npx expo export --platform all` | Passed | Web, Android Hermes and iOS Hermes JavaScript bundles can be generated with Expo SDK 57 dependencies | APK/IPA compilation, signing, installation or notification delivery |
| `npx expo prebuild --platform all --no-install` | Passed | Android/iOS generated source reflects `expo-notifications` configuration | Native compiler success or platform credentials |
| Android manifest inspection | Passed | Contains `android.permission.POST_NOTIFICATIONS` and configured default notification channel/icon for a future native build | The Expo Go host's own manifest/settings |
| Python backend test suite | 26 passed, 1 recorded third-party deprecation warning | Existing API/auth/order/payment/workflow rules remain passing after the mobile-only change | Native client reminder delivery |
| npm audit | 23 unresolved findings: 15 high, 8 moderate | The existing dependency risk remains visible | That the dependencies are safe for commercial release |

## Manual physical-device test still required

Because the current testing approach is Expo Go on Android and iPhone, the following must be observed on each target phone after applying the update:

1. Open **Studio** and opt in to the daily reminder; respond to the OS permission request.
2. Confirm the notification channel/category is present in phone settings where exposed.
3. Create a fictional future order and schedule one of its reminder choices.
4. At the scheduled time, verify generic lock-screen wording only.
5. Tap the notification; verify it opens StitchLedger and, for an order reminder, displays the matching order.
6. Confirm no status or payment changes occurred merely from tapping.
7. Turn off the daily reminder and confirm it is removed from the OS schedule.
8. Repeat on the second platform.

These checks are intentionally recorded as pending, not fabricated as completed.
