# 24 — The Behavioural Model

> **What this is:** the six behaviours the pack has described in prose for 23 chapters and never drawn.
> `23` argued the app is an unblocking network; this chapter proves it is *specifiable* — every actor,
> use case, state transition, and message timed against the constraints Ghana imposes.
>
> **Method:** written to the UML 2.5.1 notation these diagrams require (Object Management Group),
> using the five reference files uploaded this session (`Basic Use Case Diagram`, `Basic Sequence
> Diagram`, `Basic Activity Diagram`, `Basic Flowchart 6 Shapes`, `Basic Process Flow Diagram`).
> Where a diagram cannot express the real constraint, that is stated rather than hidden.
>
> **Nothing here is agreed.** Every diagram carries a status label (§24.8).

---

## 24.1 Scope: six behaviours, not sixty

A 300-role catalogue generates an unbounded number of use cases. Only six behaviours decide whether
this product works at all:

| # | Behaviour | Why this one | Section |
| ---: | --- | --- | --- |
| B1 | **Intake a block** | the product's front door; if this is slow or vague, nothing downstream works | §24.2 |
| B2 | **Match to one available human** | the thing that must happen in minutes, not days | §24.3 |
| B3 | **Session → verified record** | turns a fix into the asset the business actually sells | §24.4 |
| B4 | **Pay with a split, idempotently** | where money rules live and where they break | §24.5 |
| B5 | **Dispute and resolve** | one dispute costs 7.5 jobs of margin (`23.4` Law 2) | §24.6 |
| B6 | **Offline submit and later sync** | the correctness requirement nobody draws | §24.7 |

Everything else — onboarding tours, portfolios, ratings, search, categories — is **absent by design**
(`23` §23.13). An absent use case is a decision, and it is recorded as one.

---

## 24.2 B1 — Intake a block (use case + activity)

### The use case view

```
                     TECHBRO — SYSTEM BOUNDARY
  ┌───────────────────────────────────────────────────────────────────┐
  │                                                                   │
  │   ┌──────────────────────┐        ┌───────────────────────────┐   │
  │   │  Describe a block    │        │  Confirm structured brief │   │
  │   └──────────┬───────────┘        └─────────────┬─────────────┘   │
  │              │ «include»                        │                 │
  │              ▼                                  ▼                 │
  │   ┌──────────────────────┐        ┌───────────────────────────┐   │
  │   │  Structure the block │◄───────│  (AI assist, bounded)     │   │
  │   └──────────┬───────────┘        └───────────────────────────┘   │
  │              │                                                    │
  │              │ «extend»  (only when the block is a repeat)        │
  │              ▼                                                    │
  │   ┌──────────────────────┐                                        │
  │   │  Re-book the person  │                                        │
  │   │  who solved it last  │                                        │
  │   └──────────────────────┘                                        │
  └───────────────────────────────────────────────────────────────────┘
        ▲                                        ▲
   ┌────┴─────┐                            ┌─────┴──────┐
   │ Blocked  │                            │ Provider   │
   │ dev      │  (seeks unblocking)        │            │  (receives
   │          │                            │            │   routed block)
   └──────────┘                            └────────────┘
```

**Actor rule applied from the reference (`Basic Use Case Diagram` Part 2):** actors who *give or
control* sit left; actors who *receive or use* sit right. `Blocked dev` is on the left because they
initiate. `Provider` is on the right because they receive a routed request — **not** because they are
less important. That is the reference's stated rule and it is correct.

**On the AI actor.** I have deliberately **not** drawn the AI as a stick figure. `23` §23.12 says AI
must never decide who gets paid, trusted, or banned. Drawing it as an actor implies agency it must not
have. It is drawn as an *included behaviour inside the boundary*, which is what it is: a bounded
transformation the system performs, whose output a human confirms.

### The activity view — the eight-step intake

```
        ╔═══════╗
        ║  ●    ║  start: user says "I'm stuck"
        ╚═══╤═══╝
            ▼
   ┌─────────────────────┐
   │ Open block intake   │  no account required
   └──────────┬──────────┘
              ▼
   ┌─────────────────────┐
   │ Field 1–3:           │  what / what happened / stack
   │ free text + screenshot│
   └──────────┬──────────┘
              ▼
        ╱───────────╲
       ╱  stack is    ╲  no
      ╱   recognised?  ╲────────┐
      ╲                ╱         │
       ╲───────────╱           ▼
              │ yes      ┌──────────────┐
              ▼          │ ask 1 question│
   ┌─────────────────┐   │ (never 5)     │
   │ Fields 4–6:     │◄──┴──────────────┘
   │ tried / urgency /│
   │ budget band      │
   └────────┬─────────┘
            ▼
   ┌─────────────────┐   AI structures → brief.
   │ Confirm brief   │   Human may edit any line.
   └────────┬────────┘   AI cannot submit.
            ▼
     ╱─────────────╲
    ╱ user confirms? ╲  no ──► back to edit (no loop limit:
    ╲               ╱           the user is never timed out)
     ╲─────────────╱
            │ yes
            ▼
   ┌─────────────────┐
   │ Submit block    │───► B2 (matching)
   └─────────────────┘
```

