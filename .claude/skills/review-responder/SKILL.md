---
name: review-responder
description: >
  Write a public reply to a Google or Yelp review — positive or negative — that
  reads like a real person and doubles as marketing. Use when the user says
  "reply to a review", "respond to a Google review", "Yelp reply", "answer a bad
  review", "review response", or "respond to feedback".
user-invokable: true
argument-hint: "[review text and rating]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: support
---

# Review Responder

Reply to a Google or Yelp review, positive or negative.

## When to use
Someone left a public review and you need a reply that everyone reading can see — warm for a good one, accountable for a bad one, never a template.

## What you'll need
The review text, the star rating, and the reviewer's name (if shown).

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You write public replies to customer reviews for my business. These replies are seen by everyone, not just the reviewer, so they double as marketing.

The review:
- Reviewer name: [name, or "anonymous"]
- Rating: [e.g. 2 stars]
- Platform: [Google / Yelp / other]
- Review text: [paste the full review]

About my business: [one line — what you do and your style, e.g. "family-run pizzeria, friendly and direct"]

Write a reply that:
- Thanks them by name and references something specific they mentioned (not generic).
- For a negative review: acknowledges the issue without excuses, says what I'm doing about it, and invites them to contact me directly to make it right (give them this contact: [email or phone]). Never argue or blame the customer.
- For a positive review: is genuinely warm, reinforces what they liked, and gently invites them back — without sounding like a template.
- Stays under 75 words and sounds like a real person.

Give me two versions to choose from.
```

**Tip:** For negative reviews, never debate facts in public — move the details to a private channel. A calm, accountable reply impresses future customers more than "winning" the argument.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
