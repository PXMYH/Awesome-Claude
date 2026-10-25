---
id: spec-to-code-compliance-spec-to-code-compliance
slug: spec-to-code-compliance-spec-to-code-compliance
name: Spec-to-Code Compliance
description: '- [ANALYSIS_FORMAT.md](resources/ANALYSIS_FORMAT.md) — the on-disk format
  for a per-requirement analysis. Read'
prompt_preview: '---

  name: spec-to-code-compliance

  description: Check code against the documentation that specifies it - which requirements
  hold, which the code contradicts, which are absent, and what the code does that
  no document mentions. Use when comparing an implementation against a whitepaper,
  protocol spec, or design document.

  allowed-tools: Workflow Task Read Grep Glob

  ---


  # Spec-to-Code Compliance


  Two artifacts disagree, and the job is to find where. The documentation says what
  the system does; the co...'
full_prompt_length: 7512
tools_mentioned:
- rest
- go
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md
fetched_at: '2026-10-25T07:20:40.944380+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:45:30.581049Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee54c0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee54c0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:09.007463Z'
indexed_at: '2026-10-25T12:12:09.007467Z'
---