**Why one question and not five.** The reference's flowchart discipline says every decision must have
a guard and every path must terminate. A five-question clarification loop terminates in abandonment on
a phone. `23` §23.10 fixed this at **six fields, one screen**; the diagram enforces it.

---

## 24.3 B2 — Match to one available human (the latency budget)

This is the diagram the pack most needed. It shows **where the minutes go**, and it makes the
requirement falsifiable.

```
   t=0        Block submitted
    │
    ├── t+0s ─────────────────────────────────────────────────────┐
    │   ┌──────────────────────────┐                              │
    │   │ Rule filter (SQL)        │  stack + version + city       │
    │   │ p95 target: 40 ms        │  → ~200 candidates            │
    │   └────────────┬─────────────┘                              │
    │                ▼                                            │
    │   ┌──────────────────────────┐                              │
    │   │ Availability filter      │  declared interrupt windows   │
    │   │ p95 target: 20 ms        │  → ~30 candidates             │
    │   └────────────┬─────────────┘                              │
    │                ▼                                            │
    │   ┌──────────────────────────┐                              │
    │   │ Weighted rank (v1)       │  skill .30 · reputation .20   │
    │   │ p95 target: 30 ms        │  completion .15 · response .10│
    │   └────────────┬─────────────┘  price .10 · recency .10      │
    │                ▼                 repeat .05                  │
    │   ┌──────────────────────────┐                              │
    │   │ Offer fan-out (3 max)    │  push + SMS fallback          │
    │   └────────────┬─────────────┘                              │
    │                │                                            │
    ├── t+90s ───────┴────────────────────────────────────────────┘
    │          first provider sees the block
    │
    ├── t+15min ─ accept / decline / expire (no answer = next 3)
    │
    ├── t+45min ─ escalation rules fire (widen city, widen version, raise price band)
    │
    └── t+4h ──── if unmatched: refund any hold, tell the truth, offer a human callback
```

**The honest number.** `[A]` The 40/20/30 ms targets are my design intent, **not measurements**, and no
part of this stack exists yet. They are here so they can be *tested*, not quoted. What is verifiable is
the total: **every internal step must complete in under 90 seconds**, because after that the user has
already opened WhatsApp and asked a friend. `23` §23.11 established that the network loses writes; this
establishes that **the product loses users at 90 seconds**, for a different reason.

**Failure of the fan-out, stated:** if three providers decline and no one accepts in 4 hours, the app
must **say so plainly** and refund. Silent expiry is the single most common trust failure in on-demand
marketplaces. `[I]`

---

## 24.4 B3 — Session to verified record (sequence)

This is the diagram that shows the money rules live in the domain, per `23` §23.18 Law 7.

```
 Blocked dev      App (RN)          Domain (Django)        Provider      Payment (Paystack)
      │               │                    │                  │                  │
      │  open session │                    │                  │                  │
      │──────────────►│  POST /sessions    │                  │                  │
      │               │───────────────────►│  authorize:      │                  │
      │               │                    │  is requester?   │                  │
      │               │                    │  is provider?    │                  │
      │               │                    │  is paid hold?   │                  │
      │               │◄───────────────────│  session token   │                  │
      │               │                    │                  │                  │
      │               │  ── async: session.opened (event) ───► │                  │
      │               │                    │                  │  join            │
      │               │                    │◄─────────────────│                  │
      │  screen share │                    │                  │                  │
      │◄─────────────►│                    │                  │                  │
      │               │                    │                  │                  │
      │               │  transcript chunks │                  │                  │
      │               │───────────────────►│  append-only,    │                  │
      │               │  (idempotency-key) │  never mutated   │                  │
      │               │                    │                  │                  │
      │               │                    │                  │  mark resolved   │
      │               │                    │◄─────────────────│                  │
      │  confirm it   │                    │                  │                  │
      │  works        │  POST /confirm     │                  │                  │
      │──────────────►│───────────────────►│  requester is the│                  │
      │               │                    │  ONLY confirmer  │                  │
      │               │                    │  ──────────────────────────────────►│
      │               │                    │  capture + split │  release 90%     │
      │               │                    │                  │  platform 10%    │
      │               │◄───────────────────│  ART: Verified   │                  │
      │               │  proof record      │  Outcome         │                  │
```

