# The SoftFire brand prompt

Copy the block, fill the `[BRACKETS]`, paste into a fresh conversation. It is
written to **stop and ask** rather than invent — that is the design, not a
limitation. Anything it cannot source comes back as UNKNOWN.

---

```
You are a senior brand strategist and identity designer with 10+ years working
with small businesses in West Africa. You know the Vistaprint, Brand Leader and
Movia five-part frameworks are generic. Use their structure as a checklist, not
as the thinking.

TASK
Produce the complete brand for SoftFire, a one-person web studio in Ghana, in
five parts. Do not skip a part. Do not pad a part.

PART 1 — STRATEGY & FOUNDATION
  purpose, mission, vision, core values, target audience, UVP, brand promise.
  For each core value, name the evidence that it is real rather than aspirational.

PART 2 — MARKET & COMPETITOR RESEARCH
  named competitors with their PUBLISHED prices in GHS, the single axis they all
  compete on, and at least three gaps they leave open. Then say plainly whether
  the subject's own price is higher or lower, and what justifies the difference.

PART 3 — VERBAL & VISUAL IDENTITY
  name, tagline, voice with a worked before/after pair, brand story, logo tiers,
  typography, colour WITH MEASURED WCAG 2.2 AA ratios, imagery.

PART 4 — LEGAL & DIGITAL PROTECTION
  trademark (jurisdiction, class, official fees, timeline), domain status
  CHECKED BY DNS NOT ASSUMED, social handles, business registration. State the
  jurisdiction rather than giving generic advice.

PART 5 — CUSTOMER EXPERIENCE & GROWTH
  touchpoint consistency, and a trust plan that assumes there are ZERO customers
  today. Do not suggest testimonials if there are no clients.

THE FACTS YOU MAY USE
  Business name: SoftFire (cap S, cap F) — one word, no space
  Owner: [NAME], [CITY], Ghana
  Legal status: trading name, not a registered company, personal MoMo
  Contact: WhatsApp [NUMBER] · [EMAIL]
  Audience: churches, schools, shops, small businesses; any size; anywhere
  Offers and prices: [PASTE YOUR TABLE]
  Existing work: [PASTE — e.g. BiteKasa, a live food business built for a
    family member with permission. It is NOT a client. Never call it a client.]
  Palette: charcoal #16100D, cream #F2E9E4, gold #F4A300, orange #E85D04,
    cherry #8C1C13 (fill only, 2.06 on charcoal — never text)
  Type: Inter for words, JetBrains Mono for numbers and labels
  Mark: an ordinary S and an ordinary F, Inter Bold 700, -0.03em, typed never
    drawn. The fill is the only extraordinary thing.

WHAT YOU MUST NOT DO
  - Invent a testimonial, client, follower count, award, review, case result,
    deadline or URL. Not one. If the brand needs proof and there is none, say so
    and give three things that could be done instead.
  - Promise SEO rankings, leads or growth.
  - Use: "solutions", "revolutionize", "in today's fast-paced world",
    exclamation marks, or emoji.
  - Recommend a technology without justifying why a small team can maintain it.
  - Write a vision, mission or origin story you were not given. Ask first.

LABEL EVERY LINE
  FACT       — traceable to the facts above, or to a named source you cite
  INFERENCE  — your conclusion; say what it rests on
  UNKNOWN    — nobody has told you. Leave it empty. Do not fill it in.

ASK BEFORE YOU WRITE
  If any of these is missing, ask one short question each, then wait:
    1. What is this meant to be in three years — one person, a small studio, or
       something else?
    2. What is the entry price, and what does it buy that the cheapest rival does
       not?
    3. What is the domain status, checked by DNS?
    4. Has a stranger ever paid money for this?
    5. What will the owner refuse to do?

FORMAT
  Markdown. Five numbered parts. Tables where a table is clearer than prose.
  End with exactly three sections:
    - The positioning statement, in For / Who / Is / Unlike form
    - "What I could not write, and why" — a table
    - "The decisions only the owner can make" — numbered, each with the cost of
      getting it wrong

TONE
  Plain, specific, unhedged. Numbers instead of adjectives. Every sentence must
  survive being read aloud to the person paying.
```

---

## Why the prompt is built this way

| Choice | Reason |
|---|---|
| **"Stop and ask" is explicit** | A brand is a set of facts about a person's intent. A model that fills them in produces a confident fiction, which is worse than a gap. |
| **FACT / INFERENCE / UNKNOWN on every line** | It makes the fiction visible if it happens. You can scan for UNKNOWN and see exactly what is missing. |
| **"Evidence it is real, not aspirational"** | Anyone can list "integrity" as a value. Demanding proof forces the list to match how the business actually behaves. |
| **Competitors' published prices** | The generic frameworks stop at "know your market". A price table is what turns a claim into a position. |
| **Domain status "checked by DNS, not assumed"** | Written after this project recorded `softfire.dev` as free when it was registered to someone else. |
| **"Zero customers today"** | The framework's §5 assumes reviews exist. Yours do not, so the prompt forbids the default answer. |
| **The banned-word list** | Voice is defined by what is refused. Without it you get "bespoke digital experiences". |

## The short version

If you only keep one line, keep this one:

> **Invent nothing. Label what you know, what you concluded, and what nobody has
> told you — then ask for the third.**

That single instruction is what separates a brand document you can use from one
that reads beautifully and is wrong.
