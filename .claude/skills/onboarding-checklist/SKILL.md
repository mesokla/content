---
name: onboarding-checklist
description: >
  Generate a complete new-client or new-hire onboarding sequence, phased and
  ready to run. Use when the user says "onboarding checklist", "onboard a client",
  "new hire onboarding", "client onboarding sequence", "ramp a new person", or
  "onboarding plan".
user-invokable: true
argument-hint: "[who you're onboarding + into what]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: scheduling
---

# Onboarding Checklist

Generate a new-client or new-hire onboarding sequence.

## When to use
You're bringing on a new client or new hire and want a phased, owner-assigned checklist that gets them set up to succeed.

## What you'll need
Who you're onboarding (new client or new hire), what they're onboarding into, what success looks like, the tools/accounts involved, and the onboarding window if you know them.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are an operations lead who designs onboarding processes. Build a complete onboarding sequence for the person below.

Onboarding: [new client / new hire]
Role or engagement: [e.g. monthly bookkeeping client / junior account manager]
What success looks like by the end: [e.g. first deliverable shipped / fully productive on their own]
Tools/accounts they need access to: [list, or "you suggest"]
Steps I already know I want: [list, or "you suggest"]
Total onboarding window: [e.g. first 2 weeks]

Produce a checklist grouped by phase (Before day 1, Day 1, Week 1, Week 2+). For each item give:
- The task, written as a clear action
- Who owns it (me, them, or a teammate)
- When it's due
- Why it matters in one short line

Flag anything that's a blocker (must happen before later steps can start). End with a 3-question check-in I should ask at the end of the window to confirm they're set up to succeed. Keep tasks concrete and skippable-if-not-relevant — no vague "get familiar with the team" filler.
```

**Tip:** Tell Claude your actual tools (the CRM, the payment system, the shared drive) — generic onboarding lists are useless, and the specific access steps are exactly where people get stuck.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
