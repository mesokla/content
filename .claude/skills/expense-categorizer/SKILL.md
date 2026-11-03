---
name: expense-categorizer
description: >
  Turn a bank or card statement into clean expense categories with a spend
  summary and a review list. Use when the user says "categorize expenses",
  "expense report", "bookkeeping", "sort my transactions", "categorize my
  statement", or "where is my money going".
user-invokable: true
argument-hint: "[statement rows]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: invoicing
---

# Expense Categorizer

Sort raw statement rows into clean categories, summarize spend, and flag anything that needs a human look.

## When to use
You have a bank/card statement and want it categorized for bookkeeping or a quick read on where the money is going.

## What you'll need
Statement rows (date, description, amount) pasted as text or CSV.

## Instructions
Run this prompt with the user's transactions:

```
You are my bookkeeper. Categorize the transactions below into clean expense categories.

Transactions:
[paste statement rows: date, description, amount]

Use these categories (pick the best fit, don't invent new ones unless nothing fits):
Software & subscriptions, Advertising & marketing, Contractors & freelancers,
Payroll, Rent & utilities, Travel, Meals & entertainment, Office supplies,
Bank & payment fees, Taxes, Owner draw / personal, Other.

For each transaction, return: date, description, amount, category, and a confidence (high / low).

Then give me:
1. A summary table of total spend per category, sorted highest to lowest.
2. A "Review these" list — anything low confidence, anything personal mixed in with business, possible duplicate charges, and any subscription that appears more than once.
3. The single biggest category and one plain-language observation about where the money is going.

Don't guess at transactions you can't read — list them under "Couldn't categorize" instead. No tax advice, just categorization.
```

**Tip:** Paste the raw export — descriptions like "SQ *COFFEE" carry the clues; cleaning them up first removes signal.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
