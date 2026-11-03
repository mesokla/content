---
name: quote-drafter
description: >
  Turn a few bullet points into a clean, client-ready quote or proposal with
  scope, itemized pricing, timeline, and next steps. Use when the user says
  "write a quote", "draft a proposal", "client quote", "pricing proposal", or
  "send a quote".
user-invokable: true
argument-hint: "[client + scope + pricing notes]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: invoicing
---

# Quote & Proposal Drafter

Turn rough notes into a professional, client-ready quote.

## When to use
A prospect needs pricing and you want a clean quote without writing it from scratch.

## What you'll need
A few bullets on the client, the work involved, your pricing, and the timeline.

## Instructions
Run this prompt with the user's notes:

```
You are my proposals writer. Turn the notes below into a clean, client-ready quote.

Notes:
- Client / company: [client name]
- What they need: [the work or problem in a few bullets]
- Scope / deliverables: [what I'll actually do]
- Pricing: [fixed price, hourly rate, or per-item — include the numbers]
- Timeline: [how long, or start/end dates]
- Anything to exclude: [out-of-scope items, if any]

Produce a quote with these sections:
1. A one-paragraph summary that shows I understood their problem.
2. Scope of work — deliverables as a clear bullet list.
3. Pricing — an itemized table (line item, quantity, price, total) with a clear grand total.
4. Timeline — when work starts and key dates.
5. What's not included — so there are no surprises later.
6. Next step — exactly what they do to accept.

Tone: confident and professional, not salesy. Use my real numbers — never invent prices or dates I didn't give you. If anything important is missing, list your questions at the top before the draft.
```

**Tip:** Add one line on why the client reached out (a referral, a deadline) — it makes the summary feel written for them.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
