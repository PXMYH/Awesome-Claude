---
id: trailmark-trailmark-summary
slug: trailmark-trailmark-summary
name: Trailmark Summary
description: Return the detected language list plus the full Trailmark summary output.
prompt_preview: '---

  name: trailmark-summary

  description: "Runs a Trailmark summary analysis on a codebase. Returns auto-detected
  languages, entry point count, and dependency list. Use when vivisect or galvanize
  needs a quick structural overview. Triggers: trailmark summary, code summary, structural
  overview."

  allowed-tools: Bash Read Grep Glob

  ---


  # Trailmark Summary


  Runs `trailmark analyze --language auto --summary` on a target directory.

  This is a v0.2-safe workflow; do not require Trailmark 0.4.0 just to p...'
full_prompt_length: 3701
tools_mentioned:
- python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/trailmark/skills/trailmark-summary/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/trailmark/skills/trailmark-summary/SKILL.md
fetched_at: '2026-10-25T07:20:44.612094+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:49:36.331088Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee7680 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee7680 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:09.083600Z'
indexed_at: '2026-10-25T12:12:09.083605Z'
---
