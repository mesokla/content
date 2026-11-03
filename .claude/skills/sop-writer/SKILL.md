---
name: sop-writer
description: >
  Turn a process you describe into a clean, documented Standard Operating
  Procedure someone new could follow. Use when the user says "write an SOP",
  "document this process", "standard operating procedure", "turn this into a
  procedure", "process documentation", or "write up how I do this".
user-invokable: true
argument-hint: "[rough description of the process]"
license: MIT
metadata:
  author: Ootto
  version: "1.0.0"
  category: scheduling
---

# SOP Writer

Turn a process you describe into a documented standard procedure.

## When to use
You do something the same way each time and want it written up as an SOP someone new could follow without asking you questions.

## What you'll need
A rough description of the process — the steps as you currently do them, even if messy or out of order — plus who does it, how often, and the tools involved.

## Instructions
Collect any missing inputs from the user, then run this prompt:

```
You are a process documentation specialist. Turn my rough description into a clean Standard Operating Procedure (SOP) that someone new could follow without asking me questions.

The process:
[describe the process in your own words — list the steps as you do them, even if messy, partial, or out of order]

Who does this: [role/title]
How often: [e.g. weekly / per new order]
Tools involved: [list]

Produce an SOP with:
- Title and a one-line purpose (what this achieves and why)
- When to run it (the trigger)
- Prerequisites (access, tools, info needed before starting)
- Numbered steps, each a single clear action, in the correct order — split anything that combines two actions
- Decision points written as "If X, then Y" where the process can branch
- A "Done when" definition so the person knows they've finished correctly
- Common mistakes to avoid (only ones implied by my description — don't invent risks)

Where my description is ambiguous or has a gap, insert a clearly marked [NEEDS INPUT: question] instead of guessing. Plain language, no jargon.
```

**Tip:** Don't clean up your description first — dump the steps messily and let Claude order and structure them. The `[NEEDS INPUT]` flags will show you exactly which parts of your process you've never actually written down.

---

Built by **[Ootto](https://www.ootto.ai)** — the AI autopilot that connects your tools once and runs invoicing, follow-up, and reports for you, automatically. [Book a demo →](https://www.ootto.ai)
