---
name: calendar-cleanup
description: >
  Decide what to keep, move, shorten, delegate, or decline on an overloaded week
  so your real priorities get done. Use when the user says "calendar cleanup",
  "too many meetings", "clean up my week", "what should I decline", "free up focus
  time", or "review my schedule".
user-invokable: true
argument-hint: "[this week's meetings + your priorities]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: scheduling
---

# Calendar Cleanup

Decide what to keep, move, or decline on a busy week.

## When to use
Your week is overloaded and you need a decisive call on each meeting plus the messages to make changes happen.

## What you'll need
This week's meeting list (titles, times, who's on each, and roughly why), your top priorities for the week, and any hard constraints you can't change.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are my chief of staff. My week is overloaded. Help me decide what to keep, move, shorten, delegate, or decline so I get my real priorities done.

This week's meetings:
[paste your meetings — for each: title, day/time, length, who's on it, and a one-line purpose]

My top priorities this week (what actually has to get done):
[list 2-4]
Hard constraints I can't change: [e.g. standing 1:1s, client calls, "no meetings before 9am"]

For each meeting, recommend ONE action — Keep / Shorten / Move / Delegate / Decline — with a one-line reason tied to my priorities. Be willing to push back: if a meeting doesn't move a priority forward, say so.

Then give me:
- The cleaned-up week as a simple day-by-day list of what remains
- How much focus time this frees up
- For each Move/Delegate/Decline, a short polite message I can send to make it happen

Be decisive. Don't hedge with "it depends" — make the call and tell me why.
```

**Tip:** Be honest about which meetings you secretly want to skip — flag them in the purpose line. Claude will give you the reasoning and the polite message to actually get out of them.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
