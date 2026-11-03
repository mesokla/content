# Skill sources

- `ig-viral` (+ `ig-reel`, whose `hooks.json`/`hookscore.py` it uses) — https://github.com/Jakeschincariol/instagram-agent-skill (MIT)
- Ootto-AI (MIT) — https://github.com/Ootto-AI
  - claude-content-skills, claude-lead-skills, claude-inbox-skills, claude-support-skills,
    claude-scheduling-skills, claude-reporting-skills, claude-invoice-skills → `skills/*`
  - claude-virality-skill → `virality` (identical to the copy in claude-content-skills)
  - claude-story-audit → `story-audit`
  - ootto-watch → `watch-video` (needs yt-dlp + ffmpeg; optional faster-whisper)
  - claude-instagram-autopilot, claude-figma-stack, claude-agent-blueprint contain no SKILL.md;
    copied as-is to `vendor/ootto-ai/` (their GitHub workflows are NOT active there).

Removed after security review: `agent-reach` (over-broad "MUST USE" trigger; told Claude to run
unpinned remote install instructions from github.com/Panniantong/Agent-Reach) and `humanizer`
(duplicates the built-in anthropic-skills:humanizer).