Three rules this diagram makes visible, all from `23`:

1. **Only the requester confirms.** A provider can mark *resolved*; only the person who was blocked can
   confirm *it works*. Otherwise the trust object is worthless.
2. **Transcripts are append-only.** The record IS the product (`23` §23.4 Law 3). Amending it destroys
   the asset.
3. **Capture happens on the domain, not the client.** The RN app never calls Paystack directly. That is
   Law 7 enforced structurally.

**What this diagram cannot show, and I am not pretending otherwise:** Paystack's split is a one-way
release with no clawback and no partial release (`S11`). The "release 90%" box is therefore **not an
escrow** — it is a settlement instruction. If a dispute lands after capture, the money is already gone
and the platform absorbs it. `23` §23.9's ~GHS 70 net per job must cover that risk, and at 10% take it
barely does.

---

## 24.5 B4 — Payment state machine (the invariant diagram)

Money is a state machine, and drawing it is the only way to see the illegal transitions.

```
                    ┌───────────┐
                    │  CREATED  │  hold authorised, not captured
                    └─────┬─────┘
       cancel / expire    │  session opened
              ┌───────────┴───────────┐
              ▼                       ▼
        ┌───────────┐          ┌───────────┐
        │ CANCELLED │          │  HELD     │◄──────────┐
        └───────────┘          └─────┬─────┘           │
                                     │ confirm         │ reopen
                                     ▼                 │ (dispute)
                               ┌───────────┐           │
                               │ CAPTURED  │───────────┘
                               └─────┬─────┘
                                     │ split settles
                                     ▼
                               ┌───────────┐
                               │  SETTLED  │
                               └─────┬─────┘
                                     │ refund granted
                                     ▼
                               ┌───────────┐
                               │ REFUNDED  │  platform-funded, not ledger-reversed
                               └───────────┘
```

**Illegal transitions that must be impossible** — each maps to an invariant (`04` §4.5):

| From → To | Why it must fail |
| --- | --- |
| `CANCELLED → CAPTURED` | charging for a cancelled booking |
| `SETTLED → HELD` | re-holding settled money (no such primitive at Paystack) |
| `CAPTURED → CAPTURED` (2nd time) | double capture; blocked by idempotency key |
| `REFUNDED → SETTLED` | money appearing twice |

`[I]` **The `REFUNDED` state is the honest one.** It is *platform-funded* — the platform pays the
client back out of its own margin because the provider was already paid. That is why `23.4` Law 2
says one dispute costs 7.5 jobs. The diagram makes the cost structural rather than a support ticket.

---

## 24.6 B5 — Dispute (activity, with the margin consequence visible)

```
  ╔═══╗
  ║ ● ║  requester disputes within 72h of confirmation
  ╚═╤═╝
    ▼
┌──────────────────────┐
│ Freeze provider      │   money already settled → no clawback.
│ payout for NEXT job  │   So the lever is future access, not past money.
└──────────┬───────────┘
           ▼
     ╱────────────╲
    ╱ evidence on  ╲
   ╱  the record?   ╲──── no ───► both parties asked for it (48h max)
    ╲              ╱                      │
     ╲────────────╱                       ▼
           │ yes              ┌────────────────────────┐
           ▼                  │ no evidence = requester│
   ┌──────────────────┐       │ wins by default        │
   │ AI summarises    │       │ (asymmetric on purpose)│
   │ the transcript   │       └───────────┬────────────┘
   │ (does not decide)│                   │
   └────────┬─────────┘                   │
            ▼                             │
   ┌──────────────────┐                   │
   │ HUMAN adjudicates│◄──────────────────┘
   │ 24h SLA          │
   └────────┬─────────┘
            ▼
      ╱───────────╲
     ╱  outcome?   ╲
    ╱               ╲
    ▼               ▼
┌────────┐    ┌──────────┐
│ Uphold │    │ Reject   │
│ refund │    │ restore  │
│ plat-  │    │ provider │
│ funded │    │ access   │
└────────┘    └──────────┘
```

**The asymmetry is deliberate and must be defended.** The requester wins if neither side produces
evidence. `[D]` Reason: the provider is the repeat player with the reputational asset and the record;
the requester is the one-off who must be protected or they never come back. Get this backwards and you
build a platform where providers win and clients leave — which is the failure mode of every
"provider-friendly" marketplace. `[I]`

