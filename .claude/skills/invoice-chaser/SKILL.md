---
name: invoice-chaser
description: >
  Draft the right payment reminder for an overdue invoice, with the tone matched
  to how late it is. Use when the user says "invoice reminder", "chase invoice",
  "overdue payment", "payment reminder", "unpaid invoice", or "follow up on a
  late payment".
user-invokable: true
argument-hint: "[invoice details]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: invoicing
---

# Invoice Chaser

Draft a payment reminder whose firmness matches how overdue the invoice is.

## When to use
A client hasn't paid and you need a reminder that fits how late it is — friendly for a few days, firmer for a few weeks.

## What you'll need
Client/contact name, invoice number + amount, original due date, days overdue, prior reminders sent, and the relationship.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are my accounts-receivable assistant. Write a payment reminder email for an overdue invoice.

Details:
- Client / contact name: [client name]
- Invoice number and amount: [invoice # and amount]
- Original due date: [due date]
- Days overdue: [number of days]
- Prior reminders sent: [none / one / two — and roughly when]
- Relationship: [new client / long-standing / large account]

Match the tone to how overdue it is:
- 1-14 days: warm, assume it slipped through. Friendly nudge.
- 15-30 days: polite but clearer. Ask for a specific pay-by date.
- 31-60 days: firm and direct. State the amount, the due date, and request payment this week.
- 60+ days: serious. Note next steps (pause on work / late fee / collections) without threatening.

Write a subject line and a short email (under 150 words). Plain language, no guilt-tripping, no jargon. Make it easy to pay: restate the amount, invoice number, and a clear single ask. End with one specific question that prompts a reply. Give me 2 subject line options.
```

**Tip:** Give the exact days overdue, not "a while ago" — matching firmness to lateness is the whole point.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
