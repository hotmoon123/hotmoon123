# StitchLedger — native Android and iPhone project

You requested a mobile app, not a website. This package contains native Android and iOS projects generated from the shared React Native implementation. The app uses native React Native views; it is not a WebView wrapping a website. A backend server is still needed for accounts, shared records and API operations; that does not make the phone frontend a web app.

## Exact delivery status

- `mobile/android/`: generated Gradle Android project, resources and native entry point.
- `mobile/ios/`: generated Xcode iPhone/iPad project, resources and Podfile.
- `mobile/App.tsx`: the native screens and workflows.
- `backend/`: authenticated API, data access and SQLite database.
- `scripts/build-android-test-apk.sh`: guarded local Android build procedure.

**This ZIP contains source projects, not a compiled APK or IPA.** Native project generation and TypeScript checking passed. The earlier JavaScript export checks are documented, but they are not native compiler, installation or device tests. No signed mobile binaries have been produced in this environment. The environment currently has Java 11 and no configured Android SDK; it also has no Apple signing setup. Unresolved dependency findings and other release gates remain in `docs/QUALITY-AND-SECURITY.md`.

## Expo Go on Android and iPhone — current development route

For physical development testing without compiling an APK or IPA, use Expo Go on both phones. This is a native development host, not a standalone store-ready StitchLedger release. Both phones and the Kali laptop must be on the same trusted Wi-Fi network.

Run the backend in one terminal:

```bash
cd /home/caleb/Projects/stitchledger-native/backend
.venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

In another terminal, set the laptop's actual LAN address in the API URL and start Expo Go mode. The example below uses `192.168.1.51`; replace it if the laptop address changes.

```bash
cd /home/caleb/Projects/stitchledger-native/mobile
export EXPO_PUBLIC_API_URL="http://192.168.1.51:8000"
npx expo start --go --lan --clear
```

Scan the QR code inside Android Expo Go. On iPhone, sign in to the same Expo account in Expo Go and the CLI when Expo requires it, then scan through the Camera/Expo Go flow. Test that each phone can first open `http://192.168.1.51:8000/api/health` over the trusted LAN. Do not expose this development HTTP backend through router port forwarding. Production apps must use HTTPS.

### Local workflow reminders and daily check-in in v0.2.3

The app provides an owner-controlled generic daily 08:00 reminder and optional day-before/due-day collection reminder. In the app select **Studio** → **Turn on daily 8:00 AM reminder**, then grant the device notification permission. Tapping the daily notification opens a check-in queue that prioritises overdue/ready work. The owner may explicitly confirm Booked → Cutting → Sewing → Ready → Collected, keep the current stage, set a tomorrow reminder, or open the full order. Notification text is deliberately generic; a notification tap alone never changes a status or payment.

Expo documents that Expo Go can test local notifications but cannot test remote push notifications from SDK 53 onward. Remote production notifications require a development/production build and a separate backend notification service. See `docs/NOTIFICATIONS-DESIGN.md`.

## Android installation path on Kali

1. Install the compatible Android SDK, required SDK components, Node.js and a compatible JDK (17 or newer). Review the SDK license terms yourself. Use Android Studio's SDK manager or official command-line tools.
2. Configure and test a reachable HTTPS backend. A phone's localhost is not your Kali laptop. The app cannot use accounts or shared orders without a reachable backend.
3. Set `ANDROID_HOME` and `EXPO_PUBLIC_API_URL` in your terminal to real values. The backend URL is public configuration, not a secret.
4. From this project root, run:

```bash
bash scripts/build-android-test-apk.sh
```

If the build succeeds, the APK is generated at:

```text
mobile/android/app/build/outputs/apk/release/app-release.apk
```

The generated release configuration uses a public development signing key: this is a standalone **test APK**, not a store release. The script prints the installation command. On your own phone, authorize USB debugging and install through `adb install -r` or transfer the APK and explicitly permit installation from that source. Do not sideload files from untrusted sources.

Building and installing must still be tested; these instructions are not evidence that the binary already exists.

## iPhone installation path

Open the generated Xcode project/workspace after installing CocoaPods dependencies on a compatible Mac, configure your signing team and test on an authorized device. Alternatively use an owner-controlled EAS cloud build. Kali cannot locally compile/sign an iOS app using Apple's Xcode toolchain. Actual device provisioning and distribution require the applicable Apple signing/account setup.

Do not send passwords, signing keys or access tokens in chat. Keep account ownership and credentials under your control.

## What this package deliberately excludes

The prebuilt web app is not included in this native-focused archive. Some shared source dependencies can also target web, but the delivery targets here are Android/iOS. There is no browser installation step. Prior documentation is retained for architecture and evidence; references to the older browser preview do not mean that a browser preview fulfills the mobile-installation request.

The next deliverable needed to fulfill the installable-app requirement is a successfully compiled, tested Android APK and appropriately signed iPhone build—not another screenshot or source ZIP.
