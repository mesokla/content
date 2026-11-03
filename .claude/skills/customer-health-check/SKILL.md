---
name: customer-health-check
description: >
  Flag at-risk accounts in your customer base and explain why, sorted into
  Red/Yellow/Green with a concrete next action for each. Use when the user says
  "churn risk", "at-risk customers", "customer health", "which accounts might
  leave", "account review", or "find customers about to churn".
user-invokable: true
argument-hint: "[customer activity data]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: support
---

# Customer Health Check

Flag accounts that look at-risk and explain why.

## When to use
You want to catch churn before it happens — scan your customer base, sort accounts by risk, and get a specific action for each one that's slipping.

## What you'll need
A list of customers with recent activity (last order/login date, spend trend, support tickets, plan, etc.).

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are an account manager reviewing my customer base to catch churn before it happens.

Here is my customer data (one row per customer):
[paste a table or list — include for each: name, how long they've been a customer, last purchase or login date, spend this period vs. last period, number of open or recent support tickets, plan/tier, and anything else relevant]

Today's date is [date].

For each customer, assess churn risk and sort them into Red (likely to leave), Yellow (watch closely), and Green (healthy). For every Red and Yellow account, give me:
- The 1-2 specific signals that triggered the rating (e.g. "no login in 47 days; spend down 60%").
- A plain-English reason this matters.
- One concrete action I should take this week (e.g. "personal check-in call," "send a win-back offer").

Then list the top 5 accounts to contact first, highest risk and highest value at the top. Don't invent data — if a signal is missing for someone, say what you'd need to judge them.
```

**Tip:** Include both engagement (logins, usage) and money (spend trend) columns. A customer who's still paying but stopped logging in is often the most dangerous — quietly disengaged and one renewal away from leaving.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
