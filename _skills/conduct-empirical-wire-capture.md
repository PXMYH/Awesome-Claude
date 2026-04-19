---
id: conduct-empirical-wire-capture
slug: conduct-empirical-wire-capture
name: Conduct Empirical Wire Capture
description: '- `monitor-binary-version-baselines` — Phase 1 of the parent methodology;
  produces the version baseline this skill''s manifest references.'
prompt_preview: "---\nname: conduct-empirical-wire-capture\ndescription: >\n  Capture\
  \ outbound HTTP and telemetry from a CLI harness at runtime.\n  Covers capture-channel\
  \ selection (transcript file vs verbose-fetch\n  stderr vs outbound proxy vs on-disk\
  \ state), hook-driven per-event\n  capture vs long-running session capture, JSONL\
  \ output format for\n  diff-friendly artifacts, and the observability table that\
  \ maps each\n  target to the cheapest channel that captures it. Use when a static\n\
  \  finding needs runtime confirma..."
full_prompt_length: 16136
tools_mentioned:
- go
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/conduct-empirical-wire-capture/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/conduct-empirical-wire-capture/SKILL.md
fetched_at: '2026-04-19T04:51:21.702945+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-19T06:26:50.658781Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7cf2aae0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7d7cf2aae0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-19T07:27:51.273819Z'
indexed_at: '2026-04-19T07:27:51.273825Z'
---
