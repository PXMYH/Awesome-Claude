---
id: semgrep-rule-variant-creator-semgrep-rule-variant-creator
slug: semgrep-rule-variant-creator-semgrep-rule-variant-creator
name: Semgrep Rule Variant Creator
description: '- For applicability analysis guidance, see [applicability-analysis.md]({baseDir}/references/applicability-analysis.md)'
prompt_preview: '---

  name: semgrep-rule-variant-creator

  description: Creates language variants of existing Semgrep rules. Use when porting
  a Semgrep rule to specified target languages. Takes an existing rule and target
  languages as input, produces independent rule+test directories for each language.

  allowed-tools: Bash Read Write Edit Glob Grep WebFetch

  ---


  # Semgrep Rule Variant Creator


  Port existing Semgrep rules to new target languages with proper applicability analysis
  and test-driven validation.


  ## When...'
full_prompt_length: 8001
tools_mentioned:
- java
- Java
- go
- Go
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md
fetched_at: '2026-06-28T06:19:46.457869+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T09:56:16.990476Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2801dc0 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a2801dc0 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:29.836598Z'
indexed_at: '2026-06-28T10:04:29.836604Z'
---
