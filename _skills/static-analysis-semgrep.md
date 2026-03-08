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
full_prompt_length: 9720
tools_mentioned:
- Python
- python
- Go
- django
- Docker
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/static-analysis/skills/semgrep/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/semgrep/SKILL.md
fetched_at: '2026-03-08T04:10:50.405829+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-03-08T05:37:19.325253Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f787fa42210 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7f787fa42210 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-03-08T05:42:15.327059Z'
indexed_at: '2026-03-08T05:42:15.327064Z'
---
