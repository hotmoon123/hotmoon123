# StitchLedger v0.2.1 notification update

This update adds **opt-in local reminders** to the existing Android/iPhone Expo project. It does **not** change the backend database schema or delete your existing test records.

## What it adds

- A generic local daily 08:00 workflow check-in.
- A day-before or due-day 08:00 reminder from an active order.
- Generic lock-screen wording only; it does not expose customer names, garment details, payment details or balances.
- A notification tap opens StitchLedger for review. It never automatically moves an order or records money.

`Overdue` remains a calculated alert condition, not a replacement for the real stage. An order can be both Sewing and Overdue.

## Safe update on Kali

This archive contains only changed mobile source and documentation. Keep the existing `backend/data/` directory untouched.

1. Stop only the Expo bundler with `Ctrl+C`. The backend may stay running.
2. Back up the existing mobile source:

```bash
cd /home/caleb/Projects/stitchledger-native
stamp=$(date +%Y%m%d-%H%M%S)
cp -a mobile "mobile-before-notification-update-$stamp"
```

3. Extract this update without touching the current project folder:

```bash
mkdir -p /home/caleb/Projects/stitchledger-update-v0.2.1
unzip /home/caleb/Downloads/stitchledger-notifications-update-v0.2.1.zip \
  -d /home/caleb/Projects/stitchledger-update-v0.2.1
```

4. Copy the update over the project. This updates only `mobile/`, `docs/`, `README.md`, `CHANGELOG.md` and the native guide. It does not touch `backend/`.

```bash
cd /home/caleb/Projects/stitchledger-native
cp -a /home/caleb/Projects/stitchledger-update-v0.2.1/stitchledger-notifications-update-v0.2.1/mobile/. mobile/
cp -a /home/caleb/Projects/stitchledger-update-v0.2.1/stitchledger-notifications-update-v0.2.1/docs/. docs/
cp /home/caleb/Projects/stitchledger-update-v0.2.1/stitchledger-notifications-update-v0.2.1/README.md .
cp /home/caleb/Projects/stitchledger-update-v0.2.1/stitchledger-notifications-update-v0.2.1/CHANGELOG.md .
cp /home/caleb/Projects/stitchledger-update-v0.2.1/stitchledger-notifications-update-v0.2.1/NATIVE-START-HERE.md .
```

5. Install exactly the locked mobile dependencies and start Expo Go again:

```bash
cd /home/caleb/Projects/stitchledger-native/mobile
npm ci
export EXPO_PUBLIC_API_URL="http://192.168.1.51:8000"
npx expo start --go --lan --clear
```

6. Scan the new QR code from Android/iPhone Expo Go. In StitchLedger, sign in or choose the private demo, then open **Studio** → **Turn on daily 8:00 AM reminder**. Grant the phone permission when asked.

## Testing without waiting until 08:00

The production reminder time is intentionally fixed at 08:00 local time to prevent uncontrolled notification settings in this small first increment. To confirm it is scheduled, look in your phone's notification settings for Expo Go/StitchLedger where the OS exposes scheduled notifications. You can also set a future-dated fictional order and choose one of its reminder actions.

A complete physical Android/iPhone delivery test must still be recorded before this feature can be described as production-ready. Expo Go supports local notifications, not the production remote-push service needed for reliable server-originated reminders.
