# The Claude Agent Blueprint 🧭

**The business structure the creator of Claude Code says every company will run on — and how to build your own agent swarm.**

Boris Cherny (creator of Claude Code) shared that the businesses winning the next decade won't be organized by job titles. They collapse into **five archetypes** — workflows, not roles — staffed by **humans + hundreds-to-thousands of Claude agents**. This repo is the practical, copy-paste version.

> Source: Boris Cherny's public thread + talk on the five archetypes and "Claude everywhere." This is an independent, original breakdown — go watch/read the original for his exact words.

---

## The 5 archetypes

Every product moves through these five. One person can wear two or three. A solo founder wears all five (with agents doing the grunt work).

| # | Archetype | What it does |
|---|-----------|--------------|
| 1 | **Prototyper** | Fires out many ideas fast. Most never ship — that's the point. |
| 2 | **Builder** | Turns the one idea that lives into a real product in **minutes/hours**, not months. |
| 3 | **Sweeper** | Cleans the UI, simplifies the code, unships what isn't working, optimizes. |
| 4 | **Grower** | Iterates until it hits **product-market fit** (finds where retention drops and fixes it). |
| 5 | **Maintainer** | Keeps the mature system fast, secure and unbreakable as it scales. |

### Where to focus, by stage
- **Pre-PMF** (nobody's ripping it off the shelf yet): archetypes **1, 2, 3** — ideas, build, sweep.
- **Growing** (found PMF): **2, 3, 4, 5** — build, sweep, grow, maintain.
- **Strong PMF**: **3, 4, 5** — refine, grow, maintain.

---

## Carbon + silicon agents

The shift: your team isn't just humans ("carbon agents"). It's also **AI agents ("silicon agents")** doing most of the grunt work across all five archetypes.

Boris said he manages **hundreds to ~10,000 Claude agents at once**. The trick:

> **You're not prompting the Claudes. Your Claude is prompting the Claudes.**

- ~10–15 Claude Code sessions run at once, each owning one project/goal.
- Each session spins up **sub-agents** toward that goal — he calls these **"loops."**
- You provide the overarching goal; the orchestrating Claude decides which agents fire and when.

## The hidden 6th archetype: the Orchestrator

Someone has to decide *which* of the five to deploy, when, and how to transition as the product matures. Boris found a human central coordinator works *less* well as things speed up — so **Claude runs that too.** He calls the end state **"Claude everywhere"** (e.g. Claude tagged into Slack — proactive, multiplayer, shared memory).

---

## Build your own swarm

1. **One folder per project.** Open Claude Code in the project's root so it has full context.
2. **Write the goal, not the tasks.** Give the top-level Claude an overarching objective + a routine; let it spawn sub-agents to do the tiny tasks.
3. **Map every workstream to an archetype.** For each, a skill/prompt that captures how that archetype should behave (prototype → build → sweep → grow → maintain).
4. **Run several sessions in parallel** — one per goal — and let each orchestrate its own loop of sub-agents.
5. **Put Claude where you already work** (Slack/Telegram/your apps) so it's ambient, not another tab.

## Get the full stack
The content-growth version of exactly this (research → script → render → post → auto-DM) is open source:
**github.com/Ootto-AI/claude-content-skills**

---

*Built by [@jayantcreates.ai](https://instagram.com/jayantcreates.ai) — daily Claude builds. This is an original breakdown of publicly-shared ideas; all credit for the five-archetype framing to Boris Cherny.*

---

Built by **[Ootto](https://ootto.ai)** - the 24/7 AI operator for Instagram. It studies what is working in your niche, writes and renders the reels, posts them, and turns the comments into leads. [See it running](https://ootto.ai/content).
