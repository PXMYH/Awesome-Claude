---
id: static-analysis-sarif-parsing
slug: static-analysis-sarif-parsing
name: SARIF Parsing Best Practices
description: '- [OASIS SARIF 2.1.0 Specification](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)'
prompt_preview: "---\nname: sarif-parsing\ndescription: >-\n  Parses and processes\
  \ SARIF files from static analysis tools like CodeQL, Semgrep, or other\n  scanners.\
  \ Triggers on \"parse sarif\", \"read scan results\", \"aggregate findings\", \"\
  deduplicate\n  alerts\", or \"process sarif output\". Handles filtering, deduplication,\
  \ format conversion, and\n  CI/CD integration of SARIF data. Does NOT run scans\
  \ — use the Semgrep or CodeQL skills for that.\nallowed-tools:\n  - Bash\n  - Read\n\
  \  - Glob\n  - Grep\n---\n\n# SARIF Parsing Best P..."
full_prompt_length: 15153
tools_mentioned:
- go
- Node.js
- python
- Go
- JavaScript
- Python
category: security
category_display: Security
source_repo: trailofbits/skills
source_path: plugins/static-analysis/skills/sarif-parsing/SKILL.md
source_url: https://github.com/trailofbits/skills/blob/main/plugins/static-analysis/skills/sarif-parsing/SKILL.md
fetched_at: '2026-04-05T04:38:34.848115+00:00'
evaluation:
  model: xiaomi/mimo-v2-flash:free
  evaluated_at: '2026-04-05T08:17:02.718213Z'
  prompt_quality:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8707950 state=finished
      raised HTTPError>]'
  usefulness:
    score: 3.0
    reasoning: 'Evaluation error: RetryError[<Future at 0x7ffac8707950 state=finished
      raised HTTPError>]'
  overall_rating: 3.0
  summary: Evaluation failed
  tags_suggested: []
github_metrics:
  stars: 0
  forks: 0
  open_issues: 0
  last_commit: null
  fetched_at: '2026-04-05T08:30:00.350543Z'
indexed_at: '2026-04-05T08:30:00.350548Z'
---
