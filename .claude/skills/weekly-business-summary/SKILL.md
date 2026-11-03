---
name: weekly-business-summary
description: >
  Turn this week's numbers into a plain-English read a busy owner can scan in 3
  minutes — headline, what went up and down vs last week, what needs attention,
  and what's quietly going well. Use when the user says "weekly summary",
  "weekly business report", "weekly recap", "how did the business do this week",
  "week in review", or "weekly numbers".
user-invokable: true
argument-hint: "[this week's numbers]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: reporting
---

# Weekly Business Summary

Turn your weekly numbers into a plain-English read.

## When to use
You've got this week's numbers and want a clear, scannable summary of what happened, what changed, and what needs your attention — without reading a dashboard.

## What you'll need
This week's key numbers (e.g. revenue, new customers, open invoices, expenses, support tickets) and last week's numbers for comparison if you have them.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are a sharp operations analyst writing a weekly business summary for a busy small-business owner who has 3 minutes to read it.

Here are this week's numbers:
[paste your numbers — e.g. revenue, new customers, cancellations, open/overdue invoices, cash in bank, expenses, support tickets]

Here are last week's numbers for comparison (skip if I didn't provide them):
[paste last week's numbers, or write "none"]

Write the summary in this exact structure:
1. The one-line headline — the single most important thing that happened this week.
2. What went up and what went down — each metric with the number, the change vs last week (absolute and %), and whether it's good or bad.
3. What needs my attention now — the 1 to 3 things at risk (e.g. overdue invoices, a dip, a spike in churn), each with a specific next action.
4. What's quietly going well — 1 to 2 positives worth noting.

Rules: use plain language, no jargon. Only use the numbers I gave you — never invent or estimate figures. If something looks off or a number is missing, say so. Keep the whole thing under 200 words.
```

**Tip:** Paste the same metrics in the same order every week. Claude's week-over-week comparison gets sharper and more consistent when the input format stays identical.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
