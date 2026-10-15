# Workflow reminders design — v0.2.1

## Purpose and boundary

This increment turns the existing order-state model into an **opt-in, local-device reminder experience**. It helps a studio owner perform a deliberate daily check-in without changing order data automatically or exposing customer information on a locked phone.

It does **not** claim a production push-notification service. Server-sent push notifications require an owner-controlled native/development build, platform credentials, backend device-token registration, delivery-receipt handling and operational monitoring. Those are future release-gated work.

## Status model: fact versus derived condition

The production stage is a business fact set by the user through the existing validated state machine:

```text
Booked → Cutting → Sewing → Ready → Collected
              ↕ limited rework transitions
          → Cancelled where the financial rule permits
```

`Overdue` is deliberately **not** stored as a manually editable production status. It is a derived alert condition:

```text
order is overdue when due date < local calendar date
and status is neither Collected nor Cancelled
```

That preserves useful information. An order can truthfully be both **Sewing** and **Overdue**; replacing Sewing with Overdue would hide the work stage.

Collected and Cancelled are terminal states. They are excluded from active daily prompts and cannot receive new order reminders.

## User-facing behaviour

### Daily workflow check-in

1. The owner opens **Studio** and explicitly chooses **Turn on daily 8:00 AM reminder**.
2. The mobile operating system asks for notification permission, if it has not already been granted.
3. The device schedules one repeating local reminder for 08:00 in the device's local time zone.
4. The notification says only:

   > Your StitchLedger check-in — Review booked, cutting, sewing, ready and overdue work in your order book.

5. Tapping it opens StitchLedger to the Today/order-review context.
6. The owner reviews each active order and uses the normal status controls to record the actual work stage.

The app does **not** schedule reminders automatically on sign-in. Consent avoids unwanted daily interruptions. The reminder can be turned off in Studio and is cancelled when the owner signs out on that device.

### Per-order collection reminder

From an active order, the owner can choose:

- **Remind day before** — 08:00 local time on the day before the collection date; or
- **Remind on collection day** — 08:00 local time on the collection date.

Only one due-date reminder per order is retained on the device; setting another replaces the earlier one. A notification tap opens that order, then the existing backend workflow rules, version checks and money rules still apply.

## Why a notification does not directly change the status

One-tap actions such as “mark Ready” from a lock-screen notification are attractive but unsafe in the current stage:

- they can record an incorrect production fact through an accidental tap;
- the order may have changed on another device;
- a status move must obey the permitted state transition rules;
- collection must still require a zero balance.

Therefore a tap opens the authenticated app, where the owner sees the order context and consciously chooses the next valid status. This preserves accountability and auditability.

## Privacy and security decisions

- Notification text contains no customer name, garment, due date, amount, payment method or balance.
- The detailed order remains behind the existing app session and backend authorization.
- Reminders are local to a specific phone; no Expo token, Apple push token, Firebase token or customer data is stored by this increment.
- Local reminders depend on the operating system, user-granted permissions, notification focus/silent modes, battery policies and a correctly configured device clock. They are helpful prompts, not a delivery guarantee.
- Reminder scheduling fails safely with an explanatory in-app message if permission is denied, a browser is used, an order is closed, or the requested reminder time is already past.

## Expo Go development constraint

The current user-selected testing route is Expo Go on Android and iPhone. Expo documents that remote push notifications are unavailable in Expo Go from SDK 53 onward, while local notifications remain available. This increment therefore uses local scheduled notifications only. It is suitable for device-level development testing, not a substitute for a production notification service.

Sources:

- Expo Notifications API: https://docs.expo.dev/versions/latest/sdk/notifications/
- Expo, remote and local notifications overview: https://docs.expo.dev/push-notifications/what-you-need-to-know/
- Expo development-build FAQ: https://docs.expo.dev/develop/development-builds/faq/

## Requirements and acceptance checks

| ID | Requirement | Acceptance check | Current evidence/boundary |
|---|---|---|---|
| REM-01 | Owner can opt in or out of one generic daily 08:00 local workflow reminder on a native device. | Turn on in Studio, grant permission, inspect scheduled OS notification; turn off and confirm it no longer appears in the schedule. | Implemented in shared mobile source; physical Android/iPhone notification delivery still requires manual verification. |
| REM-02 | Owner can schedule a day-before or due-day reminder for an active order. | Set a future test order, choose a reminder, inspect OS schedule or wait for delivery, tap it, and verify that the matching order opens. | Implemented in shared mobile source; native manual test pending. |
| REM-03 | Lock-screen notification text must not disclose customer or financial data. | Inspect daily and order-reminder text on lock screen. | Implemented by fixed generic message content; device inspection pending. |
| REM-04 | Closed orders and past reminder times must not receive a new reminder. | Try scheduling against Collected/Cancelled or an already-passed time and observe an explanatory error. | Implemented logic; native manual test pending. |
| REM-05 | A notification tap must not silently alter a business status or payment. | Tap notification; app opens review context; status remains unchanged until owner confirms it in the app. | Implemented by design; native manual test pending. |
| REM-06 P1 | Production remote push service must provide durable device-token lifecycle, owner authorization, opt-out, token deletion, rate limits, delivery receipts, retry policy, monitoring and platform credentials. | Threat model, integration tests, Android/iOS development builds and operational review approved. | Not implemented; release-gated. |

## Production evolution, not implemented

A production remote-notification capability needs a separate design and data-protection review. Minimum components would include:

```text
Order deadline/status change
        ↓
Backend policy engine and idempotent notification job
        ↓
Per-user preferences, quiet hours, opt-out and rate limits
        ↓
Encrypted/controlled device-token registry
        ↓
FCM/APNs or approved notification provider
        ↓
Delivery ticket/receipt processing, invalid-token cleanup and monitoring
```

The backend must never treat an accepted push request as proof that the user saw the reminder. The system should distinguish **scheduled**, **submitted**, **provider accepted**, **provider failed**, and **user opened** where that event is available and permitted. A notification service is a reminder channel, not a reliable legal notice or a substitute for operational follow-up.
