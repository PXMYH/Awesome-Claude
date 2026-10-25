---
id: code-improver-pr-improver
slug: code-improver-pr-improver
name: PR Improver
description: '- **One-time review**: run the PR-review skill directly; the loop''s
  value is iteration'
prompt_preview: '---

  name: pr-improver

  description: "Runs an autonomous review-and-fix improvement loop over the current
  branch''s changes until a PR review comes back clean, scoped mechanically to the
  directories the branch touched. Reviews are performed by an installed PR-review
  skill (default: pr-review-toolkit''s review-pr). Use to fix review findings on a
  branch before opening or updating a pull request (''clean up this branch'', ''fix
  this PR until review passes'', ''run review-and-fix on my changes''). NOT for a...'
full_prompt_length: 7530
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/code-improver/skills/pr-improver/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/code-improver/skills/pr-improver/SKILL.md
fetched_at: '2026-10-25T07:20:32.484715+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:40:14.759055Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e2d4740 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e2d4740 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.916328Z'
indexed_at: '2026-10-25T12:12:08.916332Z'
---
