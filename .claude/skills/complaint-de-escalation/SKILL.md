---
name: complaint-de-escalation
description: >
  Write a calm, fair response to an unhappy customer that lowers the temperature
  without over-promising. Use when the user says "angry customer", "de-escalate
  a complaint", "upset customer", "handle a complaint", "calm down a customer",
  or "respond to a refund demand".
user-invokable: true
argument-hint: "[customer complaint]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: support
---

# Complaint De-Escalation

Write a calm, fair response to an unhappy customer.

## When to use
A customer is upset and you need a reply that validates their frustration, takes responsibility for your part, and states clearly what you will and won't do — firm but warm.

## What you'll need
The customer's angry message or thread, plus the facts of what actually happened.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
A customer is upset and I need a reply that lowers the temperature without giving away things I can't afford to.

The customer's message(s):
[paste the full message or email thread, most recent last]

What actually happened, from my side:
[the honest facts — what went right, what went wrong, what was outside my control]

What I'm willing to do: [e.g. partial refund, redo the work, expedited replacement]
What I cannot do: [e.g. full refund, same-day delivery]

Write a reply that:
1. Names their frustration and validates it in one genuine sentence — no "we apologize for any inconvenience."
2. Takes responsibility for our part plainly, and corrects any factual mistake in their account calmly and without defensiveness.
3. States exactly what I'll do and by when. If I'm declining something, say so clearly and explain why in one line.
4. Ends by handing them a clear choice or next step, so they're not stuck.

Stay firm but warm. Under 150 words. Flag separately if any part of their claim looks like it could become a legal or chargeback issue.
```

**Tip:** Fill in "What I cannot do" honestly before you generate. The fastest way to escalate a complaint is to over-promise in the heat of the moment and walk it back later.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