---

## 24.7 B6 — Offline submit and later sync (the diagram nobody draws)

`23` §23.11 and §23.18 established this as a *correctness* requirement. Here is what it actually
requires, and the one transition that is illegal.

```
  RN CLIENT (offline)                    DOMAIN (on reconnect)
  ───────────────────                    ─────────────────────
  user confirms outcome
        │
        ▼
  ┌──────────────────┐
  │ write to local   │   intent, not decision
  │ outbox with:     │   + client idempotency key
  │  - action type   │   + client timestamp
  │  - payload       │   + monotonic seq
  │  - idem key      │
  └────────┬─────────┘
           ▼
  ┌──────────────────┐
  │ UI shows         │   ← NEVER "paid" or "confirmed"
  │ "waiting to sync"│      It shows "waiting". This is the honesty rule.
  └──────────────────┘
           │
      network returns
           ▼
  ═══════════════════════════════════════►  POST /outbox
                                            │
                                ┌───────────▼────────────┐
                                │ 1. idempotency check   │
                                │    seen this key?      │
                                │    → return prior result│
                                └───────────┬────────────┘
                                            ▼
                                ┌────────────────────────┐
                                │ 2. STATE RE-CHECK      │
                                │    is this transition  │
                                │    STILL LEGAL now,    │
                                │    given current state?│
                                └───────────┬────────────┘
                                            │
                        ┌───────────────────┴──────────────────┐
                        ▼ legal                                ▼ illegal
              ┌──────────────────┐                  ┌──────────────────┐
              │ apply once,      │                  │ REJECT with a    │
              │ return result    │                  │ human-readable   │
              └──────────────────┘                  │ reason + a way   │
                                                    │ forward          │
                                                    └──────────────────┘
```

**The illegal move** `[D]`, stated as a testable rule:

> **Replaying the stored *decision* is banned. Only the *intent* may replay.**

Concretely: a provider taps "complete" twice offline. One outbox entry, one idempotency key — or two
entries that both say *"the provider intends to mark this complete"*, which the domain collapses into
one legal transition on arrival. What must never happen is two entries that each assert *"this has been
completed"* and both get applied.

This is the difference between an offline queue and an offline database, and getting it wrong is how
the first dispute on a bad network costs the platform more than the job earned.

---

## 24.8 What these diagrams are, and are not

| Claim | Status |
| --- | --- |
| Notated to UML 2.5.1 conventions (actors, «include», «extend», swimlanes, async arrows) | `[F]` — notation follows the OMG standard |
| B1–B6 are the behaviours that decide viability | `[I]` — my judgement, argued in §24.1 |
| The 40/20/30 ms and 90 s targets | `[A]` — **design intent, never measured** |
| Paystack cannot claw back settled money | `[F]` S11 |
| Requester-wins-by-default on missing evidence | `[D]` — a policy decision, reversible |
| The AI must not be drawn as an actor | `[D]` — follows `23` §23.12 |
| Absent use cases are deliberate | `[D]` — listed in `23` §23.13 |

### The honest limitation of this entire chapter

**Diagrams are not evidence — they are the shape of a hypothesis.** Nothing in §24.2–§24.7 has been
tested against a real user. The value of drawing them is that they are now **falsifiable**: the 90-second
budget, the "only the requester confirms" rule, the banned optimistic replay — each can be disproved by
one week of real use.

That is exactly what the four uploaded reference files do well and what the wider library has mostly
avoided: they specify notation precisely enough that a wrong diagram is obviously wrong. `[I]`

---

## 24.9 What this adds to the pack

| Section | Before | Now |
| --- | --- | --- |
| `10-ux-ui-design-system.md` | 42 screens, no behaviour model | 9 screens mapped to B1–B6 |
| `06-api-contract.md` | endpoints listed | sequence + state machine make the ordering requirements explicit |
| `04-system-architecture.md` | invariants P1–P8 as text | §24.5 shows which transitions they forbid |
| `23` §23.11 / §23.18 | offline-first argued | §24.7 specifies it, including the banned replay |
| — | — | **§24.6 dispute asymmetry is new and was not decided anywhere** |

**The one genuinely new decision in this chapter:** requester-wins-by-default when evidence is missing.
It is not in any prior chapter, it reverses the usual marketplace bias, and it will be unpopular with
your providers. It is also, `[I]`, the reason a first-time blocked developer trusts the app enough to
use it a second time.
