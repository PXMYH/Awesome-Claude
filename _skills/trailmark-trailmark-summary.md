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


  ## When to Use


  - Vivisect Phase 0 needs a quick structural overview...'
full_prompt_length: 3054
tools_mentioned:
- python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/trailmark/skills/trailmark-summary/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/trailmark/skills/trailmark-summary/SKILL.md
fetched_at: '2026-05-17T05:49:40.279012+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-17T08:24:30.938372Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f48a8e1db80 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f48a8e1db80 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-17T08:28:06.434274Z'
indexed_at: '2026-05-17T08:28:06.434280Z'
---
