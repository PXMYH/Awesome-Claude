---
id: trailmark-slicing-code-context
slug: trailmark-slicing-code-context
name: Slicing Code Context
description: '```json'
prompt_preview: '---

  name: slicing-code-context

  description: "Selects bounded, graph-informed source slices with Trailmark and delegates
  focused code analysis or patch-proposal work to a smaller subagent. Use when offloading
  function-, class-, caller-, callee-, call-path-, entrypoint-, or line-focused code
  tasks to constrained or locally hosted models without exposing the full repository."

  ---


  # Slicing Code Context


  Use the capable coordinator to choose relevant code. Give an external/local

  worker only the tas...'
full_prompt_length: 8558
tools_mentioned:
- Python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/trailmark/skills/slicing-code-context/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/trailmark/skills/slicing-code-context/SKILL.md
fetched_at: '2026-08-02T05:31:31.545156+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-08-02T09:21:16.114847Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0ac989880 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7fd0ac989880 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-08-02T09:26:17.198942Z'
indexed_at: '2026-08-02T09:26:17.198947Z'
---
