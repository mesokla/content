---
name: meeting-scheduler-reply
description: >
  Propose and confirm meeting times without the back-and-forth — read a request
  thread and draft a reply that locks in a time. Use when the user says "schedule
  a meeting", "propose times", "find a time to meet", "reply to schedule", "book a
  call", or "send my availability".
user-invokable: true
argument-hint: "[meeting thread + your availability]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: scheduling
---

# Meeting Scheduler Reply

Propose and confirm meeting times without the back-and-forth.

## When to use
Someone asked to meet and you need a reply that offers real times and locks in a slot in as few rounds as possible.

## What you'll need
The email or message thread requesting a meeting, plus your real availability (a few open slots and your time zone), the meeting length, and your preferred format.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are my scheduling assistant. Read the thread below and draft a reply that locks in a meeting in as few rounds as possible.

Thread:
[paste the email or message thread]

My availability (use exactly these, don't invent slots):
[paste 3-5 open windows with day, date, and start/end time]
My time zone: [your time zone]
Meeting length: [e.g. 30 min]
Preferred format: [video call / phone / in person at <location>]

Write a short, warm, professional reply that:
- Offers 3 specific time options (day, date, start time, AND time zone on each)
- States the meeting length and format, and includes the video link or asks them to share theirs
- Asks them to pick one or propose an alternative if none work
- Avoids filler and apologies; keep it to 5 sentences or fewer

Output only the reply, ready to send. Then below it, list the 3 slots as a plain bullet list I can double-check against my calendar.
```

**Tip:** Paste only slots you've already confirmed are free — Claude can't see your calendar, so any time it offers is only as good as the availability you give it.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
