---
id: static-analysis-semgrep
slug: static-analysis-semgrep
name: Semgrep Security Scan
description: '- [ ] Output directory resolved (user-specified or auto-incremented
  default)'
prompt_preview: "---\nname: semgrep\ndescription: >-\n  Runs a Semgrep security scan\
  \ over a codebase: detects languages, selects\n  rulesets, presents the plan for\
  \ explicit approval, then runs every approved\n  ruleset through scripts/run-scans.sh,\
  \ which batches the semgrep processes and\n  writes scans.json, and merges the output\
  \ to SARIF. Supports two scan modes,\n  \"run all\" for full ruleset coverage and\
  \ \"important only\" for security\n  findings at medium-to-high confidence and impact.\
  \ Uses Semgrep Pro for\n  cross-fi..."
full_prompt_length: 14898
tools_mentioned:
- go
- django
- docker
- python
- javascript
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/static-analysis/skills/semgrep/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/semgrep/SKILL.md
fetched_at: '2026-10-25T07:20:41.366834+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-10-25T11:45:55.090202Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee6330 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7c3b8dee6330 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-10-25T12:12:09.015272Z'
indexed_at: '2026-10-25T12:12:09.015276Z'
---
