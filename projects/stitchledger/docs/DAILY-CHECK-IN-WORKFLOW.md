# Daily order check-in workflow — v0.2.3

## User need

A studio owner needs a daily prompt that answers one practical question:

> **Where is each active customer order now, and what is the next truthful action?**

A generic reminder alone is insufficient. The app must let the owner respond to the reminder, review one order at a time, and record a verified forward move in the order lifecycle.

## Designed behaviour

```text
08:00 local device reminder
        ↓
Owner taps notification
        ↓
Authenticated StitchLedger daily check-in opens
        ↓
One active order is shown, prioritising overdue and ready work
        ↓
Owner confirms actual next stage, keeps it unchanged, opens full order,
records/handles payment where required, or requests a tomorrow reminder
        ↓
Server validates the change and writes audit history
        ↓
Next active order appears
```

The **Today → Daily check-in** button exposes the same queue for testing or manual use without waiting for the next notification.

## State model and forward moves

| Current stage | Daily check-in forward action | Guard |
|---|---|---|
| Booked | Mark Cutting | Owner confirms cutting actually started. |
| Cutting | Mark Sewing | Owner confirms sewing actually started. |
| Sewing | Mark Ready | Owner confirms the garment is ready for collection. |
| Ready | Mark Collected | Only enabled after the recorded balance is zero. |
| Collected | No daily prompt | Closed order; remains visible in order history. |
| Cancelled | No daily prompt | Closed order; cancellation remains an exceptional, reviewed full-order action. |
| Overdue | Derived condition, not a replacement stage | An active order whose collection date is past is prioritised and labelled Overdue while retaining Booked/Cutting/Sewing/Ready. |

## Why it does not silently advance an order

A notification arriving does not prove that cutting, sewing, readiness or collection has happened. Therefore:

- tapping a notification **opens the review queue**, but changes nothing by itself;
- tapping **Mark Cutting/Sewing/Ready/Collected** in the authenticated app submits the real state change;
- existing backend state-transition, version and balance rules remain authoritative;
- a stale order changed on another device is rejected and must be refreshed;
- marking Collected with a remaining balance is blocked;
- cancellation remains protected by the existing zero-net-payment rule.

This preserves a trustworthy customer record and prevents accidental lock-screen interaction from falsifying operational or financial information.

## Reminder choices

The owner may choose **Remind me tomorrow** from the daily check-in. It schedules one local 08:00 reminder for that active order and replaces any prior scheduled per-order reminder on that device. The owner may instead choose **Keep current status for now**, which moves that order out of the current check-in session without changing the stored stage. The ordinary daily reminder will still bring active work back for review later.

## Privacy and presentation

Lock-screen notifications remain generic and do not include customer name, garment, due date, amount, balance or internal notes. The customer-specific information appears only after opening the authenticated app.

The queue uses text labels and status pills. Colour supports urgency but is never the only indicator. It follows the app’s explicit workflow model rather than trying to infer production status from time, AI, location or notification activity.

## Acceptance scenarios

1. **Booked order:** daily queue shows a booked fictional order; owner taps **Mark Cutting**; server records Booked → Cutting and activity history updates.
2. **Overdue sewing order:** queue prioritises an order with past due date and shows both Sewing and Overdue; owner marks it Ready or chooses a tomorrow reminder; the actual work stage remains truthful.
3. **Ready but unpaid:** queue shows a clear payment requirement; Collected action is unavailable until a genuine payment is recorded.
4. **Ready and paid:** owner taps Mark Collected; backend permits only the valid state transition and closes the order.
5. **Cancelled/collected history:** closed orders do not create daily noise but remain filterable in the Order Book.
6. **Another-device change:** owner responds using an outdated version; backend rejects the change, preventing an incorrect overwrite.
7. **Permission denied:** reminder scheduling explains the issue; the manual Today check-in remains usable.

## Verification boundary

TypeScript checks, Expo prebuild, and Android/iOS/web JavaScript exports have passed for the source. Physical Android and iPhone tests remain necessary for actual local-notification delivery, notification tap behaviour, and the daily-check-in flow in Expo Go. Remote production push notifications are not claimed; Expo Go is limited to local-notification testing.
