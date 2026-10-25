---
id: patching-bugs-validate-bug
slug: patching-bugs-validate-bug
name: Validate Bug
description: '| Shortcut | Required action |'
prompt_preview: '---

  name: validate-bug

  description: Use when a bug PoC package needs an independent rerun and judgment
  before patching.

  ---


  # Validate Bug


  ## When to Use


  Use after `reproduce-bug` has supplied a finding and PoC package. Read the

  [record contract](../../references/records.md).

  Before target commands, follow its [project guidance](../../references/records.md#project-guidance).


  ## When NOT to Use


  Do not use to repair a PoC, develop a patch, or infer reproduction from the

  reproducer''s narrative...'
full_prompt_length: 1934
tools_mentioned: []
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/patching-bugs/skills/validate-bug/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/patching-bugs/skills/validate-bug/SKILL.md
fetched_at: '2026-10-25T07:20:37.858274+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:43:20.799117Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e057cb0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8e057cb0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:08.970789Z'
indexed_at: '2026-10-25T12:12:08.970793Z'
---
