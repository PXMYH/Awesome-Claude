---
id: gha
slug: gha
name: Gha
description: Claude skill for Gha
prompt_preview: "---\nname: gha\ndescription: Analyze GitHub Actions failures and\
  \ identify root causes\nargument-hint: <url>\n---\n\nInvestigate this GitHub Actions\
  \ URL: $ARGUMENTS\n\nUse the gh CLI to analyze this workflow run. Your investigation\
  \ should:\n\n1. **Get basic info & identify actual failure**:\n   - What workflow/job\
  \ failed, when, and on which commit?\n   - CRITICAL: Read the full logs carefully\
  \ to find what SPECIFICALLY caused the exit code 1\n   - Distinguish between warnings/non-fatal\
  \ errors vs actual failure..."
full_prompt_length: 2556
tools_mentioned: []
category: community
category_display: Community
source_repo: ykdojo/claude-code-tips
source_path: skills/gha/SKILL.md
source_url: https://github.com/ykdojo/claude-code-tips/blob/main/skills/gha/SKILL.md
fetched_at: '2026-02-15T04:22:37.250522+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-02-15T04:33:24.979909Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f86c3a68d10 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f86c3a68d10 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-02-15T04:33:51.579945Z'
indexed_at: '2026-02-15T04:33:51.579951Z'
---
