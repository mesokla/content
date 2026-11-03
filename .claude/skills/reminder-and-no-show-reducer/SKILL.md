---
name: reminder-and-no-show-reducer
description: >
  Write confirmation and reminder messages that cut no-shows for an upcoming
  appointment. Use when the user says "appointment reminder", "reduce no-shows",
  "confirmation message", "remind a client", "booking confirmation", or "no-show
  follow-up".
user-invokable: true
argument-hint: "[appointment details + channel]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: scheduling
---

# Reminder & No-Show Reducer

Write a confirmation/reminder that reduces no-shows.

## When to use
You have a booked appointment and want messages that confirm it and remind the attendee so they actually show up.

## What you'll need
The meeting details (who, what, when, where/link), what they should bring or prepare, your business name and contact, and how you'll send the reminder (email, SMS, or both).

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are a customer-communications writer. Write reminder messages for an upcoming appointment, designed to reduce no-shows.

Appointment details:
- Attendee name: [name]
- What it's for: [e.g. discovery call / consultation / service appointment]
- Date and time (with time zone): [date, time, zone]
- Duration: [e.g. 45 min]
- Location or link: [address or video link]
- What they should bring or prepare: [or "nothing"]
- My business name and contact: [name + phone/email]

Channel: [email / SMS / both]
Tone: [friendly / professional / casual]

Produce:
1. A confirmation message to send right after booking.
2. A reminder for 24 hours before.
3. A short reminder for 1 hour before (SMS-length if SMS).

For each: restate the exact date, time, and time zone; make the location or link impossible to miss; give one clear way to reschedule or cancel; and add a single sentence on what they'll get out of showing up. No guilt-tripping, no walls of text.
```

**Tip:** The reschedule option is what actually cuts no-shows — people who can't make it often just ghost. Give them an easy out and they'll move the meeting instead of vanishing.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
