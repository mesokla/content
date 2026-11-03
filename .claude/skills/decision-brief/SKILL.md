---
name: decision-brief
description: >
  Turn a problem into clear options and a recommendation — a one-page brief you
  can forward to a co-founder or board member, with the trade-off that matters,
  a pick, and the first step. Use when the user says "decision brief", "help me
  decide", "weigh my options", "should I", "make a decision", or "pros and cons".
user-invokable: true
argument-hint: "[the decision you're facing]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: reporting
---

# Decision Brief

Turn a problem into clear options and a recommendation.

## When to use
You're facing a call — a hire, a tool, a pricing change, a direction — and you want it laid out as clear options with a straight recommendation, not a wall of pros and cons.

## What you'll need
The decision you're facing, any constraints (budget, timeline, team), and what you know about the options so far.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are a pragmatic advisor helping a business owner make a decision. Produce a one-page decision brief — clear enough to forward to a co-founder or board member.

The decision I'm facing:
[describe the decision or problem in your own words]

Constraints and context:
[budget, timeline, team size, anything that limits the choice — or write "none"]

What I know about the options so far:
[list the options you're considering and anything you already know about each]

Write the brief in this exact structure:
1. The decision — restate it in one sentence so we're aligned.
2. Options — for each realistic option (include any I missed), give a one-line description, the main upside, the main downside, and rough cost or effort.
3. The trade-off that matters most — the single factor this decision really hinges on.
4. Recommendation — pick one option, say why in 2 to 3 sentences, and name the first step to take this week.
5. What would change my mind — the one fact or result that should make us reconsider.

Rules: be direct and honest, not diplomatic — if an option is weak, say so and why. Don't invent facts or numbers I didn't give you; if a key fact is missing, list it as an open question instead of guessing. Keep it under 350 words.
```

**Tip:** If the recommendation feels too cautious, reply "now argue the opposite case as hard as you can" — pressure-testing the brief against itself surfaces risks you'd otherwise miss.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
