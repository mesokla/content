---
name: payment-plan-drafter
description: >
  Propose a fair installment plan for a client who can't pay in full, plus the
  email to offer it. Use when the user says "payment plan", "installment plan",
  "client can't pay", "split the invoice", or "payment arrangement".
user-invokable: true
argument-hint: "[amount owed + client situation]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: invoicing
---

# Payment-Plan Drafter

Offer a struggling client a fair installment plan without losing the relationship.

## When to use
A client can't pay an invoice in full and you want to propose an installment plan and the email to send it.

## What you'll need
The amount owed, how overdue it is, what the client has told you, and the shortest terms you'd accept.

## Instructions
Run this prompt:

```
You are my accounts-receivable assistant. A client can't pay an invoice in full, so I want to offer an installment plan and the email to propose it.

Details:
- Client / contact name: [client name]
- Total amount owed: [amount]
- Invoice number(s): [invoice #s]
- How overdue: [days or weeks]
- What they've told me about their situation: [e.g. cash-flow gap, waiting on their own client]
- What I can accept: [shortest acceptable timeframe, whether a deposit is required, any minimum monthly amount]

Do two things:

1. Propose 2 plan options as a small table — for each: number of installments, amount per installment, dates, and the final pay-off date. Keep them realistic for what they've described. One faster, one more gradual.

2. Write a short, warm email that offers the plan. Acknowledge their situation without being preachy, state the total, present the two options clearly, and ask them to confirm which works. Keep the door open to talk if neither fits.

Use only the numbers I gave you. Don't promise to waive fees or interest unless I said I would. Plain, kind, businesslike — this is a client I want to keep.
```

**Tip:** Tell Claude the shortest timeframe you'd actually accept — without that boundary it offers a plan that's too generous.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
