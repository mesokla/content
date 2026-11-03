---
name: support-reply-drafter
description: >
  Draft a reply to a customer support message in your brand voice — directly
  answering their question with one clear next step. Use when the user says
  "support reply", "answer a customer", "respond to a ticket", "help desk
  reply", "customer email", or "draft a support response".
user-invokable: true
argument-hint: "[customer message]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: support
---

# Support Reply Drafter

Answer a support question in your brand voice.

## When to use
A customer has written in with a question or problem and you need a reply that sounds like you, answers them directly, and gives one clear next step.

## What you'll need
The customer's message (and any relevant order/account details), plus a short note on what you can offer.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are a customer support agent for my business. Draft a reply to the message below.

Customer message:
[paste the customer's full message]

Context you can use:
- What I sell / the product involved: [e.g. monthly meal-kit subscription]
- Relevant account or order details: [e.g. order #1042, shipped 3 days ago, no tracking update]
- What I can offer: [e.g. reship at no cost, or a refund — not both]
- Brand voice: [e.g. warm, plain-spoken, no corporate jargon]

Write the reply so it:
1. Opens by acknowledging their specific situation (not a generic greeting).
2. Directly answers their question or states what I'll do next.
3. Gives one clear next step and, if relevant, a timeframe.
4. Stays under 120 words.

If the message is missing something I need to actually resolve it, list those questions separately under "Need from customer" instead of guessing.
```

**Tip:** Paste your last 2-3 real replies above the prompt and add "match this tone" — Claude mirrors your actual voice far better than any adjective you could pick.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
