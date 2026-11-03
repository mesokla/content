---
name: cash-flow-snapshot
description: >
  Turn your open invoices, cash on hand, and upcoming bills into a plain-English
  cash-flow snapshot with collection priorities and a next move. Use when the
  user says "cash flow", "what am I owed", "collections priorities", "money in
  money out", or "cash flow snapshot".
user-invokable: true
argument-hint: "[open invoices + cash + bills]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: invoicing
---

# Cash-Flow Snapshot

Turn your numbers into what's owed, what's overdue, and the next move — in plain English.

## When to use
You want a fast, one-page read on cash flow: who owes you, what's overdue, and what to chase first.

## What you'll need
Open invoices (who, amount, due date, paid?), cash on hand, and known upcoming bills.

## Instructions
Run this prompt:

```
You are my finance assistant. Turn the numbers below into a plain-language cash-flow snapshot.

Money coming in — open invoices (who, amount, due date, paid yes/no):
[paste open invoices]

Cash on hand right now:
[amount]

Money going out — known bills and their due dates:
[paste upcoming bills / payroll / rent / subscriptions]

Produce:
1. Totals — total owed to me, how much is overdue (split: 1-30 days, 31-60, 60+), and total bills due in the next 30 days.
2. Net position — cash on hand plus expected payments, minus upcoming bills. Is there a shortfall, and roughly when does it hit?
3. Top 3 collections priorities — the specific invoices to chase first, biggest/most-overdue first, named with amounts.
4. The next move — one or two concrete actions for this week.

Use only the numbers I gave you — don't assume invoices will be paid on time unless I marked them paid. No forecasting beyond 30 days. Short and direct.
```

**Tip:** Mark which invoices are already paid (or leave them out) — mixing settled and outstanding invoices produces a wrong "what's owed" number.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
