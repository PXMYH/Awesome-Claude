---
id: static-analysis-semgrep
slug: static-analysis-semgrep
name: Semgrep Security Scan
description: '- [ ] Output directory resolved (user-specified or auto-incremented
  default)'
prompt_preview: "---\nname: semgrep\ndescription: >-\n  Run Semgrep static analysis\
  \ scan on a codebase using parallel subagents.\n  Supports two scan modes — \"run\
  \ all\" (full ruleset coverage) and \"important\n  only\" (high-confidence security\
  \ vulnerabilities). Automatically detects and\n  uses Semgrep Pro for cross-file\
  \ taint analysis when available. Use when asked\n  to scan code for vulnerabilities,\
  \ run a security audit with Semgrep, find\n  bugs, or perform static analysis. Spawns\
  \ parallel workers for multi-language..."
full_prompt_length: 9688
tools_mentioned:
- Python
- django
- Go
- Docker
- python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/static-analysis/skills/semgrep/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/semgrep/SKILL.md
fetched_at: '2026-06-28T06:19:47.618061+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-06-28T09:57:05.647388Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262ef30 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f13a262ef30 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-06-28T10:04:29.855097Z'
indexed_at: '2026-06-28T10:04:29.855103Z'
---
