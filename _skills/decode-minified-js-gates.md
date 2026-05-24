---
id: decode-minified-js-gates
slug: decode-minified-js-gates
name: Decode Minified JS Gates
description: '- `probe-feature-flag-state` — uses the gate-mechanics record to interpret
  runtime observations'
prompt_preview: "---\nname: decode-minified-js-gates\ndescription: >\n  Classify gate\
  \ call variants in a minified JavaScript bundle. Covers\n  context-window extraction\
  \ around a flag occurrence, identification of\n  4–6 reader variants (sync boolean,\
  \ sync config-object, bootstrap-aware\n  TTL, truthy-only, async bootstrap, async\
  \ bridge), default-value\n  extraction (boolean / null / numeric / config-object\
  \ literal),\n  conjunction detection across `&&` predicates, kill-switch inversion\n\
  \  detection, and production of a g..."
full_prompt_length: 14985
tools_mentioned:
- JavaScript
category: community
category_display: Community
source_repo: pjt222/agent-almanac
source_path: skills/decode-minified-js-gates/SKILL.md
source_url: https://github.com/pjt222/agent-almanac/blob/main/skills/decode-minified-js-gates/SKILL.md
fetched_at: '2026-05-24T06:01:16.120285+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-05-24T07:43:58.911302Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7319a1d6a0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f7319a1d6a0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-05-24T08:43:18.766604Z'
indexed_at: '2026-05-24T08:43:18.766610Z'
---
